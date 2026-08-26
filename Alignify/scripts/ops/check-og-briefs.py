#!/usr/bin/env python3
import re
from pathlib import Path

DEPLOY = Path(r"E:\自有部署项目\alignify production")
BRIEFS = Path(__file__).resolve().parents[2] / "data" / "og-briefs"

text = (DEPLOY / "src/data/tools-article-images.ts").read_text(encoding="utf-8")
all_tools = set(re.findall(r'"([a-z0-9-]+)":\s*`\$\{BASE\}', text))
tools_briefs = set(p.parent.name for p in (BRIEFS / "tools").rglob("brief.json"))
blog_briefs = set(p.parent.name for p in (BRIEFS / "blog").rglob("brief.json"))
blog_all = set(p.stem for p in (DEPLOY / "content/blog/en").glob("*.md"))

missing_tools = sorted(all_tools - tools_briefs)
extra_tools = sorted(tools_briefs - all_tools)
missing_blog = sorted(blog_all - blog_briefs)

print(f"tools: {len(tools_briefs)}/{len(all_tools)} briefs")
print(f"blog: {len(blog_briefs)}/{len(blog_all)} briefs")
if missing_tools:
    print("missing tools:", ",".join(missing_tools))
if extra_tools:
    print("extra tools briefs:", ",".join(extra_tools))
if missing_blog:
    print("missing blog:", ",".join(missing_blog))
