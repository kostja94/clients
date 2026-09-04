#!/usr/bin/env python3
"""Bing About-N-results proxy for Alignify AGENT cluster primary keywords.

Quoted phrase searches. Directional proxy, not MSV.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

PATTERNS = [
    re.compile(r"About\s+([\d,]+)\s+results", re.I),
    re.compile(r"([\d,]+)\s+results", re.I),
    re.compile(r'"totalEstimatedMatches"\s*:\s*(\d+)', re.I),
    re.compile(r"sb_count[^>]*>([^<]+)", re.I),
]


def parse_count(text: str):
    for pat in PATTERNS:
        m = pat.search(text)
        if m:
            digits = re.sub(r"[^\d]", "", m.group(1))
            if digits:
                n = int(digits)
                if 10 <= n <= 5_000_000_000:
                    return n
    return None


def bing_count(query: str, quoted: bool = True, retries: int = 3):
    q = f'"{query}"' if quoted else query
    url = (
        "https://www.bing.com/search?q="
        + urllib.parse.quote(q)
        + "&setlang=en-us&cc=US&count=10"
    )
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=25) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            n = parse_count(html)
            snippet = ""
            titles = re.findall(r"<h2[^>]*>\s*<a[^>]*>(.*?)</a>", html, re.I | re.S)
            clean = []
            for t in titles[:5]:
                t = re.sub(r"<[^>]+>", "", t)
                t = re.sub(r"\s+", " ", t).strip()
                if t:
                    clean.append(t)
            snippet = " | ".join(clean)[:400]
            return {"n": n, "titles": snippet, "html_len": len(html)}
        except Exception as e:
            last_err = str(e)
            time.sleep(1.2 * (attempt + 1))
    return {"n": None, "titles": f"error: {last_err}", "html_len": 0}


# slug -> candidates. First item is current_primary from JSON.
CANDIDATES = {
    "agent-billing": [
        "AI agent billing",
        "AI agent billing software",
        "agent monetization",
        "agent billing",
        "AI agent billing platform",
    ],
    "agent-for-desktop": [
        "Agent on desktop",
        "desktop AI agent",
        "AI desktop agent",
        "desktop agent",
        "computer use agent",
    ],
    "agent-identity": [
        "AI Agent Identity",
        "agent identity",
        "agent IAM",
        "agentic IAM",
        "AI agent identity management",
    ],
    "agent-memory": [
        "Agent Memory Layer",
        "AI agent memory",
        "agent memory",
        "memory layer for AI agents",
        "LLM agent memory",
    ],
    "agent-runtime": [
        "AI Agent Runtime",
        "agent runtime",
        "AI agent runtime",
        "agent execution runtime",
        "LLM agent runtime",
    ],
    "agent-sandbox": [
        "AI Agent Sandbox",
        "agent sandbox",
        "AI agent sandbox",
        "sandbox for AI agents",
        "code sandbox AI agent",
    ],
    "agent-skills": [
        "Agent Skills",
        "AI agent skills",
        "Claude agent skills",
        "agent skills marketplace",
        "MCP skills",
    ],
    "agent-to-agent": [
        "A2A Agent Network",
        "agent to agent",
        "A2A protocol",
        "agent-to-agent communication",
        "Google A2A",
    ],
    "agentic-commerce": [
        "Agentic Commerce",
        "agentic shopping",
        "AI agent commerce",
        "agentic checkout",
        "agent commerce",
    ],
    "agentic-payments": [
        "Agentic Payments",
        "AI agent payments",
        "agentic payment",
        "agent payments",
        "x402 payments",
    ],
    "ai-employee": [
        "AI Employee",
        "AI coworker",
        "AI teammate",
        "digital employee",
        "AI employees",
    ],
    "ai-shopping": [
        "AI Shopping",
        "AI shopping assistant",
        "AI shopping agent",
        "shop with AI",
        "AI product search",
    ],
    "browser": [
        "AI browser",
        "AI web browser",
        "agentic browser",
        "AI browsing",
        "Comet browser",
    ],
    "data-engineering-agent": [
        "Data Engineering Agent",
        "AI data engineer",
        "agentic data engineering",
        "data engineer agent",
        "AI data engineering agent",
    ],
    "expert-agent": [
        "Expert Agent",
        "AI expert agent",
        "expert AI agent",
        "AI expert network",
        "expert agent marketplace",
    ],
    "multi-agent": [
        "Multi-Agent Systems",
        "multi-agent AI",
        "multi agent system",
        "multi-agent orchestration",
        "AI multi-agent",
    ],
    "openclaw-alternatives": [
        "OpenClaw alternatives",
        "OpenClaw",
        "Clawdbot alternatives",
        "Moltbot alternatives",
        "OpenClaw vs",
    ],
    "vibe-coding-payments": [
        "vibe coding payments",
        "add payments to vibe coded app",
        "stripe vibe coding",
        "how to add payments to vibe coded app",
        "vibe coding Stripe",
    ],
    "work-agent": [
        "Work Agent",
        "AI Work Agent",
        "AI work agent",
        "work AI agent",
        "workplace agent",
    ],
    "workflow": [
        "Workflow automation",
        "AI workflow",
        "AI workflow automation",
        "workflow AI",
        "agentic workflow",
    ],
    "workspace-agent": [
        "Workspace Agent",
        "Team AI Agent",
        "AI workspace agent",
        "workspace AI agent",
        "custom GPT workspace",
    ],
    "world-model": [
        "World model",
        "world models",
        "AI world models",
        "world model AI",
        "world models machine learning",
    ],
}


def main():
    out_dir = Path("e:/clients/temp/kw-audit-results/subagent")
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_path = out_dir / "agent_bing_raw.json"
    log_path = out_dir / "agent_bing_log.txt"

    raw = {}
    if raw_path.exists():
        try:
            raw = json.loads(raw_path.read_text(encoding="utf-8"))
        except Exception:
            raw = {}
    log_lines = []
    slugs = list(CANDIDATES.keys())
    for i, slug in enumerate(slugs):
        if slug in raw and raw[slug]:
            print(f"[{i+1}/{len(slugs)}] {slug} SKIP (cached)", flush=True)
            continue
        print(f"[{i+1}/{len(slugs)}] {slug}", flush=True)
        log_lines.append(f"[{i+1}/{len(slugs)}] {slug}")
        items = []
        for kw in CANDIDATES[slug]:
            res = bing_count(kw, quoted=True)
            row = {
                "keyword": kw,
                "quoted_results": res["n"],
                "serp_titles": res["titles"],
            }
            items.append(row)
            msg = f"  {kw!r}: {res['n']} | {res['titles'][:160]}"
            try:
                print(msg, flush=True)
            except UnicodeEncodeError:
                print(f"  {kw!r}: {res['n']}", flush=True)
            log_lines.append(msg)
            time.sleep(0.85)
        raw[slug] = items
        raw_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

    raw_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    log_path.write_text("\n".join(log_lines), encoding="utf-8")
    print(f"Wrote {raw_path}", flush=True)


if __name__ == "__main__":
    main()
