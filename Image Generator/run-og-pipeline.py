#!/usr/bin/env python3
"""Run the Alignify OG generation pipeline: seo -> tools -> blog (parallel workers).

Slug discovery reads the Alignify deploy repo (paths from clients/alignify.json).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from og_clients import load_client_config, resolve_deploy_root  # noqa: E402

BATCH = SCRIPT_DIR / "batch-generate-og-covers.py"


def slugs_with_brief(cfg: dict, section: str) -> list[str]:
    root = Path(cfg["ctx_root"]) / cfg["briefs_root"] / section
    if not root.is_dir():
        return []
    return sorted(p.parent.name for p in root.rglob("brief.json"))


def all_tools_slugs(deploy: Path) -> list[str]:
    text = (deploy / "src" / "data" / "tools-article-images.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'"([a-z0-9-]+)":\s*`\$\{BASE\}', text)))


def blog_slugs(deploy: Path) -> list[str]:
    content = deploy / "content" / "blog" / "en"
    if not content.is_dir():
        return []
    return sorted(p.stem for p in content.glob("*.md"))


def events_slugs(deploy: Path) -> list[str]:
    text = (deploy / "src" / "data" / "events-meta.ts").read_text(encoding="utf-8")
    return sorted(re.findall(r'"([a-z0-9-]+)":\s*\{', text))


def insights_slugs(deploy: Path) -> list[str]:
    text = (deploy / "src" / "data" / "insights-pages-config.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'slug:\s*"([^"]+)"', text)))


def glossary_article_slugs(deploy: Path) -> list[str]:
    text = (deploy / "src/data/glossary-pages-config.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'slug:\s*"([^"]+)"', text)))


def site_slugs(deploy: Path) -> list[str]:
    text = (deploy / "src/data/site-og-pages.ts").read_text(encoding="utf-8")
    m = re.search(r"SITE_OG_PAGES = \[([\s\S]*?)\]", text)
    if not m:
        return []
    return sorted(set(re.findall(r'"([a-z0-9-]+)"', m.group(1))))


def seo_slugs(deploy: Path) -> list[str]:
    content = deploy / "content" / "seo" / "en"
    return sorted(p.stem for p in content.glob("*.md"))


def count_og(section: str, deploy_root: Path) -> int:
    base = deploy_root / "public" / section
    if not base.is_dir():
        return 0
    return len(list(base.rglob("*-og-*.webp")))


def run_batch(cfg: dict, section: str, slugs: list[str], deploy_root: Path,
              workers: int, retries: int, provider: str) -> int:
    if not slugs:
        print(f"\n=== {section.upper()}: no slugs, skip ===")
        return 0
    cmd = [
        sys.executable, str(BATCH),
        "--client", cfg["name"],
        "--section", section,
        "--slugs", ",".join(slugs),
        "--skip-existing",
        "--retries", str(retries),
        "--workers", str(workers),
        "--provider", provider,
        "--deploy-root", str(deploy_root),
    ]
    print(f"\n=== {section.upper()}: {len(slugs)} pages, up to {len(slugs)*2} images ===")
    return subprocess.call(cmd, cwd=str(SCRIPT_DIR))


def main() -> None:
    parser = argparse.ArgumentParser(description="Alignify OG pipeline: seo -> tools -> blog")
    parser.add_argument("--client", default="alignify", choices=["alignify"])
    parser.add_argument("--deploy-root")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--provider", default="fal", choices=["fal", "apineed", "gitaigc"])
    parser.add_argument("--skip-seo", action="store_true", help="SEO already done")
    parser.add_argument("--sections", default="seo,tools,blog", help="Comma-separated order")
    args = parser.parse_args()

    cfg = load_client_config(args.client)
    deploy = resolve_deploy_root(cfg, args.deploy_root)
    if deploy is None:
        raise SystemExit(f"Deploy root not found. Set {cfg['deploy_env']} or pass --deploy-root.")
    merge_script = Path(cfg["ctx_root"]) / "scripts" / "ops" / "merge-marketing-briefs.py"
    sections = [s.strip() for s in args.sections.split(",") if s.strip()]
    failed = 0

    slug_map = {
        "seo": lambda: seo_slugs(deploy),
        "tools": lambda: [s for s in all_tools_slugs(deploy) if s in set(slugs_with_brief(cfg, "tools"))] or all_tools_slugs(deploy),
        "blog": lambda: blog_slugs(deploy),
        "insights": lambda: insights_slugs(deploy),
        "events": lambda: events_slugs(deploy),
        "site": lambda: site_slugs(deploy),
        "glossary": lambda: glossary_article_slugs(deploy),
    }

    for section in sections:
        if section not in slug_map:
            print(f"Unknown section: {section}", file=sys.stderr)
            failed += 1
            continue
        if section == "seo" and args.skip_seo:
            print(f"Skip SEO (already complete: {count_og('seo', deploy)} images)")
            continue

        if merge_script.is_file():
            print("\n=== Merging briefs -> registry ===")
            subprocess.check_call([sys.executable, str(merge_script)], cwd=str(SCRIPT_DIR))

        slugs = slug_map[section]()
        # Prefer brief-backed slugs only (skip pages without brief.json)
        brief_slugs = set(slugs_with_brief(cfg, section))
        if brief_slugs:
            slugs = [s for s in slugs if s in brief_slugs]
            missing = brief_slugs - set(slug_map[section]())
            if missing:
                print(f"  Note: {len(missing)} brief(s) not in content list (skipped)")

        before = count_og(section, deploy)
        rc = run_batch(cfg, section, slugs, deploy, args.workers, args.retries, args.provider)
        after = count_og(section, deploy)
        print(f"  {section}: {before} -> {after} OG images")
        if rc != 0:
            failed += 1

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
