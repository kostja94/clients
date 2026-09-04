#!/usr/bin/env python3
"""Extract primary keywords from all Alignify knowledge blocks."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

KB = Path(r"e:/clients/Alignify/knowledge")
OUT = Path(r"e:/clients/temp/kw-audit-batches/full_kb_inventory.json")

SKIP_DIR_NAMES = {"_briefs"}
SKIP_FILENAMES = {"README.md", "_TEMPLATE.md", "KEYWORD-RESEARCH.md"}

pat_kw = re.compile(r"keywordEn`?:\s*\*\*([^*\n]+)\*\*", re.I)
pat_kw2 = re.compile(r"`keywordEn`:\s*\*\*([^*\n]+)\*\*", re.I)
pat_h1 = re.compile(r"^#\s+(.+)$", re.M)
pat_narr = re.compile(r"\*\*叙述主词[^*]*\*\*[：:]\s*\*\*([^*\n]+)\*\*")
pat_slash_title = re.compile(r"^#\s+([^/·\n]+)")


def should_skip(rel: str, path: Path) -> bool:
    if path.name in SKIP_FILENAMES:
        return True
    if rel.endswith(".plan.md"):
        return True
    parts = Path(rel).parts
    if any(p in SKIP_DIR_NAMES or p.startswith("_") for p in parts):
        return True
    return False


def first_primary(kw: str) -> str:
    return re.split(r"\s*/\s*", kw)[0].strip()


items = []
no_kw = []

for f in sorted(KB.rglob("*.md")):
    rel = f.relative_to(KB).as_posix()
    if should_skip(rel, f):
        continue
    text = f.read_text(encoding="utf-8", errors="ignore")
    m = pat_kw2.search(text) or pat_kw.search(text)
    h1 = pat_h1.search(text)
    narr = pat_narr.search(text)
    parts = Path(rel).parts
    channel = parts[0] if parts else "unknown"
    slug = f.stem
    h1_text = h1.group(1).strip() if h1 else ""
    if m:
        kw = m.group(1).strip()
        items.append(
            {
                "slug": slug,
                "path": rel,
                "channel": channel,
                "keywordEn": kw,
                "primary_test": first_primary(kw),
                "h1": h1_text,
                "has_keywordEn": True,
            }
        )
    else:
        inferred = ""
        if narr:
            inferred = first_primary(narr.group(1).strip())
        elif h1_text:
            # e.g. "AI Agent Runtime · 知识块" or "Landing Page / 落地页"
            left = re.split(r"\s*[·/|]\s*", h1_text)[0]
            left = re.sub(r"知识块.*", "", left).strip()
            inferred = left
        no_kw.append(
            {
                "slug": slug,
                "path": rel,
                "channel": channel,
                "h1": h1_text[:160],
                "narr": narr.group(1).strip() if narr else "",
                "inferred_primary": inferred,
                "has_keywordEn": False,
            }
        )

OUT.parent.mkdir(parents=True, exist_ok=True)
payload = {
    "with_keywordEn": items,
    "without_keywordEn": no_kw,
    "counts": {
        "with": len(items),
        "without": len(no_kw),
        "channels_with": dict(Counter(i["channel"] for i in items)),
        "channels_without": dict(Counter(i["channel"] for i in no_kw)),
    },
}
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(payload["counts"], ensure_ascii=False, indent=2))
print("wrote", OUT)
