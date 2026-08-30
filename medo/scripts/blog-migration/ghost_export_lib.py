#!/usr/bin/env python3
"""Shared Ghost HTML → Markdown export logic."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

import html2text
from bs4 import BeautifulSoup, Tag

SITE_HOST = "medo.dev"


def meta_from_page(soup: BeautifulSoup) -> dict:
    ld = soup.find("script", type="application/ld+json")
    data = json.loads(ld.string) if ld and ld.string else {}
    og_desc = soup.find("meta", property="og:description")
    description = (og_desc.get("content") if og_desc else "") or data.get("description", "")
    description = re.sub(r"\s+", " ", description).strip()

    published = data.get("datePublished", "")
    modified = data.get("dateModified", "")
    date = published[:10] if published else ""
    updated = modified[:10] if modified and modified != published else ""

    canonical = soup.find("link", rel="canonical")
    slug = ""
    url_path = ""
    if canonical and canonical.get("href"):
        url_path = urlparse(canonical["href"]).path.strip("/")
        slug = url_path.split("/")[-1]

    author = data.get("author", {})
    if isinstance(author, dict):
        author = author.get("name", "")

    tags_raw = data.get("keywords", "")
    ghost_tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

    return {
        "title": data.get("headline") or (soup.title.string.strip() if soup.title else ""),
        "description": description,
        "slug": slug,
        "url_path": url_path,
        "date": date,
        "updated": updated,
        "author": author,
        "ghost_tags": ghost_tags,
    }


def rewrite_links(html: str) -> str:
    html = re.sub(
        rf"https?://(?:www\.)?{re.escape(SITE_HOST)}/blog/([^\"'\s>)]+)/?",
        r"/blog/\1",
        html,
    )
    html = re.sub(r'href="/blog/([^"\']+)/"', r'href="/blog/\1"', html)
    html = re.sub(
        rf"https?://(?:www\.)?{re.escape(SITE_HOST)}/(\?[^\"'\s>]*)",
        r"/\1",
        html,
    )
    html = re.sub(rf"https?://(?:www\.)?{re.escape(SITE_HOST)}/?", r"/", html)
    return html


def extract_html_tables(content: Tag, soup: BeautifulSoup) -> list[str]:
    tables: list[str] = []
    for node in content.find_all("table"):
        tables.append(str(node))
        placeholder = soup.new_tag("p")
        placeholder.string = f"<!-- TABLE_{len(tables) - 1} -->"
        node.replace_with(placeholder)
    return tables


def html_to_markdown(html: str) -> str:
    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_links = False
    converter.ignore_images = False
    converter.single_line_break = False
    converter.protect_links = True
    converter.wrap_links = False
    md = converter.handle(html).strip()
    return re.sub(r"\n{3,}", "\n\n", md)


def infer_category(tags: list[str]) -> tuple[str, str]:
    tag_lower = {t.lower() for t in tags}
    if "tutorial" in tag_lower:
        category = "Tutorial"
    elif "guides" in tag_lower or "guide" in tag_lower:
        category = "Guide"
    elif "case study" in tag_lower:
        category = "Case Study"
    elif "product" in tag_lower:
        category = "Product"
    else:
        category = "Guide"
    return category, "Mobile App"


def build_frontmatter(meta: dict, category: str, secondary: str) -> str:
    def esc(s: str) -> str:
        return s.replace('"', "'")

    lines = [
        "---",
        f'title: "{esc(meta["title"])}"',
        f'description: "{esc(meta["description"])}"',
        f'slug: "{meta["slug"]}"',
        f'date: {meta["date"]}',
    ]
    if meta.get("updated"):
        lines.append(f'updated: {meta["updated"]}')
    if meta.get("author"):
        lines.append(f'author: "{esc(meta["author"])}"')
    lines.extend([f'category: "{category}"', f'secondary_category: "{secondary}"', "---"])
    return "\n".join(lines)


def export_from_html(html: str, source_label: str = "html") -> dict:
    soup = BeautifulSoup(html, "html.parser")
    meta = meta_from_page(soup)
    content = soup.select_one("section.gh-content")
    if not content:
        raise ValueError(f"No section.gh-content in {source_label}")

    tables = extract_html_tables(content, soup)
    inner_html = rewrite_links(str(content))
    md_body = html_to_markdown(inner_html)
    for i, table_html in enumerate(tables):
        md_body = md_body.replace(f"<!-- TABLE_{i} -->", f"\n\n{table_html}\n\n")

    category, secondary = infer_category(meta.get("ghost_tags", []))
    frontmatter = build_frontmatter(meta, category, secondary)
    markdown = f"{frontmatter}\n\n# {meta['title']}\n\n{md_body}\n"
    return {"markdown": markdown, "meta": meta}


def md_output_path(output_dir: Path, url_path: str, slug: str) -> Path:
    parts = [p for p in url_path.split("/") if p and p not in ("blog", slug)]
    if parts:
        return output_dir.joinpath(*parts, f"{slug}.md")
    return output_dir / f"{slug}.md"
