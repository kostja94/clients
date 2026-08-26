"""Shared OG page analysis + prompt assembly (Alignify context repo)."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ALIGNIFY_CTX = Path(__file__).resolve().parents[2]
BRIEFS_ROOT = ALIGNIFY_CTX / "data" / "og-briefs"
REGISTRY_PATH = ALIGNIFY_CTX / "data" / "og-prompt-registry.json"
SECTION_SIG_PATH = ALIGNIFY_CTX / "data" / "og-section-signatures.json"

DEFAULT_DEPLOY_ROOTS = [
    Path(r"E:\自有部署项目\alignify production"),
    Path(r"D:\部署项目\alignify-by-kostja"),
]

OPENAI_MODEL = os.environ.get("OG_ANALYZE_MODEL", "gpt-4o")
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

ANALYZE_SYSTEM = """You are an art director for Alignify (alignify.co) OG social cards (1200x630 editorial collage).

Your job: read page source content and produce a JSON brief so image generation is unmistakably about THIS page — not a generic category cliché.

Critical distinctions:
- GEO/AEO (Generative Engine Optimization) ≠ SEO. GEO = brand cited inside LLM answers (ChatGPT, Claude, Perplexity). Hero visual MUST be an LLM chat UI with numbered citation footnotes [1][2] in the assistant reply. NEVER use magnifying glass, search bar, or SERP as the hero for GEO.
- Tools Best pages = product workflow + output samples.
- Marketing guides = strategy-specific metaphor from the article thesis.

Output ONLY valid JSON matching the schema. composition fields must be English (image model follows English better).
Do NOT include real trademark logos (OpenAI, Anthropic, Google) — describe UI archetypes only ("ChatGPT-style dark chat panel").
"""

ANALYZE_SCHEMA = {
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
}


def resolve_deploy_root(explicit: str | None = None) -> Path:
    if explicit:
        return Path(explicit)
    env = os.environ.get("ALIGNIFY_DEPLOY_ROOT")
    if env:
        return Path(env)
    for p in DEFAULT_DEPLOY_ROOTS:
        if p.is_dir():
            return p
    raise SystemExit("Deploy root not found. Set ALIGNIFY_DEPLOY_ROOT or pass --deploy-root.")


def page_md_path(deploy_root: Path, section: str, slug: str, locale: str) -> Path:
    return deploy_root / "content" / section / locale / f"{slug}.md"


def read_page_md(path: Path, max_chars: int = 12000) -> str:
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    # Strip frontmatter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    # Remove HTML blocks noise
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
        ALIGNIFY_CTX / ".secrets" / "openai-key",
        Path.home() / ".openai-key",
    ):
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "OPENAI_API_KEY not found. Set env OPENAI_API_KEY or Alignify/.secrets/openai-key"
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
    en_md: str,
    zh_md: str,
    signatures: dict,
) -> str:
    return f"""Analyze this Alignify page for OG cover generation.

Section: {section}
Slug: {slug}
URL pattern: https://alignify.co/{section}/{slug}

Section signature rules (apply all matching):
{json.dumps(signatures, ensure_ascii=False, indent=2)}

JSON schema to output:
{json.dumps(ANALYZE_SCHEMA, ensure_ascii=False, indent=2)}

--- EN page content ---
{en_md or "(missing)"}

--- ZH page content ---
{zh_md or "(missing)"}

Requirements:
1. visual_anchors[0] must be the HERO element (largest, most recognizable).
2. anti_patterns must explicitly ban wrong-category clichés (e.g. for GEO: ban search bar hero, magnifying glass, SERP).
3. composition for EN and ZH must describe the SAME layout; ZH stricter on no extra text.
4. Headlines must match page H1 intent, PPT-level brevity.
"""


def analyze_page(
    section: str,
    slug: str,
    deploy_root: Path | None = None,
    api_key: str | None = None,
) -> dict:
    deploy_root = deploy_root or resolve_deploy_root(None)
    en_md = read_page_md(page_md_path(deploy_root, section, slug, "en"))
    zh_md = read_page_md(page_md_path(deploy_root, section, slug, "zh"))
    if not en_md and not zh_md:
        raise SystemExit(f"No page content found for {section}/{slug}")

    signatures = signatures_for_page(section, slug)
    user_prompt = build_analyze_user_prompt(section, slug, en_md, zh_md, signatures)

    key = api_key or resolve_openai_key()
    result = call_openai_json(ANALYZE_SYSTEM, user_prompt, key)

    brief = {
        "section": section,
        "slug": slug,
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

    for locale in ("en", "zh"):
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
                "style": "editorial-collage",
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
        elif locale == "zh" and "tagline" in entry:
            del entry["tagline"]

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
    """Inject analysis into fal prompt."""
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
    "professional torn-paper layering, subtle halftone grain. Thumbnail-readable at 120x63px.\n"
)
