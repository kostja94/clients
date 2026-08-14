#!/usr/bin/env python3
"""One-off inspect; used to find content selectors."""
import json
import re
import urllib.request

url = "https://dubbingai.io/blog/jett-voice-changer/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="replace")
print("len", len(html))
for pat in ["Jett Voice", "jett-voice", "__NEXT_DATA__", "application/ld+json", "wp-content", "blogbuster"]:
    print(pat, html.find(pat) if pat != "application/ld+json" else html.find("ld+json"))

for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL):
    try:
        data = json.loads(m.group(1))
        t = data.get("@type") if isinstance(data, dict) else None
        if t in ("Article", "BlogPosting", "NewsArticle"):
            print("LD headline:", data.get("headline", "")[:100])
            print("date:", data.get("datePublished"))
    except Exception as e:
        pass

# Try article tag content length
from html.parser import HTMLParser

class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_entry = False
        self.depth = 0
        self.chunks = []

    def handle_starttag(self, tag, attrs):
        cls = dict(attrs).get("class", "")
        if "entry-content" in cls or "post-content" in cls:
            self.in_entry = True
            self.depth = 1
        elif self.in_entry:
            self.depth += 1

    def handle_endtag(self, tag):
        if self.in_entry:
            self.depth -= 1
            if self.depth <= 0:
                self.in_entry = False

    def handle_data(self, data):
        if self.in_entry and data.strip():
            self.chunks.append(data.strip())

p = Extract()
p.feed(html)
print("entry-content text chunks:", len(p.chunks))
if p.chunks:
    print("first:", p.chunks[0][:120])
