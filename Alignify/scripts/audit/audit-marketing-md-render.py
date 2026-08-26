#!/usr/bin/env python3
"""Audit marketing strategy articles for blog-md render violations (E33–E36).

Scans content/blog/* and content/marketing/* for:
- E36: fenced code blocks (```) outside childrenHtml
- E33: GFM pipe tables outside childrenHtml
- E34: Markdown lists or raw <ul>/<ol> outside childrenHtml
- WARN: high table count (>=6) or pseudo-list paragraphs (>=3)

Usage (from alignify production repo root):
  python path/to/audit-marketing-md-render.py
  python path/to/audit-marketing-md-render.py --json
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
    "ugc-marketing",
    "github-for-marketing",
    "how-to-write-github-readme",
    "how-to-name-ai-products",
}


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


def audit_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    body = _body(text)
    issues: list[dict] = []
    in_children = False

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

    paras = [
        p.strip()
        for p in re.split(r"\n\s*\n", body)
        if p.strip() and not p.strip().startswith("<!--")
    ]
    pseudo = sum(
        1
        for p in paras
        if re.match(r"^\*\*[^*]+\*\*\s+\S", p)
        and len(p) < 320
        and "\n" not in p
    )
    tables = len(re.findall(r"<!-- childrenHtml:start -->[\s\S]*?<table", body))

    render_errors = [x for x in issues if x["code"] in ("E33", "E34", "E36")]
    warnings: list[str] = []
    if tables >= 6:
        warnings.append(f"high-table-count:{tables}")
    if pseudo >= 3:
        warnings.append(f"pseudo-list-paragraphs:{pseudo}")

    return {
        "path": str(path).replace("\\", "/"),
        "render_error_count": len(render_errors),
        "render_errors": render_errors,
        "html_table_count": tables,
        "pseudo_list_paragraph_count": pseudo,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--content-root",
        default=None,
        help="Path to content/ directory (default: alignify production/content)",
    )
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
                text = f.read_text(encoding="utf-8")
                fm = text.split("---", 2)[1] if text.startswith("---") else ""
                if channel == "blog" and not _is_marketing_blog(f.stem, fm):
                    continue
                row = audit_file(f)
                if row["render_error_count"] or row["warnings"]:
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
            if r["warnings"]:
                flags.append(",".join(r["warnings"]))
            print(f"{r['channel']}/{r['locale']}/{r['slug']}  {' | '.join(flags)}")
            for e in r["render_errors"][:5]:
                print(f"  {e['code']} L{e['line']}: {e['snippet']}")

    print(f"\nArticles with issues: {len(results)}", file=sys.stderr)
    render_only = sum(1 for r in results if r["render_error_count"])
    print(f"With render errors (E33/E34/E36): {render_only}", file=sys.stderr)
    return 1 if render_only else 0


if __name__ == "__main__":
    sys.exit(main())
