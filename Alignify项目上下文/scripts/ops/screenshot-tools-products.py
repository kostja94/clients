#!/usr/bin/env python3
"""
Firecrawl Screenshot Script for Tools BestTools Product Images
================================================================
Reads tools-screenshot-registry.json (and optional audit JSON) to capture
viewport screenshots into alignify-by-kostja/public/.

Usage:
  pip install firecrawl-py
  cd D:\\部署项目\\alignify-by-kostja
  python D:\\项目文档\\Alignify项目上下文\\scripts\\ops\\screenshot-tools-products.py --report
  python ...\\screenshot-tools-products.py --severity P0 --force
  python ...\\screenshot-tools-products.py --page search-engine --force
  python ...\\screenshot-tools-products.py --only search-engine:you-com --force
  python ...\\screenshot-tools-products.py --from-audit ..\\reports\\tools-images-audit-2026-06-17.json --severity P0 --dry-run
  python ...\\screenshot-tools-products.py --update-json --severity P0 --force

Set FIRECRAWL_API_KEY env var, or falls back to embedded key from legacy scripts.
"""

import argparse
import json
import os
import sys
import time
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTEXT_ROOT = os.path.dirname(SCRIPT_DIR)
REGISTRY_PATH = os.path.join(CONTEXT_ROOT, "data", "tools-screenshot-registry.json")
FAILED_CACHE = os.path.join(SCRIPT_DIR, ".tools-screenshot-failed.json")

FIRECRAWL_API_KEY = os.environ.get(
    "FIRECRAWL_API_KEY",
    "fc-6e6e4c926dae4648a65f388b57f1e346",
)

if os.path.isdir("D:\\部署项目\\alignify-by-kostja"):
    PROJECT_ROOT = "D:\\部署项目\\alignify-by-kostja"
elif os.environ.get("ALIGNIFY_DEPLOY_ROOT"):
    PROJECT_ROOT = os.environ["ALIGNIFY_DEPLOY_ROOT"]
else:
    PROJECT_ROOT = os.getcwd()

PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public")
CONTENT_TOOLS = os.path.join(PROJECT_ROOT, "content", "tools")
CONTENT_BLOG = os.path.join(PROJECT_ROOT, "content", "blog")


def load_registry_from(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if not k.startswith("_")}


def load_registry():
    return load_registry_from(REGISTRY_PATH)


def load_audit(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("issues", [])


def link_url_from_json(page_slug, product_id):
    for content_root in (CONTENT_TOOLS, CONTENT_BLOG):
        for locale in ("en", "zh"):
            fp = os.path.join(content_root, locale, f"{page_slug}.json")
            if not os.path.exists(fp):
                continue
            with open(fp, encoding="utf-8") as f:
                doc = json.load(f)
            for block in doc.get("blocks", []):
                if block.get("type") != "bestTools":
                    continue
                for tool in block.get("tools", []):
                    if tool.get("id") == product_id:
                        return tool.get("linkUrl")
    return None


def _patch_json_image_src(fp, page_slug, product_id, new_image_src):
    with open(fp, encoding="utf-8") as f:
        doc = json.load(f)
    changed = False
    for block in doc.get("blocks", []):
        if block.get("type") != "bestTools":
            continue
        for tool in block.get("tools", []):
            if tool.get("id") == product_id and tool.get("imageSrc") != new_image_src:
                tool["imageSrc"] = new_image_src
                if not tool.get("imageAlt"):
                    name = tool.get("name", product_id)
                    locale = doc.get("blogLayout", {}).get("locale") or (
                        "zh" if "/zh/" in fp.replace("\\", "/") else "en"
                    )
                    tool["imageAlt"] = (
                        f"{name} 首页截图" if locale == "zh" else f"{name} homepage screenshot"
                    )
                changed = True
    if changed:
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=2)
            f.write("\n")
        return True
    return False


