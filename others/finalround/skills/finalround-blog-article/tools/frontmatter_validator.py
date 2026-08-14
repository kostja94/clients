#!/usr/bin/env python3
"""FinalRound frontmatter validator.

Checks the YAML frontmatter of a FinalRound blog draft against the skill schema.
Since 2026-08-11, FinalRound frontmatter does NOT contain image/keywords/related.
Required: title, description, slug, date, author, category, tags, reading_time.
`date` = publication date. `updated` = last substantial update (optional, >= date).
`category` = Product | Comparison | Research. `tags` = 3-6 kebab-case items.
`reading_time` = positive integer minutes.
Filename convention: NN-{slug}-2026.md (or NN-{slug}.md).

Usage:
    python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "primary kw"
Exit code 0 = PASS, 1 = FAIL.
"""
import argparse
import re
import sys


def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    return m.group(1) if m else None


def parse_fields(fm: str) -> dict:
    """Parse scalar fields and multi-line YAML lists."""
    result = {}
    current_key = None
    for line in fm.splitlines():
        m = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            val = re.sub(r'^["\']+|["\']+$', "", val)
            result[key] = val
            current_key = key
        elif line.startswith("  - ") or line.startswith("- "):
            if current_key and current_key in result:
                result[current_key] = (result[current_key] or "") + "\n  - " + line.strip().lstrip("- ").strip()
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--keyword", required=True)
    args = ap.parse_args()

    with open(args.path, encoding="utf-8") as f:
        text = f.read()

    fm = parse_frontmatter(text)
    errors = []
    if not fm:
        print("FAIL: no YAML frontmatter found")
        sys.exit(1)

    fields = parse_fields(fm)

    for field in ["title", "description", "slug", "date", "author", "category", "tags", "reading_time"]:
        if field not in fields:
            errors.append(f"missing required field: {field}")

    # forbidden fields since 2026-08-11
    for field in ["image", "keywords", "related"]:
        if field in fields:
            errors.append(f"forbidden field (removed 2026-08-11): {field}")

    # category must be one of Product | Comparison | Research
    category_val = fields.get("category", "").strip()
    if category_val and category_val not in ("Product", "Comparison", "Research"):
        errors.append(f"category must be Product | Comparison | Research: {category_val}")

    # tags: 3-6 kebab-case items
    tags_val = fields.get("tags", "").strip()
    if tags_val:
        # handle inline array ["a", "b", ...] or multi-line list
        raw = tags_val
        if raw.startswith("[") and raw.endswith("]"):
            raw = raw[1:-1]
        items = [t.strip().strip('"').strip("'") for t in re.split(r"[,\n]", raw) if t.strip()]
        items = [t for t in items if not (t.startswith("-") and len(t) == 1)]
        items = [t.lstrip("- ").strip() for t in items]
        items = [t for t in items if t]
        if not (3 <= len(items) <= 6):
            errors.append(f"tags must have 3-6 items, got {len(items)}")
        for t in items:
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", t):
                errors.append(f"tag not kebab-case: {t}")

    # reading_time: positive integer
    rt_val = fields.get("reading_time", "").strip()
    if rt_val:
        if not re.fullmatch(r"\d+", rt_val) or int(rt_val) < 1:
            errors.append(f"reading_time must be a positive integer: {rt_val}")

    # date must be YYYY-MM-DD (publication date, never changes)
    date_val = fields.get("date", "").strip()
    if date_val and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_val):
        errors.append(f"date must be YYYY-MM-DD (ISO 8601): {date_val}")

    # updated (optional) must be YYYY-MM-DD and >= date
    updated_val = fields.get("updated", "").strip()
    if updated_val:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", updated_val):
            errors.append(f"updated must be YYYY-MM-DD (ISO 8601): {updated_val}")
        elif date_val and updated_val < date_val:
            errors.append(f"updated ({updated_val}) must be >= date ({date_val})")

    # slug checks
    slug = fields.get("slug", "").strip()
    if slug:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
            errors.append(f"slug not kebab-case: {slug}")
        if re.search(r"\d{4}", slug):
            errors.append(f"slug contains year (must be evergreen): {slug}")
        if len(slug) > 60:
            errors.append(f"slug too long ({len(slug)} > 60): {slug}")
        # slug must match filename base (strip NN- prefix and optional -2026/-NNNN year suffix)
        fname = args.path.replace("\\", "/").split("/")[-1]
        fbase = re.sub(r"^\d+-", "", fname).replace(".md", "")
        fbase = re.sub(r"-\d{4}$", "", fbase)
        if fbase != slug:
            errors.append(f"slug {slug} does not match filename base {fbase}")
    else:
        errors.append("missing slug")

    # title contains primary keyword + length
    title = fields.get("title", "")
    if title:
        if args.keyword.lower() not in title.lower():
            errors.append(f"primary keyword '{args.keyword}' not in title")
        if not (45 <= len(title) <= 100):
            errors.append(f"title length {len(title)} not in 45-100 range")
    else:
        errors.append("missing title")

    # description length
    desc = fields.get("description", "")
    if desc:
        if not (120 <= len(desc) <= 190):
            errors.append(f"description length {len(desc)} not in 120-190 range")
    else:
        errors.append("missing description")

    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("PASS: frontmatter valid")
    sys.exit(0)


if __name__ == "__main__":
    main()
