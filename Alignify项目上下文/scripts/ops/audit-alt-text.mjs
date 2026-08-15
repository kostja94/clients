// Scan content JSON files for alt text quality issues.
// Checks: missing alt, too short, too long, generic filler words,
// HTML <img> tags, and locale mismatch (English alt on ZH pages).
// Usage: node scripts/permanent/audit-alt-text.mjs
//        node scripts/permanent/audit-alt-text.mjs --json report.json

import fs from "fs";
import path from "path";

const jsonOut = process.argv.includes("--json")
  ? process.argv[process.argv.indexOf("--json") + 1]
  : null;

function walk(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) walk(p, acc);
    else if (name.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

// Only flag genuinely meaningless filler — "showing geometry", "showing metrics" etc. are descriptive
const FILLER_WORDS = []; // No mechanical filler words remain — interface is now descriptive (e.g. "conversation interface", "editing interface")
const MIN_ALT_LENGTH_EN = 20; // chars for English
const MIN_ALT_LENGTH_ZH = 12; // chars for Chinese
const MAX_ALT_LENGTH = 125; // chars - screen reader truncation threshold

function isEnglishText(text) {
  // Heuristic: >70% ASCII characters = English
  const ascii = text.replace(/[^\x00-\x7F]/g, "").length;
  return ascii / Math.max(text.length, 1) > 0.7;
}

function hasChineseChar(text) {
  return /[一-鿿]/.test(text);
}

function stripHtml(s) {
  return s.replace(/<[^>]+>/g, " ").replace(/&[a-z]+;/gi, " ").replace(/\s+/g, " ").trim();
}

const roots = ["content/tools", "content/seo", "content/marketing", "content/insights"];
const files = roots.flatMap((r) => {
  const full = path.join(process.cwd(), r);
  return walk(full);
});

const issues = [];
let totalAlts = 0;
let totalImgs = 0;

for (const file of files) {
  let j;
  try { j = JSON.parse(fs.readFileSync(file, "utf8")); } catch { continue; }
  if (!j.blocks) continue;

  const relPath = path.relative(process.cwd(), file);
  const isZh = file.includes(`${path.sep}zh${path.sep}`);

  // --- Check BestTools imageAlt ---
  for (const block of j.blocks) {
    if (block.type !== "bestTools") continue;
    if (!block.tools) continue;

    for (const tool of block.tools) {
      // Skip tools without images
      const imgSrc = tool.imageSrc || (tool.image && tool.image.src) || "";
      if (!imgSrc || !imgSrc.trim()) continue;

      totalAlts++;
      const alt = tool.imageAlt || "";
      const name = tool.name || "?";

      // 1. Missing alt
      if (!alt) {
        issues.push({
          file: relPath,
          type: "missing",
          tool: name,
          detail: "No imageAlt field — will use fallback //{name} interface//",
        });
        continue;
      }

      // 2. Too short (locale-aware threshold)
      const minLen = isZh ? MIN_ALT_LENGTH_ZH : MIN_ALT_LENGTH_EN;
      if (alt.length < minLen) {
        issues.push({ file: relPath, type: "too_short", tool: name, detail: `${alt.length} chars (min ${minLen}): "${alt}"` });
      }

      // 3. Too long
      if (alt.length > MAX_ALT_LENGTH) {
        issues.push({ file: relPath, type: "too_long", tool: name, detail: `${alt.length} chars: "${alt.slice(0, 60)}..."` });
      }

      // 4. Filler words — mechanical fillers were eliminated in May 2026 alt text rewrite
      for (const fw of FILLER_WORDS) {
        const lowerAlt = alt.toLowerCase();
        if (lowerAlt.includes(fw.toLowerCase())) {
          issues.push({ file: relPath, type: "filler", tool: name, detail: `contains "${fw}": "${alt.slice(0, 80)}..."` });
          break;
        }
      }

      // 5. Locale mismatch: ZH page with English alt
      if (isZh && isEnglishText(alt) && !hasChineseChar(alt)) {
        issues.push({ file: relPath, type: "locale", tool: name, detail: `English alt on ZH page: "${alt.slice(0, 60)}..."` });
      }
    }
  }

  // --- Check HTML <img> tags in childrenHtml and heroHtml ---
  const heroHtml = j.blogLayout?.heroHtml || "";
  for (const block of j.blocks) {
    for (const field of ["childrenHtml", "heroHtml"]) {
      const html = block[field] || "";
      if (typeof html !== "string" || !html) continue;

      const imgMatches = html.match(/<img[^>]*>/gi) || [];
      totalImgs += imgMatches.length;

      for (const img of imgMatches) {
        // Check for alt attribute
        const altMatch = img.match(/alt="([^"]*)"/i);
        if (!altMatch) {
          issues.push({
            file: relPath,
            type: "img_no_alt",
            detail: `<img> missing alt attribute in ${field}`,
          });
          continue;
        }
        const altVal = altMatch[1];
        // Empty alt is OK for decorative images
        if (altVal === "") continue;

        // Filler words in HTML alt
        for (const fw of FILLER_WORDS.slice(0, 6)) {
          if (altVal.toLowerCase().includes(fw.toLowerCase())) {
            issues.push({
              file: relPath,
              type: "img_filler",
              detail: `alt="${fw}..." in ${field}: "${altVal.slice(0, 60)}..."`,
            });
            break;
          }
        }

        // English on ZH page
        if (isZh && isEnglishText(altVal) && !hasChineseChar(altVal) && altVal.length > 10) {
          issues.push({
            file: relPath,
            type: "img_locale",
            detail: `English alt on ZH page in ${field}: "${altVal.slice(0, 60)}..."`,
          });
        }
      }
    }
  }
}

