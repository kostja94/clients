#!/usr/bin/env node
/**
 * Tools product image audit — scans content/tools JSON for:
 * missing files, filename mismatches, low quality, locale drift, YouTube migration candidates.
 *
 * Usage (from alignify-by-kostja or with ALIGNIFY_DEPLOY_ROOT):
 *   node ../../项目文档/Alignify项目上下文/scripts/audit/audit-tools-images.mjs
 *   node .../audit-tools-images.mjs --page search-engine --severity P0
 *   node .../audit-tools-images.mjs --json reports/tools-images-audit.json
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const args = process.argv.slice(2);
const jsonOutIdx = args.indexOf("--json");
const jsonOut =
  jsonOutIdx >= 0 ? args[jsonOutIdx + 1] : null;
const pageFilter = args.includes("--page")
  ? args[args.indexOf("--page") + 1]
  : null;
const severityFilter = args.includes("--severity")
  ? args[args.indexOf("--severity") + 1]
  : null;

const DEPLOY_ROOT =
  process.env.ALIGNIFY_DEPLOY_ROOT ||
  (fs.existsSync("D:\\部署项目\\alignify-by-kostja")
    ? "D:\\部署项目\\alignify-by-kostja"
    : process.cwd());

const PUBLIC = path.join(DEPLOY_ROOT, "public");
const CONTENT_TOOLS = path.join(DEPLOY_ROOT, "content", "tools");
const REPORTS_DIR = path.join(__dirname, "..", "reports");

const MIN_SIZE_KB = 40;
const MIN_WIDTH = 900;
const MIN_HEIGHT = 600;
const ASPECT_TARGET = 4 / 3;
const ASPECT_TOLERANCE = 0.15;

/** Known wrong filename → product mappings from manual verification (add when confirmed, remove after fix) */
const KNOWN_MISMATCHES = new Set([]);

