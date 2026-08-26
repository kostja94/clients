"""Shared paths for OG batch / generate scripts."""

from __future__ import annotations

from pathlib import Path

OG_EXT = "webp"


def og_filename(slug: str, locale: str) -> str:
    return f"{slug}-og-{locale}.{OG_EXT}"


def deploy_og_path(deploy_root: Path, section: str, slug: str, locale: str) -> Path:
    return deploy_root / "public" / section / slug / og_filename(slug, locale)


def job_exists(deploy_root: Path, section: str, slug: str, locale: str) -> bool:
    return deploy_og_path(deploy_root, section, slug, locale).is_file()


def list_jobs(section: str, slugs: list[str]) -> list[tuple[str, str, str]]:
    return [(section, slug, locale) for slug in slugs for locale in ("en", "zh")]
