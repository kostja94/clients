"""Unified OG page analysis + prompt assembly (Alignify & Dubbing AI).

All client-specific paths come from clients/<name>.json (loaded by the
caller and passed in as `cfg`), except the per-client LLM art-direction
prompts which live in ANALYZE_PROFILES below.
"""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPENAI_MODEL = os.environ.get("OG_ANALYZE_MODEL", "gpt-4o")
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

QUALITY_DIRECTIVE = (
    "QUALITY: Museum-grade editorial collage — sharp focal details, cohesive art direction, "
    "professional torn-paper layering, subtle halftone grain. Thumbnail-readable at 120x63px. "
    "Final crop MUST read well at exactly 1200x630 landscape.\n"
)

ANALYZE_PROFILES = {
    "alignify": {
        "system": """You are an art director for Alignify (alignify.co) OG social cards (1200x630 editorial collage).

Your job: read page source content and produce a JSON brief so image generation is unmistakably about THIS page — not a generic category cliché.

Critical distinctions:
- GEO/AEO (Generative Engine Optimization) ≠ SEO. GEO = brand cited inside LLM answers (ChatGPT, Claude, Perplexity). Hero visual MUST be an LLM chat UI with numbered citation footnotes [1][2] in the assistant reply. NEVER use magnifying glass, search bar, or SERP as the hero for GEO.
- Tools Best pages = product workflow + output samples.
- Marketing guides = strategy-specific metaphor from the article thesis.

Output ONLY valid JSON matching the schema. composition fields must be English (image model follows English better).
Do NOT include real trademark logos (OpenAI, Anthropic, Google) — describe UI archetypes only ("ChatGPT-style dark chat panel").
""",
        "schema": {
            "page_topic_one_liner": "string",
            "differentiator_vs_generic": "string — why this is NOT a generic stock visual",
            "visual_anchors": ["2-4 must-have visual elements, ordered by prominence"],
            "anti_patterns": ["explicit bans — what would make viewers think wrong topic"],
            "accent_suggestion": "klein-blue | mars-green | titian-red | alignify-navy",
            "locales": {
                "en": {
                    "headline": "string",
                    "headline_line2": "optional e.g. (2026)",
                    "subtitle": "one line",
                    "tagline": "optional second line for EN",
                    "composition": "detailed English visual brief for image model, HERO element first",
                },
                "zh": {
                    "headline": "string",
                    "headline_line2": "optional",
                    "subtitle": "one line only — keep minimal",
                    "composition": "English visual brief (same layout as EN), stricter: no extra on-image text, no blank cards",
                },
            },
        },
        "user_template": """Analyze this Alignify page for OG cover generation.

Section: {section}
Slug: {slug}
URL pattern: {url}

Section signature rules (apply all matching):
{signatures}

JSON schema to output:
{schema}

--- EN page content ---
{en_md}

--- ZH page content ---
{zh_md}

Requirements:
1. visual_anchors[0] must be the HERO element (largest, most recognizable).
2. anti_patterns must explicitly ban wrong-category clichés (e.g. for GEO: ban search bar hero, magnifying glass, SERP).
3. composition for EN and ZH must describe the SAME layout; ZH stricter on no extra text.
4. Headlines must match page H1 intent, PPT-level brevity.
""",
    },
    "dubbingai": {
        "system": """You are an art director for Dubbing AI (dubbingai.io/blog) OG social cards (1200x630 editorial collage).

Your job: read blog source content and produce a JSON brief so image generation is unmistakably about THIS article — not a generic voice-tech stock visual.

Critical distinctions:
- Real-time mic voice changer (gaming/Discord/streaming) ≠ Google Assistant TTS settings ≠ file-based voice cloning.
- Soundboard / meme article = playful collage with sound-wave tiles, game/anime cues — NOT corporate SaaS hero.
- Voice actor profile = character portrait mood + mic/stream context — NOT product comparison grid.
- Alternative/comparison = fair side-by-side workflow visuals — NO readable competitor logos (Voicemod, Discord, etc.).

Brand accent: cyan (#22D3EE) to indigo (#6366F1) gradient feel — gaming/streaming energy, young audience.

Output ONLY valid JSON matching the schema. composition fields must be English (image model follows English better).
Do NOT include real trademark logos (Discord, Voicemod, Fortnite, etc.) — describe UI archetypes only.
""",
        "schema": {
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
        },
        "user_template": """Analyze this Dubbing AI blog article for OG cover generation.

Section: {section}
Slug: {slug}
URL: {url}

Section signature rules (apply all matching):
{signatures}

JSON schema to output:
{schema}

--- EN article content ---
{en_md}

Requirements:
1. visual_anchors[0] must be the HERO element (largest, most recognizable).
2. anti_patterns must explicitly ban wrong-category clichés (e.g. for Google Assistant article: ban gaming headset hero; for voice changer hub: ban phone assistant settings UI).
3. Headlines must match article title intent, PPT-level brevity, gaming/streaming tone where appropriate.
4. Blog is English-only — only populate locales.en.
""",
    },
}


