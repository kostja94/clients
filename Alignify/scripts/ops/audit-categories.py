#!/usr/bin/env python3
"""Audit Taxonomy v2 pillar/section/contentType across content/*.md.

Checks:
  - Required keys present (pillar, contentType)
  - Valid enum values
  - EN/ZH parity on taxonomy keys
  - No deprecated category / categorySecondary

Usage:
  python scripts/ops/audit-categories.py --root "E:/自有部署项目/alignify production"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VALID_PILLARS = {
    "image", "video", "audio", "design", "3d", "dev", "search", "llm",
    "productivity", "vertical", "marketing", "seo", "geo", "insights", "events",
}
VALID_CONTENT_TYPES = {
    "tool-guide", "how-to", "strategy", "architecture", "reference", "analysis", "event",
}
TAXONOMY_KEYS = ("pillar", "section", "contentType")


def parse_fm(text: str) -> dict[str, str]:
    m = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", text)
    if not m:
        return {}
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^([A-Za-z0-9_]+):\s*"?([^"]*)"?$', line.strip())
        if kv:
            data[kv.group(1)] = kv.group(2)
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"E:\自有部署项目\alignify production")
    args = ap.parse_args()
    root = Path(args.root)
    content = root / "content"

    issues: list[str] = []
    by_slug: dict[tuple[str, str], dict[str, dict[str, str]]] = {}

    for path in sorted(content.rglob("*.md")):
        rel = path.relative_to(content).as_posix()
        parts = rel.split("/")
        if len(parts) != 3:
            continue
        channel, locale, filename = parts
        slug = filename.removesuffix(".md")
        fm = parse_fm(path.read_text(encoding="utf-8"))

        if fm.get("category") or fm.get("categorySecondary"):
            issues.append(f"{rel}: deprecated category keys present")
        if "pillar" not in fm:
            issues.append(f"{rel}: missing pillar")
        elif fm["pillar"] not in VALID_PILLARS:
            issues.append(f"{rel}: invalid pillar '{fm['pillar']}'")
        if "contentType" not in fm:
            issues.append(f"{rel}: missing contentType")
        elif fm["contentType"] not in VALID_CONTENT_TYPES:
            issues.append(f"{rel}: invalid contentType '{fm['contentType']}'")

        by_slug.setdefault((channel, slug), {})[locale] = {
            k: fm.get(k, "") for k in TAXONOMY_KEYS
        }

    for (channel, slug), locales in sorted(by_slug.items()):
        if len(locales) < 2:
            continue
        vals = list(locales.values())
        if vals[0] != vals[1]:
            issues.append(
                f"{channel}/{slug}: EN/ZH taxonomy mismatch — "
                + " | ".join(f"{loc}={locales[loc]}" for loc in sorted(locales))
            )

    if issues:
        print(f"FAIL: {len(issues)} issue(s)\n")
        for i in issues[:50]:
            print(f"  {i}")
        if len(issues) > 50:
            print(f"  ... and {len(issues) - 50} more")
        return 1

    en_count = sum(1 for p in content.rglob("*.md") if "/en/" in p.as_posix())
    print(f"PASS: {en_count} EN slugs — taxonomy v2 OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
