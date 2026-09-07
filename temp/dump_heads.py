import json, re
from pathlib import Path

d = json.loads(Path(r"e:/clients/temp/kw-audit-results/FINAL_KEYWORD_DIGEST.json").read_text(encoding="utf-8"))
inv = json.loads(Path(r"e:/clients/temp/kw-audit-batches/full_kb_inventory.json").read_text(encoding="utf-8"))
KB = Path(r"e:/clients/Alignify/knowledge")
slugs = {}
for grp in ("with_keywordEn", "without_keywordEn"):
    for it in inv[grp]:
        slugs[it["slug"]] = KB / it["path"]

sw = [i for i in d["digest"] if i.get("final_verdict") == "SWITCH"]
out = []
for i in sw:
    p = slugs.get(i["slug"])
    if not p or not p.exists():
        out.append(f"### {i['slug']}  [NO FILE]")
        continue
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    shown = []
    for ln in lines[:11]:
        if ln.strip():
            shown.append(ln.rstrip()[:300])
    out.append(f"\n########## {i['slug']}  ->  {i['recommended_primary']}   [{p.relative_to(KB)}]")
    out.extend(f"{n}| {t}" for n, t in enumerate(shown, 1))
Path(r"e:/clients/temp/heads32.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote heads32.txt with", len(sw), "files")
