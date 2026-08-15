#!/usr/bin/env python3
"""One-click internal links baseline: audit + anchor diversity + cross-page."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
AUDIT_DIR = SCRIPT_DIR.parent / "audit"
REPORTS_DIR = SCRIPT_DIR.parent / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def run_script(name: str, args: list[str]) -> dict | list | None:
    path = AUDIT_DIR / name
    cmd = [sys.executable, str(path), *args]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0 and not proc.stdout.strip():
        print(proc.stderr, file=sys.stderr)
        raise SystemExit(f"{name} failed: {proc.returncode}")
    out = proc.stdout.strip()
    if not out:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return {"raw": out}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", default="both", choices=["en", "zh", "both"])
    parser.add_argument("--source", default="both", choices=["tools", "blog", "both"])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", type=str, default="")
    args = parser.parse_args()

    locales = ["en", "zh"] if args.locale == "both" else [args.locale]
    report: dict = {"date": date.today().isoformat(), "locales": {}}

    for loc in locales:
        internal = run_script(
            "audit-tools-internal-links.py",
            ["--locale", loc, "--source", args.source, "--json"],
        )
        report["locales"][loc] = {"internal_links": internal}

    # cross-page (both locales in one run)
    cross = run_script(
        "audit-cross-page-links.py",
        ["--locale", args.locale, "--json"],
    )
    report["cross_page"] = cross

    anchor = run_script(
        "audit-anchor-text-diversity.py",
        ["--locale", args.locale],
    )
    report["anchor_diversity"] = anchor if isinstance(anchor, dict) else {"raw": anchor}

    # P0 blockers
    p0: list[dict] = []
    for loc, data in report["locales"].items():
        results = (data.get("internal_links") or {}).get("results") or {}
        for slug, entry in results.items():
            metrics = entry.get("metrics") or {}
            violations = entry.get("violations") or []
            high = [v for v in violations if v.get("severity") == "high"]
            if metrics.get("total_distinct", 0) < 5 or high:
                p0.append(
                    {
                        "slug": slug,
                        "locale": loc,
                        "distinct": metrics.get("total_distinct"),
                        "high_violations": high,
                    }
                )
    report["p0_blockers"] = p0

    out_path = Path(args.out) if args.out else REPORTS_DIR / f"internal-links-baseline-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"P0 blockers: {len(p0)}")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
