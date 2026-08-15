/**
 * [ARCHIVED — 一次性脚本] Preenche indexed_products nos JSON de VC (type=investor).
 * 回填完成后保留备查，日常不再运行。
 *
 * Uso: node scripts/archive/backfill-indexed-products.js
 */

const fs = require("fs");
const path = require("path");
const { getDeployRoot } = require("../lib/deploy-root");

const ROOT = getDeployRoot();
const PRODUCTS_DIR = path.join(ROOT, "content", "products");
const COMPANIES_DIR = path.join(ROOT, "content", "companies");

function slugify(s) {
  return String(s)
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^a-z0-9-]/g, "");
}

/** Alinhado a company-product-match.ts */
function matchPortfolioNameToProductSlug(name, productSlugs) {
  const trimmed = name.trim();
  const full = slugify(trimmed);
  for (const p of productSlugs) {
    if (p.slug === full) return p.slug;
    const pNameSlug = slugify(p.name);
    if (pNameSlug === full) return p.slug;
  }
  const first = (name.split(/[\s(（]/)[0] ?? name).trim();
  if (first !== trimmed) return undefined;
  const kSlug = slugify(first);
  for (const p of productSlugs) {
    if (p.slug === kSlug) return p.slug;
    if (slugify(p.name) === kSlug) return p.slug;
  }
  return undefined;
}

function loadProductSlugs() {
  const files = fs.readdirSync(PRODUCTS_DIR).filter((f) => f.endsWith(".json"));
  const productSlugs = [];
  for (const f of files) {
    const raw = JSON.parse(fs.readFileSync(path.join(PRODUCTS_DIR, f), "utf-8"));
    if (raw.slug && raw.name) {
      productSlugs.push({ slug: raw.slug, name: raw.name });
    }
  }
  return productSlugs;
}

function collectFromInvestedAi(content, productSlugSet) {
  const out = new Map();
  const list = content.invested_ai_products ?? [];
  for (const item of list) {
    if (!item.slug || typeof item.slug !== "string") continue;
    if (!productSlugSet.has(item.slug)) continue;
    const name = item.name || item.slug;
    out.set(item.slug, name);
  }
  return out;
}

function collectFromPortfolio(content, productSlugs) {
  const out = new Map();
  const batches = content.portfolio_batches ?? [];
  for (const batch of batches) {
    for (const company of batch.companies ?? []) {
      if (!company.name) continue;
      const slug = matchPortfolioNameToProductSlug(company.name, productSlugs);
      if (!slug) continue;
      out.set(slug, company.name);
    }
  }
  return out;
}

function mergeIndexed(merged) {
  return [...merged.entries()]
    .map(([slug, name]) => ({ slug, name }))
    .sort((a, b) => a.name.localeCompare(b.name, "pt-BR"));
}

function main() {
  const productSlugs = loadProductSlugs();
  const productSlugSet = new Set(productSlugs.map((p) => p.slug));
  const files = fs.readdirSync(COMPANIES_DIR).filter((f) => f.endsWith(".json"));
  let updated = 0;

  for (const f of files) {
    const filePath = path.join(COMPANIES_DIR, f);
    const data = JSON.parse(fs.readFileSync(filePath, "utf-8"));
    if (data.content?.type !== "investor") continue;

    const fromInvested = collectFromInvestedAi(data.content, productSlugSet);
    const fromPortfolio = collectFromPortfolio(data.content, productSlugs);
    const merged = new Map([...fromInvested, ...fromPortfolio]);

    const next = mergeIndexed(merged);
    const prev = data.indexed_products ?? [];
    const prevStr = JSON.stringify(prev);
    const nextStr = JSON.stringify(next);
    if (prevStr === nextStr) continue;

    data.indexed_products = next;
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + "\n", "utf-8");
    console.log(`${data.slug}: indexed_products ${prev.length} → ${next.length}`);
    updated++;
  }

  console.log(`\nDone. Updated ${updated} investor company file(s).`);
}

main();
