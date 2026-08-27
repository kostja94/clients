#!/usr/bin/env python3
"""Lightweight locale/voice audit for Alignify blog/marketing/tools md."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CLIENTS = Path(__file__).resolve().parents[2]  # e:/clients/Alignify
GLOSSARY = CLIENTS / "skills/create-article/rules/locale-glossary.json"
PROD = Path(r"E:/自有部署项目/alignify production")
ZH_CHANNELS = ("blog", "marketing", "tools")

# Abbreviations / tokens allowed as bare Latin in ZH prose
ZH_LATIN_ALLOW = re.compile(
    r"^(?:AI|SEO|API|SaaS|PLG|GTM|KPI|FAQ|EU|MP4|PNG|WAV|TTS|LLM|URL|CTA|SKU|LTD|ARR|DAU|UX|UI|CLI|IDE|Pro|Plus|Ultra|Standard|Creator|Lite|Help|Settings|Toggle|USD|min|Art\.50)$",
    re.I,
)


def strip_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3 :].strip(), text[: end + 3]
    return text.strip(), ""


def extract_frontmatter_description(fm: str) -> str:
    m = re.search(r"^description:\s*[\"']?(.+?)[\"']?\s*$", fm, re.M)
    return m.group(1) if m else ""


def han_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def en_word_count(text: str) -> int:
    body = strip_frontmatter(text)[0]
    body = re.sub(r"```[\s\S]*?```", "", body)
    body = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", body)
    return len(re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?", body))


def mask_exempt_zones(text: str) -> str:
    """Mask URLs, code, anchor ids, inline backticks, markdown links."""
    out = text
    out = re.sub(r"\[([^\]]*)\]\([^\)]+\)", r"\1", out)
    out = re.sub(r"https?://[^\s)>\]]+", " ", out)
    out = re.sub(r"`[^`]+`", " ", out)
    out = re.sub(r"\{#([^}]+)\}", " ", out)
    out = re.sub(r"<!--[^>]*-->", " ", out)
    return out


def audit_zh_naked_loanwords(body: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    masked = mask_exempt_zones(body)
    masked_lower = masked.lower()

    for en_key, zh_val in glossary.get("localize_required", {}).items():
        if en_key.lower() in masked_lower:
            issues.append(
                f"ZH uses English phrase '{en_key}'; use '{zh_val}' "
                "(locale-glossary.json localize_required · zh-en-mixing.md)"
            )

    loanwords = {
        **glossary.get("naked_loanwords_zh", {}),
        **glossary.get("naked_loanwords_zh_gate_as_word", {}),
    }
    for word, zh_val in loanwords.items():
        pattern = rf"(?<![A-Za-z]){re.escape(word)}(?![A-Za-z])"
        if re.search(pattern, masked, re.I):
            issues.append(
                f"ZH naked loanword '{word}'; use '{zh_val}' "
                "(zh-en-mixing.md · naked_loanwords_zh)"
            )

    return issues


def audit_zh_regex(body: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    masked = mask_exempt_zones(body)
    for entry in glossary.get("forbidden_regex_zh", []):
        pattern = entry.get("pattern", "")
        if pattern and re.search(pattern, masked):
            hint = entry.get("hint", "")
            issues.append(
                f"ZH forbidden regex /{pattern}/"
                + (f"; {hint}" if hint else "")
                + " (zh-en-mixing.md · gtm-prose-voice.md)"
            )
    return issues


def audit_zh_forbidden_literals(body: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    for bad in glossary.get("forbidden_in_zh", []):
        if bad.replace(" X ", " ") in body or bad in body:
            issues.append(f"ZH forbidden pattern: {bad} (gtm-prose-voice.md)")
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


def audit_zh_description(desc: str, glossary: dict) -> list[str]:
    if not desc:
        return []
    return (
        audit_zh_naked_loanwords(desc, glossary)
        + audit_zh_regex(desc, glossary)
        + audit_zh_forbidden_literals(desc, glossary)
    )


def audit_zh(text: str, glossary: dict, channel: str = "blog") -> list[str]:
    issues: list[str] = []
    body, fm = strip_frontmatter(text)
    desc = extract_frontmatter_description(fm)
    if desc:
        issues.extend(f"[description] {x}" for x in audit_zh_description(desc, glossary))

    strategy = channel in ("blog", "marketing")
    if strategy and han_count(body) < 1200:
        issues.append(f"ZH han chars low ({han_count(body)}); check depth not padding")
    if body.count("→") >= 3:
        issues.append("ZH body uses arrow chains (→); rewrite as prose")
    issues.extend(audit_zh_forbidden_literals(body, glossary))
    issues.extend(audit_zh_regex(body, glossary))
    issues.extend(audit_zh_naked_loanwords(body, glossary))
    if strategy and not re.search(r"(我|我的判断|我认为|我会)", body):
        issues.append("ZH missing Kostja first-person judgment (我/我认为)")
    return issues


def audit_en(text: str, glossary: dict) -> list[str]:
    issues: list[str] = []
    body = strip_frontmatter(text)[0]
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


def resolve_channel_slug(slug: str, channel: str) -> tuple[str, str]:
    if channel != "auto":
        return channel, slug
    for ch in ZH_CHANNELS:
        if (PROD / f"content/{ch}/zh/{slug}.md").exists():
            return ch, slug
    return "blog", slug


def discover_all_zh_slugs() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for ch in ZH_CHANNELS:
        d = PROD / f"content/{ch}/zh"
        if d.is_dir():
            for p in sorted(d.glob("*.md")):
                found.append((ch, p.stem))
    return found


def audit_slug(
    slug: str, channel: str, glossary: dict, zh_only: bool = False
) -> list[str]:
    channel, slug = resolve_channel_slug(slug, channel)
    zh_path = PROD / f"content/{channel}/zh/{slug}.md"
    en_path = PROD / f"content/{channel}/en/{slug}.md"
    all_issues: list[str] = []

    if zh_path.exists():
        zh = zh_path.read_text(encoding="utf-8")
        all_issues.extend(f"[zh] {x}" for x in audit_zh(zh, glossary, channel))
    else:
        all_issues.append(f"[zh] missing {zh_path}")

    if not zh_only and en_path.exists():
        en = en_path.read_text(encoding="utf-8")
        all_issues.extend(f"[en] {x}" for x in audit_en(en, glossary))
    elif not zh_only and not en_path.exists():
        all_issues.append(f"[en] missing {en_path}")

    return all_issues


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", help="Single slug to audit")
    p.add_argument(
        "--channel",
        default="auto",
        choices=["blog", "marketing", "tools", "auto"],
    )
    p.add_argument(
        "--batch",
        choices=["gtm", "all-zh"],
        help="gtm = GTM cluster; all-zh = every content/*/zh/*.md",
    )
    p.add_argument("--zh-only", action="store_true", help="Skip EN audit")
    args = p.parse_args()

    if not args.slug and not args.batch:
        p.error("Provide --slug or --batch gtm|all-zh")

    glossary_path = GLOSSARY
    if not glossary_path.is_file():
        print(f"FAIL\nmissing glossary {glossary_path}")
        return 1
    glossary = json.loads(glossary_path.read_text(encoding="utf-8"))

    targets: list[tuple[str, str]] = []
    if args.batch == "gtm":
        for slug in glossary.get("gtm_batch_slugs", []):
            ch, slug = resolve_channel_slug(slug, "auto")
            targets.append((ch, slug))
    elif args.batch == "all-zh":
        targets = discover_all_zh_slugs()
    elif args.slug:
        ch, slug = resolve_channel_slug(args.slug, args.channel)
        targets = [(ch, slug)]

    failed = False
    passed = 0
    for ch, slug in targets:
        issues = audit_slug(slug, ch, glossary, zh_only=args.zh_only)
        if issues:
            failed = True
            print(f"=== [{ch}] {slug} ===")
            print("FAIL")
            for i in issues:
                print(i)
            print()
        else:
            passed += 1
            if args.batch:
                print(f"=== [{ch}] {slug} === PASS")

    if args.batch == "all-zh":
        print(f"\nSUMMARY: PASS {passed} / FAIL {len(targets) - passed} / TOTAL {len(targets)}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
