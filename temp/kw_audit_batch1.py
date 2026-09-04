#!/usr/bin/env python3
"""Bing approximate result counts for Alignify KB batch1 (agent + root slugs)."""
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
            digits = re.sub(r"[^\d]", "", m.group(1))
            if digits:
                return int(digits)
    return None


def bing_count(query: str, retries: int = 2) -> int | None:
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}&setlang=en-us&cc=US&count=10"
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            return parse_count(html)
        except Exception:
            if attempt == retries:
                return None
            time.sleep(1.5)
    return None


def fmt_count(n: int | None) -> str:
    if n is None:
        return "UNKNOWN"
    return f"About {n:,} results"


# slug -> list of English keywords to test (first = normalized current primary)
SLUG_CANDIDATES = {
    "agent-for-desktop": [
        "desktop AI agent",
        "AI desktop agent",
        "computer use agent",
        "AI agent for desktop",
    ],
    "agent-identity": [
        "AI agent identity",
        "agent identity management",
        "AI agent IAM",
        "agentic access control",
    ],
    "agent-memory": [
        "AI agent memory",
        "agent memory layer",
        "AI agent memory tools",
        "LLM agent memory",
    ],
    "agent-runtime": [
        "AI agent runtime",
        "agent runtime platform",
        "AI agent orchestration",
        "agent execution runtime",
    ],
    "agent-sandbox": [
        "AI agent sandbox",
        "agent sandbox environment",
        "AI agent isolation",
        "secure agent sandbox",
    ],
    "agent-skills": [
        "agent skills",
        "AI agent skills",
        "agent skill marketplace",
        "MCP agent skills",
    ],
    "agent-to-agent": [
        "agent to agent protocol",
        "A2A agent protocol",
        "multi-agent communication",
        "agent interoperability",
    ],
    "ai-employee": [
        "AI employee",
        "AI coworker",
        "AI teammate",
        "AI employee software",
    ],
    "browser": [
        "AI browser",
        "AI web browser",
        "agentic browser",
        "AI browsing agent",
    ],
    "expert-agent": [
        "expert AI agent",
        "AI expert agent",
        "expert agent marketplace",
        "AI agent marketplace",
    ],
    "multi-agent": [
        "multi-agent systems",
        "multi-agent AI",
        "multi-agent framework",
        "multi-agent orchestration",
    ],
    "openclaw-alternatives": [
        "OpenClaw alternatives",
        "OpenClaw AI agent",
        "OpenClaw fork",
        "OpenClaw similar tools",
    ],
    "work-agent": [
        "work agent",
        "AI work agent",
        "workplace AI agent",
        "business AI agent",
    ],
    "workflow": [
        "AI workflow automation",
        "AI workflow",
        "agent workflow automation",
        "AI agent workflow",
    ],
    "workspace-agent": [
        "workspace agent",
        "team AI agent",
        "workspace AI agent",
        "collaborative AI agent",
    ],
    "agent-billing": [
        "AI agent billing",
        "agent billing software",
        "agent monetization",
        "AI agent billing platform",
    ],
    "agentic-commerce": [
        "agentic commerce",
        "AI agent commerce",
        "agentic shopping",
        "AI commerce agents",
    ],
    "agentic-payments": [
        "agentic payments",
        "AI agent payments",
        "agent payment infrastructure",
        "AI payment agents",
    ],
    "ai-shopping": [
        "AI shopping",
        "AI shopping assistant",
        "AI shopping agent",
        "AI product discovery",
    ],
    "animation-library": [
        "animation library",
        "Lottie animation library",
        "UI animation library",
        "motion design library",
    ],
    "data-engineering-agent": [
        "data engineering agent",
        "AI data engineering agent",
        "data pipeline agent",
        "AI data agent",
    ],
    "family-assistant": [
        "AI family assistant",
        "family AI assistant",
        "AI home assistant for families",
        "family organizer AI",
    ],
    "fashion": [
        "AI fashion tools",
        "AI fashion",
        "AI fashion design software",
        "fashion AI generator",
    ],
    "lifetime-deals": [
        "lifetime deals",
        "SaaS lifetime deals",
        "software lifetime deals",
        "AppSumo lifetime deals",
    ],
    "religion": [
        "AI religion",
        "AI spiritual assistant",
        "AI faith tools",
        "religious AI chatbot",
    ],
    "vibe-coding-payments": [
        "vibe coding payments",
        "AI app builder payments",
        "no-code app payments integration",
        "vibe coding Stripe",
    ],
    "world-model": [
        "world models AI",
        "AI world model",
        "world model machine learning",
        "world models robotics",
    ],
}


