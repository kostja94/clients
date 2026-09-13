#!/usr/bin/env python3
"""
Unified OG cover generator for all clients (Alignify, Dubbing AI, ...) via
GPT Image 2 — providers: fal, apineed (async), gitaigc (OpenAI-compatible).

Client-specific branding, palette, sections, locales, output layout and
registry paths come from clients/<name>.json.

Providers:
  fal      queue.fal.run/openai/gpt-image-2 (submit + poll),       FAL_KEY
  apineed  apineed.com/v1/media/generations (async submit + poll), APINEED_API_KEY
  gitaigc  gitaigc.com/v1/images/generations (OpenAI-compatible),  GITAIGC_API_KEY

Usage:
  python generate-og-cover.py --client alignify --section seo --slug serp --locale en
  python generate-og-cover.py --client dubbingai --slug best-ai-voice-changer
  python generate-og-cover.py --client alignify --slug serp --locale en --provider gitaigc
  python generate-og-cover.py --client dubbingai --slug best-ai-voice-changer --dry-run
  python generate-og-cover.py --client alignify --list
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import random
import subprocess
import sys
import tempfile
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

from og_brief_lib import (  # noqa: E402
    QUALITY_DIRECTIVE,
    analyze_page,
    find_entry,
    format_brief_prompt_block,
    load_brief,
    load_registry,
    merge_brief_into_registry,
    save_brief,
)
from og_clients import CLIENTS_DIR, load_client_config, resolve_deploy_root  # noqa: E402
from og_cover_paths import OG_H, OG_W, og_filename, output_og_path  # noqa: E402

APINEED_ENDPOINT = "https://apineed.com/v1/media/generations"
FAL_ENDPOINT = "https://queue.fal.run/openai/gpt-image-2"
GITAIGC_ENDPOINT = "https://gitaigc.com/v1/images/generations"
GITAIGC_SIZE = "1536x1024"  # widest gpt-image landscape; post-cropped to 1200x630

GEN_W, GEN_H = 1216, 632
GEN_QUALITY = "high"
GEN_OUTPUT_FORMAT = "jpeg"
GEN_NUM_IMAGES = 1
WEBP_QUALITY = 92
HTTP_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

PROVIDERS = ("fal", "apineed", "gitaigc")
PROVIDER_ENV_KEYS = {
    "fal": ("FAL_KEY", "FAL_API_KEY"),
    "apineed": ("APINEED_API_KEY", "API_NEED_API_KEY"),
    "gitaigc": ("GITAIGC_API_KEY",),
}
PROVIDER_KEY_FILES = {
    "fal": ("fal-key",),
    "apineed": ("apineed-key",),
    "gitaigc": ("gitaigc-key",),
}

LOGO_INNER_HEIGHT = 44
LOGO_MARGIN = 18
AUTHOR_MARGIN = 18
AUTHOR_FONT_SIZE = 20
DEFAULT_AUTHOR = "Kostja"
FONT_BOLD_CANDIDATES = [
    Path(r"C:\Windows\Fonts\arialbd.ttf"),
    Path(r"C:\Windows\Fonts\SegoeUI-Bold.ttf"),
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]

def text_safe_zone_rules(top_inset_pct: float) -> str:
    return (
        "TEXT PLACEMENT (hard — no edge bleed):\n"
        f"- Headline block starts at least {top_inset_pct:.0f}% below the top edge and 8% inset from the left edge.\n"
        "- Every character fully inside the canvas — NEVER touch or clip top/left/right borders.\n"
        "- Headline fits within left 48% of canvas width; use 2 short lines or smaller type if needed.\n"
        "- Subtitle sits directly under headline, same left inset, also fully inside margins.\n"
    )

# NOTE (2026-09): target cover is 1200x630 (1.91:1) but each provider returns a
# different raw canvas, so the final scale-to-cover crop trims a provider-specific
# band. The prompt must tell the model exactly how much edge zone will be cut,
# otherwise headline/hero content near edges is lost (measured on real runs).

def expected_trim_pct(provider: str, model: str | None = None) -> tuple[float, float]:
    """(top_pct, bottom_pct) of raw canvas height removed by the 1200x630 crop.

    fal sends 1216x632 ≈ OG aspect → negligible trim.
    gitaigc fixes size=1536x1024 (3:2) → cover-fit to 1200x800 → 21.25% height trimmed.
    apineed is prompt-driven: gpt-image-1 renders 1536x1024 (3:2); gpt-image-2
    follows the prompt (~16:9 → ~6.7% trim; keep a defensive margin).
    """
    if provider == "fal":
        return (0.0, 0.0)
    if provider == "gitaigc":
        return (10.6, 10.6)
    if provider == "apineed":
        if model == "gpt-image-1":
            return (10.6, 10.6)
        return (4.0, 4.0)
    return (0.0, 0.0)


def crop_awareness_directive(provider: str, model: str | None, *, demand_landscape: bool) -> str:
    top, bottom = expected_trim_pct(provider, model)
    parts = []
    if demand_landscape:
        parts.append(
            "OUTPUT FRAME: wide landscape horizontal canvas. "
            "Do NOT render a portrait or square image."
        )
    if top > 0 or bottom > 0:
        inner = 100 - top - bottom
        parts.append(
            f"CROP AWARENESS (critical): the raw canvas will be trimmed ~{top:.0f}% from the top "
            f"and ~{bottom:.0f}% from the bottom to produce the final wide 1200x630 cover. "
            f"Treat the surviving middle ~{inner:.0f}% vertical band as the ENTIRE canvas — "
            "every headline, subtitle, tagline, and key subject must sit fully inside that band "
            "with its own margin. Keep the top and bottom edge zones decorative only "
            "(paper texture, background wash) — never text, faces, or hero objects."
        )
    return ("\n\n".join(parts) + "\n") if parts else ""


# ---------------------------------------------------------------- keys

def resolve_provider_key(cfg: dict, provider: str, key_file: str | None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    for env_name in PROVIDER_ENV_KEYS[provider]:
        key = os.environ.get(env_name)
        if key:
            return key.strip()
    for file_name in PROVIDER_KEY_FILES[provider]:
        # own client first, then sibling clients' .secrets (keys are shared across clients),
        # then home dotfile — mirrors the pre-consolidation resolution chains
        candidates = [Path(cfg["ctx_root"]) / ".secrets" / file_name]
        for cfg_path in sorted(CLIENTS_DIR.glob("*.json")):
            try:
                other_root = json.loads(cfg_path.read_text(encoding="utf-8")).get("ctx_root")
            except (json.JSONDecodeError, OSError):
                continue
            if other_root:
                candidates.append(Path(other_root) / ".secrets" / file_name)
        candidates.append(Path.home() / f".{file_name}")
        for candidate in candidates:
            if candidate.is_file():
                return candidate.read_text(encoding="utf-8").strip()
    env_names = " or ".join(PROVIDER_ENV_KEYS[provider])
    raise SystemExit(
        f"{env_names} not found. Set env {env_names.split(' or ')[0]}, "
        f"or create .secrets/{PROVIDER_KEY_FILES[provider][0]} in a client dir "
        f"(see README → 密钥)"
    )


# ---------------------------------------------------------------- branding

def pick_brand_placement(cfg: dict, section: str, slug: str, locale: str, *, shuffle: bool = False,
                         brand_mode: str | None = None, brand_corner: str | None = None) -> tuple[str, str]:
    brand = cfg["brand"]
    modes, corners = brand["modes"], ("bottom-left", "bottom-right", "top-right")
    if brand_mode and brand_mode not in modes and brand_mode != "none":
        raise SystemExit(f"Invalid --brand-mode: {brand_mode} (use {'|'.join(modes)}|none)")
    if brand_corner and brand_corner not in corners:
        raise SystemExit(f"Invalid --brand-corner: {brand_corner}")

    rng = random.Random()
    if shuffle:
        rng.seed()
    else:
        digest = hashlib.sha256(f"{section}/{slug}:{locale}:{brand['salt']}".encode()).hexdigest()
        rng.seed(int(digest[:8], 16))

    return brand_mode or rng.choice(modes), brand_corner or rng.choice(corners)


def corner_origin(corner: str, box_w: int, box_h: int, margin: int) -> tuple[int, int]:
    if corner == "bottom-left":
        return margin, OG_H - box_h - margin
    if corner == "bottom-right":
        return OG_W - box_w - margin, OG_H - box_h - margin
    if corner == "top-right":
        return OG_W - box_w - margin, margin
    raise ValueError(f"Unknown corner: {corner}")


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in FONT_BOLD_CANDIDATES:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def _text_strip(img: Image.Image, text: str, font_size: int, fill_alpha: int) -> Image.Image:
    base = img.convert("RGBA")
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    font = _load_font(font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pad_x, pad_y = 8, 5
    strip_w, strip_h = text_w + pad_x * 2, text_h + pad_y * 2
    x0, y0 = corner_origin(CORNER_CONTEXT, strip_w, strip_h, AUTHOR_MARGIN)
    draw.rounded_rectangle((x0, y0, x0 + strip_w, y0 + strip_h), radius=3, fill=(244, 244, 242, 75 + fill_alpha))
    tx, ty = x0 + pad_x, y0 + pad_y - bbox[1]
    draw.text((tx + 1, ty + 1), text, fill=(0, 0, 0, 50), font=font)
    draw.text((tx, ty), text, fill=(28, 28, 28, fill_alpha), font=font)
    return Image.alpha_composite(base, layer).convert("RGB")


# module-level corner used by _text_strip (set per call from apply_branding)
CORNER_CONTEXT = "bottom-right"


def overlay_author(img: Image.Image, author: str, corner: str) -> Image.Image:
    global CORNER_CONTEXT
    if not author:
        return img
    CORNER_CONTEXT = corner
    return _text_strip(img, author, AUTHOR_FONT_SIZE, 200)


def overlay_wordmark(img: Image.Image, wordmark: str, font_size: int, corner: str) -> Image.Image:
    global CORNER_CONTEXT
    CORNER_CONTEXT = corner
    return _text_strip(img, wordmark, font_size, 185)


def overlay_logo(img: Image.Image, logo: Image.Image | None, corner: str) -> Image.Image:
    if logo is None:
        return img
    base = img.convert("RGBA")
    margin = LOGO_MARGIN
    w, h = logo.width, logo.height
    x0, y0 = corner_origin(corner, w, h, margin)
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle((0, 0, w, h), fill=(0, 0, 0, 45))
    base.paste(shadow, (x0 + 2, y0 + 2), shadow)
    base.paste(logo, (x0, y0), logo)
    return base.convert("RGB")


def apply_branding(cfg: dict, img: Image.Image, logo: Image.Image | None, author: str,
                   brand_mode: str, brand_corner: str) -> Image.Image:
    brand = cfg["brand"]
    if brand_mode == "none":
        return img
    if brand_mode == "kostja":
        return overlay_author(img, author, brand_corner)
    if brand_mode == brand["wordmark_mode"]:
        return overlay_wordmark(img, brand["wordmark"], brand.get("wordmark_font_size", 20), brand_corner)
    if brand_mode == "logo":
        return overlay_logo(img, logo, brand_corner)
    return img


def load_logo(cfg: dict, deploy_root: Path | None) -> Image.Image | None:
    candidates = [Path(cfg["ctx_root"]) / cfg["brand"]["logo"]]
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
            w = int(logo.width * LOGO_INNER_HEIGHT / logo.height)
            return logo.resize((w, LOGO_INNER_HEIGHT), Image.Resampling.LANCZOS)
    return None


# ---------------------------------------------------------------- prompt


def build_prompt(cfg: dict, entry: dict, defaults: dict | None, brand_mode: str,
                 brand_corner: str, *, provider: str, apineed_quality: str, model: str | None = None) -> str:
    defaults = defaults or {}
    styles = cfg["styles"]
    style = entry.get("style", defaults.get("style", cfg.get("default_style", "editorial-collage")))
    accent_key = entry.get("accent", cfg["default_accent"])
    accent_hex, accent_name = cfg["accents"].get(accent_key, cfg["accents"][cfg["default_accent"]])
    locale = entry.get("locale", cfg.get("default_locale", "en"))
    brand = cfg["brand"]
    wordmark = brand["wordmark"]
    crop_block = crop_awareness_directive(provider, model, demand_landscape=(provider == "apineed"))

    lang_rule = (
        "All on-image text must be English only (headline + subtitle only)."
        if locale == "en"
        else "All on-image text must be Simplified Chinese only (headline + subtitle only). "
        "Do not mix English except the brand wordmark if needed."
    )

    if style == "editorial-collage":
        headline = entry["headline"]
        headline_line2 = entry.get("headline_line2", "")
        subtitle = entry.get("subtitle", "")
        tagline = entry.get("tagline", "")
        composition = entry.get("composition") or entry.get("motif", "")
        page_ref = cfg["page_ref_format"].format(section=entry.get("section", ""), slug=entry.get("slug", ""))
        brief = load_brief(cfg, entry.get("section", ""), entry.get("slug", ""))
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
        tagline_line = f"- Tagline line (medium size, below subtitle): '{tagline}'\n" if tagline else ""

        if locale == "en":
            typography_rules = (
                "Typography prominence (EN — text should feel substantial, like a PPT title slide):\n"
                "- Headline block must dominate the upper-left — bold condensed sans-serif, ~35–45% canvas width.\n"
                "- Subtitle + tagline must be clearly legible at thumbnail size (not tiny footnotes).\n"
            )
            clutter_rule = "Do NOT output a sparse poster with tiny text and oversized empty visuals.\n"
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

        text_budget = (
            "TEXT BUDGET (PPT slide — keep copy moderate):\n"
            "- ONLY render the headline and optional one-line subtitle provided below.\n"
            "- Do NOT add ranking lists, app names, arrow labels, footnotes, slogans, "
            "UI field labels, or extra captions anywhere on the image.\n"
            "- Convey details through visuals only (photos, grids, icons, mockups with blurred/illegible text).\n"
            f"- Do NOT render Kostja, {wordmark} wordmark, or logo — exactly ONE subtle brand mark added in post-production.\n"
        )
        top_trim, _ = expected_trim_pct(provider, model)
        top_inset = max(10.0, top_trim + 3.0)
        safe_zone_block = text_safe_zone_rules(top_inset) if cfg.get("text_safe_zone_rules") else ""

        return (
            f"{styles['editorial-collage']}\n"
            f"Page: {page_ref}. Accent: {accent_name} ({accent_hex}).\n\n"
            f"{QUALITY_DIRECTIVE}"
            f"{crop_block}"
            f"{brief_block}"
            f"{text_budget}\n"
            f"{safe_zone_block}"
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
            f"Leave {brand['corner_safe_zones'][brand_corner]} subtly clear for a small seamless brand mark ({brand_mode}) in post.\n"
            f"{cfg['vibe_line']}"
        )

    if style == "swiss-grid" and "swiss-grid" in styles:
        return (
            f"{styles['swiss-grid']}\n"
            f"{crop_block}"
            f"Accent: {accent_name} ({accent_hex}).\n"
            f"Visual motif: {entry.get('composition') or entry.get('motif', '')}.\n"
            f"Layout: large bold headline at upper-left reading exactly:\n"
            f"  Line 1: '{entry['headline']}'\n"
            + (f"  Line 2: '{entry.get('headline_line2', '')}'\n" if entry.get("headline_line2") else "")
            + (f"  Subtitle: '{entry.get('subtitle', '')}'\n" if entry.get("subtitle") else "")
            + f"{lang_rule}\n"
            "Spell all words correctly, no gibberish, no fake letters, no watermark.\n"
            "Leave the bottom-right corner clean for logo placement (about 180x90 px safe zone).\n"
            "High contrast, magazine editorial quality."
        )

    raise SystemExit(f"Unknown style '{style}' for client {cfg['name']}")


# ---------------------------------------------------------------- providers

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
        headers={"Authorization": f"Key {fal_key}", "Content-Type": "application/json"},
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


def _curl_json(args: list[str], timeout: str, extra: list[str], *, binary_out: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["curl.exe", "-sS", "--max-time", timeout, *extra, *args],
        capture_output=True, text=not binary_out,
    )


def apineed_generate(prompt: str, api_key: str) -> bytes:
    """APINEED async media endpoint (2026-09+): POST submit -> poll -> download.

    No size parameter — canvas follows the prompt; landscape framing appended.
    """
    quality = os.environ.get("OG_APINEED_QUALITY", GEN_QUALITY)
    model = os.environ.get("OG_APINEED_MODEL", "gpt-image-2")
    print(f"  APINEED quality={quality} model={model} (async /v1/media/generations)")

    body = {"workflow": "text_to_image", "model": model, "input": {"prompt": prompt}}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(body, tmp, ensure_ascii=False)
        tmp_path = tmp.name
    try:
        proc = _curl_json(
            ["-X", "POST", APINEED_ENDPOINT, "-H", f"Authorization: Bearer {api_key}",
             "-H", "Content-Type: application/json", "-H", f"User-Agent: {HTTP_UA}",
             "--data-binary", f"@{tmp_path}"],
            "60", [],
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

    deadline = time.time() + 300
    while time.time() < deadline:
        time.sleep(5)
        poll = _curl_json(
            ["-X", "GET", f"{APINEED_ENDPOINT}/{task_id}", "-H", f"Authorization: Bearer {api_key}"],
            "30", [],
        )
        if poll.returncode != 0 or not poll.stdout.strip():
            raise RuntimeError(f"APINEED poll failed: {poll.stderr[:400]}")
        try:
            status = json.loads(poll.stdout)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"APINEED poll non-JSON: {poll.stdout[:300]}") from e
        if status.get("status") == "succeeded":
            outputs = status.get("outputs") or []
            if not outputs:
                raise RuntimeError(f"APINEED succeeded with no outputs: {status}")
            url = outputs[0].get("url")
            if not url:
                raise RuntimeError(f"APINEED output has no url: {outputs[0]}")
            dl = _curl_json([url], "120", ["-L", "-A", HTTP_UA], binary_out=True)
            if dl.returncode != 0 or not dl.stdout:
                raise RuntimeError(f"APINEED image download failed: {dl.stderr[:400] if isinstance(dl.stderr, str) else dl.stderr}")
            print(f"  APINEED task {task_id} succeeded")
            return dl.stdout
        if status.get("status") in ("failed", "cancelled"):
            raise RuntimeError(f"APINEED task {status.get('status')}: {status.get('error')}")
    raise TimeoutError(f"APINEED task {task_id} timed out")


def gitaigc_generate(prompt: str, api_key: str) -> bytes:
    """gitaigc.com (Rainbow relay, New API) — OpenAI-compatible Images API.

    Synchronous POST /v1/images/generations; response carries data[0].b64_json
    (typical for gpt-image models) or data[0].url. Size is fixed to the widest
    landscape gpt-image supports; final crop to 1200x630 happens in post.
    """
    body = {"model": "gpt-image-2", "prompt": prompt, "size": GITAIGC_SIZE, "quality": GEN_QUALITY, "n": GEN_NUM_IMAGES}
    print(f"  gitaigc size={GITAIGC_SIZE} quality={GEN_QUALITY} (sync /v1/images/generations)")

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(body, tmp, ensure_ascii=False)
        tmp_path = tmp.name
    try:
        proc = _curl_json(
            ["-X", "POST", GITAIGC_ENDPOINT, "-H", f"Authorization: Bearer {api_key}",
             "-H", "Content-Type: application/json", "--data-binary", f"@{tmp_path}"],
            "600", [],
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    if proc.returncode != 0:
        raise RuntimeError(f"gitaigc curl failed ({proc.returncode}): {proc.stderr[:500]}")
    if not proc.stdout.strip():
        raise RuntimeError("gitaigc empty response (connection dropped)")
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"gitaigc non-JSON: {proc.stdout[:400]}") from e
    if data.get("error"):
        raise RuntimeError(f"gitaigc error: {data['error']}")
    items = data.get("data") or []
    if not items:
        raise RuntimeError(f"gitaigc no data in response: {json.dumps(data)[:400]}")
    item = items[0]
    if item.get("b64_json"):
        return base64.b64decode(item["b64_json"])
    if item.get("url"):
        dl = _curl_json([item["url"]], "120", ["-L", "-A", HTTP_UA], binary_out=True)
        if dl.returncode != 0 or not dl.stdout:
            raise RuntimeError("gitaigc image download failed")
        return dl.stdout
    raise RuntimeError(f"gitaigc output has neither b64_json nor url: {item}")


def generate_image(provider: str, prompt: str, *, keys: dict[str, str], fallback_fal: bool = False) -> tuple[bytes, str]:
    if provider == "fal":
        return fal_generate(prompt, keys["fal"]), "fal"
    try:
        if provider == "apineed":
            return apineed_generate(prompt, keys["apineed"]), "apineed"
        return gitaigc_generate(prompt, keys["gitaigc"]), "gitaigc"
    except RuntimeError as err:
        if not (fallback_fal and provider != "fal"):
            raise
        print(f"  {provider} failed ({err}); falling back to fal...")
        if not keys.get("fal"):
            raise SystemExit(f"{provider} failed and FAL_KEY not available for fallback") from err
        return fal_generate(prompt, keys["fal"]), "fal"


def crop_bias_for_provider(provider: str) -> str:
    # Prompts carry crop-awareness directives, so content stays in the middle
    # band and a symmetric center crop is correct for every provider.
    return "center"


def crop_to_og(raw: bytes, *, vertical_bias: str = "center") -> Image.Image:
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


# ---------------------------------------------------------------- output

def save_meta(cfg: dict, out: Path, entry: dict, provider: str, brand_mode: str,
              brand_corner: str, raw_size: tuple[int, int], *, quality: str, crop_bias: str,
              model: str | None = None) -> None:
    meta = {
        "client": cfg["name"],
        "slug": entry["slug"],
        "section": entry.get("section", "blog"),
        "locale": entry.get("locale", cfg.get("default_locale", "en")),
        "provider": provider,
        "model": model,
        "quality": quality,
        "crop_bias": crop_bias,
        "output_size": [OG_W, OG_H],
        "raw_size": list(raw_size),
        "brand_mode": brand_mode,
        "brand_corner": brand_corner,
        "headline": entry.get("headline", ""),
    }
    out.with_suffix(".meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------- main

def main() -> None:
    parser = argparse.ArgumentParser(description="Unified OG cover generator (fal / apineed / gitaigc)")
    parser.add_argument("--client", required=True, help="Client name (clients/<name>.json)")
    parser.add_argument("--provider", choices=PROVIDERS, help="Image API (default from client config)")
    parser.add_argument("--fallback-fal", action="store_true", help="If the chosen provider fails, retry via fal")
    parser.add_argument("--section")
    parser.add_argument("--slug", help="Page slug, e.g. image-generator")
    parser.add_argument("--locale")
    parser.add_argument("--deploy-root", help="Deploy site root (overrides env / config defaults)")
    parser.add_argument("--deploy", action="store_true", help="Force deploy output")
    parser.add_argument("--staging", action="store_true", help="Force context/staging output")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt only")
    parser.add_argument("--list", action="store_true", help="List registry entries")
    parser.add_argument("--fal-key-file")
    parser.add_argument("--apineed-key-file")
    parser.add_argument("--gitaigc-key-file")
    parser.add_argument("--quality", choices=["high", "low"], default="high", help="APINEED quality")
    parser.add_argument("--crop-bias", choices=["top", "center", "bottom"],
                        help="Override vertical crop bias (default: center — prompts are crop-aware)")
    parser.add_argument("--keep-raw", action="store_true",
                        help="Save the pre-crop raw image (<out>.raw.png) for crop-loss review")
    parser.add_argument("--brand-mode", help="Brand mark to overlay (default: hash-picked from client config)")
    parser.add_argument("--brand-corner", choices=["bottom-left", "bottom-right", "top-right"])
    parser.add_argument("--shuffle-branding", action="store_true", help="Randomize brand mode + corner")
    parser.add_argument("--no-branding", action="store_true", help="Skip all brand overlays")
    parser.add_argument("--analyze-first", action="store_true", help="Run LLM page analysis and merge registry before generating")
    args = parser.parse_args()

    cfg = load_client_config(args.client)
    provider = args.provider or cfg["default_provider"]
    section = args.section or cfg["default_section"]
    locale = args.locale or cfg.get("default_locale")
    default_mode = cfg["default_output"]

    registry = load_registry(cfg)

    if args.list:
        for e in registry["entries"]:
            print(
                f"{e['section']}/{e['slug']} [{e.get('locale', cfg.get('default_locale', 'en'))}] "
                f"status={e.get('status', '?')} — {e.get('headline', '')}"
            )
        return

    if not args.slug:
        parser.error("--slug is required unless --list")

    if args.analyze_first:
        deploy_root = resolve_deploy_root(cfg, args.deploy_root)
        print(f"Analyzing {section}/{args.slug} before generation...")
        brief = analyze_page(cfg, section, args.slug, deploy_root)
        save_brief(cfg, section, args.slug, brief)
        merge_brief_into_registry(cfg, brief, status="pending")
        registry = load_registry(cfg)

    entry = find_entry(cfg, registry, section, args.slug, locale)

    if args.no_branding:
        brand_mode, brand_corner = "none", "bottom-right"
    else:
        brand_mode, brand_corner = pick_brand_placement(
            cfg, section, args.slug, locale,
            shuffle=args.shuffle_branding, brand_mode=args.brand_mode, brand_corner=args.brand_corner,
        )

    apineed_quality = args.quality or os.environ.get("OG_APINEED_QUALITY", GEN_QUALITY)
    apineed_model = os.environ.get("OG_APINEED_MODEL", "gpt-image-2")
    prompt = build_prompt(cfg, entry, registry.get("defaults"), brand_mode, brand_corner,
                          provider=provider, apineed_quality=apineed_quality,
                          model=apineed_model if provider == "apineed" else None)

    deploy_root = resolve_deploy_root(cfg, args.deploy_root)
    mode = "deploy" if (args.deploy or (default_mode == "deploy" and not args.staging)) else "context"
    out = output_og_path(cfg, section, args.slug, locale, mode=mode, deploy_root=deploy_root)
    if mode == "deploy" and deploy_root is None:
        raise SystemExit(f"Deploy root not found. Set {cfg['deploy_env']} or pass --deploy-root.")

    if args.dry_run:
        print("=== PROMPT ===")
        print(prompt)
        print(f"\nBrand mark: {brand_mode} @ {brand_corner}")
        print(f"\nWould write ({mode}): {out}")
        print(f"Output size: {OG_W}x{OG_H} WebP")
        if provider == "apineed":
            print(f"APINEED quality: {apineed_quality} | model: {apineed_model}")
        if provider == "gitaigc":
            print(f"gitaigc size: {GITAIGC_SIZE} | crop: center")
        return

    keys: dict[str, str] = {}
    key_files = {"fal": args.fal_key_file, "apineed": args.apineed_key_file, "gitaigc": args.gitaigc_key_file}
    needed = {provider} | ({"fal"} if args.fallback_fal and provider != "fal" else set())
    for p in needed:
        keys[p] = resolve_provider_key(cfg, p, key_files[p])

    out.parent.mkdir(parents=True, exist_ok=True)
    crop_bias = args.crop_bias or crop_bias_for_provider(provider)
    print(f"Generating {cfg['name']} {section}/{args.slug} {og_filename(args.slug, locale)} via GPT Image 2 ({provider})...")
    print(f"Params: quality={GEN_QUALITY} format={GEN_OUTPUT_FORMAT} n={GEN_NUM_IMAGES} → crop {OG_W}x{OG_H} ({crop_bias}-bias)")
    print(f"Output ({mode}): {out}")
    print(f"Brand mark: {brand_mode} @ {brand_corner}")

    raw, used_provider = generate_image(provider, prompt, keys=keys, fallback_fal=args.fallback_fal)
    print(f"  Provider used: {used_provider}")
    raw_img = Image.open(BytesIO(raw))
    raw_size = raw_img.size
    if args.keep_raw:
        raw_path = out.with_suffix(".raw.png")
        raw_img.save(raw_path, format="PNG")
        print(f"  Raw pre-crop image kept: {raw_path}")

    img = crop_to_og(raw, vertical_bias=crop_bias)
    assert img.size == (OG_W, OG_H), f"Expected {OG_W}x{OG_H}, got {img.size}"

    author = entry.get("author") or registry.get("defaults", {}).get("author", DEFAULT_AUTHOR)
    logo = load_logo(cfg, deploy_root if mode == "deploy" else None)
    if brand_mode != "none":
        img = apply_branding(cfg, img, logo, author, brand_mode, brand_corner)

    img.save(out, format="WEBP", quality=WEBP_QUALITY, method=6)
    if img.size != (OG_W, OG_H):
        raise RuntimeError(f"Final image size {img.size} != ({OG_W}, {OG_H})")

    save_meta(cfg, out, entry, used_provider, brand_mode, brand_corner, raw_size,
              quality=apineed_quality if provider == "apineed" else GEN_QUALITY,
              crop_bias=crop_bias,
              model=apineed_model if used_provider == "apineed" else ("gpt-image-2" if used_provider == "gitaigc" else None))
    print(f"Saved {out} ({out.stat().st_size // 1024} KB) — verified {OG_W}x{OG_H}")


if __name__ == "__main__":
    main()
