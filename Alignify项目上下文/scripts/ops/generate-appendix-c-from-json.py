#!/usr/bin/env python3
"""Generate appendix C draft from JSON internal links."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AUDIT_DIR = Path(__file__).resolve().parent.parent / "audit"
sys.path.insert(0, str(AUDIT_DIR))

from internal_links_lib import (
    find_deploy_root,
    extract_links_from_blocks,
    href_for_slug,
    list_json_slugs,
)


def first_occurrence(blocks: list, locale: str) -> list[dict]:
    seen: set[str] = set()
    rows: list[dict] = []
    for block in blocks:
        btype = block.get("type", "section")
        block_raw = json.dumps(block, ensure_ascii=False)
        for slug, anchor, _, bt, _ in extract_links_from_blocks([block], locale):
            if slug in seen:
                continue
            seen.add(slug)
            rows.append(
                {
                    "slug": slug,
                    "href": href_for_slug(slug, locale),
                    "anchor": anchor,
                    "block_type": bt or btype,
                }
            )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", type=str, default="")
    parser.add_argument("--source", default="both", choices=["tools", "blog", "both"])
    parser.add_argument("--locale", default="both", choices=["en", "zh", "both"])
    args = parser.parse_args()

    root = find_deploy_root()
    slug_routes = list_json_slugs(root, args.source)
    if args.slug:
        slug_routes = {args.slug: slug_routes[args.slug]} if args.slug in slug_routes else {}

    locales = ["en", "zh"] if args.locale == "both" else [args.locale]
    out: dict = {}

    for slug, route in sorted(slug_routes.items()):
        out[slug] = {"route": route, "locales": {}}
        for loc in locales:
            path = root / "content" / route / loc / f"{slug}.json"
            if not path.is_file():
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            rows = first_occurrence(data.get("blocks", []), loc)
            out[slug]["locales"][loc] = rows

    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
