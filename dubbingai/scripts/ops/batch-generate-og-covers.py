#!/usr/bin/env python3
"""Batch-generate Dubbing AI blog OG covers (APINEED, EN only)."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from generate_og_cover_paths import job_exists, list_jobs  # noqa: E402

GENERATE = SCRIPT_DIR / "generate-og-cover.py"
DUBBINGAI_CTX = SCRIPT_DIR.parents[1]


def run_one(
    section: str,
    slug: str,
    locale: str,
    retries: int,
    deploy: bool,
    deploy_root: Path | None,
) -> tuple[str, str, str, bool]:
    label = f"{section}/{slug} [{locale}]"
    root = deploy_root if deploy else DUBBINGAI_CTX
    if job_exists(root, slug, locale, deploy=deploy):
        print(f"SKIP existing: {label}")
        return section, slug, locale, True

    cmd = [
        sys.executable,
        str(GENERATE),
        "--section",
        section,
        "--slug",
        slug,
        "--locale",
        locale,
        "--provider",
        "apineed",
    ]
    if deploy:
        cmd.append("--deploy")
        if deploy_root:
            cmd.extend(["--deploy-root", str(deploy_root)])

    for attempt in range(1, retries + 1):
        print(f"\n>>> {label} attempt {attempt}/{retries}")
        r = subprocess.run(cmd, cwd=str(SCRIPT_DIR))
        if r.returncode == 0:
            return section, slug, locale, True
        if attempt < retries:
            wait = 15 * attempt
            print(f"    failed, retry in {wait}s...")
            time.sleep(wait)
    return section, slug, locale, False


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch generate Dubbing AI OG covers via APINEED")
    parser.add_argument("--section", default="blog")
    parser.add_argument("--slugs", required=True, help="Comma-separated slugs")
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--workers", type=int, default=1, help="Parallel jobs")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip when output webp already exists",
    )
    parser.add_argument("--deploy", action="store_true", help="Write to deploy public/")
    parser.add_argument("--deploy-root", help="Dubbing AI deploy repo root")
    args = parser.parse_args()

    deploy_root = Path(args.deploy_root) if args.deploy_root else None
    if args.skip_existing and args.deploy and deploy_root is None:
        env = os.environ.get("DUBBINGAI_DEPLOY_ROOT")
        if env:
            deploy_root = Path(env)

    slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
    jobs = list_jobs(args.section, slugs)
    workers = max(1, args.workers)

    print(f"Jobs: {len(jobs)} | workers: {workers} | provider: apineed | output: 1200x630")

    ok, fail = 0, 0
    check_deploy = args.deploy
    root_for_skip = deploy_root if check_deploy else DUBBINGAI_CTX

    def should_skip(slug: str, locale: str) -> bool:
        return args.skip_existing and job_exists(root_for_skip, slug, locale, deploy=check_deploy)

    if workers == 1:
        for section, slug, locale in jobs:
            if should_skip(slug, locale):
                print(f"SKIP existing: {section}/{slug} [{locale}]")
                ok += 1
                continue
            _, _, _, success = run_one(
                section, slug, locale, args.retries, args.deploy, deploy_root
            )
            ok += success
            fail += not success
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {}
            for section, slug, locale in jobs:
                if should_skip(slug, locale):
                    print(f"SKIP existing: {section}/{slug} [{locale}]")
                    ok += 1
                    continue
                futures[pool.submit(
                    run_one, section, slug, locale, args.retries, args.deploy, deploy_root
                )] = (section, slug, locale)
            for fut in as_completed(futures):
                _, _, _, success = fut.result()
                ok += success
                fail += not success

    print(f"\nDone: {ok} succeeded, {fail} failed (total jobs {len(jobs)})")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
