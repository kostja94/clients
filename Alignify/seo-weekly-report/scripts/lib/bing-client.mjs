/**
 * Bing Webmaster JSON API — weekly aggregation
 */

import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { getReportPeriods } from './ga4-client.mjs';
import { stripDomain } from './landing-page-classifier.mjs';
import { loadProjectConfig } from './config.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '..', '.env') });

const BING_BASE = 'https://ssl.bing.com/webmaster/api.svc';

export function getBingConfig() {
  const cfg = loadProjectConfig();
  const siteUrl = process.env.BING_SITE_URL || cfg.project?.siteUrl;
  const apiKey = process.env.BING_API_KEY;
  if (!apiKey || !siteUrl) {
    throw new Error('Missing BING_API_KEY or BING_SITE_URL in scripts/.env');
  }
  return { siteUrl, apiKey };
}

function parseMsDate(str) {
  if (!str) return null;
  const m = String(str).match(/\/Date\((\d+)([+-]\d+)?\)\//);
  if (!m) return null;
  return new Date(parseInt(m[1], 10));
}

function parseDateOnly(str) {
  const [y, m, d] = str.split('-').map(Number);
  return new Date(y, m - 1, d);
}

function dateInRange(date, startStr, endStr) {
  if (!date) return false;
  const start = parseDateOnly(startStr);
  const end = parseDateOnly(endStr);
  end.setHours(23, 59, 59, 999);
  return date >= start && date <= end;
}

async function fetchBingJson(method, siteUrl, apiKey) {
  const encodedSite = encodeURIComponent(siteUrl);
  const url = `${BING_BASE}/json/${method}?siteUrl=${encodedSite}&apikey=${apiKey}`;
  const res = await fetch(url, { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Bing ${method} HTTP ${res.status}: ${text.slice(0, 200)}`);
  }
  const data = await res.json();
  if (data.ErrorCode) {
    throw new Error(`Bing ${method} ErrorCode ${data.ErrorCode}: ${data.Message}`);
  }
  return data.d || [];
}

function aggregatePageRows(rows, start, end) {
  const filtered = rows.filter((row) => {
    const date = parseMsDate(row.Date);
    return dateInRange(date, start, end);
  });

  const pageMap = new Map();
  for (const row of filtered) {
    const rawUrl = row.Query || '';
    if (!rawUrl.startsWith('http')) continue;
    const path = stripDomain(rawUrl);
    const existing = pageMap.get(path) || { url: path, clicks: 0, impressions: 0, positions: [] };
    existing.clicks += row.Clicks || 0;
    existing.impressions += row.Impressions || 0;
    const pos = row.AvgImpressionPosition || 0;
    if (pos > 0 && row.Impressions > 0) {
      existing.positions.push({ pos, weight: row.Impressions });
    }
    pageMap.set(path, existing);
  }

  return Array.from(pageMap.values()).map((p) => {
    let avgPos = 0;
    if (p.positions.length > 0) {
      const totalWeight = p.positions.reduce((s, x) => s + x.weight, 0);
      avgPos = totalWeight > 0 ? p.positions.reduce((s, x) => s + x.pos * x.weight, 0) / totalWeight : 0;
    }
    return {
      url: p.url,
      clicks: p.clicks,
      impressions: p.impressions,
      ctr: p.impressions > 0 ? p.clicks / p.impressions : 0,
      position: avgPos,
    };
  });
}

function aggregateQueryRows(rows, start, end) {
  const filtered = rows.filter((row) => dateInRange(parseMsDate(row.Date), start, end));
  const qMap = new Map();
  for (const row of filtered) {
    const q = row.Query || '';
    if (!q || q.startsWith('http')) continue;
    const existing = qMap.get(q) || { query: q, clicks: 0, impressions: 0, positions: [] };
    existing.clicks += row.Clicks || 0;
    existing.impressions += row.Impressions || 0;
    const pos = row.AvgImpressionPosition || row.AvgClickPosition || 0;
    if (pos > 0 && row.Impressions > 0) {
      existing.positions.push({ pos, weight: row.Impressions });
    }
    qMap.set(q, existing);
  }

  return Array.from(qMap.values()).map((q) => {
    let avgPos = 0;
    if (q.positions.length > 0) {
      const w = q.positions.reduce((s, x) => s + x.weight, 0);
      avgPos = w > 0 ? q.positions.reduce((s, x) => s + x.pos * x.weight, 0) / w : 0;
    }
    return {
      query: q.query,
      clicks: q.clicks,
      impressions: q.impressions,
      ctr: q.impressions > 0 ? q.clicks / q.impressions : 0,
      position: avgPos,
    };
  });
}

function sumPages(pages) {
  const t = pages.reduce(
    (acc, p) => ({
      clicks: acc.clicks + p.clicks,
      impressions: acc.impressions + p.impressions,
    }),
    { clicks: 0, impressions: 0 }
  );
  t.ctr = t.impressions > 0 ? t.clicks / t.impressions : 0;
  t.avgPosition = 0;
  return t;
}

export async function fetchBingWeeklyBundle() {
  const { siteUrl, apiKey } = getBingConfig();
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);

  process.stdout.write('  Bing GetPageStats... ');
  const pageRows = await fetchBingJson('GetPageStats', siteUrl, apiKey);
  console.log(`✓ ${pageRows.length} raw`);

  process.stdout.write('  Bing GetQueryStats... ');
  const queryRows = await fetchBingJson('GetQueryStats', siteUrl, apiKey);
  console.log(`✓ ${queryRows.length} raw`);

  let crawlIssuesCount = 0;
  try {
    process.stdout.write('  Bing GetCrawlIssues... ');
    const issues = await fetchBingJson('GetCrawlIssues', siteUrl, apiKey);
    crawlIssuesCount = Array.isArray(issues) ? issues.length : 0;
    console.log(`✓ ${crawlIssuesCount}`);
  } catch {
    console.log('— skip');
  }

  const curPages = aggregatePageRows(pageRows, periods.current.start, periods.current.end);
  const prevPages = aggregatePageRows(pageRows, periods.previous.start, periods.previous.end);
  const curQueries = aggregateQueryRows(queryRows, periods.current.start, periods.current.end);
  const prevQueries = aggregateQueryRows(queryRows, periods.previous.start, periods.previous.end);

  const prevPageMap = new Map(prevPages.map((p) => [p.url, p]));
  const pages = curPages.map((p) => {
    const prev = prevPageMap.get(p.url) || {};
    return { ...p, clicksPrev: prev.clicks || 0, impressionsPrev: prev.impressions || 0 };
  });

  const prevQMap = new Map(prevQueries.map((q) => [q.query, q]));
  const queries = curQueries.map((q) => {
    const prev = prevQMap.get(q.query) || {};
    return { ...q, clicksPrev: prev.clicks || 0, impressionsPrev: prev.impressions || 0 };
  });

  return {
    overall: sumPages(curPages),
    overallPrev: sumPages(prevPages),
    pages: pages.sort((a, b) => b.clicks - a.clicks).slice(0, 50),
    queries: queries.sort((a, b) => b.clicks - a.clicks).slice(0, 50),
    crawlIssuesCount,
  };
}
