#!/usr/bin/env python3
"""Bing keyword volume audit for Alignify KB batch4."""
import json
import re
import ssl
import time
import urllib.parse
import urllib.request
from pathlib import Path

BATCH = Path(r"e:/clients/temp/kw-audit-batches/batch4_edu_3d_enterprise.json")
OUT = Path(r"e:/clients/temp/kw-audit-results/batch4_edu_3d_enterprise_results.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

# slug -> (current_primary_en, [alternatives same-intent])
KEYWORDS = {
    "ai-flashcards": (
        "AI flashcards",
        ["AI flashcard maker", "AI study flashcards", "spaced repetition app"],
    ),
    "ai-for-science": (
        "AI for science",
        ["AI4S", "AI scientific research tools", "AI for scientific discovery"],
    ),
    "ai-homework-helper": (
        "AI homework helper",
        ["AI homework solver", "photo math solver AI", "AI math homework help"],
    ),
    "ai-language-learning": (
        "AI language learning",
        ["AI language learning app", "AI language tutor", "AI language learning tools"],
    ),
    "ai-tutor": (
        "AI tutor",
        ["AI tutoring", "AI tutoring platform", "online AI tutor"],
    ),
    "education": (
        "AI education tools",
        ["AI education", "AI learning tools", "AI tools for education"],
    ),
    "notes-generator": (
        "AI notes generator",
        ["AI note taking from video", "PDF to notes AI", "AI lecture notes generator"],
    ),
    "quiz-generator": (
        "AI quiz generator",
        ["AI quiz maker", "AI assessment generator", "AI test generator"],
    ),
    "3d-model-generator": (
        "AI 3D model generator",
        ["text to 3D", "image to 3D", "text to 3D AI"],
    ),
    "3d-modelling": (
        "3D modelling software",
        ["3D modeling tools", "DCC software", "3D modelling tools"],
    ),
    "3d-scanner": (
        "AI 3D scanner",
        ["3D scanning software", "photogrammetry software", "3D scan to model"],
    ),
    "3d": (
        "AI 3D tools",
        ["AI 3D software", "AI 3D generator", "AI 3D modeling tools"],
    ),
    "cad": (
        "AI CAD tools",
        ["CAD software", "AI CAD design", "AI CAD software"],
    ),
    "interior-design": (
        "AI interior design",
        ["AI interior design software", "AI room design", "AI home design"],
    ),
    "virtual-staging": (
        "AI virtual staging",
        ["virtual staging software", "virtual home staging", "AI home staging"],
    ),
    "ai-documents": (
        "AI documents",
        ["AI document management", "intelligent document processing", "AI document tools"],
    ),
    "documentation": (
        "developer documentation tools",
        ["API documentation tools", "technical documentation software", "docs as code tools"],
    ),
    "knowledge-base": (
        "AI knowledge base",
        ["AI knowledge management", "RAG knowledge base", "enterprise knowledge base AI"],
    ),
    "legal": (
        "AI for lawyers",
        ["legal AI tools", "AI legal software", "AI tools for legal professionals"],
    ),
    "memory": (
        "AI memory",
        ["AI second brain", "AI personal knowledge management", "AI memory assistant"],
    ),
    "ocr": (
        "OCR software",
        ["AI OCR", "optical character recognition tools", "AI text recognition"],
    ),
    "spreadsheet": (
        "AI spreadsheet",
        ["AI spreadsheet tools", "AI for Excel", "AI spreadsheet assistant"],
    ),
}

CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
CACHE: dict[str, int | None] = {}


def parse_count(html: str) -> int | None:
    m = re.search(r'sb_count">About\s*([\d,]+)\s*results', html, re.I)
    if m:
        return int(m.group(1).replace(",", ""))
    m = re.search(r'sb_count">([\d,]+)\s*results', html, re.I)
    if m:
        return int(m.group(1).replace(",", ""))
    m = re.search(r'About\s*([\d,]+)\s*results', html, re.I)
    if m:
        return int(m.group(1).replace(",", ""))
    m = re.search(r'约\s*([\d,]+)\s*条', html)
    if m:
        return int(m.group(1).replace(",", ""))
    return None


def bing_count(query: str, retries: int = 3) -> int | None:
    if query in CACHE:
        return CACHE[query]
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(query)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
            html = urllib.request.urlopen(req, context=CTX, timeout=20).read().decode("utf-8", "replace")
            count = parse_count(html)
            CACHE[query] = count
            time.sleep(0.8)
            return count
        except Exception as e:
            if attempt == retries - 1:
                CACHE[query] = None
                print(f"  FAIL {query!r}: {e}")
                return None
            time.sleep(2)
    return None


def verdict(current: str, counts: dict[str, int | None]) -> tuple[str, str]:
    valid = {k: v for k, v in counts.items() if v is not None}
    if not valid:
        return "NEEDS_REVIEW", "All Bing queries failed or returned no parseable counts."

    cur_val = valid.get(current)
    if cur_val is None:
        return "NEEDS_REVIEW", f"Current primary '{current}' returned no Bing count."

    ranked = sorted(valid.items(), key=lambda x: x[1], reverse=True)
    best_kw, best_val = ranked[0]
    second_val = ranked[1][1] if len(ranked) > 1 else 0

    # Very low volume across board
    if best_val < 1000:
        return "NEEDS_REVIEW", f"Very low Bing volume (max {best_val:,}); niche or parsing issue."

    ratio_best_to_current = best_val / cur_val if cur_val else float("inf")

    if best_kw == current:
        if len(ranked) > 1 and second_val > 0 and second_val / cur_val > 0.85:
            return "AMBIGUOUS", (
                f"Current '{current}' leads ({cur_val:,}) but '{ranked[1][0]}' is close ({second_val:,}, "
                f"{second_val/cur_val:.0%} of primary)."
            )
        return "OK", f"Current primary '{current}' has highest Bing volume ({cur_val:,})."

    # Alternative beats current significantly (>1.5x and >10k absolute gap or >2x)
    gap = best_val - cur_val
    if ratio_best_to_current >= 2.0 or (ratio_best_to_current >= 1.5 and gap >= 10000):
        return "SWITCH", (
            f"'{best_kw}' ({best_val:,}) significantly exceeds current '{current}' ({cur_val:,}); "
            f"{ratio_best_to_current:.1f}x."
        )

    if ratio_best_to_current >= 1.25:
        return "AMBIGUOUS", (
            f"'{best_kw}' ({best_val:,}) moderately exceeds '{current}' ({cur_val:,}); "
            f"{ratio_best_to_current:.1f}x — consider intent fit before switching."
        )

    return "OK", f"Current primary '{current}' ({cur_val:,}) is competitive; best alt '{best_kw}' ({best_val:,})."


def main():
    batch = json.loads(BATCH.read_text(encoding="utf-8"))
    results = []
    summary_counts = {"OK": 0, "SWITCH": 0, "AMBIGUOUS": 0, "NEEDS_REVIEW": 0}

    for item in batch:
        slug = item["slug"]
        current, alts = KEYWORDS[slug]
        all_kws = [current] + alts
        print(f"\n[{slug}]")
        counts: dict[str, int | None] = {}
        for kw in all_kws:
            c = bing_count(kw)
            counts[kw] = c
            print(f"  {kw}: {c:,}" if c else f"  {kw}: None")

        v, reason = verdict(current, counts)
        summary_counts[v] += 1

        ranked = sorted(
            [(k, v) for k, v in counts.items() if v is not None],
            key=lambda x: x[1],
            reverse=True,
        )

        results.append({
            "slug": slug,
            "path": item["path"],
            "current_primary": current,
            "alternatives_tested": alts,
            "bing_counts": counts,
            "ranked_by_volume": [{"keyword": k, "count": v} for k, v in ranked],
            "verdict": v,
            "reason": reason,
        })

    output = {
        "batch": "batch4_edu_3d_enterprise",
        "methodology": "Bing approximate result counts for current primary vs 2-4 same-intent English alternatives per slug.",
        "audited_at": "2026-09-03",
        "summary": {
            "total": len(results),
            **summary_counts,
            "switch_candidates": [r["slug"] for r in results if r["verdict"] == "SWITCH"],
            "ambiguous": [r["slug"] for r in results if r["verdict"] == "AMBIGUOUS"],
            "needs_review": [r["slug"] for r in results if r["verdict"] == "NEEDS_REVIEW"],
        },
        "results": results,
    }

    OUT.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved -> {OUT}")
    print("Summary:", json.dumps(output["summary"], indent=2))


if __name__ == "__main__":
    main()
