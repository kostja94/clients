#!/usr/bin/env python3
"""Sync skills catalog from source repo to Alignify project.
Reads D:\部署项目\marketing-skills源文件\marketing-skills\skills\*.md
Generates src/data/skills-catalog.json
"""
import os, json, re, sys

SRC = r"D:\部署项目\marketing-skills源文件\marketing-skills\skills"
OUT = r"src\data\skills-catalog.json"

if not os.path.isdir(SRC):
    print(f"ERROR: {SRC} not found"); sys.exit(1)

cats = {}
for cat in sorted(os.listdir(SRC)):
    cp = os.path.join(SRC, cat)
    if not os.path.isdir(cp): continue
    skills = []
    for root, dirs, files in os.walk(cp):
        for f in files:
            if f != "SKILL.md": continue
            fp = os.path.join(root, f)
            content = open(fp, encoding='utf-8').read()
            m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not m: continue
            fm = m.group(1)
            nm = re.search(r'^name:\s*(.+)', fm, re.MULTILINE)
            name = nm.group(1).strip() if nm else os.path.basename(root)
            dm = re.search(r'^description:\s*(.+)', fm, re.MULTILINE)
            desc = dm.group(1).strip() if dm else ""
            vm = re.search(r'version:\s*([\d.]+)', fm, re.MULTILINE)
            ver = vm.group(1) if vm else "1.0.0"
            skills.append(dict(name=name, description=desc, version=ver, dir=os.path.basename(root)))
    if skills:
        cats[cat] = sorted(skills, key=lambda x: x["name"])

total = sum(len(v) for v in cats.values())
catalog = dict(total=total, categories=cats)
json.dump(catalog, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"OK: {total} skills in {len(cats)} categories -> {OUT}")
for c, s in sorted(cats.items()):
    print(f"  {c}: {len(s)}")
