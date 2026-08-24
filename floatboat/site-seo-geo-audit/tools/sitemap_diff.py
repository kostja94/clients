#!/usr/bin/env python3
"""Compare floatboat.ai sitemap against expected URLs from audit config."""

from __future__ import annotations

import argparse
import http.client
import json
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

SITEMAP_URL = "https://floatboat.ai/sitemap.xml"
TIMEOUT = 45
UA = "FloatboatAuditBot/1.0 (+https://floatboat.ai)"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Live 200 pages often missing from sitemap (verify each audit)
EXPECTED_MISSING_FROM_SITEMAP = [
    "https://floatboat.ai/use-cases",
    "https://floatboat.ai/use-cases/for-solopreneur",
    "https://floatboat.ai/use-cases/for-creators",
    "https://floatboat.ai/use-cases/for-small-business",
    "https://floatboat.ai/use-cases/for-studio",
    "https://floatboat.ai/integrations",
    "https://floatboat.ai/models",
    "https://floatboat.ai/floatim",
    "https://floatboat.ai/zh/",
]

CRITICAL_URLS = [
    "https://floatboat.ai/",
    "https://floatboat.ai/pricing",
    "https://floatboat.ai/download",
    "https://floatboat.ai/about",
    "https://floatboat.ai/combostore",
    "https://floatboat.ai/marketplace",
    "https://floatboat.ai/blog",
    "https://floatboat.ai/alternatives",
]

# Known broken sitemap entries (404 when probed 2026-08-20)
KNOWN_SITEMAP_DEAD = [
    "https://floatboat.ai/workflowstore",
]


def fetch_sitemap(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        chunks: list[bytes] = []
        while True:
            try:
                chunk = resp.read(65536)
                if not chunk:
                    break
                chunks.append(chunk)
            except http.client.IncompleteRead as exc:
                if exc.partial:
                    chunks.append(exc.partial)
                break
        return b"".join(chunks).decode("utf-8", errors="replace")


def probe_status(url: str) -> int | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except Exception:  # noqa: BLE001
        return None


def parse_locs(xml_text: str) -> set[str]:
    root = ET.fromstring(xml_text)
    locs: set[str] = set()
    for loc in root.findall(".//sm:loc", NS):
        if loc.text:
            locs.add(loc.text.strip())
    if not locs:
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text:
                locs.add(loc.text.strip())
    return locs


def count_by_prefix(locs: set[str], prefix: str) -> int:
    return sum(1 for u in locs if prefix in u)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sitemap diff for floatboat audit")
    parser.add_argument("--sitemap-url", default=SITEMAP_URL)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--probe-dead", action="store_true", help="HEAD-check known dead URLs")
    args = parser.parse_args()

    xml_text = fetch_sitemap(args.sitemap_url)
    locs = parse_locs(xml_text)

    missing_critical = [u for u in CRITICAL_URLS if u not in locs]
    still_missing = [u for u in EXPECTED_MISSING_FROM_SITEMAP if u not in locs]
    now_in_sitemap = [u for u in EXPECTED_MISSING_FROM_SITEMAP if u in locs]

    dead_in_sitemap: list[dict[str, int | None]] = []
    if args.probe_dead:
        for url in sorted(locs):
            if url in KNOWN_SITEMAP_DEAD or "workflowstore" in url:
                dead_in_sitemap.append({"url": url, "status": probe_status(url)})

    blog_post_count = count_by_prefix(locs, "/blog/")
    combo_detail_count = sum(
        1
        for u in locs
        if "/combostore/" in u and not u.rstrip("/").endswith("/combostore")
    )

    stats = {
        "total_urls": len(locs),
        "blog_post_urls": blog_post_count,
        "combostore_detail_urls": combo_detail_count,
        "alternatives_urls": count_by_prefix(locs, "/alternatives"),
        "missing_critical": missing_critical,
        "expected_live_pages_still_not_in_sitemap": still_missing,
        "expected_live_pages_now_in_sitemap": now_in_sitemap,
        "dead_urls_in_sitemap": dead_in_sitemap,
        "sitemap_urls": sorted(locs),
    }

    if args.json:
        print(json.dumps(stats, indent=2))
    else:
        print(f"Sitemap URL count: {stats['total_urls']}")
        print(f"  /blog/* posts: {blog_post_count} (hub only = indexing risk)")
        print(f"  /combostore/* details: {combo_detail_count} (hub only = indexing risk)")
        print(f"  /alternatives*: {stats['alternatives_urls']}")
        print()
        if missing_critical:
            print("MISSING CRITICAL:")
            for u in missing_critical:
                print(f"  - {u}")
        else:
            print("All critical hub URLs present in sitemap.")
        print()
        if still_missing:
            print(
                f"Live pages still NOT in sitemap ({len(still_missing)}/"
                f"{len(EXPECTED_MISSING_FROM_SITEMAP)}):"
            )
            for u in still_missing:
                print(f"  - {u}")
        if now_in_sitemap:
            print(f"\nPreviously missing pages now IN sitemap ({len(now_in_sitemap)}):")
            for u in now_in_sitemap:
                print(f"  + {u}")
        if dead_in_sitemap:
            print("\nDEAD URLs listed in sitemap (P0):")
            for item in dead_in_sitemap:
                print(f"  - {item['url']} → HTTP {item['status']}")

    fail = bool(missing_critical or dead_in_sitemap)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