# ---------------------------------------------------------------- paths

def registry_path(cfg: dict) -> Path:
    return Path(cfg["ctx_root"]) / cfg["registry_path"]


def briefs_root(cfg: dict) -> Path:
    return Path(cfg["ctx_root"]) / cfg["briefs_root"]


def section_sig_path(cfg: dict) -> Path:
    return Path(cfg["ctx_root"]) / cfg["section_signatures_path"]


# ---------------------------------------------------------------- registry

def load_registry(cfg: dict) -> dict:
    return json.loads(registry_path(cfg).read_text(encoding="utf-8"))


def save_registry(cfg: dict, registry: dict) -> None:
    registry_path(cfg).write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def find_entry(cfg: dict, registry: dict, section: str, slug: str, locale: str) -> dict:
    fallback_locale = cfg.get("default_locale", "en")
    for entry in registry["entries"]:
        if (
            entry["section"] == section
            and entry["slug"] == slug
            and entry.get("locale", fallback_locale) == locale
        ):
            return entry
    raise SystemExit(f"No registry entry for {section}/{slug} locale={locale}")


# ---------------------------------------------------------------- briefs

def brief_path(cfg: dict, section: str, slug: str) -> Path:
    return briefs_root(cfg) / section / slug / "brief.json"


def load_brief(cfg: dict, section: str, slug: str) -> dict | None:
    p = brief_path(cfg, section, slug)
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def save_brief(cfg: dict, section: str, slug: str, brief: dict) -> Path:
    p = brief_path(cfg, section, slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding="utf-8")
    return p


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


# ---------------------------------------------------------------- page analysis

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


def load_section_signatures(cfg: dict) -> dict:
    p = section_sig_path(cfg)
    if p.is_file():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def signatures_for_page(cfg: dict, section: str, slug: str) -> dict[str, Any]:
    sigs = load_section_signatures(cfg)
    out: dict[str, Any] = {"section": section, "slug": slug, "rules": []}
    for key, rule in sigs.items():
        if slug in rule.get("slugs", []):
            out["rules"].append({"id": key, **rule})
        elif section in rule.get("sections", []):
            out["rules"].append({"id": key, **rule})
    return out


