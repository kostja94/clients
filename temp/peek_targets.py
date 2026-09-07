import json
from pathlib import Path

targets = [
    "3d-model-generator", "3d-modelling", "advertising-agent", "agent-for-desktop",
    "agent-memory", "agent-to-agent", "ai-scheduling", "api", "audio-translator",
    "avatar", "browser", "directory", "ecommerce-website-builder", "education",
    "healthcare", "image-to-video", "inference-infrastructure", "lip-sync",
    "llm-for-coding", "llm-for-math", "llm-for-reasoning", "memory",
    "multimodal-llm", "religion", "short-drama", "social-cards-generator",
    "text-to-video", "text-translator", "video-clipping", "video-translator",
    "web-fetch", "workflow",
]

inv = json.loads(Path(r"e:/clients/temp/kw-audit-batches/full_kb_inventory.json").read_text(encoding="utf-8"))
by_slug = {}
for grp in ("with_keywordEn", "without_keywordEn"):
    for it in inv[grp]:
        by_slug[it["slug"]] = it

KB = Path(r"e:/clients/Alignify/knowledge")
for t in targets:
    it = by_slug.get(t)
    if not it:
        print(f"{t}: NO INVENTORY ENTRY")
        continue
    p = KB / it["path"]
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    print(f"===== {t}  ({it['path']})  has_keywordEn={it['has_keywordEn']}")
    for i in range(min(len(lines), 10)):
        if lines[i].strip():
            print(f"{i+1}| {lines[i][:220]}")
    print()
