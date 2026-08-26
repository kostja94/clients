#!/usr/bin/env python3
"""Batch-generate OG covers for multiple slugs (EN + ZH each).

Supports parallel workers (match fal account concurrency) and skip-existing.
"""

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


def run_one(
    section: str,
    slug: str,
    locale: str,
    retries: int,
    deploy_root: Path | None,
    provider: str = "fal",
) -> tuple[str, str, str, bool]:
    """Returns (section, slug, locale, success)."""
    label = f"{section}/{slug} [{locale}]"
    if deploy_root and job_exists(deploy_root, section, slug, locale):
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
        provider,
    ]
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
    parser = argparse.ArgumentParser(description="Batch generate OG covers")
    parser.add_argument("--section", default="marketing")
    parser.add_argument("--slugs", required=True, help="Comma-separated slugs")
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Parallel jobs (match fal concurrency; e.g. 8 for limit 10)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip when deploy public/ already has the webp",
    )
    parser.add_argument("--deploy-root", help="Alignify deploy repo root")
    parser.add_argument(
        "--provider",
        choices=["fal", "apineed"],
        default="fal",
        help="fal (default) or apineed — same quality/size/format as generate-og-cover.py",
    )
    args = parser.parse_args()

    deploy_root = Path(args.deploy_root) if args.deploy_root else None
    if args.skip_existing and deploy_root is None:
        env = os.environ.get("ALIGNIFY_DEPLOY_ROOT")
        if env:
            deploy_root = Path(env)
        else:
            for p in (
                Path(r"E:\自有部署项目\alignify production"),
                Path(r"D:\部署项目\alignify-by-kostja"),
            ):
                if p.is_dir():
                    deploy_root = p
                    break

    slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
    jobs = list_jobs(args.section, slugs)
    workers = max(1, args.workers)

    print(f"Jobs: {len(jobs)} | workers: {workers} | skip-existing: {bool(deploy_root and args.skip_existing)}")

    ok, fail, skipped = 0, 0, 0
    if workers == 1:
        for section, slug, locale in jobs:
            _, _, _, success = run_one(
                section,
                slug,
                locale,
                args.retries,
                deploy_root if args.skip_existing else None,
                args.provider,
            )
            if success:
                ok += 1
            else:
                fail += 1
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {
                pool.submit(
                    run_one,
                    section,
                    slug,
                    locale,
                    args.retries,
                    deploy_root if args.skip_existing else None,
                    args.provider,
                ): (section, slug, locale)
                for section, slug, locale in jobs
            }
            for fut in as_completed(futures):
                section, slug, locale, success = fut.result()
                if success:
                    ok += 1
                else:
                    fail += 1

    print(f"\nDone: {ok} succeeded, {fail} failed (total jobs {len(jobs)})")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
