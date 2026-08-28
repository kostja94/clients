#!/usr/bin/env python3
"""Find broken knowledge/tools slug links after cluster migration."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOLS_ROOT = REPO / "knowledge" / "tools"
SKIP_DIRS = {"website-building", "blog-website-builder"}
META = {"README.md", "KEYWORD-RESEARCH.md", "territory-map.md", "_TEMPLATE.md"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#]+\.md(?:#[^)]+)?)\)")


def build_slug_map() -> dict[str, Path]:
    slug_map: dict[str, Path] = {}
    for item in TOOLS_ROOT.iterdir():
        if item.is_dir() and item.name not in SKIP_DIRS:
            for md in item.glob("*.md"):
                if md.name not in META:
                    slug_map[md.stem] = md
    for md in TOOLS_ROOT.glob("*.md"):
        if md.name not in META:
            slug_map.setdefault(md.stem, md)
    return slug_map


def main() -> int:
    slug_map = build_slug_map()
    broken: list[tuple[Path, str, str]] = []

    for md in REPO.rglob("*.md"):
        if any(p in SKIP_DIRS for p in md.parts):
            continue
        if "node_modules" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1).split("#", 1)[0]
            if not raw.endswith(".md"):
                continue
            resolved = (md.parent / raw).resolve()
            if resolved.exists():
                continue
            slug = Path(raw).name[:-3]
            if slug in slug_map:
                expected = slug_map[slug]
                try:
                    import os

                    fix = os.path.relpath(expected, md.parent).replace("\\", "/")
                except ValueError:
                    fix = str(expected)
                broken.append((md.relative_to(REPO), raw, fix))

    if not broken:
        print("No broken slug links found.")
        return 0

    print(f"Broken links: {len(broken)}")
    for file, raw, fix in broken[:50]:
        print(f"  {file}: {raw}  ->  {fix}")
    if len(broken) > 50:
        print(f"  ... and {len(broken) - 50} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
