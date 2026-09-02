#!/usr/bin/env python3
"""Bing keyword audit for Alignify KB batch2 (video + image)."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

BATCH_PATH = Path("e:/clients/temp/kw-audit-batches/batch2_video_image.json")
OUT_PATH = Path("e:/clients/temp/kw-audit-results/batch2_video_image_results.json")

# slug -> (primary_en, [alternatives])
KEYWORD_MAP = {
    "animation-generator": (
        "AI animation generator",
        ["AI anime generator", "animation generator AI", "AI animated video generator"],
    ),
    "canvas-video": (
        "AI video canvas",
        ["node-based AI video", "AI video workflow tool", "canvas video editor AI"],
    ),
    "filmmaking": (
        "AI filmmaking",
        ["AI film maker", "AI movie maker", "AI video production"],
    ),
    "image-to-video": (
        "image to video AI",
        ["AI image to video", "image to video generator", "AI image to video generator"],
    ),
    "interactive-video": (
        "interactive video AI",
        ["AI interactive video", "real-time video AI", "live interactive video"],
    ),
    "music-video-generator": (
        "AI music video generator",
        ["AI MV generator", "music video maker AI", "AI music video maker"],
    ),
    "short-drama": (
        "AI short drama",
        ["AI short drama platform", "AI drama generator", "AI short film generator"],
    ),
    "text-to-video": (
        "text to video AI",
        ["AI text to video", "text to video generator", "AI text to video generator"],
    ),
    "video-clipping": (
        "AI video clipping",
        ["AI video repurposing", "AI video clipper", "AI clip video"],
    ),
    "video-editor": (
        "AI video editor",
        ["video editor AI", "AI video editing", "AI video editing tool"],
    ),
    "video-effects": (
        "AI video effects",
        ["AI VFX", "AI video VFX", "AI video effects generator"],
    ),
    "video-generator": (
        "AI video generator",
        ["video generator AI", "AI video maker", "AI video creation tool"],
    ),
    "video-to-video": (
        "video to video AI",
        ["AI video to video", "video to video generator", "AI video to video generator"],
    ),
    "video": (
        "AI video",
        ["AI video tools", "best AI video tools", "AI video software"],
    ),
    "avatar": (
        "AI avatar generator",
        ["talking avatar AI", "AI presenter", "AI digital human"],
    ),
    "background-changer": (
        "AI background changer",
        ["AI background remover", "change background AI", "AI background editor"],
    ),
    "headshot-generator": (
        "AI headshot generator",
        ["AI professional headshot", "AI headshot", "professional headshot AI"],
    ),
    "image-editor": (
        "AI image editor",
        ["AI photo editor", "image editor AI", "AI picture editor"],
    ),
    "image-enhancer": (
        "AI image enhancer",
        ["AI photo enhancer", "AI image upscaler", "AI image enhancement"],
    ),
    "image-generator": (
        "AI image generator",
        ["text to image", "AI art generator", "text to image AI"],
    ),
    "image-relighting": (
        "AI image relighting",
        ["AI relighting", "AI photo relighting", "AI relight photo"],
    ),
    "image": (
        "AI image",
        ["AI image tools", "best AI image tools", "AI image software"],
    ),
    "logo-generator": (
        "AI logo generator",
        ["AI logo maker", "logo maker AI", "logo generator AI"],
    ),
    "poster-generator": (
        "AI poster generator",
        ["AI poster maker", "poster generator AI", "AI poster design"],
    ),
    "social-cards-generator": (
        "social cards generator",
        ["AI social media card generator", "og image generator", "social card maker AI"],
    ),
    "tattoo-generator": (
        "AI tattoo generator",
        ["AI tattoo design", "tattoo generator AI", "AI tattoo maker"],
    ),
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
    batch = json.loads(BATCH_PATH.read_text(encoding="utf-8"))
    results = []
    summary = {"total": 0, "OK": 0, "SWITCH": 0, "AMBIGUOUS": 0, "NEEDS_REVIEW": 0}

    for i, item in enumerate(batch):
        slug = item["slug"]
        current_primary = item["current_primary"]
        km = KEYWORD_MAP.get(slug)
        if not km:
            results.append(
                {
                    "slug": slug,
                    "path": item["path"],
                    "current_primary": current_primary,
                    "error": "missing keyword map entry",
                    "verdict": "NEEDS_REVIEW",
                }
            )
            summary["NEEDS_REVIEW"] += 1
            summary["total"] += 1
            continue

        primary_q, alts = km
        print(f"[{i + 1}/{len(batch)}] {slug}: primary='{primary_q}'")

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
        "batch": "batch2_video_image",
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
