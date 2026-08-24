#!/usr/bin/env python3
"""
Apply URL fixes (Section 2 + Section 3 + Section 4 of the link audit) to all
content/tools/{en,zh}/*.json files.

Usage: python3 fix-urls.py

Section 2+3: Only updates linkUrl when it currently matches an old/broken pattern.
Section 4:   Unifies EN/ZH URLs where they differ only by www/path/trailing-slash.

Reports every change. Safe to re-run — already-fixed entries are skipped.
"""

import json
import glob
import os
from urllib.parse import urlparse

BASE = "/sessions/bold-inspiring-davinci/mnt/alignify-by-kostja"

# ── Section 2+3 fix definitions ──────────────────────────────────
FIXES: dict[tuple[str, str], str] = {
    ("wegic",              "wegic.com"):         "https://wegic.ai/",
    ("durable",            "durable.co"):         "https://durable.com/",
    ("windsurf",           "windsurf.com"):       "https://devin.ai/desktop",
    ("kling",              "klingai.com"):        "https://kling.ai/",
    ("producer",           "producer.ai"):        "https://www.flowmusic.app/",
    ("kiri-engine",        "kiriengine"):         "https://www.kiriengine.app/",

    ("1-more-shot",               "1moreshot"):         "https://www.onemoreshot.ai/",
    ("onemoreshot",               "1moreshot"):         "https://www.onemoreshot.ai/",
    ("aspireiq-influencer-marketing-platform", "aspireiq"):  "https://www.aspire.io/",
    ("artisan-ai-bdr-automation",  "tryartisan"):       "https://www.artisan.co/",
    ("aha-influencer-marketing-management", "aha.inc"):    "https://www.ahacreator.com/",
    ("bocha",                     "bochaai.com"):        "https://bocha.cn/",
    ("botika",                    "botika.io"):           "https://botika.com/",
    ("gloo",                      "gloo.us"):             "https://gloo.com/",
    ("known",                     "knownapp"):            "https://knownhq.com/",
    ("letta-open-source-memory-server", "letta.ai"):      "https://www.letta.com/",
    ("magnific",                  "magnific.ai"):         "https://www.magnific.com/",
    ("maxclaw",                   "agent.minimax.io"):    "https://agent.minimaxi.com/max-claw",
    ("outreach-sales-engagement-platform", "outreach.io"): "https://www.outreach.ai/",
    ("polycam",                   "polycam.ai"):          "https://poly.cam/",
    ("qwen-image-edit-alibaba",   "qwenlm"):              "https://chat.qwen.ai/",
    ("recall",                    "getrecall.ai"):        "https://www.recall.it/",
    ("rodin",                     "rodin.ai"):            "https://www.hyper3d.ai/",
    ("gwm-1",                     ""):                    "https://runwayml.com/solutions/industry/product-design",
    ("wan",                       "alibaba"):             "https://wan.video/",

    ("claude",            "claude.ai"):          "https://claude.com/",
    ("claude-ai",         "claude.ai"):          "https://claude.com/",
    ("claude-code",       "claude.ai"):          "https://claude.com/code",
    ("claude-engine",     "claude.ai"):          "https://claude.com/",
    ("claude-opus",       "claude.ai"):          "https://claude.com/",
    ("claude-sonnet",     "claude.ai"):          "https://claude.com/",

    ("ltx-studio",        "ltx.studio"):         "https://ltx.io/studio",
    ("ltx-studio",        "lightricks.com"):     "https://ltx.io/studio",

    ("mirage",            "mirage.app"):         "https://captions.ai/features/add-subtitles-to-videos",
}

# ── Section 4: EN/ZH URL unification ─────────────────────────────
SECTION4: dict[str, str] = {
    "apollo-io-ai-powered-sales-platform":       "https://www.apollo.io/",
    "brandmark":                                 "https://brandmark.io/",
    "clay-marketing-operations":                 "https://www.clay.com/",
    "favikon-influencer-analytics-tool":         "https://www.favikon.com/",
    "indexly":                                   "https://www.indexly.ai/",
    "lalal-ai":                                  "https://www.lalal.ai/",
    "lovo":                                      "https://lovo.ai/",
    "notta":                                     "https://www.notta.ai/en/",
    "remove-bg":                                 "https://www.remove.bg/",
    "voicemod":                                  "https://www.voicemod.net/",
    "voispark":                                  "https://voispark.com/",
    "betterpic":                                 "https://www.betterpic.io/",
    "seoclarity-ai-search-indexer":              "https://www.seoclarity.net/ai-seo/ai-search-indexer",
    "trysight":                                  "https://www.trysight.ai/",
    "upstudy":                                   "https://upstudy.ai/",
    "utell-ai":                                  "https://utell.ai/",
    "utopai-studios-cinematic-foundation-model": "https://www.utopaistudios.com/",
}


def core_domain(url: str) -> str:
    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    return netloc


def apply_fixes(filepath: str) -> list[str]:
    try:
        with open(filepath, 'rb') as f:
            raw = f.read().rstrip(b'\x00')
        data = json.loads(raw.decode('utf-8'))
    except Exception as exc:
        return [f"ERROR reading {os.path.basename(filepath)}: {exc}"]

    changes: list[str] = []
    modified = False

    for block in data.get('blocks', []):
        if block.get('type') != 'bestTools':
            continue
        for tool in block.get('tools', []):
            pid = tool.get('id', '')
            current = tool.get('linkUrl', '')

            # Section 2+3: pattern-match fixes
            for (fix_pid, old_pat), new_url in FIXES.items():
                if fix_pid != pid:
                    continue
                if old_pat:
                    if old_pat not in current:
                        continue
                if current == new_url:
                    continue
                changes.append(
                    f"  [S2/3] {os.path.basename(filepath)} [{pid}]: {current} → {new_url}"
                )
                tool['linkUrl'] = new_url
                current = new_url
                modified = True

            # Section 4: domain-match unification
            if pid in SECTION4:
                new_url = SECTION4[pid]
                if current == new_url:
                    continue
                cur_domain = core_domain(current)
                new_domain = core_domain(new_url)
                if cur_domain == new_domain:
                    changes.append(
                        f"  [S4] {os.path.basename(filepath)} [{pid}]: {current} → {new_url}"
                    )
                    tool['linkUrl'] = new_url
                    modified = True

    if modified:
        with open(filepath, 'wb') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8'))
            f.write(b'\n')

    return changes


def main() -> None:
    total_changes = 0
    total_files = 0
    for lang in ('en', 'zh'):
        for filepath in sorted(glob.glob(os.path.join(BASE, f'content/tools/{lang}/*.json'))):
            changes = apply_fixes(filepath)
            total_files += 1
            for c in changes:
                print(c)
                total_changes += 1
    print(f"\nScanned {total_files} files. Made {total_changes} URL update(s).")


if __name__ == '__main__':
    main()


