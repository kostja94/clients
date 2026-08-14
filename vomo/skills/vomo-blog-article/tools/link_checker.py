#!/usr/bin/env python3
"""Markdown link checker. Gates: P0 G2 (malformed/empty), G6 (forbidden paths).

Optional --check-live: HTTP-verify external links (std-lib urllib only).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
except ImportError:  # pragma: no cover
    Request = urlopen = HTTPError = URLError = None  # type: ignore

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
RAW_URL_RE = re.compile(r"(?<!\]\()https?://[^\s\)]+")

# 权威域名白名单（用于 --check-live 之外的 judgment）：只链权威来源
AUTHORITATIVE_DOMAINS = (
    "edisonresearch.com",
    "pewresearch.org",
    "google.com",
    "gstatic.com",
    "w3.org",
    "gov.",
    "ac.uk",
    "bls.gov",
    "npr.org",
    "bbc.com",
    "bbc.co.uk",
    "nytimes.com",
    "wsj.com",
    "reuters.com",
    "apnews.com",
    "theverge.com",
    "search.google.com",
)


def emit(status: str, gate: str, msg: str, line: int | None = None) -> None:
    suffix = f" [line {line}]" if line is not None else ""
    print(f"{status} | {gate} | {msg}{suffix}")


def is_authoritative(url: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    return any(host.endswith(d.lstrip(".")) for d in AUTHORITATIVE_DOMAINS)


def live_check(url: str) -> bool:
    """HTTP-verify an external URL. Returns True if reachable (2xx/3xx)."""
    if Request is None or urlopen is None:
        return False
    req = Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0 (compatible; VOMO-LinkCheck)"})
    try:
        with urlopen(req, timeout=10) as resp:
            code = resp.getcode()
            return 200 <= code < 400
    except HTTPError as e:
        # Some servers reject HEAD; fall back to GET on 405/403.
        if e.code in (405, 403):
            try:
                req2 = Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0 (compatible; VOMO-LinkCheck)"})
                with urlopen(req2, timeout=10) as resp:
                    return 200 <= resp.getcode() < 400
            except (HTTPError, URLError):
                return False
        return False
    except (URLError, ValueError):
        return False


def check_links(text: str, forbidden: list[str], live: bool = False) -> int:
    fails = 0
    lines = text.splitlines()
    seen: set[str] = set()

    for i, line in enumerate(lines, start=1):
        for _anchor, url in LINK_RE.findall(line):
            url = url.strip()
            if not url or url in seen:
                continue
            seen.add(url)

            if url.startswith("#"):
                continue

            if url in ("", "#", "TODO", "TBD"):
                emit("FAIL", "P0-G2", f"empty or placeholder link: ({url})", i)
                fails += 1
                continue

            if url.startswith("/"):
                for prefix in forbidden:
                    if url.startswith(prefix) or prefix in url:
                        emit("FAIL", "P0-G6", f"internal link to forbidden path: {url}", i)
                        fails += 1
                if " " in url:
                    emit("FAIL", "P0-G2", f"malformed internal URL (spaces): {url}", i)
                    fails += 1
                continue

            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                emit("FAIL", "P0-G2", f"malformed URL: {url}", i)
                fails += 1
                continue

            if live:
                if not is_authoritative(url):
                    emit("FAIL", "P0-G2", f"external link to non-authoritative domain: {url}", i)
                    fails += 1
                elif not live_check(url):
                    emit("FAIL", "P0-G2", f"external link unreachable (HTTP/404): {url}", i)
                    fails += 1
                else:
                    emit("PASS", "P0-G2", f"external link reachable: {url}", i)

        for url in RAW_URL_RE.findall(line):
            if "example.com" in url.lower() and "example" in url.lower():
                emit("FAIL", "P0-G2", f"placeholder domain: {url}", i)
                fails += 1

    if fails == 0:
        emit("PASS", "P0-G2", f"checked {len(seen)} unique link targets")
        if forbidden:
            emit("PASS", "P0-G6", f"no links to forbidden prefixes: {forbidden}")
    return fails


def main() -> int:
    parser = argparse.ArgumentParser(description="Link checker for VOMO blog markdown")
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--forbidden",
        default="",
        help="Comma-separated forbidden internal path prefixes (G6)",
    )
    parser.add_argument(
        "--check-live",
        action="store_true",
        help="HTTP-verify external links + enforce authoritative-domain whitelist",
    )
    args = parser.parse_args()

    forbidden = [p.strip() for p in args.forbidden.split(",") if p.strip()]
    text = args.path.read_text(encoding="utf-8")
    fails = check_links(text, forbidden, live=args.check_live)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
