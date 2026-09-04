import json
from pathlib import Path

r = json.loads(Path(r"e:/clients/temp/kw-audit-results/FULL_PRIMARY_KEYWORD_AUDIT.json").read_text(encoding="utf-8"))

# Manual re-tiering based on KB-consistency review above.
# high = apply confidently; review = needs editorial check before editing KB
REVIEW = {
    "community": "KB category=marketing、keywordEn 已是 AI Community；'community platform' 虽符合 Circle/Skool SERP，但改词会弱化 AI 角。建议并入 Secondary，主词保留 AI Community。",
    "documentation": "页面定位 Mintlify/GitBook/Docusaurus 开发者文档站；'documentation platform' 多用于 ReadMe 类，Mintlify/Docusaurus 并不自称 platform。建议复核或维持 Developer documentation。",
    "search-indexing": "KB 叙述主轴=AI Search Indexing（收录加速/IndexNow/AI 引擎可见性）；'website indexing' 是传统 GSC 语言，会与站内 seo/website-indexing 域冲突。保持现主词。",
    "technology-profiler": "'what CMS is this' 只有 ~2.4-2.9k 且只覆盖 CMS 检测，本 KB 覆盖 Wappalyzer/BuiltWith 全栈检测；可作 Secondary。",
    "religion": "'AI Religion' SERP 被 AI-as-deity 占据；'AI religious tools' 多信仰产品词更贴。建议改为 AI religious tools。",
    "interactive-video": "SERP 'Interactive video' 偏 e-learning/shoppable（禁）；'live AI video generation' 是产品/PR 词且无 MSV。建议 KEEP Interactive video（KB 叙述主词）并加 real-time interactive video Secondary。",
}

manual_verdict = {}
for slug, note in REVIEW.items():
    manual_verdict[slug] = note

lines = []
lines.append("## 判定修订（对照 KB 定位）\n")
for slug, note in REVIEW.items():
    orig = next((x for x in r["results"] if x["slug"] == slug), None)
    if orig:
        lines.append(f"- **{slug}**: {note}")

print("\n".join(lines))
