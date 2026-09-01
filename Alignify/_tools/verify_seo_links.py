#!/usr/bin/env python3
"""Verify SEO shell SSOT paths and scan for broken stub links."""
from __future__ import annotations

import re
from pathlib import Path

KB = Path(r"E:\个人知识库")
ALIGNIFY = Path(r"E:\clients\Alignify")
SEO_DIR = ALIGNIFY / "knowledge" / "seo"

STUB_LINK_TARGETS = [
    "Sitemap知识块-Sitemap-Knowledge.md",
    "Robots-txt知识块-Robots-Txt-Knowledge.md",
    "Schema知识块-Schema-Knowledge.md",
    "SERP特性知识块-SERP-Knowledge.md",
    "GTM知识块-GTM-Knowledge.md",
    "Meta标签-Meta-Tags.md",
    "HTML-a标签与链接属性-HTML-ATag.md",
    "HTML语义标签-HTML-Semantic-Tags.md",
    "网站结构与信息架构-Website-Structure.md",
    "SEO/_briefs/",
]

LEGACY = KB / "自然搜索-Organic-Search/SEO/_参考/Alignify-SEO分册README-legacy.md"


def main() -> None:
    broken_alignify: list[tuple[str, str]] = []
    for md in SEO_DIR.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"`(E:\\个人知识库[^`]+)`", text):
            target = m.group(1).split("#")[0]
            if not Path(target).exists():
                broken_alignify.append((str(md.relative_to(ALIGNIFY)), m.group(1)))

    broken_kb: list[tuple[str, str]] = []
    for md in KB.rglob("*.md"):
        if "_tools" in md.parts:
            continue
        if md.resolve() == LEGACY.resolve():
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        for stub in STUB_LINK_TARGETS:
            if stub in text and re.search(r"\][^\n]*" + re.escape(stub), text):
                broken_kb.append((str(md.relative_to(KB)), stub))

    # Alignify skills: knowledge/seo/_briefs must exist
    skills_broken: list[str] = []
    for md in (ALIGNIFY / "skills").rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"knowledge/seo/_briefs/([a-z0-9-]+\.md)", text):
            brief = SEO_DIR / "_briefs" / m.group(1)
            if not brief.exists():
                skills_broken.append(f"{md.relative_to(ALIGNIFY)} -> {m.group(0)}")

    print("=== Alignify broken SSOT absolute paths ===")
    print(len(broken_alignify))
    for item in broken_alignify:
        print(" ", item)

    print("=== Personal KB body links to deleted stubs (excl legacy) ===")
    print(len(broken_kb))
    for item in broken_kb:
        print(" ", item)

    print("=== Alignify skills broken brief paths ===")
    print(len(skills_broken))
    for item in skills_broken:
        print(" ", item)


if __name__ == "__main__":
    main()
