#!/usr/bin/env python3
"""Merge all brief.json files under og-briefs into registry."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from og_brief_lib import BRIEFS_ROOT, load_brief, merge_brief_into_registry


def main() -> None:
    total = 0
    for brief_path in sorted(BRIEFS_ROOT.rglob("brief.json")):
        rel = brief_path.relative_to(BRIEFS_ROOT)
        section, slug = rel.parts[0], rel.parts[1]
        brief = load_brief(section, slug)
        if brief:
            n = merge_brief_into_registry(brief, status="pending")
            print(f"Merged {section}/{slug}: {n} entries")
            total += n
    print(f"Total registry entries updated: {total}")


if __name__ == "__main__":
    main()
