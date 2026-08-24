#!/usr/bin/env python3
"""Shared helpers for Tools/Blog internal link audit and injection."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

BLOG_TOOL_SLUGS = frozenset(
    {
        "ai-training-data",
        "data-engineering-agent",
        "inference-infrastructure",
        "medical-scribe",
        "web-fetch",
        "agent-sandbox",
    }
)

_blog_tools_cache: dict[str, frozenset[str]] = {}


def parse_blog_tools_slugs(deploy_root: Path) -> frozenset[str]:
    key = str(deploy_root.resolve())
    if key in _blog_tools_cache:
        return _blog_tools_cache[key]
    blog_cfg = deploy_root / "src" / "data" / "blog-pages-config.ts"
    slugs: set[str] = set()
    if blog_cfg.is_file():
        text = blog_cfg.read_text(encoding="utf-8")
        for block in re.finditer(r"\{[^{}]*?routeCategory:\s*\"tools\"[^{}]*?\}", text, re.DOTALL):
            m = re.search(r'slug:\s*"([\w-]+)"', block.group(0))
            if m:
                slugs.add(m.group(1))
    out = frozenset(slugs) if slugs else BLOG_TOOL_SLUGS
    _blog_tools_cache[key] = out
    return out

MIN_TOTAL_LINKS = 5
DENSITY_WINDOW_EN = 400
DENSITY_WINDOW_ZH = 250
MAX_LINKS_PER_WINDOW = 3
MIN_ANCHOR_LEN_ZH = 2
MIN_ANCHOR_LEN_EN = 1

BANNED_ANCHORS = {
    "click here",
    "learn more",
    "read more",
    "more",
    "here",
    "link",
    "点击这里",
    "了解更多",
    "阅读更多",
    "更多",
    "点击",
    "这里",
    "details",
    "info",
    "this page",
    "本页",
    "详情",
}

TERRITORY_GROUPS: dict[str, list[str]] = {
    "web_data": [
        "web-scraping",
        "web-fetch",
        "web-search-api",
        "headless-browser",
        "search-indexing",
        "ocr",
    ],
    "search_discovery": ["search-engine", "geo", "web-search-api", "knowledge-base"],
    "design": [
        "design",
        "logo-generator",
        "poster-generator",
        "presentation-maker",
        "website-builder",
        "user-research",
    ],
    "llm_eval": [
        "llm",
        "llm-for-coding",
        "llm-for-math",
        "llm-for-reasoning",
        "multimodal-llm",
        "evaluation",
        "world-model",
    ],
    "coding": [
        "coding",
        "vibe-coding",
        "cli",
        "code-review",
        "code-completion",
        "ide",
        "app-builder",
        "website-builder",
        "api",
        "documentation",
    ],
    "agent": [
        "agent-skills",
        "agent-for-desktop",
        "agent-sandbox",
        "openclaw-alternatives",
        "workflow",
        "browser",
        "headless-browser",
        "authentication",
        "cli",
    ],
    "media_image": [
        "image-generator",
        "image-editor",
        "image-enhancer",
        "background-changer",
        "headshot-generator",
        "avatar",
        "image",
        "virtual-staging",
        "interior-design",
        "lip-sync",
    ],
    "media_video": [
        "video",
        "video-generator",
        "text-to-video",
        "image-to-video",
        "video-to-video",
        "video-editor",
        "video-clipping",
        "video-effects",
        "canvas-video",
        "filmmaking",
        "animation-generator",
        "short-drama",
        "music-video-generator",
    ],
    "voice": [
        "voice",
        "voice-changer",
        "text-to-speech",
        "speech-to-text",
        "accent-conversion",
        "audio-translator",
        "video-translator",
        "music-generator",
    ],
    "productivity": [
        "productivity",
        "note-taker",
        "notes-generator",
        "chatbot",
        "text-generator",
        "spreadsheet",
        "memory",
        "workflow",
    ],
    "marketing": [
        "influencer-marketing",
        "affiliate-marketing",
        "referral-program",
        "geo",
        "lead-generation",
        "b2b",
        "linkedin",
    ],
    "hr": ["recruiting", "interview-assistant", "linkedin", "note-taker"],
    "health": ["healthcare", "medical-scribe", "legal", "family-assistant"],
    "3d": ["3d", "3d-model-generator", "3d-modelling", "3d-scanner", "cad", "virtual-staging"],
}

BLOG_NEIGHBOR_OVERRIDES: dict[str, list[str]] = {
    "agent-sandbox": [
        "agent-skills",
        "inference-infrastructure",
        "agent-for-desktop",
        "authentication",
        "headless-browser",
        "cli",
        "openclaw-alternatives",
        "workflow",
    ],
    "inference-infrastructure": [
        "api",
        "llm",
        "agent-sandbox",
        "agent-skills",
        "coding",
        "data-engineering-agent",
        "ai-training-data",
    ],
    "ai-training-data": [
        "evaluation",
        "web-scraping",
        "llm",
        "api",
        "world-model",
        "inference-infrastructure",
        "data-engineering-agent",
    ],
    "data-engineering-agent": [
        "workflow",
        "agent-skills",
        "coding",
        "cli",
        "api",
        "ai-training-data",
        "web-scraping",
    ],
    "medical-scribe": [
        "healthcare",
        "note-taker",
        "productivity",
        "speech-to-text",
        "legal",
    ],
    "web-fetch": [
        "web-search-api",
        "web-scraping",
        "headless-browser",
        "search-indexing",
        "llm",
    ],
}

WAVE_SLUGS: dict[str, list[str]] = {
    "wave0_blog": [
        "agent-sandbox",
        "ai-training-data",
        "data-engineering-agent",
        "inference-infrastructure",
        "medical-scribe",
        "web-fetch",
    ],
    "p0": [
        "headless-browser",
        "agent-for-desktop",
        "agent-skills",
        "browser",
        "cli",
        "workflow",
        "openclaw-alternatives",
        "coding",
    ],
    "p1": [
        "search-engine",
        "web-search-api",
        "web-scraping",
        "llm",
        "authentication",
        "documentation",
        "code-review",
        "character-chat",
        "linkedin",
        "avatar",
        "world-model",
        "evaluation",
        "api",
        "vibe-coding",
        "knowledge-base",
    ],
}

A_TAG_PATTERN = re.compile(
    r"""<a\s+[^>]*href=(?:["']|\\["'])((?:/zh)?/(?:tools|blog)/([\w-]+))(?:["']|\\["'])[^>]*>(.*?)</a>""",
    re.DOTALL,
)


def find_deploy_root() -> Path:
    env = os.environ.get("ALIGNIFY_DEPLOY_ROOT")
    if env and Path(env).is_dir():
        return Path(env)
    here = Path(__file__).resolve()
    candidates = [
        here.parents[3] / "部署项目" / "alignify-by-kostja",
        here.parents[2] / "alignify-by-kostja",
        Path(r"D:\部署项目\alignify-by-kostja"),
    ]
    for c in candidates:
        if (c / "content" / "tools").is_dir():
            return c
    raise FileNotFoundError("Cannot locate deploy repo (set ALIGNIFY_DEPLOY_ROOT)")


def content_dirs(deploy_root: Path, source: str) -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    if source in ("tools", "both"):
        p = deploy_root / "content" / "tools"
        if p.is_dir():
            out.append(("tools", p))
    if source in ("blog", "both"):
        p = deploy_root / "content" / "blog"
        if p.is_dir():
            out.append(("blog", p))
    return out


def is_blog_tools_slug(slug: str, deploy_root: Path | None = None) -> bool:
    if deploy_root is None:
        try:
            deploy_root = find_deploy_root()
        except FileNotFoundError:
            return slug in BLOG_TOOL_SLUGS
    return slug in parse_blog_tools_slugs(deploy_root)


def href_for_slug(slug: str, locale: str, deploy_root: Path | None = None) -> str:
    prefix = "/zh" if locale == "zh" else ""
    route = "blog" if is_blog_tools_slug(slug, deploy_root) else "tools"
    return f"{prefix}/{route}/{slug}"


def make_link(slug: str, anchor: str, locale: str) -> str:
    return f'<a href="{href_for_slug(slug, locale)}">{anchor}</a>'


def parse_keywords(deploy_root: Path) -> dict[str, dict[str, str]]:
    keywords: dict[str, dict[str, str]] = {}
    tools_cfg = deploy_root / "src" / "data" / "tools-pages-config.ts"
    if tools_cfg.is_file():
        text = tools_cfg.read_text(encoding="utf-8")
        for m in re.finditer(
            r'slug:\s*"([\w-]+)"[^}]*?keywordEn:\s*"([^"]+)"[^}]*?keywordZh:\s*"([^"]+)"',
            text,
            re.DOTALL,
        ):
            keywords[m.group(1)] = {"en": m.group(2), "zh": m.group(3)}
    blog_cfg = deploy_root / "src" / "data" / "blog-pages-config.ts"
    blog_tools = parse_blog_tools_slugs(deploy_root)
    if blog_cfg.is_file():
        text = blog_cfg.read_text(encoding="utf-8")
        for m in re.finditer(
            r'slug:\s*"([\w-]+)"[^}]*?shortTitleEn:\s*"([^"]+)"[^}]*?shortTitleZh:\s*"([^"]+)"',
            text,
            re.DOTALL,
        ):
            slug = m.group(1)
            if slug in blog_tools:
                keywords[slug] = {"en": m.group(2), "zh": m.group(3)}
    return keywords


def anchor_for(slug: str, locale: str, keywords: dict[str, dict[str, str]]) -> str:
    if slug in keywords:
        return keywords[slug]["zh" if locale == "zh" else "en"]
    return slug.replace("-", " ").title()


def neighbors_for(slug: str, limit: int = 10) -> list[str]:
    if slug in BLOG_NEIGHBOR_OVERRIDES:
        return [s for s in BLOG_NEIGHBOR_OVERRIDES[slug] if s != slug][:limit]
    for group in TERRITORY_GROUPS.values():
        if slug in group:
            return [s for s in group if s != slug][:limit]
    return ["llm", "workflow", "api", "productivity", "coding"][:limit]


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def count_chinese_chars(text: str) -> int:
    return len(re.findall(r"[一-鿿]", text))


def count_english_words(text: str) -> int:
    clean = re.sub(r"<[^>]+>", " ", text)
    return len(re.findall(r"[a-zA-Z]+", clean))


def get_block_text(block: dict) -> str:
    raw = json.dumps(block, ensure_ascii=False)
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r'[{}[\]",:\\]', " ", text)
    return text


def extract_links_from_blocks(blocks: list, locale: str) -> list[tuple[str, str, int, str, str]]:
    all_links: list[tuple[str, str, int, str, str]] = []
    for idx, block in enumerate(blocks):
        block_raw = json.dumps(block, ensure_ascii=False)
        btype = block.get("type", "section")
        for m in A_TAG_PATTERN.finditer(block_raw):
            href = m.group(1)
            slug = m.group(2)
            if locale == "zh" and not href.startswith("/zh/"):
                continue
            if locale == "en" and href.startswith("/zh/"):
                continue
            anchor = strip_html(m.group(3))
            all_links.append((slug, anchor, idx, btype, m.group(0)[:120]))
    return all_links


def list_json_slugs(deploy_root: Path, source: str = "both") -> dict[str, str]:
    blog_tools = parse_blog_tools_slugs(deploy_root)
    out: dict[str, str] = {}
    for route, base in content_dirs(deploy_root, source):
        for loc in ("en", "zh"):
            d = base / loc
            if not d.is_dir():
                continue
            for f in d.glob("*.json"):
                slug = f.stem
                if route == "blog" and slug not in blog_tools:
                    continue
                out[slug] = route
    return out
