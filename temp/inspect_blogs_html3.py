#!/usr/bin/env python3
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("no bs4")
    raise

import re
import urllib.request

url = "https://medo.dev/blogs/what-is-vibe-coding"
req = urllib.request.Request(url, headers={"User-Agent": "MeDoAudit/1.0"})
with urllib.request.urlopen(req, timeout=30) as resp:
    html = resp.read().decode("utf-8", errors="replace")

soup = BeautifulSoup(html, "html.parser")
article = soup.find("article")
if not article:
    raise SystemExit("no article")

# find content area - likely div with leading-[1.8]
candidates = article.find_all("div", class_=re.compile(r"leading-\[1\.8\]"))
print("leading candidates:", len(candidates))
for i, c in enumerate(candidates):
    text = c.get_text(" ", strip=True)[:120]
    print(i, text)

# also try md:col-span-9
cols = article.find_all("div", class_=re.compile(r"md:col-span-9"))
print("\ncol-span-9:", len(cols))
for i, c in enumerate(cols):
    print(i, "children", len(list(c.children)), "text len", len(c.get_text()))

if cols:
    content = cols[0]
    print("\nfirst p:", content.find("p").get_text()[:200] if content.find("p") else "none")
