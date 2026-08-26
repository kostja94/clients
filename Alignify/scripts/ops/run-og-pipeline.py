#!/usr/bin/env python3
"""Run OG generation pipeline: seo -> tools -> blog (fal, parallel workers)."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BATCH = SCRIPT_DIR / "batch-generate-og-covers.py"
MERGE = SCRIPT_DIR / "merge-marketing-briefs.py"
BRIEFS_ROOT = SCRIPT_DIR.parents[1] / "data" / "og-briefs"
DEFAULT_DEPLOY = Path(r"E:\自有部署项目\alignify production")
TOOLS_MAP = DEFAULT_DEPLOY / "src" / "data" / "tools-article-images.ts"


def slugs_with_brief(section: str) -> list[str]:
    root = BRIEFS_ROOT / section
    if not root.is_dir():
        return []
    return sorted(p.parent.name for p in root.rglob("brief.json"))


def all_tools_slugs() -> list[str]:
    text = TOOLS_MAP.read_text(encoding="utf-8")
    return sorted(set(re.findall(r'"([a-z0-9-]+)":\s*`\$\{BASE\}', text)))


def blog_slugs() -> list[str]:
    content = DEFAULT_DEPLOY / "content" / "blog" / "en"
    if not content.is_dir():
        return []
    return sorted(p.stem for p in content.glob("*.md"))


def events_slugs() -> list[str]:
    text = (DEFAULT_DEPLOY / "src" / "data" / "events-meta.ts").read_text(encoding="utf-8")
    return sorted(re.findall(r'"([a-z0-9-]+)":\s*\{', text))


def insights_slugs() -> list[str]:
    text = (DEFAULT_DEPLOY / "src" / "data" / "insights-pages-config.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'slug:\s*"([^"]+)"', text)))


def glossary_article_slugs() -> list[str]:
    text = (DEFAULT_DEPLOY / "src/data/glossary-pages-config.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'slug:\s*"([^"]+)"', text)))


def site_slugs() -> list[str]:
    text = (DEFAULT_DEPLOY / "src/data/site-og-pages.ts").read_text(encoding="utf-8")
    m = re.search(r"SITE_OG_PAGES = \[([\s\S]*?)\]", text)
    if not m:
        return []
    return sorted(set(re.findall(r'"([a-z0-9-]+)"', m.group(1))))


def seo_slugs() -> list[str]:
    content = DEFAULT_DEPLOY / "content" / "seo" / "en"
    return sorted(p.stem for p in content.glob("*.md"))


def count_og(section: str, deploy_root: Path) -> int:
    base = deploy_root / "public" / section
    if not base.is_dir():
        return 0
    return len(list(base.rglob("*-og-*.webp")))


def run_batch(
    section: str,
    slugs: list[str],
    deploy_root: Path,
    workers: int,
    retries: int,
    provider: str,
) -> int:
    if not slugs:
        print(f"\n=== {section.upper()}: no slugs, skip ===")
        return 0
    slug_csv = ",".join(slugs)
    cmd = [
        sys.executable,
        str(BATCH),
        "--section",
        section,
        "--slugs",
        slug_csv,
        "--skip-existing",
        "--retries",
        str(retries),
        "--workers",
        str(workers),
        "--provider",
        provider,
        "--deploy-root",
        str(deploy_root),
    ]
    print(f"\n=== {section.upper()}: {len(slugs)} pages, up to {len(slugs)*2} images ===")
    return subprocess.call(cmd, cwd=str(SCRIPT_DIR))


def merge_briefs() -> None:
    print("\n=== Merging briefs -> registry ===")
    subprocess.check_call([sys.executable, str(MERGE)], cwd=str(SCRIPT_DIR))


def main() -> None:
    parser = argparse.ArgumentParser(description="OG pipeline: seo -> tools -> blog")
    parser.add_argument("--deploy-root", default=str(DEFAULT_DEPLOY))
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--provider", choices=["fal", "apineed"], default="fal")
    parser.add_argument("--skip-seo", action="store_true", help="SEO already done")
    parser.add_argument("--sections", default="seo,tools,blog", help="Comma-separated order")
    args = parser.parse_args()

    deploy = Path(args.deploy_root)
    sections = [s.strip() for s in args.sections.split(",") if s.strip()]
    failed = 0

    slug_map = {
        "seo": seo_slugs,
        "tools": lambda: [s for s in all_tools_slugs() if s in set(slugs_with_brief("tools"))] or all_tools_slugs(),
        "blog": blog_slugs,
        "insights": insights_slugs,
        "events": events_slugs,
        "site": site_slugs,
        "glossary": glossary_article_slugs,
    }

    for section in sections:
        if section not in slug_map:
            print(f"Unknown section: {section}", file=sys.stderr)
            failed += 1
            continue
        if section == "seo" and args.skip_seo:
            print(f"Skip SEO (already complete: {count_og('seo', deploy)} images)")
            continue

        merge_briefs()
        slugs = slug_map[section]()
        # Prefer brief-backed slugs only (skip pages without brief.json)
        brief_slugs = set(slugs_with_brief(section))
        if brief_slugs:
            slugs = [s for s in slugs if s in brief_slugs]
            missing = brief_slugs - set(slug_map[section]() if section != "tools" else all_tools_slugs())
            if missing:
                print(f"  Note: {len(missing)} brief(s) not in content list (skipped)")

        before = count_og(section, deploy)
        rc = run_batch(section, slugs, deploy, args.workers, args.retries, args.provider)
        after = count_og(section, deploy)
        print(f"  {section}: {before} -> {after} OG images")
        if rc != 0:
            failed += 1

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
