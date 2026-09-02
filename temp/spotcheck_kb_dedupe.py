#!/usr/bin/env python3
"""Supplemental spot-check beyond audit_kb_dedupe.py heuristics."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"e:\clients\Alignify\knowledge\tools")

FINDINGS = []


def add(sev, path, kind, detail):
    FINDINGS.append({"severity": sev, "path": path, "kind": kind, "detail": detail})


def extract_urls(text):
    return [u.rstrip(".,;)>") for u in re.findall(r"https?://[^\s\)\]|>\"']+", text)]


def norm(u):
    u = u.rstrip("/").lower()
    return re.sub(r"^https?://(www\.)?", "", u)


def split_at_h2(text, header_prefix):
    m = re.search(rf"^{re.escape(header_prefix)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


for fp in sorted(ROOT.rglob("*.md")):
    rel = fp.relative_to(ROOT).as_posix()
    text = fp.read_text(encoding="utf-8")

    # 1. duplicate H2 外链索引
    headers = re.findall(r"^## 外链索引[^\n]*", text, re.M)
    if len(headers) > 1:
        add("HIGH", rel, "dup_links_h2", headers)

    # 2. duplicate ### 对比与测评
    cmp_headers = re.findall(r"^### 对比与测评[^\n]*", text, re.M)
    if len(cmp_headers) > 1:
        add("MEDIUM", rel, "dup_compare_h3", cmp_headers)

    # 3. old section name
    if "## 延伸阅读与参考材料" in text:
        add("MEDIUM", rel, "old_ext_section", "仍含旧节名")

    # 4. product homepage dup: 外链索引 vs 延伸阅读 (exact normalized URL)
    links = split_at_h2(text, "## 外链索引")
    ext = split_at_h2(text, "## 延伸阅读")
    if links and ext:
        lu = {norm(u) for u in extract_urls(links)}
        eu = {norm(u) for u in extract_urls(ext)}
        dup = lu & eu
        # ignore common doc paths that are intentionally deep links on same domain
        product_dup = {d for d in dup if not any(x in d for x in ["/docs", "/blog", "arxiv", "datatracker", "rfc-editor", "cheatsheet", "developer.mozilla"])}
        if len(product_dup) >= 2:
            add("LOW", rel, "ext_product_url_dup", sorted(product_dup)[:5])

    # 5. empty 对比与测评 under 外链索引 when products listed
    if "### 对比与测评" not in text and "## 外链索引" in text and rel not in ("README.md", "_TEMPLATE.md"):
        if re.search(r"\| \*\*[^*]+\*\* \|", links):
            add("INFO", rel, "missing_compare", "有产品表但无对比与测评小节")

    # 6. 能力栈 bold products (>=3) when 外链索引 exists
    cap = split_at_h2(text, "## 能力栈")
    if cap and links:
        cap_products = re.findall(r"\*\*([^*\|\n]{3,40}?)\*\*", cap)
        link_products = re.findall(r"\| \*\*([^*]+)\*\*", links)
        link_set = {p.split("（")[0].split("(")[0].strip() for p in link_products}
        overlap = [p for p in cap_products if any(p.startswith(x) or x.startswith(p) for x in link_set)]
        if len(overlap) >= 4:
            add("LOW", rel, "capability_bold_products", overlap[:6])

print(f"Supplemental findings: {len(FINDINGS)}")
by_sev = defaultdict(list)
for f in FINDINGS:
    by_sev[f["severity"]].append(f)
for sev in ("HIGH", "MEDIUM", "LOW", "INFO"):
    items = by_sev.get(sev, [])
    if items:
        print(f"\n{sev}: {len(items)}")
        for f in items[:15]:
            print(f"  {f['path']}: [{f['kind']}] {f['detail']}")
        if len(items) > 15:
            print(f"  ... +{len(items)-15} more")
