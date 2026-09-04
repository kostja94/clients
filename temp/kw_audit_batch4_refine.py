#!/usr/bin/env python3
"""Post-process batch4 audit: handle Bing ~509k ceiling, refine verdicts."""
import json
from pathlib import Path

INP = Path(r"e:/clients/temp/kw-audit-results/batch4_edu_3d_enterprise_results.json")
BING_CEILING = 500_000

# Manual intent-aware overrides after ceiling filtering
OVERRIDES = {
    "ai-homework-helper": (
        "OK",
        "Current 'AI homework helper' (78,900) is the correct head term; higher counts for "
        "'photo math solver' / 'AI homework solver' reflect adjacent calculator intent, not same SERP.",
    ),
    "ai-tutor": (
        "SWITCH",
        "'AI tutoring' (~509k ceiling) and related forms dominate 'AI tutor' (46,800). "
        "Recommend primary 'AI tutoring' — distinct from homework-helper intent.",
    ),
    "quiz-generator": (
        "AMBIGUOUS",
        "'AI quiz maker' (10,100) slightly beats 'AI quiz generator' (7,570); both are valid same-intent heads. "
        "'AI assessment generator' hits ceiling but skews broader B2B intent.",
    ),
    "3d-model-generator": (
        "SWITCH",
        "'text to 3D AI' (147,000) and 'image to 3D' (51,500) outperform 'AI 3D model generator' (16,700). "
        "Recommend dual primary: 'text to 3D / image to 3D' (matches current narrative).",
    ),
    "3d-modelling": (
        "SWITCH",
        "'3D modeling tools' (149,000) and 'DCC software' (142,000) far exceed '3D modelling software' (10,700). "
        "Recommend US spelling '3D modeling tools' as primary.",
    ),
    "documentation": (
        "AMBIGUOUS",
        "'docs as code tools' (323,000) leads but is a narrower sub-intent; 'developer documentation tools' (190,000) "
        "matches page scope. Keep current unless targeting docs-as-code niche.",
    ),
    "knowledge-base": (
        "OK",
        "'AI knowledge base' and 'AI knowledge management' both hit Bing ceiling — indistinguishable. "
        "Keep 'AI knowledge base' per Alignify convention (RAG knowledge base lower at 70,400).",
    ),
    "legal": (
        "AMBIGUOUS",
        "'AI for lawyers' hits ceiling; measurable 'legal AI tools' (121,000) is strong alt. "
        "Either works; ceiling prevents clear winner.",
    ),
    "memory": (
        "OK",
        "'AI memory' (45,300) leads among differentiated counts; 'AI second brain' (10,800) is lower. "
        "Ceiling hits on PKM variants are not same consumer intent.",
    ),
    "ocr": (
        "OK",
        "'OCR software' (92,500) has solid volume; 'AI OCR' hits ceiling but page covers OCR category broadly. "
        "Keep 'OCR software' / 'AI OCR' dual acceptable.",
    ),
    "ai-for-science": (
        "NEEDS_REVIEW",
        "'AI4S' nearly zero volume (51). Keep 'AI for science'; avoid AI4S as primary keyword.",
    ),
    "virtual-staging": (
        "OK",
        "'AI virtual staging' hits Bing ceiling; measurable 'virtual staging software' (207,000) is lower. "
        "Keep AI-branded primary per listing-intent scope.",
    ),
}


def is_ceiling(n: int | None) -> bool:
    return n is not None and n >= BING_CEILING


def auto_verdict(slug: str, current: str, counts: dict[str, int | None]) -> tuple[str, str]:
    if slug in OVERRIDES:
        return OVERRIDES[slug]

    valid = {k: v for k, v in counts.items() if v is not None}
    cur = valid.get(current)
    ceiling_kws = [k for k, v in valid.items() if is_ceiling(v)]
    measurable = {k: v for k, v in valid.items() if not is_ceiling(v)}

    if cur is not None and is_ceiling(cur):
        if len(ceiling_kws) >= 2:
            return (
                "AMBIGUOUS",
                f"Current '{current}' and {len(ceiling_kws)-1} alt(s) hit Bing ~509k+ ceiling — cannot rank at this granularity.",
            )
        return "OK", f"Current '{current}' hits Bing ceiling; no measurable alt beats it."

    if not measurable:
        return "NEEDS_REVIEW", "All queries hit Bing ceiling or failed; no differentiated counts."

    if cur is None:
        best_kw, best_val = max(measurable.items(), key=lambda x: x[1])
        return "NEEDS_REVIEW", f"Current primary not in measurable set; best measurable: '{best_kw}' ({best_val:,})."

    ranked = sorted(measurable.items(), key=lambda x: x[1], reverse=True)
    best_kw, best_val = ranked[0]
    second_val = ranked[1][1] if len(ranked) > 1 else 0

    if best_kw == current:
        if second_val and second_val / cur >= 0.85:
            return "AMBIGUOUS", (
                f"'{current}' ({cur:,}) leads narrowly over '{ranked[1][0]}' ({second_val:,})."
            )
        return "OK", f"Current '{current}' ({cur:,}) has highest differentiated Bing volume."

    ratio = best_val / cur if cur else float("inf")
    if ratio >= 2.0 or (ratio >= 1.5 and best_val - cur >= 10000):
        return "SWITCH", f"'{best_kw}' ({best_val:,}) beats '{current}' ({cur:,}) — {ratio:.1f}x."

    if ratio >= 1.2:
        return "AMBIGUOUS", (
            f"'{best_kw}' ({best_val:,}) moderately exceeds '{current}' ({cur:,}); {ratio:.1f}x."
        )

    return "OK", f"Current '{current}' ({cur:,}) competitive vs best alt '{best_kw}' ({best_val:,})."


def main():
    data = json.loads(INP.read_text(encoding="utf-8"))
    summary = {"total": 22, "OK": 0, "SWITCH": 0, "AMBIGUOUS": 0, "NEEDS_REVIEW": 0}

    for r in data["results"]:
        counts = r["bing_counts"]
        capped = [k for k, v in counts.items() if is_ceiling(v)]
        r["bing_ceiling_note"] = (
            f"Counts ≥{BING_CEILING:,} treated as Bing approximate ceiling (underreporting differentiation)."
        )
        r["capped_keywords"] = capped
        v, reason = auto_verdict(r["slug"], r["current_primary"], counts)
        r["verdict"] = v
        r["reason"] = reason
        summary[v] += 1

    data["methodology"] = (
        "For each slug: Bing-search current primary vs 2–4 same-intent English alternatives; "
        "compare approximate result counts (sb_count). Counts ≥500k treated as Bing ceiling. "
        "Verdict: OK / SWITCH / AMBIGUOUS / NEEDS_REVIEW."
    )
    data["bing_ceiling_threshold"] = BING_CEILING
    data["summary"] = {
        **summary,
        "switch_candidates": [r["slug"] for r in data["results"] if r["verdict"] == "SWITCH"],
        "ambiguous": [r["slug"] for r in data["results"] if r["verdict"] == "AMBIGUOUS"],
        "needs_review": [r["slug"] for r in data["results"] if r["verdict"] == "NEEDS_REVIEW"],
    }
    INP.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(data["summary"], indent=2))


if __name__ == "__main__":
    main()
