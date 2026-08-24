/**
 * Landing page path classification for dubbingai.io
 */

const RULES = [
  { type: 'download', test: (p) => p === '/download' || p === '/download-desktop' || p.startsWith('/download/') },
  { type: 'pricing', test: (p) => p === '/pricing' || p.startsWith('/pricing/') },
  { type: 'product-hub', test: (p) =>
    p === '/soundboard' || p === '/online-voice-changer' ||
    p === '/voice-changer' || p.startsWith('/soundboard/') },
  { type: 'platform-spoke', test: (p) =>
    ['/discord-voice-changer', '/zoom-voice-changer', '/vrchat-voice-changer',
      '/fortnite-voice-changer', '/valorant-voice-changer', '/roblox-voice-changer']
      .some((x) => p === x || p.startsWith(`${x}/`)) },
  { type: 'blog', test: (p) => p === '/blog' || p.startsWith('/blog/') },
  { type: 'articles', test: (p) => p === '/articles' || p.startsWith('/articles/') },
  { type: 'compare', test: (p) => p.startsWith('/compare/') },
  { type: 'hardware', test: (p) =>
    p === '/dubbing-box' || p === '/earbuds' || p.startsWith('/dubbing-box/') || p.startsWith('/earbuds/') },
  { type: 'affiliate', test: (p) => p === '/affiliate' || p.startsWith('/affiliate/') },
  { type: 'voice-changer-spoke', test: (p) =>
    p.includes('-voice-changer') || p.startsWith('/voice-changer/') },
  { type: 'soundboard-spoke', test: (p) =>
    p.includes('sound-gallery') || p.includes('soundGallery') || /-soundboard/.test(p) },
  { type: 'homepage', test: (p) => p === '/' || p === '/explore' || p.startsWith('/explore/') },
];

/** Normalize GA4 landing page path (strip query, ensure leading slash). */
export function normalizePath(raw) {
  if (!raw || raw === '(not set)') return '';
  let p = raw.split('?')[0].trim();
  if (!p.startsWith('/')) p = `/${p}`;
  return p.replace(/\/+$/, '') || '/';
}

export function classifyLandingPage(rawPath) {
  const p = normalizePath(rawPath);
  if (!p) return 'other';

  for (const rule of RULES) {
    if (rule.test(p)) return rule.type;
  }
  return 'other';
}

/** Compare landing path to registry targetUrl. */
export function isExpectedTarget(landingPath, targetUrl) {
  if (!targetUrl) return false;
  try {
    const target = new URL(targetUrl);
    const normalizedLanding = normalizePath(landingPath);
    const targetPath = normalizePath(target.pathname);
    return normalizedLanding === targetPath;
  } catch {
    return normalizePath(landingPath) === normalizePath(targetUrl);
  }
}

export function targetPathFromUrl(targetUrl) {
  if (!targetUrl) return '';
  try {
    return normalizePath(new URL(targetUrl).pathname);
  } catch {
    return normalizePath(targetUrl);
  }
}
