#!/usr/bin/env python3
"""Audit Alignify knowledge blocks for within-document semantic duplication."""
import re
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"e:\clients\Alignify\knowledge\tools")

SECTION_MARKERS = [
    (r"^## 与相邻 slug 分流", "分流表"),
    (r"^## 词汇锚点", "词汇锚点"),
    (r"^## 专题对照", "专题对照"),
    (r"^## 问题域", "问题域"),
    (r"^## 能力栈", "能力栈"),
    (r"^## 形态谱系", "形态谱系"),
    (r"^## 风险", "风险合规"),
    (r"^## 落地碎片", "落地碎片"),
    (r"^## 工具与产品类型", "工具与产品类型"),
    (r"^## 代表产品速览", "代表产品速览"),
    (r"^## 外链索引", "外链索引"),
    (r"^## 行业注记", "行业注记"),
    (r"^### 对比与测评", "对比与测评"),
    (r"^## 站外", "站外"),
    (r"^## 延伸阅读", "延伸阅读"),
]

SKIP_PRODUCTS = {
    "维度", "类型", "典型", "备注", "名称", "一句话", "URL", "Type",
    "Premium T2V model", "Value T2V model", "English", "AI",
}


def parse_sections(text: str):
    lines = text.splitlines()
    hits = []
    for i, line in enumerate(lines):
        for pat, name in SECTION_MARKERS:
            if re.match(pat, line):
                hits.append((i, name, line))
                break
    sections = {}
    for idx, (start, name, _) in enumerate(hits):
        end = hits[idx + 1][0] if idx + 1 < len(hits) else len(lines)
        # merge duplicate section names with suffix
        key = name
        n = 2
        while key in sections:
            key = f"{name}_{n}"
            n += 1
        sections[key] = (start, end)
    # Preamble ends at first H2 (includes Buyer 决策树 etc. before known markers)
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    preamble_end = first_h2
    sections["preamble"] = (0, preamble_end)
    return sections, lines


def section_text(lines, sections, name):
    if name not in sections:
        return ""
    s, e = sections[name]
    return "\n".join(lines[s:e])


def extract_products(text: str) -> set:
    products = set()
    for m in re.finditer(r"\*\*([^*\|\n]{2,50}?)\*\*", text):
        name = m.group(1).strip()
        short = name.split("（")[0].split("(")[0].strip()
        if short in SKIP_PRODUCTS or short.startswith("http"):
            continue
        if re.match(r"^[a-z-]+$", short):  # slug-like
            continue
        if len(short) >= 3:
            products.add(short)
    return products


def extract_urls(text: str) -> set:
    urls = set(re.findall(r"https?://[^\s\)\]|>\"']+", text))
    return {u.rstrip(".,;") for u in urls}


def normalize_url(u: str) -> str:
    u = u.rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.lower()


