#!/usr/bin/env python3
"""Build Alignify site-structure-internal-links.md from deployed content.

Scans content/**/*.md, extracts internal links (Markdown + <a href>),
computes outbound/inbound graphs, and writes:
  - skills/optimize-internal-links/references/site-structure-internal-links.md
  - scripts/reports/md-internal-links-status-YYYY-MM-DD.json
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CTX = HERE.parents[1]

DEPLOY_CANDIDATES = [
    CTX.parents[1] / "部署项目" / "个人部署项目" / "alignify-by-kostja",
    Path(r"E:\自有部署项目\alignify production"),
]
DEPLOY = next((p for p in DEPLOY_CANDIDATES if (p / "content").is_dir()), None)
if DEPLOY is None:
    env = __import__("os").environ.get("ALIGNIFY_DEPLOY_ROOT")
    if env and (Path(env) / "content").is_dir():
        DEPLOY = Path(env)
    else:
        sys.exit("Deploy repo not found; set ALIGNIFY_DEPLOY_ROOT")

CATEGORIES = ["tools", "seo", "blog", "marketing", "insights", "events"]
TODAY = date.today().isoformat()

STATIC_EXT = re.compile(r"\.(jpe?g|png|gif|webp|svg|ico|pdf|zip|css|js|woff2?|mp4|webm|avif)$", re.I)
ANCHOR_RE = re.compile(r"#.*$")
MD_LINK_RE = re.compile(r"(?<!\!)\[([^\]]*)\]\(([^)\s]+)")
A_HREF_RE = re.compile(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.I | re.S)


def strip_anchor(href: str) -> str:
    return ANCHOR_RE.sub("", href)


def normalise_target(href: str) -> str:
    h = href.strip()
    m = re.match(r"^https?://(?:www\.)?alignify\.co(/.*)$", h)
    if m:
        h = m.group(1)
    if not h.startswith("/"):
        return ""
    h = strip_anchor(h).rstrip("/")
    if h in ("", "/"):
        return "home"
    mm = re.match(r"^/(?:zh|en)(/.*)$", h)
    if mm:
        h = mm.group(1)
    if h in ("", "/"):
        return "home"
    parts = [p for p in h.split("/") if p]
    if len(parts) == 1:
        return parts[0]
    return f"{parts[0]}/{parts[1]}"


def is_internal(href: str) -> bool:
    h = href.strip()
    if not h or h.startswith("#") or h.startswith("mailto:") or h.startswith("tel:"):
        return False
    if h.startswith("//"):
        return False
    if re.match(r"^https?://(?:www\.)?alignify\.co", h):
        return True
    return h.startswith("/") and not STATIC_EXT.search(h)


def parse_frontmatter(text: str) -> dict:
    fm: dict = {}
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return fm
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z][\w]*):\s*\"(.*)\"\s*$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2)
    return fm


def page_key(route: str, slug: str) -> str:
    return f"{route}/{slug}"


def audit_file(path: Path) -> dict | None:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return None
    if not text.startswith("---"):
        return None
    fm = parse_frontmatter(text)
    slug = fm.get("slug", path.stem)
    locale = fm.get("locale", path.parent.name)
    route = path.relative_to(DEPLOY / "content").parts[0]
    pk = page_key(route, slug)

    body = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", "", text, flags=re.S | re.I)

    links: list[dict] = []
    for m in MD_LINK_RE.finditer(body):
        href, anchor = m.group(2), m.group(1).strip()
        if is_internal(href):
            tgt = normalise_target(href)
            if tgt:
                links.append({"anchor": anchor, "href": href, "target": tgt})
    for m in A_HREF_RE.finditer(body):
        href = m.group(1)
        anchor = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if is_internal(href):
            tgt = normalise_target(href)
            if tgt:
                links.append({"anchor": anchor or href, "href": href, "target": tgt})

    targets = [lk["target"] for lk in links]
    target_counter = Counter(targets)
    duplicates = sorted(t for t, c in target_counter.items() if c > 1)

    return {
        "pageKey": pk,
        "slug": slug,
        "locale": locale,
        "route": route,
        "title": fm.get("title", slug),
        "pageUrl": fm.get("pageUrl", ""),
        "category": fm.get("category", ""),
        "total_internal_links": len(targets),
        "distinct_targets": len(target_counter),
        "targets": sorted(target_counter),
        "target_counts": dict(target_counter),
        "duplicates": duplicates,
        "links": links,
    }


def main() -> None:
    rows: list[dict] = []
    for cat in CATEGORIES:
        d = DEPLOY / "content" / cat
        if not d.is_dir():
            continue
        for fp in sorted(d.rglob("*.md")):
            r = audit_file(fp)
            if r:
                rows.append(r)

    # inbound graph (locale-agnostic slug key)
    inbound: dict[str, Counter] = defaultdict(Counter)
    inbound_sources: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        src = r["pageKey"]
        for lk in r["links"]:
            tgt = lk["target"]
            if tgt == src:
                continue
            inbound[tgt][src] += 1
            inbound_sources[tgt].append(
                {"from": src, "locale": r["locale"], "anchor": lk["anchor"][:60]}
            )

    for r in rows:
        r["inbound_count"] = sum(inbound[r["pageKey"]].values())
        r["inbound_from"] = sorted(inbound[r["pageKey"]].keys())

    out_json = CTX / "scripts" / "reports" / f"md-internal-links-status-{TODAY}.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "date": TODAY,
        "deploy_root": str(DEPLOY),
        "article_count": len(rows),
        "articles": [{k: v for k, v in r.items() if k != "links"} for r in rows],
        "inbound_index": {
            k: {"count": sum(v.values()), "from": dict(v)} for k, v in inbound.items()
        },
    }
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- build living doc ----
    by_route: dict[str, list] = defaultdict(list)
    for r in rows:
        by_route[r["route"]].append(r)

    slug_inbound_en: dict[str, int] = {}
    for r in rows:
        if r["locale"] == "en":
            slug_inbound_en[r["pageKey"]] = r["inbound_count"]

    tools_under = [r for r in rows if r["route"] == "tools" and r["distinct_targets"] < 5]
    no_out = [r for r in rows if r["total_internal_links"] == 0]
    no_in_en = [
        r
        for r in rows
        if r["locale"] == "en" and r["inbound_count"] == 0 and r["route"] != "events"
    ]
    dupe = [r for r in rows if r["duplicates"]]

    top_inbound = sorted(
        [(k, sum(v.values())) for k, v in inbound.items()],
        key=lambda x: -x[1],
    )[:30]

    lines: list[str] = []
    lines += [
        "# Alignify 全站文章结构与内链",
        "",
        "> **用途**：全站唯一的**结构与内链优化**参考（人类 + 站点维护）。回答：**① ~400 篇文章如何按频道组织；② 当前正文内链快照；③ 后续优化优先级**",
        ">",
        f"> **Skill 对齐**：规则 SSOT [`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) · 存量优化 [`../SKILL.md`](../SKILL.md) · Marketing [`../../create-article/rules/marketing-internal-links.md`](../../create-article/rules/marketing-internal-links.md)",
        ">",
        f"> **最后更新**：{TODAY}（自动扫描部署仓 `content/**/*.md`，共 **{len(rows)}** 篇）",
        ">",
        f"> **机器可读数据**：[`../../../scripts/reports/md-internal-links-status-{TODAY}.json`](../../../scripts/reports/md-internal-links-status-{TODAY}.json)",
        "",
        "---",
        "",
        "## 一、站点文章结构",
        "",
        "```",
        "alignify.co",
        "├── /tools/{slug}          ← 216 篇（Hub 106 slug · Tools 型 Blog 6 篇计入 tools hub）",
        "├── /seo/{slug}            ← 76 篇",
        "├── /blog/{slug}           ← 52 篇（含部分原 tools 迁移文）",
        "├── /marketing/{slug}      ← 34 篇",
        "├── /insights/{slug}       ← 14 篇",
        "└── /events/{slug}         ← 8 篇",
        "```",
        "",
        "**正文 SSOT**：`E:\\自有部署项目\\alignify production\\content/{channel}/{locale}/{slug}.md`",
        "",
        "| 频道 | EN+ZH 篇数 | 内链存储 | 优化原则 |",
        "|------|-----------|---------|----------|",
    ]

    grand = {"n": 0, "total": 0, "ok5": 0}
    for cat in CATEGORIES:
        if cat not in by_route:
            continue
        rs = by_route[cat]
        n = len(rs)
        tot = sum(r["total_internal_links"] for r in rs)
        ok5 = sum(1 for r in rs if r["distinct_targets"] >= 5)
        grand["n"] += n
        grand["total"] += tot
        grand["ok5"] += ok5
        lines.append(f"| `{cat}` | {n} | 正文 Markdown / HTML | 点击意图；无硬性条数 |")
    lines += [
        f"| **合计** | **{grand['n']}** | — | — |",
        "",
        "**跨频道桥接**（常见）：`tools/*` ↔ `blog/*`（产品深度文）、`tools/*` ↔ `marketing/*`（GTM）、`seo/*` ↔ `blog/*`（搜索/GEO）。",
        "",
        "---",
        "",
        "## 二、内链规则（不在此重复）",
        "",
        "> **SSOT**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 1–2（点击意图、每段 ≤1 链、同 URL 1 次；FAQ 答案内链计入正文）",
        "> **Marketing**：[`../../create-article/rules/marketing-internal-links.md`](../../create-article/rules/marketing-internal-links.md) M1–M11",
        "> **结论内链**：[`../../create-article/rules/sections.md`](../../create-article/rules/sections.md) Part 4.4（0–2 条，非清单式）",
        "",
        "审计脚本可能仍输出 distinct 计数，**仅作观察**，不作为发布阻断条件。",
        "",
        "---",
        "",
        "## 三、当前快照概览",
        "",
        "| 类目 | 文章数 | 出链总量 | 均出链/篇 | distinct≥5（观察） | 占比 |",
        "|------|-------:|--------:|----------:|------------:|-----:|",
    ]
    for cat in CATEGORIES:
        if cat not in by_route:
            continue
        rs = by_route[cat]
        n = len(rs)
        tot = sum(r["total_internal_links"] for r in rs)
        ok5 = sum(1 for r in rs if r["distinct_targets"] >= 5)
        star = " ⭐" if cat == "tools" else ""
        lines.append(
            f"| {cat}{star} | {n} | {tot} | {tot/n:.1f} | {ok5} | {ok5/n*100:.0f}% |"
        )
    lines += [
        f"| **合计** | **{grand['n']}** | **{grand['total']}** | **{grand['total']/grand['n']:.1f}** | **{grand['ok5']}** | **{grand['ok5']/grand['n']*100:.0f}%** |",
        "",
        "### 需要关注的问题",
        "",
        f"- **Tools distinct<5（观察）**：**{len(tools_under)}** / {len(by_route.get('tools', []))} 篇",
        f"- **零出链**：**{len(no_out)}** 篇",
        f"- **零入链（EN 基准）**：**{len(no_in_en)}** 篇",
        f"- **同篇重复目标（须修）**：**{len(dupe)}** 篇",
        "",
        "---",
        "",
        "## 四、高入链 Hub（全站 Top 30 · 按入链次数）",
        "",
        "| 排名 | pageKey | 入链次数 | 说明 |",
        "|-----:|---------|--------:|------|",
    ]
    for i, (k, c) in enumerate(top_inbound, 1):
        note = "tools hub" if k.startswith("tools/") else k.split("/")[0]
        lines.append(f"| {i} | `{k}` | {c} | {note} |")

    lines += [
        "",
        "---",
        "",
        "## 五、优化优先级队列",
        "",
        "### P0 — 结构性违规（R4 重复 / 机械指路链）",
        "",
        "优先修复同篇重复 URL（含 FAQ 与正文重复）、组合拳段堆链。Tools 低 distinct 仅作观察，不为凑数加链。",
        "",
        f"**Tools distinct<5（观察）**：{len(tools_under)} 篇",
        "",
        "### P1 — 零入链 EN 页（Hub 曝光不足）",
        "",
    ]
    for r in sorted(no_in_en, key=lambda x: x["pageKey"])[:40]:
        lines.append(f"- `{r['pageKey']}` — {r['title'][:50]}")
    if len(no_in_en) > 40:
        lines.append(f"- … 另有 **{len(no_in_en) - 40}** 篇，见 JSON `inbound_count: 0`")
    lines += [
        "",
        "### P2 — 零出链",
        "",
    ]
    for r in sorted(no_out, key=lambda x: (x["route"], x["pageKey"]))[:30]:
        lines.append(f"- `{r['route']}/{r['locale']}/{r['slug']}`")
    if len(no_out) > 30:
        lines.append(f"- … 另有 **{len(no_out) - 30}** 篇")
    lines += [
        "",
        "### P3 — 同篇重复目标",
        "",
        f"共 **{len(dupe)}** 篇；见 JSON `duplicates` 字段或运行 `python scripts/audit/audit-md-internal-links.py` 刷新快照。",
        "",
        "---",
        "",
        "## 六、按频道明细",
        "",
        "> 列：**出链 distinct** · **入链** · **出链目标**（`route/slug`）· ⚠重复 = 同篇同目标 >1 次",
        "",
    ]

    for cat in CATEGORIES:
        if cat not in by_route:
            continue
        lines.append(f"### {cat}")
        lines.append("")
        lines.append("| 文章 | 语言 | 出链 | 入链 | 出链目标 |")
        lines.append("|------|------|-----:|-----:|---------|")
        for r in sorted(by_route[cat], key=lambda x: (x["locale"], x["slug"])):
            dupe_flag = " ⚠重复" if r["duplicates"] else ""
            low = " 📊" if cat == "tools" and r["distinct_targets"] < 5 else ""
            tgts = "、".join(f"`{t}`" for t in r["targets"]) if r["targets"] else "—"
            lines.append(
                f"| `{r['slug']}` | {r['locale']} | {r['distinct_targets']}{low} | "
                f"{r['inbound_count']} | {tgts}{dupe_flag} |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        "## 七、维护说明",
        "",
        "1. **刷新本文**：`python scripts/audit/build-site-internal-links-doc.py`",
        "2. **单频道快照**：`python scripts/audit/audit-md-internal-links.py`",
        "3. **改内链**：只改部署仓 `content/**/*.md` 正文；改后重跑本脚本更新快照",
        "4. **邻居选题**：SSOT 附录 B · [`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md)",
        "",
        f"*自动生成 · {TODAY} · Alignify 上下文仓 · `skills/optimize-internal-links/references/`*",
        "",
    ]

    out_doc = CTX / "skills/optimize-internal-links/references/site-structure-internal-links.md"
    out_doc.parent.mkdir(parents=True, exist_ok=True)
    out_doc.write_text("\n".join(lines), encoding="utf-8")

    print(f"Articles: {len(rows)}")
    print(f"Doc : {out_doc}")
    print(f"JSON: {out_json}")


if __name__ == "__main__":
    main()
