#!/usr/bin/env python3
"""
Tools 页面内链全面审计脚本
============================
对照 internal-links.md §1.5 底线规则，扫描 tools + Blog Tools 型 JSON（默认 both，~106 slug），
输出违规清单与分布摘要。

规则来源：internal-links.md §3.1.5
  R1: 每页 distinct 站内链接 ≥ 5 条
  R2: 单屏密度 ≤ 3 条（连续 400 英文词 / 250 中文字内不堆链）
  R3: 每页 tools↔tools 实际使用 ≤ 总配额的 70%（预留跨板块）
  R4: 同一目标页全文只出现一次
  R5: 锚文本覆盖目标页核心语义 + 自然融入上下文
  R6: 最小锚文本长度 ≥ 4 汉字 / ≥ 3 英文词
  R7: FAQ ≤3 distinct slug、与正文去重、单答 ≤2 链

用法：
  python3 audit-tools-internal-links.py                    # 全量审计
  python3 audit-tools-internal-links.py --slug avatar      # 单页审计
  python3 audit-tools-internal-links.py --violations-only  # 仅输出违规项
  python3 audit-tools-internal-links.py --json             # JSON 输出
"""

import json
import re
import os
import sys
import argparse
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

# ── 路径配置 ──────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from internal_links_lib import (
    find_deploy_root,
    extract_links_from_blocks,
    list_json_slugs,
    MIN_TOTAL_LINKS,
    DENSITY_WINDOW_EN,
    DENSITY_WINDOW_ZH,
    MAX_LINKS_PER_WINDOW,
    MIN_ANCHOR_LEN_ZH,
    MIN_ANCHOR_LEN_EN,
    BANNED_ANCHORS,
    count_chinese_chars,
    count_english_words,
    strip_html,
    get_block_text,
)

DEPLOY_ROOT = find_deploy_root()

QUOTA_TABLE = {
    (5, 9): {"tools_quota": "全部", "reserved": 0},
    (10, 15): {"tools_quota": "7-11", "reserved": "3-4"},
    (16, 20): {"tools_quota": "11-14", "reserved": "5-6"},
}


# ── 核心审计函数 ──────────────────────────────────────────

