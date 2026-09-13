"""Shared output-path helpers for the unified OG pipeline.

Two output layouts exist across clients (selected via clients/<name>.json):
  - "deploy-section": {deploy_root}/public/{section}/{slug}/{slug}-og-{locale}.webp
                      staging: {context_og_root}/{section}/{slug}/...
  - "context-blog":   {context_og_root}/{slug}/{slug}-og-{locale}.webp
                      deploy:  {deploy_root}/public/blog/images/og/{slug}/...

context_og_root defaults to the legacy in-repo locations (client assets/og or
blog/images/og); clients redirected to the central archive set
"context_og_root" to E:\\clients\\Image Generator\\output\\<client>[\\staging].
"""

from __future__ import annotations

from pathlib import Path

OG_W, OG_H = 1200, 630
OG_EXT = "webp"


def og_filename(slug: str, locale: str) -> str:
    return f"{slug}-og-{locale}.{OG_EXT}"


def _context_base(cfg: dict) -> Path:
    if cfg.get("context_og_root"):
        return Path(cfg["context_og_root"])
    if cfg["output_layout"] == "deploy-section":
        return Path(cfg["ctx_root"]) / cfg["staging_root"]
    return Path(cfg["ctx_root"]) / "blog" / "images" / "og"


def output_og_path(
    cfg: dict,
    section: str,
    slug: str,
    locale: str,
    *,
    mode: str,
    deploy_root: Path | None = None,
) -> Path:
    """mode: 'deploy' | 'context' (staging for deploy-section clients)."""
    name = og_filename(slug, locale)
    if mode == "deploy":
        if cfg["output_layout"] == "deploy-section":
            return deploy_root / "public" / section / slug / name
        return deploy_root / "public" / "blog" / "images" / "og" / slug / name
    # context / staging
    if cfg["output_layout"] == "deploy-section":
        return _context_base(cfg) / section / slug / name
    return _context_base(cfg) / slug / name


def job_exists(
    cfg: dict,
    section: str,
    slug: str,
    locale: str,
    *,
    mode: str,
    deploy_root: Path | None = None,
) -> bool:
    return output_og_path(
        cfg, section, slug, locale, mode=mode, deploy_root=deploy_root
    ).is_file()


def list_jobs(section: str, slugs: list[str], locales: list[str]) -> list[tuple[str, str, str]]:
    return [(section, slug, locale) for slug in slugs for locale in locales]
