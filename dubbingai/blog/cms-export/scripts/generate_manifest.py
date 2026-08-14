#!/usr/bin/env python3
"""Generate manifest.csv from the URL list in the agent transcript."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPT = Path(
    r"C:\Users\zyjst\.cursor\projects\d-clients\agent-transcripts"
    r"\92f6e401-a31a-4282-aa3d-ea67b3aa755d"
    r"\92f6e401-a31a-4282-aa3d-ea67b3aa755d.jsonl"
)
MANIFEST = ROOT / "manifest.csv"

P0_SLUGS = {
    "dubbing-ai-vs-voicemod",
    "how-to-get-voice-changer-on-discord",
    "jett-voice-changer",
    "minecraft-soundboard",
    "dubbing-ai-trump-voice",
}

SUPERSEDED = {
    "top-5-voice-changers": "best-ai-voice-changer",
    "top-10-free-voice-changer-online-2025": "best-ai-voice-changer",
}

SKIP_SLUGS = {"hello-world"}

PT_SLUGS = {"os-5-melhores-modificadores"}


def load_urls() -> list[str]:
    for line in TRANSCRIPT.read_text(encoding="utf-8").splitlines():
        if "how-to-use-okada-voice-changer" not in line:
            continue
        obj = json.loads(line)
        text = obj["message"]["content"][0]["text"]
        urls = re.findall(r"https://dubbingai\.io/blog/[^\s\)\]]+", text)
        urls = [u.rstrip("/") + "/" for u in urls]
        return list(dict.fromkeys(urls))
    raise RuntimeError("URL list not found in transcript")


def is_article(url: str) -> bool:
    path = url.replace("https://dubbingai.io/blog/", "").strip("/")
    if not path:
        return False
    if path.startswith("category/") or path.startswith("author/"):
        return False
    if "%" in path:
        return False
    return True


def assign_batch(slug: str) -> str:
    if slug in P0_SLUGS:
        return "P0"
    s = slug.lower()
    if any(k in s for k in ("dubbing-ai", "voice-changer", "discord", "valorant", "fortnite")):
        return "P1"
    if any(k in s for k in ("soundboard", "sound-effect", "meme", "soundbutton", "sfx")):
        return "P2"
    return "P3"


def notes_for(slug: str) -> str:
    if slug in SKIP_SLUGS:
        return "WordPress 默认稿"
    if slug in SUPERSEDED:
        return f"301→{SUPERSEDED[slug]}"
    if slug in PT_SLUGS:
        return "葡语稿"
    return ""


def main() -> None:
    rows = []
    for url in load_urls():
        if not is_article(url):
            continue
        slug = url.replace("https://dubbingai.io/blog/", "").strip("/")
        status = "skip" if slug in SKIP_SLUGS else "pending"
        rows.append(
            {
                "slug": slug,
                "url": url,
                "category": "",
                "lang": "pt" if slug in PT_SLUGS else "en",
                "status": status,
                "date_published": "",
                "migrated_at": "",
                "notes": notes_for(slug),
                "superseded_by": SUPERSEDED.get(slug, ""),
                "batch": assign_batch(slug),
            }
        )

    fieldnames = [
        "slug",
        "url",
        "category",
        "lang",
        "status",
        "date_published",
        "migrated_at",
        "notes",
        "superseded_by",
        "batch",
    ]
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {len(rows)} rows to {MANIFEST}")
    from collections import Counter

    print("By batch:", dict(Counter(r["batch"] for r in rows)))
    print("Skip:", sum(1 for r in rows if r["status"] == "skip"))


if __name__ == "__main__":
    main()
