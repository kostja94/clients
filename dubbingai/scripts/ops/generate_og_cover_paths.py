"""Shared paths for Dubbing AI OG batch / generate scripts."""

from __future__ import annotations

from pathlib import Path

OG_W, OG_H = 1200, 630
OG_EXT = "webp"


def og_filename(slug: str, locale: str = "en") -> str:
    return f"{slug}-og-{locale}.{OG_EXT}"


def context_og_path(ctx_root: Path, slug: str, locale: str = "en") -> Path:
    return ctx_root / "blog" / "images" / "og" / slug / og_filename(slug, locale)


def deploy_og_path(deploy_root: Path, slug: str, locale: str = "en") -> Path:
    return deploy_root / "public" / "blog" / "images" / "og" / slug / og_filename(slug, locale)


def job_exists(root: Path, slug: str, locale: str = "en", *, deploy: bool = False) -> bool:
    path = deploy_og_path(root, slug, locale) if deploy else context_og_path(root, slug, locale)
    return path.is_file()


def list_jobs(section: str, slugs: list[str], locale: str = "en") -> list[tuple[str, str, str]]:
    return [(section, slug, locale) for slug in slugs]
