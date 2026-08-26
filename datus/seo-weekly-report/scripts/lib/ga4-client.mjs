/**
 * GA4 Data API client helpers for Datus SEO weekly reports.
 */

import { BetaAnalyticsDataClient } from '@google-analytics/data';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

export function getGa4Config() {
  const propertyId = process.env.GA4_PROPERTY_ID;
  const clientEmail = process.env.GA4_CLIENT_EMAIL || process.env.GSC_CLIENT_EMAIL;
  let privateKey = process.env.GA4_PRIVATE_KEY || process.env.GSC_PRIVATE_KEY;

  if (!propertyId || !clientEmail || !privateKey) {
    throw new Error(
      'Missing GA4 credentials. Copy .env.example to .env and fill GA4_PROPERTY_ID, GA4_CLIENT_EMAIL, GA4_PRIVATE_KEY.'
    );
  }

  privateKey = privateKey.replace(/\\n/g, '\n');

  return { propertyId, clientEmail, privateKey };
}

export function createGa4Client() {
  const { clientEmail, privateKey } = getGa4Config();
  return new BetaAnalyticsDataClient({
    credentials: {
      client_email: clientEmail,
      private_key: privateKey,
    },
  });
}

export async function runDualPeriodReport(client, propertyId, { dimensions, metrics, dimensionFilter, limit = 10000 }) {
  const periods = getReportPeriods(process.env.REPORT_WEEK_END);
  const dimensionNames = dimensions.map((d) => ({ name: d }));
  const metricNames = metrics.map((m) => ({ name: m }));

  const request = {
    property: `properties/${propertyId}`,
    dateRanges: [
      { startDate: periods.current.start, endDate: periods.current.end, name: 'current' },
      { startDate: periods.previous.start, endDate: periods.previous.end, name: 'previous' },
    ],
    dimensions: dimensionNames,
    metrics: metricNames,
    limit,
  };

  if (dimensionFilter) {
    request.dimensionFilter = dimensionFilter;
  }

  const [response] = await client.runReport(request);

  return {
    periods,
    rows: parseDualPeriodRows(response, dimensions, metrics),
  };
}

function parseDualPeriodRows(response, dimensions, metrics) {
  const parsed = [];
  if (!response.rows) return parsed;

  for (const row of response.rows) {
    const dimValues = {};
    dimensions.forEach((name, i) => {
      dimValues[name] = row.dimensionValues[i]?.value ?? '';
    });

    const metricValues = { current: {}, previous: {} };
    metrics.forEach((name, mi) => {
      const baseIdx = mi * 2;
      metricValues.current[name] = parseMetric(row.metricValues[baseIdx]?.value);
      metricValues.previous[name] = parseMetric(row.metricValues[baseIdx + 1]?.value);
    });

    parsed.push({ dimensions: dimValues, metrics: metricValues });
  }
  return parsed;
}

function parseMetric(val) {
  if (val === undefined || val === null || val === '') return 0;
  const n = Number(val);
  return Number.isFinite(n) ? n : 0;
}

export function getReportPeriods(weekEndOverride) {
  const weekEnd = weekEndOverride ? parseDateOnly(weekEndOverride) : getLastSunday();

  const currentEnd = weekEnd;
  const currentStart = addDays(currentEnd, -6);
  const previousEnd = addDays(currentStart, -1);
  const previousStart = addDays(previousEnd, -6);

  return {
    current: { start: formatDate(currentStart), end: formatDate(currentEnd) },
    previous: { start: formatDate(previousStart), end: formatDate(previousEnd) },
    fileSuffix: formatDate(currentEnd),
  };
}

function getLastSunday(ref = new Date()) {
  const d = new Date(ref.getFullYear(), ref.getMonth(), ref.getDate());
  const dow = d.getDay();
  d.setDate(d.getDate() - (dow === 0 ? 7 : dow));
  return d;
}

function parseDateOnly(str) {
  const [y, m, d] = str.split('-').map(Number);
  return new Date(y, m - 1, d);
}

function addDays(date, n) {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d;
}

function formatDate(date) {
  const y = date.getFullYear();
  const m = String(date.getMonth() + 1).padStart(2, '0');
  const d = String(date.getDate()).padStart(2, '0');
  return `${y}-${m}-${d}`;
}

export function sumMetrics(rows, period = 'current') {
  const totals = {};
  for (const row of rows) {
    for (const [key, val] of Object.entries(row.metrics[period])) {
      totals[key] = (totals[key] || 0) + val;
    }
  }
  return totals;
}

export function pctChange(current, previous) {
  if (previous === 0) return current > 0 ? 1 : 0;
  return (current - previous) / previous;
}

export function buildOrganicFilter() {
  return {
    filter: {
      fieldName: 'sessionDefaultChannelGroup',
      stringFilter: { matchType: 'EXACT', value: 'Organic Search' },
    },
  };
}
