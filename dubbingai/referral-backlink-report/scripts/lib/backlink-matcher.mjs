/**
 * Match GA4 rows to backlink registry entries.
 */

export function normalizeDomain(input) {
  if (!input) return '';
  let d = input.toLowerCase().trim();
  d = d.replace(/^https?:\/\//, '');
  d = d.replace(/^www\./, '');
  d = d.split('/')[0].split(':')[0];
  return d;
}

export function extractPathFromUrl(url) {
  try {
    return new URL(url).pathname || '/';
  } catch {
    return '/';
  }
}

export function isExcludedSource(source, exclusions = []) {
  const domain = normalizeDomain(source);
  return exclusions.some((ex) => domain === normalizeDomain(ex) || domain.endsWith(`.${normalizeDomain(ex)}`));
}

/** Does pageReferrer URL belong to this backlink article? */
export function referrerMatchesBacklink(pageReferrer, backlink) {
  if (!pageReferrer || pageReferrer === '(not set)') return false;

  const articlePath = extractPathFromUrl(backlink.url);
  const articleDomain = normalizeDomain(backlink.domain || backlink.url);

  try {
    const ref = new URL(pageReferrer.startsWith('http') ? pageReferrer : `https://${pageReferrer}`);
    if (normalizeDomain(ref.hostname) !== articleDomain) return false;
    const refPath = ref.pathname.replace(/\/+$/, '') || '/';
    const normArticle = articlePath.replace(/\/+$/, '') || '/';
    return refPath === normArticle || refPath.startsWith(`${normArticle}/`);
  } catch {
    const lower = pageReferrer.toLowerCase();
    return lower.includes(articleDomain) && lower.includes(articlePath.replace(/\/+$/, ''));
  }
}

export function sourceMatchesBacklink(sessionSource, backlink) {
  return normalizeDomain(sessionSource) === normalizeDomain(backlink.domain || backlink.url);
}

/**
 * Assign GA4 rows to backlinks.
 * Returns Map<backlinkId, { matchMethod, referrerRows, sourceRows }>
 */
export function buildBacklinkMatches(backlinks, { referrerRows, landingRows, sourceRows }, exclusions = []) {
  const matches = new Map();

  for (const bl of backlinks) {
    matches.set(bl.id, {
      backlink: bl,
      matchMethod: null,
      referrerRows: [],
      sourceRows: [],
      landingRows: [],
    });
  }

  for (const row of referrerRows) {
    const ref = row.dimensions.pageReferrer;
    for (const bl of backlinks) {
      if (referrerMatchesBacklink(ref, bl)) {
        const m = matches.get(bl.id);
        m.referrerRows.push(row);
        if (!m.matchMethod) m.matchMethod = 'pageReferrer';
      }
    }
  }

  for (const row of landingRows) {
    const src = row.dimensions.sessionSource;
    if (isExcludedSource(src, exclusions)) continue;
    for (const bl of backlinks) {
      if (sourceMatchesBacklink(src, bl)) {
        matches.get(bl.id).landingRows.push(row);
      }
    }
  }

  for (const row of sourceRows) {
    const src = row.dimensions.sessionSource;
    if (isExcludedSource(src, exclusions)) continue;
    for (const bl of backlinks) {
      if (sourceMatchesBacklink(src, bl)) {
        const m = matches.get(bl.id);
        m.sourceRows.push(row);
        if (!m.matchMethod) m.matchMethod = 'sessionSource';
      }
    }
  }

  return matches;
}

/** Prefer referrer-level metrics; fallback to source-level (avoid double count). */
export function aggregateBacklinkMetrics(match) {
  const useReferrer = match.referrerRows.length > 0;
  const primaryRows = useReferrer ? match.referrerRows : match.sourceRows;

  const current = emptyMetrics();
  const previous = emptyMetrics();

  for (const row of primaryRows) {
    for (const [k, v] of Object.entries(row.metrics.current)) {
      current[k] = (current[k] || 0) + v;
    }
    for (const [k, v] of Object.entries(row.metrics.previous)) {
      previous[k] = (previous[k] || 0) + v;
    }
  }

  return { current, previous, matchMethod: match.matchMethod || (useReferrer ? 'pageReferrer' : 'sessionSource') };
}

function emptyMetrics() {
  return {
    sessions: 0,
    totalUsers: 0,
    newUsers: 0,
    engagedSessions: 0,
    engagementRate: 0,
    averageSessionDuration: 0,
    bounceRate: 0,
  };
}

export function aggregateLandingPages(match, classifyLandingPage, isExpectedTarget, targetUrl) {
  const rows = match.referrerRows.length > 0 ? match.referrerRows : match.landingRows;
  const byPath = new Map();

  for (const row of rows) {
    const path = row.dimensions.landingPage || row.dimensions.pagePath || '';
    if (!path || path === '(not set)') continue;

    if (!byPath.has(path)) {
      byPath.set(path, { path, sessions: 0, totalUsers: 0, sessionsPrev: 0, totalUsersPrev: 0 });
    }
    const entry = byPath.get(path);
    entry.sessions += row.metrics.current.sessions || 0;
    entry.totalUsers += row.metrics.current.totalUsers || 0;
    entry.sessionsPrev += row.metrics.previous.sessions || 0;
    entry.totalUsersPrev += row.metrics.previous.totalUsers || 0;
  }

  const totalSessions = [...byPath.values()].reduce((s, x) => s + x.sessions, 0) || 1;

  return [...byPath.values()]
    .sort((a, b) => b.sessions - a.sessions)
    .map((x) => ({
      path: x.path,
      pageType: classifyLandingPage(x.path),
      sessions: x.sessions,
      totalUsers: x.totalUsers,
      share: x.sessions / totalSessions,
      isExpectedTarget: isExpectedTarget(x.path, targetUrl),
    }));
}

export function aggregateReferrerPaths(referrerRows) {
  const byPath = new Map();
  for (const row of referrerRows) {
    const full = row.dimensions.pageReferrer || '(not set)';
    let path = full;
    try {
      path = new URL(full.startsWith('http') ? full : `https://${full}`).pathname || full;
    } catch {
      /* keep full */
    }
    if (!byPath.has(path)) byPath.set(path, 0);
    byPath.set(path, byPath.get(path) + (row.metrics.current.sessions || 0));
  }
  return [...byPath.entries()]
    .map(([referrerPath, sessions]) => ({ referrerPath, sessions }))
    .sort((a, b) => b.sessions - a.sessions);
}

export function computeAlerts(backlink, currentSessions, landingPages, daysSincePublish) {
  const alerts = [];
  if (backlink.status === 'live' && daysSincePublish >= 7 && currentSessions === 0) {
    alerts.push('ZERO_TRAFFIC_7_DAYS_POST_PUBLISH');
  }

  const targetPath = backlink.targetUrl;
  if (targetPath && currentSessions > 0 && landingPages.length > 0) {
    const targetSessions = landingPages
      .filter((lp) => lp.isExpectedTarget)
      .reduce((s, lp) => s + lp.sessions, 0);
    const matchRate = targetSessions / currentSessions;
    if (matchRate < 0.2) alerts.push('LOW_TARGET_MATCH');
  }

  return alerts.length ? alerts : null;
}

export function daysSince(dateStr, refDate = new Date()) {
  if (!dateStr) return 0;
  const pub = new Date(dateStr);
  const ref = new Date(refDate.getFullYear(), refDate.getMonth(), refDate.getDate());
  return Math.floor((ref - pub) / (86400000));
}