def update_json_image_src(page_slug, product_id, new_image_src):
    updated = []
    for content_root in (CONTENT_TOOLS, CONTENT_BLOG):
        for locale in ("en", "zh"):
            fp = os.path.join(content_root, locale, f"{page_slug}.json")
            if not os.path.exists(fp):
                continue
            if _patch_json_image_src(fp, page_slug, product_id, new_image_src):
                updated.append(fp)
    return updated


def build_jobs(registry, audit_issues=None, severity=None, page=None, only=None):
    jobs = []

    if audit_issues:
        seen = set()
        for issue in audit_issues:
            if severity and issue.get("severity") != severity:
                continue
            key = issue.get("key")
            if not key or key in seen:
                continue
            if page and not key.startswith(f"{page}:"):
                continue
            if only and key != only:
                continue
            if issue.get("type") == "youtube_should_migrate":
                continue
            seen.add(key)
            page_slug, product_id = key.split(":", 1)
            reg = registry.get(key, {})
            if reg.get("skipReason"):
                continue
            url = reg.get("screenshotUrl") or issue.get("linkUrl") or link_url_from_json(page_slug, product_id)
            out = reg.get("outputPath") or issue.get("outputPath")
            if not url or not out:
                continue
            jobs.append({
                "key": key,
                "pageSlug": page_slug,
                "productId": product_id,
                "url": url,
                "outputPath": out,
                "priority": reg.get("priority") or issue.get("severity", "P1"),
                "jsonImageSrc": reg.get("jsonImageSrc"),
                "reason": reg.get("reason", issue.get("detail", "")),
            })
        return jobs

    for key, reg in registry.items():
        if reg.get("skipReason"):
            continue
        page_slug, product_id = key.split(":", 1)
        if page and page_slug != page:
            continue
        if only and key != only:
            continue
        pri = reg.get("priority", "P1")
        if severity and pri != severity:
            continue
        url = reg.get("screenshotUrl")
        out = reg.get("outputPath")
        if not url or not out:
            continue
        jobs.append({
            "key": key,
            "pageSlug": page_slug,
            "productId": product_id,
            "url": url,
            "outputPath": out,
            "priority": pri,
            "jsonImageSrc": reg.get("jsonImageSrc"),
            "reason": reg.get("reason", ""),
        })
    return jobs


