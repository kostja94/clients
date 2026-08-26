#!/usr/bin/env python3
"""Audit marketing strategy articles for blog-md render + presentation (E33–E42).

Scans content/blog/* (category marketing or known slugs) and content/marketing/*:
- E33–E36: render / format (GFM table, MD list, fenced code)
- E37: pseudo-list paragraphs (warn if >=3)
- E38: high table count (warn if >=6)
- E40: short or colon-terminated bridge before childrenHtml
- E41: orphan bold label lines
- E42: standalone disclaimer; post-table single sentence; blog 策略文单句段 >2

Usage (from alignify production repo root):
  python path/to/audit-marketing-md-render.py
  python path/to/audit-marketing-md-render.py --json
  python path/to/audit-marketing-md-render.py --slug wrapped-marketing
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MARKETING_BLOG_SLUGS = {
    "rate-limit-reset",
    "coding-plan",
    "wrapped-marketing",
    "git-commit-attribution",
    "embedded-virality",
    "ugc-marketing",
    "github-for-marketing",
    "how-to-write-github-readme",
    "how-to-name-ai-products",
}

PRESENTATION_FAIL_CODES = frozenset({"E40", "E41", "E42"})
RENDER_FAIL_CODES = frozenset({"E33", "E34", "E36"})

DISCLAIMER_RE = re.compile(
    r"(政策与案例随产品|Policies and case details change|"
    r"核对各官方 FAQ|verify official FAQ|"
    r"执行前请核对官方|verify official Usage|"
    r"随版本变化；执行|change by vendor—verify official|"
    r"Fees and quotas change by vendor)",
    re.I,
)

ORPHAN_LABEL_RE = re.compile(r"^\*\*[^*]+[：:]\*\*\s*$")


def _body(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def _is_marketing_blog(slug: str, frontmatter: str) -> bool:
    if slug in MARKETING_BLOG_SLUGS:
        return True
    return bool(re.search(r'^category:\s*["\']?marketing["\']?\s*$', frontmatter, re.M))


def _count_sentences(text: str) -> int:
    text = text.strip()
    if not text or text.startswith("##") or text.startswith("<"):
        return 0
    zh = len(re.findall(r"[。！？；]", text))
    en_period = len(re.findall(r"[.!?](?:\s+|$)", text))
    en_semi = len(re.findall(r";\s+", text))
    en = en_period + en_semi
    if zh and en:
        return max(zh, en)
    if zh:
        return zh
    if en:
        return en
    return 1 if len(text) > 20 else 0


def _prose_paragraphs(body: str) -> list[tuple[int, str]]:
    lines = body.splitlines()
    in_children = False
    buf: list[str] = []
    start_line = 1
    out: list[tuple[int, str]] = []

    def flush(at_line: int) -> None:
        nonlocal buf, start_line
        if not buf:
            return
        text = "\n".join(buf).strip()
        buf = []
        if not text or text.startswith("<!--") or text.startswith("##"):
            return
        out.append((start_line, text))

    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s == "<!-- childrenHtml:start -->":
            flush(i)
            in_children = True
            continue
        if s == "<!-- childrenHtml:end -->":
            in_children = False
            buf = []
            start_line = i + 1
            continue
        if in_children:
            continue
        if s.startswith("<!-- block:section -->") or s.startswith("##"):
            flush(i)
            buf = []
            start_line = i + 1
            continue
        if not s:
            flush(i)
            start_line = i + 1
            continue
        if not buf:
            start_line = i
        buf.append(line)
    flush(len(lines) + 1)
    return out


def _paragraph_before_children(body: str) -> list[tuple[int, str]]:
    lines = body.splitlines()
    in_children = False
    buf: list[str] = []
    start_line = 1
    hits: list[tuple[int, str]] = []

    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s == "<!-- childrenHtml:start -->":
            text = "\n".join(buf).strip()
            if text and not text.startswith("##"):
                hits.append((start_line, text))
            in_children = True
            buf = []
            continue
        if s == "<!-- childrenHtml:end -->":
            in_children = False
            start_line = i + 1
            buf = []
            continue
        if in_children:
            continue
        if s.startswith("##") or s.startswith("<!-- block:section -->"):
            buf = []
            start_line = i + 1
            continue
        if not s:
            if buf:
                start_line = i + 1
            buf = []
            continue
        if not buf:
            start_line = i
        buf.append(line)
    return hits


def _paragraph_after_children(body: str) -> list[tuple[int, str]]:
    lines = body.splitlines()
    in_children = False
    buf: list[str] = []
    start_line = 1
    hits: list[tuple[int, str]] = []
    pending_after = False

    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s == "<!-- childrenHtml:start -->":
            in_children = True
            pending_after = False
            continue
        if s == "<!-- childrenHtml:end -->":
            in_children = False
            pending_after = True
            buf = []
            start_line = i + 1
            continue
        if in_children:
            continue
        if not pending_after:
            continue
        if s.startswith("##") or s.startswith("<!-- block:section -->"):
            pending_after = False
            buf = []
            continue
        if not s:
            if buf:
                text = "\n".join(buf).strip()
                if text and not text.startswith("##"):
                    hits.append((start_line, text))
                pending_after = False
                buf = []
            continue
        if not buf:
            start_line = i
        buf.append(line)
    if pending_after and buf:
        text = "\n".join(buf).strip()
        if text and not text.startswith("##"):
            hits.append((start_line, text))
    return hits


def audit_file(path: Path, *, channel: str) -> dict:
    text = path.read_text(encoding="utf-8")
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    slug = path.stem
    body = _body(text)
    issues: list[dict] = []
    warnings: list[str] = []
    in_children = False
    is_new_format = "<!-- block:section -->" in body
    presentation_strict = channel == "blog" or is_new_format
    strict_one_sentence = presentation_strict

    for i, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if s == "<!-- childrenHtml:start -->":
            in_children = True
            continue
        if s == "<!-- childrenHtml:end -->":
            in_children = False
            continue
        if in_children:
            continue
        if re.match(r"^```", s):
            issues.append({"code": "E36", "line": i, "snippet": s[:80]})
        if re.match(r"^\|", s) and s.count("|") >= 2:
            issues.append({"code": "E33", "line": i, "snippet": s[:80]})
        if re.match(r"^[-*+] ", s):
            issues.append({"code": "E34", "line": i, "snippet": s[:80]})
        if re.match(r"^\d+\. ", s):
            issues.append({"code": "E34", "line": i, "snippet": s[:80]})
        if re.match(r"^<(ul|ol)\b", s, re.I):
            issues.append({"code": "E34", "line": i, "snippet": s[:80]})

    paras = _prose_paragraphs(body)

    pseudo = sum(
        1
        for _, p in paras
        if re.match(r"^\*\*[^*]+\*\*\s+\S", p)
        and len(p) < 320
        and "\n" not in p
    )

    for line_no, p in paras:
        if ORPHAN_LABEL_RE.match(p):
            issue = {"code": "E41", "line": line_no, "snippet": p[:80]}
            if channel == "blog" or is_new_format:
                issues.append(issue)
            else:
                warnings.append(f"legacy-orphan-label:L{line_no}")
        if DISCLAIMER_RE.search(p) and _count_sentences(p) <= 1:
            issues.append(
                {
                    "code": "E42",
                    "line": line_no,
                    "snippet": "standalone disclaimer: " + p[:72],
                }
            )

    one_sentence_paras = [
        (ln, p) for ln, p in paras if _count_sentences(p) == 1 and len(p) < 400
    ]
    if strict_one_sentence and len(one_sentence_paras) > 2:
        for ln, p in one_sentence_paras[2:]:
            issues.append(
                {
                    "code": "E42",
                    "line": ln,
                    "snippet": f"one-sentence paragraph ({len(one_sentence_paras)} total): "
                    + p[:60],
                }
            )

    for line_no, p in _paragraph_before_children(body):
        sc = _count_sentences(p)
        if presentation_strict:
            if sc < 3:
                issues.append(
                    {
                        "code": "E40",
                        "line": line_no,
                        "snippet": f"pre-table bridge {sc} sentence(s): {p[:72]}",
                    }
                )
            if re.search(r"[：:]\s*$", p):
                issues.append(
                    {
                        "code": "E40",
                        "line": line_no,
                        "snippet": "colon-terminated pre-table: " + p[-60:],
                    }
                )

    for line_no, p in _paragraph_after_children(body):
        if presentation_strict and _count_sentences(p) == 1 and len(p) < 500:
            issues.append(
                {
                    "code": "E42",
                    "line": line_no,
                    "snippet": "post-table single sentence: " + p[:72],
                }
            )

    tables = len(re.findall(r"<!-- childrenHtml:start -->[\s\S]*?<table", body))

    render_errors = [x for x in issues if x["code"] in RENDER_FAIL_CODES]
    presentation_errors = [x for x in issues if x["code"] in PRESENTATION_FAIL_CODES]
    if tables >= 6:
        warnings.append(f"high-table-count:{tables}")
    if pseudo >= 3:
        warnings.append(f"pseudo-list-paragraphs:{pseudo}")
    if not strict_one_sentence and len(one_sentence_paras) > 2:
        warnings.append(f"legacy-one-sentence-count:{len(one_sentence_paras)}")

    fail_count = len(render_errors) + len(presentation_errors)

    return {
        "path": str(path).replace("\\", "/"),
        "fail_count": fail_count,
        "render_error_count": len(render_errors),
        "presentation_error_count": len(presentation_errors),
        "render_errors": render_errors,
        "presentation_errors": presentation_errors,
        "html_table_count": tables,
        "pseudo_list_paragraph_count": pseudo,
        "one_sentence_paragraph_count": len(one_sentence_paras),
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--content-root",
        default=None,
        help="Path to content/ directory (default: alignify production/content)",
    )
    parser.add_argument("--slug", default=None, help="Audit single slug only")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.content_root:
        content = Path(args.content_root)
    else:
        content = Path(r"E:\自有部署项目\alignify production\content")

    if not content.is_dir():
        print(f"content root not found: {content}", file=sys.stderr)
        return 1

    results: list[dict] = []
    for channel in ("blog", "marketing"):
        for loc in ("zh", "en"):
            d = content / channel / loc
            if not d.is_dir():
                continue
            for f in sorted(d.glob("*.md")):
                if args.slug and f.stem != args.slug:
                    continue
                text = f.read_text(encoding="utf-8")
                fm = text.split("---", 2)[1] if text.startswith("---") else ""
                if channel == "blog" and not _is_marketing_blog(f.stem, fm):
                    continue
                row = audit_file(f, channel=channel)
                if row["fail_count"] or row["warnings"]:
                    row["channel"] = channel
                    row["locale"] = loc
                    row["slug"] = f.stem
                    results.append(row)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            flags = []
            if r["render_error_count"]:
                flags.append(f"RENDER:{r['render_error_count']}")
            if r["presentation_error_count"]:
                flags.append(f"PRES:{r['presentation_error_count']}")
            if r["warnings"]:
                flags.append(",".join(r["warnings"]))
            print(f"{r['channel']}/{r['locale']}/{r['slug']}  {' | '.join(flags)}")
            for e in r["render_errors"][:3]:
                print(f"  {e['code']} L{e['line']}: {e['snippet']}")
            for e in r["presentation_errors"][:5]:
                print(f"  {e['code']} L{e['line']}: {e['snippet']}")

    print(f"\nArticles with issues: {len(results)}", file=sys.stderr)
    hard_fail = sum(1 for r in results if r["fail_count"])
    print(
        f"With hard failures (E33/E34/E36/E40–E42): {hard_fail}",
        file=sys.stderr,
    )
    return 1 if hard_fail else 0


if __name__ == "__main__":
    sys.exit(main())
