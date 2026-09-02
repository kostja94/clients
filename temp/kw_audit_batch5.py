#!/usr/bin/env python3
"""Bing keyword audit for Alignify KB batch5."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

BATCH_PATH = Path("e:/clients/temp/kw-audit-batches/batch5_design_llm_text_web.json")
OUT_PATH = Path("e:/clients/temp/kw-audit-results/batch5_design_llm_text_web_results.json")

# slug -> (primary_en, [alternatives])
KEYWORD_MAP = {
    "design": ("AI design tool", ["AI design tools", "AI design software", "best AI design tool"]),
    "prototyping": ("AI prototyping tool", ["AI prototyping", "AI prototype tool", "interactive prototype AI"]),
    "ui-design": ("AI UI design", ["AI UI design tool", "AI interface design", "UI design AI"]),
    "user-research": ("AI user research", ["AI user research tool", "AI UX research", "user research AI"]),
    "ux-design": ("AI UX design", ["AI UX design tool", "UX design AI", "AI experience design"]),
    "wireframing": ("AI wireframing tool", ["AI wireframe tool", "AI wireframing", "wireframe generator AI"]),
    "evaluation": ("LLM evaluation", ["AI model evaluation", "LLM benchmark", "AI evaluation"]),
    "llm-for-coding": ("LLM for coding", ["coding LLM", "best LLM for coding", "AI coding LLM"]),
    "llm-for-math": ("LLM for math", ["math LLM", "best LLM for math", "AI math LLM"]),
    "llm-for-reasoning": ("reasoning LLM", ["LLM reasoning", "best reasoning LLM", "AI reasoning model"]),
    "llm": ("large language model", ["LLM", "best LLM", "large language models"]),
    "multimodal-llm": ("multimodal LLM", ["multimodal large language model", "AI multimodal LLM", "vision language model"]),
    "essay-writer": ("AI essay writer", ["essay generator AI", "AI essay generator", "essay writing AI"]),
    "presentation-maker": ("AI presentation maker", ["AI presentation generator", "AI slide maker", "presentation maker AI"]),
    "story-generator": ("AI story generator", ["story generator AI", "AI story writer", "AI storytelling tool"]),
    "text-generator": ("AI text generator", ["text generator AI", "AI writing generator", "AI content generator"]),
    "text-translator": ("AI text translation", ["AI translator", "AI translation tool", "machine translation AI"]),
    "text": ("AI writing tools", ["AI text tools", "AI writing tool", "best AI writing tools"]),
    "headless-browser": ("headless browser", ["headless browser automation", "cloud browser API", "browser automation API"]),
    "search-indexing": ("AI search indexing", ["search indexing API", "web search indexing", "search index API"]),
    "technology-profiler": ("website technology profiler", ["technology profiler", "website tech stack detector", "builtwith alternative"]),
    "web-fetch": ("web fetch API", ["URL to markdown API", "web content extraction API", "web fetch tool"]),
    "web-scraping": ("web scraping tools", ["AI web scraping", "web scraping tool", "web scraper"]),
    "web-search-api": ("web search API", ["search API", "AI web search API", "web search API for developers"]),
}

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def parse_count(html: str) -> int | None:
    patterns = [
        r'class="sb_count"[^>]*>([^<]+)',
        r'class="sb_count[^"]*"[^>]*>([^<]+)',
        r'About\s+([\d,]+)\s+results',
        r'([\d,]+)\s+results',
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
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            count = parse_count(html)
            return {"query": query, "approx_results": count, "status": "ok" if count else "no_count"}
        except Exception as e:
            last_err = str(e)
            time.sleep(1.5 * (attempt + 1))
    return {"query": query, "approx_results": None, "status": f"error: {last_err}"}


def normalize_primary(raw: str) -> str:
    """Extract English primary from mixed primary strings."""
    if not raw:
        return ""
    # take first segment before slash or chinese
    part = raw.split("/")[0].strip()
    # remove common prefixes like "AI " if whole thing is bilingual mess - keep as-is for search
    return part


def verdict(primary_count: int | None, alt_counts: list[tuple[str, int | None]]) -> tuple[str, str | None, str]:
    if primary_count is None:
        return "NEEDS_REVIEW", None, "Could not fetch Bing count for primary keyword"

    valid_alts = [(q, c) for q, c in alt_counts if c is not None]
    if not valid_alts:
        return "NEEDS_REVIEW", None, "No alternative counts available for comparison"

    best_alt = max(valid_alts, key=lambda x: x[1])
    best_q, best_c = best_alt

    # ratios
    ratio_best = best_c / primary_count if primary_count > 0 else float("inf")

    # top 2 alts within 30% of each other -> ambiguous
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
    batch = json.loads(BATCH_PATH.read_text(encoding="utf-8"))
    results = []
    summary = {"total": 0, "OK": 0, "SWITCH": 0, "AMBIGUOUS": 0, "NEEDS_REVIEW": 0}

    for i, item in enumerate(batch):
        slug = item["slug"]
        current_primary = item["current_primary"]
        km = KEYWORD_MAP.get(slug)
        if not km:
            results.append({
                "slug": slug,
                "path": item["path"],
                "current_primary": current_primary,
                "error": "missing keyword map entry",
                "verdict": "NEEDS_REVIEW",
            })
            summary["NEEDS_REVIEW"] += 1
            summary["total"] += 1
            continue

        primary_q, alts = km
        print(f"[{i+1}/24] {slug}: primary='{primary_q}'")

        primary_res = bing_count(primary_q)
        time.sleep(0.8)
        alt_results = []
        for alt in alts:
            r = bing_count(alt)
            alt_results.append(r)
            time.sleep(0.8)

        alt_pairs = [(r["query"], r["approx_results"]) for r in alt_results]
        v, suggested, reason = verdict(primary_res["approx_results"], alt_pairs)

        entry = {
            "slug": slug,
            "path": item["path"],
            "current_primary": current_primary,
            "search_primary": primary_q,
            "primary": primary_res,
            "alternatives": alt_results,
            "verdict": v,
            "suggested_primary": suggested,
            "reason": reason,
        }
        results.append(entry)
        summary["total"] += 1
        summary[v] += 1
        print(f"  -> {v}: {reason}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "batch": "batch5_design_llm_text_web",
        "methodology": "Bing approximate result counts; primary vs 2-4 same-intent alternatives",
        "audited_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "summary": summary,
        "results": results,
    }
    OUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nWrote", OUT_PATH)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
