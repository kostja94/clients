/**
 * Validates Tools JSON: parse + /tools/ href uniqueness + TLDR/FAQ slug rules (§1.5).
 * Usage: node scripts/validate-tools-llm-json-links.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");

const files = [
  "content/tools/en/llm-for-coding.json",
  "content/tools/zh/llm-for-coding.json",
  "content/tools/en/llm-for-math.json",
  "content/tools/zh/llm-for-math.json",
  "content/tools/en/multimodal-llm.json",
  "content/tools/zh/multimodal-llm.json",
  "content/tools/en/llm-for-reasoning.json",
  "content/tools/zh/llm-for-reasoning.json",
];

function collectStrings(obj, out = []) {
  if (obj === null || obj === undefined) return out;
  if (typeof obj === "string") {
    out.push(obj);
    return out;
  }
  if (Array.isArray(obj)) {
    for (const x of obj) collectStrings(x, out);
    return out;
  }
  if (typeof obj === "object") {
    for (const k of Object.keys(obj)) collectStrings(obj[k], out);
  }
  return out;
}

function extractTldrItems(blocks) {
  const tldr = blocks.find((b) => b.type === "tldr");
  return tldr?.items ?? tldr?.data?.items ?? [];
}

function extractFaqAnswers(blocks) {
  const faq = blocks.find((b) => b.type === "faq");
  const items = faq?.items ?? faq?.data?.faqs ?? [];
  return items.map((f) => f.answer ?? "");
}

function hrefSlugs(html, localePrefix) {
  const re = new RegExp(`href="${localePrefix}/tools/([^"#/]+)"`, "g");
  const slugs = [];
  let m;
  while ((m = re.exec(html)) !== null) slugs.push(m[1]);
  return slugs;
}

let errors = [];

for (const rel of files) {
  const full = path.join(root, rel);
  let json;
  try {
    json = JSON.parse(fs.readFileSync(full, "utf8"));
  } catch (e) {
    errors.push(`${rel}: JSON.parse failed — ${e.message}`);
    continue;
  }

  const blocks = json.blogLayout?.blocks ?? json.blocks;
  if (!blocks) {
    errors.push(`${rel}: missing blocks`);
    continue;
  }

  const bodyBlocks = blocks.filter((b) => b.type !== "faq");

  const allText = collectStrings(blocks).join("\n");
  const bodyText = collectStrings(bodyBlocks).join("\n");
  const prefix = rel.includes("/zh/") ? "/zh" : "";

  const hrefRe = new RegExp(`href="${prefix}/tools/([^"#?]+)"`, "g");
  const allHrefs = [];
  let hm;
  while ((hm = hrefRe.exec(allText)) !== null) {
    allHrefs.push(hm[1].replace(/\/$/, ""));
  }

  const counts = {};
  for (const h of allHrefs) counts[h] = (counts[h] || 0) + 1;
  const dup = Object.entries(counts).filter(([, c]) => c > 1);
  if (dup.length) {
    errors.push(`${rel}: duplicate /tools/ href slug(s): ${dup.map(([s, c]) => `${s}×${c}`).join(", ")}`);
  }

  const bodyCounts = {};
  let bm;
  const bodyHrefRe = new RegExp(`href="${prefix}/tools/([^"#?]+)"`, "g");
  while ((bm = bodyHrefRe.exec(bodyText)) !== null) {
    const slug = bm[1].replace(/\/$/, "");
    bodyCounts[slug] = (bodyCounts[slug] || 0) + 1;
  }

  const items = extractTldrItems(blocks);
  const tldrSlugs = new Set();
  let tldrViolations = [];
  items.forEach((item, i) => {
    const slugs = hrefSlugs(item, prefix);
    if (slugs.length > 1) tldrViolations.push(`item ${i + 1} has ${slugs.length} links`);
    slugs.forEach((s) => tldrSlugs.add(s));
  });
  if (tldrSlugs.size > 2) tldrViolations.push(`TLDR distinct slugs ${tldrSlugs.size} > 2`);
  if (tldrViolations.length) errors.push(`${rel}: TLDR — ${tldrViolations.join("; ")}`);

  const faqAnswers = extractFaqAnswers(blocks);
  const faqSlugs = new Set();
  for (const ans of faqAnswers) {
    const sl = hrefSlugs(ans, prefix);
    sl.forEach((s) => faqSlugs.add(s));
  }
  if (faqSlugs.size > 3) errors.push(`${rel}: FAQ distinct slugs ${faqSlugs.size} > 3`);

  const overlap = [...faqSlugs].filter((s) => bodyCounts[s]);
  if (overlap.length) errors.push(`${rel}: FAQ slug(s) also in body (must be unique): ${overlap.join(", ")}`);
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}
console.log("OK: 8 JSON files parsed; href unique; TLDR ≤2 slugs; FAQ ≤3 and disjoint from body.");
