#!/usr/bin/env python3
from pathlib import Path
import re

d = Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
for p in sorted(d.glob("*.md")):
    t = p.read_text(encoding="utf-8")
    m = re.search(r'description:\s*"([^"]+)"', t)
    desc = m.group(1) if m else ""
    l = len(desc)
    pri = "P0" if l < 60 else ("P1" if l > 80 else "OK")
    print(f"{l:3d} {pri:2s} {p.stem}")
