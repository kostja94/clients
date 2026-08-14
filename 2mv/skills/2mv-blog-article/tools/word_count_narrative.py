#!/usr/bin/env python3
"""Narrative word count (excludes frontmatter, tables, FAQ Q&A blocks). Gate: H3."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# 2mv article type thresholds (see article-types.md §1)
THRESHOLDS = {
    "research": 2000,
    "comparison": 2500,
    "product": 2000,
    "alternative": 2000,
    "announcement": 1200,
}


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def remove_tables(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_table = False
    for line in lines:
        if re.match(r"^\s*\|", line):
            in_table = True
            continue
        if in_table and line.strip() == "":
            in_table = False
            continue
        if not in_table:
            out.append(line)
    return "\n".join(out)


def remove_faq_blocks(text: str) -> str:
    """Remove FAQ question/answer blocks in FAQ section."""
    lines = text.splitlines()
    out: list[str] = []
    in_faq = False
    skip_next_answer = False
    for line in lines:
        low = line.lower().strip()
        if re.match(r"^#{1,3}\s+faq", line, re.I):
            in_faq = True
            continue
        if in_faq and re.match(r"^#{1,2}\s+", line) and not re.match(r"^#{1,3}\s+faq", line, re.I):
            in_faq = False
        if in_faq:
            if re.match(r"^#{3,4}\s+", line):
                skip_next_answer = True
                continue
            if skip_next_answer and line.strip():
                skip_next_answer = False
                continue
            if skip_next_answer:
                continue
        if not in_faq or not line.strip().startswith("**Q"):
            out.append(line)
    return "\n".join(out)


def count_words(text: str) -> int:
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#>*_\-\|]", " ", text)
    words = re.findall(r"[A-Za-z0-9]+", text)
    return len(words)


def emit(status: str, gate: str, msg: str) -> None:
    print(f"{status} | {gate} | {msg}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Narrative word count for 2mv blog articles")
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--intent",
        required=True,
        choices=sorted(THRESHOLDS.keys()),
        help="Article type for H3 threshold (research|comparison|product|alternative|announcement)",
    )
    parser.add_argument("--min", type=int, default=None, help="Override minimum word count")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    body = remove_tables(body)
    body = remove_faq_blocks(body)
    n = count_words(body)
    minimum = args.min if args.min is not None else THRESHOLDS[args.intent]
    gate = "H3"

    if n >= minimum:
        emit("PASS", gate, f"narrative words {n} >= {minimum} ({args.intent})")
        return 0
    emit("FAIL", gate, f"narrative words {n} < {minimum} ({args.intent})")
    return 1


if __name__ == "__main__":
    sys.exit(main())
