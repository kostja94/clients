/**
 * 从 Bing Webmaster Tools API 拉取搜索绩效数据并存档。
 *
 * 用法：node scripts/permanent/fetch-bing-data.mjs [days]
 *   days: 筛选最近 N 天的数据，默认 28
 *
 * 环境变量：
 *   BING_API_KEY — Bing Webmaster Tools API Key
 *   BING_SITE_URL — 站点 URL，默认 https://alignify.co
 *
 * 输出：
 *   data/bing-page-YYYY-MM-DD.json  — 页面维度（与 GSC 同结构，可直接对比）
 *   data/bing-query-YYYY-MM-DD.json — 搜索词维度（辅助分析）
 *
 * 注意：Bing API 返回约 26 周的历史数据（按周聚合），不提供 date range 过滤。
 * 脚本筛选最近 N 天以保持与 GSC 快照的一致性。
 */

import { writeFileSync, mkdirSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..", "..");
const DATA_DIR = resolve(ROOT, "data");

const BING_BASE = "https://ssl.bing.com/webmaster/api.svc";

// ── 工具函数 ─────────────────────────────────────────────────────────

function formatDate(date) {
  return date.toISOString().slice(0, 10);
}

function daysAgo(n) {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d;
}

/**
 * 解析 Microsoft JSON date: /Date(1399100400000)/
 */
function parseMsDate(str) {
  if (!str) return null;
  const m = str.match(/\/Date\((\d+)([+-]\d+)?\)\//);
  if (!m) return null;
  const ts = parseInt(m[1], 10);
  return new Date(ts);
}

// ── API 调用 ─────────────────────────────────────────────────────────

async function fetchBing(endpointPath) {
  const url = `${BING_BASE}${endpointPath}`;
  const res = await fetch(url, {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`HTTP ${res.status}: ${text.slice(0, 300)}`);
  }

  return res.json();
}

// ── 主流程 ───────────────────────────────────────────────────────────

async function main() {
  const apiKey = process.env.BING_API_KEY;
  const siteUrl = process.env.BING_SITE_URL || "https://alignify.co";
  const lookbackDays = parseInt(process.argv[2], 10) || 28;

  if (!apiKey) {
    console.error("✗ 缺少 BING_API_KEY 环境变量");
    console.error("  $env:BING_API_KEY='your-key'");
    process.exit(1);
  }

  const encodedSite = encodeURIComponent(siteUrl);

  // 与 GSC 脚本对齐日期计算：endDate = 3 天前（容忍数据延迟），startDate = days+2 天前
  const endDate = formatDate(daysAgo(3));
  const startDate = formatDate(daysAgo(lookbackDays + 2));
  const startDateObj = daysAgo(lookbackDays + 2); // 用于筛选 Bing 周数据

  const effectiveDays = lookbackDays;

  console.log("═".repeat(55));
  console.log("Bing 数据存档脚本");
  console.log("═".repeat(55));
  console.log(`  站点: ${siteUrl}`);
  console.log(`  范围: ${startDate} → ${endDate} (${effectiveDays} 天，与 GSC 对齐)`);
  console.log(`  Key:  ${apiKey.slice(0, 8)}...`);
  console.log("");

  // ── 1. GetPageStats — 页面级数据 ──
  console.log("[1/4] 拉取页面级数据 (GetPageStats)...");

  let pageRows = [];
  try {
    const path = `/json/GetPageStats?siteUrl=${encodedSite}&apikey=${apiKey}`;
    const data = await fetchBing(path);
    pageRows = data?.d || [];
  } catch (err) {
    console.error(`✗ GetPageStats 失败: ${err.message}`);
    process.exit(1);
  }

  console.log(`  API 返回 ${pageRows.length} 条页面数据 (全部历史)`);

  // 筛选最近 N 天 → 按周分组，最近的 N 天覆盖的周
  const recentPageRows = pageRows.filter((row) => {
    const date = parseMsDate(row.Date);
    return date && date >= startDateObj;
  });
  console.log(`  筛选 ${startDate} ~ ${endDate}: ${recentPageRows.length} 条`);

  // 汇总：Bing 的 GetPageStats 按周返回同一条 URL 的多条记录
  // 把最近 N 天内的所有周的数据聚合到一起
  const pageMap = new Map();
  for (const row of recentPageRows) {
    // Bing 用 "Query" 字段存 page URL（命名历史遗留）
    const url = row.Query || "";
    if (!url.startsWith("http")) continue;

    const existing = pageMap.get(url) || {
      url,
      clicks: 0,
      impressions: 0,
      positions: [], // 收集各周 position 用于算加权平均
    };

    existing.clicks += row.Clicks || 0;
    existing.impressions += row.Impressions || 0;
    const pos = row.AvgImpressionPosition || 0;
    if (pos > 0 && row.Impressions > 0) {
      existing.positions.push({ pos, weight: row.Impressions });
    }
    pageMap.set(url, existing);
  }

  // 转换为统一格式
  const pages = Array.from(pageMap.values()).map((p) => {
    // 加权平均 position
    let avgPos = 0;
    if (p.positions.length > 0) {
      const totalWeight = p.positions.reduce((s, x) => s + x.weight, 0);
      avgPos = totalWeight > 0
        ? p.positions.reduce((s, x) => s + x.pos * x.weight, 0) / totalWeight
        : 0;
    }
    return {
      url: p.url,
      clicks: p.clicks,
      impressions: p.impressions,
      ctr: p.impressions > 0 ? p.clicks / p.impressions : 0,
      position: avgPos,
    };
  });

  pages.sort((a, b) => b.clicks - a.clicks);

  const totalClicks = pages.reduce((s, p) => s + p.clicks, 0);
  const totalImpressions = pages.reduce((s, p) => s + p.impressions, 0);
  const withClicks = pages.filter((p) => p.clicks > 0).length;
  const withImp = pages.filter((p) => p.impressions > 0).length;

  console.log(`  页面数: ${pages.length} | 有点击: ${withClicks} | 有曝光: ${withImp}`);
  console.log(`  总点击: ${totalClicks.toLocaleString()} | 总曝光: ${totalImpressions.toLocaleString()}`);

  // Top pages preview
  console.log("\n  流量 Top 10 页面:");
  for (const p of pages.filter((p) => p.clicks > 0).slice(0, 10)) {
    const short = p.url.replace(siteUrl, "");
    console.log(`    ${p.clicks.toString().padStart(4)} 点击  │  ${p.impressions.toString().padStart(7)} 曝光  │  ${(p.ctr * 100).toFixed(1).padStart(5)}% CTR  │  pos ${p.position.toFixed(1)}  │  ${short}`);
  }

  // ── 2. GetQueryStats — 搜索词级数据 ──
  console.log("\n[2/4] 拉取搜索词数据 (GetQueryStats)...");

  let queryRows = [];
  try {
    const path = `/json/GetQueryStats?siteUrl=${encodedSite}&apikey=${apiKey}`;
    const data = await fetchBing(path);
    queryRows = data?.d || [];
  } catch (err) {
    console.warn(`  ⚠ GetQueryStats 失败: ${err.message} — 跳过`);
  }

  const recentQueryRows = queryRows.filter((row) => {
    const date = parseMsDate(row.Date);
    return date && date >= startDateObj;
  });

  // 汇总 query 数据
  const queryMap = new Map();
  for (const row of recentQueryRows) {
    const q = row.Query || "";
    if (!q) continue;
    const existing = queryMap.get(q) || { query: q, clicks: 0, impressions: 0 };
    existing.clicks += row.Clicks || 0;
    existing.impressions += row.Impressions || 0;
    queryMap.set(q, existing);
  }

  const queries = Array.from(queryMap.values())
    .map((q) => ({
      ...q,
      ctr: q.impressions > 0 ? q.clicks / q.impressions : 0,
    }))
    .sort((a, b) => b.clicks - a.clicks);

  console.log(`  搜索词数: ${queries.length} | 有点击: ${queries.filter((q) => q.clicks > 0).length}`);

  // ── 3. GetCrawlIssues（GSC 没有的独有数据） ──
  console.log("\n[3/4] 拉取抓取问题 (GetCrawlIssues)...");

  let crawlIssues = null;
  try {
    const path = `/json/GetCrawlIssues?siteUrl=${encodedSite}&apikey=${apiKey}`;
    const data = await fetchBing(path);
    crawlIssues = data?.d || [];
  } catch (err) {
    console.warn(`  ⚠ GetCrawlIssues 失败: ${err.message} — 跳过`);
  }

  const crawlCount = crawlIssues?.length || 0;
  console.log(`  抓取问题: ${crawlCount} 个`);
  if (crawlIssues && crawlIssues.length > 0) {
    for (const issue of crawlIssues.slice(0, 5)) {
      console.log(`    ${issue.IssueType || "unknown"}: ${issue.URL || "N/A"}`);
    }
  }

  // ── 4. 保存 ──
  console.log("\n[4/4] 保存快照...");
  mkdirSync(DATA_DIR, { recursive: true });
  const today = formatDate(new Date());

  // Page 维度
  const pageFile = `bing-page-${today}.json`;
  writeFileSync(
    resolve(DATA_DIR, pageFile),
    JSON.stringify({
      fetchedAt: new Date().toISOString(),
      dateRange: { start: startDate, end: endDate },
      source: "bing",
      summary: {
        totalPages: pages.length,
        pagesWithClicks: withClicks,
        pagesWithImpressions: withImp,
        totalClicks,
        totalImpressions,
      },
      crawlIssues: crawlCount,
      pages,
    }, null, 2) + "\n",
    "utf-8"
  );
  console.log(`  ✓ data/${pageFile}`);

  // Query 维度
  if (queries.length > 0) {
    const queryFile = `bing-query-${today}.json`;
    writeFileSync(
      resolve(DATA_DIR, queryFile),
      JSON.stringify({
        fetchedAt: new Date().toISOString(),
        lookbackDays,
        source: "bing",
        summary: {
          totalQueries: queries.length,
          queriesWithClicks: queries.filter((q) => q.clicks > 0).length,
        },
        queries,
      }, null, 2) + "\n",
      "utf-8"
    );
    console.log(`  ✓ data/${queryFile}`);
  }

  console.log("\n" + "═".repeat(55));
  console.log("完成。");
  console.log("");
  console.log("文件说明:");
  console.log("  bing-page-*.json  — 页面维度，与 GSC 的 gsc-page-*.json 同结构，可直接做双引擎对比");
  console.log("  bing-query-*.json — 搜索词维度，用于发现哪些 query 在 Bing 有曝光但页面未覆盖");
  console.log("");
}

main().catch((err) => {
  console.error("\n✗ 失败:", err.message ?? err);
  process.exit(1);
});