// Sort: by type priority then file
const typeOrder = { missing: 0, img_no_alt: 1, too_short: 2, filler: 3, img_filler: 4, too_long: 5, locale: 6, img_locale: 7 };
issues.sort((a, b) => {
  const ta = typeOrder[a.type] ?? 99;
  const tb = typeOrder[b.type] ?? 99;
  if (ta !== tb) return ta - tb;
  return a.file.localeCompare(b.file);
});

// Report
console.log(`Total BestTools images with alt: ${totalAlts}`);
console.log(`Total HTML <img> tags in content: ${totalImgs}`);

const typeLabels = {
  missing: "Missing imageAlt (no fallback quality)",
  img_no_alt: "HTML <img> missing alt attribute",
  too_short: "Alt too short (<20 chars, likely generic)",
  filler: "Alt contains filler words (interface/screenshot/etc)",
  img_filler: "HTML <img> alt contains filler words",
  too_long: "Alt too long (>125 chars, screen reader cutoff)",
  locale: "English alt on Chinese page (BestTools)",
  img_locale: "English alt on Chinese page (HTML <img>)",
};

if (issues.length === 0) {
  console.log("\n✅ No alt text issues found!");
} else {
  console.log(`\n❌ ${issues.length} issues found:\n`);
  let currentType = null;
  for (const issue of issues) {
    if (issue.type !== currentType) {
      currentType = issue.type;
      console.log(`\n  [${typeLabels[issue.type] || issue.type}]`);
    }
    const toolInfo = issue.tool ? ` [${issue.tool}]` : "";
    console.log(`    ${issue.file}${toolInfo}: ${issue.detail}`);
  }
}

// Stats by type
const byType = {};
for (const issue of issues) {
  byType[issue.type] = (byType[issue.type] || 0) + 1;
}
console.log("\n--- Summary ---");
for (const [type, count] of Object.entries(byType)) {
  console.log(`  ${type}: ${count}`);
}

// JSON output
if (jsonOut) {
  fs.writeFileSync(jsonOut, JSON.stringify(issues, null, 2));
  console.log(`\nReport saved to ${jsonOut}`);
}

process.exit(issues.length > 0 ? 1 : 0);
