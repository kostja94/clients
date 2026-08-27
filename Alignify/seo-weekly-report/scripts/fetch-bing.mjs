#!/usr/bin/env node
/**
 * Fetch Bing Webmaster JSON API → ../data/bing-weekly-YYYY-MM-DD.json
 */

import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { fetchBingWeeklyBundle } from './lib/bing-client.mjs';
import { getReportPeriods } from './lib/ga4-client.mjs';
import { getBingConfig } from './lib/bing-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_DIR = join(__dirname, '..', 'data');

async function main() {
  console.log('═══ Bing Webmaster 搜索数据拉取 ═══');
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  console.log(
    `  周期: ${periods.current.start} ~ ${periods.current.end} (对比 ${periods.previous.start} ~ ${periods.previous.end})`
  );

  const data = await fetchBingWeeklyBundle();
  const { siteUrl } = getBingConfig();

  const output = {
    source: 'bing-api',
    fetchedAt: new Date().toISOString(),
    siteUrl,
    period: {
      current: periods.current,
      previous: periods.previous,
    },
    ...data,
  };

  mkdirSync(DATA_DIR, { recursive: true });
  const outPath = join(DATA_DIR, `bing-weekly-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  console.log(`  保存 → ${outPath} ✓`);
}

main().catch((err) => {
  console.error('Bing 拉取失败:', err.message || err);
  process.exit(1);
});
