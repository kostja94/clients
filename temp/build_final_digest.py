#!/usr/bin/env python3
"""Build final digest with manual editorial overrides for chat presentation."""
from __future__ import annotations

import json
from pathlib import Path

SRC = Path(r"e:/clients/temp/kw-audit-results/FULL_PRIMARY_KEYWORD_AUDIT.json")
OUT = Path(r"e:/clients/temp/kw-audit-results/FINAL_KEYWORD_DIGEST.json")

# Manual overrides: slug -> (final_verdict, final_recommended, note)
OVERRIDES = {
    "community": (
        "KEEP_INTENT",
        "AI Community",
        "KB category=marketing、keywordEn 已配 AI Community；community platform 只是产品类（Circle/Skool），弱化 AI 角 → 主词保留，platform 入 Secondary。",
    ),
    "documentation": (
        "KEEP_INTENT",
        "Developer documentation",
        "页面定位 Mintlify/GitBook/Docusaurus 开发者文档站；documentation platform 多用于 ReadMe 类，Mintlify/Docusaurus 不自称 platform → 保留现主词，复核后再定。",
    ),
    "search-indexing": (
        "KEEP_INTENT",
        "AI Search Indexing",
        "KB 主轴=收录加速/IndexNow/AI 引擎可见性；website indexing 是传统 GSC 语言，会与站内 seo/website-indexing 域冲突 → 保持现主词。",
    ),
    "technology-profiler": (
        "KEEP_INTENT",
        "website technology profiler",
        "what CMS is this 仅 2.4-2.9k 且只覆盖 CMS 检测，KB 覆盖 Wappalyzer/BuiltWith 全栈检测 → 作 Secondary，主词保留。",
    ),
    "religion": (
        "SWITCH",
        "AI religious tools",
        "AI Religion SERP 被 AI-as-deity 占据；AI religious tools 多信仰产品词更贴本页。",
    ),
    "interactive-video": (
        "KEEP_INTENT",
        "Interactive video",
        "live AI video generation 是 PR/产品词无消费 MSV；Interactive video 虽是 e-learning 头词但本页禁止追逐 → 保留叙述主词，real-time/live 词作 Secondary。",
    ),
    "ai-short-drama": ("KEEP_INTENT", "AI short drama platform", "placeholder"),
}

# rename short-drama key fix
if "ai-short-drama" in OVERRIDES:
    OVERRIDES["short-drama"] = OVERRIDES.pop("ai-short-drama")
    OVERRIDES["short-drama"] = ("SWITCH", "AI short drama generator", "生产侧 SERP 标题收敛于 AI short drama generator 而非 platform。")
del OVERRIDES["short-drama"]  # will set explicitly below
OVERRIDES["short-drama"] = (
    "SWITCH",
    "AI short drama generator",
    "生产侧（Teleplay/Dramily/StoryShort）SERP 标题收敛于 AI short drama generator 而非 platform。",
)


def main():
    r = json.loads(SRC.read_text(encoding="utf-8"))
    final = []
    for item in r["results"]:
        slug = item["slug"]
        if slug in OVERRIDES:
            verdict, rec, note = OVERRIDES[slug]
        else:
            verdict = item.get("verdict", "OK")
            rec = item.get("recommended_primary") or item.get("current_primary")
            note = item.get("reason", "")
        final.append(
            {
                "slug": slug,
                "batch": item.get("batch"),
                "current_primary": item.get("current_primary"),
                "final_verdict": verdict,
                "recommended_primary": rec,
                "note": note,
                "path": item.get("path"),
            }
        )
    final.sort(key=lambda x: x["slug"])
    from collections import Counter

    OUT.write_text(json.dumps({"digest": final, "counts": dict(Counter(x["final_verdict"] for x in final))}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(dict(Counter(x["final_verdict"] for x in final)), indent=2))
    # print switch table
    print("\nSWITCH_FINAL:")
    for x in final:
        if x["final_verdict"] in ("SWITCH",):
            print(f"{x['slug']}|{x['current_primary']}->{x['recommended_primary']}|{x['batch']}")
    print("\nAMBIGUOUS:")
    for x in final:
        if x["final_verdict"] == "AMBIGUOUS":
            print(f"{x['slug']}|{x['current_primary']}|{x['batch']}")


if __name__ == "__main__":
    main()
