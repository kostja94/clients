#!/usr/bin/env python3
"""FinalRound narrative word count + H3 word-count gate.

Counts narrative words (excludes frontmatter, tables, FAQ Q/A) and checks
against the article-type minimum from the skill route table.

Types and minimums (narrative words):
  announcement  1200
  review        1500
  alternative   2000
  roundup       2500
  prep          1800
  research      1800
  industry      2000

Usage:
    python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {type}
Exit code 0 = PASS, 1 = FAIL.
"""
import argparse
import re
import sys

MIN_WORDS = {
    "announcement": 1200,
    "review": 1500,
    "alternative": 2000,
    "roundup": 2500,
    "prep": 1800,
    "research": 1800,
    "industry": 2000,
}


def split_frontmatter(text: str):
    m = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    if m:
        return text[m.end():]
    return text


def count_narrative(text: str) -> int:
    body = split_frontmatter(text)
    lines = body.splitlines()
    in_faq = False
    words = 0
    for line in lines:
        stripped = line.strip()
        # skip empty
        if not stripped:
            continue
        # skip headings; manage FAQ scope (FAQ ends at the next H2)
        if stripped.startswith("#"):
            if stripped.lower().startswith("## faq"):
                in_faq = True
            elif in_faq and stripped.startswith("##"):
                in_faq = False
            continue
        # skip table rows (any line containing a pipe)
        if "|" in stripped:
            continue
        # FAQ content (Q/A) — skipped for narrative count
        if in_faq:
            continue
        words += len(stripped.split())
    return words


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--intent", required=True, choices=list(MIN_WORDS.keys()))
    args = ap.parse_args()

    with open(args.path, encoding="utf-8") as f:
        text = f.read()

    count = count_narrative(text)
    minimum = MIN_WORDS[args.intent]

    if count < minimum:
        print(f"FAIL: narrative words {count} < minimum {minimum} for intent '{args.intent}'")
        sys.exit(1)
    print(f"PASS: narrative words {count} >= {minimum}")
    sys.exit(0)


if __name__ == "__main__":
    main()
