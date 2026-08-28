#!/usr/bin/env python3
"""
Generate Dubbing AI blog OG covers via GPT Image 2 (APINEED default).

APINEED params: quality=high, jpeg, 1 image, then center-crop to exactly 1200x630 WebP.

Default output: context repo blog/images/og/ (use --deploy when DUBBINGAI_DEPLOY_ROOT is set).

Usage:
  set APINEED_API_KEY=your-key
  python generate-og-cover.py --slug best-ai-voice-changer
  python generate-og-cover.py --slug best-ai-voice-changer --dry-run
  python generate-og-cover.py --slug best-ai-voice-changer --deploy
  python generate-og-cover.py --list
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import random
import sys
import time
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

from generate_og_cover_paths import (  # noqa: E402
    OG_H,
    OG_W,
    context_og_path,
    deploy_og_path,
    og_filename,
)
from og_brief_lib import (  # noqa: E402
    QUALITY_DIRECTIVE,
    DUBBINGAI_CTX,
    REGISTRY_PATH,
    format_brief_prompt_block,
    load_brief,
)

BRAND_LOGO = DUBBINGAI_CTX / "assets" / "brand" / "icon-192x192.png"

APINEED_ENDPOINT = "https://apineed.com/v1/images/generations"
FAL_ENDPOINT = "https://queue.fal.run/openai/gpt-image-2"
GEN_W, GEN_H = 1216, 632
GEN_QUALITY = "high"
GEN_OUTPUT_FORMAT = "jpeg"
GEN_NUM_IMAGES = 1
OG_EXT = "webp"
WEBP_QUALITY = 92
HTTP_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

ACCENTS = {
    "dubbing-cyan": ("#22D3EE", "Dubbing cyan"),
    "dubbing-indigo": ("#6366F1", "Dubbing indigo"),
    "dubbing-gradient": ("#22D3EE", "cyan-to-indigo gradient"),
}

EDITORIAL_COLLAGE_STYLE = (
    "High-end editorial paper collage social share card, exactly 1200x630 landscape, "
    "like a zine cover for a gaming/streaming voice-tech blog. "
    "Off-white textured paper (#F4F4F2) with torn-paper layers and halftone grain. "
    "Accent energy: cyan (#22D3EE) to indigo (#6366F1) gradient hints — playful, not corporate SaaS. "
    "Every visual must illustrate THIS article's topic — not generic abstract decoration."
)

TEXT_BUDGET_RULES = (
    "TEXT BUDGET (PPT slide — keep copy moderate):\n"
    "- ONLY render the headline and optional one-line subtitle provided below.\n"
    "- Do NOT add ranking lists, app names, arrow labels, footnotes, slogans, "
    "UI field labels, or extra captions anywhere on the image.\n"
    "- Convey details through visuals only (photos, grids, icons, mockups with blurred/illegible text).\n"
    "- Do NOT render Kostja, Dubbing AI wordmark, or logo — exactly ONE subtle brand mark added in post-production.\n"
)

TEXT_SAFE_ZONE_RULES = (
    "TEXT PLACEMENT (hard — no edge bleed):\n"
    "- Headline block starts at least 10% below the top edge and 8% inset from the left edge.\n"
    "- Every character fully inside the canvas — NEVER touch or clip top/left/right borders.\n"
    "- Headline fits within left 48% of canvas width; use 2 short lines or smaller type if needed.\n"
    "- Subtitle sits directly under headline, same left inset, also fully inside margins.\n"
)

# APINEED returns taller canvases than 1200x630; post-process top-trims to OG size.
APINEED_API_SIZES = {"high": (1536, 1024), "low": (1024, 1024)}


def resolve_apineed_quality(cli_quality: str | None = None) -> str:
    if cli_quality:
        return cli_quality
    return os.environ.get("OG_APINEED_QUALITY", GEN_QUALITY)


def apineed_crop_directive(quality: str = "high") -> str:
    """Prompt block: compose for APINEED raw size → 1200x630 top-aligned crop."""
    w, h = APINEED_API_SIZES.get(quality, APINEED_API_SIZES["high"])
    scale = max(OG_W / w, OG_H / h)
    scaled_h = int(h * scale)
    trim_bottom = max(0, scaled_h - OG_H)
    trim_pct = round(100 * trim_bottom / scaled_h) if scaled_h else 0

    return (
        f"APINEED CROP SAFE ZONE (critical — API raw {w}x{h} → trimmed to exactly 1200x630):\n"
        f"- Raw canvas is taller than final OG (~{trim_pct}% of bottom band may be trimmed; top edge preserved).\n"
        f"- Compose for the final 1200x630 wide frame (1.91:1) — do NOT place important content in the bottom {trim_pct}%.\n"
        "- Headline + subtitle: upper-left safe inset (10% top, 8% left) — fully visible, no border bleed.\n"
        "- Hero visuals (phone, flow diagram): center-right and middle vertical band — not flush to bottom edge.\n"
        "- Decorative waveforms/stopwatch: may sit lower but keep key labels inside the middle 85% height.\n"
        "- Think 'title slide safe area': all readable text well inside margins before any crop happens.\n"
    )

LOGO_INNER_HEIGHT = 44
LOGO_MARGIN = 18
AUTHOR_MARGIN = 18
AUTHOR_FONT_SIZE = 20
WORDMARK_FONT_SIZE = 20
DEFAULT_AUTHOR = "Kostja"
DEFAULT_WORDMARK = "Dubbing AI"
BRAND_MODES = ("kostja", "dubbingai", "logo")
BRAND_CORNERS = ("bottom-left", "bottom-right", "top-right")
CORNER_SAFE_ZONES = {
    "bottom-left": "bottom-left 140x48px",
    "bottom-right": "bottom-right 120x100px",
    "top-right": "top-right 120x100px",
}
FONT_BOLD_CANDIDATES = [
    Path(r"C:\Windows\Fonts\arialbd.ttf"),
    Path(r"C:\Windows\Fonts\SegoeUI-Bold.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]


def load_registry() -> dict:
    with REGISTRY_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def find_entry(registry: dict, section: str, slug: str, locale: str) -> dict:
    for entry in registry["entries"]:
        if (
            entry["section"] == section
            and entry["slug"] == slug
            and entry.get("locale", "en") == locale
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
    valid_corners = set(BRAND_CORNERS)
    if brand_mode and brand_mode not in BRAND_MODES and brand_mode != "none":
        raise SystemExit(f"Invalid --brand-mode: {brand_mode} (use kostja|dubbingai|logo|none)")
    if brand_corner and brand_corner not in valid_corners:
        raise SystemExit(f"Invalid --brand-corner: {brand_corner}")

    rng = random.Random()
    if shuffle:
        rng.seed()
    else:
        digest = hashlib.sha256(f"{section}/{slug}:{locale}:dubbing-brand-v1".encode()).hexdigest()
        rng.seed(int(digest[:8], 16))

    mode = brand_mode or rng.choice(BRAND_MODES)
    corner = brand_corner or rng.choice(BRAND_CORNERS)
    return mode, corner


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
    *,
    provider: str = "apineed",
    apineed_quality: str = "high",
) -> str:
    defaults = defaults or {}
    accent_key = entry.get("accent", "dubbing-gradient")
    accent_hex, accent_name = ACCENTS.get(accent_key, ACCENTS["dubbing-gradient"])
    headline = entry["headline"]
    headline_line2 = entry.get("headline_line2", "")
    subtitle = entry.get("subtitle", "")
    tagline = entry.get("tagline", "")
    composition = entry.get("composition") or entry.get("motif", "")
    page_ref = f"blog/{entry.get('slug', '')}"
    section = entry.get("section", "blog")
    slug = entry.get("slug", "")
    brief = load_brief(section, slug)
    brief_block = format_brief_prompt_block(brief, entry)

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
    typography_rules = (
        "Typography prominence (EN — text should feel substantial, like a PPT title slide):\n"
        "- Headline block upper-left inside safe inset — bold condensed sans-serif, max ~45% canvas width.\n"
        "- Subtitle + tagline clearly legible at thumbnail size (not tiny footnotes).\n"
    )
    clutter_rule = (
        "Do NOT output a sparse poster with tiny text and oversized empty visuals.\n"
    )
    apineed_block = apineed_crop_directive(apineed_quality) if provider == "apineed" else ""

    return (
        f"{EDITORIAL_COLLAGE_STYLE}\n"
        f"Page: {page_ref}. Accent: {accent_name} ({accent_hex}).\n\n"
        f"{QUALITY_DIRECTIVE}"
        f"{apineed_block}"
        f"{brief_block}"
        f"{TEXT_BUDGET_RULES}\n"
        f"{TEXT_SAFE_ZONE_RULES}\n"
        f"{typography_rules}"
        f"{headline_block}\n"
        f"{subtitle_line}"
        f"{tagline_line}\n"
        f"Page-relevant visuals (composition detail):\n"
        f"{composition}\n\n"
        "All on-image text must be English only (headline + subtitle only).\n"
        f"{clutter_rule}"
        "Do NOT clutter with paragraphs or multiple text cards.\n"
        "Spell headline/subtitle/tagline correctly. No watermark.\n"
        f"Leave {CORNER_SAFE_ZONES[brand_corner]} subtly clear for a small seamless brand mark ({brand_mode}) in post.\n"
        "Editorial collage quality — visual storytelling, PPT-level copy, gaming/streaming vibe."
    )


def apineed_generate(prompt: str, api_key: str, quality: str | None = None) -> bytes:
    import subprocess
    import tempfile

    quality = quality or resolve_apineed_quality(None)
    print(f"  APINEED quality={quality} size={'1536x1024' if quality != 'low' else '1024x1024'}")

    def _request(size: str) -> dict:
        q = quality or resolve_apineed_quality(None)
        body = {
            "model": "gpt-image-2",
            "prompt": prompt,
            "n": GEN_NUM_IMAGES,
            "size": size,
            "quality": q,
            "output_format": GEN_OUTPUT_FORMAT,
        }
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
            json.dump(body, tmp, ensure_ascii=False)
            tmp_path = tmp.name
        try:
            cmd = [
                "curl.exe",
                "-sS",
                "--max-time",
                "300",
                "-X",
                "POST",
                APINEED_ENDPOINT,
                "-H",
                f"Authorization: Bearer {api_key}",
                "-H",
                "Content-Type: application/json",
                "-H",
                f"User-Agent: {HTTP_UA}",
                "--data-binary",
                f"@{tmp_path}",
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True)
        finally:
            Path(tmp_path).unlink(missing_ok=True)
        if proc.returncode != 0:
            raise RuntimeError(f"APINEED curl failed ({proc.returncode}): {proc.stderr[:500]}")
        if not proc.stdout.strip():
            raise RuntimeError("APINEED empty response (connection dropped)")
        try:
            data = json.loads(proc.stdout)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"APINEED non-JSON: {proc.stdout[:400]}") from e
        if data.get("error"):
            raise RuntimeError(f"APINEED error: {data['error']}")
        return data

    first_size = "1024x1024" if quality == "low" else "1536x1024"
    try:
        result = _request(first_size)
    except RuntimeError as err:
        msg = str(err).lower()
        if first_size != "1024x1024" and ("524" in msg or "timeout" in msg or "size" in msg or "invalid" in msg):
            print(f"  APINEED {first_size} failed, retrying 1024x1024...")
            result = _request("1024x1024")
        else:
            raise

    items = result.get("data") or []
    if not items:
        raise RuntimeError(f"No images in APINEED result: {result}")
    item = items[0]
    if item.get("b64_json"):
        return base64.b64decode(item["b64_json"])
    url = item.get("url")
    if not url:
        raise RuntimeError(f"APINEED item has neither url nor b64_json: {item}")
    dl = subprocess.run(
        ["curl.exe", "-sS", "--max-time", "120", "-L", "-A", HTTP_UA, url],
        capture_output=True,
    )
    if dl.returncode != 0 or not dl.stdout:
        raise RuntimeError(f"APINEED image download failed: {dl.stderr[:400]}")
    return dl.stdout


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
            urllib.request.Request(status_url, headers={"Authorization": f"Key {fal_key}"}),
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
        urllib.request.Request(response_url, headers={"Authorization": f"Key {fal_key}"}),
        timeout=60,
    ) as resp:
        result = json.loads(resp.read())

    images = result.get("images") or []
    if not images:
        raise RuntimeError(f"No images in fal result: {result}")

    image_url = images[0]["url"]
    with urllib.request.urlopen(image_url, timeout=120) as resp:
        return resp.read()


def generate_image(
    provider: str,
    prompt: str,
    *,
    apineed_key: str | None = None,
    fal_key: str | None = None,
    fallback_fal: bool = False,
    apineed_quality: str | None = None,
) -> tuple[bytes, str]:
    if provider == "fal":
        if not fal_key:
            raise SystemExit("FAL_KEY not found. Set env or Alignify/.secrets/fal-key")
        return fal_generate(prompt, fal_key), "fal"
    if not apineed_key:
        raise SystemExit("APINEED_API_KEY not found. Set env or dubbingai/.secrets/apineed-key")
    q = resolve_apineed_quality(apineed_quality)
    try:
        return apineed_generate(prompt, apineed_key, q), "apineed"
    except RuntimeError as err:
        if not fallback_fal:
            raise
        print(f"  APINEED failed ({err}); falling back to fal...")
        if not fal_key:
            raise SystemExit("APINEED failed and FAL_KEY not available for fallback") from err
        return fal_generate(prompt, fal_key), "fal"


def crop_bias_for_provider(provider: str) -> str:
    # APINEED: taller raw canvas → preserve top (headline zone)
    # fal: ~1216x632 ≈ OG aspect → center crop is fine
    return "top" if provider == "apineed" else "center"


def crop_to_og(raw: bytes, *, vertical_bias: str = "center") -> Image.Image:
    """Scale-to-cover then crop to 1200x630.

    APINEED raw frames are taller than OG — use vertical_bias='top' to keep headline
    and trim excess from the bottom instead of center-slice.
    """
    img = Image.open(BytesIO(raw)).convert("RGB")
    scale = max(OG_W / img.width, OG_H / img.height)
    resized = img.resize(
        (int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS
    )
    left = max(0, (resized.width - OG_W) // 2)
    if resized.height <= OG_H:
        top = 0
    elif vertical_bias == "top":
        top = 0
    else:
        top = (resized.height - OG_H) // 2
    cropped = resized.crop((left, top, left + OG_W, top + OG_H))
    if cropped.size != (OG_W, OG_H):
        raise RuntimeError(f"Crop size mismatch: {cropped.size}, expected ({OG_W}, {OG_H})")
    return cropped


def load_logo(deploy_root: Path | None) -> Image.Image | None:
    candidates = [BRAND_LOGO]
    if deploy_root:
        candidates.extend(
            [
                deploy_root / "public" / "icons" / "icon-192x192.png",
                deploy_root / "public" / "apple-touch-icon.png",
                deploy_root / "public" / "favicon.png",
            ]
        )
    for path in candidates:
        if path.exists():
            logo = Image.open(path).convert("RGBA")
            target_h = LOGO_INNER_HEIGHT
            w = int(logo.width * target_h / logo.height)
            return logo.resize((w, target_h), Image.Resampling.LANCZOS)
    return None


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in FONT_BOLD_CANDIDATES:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def overlay_author(
    img: Image.Image,
    author: str,
    corner: str = "bottom-left",
) -> Image.Image:
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
    corner: str = "bottom-right",
) -> Image.Image:
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
    author: str,
    brand_mode: str,
    brand_corner: str,
) -> Image.Image:
    if brand_mode == "none":
        return img
    if brand_mode == "kostja":
        return overlay_author(img, author, brand_corner)
    if brand_mode == "dubbingai":
        return overlay_wordmark(img, DEFAULT_WORDMARK, brand_corner)
    if brand_mode == "logo":
        return overlay_logo(img, logo, brand_corner)
    return img


def resolve_fal_key(key_file: str | None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    key = os.environ.get("FAL_KEY") or os.environ.get("FAL_API_KEY")
    if key:
        return key.strip()
    for candidate in (
        DUBBINGAI_CTX / ".secrets" / "fal-key",
        DUBBINGAI_CTX.parent / "Alignify" / ".secrets" / "fal-key",
        Path.home() / ".fal-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit("FAL_KEY not found. Set env FAL_KEY or Alignify/.secrets/fal-key")


def resolve_apineed_key(key_file: str | None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    key = os.environ.get("APINEED_API_KEY") or os.environ.get("API_NEED_API_KEY")
    if key:
        return key.strip()
    for candidate in (
        DUBBINGAI_CTX / ".secrets" / "apineed-key",
        DUBBINGAI_CTX.parent / "Alignify" / ".secrets" / "apineed-key",
        Path.home() / ".apineed-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "APINEED_API_KEY not found. Set env APINEED_API_KEY or dubbingai/.secrets/apineed-key"
    )


def resolve_output_path(
    slug: str,
    locale: str,
    *,
    deploy: bool,
    deploy_root: Path | None,
) -> tuple[Path, str]:
    if deploy:
        if deploy_root is None:
            from og_brief_lib import resolve_deploy_root

            deploy_root = resolve_deploy_root(None)
        if deploy_root is None:
            raise SystemExit("Deploy root not found. Set DUBBINGAI_DEPLOY_ROOT or pass --deploy-root.")
        return deploy_og_path(deploy_root, slug, locale), "deploy"
    return context_og_path(DUBBINGAI_CTX, slug, locale), "context"


def save_meta(
    out: Path,
    entry: dict,
    provider: str,
    brand_mode: str,
    brand_corner: str,
    raw_size: tuple[int, int],
    *,
    quality: str = "high",
    crop_bias: str = "center",
) -> None:
    meta = {
        "slug": entry["slug"],
        "section": entry.get("section", "blog"),
        "locale": entry.get("locale", "en"),
        "provider": provider,
        "quality": quality,
        "crop_bias": crop_bias,
        "output_size": [OG_W, OG_H],
        "raw_size": list(raw_size),
        "brand_mode": brand_mode,
        "brand_corner": brand_corner,
        "headline": entry.get("headline", ""),
    }
    meta_path = out.with_suffix(".meta.json")
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Dubbing AI blog OG cover via APINEED GPT Image 2")
    parser.add_argument(
        "--provider",
        choices=["apineed", "fal"],
        default="apineed",
        help="Image API (default: apineed)",
    )
    parser.add_argument(
        "--fallback-fal",
        action="store_true",
        help="If APINEED fails, retry via fal GPT Image 2",
    )
    parser.add_argument("--fal-key-file", help="Path to file containing fal API key")
    parser.add_argument("--section", default="blog")
    parser.add_argument("--slug", help="Blog slug, e.g. best-ai-voice-changer")
    parser.add_argument("--locale", default="en", choices=["en"], help="Locale (EN only)")
    parser.add_argument("--deploy-root", help="Dubbing AI deploy site root")
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="Write to deploy public/blog/images/og/ (default: context repo blog/images/og/)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print prompt only")
    parser.add_argument("--list", action="store_true", help="List registry entries")
    parser.add_argument("--apineed-key-file", help="Path to file containing APINEED API key")
    parser.add_argument(
        "--quality",
        choices=["high", "low"],
        default="high",
        help="APINEED quality (default: high — always use high unless debugging)",
    )
    parser.add_argument(
        "--brand-mode",
        choices=[*BRAND_MODES, "none"],
        help="Brand mark to overlay (default: one of kostja|dubbingai|logo via hash)",
    )
    parser.add_argument("--brand-corner", choices=BRAND_CORNERS, help="Corner for the single brand mark")
    parser.add_argument("--shuffle-branding", action="store_true", help="Randomize brand mode + corner")
    parser.add_argument("--no-branding", action="store_true", help="Skip all brand overlays")
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
                f"{e['section']}/{e['slug']} [{e.get('locale', 'en')}] "
                f"status={e.get('status', '?')} — {e.get('headline', '')}"
            )
        return

    if not args.slug:
        parser.error("--slug is required unless --list")

    if args.analyze_first:
        from og_brief_lib import analyze_page, merge_brief_into_registry, resolve_openai_key, save_brief

        print(f"Analyzing blog/{args.slug} before generation...")
        brief = analyze_page(args.section, args.slug, resolve_openai_key())
        save_brief(args.section, args.slug, brief)
        merge_brief_into_registry(brief, status="pending")
        registry = load_registry()

    entry = find_entry(registry, args.section, args.slug, args.locale)

    if args.no_branding:
        brand_mode, brand_corner = "none", "bottom-right"
    else:
        brand_mode, brand_corner = pick_brand_placement(
            args.section,
            args.slug,
            args.locale,
            shuffle=args.shuffle_branding,
            brand_mode=args.brand_mode,
            brand_corner=args.brand_corner,
        )

    apineed_quality = resolve_apineed_quality(args.quality)
    prompt = build_prompt(
        entry,
        registry.get("defaults"),
        brand_mode,
        brand_corner,
        provider=args.provider,
        apineed_quality=apineed_quality,
    )

    deploy_root = Path(args.deploy_root) if args.deploy_root else None
    out, mode = resolve_output_path(
        args.slug,
        args.locale,
        deploy=args.deploy,
        deploy_root=deploy_root,
    )

    if args.dry_run:
        print("=== PROMPT ===")
        print(prompt)
        print(f"\nBrand mark: {brand_mode} @ {brand_corner}")
        print(f"\nWould write ({mode}): {out}")
        print(f"Output size: {OG_W}x{OG_H} WebP")
        if args.provider == "apineed":
            print(f"APINEED quality: {apineed_quality} | crop: top-aligned trim")
        return

    apineed_key = resolve_apineed_key(args.apineed_key_file) if args.provider == "apineed" else None
    fal_key = None
    if args.provider == "fal" or args.fallback_fal:
        try:
            fal_key = resolve_fal_key(args.fal_key_file)
        except SystemExit:
            if args.provider == "fal":
                raise
    out.parent.mkdir(parents=True, exist_ok=True)

    quality_label = apineed_quality if args.provider == "apineed" else GEN_QUALITY
    crop_bias = crop_bias_for_provider(args.provider)
    print(f"Generating blog/{args.slug} {og_filename(args.slug, args.locale)} via GPT Image 2 ({args.provider})...")
    print(
        f"Params: quality={quality_label} format={GEN_OUTPUT_FORMAT} n={GEN_NUM_IMAGES} "
        f"→ crop {OG_W}x{OG_H} ({crop_bias}-bias)"
    )
    print(f"Output ({mode}): {out}")
    print(f"Brand mark: {brand_mode} @ {brand_corner}")

    raw, used_provider = generate_image(
        args.provider,
        prompt,
        apineed_key=apineed_key,
        fal_key=fal_key,
        fallback_fal=args.fallback_fal,
        apineed_quality=apineed_quality,
    )
    print(f"  Provider used: {used_provider}")
    raw_img = Image.open(BytesIO(raw))
    raw_size = raw_img.size

    img = crop_to_og(raw, vertical_bias=crop_bias_for_provider(used_provider))
    assert img.size == (OG_W, OG_H), f"Expected {OG_W}x{OG_H}, got {img.size}"

    author = entry.get("author") or registry.get("defaults", {}).get("author", DEFAULT_AUTHOR)
    logo = load_logo(deploy_root if args.deploy else None)
    if brand_mode != "none":
        img = apply_branding(img, logo, author, brand_mode, brand_corner)

    img.save(out, format="WEBP", quality=WEBP_QUALITY, method=6)
    if img.size != (OG_W, OG_H):
        raise RuntimeError(f"Final image size {img.size} != ({OG_W}, {OG_H})")

    save_meta(
        out,
        entry,
        used_provider,
        brand_mode,
        brand_corner,
        raw_size,
        quality=quality_label,
        crop_bias=crop_bias_for_provider(used_provider),
    )
    print(f"Saved {out} ({out.stat().st_size // 1024} KB) — verified {OG_W}x{OG_H}")


if __name__ == "__main__":
    main()
