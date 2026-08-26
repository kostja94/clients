#!/usr/bin/env python3
"""Full-site OG audit: articles, hubs, manifest vs disk."""
from __future__ import annotations

import json
import re
from pathlib import Path

DEPLOY = Path(r"E:\自有部署项目\alignify production")
PUBLIC = DEPLOY / "public"
MANIFEST = DEPLOY / "src/data/og-locale-ready.json"
LOCALES = ("en", "zh")


def content_slugs(section: str) -> list[str]:
    d = DEPLOY / "content" / section / "en"
    return sorted(p.stem for p in d.glob("*.md")) if d.is_dir() else []


def tools_slugs() -> list[str]:
    text = (DEPLOY / "src/data/tools-article-images.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'"([a-z0-9-]+)":\s*`\$\{BASE\}', text)))


def config_slugs(path: str, pattern: str) -> list[str]:
    text = (DEPLOY / path).read_text(encoding="utf-8")
    return sorted(set(re.findall(pattern, text)))


def load_manifest() -> set[str]:
    if not MANIFEST.is_file():
        return set()
    return set(json.loads(MANIFEST.read_text(encoding="utf-8")))


def og_on_disk(section: str, slug: str, locale: str) -> bool:
    return (PUBLIC / section / slug / f"{slug}-og-{locale}.webp").is_file()


def glossary_legacy_og(slug: str, locale: str) -> bool:
    return (PUBLIC / "glossary" / f"{slug}-{locale}.png").is_file()


def main() -> None:
    sections = {
        "marketing": content_slugs("marketing"),
        "seo": content_slugs("seo"),
        "tools": tools_slugs(),
        "blog": content_slugs("blog"),
        "insights": config_slugs("src/data/insights-pages-config.ts", r'slug:\s*"([^"]+)"'),
        "events": sorted(re.findall(
            r'"([a-z0-9-]+)":\s*\{',
            (DEPLOY / "src/data/events-meta.ts").read_text(encoding="utf-8"),
        )),
    }
    glossary_slugs = config_slugs("src/data/glossary-pages-config.ts", r'slug:\s*"([^"]+)"')

    manifest = load_manifest()
    disk_total = len(list(PUBLIC.rglob("*-og-*.webp")))

    print("=== 1. 文章页 locale OG（webp 流水线 + manifest）===\n")
    missing_disk: list[str] = []
    missing_manifest: list[str] = []
    article_ok = 0
    article_need = 0

    for sec, slugs in sections.items():
        sec_disk_miss = []
        sec_manifest_miss = []
        for slug in slugs:
            for loc in LOCALES:
                article_need += 1
                key = f"{sec}/{slug}:{loc}"
                on_disk = og_on_disk(sec, slug, loc)
                in_manifest = key in manifest
                if on_disk and in_manifest:
                    article_ok += 1
                else:
                    if not on_disk:
                        sec_disk_miss.append(f"{sec}/{slug} [{loc}]")
                        missing_disk.append(f"{sec}/{slug} [{loc}]")
                    if not in_manifest:
                        sec_manifest_miss.append(f"{sec}/{slug} [{loc}]")
                        missing_manifest.append(key)
        mark = "OK" if not sec_disk_miss else f"DISK_MISS {len(sec_disk_miss)}"
        print(f"  {sec:12} {len(slugs)*2 - len(sec_disk_miss):3}/{len(slugs)*2}  disk  {mark}")
        if sec_manifest_miss and not sec_disk_miss:
            print(f"               manifest only miss: {len(sec_manifest_miss)}")

    print(f"\n  文章页合计: {article_ok}/{article_need} 完整（磁盘+manifest）")
    print(f"  磁盘 webp 总数: {disk_total}  |  manifest 条目: {len(manifest)}")

    if missing_disk:
        print("\n  缺磁盘文件:")
        for m in missing_disk:
            print(f"    {m}")

    # Glossary — legacy PNG per locale
    print("\n=== 2. Glossary 文章页（legacy PNG，非 webp 流水线）===\n")
    gloss_ok = 0
    gloss_miss = []
    for slug in glossary_slugs:
        for loc in LOCALES:
            if glossary_legacy_og(slug, loc):
                gloss_ok += 1
            else:
                gloss_miss.append(f"glossary/{slug} [{loc}]")
    print(f"  glossary: {gloss_ok}/{len(glossary_slugs)*2}  legacy PNG  ", end="")
    print("OK" if not gloss_miss else f"MISS {len(gloss_miss)}")

    # Hub pages
    print("\n=== 3. Hub / 独立页 OG 来源 ===\n")
    hubs_unique = [
        ("/", "og-image.png", PUBLIC / "og-image.png", "unique"),
        ("/about", "alignifyDefaultOgImage", None, "shared_default"),
        ("/tools", "og-tools-hub.png", PUBLIC / "tools" / "og-tools-hub.png", "unique"),
        ("/seo", "alignifyDefaultOgImage", None, "shared_default"),
        ("/marketing", "alignifyDefaultOgImage", None, "shared_default"),
        ("/blog", "alignifyDefaultOgImage", None, "shared_default"),
        ("/insights", "alignifyDefaultOgImage", None, "shared_default"),
        ("/events", "alignifyDefaultOgImage", None, "shared_default"),
        ("/glossary", "alignifyDefaultOgImage", None, "shared_default"),
        ("/explore", "alignifyDefaultOgImage", None, "shared_default"),
        ("/services", "alignifyDefaultOgImage", None, "shared_default"),
        ("/customer-stories", "og-customer-stories.png", PUBLIC / "customer-stories" / "og-customer-stories.png", "unique"),
        ("/betalist", "YouTube thumbnail", None, "unique_other"),
        ("/media-kit", "alignifyDefaultOgImage", None, "shared_default"),
        ("/partnership", "alignifyDefaultOgImage", None, "shared_default"),
        ("/privacy-policy", "alignifyDefaultOgImage", None, "shared_default"),
        ("/skills", "alignifyDefaultOgImage", None, "shared_default"),
        ("/author/kostja", "og-kostja.png", PUBLIC / "author" / "og-kostja.png", "unique"),
    ]

    shared_default = []
    unique_hubs = []
    for path, src, f, kind in hubs_unique:
        if kind == "shared_default":
            shared_default.append(path)
            print(f"  {path:22} 共享站点默认 og-image.png")
        elif kind == "unique_other":
            print(f"  {path:22} 独立（YouTube 缩略图，非 1200x630）")
            unique_hubs.append(path)
        elif f and f.is_file():
            print(f"  {path:22} 独立定制 OK")
            unique_hubs.append(path)
        else:
            print(f"  {path:22} 应有独立图但文件缺失")

    # Unlocalized
    print("\n=== 4. 未本地化工具页 ===\n")
    for p in ["/audit-website", "/audit-website-by-lovable"]:
        print(f"  {p:30} 无独立 OG（工具页，通常 noindex）")

    # Summary
    print("\n=== 结论 ===\n")
    all_articles_ok = article_ok == article_need and not gloss_miss
    print(f"  文章页（7 频道 webp）: {'全部覆盖' if not missing_disk else f'缺 {len(missing_disk)} 张'}")
    print(f"  Glossary 3 篇: {'全部有 legacy PNG' if not gloss_miss else f'缺 {len(gloss_miss)} 张'}")
    print(f"  Hub 独立定制: 4 个（/, /tools, /customer-stories, /author/kostja）+ betalist 缩略图")
    print(f"  Hub 仍共享默认 OG: {len(shared_default)} 个")
    for p in shared_default:
        print(f"    - {p}")
    print()
    if all_articles_ok and not gloss_miss:
        print("  >> 所有内容文章页均有独特 OG（webp 或 glossary PNG）。")
        print("  >> 但 12 个 Hub/独立页仍共用 og-image.png，不算「每页独特」。")
    else:
        print("  >> 尚有内容页缺 OG，见上方列表。")


if __name__ == "__main__":
    main()
