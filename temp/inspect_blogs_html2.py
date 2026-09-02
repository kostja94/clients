#!/usr/bin/env python3
import re
import urllib.request

url = "https://medo.dev/blogs/what-is-vibe-coding"
req = urllib.request.Request(url, headers={"User-Agent": "MeDoAudit/1.0"})
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode("utf-8", errors="replace")

# BlogPosting JSON-LD
for m in re.finditer(r'<script type="application/ld\+json">(\{.*?\})</script>', html, re.S):
    if "BlogPosting" in m.group(1):
        print("=== BlogPosting JSON ===")
        print(m.group(1)[:2500])
        break

# article inner structure - find h2 tags
article = re.search(r"<article>([\s\S]*)</article>", html)
if article:
    body = article.group(1)
    classes = sorted(set(re.findall(r'class="([^"]+)"', body)))
    print("\n=== article classes (sample) ===")
    for c in classes[:30]:
        print(c)
    h2s = re.findall(r"<h2[^>]*>([^<]+)", body)
    print("\n=== h2 headings ===")
    for h in h2s[:8]:
        print(h.strip())
