#!/usr/bin/env python3
"""
Cross-page internal link graph audit (tools + blog Tools JSON).

Checks: orphans, inbound<3, missing backlinks, PageRank, click depth.

Usage:
  python audit-cross-page-links.py --json
  python audit-cross-page-links.py --orphans-only
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from internal_links_lib import (  # noqa: E402
    extract_links_from_blocks,
    find_deploy_root,
    list_json_slugs,
)

MIN_INBOUND = 3


def build_combined_graph(root: Path) -> tuple[dict[str, set[str]], dict[str, set[str]], list[str]]:
    """Merge EN+ZH edges: source->targets, incoming sources per target."""
    slug_routes = list_json_slugs(root, "both")
    all_slugs = sorted(slug_routes.keys())
    outgoing: dict[str, set[str]] = {s: set() for s in all_slugs}
    incoming: dict[str, set[str]] = defaultdict(set)

    for slug, route in slug_routes.items():
        for loc in ("en", "zh"):
            path = root / "content" / route / loc / f"{slug}.json"
            if not path.is_file():
                continue
            doc = json.loads(path.read_text(encoding="utf-8"))
            for tgt, _, _, _, _ in extract_links_from_blocks(doc.get("blocks", []), loc):
                if tgt in slug_routes and tgt != slug:
                    outgoing[slug].add(tgt)
                    incoming[tgt].add(slug)

    return outgoing, incoming, all_slugs


def find_orphans(all_slugs: list[str], incoming: dict[str, set[str]]) -> list[str]:
    return sorted(s for s in all_slugs if len(incoming.get(s, set())) == 0)


def find_low_inbound(all_slugs: list[str], incoming: dict[str, set[str]], threshold: int) -> list[dict]:
    out = []
    for s in all_slugs:
        n = len(incoming.get(s, set()))
        if n < threshold:
            out.append({"slug": s, "inbound": n, "sources": sorted(incoming.get(s, set()))})
    return sorted(out, key=lambda x: x["inbound"])


def find_missing_backlinks(outgoing: dict[str, set[str]], incoming: dict[str, set[str]]) -> list[dict]:
    missing = []
    for source, targets in outgoing.items():
        for target in targets:
            if target in outgoing and source not in outgoing[target]:
                missing.append({"source": source, "target": target, "locale": "combined"})
    return missing


def compute_pagerank(outgoing: dict[str, set[str]], incoming: dict[str, set[str]], iterations: int = 10) -> dict[str, float]:
    pages = sorted(set(outgoing.keys()) | set(incoming.keys()))
    n = len(pages)
    if n == 0:
        return {}
    idx = {p: i for i, p in enumerate(pages)}
    rank = [1.0 / n] * n
    d = 0.85
    for _ in range(iterations):
        new = [0.0] * n
        for i, page in enumerate(pages):
            inc = 0.0
            for src in incoming.get(page, set()):
                out_n = len(outgoing.get(src, set())) or 1
                inc += rank[idx[src]] / out_n
            new[i] = (1 - d) / n + d * inc
        rank = new
    return {pages[i]: rank[i] for i in range(n)}


def compute_click_depth(outgoing: dict[str, set[str]], starts: list[str] | None = None) -> dict[str, float]:
    if starts is None:
        starts = ["llm", "agent-skills", "web-scraping", "image-generator", "search-engine", "api"]
    depth = {p: float("inf") for p in outgoing}
    q = deque()
    for s in starts:
        if s in outgoing:
            depth[s] = 0
            q.append(s)
    while q:
        cur = q.popleft()
        for nb in outgoing.get(cur, set()):
            if depth[nb] > depth[cur] + 1:
                depth[nb] = depth[cur] + 1
                q.append(nb)
    return depth


def build_report(root: Path) -> dict:
    outgoing, incoming, all_slugs = build_combined_graph(root)
    orphans = find_orphans(all_slugs, incoming)
    low_inbound = find_low_inbound(all_slugs, incoming, MIN_INBOUND)
    missing = find_missing_backlinks(outgoing, incoming)
    pr = compute_pagerank(outgoing, incoming)
    depth = compute_click_depth(outgoing)

    page_metrics = {}
    for page in all_slugs:
        page_metrics[page] = {
            "out_links": len(outgoing.get(page, set())),
            "in_links": len(incoming.get(page, set())),
            "pagerank": round(pr.get(page, 0), 6),
            "click_depth": depth.get(page, -1) if depth.get(page, float("inf")) != float("inf") else -1,
        }

    return {
        "date": datetime.now().isoformat(),
        "scope": "combined_en_zh_tools_and_blog",
        "total_pages": len(all_slugs),
        "min_inbound_threshold": MIN_INBOUND,
        "orphans": orphans,
        "orphan_count": len(orphans),
        "inbound_below_threshold": low_inbound,
        "inbound_below_threshold_count": len(low_inbound),
        "missing_backlinks": missing,
        "missing_backlink_count": len(missing),
        "page_metrics": page_metrics,
    }


def print_human(report: dict, orphans_only: bool) -> None:
    print(f"\n{'='*80}")
    print(f"Cross-Page Link Analysis — COMBINED EN+ZH ({report['total_pages']} pages)")
    print(f"{'='*80}")

    if orphans_only:
        print(f"\nOrphans: {report['orphan_count']}")
        for o in report["orphans"]:
            m = report["page_metrics"].get(o, {})
            print(f"  - {o} (out={m.get('out_links', 0)})")
        print(f"\nInbound<{MIN_INBOUND}: {report['inbound_below_threshold_count']}")
        for row in report["inbound_below_threshold"]:
            print(f"  - {row['slug']}: in={row['inbound']} from {row['sources'][:5]}")
        return

    print(f"\nOrphans: {report['orphan_count']}")
    for o in report["orphans"]:
        print(f"  - {o}")
    print(f"\nInbound<{MIN_INBOUND}: {report['inbound_below_threshold_count']}")
    for row in report["inbound_below_threshold"][:20]:
        print(f"  - {row['slug']}: in={row['inbound']}")
    print(f"\nMissing backlinks (sample): {min(10, report['missing_backlink_count'])}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", default="both", choices=["en", "zh", "both"], help="legacy; graph is always combined")
    parser.add_argument("--orphans-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    root = find_deploy_root()
    report = build_report(root)

    if args.out:
        p = Path(args.out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {p}")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_human(report, args.orphans_only)

    if report["orphan_count"] or report["inbound_below_threshold_count"]:
        if args.json and not args.orphans_only:
            pass  # report only
        elif not args.orphans_only:
            pass


if __name__ == "__main__":
    main()
