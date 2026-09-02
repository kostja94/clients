#!/usr/bin/env python3
import json, sys
sys.path.insert(0, r"e:\clients\temp")
from audit_kb_dedupe import audit_file
from pathlib import Path

ROOT = Path(r"e:\clients\Alignify\knowledge\tools")
targets = []

for f in (ROOT / "website-builder").glob("*.md"):
    if f.name not in ("README.md", "KEYWORD-RESEARCH.md"):
        targets.append(f)

for f in (ROOT / "cms").glob("*.md"):
    if f.name not in ("README.md", "KEYWORD-RESEARCH.md"):
        targets.append(f)

targets.extend((ROOT / "chat-social").glob("*.md"))
targets.extend((ROOT / "healthcare").glob("*.md"))

root_names = [
    "world-model.md", "family-assistant.md", "fashion.md", "religion.md",
    "animation-library.md", "lifetime-deals.md", "vibe-coding-payments.md",
    "agentic-payments.md", "agentic-commerce.md", "ai-shopping.md",
    "data-engineering-agent.md",
]
for n in root_names:
    p = ROOT / n
    if p.exists():
        targets.append(p)

results = [audit_file(f) for f in sorted(set(targets))]
for r in sorted(results, key=lambda x: (-x["score"], x["path"])):
    if r["severity"] != "NONE":
        print(f"{r['severity']:6} score={r['score']:2} {r['path']}")
        for i in r["issues"]:
            print(f"  [{i['severity']}] {i['type']}: {i['detail']}")
print("---")
print(f"Total: {len(results)}, with issues: {sum(1 for r in results if r['issues'])}")
