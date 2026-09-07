import json
from pathlib import Path

d = json.loads(Path(r"e:/clients/temp/kw-audit-results/FINAL_KEYWORD_DIGEST.json").read_text(encoding="utf-8"))
sw = sorted([i for i in d["digest"] if i.get("final_verdict") == "SWITCH"], key=lambda x: x["slug"])
for i in sw:
    print(f"{i['slug']}\tCUR={i.get('current_primary')!r}\tREC={i.get('recommended_primary')!r}\tSEC={i.get('secondary_keywords') or i.get('secondary') or ''}")
