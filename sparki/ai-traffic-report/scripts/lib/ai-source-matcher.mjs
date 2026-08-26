/**
 * Match GA4 sessionSource / pageReferrer to AI assistant registry entries.
 */

export function normalizeDomain(input) {
  if (!input) return '';
  let d = input.toLowerCase().trim();
  d = d.replace(/^https?:\/\//, '');
  d = d.replace(/^www\./, '');
  d = d.split('/')[0].split(':')[0];
  return d;
}

export function isExcludedSource(source, exclusions = []) {
  const domain = normalizeDomain(source);
  return exclusions.some(
    (ex) => domain === normalizeDomain(ex) || domain.endsWith(`.${normalizeDomain(ex)}`)
  );
}

/** Match sessionSource string to a registry aiSource id, or null. */
export function matchSourceToAiSource(sessionSource, aiSources) {
  const domain = normalizeDomain(sessionSource);
  if (!domain) return null;

  for (const src of aiSources) {
    for (const pattern of src.matchPatterns || []) {
      const p = normalizeDomain(pattern);
      if (domain === p || domain.endsWith(`.${p}`) || domain.includes(p)) {
        return src.id;
      }
    }
  }
  return null;
}

/** Match pageReferrer URL to aiSource id. */
export function referrerMatchesAiSource(pageReferrer, aiSources) {
  if (!pageReferrer || pageReferrer === '(not set)') return null;

  try {
    const ref = new URL(pageReferrer.startsWith('http') ? pageReferrer : `https://${pageReferrer}`);
    return matchSourceToAiSource(ref.hostname, aiSources);
  } catch {
    const lower = pageReferrer.toLowerCase();
    for (const src of aiSources) {
      for (const pattern of src.matchPatterns || []) {
        if (lower.includes(normalizeDomain(pattern))) return src.id;
      }
    }
  }
  return null;
}

/**
 * Assign GA4 rows to aiSources.
 * Returns Map<aiSourceId, { sourceRows, landingRows, referrerRows }>
 */
export function buildAiSourceMatches(aiSources, { sourceRows, landingRows, referrerRows }, exclusions = []) {
  const matches = new Map();

  for (const src of aiSources) {
    matches.set(src.id, {
      aiSource: src,
      sourceRows: [],
      landingRows: [],
      referrerRows: [],
      matchMethod: null,
    });
  }

  const unmatched = [];

  for (const row of sourceRows) {
    const src = row.dimensions.sessionSource;
    if (isExcludedSource(src, exclusions)) continue;

    const id = matchSourceToAiSource(src, aiSources);
    if (id) {
      const m = matches.get(id);
      m.sourceRows.push(row);
      if (!m.matchMethod) m.matchMethod = 'sessionSource';
    } else {
      unmatched.push(row);
    }
  }

  for (const row of landingRows) {
    const src = row.dimensions.sessionSource;
    if (isExcludedSource(src, exclusions)) continue;

    const id = matchSourceToAiSource(src, aiSources);
    if (id) {
      matches.get(id).landingRows.push(row);
    }
  }

  for (const row of referrerRows) {
    const ref = row.dimensions.pageReferrer;
    const id = referrerMatchesAiSource(ref, aiSources);
    if (id) {
      const m = matches.get(id);
      m.referrerRows.push(row);
      m.matchMethod = 'pageReferrer';
    }
  }

  return { matches, unmatchedSourceRows: unmatched };
}

export function aggregateAiSourceMetrics(match) {
  const rows = match.referrerRows.length > 0 ? match.referrerRows : match.sourceRows;
  const current = sumRowMetrics(rows, 'current');
  const previous = sumRowMetrics(rows, 'previous');

  return {
    current,
    previous,
    matchMethod: match.matchMethod || (match.referrerRows.length ? 'pageReferrer' : 'sessionSource'),
  };
}

function sumRowMetrics(rows, period) {
  const totals = { sessions: 0, totalUsers: 0, engagedSessions: 0 };
  for (const row of rows) {
    totals.sessions += row.metrics[period].sessions || 0;
    totals.totalUsers += row.metrics[period].totalUsers || 0;
    totals.engagedSessions += row.metrics[period].engagedSessions || 0;
  }
  if (totals.sessions > 0) {
    totals.engagementRate = totals.engagedSessions / totals.sessions;
  }
  return totals;
}

export function aggregateLandingPagesForSource(landingRows, aiSourceId, aiSources, classifyLandingPage) {
  const byPath = new Map();

  for (const row of landingRows) {
    const src = row.dimensions.sessionSource;
    if (matchSourceToAiSource(src, aiSources) !== aiSourceId) continue;

    const path = row.dimensions.landingPage || '';
    if (!path || path === '(not set)') continue;

    const normalized = classifyLandingPage(path);
    if (!byPath.has(normalized.path)) {
      byPath.set(normalized.path, {
        path: normalized.path,
        pageType: normalized.pageType,
        sessions: 0,
        totalUsers: 0,
        sessionsPrev: 0,
      });
    }
    const entry = byPath.get(normalized.path);
    entry.sessions += row.metrics.current.sessions || 0;
    entry.totalUsers += row.metrics.current.totalUsers || 0;
    entry.sessionsPrev += row.metrics.previous.sessions || 0;
  }

  return [...byPath.values()].sort((a, b) => b.sessions - a.sessions);
}

export function aggregateAllPages(pageRows, classifyLandingPage, topN = 100) {
  const byPath = new Map();

  for (const row of pageRows) {
    const raw = row.dimensions.pagePath || row.dimensions.landingPage || '';
    if (!raw || raw === '(not set)') continue;

    const normalized = classifyLandingPage(raw);
    if (!byPath.has(normalized.path)) {
      byPath.set(normalized.path, {
        path: normalized.path,
        pageType: normalized.pageType,
        sessions: 0,
        totalUsers: 0,
        screenPageViews: 0,
        sessionsPrev: 0,
        screenPageViewsPrev: 0,
      });
    }
    const entry = byPath.get(normalized.path);
    entry.sessions += row.metrics.current.sessions || 0;
    entry.totalUsers += row.metrics.current.totalUsers || 0;
    entry.screenPageViews += row.metrics.current.screenPageViews || 0;
    entry.sessionsPrev += row.metrics.previous.sessions || 0;
    entry.screenPageViewsPrev += row.metrics.previous.screenPageViews || 0;
  }

  return [...byPath.values()]
    .sort((a, b) => b.sessions - a.sessions)
    .slice(0, topN);
}

export function aggregateChannelBreakdown(channelRows) {
  return channelRows
    .map((row) => ({
      channel: row.dimensions.sessionDefaultChannelGroup,
      sessions: row.metrics.current.sessions || 0,
      totalUsers: row.metrics.current.totalUsers || 0,
      sessionsPrev: row.metrics.previous.sessions || 0,
    }))
    .sort((a, b) => b.sessions - a.sessions);
}

export function findUnmatchedAiLikeSources(unmatchedRows, aiSources) {
  const knownPatterns = new Set();
  for (const src of aiSources) {
    for (const p of src.matchPatterns || []) {
      knownPatterns.add(normalizeDomain(p));
    }
  }

  return unmatchedRows
    .filter((row) => (row.metrics.current.sessions || 0) > 0)
    .map((row) => ({
      sessionSource: row.dimensions.sessionSource,
      sessionMedium: row.dimensions.sessionMedium,
      channelGroup: row.dimensions.sessionDefaultChannelGroup,
      sessions: row.metrics.current.sessions,
      totalUsers: row.metrics.current.totalUsers,
      note: '匹配 sourceRegex 但未在 aiSources 注册，建议追加到 registry',
    }))
    .sort((a, b) => b.sessions - a.sessions)
    .slice(0, 15);
}
