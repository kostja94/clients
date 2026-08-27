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

BLOG_GTM_SLUGS = frozenset(
    {
        "coding-plan",
        "rate-limit-reset",
        "ugc-marketing",
        "wrapped-marketing",
        "embedded-virality",
        "watermark-growth",
        "platform-subdomain-gating",
        "git-commit-attribution",
    }
)
OVER_LINKED_DISTINCT = 7
BACKLOG_PATH = (
    CTX / "skills/optimize-internal-links/references/marketing-internal-links-backlog.md"
)

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


def find_row(rows: list[dict], route: str, slug: str, locale: str) -> dict | None:
    for r in rows:
        if r["route"] == route and r["slug"] == slug and r["locale"] == locale:
            return r
    return None


def marketing_status_flags(en: dict | None, zh: dict | None) -> str:
    flags: list[str] = []
    for r in (en, zh):
        if r is None:
            continue
        if r["distinct_targets"] == 0:
            flags.append("零出")
        if r["inbound_count"] == 0:
            flags.append("零入")
        if r["distinct_targets"] >= OVER_LINKED_DISTINCT or r["duplicates"]:
            flags.append("堆链")
    if en and zh and abs(en["distinct_targets"] - zh["distinct_targets"]) >= 3:
        flags.append("EN/ZH不对称")
    return " · ".join(dict.fromkeys(flags)) if flags else "✓"


