import json
from pathlib import Path

d = json.loads(Path(r"e:/clients/temp/kw-audit-results/FINAL_KEYWORD_DIGEST.json").read_text(encoding="utf-8"))
print("TOP KEYS:", list(d.keys()) if isinstance(d, dict) else type(d))
res = d.get("results", d) if isinstance(d, dict) else d
if isinstance(res, dict):
    # maybe keyed by verdict
    for k, v in res.items():
        if isinstance(v, list):
            print(f"\n== {k}: {len(v)} ==")
            for it in v[:60]:
                print(f"  {it.get('slug')}: {it.get('current_primary')} -> {it.get('recommended') or it.get('recommended_primary')} | {str(it.get('note') or '')[:90]}")
        else:
            print(f"\n== {k} ==")
            print(json.dumps(v, ensure_ascii=False, indent=1)[:800])
