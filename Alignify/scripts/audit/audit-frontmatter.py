#!/usr/bin/env python3
"""Audit content/*.md YAML frontmatter consistency (E44–E48 + schema).

Required keys (all locales):
  title, description, slug, date, updated, readingMinutes, pageUrl, locale,
  pillar, contentType

Optional keys:
  section, heroImage, heroImageAlt

Deprecated (must not appear after Taxonomy v2 migration):
  category, categorySecondary

Forbidden keys:
  heroHtml, howTo, heroContent

Usage:
  python audit-frontmatter.py --root "E:/自有部署项目/alignify production"
  python audit-frontmatter.py --root ... --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = frozenset(
    {
        "title",
        "description",
        "slug",
        "date",
        "updated",
        "readingMinutes",
        "pageUrl",
        "locale",
        "pillar",
        "contentType",
    }
)
OPTIONAL = frozenset({"section", "heroImage", "heroImageAlt"})
DEPRECATED = frozenset({"category", "categorySecondary"})
ALLOWED = REQUIRED | OPTIONAL
FORBIDDEN = frozenset({"heroHtml", "howTo", "heroContent"})


def parse_keys(text: str) -> tuple[dict[str, str], list[str]]:
    m = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", text)
    if not m:
        return {}, ["E01: missing frontmatter delimiters"]
    issues: list[str] = []
    data: dict[str, str] = {}
    in_hero = False
    head_lines = m.group(1).splitlines()

    if head_lines and not head_lines[0].strip():
        issues.append("E48: leading blank line in frontmatter")
    if head_lines and not head_lines[-1].strip():
        issues.append("E48: trailing blank line in frontmatter")

    for line in head_lines:
        if in_hero:
            if re.match(r"^\s+", line):
                continue
            in_hero = False
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("heroHtml:"):
            issues.append("E44: forbidden frontmatter key heroHtml")
            in_hero = True
            continue
        if re.match(r"^\s*<", line):
            issues.append("E45: HTML line in frontmatter (legacy heroHtml residue)")
            continue
        kv = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if not kv:
            issues.append(f"E45: unparseable frontmatter line: {stripped[:60]}")
            continue
        key, val = kv.group(1), kv.group(2)
        if key in FORBIDDEN:
            issues.append(f"E44: forbidden frontmatter key {key}")
        elif key in DEPRECATED:
            issues.append(f"E49: deprecated frontmatter key {key} (use pillar/section/contentType)")
        elif key not in ALLOWED:
            issues.append(f"E46: unknown frontmatter key {key}")
        data[key] = val.strip().strip('"')

    missing = REQUIRED - set(data.keys())
    for k in sorted(missing):
        issues.append(f"E47: missing required key {k}")

    return data, issues


def channel_slug(path: Path) -> tuple[str, str, str]:
    parts = path.parts
    # content/{channel}/{locale}/{slug}.md
    try:
        i = parts.index("content")
        channel, locale, filename = parts[i + 1], parts[i + 2], parts[i + 3]
        slug = filename.removesuffix(".md")
        return channel, locale, slug
    except (ValueError, IndexError):
        return "", "", path.stem


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--root",
        default=r"E:\自有部署项目\alignify production",
    )
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    content = root / "content"

    by_slug: dict[tuple[str, str], dict] = {}
    file_issues: list[dict] = []

    for path in sorted(content.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        data, issues = parse_keys(text)
        channel, locale, slug = channel_slug(path)
        rel = str(path.relative_to(root))

        if issues:
            file_issues.append({"path": rel, "issues": issues})

        keyset = frozenset(data.keys())
        by_slug.setdefault((channel, slug), {})[locale] = {
            "path": rel,
            "keys": sorted(keyset),
        }

    parity_issues: list[dict] = []
    for (channel, slug), locales in sorted(by_slug.items()):
        if len(locales) < 2:
            continue
        keysets = {loc: frozenset(info["keys"]) for loc, info in locales.items()}
        unique = set(keysets.values())
        if len(unique) > 1:
            parity_issues.append(
                {
                    "channel": channel,
                    "slug": slug,
                    "locales": {k: sorted(v) for k, v in keysets.items()},
                }
            )

    fail_count = len(file_issues) + len(parity_issues)
    report = {
        "files_with_issues": len(file_issues),
        "parity_mismatches": len(parity_issues),
        "file_issues": file_issues,
        "parity_issues": parity_issues,
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for item in file_issues:
            print(item["path"])
            for iss in item["issues"]:
                print(f"  {iss}")
        for item in parity_issues:
            print(f"PARITY {item['channel']}/{item['slug']}")
            for loc, keys in item["locales"].items():
                print(f"  {loc}: {keys}")

        print(
            f"\nFiles with issues: {len(file_issues)} | "
            f"ZH/EN key parity mismatches: {len(parity_issues)}"
        )

    return 1 if fail_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
