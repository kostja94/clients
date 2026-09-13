#!/usr/bin/env python3
"""Merge all brief.json files under og-briefs into registry."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
IMAGE_GENERATOR = Path(r"E:\clients\Image Generator")
sys.path.insert(0, str(IMAGE_GENERATOR))

from og_brief_lib import briefs_root, load_brief, merge_brief_into_registry  # noqa: E402
from og_clients import load_client_config  # noqa: E402

CFG = load_client_config("alignify")
BRIEFS_ROOT = briefs_root(CFG)


def main() -> None:
    total = 0
    for brief_path in sorted(BRIEFS_ROOT.rglob("brief.json")):
        rel = brief_path.relative_to(BRIEFS_ROOT)
        section, slug = rel.parts[0], rel.parts[1]
        brief = load_brief(CFG, section, slug)
        if brief:
            n = merge_brief_into_registry(CFG, brief, status="pending")
            print(f"Merged {section}/{slug}: {n} entries")
            total += n
    print(f"Total registry entries updated: {total}")


if __name__ == "__main__":
    main()
