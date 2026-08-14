#!/usr/bin/env python3
"""Fetch CMS blog posts and write cms-export/{slug}.md with YAML frontmatter."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from html import unescape
from pathlib import Path

import html2text
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.csv"
TODAY = date.today().isoformat()

USER_AGENT = "Mozilla/5.0 (compatible; DubbingAICMSExport/1.0)"


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="replace")


def meta_content(soup: BeautifulSoup, *keys: tuple[str, str]) -> str | None:
    for attr, val in keys:
        tag = soup.find("meta", attrs={attr: val})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None


def parse_ld_json(soup: BeautifulSoup) -> dict | None:
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
        except (json.JSONDecodeError, TypeError):
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict):
                continue
            t = item.get("@type", "")
            if t in ("Article", "BlogPosting", "NewsArticle") or (
                isinstance(t, list) and any(x in ("Article", "BlogPosting", "NewsArticle") for x in t)
            ):
                return item
    return None


def extract_categories(soup: BeautifulSoup) -> list[str]:
    cats = []
    for a in soup.select('a[href*="/blog/category/"]'):
        href = a.get("href", "")
        m = re.search(r"/blog/category/([^/]+)", href)
        if m:
            cats.append(m.group(1).strip("/"))
    return list(dict.fromkeys(cats))


def extract_content_html(soup: BeautifulSoup) -> BeautifulSoup | None:
    for sel in (".entry-content", ".post-content", "article .content", "article"):
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 200:
            return node
    return None


def html_to_markdown(html: str) -> str:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False
    h.protect_links = True
    h.single_line_break = False
    h.unicode_snob = True
    return h.handle(html).strip()


def clean_markdown(md: str) -> str:
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip()
    # Drop trailing CMS footer lines leaked into entry-content
    footer_markers = (
        "all rights reserved",
        "terms of use",
        "privacy policy",
        "halo interactive",
    )
    lines = md.splitlines()
    while lines:
        low = lines[-1].lower()
        if any(m in low for m in footer_markers) and len(low) < 120:
            lines.pop()
        else:
            break
    return "\n".join(lines).strip()


def yaml_quote(s: str) -> str:
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def yaml_list(items: list[str], indent: int = 0) -> str:
    if not items:
        return "[]"
    pad = " " * indent
    lines = [f"{pad}- {yaml_quote(i)}" for i in items]
    return "\n".join(lines)


def build_frontmatter(data: dict) -> str:
    lines = ["---"]
    lines.append(f"title: {yaml_quote(data['title'])}")
    lines.append(f"description: {yaml_quote(data['description'])}")
    lines.append(f'slug: {yaml_quote(data["slug"])}')
    lines.append(f"date: {data['date']}")
    lines.append(f"author: {yaml_quote(data['author'])}")
    if data.get("category"):
        lines.append(f"category: {yaml_quote(data['category'])}")
    lines.append(f"lang: {yaml_quote(data.get('lang', 'en'))}")
    lines.append(f'status: {yaml_quote(data.get("status", "published"))}')
    lines.append(f'source: {yaml_quote("cms")}')
    lines.append(f"canonical: {yaml_quote(data['canonical'])}")
    lines.append(f"migrated_at: {data.get('migrated_at', TODAY)}")
    sb = data.get("superseded_by") or ""
    lines.append(f'superseded_by: {yaml_quote(sb)}')
    lines.append("---")
    return "\n".join(lines)


def convert_slug(slug: str, url: str, lang: str, superseded_by: str) -> dict:
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")

    ld = parse_ld_json(soup) or {}
    h1_tag = soup.select_one(".entry-title, h1.entry-title, article h1")
    h1_text = h1_tag.get_text(strip=True) if h1_tag else ""
    title = (
        (ld.get("headline") or "")
        or meta_content(soup, ("property", "og:title"), ("name", "twitter:title"))
        or h1_text
        or slug.replace("-", " ").title()
    )
    title = unescape(re.sub(r"\s*[|\-–—]\s*Dubbing AI.*$", "", title, flags=re.I).strip())

    description = (
        (ld.get("description") or "")
        or meta_content(soup, ("name", "description"), ("property", "og:description"))
        or ""
    )
    description = unescape(description.strip())

    date_pub = ld.get("datePublished") or meta_content(soup, ("property", "article:published_time"))
    if date_pub:
        date_pub = date_pub[:10]
    else:
        date_pub = TODAY

    image = meta_content(soup, ("property", "og:image")) or f"/blog/images/{slug}.jpg"

    author = "Kostja"
    if ld.get("author"):
        a = ld["author"]
        if isinstance(a, dict):
            author = a.get("name") or author
        elif isinstance(a, str):
            author = a
    if author.lower() in ("admin", "dubbing ai"):
        author = "Kostja"

    cats = extract_categories(soup)
    category = cats[0] if cats else ""

    content_node = extract_content_html(soup)
    if not content_node:
        raise ValueError("No entry-content found")

    # Remove related posts / share widgets inside content if present
    for bad in content_node.select(
        ".blogbuster-related-posts-wrapper, .sharedaddy, .jp-relatedposts, nav, .post-navigation"
    ):
        bad.decompose()

    body_md = clean_markdown(html_to_markdown(str(content_node)))

    # Ensure H1 at top matches title
    if not body_md.startswith("#"):
        body_md = f"# {title}\n\n{body_md}"
    else:
        body_md = re.sub(r"^#\s+.*?\n", f"# {title}\n", body_md, count=1)

    fm = build_frontmatter(
        {
            "title": title,
            "description": description,
            "slug": slug,
            "date": date_pub,
            "author": author,
            "category": category,
            "lang": lang,
            "status": "published",
            "canonical": url.rstrip("/") + "/",
            "migrated_at": TODAY,
            "superseded_by": superseded_by,
        }
    )

    out_path = ROOT / f"{slug}.md"
    out_path.write_text(fm + "\n\n" + body_md + "\n", encoding="utf-8")

    return {
        "date_published": date_pub,
        "category": category,
        "migrated_at": TODAY,
        "status": "done",
    }


def load_manifest() -> tuple[list[dict], list[str]]:
    with MANIFEST.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows, list(rows[0].keys()) if rows else []


def save_manifest(rows: list[dict], fieldnames: list[str]) -> None:
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", help="Only process this batch (P0, P1, P2, P3)")
    parser.add_argument("--slug", help="Only process one slug")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    parser.add_argument("--force", action="store_true", help="Re-fetch even if status=done")
    args = parser.parse_args()

    rows, fieldnames = load_manifest()
    if not rows:
        print("Empty manifest", file=sys.stderr)
        return 1

    ok = err = skip = 0
    for row in rows:
        slug = row["slug"]
        if args.slug and slug != args.slug:
            continue
        if args.batch and row.get("batch") != args.batch:
            continue
        if row["status"] == "skip":
            skip += 1
            continue
        if row["status"] == "done" and not args.force:
            continue
        if row["status"] == "error" and not args.force and not args.slug:
            continue

        url = row["url"]
        print(f"Fetching {slug} ...", flush=True)
        try:
            result = convert_slug(
                slug,
                url,
                row.get("lang") or "en",
                row.get("superseded_by") or "",
            )
            row.update(result)
            ok += 1
        except urllib.error.HTTPError as e:
            row["status"] = "error"
            row["notes"] = (row.get("notes") or "") + f" HTTP {e.code}"
            err += 1
            print(f"  ERROR HTTP {e.code}", flush=True)
        except Exception as e:
            row["status"] = "error"
            row["notes"] = (row.get("notes") or "") + f" {type(e).__name__}: {e}"
            err += 1
            print(f"  ERROR {e}", flush=True)

        save_manifest(rows, fieldnames)
        time.sleep(args.delay)

    print(f"Done: ok={ok} err={err} skip={skip}")
    return 0 if err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
