#!/usr/bin/env node
/**
 * Fetch GA4 data for Sparki AI traffic report:
 * - AI assistant sources (filtered by registry regex)
 * - All pages (all channels)
 * - Site channel overview
 *
 * Output: ../data/ga4-traffic-weekly-YYYY-MM-DD.json
 */

import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { parse as parseYaml } from 'yaml';
import {
  createGa4Client,
  getGa4Config,
  getReportPeriods,
  runDualPeriodReport,
  buildSourceRegexFilter,
  buildReferrerRegexFilter,
} from './lib/ga4-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const DATA_DIR = join(__dirname, '..', 'data');
const REGISTRY_PATH = process.env.AI_SOURCE_REGISTRY_PATH || join(__dirname, '..', 'ai-source-registry.yaml');

function loadRegistry() {
  return parseYaml(readFileSync(REGISTRY_PATH, 'utf8'));
}

const BASE_METRICS = ['sessions', 'totalUsers', 'newUsers', 'engagedSessions', 'engagementRate', 'averageSessionDuration', 'bounceRate'];
const LIGHT_METRICS = ['sessions', 'totalUsers', 'engagedSessions'];

async function main() {
  console.log('═══ GA4 Sparki 流量数据拉取 ═══');

  const registry = loadRegistry();
  const sourceRegex = registry.sourceRegex?.replace(/\s+/g, '') || '';
  if (!sourceRegex) {
    throw new Error('ai-source-registry.yaml 缺少 sourceRegex');
  }

  const client = createGa4Client();
  const { propertyId } = getGa4Config();
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);

  console.log(`  周期: ${periods.current.start} ~ ${periods.current.end} (对比 ${periods.previous.start} ~ ${periods.previous.end})`);

  const aiFilter = buildSourceRegexFilter(sourceRegex);
  const referrerFilter = buildReferrerRegexFilter(sourceRegex);

  const REPORTS = [
    {
      key: 'aiBySource',
      label: 'ai-by-source',
      dimensions: ['sessionSource', 'sessionMedium', 'sessionDefaultChannelGroup'],
      metrics: BASE_METRICS,
      dimensionFilter: aiFilter,
    },
    {
      key: 'aiByLanding',
      label: 'ai-by-landing',
      dimensions: ['sessionSource', 'landingPage'],
      metrics: LIGHT_METRICS,
      dimensionFilter: aiFilter,
    },
    {
      key: 'aiByReferrer',
      label: 'ai-by-referrer',
      dimensions: ['pageReferrer', 'landingPage', 'sessionSource'],
      metrics: ['sessions', 'totalUsers'],
      dimensionFilter: referrerFilter,
    },
    {
      key: 'allPagesByPath',
      label: 'all-pages-by-path',
      dimensions: ['pagePath'],
      metrics: ['sessions', 'totalUsers', 'screenPageViews', 'engagedSessions'],
      dimensionFilter: null,
    },
    {
      key: 'allPagesByLanding',
      label: 'all-pages-by-landing',
      dimensions: ['landingPage'],
      metrics: ['sessions', 'totalUsers', 'engagedSessions'],
      dimensionFilter: null,
    },
    {
      key: 'siteByChannel',
      label: 'site-by-channel',
      dimensions: ['sessionDefaultChannelGroup'],
      metrics: ['sessions', 'totalUsers', 'engagedSessions'],
      dimensionFilter: null,
    },
    {
      key: 'aiEvents',
      label: 'ai-events',
      dimensions: ['sessionSource', 'eventName'],
      metrics: ['eventCount', 'totalUsers'],
      dimensionFilter: aiFilter,
    },
  ];

  const output = {
    source: 'ga4-api',
    fetchedAt: new Date().toISOString(),
    ga4PropertyId: propertyId,
    period: {
      current: periods.current,
      previous: periods.previous,
    },
    sourceRegex,
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
  const outPath = join(DATA_DIR, `ga4-traffic-weekly-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  console.log(`  保存 → ${outPath} ✓`);
}

main().catch((err) => {
  console.error('拉取失败:', err.message || err);
  process.exit(1);
});
