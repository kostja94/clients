#!/usr/bin/env python3
"""Local audit for luciusai-blog zh localization."""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(r"E:/客户部署项目/luciusai-blog")
ZH_DIR = ROOT / "content/blog/zh"
EN_DIR = ROOT / "content/blog"

EN_PREFIX = re.compile(
    r"^(Introducing|How to|Build your own|Automate|What is|What Is|Agentic|Human in the Loop)",
    re.I,
)
EN_TITLE = re.compile(r"^[A-Za-z][A-Za-z0-9 ,\-']{6,}[：:]")
DESC_MIN = 60
DESC_MAX = 80


def parse_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    body_start = end + 3
    fm_text = text[3:end]
    if yaml:
        fm = yaml.safe_load(fm_text) or {}
    else:
        fm = {}
        for line in fm_text.splitlines():
            m = re.match(r'^(\w+):\s*"(.*)"\s*$', line.strip())
            if m:
                fm[m.group(1)] = m.group(2)
    return fm, text[body_start:].lstrip("\n")


def main():
    issues: list[dict] = []

    chrome = (ROOT / "src/chrome/site-chrome.ts").read_text(encoding="utf-8")
    for label in ["Features", "Pricing", "Docs", "Privacy", "Terms", "DPA"]:
        if f'label: "{label}"' in chrome:
            issues.append(
                {
                    "category": "Chrome",
                    "file": "site-chrome.ts",
                    "detail": label,
                    "priority": "P0",
                    "note": "English label",
                }
            )

    zh_slugs = sorted(p.stem for p in ZH_DIR.glob("*.md"))
    en_slugs = set(
        p.stem for p in EN_DIR.glob("*.md") if p.parent.name != "zh"
    )

    for slug in zh_slugs:
        p = ZH_DIR / f"{slug}.md"
        text = p.read_text(encoding="utf-8")
        fm, body = parse_fm(text)
        title = fm.get("title", "")
        desc = fm.get("description", "")

        if slug not in en_slugs:
            issues.append(
                {
                    "category": "Parity",
                    "file": slug,
                    "detail": "missing en",
                    "priority": "P0",
                    "note": "",
                }
            )

        if EN_PREFIX.search(title) or EN_TITLE.match(title):
            issues.append(
                {
                    "category": "Title",
                    "file": slug,
                    "detail": title[:70],
                    "priority": "P0",
                    "note": "English prefix",
                }
            )

        dlen = len(desc)
        if dlen < DESC_MIN:
            issues.append(
                {
                    "category": "Description",
                    "file": slug,
                    "detail": f"len={dlen}",
                    "priority": "P0",
                    "note": desc[:60],
                }
            )
        elif dlen > DESC_MAX:
            issues.append(
                {
                    "category": "Description",
                    "file": slug,
                    "detail": f"len={dlen}",
                    "priority": "P1",
                    "note": desc[:60],
                }
            )

        for pat, label in [
            (r"\bIntroducing\b", "Introducing"),
            (r"Build your own", "Build your own"),
        ]:
            if re.search(pat, body, re.I):
                issues.append(
                    {
                        "category": "Body",
                        "file": slug,
                        "detail": label,
                        "priority": "P1",
                        "note": "",
                    }
                )

    # JSON
    for fname in ["tldr-data.json", "faq-data.json"]:
        fp = ROOT / "src/data" / fname
        data = json.loads(fp.read_text(encoding="utf-8"))
        for key, val in data.items():
            if not str(key).startswith("/zh/blog"):
                continue
            if not isinstance(val, dict):
                continue
            intro = val.get("introduction") or val.get("intro") or ""
            if intro and not re.search(r"[\u4e00-\u9fff]", intro[:30]):
                issues.append(
                    {
                        "category": "JSON",
                        "file": fname,
                        "detail": key,
                        "priority": "P0",
                        "note": intro[:50],
                    }
                )
            items = val.get("items") or val.get("faqs") or []
            for i, item in enumerate(items):
                for field in ("title", "question", "answer", "content"):
                    txt = item.get(field, "")
                    if txt and re.match(
                        r"^(How|What|Why|When|Build|Introducing|Automate)", txt, re.I
                    ):
                        issues.append(
                            {
                                "category": "JSON",
                                "file": fname,
                                "detail": f"{key} [{field}]",
                                "priority": "P1",
                                "note": txt[:50],
                            }
                        )

    rp = ROOT / "src/data/related-posts-data.json"
    rp_data = json.loads(rp.read_text(encoding="utf-8"))
    for key, slugs in rp_data.items():
        if not str(key).startswith("/zh/blog"):
            continue
        for s in slugs if isinstance(slugs, list) else []:
            slug = s if isinstance(s, str) else s.get("slug", "")
            slug = slug.replace("/zh/blog/", "").replace("/blog/", "")
            if slug and slug not in zh_slugs:
                issues.append(
                    {
                        "category": "Related",
                        "file": key,
                        "detail": slug,
                        "priority": "P0",
                        "note": "invalid slug",
                    }
                )

    out = Path(r"E:/clients/temp/lucius_blog_local_audit.json")
    out.write_text(json.dumps(issues, ensure_ascii=False, indent=2), encoding="utf-8")

    from collections import Counter

    print(f"ZH: {len(zh_slugs)} EN: {len(en_slugs)} Issues: {len(issues)}")
    for cat, n in Counter(i["category"] for i in issues).most_common():
        print(f"  {cat}: {n}")
    print("\nP0:")
    for i in issues:
        if i["priority"] == "P0":
            print(f"  {i['category']} | {i['file']} | {i['detail']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
