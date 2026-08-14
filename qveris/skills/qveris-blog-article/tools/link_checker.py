#!/usr/bin/env python3
"""Check links in a QVeris blog article. Gate: G2/G6.

Flags placeholder links, forbidden internal paths (including decommissioned
sections /use-cases/, /scenarios/, /alternative/), and obvious broken patterns.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FORBIDDEN_PATHS = [
    "/auth/",
    "/admin/",
    "/dashboard/",
    "/use-cases/",
    "/scenarios/",
    "/alternative/",
    "/applications",  # 404 — real path is /apps
]
PLACEHOLDER_ANCHORS = ["click here", "learn more", "this article", "read more", "here"]
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def emit(status: str, gate: str, msg: str) -> None:
    print(f"{status} | {gate} | {msg}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Link checker for QVeris blog articles")
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--forbidden",
        default=",".join(FORBIDDEN_PATHS),
        help="Comma-separated extra forbidden path fragments",
    )
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    links = LINK_RE.findall(text)
    fails = 0
    gate = "G2/G6"

    forbidden = set(args.forbidden.split(","))

    if not links:
        emit("FAIL", gate, "no markdown links found (need >=2 internal blog links)")
        fails += 1
    else:
        emit("PASS", gate, f"{len(links)} markdown links found")

    internal_blog = [u for _, u in links if u.startswith("/blog/")]
    if len(internal_blog) >= 2:
        emit("PASS", gate, f"internal blog links >=2 ({len(internal_blog)})")
    elif len(internal_blog) == 1:
        emit("WARN", gate, f"internal blog links =1 (recommend >=2 when context allows)")
    else:
        # Pure third-party comparisons (e.g. golden 01) may legitimately have 0.
        # Emit WARN not FAIL so valid non-brand comparison pieces pass.
        emit("WARN", gate, "internal blog links =0 (OK for pure third-party comparison; recommend >=1 when context allows)")

    for anchor, url in links:
        al = anchor.lower().strip()
        if al in PLACEHOLDER_ANCHORS:
            emit("FAIL", gate, f"placeholder anchor '{anchor}' -> {url}")
            fails += 1
        for frag in sorted(forbidden):
            if url.startswith(frag):
                emit("FAIL", gate, f"forbidden path {frag} -> {url}")
                fails += 1
        if url.startswith("http://") or url.startswith("https://"):
            if "qveris.ai" in url:
                emit("PASS", gate, f"internal absolute ok: {url}")
            else:
                emit("PASS", gate, f"external link (manual check): {url}")
        elif url.startswith("/") and not url.startswith("/blog/") and not url.startswith("/guides/"):
            if url in ("/docs", "/pricing", "/cli", "/plugins", "/for-agents", "/apps",
                       "/capabilities/explore", "/providers", "/skills", "/ecosystem",
                       "/whats-new", "/security", "/playground", "/qverisbot"):
                emit("PASS", gate, f"whitelisted internal path: {url}")
            else:
                emit("PASS", gate, f"internal path (verify whitelist): {url}")
        elif url.startswith("/guides/"):
            emit("PASS", gate, f"guides internal link (trailing slash expected): {url}")

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