def download_with_retry(screenshot_url, output_path, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                screenshot_url,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            with urllib.request.urlopen(req, timeout=90) as response:
                data = response.read()
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(data)
                size_kb = len(data) / 1024
                print(f"    -> {output_path} ({size_kb:.0f} KB)")
                return True
        except Exception as e:
            if attempt < max_retries - 1:
                wait = (attempt + 1) * 3
                print(f"    Retry {attempt + 1}/{max_retries} after {wait}s: {e}")
                time.sleep(wait)
            else:
                print(f"    FAILED: {e}")
    return False


def screenshot_one(url, output_path, label, quality=90):
    try:
        from firecrawl import Firecrawl
    except ImportError:
        print("  firecrawl-py not installed. Run: pip install firecrawl-py")
        return False

    app = Firecrawl(api_key=FIRECRAWL_API_KEY)
    try:
        print(f"  [{label}]")
        print(f"    URL: {url}")
        response = app.scrape(
            url,
            formats=[{"type": "screenshot", "fullPage": False, "quality": quality}],
        )
        screenshot_url = getattr(response, "screenshot", None)
        if not screenshot_url:
            print("    No screenshot in response")
            return False
        return download_with_retry(screenshot_url, output_path)
    except Exception as e:
        print(f"    ERROR: {e}")
        return False


def load_failed():
    if os.path.exists(FAILED_CACHE):
        try:
            with open(FAILED_CACHE, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_failed(keys):
    try:
        with open(FAILED_CACHE, "w", encoding="utf-8") as f:
            json.dump(keys, f, indent=2)
    except OSError:
        pass


def cmd_report(registry, registry_path):
    print("# Tools Product Screenshot Report\n")
    print(f"**Registry**: `{registry_path}`")
    print(f"**Public**: `{PUBLIC_DIR}`\n")
    print("| Key | Priority | Status | Size | Path |")
    print("|-----|----------|--------|------|------|")
    for key, reg in sorted(registry.items()):
        if reg.get("skipReason"):
            print(f"| {key} | {reg.get('priority','-')} | SKIP ({reg['skipReason']}) | - | - |")
            continue
        out = reg.get("outputPath", "")
        abs_path = os.path.join(PUBLIC_DIR, out)
        if os.path.exists(abs_path):
            kb = os.path.getsize(abs_path) / 1024
            print(f"| {key} | {reg.get('priority','-')} | OK | {kb:.0f} KB | `{out}` |")
        else:
            print(f"| {key} | {reg.get('priority','-')} | MISSING | - | `{out}` |")
    return True


def run_jobs(jobs, quality, force, dry_run, update_json):
    print("Tools Product Screenshots")
    print("=" * 60)
    print(f"Jobs: {len(jobs)} | Quality: {quality} | Force: {force} | Dry-run: {dry_run}")
    print("=" * 60 + "\n")

    if not jobs:
        print("No jobs matched filters.")
        return True

    ok_list, skip_list, fail_list = [], [], []

    for job in jobs:
        out_abs = os.path.join(PUBLIC_DIR, job["outputPath"])
        label = job["key"]

        if dry_run:
            exists = os.path.exists(out_abs)
            print(f"  [DRY] {label}")
            print(f"    URL:  {job['url']}")
            print(f"    OUT:  {job['outputPath']} ({'exists' if exists else 'missing'})")
            print(f"    WHY:  {job.get('reason', '')}\n")
            continue

        if os.path.exists(out_abs) and not force:
            kb = os.path.getsize(out_abs) / 1024
            print(f"  SKIP ({kb:.0f} KB): {job['outputPath']}")
            skip_list.append(label)
            continue

        t0 = time.time()
        success = screenshot_one(job["url"], out_abs, label, quality)
        elapsed = time.time() - t0
        print(f"    {'OK' if success else 'FAIL'} ({elapsed:.1f}s)\n")

        if success:
            ok_list.append(label)
            if update_json and job.get("jsonImageSrc"):
                paths = update_json_image_src(
                    job["pageSlug"], job["productId"], job["jsonImageSrc"]
                )
                for p in paths:
                    print(f"    JSON updated: {p}")
        else:
            fail_list.append(label)

    if not dry_run:
        save_failed(fail_list)
        print("=" * 60)
        print(f"Done: {len(ok_list)} new, {len(skip_list)} skipped, {len(fail_list)} failed")
    return len(fail_list) == 0


def main():
    parser = argparse.ArgumentParser(description="Tools BestTools screenshots via Firecrawl")
    parser.add_argument("--report", action="store_true", help="Registry status report")
    parser.add_argument("--registry", default=REGISTRY_PATH, help="Registry JSON path")
    parser.add_argument("--from-audit", help="Audit JSON from audit-tools-images.mjs")
    parser.add_argument("--severity", help="Filter by priority/severity (P0, P1, P2)")
    parser.add_argument("--page", help="Filter by page slug (e.g. search-engine)")
    parser.add_argument("--only", help="Single registry key (e.g. search-engine:you-com)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Print jobs without API calls")
    parser.add_argument("--quality", type=int, default=90, help="JPEG quality 1-100")
    parser.add_argument("--update-json", action="store_true", help="Update imageSrc when jsonImageSrc set")
    parser.add_argument("--retry-failed", action="store_true", help="Retry cached failed keys")
    args = parser.parse_args()

    registry_path = args.registry
    registry = load_registry_from(registry_path)
    quality = max(1, min(100, args.quality))

    if args.report:
        return cmd_report(registry, registry_path)

    audit_issues = load_audit(args.from_audit) if args.from_audit else None

    if args.retry_failed:
        failed = load_failed()
        jobs = [
            j for j in build_jobs(registry, severity=args.severity, page=args.page)
            if j["key"] in failed
        ]
    else:
        jobs = build_jobs(
            registry,
            audit_issues=audit_issues,
            severity=args.severity,
            page=args.page,
            only=args.only,
        )

    return run_jobs(jobs, quality, args.force, args.dry_run, args.update_json)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
