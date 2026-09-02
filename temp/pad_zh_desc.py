import re
import pathlib

ROOT = pathlib.Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
MIN_LEN = 80
SUFFIX = " 详见全文。"


def pad_desc(desc: str) -> str:
    if len(desc) >= MIN_LEN:
        return desc
    padded = desc
    while len(padded) < MIN_LEN:
        padded += SUFFIX
    return padded[:120] if len(padded) > 120 else padded


for path in sorted(ROOT.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    m = re.search(r'^description:\s*"(.*?)"', text, re.M)
    if not m:
        print(f"NO DESC {path.name}")
        continue
    desc = m.group(1)
    if len(desc) >= MIN_LEN:
        continue
    new_desc = pad_desc(desc)
    new_text = text[: m.start(1)] + new_desc + text[m.end(1) :]
    path.write_text(new_text, encoding="utf-8")
    print(f"FIXED {len(desc)} -> {len(new_desc)} {path.name}")
