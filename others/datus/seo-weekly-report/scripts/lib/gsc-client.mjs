/**
 * GSC Search Analytics API client for Datus SEO weekly reports.
 */

import { google } from 'googleapis';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { getReportPeriods } from './ga4-client.mjs';
import { stripDomain } from './landing-page-classifier.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

export function getGscConfig() {
  const siteUrl = process.env.GSC_SITE_URL || 'https://datus.ai/';
  const clientEmail = process.env.GSC_CLIENT_EMAIL;
  let privateKey = process.env.GSC_PRIVATE_KEY;

  if (!clientEmail || !privateKey) {
    throw new Error(
      'Missing GSC credentials. Fill GSC_CLIENT_EMAIL and GSC_PRIVATE_KEY in scripts/.env'
    );
  }

  privateKey = privateKey.replace(/\\n/g, '\n');

  return { siteUrl, clientEmail, privateKey };
}

export function createGscClient() {
  const { clientEmail, privateKey } = getGscConfig();
  const auth = new google.auth.JWT({
    email: clientEmail,
    key: privateKey,
    scopes: ['https://www.googleapis.com/auth/webmasters.readonly'],
  });
  return google.searchconsole({ version: 'v1', auth });
}

async function fetchDimension(client, siteUrl, dimension, startDate, endDate, rowLimit = 25000) {
  const rows = [];
  let startRow = 0;

  while (true) {
    const res = await client.searchanalytics.query({
      siteUrl,
      requestBody: {
        startDate,
        endDate,
        dimensions: [dimension],
        rowLimit: Math.min(25000, rowLimit),
        startRow,
        dataState: 'final',
        type: 'web',
      },
    });

    const batch = res.data.rows || [];
    rows.push(...batch);
    if (batch.length < 25000) break;
    startRow += batch.length;
    if (startRow >= rowLimit) break;
  }

  return rows;
}

function mapPageRows(rows) {
  return rows.map((r) => ({
    url: stripDomain(r.keys[0]),
    clicks: r.clicks || 0,
    impressions: r.impressions || 0,
    ctr: r.ctr || 0,
    position: r.position || 0,
  }));
}

function mapQueryRows(rows) {
  return rows.map((r) => ({
    query: r.keys[0],
    clicks: r.clicks || 0,
    impressions: r.impressions || 0,
    ctr: r.ctr || 0,
    position: r.position || 0,
  }));
}

function mapSimpleRows(rows, keyName) {
  return rows.map((r) => ({
    [keyName]: r.keys[0],
    clicks: r.clicks || 0,
    impressions: r.impressions || 0,
    ctr: r.ctr || 0,
    position: r.position || 0,
  }));
}

function mergeDualPeriod(currentRows, previousRows, keyField) {
  const prevMap = new Map(previousRows.map((r) => [r[keyField], r]));
  return currentRows.map((cur) => {
    const prev = prevMap.get(cur[keyField]) || {};
    return {
      ...cur,
      clicksPrev: prev.clicks || 0,
      impressionsPrev: prev.impressions || 0,
      ctrPrev: prev.ctr || 0,
      positionPrev: prev.position || 0,
    };
  });
}

function sumOverall(rows) {
  return rows.reduce(
    (acc, r) => ({
      clicks: acc.clicks + (r.clicks || 0),
      impressions: acc.impressions + (r.impressions || 0),
      ctr: 0,
      avgPosition: 0,
    }),
    { clicks: 0, impressions: 0, ctr: 0, avgPosition: 0 }
  );
}

export async function fetchGscWeeklyBundle() {
  const { siteUrl } = getGscConfig();
  const client = createGscClient();
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);

  const dims = ['page', 'query', 'country', 'device'];
  const result = { periods, dimensions: {} };

  for (const dim of dims) {
    process.stdout.write(`  GSC ${dim}... `);
    const [cur, prev] = await Promise.all([
      fetchDimension(client, siteUrl, dim, periods.current.start, periods.current.end),
      fetchDimension(client, siteUrl, dim, periods.previous.start, periods.previous.end),
    ]);

    if (dim === 'page') {
      const curMapped = mapPageRows(cur);
      const prevMapped = mapPageRows(prev);
      result.dimensions.pages = mergeDualPeriod(curMapped, prevMapped, 'url');
    } else if (dim === 'query') {
      const curMapped = mapQueryRows(cur);
      const prevMapped = mapQueryRows(prev);
      result.dimensions.queries = mergeDualPeriod(curMapped, prevMapped, 'query');
    } else if (dim === 'country') {
      const curMapped = mapSimpleRows(cur, 'country');
      const prevMapped = mapSimpleRows(prev, 'country');
      result.dimensions.countries = mergeDualPeriod(curMapped, prevMapped, 'country');
    } else if (dim === 'device') {
      const curMapped = mapSimpleRows(cur, 'device');
      const prevMapped = mapSimpleRows(prev, 'device');
      result.dimensions.devices = mergeDualPeriod(curMapped, prevMapped, 'device');
    }

    console.log(`✓ ${result.dimensions[dim === 'page' ? 'pages' : dim === 'query' ? 'queries' : dim === 'country' ? 'countries' : 'devices'].length} 行`);
  }

  const pages = result.dimensions.pages || [];
  const queries = result.dimensions.queries || [];

  result.overall = sumOverall(pages.length ? pages : queries);
  const prevPages = await fetchDimension(client, siteUrl, 'page', periods.previous.start, periods.previous.end);
  result.overallPrev = sumOverall(mapPageRows(prevPages));

  if (result.overall.impressions > 0) {
    result.overall.ctr = result.overall.clicks / result.overall.impressions;
  }
  if (result.overallPrev.impressions > 0) {
    result.overallPrev.ctr = result.overallPrev.clicks / result.overallPrev.impressions;
  }

  const blogPages = pages.filter((p) => p.url.startsWith('/blog/'));
  result.blogSummary = {
    clicks: blogPages.reduce((s, p) => s + p.clicks, 0),
    impressions: blogPages.reduce((s, p) => s + p.impressions, 0),
    pageCount: blogPages.length,
    clicksPrev: blogPages.reduce((s, p) => s + (p.clicksPrev || 0), 0),
  };

  return result;
}
