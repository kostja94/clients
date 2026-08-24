#!/usr/bin/env node
/**
 * Tools product URL audit — scans content/tools JSON bestTools linkUrl,
 * HTTP-checks each URL, flags dead/parked sites, optional web search verification.
 *
 * Usage (from deploy repo or with ALIGNIFY_DEPLOY_ROOT):
 *   node ../../clients/Alignify/scripts/audit/audit-tools-product-urls.mjs
 *   node .../audit-tools-product-urls.mjs --json reports/tools-product-url-audit.json
 *   node .../audit-tools-product-urls.mjs --no-web-verify
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const args = process.argv.slice(2);
const jsonOutIdx = args.indexOf("--json");
const jsonOut = jsonOutIdx >= 0 ? args[jsonOutIdx + 1] : null;
const pageFilter = args.includes("--page")
  ? args[args.indexOf("--page") + 1]
  : null;
const skipWebVerify = args.includes("--no-web-verify");
const concurrency = args.includes("--concurrency")
  ? parseInt(args[args.indexOf("--concurrency") + 1], 10)
  : 8;

const DEPLOY_ROOT =
  process.env.ALIGNIFY_DEPLOY_ROOT ||
  (fs.existsSync("D:\\部署项目\\alignify-by-kostja")
    ? "D:\\部署项目\\alignify-by-kostja"
    : process.cwd());

const CONTENT_TOOLS = path.join(DEPLOY_ROOT, "content", "tools");
const REPORTS_DIR = path.join(__dirname, "..", "reports");

const PARKING_PATTERNS = [
  /domain (is )?(for sale|available|parked)/i,
  /buy this domain/i,
  /this domain has expired/i,
  /service (has been )?(discontinued|shut down|sunset|retired)/i,
  /no longer (available|operating|in service)/i,
  /permanently closed/i,
  /404 not found/i,
  /page not found/i,
  /website is under construction/i,
  /godaddy parking/i,
  /sedo parking/i,
];

const SHUTDOWN_SEARCH_PATTERNS = [
  /shut\s*down/i,
  /sunset/i,
  /discontinued/i,
  /no longer (available|operating|in service)/i,
  /permanently closed/i,
  /service ended/i,
  /acquihir/i,
  /404/i,
  /went offline/i,
  /ceased operations/i,
];

const USER_AGENT =
  "Mozilla/5.0 (compatible; AlignifyToolsUrlAudit/1.0; +https://alignify.co)";

function walk(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walk(p, acc);
    else if (ent.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

function pageSlugFromPath(jsonPath) {
  const rel = path.relative(CONTENT_TOOLS, jsonPath);
  const parts = rel.split(path.sep);
  return parts.length >= 2 ? parts[1].replace(/\.json$/, "") : parts[0];
}

function extractProducts() {
  const products = [];
  const seen = new Set();

  for (const jsonPath of walk(CONTENT_TOOLS)) {
    const locale = jsonPath.includes(`${path.sep}en${path.sep}`) ? "en" : "zh";
    const pageSlug = pageSlugFromPath(jsonPath);
    if (pageFilter && pageSlug !== pageFilter) continue;

    let data;
    try {
      data = JSON.parse(fs.readFileSync(jsonPath, "utf8"));
    } catch {
      continue;
    }

    for (const block of data.blocks || []) {
      if (block.type !== "bestTools" || !Array.isArray(block.tools)) continue;
      for (const tool of block.tools) {
        const linkUrl = (tool.linkUrl || "").trim();
        if (!linkUrl || !/^https?:\/\//i.test(linkUrl)) continue;
        const key = `${pageSlug}:${tool.id || tool.name}:${locale}`;
        if (seen.has(key)) continue;
        seen.add(key);
        products.push({
          key,
          pageSlug,
          locale,
          productId: tool.id || "",
          name: tool.name || "",
          linkUrl,
          sectionId: block.id || "",
        });
      }
    }
  }

  return products;
}

async function fetchWithTimeout(url, method = "GET", timeoutMs = 15000) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const res = await fetch(url, {
      method,
      redirect: "follow",
      signal: controller.signal,
      headers: {
        "User-Agent": USER_AGENT,
        Accept: "text/html,application/xhtml+xml,*/*",
      },
    });
    let body = "";
    if (method === "GET" && res.ok) {
      const text = await res.text();
      body = text.slice(0, 8000);
    }
    return {
      ok: true,
      status: res.status,
      finalUrl: res.url,
      body,
    };
  } catch (err) {
    return {
      ok: false,
      status: 0,
      finalUrl: url,
      error: err.name === "AbortError" ? "timeout" : err.message,
      body: "",
    };
  } finally {
    clearTimeout(timer);
  }
}

