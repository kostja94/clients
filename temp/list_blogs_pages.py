#!/usr/bin/env python3
import re
import urllib.request
from pathlib import Path

req = urllib.request.Request(
    "https://medo.dev/blogs/", headers={"User-Agent": "MeDoAudit/1.0"}
)
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode("utf-8", errors="replace")

live = sorted({s for s in re.findall(r'href="/blogs/([^"/?#]+)"', html) if s != "blogs"})

content = Path(r"E:\客户部署项目\medo-blog\content\blog")
local_ed = {p.stem for p in content.glob("*.md")}

print(f"LIVE /blogs/ COUNT: {len(live)}\n")
for i, slug in enumerate(live, 1):
    synced = "Y" if slug in local_ed else "N"
    print(f"{i:2}. https://medo.dev/blogs/{slug}/  [medo-blog: {synced}]")
