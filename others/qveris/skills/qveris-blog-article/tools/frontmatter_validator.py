#!/usr/bin/env python3
"""Validate QVeris blog article frontmatter + body header. Gate: Gate C / SEO.

QVeris schema v1.2 (lean): frontmatter keeps slug/metaTitle/description/author/
publishedAt/updatedAt/readTime. title, excerpt, and tldr live in the body:
first `# H1` = title, first paragraph after H1 = excerpt, `## TL;DR` block
after excerpt = tldr bullets.

Removed fields are FORBIDDEN: title, excerpt, tldr, badge, breadcrumb,
authorInitials, heroImage, heroAlt, tocExtra, plus legacy date/isoDate/
category/keywords/related/disclosure.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

REQUIRED_FIELDS = [
    "slug",
    "metaTitle",
    "description",
    "author",
    "publishedAt",
    "updatedAt",
]
FORBIDDEN_FIELDS = {
    "title",
    "excerpt",
    "tldr",
    "badge",
    "breadcrumb",
    "authorInitials",
    "heroImage",
    "heroAlt",
    "tocExtra",
    "date",
    "isoDate",
    "category",
    "keywords",
    "related",
    "disclosure",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    body = parts[2]
    if yaml is None:
        fm: dict = {}
        for line in parts[1].strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
        return fm, body
    fm = yaml.safe_load(parts[1]) or {}
    return fm, body


def emit(status: str, gate: str, msg: str) -> None:
    print(f"{status} | {gate} | {msg}")


def extract_title(body: str) -> str:
    """First `# H1` line in the body = article title."""
    h1s = re.findall(r"^# (.+)$", body, re.M)
    return h1s[0].strip() if h1s else ""


def extract_excerpt(body: str) -> str:
    """First paragraph after the first H1 = excerpt."""
    m = re.search(r"^# .+\n\s*\n([^\n#][^\n]*)", body, re.M)
    return m.group(1).strip().strip("*").strip() if m else ""


def extract_tldr(body: str) -> list[tuple[str, str]]:
    """Parse `## TL;DR` block into (label, body) pairs.

    Expected bullet shape: `- **label** — body`
    """
    m = re.search(r"^##\s+TL;DR\s*\n+(.*?)(?=\n## |\Z)", body, re.M | re.S)
    if not m:
        return []
    block = m.group(1)
    items = re.findall(r"^\s*-\s*\*\*(.+?)\*\*\s*[—:]\s*(.+)$", block, re.M)
    return [(label.strip(), body_text.strip()) for label, body_text in items]


def main() -> int:
    parser = argparse.ArgumentParser(description="Frontmatter/body validator for QVeris blog articles")
    parser.add_argument("path", type=Path)
    parser.add_argument("--keyword", default="", help="Primary keyword for title check")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    fails = 0
    gate = "GateC-FM"

    if not fm:
        emit("FAIL", gate, "Missing or invalid YAML frontmatter")
        return 1

    for key in FORBIDDEN_FIELDS:
        if key in fm:
            emit("FAIL", f"{gate}-schema", f"forbidden frontmatter field present: {key}")
            fails += 1
    if not any(k in fm for k in FORBIDDEN_FIELDS):
        emit("PASS", f"{gate}-schema", "no forbidden fields (title/excerpt/tldr/badge/breadcrumb/authorInitials/heroImage/heroAlt/tocExtra/legacy)")

    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] in (None, ""):
            emit("FAIL", f"{gate}-required", f"missing required field: {field}")
            fails += 1
        else:
            emit("PASS", f"{gate}-required", f"{field} present")

    meta_title = str(fm.get("metaTitle") or "")
    desc = str(fm.get("description") or "")
    slug = str(fm.get("slug") or "")
    read_time = str(fm.get("readTime") or "")

    # title comes from the body H1
    title = extract_title(body)
    if not title:
        emit("FAIL", f"{gate}-B1", "no `# H1` title found in body")
        fails += 1
    else:
        emit("PASS", f"{gate}-B1", f"H1 title found: {title[:60]}...")
        if args.keyword and args.keyword.lower() not in title.lower():
            emit("FAIL", f"{gate}-B1", f"H1 title missing primary keyword '{args.keyword}'")
            fails += 1
        else:
            emit("PASS", f"{gate}-B1", "title keyword check" + (" skipped (no --keyword)" if not args.keyword else ""))
        tlen = len(title)
        if tlen < 45 or tlen > 90:
            emit("FAIL", f"{gate}-B1", f"H1 title length {tlen} not in 45-90 chars")
            fails += 1
        else:
            emit("PASS", f"{gate}-B1", f"H1 title length {tlen} OK")

    # excerpt comes from the first body paragraph after H1
    excerpt = extract_excerpt(body)
    if not excerpt:
        emit("FAIL", f"{gate}-B2", "no excerpt paragraph found after H1")
        fails += 1
    elif len(excerpt) < 40:
        emit("FAIL", f"{gate}-B2", f"excerpt too short ({len(excerpt)} chars < 40)")
        fails += 1
    else:
        emit("PASS", f"{gate}-B2", f"excerpt present ({len(excerpt)} chars)")

    # TL;DR comes from the `## TL;DR` body block
    tldr = extract_tldr(body)
    if len(tldr) < 3:
        emit("FAIL", f"{gate}-B3", f"body `## TL;DR` block must have >=3 '- **label** — body' bullets; got {len(tldr)}")
        fails += 1
    else:
        emit("PASS", f"{gate}-B3", f"body TL;DR block has {len(tldr)} bullets (>=3)")
        first_label, first_body = tldr[0]
        if len(first_body) >= 40:
            emit("PASS", f"{gate}-B3", f"TL;DR first bullet is BLUF (label='{first_label}', body {len(first_body)} chars)")
        else:
            emit("FAIL", f"{gate}-B3", f"TL;DR first bullet body too short ({len(first_body)} chars < 40)")
            fails += 1

    if "| QVeris" not in meta_title:
        emit("FAIL", f"{gate}-F2", f"metaTitle missing '| QVeris' suffix: {meta_title!r}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F2", "metaTitle brand suffix OK")

    dlen = len(desc)
    if dlen < 100 or dlen > 280:
        emit("FAIL", f"{gate}-F3", f"description length {dlen} not in 100-280 chars")
        fails += 1
    else:
        emit("PASS", f"{gate}-F3", f"description length {dlen} OK")

    if re.search(r"\b20\d{2}\b", slug):
        emit("FAIL", f"{gate}-F4", f"slug contains year: {slug}")
        fails += 1
    elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
        emit("FAIL", f"{gate}-F4", f"slug not kebab-case: {slug}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F4", f"slug={slug} OK")

    if read_time and not re.match(r"^\d+\s+min read$", read_time.strip()):
        emit("FAIL", f"{gate}-F5", f"readTime not 'N min read': {read_time!r}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F5", "readTime format OK" if read_time else "readTime empty (warn)")

    # Structure: penultimate H2 = Conclusion, last H2 = FAQ (ADVISORY).
    h2s = re.findall(r"^## (.+)$", body, re.M)
    if len(h2s) >= 2:
        last = h2s[-1].strip()
        prev = h2s[-2].strip()
        last_ok = last.lower() == "faq" or last.lower().startswith("faq")
        prev_ok = prev.lower() == "conclusion"
        if last_ok and prev_ok:
            emit("PASS", f"{gate}-structure", "Conclusion then FAQ")
        elif last_ok and not prev_ok:
            emit("WARN", f"{gate}-structure", f"FAQ present but preceding H2 is '{prev}' (recommend Conclusion)")
        else:
            emit("WARN", f"{gate}-structure", f"no Conclusion→FAQ tail (got last H2 '{last}'); optional")
    elif h2s:
        emit("WARN", f"{gate}-structure", f"only one H2 ('{h2s[-1].strip()}'); recommend adding Conclusion+FAQ for SEO")
    else:
        emit("PASS", f"{gate}-structure", "no H2 detected (skip)")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
