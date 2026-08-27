/**
 * GSC Search Analytics API client
 */

import { google } from 'googleapis';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { getReportPeriods } from './ga4-client.mjs';
import { stripDomain } from './landing-page-classifier.mjs';
import { loadProjectConfig } from './config.mjs';
import { loadGoogleServiceAccountCredentials } from './google-credentials.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '..', '.env') });

export function getGscConfig() {
  const cfg = loadProjectConfig();
  const siteUrl = process.env.GSC_SITE_URL || cfg.project?.siteUrl;
  if (!siteUrl) {
    throw new Error('Missing GSC_SITE_URL in scripts/.env or project-config.yaml');
  }

  const { client_email: clientEmail, private_key: privateKey } = loadGoogleServiceAccountCredentials();
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
  const result = { periods, dimensions: {} };

  for (const dim of ['page', 'query', 'country', 'device']) {
    process.stdout.write(`  GSC ${dim}... `);
    const [cur, prev] = await Promise.all([
      fetchDimension(client, siteUrl, dim, periods.current.start, periods.current.end),
      fetchDimension(client, siteUrl, dim, periods.previous.start, periods.previous.end),
    ]);

    if (dim === 'page') {
      result.dimensions.pages = mergeDualPeriod(mapPageRows(cur), mapPageRows(prev), 'url');
    } else if (dim === 'query') {
      result.dimensions.queries = mergeDualPeriod(mapQueryRows(cur), mapQueryRows(prev), 'query');
    } else if (dim === 'country') {
      result.dimensions.countries = mergeDualPeriod(mapSimpleRows(cur, 'country'), mapSimpleRows(prev, 'country'), 'country');
    } else if (dim === 'device') {
      result.dimensions.devices = mergeDualPeriod(mapSimpleRows(cur, 'device'), mapSimpleRows(prev, 'device'), 'device');
    }

    const key = dim === 'page' ? 'pages' : dim === 'query' ? 'queries' : dim === 'country' ? 'countries' : 'devices';
    console.log(`✓ ${result.dimensions[key].length} rows`);
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

  return result;
}
