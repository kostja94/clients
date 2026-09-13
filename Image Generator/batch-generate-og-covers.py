#!/usr/bin/env python3
"""Batch-generate OG covers for multiple slugs (config-driven, parallel workers).

Locales default to the client config (alignify: en+zh, dubbingai: en).
Output mode defaults to the client config default (deploy or context).
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from og_clients import load_client_config, resolve_deploy_root  # noqa: E402
from og_cover_paths import job_exists, list_jobs  # noqa: E402

GENERATE = SCRIPT_DIR / "generate-og-cover.py"


def run_one(cfg: dict, section: str, slug: str, locale: str, retries: int, provider: str,
            mode: str, deploy_root: Path | None) -> tuple[str, str, str, bool]:
    label = f"{cfg['name']}/{section}/{slug} [{locale}]"
    if job_exists(cfg, section, slug, locale, mode=mode, deploy_root=deploy_root):
        print(f"SKIP existing: {label}")
        return section, slug, locale, True

    cmd = [
        sys.executable, str(GENERATE),
        "--client", cfg["name"],
        "--section", section,
        "--slug", slug,
        "--locale", locale,
        "--provider", provider,
    ]
    if mode == "deploy":
        cmd.append("--deploy")
        if deploy_root:
            cmd.extend(["--deploy-root", str(deploy_root)])
    elif cfg["default_output"] == "deploy":
        cmd.append("--staging")

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
    parser = argparse.ArgumentParser(description="Batch generate OG covers (unified)")
    parser.add_argument("--client", required=True, help="Client name (clients/<name>.json)")
    parser.add_argument("--section")
    parser.add_argument("--slugs", required=True, help="Comma-separated slugs")
    parser.add_argument("--locales", help="Comma-separated locales (default: client config)")
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--workers", type=int, default=1, help="Parallel jobs (match provider concurrency)")
    parser.add_argument("--skip-existing", action="store_true", help="Skip when output webp already exists")
    parser.add_argument("--deploy", action="store_true", help="Force deploy output")
    parser.add_argument("--staging", action="store_true", help="Force context/staging output")
    parser.add_argument("--deploy-root", help="Deploy repo root (overrides env / config defaults)")
    parser.add_argument("--provider", help="fal | apineed | gitaigc (default: client config)")
    args = parser.parse_args()

    cfg = load_client_config(args.client)
    provider = args.provider or cfg["default_provider"]
    section = args.section or cfg["default_section"]
    locales = [l.strip() for l in args.locales.split(",")] if args.locales else list(cfg.get("locales", ["en"]))

    mode = "deploy" if (args.deploy or (cfg["default_output"] == "deploy" and not args.staging)) else "context"
    deploy_root = Path(args.deploy_root) if args.deploy_root else resolve_deploy_root(cfg, None)
    if mode == "deploy" and deploy_root is None:
        raise SystemExit(f"Deploy root not found. Set {cfg['deploy_env']} or pass --deploy-root.")

    slugs = [s.strip() for s in args.slugs.split(",") if s.strip()]
    jobs = list_jobs(section, slugs, locales)
    workers = max(1, args.workers)

    print(f"Client: {cfg['name']} | jobs: {len(jobs)} | workers: {workers} | provider: {provider} | mode: {mode}")

    def should_skip(slug: str, locale: str) -> bool:
        return args.skip_existing and job_exists(cfg, section, slug, locale, mode=mode, deploy_root=deploy_root)

    ok, fail = 0, 0
    if workers == 1:
        for _, slug, locale in jobs:
            if should_skip(slug, locale):
                print(f"SKIP existing: {section}/{slug} [{locale}]")
                ok += 1
                continue
            _, _, _, success = run_one(cfg, section, slug, locale, args.retries, provider, mode, deploy_root)
            ok += success
            fail += not success
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {}
            for _, slug, locale in jobs:
                if should_skip(slug, locale):
                    print(f"SKIP existing: {section}/{slug} [{locale}]")
                    ok += 1
                    continue
                futures[pool.submit(run_one, cfg, section, slug, locale, args.retries, provider, mode, deploy_root)] = (slug, locale)
            for fut in as_completed(futures):
                _, _, _, success = fut.result()
                ok += success
                fail += not success

    print(f"\nDone: {ok} succeeded, {fail} failed (total jobs {len(jobs)})")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
