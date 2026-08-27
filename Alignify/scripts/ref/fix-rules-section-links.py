#!/usr/bin/env python3
"""Fix broken ../section/ links in skills/create-article/rules after content/ merge."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RULES = ROOT / "skills" / "create-article" / "rules"

REPLACEMENTS = [
    ("../section/section-consistency.md", "../copy-quality.md"),
    ("../section/section-meta-copy.md", "../meta.md"),
    ("../section/section-seo.md", "../meta.md"),
    ("../section/section-heading-best-practices.md", "../sections/generic.md"),
    ("../section/section-hero.md", "./bloglayout.md"),
    ("../section/section-tldr.md", "../sections/tldr.md"),
    ("../section/section-what-is.md", "../sections/what-is.md"),
    ("../section/section-how-it-works.md", "../sections/what-is.md"),
    ("../section/section-best-tools.md", "../sections/best-tools.md"),
    ("../section/section-comparison-table.md", "../sections/comparison-table.md"),
    ("../section/section-how-to.md", "../sections/how-to.md"),
    ("../section/section-faq.md", "../sections/faq.md"),
    ("../section/section-links.md", "../internal-links.md"),
    ("../section/section-references.md", "../sections/references.md"),
    ("../section/section-use-cases.md", "../sections/generic.md"),
    ("../section/section-content-import.md", "../README.md"),
    ("../section/section-optimization-playbook.md", "../README.md"),
    ("../section/section-generic.md", "../sections/generic.md"),
    ("../section/section-also-interested-in.md", "../sections/generic.md"),
    ("../section/README.md", "../README.md"),
    ("./template-tools.md", "./best-ranking.md"),
    ("./template-bloglayout.md", "./bloglayout.md"),
    ("./sections/content-rules/section-consistency.md", "../copy-quality.md"),
    ("content JSON（补充段落", "content Markdown（补充段落"),
    ("修改对应 content JSON", "修改对应 content Markdown"),
    ("Tldr 组件", "md `#article-intro` section"),
    ("HowItWorks", "md section"),
    ("BestTools 组件", "md Best 榜单 section"),
    ("UseCases", "md 应用场景 section"),
    ("FAQ 组件", "md `#faq` section"),
    ("References 组件", "md `#references` section"),
]

for fp in RULES.rglob("*.md"):
    text = fp.read_text(encoding="utf-8")
    orig = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != orig:
        fp.write_text(text, encoding="utf-8")
        print(f"fixed: {fp.relative_to(ROOT)}")

# ops
ops = ROOT / "skills" / "ops" / "gsc-optimization-plan.md"
if ops.exists():
    t = ops.read_text(encoding="utf-8")
    t2 = t.replace("../section/section-optimization-playbook.md", "../create-article/rules/README.md")
    t2 = t2.replace("content JSON", "content Markdown")
    if t2 != t:
        ops.write_text(t2, encoding="utf-8")
        print("fixed: skills/ops/gsc-optimization-plan.md")

print("Done.")
