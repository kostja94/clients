import re
import json
from pathlib import Path

root = Path(r"e:/clients/Alignify/knowledge")
skip = {"README.md", "_TEMPLATE.md", "KEYWORD-RESEARCH.md", "territory-map.md", "search-engine.plan.md", "search-engine-optimization-plan.md"}
results = []

# SEO slug -> likely English primary keyword mapping from H1
seo_en_map = {
    "internal-links": "internal linking",
    "link-building": "link building",
    "navigation-menu": "navigation menu SEO",
    "breadcrumbs": "breadcrumb navigation SEO",
    "external-links": "external links SEO",
    "submit-website": "submit website to search engines",
    "website-traffic": "website traffic analysis",
    "website-structure": "website structure SEO",
    "url-optimization": "URL optimization SEO",
    "checklist": "SEO checklist",
    "landing-page": "landing page SEO",
    "local-search-engines": "local search engines",
    "website-indexing": "website indexing",
    "serp": "SERP features",
    "glossary": "SEO glossary",
    "website-rendering": "website rendering SEO",
    "branded-queries-filter-google-search-console": "Google Search Console branded queries",
    "how-search-engine-works": "how search engines work",
    "sitemap": "XML sitemap",
    "crawler": "web crawler",
    "domain": "domain SEO",
    "html-tag": "HTML tags SEO",
    "redirect-chain": "redirect chain SEO",
    "search-engine": "search engine types",
    "robots-txt": "robots.txt",
    "learn-seo": "learn SEO",
    "best-tools": "SEO tools",
    "html-a-tag": "HTML anchor tag SEO",
    "meta-tag": "meta tags SEO",
    "create-blog": "create a blog",
    "schema": "schema markup",
    "category-pages": "category page SEO",
    "google-tag-manager": "Google Tag Manager",
    "subdomain-vs-subfolder": "subdomain vs subfolder SEO",
    "new-domains-tld": "new top level domains",
    "programmatic-seo": "programmatic SEO",
    "dark-traffic": "dark traffic analytics",
    "search-and-traffic-definitions": "search traffic definitions",
    "gsc-platform-properties": "Google Search Console properties",
}

for folder in ["seo", "marketing", "insights"]:
    fpath = root / folder
    if not fpath.exists():
        continue
    for md in sorted(fpath.rglob("*.md")):
        if md.name.startswith("_") or md.name in skip:
            continue
        text = md.read_text(encoding="utf-8", errors="ignore")
        rel = str(md.relative_to(root)).replace("\\", "/")
        slug = md.stem
        h1 = None
        m = re.search(r"^#\s+(.+?)\s*·\s*知识块", text, re.M)
        if m:
            h1 = m.group(1).strip()
        keyword_en = seo_en_map.get(slug) if folder == "seo" else None
        m = re.search(r"keywordEn[`'\"]?\s*[:：]\s*\*?\*?([^*\n·]+?)\*?\*?", text)
        if m:
            keyword_en = m.group(1).strip().strip("*").strip()
        results.append({
            "path": rel,
            "slug": slug,
            "folder": folder,
            "current_primary": keyword_en or h1 or slug,
            "h1": h1,
        })

out = Path(r"e:/clients/temp/kw-audit-batches/batch7_seo_marketing_insights.json")
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"batch7: {len(results)} slugs -> {out}")
