import json, re
from pathlib import Path

d = json.loads(Path(r"e:/clients/temp/kw-audit-results/FINAL_KEYWORD_DIGEST.json").read_text(encoding="utf-8"))
inv = json.loads(Path(r"e:/clients/temp/kw-audit-batches/full_kb_inventory.json").read_text(encoding="utf-8"))
KB = Path(r"e:/clients/Alignify/knowledge")

# slug -> path
slugs = {}
for grp in ("with_keywordEn", "without_keywordEn"):
    for it in inv[grp]:
        slugs[it["slug"]] = KB / it["path"]

sw = [i for i in d["digest"] if i.get("final_verdict") == "SWITCH"]
out = [f"SWITCH total: {len(sw)}"]
for i in sw:
    p = slugs.get(i["slug"])
    if not p or not p.exists():
        out.append(f"\n### {i['slug']}  [NO FILE] {i['current_primary']} -> {i['recommended_primary']}")
        continue
    txt = p.read_text(encoding="utf-8", errors="ignore")
    lines = txt.splitlines()
    # find keywordEn line within first 15 lines
    kw_line = ""
    for ln in lines[:15]:
        if re.search(r"`?keywordEn`?\s*[:：]", ln):
            kw_line = ln.strip()
            break
    # find narrative line 叙述主词
    narr_line = ""
    for ln in lines[:6]:
        if "叙述主词" in ln:
            narr_line = ln.strip()[:200]
            break
    h1 = lines[0].strip()[:120] if lines else ""
    out.append(f"\n### {i['slug']}  [{p.relative_to(KB)}]")
    out.append(f"  change: {i['current_primary']}  ->  {i['recommended_primary']}")
    out.append(f"  note: {i['note'][:150]}")
    out.append(f"  H1: {h1}")
    if kw_line:
        out.append(f"  KWLINE: {kw_line}")
    if narr_line:
        out.append(f"  NARR: {narr_line}")

Path(r"e:/clients/temp/switch_targets.txt").write_text("\n".join(out), encoding="utf-8")
print("wrote", len(sw))
