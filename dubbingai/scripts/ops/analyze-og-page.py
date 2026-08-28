#!/usr/bin/env python3
"""
LLM-analyze a Dubbing AI blog article and produce OG visual brief.

Usage:
  python analyze-og-page.py --slug best-ai-voice-changer
  python analyze-og-page.py --slug best-ai-voice-changer --merge-registry
  python analyze-og-page.py --slug best-ai-voice-changer --dry-run

Output: data/og-briefs/blog/{slug}/brief.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from og_brief_lib import (
    analyze_page,
    merge_brief_into_registry,
    resolve_openai_key,
    save_brief,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="LLM-analyze Dubbing AI blog article for OG cover brief")
    parser.add_argument("--section", default="blog")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--openai-key-file")
    parser.add_argument(
        "--merge-registry",
        action="store_true",
        help="Write brief fields into og-prompt-registry.json",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print brief JSON only")
    args = parser.parse_args()

    api_key = resolve_openai_key(args.openai_key_file)
    print(f"Analyzing blog/{args.slug}...")
    brief = analyze_page(args.section, args.slug, api_key)

    if args.dry_run:
        print(json.dumps(brief, ensure_ascii=False, indent=2))
        return

    out = save_brief(args.section, args.slug, brief)
    print(f"Saved brief: {out}")

    if args.merge_registry:
        n = merge_brief_into_registry(brief, status="pending")
        print(f"Merged {n} registry entry (en)")

    print("\nVisual anchors:")
    for i, a in enumerate(brief.get("visual_anchors", []), 1):
        print(f"  {i}. {a}")
    print("\nAnti-patterns:")
    for a in brief.get("anti_patterns", []):
        print(f"  - {a}")


if __name__ == "__main__":
    main()
