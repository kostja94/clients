#!/usr/bin/env python3
"""
Generate tools-screenshot-registry.json entries from audit-tools-images.mjs output.

Usage:
  python generate-registry-from-audit.py reports/tools-images-audit-2026-06-17.json
  python generate-registry-from-audit.py reports/tools-images-audit-2026-06-17.json --severity P0 --merge
"""

import argparse
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REGISTRY = os.path.join(SCRIPT_DIR, "..", "data", "tools-screenshot-registry.json")

if os.path.isdir("D:\\部署项目\\alignify-by-kostja"):
    PROJECT_ROOT = "D:\\部署项目\\alignify-by-kostja"
else:
    PROJECT_ROOT = os.environ.get("ALIGNIFY_DEPLOY_ROOT", os.getcwd())

CONTENT_TOOLS = os.path.join(PROJECT_ROOT, "content", "tools")


def link_url(page_slug, product_id):
    for locale in ("en", "zh"):
        fp = os.path.join(CONTENT_TOOLS, locale, f"{page_slug}.json")
        if not os.path.exists(fp):
            continue
        with open(fp, encoding="utf-8") as f:
            doc = json.load(f)
        for block in doc.get("blocks", []):
            if block.get("type") != "bestTools":
                continue
            for tool in block.get("tools", []):
                if tool.get("id") == product_id:
                    return tool.get("linkUrl")
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json", help="Audit JSON from audit-tools-images.mjs")
    parser.add_argument("--severity", default=None, help="Filter severity (P0, P1, P2)")
    parser.add_argument("--merge", action="store_true", help="Merge into existing registry")
    parser.add_argument("--out", default=DEFAULT_REGISTRY, help="Output registry path")
    args = parser.parse_args()

    with open(args.audit_json, encoding="utf-8") as f:
        audit = json.load(f)

    registry = {}
    if args.merge and os.path.exists(args.out):
        with open(args.out, encoding="utf-8") as f:
            raw = json.load(f)
            registry = {k: v for k, v in raw.items() if not k.startswith("_")}

    actionable_types = {
        "missing_file",
        "filename_mismatch",
        "known_mismatch",
        "low_size",
        "low_resolution",
    }

    seen = set()
    added = 0
    for issue in audit.get("issues", []):
        if args.severity and issue.get("severity") != args.severity:
            continue
        if issue.get("type") not in actionable_types:
            continue
        key = issue.get("key")
        if not key or key in seen:
            continue
        seen.add(key)

        page_slug, product_id = key.split(":", 1)
        url = issue.get("linkUrl") or link_url(page_slug, product_id)
        out = issue.get("outputPath")
        if not url or not out:
            continue

        if args.merge and key in registry:
            continue

        entry = {
            "screenshotUrl": url,
            "outputPath": out,
            "reason": issue.get("detail", ""),
            "priority": issue.get("severity", "P1"),
        }
        if issue.get("type") in ("filename_mismatch", "known_mismatch", "missing_file"):
            entry["jsonImageSrc"] = f"/{out}"

        registry[key] = entry
        added += 1

    out_doc = {"_meta": {
        "description": "Screenshot URL registry for Tools BestTools product images.",
        "keyFormat": "{pageSlug}:{productId}",
        "updated": __import__("datetime").date.today().isoformat(),
    }}
    out_doc.update(dict(sorted(registry.items())))

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out_doc, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Wrote {added} entries to {args.out} (total {len(registry)} products)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
