#!/usr/bin/env python3
import sys
sys.path.insert(0, r"e:\clients\temp")
from audit_kb_dedupe import audit_file
from pathlib import Path

targets = [
    Path(r"e:\clients\Alignify\knowledge\tools\voice-audio"),
    Path(r"e:\clients\Alignify\knowledge\tools\llm"),
    Path(r"e:\clients\Alignify\knowledge\tools\search-geo"),
]
files = [Path(r"e:\clients\Alignify\knowledge\tools\llm-leaderboard-snapshots.md")]
for f in targets:
    files.extend(sorted(f.glob("*.md")))

for fp in files:
    r = audit_file(fp)
    print(f"{r['severity']:6} score={r['score']:2} lines={r['lines']:4} {r['path']}")
    for i in r["issues"]:
        print(f"       [{i['severity']}] {i['type']}: {i['detail']}")
