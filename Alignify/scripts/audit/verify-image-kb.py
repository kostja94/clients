#!/usr/bin/env python3
"""Verify static image knowledge blocks (no cluster meta file)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB_DIR = ROOT / "knowledge" / "tools"

IMAGE_SLUGS = [
    "image",
    "image-generator",
    "image-editor",
    "image-enhancer",
    "image-relighting",
    "background-changer",
    "headshot-generator",
    "logo-generator",
    "poster-generator",
    "tattoo-generator",
    "avatar",
    "image-to-video",
]

CANONICAL_FACTS = [
    ("V8.1", r"V8\.1"),
    ("gpt-image-2", r"gpt-image-2|ChatGPT Images 2\.0"),
    ("Ideogram 4.0", r"Ideogram 4\.0"),
    ("DALL-E retirement", r"2026-05-12|2026 年 5 月 12 日"),
    ("FLUX.2", r"FLUX\.2"),
]

HUB_FORBIDDEN = [
    (r"\bDALL-E 3\b", "DALL-E 3"),
    (r"\bFLUX\.1\b", "FLUX.1"),
]

HUB_ALLOWED_DALLE = re.compile(r"DALL·E 2/3.*退役|DALL-E 2/3.*退役", re.I)
MAX_SPOKE_URL_ROWS = 12
DATE_PATTERN = re.compile(r"网摘整理日期 \*\*2026-06-2[23]\*\*")


def count_url_table_rows(text: str) -> int:
    in_index = False
    rows = 0
    for line in text.splitlines():
        if line.strip().startswith("## 外链索引"):
            in_index = True
            continue
        if in_index and line.startswith("## "):
            break
        if in_index and line.strip().startswith("|") and "---" not in line:
            if line.count("|") >= 3:
                first_cell = line.split("|")[1].strip()
                if first_cell and first_cell not in ("名称", "类型（英文常检索词）"):
                    rows += 1
    return rows


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if (KB_DIR / "media-image-cluster.md").exists():
        errors.append("media-image-cluster.md should be removed")

    for slug in IMAGE_SLUGS:
        path = KB_DIR / f"{slug}.md"
        if not path.exists():
            errors.append(f"missing {slug}.md")
            continue
        text = path.read_text(encoding="utf-8")

        if "media-image-cluster" in text:
            errors.append(f"{slug}: still references media-image-cluster")

        if slug != "image-to-video" and not DATE_PATTERN.search(text):
            warnings.append(f"{slug}: material date not 2026-06-23")

        if slug == "image":
            if "## 内容分工" not in text:
                errors.append("image.md: missing §内容分工")
            for pat, label in HUB_FORBIDDEN:
                for m in re.finditer(pat, text):
                    ctx = text[max(0, m.start() - 80) : m.end() + 80]
                    if "DALL" in label and HUB_ALLOWED_DALLE.search(ctx):
                        continue
                    errors.append(f"image.md: forbidden {label}")
            if count_url_table_rows(text) > 3:
                warnings.append(f"image.md: URL rows={count_url_table_rows(text)}")

        if slug == "image-generator":
            if "## 共享事实速查" not in text:
                errors.append("image-generator: missing §共享事实速查")
            if re.search(r"仍弱（~10% 成功率）", text):
                errors.append("image-generator: stale Midjourney ~10% text")

        if slug not in ("image", "image-generator") and count_url_table_rows(text) > MAX_SPOKE_URL_ROWS:
            warnings.append(f"{slug}: URL rows={count_url_table_rows(text)} > {MAX_SPOKE_URL_ROWS}")

    gen = (KB_DIR / "image-generator.md").read_text(encoding="utf-8")
    for label, pat in CANONICAL_FACTS:
        if not re.search(pat, gen):
            errors.append(f"image-generator missing: {label}")

    print("=== verify-image-kb ===")
    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  - {w}")
    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\nOK: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
