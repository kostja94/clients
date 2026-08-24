#!/usr/bin/env python3
"""One-time upgrade of audit-tools-internal-links.py for blog + lib."""
from pathlib import Path
import re

p = Path(__file__).resolve().parent / "audit-tools-internal-links.py"
text = p.read_text(encoding="utf-8")

text = text.replace(
    "扫描全部 105 个 tools 页面",
    "扫描 tools + Blog Tools 型 JSON（默认 both，~106 slug）",
)
text = text.replace(
    "  R7: FAQ 内链 Tools JSON ≤ 3 条与正文去重",
    "  R7: FAQ ≤3 distinct slug、与正文去重、单答 ≤2 链",
)

old_path = '''# ── 路径配置 ──────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CONTENT_DIR = "/sessions/adoring-jolly-ramanujan/mnt/alignify-by-kostja/content/tools"
# Fallback for other environments
if not os.path.exists(CONTENT_DIR):
    CONTENT_DIR = os.path.join(PROJECT_ROOT, "..", "..", "部署项目", "alignify-by-kostja", "content", "tools")
if not os.path.exists(CONTENT_DIR):
    alt_path = os.path.join(os.path.dirname(SCRIPT_DIR), "..", "部署项目", "alignify-by-kostja", "content", "tools")
    if os.path.exists(alt_path):
        CONTENT_DIR = alt_path

DOCS_DIR = os.path.join(PROJECT_ROOT, "docs", "internal-links")'''

new_path = '''# ── 路径配置 ──────────────────────────────────────────────
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

DEPLOY_ROOT = find_deploy_root()'''

if old_path in text:
    text = text.replace(old_path, new_path)
else:
    raise SystemExit("path block not found")

text = re.sub(
    r"# ── 常量 ──.*?MIN_TOTAL_LINKS = 5.*?BANNED_ANCHORS = \{.*?\}\n\n",
    "",
    text,
    flags=re.DOTALL,
)

text = re.sub(
    r"# ── 工具函数 ──.*?# Pattern:.*?ALL_HREF = re.compile\([^)]+\)\n\n",
    "",
    text,
    flags=re.DOTALL,
)

text = text.replace(
    """    pattern = A_TAG_ZH if locale == "zh" else A_TAG_EN

    # ── 提取所有链接 ──
    all_links = []  # (slug, anchor_text, block_idx, block_type, href_full)

    for idx, block in enumerate(blocks):
        block_raw = json.dumps(block, ensure_ascii=False)
        btype = block.get("type", "section")
        for m in pattern.finditer(block_raw):
            slug = m.group(1)
            anchor_raw = m.group(2).strip()
            anchor_text = strip_html(anchor_raw)
            all_links.append((slug, anchor_text, idx, btype, m.group(0)[:120]))""",
    "    all_links = extract_links_from_blocks(blocks, locale)",
)

text = text.replace(
    """        for m in pattern.finditer(block_raw):
            slug = m.group(1)
            # Approximate position in the concatenated text
            link_positions.append((len(' '.join(full_text_parts)), slug))""",
    """        for slug, _, _, _, _ in extract_links_from_blocks([block], locale):
            link_positions.append((len(' '.join(full_text_parts)), slug))""",
)

text = text.replace(
    """    faq_body_overlap = faq_slugs & body_slugs
    # FAQ-body overlap no longer a violation per 2026-05-20 rule update
    # (FAQ links treated identically to body links; R4 handles dedup)
    if len(faq_slugs) > 3:
        violations.append({
            "rule": "R7",
            "desc": f"FAQ has {len(faq_slugs)} distinct slugs (max 3)",
            "severity": "medium",
        })""",
    """    faq_body_overlap = faq_slugs & body_slugs
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
        })""",
)

text = text.replace(
    "                    answer_links = pattern.findall(str(answer))",
    "                    answer_links = extract_links_from_blocks([{'type':'faq','items':[{'answer': str(answer)}]}], locale)",
)

old_audit_all = '''def audit_all(locale="en", violations_only=False, single_slug=None):
    """
    审计全部 tools 页面。
    """
    locale_dir = os.path.join(CONTENT_DIR, locale)
    if not os.path.exists(locale_dir):
        print(f"ERROR: directory not found: {locale_dir}")
        return

    all_results = {}

    files = os.listdir(locale_dir)
    if single_slug:
        files = [f"{single_slug}.json"]

    for fname in sorted(files):
        if not fname.endswith('.json'):
            continue
        slug = fname.replace('.json', '')
        filepath = os.path.join(locale_dir, fname)

        violations, metrics, links = audit_single_file(filepath, locale)
        all_results[slug] = {
            "violations": violations,
            "metrics": metrics,
            "links": links,
        }

    return all_results'''

new_audit_all = '''def audit_all(locale="en", source="both", single_slug=None):
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
    return all_results'''

text = text.replace(old_audit_all, new_audit_all)

if 'parser.add_argument("--source"' not in text:
    text = text.replace(
        '    parser.add_argument("--global-only", action="store_true", help="仅输出全局分析")',
        '    parser.add_argument("--source", type=str, default="both", choices=["tools", "blog", "both"], help="content source")\n    parser.add_argument("--global-only", action="store_true", help="仅输出全局分析")',
    )

text = text.replace(
    "        results = audit_all(locale, args.violations_only, args.slug)",
    "        results = audit_all(locale, args.source, args.slug)",
)

text = text.replace(
    """            output["results"][slug] = {
                "metrics": data["metrics"],
                "violations": data["violations"],
            }""",
    """            output["results"][slug] = {
                "content_source": data.get("content_source"),
                "route": data.get("route"),
                "metrics": data["metrics"],
                "violations": data["violations"],
            }""",
)

text = text.replace(
    '    print(f"Tools Internal Links Audit — {locale.upper()} ({total_pages} pages)")',
    '    print(f"Tools/Blog Internal Links Audit — {locale.upper()} ({total_pages} pages)")',
)

p.write_text(text, encoding="utf-8")
print("OK:", p)
