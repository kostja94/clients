#!/usr/bin/env node
/**
 * Merge GSC + GA4 + blog-catalog → seo-report-bundle-YYYY-MM-DD.json
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { parse as parseYaml } from 'yaml';
import dotenv from 'dotenv';

import { getReportPeriods, sumMetrics, pctChange } from './lib/ga4-client.mjs';
import { splitBrandedMetrics } from './lib/brand-matcher.mjs';
import {
  aggregateClusterMetrics,
  findWeeklyNewPosts,
  attachFirstWeekGscPerformance,
  summarizeBlogInventory,
  matchBlogPostToCluster,
} from './lib/content-cluster-matcher.mjs';
import { classifyLandingPage, stripDomain } from './lib/landing-page-classifier.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

const ROOT = join(__dirname, '..');
const DATA_DIR = join(ROOT, 'data');

function loadYaml(path) {
  return parseYaml(readFileSync(path, 'utf8'));
}

function loadJsonIfExists(path) {
  if (!existsSync(path)) return null;
  return JSON.parse(readFileSync(path, 'utf8'));
}

function buildGa4Overview(ga4) {
  if (!ga4?.reports?.byChannel) return null;

  const channelRows = ga4.reports.byChannel;
  const cur = sumMetrics(channelRows, 'current');
  const prev = sumMetrics(channelRows, 'previous');

  const organic = channelRows.find((r) => r.dimensions.sessionDefaultChannelGroup === 'Organic Search');

  return {
    current: {
      sessions: cur.sessions || 0,
      totalUsers: cur.totalUsers || 0,
      screenPageViews: cur.screenPageViews || 0,
      engagedSessions: cur.engagedSessions || 0,
    },
    previous: {
      sessions: prev.sessions || 0,
      totalUsers: prev.totalUsers || 0,
      screenPageViews: prev.screenPageViews || 0,
      engagedSessions: prev.engagedSessions || 0,
    },
    organicSearch: organic
      ? {
          sessions: organic.metrics.current.sessions || 0,
          sessionsPrev: organic.metrics.previous.sessions || 0,
        }
      : null,
    channels: channelRows
      .map((r) => ({
        channel: r.dimensions.sessionDefaultChannelGroup,
        sessions: r.metrics.current.sessions || 0,
        sessionsPrev: r.metrics.previous.sessions || 0,
        screenPageViews: r.metrics.current.screenPageViews || 0,
      }))
      .sort((a, b) => b.sessions - a.sessions)
      .slice(0, 15),
  };
}

function buildGa4TopPages(ga4) {
  const rows = ga4?.reports?.topLandingPages || ga4?.reports?.topPages || [];
  return rows
    .map((r) => {
      const path = stripDomain(r.dimensions.landingPage || r.dimensions.pagePath);
      const { pageType } = classifyLandingPage(path);
      return {
        path,
        pageType,
        sessions: r.metrics.current.sessions || 0,
        sessionsPrev: r.metrics.previous.sessions || 0,
        screenPageViews: r.metrics.current.screenPageViews || 0,
        totalUsers: r.metrics.current.totalUsers || 0,
      };
    })
    .sort((a, b) => b.sessions - a.sessions)
    .slice(0, 30);
}

function buildGa4Events(ga4, conversionEvents) {
  const rows = ga4?.reports?.events || [];
  const eventSet = new Set(conversionEvents);
  return rows
    .filter((r) => eventSet.size === 0 || eventSet.has(r.dimensions.eventName))
    .map((r) => ({
      eventName: r.dimensions.eventName,
      eventCount: r.metrics.current.eventCount || 0,
      totalUsers: r.metrics.current.totalUsers || 0,
      eventCountPrev: r.metrics.previous.eventCount || 0,
    }))
    .sort((a, b) => b.eventCount - a.eventCount);
}

function computePageOverlap(gscPages, ga4Pages) {
  const ga4Set = new Set(ga4Pages.map((p) => p.path));
  const gscPaths = gscPages.map((p) => p.url).filter(Boolean);
  if (gscPaths.length === 0) return 0;
  const matched = gscPaths.filter((p) => ga4Set.has(p)).length;
  return matched / gscPaths.length;
}

function buildHealthCheck({ gsc, ga4, brandRegistry, catalog, overlapRate }) {
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  const gscClicks = gsc?.overall?.clicks || 0;

  return {
    d0_dataSource: gsc && ga4 ? 'api-auto' : gsc ? 'gsc-only' : ga4 ? 'ga4-only' : 'manual',
    d1_periodAligned: true,
    d1_note: `current ${periods.current.start}~${periods.current.end}`,
    d2_gscDimensionsComplete: {
      pages: Boolean(gsc?.dimensions?.pages?.length),
      queries: Boolean(gsc?.dimensions?.queries?.length),
      countries: Boolean(gsc?.dimensions?.countries?.length),
      devices: Boolean(gsc?.dimensions?.devices?.length),
    },
    d3_ga4Present: Boolean(ga4),
    d3_bingPresent: false,
    d4_pageOverlapRate: overlapRate,
    d4_blogCatalogSynced: Boolean(catalog?.meta?.syncedAt),
    d5_magnitudeReasonable: gscClicks === 0 || (gscClicks >= 1 && gscClicks <= 5000),
    d5_note: gscClicks === 0 ? 'GSC 点击为 0 — 早期站点正常，确认属性 URL 正确' : '',
  };
}

function main() {
  console.log('═══ Datus SEO 周报数据合并 ═══');

  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  const suffix = periods.fileSuffix;

  const brandRegistry = loadYaml(join(ROOT, 'brand-query-registry.yaml'));
  const clusterRegistry = loadYaml(join(ROOT, 'content-cluster-registry.yaml'));
  const catalog = loadYaml(join(ROOT, 'blog-catalog.yaml'));

  const gsc = loadJsonIfExists(join(DATA_DIR, `gsc-weekly-${suffix}.json`));
  const ga4 = loadJsonIfExists(join(DATA_DIR, `ga4-weekly-${suffix}.json`));

  if (!gsc && !ga4) {
    throw new Error(`找不到 data/gsc-weekly-${suffix}.json 或 ga4-weekly-${suffix}.json。请先运行 fetch 或改用手动模式。`);
  }

  const gscPages = gsc?.dimensions?.pages || [];
  const gscQueries = [...(gsc?.dimensions?.queries || [])];

  const brandedSplit = gscQueries.length
    ? splitBrandedMetrics(gscQueries, brandRegistry)
    : null;

  const contentClusters = gscPages.length
    ? aggregateClusterMetrics(gscPages, clusterRegistry)
    : [];

  const weeklyNewPosts = findWeeklyNewPosts(catalog, periods.current.start, periods.current.end);
  const newPostsWithGsc = attachFirstWeekGscPerformance(weeklyNewPosts, gscPages, { current: periods.current });

  const newPostsEnriched = newPostsWithGsc.map((p) => {
    const post = catalog.posts.find((x) => x.slug === p.slug) || p;
    const cluster = matchBlogPostToCluster(post, clusterRegistry);
    return { ...p, clusterId: cluster.clusterId, clusterLabel: cluster.clusterLabel };
  });

  const ga4Overview = ga4 ? buildGa4Overview(ga4) : null;
  const ga4TopPages = ga4 ? buildGa4TopPages(ga4) : [];
  const ga4Events = ga4 ? buildGa4Events(ga4, clusterRegistry.conversionEvents || []) : [];

  const overlapRate = computePageOverlap(gscPages, ga4TopPages);

  const bundle = {
    source: 'api-auto',
    fetchedAt: new Date().toISOString(),
    period: {
      current: periods.current,
      previous: periods.previous,
    },

    gsc: gsc
      ? {
          overall: gsc.overall,
          overallPrev: gsc.overallPrev,
          blogSummary: gsc.blogSummary,
          branded: brandedSplit?.branded || null,
          nonBranded: brandedSplit?.nonBranded || null,
          category: brandedSplit?.category || null,
          pages: gscPages.slice(0, 50),
          queries: gscQueries.sort((a, b) => b.clicks - a.clicks).slice(0, 50),
          countries: (gsc.dimensions?.countries || []).slice(0, 20),
          devices: gsc.dimensions?.devices || [],
        }
      : null,

    ga4: ga4
      ? {
          overall: ga4Overview?.current || null,
          overallPrev: ga4Overview?.previous || null,
          organicSearch: ga4Overview?.organicSearch || null,
          channels: ga4Overview?.channels || [],
          topPages: ga4TopPages,
          events: ga4Events,
        }
      : null,

    blog: {
      inventory: summarizeBlogInventory(catalog),
      weeklyNewPosts: newPostsEnriched,
      weeklyNewCount: newPostsEnriched.length,
    },

    contentClusters,

    healthCheck: buildHealthCheck({
      gsc,
      ga4,
      brandRegistry,
      catalog,
      overlapRate,
    }),
  };

  if (gsc?.overall && gsc?.overallPrev) {
    bundle.gsc.overallChange = {
      clicksPct: pctChange(gsc.overall.clicks, gsc.overallPrev.clicks),
      impressionsPct: pctChange(gsc.overall.impressions, gsc.overallPrev.impressions),
    };
  }

  const outPath = join(DATA_DIR, `seo-report-bundle-${suffix}.json`);
  writeFileSync(outPath, JSON.stringify(bundle, null, 2), 'utf8');

  console.log(`  GSC: ${gsc ? '✓' : '—'}  GA4: ${ga4 ? '✓' : '—'}`);
  console.log(`  本周新发布 blog: ${newPostsEnriched.length} 篇`);
  console.log(`  保存 → ${outPath} ✓`);
}

main();
