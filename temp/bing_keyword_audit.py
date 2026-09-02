#!/usr/bin/env python3
"""Bing approximate result count fetcher for keyword volume audit."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def bing_count(query: str) -> str | None:
    url = "https://www.bing.com/search?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return f"ERROR:{e}"
    # Bing: "About 1,230,000 results" or "1,230,000 results"
    m = re.search(r"([\d,]+)\s+results", html, re.I)
    if m:
        return m.group(1).replace(",", "")
    m = re.search(r"About\s+([\d,]+)", html, re.I)
    if m:
        return m.group(1).replace(",", "")
    return "UNKNOWN"


def alternatives_for(slug: str, current: str) -> list[str]:
    """Generate candidate keywords from slug + current primary."""
    cands = set()
    # normalize current - take first English segment
    for part in re.split(r"[/·|/]", current):
        p = part.strip()
        if p and re.search(r"[a-zA-Z]", p):
            cands.add(p)
    # slug-based
    words = slug.replace("-", " ")
    cands.add(f"AI {words}")
    cands.add(words)
    if not words.startswith("ai "):
        cands.add(f"{words} tools")
        cands.add(f"AI {words} tools")
    # common patterns
    if "generator" in slug:
        cands.add(f"AI {words}")
        cands.add(words.replace("generator", "generator AI"))
    return list(cands)[:5]


def audit_slug(item: dict) -> dict:
    slug = item["slug"]
    current = item["current_primary"]
    cands = alternatives_for(slug, current)
    if current not in cands:
        cands.insert(0, current.split("/")[0].strip())
    tested = []
    for kw in cands[:4]:
        count = bing_count(kw)
        tested.append({"keyword": kw, "bing_approx": count})
        time.sleep(0.8)
    # find highest numeric
    best = max(
        tested,
        key=lambda x: int(x["bing_approx"]) if x["bing_approx"].isdigit() else 0,
    )
    current_counts = [t for t in tested if current.split("/")[0].strip().lower() in t["keyword"].lower()]
    current_best = max(
        current_counts or tested[:1],
        key=lambda x: int(x["bing_approx"]) if x["bing_approx"].isdigit() else 0,
    )
    best_num = int(best["bing_approx"]) if best["bing_approx"].isdigit() else 0
    cur_num = int(current_best["bing_approx"]) if current_best["bing_approx"].isdigit() else 0
    if best_num > cur_num * 1.5 and best["keyword"].lower() != current_best["keyword"].lower():
        verdict = "SWITCH"
    elif best_num > 0 and abs(best_num - cur_num) / max(best_num, 1) < 0.3:
        verdict = "OK"
    else:
        verdict = "AMBIGUOUS"
    return {
        "slug": slug,
        "current_primary": current,
        "candidates_tested": tested,
        "highest_volume_keyword": best["keyword"],
        "verdict": verdict,
        "recommended_primary": best["keyword"] if verdict == "SWITCH" else current.split("/")[0].strip(),
        "notes": f"best={best['bing_approx']} vs current~{cur_num}",
    }


if __name__ == "__main__":
    import sys

    batch = sys.argv[1] if len(sys.argv) > 1 else "batch1_agent_root"
    inp = Path(f"e:/clients/temp/kw-audit-batches/{batch}.json")
    out_dir = Path("e:/clients/temp/kw-audit-results")
    out_dir.mkdir(exist_ok=True)
    items = json.loads(inp.read_text(encoding="utf-8"))
    results = []
    for i, item in enumerate(items):
        print(f"[{i+1}/{len(items)}] {item['slug']}...", flush=True)
        results.append(audit_slug(item))
    out = out_dir / f"{batch}_results.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = {}
    for v in ["OK", "SWITCH", "AMBIGUOUS", "NEEDS_REVIEW"]:
        summary[v] = sum(1 for r in results if r["verdict"] == v)
    print("SUMMARY", summary)
    print("SWITCH:", [r["slug"] for r in results if r["verdict"] == "SWITCH"])
