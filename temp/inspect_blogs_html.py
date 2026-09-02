#!/usr/bin/env python3
import re
import urllib.request

url = "https://medo.dev/blogs/what-is-vibe-coding"
req = urllib.request.Request(url, headers={"User-Agent": "MeDoAudit/1.0"})
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode("utf-8", errors="replace")

for token in ["article", "prose", "gh-content", "blog-content", "BlogPosting", "ld+json"]:
    print(f"{token}: {token.lower() in html.lower()}")

for pattern in [
    r'<script type="application/ld\+json">([\s\S]{0,2000})',
    r'<article[^>]*>([\s\S]{0,500})',
    r'class="[^"]*prose[^"]*"[^>]*>([\s\S]{0,300})',
]:
    m = re.search(pattern, html, re.I)
    if m:
        print("\n=== MATCH", pattern[:40], "===")
        print(m.group(0)[:1200])
