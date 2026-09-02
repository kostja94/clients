#!/usr/bin/env python3
import json
import re

with open("e:/clients/temp/zh_localization_audit.json", encoding="utf-8") as f:
    data = json.load(f)

# add museon from separate run
import sys
sys.path.insert(0, "e:/clients/temp")
from audit_zh_localization import audit_page
for i,p in enumerate(data):
    if "museon" in p.get("url","") and "error" in p:
        data[i] = audit_page("/zh/case-studies/museon")

SKIP = {"image/png","index, follow","width=device-width, initial-scale=1","Lucius AI"}

for page in data:
    if "error" in page:
        print("ERROR", page["url"], page["error"])
        continue
    path = page["url"].replace("https://luciusai.com","")
    if path.startswith("/zh/docs/") and path != "/zh/docs":
        continue  # skip duplicate docs subpages
    issues = []
    for i in page["issues"]:
        t = i["text"]
        if t in SKIP: continue
        if i["category"]=="meta" and t.startswith("Lucius AI 产品"): continue
        if i["severity"]=="低": continue
        # include if pure english chunk or heading/meta/nav
        pure_en = not re.search(r"[\u4e00-\u9fff]", t)
        mixed_heading = i["category"] in ("标题","CTA/按钮","导航","页脚") and re.search(r"[A-Za-z]{2,}", t)
        if pure_en or mixed_heading or (i["category"]=="meta" and "teammates" in t):
            issues.append(i)
    if not issues and path.startswith("/zh/docs"):
        # docs always has issues
        issues = [i for i in page["issues"] if i["severity"]=="高"]
    print("\n" + "="*60)
    print(path)
    print("title:", page["title"])
    for i in issues:
        print(f"  [{i['severity']}] {i['category']}: {t if (t:=i['text']) else ''}")
