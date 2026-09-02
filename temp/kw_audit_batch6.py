#!/usr/bin/env python3
"""Bing keyword audit for Alignify KB batch6 (misc clusters)."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

BATCH_PATH = Path("e:/clients/temp/kw-audit-batches/batch6_misc.json")
OUT_PATH = Path("e:/clients/temp/kw-audit-results/batch6_misc_results.json")

# slug -> (primary_en, [alternatives])
KEYWORD_MAP = {
    # chat-social
    "character-chat": (
        "character chat",
        ["AI character chat", "character AI chat", "AI companion chat"],
    ),
    "chatbot": (
        "AI chatbot",
        ["chatbot", "best AI chatbot", "AI chat bot"],
    ),
    "community": (
        "AI community",
        ["AI communities", "artificial intelligence community", "AI forum"],
    ),
    "dating": (
        "AI dating",
        ["AI dating app", "AI matchmaking", "AI dating platform"],
    ),
    "directory": (
        "AI directory",
        ["AI tools directory", "AI tool directory", "AI tools list"],
    ),
    # website-builder (verify KEYWORD-RESEARCH.md)
    "blog-website-builder": (
        "blog website builder",
        ["blogging platform", "blog CMS", "website builder for blogs"],
    ),
    "ecommerce-website-builder": (
        "online store platform",
        ["ecommerce website builder", "e-commerce website builder", "online store builder"],
    ),
    "landing-page-builder": (
        "landing page builder",
        ["landing page software", "conversion page builder", "landing page creator"],
    ),
    "portfolio-website-builder": (
        "portfolio website builder",
        ["photography website builder", "online portfolio maker", "portfolio site builder"],
    ),
    "website-builder": (
        "website builder",
        ["AI website builder", "best website builder", "website builder tool"],
    ),
    # cms (verify KEYWORD-RESEARCH.md)
    "content-management-system": (
        "content management system",
        ["CMS", "best CMS", "content management software"],
    ),
    "enterprise-cms": (
        "enterprise CMS",
        ["DXP", "digital experience platform", "enterprise content management"],
    ),
    "headless-cms": (
        "headless CMS",
        ["API-first CMS", "headless content management", "content API CMS"],
    ),
    "open-source-cms": (
        "open source CMS",
        ["self-hosted CMS", "open source content management system", "free CMS"],
    ),
    # hr-recruiting
    "hr-assistant": (
        "AI HR assistant",
        ["AI HR tools", "HR AI assistant", "AI human resources assistant"],
    ),
    "interview-assistant": (
        "AI interview assistant",
        ["AI interview tool", "interview AI assistant", "AI interview prep"],
    ),
    "linkedin": (
        "LinkedIn AI tools",
        ["AI for LinkedIn", "LinkedIn automation AI", "AI LinkedIn assistant"],
    ),
    "recruiting": (
        "AI recruiting",
        ["AI recruitment tools", "AI hiring tools", "AI talent acquisition"],
    ),
    # infrastructure
    "ai-training-data": (
        "AI training data platform",
        ["AI training data", "machine learning data platform", "LLM training data"],
    ),
    "api": (
        "unified AI API",
        ["AI API platform", "LLM API gateway", "AI API aggregator"],
    ),
    "authentication": (
        "authentication",
        ["CIAM", "identity and access management", "customer identity access management"],
    ),
    "inference-infrastructure": (
        "AI inference infrastructure",
        ["AI inference platform", "LLM inference hosting", "AI model hosting infrastructure"],
    ),
    # productivity
    "ai-scheduling": (
        "AI scheduling",
        ["AI calendar", "AI scheduling assistant", "AI meeting scheduler"],
    ),
    "note-taker": (
        "AI note taker",
        ["AI meeting notes", "AI meeting transcription", "AI meeting assistant"],
    ),
    "productivity": (
        "AI productivity tools",
        ["AI productivity", "best AI productivity tools", "AI productivity software"],
    ),
    "project-management": (
        "AI project management",
        ["AI project management tools", "project management AI", "AI PM tools"],
    ),
    # search-geo
    "ai-traffic-and-citation-sources": (
        "AI traffic sources",
        ["AI citation sources", "AI search traffic", "AI referral traffic"],
    ),
    "ai-visibility": (
        "AI visibility",
        ["AI brand visibility", "visibility in AI search", "AI search visibility"],
    ),
    "geo": (
        "generative engine optimization",
        ["GEO SEO", "AI SEO", "generative search optimization"],
    ),
    "search-engine": (
        "AI search engine",
        ["conversational AI search", "AI powered search", "AI answer engine"],
    ),
    # healthcare
    "healthcare": (
        "AI healthcare",
        ["AI in healthcare", "healthcare AI", "artificial intelligence healthcare"],
    ),
    "medical-scribe": (
        "AI medical scribe",
        ["medical scribe AI", "AI scribe for doctors", "clinical documentation AI"],
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


def verify_keyword_research(slug: str, entry: dict) -> dict | None:
    """Cross-check website-builder / cms slugs against KEYWORD-RESEARCH.md SSOT."""
    notes = {
        "blog-website-builder": "SSOT: blog website builder > blogging platform; verify ~900k",
        "ecommerce-website-builder": "SSOT: online store platform vs ecommerce website builder dual primary",
        "landing-page-builder": "SSOT: landing page builder primary",
        "portfolio-website-builder": "SSOT: portfolio website builder; photography as secondary",
        "website-builder": "SSOT: website builder hub primary",
        "content-management-system": "SSOT: content management system / CMS hub",
        "enterprise-cms": "SSOT: enterprise CMS / DXP",
        "headless-cms": "SSOT: headless CMS primary",
        "open-source-cms": "SSOT: open source CMS primary",
    }
    if slug not in notes:
        return None

    primary = entry["primary"]["approx_results"]
    alts = {a["query"]: a["approx_results"] for a in entry["alternatives"]}
    note = notes[slug]
    still_holds = entry["verdict"] in ("OK", "AMBIGUOUS", "NEEDS_REVIEW")
    if slug == "ecommerce-website-builder":
        ecom = alts.get("ecommerce website builder")
        store = primary
        still_holds = ecom is not None and store is not None
        note += f"; store={store:,} ecom={ecom:,}"
    elif slug == "portfolio-website-builder":
        photo = alts.get("photography website builder")
        still_holds = primary is not None and (photo is None or primary >= photo * 0.3)
        note += f"; portfolio={primary:,} photography={photo:,}"
    elif slug == "headless-cms":
        api_first = alts.get("API-first CMS")
        still_holds = primary is not None and (api_first is None or primary >= api_first)
        note += f"; headless={primary:,} api-first={api_first:,}"

    return {"ssot_note": note, "ssot_still_holds": still_holds}


def main():
    batch = json.loads(BATCH_PATH.read_text(encoding="utf-8"))
    results = []
    summary = {"total": 0, "OK": 0, "SWITCH": 0, "AMBIGUOUS": 0, "NEEDS_REVIEW": 0}
    switch_items = []

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
        print(f"[{i+1}/{len(batch)}] {slug}: primary='{primary_q}'")

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

        ssot = verify_keyword_research(slug, entry)
        if ssot:
            entry["keyword_research_verification"] = ssot

        results.append(entry)
        summary["total"] += 1
        summary[v] += 1
        if v == "SWITCH":
            switch_items.append(
                {
                    "slug": slug,
                    "current_primary": current_primary,
                    "suggested_primary": suggested,
                    "reason": reason,
                }
            )
        print(f"  -> {v}: {reason}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "batch": "batch6_misc",
        "clusters": [
            "chat-social",
            "website-builder",
            "cms",
            "hr-recruiting",
            "infrastructure",
            "productivity",
            "search-geo",
            "healthcare",
        ],
        "methodology": "Bing approximate result counts; primary vs 2-4 same-intent alternatives",
        "audited_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "summary": summary,
        "switch_items": switch_items,
        "results": results,
    }
    OUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nWrote", OUT_PATH)
    print(json.dumps(summary, indent=2))
    if switch_items:
        print("\nSWITCH items:")
        for s in switch_items:
            print(f"  - {s['slug']}: {s['suggested_primary']}")


if __name__ == "__main__":
    main()
