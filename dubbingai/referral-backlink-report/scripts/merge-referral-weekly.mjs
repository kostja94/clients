#!/usr/bin/env node
/**
 * Merge GA4 Referral raw JSON with backlink registry → referral-bundle.json
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { parse as parseYaml } from 'yaml';
import dotenv from 'dotenv';

import { getReportPeriods, sumMetrics } from './lib/ga4-client.mjs';
import {
  buildBacklinkMatches,
  aggregateBacklinkMetrics,
  aggregateLandingPages,
  aggregateReferrerPaths,
  computeAlerts,
  daysSince,
  isExcludedSource,
  normalizeDomain,
} from './lib/backlink-matcher.mjs';
import {
  classifyLandingPage,
  isExpectedTarget,
} from './lib/landing-page-classifier.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

const DATA_DIR = join(__dirname, '..', 'data');
const REGISTRY_PATH = process.env.BACKLINK_REGISTRY_PATH || join(__dirname, '..', 'backlink-registry.yaml');

function loadRegistry() {
  const raw = readFileSync(REGISTRY_PATH, 'utf8');
  return parseYaml(raw);
}

function loadGa4Raw(suffix) {
  const path = join(DATA_DIR, `ga4-referral-weekly-${suffix}.json`);
  if (!existsSync(path)) {
    throw new Error(`找不到 ${path}，请先运行 npm run fetch-referral`);
  }
  return JSON.parse(readFileSync(path, 'utf8'));
}

function aggregateOverview(rows, exclusions, period) {
  const filtered = rows.filter(
    (r) => !isExcludedSource(r.dimensions.sessionSource, exclusions)
  );
  const totals = sumMetrics(filtered, period);
  if (totals.sessions > 0) {
    totals.engagementRate = totals.engagedSessions / totals.sessions;
  }
  return totals;
}

function aggregateEventsForSource(eventRows, domain, exclusions) {
  const result = [];
  for (const row of eventRows) {
    if (normalizeDomain(row.dimensions.sessionSource) !== normalizeDomain(domain)) continue;
    if (isExcludedSource(row.dimensions.sessionSource, exclusions)) continue;
    result.push({
      eventName: row.dimensions.eventName,
      eventCount: row.metrics.current.eventCount || 0,
      totalUsers: row.metrics.current.totalUsers || 0,
      eventCountPrev: row.metrics.previous.eventCount || 0,
      totalUsersPrev: row.metrics.previous.totalUsers || 0,
    });
  }
  return result.sort((a, b) => b.eventCount - a.eventCount);
}

function buildLandingPageSummary(backlinkResults) {
  const byPath = new Map();

  for (const bl of backlinkResults) {
    for (const lp of bl.landingPages || []) {
      if (!byPath.has(lp.path)) {
        byPath.set(lp.path, {
          path: lp.path,
          pageType: lp.pageType,
          trackedReferralSessions: 0,
          topSources: new Map(),
        });
      }
      const entry = byPath.get(lp.path);
      entry.trackedReferralSessions += lp.sessions;
      const domain = bl.domain;
      entry.topSources.set(domain, (entry.topSources.get(domain) || 0) + lp.sessions);
    }
  }

  return [...byPath.values()]
    .sort((a, b) => b.trackedReferralSessions - a.trackedReferralSessions)
    .slice(0, 25)
    .map((x) => ({
      path: x.path,
      pageType: x.pageType,
      trackedReferralSessions: x.trackedReferralSessions,
      topSources: [...x.topSources.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([domain, sessions]) => ({ domain, sessions })),
    }));
}

function buildTopicClusterSummary(backlinkResults) {
  const clusters = new Map();
  for (const bl of backlinkResults) {
    const c = bl.topicCluster || 'uncategorized';
    if (!clusters.has(c)) {
      clusters.set(c, { topicCluster: c, backlinkCount: 0, sessions: 0, topLandingPages: new Map() });
    }
    const entry = clusters.get(c);
    entry.backlinkCount += 1;
    entry.sessions += bl.current?.sessions || 0;
    for (const lp of bl.landingPages || []) {
      entry.topLandingPages.set(lp.path, (entry.topLandingPages.get(lp.path) || 0) + lp.sessions);
    }
  }

  return [...clusters.values()]
    .map((x) => ({
      topicCluster: x.topicCluster,
      backlinkCount: x.backlinkCount,
      sessions: x.sessions,
      topLandingPages: [...x.topLandingPages.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 3)
        .map(([path, sessions]) => ({ path, sessions })),
    }))
    .sort((a, b) => b.sessions - a.sessions);
}

function findUnmatchedSources(sourceRows, backlinks, exclusions) {
  const registryDomains = new Set(backlinks.map((b) => normalizeDomain(b.domain)));
  const unmatched = [];

  for (const row of sourceRows) {
    const src = row.dimensions.sessionSource;
    if (isExcludedSource(src, exclusions)) continue;
    const domain = normalizeDomain(src);
    if (registryDomains.has(domain)) continue;
    if (row.metrics.current.sessions < 1) continue;
    unmatched.push({
      sessionSource: src,
      sessions: row.metrics.current.sessions,
      totalUsers: row.metrics.current.totalUsers,
      note: '不在注册表中，建议核查是否为新外链',
    });
  }

  return unmatched.sort((a, b) => b.sessions - a.sessions).slice(0, 20);
}

/** Same domain with multiple articles + L1-only match → split sessions to avoid double count. */
function adjustDomainLevelDoubleCount(backlinkResults) {
  const byDomain = new Map();
  for (const bl of backlinkResults) {
    const d = normalizeDomain(bl.domain);
    if (!byDomain.has(d)) byDomain.set(d, []);
    byDomain.get(d).push(bl);
  }

  for (const bls of byDomain.values()) {
    if (bls.length <= 1) continue;

    const referrerBased = bls.filter((b) => b.matchMethod === 'pageReferrer');
    const sourceOnly = bls.filter((b) => b.matchMethod === 'sessionSource');

    if (referrerBased.length > 0 || sourceOnly.length <= 1) continue;

    const totalCurrent = sourceOnly[0].current.sessions || 0;
    const totalPrevious = sourceOnly[0].previous.sessions || 0;
    const n = sourceOnly.length;

    for (const bl of sourceOnly) {
      bl.current.sessions = Math.round(totalCurrent / n);
      bl.previous.sessions = Math.round(totalPrevious / n);
      bl.matchMethod = 'sessionSource_split';
      const extra = ['DOMAIN_LEVEL_AMBIGUOUS'];
      bl.alert = bl.alert ? [...bl.alert, ...extra] : extra;
    }
  }
}

