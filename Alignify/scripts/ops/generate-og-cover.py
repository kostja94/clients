#!/usr/bin/env python3
"""
Generate Alignify OG covers via GPT Image 2 (fal or APINEED).

Both providers share the same generation params:
  quality=high, jpeg, 1 image, 1216x632 then crop to 1200x630 WebP.

Default output: deploy repo public/ ONLY (single source of truth).

Usage:
  set FAL_KEY=your-key
  set APINEED_API_KEY=your-key
  set ALIGNIFY_DEPLOY_ROOT=E:\\自有部署项目\\alignify production
  python generate-og-cover.py --slug image-generator --locale en
  python generate-og-cover.py --provider apineed --section seo --slug serp --locale en
  python generate-og-cover.py --to-staging --slug image-generator --locale en   # preview only
  python generate-og-cover.py --list

Live path (default):
  {DEPLOY_ROOT}/public/{section}/{slug}/{slug}-og-{locale}.webp
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
import time
import urllib.error
import urllib.request
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Install Pillow: pip install pillow", file=sys.stderr)
    raise

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from og_brief_lib import (  # noqa: E402
    QUALITY_DIRECTIVE,
    format_brief_prompt_block,
    load_brief,
)

ALIGNIFY_CTX = SCRIPT_DIR.parents[1]
REGISTRY_PATH = ALIGNIFY_CTX / "data" / "og-prompt-registry.json"
OG_STAGING_ROOT = ALIGNIFY_CTX / "assets" / "og"
BRAND_LOGO = ALIGNIFY_CTX / "assets" / "brand" / "icon-192x192.png"

DEFAULT_DEPLOY_ROOTS = [
    Path(r"E:\自有部署项目\alignify production"),
    Path(r"D:\部署项目\alignify-by-kostja"),
]

FAL_ENDPOINT = "https://queue.fal.run/openai/gpt-image-2"
APINEED_ENDPOINT = "https://apineed.com/v1/media/generations"
OG_W, OG_H = 1200, 630
GEN_W, GEN_H = 1216, 632
GEN_QUALITY = "high"
GEN_OUTPUT_FORMAT = "jpeg"
GEN_NUM_IMAGES = 1
GEN_SIZE = f"{GEN_W}x{GEN_H}"
OG_EXT = "webp"
WEBP_QUALITY = 92
HTTP_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

ACCENTS = {
    "klein-blue": ("#002FA7", "Klein blue"),
    "mars-green": ("#006B54", "Mars green"),
    "titian-red": ("#C62828", "Titian red"),
    "alignify-navy": ("#1e3a5f", "Alignify navy"),
}

SWISS_GRID_STYLE = (
    "Swiss modernist editorial poster for a B2B AI tools publication. "
    "Warm off-white paper background (#F5F2EA), subtle paper grain, modular grid, "
    "70% negative space, one high-chroma accent color block, flat fields, no 3D mockups, "
    "no product logos, no stock photos, no glossy SaaS gradients. "
    "Clean bold sans-serif typography area for headline. "
    "1200x630 landscape social share card composition."
)

EDITORIAL_COLLAGE_STYLE = (
    "High-end editorial paper collage social share card, 1200x630 landscape, "
    "like a zine cover or 2mv-style editorial OG. "
    "Off-white textured paper (#F4F4F2) with torn-paper layers and halftone grain. "
    "Every visual must illustrate THIS page's topic — not generic abstract decoration."
)

# PPT-like text density + safe zones for PIL overlays
TEXT_BUDGET_RULES = (
    "TEXT BUDGET (PPT slide — keep copy moderate):\n"
    "- ONLY render the headline and optional one-line subtitle provided below.\n"
    "- Do NOT add ranking lists, model names, arrow labels, footnotes, slogans, "
    "UI field labels, or extra captions anywhere on the image.\n"
    "- Convey details through visuals only (photos, grids, icons, mockups with blurred/illegible text).\n"
    "- Do NOT render Kostja, Alignify wordmark, or logo — exactly ONE subtle brand mark added in post-production.\n"
)

LOGO_INNER_HEIGHT = 44
LOGO_MARGIN = 18
AUTHOR_MARGIN = 18
AUTHOR_FONT_SIZE = 20
WORDMARK_FONT_SIZE = 22
DEFAULT_AUTHOR = "Kostja"
DEFAULT_WORDMARK = "Alignify"
BRAND_MODES = ("kostja", "alignify", "logo")
# Headline usually occupies top-left; brand mark uses one other corner.
BRAND_CORNERS = ("bottom-left", "bottom-right", "top-right")
CORNER_SAFE_ZONES = {
    "bottom-left": "bottom-left 140x48px",
    "bottom-right": "bottom-right 100x100px",
    "top-right": "top-right 100x100px",
}
FONT_BOLD_CANDIDATES = [
    Path(r"C:\Windows\Fonts\arialbd.ttf"),
    Path(r"C:\Windows\Fonts\SegoeUI-Bold.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]


def resolve_deploy_root(explicit: str | None) -> Path | None:
    if explicit:
        return Path(explicit)
    env = os.environ.get("ALIGNIFY_DEPLOY_ROOT")
    if env:
        return Path(env)
    for p in DEFAULT_DEPLOY_ROOTS:
        if p.is_dir():
            return p
    return None


def resolve_output_root(to_staging: bool, deploy_root: Path | None) -> tuple[Path, str]:
    if to_staging:
        return ALIGNIFY_CTX, "context"
    if deploy_root is None:
        raise SystemExit("Deploy root not found. Set ALIGNIFY_DEPLOY_ROOT or pass --deploy-root.")
    return deploy_root, "deploy"


def og_filename(slug: str, locale: str) -> str:
    return f"{slug}-og-{locale}.{OG_EXT}"


def output_path(root: Path, mode: str, section: str, slug: str, locale: str) -> Path:
    name = og_filename(slug, locale)
    if mode == "deploy":
        return root / "public" / section / slug / name
    return root / "assets" / "og" / section / slug / name


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def find_entry(registry: dict, section: str, slug: str, locale: str) -> dict:
    for entry in registry["entries"]:
        if (
            entry["section"] == section
            and entry["slug"] == slug
            and entry["locale"] == locale
        ):
            return entry
    raise SystemExit(f"No registry entry for {section}/{slug} locale={locale}")


def pick_brand_placement(
    section: str,
    slug: str,
    locale: str,
    *,
    shuffle: bool = False,
    brand_mode: str | None = None,
    brand_corner: str | None = None,
) -> tuple[str, str]:
    """Pick ONE brand element (kostja | alignify | logo) + corner (stable per slug)."""
    valid_corners = set(BRAND_CORNERS)
    if brand_mode and brand_mode not in BRAND_MODES and brand_mode != "none":
        raise SystemExit(f"Invalid --brand-mode: {brand_mode} (use kostja|alignify|logo|none)")
    if brand_corner and brand_corner not in valid_corners:
        raise SystemExit(f"Invalid --brand-corner: {brand_corner}")

    rng = random.Random()
    if shuffle:
        rng.seed()
    else:
        digest = hashlib.sha256(f"{section}/{slug}:{locale}:brand-v35".encode()).hexdigest()
        rng.seed(int(digest[:8], 16))

    mode = brand_mode or rng.choice(BRAND_MODES)
    corner = brand_corner or rng.choice(BRAND_CORNERS)
    return mode, corner


def pick_branding_corners(*args, **kwargs) -> tuple[str, str]:
    """Deprecated alias — returns same corner twice for legacy callers."""
    _, corner = pick_brand_placement(*args, **kwargs)
    return corner, corner


def corner_origin(corner: str, box_w: int, box_h: int, margin: int) -> tuple[int, int]:
    if corner == "bottom-left":
        return margin, OG_H - box_h - margin
    if corner == "bottom-right":
        return OG_W - box_w - margin, OG_H - box_h - margin
    if corner == "top-right":
        return OG_W - box_w - margin, margin
    raise ValueError(f"Unknown corner: {corner}")


def build_prompt(
    entry: dict,
    defaults: dict | None = None,
    brand_mode: str = "kostja",
    brand_corner: str = "bottom-left",
) -> str:
    defaults = defaults or {}
    style = entry.get("style", defaults.get("style", "editorial-collage"))
    accent_key = entry.get("accent", "klein-blue")
    accent_hex, accent_name = ACCENTS.get(accent_key, ACCENTS["klein-blue"])
    locale = entry["locale"]
    lang_rule = (
        "All on-image text must be English only (headline + subtitle only)."
        if locale == "en"
        else "All on-image text must be Simplified Chinese only (headline + subtitle only). "
        "Do not mix English except Alignify if needed."
    )
    headline = entry["headline"]
    headline_line2 = entry.get("headline_line2", "")
    subtitle = entry.get("subtitle", "")
    tagline = entry.get("tagline", "")
    composition = entry.get("composition") or entry.get("motif", "")
    page_ref = f"{entry.get('section', 'tools')}/{entry.get('slug', '')}"
    section = entry.get("section", "tools")
    slug = entry.get("slug", "")
    brief = load_brief(section, slug)
    brief_block = format_brief_prompt_block(brief, entry)

    if style == "editorial-collage":
        headline_block = f"  Line 1 (extra-large, bold, dominant): '{headline}'"
        if headline_line2:
            headline_block += f"\n  Line 2 (extra-large, bold): '{headline_line2}'"
        subtitle_line = (
            f"- Subtitle line (medium-large, clearly readable): '{subtitle}'\n"
            f"- Optional {accent_name} accent underline under subtitle.\n"
            if subtitle
            else ""
        )
        tagline_line = (
            f"- Tagline line (medium size, below subtitle): '{tagline}'\n"
            if tagline
            else ""
        )
        if locale == "en":
            typography_rules = (
                "Typography prominence (EN — text should feel substantial, like a PPT title slide):\n"
                "- Headline block must dominate the upper-left — bold condensed sans-serif, ~35–40% canvas width.\n"
                "- Subtitle + tagline must be clearly legible at thumbnail size (not tiny footnotes).\n"
            )
            clutter_rule = (
                "Do NOT output a sparse poster with tiny text and oversized empty visuals.\n"
            )
        else:
            typography_rules = (
                "Typography restraint (ZH — minimal copy, visuals carry the story):\n"
                "- Headline block upper-left, bold, readable — but do NOT add any text beyond the lines listed below.\n"
                "- Subtitle only if provided — one line max.\n"
            )
            clutter_rule = (
                "STRICT ZH TEXT BAN: Do NOT render ranking lists, model names, category labels on images "
                "(人像/风景/产品/抽象), prompt example cards, section headers (热门模型排行), UI field labels, "
                "footer slogans, arrows with labels, or any extra Chinese/English captions.\n"
                "LAYOUT FILL: Do NOT leave large empty white rectangles, blank rounded cards, or unfilled "
                "placeholder panels — every collage piece must contain visual content (blurred lines, icons, "
                "thumbnails, photos, textures). Canvas should feel full, not sparse.\n"
            )
        return (
            f"{EDITORIAL_COLLAGE_STYLE}\n"
            f"Page: {page_ref}. Accent: {accent_name} ({accent_hex}).\n\n"
            f"{QUALITY_DIRECTIVE}"
            f"{brief_block}"
            f"{TEXT_BUDGET_RULES}\n"
            f"{typography_rules}"
            f"{headline_block}\n"
            f"{subtitle_line}"
            f"{tagline_line}\n"
            f"Page-relevant visuals (composition detail):\n"
            f"{composition}\n\n"
            f"{lang_rule}\n"
            f"{clutter_rule}"
            "Do NOT clutter with paragraphs or multiple text cards.\n"
            "Spell headline/subtitle/tagline correctly. No watermark.\n"
            f"Leave {CORNER_SAFE_ZONES[brand_corner]} subtly clear for a small seamless brand mark ({brand_mode}) in post.\n"
            "Editorial collage quality similar to 2mv editorial OG — visual storytelling, PPT-level copy."
        )

    return (
        f"{SWISS_GRID_STYLE}\n"
        f"Accent: {accent_name} ({accent_hex}).\n"
        f"Visual motif: {composition}.\n"
        f"Layout: large bold headline at upper-left reading exactly:\n"
        f"  Line 1: '{headline}'\n"
        + (f"  Line 2: '{headline_line2}'\n" if headline_line2 else "")
        + (f"  Subtitle: '{subtitle}'\n" if subtitle else "")
        + f"{lang_rule}\n"
        "Spell all words correctly, no gibberish, no fake letters, no watermark.\n"
        "Leave the bottom-right corner clean for logo placement (about 180x90 px safe zone).\n"
        "High contrast, magazine editorial quality."
    )


def fal_generate(prompt: str, fal_key: str) -> bytes:
    payload = json.dumps(
        {
            "prompt": prompt,
            "image_size": {"width": GEN_W, "height": GEN_H},
            "quality": GEN_QUALITY,
            "num_images": GEN_NUM_IMAGES,
            "output_format": GEN_OUTPUT_FORMAT,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        FAL_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"Key {fal_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        submit = json.loads(resp.read().decode())

    status_url = submit.get("status_url") or submit.get("response_url")
    response_url = submit.get("response_url")
    if not status_url:
        raise RuntimeError(f"Unexpected fal submit response: {submit}")

    for _ in range(90):
        time.sleep(2)
        with urllib.request.urlopen(
            urllib.request.Request(
                status_url,
                headers={"Authorization": f"Key {fal_key}"},
            ),
            timeout=60,
        ) as resp:
            status = json.loads(resp.read().decode())
        state = status.get("status", "")
        if state == "COMPLETED":
            break
        if state in ("FAILED", "CANCELLED"):
            raise RuntimeError(f"fal job failed: {status}")
    else:
        raise TimeoutError("fal job timed out")

    with urllib.request.urlopen(
        urllib.request.Request(
            response_url,
            headers={"Authorization": f"Key {fal_key}"},
        ),
        timeout=60,
    ) as resp:
        result = json.loads(resp.read().decode())

    images = result.get("images") or []
    if not images:
        raise RuntimeError(f"No images in fal result: {result}")

    image_url = images[0]["url"]
    with urllib.request.urlopen(image_url, timeout=120) as resp:
        return resp.read()


def apineed_generate(prompt: str, api_key: str) -> bytes:
    """OpenAI-compatible Images API via APINEED's async media endpoint.

    NOTE (2026-09): APINEED deprecated the synchronous /v1/images/generations
    endpoint. New flow is POST /v1/media/generations with
    {"workflow": "text_to_image", "model": ..., "input": {"prompt": ...}}
    which returns a task id; poll GET /v1/media/generations/{id} until
    status == "succeeded", then download outputs[0].url.

    The API no longer accepts a size parameter (silently routes upstream);
    the generated canvas follows the prompt, so keep the "wide 1200x630
    landscape" phrasing in the prompt for OG-compatible output.
    """
    import subprocess
    import tempfile
    import time

    quality = os.environ.get("OG_APINEED_QUALITY", GEN_QUALITY)
    print(f"  APINEED quality={quality} (async /v1/media/generations)")

    # Force a landscape 16:9-ish canvas for OG use (API ignores size params).
    full_prompt = (
        f"{prompt}\n\n"
        "COMPOSITION: wide landscape 16:9 horizontal frame, 1200x630 social share card aspect. "
        "Do NOT render a portrait or square image."
    )

    body = {
        "workflow": "text_to_image",
        "model": "gpt-image-2",
        "input": {"prompt": full_prompt},
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(body, tmp, ensure_ascii=False)
        tmp_path = tmp.name
    try:
        proc = subprocess.run(
            [
                "curl.exe", "-sS", "--max-time", "60",
                "-X", "POST", APINEED_ENDPOINT,
                "-H", f"Authorization: Bearer {api_key}",
                "-H", "Content-Type: application/json",
                "-H", f"User-Agent: {HTTP_UA}",
                "--data-binary", f"@{tmp_path}",
            ],
            capture_output=True, text=True,
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    if proc.returncode != 0:
        raise RuntimeError(f"APINEED submit curl failed ({proc.returncode}): {proc.stderr[:500]}")
    if not proc.stdout.strip():
        raise RuntimeError("APINEED empty response (connection dropped)")
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"APINEED submit non-JSON: {proc.stdout[:400]}") from e
    if data.get("error"):
        raise RuntimeError(f"APINEED submit error: {data['error']}")
    task_id = data.get("id")
    if not task_id:
        raise RuntimeError(f"APINEED no task id in submit: {data}")

    # Poll until succeeded / failed.
    deadline = time.time() + 300
    while time.time() < deadline:
        time.sleep(5)
        poll = subprocess.run(
            [
                "curl.exe", "-sS", "--max-time", "30",
                "-X", "GET", f"{APINEED_ENDPOINT}/{task_id}",
                "-H", f"Authorization: Bearer {api_key}",
            ],
            capture_output=True, text=True,
        )
        if poll.returncode != 0 or not poll.stdout.strip():
            raise RuntimeError(f"APINEED poll failed: {poll.stderr[:400]}")
        try:
            status = json.loads(poll.stdout)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"APINEED poll non-JSON: {poll.stdout[:300]}") from e
        state = status.get("status")
        if state == "succeeded":
            outputs = status.get("outputs") or []
            if not outputs:
                raise RuntimeError(f"APINEED succeeded with no outputs: {status}")
            url = outputs[0].get("url")
            if not url:
                raise RuntimeError(f"APINEED output has no url: {outputs[0]}")
            dl = subprocess.run(
                ["curl.exe", "-sS", "--max-time", "120", "-L", "-A", HTTP_UA, url],
                capture_output=True,
            )
            if dl.returncode != 0 or not dl.stdout:
                raise RuntimeError(f"APINEED image download failed: {dl.stderr[:400]}")
            print(f"  APINEED task {task_id} succeeded")
            return dl.stdout
        if state in ("failed", "cancelled"):
            raise RuntimeError(f"APINEED task {state}: {status.get('error')}")
    raise TimeoutError(f"APINEED task {task_id} timed out")


def generate_image(provider: str, prompt: str, *, fal_key: str | None = None, apineed_key: str | None = None) -> bytes:
    if provider == "apineed":
        if not apineed_key:
            raise SystemExit("APINEED_API_KEY not found. Set env or Alignify/.secrets/apineed-key")
        return apineed_generate(prompt, apineed_key)
    if not fal_key:
        raise SystemExit("FAL_KEY not found. Set env FAL_KEY, or create Alignify/.secrets/fal-key")
    return fal_generate(prompt, fal_key)


def crop_to_og(raw: bytes) -> Image.Image:
    img = Image.open(BytesIO(raw)).convert("RGB")
    scale = max(OG_W / img.width, OG_H / img.height)
    resized = img.resize(
        (int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS
    )
    left = (resized.width - OG_W) // 2
    top = (resized.height - OG_H) // 2
    return resized.crop((left, top, left + OG_W, top + OG_H))


def load_logo(deploy_root: Path | None) -> Image.Image | None:
    candidates = [BRAND_LOGO]
    if deploy_root:
        candidates.extend(
            [
                deploy_root / "public" / "icons" / "icon-192x192.png",
                deploy_root / "public" / "apple-touch-icon.png",
            ]
        )
    for path in candidates:
        if path.exists():
            logo = Image.open(path).convert("RGBA")
            target_h = LOGO_INNER_HEIGHT
            w = int(logo.width * target_h / logo.height)
            return logo.resize((w, target_h), Image.Resampling.LANCZOS)
    return None


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in FONT_BOLD_CANDIDATES:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def overlay_author(
    img: Image.Image,
    author: str,
    accent_hex: str = "#002FA7",
    corner: str = "bottom-left",
) -> Image.Image:
    """Small byline — soft paper tint, no heavy badge."""
    if not author:
        return img
    base = img.convert("RGBA")
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    font = _load_font(AUTHOR_FONT_SIZE)
    margin = AUTHOR_MARGIN
    bbox = draw.textbbox((0, 0), author, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    pad_x, pad_y = 8, 5
    strip_w = text_w + pad_x * 2
    strip_h = text_h + pad_y * 2
    x0, y0 = corner_origin(corner, strip_w, strip_h, margin)
    draw.rounded_rectangle(
        (x0, y0, x0 + strip_w, y0 + strip_h),
        radius=3,
        fill=(244, 244, 242, 85),
    )
    tx = x0 + pad_x
    ty = y0 + pad_y - bbox[1]
    draw.text((tx + 1, ty + 1), author, fill=(0, 0, 0, 55), font=font)
    draw.text((tx, ty), author, fill=(28, 28, 28, 200), font=font)
    return Image.alpha_composite(base, layer).convert("RGB")


def overlay_wordmark(
    img: Image.Image,
    wordmark: str = DEFAULT_WORDMARK,
    corner: str = "bottom-right",
) -> Image.Image:
    """Alignify wordmark — minimal typeset, no colored badge."""
    base = img.convert("RGBA")
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    font = _load_font(WORDMARK_FONT_SIZE)
    margin = AUTHOR_MARGIN
    bbox = draw.textbbox((0, 0), wordmark, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    pad_x, pad_y = 8, 5
    strip_w = text_w + pad_x * 2
    strip_h = text_h + pad_y * 2
    x0, y0 = corner_origin(corner, strip_w, strip_h, margin)
    draw.rounded_rectangle(
        (x0, y0, x0 + strip_w, y0 + strip_h),
        radius=3,
        fill=(244, 244, 242, 75),
    )
    tx = x0 + pad_x
    ty = y0 + pad_y - bbox[1]
    draw.text((tx + 1, ty + 1), wordmark, fill=(0, 0, 0, 50), font=font)
    draw.text((tx, ty), wordmark, fill=(28, 28, 28, 185), font=font)
    return Image.alpha_composite(base, layer).convert("RGB")


def overlay_logo(
    img: Image.Image,
    logo: Image.Image | None,
    accent_hex: str = "#002FA7",
    corner: str = "bottom-right",
) -> Image.Image:
    """Logo only — no accent badge box, soft shadow blend."""
    if logo is None:
        return img
    base = img.convert("RGBA")
    margin = LOGO_MARGIN
    w, h = logo.width, logo.height
    x0, y0 = corner_origin(corner, w, h, margin)
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rectangle((0, 0, w, h), fill=(0, 0, 0, 45))
    base.paste(shadow, (x0 + 2, y0 + 2), shadow)
    base.paste(logo, (x0, y0), logo)
    return base.convert("RGB")


def apply_branding(
    img: Image.Image,
    logo: Image.Image | None,
    accent_hex: str,
    author: str,
    brand_mode: str,
    brand_corner: str,
) -> Image.Image:
    """Apply exactly ONE seamless brand mark."""
    if brand_mode == "none":
        return img
    if brand_mode == "kostja":
        return overlay_author(img, author, accent_hex, brand_corner)
    if brand_mode == "alignify":
        return overlay_wordmark(img, DEFAULT_WORDMARK, brand_corner)
    if brand_mode == "logo":
        return overlay_logo(img, logo, accent_hex, brand_corner)
    return img


def resolve_fal_key(key_file: str | None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    key = os.environ.get("FAL_KEY") or os.environ.get("FAL_API_KEY")
    if key:
        return key.strip()
    for candidate in (
        ALIGNIFY_CTX / ".secrets" / "fal-key",
        Path.home() / ".fal-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "FAL_KEY not found. Set env FAL_KEY, or create Alignify/.secrets/fal-key"
    )


def resolve_apineed_key(key_file: str | None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    key = os.environ.get("APINEED_API_KEY") or os.environ.get("API_NEED_API_KEY")
    if key:
        return key.strip()
    for candidate in (
        ALIGNIFY_CTX / ".secrets" / "apineed-key",
        Path.home() / ".apineed-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "APINEED_API_KEY not found. Set env APINEED_API_KEY, or create Alignify/.secrets/apineed-key"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Alignify OG cover via GPT Image 2")
    parser.add_argument(
        "--provider",
        choices=["fal", "apineed"],
        default="fal",
        help="Image API: fal (default) or apineed — same quality/size/format",
    )
    parser.add_argument("--section", default="tools")
    parser.add_argument("--slug", help="Page slug, e.g. image-generator")
    parser.add_argument("--locale", choices=["en", "zh"], help="Locale for text language")
    parser.add_argument("--deploy-root", help="alignify production root")
    parser.add_argument(
        "--to-staging",
        action="store_true",
        help="Preview to context assets/og/ instead of deploy public/ (default: deploy only)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print prompt only")
    parser.add_argument("--list", action="store_true", help="List registry entries")
    parser.add_argument("--fal-key-file", help="Path to file containing fal API key")
    parser.add_argument("--apineed-key-file", help="Path to file containing APINEED API key")
    parser.add_argument(
        "--brand-mode",
        choices=[*BRAND_MODES, "none"],
        help="Brand mark to overlay (default: one of kostja|alignify|logo via hash)",
    )
    parser.add_argument(
        "--brand-corner",
        choices=BRAND_CORNERS,
        help="Corner for the single brand mark",
    )
    parser.add_argument(
        "--shuffle-branding",
        action="store_true",
        help="Randomize brand mode + corner (default: stable per slug+locale hash)",
    )
    parser.add_argument("--no-branding", action="store_true", help="Skip all brand overlays")
    # Legacy flags — map to none / single mode
    parser.add_argument("--no-logo", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--no-author", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--author-corner", choices=BRAND_CORNERS, help=argparse.SUPPRESS)
    parser.add_argument("--logo-corner", choices=BRAND_CORNERS, help=argparse.SUPPRESS)
    parser.add_argument(
        "--analyze-first",
        action="store_true",
        help="Run LLM page analysis and merge registry before generating",
    )
    args = parser.parse_args()

    registry = load_registry()

    if args.list:
        for e in registry["entries"]:
            print(
                f"{e['section']}/{e['slug']} [{e['locale']}] status={e.get('status','?')} "
                f"— {e.get('headline','')}"
            )
        return

    if not args.slug or not args.locale:
        parser.error("--slug and --locale are required unless --list")

    if args.analyze_first:
        from og_brief_lib import analyze_page, merge_brief_into_registry, resolve_openai_key, save_brief

        deploy_root = resolve_deploy_root(args.deploy_root)
        print(f"Analyzing {args.section}/{args.slug} before generation...")
        brief = analyze_page(args.section, args.slug, deploy_root, resolve_openai_key())
        save_brief(args.section, args.slug, brief)
        merge_brief_into_registry(brief, status="pending")
        registry = load_registry()

    entry = find_entry(registry, args.section, args.slug, args.locale)

    if args.no_branding or (args.no_logo and args.no_author):
        brand_mode, brand_corner = "none", "bottom-right"
    else:
        forced_mode = args.brand_mode
        if args.no_logo and not forced_mode:
            forced_mode = "kostja"
        forced_corner = args.brand_corner or args.author_corner or args.logo_corner
        brand_mode, brand_corner = pick_brand_placement(
            args.section,
            args.slug,
            args.locale,
            shuffle=args.shuffle_branding,
            brand_mode=forced_mode,
            brand_corner=forced_corner,
        )

    prompt = build_prompt(
        entry,
        registry.get("defaults"),
        brand_mode,
        brand_corner,
    )
    deploy_root = resolve_deploy_root(args.deploy_root)
    out_root, mode = resolve_output_root(args.to_staging, deploy_root)
    out = output_path(out_root, mode, args.section, args.slug, args.locale)

    if args.dry_run:
        print("=== PROMPT ===")
        print(prompt)
        print(f"\nBrand mark: {brand_mode} @ {brand_corner}")
        print(f"\nWould write ({mode}): {out}")
        return

    fal_key = resolve_fal_key(args.fal_key_file) if args.provider == "fal" else None
    apineed_key = resolve_apineed_key(args.apineed_key_file) if args.provider == "apineed" else None
    out.parent.mkdir(parents=True, exist_ok=True)

    print(f"Generating {args.section}/{args.slug} {og_filename(args.slug, args.locale)} via GPT Image 2 ({args.provider})...")
    print(f"Params: quality={GEN_QUALITY} size={GEN_SIZE} format={GEN_OUTPUT_FORMAT} n={GEN_NUM_IMAGES}")
    print(f"Output ({mode}): {out}")
    print(f"Brand mark: {brand_mode} @ {brand_corner}")
    raw = generate_image(args.provider, prompt, fal_key=fal_key, apineed_key=apineed_key)
    img = crop_to_og(raw)
    accent_hex = ACCENTS.get(entry.get("accent", "klein-blue"), ACCENTS["klein-blue"])[0]
    author = entry.get("author") or registry.get("defaults", {}).get("author", DEFAULT_AUTHOR)
    logo = load_logo(deploy_root)
    if brand_mode != "none":
        img = apply_branding(img, logo, accent_hex, author, brand_mode, brand_corner)
    img.save(out, format="WEBP", quality=WEBP_QUALITY, method=6)
    print(f"Saved {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
