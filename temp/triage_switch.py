#!/usr/bin/env python3
"""Split SWITCH recommendations into high/low confidence for presentation."""
from __future__ import annotations

import json
import re
from pathlib import Path

SRC = Path(r"e:/clients/temp/kw-audit-results/FULL_PRIMARY_KEYWORD_AUDIT.json")
OUT = Path(r"e:/clients/temp/kw-audit-results/SWITCH_TRIAGE.json")

# Patterns that often mean polluted / brand / too-broad SWITCH
LOW_PATTERNS = [
    r"\bgoogle\b",
    r"\bopenai\b",
    r"\bwhat cms\b",
    r"^shop with ai$",
    r"^digital employee$",
    r"^community platform$",
    r"^documentation platform$",
    r"^website indexing$",
    r"^code sandbox",
    r"^agentic iam$",
    r"^google a2a$",
    r"^llm agent runtime$",
    r"^memory layer for ai agents$",
]

# High-confidence: clear morphology / established category head term flips
HIGH_HINTS = [
    "ecommerce website builder",
    "AI desktop agent",
    "Team AI Agent",
    "MCP agent skills",
    "AI workflow automation",
    "how to add payments to vibe coded app",
    "AI avatar generator",
    "image to video AI",
    "text to video AI",
    "lip sync AI",
    "AI Audio Translator",
    "AI Video Translator",
    "multimodal LLM",
    "LLM for coding",
    "LLM for math",
    "reasoning model",
    "AI Gateway",
    "AI inference platform",
    "AI tools directory",
    "AI scheduling assistant",
    "AI video clipper",
    "OG image generator",
    "AI translator",
    "URL to Markdown",
    "world model AI",
    "agentic browser",
    "live AI video generation",
    "AI short drama generator",
    "3D modeling",
    "AI 3D model generator",
    "AI in education",
    "AI in healthcare",
    "AI second brain",
    "Agentic advertising",
]


def main():
    report = json.loads(SRC.read_text(encoding="utf-8"))
    high, low, mid = [], [], []
    for s in report["switch_recommendations"]:
        rec = (s.get("recommended_primary") or "").strip()
        low_hit = any(re.search(p, rec, re.I) for p in LOW_PATTERNS)
        high_hit = any(rec.lower() == h.lower() or h.lower() in rec.lower() for h in HIGH_HINTS)
        if low_hit and not high_hit:
            low.append(s)
        elif high_hit:
            high.append(s)
        else:
            mid.append(s)

    triage = {
        "audit_date": report["audit_date"],
        "total_switch": len(report["switch_recommendations"]),
        "high_confidence": high,
        "review_needed": mid,
        "likely_false_positive": low,
        "verdict_summary": report["verdict_summary"],
        "ok_count": report["ok_count"],
        "keep_intent_count": len(report["keep_intent"]),
        "ambiguous_count": len(report["ambiguous"]),
    }
    OUT.write_text(json.dumps(triage, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "high": len(high),
                "mid": len(mid),
                "low": len(low),
                "high_slugs": [x["slug"] for x in high],
                "low_slugs": [x["slug"] for x in low],
                "mid_slugs": [x["slug"] for x in mid],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
