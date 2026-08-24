/**
 * Audits zh and en tools page.tsx files for:
 * - ZH: meta title must contain 最佳
 * - EN: meta title must contain "Best" (case-sensitive word boundary avoided — substring Best)
 * - (2026) or （2026） with colon subtitle before | Alignify
 *
 * Run: node scripts/permanent/audit-tools-meta-titles.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "../..");

function walkDir(dir) {
  const out = [];
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory() && !name.name.startsWith(".")) out.push(...walkDir(p));
    else if (name.name === "page.tsx") out.push(p);
  }
  return out;
}

function extractTitles(content) {
  const titles = new Set();
  // const PAGE_TITLE = "..." or multiline
  const single = content.match(
    /const PAGE_TITLE\s*=\s*["'`]([^"'`]+)["'`]/s,
  );
  if (single) titles.add(single[1].replace(/\s+/g, " ").trim());
  const multi = content.match(
    /const PAGE_TITLE\s*=\s*\n\s*["']([^"']*)["']\s*\n\s*["']([^"']*)["']/,
  );
  if (multi) titles.add((multi[1] + multi[2]).replace(/\s+/g, " ").trim());

  for (const m of content.matchAll(/\btitle:\s*"([^"]+)"/g)) {
    titles.add(m[1].trim());
  }
  // seoMetadata.title object
  const sm = content.match(
    /(?:export\s+)?const\s+seoMetadata[^=]*=\s*\{[^}]*title:\s*"([^"]+)"/s,
  );
  if (sm) titles.add(sm[1].trim());
  return [...titles].filter(
    (t) =>
      t &&
      !t.startsWith("http") &&
      t !== "summary_large_image" &&
      t.length > 5,
  );
}

const zhDir = path.join(root, "app/zh/tools");
const enDir = path.join(root, "app/tools");

const issues = { zh: [], en: [] };

for (const file of walkDir(zhDir)) {
  const c = fs.readFileSync(file, "utf8");
  const rel = path.relative(root, file);
  const titles = extractTitles(c);
  for (const t of titles) {
    if (!t.includes("最佳")) issues.zh.push({ file: rel, title: t });
  }
  // year + colon
  for (const t of titles) {
    if (/\| Alignify/.test(t) && /（2026）\s*\|/.test(t)) {
      issues.zh.push({ file: rel, title: t, err: "missing colon block before | Alignify" });
    }
  }
}

for (const file of walkDir(enDir)) {
  const c = fs.readFileSync(file, "utf8");
  const rel = path.relative(root, file);
  const titles = extractTitles(c);
  for (const t of titles) {
    if (!t.includes("Best")) issues.en.push({ file: rel, title: t });
  }
  for (const t of titles) {
    if (/\| Alignify/.test(t) && /\(2026\)\s*\|/.test(t)) {
      issues.en.push({ file: rel, title: t, err: "missing colon block before | Alignify" });
    }
  }
}

function dedup(arr) {
  const m = new Map();
  for (const x of arr) {
    const k = x.file + "\t" + x.title + "\t" + (x.err || "");
    m.set(k, x);
  }
  return [...m.values()];
}

issues.zh = dedup(issues.zh);
issues.en = dedup(issues.en);

const zhBad = issues.zh.filter((x) => !x.err);
const zhYear = issues.zh.filter((x) => x.err);
const enBad = issues.en.filter((x) => !x.err);
const enYear = issues.en.filter((x) => x.err);

console.log(
  JSON.stringify(
    {
      zhMissingZuijia: zhBad,
      zhYearFormat: zhYear,
      enMissingBest: enBad,
      enYearFormat: enYear,
    },
    null,
    2,
  ),
);

const exit =
  zhBad.length + enBad.length + zhYear.length + enYear.length > 0 ? 1 : 0;
process.exit(exit);
