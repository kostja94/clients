/**
 * Bundle health checks D0–D5
 */

import { getReportPeriods, parseDateOnly } from './ga4-client.mjs';

function isMondayToSunday(startStr, endStr) {
  const start = parseDateOnly(startStr);
  const end = parseDateOnly(endStr);
  if (Number.isNaN(start.getTime()) || Number.isNaN(end.getTime())) return false;
  const diffDays = Math.round((end - start) / 86400000);
  return start.getDay() === 1 && end.getDay() === 0 && diffDays === 6;
}

export function buildHealthCheck({
  gsc,
  ga4,
  bing,
  overlapRate,
  healthConfig = {},
  period,
}) {
  const periods = period || getReportPeriods(process.env.REPORT_WEEK_END);
  const gscClicks = gsc?.overall?.clicks ?? 0;
  const minClicks = healthConfig.gscWeeklyClicksMin ?? 0;
  const maxClicks = healthConfig.gscWeeklyClicksMax ?? 500000;

  const hasGsc = Boolean(gsc);
  const hasGa4 = Boolean(ga4);
  const hasBing = Boolean(bing);

  let d0 = 'manual';
  if (hasGsc || hasGa4 || hasBing) {
    d0 = hasGsc && hasGa4 && hasBing ? 'api-auto' : 'partial';
  }

  const d2 = {
    pages: Boolean(gsc?.pages?.length || gsc?.dimensions?.pages?.length),
    queries: Boolean(gsc?.queries?.length || gsc?.dimensions?.queries?.length),
    countries: Boolean(gsc?.countries?.length || gsc?.dimensions?.countries?.length),
    devices: Boolean(gsc?.devices?.length || gsc?.dimensions?.devices?.length),
  };

  const magnitudeOk =
    gscClicks === 0 ? true : gscClicks >= minClicks && gscClicks <= maxClicks;

  return {
    d0_dataSource: d0,
    d1_periodAligned: isMondayToSunday(periods.current.start, periods.current.end),
    d1_note: `current ${periods.current.start}~${periods.current.end}`,
    d2_gscDimensionsComplete: d2,
    d3_ga4Present: hasGa4,
    d3_bingPresent: hasBing,
    d4_pageOverlapRate: overlapRate ?? 0,
    d5_magnitudeReasonable: magnitudeOk,
    d5_note:
      gscClicks === 0
        ? 'GSC 点击为 0 — 早期站点正常，请确认属性 URL 正确'
        : !magnitudeOk
          ? `GSC 周点击 ${gscClicks} 超出 health 区间 [${minClicks}, ${maxClicks}]`
          : '',
  };
}
