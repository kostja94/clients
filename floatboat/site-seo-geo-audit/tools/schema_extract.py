#!/usr/bin/env python3
"""Extract JSON-LD blocks and check required fields from Floatboat pages."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from typing import Any

TIMEOUT = 30
DEFAULT_URLS = [
    "https://floatboat.ai/",
    "https://floatboat.ai/pricing",
    "https://floatboat.ai/alternatives/chatgpt-alternative",
    "https://floatboat.ai/blog/calendar-driven-ai-vs-chat-ai",
]

REQUIRED_BY_TYPE = {
    "Organization": ["name", "url"],
    "WebSite": ["name", "url"],
    "SoftwareApplication": ["name", "description"],
    "FAQPage": ["mainEntity"],
    "BlogPosting": ["headline", "datePublished"],
    "BreadcrumbList": ["itemListElement"],
}


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "FloatboatAuditBot/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_json_ld(html: str) -> list[Any]:
    blocks: list[Any] = []
    pattern = re.compile(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        re.I | re.S,
    )
    for match in pattern.finditer(html):
        raw = match.group(1).strip()
        try:
            data = json.loads(raw)
            blocks.append(data)
        except json.JSONDecodeError:
            blocks.append({"_parse_error": raw[:200]})
    return blocks


def flatten_types(blocks: list[Any]) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    for block in blocks:
        if isinstance(block, dict):
            if "@graph" in block and isinstance(block["@graph"], list):
                nodes.extend([n for n in block["@graph"] if isinstance(n, dict)])
            else:
                nodes.append(block)
        elif isinstance(block, list):
            nodes.extend([n for n in block if isinstance(n, dict)])
    return nodes


def audit_node(node: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    node_type = node.get("@type")
    if isinstance(node_type, list):
        node_type = node_type[0] if node_type else None
    if not node_type:
        return issues
    required = REQUIRED_BY_TYPE.get(node_type, [])
    for field in required:
        if field not in node or node[field] in (None, "", []):
            issues.append(f"{node_type} missing `{field}`")
    if node_type == "Organization" and "legalName" not in node:
        issues.append("Organization missing `legalName` (P1)")
    if node_type == "Organization" and "sameAs" not in node:
        issues.append("Organization missing `sameAs` (P1)")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Schema JSON-LD extract for floatboat audit")
    parser.add_argument("--urls", nargs="*", default=DEFAULT_URLS)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report: dict[str, Any] = {}
    all_issues: list[str] = []

    for url in args.urls:
        html = fetch_html(url)
        blocks = extract_json_ld(html)
        nodes = flatten_types(blocks)
        types_found = []
        url_issues: list[str] = []
        for node in nodes:
            t = node.get("@type")
            if isinstance(t, list):
                types_found.extend(t)
            elif t:
                types_found.append(t)
            url_issues.extend(audit_node(node))
        report[url] = {
            "types": sorted(set(types_found)),
            "block_count": len(blocks),
            "issues": url_issues,
        }
        all_issues.extend(f"{url}: {i}" for i in url_issues)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for url, data in report.items():
            print(f"\n{url}")
            print(f"  Types: {', '.join(data['types']) or '(none)'}")
            print(f"  JSON-LD blocks: {data['block_count']}")
            if data["issues"]:
                for issue in data["issues"]:
                    print(f"  ! {issue}")
            else:
                print("  No field issues detected.")

    return 1 if all_issues else 0


if __name__ == "__main__":
    sys.exit(main())
