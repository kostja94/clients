#!/usr/bin/env python3
"""Markdown link checker. Gates: P0 G2 (malformed/empty), G6 (forbidden paths)."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
RAW_URL_RE = re.compile(r"(?<!\]\()https?://[^\s\)]+")


def emit(status: str, gate: str, msg: str, line: int | None = None) -> None:
    suffix = f" [line {line}]" if line is not None else ""
    print(f"{status} | {gate} | {msg}{suffix}")


def check_links(text: str, forbidden: list[str]) -> int:
    fails = 0
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
            if "example.com" in url.lower() and "example" in url.lower():
                emit("FAIL", "P0-G2", f"placeholder domain: {url}", i)
                fails += 1

    if fails == 0:
        emit("PASS", "P0-G2", f"checked {len(seen)} unique link targets")
        if forbidden:
            emit("PASS", "P0-G6", f"no links to forbidden prefixes: {forbidden}")
    return fails


def main() -> int:
    parser = argparse.ArgumentParser(description="Link checker for Oginify blog markdown")
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--forbidden",
        default="",
        help="Comma-separated forbidden internal path prefixes (G6). Oginify default: /pricing,/vs,/templates",
    )
    args = parser.parse_args()

    forbidden = [p.strip() for p in args.forbidden.split(",") if p.strip()]
    text = args.path.read_text(encoding="utf-8")
    fails = check_links(text, forbidden)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
