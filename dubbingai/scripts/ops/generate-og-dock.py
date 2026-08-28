#!/usr/bin/env python3
"""
Dubbing AI OG covers — post-cover standalone workflow ONLY.

Uses vendored https://github.com/chainepic/post-cover:
  background (local / DuckDuckGo / procedural) → PIL frosted dock → 1200×630 WebP

Does NOT call APINEED, fal, or any image-generation API.
Separate from generate-og-cover.py (AI editorial collage).

Usage:
  python generate-og-dock.py --slug spiderman-voice-changer-pubgm
  python generate-og-dock.py --slug spiderman-voice-changer-pubgm --image path/to/bg.jpg
  python generate-og-dock.py --slug spiderman-voice-changer-pubgm --query "gaming headset neon"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parent
DUBBINGAI_CTX = SCRIPT_DIR.parents[1]
VENDOR = DUBBINGAI_CTX / "_vendor" / "post-cover"
REGISTRY_PATH = DUBBINGAI_CTX / "data" / "dock-copy-registry.json"
sys.path.insert(0, str(VENDOR))

from post_cover.core import render_dock_cover  # noqa: E402
from post_cover.search import find_background_image  # noqa: E402

from generate_og_cover_paths import OG_H, OG_W, og_filename  # noqa: E402

POST_COVER_W, POST_COVER_H = 1920, 1080


def dock_output_dir(slug: str) -> Path:
    return DUBBINGAI_CTX / "blog" / "images" / "og-dock" / slug


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def entry_for_slug(registry: dict, slug: str) -> dict:
    entry = registry.get("entries", {}).get(slug)
    if not entry:
        raise SystemExit(
            f"No dock copy for slug={slug}. Add to data/dock-copy-registry.json"
        )
    defaults = registry.get("defaults", {})
    merged = {**defaults, **entry}
    merged["slug"] = slug
    return merged


def scale_post_cover_to_og(img: Image.Image) -> Image.Image:
    """1920×1080 dock → 1200×630 (scale-to-cover, top-aligned — keep headline dock)."""
    im = img.convert("RGB")
    scale = max(OG_W / im.width, OG_H / im.height)
    nw, nh = int(im.width * scale), int(im.height * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left = max(0, (nw - OG_W) // 2)
    top = 0 if nh > OG_H else (nh - OG_H) // 2
    cropped = im.crop((left, top, left + OG_W, top + OG_H))
    if cropped.size != (OG_W, OG_H):
        raise RuntimeError(f"OG size mismatch: {cropped.size}")
    return cropped


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Dubbing AI OG via post-cover only (no AI image APIs)"
    )
    parser.add_argument("--slug", required=True)
    parser.add_argument("--image", help="Local background path (Tier 1 — skip web search)")
    parser.add_argument("--query", help="Override background search query")
    parser.add_argument("--theme", help="post-cover theme preset")
    parser.add_argument("--list", action="store_true", help="List slugs in dock registry")
    args = parser.parse_args()

    registry = load_registry()

    if args.list:
        for slug in registry.get("entries", {}):
            e = registry["entries"][slug]
            print(f"{slug} — {e.get('title', '')}")
        return

    copy = entry_for_slug(registry, args.slug)
    out_dir = dock_output_dir(args.slug)
    out_dir.mkdir(parents=True, exist_ok=True)

    out_1080 = out_dir / f"{args.slug}-dock-1080.webp"
    out_og = out_dir / og_filename(args.slug, "en")
    bg_temp = out_dir / f"{args.slug}-bg-source.webp"

    accent = tuple(copy.get("accent_rgb", [34, 211, 238]))
    theme = args.theme or copy.get("theme", "sky_blue")

    if args.image:
        bg_path = Path(args.image)
        if not bg_path.is_file():
            raise SystemExit(f"Background not found: {bg_path}")
        bg_source = "local"
        print(f"[post-cover] Local background: {bg_path}")
    else:
        query = args.query or copy.get("search_query", "gaming esports neon")
        print(f"[post-cover] Background search: {query!r}")
        if not find_background_image(query, bg_temp):
            raise SystemExit("post-cover background acquisition failed")
        bg_path = bg_temp
        bg_source = "search-or-procedural"

    print(f"[post-cover] Render dock {POST_COVER_W}x{POST_COVER_H} theme={theme}")
    render_dock_cover(
        src_image_path=bg_path,
        title=copy["title"],
        subtitle=copy.get("subtitle", ""),
        note=copy.get("note", ""),
        tags=copy.get("tags", ""),
        cta_text=copy.get("cta_text", "Voice Changer Guide"),
        brand_text=copy.get("brand_text", "DUBBING AI · BLOG"),
        theme_name=theme,
        custom_accent=accent,
        lang="en",
        out_path=out_1080,
    )

    og = scale_post_cover_to_og(Image.open(out_1080))
    og.save(out_og, "WEBP", quality=92)
    print(f"[post-cover] OG {OG_W}x{OG_H}: {out_og} ({out_og.stat().st_size // 1024} KB)")

    meta = {
        "slug": args.slug,
        "workflow": "post-cover-standalone",
        "engine": "https://github.com/chainepic/post-cover",
        "background_source": bg_source,
        "output_size": [OG_W, OG_H],
        "post_cover_size": [POST_COVER_W, POST_COVER_H],
        "intermediate_1080": str(out_1080),
        "title": copy["title"],
        "theme": theme,
        "ai_image_api": None,
    }
    meta_path = out_dir / f"{args.slug}-og-en.meta.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[post-cover] Meta: {meta_path}")


if __name__ == "__main__":
    main()
