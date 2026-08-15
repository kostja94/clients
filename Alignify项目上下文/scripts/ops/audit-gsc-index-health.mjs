/**
 * GSC 索引健康检查脚本：遍历全站页面，调用 URL Inspection API 检查每个页面的索引状态。
 *
 * 运行前提：同 fetch-gsc，需要 config/gsc-key.json 或环境变量，国内需 VPN。
 *
 * 用法：
 *   node scripts/permanent/audit-gsc-index-health.mjs          # 检查全部页面
 *   node scripts/permanent/audit-gsc-index-health.mjs --recent # 仅检查近 7 天修改的页面
 *   node scripts/permanent/audit-gsc-index-health.mjs --batch 5 # 自定义并发数（默认 5）
 *
 * 输出：
 *   1. 索引异常清单（非 submittedAndIndexed 的页面）
 *   2. 索引状态分布统计
 *   3. 按状态分组的 URL 列表，方便批量处理
 *
 * 速率控制：默认 5 req/s，全站约 300+ URL，耗时约 60-70 秒。
 * GSC URL Inspection API 每日配额 2000 次，本脚本全量运行在配额内。
 */

import { google } from "googleapis";
import { readFileSync, writeFileSync, mkdirSync, existsSync, statSync } from "fs";
import { resolve, dirname, relative, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..", "..");
const APP_DIR = resolve(ROOT, "app");
const DATA_DIR = resolve(ROOT, "data");

// ── 参数 ─────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
const RECENT_ONLY = args.includes("--recent");
const batchFlagIdx = args.indexOf("--batch");
const CONCURRENCY =
  batchFlagIdx !== -1 ? parseInt(args[batchFlagIdx + 1], 10) || 5 : 5;

// ── 认证 ─────────────────────────────────────────────────────────────

function getCredentials() {
  const keyPath = resolve(ROOT, "config", "gsc-key.json");
  try {
    const raw = readFileSync(keyPath, "utf-8");
    const parsed = JSON.parse(raw);
    return { client_email: parsed.client_email, private_key: parsed.private_key };
  } catch { /* continue */ }

  const email = process.env.GSC_CLIENT_EMAIL;
  const rawKey = process.env.GSC_PRIVATE_KEY;
  if (email && rawKey) {
    const privateKey = rawKey.includes("\\n") ? rawKey.replace(/\\n/g, "\n") : rawKey;
    return { client_email: email, private_key: privateKey };
  }

  console.error("✗ GSC 认证未配置");
  process.exit(1);
}

function getSiteUrl() {
  const url = process.env.GSC_SITE_URL;
  if (!url) {
    console.error("✗ 缺少 GSC_SITE_URL 环境变量");
    process.exit(1);
  }
  return url.replace(/\/+$/, ""); // 去掉尾部斜杠
}

// ── URL 生成 ─────────────────────────────────────────────────────────

/** 从 tools-pages-config.ts 解析所有工具页 slug */
function parseToolsSlugs() {
  const configPath = resolve(ROOT, "src", "data", "tools-pages-config.ts");
  if (!existsSync(configPath)) {
    console.warn("  ⚠ 未找到 tools-pages-config.ts，跳过工具页");
    return [];
  }

  const content = readFileSync(configPath, "utf-8");
  // 匹配 TOOLS_PAGES 数组中的 slug 值
  const slugRegex = /slug:\s*["']([^"']+)["']/g;
  const slugs = [];
  let match;
  while ((match = slugRegex.exec(content)) !== null) {
    slugs.push(match[1]);
  }
  return [...new Set(slugs)]; // 去重
}

/** 扫描 app/ 目录下所有具体的 page.tsx（排除动态路由和特殊文件） */
function scanAppPageFiles() {
  const entries = [];

  function walk(dir) {
    if (!existsSync(dir)) return;
    const items = readdirSync(dir, { withFileTypes: true });
    for (const item of items) {
      const full = join(dir, item.name);
      const rel = relative(APP_DIR, full);

      // 跳过非页面目录
      if (rel.startsWith("api")) continue;
      if (rel.startsWith("_")) continue;
      if (item.name.startsWith("(")) continue; // route groups
      if (item.name.startsWith("[")) continue; // dynamic segments

      if (item.isDirectory()) {
        walk(full);
      } else if (item.name === "page.tsx" || item.name === "page.mdx") {
        // 排除根 layout 和嵌套 layout
        if (rel === "page.tsx") {
          entries.push({ routePath: "", filePath: full });
        } else {
          const routePath = rel.replace(/\/page\.(tsx|mdx)$/, "");
          entries.push({ routePath, filePath: full });
        }
      }
    }
  }

  walk(APP_DIR);
  return entries;
}

/** 检查文件是否在 N 天内修改过 */
function isRecentlyModified(filePath, days = 7) {
  if (!existsSync(filePath)) return false;
  const stats = statSync(filePath);
  const ageMs = Date.now() - stats.mtimeMs;
  return ageMs < days * 24 * 60 * 60 * 1000;
}

/** 生成全站 URL 列表 */
function generateUrlList(siteUrl) {
  const urls = [];

  // 1. 首页
  urls.push({ url: `${siteUrl}/`, label: "首页" });
  urls.push({ url: `${siteUrl}/zh`, label: "首页 (ZH)" });

  // 2. 工具页（en + zh）
  const toolSlugs = parseToolsSlugs();
  for (const slug of toolSlugs) {
    urls.push({
      url: `${siteUrl}/tools/${slug}`,
      label: `工具: ${slug}`,
      filePath: join(APP_DIR, "tools", slug, "page.tsx"),
    });
    urls.push({
      url: `${siteUrl}/zh/tools/${slug}`,
      label: `工具 (ZH): ${slug}`,
      filePath: join(APP_DIR, "zh", "tools", slug, "page.tsx"),
    });
  }

  // 3. 其他具体页面（扫描 app/ 目录）
  const appPages = scanAppPageFiles();

  for (const page of appPages) {
    if (!page.routePath) continue; // 跳过根 page.tsx（已作为首页处理）

    urls.push({
      url: `${siteUrl}/${page.routePath}`,
      label: page.routePath,
      filePath: page.filePath,
    });
  }

  // 去重（有些路径可能被多种方式覆盖）
  const seen = new Set();
  const unique = [];
  for (const entry of urls) {
    if (seen.has(entry.url)) continue;
    seen.add(entry.url);
    unique.push(entry);
  }

  return unique;
}

// ── GSC 查询 ─────────────────────────────────────────────────────────

async function inspectUrl(sc, siteUrl, url, languageCode = "en-US") {
  try {
    const res = await sc.urlInspection.index.inspect({
      requestBody: {
        inspectionUrl: url,
        siteUrl,
        languageCode,
      },
    });
    return res.data.inspectionResult;
  } catch (err) {
    return {
      inspectionResultLink: url,
      error: err.message ?? "Unknown error",
      _fetchError: true,
    };
  }
}

async function inspectBatch(sc, siteUrl, entries, concurrency) {
  const results = [];
  for (let i = 0; i < entries.length; i += concurrency) {
    const batch = entries.slice(i, i + concurrency);
    const batchResults = await Promise.all(
      batch.map(async (entry) => {
        const lang = entry.url.includes("/zh/") ? "zh-CN" : "en-US";
        const result = await inspectUrl(sc, siteUrl, entry.url, lang);
        return { entry, result };
      }),
    );
    results.push(...batchResults);

    // 进度输出
    const done = Math.min(i + concurrency, entries.length);
    process.stdout.write(`\r  进度: ${done}/${entries.length}`);
  }
  process.stdout.write("\n");
  return results;
}

// ── 状态分类 ─────────────────────────────────────────────────────────

function classifyIndexStatus(result) {
  if (result._fetchError) return "API_ERROR";

  const status = result?.indexStatusResult?.status;
  if (!status) return "UNKNOWN";

  // GSC 返回的状态值
  const statusMap = {
    SUBMITTED_AND_INDEXED: "INDEXED",
    CRAWLED_CURRENTLY_NOT_INDEXED: "CRAWLED_NOT_INDEXED",
    DISCOVERED_NOT_CRAWLED: "DISCOVERED",
    BLOCKED_BY_ROBOTS_TXT: "BLOCKED_ROBOTS",
    BLOCKED_BY_NOINDEX: "NOINDEX",
    BLOCKED_BY_REMOVAL: "REMOVAL_TOOL",
    BLOCKED_DUE_TO_OTHER_4XX: "4XX",
    SOFT_404: "SOFT_404",
  };

  return statusMap[status] || status;
}

// ── 主流程 ───────────────────────────────────────────────────────────

async function main() {
  console.log("═".repeat(60));
  console.log("GSC 索引健康检查");
  console.log("═".repeat(60));

  // 1. 认证
  console.log("\n[1/4] 初始化...");
  const credentials = getCredentials();
  const siteUrl = getSiteUrl();
  console.log(`  站点: ${siteUrl}`);
  console.log(`  并发: ${CONCURRENCY} req/s`);

  const auth = new google.auth.GoogleAuth({
    credentials,
    scopes: ["https://www.googleapis.com/auth/webmasters"],
  });
  const sc = google.searchconsole({ version: "v1", auth });

  // 2. 生成 URL 列表
  console.log("\n[2/4] 生成 URL 列表...");
  let urlEntries = generateUrlList(siteUrl);
  console.log(`  共 ${urlEntries.length} 个页面`);

  // --recent 模式：仅检查最近修改的页面
  if (RECENT_ONLY) {
    const before = urlEntries.length;
    urlEntries = urlEntries.filter(
      (e) => e.filePath && isRecentlyModified(e.filePath, 7),
    );
    console.log(
      `  --recent: 过滤后 ${urlEntries.length} 个（排除 ${before - urlEntries.length} 个未修改）`,
    );
  }

  if (urlEntries.length === 0) {
    console.log("\n  没有需要检查的页面。");
    return;
  }

  // 3. 批量查询
  console.log(`\n[3/4] 调用 URL Inspection API...`);
  const results = await inspectBatch(sc, siteUrl, urlEntries, CONCURRENCY);

  // 4. 分析输出
  console.log("\n[4/4] 分析结果...\n");

  // 按状态分组
  const groups = {
    INDEXED: [],
    CRAWLED_NOT_INDEXED: [],
    DISCOVERED: [],
    BLOCKED_ROBOTS: [],
    NOINDEX: [],
    REMOVAL_TOOL: [],
    "4XX": [],
    SOFT_404: [],
    API_ERROR: [],
    UNKNOWN: [],
  };

  for (const { entry, result } of results) {
    const status = classifyIndexStatus(result);
    groups[status]?.push({ ...entry, result, status });
  }

  // 输出索引异常清单
  const problemStatuses = [
    "CRAWLED_NOT_INDEXED",
    "DISCOVERED",
    "BLOCKED_ROBOTS",
    "NOINDEX",
    "REMOVAL_TOOL",
    "4XX",
    "SOFT_404",
    "API_ERROR",
    "UNKNOWN",
  ];

  const totalProblems = problemStatuses.reduce(
    (sum, s) => sum + (groups[s]?.length || 0),
     (s) => sum + (groups[s]?.length || 0), 0,
  );

  if (totalProblems === 0) {
    console.log("✓ 所有页面索引状态正常（submittedAndIndexed）。\n");
  } else {
    console.log("═".repeat(60));
    console.log(`索引异常页面（共 ${totalProblems} 个）`);
    console.log("═".repeat(60));

    for (const status of problemStatuses) {
      const items = groups[status] || [];
      if (items.length === 0) continue;

      const label = {
        CRAWLED_NOT_INDEXED: "已抓取但未索引",
        DISCOVERED: "已发现但未抓取",
        BLOCKED_ROBOTS: "被 robots.txt 阻止",
        NOINDEX: "被 noindex 标记排除",
        REMOVAL_TOOL: "被移除工具排除",
        "4XX": "返回 4xx 状态码",
        SOFT_404: "被判定为软 404",
        API_ERROR: "API 调用失败",
        UNKNOWN: "未知状态",
      }[status];

      console.log(`\n── ${label} (${items.length} 个) ──`);

      items.forEach((item, i) => {
        const urlShort = item.url.replace(siteUrl, "");
        const errorDetail =
          item.result?.indexStatusResult?.coverageState ||
          item.result?.error ||
          "";

        console.log(`  ${i + 1}. ${urlShort}`);
        if (errorDetail) {
          console.log(`     详情: ${errorDetail}`);
        }

        // 对有 filePath 的给出文件位置
        if (item.filePath) {
          const rel = relative(ROOT, item.filePath);
          console.log(`     文件: ${rel}`);
        }
      });

      // 给出修复建议
      const suggestion = {
        CRAWLED_NOT_INDEXED:
          "  → 建议：提升内容质量/独特性，确认 canonical 正确，考虑加内链",
        DISCOVERED: "  → 建议：确保页面在 sitemap 中，增加站内内链指向该页",
        BLOCKED_ROBOTS:
          "  → 建议：检查 robots.txt 是否误封，或是否为预期行为",
        NOINDEX: "  → 建议：确认是否误设 noindex，或是否为预期行为",
        SOFT_404: "  → 建议：页面内容过少或与标题不符，补充实质性内容",
        API_ERROR: "  → 建议：可能是临时网络问题，稍后重试",
      }[status];

      if (suggestion) console.log(suggestion);
    }
  }

  // 统计摘要
  console.log("\n" + "═".repeat(60));
  console.log("索引状态分布");
  console.log("═".repeat(60));

  const allStatuses = [
    "INDEXED", "CRAWLED_NOT_INDEXED", "DISCOVERED", "BLOCKED_ROBOTS",
    "NOINDEX", "SOFT_404", "4XX", "REMOVAL_TOOL", "API_ERROR", "UNKNOWN",
  ];

  const labels = {
    INDEXED: "已索引",
    CRAWLED_NOT_INDEXED: "已抓取未索引",
    DISCOVERED: "已发现未抓取",
    BLOCKED_ROBOTS: "robots 阻止",
    NOINDEX: "noindex 排除",
    SOFT_404: "软 404",
    "4XX": "4xx 错误",
    REMOVAL_TOOL: "移除工具",
    API_ERROR: "API 错误",
    UNKNOWN: "未知",
  };

  for (const status of allStatuses) {
    const count = groups[status]?.length || 0;
    if (count > 0) {
      const health =
        status === "INDEXED" ? "  ✓" : status === "API_ERROR" ? "  ⚠" : "  ✗";
      console.log(`${health} ${labels[status]}: ${count}`);
    }
  }

  const indexedRate = ((groups.INDEXED?.length || 0) / results.length * 100).toFixed(1);
  console.log(`\n  索引率: ${indexedRate}%`);

  // 保存结果到 data/ 目录
  mkdirSync(DATA_DIR, { recursive: true });
  const today = new Date().toISOString().slice(0, 10);
  const reportPath = resolve(DATA_DIR, `gsc-index-health-${today}.json`);

  const report = {
    checkedAt: new Date().toISOString(),
    siteUrl,
    totalChecked: results.length,
    recentOnly: RECENT_ONLY,
    summary: Object.fromEntries(
      allStatuses.map((s) => [s, groups[s]?.length || 0]),
    ),
    details: problemStatuses.flatMap((s) =>
      (groups[s] || []).map((item) => ({
        url: item.url,
        status: item.status,
        file: item.filePath ? relative(ROOT, item.filePath) : null,
      })),
    ),
  };

  writeFileSync(reportPath, JSON.stringify(report, null, 2) + "\n", "utf-8");
  console.log(`\n  详细报告已保存到 data/gsc-index-health-${today}.json`);

  console.log("\n" + "═".repeat(60));
  console.log("完成。\n");
}

main().catch((err) => {
  console.error("\n✗ 脚本执行失败:");
  if (err.message?.includes("ETIMEDOUT") || err.message?.includes("ENOTFOUND")) {
    console.error("  网络连接失败。如果在国内，请确保已连接 VPN。");
  } else {
    console.error(err.message ?? err);
  }
  process.exit(1);
});
