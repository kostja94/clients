/**
 * Lista tags hero ainda sem alias em TAG_ALIAS_ROWS (product-tag-categories.ts).
 * Run: node scripts/audit-product-tags.js
 */
const fs = require("fs");
const path = require("path");
const { getDeployRoot } = require("../lib/deploy-root");

const src = fs.readFileSync(
  path.join(getDeployRoot(), "src/lib/content/product-tag-categories.ts"),
  "utf8"
);
const i = src.indexOf("export const TAG_ALIAS_ROWS");
const block = src.slice(i);
const arrMatch = /=\s*\[([\s\S]*)\]\s*as const/.exec(block);
if (!arrMatch) throw new Error("TAG_ALIAS_ROWS array not found");
const body = arrMatch[1];
const TAG_TO_CATEGORY = {};
for (const line of body.split("\n")) {
  const m = /^\s*\["([^"]+)",\s*"([a-z0-9-]+)"\]\s*,?\s*$/.exec(line);
  if (m) TAG_TO_CATEGORY[m[1]] = m[2];
}

function normalize(tag) {
  return tag.trim().normalize("NFC").toLowerCase();
}
const known = new Set(Object.keys(TAG_TO_CATEGORY).map(normalize));

const dir = path.join(getDeployRoot(), "content/products");
const files = fs.readdirSync(dir).filter((f) => f.endsWith(".json"));

const freq = {};
const firstUnmapped = {};
for (const f of files) {
  const j = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  const tags = j.content?.hero?.tags || [];
  for (const t of tags) {
    if (!known.has(normalize(t))) freq[t] = (freq[t] || 0) + 1;
  }
  const first = tags.find((t) => known.has(normalize(t)));
  const firstBad = tags.find((t) => !known.has(normalize(t)));
  if (firstBad && (!first || tags.indexOf(firstBad) < tags.indexOf(first)))
    firstUnmapped[firstBad] = (firstUnmapped[firstBad] || 0) + 1;
}

const top = Object.entries(freq).sort((a, b) => b[1] - a[1]);
console.log("UNMAPPED_TAG_COUNT", top.length);
console.log("\n--- TOP 40 unmapped by frequency ---");
top.slice(0, 40).forEach(([t, n]) => console.log(`${n}\t${t}`));

console.log("\n--- Often FIRST unmapped ---");
Object.entries(firstUnmapped)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 30)
  .forEach(([t, n]) => console.log(`${n}\t${t}`));
