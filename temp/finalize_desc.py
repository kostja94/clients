import re
from pathlib import Path

ROOT = Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
PAD = "含 Lucius 实践建议与落地边界。"

for path in sorted(ROOT.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    m = re.search(r'^description:\s*"(.*?)"', text, re.M)
    if not m:
        continue
    desc = m.group(1)
    while "（含 Lucius 实践建议）" in desc:
        desc = desc.replace("（含 Lucius 实践建议）", "")
    desc = desc.rstrip("。") + "。" if desc and not desc.endswith("。") else desc
    while len(desc) < 80:
        desc = desc.rstrip("。") + "。" + PAD
    if len(desc) > 320:
        desc = desc[:317] + "..."
    new_text, c = re.subn(
        r'^description:\s*".*?"',
        f'description: "{desc}"',
        text,
        1,
        re.M,
    )
    if c != 1:
        print("FAIL", path.name)
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"{len(desc):3d} {path.name}")