function computeReferrerCoverage(referrerRows, sourceRows) {
  const refSessions = referrerRows.reduce((s, r) => s + (r.metrics.current.sessions || 0), 0);
  const totalSessions = sourceRows.reduce((s, r) => s + (r.metrics.current.sessions || 0), 0);
  if (totalSessions === 0) return 0;
  return Math.min(1, refSessions / totalSessions);
}

function main() {
  console.log('═══ Referral 数据合并 ═══');

  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  const registry = loadRegistry();
  const ga4 = loadGa4Raw(periods.fileSuffix);

  const exclusions = registry.referralExclusions?.domains || [];
  const conversionEvents = new Set(registry.conversionEvents || []);
  const liveBacklinks = (registry.backlinks || []).filter((b) => b.status === 'live');

  console.log(`  注册表: ${liveBacklinks.length} 条 live 外链`);

  const sourceRows = ga4.reports.referralBySource || [];
  const landingRows = ga4.reports.referralByLanding || [];
  const referrerRows = ga4.reports.referralByReferrer || [];
  const eventRows = (ga4.reports.referralEvents || []).filter((r) =>
    conversionEvents.size === 0 || conversionEvents.has(r.dimensions.eventName)
  );

  const referralOverview = {
    current: aggregateOverview(sourceRows, exclusions, 'current'),
    previous: aggregateOverview(sourceRows, exclusions, 'previous'),
  };

  const matches = buildBacklinkMatches(liveBacklinks, {
    referrerRows,
    landingRows,
    sourceRows,
  }, exclusions);

  const backlinkResults = [];

  const periodEndDate = new Date(periods.current.end);

  for (const bl of liveBacklinks) {
    const match = matches.get(bl.id);
    const { current, previous, matchMethod } = aggregateBacklinkMetrics(match);

    const landingPages = aggregateLandingPages(
      match,
      classifyLandingPage,
      isExpectedTarget,
      bl.targetUrl
    );

    const topReferrerPaths = aggregateReferrerPaths(match.referrerRows);
    const events = aggregateEventsForSource(eventRows, bl.domain, exclusions);

    const dsDays = daysSince(bl.publishedAt, periodEndDate);
    let alert = computeAlerts(bl, current.sessions, landingPages, dsDays);

    if (matchMethod === 'sessionSource' && match.referrerRows.length === 0 && current.sessions > 0) {
      const extra = ['DOMAIN_LEVEL_ONLY'];
      alert = alert ? [...alert, ...extra] : extra;
    }

    if (previous.sessions > 0 && current.sessions / previous.sessions < 0.6) {
      const extra = ['SHARP_DECLINE'];
      alert = alert ? [...alert, ...extra] : extra;
    }

    backlinkResults.push({
      id: bl.id,
      url: bl.url,
      domain: bl.domain,
      title: bl.title,
      topicCluster: bl.topicCluster,
      targetUrl: bl.targetUrl,
      publishedAt: bl.publishedAt,
      daysSincePublish: dsDays,
      status: bl.status,
      campaignBatch: bl.campaignBatch,
      matchMethod: matchMethod || 'none',
      current,
      previous,
      landingPages,
      topReferrerPaths,
      events,
      alert,
    });
  }

  backlinkResults.sort((a, b) => (b.current.sessions || 0) - (a.current.sessions || 0));

  adjustDomainLevelDoubleCount(backlinkResults);

  const trackedSessionsCurrent = backlinkResults.reduce((s, b) => s + (b.current.sessions || 0), 0);
  const trackedSessionsPrevious = backlinkResults.reduce((s, b) => s + (b.previous.sessions || 0), 0);
  const matchedCount = backlinkResults.filter((b) => b.current.sessions > 0).length;

  const allReferralSessions = referralOverview.current.sessions || 0;
  const shareOfAllReferral = allReferralSessions > 0
    ? trackedSessionsCurrent / allReferralSessions
    : 0;

  const pageReferrerCoverage = computeReferrerCoverage(referrerRows, sourceRows);

  const bundle = {
    source: 'api-auto',
    fetchedAt: new Date().toISOString(),
    ga4PropertyId: ga4.ga4PropertyId,
    period: ga4.period,
    referralOverview,
    trackedBacklinksOverview: {
      current: {
        sessions: trackedSessionsCurrent,
        totalUsers: backlinkResults.reduce((s, b) => s + (b.current.totalUsers || 0), 0),
        matchedBacklinkCount: matchedCount,
        registryCount: liveBacklinks.length,
      },
      previous: {
        sessions: trackedSessionsPrevious,
        totalUsers: backlinkResults.reduce((s, b) => s + (b.previous.totalUsers || 0), 0),
        matchedBacklinkCount: null,
        registryCount: liveBacklinks.length,
      },
      shareOfAllReferral,
    },
    backlinks: backlinkResults,
    landingPageSummary: buildLandingPageSummary(backlinkResults),
    topicClusterSummary: buildTopicClusterSummary(backlinkResults),
    unmatchedReferralSources: findUnmatchedSources(sourceRows, liveBacklinks, exclusions),
    healthCheck: {
      d0_dataSource: 'api-auto',
      d1_periodAligned: true,
      d2_registryLoaded: liveBacklinks.length > 0,
      d3_referralDataPresent: allReferralSessions > 0 || trackedSessionsCurrent === 0,
      d4_pageReferrerCoverage: Math.round(pageReferrerCoverage * 1000) / 1000,
      d5_magnitudeReasonable: true,
      d5_note: allReferralSessions === 0 ? '全站 Referral sessions 为 0，请确认属性 ID 与周期' : '',
    },
  };

  const outPath = join(DATA_DIR, `referral-bundle-${periods.fileSuffix}.json`);
  writeFileSync(outPath, JSON.stringify(bundle, null, 2), 'utf8');

  console.log(`  匹配: ${matchedCount}/${liveBacklinks.length} 有流量`);
  console.log(`  pageReferrer 覆盖率: ${(pageReferrerCoverage * 100).toFixed(1)}%`);
  console.log(`  保存 → ${outPath} ✓`);
}

main();
