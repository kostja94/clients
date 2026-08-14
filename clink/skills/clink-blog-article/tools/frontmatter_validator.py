#!/usr/bin/env python3
"""Validate Clink blog article frontmatter. Gate: Gate C / SEO."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ALLOWED_CATEGORIES = {"Product", "Comparison", "Opinion", "Glossary"}
# Removed from schema (do not require): keywords, related, disclosure
FORBIDDEN_FM_KEYS = {"keywords", "related", "disclosure"}


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


def emit(status: str, gate: str, msg: str, line: int | None = None) -> None:
    suffix = f" [line {line}]" if line is not None else ""
    print(f"{status} | {gate} | {msg}{suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Frontmatter validator for Clink blog articles")
    parser.add_argument("path", type=Path)
    parser.add_argument("--keyword", default="", help="Primary keyword for title check")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    fails = 0
    gate = "GateC-SEO-F"

    if not fm:
        emit("FAIL", gate, "Missing or invalid YAML frontmatter", 1)
        return 1

    title = str(fm.get("title") or "")
    desc = str(fm.get("description") or "")
    slug = str(fm.get("slug") or "")
    category = str(fm.get("category") or "")
    image = str(fm.get("image") or "")
    author = str(fm.get("author") or "")
    date = str(fm.get("date") or "")

    for key in FORBIDDEN_FM_KEYS:
        if key in fm:
            emit("FAIL", f"{gate}-schema", f"deprecated frontmatter field present: {key}")
            fails += 1
    if not any(k in fm for k in FORBIDDEN_FM_KEYS):
        emit("PASS", f"{gate}-schema", "no keywords/related/disclosure fields")

    if args.keyword and args.keyword.lower() not in title.lower():
        emit("FAIL", f"{gate}-F1", f"title missing primary keyword '{args.keyword}'")
        fails += 1
    else:
        emit("PASS", f"{gate}-F1", "title keyword check" + (" skipped (no --keyword)" if not args.keyword else ""))

    tlen = len(title)
    if tlen < 45 or tlen > 90:
        emit("FAIL", f"{gate}-F1", f"title length {tlen} not in 45-90 chars")
        fails += 1
    elif tlen > 70:
        emit("PASS", f"{gate}-F1", f"title length {tlen} OK (over 70; prefer ≤70 for new posts)")
    else:
        emit("PASS", f"{gate}-F1", f"title length {tlen} OK")

    dlen = len(desc)
    if dlen < 100 or dlen > 280:
        emit("FAIL", f"{gate}-F2", f"description length {dlen} not in 100-280 chars")
        fails += 1
    elif dlen > 160:
        emit("PASS", f"{gate}-F2", f"description length {dlen} OK (over 160; prefer 120-160 for new posts)")
    else:
        emit("PASS", f"{gate}-F2", f"description length {dlen} OK")

    if re.search(r"\b20\d{2}\b", slug):
        emit("FAIL", f"{gate}-F4", f"slug contains year: {slug}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F4", "slug evergreen OK")

    if category not in ALLOWED_CATEGORIES:
        emit("FAIL", f"{gate}-F5", f"category must be one of {sorted(ALLOWED_CATEGORIES)}: {category!r}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F5", f"category={category}")

    if not image:
        emit("PASS", f"{gate}-F6", "image empty (optional; skip OG image)")
    elif not image.startswith("/blog/images/"):
        emit("FAIL", f"{gate}-F6", f"image path not /blog/images/{{slug}}.jpg: {image}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F6", "image path OK")

    if not author:
        emit("FAIL", f"{gate}-F7", "author missing")
        fails += 1
    else:
        emit("PASS", f"{gate}-F7", "author present")

    if not slug:
        emit("FAIL", f"{gate}-F8", "slug missing")
        fails += 1
    elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
        emit("FAIL", f"{gate}-F8", f"slug not kebab-case: {slug}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F8", f"slug={slug} OK")

    if date and not re.match(r"^['\"]?\d{4}-\d{2}-\d{2}['\"]?$", str(date).strip()):
        if not re.match(r"^\d{4}-\d{2}-\d{2}", str(date)):
            emit("FAIL", f"{gate}-date", f"date not ISO YYYY-MM-DD: {date!r}")
            fails += 1
        else:
            emit("PASS", f"{gate}-date", f"date={date}")
    else:
        emit("PASS", f"{gate}-date", f"date={date}" if date else "date empty (warn)")

    # Structure: penultimate H2 = Conclusion, last H2 = FAQ
    h2s = re.findall(r"^## (.+)$", body, re.M)
    if len(h2s) >= 2:
        last = h2s[-1].strip()
        prev = h2s[-2].strip()
        last_ok = last.lower() == "faq" or last.lower().startswith("faq")
        prev_ok = prev.lower() == "conclusion"
        if not last_ok:
            emit("FAIL", f"{gate}-structure", f"last H2 must be FAQ; got '{last}'")
            fails += 1
        elif not prev_ok:
            emit("FAIL", f"{gate}-structure", f"H2 before FAQ must be Conclusion; got '{prev}'")
            fails += 1
        else:
            emit("PASS", f"{gate}-structure", "Conclusion then FAQ")
    elif h2s:
        last = h2s[-1].strip()
        emit("FAIL", f"{gate}-structure", f"need Conclusion + FAQ; only found '{last}'")
        fails += 1
    else:
        emit("PASS", f"{gate}-structure", "no H2 detected (skip)")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
