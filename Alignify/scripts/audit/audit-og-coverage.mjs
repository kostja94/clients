#!/usr/bin/env node
/**
 * Audit OG cover coverage — deploy public is canonical (single copy).
 *
 * Usage:
 *   node audit-og-coverage.mjs              # deploy public (default)
 *   node audit-og-coverage.mjs --staging    # legacy context assets/og only
 *   node audit-og-coverage.mjs --both       # deploy + staging (find duplicates)
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ALIGNIFY_CTX = path.resolve(__dirname, "..", "..");

const DEPLOY_ROOT =
  process.env.ALIGNIFY_DEPLOY_ROOT ||
  (fs.existsSync("E:\\自有部署项目\\alignify production")
    ? "E:\\自有部署项目\\alignify production"
    : fs.existsSync("D:\\部署项目\\alignify-by-kostja")
      ? "D:\\部署项目\\alignify-by-kostja"
      : null);

const STAGING_ROOT = path.join(ALIGNIFY_CTX, "assets", "og");
const args = process.argv.slice(2);
const stagingOnly = args.includes("--staging");
const scanBoth = args.includes("--both");
const scanStaging = stagingOnly || scanBoth;
const scanDeploy = !stagingOnly && DEPLOY_ROOT;

const PUBLIC = scanDeploy ? path.join(DEPLOY_ROOT, "public") : null;
const SRC = scanDeploy ? path.join(DEPLOY_ROOT, "src", "data") : null;

const SECTIONS = [
  { name: "tools", mapFile: "tools-article-images.ts", contentDir: null },
  { name: "blog", mapFile: "blog-article-images.ts", contentDir: "blog" },
  { name: "seo", mapFile: "seo-article-images.ts", contentDir: "seo" },
  { name: "marketing", mapFile: "marketing-article-images.ts", contentDir: "marketing" },
  { name: "insights", mapFile: "insights-article-images.ts", contentDir: "insights" },
  { name: "events", mapFile: "events-article-images.ts", contentDir: "events" },
];

function readMapSlugs(mapFile) {
  if (!SRC) return {};
  const p = path.join(SRC, mapFile);
  if (!fs.existsSync(p)) return {};
  const text = fs.readFileSync(p, "utf8");
  const out = {};
  for (const m of text.matchAll(/"([^"]+)":\s*`?\$\{BASE\}([^`"]+)`?/g)) {
    out[m[1]] = m[2];
  }
  for (const m of text.matchAll(/^\s+([a-z0-9-]+):\s*`?\$\{BASE\}([^`"]+)`?/gm)) {
    out[m[1]] = m[2];
  }
  return out;
}

function countContentSlugs(dirName) {
  if (!DEPLOY_ROOT) return new Set();
  const base = path.join(DEPLOY_ROOT, "content", dirName);
  const slugs = new Set();
  if (!fs.existsSync(base)) return slugs;
  const walk = (d) => {
    for (const ent of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, ent.name);
      if (ent.isDirectory()) walk(p);
      else if (ent.name.endsWith(".md")) slugs.add(path.basename(ent.name, ".md"));
    }
  };
  walk(base);
  return slugs;
}

function ogCoverName(slug, locale) {
  return `${slug}-og-${locale}.webp`;
}

function hasOgAt(root, section, slug, locale) {
  if (!root) return false;
  return fs.existsSync(path.join(root, section, slug, ogCoverName(slug, locale)));
}

function listStagingCovers() {
  const found = [];
  if (!fs.existsSync(STAGING_ROOT)) return found;
  const walk = (dir, parts) => {
    for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, ent.name);
      if (ent.isDirectory()) walk(p, [...parts, ent.name]);
      else if (/^(.+)-og-(en|zh)\.webp$/i.test(ent.name)) {
        const locale = ent.name.match(/^(.+)-og-(en|zh)\.webp$/i)[2];
        const slugFromFile = ent.name.match(/^(.+)-og-(en|zh)\.webp$/i)[1];
        const [section, slug] = parts;
        found.push({ section, slug: slug || slugFromFile, locale, path: p });
      }
    }
  };
  walk(STAGING_ROOT, []);
  return found;
}

function isProductScreenshot(url) {
  return (
    /\/tools\/[^/]+\/[^/]+\.(jpg|png|webp)$/i.test(url) &&
    !/-og-(en|zh)\.webp$/i.test(url)
  );
}

// --- Staging summary ---
if (scanStaging) {
  const staging = listStagingCovers();
  console.log(`Context staging: ${STAGING_ROOT}`);
  console.log(`Staging covers: ${staging.length}`);
  for (const s of staging) {
    const kb = Math.round(fs.statSync(s.path).size / 1024);
    console.log(`  ${s.section}/${s.slug} ${ogCoverName(s.slug, s.locale)} (${kb} KB)`);
  }
  console.log();
}

// --- Deploy coverage vs legacy maps ---
if (!scanDeploy) {
  process.exit(0);
}

const rows = [];
let deployEn = 0;
let deployZh = 0;
let stagingEn = 0;
let stagingZh = 0;

for (const sec of SECTIONS) {
  const map = readMapSlugs(sec.mapFile);
  const slugs =
    sec.name === "tools"
      ? Object.keys(map)
      : sec.contentDir
        ? [...countContentSlugs(sec.contentDir)]
        : Object.keys(map);

  for (const slug of slugs.sort()) {
    const stEn = hasOgAt(STAGING_ROOT, sec.name, slug, "en");
    const stZh = hasOgAt(STAGING_ROOT, sec.name, slug, "zh");
    const dpEn = hasOgAt(PUBLIC, sec.name, slug, "en");
    const dpZh = hasOgAt(PUBLIC, sec.name, slug, "zh");
    if (stEn) stagingEn++;
    if (stZh) stagingZh++;
    if (dpEn) deployEn++;
    if (dpZh) deployZh++;

    rows.push({
      section: sec.name,
      slug,
      stagingEn: stEn,
      stagingZh: stZh,
      deployEn: dpEn,
      deployZh: dpZh,
      legacyMap: map[slug] || "(none)",
      legacyIsProduct: map[slug] ? isProductScreenshot(map[slug]) : false,
    });
  }
}

const reportDir = path.join(__dirname, "..", "reports");
fs.mkdirSync(reportDir, { recursive: true });
const stamp = new Date().toISOString().slice(0, 10);
const jsonPath = path.join(reportDir, `og-coverage-audit-${stamp}.json`);
fs.writeFileSync(
  jsonPath,
  JSON.stringify({ alignifyCtx: ALIGNIFY_CTX, deployRoot: DEPLOY_ROOT, rows }, null, 2)
);

console.log(`Deploy root: ${DEPLOY_ROOT}`);
console.log(`Pages scanned: ${rows.length}`);
console.log(`Staging en / zh: ${stagingEn} / ${stagingZh}`);
console.log(`Deploy en / zh: ${deployEn} / ${deployZh}`);
console.log(`Report: ${jsonPath}`);

const readyToMigrate = rows.filter((r) => (r.stagingEn || r.stagingZh) && !(r.deployEn && r.deployZh));
if (readyToMigrate.length) {
  console.log("\nReady to migrate (staging exists, not yet on deploy):");
  for (const r of readyToMigrate.slice(0, 20)) {
    const parts = [];
    if (r.stagingEn && !r.deployEn) parts.push("en");
    if (r.stagingZh && !r.deployZh) parts.push("zh");
    if (parts.length) console.log(`  ${r.section}/${r.slug}: ${parts.join(", ")}`);
  }
}
