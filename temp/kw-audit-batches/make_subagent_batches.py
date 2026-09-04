#!/usr/bin/env python3
"""Split KB slugs into subagent batches with current primary keywords."""
from __future__ import annotations

import json
import re
from pathlib import Path

INV = json.loads(Path(r"e:/clients/temp/kw-audit-batches/full_kb_inventory.json").read_text(encoding="utf-8"))
OUT_DIR = Path(r"e:/clients/temp/kw-audit-batches/subagent")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SKIP_SLUGS = {"territory-map", "llm-leaderboard-snapshots"}

ZH_ONLY = re.compile(r"^[\u4e00-\u9fff（）()·\s—\-]+$")


def clean_primary(s: str) -> str:
    s = s.strip()
    s = re.sub(r"（[^)]*）", "", s)
    s = re.sub(r"\([^)]*\)", "", s)
    s = s.replace("知识块", "").strip(" ·/-")
    return s.strip()


rows = []
for item in INV["with_keywordEn"]:
    if item["slug"] in SKIP_SLUGS:
        continue
    rows.append(
        {
            "slug": item["slug"],
            "path": item["path"],
            "current_primary": item["primary_test"],
            "keywordEn_full": item["keywordEn"],
            "h1": item["h1"],
        }
    )
for item in INV["without_keywordEn"]:
    if item["slug"] in SKIP_SLUGS:
        continue
    primary = item.get("inferred_primary") or item.get("narr") or item["slug"].replace("-", " ")
    primary = clean_primary(primary)
    if ZH_ONLY.match(primary) or not primary:
        # fallback: English-looking part of h1/narr
        h1 = item.get("h1") or ""
        m = re.search(r"[A-Za-z][A-Za-z0-9 +/&-]{2,}", h1)
        primary = m.group(0).strip(" /") if m else item["slug"].replace("-", " ")
    rows.append(
        {
            "slug": item["slug"],
            "path": item["path"],
            "current_primary": primary,
            "keywordEn_full": item.get("narr") or "",
            "h1": item.get("h1") or "",
        }
    )

# cluster by path prefix
CLUSTER = {
    "agent": [],
    "video": [],
    "image_3d": [],
    "voice_coding": [],
    "edu_hr_health": [],
    "mkt_design_text": [],
    "llm_infra_web": [],
    "cms_builder_misc": [],
}


def assign(row: dict) -> str:
    p = row["path"]
    slug = row["slug"]
    if "/agent/" in p or slug in {
        "agent-billing",
        "agentic-commerce",
        "agentic-payments",
        "vibe-coding-payments",
        "ai-shopping",
        "data-engineering-agent",
        "world-model",
    }:
        return "agent"
    if "/video/" in p:
        return "video"
    if "/image/" in p or "/3d-spatial/" in p:
        return "image_3d"
    if "/voice-audio/" in p or "/coding/" in p:
        return "voice_coding"
    if "/education/" in p or "/hr-recruiting/" in p or "/healthcare/" in p or "/productivity/" in p:
        return "edu_hr_health"
    if "/marketing-growth/" in p or "/design/" in p or "/text-content/" in p:
        return "mkt_design_text"
    if "/llm/" in p or "/infrastructure/" in p or "/web-data/" in p or "/search-geo/" in p or "/enterprise-knowledge/" in p:
        return "llm_infra_web"
    return "cms_builder_misc"


for row in rows:
    CLUSTER[assign(row)].append(row)

index = []
for name, items in CLUSTER.items():
    items = sorted(items, key=lambda x: x["slug"])
    fp = OUT_DIR / f"{name}.json"
    fp.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    index.append({"batch": name, "count": len(items), "file": str(fp), "slugs": [i["slug"] for i in items]})

summary = {"total": len(rows), "batches": index}
(OUT_DIR / "index.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v["count"] for k, v in zip([b["batch"] for b in index], index)}, indent=2))
print("TOTAL", len(rows))
for b in index:
    print(f"{b['batch']:20} {b['count']:3}")