def resolve_openai_key(cfg: dict, key_file: str | None = None) -> str:
    if key_file:
        return Path(key_file).read_text(encoding="utf-8").strip()
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        return key.strip()
    for candidate in (
        Path(cfg["ctx_root"]) / ".secrets" / "openai-key",
        Path.home() / ".openai-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "OPENAI_API_KEY not found. Set env OPENAI_API_KEY or <client>/.secrets/openai-key"
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


def _find_blog_md(cfg: dict, slug: str) -> Path | None:
    blog_root = Path(cfg["ctx_root"]) / "blog"
    for p in sorted(blog_root.glob(f"*-{slug}-*.md")):
        return p
    for candidate in (
        blog_root / f"{slug}.md",
        blog_root / "cms-export" / f"{slug}.md",
    ):
        if candidate.is_file():
            return candidate
    return None


def analyze_page(cfg: dict, section: str, slug: str, deploy_root: Path | None = None, api_key: str | None = None) -> dict:
    """Dispatch per-client page-source strategy (alignify: deploy content en+zh;
    dubbingai: context blog markdown, en only)."""
    profile = ANALYZE_PROFILES[cfg["name"]]
    source = cfg.get("analyze_source", "blog-md")

    if source == "deploy-content":
        en_md = read_page_md(deploy_root / "content" / section / "en" / f"{slug}.md") if deploy_root else ""
        zh_md = read_page_md(deploy_root / "content" / section / "zh" / f"{slug}.md") if deploy_root else ""
        if not en_md and not zh_md:
            raise SystemExit(f"No page content found for {section}/{slug}")
        user_prompt = profile["user_template"].format(
            section=section, slug=slug,
            url=cfg["url_pattern"].format(section=section, slug=slug),
            signatures=json.dumps(signatures_for_page(cfg, section, slug), ensure_ascii=False, indent=2),
            schema=json.dumps(profile["schema"], ensure_ascii=False, indent=2),
            en_md=en_md or "(missing)", zh_md=zh_md or "(missing)",
        )
    else:
        md_path = _find_blog_md(cfg, slug)
        if md_path is None:
            raise SystemExit(f"No blog markdown found for slug={slug}")
        md = read_page_md(md_path)
        user_prompt = profile["user_template"].format(
            section=section, slug=slug,
            url=cfg["url_pattern"].format(section=section, slug=slug),
            signatures=json.dumps(signatures_for_page(cfg, section, slug), ensure_ascii=False, indent=2),
            schema=json.dumps(profile["schema"], ensure_ascii=False, indent=2),
            en_md=md or "(missing)",
        )

    key = api_key or resolve_openai_key(cfg)
    result = call_openai_json(profile["system"], user_prompt, key)

    brief = {
        "section": section,
        "slug": slug,
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "model": OPENAI_MODEL,
        **result,
    }
    return brief


def merge_brief_into_registry(cfg: dict, brief: dict, status: str = "pending") -> int:
    registry = load_registry(cfg)
    section = brief["section"]
    slug = brief["slug"]
    updated = 0
    entries = registry.setdefault("entries", [])

    for locale in cfg.get("locales", ["en"]):
        loc = brief.get("locales", {}).get(locale)
        if not loc:
            continue
        entry = None
        for e in entries:
            if e.get("section") == section and e.get("slug") == slug and e.get("locale") == locale:
                entry = e
                break
        if entry is None:
            entry = {
                "section": section,
                "slug": slug,
                "locale": locale,
                "style": cfg.get("default_style", "editorial-collage"),
                "author": "Kostja",
            }
            entries.append(entry)

        entry["headline"] = loc.get("headline", entry.get("headline", ""))
        if loc.get("headline_line2"):
            entry["headline_line2"] = loc["headline_line2"]
        if loc.get("subtitle"):
            entry["subtitle"] = loc["subtitle"]
        if locale == "en" and loc.get("tagline"):
            entry["tagline"] = loc["tagline"]
        elif locale != "en" and "tagline" in entry:
            del entry["tagline"]

        entry["composition"] = loc.get("composition", entry.get("composition", ""))
        if brief.get("accent_suggestion"):
            entry["accent"] = brief["accent_suggestion"]
        entry["visual_anchors"] = brief.get("visual_anchors", [])
        entry["anti_patterns"] = brief.get("anti_patterns", [])
        entry["status"] = status
        entry["notes"] = f"LLM brief {brief.get('analyzed_at', '')[:10]}"
        updated += 1

    save_registry(cfg, registry)
    return updated
