#!/usr/bin/env node
/**
 * Merge GSC + GA4 + Bing → seo-report-bundle-YYYY-MM-DD.json
 */

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { parse as parseYaml } from 'yaml';
import dotenv from 'dotenv';

import { getReportPeriods, sumMetrics, pctChange } from './lib/ga4-client.mjs';
import { splitBrandedMetrics } from './lib/brand-matcher.mjs';
import { classifyLandingPage, stripDomain } from './lib/landing-page-classifier.mjs';
import { buildHealthCheck } from './lib/health-check.mjs';
import { loadProjectConfig, configPath, PACKAGE_ROOT } from './lib/config.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

const DATA_DIR = join(PACKAGE_ROOT, 'data');

function loadYamlIfExists(path) {
  if (!existsSync(path)) return null;
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
  const organic = channelRows.find(
    (r) => r.dimensions.sessionDefaultChannelGroup === 'Organic Search'
  );

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
  const eventSet = new Set(conversionEvents || []);
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

function buildAiAssistant(ga4, projectConfig) {
  const patterns = projectConfig.aiAssistantChannels || ['AI Assistant'];
  const channelRows = ga4?.reports?.byChannel || [];
  const sources = [];
  let sessions = 0;
  let sessionsPrev = 0;

  for (const r of channelRows) {
    const ch = r.dimensions.sessionDefaultChannelGroup || '';
    const matched = patterns.some((p) => ch === p || ch.includes(p));
    if (!matched) continue;
    const s = r.metrics.current.sessions || 0;
    const sp = r.metrics.previous.sessions || 0;
    sources.push({ channel: ch, sessions: s, sessionsPrev: sp });
    sessions += s;
    sessionsPrev += sp;
  }

  if (sources.length === 0) return null;
  return { sessions, sessionsPrev, sources };
}

function computePageOverlap(gscPages, ga4Pages) {
  const ga4Set = new Set(ga4Pages.map((p) => p.path));
  const gscPaths = gscPages.map((p) => p.url).filter(Boolean);
  if (gscPaths.length === 0) return 0;
  const matched = gscPaths.filter((p) => ga4Set.has(p)).length;
  return matched / gscPaths.length;
}

function findWeeklyNewPosts(catalog, start, end) {
  if (!catalog?.posts?.length) return [];
  return catalog.posts
    .filter((p) => {
      const d = p.publishedAt || p.date;
      return d && d >= start && d <= end;
    })
    .map((p) => ({
      slug: p.slug,
      title: p.title || p.slug,
      url: p.url || p.path || '',
      publishedAt: p.publishedAt || p.date,
    }));
}

function attachGscToPosts(posts, gscPages) {
  const pageMap = new Map(gscPages.map((p) => [p.url, p]));
  return posts.map((post) => {
    const path = stripDomain(post.url);
    const gsc = pageMap.get(path);
    return {
      ...post,
      gscClicks: gsc?.clicks || 0,
      gscImpressions: gsc?.impressions || 0,
    };
  });
}

function buildBingBlock(bing) {
  if (!bing) return null;
  const block = {
    overall: bing.overall,
    overallPrev: bing.overallPrev,
    pages: bing.pages || [],
    queries: bing.queries || [],
    crawlIssuesCount: bing.crawlIssuesCount || 0,
  };
  if (bing.overall && bing.overallPrev) {
    block.overallChange = {
      clicksPct: pctChange(bing.overall.clicks, bing.overallPrev.clicks),
      impressionsPct: pctChange(bing.overall.impressions, bing.overallPrev.impressions),
    };
  }
  return block;
}

function main() {
  console.log('═══ SEO 周报数据合并 ═══');

  const projectConfig = loadProjectConfig();
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  const suffix = periods.fileSuffix;

  const brandPath = configPath('brand-query-registry.yaml');
  if (!existsSync(brandPath)) {
    console.warn('⚠ 未找到 config/brand-query-registry.yaml，品牌词拆分将为空（请从 example 复制）');
  }
  const brandRegistry = loadYamlIfExists(brandPath) || {
    brandGroups: [],
  };
  const catalogName = projectConfig.paths?.blogCatalog || 'content-catalog.yaml';
  const catalog = loadYamlIfExists(configPath(catalogName));

  const gscRaw = loadJsonIfExists(join(DATA_DIR, `gsc-weekly-${suffix}.json`));
  const ga4Raw = loadJsonIfExists(join(DATA_DIR, `ga4-weekly-${suffix}.json`));
  const bingRaw = loadJsonIfExists(join(DATA_DIR, `bing-weekly-${suffix}.json`));

  if (!gscRaw && !ga4Raw && !bingRaw) {
    throw new Error(
      `找不到 data/*-weekly-${suffix}.json。请先运行 fetch-gsc / fetch-ga4 / fetch-bing，或改用手动模式。`
    );
  }

  const gscPages = gscRaw?.dimensions?.pages || [];
  const gscQueries = [...(gscRaw?.dimensions?.queries || [])];
  const brandedSplit = gscQueries.length ? splitBrandedMetrics(gscQueries, brandRegistry) : null;

  const ga4Overview = ga4Raw ? buildGa4Overview(ga4Raw) : null;
  const ga4TopPages = ga4Raw ? buildGa4TopPages(ga4Raw) : [];
  const ga4Events = ga4Raw ? buildGa4Events(ga4Raw, projectConfig.conversionEvents) : [];
  const aiAssistant = ga4Raw ? buildAiAssistant(ga4Raw, projectConfig) : null;

  const overlapRate = computePageOverlap(gscPages, ga4TopPages);
  const weeklyNewPosts = attachGscToPosts(
    findWeeklyNewPosts(catalog, periods.current.start, periods.current.end),
    gscPages
  );

  const gscBlock = gscRaw
    ? {
        overall: gscRaw.overall,
        overallPrev: gscRaw.overallPrev,
        branded: brandedSplit?.branded || null,
        nonBranded: brandedSplit?.nonBranded || null,
        category: brandedSplit?.category || null,
        pages: gscPages.slice(0, 50),
        queries: gscQueries.sort((a, b) => b.clicks - a.clicks).slice(0, 50),
        countries: (gscRaw.dimensions?.countries || []).slice(0, 20),
        devices: gscRaw.dimensions?.devices || [],
      }
    : null;

  if (gscBlock?.overall && gscBlock?.overallPrev) {
    gscBlock.overallChange = {
      clicksPct: pctChange(gscBlock.overall.clicks, gscBlock.overallPrev.clicks),
      impressionsPct: pctChange(gscBlock.overall.impressions, gscBlock.overallPrev.impressions),
    };
  }

  const ga4Block = ga4Raw
    ? {
        overall: ga4Overview?.current || null,
        overallPrev: ga4Overview?.previous || null,
        organicSearch: ga4Overview?.organicSearch || null,
        channels: ga4Overview?.channels || [],
        topPages: ga4TopPages,
        events: ga4Events,
        aiAssistant,
      }
    : null;

  const bundle = {
    schemaVersion: '1.0.0',
    source: gscRaw || ga4Raw || bingRaw ? 'api-auto' : 'manual',
    fetchedAt: new Date().toISOString(),
    project: {
      id: projectConfig.project?.id || 'default',
      displayName: projectConfig.project?.displayName || 'Site',
    },
    period: {
      current: periods.current,
      previous: periods.previous,
    },
    gsc: gscBlock,
    ga4: ga4Block,
    bing: buildBingBlock(bingRaw),
    content: {
      weeklyNewPosts,
      weeklyNewCount: weeklyNewPosts.length,
      catalogPresent: Boolean(catalog),
    },
    supplements: {
      manualBlocksParsed: false,
      backlinksTracked: [],
      weeklyContent: [],
    },
    extensions: {
      paidAds: null,
      social: null,
      landingConversionMap: null,
    },
    healthCheck: buildHealthCheck({
      gsc: gscBlock,
      ga4: ga4Block,
      bing: bingRaw,
      overlapRate,
      healthConfig: projectConfig.health || {},
      period: periods,
    }),
  };

  const outPath = join(DATA_DIR, `seo-report-bundle-${suffix}.json`);
  writeFileSync(outPath, JSON.stringify(bundle, null, 2), 'utf8');

  console.log(
    `  GSC: ${gscRaw ? '✓' : '—'}  GA4: ${ga4Raw ? '✓' : '—'}  Bing: ${bingRaw ? '✓' : '—'}`
  );
  console.log(`  本周新内容: ${weeklyNewPosts.length} 条`);
  console.log(`  d4 页面对齐率: ${(overlapRate * 100).toFixed(1)}%`);
  console.log(`  保存 → ${outPath} ✓`);
}

try {
  main();
} catch (err) {
  console.error('合并失败:', err.message || err);
  process.exit(1);
}
