import yaml
from pathlib import Path

root = Path(r"E:\客户部署项目\luciusai-blog\content\blog\zh")
suffix = "适合正在评估 AI 员工与自动化落地路径的团队阅读。"

for p in sorted(root.glob("*.md")):
    raw = p.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        continue
    parts = raw.split("---", 2)
    fm = yaml.safe_load(parts[1]) or {}
    desc = fm.get("description", "")
    if len(desc) >= 80:
        continue
    new_desc = desc.rstrip("。") + "。" + suffix
    while len(new_desc) < 80:
        new_desc += "。"
    fm["description"] = new_desc[:320]
    new_fm = yaml.dump(fm, allow_unicode=True, sort_keys=False).strip()
    new_raw = f"---\n{new_fm}\n---{parts[2]}"
    p.write_text(new_raw, encoding="utf-8", newline="\n")
    print(p.name, len(desc), "->", len(fm["description"]))
