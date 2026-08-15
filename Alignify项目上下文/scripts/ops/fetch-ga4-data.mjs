/**
 * 从 GA4 Data API 拉取站点分析数据并存档。
 *
 * 用法：node scripts/permanent/fetch-ga4-data.mjs [days]
 *   days: 拉取最近 N 天的数据，默认 30
 *
 * 输出：data/ga4-overview-YYYY-MM-DD.json
 *
 * 方式：调用已部署的 Vercel API（https://alignify.co/api/ga4/overview），
 * 无需本地 GA4 凭证——Vercel 端已完成 Google 认证。
 */

import { writeFileSync, mkdirSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..", "..");
const DATA_DIR = resolve(ROOT, "data");

function formatDate(date) {
  return date.toISOString().slice(0, 10);
}

function daysAgo(n) {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d;
}

async function main() {
  const days = parseInt(process.argv[2], 10) || 30;
  const baseUrl = process.env.GA4_API_BASE_URL || "https://alignify.co";

  console.log("═".repeat(55));
  console.log("GA4 数据存档脚本");
  console.log("═".repeat(55));

  // 1. 检查 API 可达性
  console.log("\n[1/3] 检查 GA4 API 可达性...");
  const apiUrl = `${baseUrl}/api/ga4/overview?days=${days}&limit=200`;

  let data;
  try {
    const res = await fetch(apiUrl);
    if (!res.ok) {
      const text = await res.text().catch(() => "");
      console.error(`✗ API 返回 HTTP ${res.status}`);
      console.error(`  ${text.slice(0, 300)}`);
      console.error("\n  排查:");
      console.error("  - Vercel 部署是否成功？");
      console.error("  - GA_PROPERTY_ID 环境变量是否正确？");
      console.error("  - Google Analytics Data API 是否已启用？");
      console.error("  - 服务账号是否已添加到 GA4 媒体资源？");
      process.exit(1);
    }
    data = await res.json();
    if (data.error) {
      console.error("✗ GA4 API 返回错误:", JSON.stringify(data.error, null, 2));
      process.exit(1);
    }
    console.log("  ✓ API 可达");
  } catch (err) {
    console.error(`✗ 无法连接到 ${baseUrl}:`, err.message);
    process.exit(1);
  }

  // 2. 展示数据概要
  console.log("\n[2/3] GA4 数据概要...");
  const overview = data.overview;
  const topPages = data.topPages || [];

  if (!overview) {
    console.log("  ⚠ GA4 返回空数据。可能原因:");
    console.log("     - 该 GA4 媒体资源还没有数据");
    console.log("     - 时间范围太短");
    console.log("    保存空快照以供参考。");
  } else {
    console.log(`  用户数: ${overview.totalUsers?.toLocaleString() || 0}`);
    console.log(`  页面浏览: ${overview.screenPageViews?.toLocaleString() || 0}`);
    console.log(`  平均会话时长: ${(overview.averageSessionDuration || 0).toFixed(0)}s`);
    console.log(`  跳出率: ${((overview.bounceRate || 0) * 100).toFixed(1)}%`);
    console.log(`  Top 页面数: ${topPages.length}`);
  }

  // 3. 保存
  console.log("\n[3/3] 保存快照...");
  mkdirSync(DATA_DIR, { recursive: true });

  const endDate = formatDate(daysAgo(3));
  const startDate = formatDate(daysAgo(days + 2));
  const today = formatDate(new Date());
  const fileName = `ga4-overview-${today}.json`;
  const filePath = resolve(DATA_DIR, fileName);

  const output = {
    fetchedAt: new Date().toISOString(),
    dateRange: { start: startDate, end: endDate },
    source: "ga4",
    overview: overview || {
      totalUsers: 0,
      screenPageViews: 0,
      averageSessionDuration: 0,
      bounceRate: 0,
    },
    topPages: topPages.map((p) => ({
      pagePath: p.pagePath,
      pageTitle: p.pageTitle,
      screenPageViews: p.screenPageViews,
      averageSessionDuration: p.averageSessionDuration,
      bounceRate: p.bounceRate,
    })),
  };

  writeFileSync(filePath, JSON.stringify(output, null, 2) + "\n", "utf-8");
  console.log(`  ✓ 已保存 data/${fileName}`);
  console.log("\n" + "═".repeat(55));
  console.log("完成。\n");
}

main().catch((err) => {
  console.error("\n✗ 失败:", err.message ?? err);
  process.exit(1);
});
