#!/usr/bin/env python3
"""
Firecrawl Screenshot Script for Customer Stories Featured Products
==================================================================
Takes viewport (first-screen) screenshots of 6 featured product
homepages using Firecrawl API, saves them as JPGs.

Modes:
  default        Screenshot all 6 products (skips existing)
  --only KEY     Screenshot a single product by key
  --retry-failed Re-screenshot only previously failed products
  --report       Print markdown summary of existing screenshots
  --quality N    JPEG quality (default 85, range 1-100)

Usage:
  1. pip install firecrawl-py
  2. cd D:\部署项目\alignify-by-kostja
  3. python D:\项目文档\Alignify项目上下文\scripts\ops\screenshot-customer-products.py
"""

import json, os, sys, time, urllib.request

FIRECRAWL_API_KEY = "fc-6e6e4c926dae4648a65f388b57f1e346"

# Auto-detect project root
if os.path.isdir("D:\\部署项目\\alignify-by-kostja"):
    PROJECT_ROOT = "D:\\部署项目\\alignify-by-kostja"
elif os.path.isdir("/sessions/bold-inspiring-davinci/mnt/alignify-by-kostja"):
    PROJECT_ROOT = "/sessions/bold-inspiring-davinci/mnt/alignify-by-kostja"
else:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "public", "assets", "customer-stories")
FAILED_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".failed-cache.json")

PRODUCTS = [
    ("tunee",       "https://www.tunee.ai/",               "Tunee — Voice / Music"),
    ("voispark",    "https://voispark.com/",                "VoiSpark — Voice / TTS"),
    ("lessie-ai",   "https://lessie.ai/",                   "Lessie AI — Agent / Growth Intel"),
    ("medeo-ai",    "https://www.medeo.app/",               "Medeo AI — Agent / Video"),
    ("finalround",  "https://www.finalroundai.com/",        "Final Round AI — Agent / Career"),
    ("thetawave",   "https://thetawave.ai/",                "ThetaWave — Industry / EdTech"),
]

# ── helpers ──────────────────────────────────────────────────────────

