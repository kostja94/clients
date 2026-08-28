#!/usr/bin/env python3
"""Analyze article categories across all channels."""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

DEPLOY = Path(r"E:\自有部署项目\alignify production")
VALID = {
    "ai-video", "ai-audio", "ai-creative", "ai-text", "coding-dev",
    "ai-agents", "data-infra", "business", "seo", "geo", "marketing", "insights",
}


def parse_fm(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    fm = text[3:end]
    d = {}
    for line in fm.splitlines():
        m = re.match(r'^(\w+):\s*"(.*)"\s*$', line.strip())
        if m:
            d[m.group(1)] = m.group(2)
        else:
            m2 = re.match(r"^(\w+):\s*(.+)\s*$", line.strip())
            if m2:
                d[m2.group(1)] = m2.group(2).strip()
    return d


articles = []
for ch in ["blog", "tools", "seo", "marketing", "insights", "events"]:
    en_dir = DEPLOY / "content" / ch / "en"
    if not en_dir.exists():
        continue
    for md in sorted(en_dir.glob("*.md")):
        fm = parse_fm(md)
        slug = fm.get("slug", md.stem)
        cat = fm.get("category", "(missing)")
        sec = fm.get("categorySecondary", "") or ""
        articles.append({
            "channel": ch,
            "slug": slug,
            "category": cat,
            "secondary": sec,
            "title": (fm.get("title") or "")[:70],
        })

by_cat = Counter(a["category"] for a in articles)
by_channel = defaultdict(list)
for a in articles:
    by_channel[a["channel"]].append(a)

invalid_sec = [a for a in articles if a["secondary"] and a["secondary"] not in VALID]
invalid_cat = [a for a in articles if a["category"] not in VALID and a["category"] != "(missing)"]

# Load blog-pages-config hub assignments (simple grep)
blog_config = (DEPLOY / "src/data/blog-pages-config.ts").read_text(encoding="utf-8")
blog_hubs = {}
for m in re.finditer(
    r'slug:\s*"([^"]+)"[\s\S]*?(?:toolsHubCategory:\s*"([^"]+)"|marketingHubCategory:\s*"([^"]+)")',
    blog_config,
):
    slug = m.group(1)
    hub = m.group(2) or m.group(3) or ""
    blog_hubs[slug] = hub

print(json.dumps({
    "total": len(articles),
    "by_channel_count": {ch: len(v) for ch, v in by_channel.items()},
    "primary_category": dict(by_cat.most_common()),
    "invalid_secondary": invalid_sec,
    "invalid_primary": invalid_cat,
    "blog_articles": [
        {**a, "hubGroup": blog_hubs.get(a["slug"], "")}
        for a in articles if a["channel"] == "blog"
    ],
    "tools_by_category": dict(Counter(a["category"] for a in articles if a["channel"] == "tools").most_common()),
}, ensure_ascii=False, indent=2))
