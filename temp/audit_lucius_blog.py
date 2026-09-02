import json
import re
import yaml
from pathlib import Path

root = Path(r"E:\客户部署项目\luciusai-blog")
issues = []

cta = json.loads((root / "src/data/final-cta-data.json").read_text(encoding="utf-8"))["slugs"]
en_slugs = {p.stem for p in (root / "content/blog").glob("*.md")}

for s in sorted(en_slugs):
    e = cta.get(s, {})
    if not e.get("en") or not e.get("zh"):
        issues.append(f"CTA missing en/zh: {s}")

for slug in ["introducing-knockin", "how-to-use-knockin"]:
    for loc in ["", "zh/"]:
        p = root / f"content/blog/{loc}{slug}.md"
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        if fm.get("category") != "Knockin":
            issues.append(f"category not Knockin: {loc}{slug} -> {fm.get('category')}")
        if fm.get("author") != "Lucius Team":
            issues.append(f"author not Lucius Team: {loc}{slug}")

for p in (root / "content/blog/zh").glob("*.md"):
    fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
    d = fm.get("description", "")
    if len(d) < 80:
        issues.append(f"ZH desc <80: {p.name} ({len(d)})")

tldr = json.loads((root / "src/data/tldr-data.json").read_text(encoding="utf-8"))["pages"]
faq = json.loads((root / "src/data/faq-data.json").read_text(encoding="utf-8"))["pages"]
related = json.loads((root / "src/data/related-posts-data.json").read_text(encoding="utf-8"))["pages"]

for slug in en_slugs:
    for loc in ["", "zh/"]:
        prefix = "/zh/blog" if loc else "/blog"
        key = f"{prefix}/{slug}"
        if key not in tldr:
            issues.append(f"missing tldr: {key}")
        if key not in faq:
            issues.append(f"missing faq: {key}")

for slug in ["introducing-knockin", "how-to-use-knockin"]:
    for loc in ["", "zh/"]:
        key = f"{'/zh' if loc else ''}/blog/{slug}".replace("//", "/")
        if key not in related:
            issues.append(f"missing related: {key}")

pat = re.compile(r"\[luciusai\.com|\[Lucius\]\(https://|\[Book demo\]|读完本节|By the end of this section")
for p in (root / "content/blog").rglob("*.md"):
    if pat.search(p.read_text(encoding="utf-8")):
        issues.append(f"content pattern: {p.relative_to(root)}")

HEADING = re.compile(r"\s*\{#([a-z0-9-]+)\}\s*$", re.I)

def parse_heading(t):
    m = HEADING.search(t.strip())
    if m:
        return t.strip()[: m.start()].strip(), m.group(1).lower()
    return t.strip(), None

for line in (root / "content/blog/zh/how-to-use-knockin.md").read_text(encoding="utf-8").splitlines():
    if line.startswith("## "):
        title, aid = parse_heading(line[3:])
        if aid and "{" in title:
            issues.append(f"heading parse would fail: {line}")

print(f"ISSUES: {len(issues)}")
for i in issues:
    print("-", i)
print(f"Summary: {len(en_slugs)} EN slugs, {len(cta)} CTA entries, tldr keys {len(tldr)}, faq keys {len(faq)}")
