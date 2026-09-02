#!/usr/bin/env python3
"""Audit luciusai.com /zh/blog pages for localization."""
import json
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
BASE = "https://luciusai.com"

NAV_FOOTER_EN = [
    "Agents", "Lucius Agents", "Customer Support", "Community Operator", "Moderator",
    "Email Assistant", "Discover", "Website", "Discord", "Slack", "Telegram", "Lark",
    "Email", "WhatsApp", "Utell", "Museon", "Jarsy", "Features", "Pricing", "Book",
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (audit)"})
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")


def strip_tags(s):
    s = re.sub(r"<script[^>]*>.*?</script>", "", s, flags=re.I | re.S)
    s = re.sub(r"<style[^>]*>.*?</style>", "", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def extract_meta(html, name):
    for pat in [
        rf'<meta[^>]+name=["\']{name}["\'][^>]+content=["\']([^"\']+)["\']',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']{name}["\']',
        rf'<meta[^>]+property=["\']{name}["\'][^>]+content=["\']([^"\']+)["\']',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']{name}["\']',
    ]:
        m = re.search(pat, html, re.I)
        if m:
            return m.group(1).strip()
    return None


def extract_section(html, tag):
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.I | re.S)
    return m.group(1) if m else ""


def is_mostly_english(text):
    if not text or len(text) < 3:
        return False
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return False
    latin = sum(1 for c in letters if ord(c) < 128)
    return latin / len(letters) > 0.85


def english_prefix_title(title):
    """Detect English-leading titles like 'How to X：中文'."""
    if not title:
        return False
    if re.match(r"^[A-Za-z][A-Za-z0-9 ,\-']{8,}[：:]", title):
        return True
    if is_mostly_english(title):
        return True
    return False


def find_nav_footer_en(text):
    found = []
    for p in NAV_FOOTER_EN:
        if re.search(rf"\b{re.escape(p)}\b", text):
            found.append(p)
    return found


def count_english_paragraphs(body_text):
    paras = [p.strip() for p in re.split(r"\n{2,}|</p>", body_text) if len(p.strip()) > 40]
    en = sum(1 for p in paras if is_mostly_english(p))
    return en, len(paras)


# Get all blog slugs from listing
listing_html = fetch(f"{BASE}/zh/blog")
slugs = sorted(set(re.findall(r'href="/zh/blog/([^"/?#]+)"', listing_html)))
print(f"Found {len(slugs)} blog slugs")

listing_title = extract_meta(listing_html, "title") or ""
listing_desc = extract_meta(listing_html, "description") or ""
listing_nav = strip_tags(extract_section(listing_html, "nav"))
listing_footer = strip_tags(extract_section(listing_html, "footer"))

# Parse listing card titles from markdown-like structure isn't in HTML - use h2/h3
listing_headings = [strip_tags(h) for h in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", listing_html, re.I | re.S)]

results = {
    "listing": {
        "url": f"{BASE}/zh/blog",
        "meta_title": listing_title,
        "meta_description": listing_desc,
        "nav_en": find_nav_footer_en(listing_nav),
        "footer_en": find_nav_footer_en(listing_footer),
        "nav_text": listing_nav[:600],
        "footer_text": listing_footer[:600],
        "article_count": len(slugs),
    },
    "articles": {},
}

en_title_slugs = []
fully_zh = []
mixed = []

for slug in slugs:
    url = f"{BASE}/zh/blog/{slug}"
    try:
        html = fetch(url)
        title = extract_meta(html, "title") or ""
        desc = extract_meta(html, "description") or ""
        og_title = extract_meta(html, "og:title") or ""
        h1 = strip_tags((re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S) or [None, ""])[1])
        nav = strip_tags(extract_section(html, "nav"))
        footer = strip_tags(extract_section(html, "footer"))
        body = strip_tags(re.sub(r"<nav[^>]*>.*?</nav>", " ", html, flags=re.I | re.S))
        body = strip_tags(re.sub(r"<footer[^>]*>.*?</footer>", " ", body, flags=re.I | re.S))
        headings = [strip_tags(h) for h in re.findall(r"<h[2-6][^>]*>(.*?)</h[2-6]>", html, re.I | re.S)]
        en_headings = [h for h in headings if is_mostly_english(h) and len(h) > 5]

        # TL;DR check - body english ratio heuristic
        words = re.findall(r"[\u4e00-\u9fff]|[A-Za-z]+", body)
        zh_words = sum(1 for w in words if re.match(r"[\u4e00-\u9fff]", w))
        en_words = sum(1 for w in words if re.match(r"[A-Za-z]", w))
        total = zh_words + en_words or 1
        zh_ratio = zh_words / total

        status = "fully_zh"
        if zh_ratio < 0.5:
            status = "mostly_en"
        elif english_prefix_title(h1) or english_prefix_title(title):
            status = "mixed_title"
        elif en_headings and len(en_headings) > 3:
            status = "mixed_body"
        elif zh_ratio < 0.75:
            status = "mixed_terms"

        if english_prefix_title(h1):
            en_title_slugs.append(slug)

        if status == "fully_zh":
            fully_zh.append(slug)
        else:
            mixed.append(slug)

        results["articles"][slug] = {
            "url": url,
            "meta_title": title,
            "meta_description": desc[:200],
            "h1": h1,
            "title_mixed_en": english_prefix_title(h1),
            "nav_en": find_nav_footer_en(nav),
            "footer_en": find_nav_footer_en(footer),
            "en_headings": en_headings[:8],
            "zh_ratio": round(zh_ratio, 3),
            "status": status,
        }
        print(f"OK {slug} ({status})", flush=True)
    except Exception as e:
        results["articles"][slug] = {"url": url, "error": str(e)}
        print(f"ERR {slug}: {e}", flush=True)

results["summary"] = {
    "total": len(slugs),
    "en_title_prefix_count": len(en_title_slugs),
    "en_title_slugs": en_title_slugs,
    "fully_zh_count": len(fully_zh),
    "mixed_count": len(mixed),
    "coverage_pct": round(len(fully_zh) / len(slugs) * 100, 1) if slugs else 0,
}

out = r"e:\clients\temp\lucius_zh_blog_audit.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"Wrote {out}")
print(json.dumps(results["summary"], ensure_ascii=False, indent=2))
