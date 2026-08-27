#!/usr/bin/env python3
"""Lightweight locale/voice audit for Alignify blog/marketing md."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CLIENTS = Path(__file__).resolve().parents[2]  # e:/clients/Alignify
GLOSSARY = CLIENTS / "skills/create-article/rules/locale-glossary.json"
PROD = Path(r"E:/自有部署项目/alignify production")


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3 :].strip()
    return text.strip()


def han_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def en_word_count(text: str) -> int:
    body = strip_frontmatter(text)
    body = re.sub(r"```[\s\S]*?```", "", body)
    body = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", body)
    return len(re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?", body))


def audit_zh_localize(body: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    body_lower = body.lower()
    for en_key, zh_val in glossary.get("localize_required", {}).items():
        if en_key.lower() in body_lower:
            issues.append(
                f"ZH uses English phrase '{en_key}'; use '{zh_val}' "
                "(locale-glossary.json localize_required)"
            )
    return issues


def audit_zh_regex(body: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    for entry in glossary.get("forbidden_regex_zh", []):
        pattern = entry.get("pattern", "")
        if pattern and re.search(pattern, body):
            hint = entry.get("hint", "")
            issues.append(
                f"ZH forbidden regex /{pattern}/"
                + (f"; {hint}" if hint else "")
                + " (gtm-prose-voice.md)"
            )
    return issues


def audit_en_regex(body: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    for entry in glossary.get("forbidden_regex_en", []):
        pattern = entry.get("pattern", "")
        if pattern and re.search(pattern, body):
            hint = entry.get("hint", "")
            issues.append(
                f"EN forbidden regex /{pattern}/"
                + (f"; {hint}" if hint else "")
                + " (gtm-prose-voice.md)"
            )
    return issues


def audit_zh(text: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    body = strip_frontmatter(text)
    if han_count(body) < 1200:
        issues.append(f"ZH han chars low ({han_count(body)}); check depth not padding")
    if body.count("→") >= 3:
        issues.append("ZH body uses arrow chains (→); rewrite as prose")
    for bad in glossary.get("forbidden_in_zh", []):
        if bad.replace(" X ", " ") in body or bad in body:
            issues.append(f"ZH forbidden pattern: {bad} (gtm-prose-voice.md)")
    issues.extend(audit_zh_regex(body, glossary))
    issues.extend(audit_zh_localize(body, glossary))
    if not re.search(r"(我|我的判断|我认为|我会)", body):
        issues.append("ZH missing Kostja first-person judgment (我/我认为)")
    return issues


def audit_en(text: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    body = strip_frontmatter(text)
    wc = en_word_count(text)
    if wc < 900:
        issues.append(f"EN word count low ({wc}); check depth not padding")
    if body.count("→") >= 2:
        issues.append("EN body uses →; rewrite as full sentences")
    for bad in glossary.get("forbidden_in_en", []):
        if bad in body:
            issues.append(f"EN forbidden pattern: {bad} (gtm-prose-voice.md)")
    issues.extend(audit_en_regex(body, glossary))
    if not re.search(r"\bI\b|\bmy read\b|\bI think\b", body, re.I):
        issues.append("EN missing first-person author voice (I / my read)")
    short = len(re.findall(r"(?<=[.!?])\s+[A-Z][a-z]+[^.!?]{0,25}[.!?]", body))
    if short > 15:
        issues.append("EN has many very short sentences; check telegraphic tone")
    return issues


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--channel", default="blog", choices=["blog", "marketing"])
    args = p.parse_args()

    glossary_path = GLOSSARY
    if not glossary_path.is_file():
        print(f"FAIL\nmissing glossary {glossary_path}")
        return 1
    glossary = json.loads(glossary_path.read_text(encoding="utf-8"))

    zh_path = PROD / f"content/{args.channel}/zh/{args.slug}.md"
    en_path = PROD / f"content/{args.channel}/en/{args.slug}.md"
    all_issues: list[str] = []

    if zh_path.exists():
        zh = zh_path.read_text(encoding="utf-8")
        all_issues.extend(f"[zh] {x}" for x in audit_zh(zh, glossary))
    else:
        all_issues.append(f"[zh] missing {zh_path}")

    if en_path.exists():
        en = en_path.read_text(encoding="utf-8")
        all_issues.extend(f"[en] {x}" for x in audit_en(en, glossary))
    else:
        all_issues.append(f"[en] missing {en_path}")

    if all_issues:
        print("FAIL")
        for i in all_issues:
            print(i)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
