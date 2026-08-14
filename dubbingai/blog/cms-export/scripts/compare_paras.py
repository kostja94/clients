#!/usr/bin/env python3
import re, urllib.request
from pathlib import Path
from html import unescape
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
UA = {"User-Agent": "Mozilla/5.0"}

def live_body_start(slug):
    url = f"https://dubbingai.io/blog/{slug}/"
    html = urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read().decode()
    node = BeautifulSoup(html, "lxml").select_one(".entry-content")
    paras = [p.get_text(strip=True) for p in node.find_all("p") if p.get_text(strip=True)]
    return paras[0][:180], paras[1][:180] if len(paras)>1 else ""

def local_body_start(slug):
    text = (ROOT/f"{slug}.md").read_text(encoding="utf-8")
    body = text.split("---", 2)[2]
    paras = []
    for block in re.split(r"\n\n+", body):
        block = block.strip()
        if block.startswith("#") or block.startswith("!["):
            continue
        if block.startswith("**[DOWNLOAD") or block == "The Best AI Voice Changer with soundboard":
            continue
        plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", block)
        plain = re.sub(r"\*\*", "", plain)
        if plain.strip():
            paras.append(plain.strip()[:180])
    return paras[0] if paras else "", paras[1] if len(paras)>1 else ""

for slug in ["jett-voice-changer", "dubbing-ai-vs-voicemod", "minecraft-soundboard", "how-to-get-voice-changer-on-discord"]:
    lp1, lp2 = local_body_start(slug)
    wp1, wp2 = live_body_start(slug)
    print(f"\n=== {slug} ===")
    print("LIVE P1:", wp1)
    print("LOCAL P1:", lp1)
    print("P1 match:", wp1[:100] == lp1[:100] or wp1[:80] in lp1)
    if wp2:
        print("LIVE P2:", wp2[:100])
        print("LOCAL P2:", lp2[:100])
        print("P2 match:", wp2[:80] in lp2 or lp2[:80] in wp2)
