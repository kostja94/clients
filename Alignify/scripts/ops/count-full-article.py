#!/usr/bin/env python3
"""Full reader-facing word count: md body + TL;DR + FAQ + hero."""
import json
import re
import sys
from pathlib import Path


def strip_md_noise(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"<!--[\s\S]*?-->", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\s*\{#[^}]+\}", "", text)
    text = re.sub(r"[*_`<>/]", "", text)
    return text


def strip_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    return text[3:end], text[end + 3 :].strip()


def han(s: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", s))


def enw(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?", s))


def main() -> None:
    slug = sys.argv[1] if len(sys.argv) > 1 else "rate-limit-reset"
    root = Path(r"E:/自有部署项目/alignify production")
    tldr = json.loads((root / "src/data/tldr-data.json").read_text(encoding="utf-8"))["pages"]
    faq = json.loads((root / "src/data/faq-data.json").read_text(encoding="utf-8"))["pages"]

    for locale, tkey in [("zh", f"/zh/blog/{slug}"), ("en", f"/blog/{slug}")]:
        md = (root / f"content/blog/{locale}/{slug}.md").read_text(encoding="utf-8")
        fm, body = strip_frontmatter(md)
        hero = ""  # legacy: frontmatter heroHtml removed (E44); count body only

        t = tldr[tkey]
        t_text = t.get("introduction", "") + " " + " ".join(t.get("items", []))
        f_text = " ".join(i["question"] + " " + i["answer"] for i in faq[tkey]["items"])

        parts = {
            "body": strip_md_noise(body),
            "tldr": t_text,
            "faq": f_text,
            "hero": strip_md_noise(hero),
        }

        print(f"=== {locale} ===")
        if locale == "zh":
            totals = {"han": 0, "en": 0}
            for name, text in parts.items():
                h, e = han(text), enw(text)
                totals["han"] += h
                totals["en"] += e
                print(f"  {name}: {h} han + {e} latin")
            print(f"  TOTAL: {totals['han']} han + {totals['en']} latin = {totals['han']+totals['en']} units")
        else:
            total = 0
            for name, text in parts.items():
                w = enw(text)
                total += w
                print(f"  {name}: {w} words")
            print(f"  TOTAL: {total} words")
        print()


if __name__ == "__main__":
    main()
