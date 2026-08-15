#!/usr/bin/env python3
"""Audit knowledge/tools KB blocks against A/B/C tier standards."""
import json
import re
from pathlib import Path

KB_DIR = Path(__file__).resolve().parents[2] / "knowledge" / "tools"
OUT = KB_DIR / "_audit-quality-report.json"

REQ = {
    "材料范围": r"材料范围",
    "词汇锚点": r"词汇锚点",
    "问题域": r"问题域",
    "风险合规": r"风险\s*[·\.·\s]*合规",
    "外链索引": r"外链索引",
    "说明": r"\*\*说明\*\*|^## 说明|^\*说明：|^说明（",
}
REC = {
    "能力栈": r"能力栈",
    "落地碎片": r"落地碎片",
    "工具表": r"工具与产品|代表工具|产品类型",
    "对比测评": r"对比与测评|专题对照|扩展定义",
}


def load_tiers():
    tiers = {"A": [], "B": [], "C": [], "meta": []}
    current = None
    for line in (KB_DIR / "territory-map.md").read_text(encoding="utf-8").splitlines():
        if "## A 档" in line:
            current = "A"
        elif "## B 档" in line:
            current = "B"
        elif "## C 档" in line:
            current = "C"
        elif "## Meta" in line or "## 未归类" in line:
            current = "meta"
        elif current in ("A", "B", "C") and line.startswith("| `") and not line.startswith("| Slug") and not line.startswith("|------"):
            slug = line.split("|")[1].strip().strip("`")
            if slug and not slug.endswith(".md"):
                tiers[current].append(slug)
    return tiers


def count_vocab(text):
    return len(re.findall(r"^- \*\*[^*]+\*\*", text, re.M))


def count_problems(text):
    in_q = False
    n = 0
    for line in text.splitlines():
        if "问题域" in line and ("**" in line or line.startswith("##")):
            in_q = True
            continue
        if in_q:
            if line.startswith("- "):
                n += 1
            elif line.startswith("**") or line.startswith("##") or line.startswith("---"):
                if n > 0:
                    break
    return n


def count_links(text):
    return len(re.findall(r"https?://[^\s\)>\]]+", text))


def audit_slug(slug, tier):
    fp = KB_DIR / f"{slug}.md"
    if not fp.exists():
        return {"tier": tier, "missing_file": True, "issues": [("P0", "文件缺失")]}
    text = fp.read_text(encoding="utf-8")
    size_kb = len(text.encode("utf-8")) / 1024
    req_miss = [k for k, p in REQ.items() if not re.search(p, text, re.M)]
    rec_miss = [k for k, p in REC.items() if not re.search(p, text, re.M)]
    links = count_links(text)
    vocab = count_vocab(text)
    problems = count_problems(text)
    bold_sections = len(re.findall(r"^\*\*[^*]+\*\*\s*$", text, re.M))
    h2_sections = len(re.findall(r"^## ", text, re.M))
    issues = []
    if req_miss:
        issues.append(("P0", f"缺必需节: {req_miss}"))
    if tier == "A":
        if links < 10:
            issues.append(("P0", f"外链不足: {links}<10"))
        for r in rec_miss:
            issues.append(("P1", f"缺推荐节: {r}"))
    elif tier == "B":
        if vocab < 5:
            issues.append(("P0", f"词汇锚点不足: {vocab}<5"))
        if problems < 5:
            issues.append(("P0", f"问题域不足: {problems}<5"))
        for r in rec_miss:
            issues.append(("P1", f"缺推荐节: {r}"))
    elif tier == "C":
        if size_kb > 15:
            issues.append(("P1", f"C档体积偏大: {size_kb:.1f}KB"))
    if tier == "A" and size_kb < 15:
        issues.append(("P1", f"A档体积偏小: {size_kb:.1f}KB"))
    if bold_sections > 5 and h2_sections < 2:
        issues.append(("P1", "体例: 过多**节标题、缺少##"))
    ph_first = bool(re.search(r"Product Hunt", text))
    if ph_first and not re.search(r"producthunt\.com", text, re.I):
        issues.append(("P1", "提及 Product Hunt 但无 PH 链接"))
    return {
        "tier": tier,
        "path": str(fp),
        "size_kb": round(size_kb, 1),
        "links": links,
        "vocab": vocab,
        "problems": problems,
        "req_miss": req_miss,
        "rec_miss": rec_miss,
        "issues": issues,
    }


def main():
    tiers = load_tiers()
    results = {}
    for tier in ("A", "B", "C"):
        for slug in tiers[tier]:
            results[slug] = audit_slug(slug, tier)

    summary = {}
    for tier in ("A", "B", "C"):
        slugs = [s for s, d in results.items() if d.get("tier") == tier]
        passed = sum(1 for s in slugs if not results[s].get("issues") and not results[s].get("missing_file"))
        summary[tier] = {"total": len(slugs), "passed": passed, "rate": round(passed / len(slugs) * 100, 1) if slugs else 0}

    p0 = sorted(s for s, d in results.items() if any(i[0] == "P0" for i in d.get("issues", [])))
    p1 = sorted(
        s
        for s, d in results.items()
        if any(i[0] == "P1" for i in d.get("issues", [])) and s not in p0
    )

    report = {"summary": summary, "p0": {s: results[s] for s in p0}, "p1": {s: results[s] for s in p1}, "all": results}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("=== KB Quality Audit ===")
    for tier in ("A", "B", "C"):
        s = summary[tier]
        print(f"{tier}: {s['passed']}/{s['total']} pass ({s['rate']}%)")
    print(f"P0 slugs: {len(p0)}")
    print(f"P1 slugs: {len(p1)}")
    print(f"Report: {OUT}")


if __name__ == "__main__":
    main()
