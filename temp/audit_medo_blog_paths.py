#!/usr/bin/env python3
import re
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
UA = "MeDoAudit/1.0"


def fetch(url: str, max_bytes: int = 80000) -> tuple[str, str, int]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as resp:
        final = resp.geturl()
        code = resp.status
        body = resp.read(max_bytes).decode("utf-8", errors="replace")
    return body, final, code


def sitemap_urls(url: str) -> list[str]:
    body, _, _ = fetch(url, max_bytes=2_000_000)
    root = ET.fromstring(body)
    return [
        u.findtext("sm:loc", default="", namespaces=NS).strip()
        for u in root.findall("sm:url", NS)
        if u.findtext("sm:loc", default="", namespaces=NS)
    ]


def blog_links(html: str) -> set[str]:
    return set(re.findall(r'href="([^"]*(?:/blog|/blogs)[^"]*)"', html, flags=re.I))


def head_status(url: str) -> str:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return str(resp.status)
    except urllib.error.HTTPError as exc:
        return str(exc.code)
    except Exception as exc:
        return f"ERR:{exc.__class__.__name__}"


def main() -> None:
    checks = [
        "https://medo.dev/blog/",
        "https://medo.dev/blogs/",
        "https://miaoda.io/blog/",
        "https://miaoda.io/blogs/",
    ]
    print("=== INDEX PAGES ===")
    for url in checks:
        try:
            html, final, code = fetch(url)
            links = sorted(blog_links(html))
            print(f"{url} -> {final} [{code}] blog links: {len(links)}")
            for link in links[:8]:
                print(f"  {link}")
            if len(links) > 8:
                print("  ...")
        except Exception as exc:
            print(f"{url} FAILED: {exc}")

    print("\n=== SITEMAPS ===")
    for url in [
        "https://medo.dev/blog/sitemap-posts.xml",
        "https://medo.dev/blog/sitemap.xml",
    ]:
        try:
            locs = sitemap_urls(url)
            print(f"{url}: {len(locs)} urls")
            blogs = [l for l in locs if "/blogs/" in l]
            blog = [l for l in locs if "/blog/" in l and "/blogs/" not in l]
            print(f"  /blog/*: {len(blog)}, /blogs/*: {len(blogs)}")
        except Exception as exc:
            print(f"{url} FAILED: {exc}")

    print("\n=== SAMPLE /blogs ARTICLE STATUS (miaoda.io) ===")
    sample_slugs = [
        "what-is-vibe-coding",
        "how-to-build-mobile-app-with-ai",
        "best-ai-mobile-app-builders",
    ]
    for slug in sample_slugs:
        for prefix in ["https://miaoda.io/blogs/", "https://medo.dev/blog/", "https://medo.dev/blogs/"]:
            url = prefix + slug + "/"
            print(f"  {url} -> {head_status(url)}")


if __name__ == "__main__":
    main()
