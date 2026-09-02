import re
import pathlib

root = pathlib.Path(r"E:\客户部署项目\luciusai-blog\content\blog\zh")
for f in sorted(root.glob("*.md")):
    text = f.read_text(encoding="utf-8")
    m = re.search(r'^description:\s*"(.*?)"', text, re.M)
    if m:
        d = m.group(1)
        print(f"{len(d):3d} {f.name}")
