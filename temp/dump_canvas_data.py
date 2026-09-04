import json
from pathlib import Path

r = json.loads(Path(r"e:/clients/temp/kw-audit-results/FULL_PRIMARY_KEYWORD_AUDIT.json").read_text(encoding="utf-8"))
t = json.loads(Path(r"e:/clients/temp/kw-audit-results/SWITCH_TRIAGE.json").read_text(encoding="utf-8"))
out = {
    "verdict_summary": r["verdict_summary"],
    "by_batch": r["by_batch"],
    "ok_count": r["ok_count"],
    "high": [
        {"slug": x["slug"], "from": x["current_primary"], "to": x["recommended_primary"], "batch": x["batch"]}
        for x in t["high_confidence"]
    ],
    "low": [
        {"slug": x["slug"], "from": x["current_primary"], "to": x["recommended_primary"], "batch": x["batch"]}
        for x in t["likely_false_positive"]
    ],
    "mid": t["review_needed"],
    "keep_intent": r["keep_intent"],
    "ambiguous": r["ambiguous"],
}
Path(r"e:/clients/temp/kw-audit-results/canvas_data.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("ok", out["verdict_summary"], "high", len(out["high"]), "low", len(out["low"]))