def audit_file(fp: Path):
    rel = fp.relative_to(ROOT).as_posix()
    text = fp.read_text(encoding="utf-8", errors="replace")
    line_count = len(text.splitlines())
    sections, lines = parse_sections(text)
    issues = []
    score = 0

    morph = section_text(lines, sections, "形态谱系")
    types = section_text(lines, sections, "工具与产品类型")
    links = section_text(lines, sections, "外链索引")
    rep = section_text(lines, sections, "代表产品速览")

    morph_p = extract_products(morph)
    types_p = extract_products(types)
    links_p = extract_products(links)
    rep_p = extract_products(rep)

    # 1 taxonomy triple-stack
    if morph and types and links:
        triple = morph_p & types_p & links_p
        if len(triple) >= 2:
            issues.append({
                "severity": "HIGH",
                "type": "taxonomy_triple_stack",
                "detail": f"形态谱系+工具类型+外链三处重复枚举 {len(triple)} 个产品",
                "products": sorted(triple)[:10],
                "sections": ["形态谱系", "工具与产品类型", "外链索引"],
                "ssot": "外链索引（产品 URL+规格）；形态谱系仅保留 Type 架构；工具类型仅保留检索词分类",
            })
            score += 4
        else:
            double = (morph_p & types_p) | (morph_p & links_p) | (types_p & links_p)
            if len(double) >= 4:
                issues.append({
                    "severity": "MEDIUM",
                    "type": "taxonomy_double_stack",
                    "detail": f"两两重复产品 {len(double)} 个",
                    "products": sorted(double)[:8],
                    "sections": ["形态谱系", "工具与产品类型", "外链索引"],
                    "ssot": "外链索引为产品 SSOT；形态谱系去品牌留 Type",
                })
                score += 2

    # 代表产品速览 as 4th stack layer
    if rep and links and len(rep_p & links_p) >= 3:
        issues.append({
            "severity": "MEDIUM",
            "type": "rep_vs_links_dup",
            "detail": f"代表产品速览与外链索引重复 {len(rep_p & links_p)} 个",
            "products": sorted(rep_p & links_p)[:6],
            "sections": ["代表产品速览", "外链索引"],
            "ssot": "外链索引",
        })
        score += 2

    # 2 vocab vs topic
    vocab = section_text(lines, sections, "词汇锚点")
    topic = section_text(lines, sections, "专题对照")
    if vocab and topic:
        boundary_terms = [
            "T2V", "I2V", "V2V", "Query Model", "Live Model",
            "text-to-video", "image-to-video", "video-to-video",
            "Agentic IDE", "Copilot IDE", "Expert Network",
        ]
        vh = {t for t in boundary_terms if t.lower() in vocab.lower()}
        th = {t for t in boundary_terms if t.lower() in topic.lower()}
        shared = vh & th
        both_table = "|" in vocab and "|" in topic
        both_vs = "vs" in vocab.lower() and "vs" in topic.lower()
        if shared and (both_table or both_vs):
            issues.append({
                "severity": "MEDIUM",
                "type": "vocab_topic_overlap",
                "detail": f"词汇锚点与专题对照双重定义边界: {sorted(shared)}",
                "sections": ["词汇锚点", "专题对照"],
                "ssot": "词汇锚点（术语定义）；专题对照仅列买家体验差/对照表",
            })
            score += 2
        elif len(shared) >= 3:
            issues.append({
                "severity": "LOW",
                "type": "vocab_topic_overlap",
                "detail": f"共享边界术语: {sorted(shared)}",
                "sections": ["词汇锚点", "专题对照"],
                "ssot": "词汇锚点",
            })
            score += 1

    # 3 capability stack product specs
    cap = section_text(lines, sections, "能力栈")
    if cap:
        cap_p = extract_products(cap)
        for sec_name, sec_text in [
            ("形态谱系", morph), ("外链索引", links), ("落地碎片", section_text(lines, sections, "落地碎片"))
        ]:
            if not sec_text:
                continue
            overlap = {p for p in (cap_p & extract_products(sec_text)) if len(p) > 4}
            if len(overlap) >= 4:
                issues.append({
                    "severity": "MEDIUM",
                    "type": "capability_product_dup",
                    "detail": f"能力栈与{sec_name}重复 {len(overlap)} 个产品/规格",
                    "products": sorted(overlap)[:6],
                    "sections": ["能力栈", sec_name],
                    "ssot": "能力栈（概念维度）；产品名/评分/价格仅外链索引或落地碎片一处",
                })
                score += 2
                break

    # 4 boundary triple
    preamble = section_text(lines, sections, "preamble")
    split = section_text(lines, sections, "分流表")
    has_narr = "叙述主词" in preamble
    has_dont = "勿与" in preamble and "混买" in preamble
    if has_narr and has_dont and split:
        narr_slugs = set(re.findall(r"`([a-z0-9-]+)`", preamble))
        split_slugs = set(re.findall(r"`([a-z0-9-]+)`", split))
        common = narr_slugs & split_slugs
        if len(common) >= 3:
            issues.append({
                "severity": "MEDIUM",
                "type": "boundary_triple",
                "detail": f"叙述主词+勿与混买+分流表三重复述 sibling 分流 ({len(common)} slugs)",
                "products": sorted(common),
                "sections": ["preamble", "分流表"],
                "ssot": "分流表（canonical）；文首叙述主词一句+勿与混买指针即可",
            })
            score += 2

    # 5 duplicate URLs
    if links:
        link_urls = {normalize_url(u) for u in extract_urls(links)}
        for sec_name in ["站外", "行业注记", "对比与测评", "延伸阅读", "延伸阅读_2"]:
            sec = section_text(lines, sections, sec_name)
            if not sec:
                continue
            other = {normalize_url(u) for u in extract_urls(sec)}
            dup = link_urls & other
            if len(dup) >= 2:
                issues.append({
                    "severity": "MEDIUM",
                    "type": "duplicate_urls",
                    "detail": f"外链索引与{sec_name}重复 URL {len(dup)} 个",
                    "sections": ["外链索引", sec_name],
                    "ssot": "外链索引（产品 URL）；站外/延伸阅读仅放研究/框架类链接",
                })
                score += 2
                break

    # 6 industry note dup
    note = section_text(lines, sections, "行业注记")
    if note:
        note_p = extract_products(note)
        for sec_name, sec in [("问题域", section_text(lines, sections, "问题域")),
                              ("外链索引", links),
                              ("对比与测评", section_text(lines, sections, "对比与测评"))]:
            if not sec:
                continue
            overlap = note_p & extract_products(sec)
            if len(overlap) >= 3:
                issues.append({
                    "severity": "MEDIUM",
                    "type": "industry_note_dup",
                    "detail": f"行业注记与{sec_name}重复趋势/产品事实 {len(overlap)} 项",
                    "products": sorted(overlap)[:5],
                    "sections": ["行业注记", sec_name],
                    "ssot": "行业注记（宏观趋势）；问题域/对比与测评去重复产品枚举",
                })
                score += 2
                break

    # 7 dual further reading
    ext_headers = re.findall(r"^## 延伸阅读[^\n]*", text, re.M)
    if len(ext_headers) >= 2:
        issues.append({
            "severity": "MEDIUM",
            "type": "dual_further_reading",
            "detail": f"存在 {len(ext_headers)} 个延伸阅读节: {ext_headers}",
            "sections": ext_headers,
            "ssot": "合并为单一「延伸阅读 · 站内外」",
        })
        score += 2

    # duplicate ## 外链索引 headers
    link_headers = re.findall(r"^## 外链索引[^\n]*", text, re.M)
    if len(link_headers) >= 2:
        issues.append({
            "severity": "MEDIUM",
            "type": "duplicate_links_index",
            "detail": f"存在 {len(link_headers)} 个外链索引节: {link_headers}",
            "sections": link_headers,
            "ssot": "合并为单一「## 外链索引」",
        })
        score += 2

    # compare vs links subsection dup (video-generator pattern)
    compare = section_text(lines, sections, "对比与测评")
    if compare and links:
        compare_p = extract_products(compare)
        overlap = compare_p & links_p
        if len(overlap) >= 3:
            issues.append({
                "severity": "MEDIUM",
                "type": "compare_links_dup",
                "detail": f"对比与测评与外链索引重复产品评价 {len(overlap)} 项",
                "products": sorted(overlap)[:5],
                "sections": ["对比与测评", "外链索引"],
                "ssot": "外链索引（产品事实）；对比与测评仅第三方观点/无重复规格",
            })
            score += 2

    # overall severity
    if any(i["severity"] == "HIGH" for i in issues):
        sev = "HIGH"
    elif score >= 3 or len([i for i in issues if i["severity"] == "MEDIUM"]) >= 2:
        sev = "MEDIUM"
    elif issues:
        sev = "LOW"
    else:
        sev = "NONE"

    return {
        "path": rel,
        "abs_path": str(fp),
        "lines": line_count,
        "severity": sev,
        "score": score,
        "issues": issues,
        "section_count": len(sections),
    }


