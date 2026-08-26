/**
 * Datus landing page classification (datus.ai)
 */

const RULES = [
  { type: 'homepage', test: (p) => p === '/' },
  { type: 'blog', test: (p) => p === '/blog' || p.startsWith('/blog/') },
  { type: 'glossary-index', test: (p) => p === '/glossary' || p.startsWith('/glossary/') },
  { type: 'product', test: (p) => p.startsWith('/products/') },
  { type: 'pricing', test: (p) => p === '/pricing' || p.startsWith('/pricing/') },
  { type: 'integrations', test: (p) => p === '/integrations' || p.startsWith('/integrations/') },
  { type: 'faq', test: (p) => p === '/faq' || p.startsWith('/faq/') },
  { type: 'osi-tool', test: (p) => p === '/osi-field-mapping' || p.startsWith('/osi-field-mapping/') },
  { type: 'osi-tool', test: (p) => p === '/tools/osi-playground' || p.startsWith('/tools/osi-playground/') },
  { type: 'tools', test: (p) => p.startsWith('/tools/') },
  { type: 'auth', test: (p) =>
    ['/login', '/register', '/sign-up', '/signup'].some((x) => p === x || p.startsWith(`${x}/`)) },
  { type: 'zh', test: (p) => p === '/zh' || p.startsWith('/zh/') },
];

export function normalizePath(raw) {
  if (!raw || raw === '(not set)') return '';
  let p = raw.split('?')[0].trim();
  if (!p.startsWith('/')) p = `/${p}`;
  p = p.replace(/\/+$/, '') || '/';
  return p;
}

export function stripDomain(url) {
  if (!url) return '';
  try {
    if (url.startsWith('http')) {
      const u = new URL(url);
      return normalizePath(u.pathname);
    }
  } catch {
    /* fall through */
  }
  return normalizePath(url);
}

export function classifyLandingPage(rawPath) {
  const path = normalizePath(rawPath);
  if (!path) return { path: '', pageType: 'other' };

  for (const rule of RULES) {
    if (rule.test(path)) return { path, pageType: rule.type };
  }
  return { path, pageType: 'other' };
}

export function isBlogPath(path) {
  const p = normalizePath(path);
  return p.startsWith('/blog/') && p !== '/blog';
}

export function blogPathFromSlug(slug) {
  const s = (slug || '').replace(/^\/+|\/+$/g, '');
  return s ? `/blog/${s}` : '/blog';
}
