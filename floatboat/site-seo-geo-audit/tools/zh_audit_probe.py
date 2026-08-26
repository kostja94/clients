#!/usr/bin/env python3
"""Probe /zh/ pages vs EN for translation coverage."""

from __future__ import annotations

import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "https://floatboat.ai"

EN_PATHS = [
    "/",
    "/about",
    "/pricing",
    "/download",
    "/combostore",
    "/blog",
    "/marketplace",
    "/ai-scheduling-assistant",
    "/ai-agent-workspace",
    "/ai-workspace-for-consultants",
    "/integrations",
    "/models",
    "/floatim",
    "/showcases",
    "/use-cases",
    "/use-cases/for-solopreneur",
    "/use-cases/for-creators",
    "/use-cases/for-small-business",
    "/use-cases/for-studio",
    "/alternatives",
    "/alternatives/notion-alternative",
    "/alternatives/chatgpt-alternative",
    "/privacy",
    "/terms",
    "/wishlist",
    "/app",
    "/use-cases/one-person-company",
    "/timeshop",
    "/download/success",
]

# Known zh-only or zh blog samples from GA reports
EXTRA_ZH = [
    "/zh/blog/genspark-ai-pricing",
    "/zh/blog/google-calendar-vs-apple-calendar",
    "/zh/blog/gpt-image-2-vs-midjourney-nano-banana-2",
    "/zh/blog/ai-scheduling-agent",
    "/zh/blog/best-ai-scheduling-assistants",
]


def zh_path(en_path: str) -> str:
    if en_path == "/":
        return "/zh"
    return "/zh" + en_path


def fetch(path: str) -> dict:
    url = BASE + path
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "FloatboatAuditBot/1.0",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            },
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            status = resp.status
            final_url = resp.geturl()
    except Exception as exc:  # noqa: BLE001
        return {"path": path, "status": "error", "error": str(exc)}

    title_m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    title = re.sub(r"\s+", " ", title_m.group(1).strip()) if title_m else ""

    h1_m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    h1 = re.sub(r"<[^>]+>", "", h1_m.group(1)).strip() if h1_m else ""

    lang_m = re.search(r'<html[^>]*\blang=["\']([^"\']+)["\']', html, re.I)
    lang = lang_m.group(1) if lang_m else ""

    text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.I | re.S)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    cn = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin = len(re.findall(r"[A-Za-z]", text))
    cn_ratio = round(cn / (cn + latin), 3) if (cn + latin) else 0

    # Heuristic classification
    if status != 200:
        state = "missing"
    elif cn_ratio >= 0.35:
        state = "localized"
    elif cn_ratio >= 0.08:
        state = "partial"
    else:
        state = "english_fallback"

    return {
        "path": path,
        "status": status,
        "final_url": final_url,
        "title": title[:140],
        "h1": h1[:140],
        "lang": lang,
        "cn_ratio": cn_ratio,
        "bytes": len(html),
        "state": state,
    }


def main() -> None:
    targets = {zh_path(p): p for p in EN_PATHS}
    for p in EXTRA_ZH:
        targets[p] = p.replace("/zh", "")

    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futs = {pool.submit(fetch, path): path for path in sorted(targets)}
        for fut in as_completed(futs):
            results.append(fut.result())

    results.sort(key=lambda x: x["path"])

    summary = {}
    for r in results:
        summary.setdefault(r.get("state", "error"), []).append(r["path"])

    print(json.dumps({"summary": {k: len(v) for k, v in summary.items()}, "pages": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
