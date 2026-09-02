import re
import json
from pathlib import Path

root = Path(r"e:/clients/Alignify/knowledge")
skip_names = {"README.md", "_TEMPLATE.md", "KEYWORD-RESEARCH.md", "territory-map.md"}
results = []

for md in sorted(root.rglob("*.md")):
    if md.name.startswith("_") or md.name in skip_names:
        continue
    text = md.read_text(encoding="utf-8", errors="ignore")
    rel = str(md.relative_to(root)).replace("\\", "/")

    slug = md.stem
    keyword_en = None
    keyword_zh = None
    narrative = None

    m = re.search(
        r"keywordEn[`'\"]?\s*[:：]\s*\*?\*?([^*\n·]+?)\*?\*?(?:\s*·|\s*\||\s*\n|$)",
        text,
    )
    if m:
        keyword_en = m.group(1).strip().strip("*").strip()

    m = re.search(
        r"keywordZh[`'\"]?\s*[:：]\s*\*?\*?([^*\n·]+?)\*?\*?(?:\s*·|\s*\||\s*\n|$)",
        text,
    )
    if m:
        keyword_zh = m.group(1).strip().strip("*").strip()

    m = re.search(r"\*\*叙述主词[^*]*\*\*[^：]*：\*\*([^*]+)\*\*", text)
    if m:
        narrative = m.group(1).strip()

    h1 = None
    m = re.search(r"^#\s+(.+?)\s*·\s*知识块", text, re.M)
    if m:
        h1 = m.group(1).strip()

    if keyword_en or narrative or h1:
        results.append(
            {
                "path": rel,
                "slug": slug,
                "keywordEn": keyword_en,
                "keywordZh": keyword_zh,
                "narrative": narrative,
                "h1": h1,
            }
        )

out = Path(r"e:/clients/temp/kb-keywords-extract.json")
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total: {len(results)}")
print(f"Saved to {out}")
