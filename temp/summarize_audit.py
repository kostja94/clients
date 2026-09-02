#!/usr/bin/env python3
import json

with open(r"e:\clients\temp\lucius_zh_audit.json", encoding="utf-8") as f:
    data = json.load(f)

SITE_JS_NAV_FOOTER_ZH = [
    ("nav", "Agents", "roles"),
    ("nav", "Lucius Agents", "roleSystem"),
    ("nav", "Customer Support", "customerSupport"),
    ("nav", "Community Operator", "support"),
    ("nav", "Moderator", "moderator"),
    ("nav", "Email Assistant", "emailSupport"),
    ("nav", "Website", "website"),
    ("nav", "Discover", "discover"),
    ("nav", "Discord", "hardcoded"),
    ("nav", "Telegram", "hardcoded"),
    ("nav", "Lark", "hardcoded"),
    ("nav", "Slack", "hardcoded"),
    ("nav", "Email", "hardcoded"),
    ("nav", "WhatsApp", "hardcoded"),
    ("footer", "Discord", "hardcoded"),
    ("footer", "Slack", "hardcoded"),
    ("footer", "Telegram", "hardcoded"),
    ("footer", "Lark", "hardcoded"),
    ("footer", "Email", "hardcoded"),
    ("footer", "WhatsApp", "hardcoded"),
    ("footer", "Website", "website"),
    ("footer", "Discover", "discover"),
    ("footer", "Utell · AI Tool", "hardcoded"),
    ("footer", "Museon · KOL Operations", "hardcoded"),
    ("footer", "Jarsy · Financial Product", "hardcoded"),
    ("footer", "Moderator · 垃圾信息防护", "spamCase partial"),
]

for path, d in sorted(data.items()):
    print("\n" + "=" * 60)
    print(path)
    meta = d.get("meta", {})
    if meta.get("title_en"):
        print("META title:", meta.get("title"))
    if meta.get("description_en"):
        print("META desc:", meta.get("description"))
    hs = [h for h in d.get("body", {}).get("english_headings", []) if not h.startswith("${")]
    if hs:
        print("HEADINGS:", hs)
    phrases = d.get("body", {}).get("english_phrases", [])
    if phrases:
        print("PHRASES:", phrases)
    ctas = d.get("cta", {}).get("english", [])
    if ctas:
        print("CTAS:", ctas)
    lines = d.get("body", {}).get("english_lines_sample", [])
    if lines:
        print("BODY EN SAMPLES:")
        for ln in lines[:5]:
            print(" -", ln[:120])

print("\n\nSITE.JS GLOBAL NAV/FOOTER ISSUES (all zh pages):")
for cat, text, key in SITE_JS_NAV_FOOTER_ZH:
    print(f"  [{cat}] {text} ({key})")
