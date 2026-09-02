#!/usr/bin/env python3
"""Fetch approximate Bing result counts for keyword audit."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

PATTERNS = [
    re.compile(r"About\s+([\d,]+)\s+results", re.I),
    re.compile(r"([\d,]+)\s+results", re.I),
    re.compile(r'"totalResults"\s*:\s*"?([\d,]+)"?', re.I),
    re.compile(r"sb_count[^>]*>([^<]+)", re.I),
]


def parse_count(text: str) -> int | None:
    for pat in PATTERNS:
        m = pat.search(text)
        if m:
            raw = m.group(1).replace(",", "").strip()
            digits = re.sub(r"[^\d]", "", raw)
            if digits:
                return int(digits)
    return None


def bing_count(query: str, retries: int = 2) -> dict:
    encoded = urllib.parse.quote(query)
    url = f"https://www.bing.com/search?q={encoded}&setlang=en-us&cc=US&count=10"
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            count = parse_count(html)
            return {"query": query, "approx_results": count, "status": "ok" if count else "no_count"}
        except Exception as e:
            if attempt == retries:
                return {"query": query, "approx_results": None, "status": f"error: {e}"}
            time.sleep(1.5)
    return {"query": query, "approx_results": None, "status": "error"}


# Slug -> (current_primary_en, alternatives[])
AUDIT = {
    "accent-conversion": (
        "AI accent conversion",
        ["accent changer AI", "AI accent modification", "accent conversion tool"],
    ),
    "audio-translator": (
        "AI audio translation",
        ["audio translator AI", "AI voice translation", "translate audio AI"],
    ),
    "lip-sync": (
        "AI lip sync",
        ["lip sync AI", "AI lip sync tool", "video lip sync AI"],
    ),
    "music-generator": (
        "AI music generator",
        ["AI music maker", "text to music AI", "AI song generator"],
    ),
    "speech-to-text": (
        "speech to text AI",
        ["AI transcription", "automatic speech recognition", "AI speech to text"],
    ),
    "text-to-speech": (
        "text to speech AI",
        ["AI voice generator", "TTS AI", "AI text to speech"],
    ),
    "video-translator": (
        "AI video translation",
        ["AI video dubbing", "video translator AI", "AI video localization"],
    ),
    "voice-changer": (
        "AI voice changer",
        ["real-time voice changer", "voice modifier AI", "AI voice converter"],
    ),
    "voice-cloning": (
        "AI voice cloning",
        ["voice clone AI", "AI voice clone", "voice cloning tool"],
    ),
    "voice": (
        "AI voice",
        ["AI voice tools", "AI voice generator", "AI voice software"],
    ),
    "ai-components": (
        "AI components",
        ["prompt as component", "AI component library", "AI UI components"],
    ),
    "app-builder": (
        "AI app builder",
        ["AI application builder", "no code app builder AI", "AI app maker"],
    ),
    "cli": (
        "AI CLI",
        ["agentic CLI", "AI command line tools", "AI terminal agent"],
    ),
    "code-completion": (
        "AI code completion",
        ["code completion AI", "AI code assistant", "AI autocomplete code"],
    ),
    "code-review": (
        "AI code review",
        ["automated code review AI", "AI PR review", "AI code review tool"],
    ),
    "coding": (
        "AI coding",
        ["AI coding agent", "AI programming assistant", "AI code generator"],
    ),
    "git-hosting": (
        "agent native git hosting",
        ["AI git hosting", "code forge", "git hosting for AI agents"],
    ),
    "ide": (
        "AI IDE",
        ["agentic IDE", "AI code editor", "AI development environment"],
    ),
    "vibe-coding": (
        "vibe coding",
        ["AI coding", "AI app builder", "vibe coding AI"],
    ),
    "advertising-agent": (
        "AI advertising agent",
        ["advertising agent AI", "AI ad automation", "AI ads agent"],
    ),
    "affiliate-marketing": (
        "AI affiliate marketing",
        ["affiliate marketing tools", "affiliate marketing software", "affiliate marketing platform"],
    ),
    "b2b": (
        "AI B2B marketing tools",
        ["B2B marketing AI", "B2B marketing software", "AI B2B marketing"],
    ),
    "fundraising": (
        "AI fundraising",
        ["AI fundraising tools", "startup fundraising AI", "AI fundraising platform"],
    ),
    "influencer-marketing": (
        "AI influencer marketing",
        ["influencer marketing tools", "influencer marketing platform", "influencer marketing software"],
    ),
    "lead-generation": (
        "AI lead generation",
        ["lead generation tools", "AI sales leads", "B2B lead generation AI"],
    ),
    "referral-program": (
        "referral program software",
        ["referral marketing tools", "AI referral program", "referral program platform"],
    ),
    "social-media-tools": (
        "social media management tools",
        ["social media scheduling tools", "AI social media tools", "social media management software"],
    ),
    "ugc": (
        "UGC marketing",
        ["user generated content tools", "UGC platform", "UGC marketing tools"],
    ),
}


def verdict(primary_count: int | None, alt_counts: list[tuple[str, int | None]], ratio_switch: float = 3.0) -> tuple[str, str, str | None]:
    """Return verdict, rationale, recommended_primary."""
    valid = [(q, c) for q, c in alt_counts if c is not None]
    if primary_count is None and not valid:
        return "NEEDS_REVIEW", "No Bing counts retrieved", None
    if primary_count is None:
        best = max(valid, key=lambda x: x[1])
        return "NEEDS_REVIEW", f"Primary count missing; best alt '{best[0]}' ~{best[1]:,}", best[0]

    if not valid:
        return "NEEDS_REVIEW", "Only primary retrieved", None

    best_alt_q, best_alt_c = max(valid, key=lambda x: x[1])
    if best_alt_c >= primary_count * ratio_switch:
        return "SWITCH", f"'{best_alt_q}' ~{best_alt_c:,} >> primary ~{primary_count:,} (>{ratio_switch}x)", best_alt_q

    # Check if primary is clearly dominant (2x+ over all alts)
    if all(primary_count >= c * 2 for _, c in valid):
        return "OK", f"Primary ~{primary_count:,} dominates alternatives", None

    # Close counts within 2x
    close = [c for _, c in valid if c >= primary_count * 0.5]
    if len(close) >= 2 or (close and best_alt_c >= primary_count * 0.67):
        return "AMBIGUOUS", f"Primary ~{primary_count:,} vs best alt '{best_alt_q}' ~{best_alt_c:,} within ~2x", None

    if best_alt_c > primary_count:
        return "SWITCH", f"'{best_alt_q}' ~{best_alt_c:,} > primary ~{primary_count:,}", best_alt_q

    return "OK", f"Primary ~{primary_count:,} >= best alt ~{best_alt_c:,}", None


def main():
    batch_path = Path("e:/clients/temp/kw-audit-batches/batch3_voice_coding_marketing.json")
    out_dir = Path("e:/clients/temp/kw-audit-results")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "batch3_voice_coding_marketing_results.json"

    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    batch_by_slug = {item["slug"]: item for item in batch}

    results = []
    for slug, (primary, alts) in AUDIT.items():
        meta = batch_by_slug.get(slug, {})
        print(f"Auditing {slug}...", flush=True)

        primary_res = bing_count(primary)
        time.sleep(0.8)
        alt_results = []
        for alt in alts:
            r = bing_count(alt)
            alt_results.append(r)
            time.sleep(0.8)

        alt_tuples = [(r["query"], r["approx_results"]) for r in alt_results]
        v, rationale, rec = verdict(primary_res["approx_results"], alt_tuples)

        entry = {
            "slug": slug,
            "path": meta.get("path"),
            "current_primary": meta.get("current_primary"),
            "primary_query": primary,
            "primary_approx_results": primary_res["approx_results"],
            "alternatives": [
                {"query": r["query"], "approx_results": r["approx_results"], "status": r["status"]}
                for r in alt_results
            ],
            "verdict": v,
            "rationale": rationale,
            "recommended_primary": rec,
            "audit_date": "2026-09-03",
            "method": "Bing EN-US approximate result count (directional proxy, not MSV)",
        }
        results.append(entry)
        print(f"  {v}: {primary_res['approx_results']} vs {[r['approx_results'] for r in alt_results]}", flush=True)

    summary = {
        "batch": "batch3_voice_coding_marketing",
        "total": len(results),
        "verdicts": {},
        "switch_recommendations": [
            {"slug": r["slug"], "from": r["primary_query"], "to": r["recommended_primary"], "rationale": r["rationale"]}
            for r in results if r["verdict"] == "SWITCH"
        ],
        "ambiguous": [r["slug"] for r in results if r["verdict"] == "AMBIGUOUS"],
        "needs_review": [r["slug"] for r in results if r["verdict"] == "NEEDS_REVIEW"],
        "ok": [r["slug"] for r in results if r["verdict"] == "OK"],
    }
    for r in results:
        summary["verdicts"][r["verdict"]] = summary["verdicts"].get(r["verdict"], 0) + 1

    output = {"summary": summary, "results": results}
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