def verdict(counts: list[tuple[str, int | None]], current: str) -> tuple[str, str, str, str]:
    valid = [(k, v) for k, v in counts if v is not None]
    if not valid:
        return "NEEDS_REVIEW", current, current, "No Bing counts retrieved for any candidate"

    valid.sort(key=lambda x: x[1], reverse=True)
    top_kw, top_n = valid[0]
    cur_n = next((v for k, v in valid if k == current), None)
    if cur_n is None:
        return "NEEDS_REVIEW", top_kw, top_kw, f"Current test keyword '{current}' missing count; top={top_kw} ({top_n:,})"

    # Unnatural / very low volume niche
    if top_n < 500 and all(v < 2000 for _, v in valid):
        return "NEEDS_REVIEW", top_kw, top_kw, f"All counts very low (<2k); query may be unnatural or too niche"

    # Tied within 25%
    if cur_n >= top_n * 0.75:
        if cur_n == top_n:
            return "OK", top_kw, current, f"Current tied for top at {cur_n:,} results"
        return "OK", top_kw, current, f"Current within 25% of top ({cur_n:,} vs {top_n:,})"

    # Clear switch: alt >= 2x current
    if top_n >= cur_n * 2:
        return "SWITCH", top_kw, top_kw, f"'{top_kw}' ~{top_n:,} is >=2x current '{current}' ~{cur_n:,}"

    # Moderate gap or intent split
    second_n = valid[1][1] if len(valid) > 1 else 0
    if second_n >= cur_n * 0.67 and abs(top_n - second_n) / max(top_n, 1) < 0.3:
        return "AMBIGUOUS", top_kw, current, (
            f"Multiple strong candidates: {valid[0][0]} ({valid[0][1]:,}), "
            f"{valid[1][0]} ({valid[1][1]:,}); current {cur_n:,}"
        )

    if top_n > cur_n:
        return "AMBIGUOUS", top_kw, current, f"Top '{top_kw}' ({top_n:,}) moderately beats current ({cur_n:,}) but <2x"

    return "OK", top_kw, current, f"Current ({cur_n:,}) >= top alternative ({top_n:,})"


def main():
    batch_path = Path("e:/clients/temp/kw-audit-batches/batch1_agent_root.json")
    out_dir = Path("e:/clients/temp/kw-audit-results")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "batch1_agent_root_results.json"
    log_path = out_dir / "batch1_agent_root_log.txt"

    batch = json.loads(batch_path.read_text(encoding="utf-8"))
    results = []
    log_lines = []

    for i, item in enumerate(batch):
        slug = item["slug"]
        candidates = SLUG_CANDIDATES[slug]
        current = candidates[0]
        line = f"[{i+1}/27] {slug}..."
        print(line, flush=True)
        log_lines.append(line)

        tested = []
        for kw in candidates:
            n = bing_count(kw)
            tested.append({"keyword": kw, "bing_approx": fmt_count(n)})
            time.sleep(0.7)

        counts = [(t["keyword"], parse_count(t["bing_approx"]) if t["bing_approx"] != "UNKNOWN" else None) for t in tested]
        v, highest, recommended, notes = verdict(counts, current)

        results.append({
            "slug": slug,
            "current_primary": item["current_primary"],
            "candidates_tested": tested,
            "highest_volume_keyword": highest,
            "verdict": v,
            "recommended_primary": recommended,
            "notes": notes,
        })
        detail = f"  {v}: {notes}"
        print(detail, flush=True)
        log_lines.append(detail)

    summary = {"OK": 0, "SWITCH": 0, "AMBIGUOUS": 0, "NEEDS_REVIEW": 0}
    switch_items = []
    for r in results:
        summary[r["verdict"]] += 1
        if r["verdict"] == "SWITCH":
            switch_items.append({
                "slug": r["slug"],
                "current_primary": r["current_primary"],
                "recommended_primary": r["recommended_primary"],
                "highest_volume_keyword": r["highest_volume_keyword"],
                "notes": r["notes"],
            })

    output = {
        "batch": "batch1_agent_root",
        "methodology": "intent-near-keyword-volume via Bing EN-US approximate result counts (directional, not MSV)",
        "audit_date": "2026-09-03",
        "slug_count": len(results),
        "summary": summary,
        "switch_items": switch_items,
        "results": results,
    }
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    print("\n=== SUMMARY ===", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    print(f"Saved: {out_path}", flush=True)


if __name__ == "__main__":
    main()
