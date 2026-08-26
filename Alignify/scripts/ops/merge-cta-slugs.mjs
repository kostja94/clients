#!/usr/bin/env node
/**
 * Merge slug CTA entries into deploy repo cta-config.json.
 * Usage:
 *   node merge-cta-slugs.mjs --batch path/to/batch.json
 *   node merge-cta-slugs.mjs --check   # list slugs missing from cta-config
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const DEPLOY_ROOTS = [
  process.env.ALIGNIFY_DEPLOY_ROOT,
  "E:\\自有部署项目\\alignify production",
  "D:\\部署项目\\alignify-by-kostja",
].filter(Boolean);

function resolveDeployRoot() {
  for (const root of DEPLOY_ROOTS) {
    const cfg = path.join(root, "src", "data", "cta-config.json");
    if (fs.existsSync(cfg)) return root;
  }
  throw new Error("Deploy root not found; set ALIGNIFY_DEPLOY_ROOT");
}

function listMissingSlugs(deployRoot) {
  const cfg = JSON.parse(
    fs.readFileSync(path.join(deployRoot, "src/data/cta-config.json"), "utf8")
  );
  const channels = ["blog", "marketing", "tools", "seo", "insights", "events", "glossary"];
  const missing = new Set();
  for (const ch of channels) {
    for (const loc of ["en", "zh"]) {
      const dir = path.join(deployRoot, "content", ch, loc);
      if (!fs.existsSync(dir)) continue;
      for (const f of fs.readdirSync(dir)) {
        if (!f.endsWith(".md")) continue;
        const slug = f.replace(/\.md$/, "");
        if (!cfg.slugs[slug]) missing.add(slug);
      }
    }
  }
  return [...missing].sort();
}

function mergeBatch(deployRoot, batchPath) {
  const cfgPath = path.join(deployRoot, "src/data/cta-config.json");
  const cfg = JSON.parse(fs.readFileSync(cfgPath, "utf8"));
  const batch = JSON.parse(fs.readFileSync(batchPath, "utf8"));
  let added = 0;
  let updated = 0;
  for (const [slug, entry] of Object.entries(batch)) {
    if (!entry?.zh?.title || !entry?.en?.title) {
      throw new Error(`Invalid entry for slug "${slug}"`);
    }
    if (cfg.slugs[slug]) updated++;
    else added++;
    cfg.slugs[slug] = entry;
  }
  const sorted = Object.keys(cfg.slugs)
    .sort()
    .reduce((acc, k) => {
      acc[k] = cfg.slugs[k];
      return acc;
    }, {});
  cfg.slugs = sorted;
  fs.writeFileSync(cfgPath, JSON.stringify(cfg, null, 2) + "\n", "utf8");
  console.log(`Merged ${Object.keys(batch).length} slugs (${added} new, ${updated} updated)`);
  const stillMissing = listMissingSlugs(deployRoot);
  if (stillMissing.length) {
    console.log(`Still missing (${stillMissing.length}):`);
    stillMissing.forEach((s) => console.log(`  - ${s}`));
  } else {
    console.log("All content slugs have CTA entries.");
  }
}

const deployRoot = resolveDeployRoot();
const args = process.argv.slice(2);
if (args[0] === "--check") {
  const missing = listMissingSlugs(deployRoot);
  console.log(`Missing: ${missing.length}`);
  missing.forEach((s) => console.log(s));
  process.exit(missing.length ? 1 : 0);
}
if (args[0] === "--batch" && args[1]) {
  mergeBatch(deployRoot, path.resolve(args[1]));
} else {
  console.error("Usage: merge-cta-slugs.mjs --batch <batch.json> | --check");
  process.exit(1);
}
