/**
 * 读取 seo-weekly-report 合并 bundle 中的 GSC 页面数据。
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ALIGNIFY_ROOT = path.resolve(__dirname, "..", "..");
const BUNDLE_DIR = path.resolve(ALIGNIFY_ROOT, "seo-weekly-report", "data");
const DEFAULT_DEPLOY_ROOT = path.resolve(ALIGNIFY_ROOT, "..", "..", "自有部署项目", "alignify production");

export function getDeployRoot() {
  return process.env.ALIGNIFY_DEPLOY_ROOT || DEFAULT_DEPLOY_ROOT;
}

/** 最新 seo-report-bundle-*.json 路径 */
export function findLatestBundlePath() {
  if (!fs.existsSync(BUNDLE_DIR)) {
    console.error(`✗ 目录不存在: seo-weekly-report/data/`);
    console.error("  请先运行: cd seo-weekly-report/scripts && npm run fetch-all");
    process.exit(1);
  }

  const files = fs
    .readdirSync(BUNDLE_DIR)
    .filter((f) => f.startsWith("seo-report-bundle-") && f.endsWith(".json"))
    .sort()
    .reverse();

  if (files.length === 0) {
    console.error("✗ 未找到 seo-report-bundle-*.json");
    console.error("  请先运行: cd seo-weekly-report/scripts && npm run fetch-all");
    process.exit(1);
  }

  return path.join(BUNDLE_DIR, files[0]);
}

export function loadLatestBundle() {
  const filePath = findLatestBundlePath();
  const raw = JSON.parse(fs.readFileSync(filePath, "utf-8"));
  return { filePath, bundle: raw };
}

/** 将 bundle.gsc.pages 规范化为审计脚本使用的 pages 数组 */
export function normalizeGscPages(bundle, siteUrl = "https://alignify.co") {
  const pages = bundle?.gsc?.pages || [];
  const base = (siteUrl || bundle?.project?.siteUrl || "https://alignify.co").replace(/\/+$/, "");

  return pages.map((p) => {
    let url = (p.url || "").trim();
    if (url && !url.startsWith("http")) {
      url = `${base}${url.startsWith("/") ? "" : "/"}${url}`;
    }
    return {
      url,
      clicks: p.clicks ?? 0,
      impressions: p.impressions ?? 0,
      ctr: p.ctr ?? 0,
      position: p.position ?? 0,
      positionPrev: p.positionPrev ?? p.position ?? 0,
      impressionsPrev: p.impressionsPrev ?? 0,
      clicksPrev: p.clicksPrev ?? 0,
    };
  });
}

export function bundleSummary(bundle, pages) {
  const period = bundle?.period?.current;
  const overall = bundle?.gsc?.overall;
  return {
    dateRange: period
      ? { start: period.start, end: period.end }
      : { start: "?", end: "?" },
    summary: {
      totalPages: pages.length,
      pagesWithClicks: pages.filter((p) => p.clicks > 0).length,
      totalClicks: overall?.clicks ?? pages.reduce((s, p) => s + p.clicks, 0),
      totalImpressions: overall?.impressions ?? pages.reduce((s, p) => s + p.impressions, 0),
    },
  };
}
