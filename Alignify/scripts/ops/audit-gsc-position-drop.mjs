/**
 * GSC 位置滑坡审计：基于 seo-report-bundle 内 position vs positionPrev 环比。
 *
 * 运行前提：cd seo-weekly-report/scripts && npm run fetch-all
 *
 * 用法：
 *   node scripts/ops/audit-gsc-position-drop.mjs          # 默认阈值
 *   node scripts/ops/audit-gsc-position-drop.mjs 5 200    # pos下降>5, 曝光>200
 *
 * 默认阈值：position 上升 > 3（排名下降）且 impressions > 100
 */

import path from "path";
import {
  loadLatestBundle,
  normalizeGscPages,
  bundleSummary,
} from "./lib/seo-report-data.mjs";

const MIN_POSITION_DROP = parseInt(process.argv[2], 10) || 3;
const MIN_IMPRESSIONS = parseInt(process.argv[3], 10) || 100;

function isZhPage(url) {
  return url.includes("/zh/");
}

function main() {
  console.log("═".repeat(60));
  console.log("GSC 位置滑坡审计");
  console.log("═".repeat(60));
  console.log(`  阈值: position 下降 > ${MIN_POSITION_DROP} 且 impressions > ${MIN_IMPRESSIONS}`);

  const { filePath, bundle } = loadLatestBundle();
  const fileName = path.basename(filePath);
  const period = bundle?.period?.current;
  const prevPeriod = bundle?.period?.previous;

  console.log(`\n  数据源: seo-weekly-report/data/${fileName}`);
  if (period) {
    console.log(`  本期: ${period.start} → ${period.end}`);
  }
  if (prevPeriod) {
    console.log(`  上期: ${prevPeriod.start} → ${prevPeriod.end}`);
  }

  const pages = normalizeGscPages(bundle);
  const { summary } = bundleSummary(bundle, pages);

  const dropped = [];
  const improved = [];

  for (const p of pages) {
    if (p.impressions < MIN_IMPRESSIONS && p.impressionsPrev < MIN_IMPRESSIONS) continue;

    const posChange = p.position - p.positionPrev;
    if (posChange > MIN_POSITION_DROP && p.impressions >= MIN_IMPRESSIONS) {
      dropped.push({ ...p, posChange });
    } else if (posChange < -MIN_POSITION_DROP && p.impressionsPrev >= MIN_IMPRESSIONS) {
      improved.push({ ...p, gain: Math.abs(posChange) });
    }
  }

  dropped.sort((a, b) => b.impressions - a.impressions);
  improved.sort((a, b) => b.impressions - a.impressions);

  console.log("\n" + "═".repeat(60));
  console.log(`排名下降 > ${MIN_POSITION_DROP} 位（共 ${dropped.length} 个页面）`);
  console.log("═".repeat(60));

  if (dropped.length === 0) {
    console.log("\n  ✓ 没有页面排名显著下降。\n");
  } else {
    dropped.forEach((r, i) => {
      const zh = isZhPage(r.url) ? "[ZH]" : "[EN]";
      const urlShort = r.url.replace(/^https?:\/\/[^/]+/, "");
      console.log(`${i + 1}. ${zh} ${urlShort}`);
      console.log(
        `   位置 ${r.positionPrev.toFixed(1)} → ${r.position.toFixed(1)} (下降 ${r.posChange.toFixed(1)} 位)`,
      );
      console.log(`   曝光 ${r.impressions.toLocaleString()} | CTR ${(r.ctr * 100).toFixed(1)}%`);
      console.log("");
    });
  }

  if (improved.length > 0) {
    console.log("─".repeat(60));
    console.log(`排名上升 > ${MIN_POSITION_DROP} 位（共 ${improved.length} 个，展示前 10）`);
    console.log("─".repeat(60));
    improved.slice(0, 10).forEach((r, i) => {
      const zh = isZhPage(r.url) ? "[ZH]" : "[EN]";
      const urlShort = r.url.replace(/^https?:\/\/[^/]+/, "");
      console.log(
        `  ${i + 1}. ${zh} ${urlShort}  ${r.positionPrev.toFixed(1)} → ${r.position.toFixed(1)} (+${r.gain.toFixed(1)})`,
      );
    });
    console.log("");
  }

  console.log("═".repeat(60));
  console.log("统计摘要\n");
  console.log(`  页面总数: ${summary.totalPages}`);
  console.log(`  排名下降: ${dropped.length}`);
  console.log(`  排名上升: ${improved.length}`);
  console.log("\n  修复后，下次 fetch-all 时 bundle 会自动反映改善效果。\n");
  console.log("═".repeat(60));
  console.log("完成。\n");
}

main();