function detectParking(body) {
  if (!body) return null;
  for (const re of PARKING_PATTERNS) {
    const m = body.match(re);
    if (m) return m[0].slice(0, 120);
  }
  return null;
}

function classifyHttp(result) {
  if (!result.ok) {
    if (result.error === "timeout") {
      return { suspect: true, reason: "timeout", severity: "suspect" };
    }
    if (/ENOTFOUND|ECONNREFUSED|getaddrinfo/i.test(result.error || "")) {
      return { suspect: true, reason: "dns_or_connection", severity: "suspect" };
    }
    return { suspect: true, reason: result.error || "fetch_error", severity: "suspect" };
  }

  if (result.status === 404 || result.status === 410) {
    return { suspect: true, reason: `http_${result.status}`, severity: "high" };
  }

  const parking = detectParking(result.body);
  if (parking) {
    return { suspect: true, reason: `parking: ${parking}`, severity: "high" };
  }

  if (result.status >= 500) {
    return { suspect: true, reason: `http_${result.status}`, severity: "suspect" };
  }

  return { suspect: false, reason: "ok", severity: "ok" };
}

async function webVerify(productName, linkUrl) {
  const query = encodeURIComponent(
    `"${productName}" shutdown OR discontinued OR sunset 2025 OR 2026`
  );
  const searchUrl = `https://html.duckduckgo.com/html/?q=${query}`;

  try {
    const res = await fetch(searchUrl, {
      headers: { "User-Agent": USER_AGENT },
      signal: AbortSignal.timeout(12000),
    });
    if (!res.ok) {
      return {
        webVerdict: "unverified",
        webNotes: `Search fetch HTTP ${res.status}`,
        recommendation: "manual_review",
      };
    }
    const html = (await res.text()).slice(0, 12000);
    const text = html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ");

    const shutdownHits = SHUTDOWN_SEARCH_PATTERNS.filter((re) => re.test(text));
    const domain = new URL(linkUrl).hostname.replace(/^www\./, "");
    const domainMentioned = text.toLowerCase().includes(domain.toLowerCase());

    if (shutdownHits.length >= 2 || (shutdownHits.length >= 1 && domainMentioned)) {
      return {
        webVerdict: "likely_discontinued",
        webNotes: `Search snippets mention shutdown/discontinued (${shutdownHits.length} signals)`,
        recommendation: "remove_after_confirm",
      };
    }

    if (shutdownHits.length === 1) {
      return {
        webVerdict: "possible_discontinued",
        webNotes: "Weak shutdown signal in search results — verify manually",
        recommendation: "manual_review",
      };
    }

    return {
      webVerdict: "likely_active",
      webNotes: "No strong shutdown signals in search snippets",
      recommendation: "keep_if_http_ok",
    };
  } catch (err) {
    return {
      webVerdict: "unverified",
      webNotes: `Web search failed: ${err.message}`,
      recommendation: "manual_review",
    };
  }
}

async function poolMap(items, limit, fn) {
  const results = new Array(items.length);
  let idx = 0;

  async function worker() {
    while (idx < items.length) {
      const i = idx++;
      results[i] = await fn(items[i], i);
    }
  }

  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, worker));
  return results;
}

async function auditProduct(product) {
  let head = await fetchWithTimeout(product.linkUrl, "HEAD");
  if (!head.ok || head.status === 405 || head.status === 403) {
    head = await fetchWithTimeout(product.linkUrl, "GET");
  } else if (head.ok && head.status >= 200 && head.status < 400 && !head.body) {
    const getResult = await fetchWithTimeout(product.linkUrl, "GET");
    head = { ...head, body: getResult.body };
  }

  const httpClass = classifyHttp(head);
  const entry = {
    ...product,
    httpStatus: head.status || 0,
    finalUrl: head.finalUrl || product.linkUrl,
    httpReason: httpClass.reason,
    suspect: httpClass.suspect,
    severity: httpClass.severity,
    webVerdict: null,
    webNotes: null,
    recommendation: httpClass.suspect ? "manual_review" : "keep",
  };

  if (httpClass.suspect && !skipWebVerify) {
    await new Promise((r) => setTimeout(r, 800 + Math.random() * 400));
    const web = await webVerify(product.name, product.linkUrl);
    entry.webVerdict = web.webVerdict;
    entry.webNotes = web.webNotes;
    if (web.webVerdict === "likely_discontinued") {
      entry.recommendation = "remove_after_confirm";
    } else if (httpClass.severity === "high" && web.webVerdict !== "likely_active") {
      entry.recommendation = "remove_after_confirm";
    } else {
      entry.recommendation = web.recommendation;
    }
  }

  return entry;
}

