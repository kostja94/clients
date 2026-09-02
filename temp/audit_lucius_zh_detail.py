#!/usr/bin/env python3
"""Detailed English text extraction from lucius zh pages."""
import json
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
BASE = "https://luciusai.com"

PAGES = [
    "/zh", "/zh/features", "/zh/pricing", "/zh/roles", "/zh/discover", "/zh/profile",
    "/zh/customer-support", "/zh/customer-support/community", "/zh/customer-support/email",
    "/zh/community-moderation", "/zh/administrator",
    "/zh/channels", "/zh/channels/discord", "/zh/channels/telegram", "/zh/channels/feishu",
    "/zh/channels/website", "/zh/channels/slack", "/zh/channels/email", "/zh/channels/whatsapp",
    "/zh/features/knowledge", "/zh/features/customer-profile", "/zh/features/tasks",
    "/zh/features/data-analysis", "/zh/features/automation",
]

BRAND_OK = {
    "Lucius", "Lucius AI", "Discord", "Telegram", "Slack", "WhatsApp", "Lark", "Feishu",
    "ChatGPT", "Claude", "Gemini", "Perplexity", "Email", "Website", "EN", "AI", "KOL",
    "Utell", "Museon", "Jarsy", "FAQ", "DPA", "API", "CRM", "SaaS", "ROI", "GDPR",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (audit)"})
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")

def strip_tags(s):
    s = re.sub(r"<script[^>]*>.*?</script>", "", s, flags=re.I | re.S)
    s = re.sub(r"<style[^>]*>.*?</style>", "", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def latin_ratio(text):
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0
    return sum(1 for c in letters if ord(c) < 128) / len(letters)

def is_english_text(text, threshold=0.75):
    t = text.strip()
    if len(t) < 3:
        return False
    if t in BRAND_OK:
        return False
    # mostly ASCII words
    words = re.findall(r"[A-Za-z][A-Za-z'\-]{1,}", t)
    if len(words) >= 2 and latin_ratio(t) >= threshold:
        return True
    if len(words) == 1 and len(words[0]) >= 5 and latin_ratio(t) >= 0.9:
        return True
    return False

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

def extract_elements(html, pattern):
    return [strip_tags(m.group(1)) for m in re.finditer(pattern, html, re.I | re.S) if strip_tags(m.group(1))]

results = {}
for path in PAGES:
    url = BASE + path
    html = fetch(url)
    title = extract_meta(html, "title") or strip_tags(re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S).group(1))
    desc = extract_meta(html, "description")
    og_title = extract_meta(html, "og:title")
    og_desc = extract_meta(html, "og:description")

    nav = re.search(r"<nav[^>]*>(.*?)</nav>", html, re.I | re.S)
    footer = re.search(r"<footer[^>]*>(.*?)</footer>", html, re.I | re.S)
    nav_html = nav.group(1) if nav else ""
    footer_html = footer.group(1) if footer else ""

    body = re.search(r"<body[^>]*>(.*?)</body>", html, re.I | re.S).group(1)
    body_only = body
    body_only = re.sub(r"<nav[^>]*>.*?</nav>", " ", body_only, flags=re.I | re.S)
    body_only = re.sub(r"<footer[^>]*>.*?</footer>", " ", body_only, flags=re.I | re.S)

    nav_links = extract_elements(nav_html, r'<(?:a|button)[^>]*>(.*?)</(?:a|button)>')
    footer_links = extract_elements(footer_html, r'<(?:a|button|p)[^>]*class="[^"]*(?:footer|drop)[^"]*"[^>]*>(.*?)</(?:a|button|p)>')
    footer_all = extract_elements(footer_html, r'<(?:a|button|p)[^>]*>(.*?)</(?:a|button|p)>')

    headings = extract_elements(body_only, r'<h[1-6][^>]*>(.*?)</h[1-6]>')
    paras = extract_elements(body_only, r'<p[^>]*>(.*?)</p>')
    lis = extract_elements(body_only, r'<li[^>]*>(.*?)</li>')
    btns = extract_elements(body_only, r'<(?:button|a)[^>]*class="[^"]*(?:btn|button|cta)[^"]*"[^>]*>(.*?)</(?:button|a)>')
    # also mailto/demo links
    btns += extract_elements(body_only, r'<a[^>]*href="[^"]*(?:mailto|demo|signup|contact)[^"]*"[^>]*>(.*?)</a>')

    def filter_en(items):
        seen = set()
        out = []
        for x in items:
            x = x.strip()
            if not x or x in seen:
                continue
            if is_english_text(x):
                seen.add(x)
                out.append(x)
        return out

    results[path] = {
        "meta_en": {k: v for k, v in {
            "title": title, "description": desc, "og:title": og_title, "og:description": og_desc
        }.items() if v and is_english_text(v)},
        "nav_en": filter_en(nav_links),
        "footer_en": filter_en(footer_all),
        "headings_en": filter_en(headings),
        "paragraphs_en": filter_en(paras)[:8],
        "bullets_en": filter_en(lis)[:10],
        "cta_en": filter_en(btns),
    }
    print(path, "done")

with open(r"e:\clients\temp\lucius_zh_audit_detail.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
