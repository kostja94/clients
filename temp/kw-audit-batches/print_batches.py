import json
from pathlib import Path

d = Path(r"e:/clients/temp/kw-audit-batches/subagent")
for f in sorted(d.glob("*.json")):
    if f.name == "index.json":
        continue
    items = json.loads(f.read_text(encoding="utf-8"))
    if not isinstance(items, list):
        continue
    print("==", f.stem, len(items))
    for i in items:
        print(f"  {i['slug']}|{i['current_primary']}")
