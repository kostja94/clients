import json
from pathlib import Path

r = json.loads(Path("e:/clients/temp/kw-audit-results/MERGED_AUDIT_REPORT.json").read_text(encoding="utf-8"))
for x in r["switch_recommendations"]:
    cur = x.get("current_primary") or (x.get("raw") or {}).get("current_primary", "?")
    rec = x.get("recommended_primary") or x.get("highest_volume_keyword") or "?"
    notes = x.get("notes") or (x.get("raw") or {}).get("reason", "")
    print(f"{x['slug']}|{cur}|{rec}|{notes[:100]}")
