#!/usr/bin/env node
/**
 * Merge GA4 raw JSON with ai-source registry → ai-traffic-bundle.json
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { parse as parseYaml } from 'yaml';
import dotenv from 'dotenv';

import { getReportPeriods, sumMetrics, pctChange } from './lib/ga4-client.mjs';
import {
  buildAiSourceMatches,
  aggregateAiSourceMetrics,
  aggregateLandingPagesForSource,
  aggregateAllPages,
  aggregateChannelBreakdown,
  findUnmatchedAiLikeSources,
  isExcludedSource,
  matchSourceToAiSource,
} from './lib/ai-source-matcher.mjs';
import {
  classifyLandingPage,
  buildAiLandingSummary,
} from './lib/landing-page-classifier.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

const DATA_DIR = join(__dirname, '..', 'data');
const REGISTRY_PATH = process.env.AI_SOURCE_REGISTRY_PATH || join(__dirname, '..', 'ai-source-registry.yaml');

function loadRegistry() {
  return parseYaml(readFileSync(REGISTRY_PATH, 'utf8'));
}

function loadGa4Raw(suffix) {
  const path = join(DATA_DIR, `ga4-traffic-weekly-${suffix}.json`);
  if (!existsSync(path)) {
    throw new Error(`找不到 ${path}，请先运行 npm run fetch-traffic`);
  }
  return JSON.parse(readFileSync(path, 'utf8'));
}

function computeReferrerCoverage(referrerRows, sourceRows) {
  const refSessions = referrerRows.reduce((s, r) => s + (r.metrics.current.sessions || 0), 0);
  const totalSessions = sourceRows.reduce((s, r) => s + (r.metrics.current.sessions || 0), 0);
  if (totalSessions === 0) return 0;
  return Math.min(1, refSessions / totalSessions);
}

function aggregateEventsForAiSource(eventRows, aiSourceId, aiSources, conversionEvents, exclusions) {
  const result = [];

  for (const row of eventRows) {
    const src = row.dimensions.sessionSource;
    if (isExcludedSource(src, exclusions)) continue;
    if (conversionEvents.size > 0 && !conversionEvents.has(row.dimensions.eventName)) continue;
    if (matchSourceToAiSource(src, aiSources) !== aiSourceId) continue;

    result.push({
      eventName: row.dimensions.eventName,
      eventCount: row.metrics.current.eventCount || 0,
      totalUsers: row.metrics.current.totalUsers || 0,
      eventCountPrev: row.metrics.previous.eventCount || 0,
    });
  }

  return result.sort((a, b) => b.eventCount - a.eventCount);
}

function main() {
  console.log('═══ AI 流量数据合并 ═══');

  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  const registry = loadRegistry();
  const ga4 = loadGa4Raw(periods.fileSuffix);

  const exclusions = registry.trafficExclusions?.domains || [];
  const conversionEvents = new Set(registry.conversionEvents || []);
  const aiSources = registry.aiSources || [];

  console.log(`  注册表: ${aiSources.length} 个 AI 来源`);

  const sourceRows = ga4.reports.aiBySource || [];
  const landingRows = ga4.reports.aiByLanding || [];
  const referrerRows = ga4.reports.aiByReferrer || [];
  const pageRows = ga4.reports.allPagesByPath || [];
  const channelRows = ga4.reports.siteByChannel || [];
  const eventRows = ga4.reports.aiEvents || [];

  const aiOverview = {
    current: sumMetrics(sourceRows, 'current'),
    previous: sumMetrics(sourceRows, 'previous'),
  };
  if (aiOverview.current.sessions > 0) {
    aiOverview.current.engagementRate =
      (aiOverview.current.engagedSessions || 0) / aiOverview.current.sessions;
  }

  const siteOverview = {
    current: sumMetrics(channelRows, 'current'),
    previous: sumMetrics(channelRows, 'previous'),
  };

  const allPages = aggregateAllPages(pageRows, (p) => classifyLandingPage(p), 100);

  const { matches, unmatchedSourceRows } = buildAiSourceMatches(
    aiSources,
    { sourceRows, landingRows, referrerRows },
    exclusions
  );

  const aiSourceResults = [];

  for (const src of aiSources) {
    const match = matches.get(src.id);
    const { current, previous, matchMethod } = aggregateAiSourceMetrics(match);

    const landingPages = aggregateLandingPagesForSource(
      landingRows,
      src.id,
      aiSources,
      (p) => classifyLandingPage(p)
    );

    aiSourceResults.push({
      id: src.id,
      label: src.label,
      category: src.category,
      matchMethod: matchMethod || 'none',
      current,
      previous,
      wowSessionsPct: pctChange(current.sessions, previous.sessions),
      landingPages,
      events: aggregateEventsForAiSource(eventRows, src.id, aiSources, conversionEvents, exclusions),
      shareOfAiTraffic:
        aiOverview.current.sessions > 0 ? current.sessions / aiOverview.current.sessions : 0,
    });
  }

  aiSourceResults.sort((a, b) => (b.current.sessions || 0) - (a.current.sessions || 0));

  const aiSessionsCurrent = aiOverview.current.sessions || 0;
  const siteSessionsCurrent = siteOverview.current.sessions || 0;

  const bundle = {
    source: 'api-auto',
    fetchedAt: new Date().toISOString(),
    ga4PropertyId: ga4.ga4PropertyId,
    period: ga4.period,
    sourceRegex: ga4.sourceRegex,
    aiTrafficOverview: aiOverview,
    siteTrafficOverview: siteOverview,
    aiShareOfSite: siteSessionsCurrent > 0 ? aiSessionsCurrent / siteSessionsCurrent : 0,
    aiSources: aiSourceResults,
    aiLandingPageSummary: buildAiLandingSummary(aiSourceResults),
    allPages,
    channelBreakdown: aggregateChannelBreakdown(channelRows),
    unmatchedAiLikeSources: findUnmatchedAiLikeSources(unmatchedSourceRows, aiSources),
    geoContentClusters: registry.geoContentClusters || [],
    healthCheck: {
      d0_dataSource: 'api-auto',
      d1_periodAligned: true,
      d2_registryLoaded: aiSources.length > 0,
      d3_aiDataPresent: aiSessionsCurrent > 0 || aiSourceResults.every((s) => s.current.sessions === 0),
      d4_pageReferrerCoverage: Math.round(computeReferrerCoverage(referrerRows, sourceRows) * 1000) / 1000,
      d5_siteDataPresent: siteSessionsCurrent > 0,
      d5_note:
        aiSessionsCurrent === 0
          ? 'AI sessions 为 0：可能属性 ID 错误、周期无数据，或 AI 点击记为 direct'
          : '',
    },
  };

  const outPath = join(DATA_DIR, `ai-traffic-bundle-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(bundle, null, 2), 'utf8');

  const activeCount = aiSourceResults.filter((s) => s.current.sessions > 0).length;
  console.log(`  活跃 AI 来源: ${activeCount}/${aiSources.length}`);
  console.log(`  AI 占全站 sessions: ${((bundle.aiShareOfSite || 0) * 100).toFixed(1)}%`);
  console.log(`  保存 → ${outPath} ✓`);
}

main();
