#!/usr/bin/env python3
"""Prose rhythm, pseudo-list, Chinese, and list/table ratio audit (Phase 5 blocking gate)."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

PSEUDO_BOLD_DOT_RE = re.compile(r"^\*\*[^*]+\*\*\.")
PSEUDO_MISTAKE_RE = re.compile(r"^\*\*Mistake \d+", re.I)
PSEUDO_CHOOSE_WHEN_RE = re.compile(r"^\*\*Choose .+ when:\*\*$", re.I)
CHINESE_RE = re.compile(r"[\u4e00-\u9fff]")
LIST_LINE_RE = re.compile(r"^\s*([-*]|\d+\.)\s")


def strip_fm(text: str) -> tuple[str, dict[str, str]]:
    meta: dict[str, str] = {}
    if not text.startswith("---"):
        return text, meta
    end = text.find("---", 3)
    if end == -1:
        return text, meta
    fm_block = text[3:end].strip()
    for line in fm_block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip('"').strip("'")
    return text[end + 3 :].lstrip(), meta


def count_sentences(p: str) -> int:
    parts = re.split(r"(?<=[.!?])\s+", p.strip())
    return len([x for x in parts if x.strip()])


def infer_intent(meta: dict[str, str]) -> str | None:
    sec = meta.get("secondary_category", "").lower()
    cat = meta.get("category", "").lower()
    if "comparison" in sec:
        return "comparison"
    if cat == "product":
        return "brandpillar"
    return None


def detect_pseudo_lists(lines: list[str]) -> tuple[int, list[str]]:
    """Return (count, sample messages) for pseudo-list patterns."""
    hits: list[str] = []
    count = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        line_no = i + 1

        if PSEUDO_BOLD_DOT_RE.match(stripped):
            count += 1
            hits.append(f"line {line_no}: bold-dot pseudo-list: {stripped[:60]}")
            continue

        if PSEUDO_MISTAKE_RE.match(stripped):
            count += 1
            hits.append(f"line {line_no}: Mistake pseudo-list: {stripped[:60]}")
            continue

        if PSEUDO_CHOOSE_WHEN_RE.match(stripped):
            # Check if followed by bullet lines within next 5 lines
            following = lines[i + 1 : i + 6]
            if any(LIST_LINE_RE.match(f) for f in following):
                count += 1
                hits.append(f"line {line_no}: Choose-when header + bullets")

    return count, hits


def extract_tldr_blog_links(body: str) -> int:
    m = re.search(r"^## TL;DR\s*$", body, re.M)
    if not m:
        return 0
    rest = body[m.end() :]
    next_h2 = re.search(r"^## ", rest, re.M)
    tldr = rest[: next_h2.start()] if next_h2 else rest
    md_links = len(re.findall(r"\]\(/blog/", tldr))
    html_links = len(re.findall(r'href="/blog/', tldr))
    return md_links + html_links


def analyze(path: Path, intent: str | None = None) -> dict:
    raw = path.read_text(encoding="utf-8")
    body, meta = strip_fm(raw)
    if intent is None:
        intent = infer_intent(meta)
    lines = body.splitlines()

    prose_chars = list_chars = table_chars = 0
    in_table = False

    for line in lines:
        s = line.strip()
        if s.startswith("|") and "|" in s[1:]:
            in_table = True
            table_chars += len(line) + 1
            continue
        if in_table and not s.startswith("|"):
            in_table = False
        if LIST_LINE_RE.match(line):
            list_chars += len(line) + 1
        elif s and not line.startswith("#"):
            prose_chars += len(line) + 1

    blocks = re.split(r"\n\s*\n", body)
    long_paras = 0
    consecutive_short = 0
    max_consecutive_short = 0
    pseudo_block_re = re.compile(r"^\*\*[^*]+\*\*\.\s+\S", re.M)
    pseudo_list_blocks = 0

    for b in blocks:
        b = b.strip()
        if not b or b.startswith("#") or b.startswith("|") or b.startswith("- "):
            continue
        if b.startswith("1.") or b.startswith("!["):
            continue
        if LIST_LINE_RE.match(b):
            continue
        sc = count_sentences(b)
        if sc >= 4:
            long_paras += 1
            consecutive_short = 0
        elif 1 <= sc <= 3:
            consecutive_short += 1
            max_consecutive_short = max(max_consecutive_short, consecutive_short)
        if pseudo_block_re.match(b):
            pseudo_list_blocks += 1

    pseudo_line_count, pseudo_line_samples = detect_pseudo_lists(lines)
    pseudo_list_total = pseudo_list_blocks + pseudo_line_count

    blog_slugs = re.findall(r"\]\((/blog/[^\)#]+)", body)
    slug_counts = defaultdict(int)
    for s in blog_slugs:
        slug_counts[s] += 1
    dup_slugs = {k: v for k, v in slug_counts.items() if v > 1}

    chinese_lines = [
        (i + 1, line)
        for i, line in enumerate(lines)
        if CHINESE_RE.search(line)
    ]

    total = prose_chars + list_chars + table_chars
    ratio = (list_chars + table_chars) / total * 100 if total else 0

    fails: list[str] = []
    if long_paras < 3:
        fails.append(f"long_paras_ge4={long_paras} (need ≥3)")
    if pseudo_list_total > 5:
        fails.append(f"pseudo_list={pseudo_list_total} (max 5)")
    if intent in ("comparison", "brandpillar") and ratio > 35:
        fails.append(f"list_table_pct={ratio:.1f}% for {intent} (max 35%)")
    if chinese_lines:
        fails.append(f"chinese_line_count={len(chinese_lines)} (body must be English only)")

    return {
        "path": str(path),
        "intent": intent,
        "long_paras_ge4": long_paras,
        "max_consecutive_short_paras": max_consecutive_short,
        "pseudo_list_blocks": pseudo_list_blocks,
        "pseudo_list_lines": pseudo_line_count,
        "pseudo_list_total": pseudo_list_total,
        "pseudo_list_samples": pseudo_line_samples[:8],
        "list_table_pct": round(ratio, 1),
        "blog_link_instances": len(blog_slugs),
        "blog_unique_slugs": len(set(blog_slugs)),
        "dup_slugs": dup_slugs,
        "tldr_blog_links": extract_tldr_blog_links(body),
        "chinese_line_count": len(chinese_lines),
        "chinese_lines": chinese_lines[:5],
        "fails": fails,
        "pass": len(fails) == 0,
    }


def print_report(r: dict) -> None:
    print(f"=== {r['path']} ===")
    print(f"  intent: {r['intent']}")
    print(f"  long_paras_ge4: {r['long_paras_ge4']}")
    print(f"  max_consecutive_short_paras: {r['max_consecutive_short_paras']}")
    print(f"  pseudo_list_total: {r['pseudo_list_total']} (blocks={r['pseudo_list_blocks']}, lines={r['pseudo_list_lines']})")
    if r["pseudo_list_samples"]:
        for s in r["pseudo_list_samples"]:
            print(f"    - {s}")
    print(f"  list_table_pct: {r['list_table_pct']}")
    print(f"  blog links: {r['blog_link_instances']} instances, {r['blog_unique_slugs']} unique")
    if r["dup_slugs"]:
        print(f"  dup_slugs: {r['dup_slugs']}")
    print(f"  tldr_blog_links: {r['tldr_blog_links']}")
    print(f"  chinese_line_count: {r['chinese_line_count']}")
    if r["chinese_lines"]:
        for ln, text in r["chinese_lines"]:
            print(f"    line {ln}: {text[:70]}")
    print()
    if r["pass"]:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")
        for f in r["fails"]:
            print(f"  - {f}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description="Prose and link rhythm audit for blog markdown")
    parser.add_argument("path", type=Path, help="Path to markdown file (from today/ root)")
    parser.add_argument(
        "--intent",
        choices=["comparison", "brandpillar", "alternative", "glossary", "usecase", "howto", "opinion", "healthcare"],
        help="Article type for threshold selection (auto-detected from frontmatter if omitted)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 on FAIL conditions (Phase 5 blocking gate)",
    )
    args = parser.parse_args()

    if not args.path.is_file():
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 1

    result = analyze(args.path, intent=args.intent)
    print_report(result)

    if args.strict and not result["pass"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