def main():
    md_files = sorted({p for p in ROOT.rglob("*.md")})
    results = [audit_file(fp) for fp in md_files]

    folder_stats = defaultdict(lambda: {"total": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "NONE": 0})
    for r in results:
        parts = r["path"].split("/")
        folder = parts[0] if len(parts) > 1 else "(root)"
        folder_stats[folder][r["severity"]] += 1
        folder_stats[folder]["total"] += 1

    out = {
        "total": len(results),
        "high": sum(1 for r in results if r["severity"] == "HIGH"),
        "medium": sum(1 for r in results if r["severity"] == "MEDIUM"),
        "low": sum(1 for r in results if r["severity"] == "LOW"),
        "none": sum(1 for r in results if r["severity"] == "NONE"),
        "folder_stats": dict(folder_stats),
        "results": sorted(results, key=lambda x: (-x["score"], -x["lines"])),
    }
    out_path = Path(r"e:\clients\temp\kb_dedupe_audit.json")
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ["total", "high", "medium", "low", "none"]}, indent=2))
    print("TOP HIGH/MEDIUM:")
    for r in out["results"]:
        if r["severity"] in ("HIGH", "MEDIUM"):
            print(f"{r['severity']:6} score={r['score']:2} lines={r['lines']:4} {r['path']}")
            for i in r["issues"]:
                print(f"       [{i['severity']}] {i['type']}: {i['detail']}")


if __name__ == "__main__":
    main()
