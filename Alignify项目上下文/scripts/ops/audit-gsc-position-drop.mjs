/**
 * GSC 位置滑坡审计脚本：对比最近两期数据快照，识别排名下降的页面。
 *
 * 运行前提：至少有两期 data/gsc-page-*.json 快照（即已运行过至少两次 npm run fetch-gsc）。
 *
 * 用法：
 *   node scripts/permanent/audit-gsc-position-drop.mjs          # 默认阈值
 *   node scripts/permanent/audit-gsc-position-drop.mjs 5 200    # pos下降>5, 曝光>200
 *
 * 默认阈值：position 下降 > 3 且 impressions > 100
 *
 * 输出：
 *   1. 排名下降清单（按曝光量降序，优先修）
 *   2. 消失页面清单（上期有曝光、本期消失）— 可能是索引问题或大幅滑坡
 *   3. 排名上升清单（附带输出，用于验证哪些优化见效了）
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..", "..");
const DATA_DIR = path.resolve(ROOT, "data");

// ── 参数 ─────────────────────────────────────────────────────────────

const MIN_POSITION_DROP = parseInt(process.argv[2], 10) || 3;
const MIN_IMPRESSIONS = parseInt(process.argv[3], 10) || 100;

// ── 工具 ─────────────────────────────────────────────────────────────

/** 获取 data/ 下所有 gsc-page-*.json，按文件名排序（旧→新） */
function listDataFiles() {
  if (!fs.existsSync(DATA_DIR)) {
    console.error("✗ data/ 目录不存在。请先运行 npm run fetch-gsc 拉取数据。");
    process.exit(1);
  }

  const files = fs
    .readdirSync(DATA_DIR)
    .filter((f) => f.startsWith("gsc-page-") && f.endsWith(".json"))
    .sort();

  if (files.length < 2) {
    console.error(`✗ 仅有 ${files.length} 期数据，需要至少 2 期才能对比趋势。`);
    console.error("  请再运行一次 npm run fetch-gsc（间隔至少一周）。");
    process.exit(1);
  }

  return files.map((f) => ({
    name: f,
    path: path.join(DATA_DIR, f),
  }));
}

/** 建立 URL → 页面数据的映射 */
function buildPageMap(pages) {
  const map = new Map();
  for (const p of pages) {
    // 标准化 URL：去掉尾部斜杠和参数
    let url = (p.url || "").trim().replace(/\/+$/, "");
    if (!url) continue;
    map.set(url, {
      clicks: p.clicks ?? 0,
      impressions: p.impressions ?? 0,
      ctr: p.ctr ?? 0,
      position: p.position ?? 0,
    });
  }
  return map;
}

/** 判断是否是中文页面 */
function isZhPage(url) {
  return url.includes("/zh/");
}

// ── 主流程 ───────────────────────────────────────────────────────────

