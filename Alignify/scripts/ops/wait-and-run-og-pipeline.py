#!/usr/bin/env python3
"""Wait for SEO batch, then run tools -> blog OG pipeline."""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEPLOY = Path(r"E:\自有部署项目\alignify production")
BRIEFS = SCRIPT_DIR.parents[1] / "data" / "og-briefs"
SEO_TARGET = 76  # 38 pages x 2 locales


def count_og(section: str) -> int:
    base = DEPLOY / "public" / section
    return len(list(base.rglob("*-og-*.webp"))) if base.is_dir() else 0


def count_briefs(section: str) -> int:
    root = BRIEFS / section
    return len(list(root.rglob("brief.json"))) if root.is_dir() else 0


def run(cmd: list[str]) -> int:
    print("\n>>", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(SCRIPT_DIR))


def main() -> None:
    wait_pid = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    if wait_pid:
        print(f"Waiting for PID {wait_pid}...")
        while True:
            try:
                import os

                os.kill(wait_pid, 0)
                time.sleep(15)
            except (OSError, ProcessLookupError):
                break

    # Finish SEO if incomplete
    seo_n = count_og("seo")
    if seo_n < SEO_TARGET:
        print(f"SEO {seo_n}/{SEO_TARGET} — finishing remaining...")
        slugs = sorted(p.stem for p in (DEPLOY / "content" / "seo" / "en").glob("*.md"))
        rc = run(
            [
                sys.executable,
                str(SCRIPT_DIR / "batch-generate-og-covers.py"),
                "--section",
                "seo",
                "--slugs",
                ",".join(slugs),
                "--skip-existing",
                "--retries",
                "4",
                "--workers",
                "8",
                "--provider",
                "fal",
                "--deploy-root",
                str(DEPLOY),
            ]
        )
        if rc != 0:
            print("SEO batch had failures; continuing to tools/blog anyway.")
    print(f"SEO done: {count_og('seo')}/{SEO_TARGET}")

    # Wait until brief coverage is complete
    while True:
        subprocess.check_call([sys.executable, str(SCRIPT_DIR / "check-og-briefs.py")], cwd=str(SCRIPT_DIR))
        import re

        out = subprocess.check_output(
            [sys.executable, str(SCRIPT_DIR / "check-og-briefs.py")],
            cwd=str(SCRIPT_DIR),
            text=True,
        )
        if "missing tools:" not in out and "missing blog:" not in out:
            break
        print("Briefs incomplete, waiting 30s...")
        time.sleep(30)

    run([sys.executable, str(SCRIPT_DIR / "merge-marketing-briefs.py")])

    for section in ("tools", "blog"):
        print(f"\n========== {section.upper()} ==========")
        rc = run(
            [
                sys.executable,
                str(SCRIPT_DIR / "run-og-pipeline.py"),
                "--skip-seo",
                "--sections",
                section,
                "--workers",
                "8",
                "--deploy-root",
                str(DEPLOY),
            ]
        )
        if rc != 0:
            sys.exit(rc)

    print(f"\nAll done. SEO={count_og('seo')} Tools={count_og('tools')} Blog={count_og('blog')}")


if __name__ == "__main__":
    main()
