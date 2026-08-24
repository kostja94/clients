#!/usr/bin/env node
/**
 * Fetch GA4 Referral reports for current + previous week.
 * Output: ../data/ga4-referral-weekly-YYYY-MM-DD.json
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

const REPORTS = [
  {
    key: 'referralBySource',
    label: 'referral-by-source',
    dimensions: ['sessionSource', 'sessionMedium', 'sessionDefaultChannelGroup'],
    metrics: ['sessions', 'totalUsers', 'newUsers', 'engagedSessions', 'engagementRate', 'averageSessionDuration', 'bounceRate'],
  },
  {
    key: 'referralByLanding',
    label: 'referral-by-landing',
    dimensions: ['sessionSource', 'landingPage'],
    metrics: ['sessions', 'totalUsers', 'engagedSessions'],
  },
  {
    key: 'referralByReferrer',
    label: 'referral-by-referrer',
    dimensions: ['pageReferrer', 'landingPage', 'sessionSource'],
    metrics: ['sessions', 'totalUsers'],
    dimensionFilter: {
      andGroup: {
        expressions: [
          {
            filter: {
              fieldName: 'sessionDefaultChannelGroup',
              stringFilter: { matchType: 'EXACT', value: 'Referral' },
            },
          },
          {
            notExpression: {
              filter: {
                fieldName: 'pageReferrer',
                stringFilter: { matchType: 'EXACT', value: '(not set)' },
              },
            },
          },
        ],
      },
    },
  },
  {
    key: 'referralEvents',
    label: 'referral-events',
    dimensions: ['sessionSource', 'eventName'],
    metrics: ['eventCount', 'totalUsers'],
  },
];

async function main() {
  console.log('═══ GA4 Referral 数据拉取 ═══');

  const client = createGa4Client();
  const { propertyId } = getGa4Config();
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);

  console.log(`  周期: ${periods.current.start} ~ ${periods.current.end} (对比 ${periods.previous.start} ~ ${periods.previous.end})`);

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
      dimensionFilter: spec.dimensionFilter,
    });

    output.reports[spec.key] = result.rows;
    console.log(`✓ ${result.rows.length} 行`);
  }

  mkdirSync(DATA_DIR, { recursive: true });
  const outPath = join(DATA_DIR, `ga4-referral-weekly-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  console.log(`  保存 → ${outPath} ✓`);
}

main().catch((err) => {
  console.error('拉取失败:', err.message || err);
  process.exit(1);
});