async function audit() {
  const products = extractProducts();
  console.log(`Scanning ${products.length} product URLs...`);

  const results = await poolMap(products, concurrency, auditProduct);
  const suspects = results.filter((r) => r.suspect);
  const removeCandidates = results.filter(
    (r) => r.recommendation === "remove_after_confirm"
  );

  return {
    generatedAt: new Date().toISOString(),
    deployRoot: DEPLOY_ROOT,
    totalProducts: products.length,
    totalSuspects: suspects.length,
    removeCandidates: removeCandidates.length,
    webVerifyEnabled: !skipWebVerify,
    results: results.sort((a, b) => {
      if (a.suspect !== b.suspect) return a.suspect ? -1 : 1;
      return a.pageSlug.localeCompare(b.pageSlug);
    }),
  };
}

function writeReports(summary) {
  fs.mkdirSync(REPORTS_DIR, { recursive: true });
  const date = new Date().toISOString().slice(0, 10);
  const jsonPath =
    jsonOut || path.join(REPORTS_DIR, `tools-product-url-audit-${date}.json`);
  const mdPath = jsonPath.replace(/\.json$/, ".md");

  fs.writeFileSync(jsonPath, JSON.stringify(summary, null, 2), "utf8");

  const lines = [
    `# Tools Product URL Audit`,
    ``,
    `**Generated**: ${summary.generatedAt}`,
    `**Deploy root**: \`${summary.deployRoot}\``,
    `**Products scanned**: ${summary.totalProducts}`,
    `**Suspect URLs**: ${summary.totalSuspects}`,
    `**Remove candidates (needs your confirm)**: ${summary.removeCandidates}`,
    `**Web verify**: ${summary.webVerifyEnabled ? "enabled" : "disabled"}`,
    ``,
    `> Phind and Clockwise were removed in this session. Other removals require your confirmation.`,
    ``,
    `## Summary by recommendation`,
    ``,
    `| Recommendation | Count |`,
    `|----------------|-------|`,
  ];

  const byRec = {};
  for (const r of summary.results) {
    byRec[r.recommendation] = (byRec[r.recommendation] || 0) + 1;
  }
  for (const [rec, count] of Object.entries(byRec).sort()) {
    lines.push(`| ${rec} | ${count} |`);
  }

  const suspectRows = summary.results.filter((r) => r.suspect);
  if (suspectRows.length) {
    lines.push(
      ``,
      `## Suspect URLs (${suspectRows.length})`,
      ``,
      `| Page | Product | URL | HTTP | Web verdict | Recommendation | Notes |`,
      `|------|---------|-----|------|-------------|----------------|-------|`
    );
    for (const r of suspectRows) {
      lines.push(
        `| ${r.pageSlug} | ${r.name} | ${r.linkUrl} | ${r.httpStatus} (${r.httpReason}) | ${r.webVerdict || "—"} | ${r.recommendation} | ${(r.webNotes || "").replace(/\|/g, "/")} |`
      );
    }
  } else {
    lines.push(``, `## Suspect URLs`, ``, `No suspect URLs detected.`);
  }

  const removeRows = summary.results.filter(
    (r) => r.recommendation === "remove_after_confirm"
  );
  if (removeRows.length) {
    lines.push(
      ``,
      `## Recommended for removal (confirm before deleting)`,
      ``
    );
    for (const r of removeRows) {
      lines.push(
        `- **${r.pageSlug}** / ${r.name} (\`${r.productId}\`): ${r.linkUrl} — ${r.httpReason}; web: ${r.webVerdict}`
      );
    }
  }

  lines.push(
    ``,
    `## All OK (${summary.results.filter((r) => !r.suspect).length})`,
    ``,
    `See JSON for full list.`
  );

  fs.writeFileSync(mdPath, lines.join("\n"), "utf8");
  return { jsonPath, mdPath };
}

const summary = await audit();
const { jsonPath, mdPath } = writeReports(summary);

console.log(`\nTools Product URL Audit`);
console.log(`${"=".repeat(50)}`);
console.log(`Products: ${summary.totalProducts}`);
console.log(`Suspects: ${summary.totalSuspects}`);
console.log(`Remove candidates: ${summary.removeCandidates}`);
console.log(`\nJSON: ${jsonPath}`);
console.log(`MD:   ${mdPath}`);

process.exit(summary.removeCandidates.length > 0 ? 1 : 0);
