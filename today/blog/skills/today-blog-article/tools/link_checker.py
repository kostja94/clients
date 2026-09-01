#!/usr/bin/env python3
"""Markdown link checker. Gates: P0 G2 (malformed/empty), G6 (forbidden paths), R4, R5."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
RAW_URL_RE = re.compile(r"(?<!\]\()https?://[^\s\)]+")
HTML_BLOG_RE = re.compile(r'href="(/blog/[^"#]+)(?:#[^"]*)?"')
BLOG_SLUG_RE = re.compile(r"(/blog/[^\)#]+)")


def emit(status: str, gate: str, msg: str, line: int | None = None) -> None:
    suffix = f" [line {line}]" if line is not None else ""
    print(f"{status} | {gate} | {msg}{suffix}")


def blog_slug(url: str) -> str | None:
    """Normalize /blog/ link to slug path without anchor."""
    url = url.strip()
    if not url.startswith("/blog/"):
        return None
    return url.split("#")[0]


def extract_tldr_section(text: str) -> tuple[str | None, int | None]:
    """Return TL;DR body and starting line number (1-based), or (None, None)."""
    lines = text.splitlines()
    in_tldr = False
    tldr_lines: list[str] = []
    start_line: int | None = None

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped == "## TL;DR":
            in_tldr = True
            start_line = i
            continue
        if in_tldr:
            if stripped.startswith("## ") and stripped != "## TL;DR":
                break
            tldr_lines.append(line)

    if not in_tldr or start_line is None:
        return None, None
    return "\n".join(tldr_lines), start_line


def collect_blog_slugs(text: str) -> dict[str, list[int]]:
    """Map normalized /blog/{slug} paths to line numbers where they appear."""
    slug_lines: dict[str, list[int]] = defaultdict(list)
    lines = text.splitlines()

    for i, line in enumerate(lines, start=1):
        for _anchor, url in LINK_RE.findall(line):
            slug = blog_slug(url)
            if slug:
                slug_lines[slug].append(i)
        for slug in HTML_BLOG_RE.findall(line):
            slug_lines[slug].append(i)

    return slug_lines


def count_blog_links_in_section(section: str) -> int:
    count = len(BLOG_SLUG_RE.findall(section))
    count += len(HTML_BLOG_RE.findall(section))
    return count


def check_links(text: str, forbidden: list[str]) -> tuple[int, int]:
    fails = 0
    warns = 0
    lines = text.splitlines()
    seen: set[str] = set()

    for i, line in enumerate(lines, start=1):
        for _anchor, url in LINK_RE.findall(line):
            url = url.strip()
            if not url or url in seen:
                continue
            seen.add(url)

            if url.startswith("#"):
                continue

            if url in ("", "#", "TODO", "TBD"):
                emit("FAIL", "P0-G2", f"empty or placeholder link: ({url})", i)
                fails += 1
                continue

            if url.startswith("/"):
                for prefix in forbidden:
                    if url.startswith(prefix) or prefix in url:
                        emit("FAIL", "P0-G6", f"internal link to forbidden path: {url}", i)
                        fails += 1
                if " " in url:
                    emit("FAIL", "P0-G2", f"malformed internal URL (spaces): {url}", i)
                    fails += 1
                continue

            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                emit("FAIL", "P0-G2", f"malformed URL: {url}", i)
                fails += 1

        for url in RAW_URL_RE.findall(line):
            if "example.com" in url.lower():
                emit("FAIL", "P0-G2", f"placeholder domain: {url}", i)
                fails += 1

    # R4: duplicate /blog/{slug} in same file
    slug_lines = collect_blog_slugs(text)
    for slug, occurrences in sorted(slug_lines.items()):
        if len(occurrences) > 1:
            emit(
                "FAIL",
                "R4",
                f"duplicate /blog/ slug ({len(occurrences)}x): {slug} at lines {occurrences}",
                occurrences[0],
            )
            fails += 1

    if not any(len(v) > 1 for v in slug_lines.values()):
        emit("PASS", "R4", f"no duplicate /blog/ slugs ({len(slug_lines)} unique)")

    # R5: TL;DR should have at most 1 /blog/ link
    tldr_section, tldr_line = extract_tldr_section(text)
    if tldr_section is None:
        emit("WARN", "R5", "no ## TL;DR section found")
        warns += 1
    else:
        tldr_blog_count = count_blog_links_in_section(tldr_section)
        if tldr_blog_count > 1:
            emit(
                "WARN",
                "R5",
                f"TL;DR has {tldr_blog_count} /blog/ links (max 1); spread links across H2 sections",
                tldr_line,
            )
            warns += 1
        else:
            emit("PASS", "R5", f"TL;DR /blog/ links: {tldr_blog_count} (max 1)")

    if fails == 0:
        emit("PASS", "P0-G2", f"checked {len(seen)} unique link targets")
        if forbidden:
            emit("PASS", "P0-G6", f"no links to forbidden prefixes: {forbidden}")
    return fails, warns


def main() -> int:
    parser = argparse.ArgumentParser(description="Link checker for blog markdown (generic)")
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--forbidden",
        default="",
        help="Comma-separated forbidden internal path prefixes (G6), from project-config",
    )
    parser.add_argument(
        "--strict-r5",
        action="store_true",
        help="Treat R5 TL;DR link warnings as FAIL",
    )
    args = parser.parse_args()

    forbidden = [p.strip() for p in args.forbidden.split(",") if p.strip()]
    text = args.path.read_text(encoding="utf-8")
    fails, warns = check_links(text, forbidden)

    if args.strict_r5 and warns:
        fails += warns
        warns = 0

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
