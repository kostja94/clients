#!/usr/bin/env python3
"""Validate blog article frontmatter (F1-F8). Gate: Gate C / SEO dimension."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

DEFAULT_CATEGORIES = {"tutorial", "guide", "case study", "product", "glossary", "insights", "news"}


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
    parser = argparse.ArgumentParser(description="Frontmatter validator for blog articles (generic)")
    parser.add_argument("path", type=Path)
    parser.add_argument("--keyword", default="", help="Primary keyword for F1 check")
    parser.add_argument(
        "--categories",
        default="",
        help="Comma-separated allowed categories (default: tutorial,guide,case study,product,glossary,insights,news)",
    )
    parser.add_argument(
        "--require-secondary-category",
        action="store_true",
        help="Fail if secondary_category is missing",
    )
    args = parser.parse_args()

    allowed = (
        {c.strip().lower() for c in args.categories.split(",") if c.strip()}
        if args.categories
        else DEFAULT_CATEGORIES
    )

    text = args.path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(text)
    fails = 0
    gate = "GateC-SEO-F"

    if not fm:
        emit("FAIL", gate, "Missing or invalid YAML frontmatter", 1)
        return 1

    title = str(fm.get("title") or "")
    desc = str(fm.get("description") or "")
    slug = str(fm.get("slug") or "")
    category = str(fm.get("category") or "")
    secondary_category = str(fm.get("secondary_category") or "")
    author = str(fm.get("author") or "")

    if args.keyword and args.keyword.lower() not in title.lower():
        emit("FAIL", f"{gate}-F1", f"title missing primary keyword '{args.keyword}'")
        fails += 1
    else:
        emit("PASS", f"{gate}-F1", "title keyword check" + (" skipped (no --keyword)" if not args.keyword else ""))

    tlen = len(title)
    if tlen < 45 or tlen > 65:
        emit("FAIL", f"{gate}-F1", f"title length {tlen} not in 45-65 chars")
        fails += 1
    else:
        emit("PASS", f"{gate}-F1", f"title length {tlen} OK")

    dlen = len(desc)
    if dlen < 120 or dlen > 160:
        emit("FAIL", f"{gate}-F2", f"description length {dlen} not in 120-160 chars")
        fails += 1
    else:
        emit("PASS", f"{gate}-F2", f"description length {dlen} OK")

    if re.search(r"\b20\d{2}\b", slug):
        emit("FAIL", f"{gate}-F4", f"slug contains year: {slug}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F4", "slug evergreen OK")

    if category.lower() not in allowed:
        emit("FAIL", f"{gate}-F5", f"category not in allowed set {sorted(allowed)}: {category}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F5", f"category={category}")

    if args.require_secondary_category and not secondary_category:
        emit("FAIL", f"{gate}-F5", "secondary_category missing (--require-secondary-category)")
        fails += 1
    elif secondary_category:
        emit("PASS", f"{gate}-F5", f"secondary_category={secondary_category}")

    for banned in ("image", "keywords", "related"):
        if banned in fm:
            emit("FAIL", f"{gate}-F6", f"deprecated field '{banned}' present")
            fails += 1
        else:
            emit("PASS", f"{gate}-F6", f"no deprecated '{banned}' field")

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

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
