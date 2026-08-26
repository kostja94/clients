#!/usr/bin/env python3
"""Audit content/**/*.md for GFM tables / Markdown lists outside childrenHtml fences."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEPLOY = Path(r"E:\自有部署项目\alignify production")
if len(sys.argv) > 1:
    DEPLOY = Path(sys.argv[1])

CONTENT = DEPLOY / "content"
CATS = ["blog", "marketing", "seo", "insights", "events", "tools"]

PIPE_RE = re.compile(r"^\|")
UL_RE = re.compile(r"^-\s+\S")
OL_RE = re.compile(r"^\d+\.\s+\S")
FENCE_RE = re.compile(r"^```")


def audit() -> list[tuple[str, int, str, str]]:
    findings: list[tuple[str, int, str, str]] = []
    for cat in CATS:
        d = CONTENT / cat
        if not d.exists():
            continue
        for md in sorted(d.rglob("*.md")):
            lines = md.read_text(encoding="utf-8").splitlines()
            in_children = False
            in_fence = False
            for i, line in enumerate(lines, 1):
                s = line.strip()
                if s in ("<!-- childrenHtml:start -->", "<!-- html-block:start -->"):
                    in_children = True
                    continue
                if s in ("<!-- childrenHtml:end -->", "<!-- html-block:end -->"):
                    in_children = False
                    continue
                if FENCE_RE.match(s):
                    in_fence = not in_fence
                    continue
                if in_children or in_fence:
                    continue
                if PIPE_RE.match(line):
                    findings.append((str(md.relative_to(CONTENT)), i, "GFM_TABLE", line[:120]))
                elif UL_RE.match(line):
                    findings.append((str(md.relative_to(CONTENT)), i, "MD_UL", line[:120]))
                elif OL_RE.match(line):
                    findings.append((str(md.relative_to(CONTENT)), i, "MD_OL", line[:120]))
    return findings


def main() -> None:
    findings = audit()
    by_file: dict[str, list] = defaultdict(list)
    for f in findings:
        by_file[f[0]].append(f)

    print(f"Deploy: {DEPLOY}")
    print(f"Total findings: {len(findings)} in {len(by_file)} files\n")
    for path in sorted(by_file):
        items = by_file[path]
        kinds: dict[str, int] = defaultdict(int)
        for _, _, k, _ in items:
            kinds[k] += 1
        print(
            f"{path}  (tables={kinds['GFM_TABLE']}, ul={kinds['MD_UL']}, ol={kinds['MD_OL']})"
        )
        for _, ln, k, preview in items[:10]:
            print(f"  L{ln} [{k}] {preview}")
        if len(items) > 10:
            print(f"  ... +{len(items) - 10} more")
        print()

    if findings:
        sys.exit(1)


if __name__ == "__main__":
    main()
