#!/usr/bin/env python3
"""Extract keywordEn from Alignify knowledge blocks."""
import json
import re
from pathlib import Path

KB_ROOT = Path("e:/clients/Alignify/knowledge")
OUT = Path("e:/clients/temp/kw-audit-batches/all_kb_keywords.json")

SKIP_PARTS = {"_briefs", "README.md", "_TEMPLATE.md", "KEYWORD-RESEARCH.md"}

pat = re.compile(r"keywordEn[`']?:\s*\*\*([^*\n]+)\*\*")

items = []
for f in sorted(KB_ROOT.rglob("*.md")):
    rel = f.relative_to(KB_ROOT).as_posix()
    if any(s in rel for s in SKIP_PARTS):
        continue
    text = f.read_text(encoding="utf-8", errors="ignore")
    m = pat.search(text)
    if not m:
        continue
    kw = m.group(1).strip()
    # first segment before slash as primary test query
    primary = kw.split("/")[0].strip()
    items.append({
        "slug": f.stem,
        "path": rel,
        "keywordEn": kw,
        "primary_test": primary,
    })

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Extracted {len(items)} slugs -> {OUT}")
