#!/usr/bin/env python3
"""Rewrite knowledge/tools slug links after theme-cluster folder migration."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOLS_ROOT = REPO / "knowledge" / "tools"
SKIP_DIRS = {"website-building", "blog-website-builder"}
META_FILES = {"README.md", "KEYWORD-RESEARCH.md", "territory-map.md", "_TEMPLATE.md"}

LINK_RE = re.compile(r"(\[[^\]]*\]\()([^)]+)(\))")
BARE_KB_RE = re.compile(r"(?<![/\w-])knowledge/tools/([a-z0-9-]+)\.md")
BACKTICK_KB_RE = re.compile(r"`knowledge/tools/([a-z0-9-]+)\.md`")


def build_slug_map() -> dict[str, str]:
    slug_map: dict[str, str] = {}

    for item in sorted(TOOLS_ROOT.iterdir()):
        if not item.is_dir() or item.name in SKIP_DIRS:
            continue
        for md in sorted(item.glob("*.md")):
            if md.name in META_FILES:
                continue
            slug_map[md.stem] = item.name

    for md in sorted(TOOLS_ROOT.glob("*.md")):
        if md.name in META_FILES:
            continue
        slug_map.setdefault(md.stem, "")

    return slug_map


def target_rel(from_file: Path, slug: str, slug_map: dict[str, str]) -> str | None:
    if slug not in slug_map:
        return None
    cluster = slug_map[slug]
    if cluster:
        target = TOOLS_ROOT / cluster / f"{slug}.md"
    else:
        target = TOOLS_ROOT / f"{slug}.md"
    rel = os.path.relpath(target, from_file.parent).replace("\\", "/")
    return rel


def split_path_anchor(raw: str) -> tuple[str, str]:
    if "#" in raw:
        path, anchor = raw.split("#", 1)
        return path, f"#{anchor}"
    return raw, ""


def slug_from_path(path: str) -> str | None:
    if not path.endswith(".md"):
        return None
    name = path.rsplit("/", 1)[-1]
    return name[:-3]


def rewrite_links(text: str, from_file: Path, slug_map: dict[str, str]) -> tuple[str, int]:
    changes = 0

    def repl_link(match: re.Match[str]) -> str:
        nonlocal changes
        prefix, raw, suffix = match.group(1), match.group(2), match.group(3)
        path, anchor = split_path_anchor(raw)
        slug = slug_from_path(path)
        if not slug:
            return match.group(0)
        new_path = target_rel(from_file, slug, slug_map)
        if not new_path:
            return match.group(0)
        candidate = new_path + anchor
        if candidate == raw:
            return match.group(0)
        changes += 1
        return prefix + candidate + suffix

    text = LINK_RE.sub(repl_link, text)

    def repl_bare(match: re.Match[str]) -> str:
        nonlocal changes
        slug = match.group(1)
        if slug not in slug_map:
            return match.group(0)
        cluster = slug_map[slug]
        new = f"knowledge/tools/{cluster}/{slug}.md" if cluster else f"knowledge/tools/{slug}.md"
        old = f"knowledge/tools/{slug}.md"
        if new == old:
            return match.group(0)
        changes += 1
        return new

    text = BARE_KB_RE.sub(repl_bare, text)

    def repl_backtick(match: re.Match[str]) -> str:
        nonlocal changes
        slug = match.group(1)
        if slug not in slug_map:
            return match.group(0)
        cluster = slug_map[slug]
        new = f"knowledge/tools/{cluster}/{slug}.md" if cluster else f"knowledge/tools/{slug}.md"
        old = f"knowledge/tools/{slug}.md"
        if new == old:
            return match.group(0)
        changes += 1
        return f"`{new}`"

    text = BACKTICK_KB_RE.sub(repl_backtick, text)
    return text, changes


def iter_markdown_roots() -> list[Path]:
    roots = [
        TOOLS_ROOT,
        REPO / "knowledge",
        REPO / "skills",
        REPO / "keywords",
    ]
    files: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.resolve() in seen:
                continue
            seen.add(path.resolve())
            files.append(path)
    return sorted(files)


def main() -> int:
    slug_map = build_slug_map()
    total_files = 0
    total_changes = 0

    for path in iter_markdown_roots():
        original = path.read_text(encoding="utf-8")
        updated, changes = rewrite_links(original, path, slug_map)
        if changes:
            path.write_text(updated, encoding="utf-8", newline="\n")
            total_files += 1
            total_changes += changes
            print(f"{changes:4d}  {path.relative_to(REPO)}")

    print(f"\nUpdated {total_files} files, {total_changes} link rewrites.")
    print(f"Indexed {len(slug_map)} slugs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
