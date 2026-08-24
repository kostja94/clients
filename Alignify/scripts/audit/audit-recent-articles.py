#!/usr/bin/env python3
"""Review recent tool articles vs KB."""
import json
import re
from pathlib import Path

DEPLOY = Path(r"d:\部署项目\alignify-by-kostja")
KB = Path(r"D:\项目文档\Alignify项目上下文\knowledge\tools")
SLUGS = ["chatbot", "headless-browser", "filmmaking", "search-engine", "web-search-api"]

GENERIC = re.compile(
    r"(?i)includes a selection framework|this guide compares|especially useful for|Determine Your Purpose|across teams and production"
)


def review_slug(slug):
    issues = []
    en = DEPLOY / "content/tools/en" / f"{slug}.json"
    zh = DEPLOY / "content/tools/zh" / f"{slug}.json"
    kb = KB / f"{slug}.md"
    if not en.exists():
        return {"slug": slug, "severity": "P0", "issues": ["EN JSON 缺失"]}
    art = json.loads(en.read_text(encoding="utf-8"))
    tldr = next((b for b in art.get("blocks", []) if b.get("type") == "tldr"), None)
    if not tldr:
        issues.append(("P0", "无 TLDR block"))
    else:
        blob = json.dumps(tldr, ensure_ascii=False)
        if GENERIC.search(blob):
            issues.append(("P1", "TLDR 模板化措辞"))
        if len(tldr.get("items", [])) < 4:
            issues.append(("P1", "TLDR items 不足 4 条"))
        intro = tldr.get("introduction", "")
        if len(intro) < 80:
            issues.append(("P2", "TLDR introduction 过短"))
        if "..." in blob:
            issues.append(("P1", "TLDR 含截断省略号"))
    layout = art.get("blogLayout", {})
    if not layout.get("pageUrl"):
        issues.append(("P0", "缺 pageUrl"))
    if not layout.get("excerpt"):
        issues.append(("P1", "缺 excerpt"))
    if not zh.exists():
        issues.append(("P1", "ZH JSON 缺失"))
    if not kb.exists():
        issues.append(("P0", "KB 缺失"))
    else:
        kb_text = kb.read_text(encoding="utf-8")
        products = re.findall(r"\*\*[^*]+\*\*", kb_text)
        named = re.findall(r"(Intercom|Perplexity|Browserbase|Google Flow|LTX|Brave|Tavily)", blob if tldr else "")
        if tldr and len(named) < 2:
            issues.append(("P2", "TLDR 未充分引用 KB 代表产品"))
    sev = "OK"
    if any(s == "P0" for s, _ in issues):
        sev = "P0"
    elif any(s == "P1" for s, _ in issues):
        sev = "P1"
    elif issues:
        sev = "P2"
    return {"slug": slug, "severity": sev, "modified": layout.get("modifiedDate"), "route": layout.get("pageUrl"), "issues": issues}


if __name__ == "__main__":
    for slug in SLUGS:
        r = review_slug(slug)
        print(f"\n=== {slug} [{r['severity']}] ===")
        print(f"route: {r.get('route')} modified: {r.get('modified')}")
        for sev, msg in r.get("issues", []):
            print(f"  {sev}: {msg}")
