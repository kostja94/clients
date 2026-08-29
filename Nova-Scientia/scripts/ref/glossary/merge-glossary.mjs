/**
 * Junta partes em scripts/ref/glossary/parts/*.json → 部署仓 content/glossary.json
 * Uso（部署仓根目录）: node ../../clients/Nova-Scientia/scripts/ref/glossary/merge-glossary.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const requireDeploy = createRequire(import.meta.url);
const { getDeployRoot } = requireDeploy(
  path.join(__dirname, "..", "..", "lib", "deploy-root.js")
);
const root = getDeployRoot();
const partsDir = path.join(__dirname, "parts");

const hero = JSON.parse(
  fs.readFileSync(path.join(partsDir, "hero.json"), "utf8")
);
const partFiles = fs
  .readdirSync(partsDir)
  .filter((f) => /^part-\d+\.json$/.test(f))
  .sort();

const categories = [];
for (const f of partFiles) {
  const chunk = JSON.parse(
    fs.readFileSync(path.join(partsDir, f), "utf8")
  );
  if (!Array.isArray(chunk)) {
    throw new Error(`${f} must be a JSON array of categories`);
  }
  categories.push(...chunk);
}

const totalTerms = categories.reduce(
  (n, c) => n + (c.terms?.length ?? 0),
  0
);

const out = {
  ...hero,
  lastUpdated: new Date().toISOString().slice(0, 10),
  termCount: totalTerms,
  categories,
};

fs.writeFileSync(
  path.join(root, "content", "glossary.json"),
  JSON.stringify(out, null, 2) + "\n",
  "utf8"
);

console.log(`OK: ${categories.length} categorias, ${totalTerms} termos → ${path.join(root, "content", "glossary.json")}`);
