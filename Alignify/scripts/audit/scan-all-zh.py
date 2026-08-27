#!/usr/bin/env python3
"""Scan all ZH md under production content/*/zh/."""
from __future__ import annotations

import json
import sys
from pathlib import Path

CLIENTS = Path(__file__).resolve().parents[2]
PROD = Path(r"E:/自有部署项目/alignify production")
import importlib.util

spec = importlib.util.spec_from_file_location(
    "audit_locale_voice",
    CLIENTS / "scripts/audit/audit-locale-voice.py",
)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)  # type: ignore

GLOSSARY = json.loads(
    (CLIENTS / "skills/create-article/rules/locale-glossary.json").read_text("utf-8")
)


def main() -> int:
    failures: list[tuple[str, str, int, list[str]]] = []
    passes: list[tuple[str, str]] = []
    for ch in ("blog", "marketing", "tools"):
        d = PROD / f"content/{ch}/zh"
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            slug = p.stem
            issues = a.audit_zh(p.read_text(encoding="utf-8"), GLOSSARY)
            if issues:
                failures.append((ch, slug, len(issues), issues))
            else:
                passes.append((ch, slug))

    print(f"PASS: {len(passes)}  FAIL: {len(failures)}")
    for ch, slug, n, issues in failures:
        print(f"\n=== [{ch}] {slug} ({n}) ===")
        for i in issues[:8]:
            print(i)
        if n > 8:
            print(f"  ... +{n - 8} more")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
