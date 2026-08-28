#!/usr/bin/env node
/**
 * Fetch GSC Search Analytics for Datus weekly SEO report.
 * Output: ../data/gsc-weekly-YYYY-MM-DD.json
 */

import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { fetchGscWeeklyBundle } from './lib/gsc-client.mjs';
import { getReportPeriods } from './lib/ga4-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_DIR = join(__dirname, '..', 'data');

async function main() {
  console.log('═══ GSC Datus 搜索数据拉取 ═══');
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  console.log(`  周期: ${periods.current.start} ~ ${periods.current.end} (对比 ${periods.previous.start} ~ ${periods.previous.end})`);

  const bundle = await fetchGscWeeklyBundle();

  const output = {
    source: 'gsc-api',
    fetchedAt: new Date().toISOString(),
    siteUrl: process.env.GSC_SITE_URL || 'https://datus.ai/',
    period: {
      current: periods.current,
      previous: periods.previous,
    },
    overall: bundle.overall,
    overallPrev: bundle.overallPrev,
    blogSummary: bundle.blogSummary,
    dimensions: bundle.dimensions,
  };

  mkdirSync(DATA_DIR, { recursive: true });
  const outPath = join(DATA_DIR, `gsc-weekly-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  console.log(`  保存 → ${outPath} ✓`);
}

main().catch((err) => {
  console.error('GSC 拉取失败:', err.message || err);
  process.exit(1);
});
