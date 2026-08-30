#!/usr/bin/env python3
"""Fetch all Ghost posts from medo.dev/blog and export Markdown only."""

from __future__ import annotations

import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ghost_export_lib import export_from_html, md_output_path

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
USER_AGENT = "MeDoBlogMigration/1.0"
SITEMAP_URL = "https://medo.dev/blog/sitemap-posts.xml"
OUT_DIR = Path(__file__).resolve().parent.parent.parent / "blog-migration"


def parse_post_urls(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    urls: list[dict] = []
    for url_el in root.findall("sm:url", SITEMAP_NS):
        loc = url_el.findtext("sm:loc", default="", namespaces=SITEMAP_NS).strip()
        m = re.match(r"https?://medo\.dev/blog/(.+)/?", loc)
        if not m:
            continue
        path = m.group(1).strip("/")
        urls.append({"loc": loc, "path": path, "slug": path.split("/")[-1]})
    return urls


def fetch_url(url: str, timeout: int = 60) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main() -> int:
    posts = parse_post_urls(fetch_url(SITEMAP_URL))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    print(f"Exporting {len(posts)} posts → {OUT_DIR}")
    for i, post in enumerate(posts, 1):
        print(f"[{i}/{len(posts)}] {post['path']}", flush=True)
        try:
            html = fetch_url(post["loc"])
            result = export_from_html(html, post["loc"])
            meta = result["meta"]
            md_path = md_output_path(OUT_DIR, meta.get("url_path", post["path"]), post["slug"])
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(result["markdown"], encoding="utf-8")
        except (HTTPError, URLError, ValueError) as exc:
            errors.append(f"{post['loc']}: {exc}")
            print(f"  ERROR: {exc}", file=sys.stderr)
        if i < len(posts):
            time.sleep(1.0)

    print(f"Done: {len(posts) - len(errors)} ok, {len(errors)} failed")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
