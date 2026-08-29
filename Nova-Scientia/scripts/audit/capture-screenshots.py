#!/usr/bin/env python3
"""
Captura screenshots via Firecrawl API e atualiza JSONs no deploy repo.

Uso:
  pip install firecrawl-py
  $env:FIRECRAWL_API_KEY="..."
  python capture-screenshots.py --target products
  python capture-screenshots.py --target companies
  python capture-screenshots.py --target all
"""

import argparse
import json
import os
import sys
import time

FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
if not FIRECRAWL_API_KEY:
    sys.exit("FIRECRAWL_API_KEY environment variable is required.")

_CONTEXT_ROOT = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)
PROJECT_ROOT = os.environ.get("NOVA_SCIENTIA_DEPLOY_ROOT") or os.path.normpath(
    os.path.join(_CONTEXT_ROOT, "..", "..", "自有部署项目", "nova-scientia-main")
)

PRODUCT_TARGETS = [
    {"slug": "meta", "name": "Meta AI", "url": "https://ai.meta.com"},
    {"slug": "questionai", "name": "Question.AI", "url": "https://www.questionai.ai"},
    {"slug": "talkie-ai", "name": "Talkie", "url": "https://www.talkie-ai.com"},
]

COMPANY_TARGETS = [
    {"slug": "baincapitalventures", "name": "Bain Capital Ventures", "url": "https://www.baincapitalventures.com"},
    {"slug": "conviction", "name": "Conviction", "url": "https://www.conviction.com"},
    {"slug": "foundersfund", "name": "Founders Fund", "url": "https://foundersfund.com"},
    {"slug": "generalcatalyst", "name": "General Catalyst", "url": "https://generalcatalyst.com"},
    {"slug": "greenoaks", "name": "Greenoaks", "url": "https://greenoaks.com"},
    {"slug": "insightpartners", "name": "Insight Partners", "url": "https://www.insightpartners.com"},
    {"slug": "luxcapital", "name": "Lux Capital", "url": "https://luxcapital.com"},
    {"slug": "sparkcapital", "name": "Spark Capital", "url": "https://www.sparkcapital.com"},
    {"slug": "thrivecapital", "name": "Thrive Capital", "url": "https://www.thrivecap.com"},
    {"slug": "tigerglobal", "name": "Tiger Global", "url": "https://www.tigerglobal.com"},
]


def screenshot_with_firecrawl(url, output_path):
    try:
        from firecrawl import Firecrawl
    except ImportError:
        print("  ERROR: firecrawl-py not installed. Run: pip install firecrawl-py")
        return False

    app = Firecrawl(api_key=FIRECRAWL_API_KEY)
    try:
        print(f"  📸 Capturando: {url}")
        response = app.scrape(
            url,
            formats=["markdown", {"type": "screenshot", "fullPage": True, "quality": 85}],
        )
        screenshot_url = getattr(response, "screenshot", None)
        if not screenshot_url:
            print("  ⚠️  Sem screenshot na resposta")
            return False

        import urllib.request

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        req = urllib.request.Request(screenshot_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            with open(output_path, "wb") as f:
                while True:
                    chunk = r.read(65536)
                    if not chunk:
                        break
                    f.write(chunk)

        size_kb = os.path.getsize(output_path) / 1024
        if size_kb < 5:
            raise Exception(f"Download muito pequeno: {size_kb:.0f} KB")

        print(f"  ✅ {os.path.basename(output_path)} ({size_kb:.0f} KB)")
        return True
    except Exception as e:
        print(f"  ❌ Falhou: {e}")
        return False


def update_product_json(slug, image_path):
    json_path = os.path.join(PROJECT_ROOT, "content", "products", f"{slug}.json")
    if not os.path.exists(json_path):
        print(f"  ⚠️  JSON não encontrado: {json_path}")
        return False

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rel_path = f"/images/products/{os.path.basename(image_path)}"
    data["content"]["hero"]["screenshot_url"] = rel_path

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"  📝 JSON atualizado: {slug}.json → {rel_path}")
    return True


def update_company_json(slug, image_path):
    json_path = os.path.join(PROJECT_ROOT, "content", "companies", f"{slug}.json")
    if not os.path.exists(json_path):
        print(f"  ⚠️  JSON não encontrado: {json_path}")
        return False

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rel_path = f"/images/companies/{os.path.basename(image_path)}"
    if "content" in data:
        data["content"]["logo_url"] = rel_path
    else:
        data["logo_url"] = rel_path

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"  📝 JSON atualizado: {slug}.json → {rel_path}")
    return True


def run_batch(target_kind, targets):
    if target_kind == "products":
        public_dir = os.path.join(PROJECT_ROOT, "public", "images", "products")
        update_fn = update_product_json
        label = "Produtos"
    else:
        public_dir = os.path.join(PROJECT_ROOT, "public", "images", "companies")
        update_fn = update_company_json
        label = "Empresas"

    os.makedirs(public_dir, exist_ok=True)
    print("=" * 60)
    print(f"Nova Scientia — Screenshots ({label})")
    print(f"Alvos: {len(targets)}")
    print("=" * 60)

    success = 0
    for i, t in enumerate(targets):
        print(f"\n[{i + 1}/{len(targets)}] {t['name']}")
        output_path = os.path.join(public_dir, f"{t['slug']}.png")

        if os.path.exists(output_path) and os.path.getsize(output_path) > 10000:
            print(f"  ⏭️  Já existe ({os.path.getsize(output_path) / 1024:.0f} KB)")
            update_fn(t["slug"], output_path)
            success += 1
            continue

        if screenshot_with_firecrawl(t["url"], output_path):
            update_fn(t["slug"], output_path)
            success += 1

        if i < len(targets) - 1:
            time.sleep(3)

    print(f"\n{'=' * 60}")
    print(f"RESULTADO ({label}): {success}/{len(targets)}")
    print("=" * 60)
    return success


def main():
    parser = argparse.ArgumentParser(description="Captura screenshots via Firecrawl")
    parser.add_argument(
        "--target",
        choices=["products", "companies", "all"],
        default="products",
        help="Tipo de entidade (default: products)",
    )
    args = parser.parse_args()

    if args.target in ("products", "all"):
        run_batch("products", PRODUCT_TARGETS)
    if args.target in ("companies", "all"):
        run_batch("companies", COMPANY_TARGETS)


if __name__ == "__main__":
    main()
