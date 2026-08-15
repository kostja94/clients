#!/usr/bin/env python3
"""Scan video cluster KB files for repeated phrase fingerprints (read-only)."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB_DIR = ROOT / "knowledge" / "tools"
REPORT_DIR = ROOT / "scripts" / "reports"

VIDEO_SLUGS = [
    "video",
    "video-generator",
    "text-to-video",
    "image-to-video",
    "video-to-video",
    "video-editor",
    "video-clipping",
    "video-effects",
    "canvas-video",
    "filmmaking",
    "animation-generator",
    "short-drama",
    "music-video-generator",
]

FINGERPRINTS = [
    "Veo 3.1",
    "Runway Gen-4.5",
    "Kling 3.0",
    "Sora 2",
    "Sora 已于",
    "Motion Brush",
    "native audio",
    "DiT",
    "站内相邻",
    "延伸阅读 · 站内知识块",
]

THRESHOLDS = {
    "Veo 3.1": 8,
    "Runway Gen-4.5": 6,
    "Kling 3.0": 8,
    "Sora 2": 5,
    "Sora 已于": 4,
    "Motion Brush": 6,
}


def main() -> None:
    per_file: dict[str, dict[str, int]] = {}
    totals: Counter[str] = Counter()

    for slug in VIDEO_SLUGS:
        path = KB_DIR / f"{slug}.md"
        if not path.exists():
            per_file[slug] = {"_missing": 1}
            continue
        text = path.read_text(encoding="utf-8")
        counts = {}
        for fp in FINGERPRINTS:
            n = len(re.findall(re.escape(fp), text, flags=re.IGNORECASE))
            counts[fp] = n
            totals[fp] += n
        per_file[slug] = counts

    warnings = []
    for fp, threshold in THRESHOLDS.items():
        if totals[fp] > threshold:
            warnings.append(
                {
                    "fingerprint": fp,
                    "total": totals[fp],
                    "threshold": threshold,
                    "files": {
                        slug: per_file[slug].get(fp, 0)
                        for slug in VIDEO_SLUGS
                        if per_file.get(slug, {}).get(fp, 0)
                    },
                }
            )

    checklist = {
        slug: {
            "has_adjacent": bool(
                re.search(r"\*\*站内相邻\*\*", (KB_DIR / f"{slug}.md").read_text(encoding="utf-8"))
            )
            if (KB_DIR / f"{slug}.md").exists()
            else False,
            "has_footer_links": bool(
                re.search(
                    r"延伸阅读 · 站内知识块",
                    (KB_DIR / f"{slug}.md").read_text(encoding="utf-8"),
                )
            )
            if (KB_DIR / f"{slug}.md").exists()
            else False,
        }
        for slug in VIDEO_SLUGS
    }

    report = {
        "date": date.today().isoformat(),
        "slugs": VIDEO_SLUGS,
        "per_file": per_file,
        "totals": dict(totals),
        "warnings": warnings,
        "checklist": checklist,
    }

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORT_DIR / f"kb-video-overlap-{date.today().isoformat()}.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    print(f"Warnings: {len(warnings)}")
    for w in warnings:
        print(f"  - {w['fingerprint']}: {w['total']} (threshold {w['threshold']})")


if __name__ == "__main__":
    main()
