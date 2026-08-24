#!/usr/bin/env python3
"""Sample Combo Store URLs from sitemap and check title/meta duplication."""

from __future__ import annotations

import argparse
import random
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import asdict, dataclass

SITEMAP_URL = "https://floatboat.ai/sitemap.xml"
TIMEOUT = 45
UA = "FloatboatAuditBot/1.0 (+https://floatboat.ai)"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Fallback when sitemap only lists hub (observed 2026-08-20)
FALLBACK_SAMPLE_URLS = [
    "https://floatboat.ai/combostore/bracket-boss-1nKR69",
    "https://floatboat.ai/combostore/产品发布策略-3NfyPG",
]


@dataclass
class SampleResult:
    url: str
    status: int | None
    bytes: int
    title: str
    meta_description: str
    h1: str
    error: str | None = None


def fetch_sitemap_combostore_urls() -> list[str]:
    req = urllib.request.Request(SITEMAP_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        xml_text = resp.read().decode("utf-8", errors="replace")
    root = ET.fromstring(xml_text)
    urls: list[str] = []
    for loc in root.findall(".//sm:loc", NS):
        if loc.text and "/combostore/" in loc.text:
            if not loc.text.rstrip("/").endswith("/combostore"):
                urls.append(loc.text.strip())
    if not urls:
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text and "/combostore/" in loc.text:
                if not loc.text.rstrip("/").endswith("/combostore"):
                    urls.append(loc.text.strip())
    return urls


def parse_page(url: str) -> SampleResult:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "FloatboatAuditBot/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read()
            html = body.decode("utf-8", errors="replace")
            status = resp.status
        title_m = re.search(r"<title[^>]*>([^<]+)</title>", html, re.I)
        meta_m = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)',
            html,
            re.I,
        )
        if not meta_m:
            meta_m = re.search(
                r'<meta[^>]+content=["\']([^"\']*)["\'][^>]+name=["\']description["\']',
                html,
                re.I,
            )
        h1_m = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.I)
        return SampleResult(
            url=url,
            status=status,
            bytes=len(body),
            title=(title_m.group(1).strip() if title_m else ""),
            meta_description=(meta_m.group(1).strip() if meta_m else ""),
            h1=(h1_m.group(1).strip() if h1_m else ""),
        )
    except Exception as e:  # noqa: BLE001
        return SampleResult(url, None, 0, "", "", "", str(e))


def main() -> int:
    parser = argparse.ArgumentParser(description="Combo Store sample audit")
    parser.add_argument("-n", "--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=20260820)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    all_urls = fetch_sitemap_combostore_urls()
    source = "sitemap"
    if not all_urls:
        all_urls = FALLBACK_SAMPLE_URLS.copy()
        source = "fallback (sitemap has hub only — detail pages live but unlisted)"
        print(
            f"Note: no /combostore/{{id}} URLs in sitemap; using fallback sample.",
            file=sys.stderr,
        )

    random.seed(args.seed)
    sample = random.sample(all_urls, min(args.count, len(all_urls)))
    results = [parse_page(u) for u in sample]

    title_groups: dict[str, list[str]] = defaultdict(list)
    meta_groups: dict[str, list[str]] = defaultdict(list)
    for r in results:
        if r.title:
            title_groups[r.title].append(r.url)
        if r.meta_description:
            meta_groups[r.meta_description].append(r.url)

    dup_titles = {t: urls for t, urls in title_groups.items() if len(urls) > 1}
    dup_metas = {m: urls for m, urls in meta_groups.items() if len(urls) > 1}
    thin = [r for r in results if r.bytes < 8000]

    if args.json:
        import json

        print(
            json.dumps(
                {
                    "sample_size": len(results),
                    "sample_source": source,
                    "sitemap_combostore_detail_count": len(fetch_sitemap_combostore_urls()),
                    "results": [asdict(r) for r in results],
                    "duplicate_titles": dup_titles,
                    "duplicate_metas": dup_metas,
                    "thin_urls": [r.url for r in thin],
                },
                indent=2,
            )
        )
    else:
        print(f"Combo store URLs in sitemap: {len(all_urls)}")
        print(f"Sample size: {len(results)} (seed={args.seed})")
        print(f"\n{'URL':<60} {'BYTES':>7} {'TITLE':<40}")
        print("-" * 110)
        for r in results:
            t = (r.title[:37] + "…") if len(r.title) > 38 else r.title
            print(f"{r.url:<60} {r.bytes:>7} {t:<40}")
            if r.error:
                print(f"  error: {r.error}")
        print(f"\nThin pages (<8KB): {len(thin)}")
        print(f"Duplicate title groups: {len(dup_titles)}")
        print(f"Duplicate meta groups: {len(dup_metas)}")
        if dup_titles:
            print("\nDuplicate titles:")
            for title, urls in list(dup_titles.items())[:5]:
                print(f"  [{len(urls)}x] {title[:60]}")

    fail = len(dup_titles) > 0 or len(thin) > len(results) * 0.3
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