def build_marketing_gtm_section(rows: list[dict]) -> list[str]:
    marketing_slugs = sorted({r["slug"] for r in rows if r["route"] == "marketing"})
    blog_gtm = sorted(BLOG_GTM_SLUGS)

    def stats_for(route: str, slugs: list[str], locale: str) -> dict:
        rs = [find_row(rows, route, s, locale) for s in slugs]
        rs = [r for r in rs if r]
        zero_out = sum(1 for r in rs if r["distinct_targets"] == 0)
        over = sum(
            1
            for r in rs
            if r["distinct_targets"] >= OVER_LINKED_DISTINCT or r["duplicates"]
        )
        zero_in = sum(1 for r in rs if r["inbound_count"] == 0)
        return {
            "count": len(rs),
            "zero_out": zero_out,
            "over": over,
            "zero_in": zero_in,
        }

    m_en = stats_for("marketing", marketing_slugs, "en")
    m_zh = stats_for("marketing", marketing_slugs, "zh")
    b_en = stats_for("blog", blog_gtm, "en")
    b_zh = stats_for("blog", blog_gtm, "zh")

    lines: list[str] = [
        "## 七、Marketing / GTM 内链专项",
        "",
        "> **规则**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 4.5（M1–M11）",
        "> **Cluster 矩阵与逐页指令**：[`marketing-internal-links-backlog.md`](marketing-internal-links-backlog.md)（人工维护；本节 §7.2–7.3 为脚本快照）",
        "",
        "### 7.1 范围",
        "",
        f"- **`/marketing/*`**：{len(marketing_slugs)} slug × 2 语言 = **{len(marketing_slugs) * 2}** 篇",
        f"- **`/blog/*` 增长策略**：{len(blog_gtm)} slug × 2 语言 = **{len(blog_gtm) * 2}** 篇（`ugc-marketing` 等已迁 `/blog/`，勿按 `/marketing/` 查）",
        "",
        "### 7.2 快照摘要",
        "",
        "| 分区 | 语言 | 篇数 | 零出链 | 堆链/重复 | 零入链 |",
        "|------|------|-----:|-------:|----------:|-------:|",
        f"| marketing | en | {m_en['count']} | {m_en['zero_out']} | {m_en['over']} | {m_en['zero_in']} |",
        f"| marketing | zh | {m_zh['count']} | {m_zh['zero_out']} | {m_zh['over']} | {m_zh['zero_in']} |",
        f"| blog GTM | en | {b_en['count']} | {b_en['zero_out']} | {b_en['over']} | {b_en['zero_in']} |",
        f"| blog GTM | zh | {b_zh['count']} | {b_zh['zero_out']} | {b_zh['over']} | {b_zh['zero_in']} |",
        "",
        "**典型待办**：EN `/marketing/*` 零出链孤岛 · `geo` / `lifetime-deal` 堆链 · `blog/wrapped-marketing` 零入链 · blog GTM 8 篇互链（Batch 5）。",
        "",
        "### 7.3 逐页现状（自动）",
        "",
        "#### `/marketing/*`",
        "",
        "| slug | en 出 | zh 出 | en 入 | zh 入 | 标记 |",
        "|------|------:|------:|------:|------:|------|",
    ]

    for slug in marketing_slugs:
        en = find_row(rows, "marketing", slug, "en")
        zh = find_row(rows, "marketing", slug, "zh")
        lines.append(
            f"| `{slug}` | "
            f"{en['distinct_targets'] if en else '—'} | "
            f"{zh['distinct_targets'] if zh else '—'} | "
            f"{en['inbound_count'] if en else '—'} | "
            f"{zh['inbound_count'] if zh else '—'} | "
            f"{marketing_status_flags(en, zh)} |"
        )

    lines += [
        "",
        "#### `/blog/*` 增长策略",
        "",
        "| slug | en 出 | zh 出 | en 入 | zh 入 | 标记 |",
        "|------|------:|------:|------:|------:|------|",
    ]
    for slug in blog_gtm:
        en = find_row(rows, "blog", slug, "en")
        zh = find_row(rows, "blog", slug, "zh")
        lines.append(
            f"| `{slug}` | "
            f"{en['distinct_targets'] if en else '—'} | "
            f"{zh['distinct_targets'] if zh else '—'} | "
            f"{en['inbound_count'] if en else '—'} | "
            f"{zh['inbound_count'] if zh else '—'} | "
            f"{marketing_status_flags(en, zh)} |"
        )

    lines += [
        "",
        "### 7.4 Cluster 矩阵 · 逐页指令 · 执行批次",
        "",
    ]
    if BACKLOG_PATH.is_file():
        backlog = BACKLOG_PATH.read_text(encoding="utf-8")
        # Drop duplicate H1; keep from first ## onward
        backlog = re.sub(r"^# .+\n\n", "", backlog, count=1)
        lines.append(backlog.rstrip())
        lines.append("")
    else:
        lines.append(f"*Backlog 文件缺失：{BACKLOG_PATH}*")
        lines.append("")

    return lines


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

    route_counts = {cat: len(by_route.get(cat, [])) for cat in CATEGORIES}

    lines: list[str] = []
    lines += [
        "# Alignify 全站文章结构与内链",
        "",
        "> **用途**：全站唯一的**结构与内链优化**参考（人类 + 站点维护）。回答：**① ~400 篇文章如何按频道组织；② 当前正文内链快照；③ 后续优化优先级**",
        ">",
        f"> **Skill 对齐**：规则 SSOT [`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) · 存量优化 [`../SKILL.md`](../SKILL.md) · Marketing Part 4.5（M1–M11）",
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
        f"├── /tools/{{slug}}          ← {route_counts.get('tools', 0)} 篇",
        f"├── /seo/{{slug}}            ← {route_counts.get('seo', 0)} 篇",
        f"├── /blog/{{slug}}           ← {route_counts.get('blog', 0)} 篇",
        f"├── /marketing/{{slug}}      ← {route_counts.get('marketing', 0)} 篇",
        f"├── /insights/{{slug}}       ← {route_counts.get('insights', 0)} 篇",
        f"└── /events/{{slug}}         ← {route_counts.get('events', 0)} 篇",
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
        "> **Marketing M1–M11**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md#part-45-marketing-频道内链)",
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

    lines += build_marketing_gtm_section(rows)

    lines += [
        "---",
        "",
        "## 八、维护说明",
        "",
        "1. **刷新本文**：`python scripts/audit/build-site-internal-links-doc.py`",
        "2. **Marketing backlog**：改 [`marketing-internal-links-backlog.md`](marketing-internal-links-backlog.md) 后重跑上一条（§7.4 自动嵌入）",
        "3. **单频道快照**：`python scripts/audit/audit-md-internal-links.py`",
        "4. **改内链**：只改部署仓 `content/**/*.md` 正文；改后重跑本脚本更新快照",
        "5. **邻居选题**：SSOT 附录 B · [`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md)",
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
