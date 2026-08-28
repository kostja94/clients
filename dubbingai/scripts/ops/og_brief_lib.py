"""Shared OG page analysis + prompt assembly (Dubbing AI context repo)."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DUBBINGAI_CTX = Path(__file__).resolve().parents[2]
BRIEFS_ROOT = DUBBINGAI_CTX / "data" / "og-briefs"
REGISTRY_PATH = DUBBINGAI_CTX / "data" / "og-prompt-registry.json"
SECTION_SIG_PATH = DUBBINGAI_CTX / "data" / "og-section-signatures.json"
BLOG_ROOT = DUBBINGAI_CTX / "blog"

DEFAULT_DEPLOY_ROOTS: list[Path] = []

OPENAI_MODEL = os.environ.get("OG_ANALYZE_MODEL", "gpt-4o")
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

ANALYZE_SYSTEM = """You are an art director for Dubbing AI (dubbingai.io/blog) OG social cards (1200x630 editorial collage).

Your job: read blog source content and produce a JSON brief so image generation is unmistakably about THIS article — not a generic voice-tech stock visual.

Critical distinctions:
- Real-time mic voice changer (gaming/Discord/streaming) ≠ Google Assistant TTS settings ≠ file-based voice cloning.
- Soundboard / meme article = playful collage with sound-wave tiles, game/anime cues — NOT corporate SaaS hero.
- Voice actor profile = character portrait mood + mic/stream context — NOT product comparison grid.
- Alternative/comparison = fair side-by-side workflow visuals — NO readable competitor logos (Voicemod, Discord, etc.).

