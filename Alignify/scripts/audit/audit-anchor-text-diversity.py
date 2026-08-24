#!/usr/bin/env python3
"""
锚文本多样性审计脚本
========================
扫描所有 tools 页面，统计每个目标 slug 收到的锚文本变体数量。
研究显示 11+ 种不同锚文本变体与 13 倍 SEO 访问量相关。
（来源：§1.5.3 锚文本规范 · §1.5.5 已知局限）

输出：
  - 每个目标 slug 的锚文本变体数、来源页数
  - 变体 <3 的目标 slug（至少被 3 个源页引用）
  - 通用/禁止锚文本检测

用法：
  python3 audit-anchor-text-diversity.py              # EN+ZH 全量
  python3 audit-anchor-text-diversity.py --locale en  # 仅 EN
  python3 audit-anchor-text-diversity.py --slug geo   # 单目标页
"""

import json
import re
import os
import sys
import argparse
from collections import defaultdict
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 尝试找到 content/tools 目录
for candidate in [
    os.path.join(SCRIPT_DIR, "..", "..", "部署项目", "alignify-by-kostja", "content", "tools"),
    os.path.join(os.path.dirname(SCRIPT_DIR), "..", "部署项目", "alignify-by-kostja", "content", "tools"),
]:
    if os.path.exists(candidate):
        CONTENT_DIR = candidate
        break
else:
    CONTENT_DIR = ""

A_TAG_EN = re.compile(
    r"""<a\s+[^>]*href=(?:["']|\\["'])/tools/([\w-]+)(?:["']|\\["'])[^>]*>(.*?)</a>""",
    re.DOTALL
)
A_TAG_ZH = re.compile(
    r"""<a\s+[^>]*href=(?:["']|\\["'])/zh/tools/([\w-]+)(?:["']|\\["'])[^>]*>(.*?)</a>""",
    re.DOTALL
)

BANNED_ANCHORS = {
    "click here", "learn more", "read more", "more", "here", "link",
    "点击这里", "了解更多", "阅读更多", "更多", "点击", "这里",
    "details", "info", "this page", "本页", "详情",
}

def strip_html(text):
    return re.sub(r'<[^>]+>', '', text).strip()

def normalize_anchor(anchor):
    """Normalize anchor for comparison: lowercase, trim, collapse whitespace."""
    return ' '.join(anchor.lower().split())

def analyze_locale(locale, target_slug=None):
    """Analyze anchor text diversity for one locale."""
    locale_dir = os.path.join(CONTENT_DIR, locale)
    if not os.path.exists(locale_dir):
        print(f"ERROR: directory not found: {locale_dir}")
        return {}

    pattern = A_TAG_ZH if locale == "zh" else A_TAG_EN

    # target_slug -> {source_slug: [anchor_texts]}
    anchor_map = defaultdict(lambda: defaultdict(list))
    # source_slug -> [(target_slug, anchor_text, block_type)]
    source_links = defaultdict(list)

    for fname in sorted(os.listdir(locale_dir)):
        if not fname.endswith('.json'):
            continue
        source_slug = fname.replace('.json', '')
        filepath = os.path.join(locale_dir, fname)

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        blocks = data.get("blocks", [])
        for block in blocks:
            block_raw = json.dumps(block, ensure_ascii=False)
            btype = block.get("type", "section")
            for m in pattern.finditer(block_raw):
                tgt = m.group(1)
                if target_slug and tgt != target_slug:
                    continue
                anchor = strip_html(m.group(2).strip())
                norm = normalize_anchor(anchor)
                anchor_map[tgt][source_slug].append(anchor)
                source_links[source_slug].append((tgt, anchor, btype))

    # Compute diversity metrics
    results = {}
    for target, sources in anchor_map.items():
        all_anchors = set()
        for anchors in sources.values():
            all_anchors.update(normalize_anchor(a) for a in anchors)

        is_banned = any(normalize_anchor(a).strip() in BANNED_ANCHORS for a in all_anchors)

        results[target] = {
            "source_count": len(sources),
            "variant_count": len(all_anchors),
            "variants": sorted(all_anchors),
            "sources": dict(sources),
            "has_banned_anchor": is_banned,
        }

    return results


def print_report(results, locale):
    """格式化输出。"""
    print(f"\n{'='*80}")
    print(f"Anchor Text Diversity Report — {locale.upper()}")
    print(f"{'='*80}")

    # Sort by source_count descending
    sorted_targets = sorted(results.items(),
                            key=lambda x: (-x[1]["source_count"], x[0]))

    print(f"\n{'Target':<28} {'Sources':>7} {'Variants':>8} {'V/S':>5} {'Status'}")
    print(f"{'─'*60}")

    low_diversity = []
    banned = []

    for target, info in sorted_targets:
        sc = info["source_count"]
        vc = info["variant_count"]
        vs_ratio = f"{vc/sc:.1f}" if sc > 0 else "-"

        status = ""
        if sc >= 3 and vc < 3:
            status = "⚠️ LOW"
            low_diversity.append(target)
        elif info["has_banned_anchor"]:
            status = "🔴 BANNED"
            banned.append(target)
        elif vc >= 11:
            status = "✅ RICH"
        elif vc >= 5:
            status = "✅ OK"
        elif sc == 0:
            status = "⚫ NONE"

        print(f"{target:<28} {sc:>7} {vc:>8} {vs_ratio:>5} {status}")

    # Summary
    print(f"\n{'─'*60}")
    print(f"Total target slugs: {len(results)}")
    print(f"Low diversity (<3 variants, ≥3 sources): {len(low_diversity)}")
    if low_diversity:
        print(f"  {', '.join(low_diversity[:20])}")
    print(f"Banned anchors detected: {len(banned)}")
    if banned:
        print(f"  {', '.join(banned[:20])}")

    # Show details for low diversity
    if low_diversity:
        print(f"\n{'─'*60}")
        print("LOW DIVERSITY DETAILS:")
        for target in low_diversity:
            info = results[target]
            print(f"\n  {target} ({info['variant_count']} variants across {info['source_count']} sources):")
            for source, anchors in sorted(info["sources"].items()):
                print(f"    ← {source}: {', '.join(anchors)}")

    # Banned anchor detail
    if banned:
        print(f"\n{'─'*60}")
        print("BANNED ANCHOR DETAILS:")
        for target in banned:
            info = results[target]
            for source, anchors in info["sources"].items():
                for a in anchors:
                    if normalize_anchor(a).strip() in BANNED_ANCHORS:
                        print(f"  {source} → {target}: '{a}'")


def main():
    parser = argparse.ArgumentParser(description="锚文本多样性审计")
    parser.add_argument("--locale", default="both", choices=["en", "zh", "both"])
    parser.add_argument("--slug", type=str, help="仅分析特定目标 slug")
    args = parser.parse_args()

    locales = ["en", "zh"] if args.locale == "both" else [args.locale]

    for locale in locales:
        results = analyze_locale(locale, args.slug)
        print_report(results, locale)

    # Cross-locale comparison
    if args.locale == "both" and not args.slug:
        en_results = analyze_locale("en")
        zh_results = analyze_locale("zh")

        # Find targets present in EN but not ZH (and vice versa)
        en_only = set(en_results.keys()) - set(zh_results.keys())
        zh_only = set(zh_results.keys()) - set(en_results.keys())

        if en_only:
            print(f"\nTargets only in EN: {sorted(en_only)}")
        if zh_only:
            print(f"\nTargets only in ZH: {sorted(zh_only)}")


if __name__ == "__main__":
    main()
