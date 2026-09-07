import json, re
from pathlib import Path

d = json.loads(Path(r"e:/clients/temp/kw-audit-results/FINAL_KEYWORD_DIGEST.json").read_text(encoding="utf-8"))
sw = [i for i in d["digest"] if i.get("final_verdict") == "SWITCH"]

# build slug->path from inventory
inv = json.loads(Path(r"e:/clients/temp/kw-audit-batches/full_kb_inventory.json").read_text(encoding="utf-8"))
slugs = {}
for grp in ("with_keywordEn", "without_keywordEn"):
    for it in inv[grp]:
        slugs[it["slug"]] = it["path"]

KB = Path(r"e:/clients/Alignify/knowledge")
fails = []
for i in sw:
    rel = slugs.get(i["slug"])
    rec = i.get("recommended_primary") or ""
    if not rel:
        fails.append(f"{i['slug']}: NO INVENTORY PATH"); continue
    p = KB / rel
    if not p.exists():
        fails.append(f"{i['slug']}: MISSING FILE {rel}"); continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    # count keywordEn occurrences
    kes = re.findall(r"`keywordEn`\s*[:：]\s*\*\*(.+?)\*\*", txt)
    head = txt[:600]
    if not kes:
        fails.append(f"{i['slug']}: NO keywordEn FOUND  [{rel}]")
    else:
        primary = kes[0].strip()
        norm = lambda s: re.sub(r"\s+", " ", s.lower())
        if norm(primary) != norm(rec):
            fails.append(f"{i['slug']}: keywordEn={primary!r} != recommended {rec!r}  [{rel}]")
        else:
            print(f"OK  {i['slug']}: {primary}  [{rel}]")

print("\n=====")
print("TOTAL SWITCH:", len(sw), " FAILS:", len(fails))
for f in fails:
    print("FAIL:", f)
