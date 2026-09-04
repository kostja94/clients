#!/usr/bin/env python3
"""Refined BATCH 2 keyword audit: video + image slugs (25, no hub pages)."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

BATCH_PATH = Path("e:/clients/temp/kw-audit-batches/batch2_video_image.json")
OUT_PATH = Path("e:/clients/temp/kw-audit-results/batch2_video_image_results.json")
CAP = 509_000
SUSPICIOUS_LOW = 100

USER_SLUGS = [
    "animation-generator", "canvas-video", "filmmaking", "image-to-video",
    "interactive-video", "music-video-generator", "short-drama", "text-to-video",
    "video-clipping", "video-editor", "video-effects", "video-generator", "video-to-video",
    "avatar", "background-changer", "headshot-generator", "image-editor", "image-enhancer",
    "image-generator", "image-relighting", "logo-generator", "poster-generator",
    "social-cards-generator", "tattoo-generator",
]

# slug -> list of intent-near English queries (first should mirror KB primary EN head term)
CANDIDATES = {
    "animation-generator": [
        "AI animation generator",
        "AI anime generator",
        "animation generator AI",
        "AI animated video generator",
    ],
    "canvas-video": [
        "AI video canvas",
        "node-based AI video workflow",
        "canvas video AI",
        "AI video workflow tool",
    ],
    "filmmaking": [
        "AI filmmaking",
        "AI filmmaking tools",
        "AI film production",
        "AI movie maker",
    ],
    "image-to-video": [
        "image to video",
        "image-to-video",
        "AI image to video",
        "image to video AI generator",
    ],
    "interactive-video": [
        "interactive video",
        "AI interactive video",
        "live video generation",
        "real-time interactive video",
    ],
    "music-video-generator": [
        "AI music video generator",
        "music video generator AI",
        "AI music video maker",
        "music video maker AI",
    ],
    "short-drama": [
        "AI short drama platform",
        "AI short drama",
        "AI short film platform",
        "AI drama generator",
    ],
    "text-to-video": [
        "text to video",
        "text-to-video",
        "AI text to video",
        "text to video AI generator",
    ],
    "video-clipping": [
        "AI video clipping",
        "video clipping",
        "AI video repurposing",
        "AI video clipper",
    ],
    "video-editor": [
        "AI video editor",
        "AI video editor tools",
        "video editor AI",
        "AI video editing",
    ],
    "video-effects": [
        "AI video effects",
        "AI VFX",
        "video effects",
        "AI video VFX",
    ],
    "video-generator": [
        "AI video generator",
        "AI video generator tools",
        "video generator AI",
        "AI video maker",
    ],
    "video-to-video": [
        "video to video",
        "video-to-video",
        "AI video to video",
        "video to video AI",
    ],
    "avatar": [
        "talking avatar",
        "AI avatar",
        "AI presenter",
        "AI digital human",
    ],
    "background-changer": [
        "AI background changer",
        "background changer",
        "AI background remover",
        "change background AI",
    ],
    "headshot-generator": [
        "AI headshot generator",
        "headshot generator",
        "AI professional headshot",
        "professional headshot AI",
    ],
    "image-editor": [
        "AI image editor",
        "image editor tools",
        "AI photo editor",
        "image editor AI",
    ],
    "image-enhancer": [
        "AI image enhancer",
        "AI photo enhancer",
        "image enhancer",
        "AI image upscaler",
    ],
    "image-generator": [
        "AI image generator",
        "text to image",
        "AI art generator",
        "text to image AI",
    ],
    "image-relighting": [
        "AI image relighting",
        "image relighting",
        "AI relighting",
        "AI photo relighting",
    ],
    "logo-generator": [
        "AI logo generator",
        "logo generator AI",
        "AI logo maker",
        "logo maker AI",
    ],
    "poster-generator": [
        "AI poster generator",
        "poster generator",
        "AI poster maker",
        "poster maker AI",
    ],
    "social-cards-generator": [
        "social cards generator",
        "AI social cards generator",
        "og image generator",
        "social media card generator",
    ],
    "tattoo-generator": [
        "AI tattoo generator",
        "tattoo generator",
        "tattoo generator AI",
        "AI tattoo design",
    ],
}

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def parse_count(html: str) -> int | None:
    patterns = [
        r'class="sb_count"[^>]*>([^<]+)',
        r'About\s+([\d,]+)\s+results',
        r'([\d,]+)\s+results',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.I)
        if m:
            nums = re.findall(r"[\d,]+", m.group(1).replace("\xa0", " "))
            if nums:
                return int(nums[0].replace(",", ""))
    return None


def bing_count(query: str, retries: int = 3) -> int | None:
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(query) + "&setlang=en-us&cc=US"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
            )
            with urllib.request.urlopen(req, timeout=25) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            return parse_count(html)
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    return None


def primary_en_from_kb(current_primary: str) -> str:
    """First English segment before / or Chinese."""
    part = current_primary.split("/")[0].strip()
    part = re.sub(r"\s*\([^)]*\)\s*", " ", part).strip()
    return part


def is_capped(n: int | None) -> bool:
    return n is not None and n >= CAP


def pick_primary_candidate(current_primary: str, queries: list[str]) -> str:
    en = primary_en_from_kb(current_primary).lower()
    for q in queries:
        if q.lower() == en or en in q.lower() or q.lower() in en:
            return q
    return queries[0]


def refine_verdict(current_primary: str, tested: list[dict]) -> tuple[str, str, str, str]:
    primary_q = pick_primary_candidate(current_primary, [t["keyword"] for t in tested])
    primary_count = next((t["bing_approx"] for t in tested if t["keyword"] == primary_q), None)
    all_pairs = [(t["keyword"], t["bing_approx"]) for t in tested if t["bing_approx"] is not None]
    if not all_pairs:
        return "NEEDS_REVIEW", primary_q, primary_q, "No Bing counts retrieved"

    best_q, best_c = max(all_pairs, key=lambda x: x[1])
    non_capped = [(q, c) for q, c in all_pairs if not is_capped(c)]
    non_capped_primary = None if is_capped(primary_count) else primary_count

    if is_capped(primary_count) and non_capped:
        nc_best_q, nc_best_c = max(non_capped, key=lambda x: x[1])
        if nc_best_q.lower() != primary_q.lower() and nc_best_c >= (primary_count or 0) * 0.5:
            return (
                "NEEDS_REVIEW",
                best_q,
                nc_best_q,
                f"Primary '{primary_q}' capped ~{primary_count:,}; best non-capped '{nc_best_q}' ~{nc_best_c:,}",
            )
        return (
            "AMBIGUOUS",
            best_q,
            primary_q,
            f"Primary '{primary_q}' and alts hit Bing ~{CAP:,} cap — SERP title review needed",
        )

    if primary_count is None:
        return "NEEDS_REVIEW", best_q, best_q, f"Primary count missing; best '{best_q}' ~{best_c:,}"

    if non_capped_primary is not None and non_capped:
        nc_best_q, nc_best_c = max(non_capped, key=lambda x: x[1])
        if nc_best_q.lower() != primary_q.lower() and nc_best_c >= non_capped_primary * 2:
            return (
                "SWITCH",
                best_q,
                nc_best_q,
                f"'{nc_best_q}' ~{nc_best_c:,} >=2x primary '{primary_q}' ~{non_capped_primary:,}",
            )
        if all(non_capped_primary >= c * 1.5 for q, c in non_capped if q.lower() != primary_q.lower()):
            return (
                "OK",
                best_q,
                primary_q,
                f"Primary '{primary_q}' ~{non_capped_primary:,} leads non-capped alts",
            )
        close = [c for q, c in non_capped if q.lower() != primary_q.lower() and c >= non_capped_primary * 0.67]
        if len(close) >= 2:
            return (
                "AMBIGUOUS",
                best_q,
                primary_q,
                f"Primary ~{non_capped_primary:,}; multiple alts within ~1.5x",
            )
        if nc_best_q.lower() != primary_q.lower() and nc_best_c > non_capped_primary * 1.3:
            return (
                "NEEDS_REVIEW",
                best_q,
                nc_best_q,
                f"'{nc_best_q}' ~{nc_best_c:,} moderately above primary ~{non_capped_primary:,}",
            )

    if primary_count is not None and primary_count <= SUSPICIOUS_LOW:
        return "NEEDS_REVIEW", best_q, best_q, f"Primary suspiciously low ~{primary_count:,}"

  # fallback: compare raw best vs primary
    if best_q.lower() != primary_q.lower() and best_c >= (primary_count or 0) * 2:
        return "SWITCH", best_q, best_q, f"'{best_q}' ~{best_c:,} >=2x primary ~{primary_count:,}"

    rec = primary_q if (primary_count or 0) >= best_c * 0.67 else best_q
    verdict = "OK" if rec == primary_q else "NEEDS_REVIEW"
    return verdict, best_q, rec, f"best='{best_q}' ~{best_c:,}; primary='{primary_q}' ~{primary_count:,}"


def main():
    batch = {item["slug"]: item for item in json.loads(BATCH_PATH.read_text(encoding="utf-8"))}
    results = []

    for i, slug in enumerate(USER_SLUGS):
        item = batch[slug]
        current_primary = item["current_primary"]
        queries = CANDIDATES[slug]
        print(f"[{i+1}/{len(USER_SLUGS)}] {slug}", flush=True)

        tested = []
        for q in queries:
            c = bing_count(q)
            tested.append({"keyword": q, "bing_approx": c})
            print(f"  {q}: {c}", flush=True)
            time.sleep(0.7)

        best_q = max(
            (t for t in tested if t["bing_approx"] is not None),
            key=lambda x: x["bing_approx"],
            default={"keyword": queries[0], "bing_approx": None},
        )["keyword"]
        highest = max((t["bing_approx"] or 0 for t in tested), default=0)
        highest_kw = next(t["keyword"] for t in tested if t["bing_approx"] == highest)

        verdict, _, rec, notes = refine_verdict(current_primary, tested)
        capped = [t["keyword"] for t in tested if is_capped(t["bing_approx"])]
        if capped:
            notes += f"; capped: {', '.join(capped)}"

        results.append({
            "slug": slug,
            "current_primary": current_primary,
            "candidates_tested": tested,
            "highest_volume_keyword": highest_kw,
            "verdict": verdict,
            "recommended_primary": rec,
            "notes": notes,
        })
        print(f"  -> {verdict}: {notes}\n", flush=True)

    OUT_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    summary = {}
    for r in results:
        summary[r["verdict"]] = summary.get(r["verdict"], 0) + 1
    print("SUMMARY:", json.dumps(summary))
    print("Wrote", OUT_PATH)


if __name__ == "__main__":
    main()
