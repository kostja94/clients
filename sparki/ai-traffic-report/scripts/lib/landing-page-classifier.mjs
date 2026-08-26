/**
 * Landing page path classification for sparki.io
 */

const RULES = [
  { type: 'homepage', test: (p) => p === '/' },
  { type: 'feature', test: (p) => p === '/features' || p.startsWith('/features/') },
  { type: 'pricing', test: (p) => p === '/pricing' || p.startsWith('/pricing/') || p === '/#pricing' },
  { type: 'blog', test: (p) => p === '/blog' || p.startsWith('/blog/') },
  { type: 'auth', test: (p) =>
    ['/login', '/sign-in', '/register', '/signup', '/sign-up'].some((x) => p === x || p.startsWith(`${x}/`)) },
  { type: 'enterprise', test: (p) => p === '/enterprise' || p.startsWith('/enterprise/') },
  { type: 'docs', test: (p) => p === '/docs' || p.startsWith('/docs/') },
  { type: 'legal', test: (p) =>
    ['/privacy', '/terms', '/legal'].some((x) => p === x || p.startsWith(`${x}/`)) },
];

export function normalizePath(raw) {
  if (!raw || raw === '(not set)') return '';
  let p = raw.split('?')[0].trim();
  if (!p.startsWith('/')) p = `/${p}`;
  return p.replace(/\/+$/, '') || '/';
}

export function classifyLandingPage(rawPath) {
  const path = normalizePath(rawPath);
  if (!path) return { path: '', pageType: 'other' };

  for (const rule of RULES) {
    if (rule.test(path)) return { path, pageType: rule.type };
  }
  return { path, pageType: 'other' };
}

/** Aggregate landing pages across all AI sources for site-level summary. */
export function buildAiLandingSummary(aiSourceResults, topN = 25) {
  const byPath = new Map();

  for (const src of aiSourceResults) {
    for (const lp of src.landingPages || []) {
      if (!byPath.has(lp.path)) {
        byPath.set(lp.path, {
          path: lp.path,
          pageType: lp.pageType,
          aiSessions: 0,
          topAiSources: new Map(),
        });
      }
      const entry = byPath.get(lp.path);
      entry.aiSessions += lp.sessions;
      entry.topAiSources.set(
        src.label,
        (entry.topAiSources.get(src.label) || 0) + lp.sessions
      );
    }
  }

  return [...byPath.values()]
    .sort((a, b) => b.aiSessions - a.aiSessions)
    .slice(0, topN)
    .map((x) => ({
      path: x.path,
      pageType: x.pageType,
      aiSessions: x.aiSessions,
      topAiSources: [...x.topAiSources.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([label, sessions]) => ({ label, sessions })),
    }));
}
