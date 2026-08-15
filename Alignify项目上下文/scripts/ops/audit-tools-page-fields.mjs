/**
 * Audits Tools pages: meta title, meta description, H1, excerpt.
 * - page.tsx: meta title (最佳/Best, year+colon), description length
 * - content/tools/{zh,en}/[slug].json: blogLayout.title, blogLayout.excerpt length
 *
 * Run: node scripts/permanent/audit-tools-page-fields.mjs
 *      node scripts/permanent/audit-tools-page-fields.mjs --json
 * Exit 1: any error; warnings only (default) do not change exit. Use --strict to exit 1 on warn too.
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "../..");

const argv = new Set(process.argv.slice(2));
const jsonOut = argv.has("--json");
const strict = argv.has("--strict");

const lenZh = (s) => (s == null || s === "" ? 0 : [...String(s)].length);
const lenEn = (s) => (s == null || s === "" ? 0 : String(s).length);

/**
 * @param {string} content
 * @returns {{ title?: string, description?: string }}
 */
function extractPageMeta(content) {
  let title;
  let description;

  const ptMulti = content.match(
    /const PAGE_TITLE\s*=\s*\n\s*"([^"]+)"\s*\n\s*"([^"]+)"/,
  );
  if (ptMulti) title = (ptMulti[1] + ptMulti[2]).replace(/\s+/g, " ").trim();
  else {
  const pt = content.match(/const PAGE_TITLE\s*=\s*(?:\n\s*)?"([^"]+)"/s);
  if (pt) title = pt[1].replace(/\s+/g, " ").trim();
  }

  const pdMulti = content.match(
    /const PAGE_DESCRIPTION\s*=\s*\n\s*"([^"]+)"\s*\n\s*"([^"]+)"/,
  );
  if (pdMulti) description = (pdMulti[1] + pdMulti[2]).replace(/\s+/g, " ").trim();
  else {
    const pd = content.match(
      /const PAGE_DESCRIPTION\s*=\s*(?:\n\s*)?"([^"]+)"/s,
    );
    if (pd) description = pd[1].replace(/\s+/g, " ").trim();
  }

  const sm = content.match(
    /const\s+seoMetadata\s*=\s*\{[\s\S]*?title:\s*"([^"]+)"[\s\S]*?description:\s*"([^"]+)"/,
  );
  if (sm) {
    if (!title) title = sm[1].trim();
    if (!description) description = sm[2].trim();
  }

  if (!title) {
    const m = content.match(
      /export const metadata[^{]*\{[\s\S]*?title:\s*"([^"]+)"/,
    );
    if (m) title = m[1].trim();
  }
  if (!title) {
    const m2 = content.match(
      /export const metadata[^{]*\{[\s\S]*?title:\s*seoMetadata\.title/,
    );
    if (m2) {
      const t = content.match(
        /const\s+seoMetadata\s*=\s*\{[\s\S]*?title:\s*"([^"]+)"/,
      );
      if (t) title = t[1].trim();
    }
  }

  if (!description) {
    const m = content.match(
      /export const metadata[^{]*\{[\s\S]*?description:\s*"([^"]+)"/,
    );
    if (m) description = m[1].trim();
  }
  if (!description) {
    const m2 = content.match(
      /export const metadata[^{]*\{[\s\S]*?description:\s*seoMetadata\.description/,
    );
    if (m2) {
      const t = content.match(
        /const\s+seoMetadata\s*=\s*\{[\s\S]*?description:\s*"([^"]+)"/,
      );
      if (t) description = t[1].trim();
    }
  }
  if (!description) {
    const m = content.match(
      /export const metadata[^{]*\{[\s\S]*?description:\s*`([^`]+)`/,
    );
    if (m) description = m[1].replace(/\$\{[^}]+\}/g, "…").trim();
  }

  return { title, description };
}

/**
 * @param {string} locale
 * @param {string} title
 * @param {"error"|"warning"} [severity]
 * @param {string} code
 * @param {string} [detail]
 */
function issue(locale, slug, field, title, severity, code, detail) {
  return { locale, slug, field, pageTitle: title, severity, code, detail };
}

function auditTitleZh(t, rel) {
  const out = [];
  if (!t) {
    out.push(issue("zh", rel, "metaTitle", t, "error", "missing-title", ""));
    return out;
  }
  if (!t.includes("最佳")) {
    out.push(issue("zh", rel, "metaTitle", t, "error", "缺少「最佳」", ""));
  }
  if (/\| Alignify/.test(t) && /（2026）\s*\|/.test(t)) {
    out.push(issue("zh", rel, "metaTitle", t, "error", "year-then-pipe", ""));
  }
  const z = lenZh(t);
  if (z < 20 || z > 38) {
    out.push(issue("zh", rel, "metaTitle", t, "warning", "meta-title-length-zh", `当前 ${z} 字，建议 25–32（容差 20–38）`));
  }
  return out;
}

function auditTitleEn(t, rel) {
  const out = [];
  if (!t) {
    out.push(issue("en", rel, "metaTitle", t, "error", "missing-title", ""));
    return out;
  }
  if (!t.includes("Best")) {
    out.push(issue("en", rel, "metaTitle", t, "error", "missing-Best", ""));
  }
  if (/\| Alignify/.test(t) && /\(2026\)\s*\|/.test(t)) {
    out.push(issue("en", rel, "metaTitle", t, "error", "year-then-pipe", ""));
  }
  const n = lenEn(t);
  if (n < 40 || n > 72) {
    out.push(issue("en", rel, "metaTitle", t, "warning", "meta-title-length-en", `当前 ${n} 字符，建议 50–60（容差 40–72）`));
  }
  return out;
}

function auditDescZh(d, rel) {
  const out = [];
  if (d == null || d === "") {
    out.push(issue("zh", rel, "metaDescription", d, "error", "missing-description", ""));
    return out;
  }
  if (d.includes("…") && d.includes("template")) {
    // placeholder skipped
  }
  const z = lenZh(d);
  if (z < 55) {
    out.push(issue("zh", rel, "metaDescription", d, "error", "meta-desc-too-short-zh", `当前 ${z} 字，目标 ≥60`));
  } else if (z < 60 || z > 88) {
    out.push(issue("zh", rel, "metaDescription", d, "warning", "meta-desc-length-zh", `当前 ${z} 字，建议 60–80（容差至 88）`));
  }
  return out;
}

function auditDescEn(d, rel) {
  const out = [];
  if (d == null || d === "") {
    out.push(issue("en", rel, "metaDescription", d, "error", "missing-description", ""));
    return out;
  }
  const n = lenEn(d);
  if (n < 110) {
    out.push(issue("en", rel, "metaDescription", d, "error", "meta-desc-too-short-en", `当前 ${n} 字符，目标 ≥120`));
  } else if (n < 120 || n > 168) {
    out.push(issue("en", rel, "metaDescription", d, "warning", "meta-desc-length-en", `当前 ${n} 字符，建议 120–158`));
  }
  return out;
}

function auditH1Zh(t, slug) {
  const out = [];
  if (t == null || t === "") {
    out.push(issue("zh", slug, "H1", t, "error", "missing-h1", "blogLayout.title"));
    return out;
  }
  const z = lenZh(t);
  if (z < 8) {
    out.push(issue("zh", slug, "H1", t, "error", "h1-too-short-zh", String(z)));
  } else if (z < 12 || z > 36) {
    out.push(issue("zh", slug, "H1", t, "warning", "h1-length-zh", `当前 ${z} 字，建议 14–22、允许至约 36（含副标题/年份）`));
  }
  return out;
}

function auditH1En(t, slug) {
  const out = [];
  if (t == null || t === "") {
    out.push(issue("en", slug, "H1", t, "error", "missing-h1", "blogLayout.title"));
    return out;
  }
  const n = lenEn(t);
  if (n < 25) {
    out.push(issue("en", slug, "H1", t, "error", "h1-too-short-en", String(n)));
  } else if (n < 38 || n > 85) {
    out.push(issue("en", slug, "H1", t, "warning", "h1-length-en", `当前 ${n} 字符，建议 40–60、允许至约 85`));
  }
  return out;
}

function auditExcerptZh(t, slug) {
  const out = [];
  if (t == null || t === "") {
    out.push(issue("zh", slug, "excerpt", t, "error", "missing-excerpt", "blogLayout.excerpt"));
    return out;
  }
  const z = lenZh(t);
  if (z < 60) {
    out.push(issue("zh", slug, "excerpt", t, "error", "excerpt-too-short-zh", String(z)));
  } else if (z < 90 || z > 180) {
    out.push(issue("zh", slug, "excerpt", t, "warning", "excerpt-length-zh", `当前 ${z} 字，建议 100–150（容差 90–180）`));
  }
  return out;
}

function auditExcerptEn(t, slug) {
  const out = [];
  if (t == null || t === "") {
    out.push(issue("en", slug, "excerpt", t, "error", "missing-excerpt", "blogLayout.excerpt"));
    return out;
  }
  const n = lenEn(t);
  if (n < 150) {
    out.push(issue("en", slug, "excerpt", t, "error", "excerpt-too-short-en", String(n)));
  } else if (n < 200 || n > 280) {
    out.push(issue("en", slug, "excerpt", t, "warning", "excerpt-length-en", `当前 ${n} 字符，建议 200–250`));
  }
  return out;
}

// --- run ---

const allIssues = [];

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, "utf8"));
}

// Hub pages: tools index (no content/tools JSON for hub)
for (const hub of [
  [path.join(root, "app/zh/tools/page.tsx"), "zh", "app/zh/tools/page.tsx"],
  [path.join(root, "app/tools/page.tsx"), "en", "app/tools/page.tsx"],
]) {
  const [fpath, loc] = hub;
  if (!fs.existsSync(fpath)) continue;
  const c = fs.readFileSync(fpath, "utf8");
  const { title, description } = extractPageMeta(c);
  if (loc === "zh") {
    allIssues.push(...auditTitleZh(title, hub[2]), ...auditDescZh(description, hub[2]));
  } else {
    allIssues.push(...auditTitleEn(title, hub[2]), ...auditDescEn(description, hub[2]));
  }
}

for (const loc of ["zh", "en"]) {
  const dir = path.join(root, "content", "tools", loc);
  if (!fs.existsSync(dir)) continue;
  for (const name of fs.readdirSync(dir)) {
    if (!name.endsWith(".json")) continue;
    const slug = name.replace(/\.json$/, "");
    const jsonPath = path.join(dir, name);
    const pagePath = path.join(
      root,
      "app",
      loc === "zh" ? "zh/tools" : "tools",
      slug,
      "page.tsx",
    );
    if (!fs.existsSync(pagePath)) {
      allIssues.push({
        locale: loc,
        slug,
        field: "page",
        severity: "warning",
        code: "missing-page-tsx",
        detail: `No ${path.relative(root, pagePath)}`,
      });
      continue;
    }
    const doc = readJson(jsonPath);
    const bl = doc.blogLayout || {};
    const h1 = bl.title;
    const ex = bl.excerpt;
    const page = fs.readFileSync(pagePath, "utf8");
    const { title: metaTitle, description: metaDesc } = extractPageMeta(page);

    if (loc === "zh") {
      allIssues.push(
        ...auditTitleZh(metaTitle, `tools/zh/${slug}`),
        ...auditDescZh(metaDesc, `tools/zh/${slug}`),
        ...auditH1Zh(h1, slug),
        ...auditExcerptZh(ex, slug),
      );
    } else {
      allIssues.push(
        ...auditTitleEn(metaTitle, `tools/en/${slug}`),
        ...auditDescEn(metaDesc, `tools/en/${slug}`),
        ...auditH1En(h1, slug),
        ...auditExcerptEn(ex, slug),
      );
    }
  }
}

const errors = allIssues.filter((i) => i.severity === "error");
const warnings = allIssues.filter((i) => i.severity === "warning");

const out = {
  summary: { errors: errors.length, warnings: warnings.length, total: allIssues.length },
  errors,
  warnings,
};

if (jsonOut) {
  console.log(JSON.stringify(out, null, 2));
} else {
  console.log(
    JSON.stringify(
      {
        ...out.summary,
        errorSample: errors.slice(0, 50),
        warningCount: warnings.length,
      },
      null,
      2,
    ),
  );
  if (errors.length > 50) {
    console.error("More errors: use --json for full list.");
  }
}

const exit = errors.length > 0 || (strict && warnings.length > 0) ? 1 : 0;
process.exit(exit);
