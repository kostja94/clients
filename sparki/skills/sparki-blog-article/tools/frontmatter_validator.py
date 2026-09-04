#!/usr/bin/env python3
"""Validate blog article frontmatter (F1-F8). Gate: Gate C / SEO dimension.

Sparki-specific:
- filename MUST equal frontmatter `slug` (validate:posts hard rule)
- description must be 80-320 chars (validate:posts), 120-160 recommended
- `cover` is the featured-image field (NOT `image`)
- author default "Sparki Team"; category must be in allowed enum (informational)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

# Informational category enum (see SKILL.md §1)
ALLOWED_CATEGORIES = {
    "Clone Edit Viral Videos",
    "Video Editing Features",
    "ai-video-editor",
    "AI Video Editing",
    "AI Tools",
    "Editor-in-browser",
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


def emit(status: str, gate: str, msg: str, line: int | None = None) -> None:
    suffix = f" [line {line}]" if line is not None else ""
    print(f"{status} | {gate} | {msg}{suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Frontmatter validator for Sparki blog articles")
    parser.add_argument("path", type=Path)
    parser.add_argument("--keyword", default="", help="Primary keyword for F1 check")
    args = parser.parse_args()

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
    author = str(fm.get("author") or "")

    # F1: title keyword + length
    if args.keyword and args.keyword.lower() not in title.lower():
        emit("FAIL", f"{gate}-F1", f"title missing primary keyword '{args.keyword}'")
        fails += 1
    else:
        emit("PASS", f"{gate}-F1", "title keyword check" + (" skipped (no --keyword)" if not args.keyword else ""))

    tlen = len(title)
    # Hard bounds aligned with existing corpus (35-90); SEO recommendation 45-65 is a WARN
    if tlen < 35 or tlen > 90:
        emit("FAIL", f"{gate}-F1", f"title length {tlen} outside hard bounds 35-90")
        fails += 1
    else:
        emit("PASS", f"{gate}-F1", f"title length {tlen} OK (35-90)")
        if tlen < 45 or tlen > 65:
            emit("WARN", f"{gate}-F1", f"title length {tlen} outside recommended 45-65")

    # F2: description length (validate:posts hard: 80-320; skill target 120-160)
    dlen = len(desc)
    if dlen < 80 or dlen > 320:
        emit("FAIL", f"{gate}-F2", f"description length {dlen} outside validate:posts range 80-320")
        fails += 1
    else:
        emit("PASS", f"{gate}-F2", f"description length {dlen} OK (80-320)")
        if dlen < 120 or dlen > 160:
            emit("WARN", f"{gate}-F2", f"description length {dlen} outside recommended 120-160")

    # F3: slug == filename (sparki hard rule)
    slug_from_file = args.path.stem
    if slug and slug != slug_from_file:
        emit("FAIL", f"{gate}-F3", f"slug '{slug}' != filename '{slug_from_file}' (validate:posts hard rule)")
        fails += 1
    else:
        emit("PASS", f"{gate}-F3", f"slug matches filename: {slug_from_file}")

    # F4: slug evergreen (no year)
    slug_has_year = bool(re.search(r"\b20\d{2}\b", slug))
    if slug_has_year:
        emit("FAIL", f"{gate}-F4", f"slug contains year: {slug}")
        fails += 1
    else:
        emit("PASS", f"{gate}-F4", "slug evergreen OK")

    # F5: category present + enum
    if not category:
        emit("FAIL", f"{gate}-F5", "category missing")
        fails += 1
    else:
        if category not in ALLOWED_CATEGORIES:
            emit("WARN", f"{gate}-F5", f"category '{category}' not in known enum {sorted(ALLOWED_CATEGORIES)}")
        else:
            emit("PASS", f"{gate}-F5", f"category={category}")

    # F6: featured image field — sparki uses `cover`; `image` is NOT the schema field
    if "image" in fm:
        emit("FAIL", f"{gate}-F6", "field 'image' not in sparki schema — use 'cover' (path/URL)")
        fails += 1
    else:
        emit("PASS", f"{gate}-F6", "no 'image' field (schema uses 'cover')")
    if "cover" in fm and fm.get("cover"):
        emit("PASS", f"{gate}-F6", f"cover present: {fm.get('cover')}")

    # F7: author
    if not author:
        emit("FAIL", f"{gate}-F7", "author missing (default 'Sparki Team')")
        fails += 1
    elif author != "Sparki Team":
        emit("WARN", f"{gate}-F7", f"author '{author}' != default 'Sparki Team'")
    else:
        emit("PASS", f"{gate}-F7", "author present")

    # F8: slug non-empty + kebab-case
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
