import json
from pathlib import Path

raw = json.loads(Path(r"e:/clients/temp/kw-audit-results/subagent/agent_bing_raw.json").read_text(encoding="utf-8"))

for slug, rows in raw.items():
    print("=" * 4, slug)
    for r in rows:
        n = r.get("quoted_results")
        t = (r.get("serp_titles") or "").strip()
        print(f"  {n} | {r['keyword']} | {t[:140]}")