def download_with_retry(screenshot_url, output_path, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                screenshot_url,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            with urllib.request.urlopen(req, timeout=60) as response:
                data = response.read()
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(data)
                size_kb = len(data) / 1024
                print(f"    ✓ {output_path} ({size_kb:.0f} KB)")
                return True
        except Exception as e:
            if attempt < max_retries - 1:
                wait = (attempt + 1) * 3
                print(f"    ⟳ Retry {attempt+1}/{max_retries} after {wait}s: {e}")
                time.sleep(wait)
            else:
                print(f"    ✗ Failed after {max_retries} attempts: {e}")
    return False


def screenshot_one(url, output_path, label, quality=85):
    try:
        from firecrawl import Firecrawl
    except ImportError:
        print("  ✗ firecrawl-py not installed. Run: pip install firecrawl-py")
        return False

    app = Firecrawl(api_key=FIRECRAWL_API_KEY)
    try:
        print(f"  [{label}]")
        print(f"    URL: {url}")

        response = app.scrape(
            url,
            formats=[
                {"type": "screenshot", "fullPage": False, "quality": quality}
            ],
        )
        screenshot_url = getattr(response, "screenshot", None)
        if not screenshot_url:
            print(f"    ✗ No screenshot in response")
            return False

        return download_with_retry(screenshot_url, output_path)
    except Exception as e:
        print(f"    ✗ {e}")
        return False


def load_failed_cache():
    """Load list of previously failed product keys."""
    if os.path.exists(FAILED_CACHE):
        try:
            with open(FAILED_CACHE) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_failed_cache(keys):
    """Persist list of failed product keys for --retry-failed."""
    try:
        with open(FAILED_CACHE, "w") as f:
            json.dump(keys, f, indent=2)
    except OSError:
        pass  # best effort


# ── modes ────────────────────────────────────────────────────────────

def cmd_default(quality):
    """Screenshot all products (skip existing)."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = len(PRODUCTS)

    print(f"Customer Stories — Featured Product Screenshots")
    print(f"{'='*60}")
    print(f"Products: {total}  |  Quality: {quality}  |  Output: {OUTPUT_DIR}")
    print(f"{'='*60}\n")

    results = {"success": [], "skipped": [], "failed": []}
    failed_keys = []

    for filename, url, label in PRODUCTS:
        output_path = os.path.join(OUTPUT_DIR, f"{filename}.jpg")

        if os.path.exists(output_path):
            size_kb = os.path.getsize(output_path) / 1024
            print(f"  EXISTS ({size_kb:.0f} KB): {output_path}")
            results["skipped"].append(label)
            continue

        t0 = time.time()
        ok = screenshot_one(url, output_path, label, quality)
        elapsed = time.time() - t0
        status = "✓" if ok else "✗"
        print(f"    {status}  ({elapsed:.1f}s)\n")

        if ok:
            results["success"].append(label)
        else:
            results["failed"].append(label)
            failed_keys.append(filename)

    save_failed_cache(failed_keys)

    print(f"{'='*60}")
    print(f"Results: {len(results['success'])} succeeded, "
          f"{len(results['skipped'])} skipped, "
          f"{len(results['failed'])} failed")
    if results["failed"]:
        print(f"Retry with: python screenshot-customer-products.py --retry-failed")
    print(f"Done. Images in: {OUTPUT_DIR}")
    return len(results["failed"]) == 0


def cmd_retry_failed(quality):
    """Re-screenshot only products that failed last time."""
    failed_keys = load_failed_cache()
    if not failed_keys:
        print("No failed products cached — nothing to retry.")
        return True

    targets = [(f, u, l) for f, u, l in PRODUCTS if f in failed_keys]
    if not targets:
        print("No matching products found in cache.")
        return True

    print(f"Retrying {len(targets)} previously failed product(s):")
    for filename, url, label in targets:
        print(f"  • {label} ({url})")
    print()

    still_failed = []
    for filename, url, label in targets:
        output_path = os.path.join(OUTPUT_DIR, f"{filename}.jpg")
        t0 = time.time()
        ok = screenshot_one(url, output_path, label, quality)
        elapsed = time.time() - t0
        status = "✓" if ok else "✗"
        print(f"    {status}  ({elapsed:.1f}s)\n")
        if not ok:
            still_failed.append(filename)

    save_failed_cache(still_failed)

    if still_failed:
        print(f"Still failed: {len(still_failed)}/{len(targets)}")
        print(f"Run again with --retry-failed to retry these.")
        return False
    else:
        print("All retried products succeeded!")
        return True


def cmd_only(key, quality):
    """Screenshot a single product by key."""
    matches = [p for p in PRODUCTS if p[0] == key]
    if not matches:
        print(f"No product found with key: {key}")
        print(f"Available: {', '.join(p[0] for p in PRODUCTS)}")
        return False

    filename, url, label = matches[0]
    output_path = os.path.join(OUTPUT_DIR, f"{filename}.jpg")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Screenshotting 1 product: {label}")
    print(f"{'='*60}\n")

    t0 = time.time()
    ok = screenshot_one(url, output_path, label, quality)
    elapsed = time.time() - t0
    print(f"\n{'='*60}")
    print(f"{'✓' if ok else '✗'}  ({elapsed:.1f}s)")
    return ok


def cmd_report():
    """Print markdown report of existing screenshots."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    existing = []
    missing = []
    for filename, _, label in PRODUCTS:
        path = os.path.join(OUTPUT_DIR, f"{filename}.jpg")
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            mtime = os.path.getmtime(path)
            age_h = (time.time() - mtime) / 3600
            existing.append((label, size_kb, age_h, filename))
        else:
            missing.append((label, filename))

    print(f"# Customer Stories Screenshot Report")
    print(f"")
    print(f"**Output**: `{OUTPUT_DIR}`")
    print(f"**Total**: {len(PRODUCTS)} products")
    print(f"**Done**: {len(existing)}  **Missing**: {len(missing)}")
    print(f"")

    if existing:
        print(f"## Existing Screenshots")
        print(f"")
        print(f"| Product | Size | Age | File |")
        print(f"|---|---|---|---|")
        for label, size_kb, age_h, filename in existing:
            age_str = f"{age_h:.0f}h" if age_h < 72 else f"{age_h/24:.0f}d"
            print(f"| {label} | {size_kb:.0f} KB | {age_str} | `{filename}.jpg` |")
        print(f"")

    if missing:
        print(f"## Missing")
        print(f"")
        for label, filename in missing:
            print(f"- {label} → `python {os.path.basename(__file__)} --only {filename}`")
        print(f"")

    return len(missing) == 0


# ── CLI ──────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Customer Stories featured product screenshots",
    )
    parser.add_argument("--only", help="Screenshot one product by key (e.g. tunee)")
    parser.add_argument("--retry-failed", action="store_true",
                        help="Retry only previously failed products")
    parser.add_argument("--report", action="store_true",
                        help="Print markdown summary of existing screenshots")
    parser.add_argument("--quality", type=int, default=85,
                        help="JPEG quality 1-100 (default 85)")
    args = parser.parse_args()

    # Validate quality
    quality = max(1, min(100, args.quality))

    if args.report:
        return cmd_report()
    elif args.retry_failed:
        return cmd_retry_failed(quality)
    elif args.only:
        return cmd_only(args.only, quality)
    else:
        return cmd_default(quality)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
