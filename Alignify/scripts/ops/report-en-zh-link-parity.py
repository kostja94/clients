#!/usr/bin/env python3
"""Compare EN/ZH distinct href sets per slug."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AUDIT_DIR = Path(__file__).resolve().parent.parent / "audit"
sys.path.insert(0, str(AUDIT_DIR))

from internal_links_lib import find_deploy_root, extract_links_from_blocks, list_json_slugs


def distinct_slugs(path: Path, locale: str) -> set[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    links = extract_links_from_blocks(data.get("blocks", []), locale)
    return {s for s, _, _, _, _ in links}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="both", choices=["tools", "blog", "both"])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--min-diff", type=int, default=3)
    args = parser.parse_args()

    root = find_deploy_root()
    slug_routes = list_json_slugs(root, args.source)
    asym: list[dict] = []

    for slug, route in sorted(slug_routes.items()):
        en_path = root / "content" / route / "en" / f"{slug}.json"
        zh_path = root / "content" / route / "zh" / f"{slug}.json"
        if not en_path.is_file() or not zh_path.is_file():
            continue
        en_set = distinct_slugs(en_path, "en")
        zh_set = distinct_slugs(zh_path, "zh")
        only_en = sorted(en_set - zh_set)
        only_zh = sorted(zh_set - en_set)
        diff = max(len(only_en), len(only_zh))
        if only_en or only_zh:
            asym.append(
                {
                    "slug": slug,
                    "route": route,
                    "en_count": len(en_set),
                    "zh_count": len(zh_set),
                    "only_en": only_en,
                    "only_zh": only_zh,
                    "diff": diff,
                }
            )

    flagged = [a for a in asym if a["diff"] >= args.min_diff]
    if args.json:
        print(json.dumps({"asymmetric": asym, "flagged": flagged}, ensure_ascii=False, indent=2))
    else:
        print(f"Asymmetric slugs: {len(asym)}; flagged (diff>={args.min_diff}): {len(flagged)}")
        for row in flagged[:30]:
            print(
                f"  {row['slug']}: en={row['en_count']} zh={row['zh_count']} "
                f"only_en={row['only_en']} only_zh={row['only_zh']}"
            )


if __name__ == "__main__":
    main()
