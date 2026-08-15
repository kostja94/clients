/**
 * Simula categorias para todos os produtos (hero.tags → deriveProductCategoryFromTags).
 * Uso（部署仓根目录）: npx tsx ../../项目文档/Nova-Scientia项目上下文/scripts/audit/simulate-product-categories.ts
 */
import fs from "fs";
import path from "path";
import { fileURLToPath, pathToFileURL } from "url";
import { createRequire } from "module";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const requireDeploy = createRequire(import.meta.url);
const { getDeployRoot } = requireDeploy(
  path.join(__dirname, "..", "lib", "deploy-root.js")
);

const deployRoot = getDeployRoot();
const mod = await import(
  pathToFileURL(
    path.join(deployRoot, "src/lib/content/product-tag-categories.ts")
  ).href
);
const {
  deriveProductCategoryFromTags,
  normalizeHeroTag,
  TAG_ALIAS_ROWS,
} = mod;

const dir = path.join(deployRoot, "content/products");
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"));

const known = new Set(
  TAG_ALIAS_ROWS.map(([label]: [string, string]) => normalizeHeroTag(label))
);

const byCat: Record<string, number> = {};
const list: { slug: string; cat: string; tags: string[] }[] = [];
for (const f of files) {
  const j = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  const tags = j.content?.hero?.tags || [];
  const cat = deriveProductCategoryFromTags(tags);
  byCat[cat] = (byCat[cat] || 0) + 1;
  list.push({ slug: j.slug, cat, tags });
}
console.log("TOTAL", files.length);
console.log("BY_CATEGORY", byCat);

const noKnownTag = list.filter(
  (x) => !x.tags.some((t) => known.has(normalizeHeroTag(t)))
);
console.log("NO_KNOWN_TAG_ALIAS", noKnownTag.length);
noKnownTag.forEach((x) =>
  console.log("  ", x.slug, "|", x.tags.slice(0, 6).join(" | "))
);
