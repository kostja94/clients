import re
import pathlib

ROOT = pathlib.Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
for path in sorted(ROOT.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    m = re.search(r'^description:\s*"(.*?)"', text, re.M)
    if not m:
        print(f"NO DESC {path.name}")
        continue
    desc = m.group(1)
    n = len(desc)
    status = "OK" if n >= 80 else "SHORT"
    if n < 80:
        print(f"{status} {n:3d} {path.name}")
