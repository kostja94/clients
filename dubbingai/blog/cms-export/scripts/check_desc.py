import urllib.request
from pathlib import Path
from html import unescape
from bs4 import BeautifulSoup

slug = "jett-voice-changer"
url = f"https://dubbingai.io/blog/{slug}/"
html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})).read().decode()
soup = BeautifulSoup(html, "lxml")
live = unescape(soup.find("meta", attrs={"name": "description"})["content"])
local = ""
for line in (Path(__file__).resolve().parents[1] / f"{slug}.md").read_text(encoding="utf-8").splitlines():
    if line.startswith("description:"):
        local = line.split(":", 1)[1].strip().strip('"')
        break
print("LIVE:", live)
print("LOCAL:", local)
print("MATCH:", live == local)
