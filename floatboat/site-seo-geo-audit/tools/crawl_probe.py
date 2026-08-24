#!/usr/bin/env python3
"""Probe Floatboat URLs for HTTP status, content-type, size, and basic SEO signals."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from typing import Iterable

DEFAULT_UA = "FloatboatAuditBot/1.0 (+https://floatboat.ai)"
TIMEOUT = 30

T0_URLS = [
    "https://floatboat.ai/",
    "https://floatboat.ai/pricing",
    "https://floatboat.ai/download",
    "https://floatboat.ai/about",
    "https://floatboat.ai/combostore",
    "https://floatboat.ai/marketplace",
]

T1_URLS = [
    "https://floatboat.ai/alternatives",
    "https://floatboat.ai/alternatives/chatgpt-alternative",
    "https://floatboat.ai/use-cases",
    "https://floatboat.ai/use-cases/for-solopreneur",
    "https://floatboat.ai/floatim",
    "https://floatboat.ai/integrations",
    "https://floatboat.ai/models",
    "https://floatboat.ai/showcases",
]

MIN_BYTES = {
    "t0": 25_000,
    "t1": 15_000,
    "t2": 20_000,
    "t4": 8_000,
}


@dataclass
class ProbeResult:
    url: str
    status: int | None
    content_type: str
    bytes: int
    has_h1: bool
    has_ld_json: bool
    title: str
    error: str | None
    thin: bool | None = None


def fetch(url: str, user_agent: str = DEFAULT_UA) -> tuple[int, dict[str, str], bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": user_agent})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        body = resp.read()
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return resp.status, headers, body


def parse_html_signals(html: str) -> tuple[bool, bool, str]:
    has_h1 = bool(re.search(r"<h1\b", html, re.I))
    has_ld = bool(re.search(r"application/ld\+json", html, re.I))
    title_match = re.search(r"<title[^>]*>([^<]+)</title>", html, re.I)
    title = title_match.group(1).strip() if title_match else ""
    return has_h1, has_ld, title


def probe_url(url: str, min_bytes: int | None = None, user_agent: str = DEFAULT_UA) -> ProbeResult:
    try:
        status, headers, body = fetch(url, user_agent=user_agent)
        html = body.decode("utf-8", errors="replace")
        has_h1, has_ld, title = parse_html_signals(html)
        content_type = headers.get("content-type", "")
        size = len(body)
        thin = size < min_bytes if min_bytes else None
        return ProbeResult(
            url=url,
            status=status,
            content_type=content_type,
            bytes=size,
            has_h1=has_h1,
            has_ld_json=has_ld,
            title=title,
            error=None,
            thin=thin,
        )
    except urllib.error.HTTPError as e:
        return ProbeResult(url, e.code, "", 0, False, False, "", str(e))
    except Exception as e:  # noqa: BLE001
        return ProbeResult(url, None, "", 0, False, False, "", str(e))


def urls_for_tier(tier: str) -> list[str]:
    tier = tier.lower()
    if tier == "t0":
        return T0_URLS
    if tier == "t1":
        return T1_URLS
    if tier == "t0+t1":
        return T0_URLS + T1_URLS
    raise ValueError(f"Unknown tier: {tier}")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Crawl probe for floatboat.ai audit")
    parser.add_argument("--urls", nargs="*", help="Explicit URLs to probe")
    parser.add_argument("--tier", choices=["t0", "t1", "t0+t1"], help="Preset URL tier")
    parser.add_argument("--min-bytes", type=int, help="Flag thin if body smaller than this")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--user-agent", default=DEFAULT_UA)
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.urls:
        urls = args.urls
        min_bytes = args.min_bytes
    elif args.tier:
        urls = urls_for_tier(args.tier)
        min_bytes = args.min_bytes or MIN_BYTES.get(args.tier.split("+")[0])
    else:
        urls = urls_for_tier("t0+t1")
        min_bytes = args.min_bytes

    results = [probe_url(u, min_bytes=min_bytes, user_agent=args.user_agent) for u in urls]

    if args.json:
        print(json.dumps([asdict(r) for r in results], indent=2))
    else:
        print(f"{'URL':<55} {'ST':>4} {'BYTES':>8} {'H1':>3} {'LD':>3} {'THIN':>5} TITLE")
        print("-" * 110)
        for r in results:
            thin = "yes" if r.thin else ("no" if r.thin is False else "-")
            title = (r.title[:40] + "…") if len(r.title) > 41 else r.title
            print(
                f"{r.url:<55} {r.status or 'ERR':>4} {r.bytes:>8} "
                f"{'Y' if r.has_h1 else 'N':>3} {'Y' if r.has_ld_json else 'N':>3} {thin:>5} {title}"
            )
            if r.error:
                print(f"  error: {r.error}")

    fails = sum(1 for r in results if r.status != 200 or r.thin)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
