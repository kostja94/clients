#!/usr/bin/env python3
"""Validate seo-report-bundle JSON against v1.0.0 contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_TOP = [
    "schemaVersion",
    "source",
    "fetchedAt",
    "project",
    "period",
    "healthCheck",
    "extensions",
]

REQUIRED_PERIOD = ["current", "previous"]
REQUIRED_HEALTH = [
    "d0_dataSource",
    "d1_periodAligned",
    "d2_gscDimensionsComplete",
    "d3_ga4Present",
    "d3_bingPresent",
    "d4_pageOverlapRate",
    "d5_magnitudeReasonable",
]


def err(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)


def validate(data: dict) -> list[str]:
    errors: list[str] = []

    if data.get("schemaVersion") != "1.0.0":
        errors.append(f"schemaVersion must be 1.0.0, got {data.get('schemaVersion')!r}")

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing top-level field: {key}")

    period = data.get("period") or {}
    for key in REQUIRED_PERIOD:
        if key not in period:
            errors.append(f"missing period.{key}")
        else:
            for sub in ("start", "end"):
                if sub not in period[key]:
                    errors.append(f"missing period.{key}.{sub}")

    hc = data.get("healthCheck") or {}
    for key in REQUIRED_HEALTH:
        if key not in hc:
            errors.append(f"missing healthCheck.{key}")

    ext = data.get("extensions")
    if ext is not None and not isinstance(ext, dict):
        errors.append("extensions must be object")

    if data.get("gsc") is None and data.get("ga4") is None and data.get("bing") is None:
        errors.append("at least one of gsc / ga4 / bing should be present")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate seo-report-bundle JSON")
    parser.add_argument("bundle", type=Path, help="Path to seo-report-bundle-*.json")
    args = parser.parse_args()

    if not args.bundle.exists():
        err(f"file not found: {args.bundle}")
        return 1

    try:
        data = json.loads(args.bundle.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"invalid JSON: {e}")
        return 1

    errors = validate(data)
    if errors:
        for e in errors:
            err(e)
        return 1

    print(f"OK: {args.bundle.name}")
    hc = data.get("healthCheck", {})
    print(
        f"  source={data.get('source')} "
        f"d0={hc.get('d0_dataSource')} "
        f"d4_overlap={hc.get('d4_pageOverlapRate')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
