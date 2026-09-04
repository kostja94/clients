#!/usr/bin/env python3
"""Merge all batch keyword audit results into one report."""
import json
from collections import Counter
from pathlib import Path

RESULTS_DIR = Path("e:/clients/temp/kw-audit-results")
OUT = Path("e:/clients/temp/kw-audit-results/MERGED_AUDIT_REPORT.json")


def normalize_entry(r: dict, batch: str) -> dict:
    slug = r["slug"]
    verdict = r.get("verdict", "UNKNOWN")

    # batch1 format
    if "candidates_tested" in r:
        tested = r["candidates_tested"]
        counts = []
        for t in tested:
            raw = t.get("bing_approx", "")
            n = int(raw.replace("About ", "").replace(",", "").replace(" results", "")) if "About" in raw else None
            counts.append({"query": t["keyword"], "approx_results": n})
        primary_q = r.get("current_primary", counts[0]["query"] if counts else "")
        recommended = r.get("recommended_primary")
        highest = r.get("highest_volume_keyword")
        notes = r.get("notes", "")
        return {
            "slug": slug,
            "batch": batch,
            "verdict": verdict,
            "current_primary": primary_q,
            "recommended_primary": recommended,
            "highest_volume_keyword": highest,
            "candidates": counts,
            "notes": notes,
        }

    # batch6 format
    if "primary" in r and isinstance(r["primary"], dict):
        primary = r["primary"]
        alts = r.get("alternatives", [])
        candidates = [{"query": primary["query"], "approx_results": primary.get("approx_results")}]
        candidates += [{"query": a["query"], "approx_results": a.get("approx_results")} for a in alts]
        return {
            "slug": slug,
            "batch": batch,
            "verdict": verdict,
            "current_primary": r.get("current_primary", primary["query"]),
            "recommended_primary": r.get("suggested_primary"),
            "highest_volume_keyword": max(candidates, key=lambda x: x.get("approx_results") or 0)["query"] if candidates else None,
            "candidates": candidates,
            "notes": r.get("reason", ""),
        }

    # batch3+ refined format
    if "primary_query" in r:
        candidates = [{"query": r["primary_query"], "approx_results": r.get("primary_approx_results")}]
        for a in r.get("alternatives", []):
            candidates.append({"query": a["query"], "approx_results": a.get("approx_results")})
        return {
            "slug": slug,
            "batch": batch,
            "verdict": verdict,
            "current_primary": r.get("current_primary", r["primary_query"]),
            "recommended_primary": r.get("recommended_primary"),
            "highest_volume_keyword": max(candidates, key=lambda x: x.get("approx_results") or 0)["query"] if candidates else None,
            "candidates": candidates,
            "notes": r.get("rationale", r.get("notes", "")),
            "flags": r.get("flags", []),
        }

    return {"slug": slug, "batch": batch, "verdict": verdict, "raw": r}


def main():
    merged = {}
    for f in sorted(RESULTS_DIR.glob("batch*_results.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        batch = data.get("batch", f.stem) if isinstance(data, dict) else f.stem
        items = data if isinstance(data, list) else data.get("results", [])
        for r in items:
            if not isinstance(r, dict) or "slug" not in r:
                continue
            merged[r["slug"]] = normalize_entry(r, batch)

    verdicts = Counter(v["verdict"] for v in merged.values())
    switch = [v for v in merged.values() if v["verdict"] == "SWITCH"]
    ambiguous = [v for v in merged.values() if v["verdict"] == "AMBIGUOUS"]
    needs_review = [v for v in merged.values() if v["verdict"] == "NEEDS_REVIEW"]
    ok = [v for v in merged.values() if v["verdict"] == "OK"]

    report = {
        "audit_date": "2026-09-03",
        "methodology": "Bing EN-US approximate result counts (directional proxy per intent-near-keyword-volume.md; NOT precise MSV)",
        "caveat": "Bing caps many broad AI queries at ~509,000; SWITCH on capped counts requires SERP title review",
        "total_slugs": len(merged),
        "verdict_summary": dict(verdicts),
        "switch_recommendations": sorted(switch, key=lambda x: x["slug"]),
        "ambiguous_slugs": sorted([x["slug"] for x in ambiguous]),
        "needs_review_slugs": sorted([x["slug"] for x in needs_review]),
        "ok_count": len(ok),
        "results": sorted(merged.values(), key=lambda x: x["slug"]),
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "total": len(merged),
        "verdicts": dict(verdicts),
        "switch_count": len(switch),
        "ambiguous_count": len(ambiguous),
        "needs_review_count": len(needs_review),
        "output": str(OUT),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
