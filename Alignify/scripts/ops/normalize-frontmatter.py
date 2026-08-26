#!/usr/bin/env python3
"""Normalize md frontmatter: trim blank lines inside --- blocks (E48).

Usage:
  python normalize-frontmatter.py --root "E:/自有部署项目/alignify production"
  python normalize-frontmatter.py --root ... --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def normalize(text: str) -> tuple[str, bool]:
    m = re.match(r"^(---\r?\n)([\s\S]*?)(\r?\n---\r?\n?)([\s\S]*)$", text)
    if not m:
        return text, False
    open_delim, head, close_delim, body = m.groups()
    orig_lines = head.splitlines()
    lines = list(orig_lines)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    if lines == orig_lines:
        return text, False
    new_head = "\n".join(lines)
    new_text = f"{open_delim}{new_head}\n{close_delim.lstrip(chr(10))}{body}"
    # ensure single newline after closing ---
    if not new_text.split("---", 2)[2].startswith("\n"):
        new_text = re.sub(r"(\n---)\n?", r"\1\n\n", new_text, count=1)
    return new_text, True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"E:\自有部署项目\alignify production")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    content = root / "content"
    n = 0
    for path in sorted(content.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        new_text, changed = normalize(text)
        if changed:
            n += 1
            rel = path.relative_to(root)
            print(f"{'[dry-run] ' if args.dry_run else ''}normalized: {rel}")
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")
    print(f"\nDone: {n} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
