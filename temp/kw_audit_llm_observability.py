#!/usr/bin/env python3
"""Bing keyword audit for llm-observability slug."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

OUT_PATH = Path("e:/clients/temp/kw-audit-results/llm_observability_results.json")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def parse_count(html: str) -> int | None:
    patterns = [
        r'class="sb_count"[^>]*>([^<]+)',
        r'class="sb_count[^"]*"[^>]*>([^<]+)',
        r"About\s+([\d,]+)\s+results",
        r"([\d,]+)\s+results",
    ]
    for pat in patterns:
        m = re.search(pat, html, re.I)
        if m:
            raw = m.group(1)
            nums = re.findall(r"[\d,]+", raw.replace("\xa0", " "))
            if nums:
                return int(nums[0].replace(",", ""))
    return None


def bing_count(query: str, retries: int = 3) -> dict:
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(query)
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            count = parse_count(html)
            return {"query": query, "approx_results": count, "status": "ok" if count else "no_count"}
        except Exception as e:
            last_err = str(e)
            time.sleep(1.5 * (attempt + 1))
    return {"query": query, "approx_results": None, "status": f"error: {last_err}"}


def verdict(primary_count: int | None, alt_counts: list[tuple[str, int | None]]) -> tuple[str, str | None, str]:
    if primary_count is None:
        return "NEEDS_REVIEW", None, "Could not fetch Bing count for primary keyword"

    valid_alts = [(q, c) for q, c in alt_counts if c is not None]
    if not valid_alts:
        return "NEEDS_REVIEW", None, "No alternative counts available for comparison"

    best_alt = max(valid_alts, key=lambda x: x[1])
    best_q, best_c = best_alt
    ratio_best = best_c / primary_count if primary_count > 0 else float("inf")

    sorted_alts = sorted(valid_alts, key=lambda x: x[1], reverse=True)
    if len(sorted_alts) >= 2:
        c1, c2 = sorted_alts[0][1], sorted_alts[1][1]
        if c1 > 0 and abs(c1 - c2) / max(c1, 1) < 0.15 and c1 > primary_count * 1.5:
            return (
                "AMBIGUOUS",
                None,
                f"Top alternatives close: '{sorted_alts[0][0]}' ({c1:,}) vs '{sorted_alts[1][0]}' ({c2:,}); primary {primary_count:,}",
            )

    if best_c >= primary_count * 2.0:
        return (
            "SWITCH",
            best_q,
            f"Alternative '{best_q}' has ~{best_c:,} vs primary ~{primary_count:,} ({ratio_best:.1f}x)",
        )

    if best_c >= primary_count * 1.3:
        return (
            "NEEDS_REVIEW",
            best_q,
            f"Alternative '{best_q}' moderately higher: ~{best_c:,} vs ~{primary_count:,} ({ratio_best:.1f}x)",
        )

    return (
        "OK",
        None,
        f"Primary competitive; best alt '{best_q}' ~{best_c:,} vs primary ~{primary_count:,}",
    )


def main():
    primary_q = "LLM observability"
    alts = [
        "LLM tracing",
        "AI observability",
        "LLM monitoring",
        "observability for LLM applications",
    ]

    print(f"Primary: {primary_q}")
    primary_res = bing_count(primary_q)
    time.sleep(0.8)

    alt_results = []
    for alt in alts:
        r = bing_count(alt)
        alt_results.append(r)
        print(f"  {alt}: {r['approx_results']}")
        time.sleep(0.8)

    alt_pairs = [(r["query"], r["approx_results"]) for r in alt_results]
    v, suggested, reason = verdict(primary_res["approx_results"], alt_pairs)

    entry = {
        "slug": "llm-observability",
        "path": "tools/llm/llm-observability.md",
        "current_primary": "LLM Observability",
        "search_primary": primary_q,
        "primary": primary_res,
        "alternatives": alt_results,
        "verdict": v,
        "suggested_primary": suggested,
        "reason": reason,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(entry, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(entry, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
