#!/usr/bin/env python3
"""Probe floatboat.ai with multiple AI crawler user-agents."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass

TIMEOUT = 30

AI_USER_AGENTS = {
    "OAI-SearchBot": "OAI-SearchBot",
    "PerplexityBot": "PerplexityBot",
    "Claude-SearchBot": "Claude-SearchBot",
    "Claude-User": "Claude-User",
    "GPTBot": "GPTBot",
    "Google-Extended": "Google-Extended",
    "Googlebot": "Googlebot",
}

DEFAULT_URLS = [
    "https://floatboat.ai/",
    "https://floatboat.ai/pricing",
    "https://floatboat.ai/blog/calendar-driven-ai-vs-chat-ai",
]


@dataclass
class UAResult:
    url: str
    user_agent: str
    status: int | None
    blocked: bool
    error: str | None


def probe(url: str, ua_name: str, ua_value: str) -> UAResult:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": ua_value})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            status = resp.status
            blocked = status in (403, 401, 429)
            return UAResult(url, ua_name, status, blocked, None)
    except urllib.error.HTTPError as e:
        return UAResult(url, ua_name, e.code, e.code in (403, 401, 429), str(e))
    except Exception as e:  # noqa: BLE001
        return UAResult(url, ua_name, None, True, str(e))


def main() -> int:
    parser = argparse.ArgumentParser(description="AI user-agent probe for floatboat.ai")
    parser.add_argument("--urls", nargs="*", default=DEFAULT_URLS)
    parser.add_argument("--agents", nargs="*", default=list(AI_USER_AGENTS.keys()))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results: list[UAResult] = []
    for url in args.urls:
        for name in args.agents:
            ua = AI_USER_AGENTS.get(name, name)
            results.append(probe(url, name, ua))

    if args.json:
        print(json.dumps([asdict(r) for r in results], indent=2))
    else:
        print(f"{'URL':<52} {'AGENT':<18} {'STATUS':>6} {'BLOCKED':>8}")
        print("-" * 90)
        for r in results:
            print(f"{r.url:<52} {r.user_agent:<18} {r.status or 'ERR':>6} {'YES' if r.blocked else 'no':>8}")
            if r.error:
                print(f"  {r.error}")

    # Search bots must get 200
    search_bots = {"OAI-SearchBot", "PerplexityBot", "Claude-SearchBot", "Claude-User"}
    failures = [
        r
        for r in results
        if r.user_agent in search_bots and (r.status != 200 or r.blocked)
    ]
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
