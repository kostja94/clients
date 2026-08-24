#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict

LINK_RE = re.compile(r"\[([^\]]*)\]\((/blog/[^)]+)\)")
BAD_ANCHOR = re.compile(r"click here|learn more|this article", re.I)
SKIP = {"README.md", "blog-structure-internal-links.md", "blog-article-backlog.md", "_link_audit.py"}

articles = [
    p for p in Path(".").rglob("*.md")
    if p.name not in SKIP and "_link_audit" not in p.name
]

inbound = defaultdict(set)
issues = []

for p in sorted(articles):
    text = p.read_text(encoding="utf-8")
    body = text.split("---", 2)[2] if text.startswith("---") else text
    lines = body.splitlines()

    tldr_start = tldr_end = faq_start = None
    for idx, line in enumerate(lines):
        if line.strip() == "## TL;DR":
            tldr_start = idx
        elif tldr_start is not None and tldr_end is None and line.startswith("## ") and line.strip() != "## TL;DR":
            tldr_end = idx
        if line.strip() == "## Frequently asked questions":
            faq_start = idx

    if tldr_start is not None and tldr_end is None:
        tldr_end = faq_start if faq_start is not None else len(lines)

    slug_counts = defaultdict(int)
    unique_blog = set()

    for idx, line in enumerate(lines):
        for anchor, url in LINK_RE.findall(line):
            slug_counts[url] += 1
            unique_blog.add(url)
            inbound[url].add(p.as_posix())

            if BAD_ANCHOR.search(anchor):
                issues.append(f"R2_BAD_ANCHOR {p.name}:{idx+1} [{anchor}] -> {url}")

            in_tldr = tldr_start is not None and tldr_start <= idx < (tldr_end or len(lines))
            in_faq = faq_start is not None and idx >= faq_start
            if in_tldr:
                issues.append(f"R4_TLDR {p.name}:{idx+1} -> {url}")
            if in_faq:
                issues.append(f"R4_FAQ {p.name}:{idx+1} -> {url}")

    if len(unique_blog) < 2:
        issues.append(f"R1_LOW {p.name} unique_blog={len(unique_blog)}")

    for url, cnt in slug_counts.items():
        if cnt > 2:
            issues.append(f"R3_DUP {p.name} {url} x{cnt}")

# R7 Pillar
pillar = Path("creator-affiliate/01-how-to-make-money-on-tiktok.md")
if pillar.exists():
    body = pillar.read_text(encoding="utf-8").split("---", 2)[2]
    required = [
        "tiktok-shop-setup", "faceless-tiktok-shop-videos", "tiktok-product-research",
        "tiktok-video-hooks", "tiktok-captions-hashtags", "tiktok-affiliate-side-hustle",
        "tiktok-shop-no-sales", "tiktok-shop-influencer-marketing",
    ]
    for s in required:
        if f"/blog/{s}" not in body:
            issues.append(f"R7_MISSING #01 -> /blog/{s}")

all_slugs = set()
for p in articles:
    m = re.search(r'^slug:\s*"(/blog/[^"]+)"', p.read_text(encoding="utf-8"), re.M)
    if m:
        all_slugs.add(m.group(1))

zero_in, one_in = [], []
for slug in sorted(all_slugs):
    n = len(inbound.get(slug, set()))
    name = slug.replace("/blog/", "")
    if n == 0:
        zero_in.append(name)
    elif n == 1:
        one_in.append(name)

print("ARTICLES", len(articles))
print("\n=== R1 (<2 outbound) ===")
for x in [i for i in issues if i.startswith("R1")]:
    print(x)
if not [i for i in issues if i.startswith("R1")]:
    print("PASS (all >=2)")

print("\n=== R3 (>2 same slug) ===")
r3 = [i for i in issues if i.startswith("R3")]
for x in r3[:25]:
    print(x)
print(f"total R3: {len(r3)}")

print("\n=== R4 TL;DR/FAQ ===")
r4 = [i for i in issues if i.startswith("R4")]
for x in r4[:25]:
    print(x)
print(f"total R4: {len(r4)}")

print("\n=== R2 bad anchor ===")
for x in [i for i in issues if i.startswith("R2")]:
    print(x)
if not [i for i in issues if i.startswith("R2")]:
    print("PASS")

print("\n=== R7 Pillar ===")
for x in [i for i in issues if i.startswith("R7")]:
    print(x)
if not [i for i in issues if i.startswith("R7")]:
    print("PASS")

print(f"\n=== Zero inbound ({len(zero_in)}) ===")
print(", ".join(zero_in))

print(f"\n=== One inbound ({len(one_in)}) ===")
print(", ".join(one_in))

seasonal_slugs = [
    s for s in all_slugs
    if any(k in s for k in [
        "labor-day", "september-restock", "back-to-school", "black-friday",
        "holiday-gifts", "halloween", "fall-deals", "jumpstart", "summer-sale",
    ])
]
print("\n=== Cluster F spokes: inbound from outside seasonal-campaign/ ===")
for slug in sorted(seasonal_slugs):
    sources = inbound.get(slug, set())
    ext = [s for s in sources if "seasonal-campaign/" not in s]
    print(f"  {slug.replace('/blog/', '')}: total={len(sources)} external={len(ext)}")

# Matrix gaps: content-graph weak list
weak = [
    "tiktok-shop-influencer-marketing", "tiktok-two-step-verification",
    "tiktok-shop-domestic-seller", "how-to-shop-on-tiktok-shop", "how-to-use-tiktok-trends",
]
print("\n=== Known weak slugs (content-graph) inbound count ===")
for name in weak:
    slug = f"/blog/{name}"
    print(f"  {name}: {len(inbound.get(slug, set()))}")
