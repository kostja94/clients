#!/usr/bin/env python3
"""Audit duplicate fingerprints across image KB slugs."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
KB = ROOT / "knowledge" / "tools"

SLUGS = [
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

FINGERPRINTS = [
    "Midjourney V8.1",
    "Ideogram 4.0",
    "Canva AI 2.0",
    "Generative Fill",
    "Photoroom",
    "gpt-image-2",
    "FLUX.2",
    "DALL·E",
    "Nano Banana",
]

WARN_TOTAL = 8  # cluster-wide; generator/hub expected to hold SSOT facts
SSOT_SLUGS = {"image-generator", "image"}


def main() -> int:
    print("=== audit-kb-image-overlap ===\n")
    errors: list[str] = []
    for fp in FINGERPRINTS:
        total = 0
        for slug in SLUGS:
            path = KB / f"{slug}.md"
            if not path.exists():
                continue
            n = len(re.findall(re.escape(fp), path.read_text(encoding="utf-8")))
            if n:
                print(f"  {slug}: {fp} x{n}")
                total += n
        print(f"  TOTAL {fp}: {total}\n")
        if total > WARN_TOTAL:
            # High cluster-wide count is expected when SSOT holds canonical facts
            spoke_only = sum(
                len(re.findall(re.escape(fp), (KB / f"{s}.md").read_text(encoding="utf-8")))
                for s in SLUGS
                if s not in SSOT_SLUGS and (KB / f"{s}.md").exists()
            )
            if spoke_only > WARN_TOTAL:
                errors.append(f"{fp} appears {spoke_only} times in spokes (>{WARN_TOTAL})")

    print("=== sizes (bytes) ===")
    for slug in SLUGS:
        path = KB / f"{slug}.md"
        if path.exists():
            print(f"  {slug}: {len(path.read_text(encoding='utf-8'))}")

    if errors:
        print("\nWARNINGS:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\nOK: no excessive fingerprint spread")
    return 0


if __name__ == "__main__":
    sys.exit(main())
