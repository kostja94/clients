#!/usr/bin/env python3
"""Compare local cms-export md vs live CMS page content."""
from __future__ import annotations

import re
import urllib.request
from html import unescape
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = [
    "jett-voice-changer",
    "dubbing-ai-vs-voicemod",
    "minecraft-soundboard",
    "how-to-get-voice-changer-on-discord",
    "top-5-wah-wah-wah-sound-effect-sites",
]

USER_AGENT = "Mozilla/5.0 (compatible; DubbingAICMSExport/1.0)"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    block = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    data = {}
    for line in block.splitlines():
        m = re.match(r'^(\w+):\s*"?([^"]*)"?$', line)
        if m:
            data[m.group(1)] = m.group(2).strip()
    return data, body


def fetch_live(slug: str) -> dict:
    url = f"https://dubbingai.io/blog/{slug}/"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", errors="replace")
    soup = BeautifulSoup(html, "lxml")

    title = ""
    og = soup.find("meta", property="og:title")
    if og and og.get("content"):
        title = unescape(og["content"].strip())
        title = re.sub(r"\s*[|\-–—]\s*Dubbing AI.*$", "", title, flags=re.I).strip()

    desc = ""
    md = soup.find("meta", attrs={"name": "description"})
    if md and md.get("content"):
        desc = unescape(md["content"].strip())

    node = soup.select_one(".entry-content") or soup.select_one(".post-content")
    if not node:
        raise ValueError("no entry-content")
    for bad in node.select(".blogbuster-related-posts-wrapper, nav, .post-navigation"):
        bad.decompose()

    text = re.sub(r"\s+", " ", node.get_text(" ", strip=True))
    h2s = [unescape(h.get_text(strip=True)) for h in node.find_all("h2")]
    h3_count = len(node.find_all("h3"))
    paras = [p.get_text(strip=True) for p in node.find_all("p") if p.get_text(strip=True)]

    return {
        "url": url,
        "title": title,
        "description": desc,
        "char_count": len(text),
        "h2_count": len(h2s),
        "h2_titles": h2s,
        "h3_count": h3_count,
        "para_count": len(paras),
        "first_para": paras[0][:200] if paras else "",
        "last_para": paras[-1][:200] if paras else "",
    }


def parse_local(slug: str) -> dict:
    path = ROOT / f"{slug}.md"
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    plain = re.sub(r"[#*_>`\[\]()!|-]", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    h2s = [m.group(1).strip() for m in re.finditer(r"^## (.+)$", body, re.M)]
    h3_count = len(re.findall(r"^### ", body, re.M))
    paras = [p.strip() for p in re.split(r"\n\n+", body) if p.strip() and not p.startswith("#")]

    return {
        "title": fm.get("title", ""),
        "description": fm.get("description", ""),
        "char_count": len(plain),
        "h2_count": len(h2s),
        "h2_titles": h2s,
        "h3_count": h3_count,
        "para_count": len(paras),
        "first_para": paras[0][:200] if paras else "",
        "last_para": paras[-1][:200] if paras else "",
    }


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower().strip())


def compare(slug: str) -> dict:
    live = fetch_live(slug)
    local = parse_local(slug)
    issues = []

    if norm(live["title"]) != norm(local["title"]):
        issues.append(f"title mismatch: live={live['title'][:60]!r} local={local['title'][:60]!r}")

    if norm(live["description"]) != norm(local["description"]):
        issues.append("description mismatch")

    if abs(live["h2_count"] - local["h2_count"]) > 0:
        issues.append(f"h2 count: live={live['h2_count']} local={local['h2_count']}")

    if abs(live["h3_count"] - local["h3_count"]) > 1:
        issues.append(f"h3 count: live={live['h3_count']} local={local['h3_count']}")

    ratio = local["char_count"] / max(live["char_count"], 1)
    if ratio < 0.85 or ratio > 1.15:
        issues.append(f"text length ratio local/live={ratio:.2f} (live={live['char_count']} local={local['char_count']})")

    live_fp = norm(re.sub(r"[^\w\s]", "", live["first_para"])[:120])
    local_fp = norm(re.sub(r"[^\w\s]", "", local["first_para"])[:120])
    if live_fp[:80] not in local_fp and local_fp[:80] not in live_fp:
        issues.append("first paragraph diverges")

    h2_match = sum(
        1 for a, b in zip(live["h2_titles"], local["h2_titles"]) if norm(a) == norm(b)
    )
    if live["h2_count"] and h2_match < live["h2_count"]:
        issues.append(f"h2 titles matched {h2_match}/{live['h2_count']}")

    return {
        "slug": slug,
        "ok": len(issues) == 0,
        "issues": issues,
        "live": live,
        "local": local,
    }


def main() -> None:
    for slug in SAMPLES:
        print(f"\n{'='*60}\n{slug}\n{'='*60}")
        try:
            r = compare(slug)
            status = "PASS" if r["ok"] else "DIFF"
            print(f"Result: {status}")
            print(f"  title: {r['local']['title'][:70]}")
            print(f"  H2: live={r['live']['h2_count']} local={r['local']['h2_count']}")
            print(f"  H3: live={r['live']['h3_count']} local={r['local']['h3_count']}")
            print(f"  chars(plain): live={r['live']['char_count']} local={r['local']['char_count']}")
            if r["issues"]:
                for i in r["issues"]:
                    print(f"  ! {i}")
            if r["live"]["h2_titles"]:
                print("  H2 live:", r["live"]["h2_titles"][:3], "..." if len(r["live"]["h2_titles"]) > 3 else "")
                print("  H2 local:", r["local"]["h2_titles"][:3], "..." if len(r["local"]["h2_titles"]) > 3 else "")
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
