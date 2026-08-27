/**
 * GSC CTR 审计脚本：识别高曝光低点击页面，输出 title/meta 优化清单。
 *
 * 运行前提：已执行 seo-weekly-report/scripts npm run fetch-all。
 * 用法：
 *   node scripts/ops/audit-gsc-ctr.mjs          # 默认阈值
 *   node scripts/ops/audit-gsc-ctr.mjs 500 0.03 # 自定义阈值
 *
 * 默认阈值：impressions > 200 且 CTR < 2%
 */

import fs from "fs";
import path from "path";
import {
  loadLatestBundle,
  normalizeGscPages,
  bundleSummary,
  getDeployRoot,
} from "./lib/seo-report-data.mjs";

const APP_DIR = path.join(getDeployRoot(), "app");

// ── 参数 ─────────────────────────────────────────────────────────────

const MIN_IMPRESSIONS = parseInt(process.argv[2], 10) || 200;
const MAX_CTR = parseFloat(process.argv[3]) || 0.02; // 2%

// ── 工具函数 ─────────────────────────────────────────────────────────

/** 从 page.tsx 提取 title 和 description */
function urlToPageTsx(url) {
  // 去掉协议和域名，保留路径部分
  let pathname = url;
  try {
    const u = new URL(url);
    pathname = u.pathname;
  } catch {
    // 如果不是完整 URL，直接当路径处理
  }

  // 去掉首尾斜杠
  pathname = pathname.replace(/^\/+|\/+$/g, "");

  if (!pathname) {
    // 首页
    return path.join(APP_DIR, "page.tsx");
  }

  // 尝试常见模式
  const candidates = [
    path.join(APP_DIR, pathname, "page.tsx"),
    // MDX 页面
    path.join(APP_DIR, pathname, "page.mdx"),
    // 带参数的路由（如 [slug]）— 低概率匹配，留空跳过
  ];

  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) {
      return candidate;
    }
  }

  return null;
}

/** 从 page.tsx 提取 title 和 description */
function extractPageMetadata(filePath) {
  if (!filePath || !fs.existsSync(filePath)) return null;

  const content = fs.readFileSync(filePath, "utf-8");

  // 匹配 Next.js Metadata 格式:
  //   title: "xxx",
  //   description: "xxx",
  const titleMatch = content.match(/title:\s*["'`]([^"'`]+)["'`]/);
  const descMatch = content.match(/description:\s*["'`]([^"'`]+)["'`]/);

  if (!titleMatch) return null;

  return {
    title: titleMatch[1],
    description: descMatch ? descMatch[1] : null,
    titleLen: titleMatch[1].length,
    descLen: descMatch ? descMatch[1].length : 0,
  };
}

/** 判断是否是中文页面 */
function isZhPage(url) {
  return url.includes("/zh/");
}

// ── 主流程 ───────────────────────────────────────────────────────────

function main() {
  console.log("═".repeat(60));
  console.log("GSC CTR 审计");
  console.log("═".repeat(60));
  console.log(`  阈值: impressions > ${MIN_IMPRESSIONS}, CTR < ${(MAX_CTR * 100).toFixed(1)}%`);

  // 1. 读取最新 bundle
  const { filePath, bundle } = loadLatestBundle();
  const fileName = path.basename(filePath);
  console.log(`\n  数据源: seo-weekly-report/data/${fileName}`);

  const pages = normalizeGscPages(bundle);
  const { dateRange, summary } = bundleSummary(bundle, pages);

  console.log(`  日期范围: ${dateRange.start} → ${dateRange.end}`);
  console.log(`  总页面数: ${summary.totalPages}`);
  console.log(`  有点击的页面: ${summary.pagesWithClicks}`);

  // 2. 筛选低 CTR 页面
  const flagged = pages.filter(
    (p) => p.impressions > MIN_IMPRESSIONS && p.ctr < MAX_CTR,
  );

  console.log(`\n  命中阈值: ${flagged.length} 个页面`);

  if (flagged.length === 0) {
    console.log("\n  ✓ 没有页面需要优化，CTR 整体健康。\n");
    return;
  }

  // 3. 提取每个页面的当前元数据
  const results = flagged.map((p) => {
    const tsxPath = urlToPageTsx(p.url);
    const metadata = extractPageMetadata(tsxPath);
    return { ...p, tsxPath, metadata };
  });

  const withMetadata = results.filter((r) => r.metadata);
  const withoutMetadata = results.filter((r) => !r.metadata);

  // 4. 输出报告
  console.log("\n" + "─".repeat(60));
  console.log("优化清单（按曝光量降序，先修排在前面的）\n");

  // 按曝光降序排列
  results.sort((a, b) => b.impressions - a.impressions);

  results.forEach((r, i) => {
    const zh = isZhPage(r.url) ? "[ZH]" : "[EN]";
    const urlShort = r.url.replace(/^https?:\/\/[^/]+/, "");
    const pct = (r.ctr * 100).toFixed(1);

    console.log(`${i + 1}. ${zh} ${urlShort}`);
    console.log(`   曝光 ${r.impressions.toLocaleString()} | 点击 ${r.clicks} | CTR ${pct}% | 平均位置 ${r.position.toFixed(1)}`);

    if (r.metadata) {
      const titlePreview =
        r.metadata.title.length > 80
          ? r.metadata.title.slice(0, 77) + "..."
          : r.metadata.title;
      console.log(`   title: "${titlePreview}" (${r.metadata.titleLen} chars)`);
      if (r.metadata.description) {
        const descPreview =
          r.metadata.description.length > 80
            ? r.metadata.description.slice(0, 77) + "..."
            : r.metadata.description;
        console.log(`   desc:  "${descPreview}" (${r.metadata.descLen} chars)`);
      }
      console.log(`   文件: ${r.tsxPath.replace(getDeployRoot(), "")}`);
    } else {
      console.log("   (未找到对应 page.tsx，可能是 MDX 或动态路由页面)");
    }
    console.log("");
  });

  // 5. 统计摘要
  console.log("─".repeat(60));
  console.log("统计摘要\n");
  console.log(`  命中页面总数:       ${flagged.length}`);
  console.log(`  含 title/desc 信息: ${withMetadata.length}`);
  console.log(`  无 page.tsx 映射:   ${withoutMetadata.length}`);
  console.log(`  中文页面:           ${flagged.filter((p) => isZhPage(p.url)).length}`);
  console.log(`  英文页面:           ${flagged.filter((p) => !isZhPage(p.url)).length}`);

  const avgImpressions = Math.round(
    flagged.reduce((s, p) => s + p.impressions, 0) / flagged.length,
  );
  const avgCtr = (
    (flagged.reduce((s, p) => s + p.ctr, 0) / flagged.length) *
    100
  ).toFixed(1);
  console.log(`  平均曝光:           ${avgImpressions.toLocaleString()}`);
  console.log(`  平均 CTR:           ${avgCtr}%`);

  // 6. 优化建议
  console.log("\n─".repeat(60));
  console.log("优化方向\n");
  console.log("  以下策略按场景适用：\n");
  console.log("  A. title 不含数字或痛点 → 加入「N 个」「最佳」「2026」等具体元素");
  console.log("  B. title 超过 60 字符 → 会被 SERP 截断，收紧到 50-60");
  console.log("  C. description 太泛 → 加入独特卖点、行动号召、或你的差异化信息");
  console.log("  D. 位置好但没人点 → 标题可能和搜索意图错位，检查对应的 top query");
  console.log("  E. 位置也在 10+ → 先优化内容深度，再做标题微调\n");
}

main();
