#!/usr/bin/env python3
"""Validate cms-export markdown files against acceptance checklist."""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.csv"

REQUIRED_FM = (
    "title",
    "description",
    "slug",
    "date",
    "author",
    "status",
    "source",
    "canonical",
    "migrated_at",
)

LEAK_PATTERNS = (
    "blogbuster-related-posts",
)

FOOTER_LEAK_MARKERS = (
    "all rights reserved",
    "halo interactive pte",
)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    block = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    data = {}
    for line in block.splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip('"')
            data[key] = val
    return data, body


def validate_file(path: Path) -> list[str]:
    issues = []
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    slug = path.stem
    for k in REQUIRED_FM:
        if not fm.get(k):
            issues.append(f"missing frontmatter: {k}")
    if fm.get("slug") and fm["slug"] != slug:
        issues.append(f"slug mismatch file={slug} fm={fm['slug']}")
    if not body.startswith("#"):
        issues.append("body missing H1")
    elif fm.get("title"):
        h1 = body.splitlines()[0].lstrip("#").strip()
        if fm["title"] not in h1 and h1 not in fm["title"]:
            issues.append(f"H1/title mismatch: {h1[:40]!r} vs {fm['title'][:40]!r}")
    for pat in LEAK_PATTERNS:
        if pat in body:
            issues.append(f"possible CMS leak: {pat}")
    tail = "\n".join(body.splitlines()[-3:]).lower()
    if any(m in tail for m in FOOTER_LEAK_MARKERS):
        issues.append("possible CMS footer in tail")
    if len(body.strip()) < 200:
        issues.append("body too short")
    return issues


def main() -> None:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8")))
    done_slugs = {r["slug"] for r in rows if r["status"] == "done"}
    md_files = {p.stem for p in ROOT.glob("*.md") if p.name not in ("_template.md", "README.md")}

    missing_files = done_slugs - md_files
    extra_files = md_files - done_slugs

    bad = []
    for slug in sorted(done_slugs):
        path = ROOT / f"{slug}.md"
        if not path.exists():
            continue
        issues = validate_file(path)
        if issues:
            bad.append((slug, issues))

    p0 = [
        "dubbing-ai-vs-voicemod",
        "how-to-get-voice-changer-on-discord",
        "jett-voice-changer",
        "minecraft-soundboard",
        "dubbing-ai-trump-voice",
    ]
    print("=== Summary ===")
    print(f"manifest done: {len(done_slugs)}")
    print(f"md files: {len(md_files)}")
    print(f"missing md for done: {len(missing_files)}")
    print(f"extra md files: {len(extra_files)}")
    print(f"validation issues: {len(bad)}")

    print("\n=== P0 spot-check ===")
    for slug in p0:
        path = ROOT / f"{slug}.md"
        if not path.exists():
            print(f"  {slug}: MISSING")
            continue
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        h2 = len(re.findall(r"^## ", body, re.M))
        print(f"  {slug}: H2={h2}, chars={len(body)}, category={fm.get('category','')}")

    if bad[:10]:
        print("\n=== First issues ===")
        for slug, issues in bad[:10]:
            print(f"  {slug}: {issues}")


if __name__ == "__main__":
    main()
