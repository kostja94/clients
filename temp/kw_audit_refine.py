#!/usr/bin/env python3
"""Post-process batch3 audit: flag Bing 509k cap, refine verdicts."""
import json
from pathlib import Path

CAP = 509_000
SUSPICIOUS_LOW = 100  # likely parse errors

path = Path("e:/clients/temp/kw-audit-results/batch3_voice_coding_marketing_results.json")
data = json.loads(path.read_text(encoding="utf-8"))

def is_capped(n):
    return n is not None and n >= CAP

def refine_verdict(entry):
    p = entry["primary_approx_results"]
    alts = entry["alternatives"]
    alt_counts = [(a["query"], a["approx_results"]) for a in alts]
    valid = [(q, c) for q, c in alt_counts if c is not None]

    flags = []
    if is_capped(p):
        flags.append("primary_capped")
    capped_alts = [q for q, c in valid if is_capped(c)]
    if capped_alts:
        flags.append("alt_capped")
    if p is not None and p <= SUSPICIOUS_LOW:
        flags.append("primary_suspicious_low")

    # Recalculate with cap awareness
    non_capped = [(q, c) for q, c in valid if not is_capped(c)]
    non_capped_primary = None if is_capped(p) else p

    if p is None and not valid:
        v, rationale, rec = "NEEDS_REVIEW", "No Bing counts retrieved", None
    elif is_capped(p) and all(is_capped(c) for _, c in valid):
        v, rationale, rec = "AMBIGUOUS", f"Primary and all alts hit Bing ~{CAP:,} cap — need SERP title review", None
    elif is_capped(p) and non_capped:
        best_q, best_c = max(non_capped, key=lambda x: x[1])
        v, rationale, rec = "NEEDS_REVIEW", f"Primary capped ~{CAP:,}; best non-capped alt '{best_q}' ~{best_c:,}", best_q
    elif non_capped_primary is not None and non_capped:
        best_q, best_c = max(non_capped, key=lambda x: x[1])
        if best_c >= non_capped_primary * 3:
            v, rationale, rec = "SWITCH", f"'{best_q}' ~{best_c:,} >> primary ~{non_capped_primary:,} (>3x, non-capped)", best_q
        elif all(non_capped_primary >= c * 2 for _, c in non_capped):
            v, rationale, rec = "OK", f"Primary ~{non_capped_primary:,} dominates non-capped alts", None
        elif best_c >= non_capped_primary * 0.5:
            v, rationale, rec = "AMBIGUOUS", f"Primary ~{non_capped_primary:,} vs '{best_q}' ~{best_c:,} within ~2x", None
        elif best_c > non_capped_primary:
            v, rationale, rec = "SWITCH", f"'{best_q}' ~{best_c:,} > primary ~{non_capped_primary:,}", best_q
        else:
            v, rationale, rec = "OK", f"Primary ~{non_capped_primary:,} >= best alt ~{best_c:,}", None
    elif p is not None and p <= SUSPICIOUS_LOW and valid:
        best_q, best_c = max(valid, key=lambda x: x[1] if x[1] else 0)
        if best_c and best_c > p * 3:
            v, rationale, rec = "SWITCH", f"Primary suspiciously low ~{p:,}; '{best_q}' ~{best_c:,}", best_q
        else:
            v, rationale, rec = "NEEDS_REVIEW", f"Primary suspiciously low ~{p:,} — verify parse", None
    else:
        v, rationale, rec = entry["verdict"], entry["rationale"], entry.get("recommended_primary")

    entry["flags"] = flags
    entry["verdict"] = v
    entry["rationale"] = rationale
    entry["recommended_primary"] = rec
    return entry

results = [refine_verdict(r) for r in data["results"]]

summary = {
    "batch": "batch3_voice_coding_marketing",
    "total": len(results),
    "audit_date": "2026-09-03",
    "method": "Bing EN-US approximate result count (directional proxy, not MSV)",
    "caveat": "Bing frequently caps broad AI queries at ~509,000; capped counts flagged; SWITCH/OK based on non-capped comparisons where possible.",
    "verdicts": {},
    "switch_recommendations": [],
    "ambiguous": [],
    "needs_review": [],
    "ok": [],
}

for r in results:
    summary["verdicts"][r["verdict"]] = summary["verdicts"].get(r["verdict"], 0) + 1
    if r["verdict"] == "SWITCH":
        summary["switch_recommendations"].append({
            "slug": r["slug"],
            "from": r["primary_query"],
            "to": r["recommended_primary"],
            "rationale": r["rationale"],
            "flags": r.get("flags", []),
        })
    elif r["verdict"] == "AMBIGUOUS":
        summary["ambiguous"].append(r["slug"])
    elif r["verdict"] == "NEEDS_REVIEW":
        summary["needs_review"].append(r["slug"])
    elif r["verdict"] == "OK":
        summary["ok"].append(r["slug"])

output = {"summary": summary, "results": results}
path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=2, ensure_ascii=False))
