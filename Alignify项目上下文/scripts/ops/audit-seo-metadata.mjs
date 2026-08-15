/**
 * SEO 页 metadata 审计：提取 title、description，检测重复与超长
 * 依据：content/sections/section-seo.md
 * 规范：title 唯一 50-60 字符(EN)/25-32 字(ZH)；description ~105 字符(EN)/60-80 字(ZH)
 *
 * 运行：node scripts/permanent/audit-seo-metadata.mjs
 */

import fs from "fs";
import path from "path";

const SEO_DIRS = [
  path.join(process.cwd(), "app/seo"),
  path.join(process.cwd(), "app/zh/seo"),
];

function walkDir(dir, files = []) {
  if (!fs.existsSync(dir)) return files;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walkDir(full, files);
    else if (e.name === "page.tsx") files.push(full);
  }
  return files;
}

function extractMetadata(filePath) {
  const content = fs.readFileSync(filePath, "utf-8");
  const titleMatch = content.match(/title:\s*["']([^"']+)["']/);
  const descMatch = content.match(/description:\s*["']([^"']+)["']/);
  const title = titleMatch ? titleMatch[1] : "";
  const description = descMatch ? descMatch[1] : "";
  const relPath = filePath
    .replace(process.cwd(), "")
    .replace(/\\/g, "/")
    .replace(/^\/app/, "")
    .replace(/\\/g, "/");
  const isZh = relPath.includes("/zh/seo");
  return {
    path: relPath,
    title,
    titleLen: title.length,
    description,
    descLen: description.length,
    isZh,
  };
}

function countChineseChars(str) {
  return (str.match(/[\u4e00-\u9fff]/g) || []).length;
}

const allFiles = SEO_DIRS.flatMap((d) => walkDir(d));
const results = allFiles.map((f) => extractMetadata(f));

const titleMap = new Map();
const descMap = new Map();
const issues = [];

for (const r of results) {
  const titleKey = r.title.toLowerCase().trim();
  if (titleMap.has(titleKey)) {
    titleMap.get(titleKey).push(r.path);
  } else {
    titleMap.set(titleKey, [r.path]);
  }
  const descKey = r.description.slice(0, 80);
  if (descMap.has(descKey)) {
    descMap.get(descKey).push(r.path);
  } else {
    descMap.set(descKey, [r.path]);
  }
}

for (const [title, paths] of titleMap) {
  if (paths.length > 1) {
    issues.push({ type: "title_dup", value: title, paths });
  }
}

for (const [desc, paths] of descMap) {
  if (paths.length > 1) {
    issues.push({ type: "desc_dup", value: desc.slice(0, 40) + "...", paths });
  }
}

for (const r of results) {
  if (r.isZh) {
    if (r.titleLen > 0 && (r.titleLen < 20 || r.titleLen > 40)) {
      issues.push({
        type: "title_len_zh",
        path: r.path,
        len: r.titleLen,
        expected: "25-32 字",
      });
    }
    if (r.descLen > 0 && (r.descLen < 50 || r.descLen > 100)) {
      issues.push({
        type: "desc_len_zh",
        path: r.path,
        len: r.descLen,
        expected: "60-80 字",
      });
    }
  } else {
    if (r.titleLen > 0 && (r.titleLen < 40 || r.titleLen > 70)) {
      issues.push({
        type: "title_len_en",
        path: r.path,
        len: r.titleLen,
        expected: "50-60 chars",
      });
    }
    if (r.descLen > 0 && (r.descLen < 90 || r.descLen > 130)) {
      issues.push({
        type: "desc_len_en",
        path: r.path,
        len: r.descLen,
        expected: "~105 chars",
      });
    }
  }
}

console.log("=== SEO Metadata Audit ===\n");
console.log("Total pages:", results.length);
console.log("\n--- By path ---");
results.forEach((r) => {
  const zh = r.isZh ? "[ZH]" : "[EN]";
  console.log(`${zh} ${r.path}`);
  console.log(`  title: ${r.titleLen} chars - ${r.title.slice(0, 50)}${r.title.length > 50 ? "..." : ""}`);
  console.log(`  desc:  ${r.descLen} chars - ${r.description.slice(0, 50)}${r.description.length > 50 ? "..." : ""}`);
});

if (issues.length > 0) {
  console.log("\n--- Issues ---");
  issues.forEach((i) => {
    if (i.type === "title_dup" || i.type === "desc_dup") {
      console.log(`[${i.type}] ${i.value}`);
      console.log(`  paths: ${i.paths.join(", ")}`);
    } else {
      console.log(`[${i.type}] ${i.path}: len=${i.len} (expected ${i.expected})`);
    }
  });
} else {
  console.log("\n✓ No duplicate titles/descriptions or length issues found.");
}