function walk(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walk(p, acc);
    else if (ent.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

function normalize(s) {
  return (s || "")
    .toLowerCase()
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "");
}

function tokensFromProduct(id, name) {
  const raw = `${id} ${name}`.toLowerCase();
  const parts = raw.split(/[\s\-_.]+/).filter((t) => t.length > 2);
  const merged = [];
  for (const p of parts) {
    merged.push(normalize(p));
    if (p.includes(".")) merged.push(normalize(p.replace(/\./g, "")));
  }
  return [...new Set(merged.filter(Boolean))];
}

function filenameStem(imageSrc) {
  if (!imageSrc || !imageSrc.startsWith("/")) return "";
  const base = path.basename(imageSrc, path.extname(imageSrc));
  return normalize(base);
}

function filenameMismatch(id, name, imageSrc) {
  if (!imageSrc?.startsWith("/")) return false;
  const stem = filenameStem(imageSrc);
  if (!stem || stem.length < 3) return false;
  const tokens = tokensFromProduct(id, name);
  if (tokens.some((t) => t.length >= 4 && (stem.includes(t) || t.includes(stem))))
    return false;
  if (tokens.some((t) => t.length >= 3 && stem.includes(t.slice(0, 3)))) return false;
  // Short stems that are abbreviations (e.g. "exa" for Exa)
  if (tokens.some((t) => stem === t)) return false;
  return true;
}

function readImageDimensions(filePath) {
  try {
    const buf = fs.readFileSync(filePath);
    // PNG
    if (buf[0] === 0x89 && buf[1] === 0x50) {
      return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
    }
    // JPEG — scan for SOF0/SOF2
    if (buf[0] === 0xff && buf[1] === 0xd8) {
      let i = 2;
      while (i < buf.length - 8) {
        if (buf[i] !== 0xff) {
          i++;
          continue;
        }
        const marker = buf[i + 1];
        if (marker === 0xc0 || marker === 0xc2) {
          return {
            height: buf.readUInt16BE(i + 5),
            width: buf.readUInt16BE(i + 7),
          };
        }
        const len = buf.readUInt16BE(i + 2);
        i += 2 + len;
      }
    }
    // WebP
    if (buf.toString("ascii", 0, 4) === "RIFF" && buf.toString("ascii", 8, 12) === "WEBP") {
      const chunk = buf.toString("ascii", 12, 16);
      if (chunk === "VP8 ") {
        return {
          width: buf.readUInt16LE(26) & 0x3fff,
          height: buf.readUInt16LE(28) & 0x3fff,
        };
      }
    }
  } catch {
    /* ignore */
  }
  return null;
}

function isYoutube(src) {
  return typeof src === "string" && src.includes("img.youtube.com");
}

function isWebsiteUrl(url) {
  if (!url || typeof url !== "string") return false;
  return /^https?:\/\//i.test(url) && !url.includes("youtube.com");
}

function isLocalPath(src) {
  return typeof src === "string" && src.startsWith("/") && src.trim().length > 0;
}

function canonicalPath(src) {
  return src?.startsWith("/") ? src.slice(1) : null;
}

function collectTools() {
  const byKey = new Map(); // pageSlug:productId -> { en, zh, ... }

  for (const locale of ["en", "zh"]) {
    const dir = path.join(CONTENT_TOOLS, locale);
    for (const file of walk(dir)) {
      const pageSlug = path.basename(file, ".json");
      if (pageFilter && pageSlug !== pageFilter) continue;

      let doc;
      try {
        doc = JSON.parse(fs.readFileSync(file, "utf8"));
      } catch {
        continue;
      }
      if (!doc.blocks) continue;

      for (const block of doc.blocks) {
        if (block.type !== "bestTools" || !block.tools) continue;
        for (const tool of block.tools) {
          const id = tool.id || "";
          const key = `${pageSlug}:${id}`;
          if (!byKey.has(key)) {
            byKey.set(key, {
              pageSlug,
              productId: id,
              name: tool.name,
              linkUrl: tool.linkUrl,
              entries: {},
            });
          }
          const entry = byKey.get(key);
          entry.name = tool.name || entry.name;
          entry.linkUrl = tool.linkUrl || entry.linkUrl;
          entry.entries[locale] = {
            imageSrc: tool.imageSrc || (tool.image && tool.image.src) || "",
            file: path.relative(DEPLOY_ROOT, file),
          };
        }
      }
    }
  }
  return byKey;
}

function audit() {
  const products = collectTools();
  const issues = [];
  const fileUsage = new Map(); // relPath -> [{ pageSlug, productId, name }]

  for (const [key, product] of products) {
    const { pageSlug, productId, name, linkUrl, entries } = product;
    const enSrc = entries.en?.imageSrc ?? "";
    const zhSrc = entries.zh?.imageSrc ?? "";

    // Locale drift
    if (enSrc && zhSrc && enSrc !== zhSrc) {
      issues.push({
        severity: "P1",
        type: "locale_drift",
        key,
        pageSlug,
        productId,
        name,
        detail: `EN "${enSrc}" vs ZH "${zhSrc}"`,
      });
    }

    for (const [locale, { imageSrc, file }] of Object.entries(entries)) {
      if (imageSrc === "") {
        issues.push({
          severity: "P2",
          type: "empty_image",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          detail: "imageSrc is empty string",
        });
        continue;
      }
      if (!imageSrc?.trim()) continue;

      // YouTube migration candidate
      if (isYoutube(imageSrc) && isWebsiteUrl(linkUrl)) {
        issues.push({
          severity: "P2",
          type: "youtube_should_migrate",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          imageSrc,
          linkUrl,
          detail: "Official website exists but image is YouTube thumbnail",
        });
        continue;
      }

      if (!isLocalPath(imageSrc)) continue;

      const rel = canonicalPath(imageSrc);
      const abs = path.join(PUBLIC, rel);
      const mismatchKey = `${key}:${imageSrc}`;

      if (!fileUsage.has(rel)) fileUsage.set(rel, []);
      fileUsage.get(rel).push({ pageSlug, productId, name, locale, key });

      // Missing file
      if (!fs.existsSync(abs)) {
        issues.push({
          severity: "P0",
          type: "missing_file",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          imageSrc,
          outputPath: rel,
          linkUrl,
          detail: `File not found: public/${rel}`,
        });
        continue;
      }

      const stat = fs.statSync(abs);
      const sizeKb = stat.size / 1024;
      const dims = readImageDimensions(abs);

      // Known manual mismatches
      if (KNOWN_MISMATCHES.has(mismatchKey)) {
        issues.push({
          severity: "P0",
          type: "known_mismatch",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          imageSrc,
          outputPath: rel,
          linkUrl,
          detail: "Manually verified wrong product screenshot",
        });
      } else if (filenameMismatch(productId, name, imageSrc)) {
        issues.push({
          severity: "P0",
          type: "filename_mismatch",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          imageSrc,
          outputPath: rel,
          linkUrl,
          detail: `Filename "${path.basename(imageSrc)}" does not match product id/name`,
        });
      }

      if (sizeKb < MIN_SIZE_KB) {
        issues.push({
          severity: "P1",
          type: "low_size",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          imageSrc,
          outputPath: rel,
          linkUrl,
          sizeKb: Math.round(sizeKb),
          detail: `File size ${sizeKb.toFixed(1)} KB < ${MIN_SIZE_KB} KB`,
        });
      }

      if (dims) {
        if (dims.width < MIN_WIDTH || dims.height < MIN_HEIGHT) {
          issues.push({
            severity: "P1",
            type: "low_resolution",
            key,
            pageSlug,
            productId,
            name,
            locale,
            file,
            imageSrc,
            outputPath: rel,
            linkUrl,
            width: dims.width,
            height: dims.height,
            detail: `Resolution ${dims.width}x${dims.height} below ${MIN_WIDTH}x${MIN_HEIGHT}`,
          });
        }
        const ratio = dims.width / dims.height;
        if (Math.abs(ratio - ASPECT_TARGET) / ASPECT_TARGET > ASPECT_TOLERANCE) {
          issues.push({
            severity: "P1",
            type: "aspect_ratio",
            key,
            pageSlug,
            productId,
            name,
            locale,
            file,
            imageSrc,
            outputPath: rel,
            width: dims.width,
            height: dims.height,
            detail: `Aspect ratio ${ratio.toFixed(2)} deviates from 4:3`,
          });
        }
      }

      // Path convention INFO
      const expected = `tools/${pageSlug}/${productId}.jpg`;
      if (!imageSrc.includes(expected) && !imageSrc.startsWith("/seo/")) {
        issues.push({
          severity: "INFO",
          type: "nonstandard_path",
          key,
          pageSlug,
          productId,
          name,
          locale,
          file,
          imageSrc,
          detail: `Expected convention /tools/${pageSlug}/${productId}.jpg`,
        });
      }
    }
  }

  // Shared file across different products on same page
  for (const [rel, users] of fileUsage) {
    const byPage = new Map();
    for (const u of users) {
      if (!byPage.has(u.pageSlug)) byPage.set(u.pageSlug, new Map());
      const m = byPage.get(u.pageSlug);
      if (!m.has(u.productId)) m.set(u.productId, u);
    }
    for (const [pageSlug, idMap] of byPage) {
      if (idMap.size > 1) {
        const ids = [...idMap.values()];
        issues.push({
          severity: "P0",
          type: "shared_file",
          key: `${pageSlug}:*`,
          pageSlug,
          productId: ids.map((x) => x.productId).join(", "),
          name: ids.map((x) => x.name).join(" / "),
          imageSrc: `/${rel}`,
          outputPath: rel,
          detail: `${idMap.size} products on ${pageSlug} share ${rel}`,
        });
      }
    }
  }

  // Deduplicate by key+type+locale+imageSrc
  const seen = new Set();
  const deduped = issues.filter((i) => {
    const k = `${i.key}|${i.type}|${i.locale || ""}|${i.imageSrc || ""}`;
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  let filtered = deduped;
  if (severityFilter) {
    filtered = filtered.filter((i) => i.severity === severityFilter);
  }

  const summary = {
    generatedAt: new Date().toISOString(),
    deployRoot: DEPLOY_ROOT,
    totalProducts: products.size,
    totalIssues: filtered.length,
    bySeverity: {},
    byType: {},
    issues: filtered,
  };

  for (const i of filtered) {
    summary.bySeverity[i.severity] = (summary.bySeverity[i.severity] || 0) + 1;
    summary.byType[i.type] = (summary.byType[i.type] || 0) + 1;
  }

  return summary;
}

function writeReports(summary) {
  fs.mkdirSync(REPORTS_DIR, { recursive: true });
  const date = new Date().toISOString().slice(0, 10);
  const jsonPath =
    jsonOut || path.join(REPORTS_DIR, `tools-images-audit-${date}.json`);
  const mdPath = jsonPath.replace(/\.json$/, ".md");

  fs.writeFileSync(jsonPath, JSON.stringify(summary, null, 2), "utf8");

  const lines = [
    `# Tools Images Audit`,
    ``,
    `**Generated**: ${summary.generatedAt}`,
    `**Deploy root**: \`${summary.deployRoot}\``,
    `**Products scanned**: ${summary.totalProducts}`,
    `**Issues**: ${summary.totalIssues}`,
    ``,
    `## By severity`,
    ``,
    `| Severity | Count |`,
    `|----------|-------|`,
  ];
  for (const [sev, count] of Object.entries(summary.bySeverity).sort()) {
    lines.push(`| ${sev} | ${count} |`);
  }
  lines.push(``, `## By type`, ``, `| Type | Count |`, `|------|-------|`);
  for (const [t, count] of Object.entries(summary.byType).sort()) {
    lines.push(`| ${t} | ${count} |`);
  }

  for (const sev of ["P0", "P1", "P2", "INFO"]) {
    const group = summary.issues.filter((i) => i.severity === sev);
    if (!group.length) continue;
    lines.push(``, `## ${sev} (${group.length})`, ``);
    for (const i of group.slice(0, 200)) {
      lines.push(
        `- **${i.pageSlug}** / \`${i.productId}\` (${i.name}): ${i.detail}`
      );
      if (i.imageSrc) lines.push(`  - image: \`${i.imageSrc}\``);
    }
    if (group.length > 200) {
      lines.push(`- ... and ${group.length - 200} more`);
    }
  }

  fs.writeFileSync(mdPath, lines.join("\n"), "utf8");
  return { jsonPath, mdPath };
}

const summary = audit();
const { jsonPath, mdPath } = writeReports(summary);

console.log(`Tools Images Audit`);
console.log(`${"=".repeat(50)}`);
console.log(`Products: ${summary.totalProducts}`);
console.log(`Issues:   ${summary.totalIssues}`);
for (const [sev, n] of Object.entries(summary.bySeverity).sort()) {
  console.log(`  ${sev}: ${n}`);
}
console.log(`\nJSON: ${jsonPath}`);
console.log(`MD:   ${mdPath}`);

process.exit(summary.issues.some((i) => i.severity === "P0") ? 1 : 0);
