/**
 * 从 GSC API 拉取搜索绩效数据并存入 data/ 目录作为历史快照。
 *
 * 用法：node scripts/permanent/fetch-gsc-data.mjs [days]
 *   days: 拉取最近 N 天的数据，默认 28
 *
 * 输出：data/gsc-page-YYYY-MM-DD.json
 *
 * 方式：调用已部署的 Vercel API（https://alignify.co/api/gsc/search-analytics），
 * 无需 VPN，无需本地 GSC 凭证——Vercel 端已完成 Google 认证。
 */

import { writeFileSync, mkdirSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..", "..");
const DATA_DIR = resolve(ROOT, "data");

// ── 日期工具 ─────────────────────────────────────────────────────────

function formatDate(date) {
  return date.toISOString().slice(0, 10);
}

function daysAgo(n) {
  const d = new Date();
  d.setDate(d.getDate() - n);
  return d;
}

// ── API 调用 ─────────────────────────────────────────────────────────

async function fetchFromApi(startDate, endDate, baseUrl) {
  const endpoint = `${baseUrl}/api/gsc/search-analytics`;
  const rows = [];
  const rowLimit = 5000;
  let startRow = 0;

  console.log(`  端点: ${endpoint}`);
  console.log(`  范围: ${startDate} → ${endDate}`);
  console.log(`  维度: page`);

  while (true) {
    const body = {
      startDate,
      endDate,
      dimensions: ["page"],
      rowLimit,
      startRow,
    };

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      if (!res.ok) {
        const err = await res.text();
        throw new Error(`HTTP ${res.status}: ${err}`);
      }

      const data = await res.json();
      const batch = data.rows ?? [];
      rows.push(...batch);

      process.stdout.write(`\r  已获取: ${rows.length} 行`);

      if (batch.length < rowLimit) break;
      startRow += rowLimit;
    } catch (err) {
      if (err.message?.includes("fetch failed") || err.message?.includes("ENOTFOUND")) {
        console.error(`\n✗ 无法连接到 ${baseUrl}`);
        console.error("  确认站点已部署且可访问。");
        process.exit(1);
      }
      throw err;
    }
  }

  console.log("");
  return rows;
}

// ── 主流程 ───────────────────────────────────────────────────────────

async function main() {
  const days = parseInt(process.argv[2], 10) || 28;
  const baseUrl = process.env.GSC_API_BASE_URL || "https://alignify.co";

  console.log("═".repeat(50));
  console.log("GSC 数据存档脚本");
  console.log("═".repeat(50));

  // 1. 检查站点可达性
  console.log("\n[1/3] 检查 API 可达性...");
  try {
    const check = await fetch(`${baseUrl}/api/gsc/search-analytics`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        startDate: formatDate(daysAgo(5)),
        endDate: formatDate(daysAgo(4)),
        rowLimit: 1,
      }),
    });

    if (!check.ok && check.status !== 200) {
      const text = await check.text().catch(() => "");
      console.error(`✗ API 返回 HTTP ${check.status}`);
      console.error(`  ${text.slice(0, 200)}`);
      console.error("\n  排查:");
      console.error("  - Vercel 部署是否成功？");
      console.error("  - API route 是否在 app/api/gsc/search-analytics/route.ts？");
      console.error("  - Vercel 环境变量 GSC_CLIENT_EMAIL + GSC_PRIVATE_KEY + GSC_SITE_URL 是否已配置？");
      process.exit(1);
    }

    const testData = await check.json();
    console.log("  ✓ API 可达" + (testData.rows ? `（测试返回 ${testData.rows.length} 行）` : ""));
  } catch (err) {
    console.error(`✗ 无法连接到 ${baseUrl}`);
    console.error("  确认站点已部署且可从当前网络访问。");
    process.exit(1);
  }

  // 2. 拉取数据
  const endDate = formatDate(daysAgo(3));
  const startDate = formatDate(daysAgo(days + 2));
  console.log(`\n[2/3] 拉取 GSC 数据...`);

  const rows = await fetchFromApi(startDate, endDate, baseUrl);

  if (rows.length === 0) {
    console.log("\n  ⚠ GSC 返回 0 行数据。可能原因:");
    console.log("     - GSC 数据有 2-3 天延迟，近期可能还没有数据");
    console.log("     - 站点是新站，暂无搜索流量");
    console.log("     - 时间范围太短");
    console.log("    保存空快照以供参考。");
  }

  // 3. 整理并保存
  console.log("\n[3/3] 整理并保存...");
  const pages = rows.map((row) => ({
    url: row.keys[0],
    clicks: row.clicks ?? 0,
    impressions: row.impressions ?? 0,
    ctr: row.ctr ?? 0,
    position: row.position ?? 0,
  }));

  pages.sort((a, b) => b.clicks - a.clicks);

  const totalClicks = pages.reduce((sum, p) => sum + p.clicks, 0);
  const totalImpressions = pages.reduce((sum, p) => sum + p.impressions, 0);
  const pagesWithClicks = pages.filter((p) => p.clicks > 0).length;
  const pagesWithImpressions = pages.filter((p) => p.impressions > 0).length;

  console.log(`  页面: ${pages.length} | 有点击: ${pagesWithClicks} | 有曝光: ${pagesWithImpressions}`);
  console.log(`  总点击: ${totalClicks.toLocaleString()} | 总曝光: ${totalImpressions.toLocaleString()}`);

  mkdirSync(DATA_DIR, { recursive: true });

  const today = formatDate(new Date());
  const fileName = `gsc-page-${today}.json`;
  const filePath = resolve(DATA_DIR, fileName);

  const output = {
    fetchedAt: new Date().toISOString(),
    dateRange: { start: startDate, end: endDate },
    summary: {
      totalPages: pages.length,
      pagesWithClicks,
      pagesWithImpressions,
      totalClicks,
      totalImpressions,
    },
    pages,
  };

  writeFileSync(filePath, JSON.stringify(output, null, 2) + "\n", "utf-8");
  console.log(`  ✓ 已保存 data/${fileName}`);
  console.log("\n" + "═".repeat(50));
  console.log("完成。\n");
}

main().catch((err) => {
  console.error("\n✗ 失败:", err.message ?? err);
  process.exit(1);
});