function main() {
  console.log("═".repeat(60));
  console.log("GSC 位置滑坡审计");
  console.log("═".repeat(60));
  console.log(`  阈值: position 下降 > ${MIN_POSITION_DROP} 且 impressions > ${MIN_IMPRESSIONS}`);

  // 1. 加载最近两期数据
  const files = listDataFiles();
  const older = files[files.length - 2];
  const newer = files[files.length - 1];

  console.log(`\n  上期: data/${older.name}`);
  console.log(`  本期: data/${newer.name}`);

  const olderData = JSON.parse(fs.readFileSync(older.path, "utf-8"));
  const newerData = JSON.parse(fs.readFileSync(newer.path, "utf-8"));

  const olderMap = buildPageMap(olderData.pages);
  const newerMap = buildPageMap(newerData.pages);

  // 2. 逐一对比
  const dropped = [];   // 排名下降
  const improved = [];  // 排名上升
  const vanished = [];  // 上期有、本期消失
  const appeared = [];  // 本期新增

  for (const [url, olderPage] of olderMap) {
    const newerPage = newerMap.get(url);

    if (!newerPage || newerPage.impressions === 0) {
      // 页面从本期消失（可能是 0 曝光或掉出数据范围）
      if (olderPage.impressions >= MIN_IMPRESSIONS) {
        vanished.push({
          url,
          older,
          newer: newerPage || { clicks: 0, impressions: 0, ctr: 0, position: 0 },
        });
      }
      continue;
    }

    const posChange = newerPage.position - olderPage.position;
    // posChange > 0 表示排名数字变大 → 排名下降
    // posChange < 0 表示排名数字变小 → 排名上升

    // 只关注上期有足够曝光的页面
    if (olderPage.impressions < MIN_IMPRESSIONS) continue;

    if (posChange > MIN_POSITION_DROP) {
      dropped.push({
        url,
        older,
        newer: newerPage,
        drop: posChange,
      });
    } else if (posChange < -MIN_POSITION_DROP) {
      improved.push({
        url,
        older,
        newer: newerPage,
        gain: Math.abs(posChange),
      });
    }
  }

  // 发现本期新增且有曝光的页面
  for (const [url, newerPage] of newerMap) {
    if (!olderMap.has(url) && newerPage.impressions >= MIN_IMPRESSIONS) {
      appeared.push({ url, ...newerPage });
    }
  }

  // 按本期曝光量降序排列（曝光越大越优先关注）
  dropped.sort((a, b) => b.newer.impressions - a.newer.impressions);
  improved.sort((a, b) => b.newer.impressions - a.newer.impressions);
  vanished.sort((a, b) => b.older.impressions - a.older.impressions);
  appeared.sort((a, b) => b.impressions - a.impressions);

  // 3. 输出排名下降清单（主报告）
  console.log("\n" + "═".repeat(60));
  console.log(`排名下降 > ${MIN_POSITION_DROP} 位（共 ${dropped.length} 个页面）`);
  console.log("═".repeat(60));

  if (dropped.length === 0) {
    console.log("\n  ✓ 没有页面排名显著下降。\n");
  } else {
    dropped.forEach((r, i) => {
      const zh = isZhPage(r.url) ? "[ZH]" : "[EN]";
      const urlShort = r.url.replace(/^https?:\/\/[^/]+/, "");
      const oldPos = r.older.position.toFixed(1);
      const newPos = r.newer.position.toFixed(1);
      const imps = r.newer.impressions.toLocaleString();
      const ctrOld = (r.older.ctr * 100).toFixed(1);
      const ctrNew = (r.newer.ctr * 100).toFixed(1);

      console.log(`${i + 1}. ${zh} ${urlShort}`);
      console.log(`   位置 ${oldPos} → ${newPos} (下降 ${r.drop.toFixed(1)} 位)`);
      console.log(`   曝光 ${imps} | CTR ${ctrOld}% → ${ctrNew}%`);
      console.log("");
    });
  }

  // 4. 消失页面
  if (vanished.length > 0) {
    console.log("─".repeat(60));
    console.log(`从本期消失的页面（共 ${vanished.length} 个，上期曝光 ≥ ${MIN_IMPRESSIONS}）`);
    console.log("─".repeat(60));
    vanished.forEach((v, i) => {
      const zh = isZhPage(v.url) ? "[ZH]" : "[EN]";
      const urlShort = v.url.replace(/^https?:\/\/[^/]+/, "");
      console.log(`${i + 1}. ${zh} ${urlShort}`);
      console.log(`   上期: 位置 ${v.older.position.toFixed(1)} | 曝光 ${v.older.impressions.toLocaleString()} | 点击 ${v.older.clicks}`);
      console.log("   本期: 无数据或 0 曝光（需排查索引状态）");
      console.log("");
    });
    console.log("  → 建议：对消失的页面运行 url-inspection 检查索引状态\n");
  }

  // 5. 排名上升（附带输出，正面信号）
  if (improved.length > 0) {
    console.log("─".repeat(60));
    console.log(`排名上升 > ${MIN_POSITION_DROP} 位（共 ${improved.length} 个页面）`);
    console.log("─".repeat(60));
    improved.slice(0, 10).forEach((r, i) => {
      const zh = isZhPage(r.url) ? "[ZH]" : "[EN]";
      const urlShort = r.url.replace(/^https?:\/\/[^/]+/, "");
      console.log(`  ${i + 1}. ${zh} ${urlShort}  ${r.older.position.toFixed(1)} → ${r.newer.position.toFixed(1)} (+${r.gain.toFixed(1)})`);
    });
    if (improved.length > 10) {
      console.log(`  ...及其他 ${improved.length - 10} 个页面`);
    }
    console.log("");
  }

  // 6. 统计摘要
  console.log("═".repeat(60));
  console.log("统计摘要\n");
  console.log(`  上期页面数: ${olderData.summary.totalPages}`);
  console.log(`  本期页面数: ${newerData.summary.totalPages}`);
  console.log(`  排名下降:   ${dropped.length}`);
  console.log(`  排名上升:   ${improved.length}`);
  console.log(`  消失页面:   ${vanished.length}`);
  console.log(`  新增页面:   ${appeared.length}`);

  // 7. 行动建议
  if (dropped.length > 0) {
    console.log("\n─".repeat(60));
    console.log("行动建议\n");
    console.log("  排名下降的常见原因和对应解法：\n");
    console.log("  1. 竞争对手更新了内容 → 刷新你的 content JSON（补充新数据、案例、FAQ）");
    console.log("  2. 内容过时 → 更新 modifiedDate，加入 2026 年新信息");
    console.log("  3. 内链变弱 → 从高流量相关页面添加指向该页的内链");
    console.log("  4. 搜索意图变化 → 检查该页面当前的 top query 是否与内容匹配");
    console.log("  5. 技术问题 → 用 url-inspection 检查是否有抓取/渲染错误");
    console.log("");
    console.log("  修复后，下次 fetch-gsc 时数据会自动反映改善效果。\n");
  }

  console.log("═".repeat(60));
  console.log("完成。\n");
}

main();