def audit_single_file(filepath, locale):
    """
    审计单个 JSON 文件，返回违规列表。
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    blocks = data.get("blocks", [])
    violations = []
    metrics = {}
    all_links = extract_links_from_blocks(blocks, locale)

    distinct_slugs = set(slug for slug, _, _, _, _ in all_links)
    total_distinct = len(distinct_slugs)

    # ── R1: 总链接数 ≥ 5 ──
    if total_distinct < MIN_TOTAL_LINKS:
        violations.append({
            "rule": "R1",
            "desc": f"distinct links {total_distinct} < minimum {MIN_TOTAL_LINKS}",
            "severity": "high",
        })

    # ── R2: 密度检查（按正文位置滑动窗口） ──
    plain_parts: list[str] = []
    link_positions: list[tuple[int, str]] = []
    for block in blocks:
        block_plain = get_block_text(block)
        block_start = sum(len(p) + 1 for p in plain_parts)
        search_from = 0
        for slug, anchor, _, _, _ in extract_links_from_blocks([block], locale):
            idx = block_plain.find(anchor, search_from)
            if idx < 0:
                idx = search_from
            link_positions.append((block_start + idx, slug))
            search_from = idx + max(len(anchor), 1)
        plain_parts.append(block_plain)

    full_text = " ".join(plain_parts)
    is_zh = locale == "zh"
    window_size = DENSITY_WINDOW_ZH if is_zh else DENSITY_WINDOW_EN

    def distance_units(start: int, end: int) -> int:
        segment = full_text[start:end]
        if is_zh:
            return count_chinese_chars(segment) + count_english_words(segment)
        return count_english_words(segment)

    dense_regions = []
    for i in range(len(link_positions)):
        pos_i, _ = link_positions[i]
        links_in_window = 1
        slugs_in_window = [link_positions[i][1]]
        for j in range(i + 1, len(link_positions)):
            pos_j, slug_j = link_positions[j]
            if distance_units(pos_i, pos_j) <= window_size:
                links_in_window += 1
                slugs_in_window.append(slug_j)
            else:
                break
        if links_in_window > MAX_LINKS_PER_WINDOW:
            dense_regions.append(
                {"position": pos_i, "count": links_in_window, "slugs": slugs_in_window[:6]}
            )

    R2_HUB_EXEMPT = frozenset(
        {"documentation", "agent-skills", "llm", "api", "search-engine", "web-scraping", "evaluation"}
    )
    source_slug = Path(filepath).stem
    if dense_regions and source_slug not in R2_HUB_EXEMPT:
        densest = max(dense_regions, key=lambda x: x["count"])
        violations.append({
            "rule": "R2",
            "desc": f"density violation: {densest['count']} links in ~{window_size} {'chars' if is_zh else 'words'} window (max {MAX_LINKS_PER_WINDOW})",
            "severity": "medium",
            "detail": densest,
        })

    # ── R3: 跨板块配额 ──
    # 确定该页属于哪个配额档
    quota_ok = True
    for (lo, hi), quota in QUOTA_TABLE.items():
        if lo <= total_distinct <= hi:
            if isinstance(quota["tools_quota"], str) and quota["tools_quota"] != "全部":
                # Parse "7-11" style
                q_lo, q_hi = map(int, quota["tools_quota"].split("-"))
                if total_distinct > q_hi:
                    quota_ok = False
                    violations.append({
                        "rule": "R3",
                        "desc": f"tools links {total_distinct} exceeds quota {quota['tools_quota']} for {lo}-{hi} range (reserved: {quota['reserved']} for cross-section)",
                        "severity": "low",
                    })
            break

    # ── R4: 重复 slug 检测 ──
    slug_counts = Counter(slug for slug, _, _, _, _ in all_links)
    duplicates = {s: c for s, c in slug_counts.items() if c > 1}
    if duplicates:
        violations.append({
            "rule": "R4",
            "desc": f"duplicate slugs found: {dict(duplicates)}",
            "severity": "high",
        })

    # ── R5: 锚文本语义检查（浅层） ──
    # 检查锚文本是否与目标页 slug 有明显语义关联
    for slug, anchor, _, _, _ in all_links:
        # Check if anchor is too generic relative to slug
        slug_words = set(re.findall(r'[a-z]+', slug.lower()))
        anchor_lower = anchor.lower()
        # If anchor has no overlap with slug words and is short, flag
        if len(anchor) < 20 and not any(w in anchor_lower for w in slug_words if len(w) > 2):
            # Only flag if anchor is very short
            if len(anchor) < 10:
                violations.append({
                    "rule": "R5",
                    "desc": f"weak anchor: '{anchor}' for target '{slug}' — little semantic overlap",
                    "severity": "low",
                })

    # ── R6: 锚文本长度 ──
    for slug, anchor, _, _, _ in all_links:
        ch_chars = count_chinese_chars(anchor)
        en_words = count_english_words(anchor)

        # Check against banned list
        if anchor.lower().strip() in BANNED_ANCHORS:
            violations.append({
                "rule": "R6",
                "desc": f"banned generic anchor: '{anchor}' for target '{slug}'",
                "severity": "high",
            })
        elif ch_chars > 0 and ch_chars < MIN_ANCHOR_LEN_ZH:
            violations.append({
                "rule": "R6",
                "desc": f"anchor too short (ZH): '{anchor}' ({ch_chars} chars, need ≥{MIN_ANCHOR_LEN_ZH}) for target '{slug}'",
                "severity": "medium",
            })
        elif en_words > 0 and ch_chars == 0:
            # EN-only anchor: need ≥1 word with ≥2 chars (allow GEO, API, Avatar, etc.)
            if en_words < MIN_ANCHOR_LEN_EN or len(anchor.strip()) < 2:
                violations.append({
                    "rule": "R6",
                    "desc": f"anchor too short (EN): '{anchor}' ({en_words} words, {len(anchor)} chars) for target '{slug}'",
                    "severity": "low",
                })

    # ── R7: FAQ 内链 ──
    faq_links = [(s, a) for s, a, _, bt, _ in all_links if bt == "faq"]
    faq_slugs = set(s for s, _ in faq_links)
    body_slugs = set(s for s, _, _, bt, _ in all_links if bt != "faq")
    faq_body_overlap = faq_slugs & body_slugs
    if faq_body_overlap:
        violations.append({
            "rule": "R7",
            "desc": f"FAQ slugs overlap body: {sorted(faq_body_overlap)}",
            "severity": "high",
        })
    if len(faq_slugs) > 3:
        violations.append({
            "rule": "R7",
            "desc": f"FAQ has {len(faq_slugs)} distinct slugs (max 3)",
            "severity": "high",
        })
    # Check per-FAQ-answer: ≤2 links
    for block in blocks:
        if block.get("type") == "faq":
            faq_items = block.get("items", block.get("questions", []))
            if isinstance(faq_items, list):
                for item in faq_items:
                    answer = ""
                    if isinstance(item, dict):
                        answer = item.get("answer", item.get("answerHtml", ""))
                    answer_links = extract_links_from_blocks([{'type':'faq','items':[{'answer': str(answer)}]}], locale)
                    if len(answer_links) > 2:
                        violations.append({
                            "rule": "R7",
                            "desc": f"FAQ answer has {len(answer_links)} links (max 2 per answer)",
                            "severity": "low",
                        })

    # ── 指标汇总 ──
    block_distribution = defaultdict(int)
    for _, _, _, btype, _ in all_links:
        block_distribution[btype] += 1

    howit_links = sum(1 for _, _, _, bt, _ in all_links if bt == "howItWorks")
    howit_pct = (howit_links / total_distinct * 100) if total_distinct > 0 else 0

    metrics = {
        "total_distinct": total_distinct,
        "total_raw_links": len(all_links),
        "block_distribution": dict(block_distribution),
        "howit_pct": round(howit_pct, 1),
        "char_count_zh": count_chinese_chars(' '.join(get_block_text(b) for b in blocks)),
        "word_count_en": count_english_words(' '.join(get_block_text(b) for b in blocks)),
        "duplicate_slugs": {s: c for s, c in slug_counts.items() if c > 1},
        "violation_count": len(violations),
    }

    return violations, metrics, all_links


def audit_all(locale="en", source="both", single_slug=None):
    """Audit tools and/or blog Tools JSON pages."""
    slug_routes = list_json_slugs(DEPLOY_ROOT, source)
    if single_slug:
        if single_slug not in slug_routes:
            print(f"ERROR: slug not found: {single_slug} (source={source})")
            return {}
        slug_routes = {single_slug: slug_routes[single_slug]}

    all_results = {}
    for slug, route in sorted(slug_routes.items()):
        filepath = DEPLOY_ROOT / "content" / route / locale / f"{slug}.json"
        if not filepath.is_file():
            continue
        violations, metrics, links = audit_single_file(str(filepath), locale)
        all_results[slug] = {
            "content_source": route,
            "route": route,
            "violations": violations,
            "metrics": metrics,
            "links": links,
        }
    return all_results


# ── 全局分析（跨页面） ──

def global_analysis(results_en, results_zh):
    """
    跨页面的全局分析：孤页、锚文本多样性、双向链接。
    """
    report = {}

    # ── 孤页检测 ──
    # 所有被引用的 slug
    all_targets_en = set()
    all_targets_zh = set()
    for slug, data in results_en.items():
        for link_slug, _, _, _, _ in data["links"]:
            all_targets_en.add(link_slug)
    for slug, data in results_zh.items():
        for link_slug, _, _, _, _ in data["links"]:
            all_targets_zh.add(link_slug)

    # 所有存在的 slug（源页）
    all_sources_en = set(results_en.keys())
    all_sources_zh = set(results_zh.keys())

    orphans_en = all_sources_en - all_targets_en
    orphans_zh = all_sources_zh - all_targets_zh

    report["orphans_en"] = sorted(orphans_en)
    report["orphans_zh"] = sorted(orphans_zh)

    # ── 锚文本多样性 ──
    # 对每个目标 slug，统计不同源页使用的锚文本变体数
    anchor_variants_en = defaultdict(lambda: defaultdict(set))  # target_slug -> source_slug -> {anchor_texts}
    anchor_variants_zh = defaultdict(lambda: defaultdict(set))

    for source_slug, data in results_en.items():
        for target_slug, anchor, _, _, _ in data["links"]:
            anchor_variants_en[target_slug][source_slug].add(anchor)

    for source_slug, data in results_zh.items():
        for target_slug, anchor, _, _, _ in data["links"]:
            anchor_variants_zh[target_slug][source_slug].add(anchor)

    # 统计每 target 的总变体数
    diversity_en = {}
    for target, sources in anchor_variants_en.items():
        all_anchors = set()
        for anchors in sources.values():
            all_anchors.update(anchors)
        diversity_en[target] = {
            "source_count": len(sources),
            "variant_count": len(all_anchors),
            "variants": sorted(all_anchors),
        }

    diversity_zh = {}
    for target, sources in anchor_variants_zh.items():
        all_anchors = set()
        for anchors in sources.values():
            all_anchors.update(anchors)
        diversity_zh[target] = {
            "source_count": len(sources),
            "variant_count": len(all_anchors),
            "variants": sorted(all_anchors),
        }

    # 标记变体 < 3 的目标 slug
    low_diversity_en = {t: d for t, d in diversity_en.items() if d["source_count"] >= 3 and d["variant_count"] < 3}
    low_diversity_zh = {t: d for t, d in diversity_zh.items() if d["source_count"] >= 3 and d["variant_count"] < 3}

    report["anchor_diversity_en"] = diversity_en
    report["anchor_diversity_zh"] = diversity_zh
    report["low_diversity_en"] = low_diversity_en
    report["low_diversity_zh"] = low_diversity_zh

    # ── 双向链接检查 ──
    # 对于 A→B 的链接，检查 B→A 是否存在
    missing_backlinks = []
    for source_slug, data in results_en.items():
        for target_slug, _, _, _, _ in data["links"]:
            if target_slug in results_en:
                target_links_out = set(s for s, _, _, _, _ in results_en[target_slug]["links"])
                if source_slug not in target_links_out:
                    # Check if it's a likely reciprocal relationship (both in same category)
                    missing_backlinks.append((source_slug, target_slug, "en"))

    for source_slug, data in results_zh.items():
        for target_slug, _, _, _, _ in data["links"]:
            if target_slug in results_zh:
                target_links_out = set(s for s, _, _, _, _ in results_zh[target_slug]["links"])
                if source_slug not in target_links_out:
                    missing_backlinks.append((source_slug, target_slug, "zh"))

    report["missing_backlinks"] = missing_backlinks
    report["missing_backlink_count"] = len(missing_backlinks)

    return report


# ── CLI 输出 ──

def print_report(all_results, locale, global_rpt=None, violations_only=False, json_out=False):
    """格式化输出审计结果。"""

    if json_out:
        output = {
            "audit_date": datetime.now().isoformat(),
            "locale": locale,
            "results": {},
        }
        for slug, data in all_results.items():
            output["results"][slug] = {
                "content_source": data.get("content_source"),
                "route": data.get("route"),
                "metrics": data["metrics"],
                "violations": data["violations"],
            }
        if global_rpt:
            output["global"] = {
                "orphans": global_rpt.get(f"orphans_{locale}", []),
                "low_diversity": global_rpt.get(f"low_diversity_{locale}", {}),
                "missing_backlinks": [b for b in global_rpt.get("missing_backlinks", []) if b[2] == locale],
            }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    total_pages = len(all_results)
    pages_with_violations = sum(1 for d in all_results.values() if d["violations"])
    total_violations = sum(len(d["violations"]) for d in all_results.values())

    print(f"\n{'='*80}")
    print(f"Tools/Blog Internal Links Audit — {locale.upper()} ({total_pages} pages)")
    print(f"{'='*80}")
    print(f"Pages with violations: {pages_with_violations}/{total_pages}")
    print(f"Total violations: {total_violations}")
    print()

    # ── Per-page detail ──
    for slug in sorted(all_results.keys()):
        data = all_results[slug]
        v = data["violations"]
        m = data["metrics"]

        if violations_only and not v:
            continue

        severity = "🔴" if any(x["severity"] == "high" for x in v) else \
                   "🟡" if any(x["severity"] == "medium" for x in v) else \
                   "🟢" if v else "✅"

        print(f"{severity} {slug:<30} links={m['total_distinct']:>3}  howit={m['howit_pct']:>5.0f}%  violations={len(v)}")

        if v:
            for vi in v:
                sev_mark = "🔴" if vi["severity"] == "high" else "🟡" if vi["severity"] == "medium" else "⚪"
                print(f"    {sev_mark} [{vi['rule']}] {vi['desc']}")

    # ── Distribution summary ──
    print(f"\n{'─'*80}")
    print("Distribution Summary:")
    print(f"{'Slug':<30} {'Total':>5} {'TLDR':>5} {'WhatIs':>6} {'HowIt':>5} {'UseCs':>5} {'HowCh':>5} {'CmpTbl':>6} {'FAQ':>4} {'SecOth':>6}")
    print(f"{'─'*80}")

    block_order = ["tldr", "section", "howItWorks", "useCases", "howToChoose",
                   "comparisonSection", "table", "faq", "bestTools", "html", "references"]

    for slug in sorted(all_results.keys()):
        m = all_results[slug]["metrics"]
        bd = m["block_distribution"]
        total = m["total_distinct"]

        tldr = bd.get("tldr", 0)
        section = bd.get("section", 0) + bd.get("html", 0)
        howit = bd.get("howItWorks", 0)
        usecs = bd.get("useCases", 0)
        howch = bd.get("howToChoose", 0)
        cmptbl = bd.get("comparisonSection", 0) + bd.get("table", 0)
        faq = bd.get("faq", 0)
        other = sum(c for t, c in bd.items() if t not in
                    {"tldr", "section", "html", "howItWorks", "useCases",
                     "howToChoose", "comparisonSection", "table", "faq"})

        print(f"{slug:<30} {total:>5} {tldr:>5} {section:>6} {howit:>5} {usecs:>5} {howch:>5} {cmptbl:>6} {faq:>4} {other:>6}")

    # ── Global analysis ──
    if global_rpt:
        print(f"\n{'='*80}")
        print(f"GLOBAL ANALYSIS — {locale.upper()}")
        print(f"{'='*80}")

        orphans = global_rpt.get(f"orphans_{locale}", [])
        if orphans:
            print(f"\n🔴 Orphan pages (zero inbound links): {len(orphans)}")
            for o in orphans:
                print(f"    - {o}")
        else:
            print(f"\n✅ No orphan pages found.")

        low_div = global_rpt.get(f"low_diversity_{locale}", {})
        if low_div:
            print(f"\n🟡 Low anchor text diversity (<3 variants, ≥3 sources): {len(low_div)}")
            for target, info in sorted(low_div.items()):
                print(f"    - {target}: {info['variant_count']} variants across {info['source_count']} sources")
        else:
            print(f"\n✅ Anchor text diversity OK.")

        missing_bl = [b for b in global_rpt.get("missing_backlinks", []) if b[2] == locale]
        if missing_bl:
            print(f"\n🟡 Missing potential backlinks: {len(missing_bl)} (showing first 20)")
            for src, tgt, loc in missing_bl[:20]:
                print(f"    - {src} → {tgt} (no reverse link)")

    print()


# ── Main ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Tools 页面内链审计")
    parser.add_argument("--slug", type=str, help="审计单个 slug")
    parser.add_argument("--locale", type=str, default="en", choices=["en", "zh", "both"],
                        help="语言版本 (default: en)")
    parser.add_argument("--violations-only", action="store_true", help="仅显示违规页")
    parser.add_argument("--json", action="store_true", help="JSON 输出")
    parser.add_argument("--source", type=str, default="both", choices=["tools", "blog", "both"], help="content source")
    parser.add_argument("--global-only", action="store_true", help="仅输出全局分析")
    args = parser.parse_args()

    locales = ["en", "zh"] if args.locale == "both" else [args.locale]

    for locale in locales:
        results = audit_all(locale, args.source, args.slug)

        # Global analysis
        if locale == "en":
            results_en = results
        else:
            results_zh = results

    # Run global analysis if processing both
    if args.locale == "both" and not args.slug:
        global_rpt = global_analysis(results_en, results_zh)
    elif not args.slug:
        # Single locale global analysis
        if args.locale == "en":
            global_rpt = global_analysis(results, {})
        else:
            global_rpt = global_analysis({}, results)
    else:
        global_rpt = None

    # Print report for each locale
    for locale in locales:
        results = results_en if locale == "en" else results_zh
        if args.global_only:
            print(f"\n{'='*60}")
            print(f"GLOBAL — {locale.upper()}")
            print(f"{'='*60}")
            if global_rpt:
                orphans = global_rpt.get(f"orphans_{locale}", [])
                print(f"Orphans: {orphans}")
                low_div = global_rpt.get(f"low_diversity_{locale}", {})
                print(f"Low diversity: {list(low_div.keys())}")
        else:
            print_report(results, locale, global_rpt, args.violations_only, args.json)


if __name__ == "__main__":
    main()
