#!/usr/bin/env python3
"""Audit internal links across the deployed repo's content/**/*.md.

Scans every article Markdown file, extracts site-internal links (Markdown
[text](href) and <a href="...">), normalises targets, and writes:
  - scripts/reports/md-internal-links-status-YYYY-MM-DD.json  (raw data)
  - scripts/reports/md-internal-links-status-YYYY-MM-DD.md    (human doc)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CTX = HERE.parents[1]

DEPLOY_CANDIDATES = [
    CTX.parents[1] / "部署项目" / "个人部署项目" / "alignify-by-kostja",
    CTX.parents[1] / "部署项目" / "alignify-by-kostja",
    CTX.parents[0] / "alignify-by-kostja",
    Path(r"D:\部署项目\个人部署项目\alignify-by-kostja"),
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

STATIC_EXT = re.compile(r"\.(jpe?g|png|gif|webp|svg|ico|pdf|zip|css|js|woff2?|mp4|webm|avif)$", re.I)
ANCHOR_RE = re.compile(r"#.*$")

MD_LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)")
A_HREF_RE = re.compile(r'<a[^>]*href=["\']([^"\']+)["\']', re.I)


def strip_anchor(href: str) -> str:
    return ANCHOR_RE.sub("", href)


def normalise_target(href: str) -> str:
    """Normalise an internal href to a target key like 'tools/avatar' or 'services'."""
    h = href.strip()
    # absolute alignify URLs
    m = re.match(r"^https?://(?:www\.)?alignify\.co(/.*)$", h)
    if m:
        h = m.group(1)
    if not h.startswith("/"):
        return ""  # external or protocol-relative
    h = strip_anchor(h)
    if h in ("/", "/zh", "/en"):
        return "home"
    h = h.rstrip("/")
    # strip locale prefix (/zh or /en)
    mm = re.match(r"^/(?:zh|en)(/.*)$", h)
    if mm:
        h = mm.group(1)
    if h == "/":
        return "home"
    parts = [p for p in h.split("/") if p]
    if not parts:
        return "home"
    if len(parts) == 1:
        return parts[0]  # hub / aggregation page (e.g. /tools)
    return f"{parts[0]}/{parts[1]}"


def is_internal(href: str) -> bool:
    h = href.strip()
    if not h:
        return False
    if h.startswith("#"):
        return False
    if h.startswith("mailto:") or h.startswith("tel:"):
        return False
    if h.startswith("//"):
        return False
    if re.match(r"^https?://(?:www\.)?alignify\.co", h):
        return True
    if h.startswith("/"):
        return not STATIC_EXT.search(h)
    return False


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
    page_url = fm.get("pageUrl", "")

    # Strip script/style content so schema JSON links don't pollute the count.
    body = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", "", text, flags=re.S | re.I)

    raw_hrefs: list[str] = []
    for m in MD_LINK_RE.finditer(body):
        raw_hrefs.append(m.group(1))
    for m in A_HREF_RE.finditer(body):
        raw_hrefs.append(m.group(1))

    internal: list[str] = [h for h in raw_hrefs if is_internal(h)]
    targets = [normalise_target(h) for h in internal]
    targets = [t for t in targets if t]
    target_counter = Counter(targets)
    duplicates = sorted(t for t, c in target_counter.items() if c > 1)
    distinct = len(target_counter)
    total = len(targets)

    return {
        "slug": slug,
        "locale": locale,
        "route": route,
        "title": fm.get("title", slug),
        "pageUrl": page_url,
        "category": fm.get("category", ""),
        "categorySecondary": fm.get("categorySecondary", ""),
        "total_internal_links": total,
        "distinct_targets": distinct,
        "targets": sorted(target_counter),
        "duplicates": duplicates,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-doc", type=Path, default=CTX / "scripts" / "reports" / f"md-internal-links-status-{date.today().isoformat()}.md")
    ap.add_argument("--out-json", type=Path, default=None)
    args = ap.parse_args()

    rows: list[dict] = []
    for cat in CATEGORIES:
        d = DEPLOY / "content" / cat
        if not d.is_dir():
            continue
        for fp in sorted(d.rglob("*.md")):
            r = audit_file(fp)
            if r:
                rows.append(r)

    out_json = args.out_json or CTX / "scripts" / "reports" / f"md-internal-links-status-{date.today().isoformat()}.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(
        json.dumps({"date": date.today().isoformat(), "articles": rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ---- summarise per category/locale ----
    by_cat: dict[str, dict[str, list]] = {}
    for r in rows:
        by_cat.setdefault(r["route"], {"en": [], "zh": []})[r["locale"]].append(r)

    lines: list[str] = []
    lines.append("# Alignify 文章页面内链情况（快照）")
    lines.append("")
    lines.append(f"> 生成日期：{date.today().isoformat()}")
    lines.append(f"> 数据源：`alignify-by-kostja/content/**/*.md`（共 {len(rows)} 篇文章）")
    lines.append("> 方法：提取每篇正文与 frontmatter 中的站内链接（Markdown `[text](/path)` 与 `<a href=\"/path\">`），")
    lines.append("> 归一化目标为 `route/slug`（忽略 `/zh` 前缀）；外链、锚点、图片与静态资源不计。")
    lines.append("> 完整数据见 `scripts/reports/md-internal-links-status-YYYY-MM-DD.json`。")
    lines.append("")
    lines.append("> **口径说明**：`≥5 distinct` 为 SSOT 中 **Tools 长文**的硬性 R1 底线（`internal-links.md §3.1.5`）；")
    lines.append("> SEO 频道遵循「少而准」与学习页节制原则（§4.1.6），**不适用** R1 硬标准；")
    lines.append("> 因此「≥5 distinct」对其他类目仅为**观察性指标**，不构成违规判断。")
    lines.append("")

    # ---- overview ----
    lines.append("## 概览")
    lines.append("")
    lines.append("| 类目 | 文章数 | 内链总量 | 平均内链/篇 | ≥5 distinct 篇数 | ≥5 distinct 占比 |")
    lines.append("|------|-------:|--------:|------------:|-----------------:|-----------------:|")
    grand = {"n": 0, "total": 0, "ok": 0}
    for cat in CATEGORIES:
        if cat not in by_cat:
            continue
        rows_cat = [r for lst in by_cat[cat].values() for r in lst]
        n = len(rows_cat)
        tot = sum(r["total_internal_links"] for r in rows_cat)
        ok = sum(1 for r in rows_cat if r["distinct_targets"] >= 5)
        avg = tot / n if n else 0
        grand["n"] += n
        grand["total"] += tot
        grand["ok"] += ok
        star = " ⭐R1" if cat == "tools" else ""
        lines.append(f"| {cat}{star} | {n} | {tot} | {avg:.1f} | {ok} | {ok/n*100:.0f}% |")
    lines.append(f"| **合计** | **{grand['n']}** | **{grand['total']}** | **{grand['total']/grand['n']:.1f}** | **{grand['ok']}** | **{grand['ok']/grand['n']*100:.0f}%** |")
    lines.append("")
    lines.append("- ⭐R1：SSOT 硬性底线仅适用于 tools 类目（正文 4–9 条 distinct 内链，底线 ≥5）。")
    lines.append("")

    # ---- issue lists ----
    tools_under = [r for r in rows if r["route"] == "tools" and r["distinct_targets"] < 5]
    other_low = [r for r in rows if r["route"] != "tools" and r["distinct_targets"] < 5]
    dupe = [r for r in rows if r["duplicates"]]
    no_link = [r for r in rows if r["total_internal_links"] == 0]

    lines.append("## 需要关注的问题")
    lines.append("")
    lines.append(f"- **Tools R1 未达标**（distinct 站内目标 < 5，SSOT 硬规则）：**{len(tools_under)}** 篇 / {len([r for r in rows if r['route']=='tools'])} 篇")
    lines.append(f"- **其他类目低内链**（< 5 distinct，观察性，非违规）：**{len(other_low)}** 篇")
    lines.append(f"- **存在重复目标**（同一 `route/slug` 出现 >1 次）：**{len(dupe)}** 篇")
    lines.append(f"- **零内链**：**{len(no_link)}** 篇")
    lines.append("")

    if tools_under:
        lines.append("### Tools R1 未达标清单（硬规则）")
        lines.append("")
        lines.append("| 文章 | 语言 | distinct | 总量 | 内链目标 |")
        lines.append("|------|------|---------:|-----:|---------|")
        for r in sorted(tools_under, key=lambda x: (x["locale"], x["slug"])):
            targets_str = "、".join(f"`{t}`" for t in r["targets"]) if r["targets"] else "—"
            lines.append(
                f"| `{r['slug']}` | {r['locale']} | {r['distinct_targets']} | "
                f"{r['total_internal_links']} | {targets_str} |"
            )
        lines.append("")

    if other_low:
        lines.append("### 其他类目低内链清单（观察性）")
        lines.append("")
        lines.append("| 文章 | 语言 | distinct | 总量 |")
        lines.append("|------|------|---------:|-----:|")
        for r in sorted(other_low, key=lambda x: (x["route"], x["locale"], x["slug"])):
            lines.append(
                f"| `{r['route']}/{r['locale']}/{r['slug']}` | {r['locale']} | "
                f"{r['distinct_targets']} | {r['total_internal_links']} |"
            )
        lines.append("")

    if dupe:
        lines.append("### 重复目标清单")
        lines.append("")
        lines.append("| 文章 | 重复目标 |")
        lines.append("|------|---------|")
        for r in sorted(dupe, key=lambda x: (x["route"], x["locale"], x["slug"])):
            lines.append(f"| `{r['route']}/{r['locale']}/{r['slug']}` | `{'`、`'.join(r['duplicates'])}` |")
        lines.append("")

    if no_link:
        lines.append("### 零内链清单")
        lines.append("")
        for r in sorted(no_link, key=lambda x: (x["route"], x["locale"], x["slug"])):
            lines.append(f"- `{r['route']}/{r['locale']}/{r['slug']}`")
        lines.append("")

    # ---- per-category details ----
    lines.append("## 按类目明细")
    lines.append("")
    for cat in CATEGORIES:
        if cat not in by_cat:
            continue
        lines.append(f"### {cat}")
        lines.append("")
        lines.append("| 文章 | 语言 | distinct | 总量 | 内链目标 |")
        lines.append("|------|------|---------:|-----:|---------|")
        for r in sorted(
            (r for lst in by_cat[cat].values() for r in lst),
            key=lambda x: (x["locale"], x["slug"]),
        ):
            dupe_flag = " ⚠重复" if r["duplicates"] else ""
            targets_str = "、".join(f"`{t}`" for t in r["targets"]) if r["targets"] else "—"
            lines.append(
                f"| `{r['slug']}` | {r['locale']} | {r['distinct_targets']} | "
                f"{r['total_internal_links']} | {targets_str}{dupe_flag} |"
            )
        lines.append("")

    args.out_doc.parent.mkdir(parents=True, exist_ok=True)
    args.out_doc.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Articles: {len(rows)}")
    print(f"JSON: {out_json}")
    print(f"Doc : {args.out_doc}")


if __name__ == "__main__":
    main()
