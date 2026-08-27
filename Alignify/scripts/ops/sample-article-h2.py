#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(r"E:\自有部署项目\alignify production")

def h2_titles(ch, slug, loc="en"):
    p = ROOT / "content" / ch / loc / f"{slug}.md"
    if not p.exists():
        return None
    t = p.read_text(encoding="utf-8")
    if t.startswith("---"):
        t = t.split("---", 2)[-1]
    return [
        (m.group(2) or m.group(1)[:50], m.group(1))
        for m in re.finditer(r"^##\s+(.+?)(?:\s+\{#([^}]+)\})?\s*$", t, re.M)
    ]

samples = {
    "tools": ["video-generator", "llm", "agent-sandbox"],
    "marketing": ["keyword-research", "rate-limit-reset", "geo"],
    "seo": ["schema-markup", "landing-page", "robots-txt"],
    "insights": ["generative-ai-landscape", "reasons-you-need-seo"],
    "blog": ["subdirectory-hosting", "coding-plan", "pricing-strategy"],
}

for ch, slugs in samples.items():
    print(f"\n=== {ch} ===")
    for s in slugs:
        h = h2_titles(ch, s)
        if not h:
            print(f"  {s}: MISSING")
            continue
        ids = [x[0] for x in h]
        print(f"  {s} ({len(h)} H2): {ids}")
