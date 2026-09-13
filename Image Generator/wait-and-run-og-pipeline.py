#!/usr/bin/env python3
"""Wait for a PID to exit, finish SEO batch, then run tools -> blog OG pipeline
for Alignify (paths from clients/alignify.json)."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from og_clients import load_client_config, resolve_deploy_root  # noqa: E402

BATCH = SCRIPT_DIR / "batch-generate-og-covers.py"
RUN_PIPELINE = SCRIPT_DIR / "run-og-pipeline.py"
SEO_TARGET = 76  # 38 pages x 2 locales


def count_og(deploy: Path, section: str) -> int:
    base = deploy / "public" / section
    return len(list(base.rglob("*-og-*.webp"))) if base.is_dir() else 0


def count_briefs(cfg: dict, section: str) -> int:
    root = Path(cfg["ctx_root"]) / cfg["briefs_root"] / section
    return len(list(root.rglob("brief.json"))) if root.is_dir() else 0


def run(cmd: list[str]) -> int:
    print("\n>>", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(SCRIPT_DIR))


def main() -> None:
    cfg = load_client_config("alignify")
    deploy = resolve_deploy_root(cfg, None)
    if deploy is None:
        raise SystemExit(f"Deploy root not found. Set {cfg['deploy_env']}.")
    alignify_ops = Path(cfg["ctx_root"]) / "scripts" / "ops"

    wait_pid = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    if wait_pid:
        print(f"Waiting for PID {wait_pid}...")
        while True:
            try:
                os.kill(wait_pid, 0)
                time.sleep(15)
            except (OSError, ProcessLookupError):
                break

    # Finish SEO if incomplete
    seo_n = count_og(deploy, "seo")
    if seo_n < SEO_TARGET:
        print(f"SEO {seo_n}/{SEO_TARGET} — finishing remaining...")
        slugs = sorted(p.stem for p in (deploy / "content" / "seo" / "en").glob("*.md"))
        rc = run(
            [
                sys.executable, str(BATCH),
                "--client", "alignify",
                "--section", "seo",
                "--slugs", ",".join(slugs),
                "--skip-existing",
                "--retries", "4",
                "--workers", "8",
                "--provider", "fal",
                "--deploy-root", str(deploy),
            ]
        )
        if rc != 0:
            print("SEO batch had failures; continuing to tools/blog anyway.")
    print(f"SEO done: {count_og(deploy, 'seo')}/{SEO_TARGET}")

    # Wait until brief coverage is complete
    check_script = alignify_ops / "check-og-briefs.py"
    while True:
        out = subprocess.check_output([sys.executable, str(check_script)], cwd=str(SCRIPT_DIR), text=True)
        print(out)
        if "missing tools:" not in out and "missing blog:" not in out:
            break
        print("Briefs incomplete, waiting 30s...")
        time.sleep(30)

    merge_script = alignify_ops / "merge-marketing-briefs.py"
    if merge_script.is_file():
        run([sys.executable, str(merge_script)])

    for section in ("tools", "blog"):
        print(f"\n========== {section.upper()} ==========")
        rc = run(
            [
                sys.executable, str(RUN_PIPELINE),
                "--skip-seo",
                "--sections", section,
                "--workers", "8",
                "--deploy-root", str(deploy),
            ]
        )
        if rc != 0:
            sys.exit(rc)

    print(f"\nAll done. SEO={count_og(deploy, 'seo')} Tools={count_og(deploy, 'tools')} Blog={count_og(deploy, 'blog')}")


if __name__ == "__main__":
    main()
