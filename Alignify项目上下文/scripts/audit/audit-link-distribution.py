#!/usr/bin/env python3
"""Per-page internal link block distribution and density flags."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from internal_links_lib import (  # noqa: E402
    extract_links_from_blocks,
    find_deploy_root,
    list_json_slugs,
)

MIN_DISTINCT = 5
DENSITY_BLOCKS = {"conclusion", "faq"}


def audit_page(path: Path, slug: str, locale: str) -> dict:
    doc = json.loads(path.read_text(encoding="utf-8"))
    blocks = doc.get("blocks", [])
    links = extract_links_from_blocks(blocks, locale)
    distinct = len({s for s, _, _, _, _ in links})
    block_dist: dict[str, int] = defaultdict(int)
    for _, _, _, bt, _ in links:
        block_dist[bt or "section"] += 1

    block_types_with_links = len(block_dist)
    conclusion_faq_pct = 0.0
    if distinct:
        cf = sum(block_dist.get(b, 0) for b in ("faq", "section") if b == "faq")
        # conclusion is section titled 结论/Conclusion — approximate via faq+last section
        cf += block_dist.get("faq", 0)
        conclusion_faq_pct = cf / distinct

    flags: list[str] = []
    if distinct < MIN_DISTINCT:
        flags.append("under5")
    if distinct == MIN_DISTINCT and block_types_with_links <= 1:
        flags.append("sparse_single_block")
    if distinct >= 6 and block_types_with_links < 2:
        flags.append("low_block_spread")
    if block_dist.get("faq", 0) >= 3 and distinct >= 5:
        flags.append("faq_heavy")

    return {
        "slug": slug,
        "locale": locale,
        "distinct": distinct,
        "block_distribution": dict(block_dist),
        "block_types_with_links": block_types_with_links,
        "flags": flags,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--flags-only", action="store_true")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    root = find_deploy_root()
    slug_routes = list_json_slugs(root, "both")
    rows: list[dict] = []
    flagged: list[dict] = []

    for slug, route in sorted(slug_routes.items()):
        for loc in ("en", "zh"):
            path = root / "content" / route / loc / f"{slug}.json"
            if not path.is_file():
                continue
            row = audit_page(path, slug, loc)
            rows.append(row)
            if row["flags"]:
                flagged.append(row)

    report = {
        "date": date.today().isoformat(),
        "total": len(rows),
        "flagged_count": len(flagged),
        "sparse_single_block": [r for r in flagged if "sparse_single_block" in r["flags"]],
        "low_block_spread": [r for r in flagged if "low_block_spread" in r["flags"]],
        "faq_heavy": [r for r in flagged if "faq_heavy" in r["flags"]],
        "rows": rows if not args.flags_only else flagged,
    }

    if args.out:
        p = Path(args.out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {p}")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Distribution audit: {len(rows)} pages, {len(flagged)} flagged")
        for r in flagged[:30]:
            print(f"  {r['slug']} [{r['locale']}]: {r['flags']} dist={r['block_distribution']}")


if __name__ == "__main__":
    main()
