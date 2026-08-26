#!/usr/bin/env python3
"""
Move legacy OG covers from context assets/og/ -> deploy public/ (one-time cleanup).

Uses shutil.move — source is removed; deploy is the only copy.

Usage:
  python migrate-og-covers.py --all-staging
  python migrate-og-covers.py --section marketing --slug geo --locale en
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ALIGNIFY_CTX = SCRIPT_DIR.parents[1]
OG_STAGING = ALIGNIFY_CTX / "assets" / "og"
REGISTRY_PATH = ALIGNIFY_CTX / "data" / "og-prompt-registry.json"
OG_LOCALE_READY_PATH = "src/lib/og-image-path.ts"

DEFAULT_DEPLOY_ROOTS = [
    Path(r"E:\自有部署项目\alignify production"),
    Path(r"D:\部署项目\alignify-by-kostja"),
]


def resolve_deploy_root(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit)
    import os

    env = os.environ.get("ALIGNIFY_DEPLOY_ROOT")
    if env:
        return Path(env)
    for p in DEFAULT_DEPLOY_ROOTS:
        if p.is_dir():
            return p
    raise SystemExit("Deploy root not found. Set ALIGNIFY_DEPLOY_ROOT or pass --deploy-root.")


OG_EXT = "webp"


def og_filename(slug: str, locale: str) -> str:
    return f"{slug}-og-{locale}.{OG_EXT}"


def staging_path(section: str, slug: str, locale: str) -> Path:
    return OG_STAGING / section / slug / og_filename(slug, locale)


def deploy_path(deploy_root: Path, section: str, slug: str, locale: str) -> Path:
    return deploy_root / "public" / section / slug / og_filename(slug, locale)


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def register_ready(deploy_root: Path, section: str, slug: str, locale: str, dry_run: bool) -> None:
    ts_path = deploy_root / OG_LOCALE_READY_PATH
    if not ts_path.exists():
        print(f"WARN: {ts_path} not found, skip OG_LOCALE_READY update")
        return

    token = f'"{section}/{slug}:{locale}"'
    text = ts_path.read_text(encoding="utf-8")
    if token in text:
        print(f"Already registered: {token}")
        return

    pattern = r"(export const OG_LOCALE_READY = new Set<string>\(\[\n)([\s\S]*?)(\n\]\);)"
    match = re.search(pattern, text)
    if not match:
        raise SystemExit(f"Could not parse OG_LOCALE_READY block in {ts_path}")

    body = match.group(2)
    lines = [ln for ln in body.splitlines() if ln.strip()]
    insert = f'  {token},'
    lines.append(insert)
    new_body = "\n".join(lines)
    if lines:
        new_body = "\n" + new_body
    new_text = text[: match.start()] + match.group(1) + new_body + match.group(3) + text[match.end() :]

    if dry_run:
        print(f"Would append to OG_LOCALE_READY: {token}")
        return

    ts_path.write_text(new_text, encoding="utf-8")
    print(f"Registered OG_LOCALE_READY: {token}")


def migrate_one(
    deploy_root: Path,
    section: str,
    slug: str,
    locale: str,
    dry_run: bool,
    register: bool,
) -> bool:
    src = staging_path(section, slug, locale)
    dst = deploy_path(deploy_root, section, slug, locale)

    if not src.is_file():
        print(f"SKIP missing staging file: {src}")
        return False

    if dry_run:
        action = "move" if not dst.is_file() else "move (overwrite deploy)"
        print(f"Would {action}:\n  {src}\n  -> {dst}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.is_file():
            dst.unlink()
        shutil.move(str(src), str(dst))
        print(f"Moved -> {dst} ({dst.stat().st_size // 1024} KB)")
        # Remove empty staging dirs
        try:
            src.parent.rmdir()
            src.parent.parent.rmdir()
        except OSError:
            pass

    if register:
        register_ready(deploy_root, section, slug, locale, dry_run)
    return True


def migrate_all_staging(deploy_root: Path, dry_run: bool, register: bool) -> int:
    ok = 0
    if not OG_STAGING.is_dir():
        return 0
    for src in sorted(OG_STAGING.rglob(f"*-og-*.{OG_EXT}")):
        rel = src.relative_to(OG_STAGING)
        if len(rel.parts) < 3:
            continue
        section, slug = rel.parts[0], rel.parts[1]
        locale = "en" if "-og-en." in src.name else "zh" if "-og-zh." in src.name else None
        if locale is None:
            continue
        if migrate_one(deploy_root, section, slug, locale, dry_run, register):
            ok += 1
    return ok


def purge_staging_duplicates(deploy_root: Path, dry_run: bool) -> int:
    """Remove staging copies when deploy already has the file (after mistaken copy)."""
    n = 0
    if not OG_STAGING.is_dir():
        return 0
    for src in sorted(OG_STAGING.rglob(f"*-og-*.{OG_EXT}")):
        rel = src.relative_to(OG_STAGING)
        if len(rel.parts) < 3:
            continue
        section, slug = rel.parts[0], rel.parts[1]
        locale = "en" if "-og-en." in src.name else "zh" if "-og-zh." in src.name else None
        if locale is None:
            continue
        dst = deploy_path(deploy_root, section, slug, locale)
        if dst.is_file():
            if dry_run:
                print(f"Would delete duplicate staging: {src}")
            else:
                src.unlink()
                print(f"Deleted duplicate staging: {src}")
                try:
                    src.parent.rmdir()
                except OSError:
                    pass
            n += 1
    return n


def main() -> None:
    parser = argparse.ArgumentParser(description="Move OG covers staging -> deploy (single copy)")
    parser.add_argument("--section", default="tools")
    parser.add_argument("--slug")
    parser.add_argument("--locale", choices=["en", "zh"])
    parser.add_argument("--deploy-root")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-register", action="store_true", help="Move only, do not edit OG_LOCALE_READY")
    parser.add_argument(
        "--approved",
        action="store_true",
        help="Move all registry entries with status=approved",
    )
    parser.add_argument(
        "--all-staging",
        action="store_true",
        help="Move all files under assets/og/ to deploy public/ (source removed)",
    )
    parser.add_argument(
        "--purge-duplicates",
        action="store_true",
        help="Delete staging copies when deploy already has the file",
    )
    args = parser.parse_args()

    deploy_root = resolve_deploy_root(args.deploy_root)
    register = not args.no_register

    if args.purge_duplicates:
        n = purge_staging_duplicates(deploy_root, args.dry_run)
        print(f"Purged {n} duplicate staging file(s)")
        return

    if args.all_staging:
        ok = migrate_all_staging(deploy_root, args.dry_run, register)
        print(f"Moved {ok} staging cover(s)")
        return

    if args.approved:
        registry = load_registry()
        ok = 0
        for entry in registry["entries"]:
            if entry.get("status") != "approved":
                continue
            if migrate_one(
                deploy_root,
                entry["section"],
                entry["slug"],
                entry["locale"],
                args.dry_run,
                register,
            ):
                ok += 1
        print(f"Moved {ok} approved cover(s)")
        return

    if not args.slug or not args.locale:
        parser.error("--slug and --locale required unless --all-staging or --purge-duplicates")

    migrate_one(deploy_root, args.section, args.slug, args.locale, args.dry_run, register)


if __name__ == "__main__":
    main()
