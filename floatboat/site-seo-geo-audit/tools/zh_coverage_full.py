#!/usr/bin/env python3
"""Expanded zh coverage audit for floatboat.ai — 2026-08-25."""

from __future__ import annotations

import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://floatboat.ai"
SITEMAP = f"{BASE}/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
UA = "FloatboatAuditBot/1.0"

# Product landings from page-composition-guide + site structure
PRODUCT_LANDINGS = [
    "/coworker",
    "/ai-file-organizer",
    "/ai-scheduling-assistant",
    "/floatim",
    "/skills-marketplace",
    "/ai-agent-workspace",
    "/ai-workspace-for-consultants",
    "/nano-banana2",
    "/marketplace",
    "/showcases",
]

T0_CORE = ["/", "/about", "/pricing", "/download", "/combostore", "/blog", "/app", "/wishlist"]
T1 = [
    "/integrations",
    "/models",
    "/use-cases",
    "/use-cases/for-solopreneur",
    "/use-cases/for-creators",
    "/use-cases/for-small-business",
    "/use-cases/for-studio",
    "/use-cases/one-person-company",
    "/alternatives",
    "/alternatives/notion-alternative",
    "/alternatives/chatgpt-alternative",
    "/alternatives/cursor-alternative",
    "/alternatives/n8n-alternative",
]
LEGAL = ["/privacy", "/terms", "/user-protection-program-terms"]
FUNNEL = ["/download/success", "/timeshop"]


def fetch_sitemap_paths() -> list[str]:
    req = urllib.request.Request(SITEMAP, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as resp:
        xml = resp.read().decode("utf-8", errors="replace")
    root = ET.fromstring(xml)
    paths: list[str] = []
    for loc in root.findall(".//sm:loc", NS):
        if loc.text:
            url = loc.text.strip()
            if url.startswith(BASE):
                paths.append(url[len(BASE) :] or "/")
    return sorted(set(paths))


def classify(path: str, cn_ratio: float, status: int | str) -> str:
    if status != 200:
        return "missing_404"
    if cn_ratio >= 0.35:
        return "localized"
    if cn_ratio >= 0.08:
        return "partial"
    return "english_fallback"


def fetch(path: str) -> dict:
    url = BASE + path
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"},
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            status = resp.status
    except Exception as exc:  # noqa: BLE001
        return {"path": path, "status": "error", "error": str(exc), "state": "missing_404"}

    title_m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = re.sub(r"\s+", " ", title_m.group(1).strip()) if title_m else ""
    h1_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    h1 = re.sub(r"<[^>]+>", "", h1_m.group(1)).strip() if h1_m else ""

    text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.I | re.S)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    cn = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    cn_ratio = round(cn / (cn + latin), 3) if (cn + latin) else 0

    hreflang = len(re.findall(r'hreflang=', html, re.I))
    state = classify(path, cn_ratio, status)

    return {
        "path": path,
        "status": status,
        "title": title[:100],
        "h1": h1[:100],
        "cn_ratio": cn_ratio,
        "hreflang": hreflang,
        "state": state,
    }


def zh_for(en_path: str) -> str:
    return "/zh" if en_path == "/" else "/zh" + en_path


def main() -> None:
    sitemap_paths = fetch_sitemap_paths()

    en_targets = sorted(
        set(
            T0_CORE
            + PRODUCT_LANDINGS
            + T1
            + LEGAL
            + FUNNEL
            + [p for p in sitemap_paths if p.startswith("/blog/")][:15]  # sample blog
        )
    )

    # All zh paths to probe
    zh_targets = sorted({zh_for(p) for p in en_targets} | {"/zh/blog"})

    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = [pool.submit(fetch, p) for p in zh_targets]
        for fut in as_completed(futs):
            results.append(fut.result())

    results.sort(key=lambda x: x["path"])

    summary: dict[str, list[str]] = {}
    for r in results:
        summary.setdefault(r.get("state", "error"), []).append(r["path"])

    out = {
        "audit_date": "2026-08-25",
        "sitemap_total": len(sitemap_paths),
        "sitemap_zh_count": sum(1 for p in sitemap_paths if p.startswith("/zh")),
        "zh_probed": len(results),
        "summary_counts": {k: len(v) for k, v in summary.items()},
        "summary_paths": summary,
        "pages": results,
        "en_product_landings": PRODUCT_LANDINGS,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
