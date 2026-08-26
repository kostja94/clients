#!/usr/bin/env node
/**
 * Audit ALL references for Alignify tools pages (v2)
 * Uses tools-pages-config metadata + references.md §8-§11 rules
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const DATA_PATH = process.argv[2] || 'E:\\自有部署项目\\alignify production\\src\\data\\references-data.json';
const CONFIG_PATH = process.argv[3] || 'E:\\自有部署项目\\alignify production\\src\\data\\tools-pages-config.ts';

const data = JSON.parse(fs.readFileSync(DATA_PATH, 'utf8'));
const configTxt = fs.readFileSync(CONFIG_PATH, 'utf8');

// Parse TOOLS_PAGES from config
const SLUG_META = {};
const pageRe = /\{\s*slug:\s*"([^"]+)",\s*keywordZh:\s*"([^"]+)",\s*keywordEn:\s*"([^"]+)",\s*hubGroup:\s*"([^"]+)"\s*\}/g;
let m;
while ((m = pageRe.exec(configTxt)) !== null) {
  SLUG_META[m[1]] = { keywordZh: m[2], keywordEn: m[3], hubGroup: m[4] };
}

const HUB_PARENT_TERMS = {
  '3d': ['3d', 'three-dimensional', 'mesh', 'nerf', 'gaussian splat', 'sculpt', 'modelling', 'modeling', 'scan', 'photogrammetry', 'lidar', 'cad', 'blender', 'maya', 'zbrush', 'render', 'voxel', 'point cloud', 'radiance field'],
  image: ['image', 'photo', 'visual', 'picture', 'diffusion', 'portrait', 'headshot', 'background', 'enhance', 'edit', 'generate', 'avatar', 'logo', 'poster', 'design', 'pixel', 'segmentation', 'inpaint', 'upscale'],
  video: ['video', 'film', 'motion', 'animation', 'frame', 'clip', 'edit', 'effect', 'lip sync', 'lip-sync', 'subtitle', 'caption', 'generator', 'translate', 'drama', 'filmmaking', 'canvas'],
  audio: ['audio', 'voice', 'speech', 'music', 'sound', 'tts', 'text-to-speech', 'stt', 'transcri', 'clone', 'changer', 'accent', 'translate', 'song', 'melody'],
  design: ['design', 'logo', 'poster', 'presentation', 'brand', 'typography', 'website', 'mockup', 'tattoo', 'visual', 'layout'],
  dev: ['code', 'coding', 'developer', 'programming', 'ide', 'cli', 'agent', 'api', 'github', 'software', 'review', 'completion', 'vibe', 'workflow', 'memory', 'sandbox', 'openclaw', 'documentation', 'authentication', 'iam'],
  search: ['search', 'index', 'crawl', 'scrap', 'browser', 'headless', 'ocr', 'web data', 'query', 'retrieval', 'playwright', 'puppeteer'],
  llm: ['llm', 'language model', 'gpt', 'claude', 'llama', 'mistral', 'benchmark', 'evaluat', 'multimodal', 'reasoning', 'math', 'world model', 'genie', 'cosmos'],
  productivity: ['productiv', 'workflow', 'note', 'meeting', 'schedul', 'calendar', 'text', 'writing', 'story', 'spreadsheet', 'knowledge', 'chat', 'character'],
  marketing: ['marketing', 'affiliate', 'influencer', 'lead gen', 'b2b', 'linkedin', 'referral', 'geo', 'social', 'growth', 'fundraising', 'community', 'directory'],
  vertical: ['education', 'healthcare', 'legal', 'recruit', 'interview', 'hr ', 'fashion', 'religion', 'dating', 'family', 'homework', 'essay', 'user research', 'professional'],
};

const HUB_GROUP_TO_PARENT = {
  '3d': '3d', 'image-overview': 'image', 'image-generation': 'image', 'image-editing': 'image', 'image-portrait': 'image',
  'video-overview': 'video', 'video-generation': 'video', 'video-editing': 'video', 'video-vertical': 'video',
  'audio-overview': 'audio', 'audio-speech': 'audio', 'audio-voice': 'audio',
  'design-overview': 'design', 'design-assets': 'design',
  'dev-coding': 'dev', 'dev-agents': 'dev', 'dev-platform': 'dev', 'dev-data-ml': 'dev', 'dev-multi-agent': 'dev',
  'search-discovery': 'search', 'search-data': 'search',
  'llm-general': 'llm', 'llm-specialized': 'llm',
  'productivity-overview': 'productivity', 'productivity-workflow': 'productivity', 'productivity-text': 'productivity',
  'productivity-chat': 'productivity', 'productivity-notes': 'productivity',
  'marketing-growth': 'marketing', 'marketing-channels': 'marketing',
  'vertical-education': 'vertical', 'vertical-professional': 'vertical', 'vertical-consumer': 'vertical',
};

const GENERIC_GVR = [
  { re: /conversational\s+ai\s+market/i, id: 'conv-ai' },
  { re: /large\s+language\s+models?\s+market/i, id: 'llm-market' },
  { re: /generative\s+ai\s+market/i, id: 'genai-market' },
];
const PAID_DOMAINS = ['researchandmarkets.com', 'giiresearch.com', 'grandviewresearch.com'];
const FORBIDDEN_ROUNDS = ['codepick.dev', 'hyscaler.com'];

function getSlug(pageKey) { return pageKey.replace(/^\/(zh\/)?tools\//, ''); }

function getTopicTerms(slug) {
  const meta = SLUG_META[slug] || {};
  const terms = new Set();
  slug.split('-').forEach(w => { if (w.length > 1) terms.add(w); });
  (meta.keywordEn || '').toLowerCase().split(/[\s/&]+/).forEach(w => { if (w.length > 2) terms.add(w); });
  (meta.keywordZh || '').split(/[工具与&]+/).forEach(w => { if (w.length > 1) terms.add(w); });
  const parent = HUB_GROUP_TO_PARENT[meta.hubGroup];
  if (parent && HUB_PARENT_TERMS[parent]) {
    HUB_PARENT_TERMS[parent].forEach(t => terms.add(t));
  }
  return [...terms];
}

function getSourceTier(url) {
  const u = url.toLowerCase();
  if (/arxiv\.org|acm\.org|ieee\.org|openreview|siggraph|nature\.com\/articles|pnas\.org|repo-sam\.inria/.test(u)) return 'L1';
  if (/github\.com|gitlab\.com|docs\.|developer\.|\/docs\//.test(u)) return 'L2';
  if (/techcrunch|theverge|arstechnica|wired|mit\.edu|technologyreview|venturebeat|searchenginejournal|forrester|gartner|emarketer|idc\.com|cbinsights/.test(u)) return 'L3';
  if (PAID_DOMAINS.some(d => u.includes(d))) return 'L4-paid';
  return 'L5';
}

function isPaidCatalog(url) {
  return PAID_DOMAINS.some(d => url.toLowerCase().includes(d));
}

function matchesGenericGVR(title, url) {
  if (!PAID_DOMAINS.some(d => url.toLowerCase().includes(d)) && !/grandviewresearch|giiresearch/i.test(url)) return null;
  for (const p of GENERIC_GVR) {
    if (p.re.test(title)) return p.id;
  }
  return null;
}

function checkRelevance(slug, title, url, description) {
  const text = `${title} ${url} ${description || ''}`.toLowerCase();
  const terms = getTopicTerms(slug);
  const meta = SLUG_META[slug] || {};
  const parent = HUB_GROUP_TO_PARENT[meta.hubGroup];

  // Direct slug/keyword match
  let hits = 0;
  for (const t of terms) {
    if (t.length > 2 && text.includes(t.toLowerCase())) hits++;
  }
  const slugNorm = slug.replace(/-/g, ' ');
  if (text.includes(slugNorm)) hits += 3;

  // Description explicitly about page topic (descriptions are curated)
  if (description && description.length > 30) {
    const descLower = description.toLowerCase();
    for (const t of terms.slice(0, 15)) {
      if (t.length > 3 && descLower.includes(t.toLowerCase())) hits += 2;
    }
  }

  // L1/L2 on matching hub parent = likely relevant
  const tier = getSourceTier(url);
  if ((tier === 'L1' || tier === 'L2') && parent) {
    const parentTerms = HUB_PARENT_TERMS[parent] || [];
    if (parentTerms.some(t => text.includes(t))) hits += 3;
  }

  if (hits >= 3) return { relevant: true, confidence: 'high', hits };
  if (hits >= 1) return { relevant: true, confidence: 'medium', hits };
  return { relevant: false, confidence: hits === 0 ? 'high' : 'medium', hits, reason: 'Insufficient topic overlap with page slug/keywords/hub' };
}

function auditRef(pageKey, item, idx) {
  const slug = getSlug(pageKey);
  const { title, url, description } = item;
  const reasons = [];
  let verdict = 'KEEP';
  const llmSlugs = ['llm', 'llm-for-coding', 'llm-for-math', 'llm-for-reasoning', 'multimodal-llm'];

  // FORBIDDEN: Generic GVR trio
  const gvr = matchesGenericGVR(title, url);
  if (gvr) {
    if (gvr === 'llm-market' && llmSlugs.includes(slug)) {
      reasons.push('LLM market report on LLM page');
    } else {
      reasons.push(`FORBIDDEN: Generic GVR (${gvr})`);
      verdict = 'DELETE';
    }
  }

  // FORBIDDEN: Third-party roundups
  if (FORBIDDEN_ROUNDS.some(d => url.toLowerCase().includes(d))) {
    reasons.push('FORBIDDEN: Third-party roundup (codepick/hyscaler)');
    verdict = 'DELETE';
  }

  // Paid catalog
  if (isPaidCatalog(url) && verdict !== 'DELETE') {
    const rel = checkRelevance(slug, title, url, description);
    if (!rel.relevant) {
      reasons.push('Paid report catalog + topic mismatch');
      verdict = 'DELETE';
    } else {
      reasons.push('Paid catalog — topic matched, prefer free alternative');
      verdict = 'REVIEW';
    }
  }

  // Topic relevance
  if (verdict === 'KEEP') {
    const rel = checkRelevance(slug, title, url, description);
    if (!rel.relevant) {
      reasons.push(rel.reason || 'Not directly relevant to page topic');
      verdict = rel.confidence === 'high' ? 'DELETE' : 'REVIEW';
    } else if (rel.confidence === 'medium') {
      reasons.push('Weak topic match — verify manually');
      verdict = 'REVIEW';
    } else {
      reasons.push(`OK (${getSourceTier(url)})`);
    }
  }

  return { idx, pageKey, slug, title, url, verdict, reason: reasons.join('; ') };
}

// ── Run audit ──
const toolsPages = Object.entries(data.pages || {})
  .filter(([k]) => /^\/(zh\/)?tools\//.test(k))
  .sort((a, b) => a[0].localeCompare(b[0]));

const allResults = [];
const urlToSlugs = new Map();

for (const [pageKey, pageData] of toolsPages) {
  const slug = getSlug(pageKey);
  for (let i = 0; i < (pageData.items || []).length; i++) {
    const r = auditRef(pageKey, pageData.items[i], i + 1);
    allResults.push(r);
    const normUrl = pageData.items[i].url.replace(/[?#].*$/, '').toLowerCase();
    if (!urlToSlugs.has(normUrl)) urlToSlugs.set(normUrl, new Set());
    urlToSlugs.get(normUrl).add(slug);
  }
}

const pageResults = {};
for (const [pageKey, pageData] of toolsPages) {
  const refs = allResults.filter(r => r.pageKey === pageKey);
  const items = pageData.items || [];
  pageResults[pageKey] = {
    slug: getSlug(pageKey),
    locale: pageKey.startsWith('/zh/') ? 'zh' : 'en',
    count: items.length,
    deleteCount: refs.filter(r => r.verdict === 'DELETE').length,
    reviewCount: refs.filter(r => r.verdict === 'REVIEW').length,
    keepCount: refs.filter(r => r.verdict === 'KEEP').length,
    allPaid: items.length > 0 && items.every(it => isPaidCatalog(it.url)),
    lowCount: items.length > 0 && items.length < 3,
    refs,
  };
}

// Cross-page URLs on 3+ unrelated slugs
const crossPage = [];
for (const [url, slugs] of urlToSlugs) {
  if (slugs.size >= 3) {
    const slugArr = [...slugs];
    const parents = slugArr.map(s => HUB_GROUP_TO_PARENT[(SLUG_META[s] || {}).hubGroup] || 'unknown');
    const uniqueParents = new Set(parents);
    crossPage.push({ url, count: slugs.size, slugs: slugArr, hubParents: [...uniqueParents], unrelated: uniqueParents.size >= 2 });
  }
}

// P0 GVR
const p0Pages = new Set();
for (const r of allResults) {
  const gvr = matchesGenericGVR(r.title, r.url);
  if (gvr) {
    const llmSlugs = ['llm', 'llm-for-coding', 'llm-for-math', 'llm-for-reasoning', 'multimodal-llm'];
    if (!(gvr === 'llm-market' && llmSlugs.includes(r.slug))) p0Pages.add(r.pageKey);
  }
}

// Identical ref sets (EN only, exclude empty)
function refKey(pageKey) {
  return (data.pages[pageKey]?.items || []).map(i => i.url).sort().join('|');
}
const refGroups = new Map();
for (const [pageKey] of toolsPages) {
  if (!pageKey.startsWith('/tools/') || pageKey.startsWith('/zh/')) continue;
  const k = refKey(pageKey);
  if (!refGroups.has(k)) refGroups.set(k, []);
  refGroups.get(k).push(pageKey);
}

const output = {
  summary: {
    totalPages: toolsPages.length,
    uniqueSlugs: new Set(toolsPages.map(([k]) => getSlug(k))).size,
    pagesWithReferences: toolsPages.filter(([, v]) => (v.items || []).length > 0).length,
    pagesWithoutReferences: toolsPages.filter(([, v]) => (v.items || []).length === 0).length,
    totalReferences: allResults.length,
    verdicts: {
      DELETE: allResults.filter(r => r.verdict === 'DELETE').length,
      REVIEW: allResults.filter(r => r.verdict === 'REVIEW').length,
      KEEP: allResults.filter(r => r.verdict === 'KEEP').length,
    },
    pageFlags: {
      allPaidOnly: Object.values(pageResults).filter(p => p.allPaid).length,
      lowReferenceCount: Object.values(pageResults).filter(p => p.lowCount).length,
      hasDeleteItems: Object.values(pageResults).filter(p => p.deleteCount > 0).length,
      hasReviewItems: Object.values(pageResults).filter(p => p.reviewCount > 0).length,
      fullyDelete: Object.values(pageResults).filter(p => p.count > 0 && p.deleteCount === p.count).length,
    },
    p0GenericGVR: { pagesStillAffected: [...p0Pages], count: p0Pages.size },
    crossPageUrls: crossPage.filter(c => c.unrelated).sort((a, b) => b.count - a.count),
    identicalRefSets: [...refGroups.entries()]
      .filter(([, pages]) => pages.length > 1 && refKey(pages[0]).length > 0)
      .map(([, pages]) => ({ pages, refCount: (data.pages[pages[0]]?.items || []).length }))
      .sort((a, b) => b.pages.length - a.pages.length),
    emptyRefPages: toolsPages.filter(([, v]) => (v.items || []).length === 0).map(([k]) => k),
  },
  perPage: pageResults,
  allReferences: allResults,
};

const outDir = path.dirname(fileURLToPath(import.meta.url));
fs.writeFileSync(path.join(outDir, 'audit-tools-references-output.json'), JSON.stringify(output, null, 2));
console.log(JSON.stringify(output.summary, null, 2));
