#!/usr/bin/env python3
"""
R0: Internal href registry audit — invalid slug (404) and wrong tools/blog route.

Usage:
  python audit-internal-href-registry.py --violations-only
  python audit-internal-href-registry.py --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from internal_links_lib import (  # noqa: E402
    find_deploy_root,
    is_blog_tools_slug,
    list_json_slugs,
    parse_blog_tools_slugs,
)

A_TAG = __import__("re").compile(
    r"""<a\s+[^>]*href=(?:["']|\\["'])((?:/zh)?/(tools|blog)/([\w-]+))(?:["']|\\["'])[^>]*>""",
    __import__("re").DOTALL,
)


def expected_segment(slug: str, deploy_root: Path) -> str:
    return "blog" if is_blog_tools_slug(slug, deploy_root) else "tools"


def audit_all(violations_only: bool = False) -> dict:
    root = find_deploy_root()
    blog_tools = parse_blog_tools_slugs(root)
    valid = set(list_json_slugs(root, "both").keys())
    violations: list[dict] = []
    by_source: dict[str, list] = defaultdict(list)

    for route in ("tools", "blog"):
        for loc in ("en", "zh"):
            base = root / "content" / route / loc
            if not base.is_dir():
                continue
            for path in sorted(base.glob("*.json")):
                source = path.stem
                if route == "blog" and source not in blog_tools:
                    continue
                raw = path.read_text(encoding="utf-8")
                for m in A_TAG.finditer(raw):
                    href, segment, target = m.group(1), m.group(2), m.group(3)
                    if loc == "zh" and not href.startswith("/zh/"):
                        continue
                    if loc == "en" and href.startswith("/zh/"):
                        continue
                    if target not in valid:
                        v = {
                            "rule": "R0a",
                            "source_slug": source,
                            "source_route": route,
                            "locale": loc,
                            "href": href,
                            "target_slug": target,
                            "desc": f"invalid slug '{target}' (not in registry)",
                            "severity": "high",
                        }
                        violations.append(v)
                        by_source[f"{source}:{loc}"].append(v)
                    elif expected_segment(target, root) != segment:
                        v = {
                            "rule": "R0b",
                            "source_slug": source,
                            "source_route": route,
                            "locale": loc,
                            "href": href,
                            "target_slug": target,
                            "expected_segment": expected_segment(target, root),
                            "actual_segment": segment,
                            "desc": f"wrong route /{segment}/ for '{target}' (expected /{expected_segment(target, root)}/)",
                            "severity": "high",
                        }
                        violations.append(v)
                        by_source[f"{source}:{loc}"].append(v)

    return {
        "date": date.today().isoformat(),
        "valid_slug_count": len(valid),
        "violation_count": len(violations),
        "violations": violations,
        "by_source": dict(by_source),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--violations-only", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    report = audit_all(args.violations_only)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {out_path}")

    if args.json or not args.violations_only:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"R0 violations: {report['violation_count']}")
        for v in report["violations"]:
            print(f"  [{v['locale']}] {v['source_slug']}: {v['desc']} ({v['href']})")

    if report["violation_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
