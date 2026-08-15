#!/usr/bin/env python3
"""
Firecrawl Screenshot Script for Social Cards Generator Tools Page
=================================================================
Takes viewport screenshots of product websites using Firecrawl API,
saves them to public/tools/social-cards/, then updates EN/ZH JSON
references to the new paths.

Usage:
  1. pip install firecrawl-py
  2. cd D:\部署项目\alignify-by-kostja
  3. python D:\项目文档\Alignify项目上下文\scripts\permanent\screenshot-social-cards.py

Requires: Firecrawl API key (from the existing script in ref/)
"""

import json, os, sys, time, urllib.request

FIRECRAWL_API_KEY = "fc-6e6e4c926dae4648a65f388b57f1e346"
# Auto-detect project root: check common paths
if os.path.isdir("D:\\部署项目\\alignify-by-kostja"):
    PROJECT_ROOT = "D:\\部署项目\\alignify-by-kostja"
elif os.path.isdir("/sessions/adoring-jolly-ramanujan/mnt/alignify-by-kostja"):
    PROJECT_ROOT = "/sessions/adoring-jolly-ramanujan/mnt/alignify-by-kostja"
else:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # fallback
PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public", "tools", "social-cards")
CONTENT_EN = os.path.join(PROJECT_ROOT, "content", "tools", "en")
CONTENT_ZH = os.path.join(PROJECT_ROOT, "content", "tools", "zh")

PRODUCTS = [
    ("oginify",       "https://oginify.com",              "oginify"),
    ("opengraph-xyz", "https://www.opengraph.xyz",        "opengraph-xyz"),
    ("vercel-og",     "https://vercel.com/docs/og-image-generation", "vercel-og"),
    ("chatgpt-images","https://openai.com",                "chatgpt-images"),
    ("google-gemini", "https://deepmind.google/technologies/gemini/", "google-gemini"),
]

JSON_IMAGE_MAP = {
    "oginify":       "oginify",
    "opengraph-xyz": "opengraph-xyz",
    "vercel-og":     "vercel-og",
    "chatgpt-images":"chatgpt-images",
    "google-gemini": "google-gemini",
}


def download_with_retry(screenshot_url, output_path, max_retries=3):
    import urllib.request
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(screenshot_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as response:
                data = response.read()
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(data)
                size_kb = len(data) / 1024
                print(f"    Downloaded: {output_path} ({size_kb:.0f} KB)")
                return size_kb, output_path
        except Exception as e:
            if attempt < max_retries - 1:
                wait = (attempt + 1) * 3
                print(f"    Retry {attempt+1}/{max_retries} after {wait}s: {e}")
                time.sleep(wait)
    return None, None


def screenshot_with_firecrawl(url, output_path):
    try:
        from firecrawl import Firecrawl
    except ImportError:
        print("  FAIL: firecrawl-py not installed. Run: pip install firecrawl-py")
        return False

    app = Firecrawl(api_key=FIRECRAWL_API_KEY)
    try:
        print(f"  Screenshotting: {url}")
        response = app.scrape(url, formats=[
            {"type": "screenshot", "fullPage": False, "quality": 85}
        ])
        screenshot_url = getattr(response, 'screenshot', None)
        if not screenshot_url:
            print(f"  WARNING: No screenshot in response")
            return False
        size_kb, actual_path = download_with_retry(screenshot_url, output_path)
        return actual_path is not None
    except Exception as e:
        print(f"  FAIL: {url} -> {e}")
        return False


def update_json_images(slug, image_dest):
    """Update image references in EN and ZH JSON files."""
    for locale, content_dir in [("en", CONTENT_EN), ("zh", CONTENT_ZH)]:
        json_path = os.path.join(content_dir, f"{slug}.json")
        if not os.path.exists(json_path):
            print(f"  SKIP (no JSON): {json_path}")
            continue
        try:
            d = json.load(open(json_path, encoding="utf-8"))
        except:
            print(f"  SKIP (bad JSON): {json_path}")
            continue

        changed = False
        for block in d.get("blocks", []):
            if block.get("type") == "bestTools":
                for tool in block.get("tools", []):
                    tool_id = tool.get("id")
                    if tool_id in JSON_IMAGE_MAP:
                        expected = f"/tools/social-cards/{JSON_IMAGE_MAP[tool_id]}.jpg"
                        if tool.get("imageSrc") != expected:
                            tool["imageSrc"] = expected
                            changed = True
                            print(f"  [{locale}] {tool_id}: imageSrc -> {expected}")

        if changed:
            json.dump(d, open(json_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(f"  Updated: {json_path}")


def main():
    os.makedirs(PUBLIC_DIR, exist_ok=True)

    print(f"Products to screenshot: {len(PRODUCTS)}")
    print()

    # Step 1: Take screenshots
    print("-- Step 1: Taking screenshots --")
    failed = []
    for name, url, filename in PRODUCTS:
        output_path = os.path.join(PUBLIC_DIR, f"{filename}.jpg")
        if os.path.exists(output_path):
            size_kb = os.path.getsize(output_path) / 1024
            print(f"  EXISTS ({size_kb:.0f} KB): {output_path}")
            continue
        if screenshot_with_firecrawl(url, output_path):
            print(f"  OK: {output_path}")
        else:
            failed.append((name, url, output_path))

    # Step 2: Update JSON image references
    print("\n-- Step 2: Updating JSON image paths --")
    update_json_images("social-cards-generator", None)

    # Summary
    print("\n-- Summary --")
    if failed:
        print(f"Failed: {len(failed)}")
        for name, url, path in failed:
            print(f"  - {name}: {url}")
    else:
        print("All screenshots OK (or already existed).")
    print(f"Images in: {PUBLIC_DIR}")


if __name__ == "__main__":
    main()