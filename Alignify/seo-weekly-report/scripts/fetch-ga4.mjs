#!/usr/bin/env node
/**
 * Fetch GA4 Data API → ../data/ga4-weekly-YYYY-MM-DD.json
 */

import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import {
  createGa4Client,
  getGa4Config,
  getReportPeriods,
  runDualPeriodReport,
} from './lib/ga4-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_DIR = join(__dirname, '..', 'data');

const BASE_METRICS = [
  'sessions',
  'totalUsers',
  'newUsers',
  'engagedSessions',
  'engagementRate',
  'averageSessionDuration',
  'bounceRate',
  'screenPageViews',
];
const LIGHT_METRICS = ['sessions', 'totalUsers', 'engagedSessions', 'screenPageViews'];

async function main() {
  console.log('═══ GA4 流量数据拉取 ═══');

  const client = createGa4Client();
  const { propertyId } = getGa4Config();
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);

  console.log(
    `  周期: ${periods.current.start} ~ ${periods.current.end} (对比 ${periods.previous.start} ~ ${periods.previous.end})`
  );

  const REPORTS = [
    { key: 'siteOverview', label: 'site-overview', dimensions: ['date'], metrics: BASE_METRICS },
    { key: 'byChannel', label: 'by-channel', dimensions: ['sessionDefaultChannelGroup'], metrics: LIGHT_METRICS },
    {
      key: 'bySourceMedium',
      label: 'by-source-medium',
      dimensions: ['sessionSource', 'sessionMedium'],
      metrics: LIGHT_METRICS,
    },
    { key: 'topLandingPages', label: 'top-landing', dimensions: ['landingPage'], metrics: LIGHT_METRICS },
    { key: 'topPages', label: 'top-pages', dimensions: ['pagePath'], metrics: LIGHT_METRICS },
    { key: 'events', label: 'events', dimensions: ['eventName'], metrics: ['eventCount', 'totalUsers'] },
  ];

  const output = {
    source: 'ga4-api',
    fetchedAt: new Date().toISOString(),
    ga4PropertyId: propertyId,
    period: {
      current: periods.current,
      previous: periods.previous,
    },
    reports: {},
  };

  let step = 0;
  for (const spec of REPORTS) {
    step += 1;
    process.stdout.write(`  [${step}/${REPORTS.length}] ${spec.label}... `);
    const result = await runDualPeriodReport(client, propertyId, {
      dimensions: spec.dimensions,
      metrics: spec.metrics,
    });
    output.reports[spec.key] = result.rows;
    console.log(`✓ ${result.rows.length} 行`);
  }

  mkdirSync(DATA_DIR, { recursive: true });
  const outPath = join(DATA_DIR, `ga4-weekly-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  console.log(`  保存 → ${outPath} ✓`);
}

main().catch((err) => {
  console.error('GA4 拉取失败:', err.message || err);
  process.exit(1);
});
