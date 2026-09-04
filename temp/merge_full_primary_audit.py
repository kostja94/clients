#!/usr/bin/env python3
"""Finalize agent-cluster verdicts from Bing raw + merge all subagent batches."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"e:/clients/temp/kw-audit-results")
SUB = ROOT / "subagent"
BATCHES = Path(r"e:/clients/temp/kw-audit-batches/subagent")
OUT_AGENT = SUB / "agent.json"
OUT_MERGED = ROOT / "FULL_PRIMARY_KEYWORD_AUDIT.json"

CAP = 450_000  # treat >= as Bing approximate ceiling / polluted

# Manual intent-aware overrides when Bing SERP is polluted or prior research exists.
# Format: slug -> (verdict, recommended, reason)
OVERRIDES = {
    "agent-billing": (
        "OK",
        "AI agent billing",
        "Prior same-intent deep research: 'AI agent billing'/'AI agent billing software' is the natural commercial head; 'agent monetization' (~4.3k) is weak and fuzzy. Bing 509k caps are generic-AI pollution, not evidence either way.",
    ),
    "agent-for-desktop": (
        "SWITCH",
        "AI desktop agent",
        "Bing has no clean signal ('Agent on desktop' = MS fallback; 'AI desktop agent' capped by generic AI). Word-order + prior audit favor 'AI desktop agent' as the natural category head.",
    ),
    "agent-identity": (
        "KEEP_INTENT",
        "AI Agent Identity",
        "All candidates are polluted or MS fallback (agentic IAM = generic Agentic AI). Emerging category with no usable Bing/MSV; keep current term, re-audit later.",
    ),
    "agent-memory": (
        "SWITCH",
        "AI agent memory",
        "Cleanest on-intent signal is 'agent memory' (~13.1k, GitHub agentmemory/TencentDB) vs current 'Agent Memory Layer' (MS fallback, not a natural query). Use 'AI agent memory' as branded head + 'agent memory' secondary.",
    ),
    "agent-runtime": (
        "KEEP_INTENT",
        "AI Agent Runtime",
        "Bing capped/polluted across candidates ('agent runtime' 5.1k on-intent but low). Term is the accepted category name; keep.",
    ),
    "agent-sandbox": (
        "KEEP_INTENT",
        "AI Agent Sandbox",
        "All candidates polluted (game/VS Code/generic AI) or fallback. Emerging term; keep current.",
    ),
    "agent-skills": (
        "KEEP_INTENT",
        "Agent Skills",
        "'Agent Skills' ~43.3k is the cleanest on-intent signal (GitHub agent-skills / SkillsMP); 'MCP skills' 86.9k is MIXED (protocol + motor-carrier), 'Claude agent skills' is brand. Keep 'Agent Skills' head.",
    ),
    "agent-to-agent": (
        "SWITCH",
        "agent to agent",
        "'agent to agent' ~132k on-intent (A2A protocol/Microsoft Learn/Google) > 'A2A Agent Network' ~92.5k. Google A2A 2.17M is brand pollution — never use. Use 'agent to agent' head, A2A as secondary.",
    ),
    "agentic-commerce": (
        "KEEP_INTENT",
        "Agentic Commerce",
        "Category term matches IBM/McKinsey on-intent pages (~15.6k); 'agentic shopping/checkout' are generic-Agentic-AI pollution. Keep.",
    ),
    "agentic-payments": (
        "KEEP_INTENT",
        "Agentic Payments",
        "Bing polluted but WebSearch titles are on-intent (Fireblocks/ACI/AWS). 'x402 payments' 20.7k is a protocol subset. Keep category head.",
    ),
    "ai-employee": (
        "KEEP_INTENT",
        "AI Employee",
        "'digital employee' 211k is dictionary pollution; 'AI teammate' ~48.1k is on-intent (Asana/Salesforce) but narrower chat-native subset; 'AI coworker' 58. AI Employee stays the brand/站内 term — add 'AI teammate' as secondary.",
    ),
    "ai-shopping": (
        "KEEP_INTENT",
        "AI Shopping",
        "All candidates polluted ('shop with AI' = SHOP.COM/Walmart; others generic-AI cap). Keep constructed but internally-consistent head; re-audit with SERP tools later.",
    ),
    "browser": (
        "SWITCH",
        "agentic browser",
        "'agentic browser' ~125k on-intent vs 'AI browser' ~61.8k on-intent; KB covers built-in agentic browsers. Switch head, keep 'AI browser' secondary.",
    ),
    "data-engineering-agent": (
        "AMBIGUOUS",
        "Data Engineering Agent",
        "Bing unusable: 'Data Engineering Agent' 296k is 'data'-word dictionary pollution; AI variants capped by generic AI. New category — keep current until reliable MSV exists.",
    ),
    "expert-agent": (
        "AMBIGUOUS",
        "Expert Agent",
        "'Expert Agent'/'expert AI agent' 274k are dictionary-expert pollution; AI variants capped. Emerging term; keep.",
    ),
    "multi-agent": (
        "KEEP_INTENT",
        "Multi-Agent Systems",
        "'Multi-Agent Systems' 104k (Multi- dictionary heavy but term is the standard academic/category head); 'AI multi-agent' capped. Keep.",
    ),
    "openclaw-alternatives": (
        "OK",
        "OpenClaw alternatives",
        "~78.5k on-intent (OpenClaw brand pages); alternatives query matches page intent. Keep.",
    ),
    "vibe-coding-payments": (
        "KEEP_INTENT",
        "how to add payments to vibe coded app",
        "All vibe-coding-payment queries polluted (Vibe music app / VIBE.com / ADD-vs-ADHD). Page maps to a how-to route; keep natural how-to phrasing as keyword intent, no reliable MSV yet.",
    ),
    "work-agent": (
        "KEEP_INTENT",
        "Work Agent",
        "'Work Agent'/'work AI agent' 426k are WORK-dictionary/Rihanna pollution; 'AI Work Agent' capped. Keep head; no usable SERP signal for this new category.",
    ),
    "workflow": (
        "SWITCH",
        "AI workflow",
        "'AI workflow' ~45.5k on-intent (2026 reviews) > 'Workflow automation' ~28k (Zapier-class, broader non-AI). 'AI workflow automation' capped/polluted. Use 'AI workflow' as head.",
    ),
    "workspace-agent": (
        "KEEP_INTENT",
        "Workspace Agent",
        "Bing polluted by Google Workspace / Microsoft Teams brands ('Team AI Agent' 333k = Microsoft Teams). OpenAI Workspace Agents supports the term; keep.",
    ),
    "world-model": (
        "OK",
        "World model",
        "'World model'/'world models' ~40-43k on-intent (arXiv/知乎/学术); 'world model AI' 1.38M is world-news pollution. Keep academic head.",
    ),
}


def polluted(titles: str | None) -> bool:
    if not titles:
        return False
    t = titles.lower()
    markers = ("openai", "google gemini", "chatgpt: chat", "what is artificial intelligence", "polluted_cap", "ms fallback")
    return any(m in t for m in markers)


def score_row(row: dict) -> float | None:
    n = row.get("quoted_results")
    if n is None:
        return None
    if polluted(row.get("serp_titles")) and n >= CAP:
        return None  # ignore polluted ceiling
    if n >= CAP:
        return CAP  # capped but not obviously polluted — weak signal
    return float(n)


def finalize_agent() -> dict:
    raw = json.loads((SUB / "agent_bing_raw.json").read_text(encoding="utf-8"))
    meta = {r["slug"]: r for r in json.loads((BATCHES / "agent.json").read_text(encoding="utf-8"))}
    results = []
    for slug, rows in raw.items():
        current = meta.get(slug, {}).get("current_primary") or rows[0]["keyword"]
        candidates = []
        scored = []
        for r in rows:
            s = score_row(r)
            candidates.append(
                {
                    "keyword": r["keyword"],
                    "volume_signal": r.get("quoted_results"),
                    "source": "Bing quoted About-N (proxy)",
                    "serp_title_note": (r.get("serp_titles") or "")[:240],
                    "usable_score": s,
                }
            )
            if s is not None:
                scored.append((r["keyword"], s))

        if slug in OVERRIDES:
            verdict, rec, reason = OVERRIDES[slug]
        else:
            # default heuristic
            usable = sorted(scored, key=lambda x: x[1], reverse=True)
            if not usable:
                verdict, rec, reason = "AMBIGUOUS", current, "All candidates capped/polluted; keep current pending SERP title review."
            else:
                best_kw, best_n = usable[0]
                cur_score = next((s for k, s in scored if k.lower() == current.lower()), None)
                if cur_score is None:
                    # current not measurable; if best is clearly same stem keep or switch
                    if best_n >= 2 * 10000 and best_kw.lower() != current.lower():
                        verdict, rec, reason = (
                            "SWITCH",
                            best_kw,
                            f"Current primary unmeasurable/polluted; highest usable same-batch phrase is '{best_kw}' (~{int(best_n):,}).",
                        )
                    else:
                        verdict, rec, reason = "AMBIGUOUS", current, "Current primary unmeasurable; no clear usable winner."
                elif best_kw.lower() == current.lower() or best_n < 1.5 * cur_score:
                    verdict, rec, reason = "OK", current, f"Current primary is among top usable signals (~{int(cur_score):,})."
                elif best_n >= 2 * cur_score:
                    # check if best is just a tool/software suffix of same stem
                    if current.lower() in best_kw.lower() and any(
                        suf in best_kw.lower() for suf in (" tool", " tools", " software", " platform")
                    ):
                        verdict, rec, reason = (
                            "KEEP_INTENT",
                            current,
                            f"'{best_kw}' higher (~{int(best_n):,}) but looks like tool-suffix inflation; keep category head '{current}'.",
                        )
                    else:
                        verdict, rec, reason = (
                            "SWITCH",
                            best_kw,
                            f"'{best_kw}' (~{int(best_n):,}) >=2x current '{current}' (~{int(cur_score):,}).",
                        )
                else:
                    verdict, rec, reason = (
                        "AMBIGUOUS",
                        current,
                        f"Best '{best_kw}' (~{int(best_n):,}) vs current (~{int(cur_score):,}) within 1.5–2x band.",
                    )

        highest = None
        if scored:
            highest = max(scored, key=lambda x: x[1])[0]
        results.append(
            {
                "slug": slug,
                "current_primary": current,
                "candidates": candidates,
                "highest_volume_same_intent": highest or rec,
                "verdict": verdict,
                "recommended_primary": rec,
                "reason": reason,
            }
        )

    payload = {
        "batch": "agent",
        "audit_date": "2026-09-03",
        "methodology": "Bing quoted About-N + SERP pollution filter + intent overrides; directional proxy not MSV",
        "slug_count": len(results),
        "summary": dict(Counter(r["verdict"] for r in results)),
        "results": sorted(results, key=lambda r: r["slug"]),
    }
    OUT_AGENT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


def merge_all(agent_payload: dict) -> dict:
    files = [
        ("agent", OUT_AGENT),
        ("video", SUB / "video.json"),
        ("image_3d", SUB / "image_3d.json"),
        ("voice_coding", SUB / "voice_coding.json"),
        ("edu_hr_health", SUB / "edu_hr_health.json"),
        ("mkt_design_text", SUB / "mkt_design_text.json"),
        ("llm_enterprise", SUB / "llm_enterprise.json"),
        ("infra_web_geo", SUB / "infra_web_geo.json"),
        ("cms_builder_misc", SUB / "cms_builder_misc.json"),
    ]
    merged = {}
    by_batch = {}
    for batch, path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        results = data.get("results", [])
        by_batch[batch] = {
            "count": len(results),
            "summary": dict(Counter(r.get("verdict") for r in results)),
        }
        for r in results:
            merged[r["slug"]] = {**r, "batch": batch}

    switch = [r for r in merged.values() if r.get("verdict") == "SWITCH"]
    keep = [r for r in merged.values() if r.get("verdict") == "KEEP_INTENT"]
    amb = [r for r in merged.values() if r.get("verdict") == "AMBIGUOUS"]
    ok = [r for r in merged.values() if r.get("verdict") == "OK"]

    report = {
        "audit_date": "2026-09-03",
        "scope": "Alignify/knowledge/tools primary keywords (seo/marketing/insights not on disk in this checkout)",
        "methodology": "Same-intent primary audit per intent-near-keyword-volume.md; Bing About-N / SERP-title / cited MSV as directional proxies — NOT precise MSV",
        "total_slugs": len(merged),
        "verdict_summary": dict(Counter(r["verdict"] for r in merged.values())),
        "by_batch": by_batch,
        "switch_recommendations": sorted(
            [
                {
                    "slug": r["slug"],
                    "batch": r["batch"],
                    "current_primary": r.get("current_primary"),
                    "recommended_primary": r.get("recommended_primary"),
                    "reason": r.get("reason"),
                }
                for r in switch
            ],
            key=lambda x: x["slug"],
        ),
        "keep_intent": sorted([r["slug"] for r in keep]),
        "ambiguous": sorted([r["slug"] for r in amb]),
        "ok_count": len(ok),
        "results": sorted(merged.values(), key=lambda r: r["slug"]),
    }
    OUT_MERGED.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main():
    agent = finalize_agent()
    report = merge_all(agent)
    print(json.dumps({"agent_summary": agent["summary"], "total": report["total_slugs"], "verdicts": report["verdict_summary"], "switch_count": len(report["switch_recommendations"])}, indent=2, ensure_ascii=False))
    print("SWITCH:")
    for s in report["switch_recommendations"]:
        print(f"  {s['slug']}: {s['current_primary']} -> {s['recommended_primary']}")


if __name__ == "__main__":
    main()