Brand accent: cyan (#22D3EE) to indigo (#6366F1) gradient feel — gaming/streaming energy, young audience.

Output ONLY valid JSON matching the schema. composition fields must be English (image model follows English better).
Do NOT include real trademark logos (Discord, Voicemod, Fortnite, etc.) — describe UI archetypes only.
"""

ANALYZE_SCHEMA = {
    "page_topic_one_liner": "string",
    "differentiator_vs_generic": "string — why this is NOT a generic stock visual",
    "visual_anchors": ["2-4 must-have visual elements, ordered by prominence"],
    "anti_patterns": ["explicit bans — what would make viewers think wrong topic"],
    "accent_suggestion": "dubbing-cyan | dubbing-indigo | dubbing-gradient",
    "locales": {
        "en": {
            "headline": "string",
            "headline_line2": "optional e.g. (2026)",
            "subtitle": "one line",
            "tagline": "optional second line",
            "composition": "detailed English visual brief for image model, HERO element first",
        }
    },
}


def resolve_deploy_root(explicit: str | None = None) -> Path | None:
    if explicit:
        return Path(explicit)
    env = os.environ.get("DUBBINGAI_DEPLOY_ROOT")
    if env:
        return Path(env)
    for p in DEFAULT_DEPLOY_ROOTS:
        if p.is_dir():
            return p
    return None


def find_blog_md(slug: str) -> Path | None:
    for p in sorted(BLOG_ROOT.glob(f"*-{slug}-*.md")):
        return p
    for candidate in (
        BLOG_ROOT / f"{slug}.md",
        BLOG_ROOT / "cms-export" / f"{slug}.md",
    ):
        if candidate.is_file():
            return candidate
    return None


def read_page_md(path: Path, max_chars: int = 12000) -> str:
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text[:max_chars]


def load_section_signatures() -> dict:
    if SECTION_SIG_PATH.is_file():
        return json.loads(SECTION_SIG_PATH.read_text(encoding="utf-8"))
    return {}


def signatures_for_page(section: str, slug: str) -> dict[str, Any]:
    sigs = load_section_signatures()
    out: dict[str, Any] = {"section": section, "slug": slug, "rules": []}
    for key, rule in sigs.items():
        if slug in rule.get("slugs", []):
            out["rules"].append({"id": key, **rule})
        elif section in rule.get("sections", []):
            out["rules"].append({"id": key, **rule})
    return out


def brief_path(section: str, slug: str) -> Path:
    return BRIEFS_ROOT / section / slug / "brief.json"


def load_brief(section: str, slug: str) -> dict | None:
    p = brief_path(section, slug)
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def save_brief(section: str, slug: str, brief: dict) -> Path:
    p = brief_path(section, slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    return p


def resolve_openai_key(key_file: str | None = None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key.strip()
    for candidate in (
        DUBBINGAI_CTX / ".secrets" / "openai-key",
        DUBBINGAI_CTX.parent / "Alignify" / ".secrets" / "openai-key",
        Path.home() / ".openai-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "OPENAI_API_KEY not found. Set env OPENAI_API_KEY or dubbingai/.secrets/openai-key"
    )


def call_openai_json(system: str, user: str, api_key: str) -> dict:
    payload = {
        "model": OPENAI_MODEL,
        "temperature": 0.4,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    req = urllib.request.Request(
        OPENAI_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else str(e)
        raise SystemExit(f"OpenAI API error: {err}") from e

    content = body["choices"][0]["message"]["content"]
    return json.loads(content)


def build_analyze_user_prompt(
    section: str,
    slug: str,
    md: str,
    signatures: dict,
) -> str:
    return f"""Analyze this Dubbing AI blog article for OG cover generation.

Section: {section}
Slug: {slug}
URL: https://dubbingai.io/blog/{slug}/

Section signature rules (apply all matching):
{json.dumps(signatures, ensure_ascii=False, indent=2)}

JSON schema to output:
{json.dumps(ANALYZE_SCHEMA, ensure_ascii=False, indent=2)}

--- EN article content ---
{md or "(missing)"}

Requirements:
1. visual_anchors[0] must be the HERO element (largest, most recognizable).
2. anti_patterns must explicitly ban wrong-category clichés (e.g. for Google Assistant article: ban gaming headset hero; for voice changer hub: ban phone assistant settings UI).
3. Headlines must match article title intent, PPT-level brevity, gaming/streaming tone where appropriate.
4. Blog is English-only — only populate locales.en.
"""


def analyze_page(
    section: str,
    slug: str,
    api_key: str | None = None,
) -> dict:
    md_path = find_blog_md(slug)
    if md_path is None:
        raise SystemExit(f"No blog markdown found for slug={slug}")
    md = read_page_md(md_path)

    signatures = signatures_for_page(section, slug)
    user_prompt = build_analyze_user_prompt(section, slug, md, signatures)

    key = api_key or resolve_openai_key()
    result = call_openai_json(ANALYZE_SYSTEM, user_prompt, key)

    brief = {
        "section": section,
        "slug": slug,
        "source_md": str(md_path.relative_to(DUBBINGAI_CTX)).replace("\\", "/"),
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "model": OPENAI_MODEL,
        **result,
    }
    return brief


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def save_registry(registry: dict) -> None:
    REGISTRY_PATH.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def merge_brief_into_registry(brief: dict, status: str = "pending") -> int:
    registry = load_registry()
    section = brief["section"]
    slug = brief["slug"]
    updated = 0
    entries = registry.setdefault("entries", [])

    loc = brief.get("locales", {}).get("en")
    if not loc:
        return 0

    entry = None
    for e in entries:
        if e.get("section") == section and e.get("slug") == slug and e.get("locale") == "en":
            entry = e
            break
    if entry is None:
        entry = {
            "section": section,
            "slug": slug,
            "locale": "en",
            "style": "editorial-collage",
            "author": "Kostja",
        }
        entries.append(entry)

    entry["headline"] = loc.get("headline", entry.get("headline", ""))
    if loc.get("headline_line2"):
        entry["headline_line2"] = loc["headline_line2"]
    if loc.get("subtitle"):
        entry["subtitle"] = loc["subtitle"]
    if loc.get("tagline"):
        entry["tagline"] = loc["tagline"]
    entry["composition"] = loc.get("composition", entry.get("composition", ""))
    if brief.get("accent_suggestion"):
        entry["accent"] = brief["accent_suggestion"]
    entry["visual_anchors"] = brief.get("visual_anchors", [])
    entry["anti_patterns"] = brief.get("anti_patterns", [])
    entry["status"] = status
    entry["notes"] = f"LLM brief {brief.get('analyzed_at', '')[:10]}"
    updated += 1

    save_registry(registry)
    return updated


def format_brief_prompt_block(brief: dict | None, entry: dict) -> str:
    anchors = entry.get("visual_anchors") or (brief or {}).get("visual_anchors") or []
    anti = entry.get("anti_patterns") or (brief or {}).get("anti_patterns") or []
    diff = (brief or {}).get("differentiator_vs_generic", "")

    lines = []
    if diff:
        lines.append(f"Topic differentiation: {diff}\n")
    if anchors:
        lines.append("MUST INCLUDE (ordered by prominence — #1 is HERO, largest on canvas):")
        for i, a in enumerate(anchors, 1):
            lines.append(f"  {i}. {a}")
        lines.append("")
    if anti:
        lines.append("STRICTLY FORBIDDEN (would mislead viewers about page topic):")
        for a in anti:
            lines.append(f"  - {a}")
        lines.append("")
    return "\n".join(lines)


QUALITY_DIRECTIVE = (
    "QUALITY: Museum-grade editorial collage — sharp focal details, cohesive art direction, "
    "professional torn-paper layering, subtle halftone grain. Thumbnail-readable at 120x63px. "
    "Final crop MUST read well at exactly 1200x630 landscape.\n"
)
