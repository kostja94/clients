#!/usr/bin/env node
/**
 * Audit ALL references for Alignify tools pages
 * Data: references-data.json
 * Rules: references.md §8-§11
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const DATA_PATH = process.argv[2] || 'E:\\自有部署项目\\alignify production\\src\\data\\references-data.json';
const data = JSON.parse(fs.readFileSync(DATA_PATH, 'utf8'));

// ── Forbidden patterns ──────────────────────────────────────────────
const GENERIC_GVR_PATTERNS = [
  { id: 'conv-ai', re: /conversational\s+ai\s+market/i, domains: ['giiresearch.com', 'grandviewresearch.com'] },
  { id: 'llm-market', re: /large\s+language\s+models?\s+market/i, domains: ['grandviewresearch.com', 'giiresearch.com'] },
  { id: 'genai-market', re: /generative\s+ai\s+market/i, domains: ['grandviewresearch.com', 'giiresearch.com'] },
];

const PAID_CATALOG_DOMAINS = [
  'researchandmarkets.com',
  'giiresearch.com',
  'grandviewresearch.com',
  'globenewswire.com', // often GVR press releases
  'prnewswire.com',
];

const FORBIDDEN_ROUNDUP_DOMAINS = ['codepick', 'hyscaler'];

// ── Source quality tiers ────────────────────────────────────────────
function getSourceTier(url, title) {
  const u = url.toLowerCase();
  const t = (title || '').toLowerCase();
  if (/arxiv\.org|acm\.org|ieee\.org|openreview\.net|papers\.nips|proceedings\.mlr|siggraph|nature\.com\/articles|science\.org|pnas\.org/.test(u)) return 'L1';
  if (/github\.com|gitlab\.com|docs\.|developer\.|\/docs\/|\/api\/|\.dev\/|readme|sdk/.test(u)) return 'L2';
  if (/techcrunch|theverge|arstechnica|wired\.com|mit\.edu|technologyreview|venturebeat|zdnet|theregister|engadget|tomshardware|analyticsinsight|searchenginejournal|moz\.com|hubspot|emarketer|forrester|gartner|idc\.com|cbinsights/.test(u)) return 'L3';
  if (PAID_CATALOG_DOMAINS.some(d => u.includes(d))) return 'L4-paid';
  if (/researchandmarkets|grandviewresearch|giiresearch|marketsandmarkets|fortunebusinessinsights|mordorintelligence|alliedmarketresearch|precedenceresearch|verifiedmarketresearch|skyquestt|technavio/.test(u)) return 'L4-paid';
  return 'L5';
}

function isPaidCatalog(url) {
  const u = url.toLowerCase();
  return PAID_CATALOG_DOMAINS.some(d => u.includes(d)) ||
    /\/industry-reports\/|\/report\/|market-report|market-size|market-forecast|market-analysis/.test(u);
}

function isForbiddenRoundup(url) {
  return FORBIDDEN_ROUNDUP_DOMAINS.some(d => url.toLowerCase().includes(d));
}

function matchesGenericGVR(title, url) {
  const u = url.toLowerCase();
  for (const p of GENERIC_GVR_PATTERNS) {
    if (p.re.test(title) && p.domains.some(d => u.includes(d))) {
      return p.id;
    }
  }
  return null;
}

// ── Slug/topic extraction ───────────────────────────────────────────
function getSlug(pageKey) {
  return pageKey.replace(/^\/(zh\/)?tools\//, '');
}

function getTopicKeywords(slug) {
  return slug.split('-').filter(w => w.length > 2);
}

// ── Topic relevance heuristic ───────────────────────────────────────
function checkTopicRelevance(slug, title, url, description) {
  const text = `${title} ${url} ${description || ''}`.toLowerCase();
  const keywords = getTopicKeywords(slug);
  const slugNorm = slug.replace(/-/g, ' ');

  // Special pages
  const llmPages = ['llm', 'llm-for-coding', 'llm-for-math', 'llm-for-reasoning', 'multimodal-llm'];
  if (llmPages.includes(slug)) {
    if (/llm|language model|gpt|claude|llama|mistral|chatbot arena|helm|humaneval|mmlu|benchmark/.test(text)) return { relevant: true, confidence: 'high' };
  }

  // Generic AI market reports on non-LLM pages
  const genericGVR = matchesGenericGVR(title, url);
  if (genericGVR && !llmPages.includes(slug)) {
    return { relevant: false, confidence: 'high', reason: `Generic GVR report (${genericGVR}) on non-LLM page` };
  }

  // Count keyword hits
  let hits = 0;
  for (const kw of keywords) {
    if (text.includes(kw)) hits++;
  }
  // Also check compound forms
  if (text.includes(slugNorm)) hits += keywords.length;

  // Synonym/expansion map for common slugs
  const expansions = {
    '3d': ['3d', 'three-dimensional', 'mesh', 'nerf', 'gaussian splat', 'blender', 'maya', 'zbrush', 'cad'],
    'voice': ['voice', 'speech', 'tts', 'text-to-speech', 'vocal', 'audio'],
    'image': ['image', 'visual', 'photo', 'picture', 'diffusion', 'stable diffusion', 'midjourney'],
    'video': ['video', 'film', 'motion', 'animation', 'frame'],
    'code': ['code', 'coding', 'programming', 'developer', 'software', 'ide', 'copilot'],
    'chatbot': ['chatbot', 'conversational', 'dialogue', 'assistant'],
    'seo': ['seo', 'search engine', 'ranking', 'serp', 'indexing'],
    'marketing': ['marketing', 'campaign', 'advertis', 'brand'],
    'affiliate': ['affiliate', 'referral', 'commission'],
    'recruiting': ['recruit', 'hiring', 'talent', 'hr ', 'human resource'],
    'legal': ['legal', 'law', 'contract', 'compliance'],
    'healthcare': ['health', 'medical', 'clinical', 'diagnos'],
    'education': ['education', 'learning', 'student', 'teaching', 'tutor'],
    'memory': ['memory', 'memgpt', 'vector', 'rag', 'retrieval'],
    'fashion': ['fashion', 'apparel', 'clothing', 'virtual try', 'viton'],
    'religion': ['religion', 'spiritual', 'faith', 'church', 'theology'],
    'tattoo': ['tattoo', 'body art', 'ink'],
    'browser': ['browser', 'web browser', 'headless', 'playwright', 'puppeteer'],
    'scraping': ['scrap', 'crawl', 'extract', 'web data'],
    'geo': ['geo', 'geospatial', 'location', 'mapping', 'gis'],
    'authentication': ['auth', 'identity', 'password', 'passkey', 'iam', 'sso'],
    'productivity': ['productiv', 'workflow', 'automation'],
    'presentation': ['presentation', 'slide', 'deck', 'pitch'],
    'poster': ['poster', 'print design', 'visual design'],
    'note': ['note', 'notetak', 'note-tak'],
    'scheduling': ['schedul', 'calendar', 'appointment', 'booking'],
    'community': ['community', 'forum', 'social'],
    'directory': ['directory', 'catalog', 'listing', 'curation'],
    'fundraising': ['fundraising', 'investor', 'venture', 'capital', 'vc '],
    'essay': ['essay', 'writing', 'academic writing'],
    'story': ['story', 'narrative', 'fiction', 'creative writing'],
    'user-research': ['user research', 'ux research', 'usability', 'user testing'],
    'evaluation': ['evaluat', 'benchmark', 'arena', 'helm', 'swe-bench'],
    'world-model': ['world model', 'genie', 'cosmos', 'simulation'],
    'animation': ['animation', 'motion', 'lottie', 'framer motion', 'gsap'],
    'openclaw': ['openclaw', 'open-claw', 'claw'],
    'influencer': ['influencer', 'creator', 'social media'],
    'linkedin': ['linkedin'],
    'lead-generation': ['lead gen', 'lead generation', 'prospect', 'pipeline'],
    'referral': ['referral', 'advocacy', 'word of mouth'],
    'interview': ['interview', 'assessment', 'candidate'],
    'b2b': ['b2b', 'business-to-business', 'enterprise'],
    'text': ['text', 'writing', 'nlp', 'language'],
    'search': ['search', 'index', 'retrieval', 'query'],
    'agent': ['agent', 'agentic', 'autonomous'],
    'workflow': ['workflow', 'automation', 'orchestrat'],
    'cli': ['cli', 'command line', 'terminal'],
    'ide': ['ide', 'editor', 'vscode', 'cursor'],
    'api': ['api', 'sdk', 'integration'],
    'music': ['music', 'audio', 'song', 'melody'],
    'avatar': ['avatar', 'virtual human', 'digital human'],
    'logo': ['logo', 'brand identity', 'branding'],
    'resume': ['resume', 'cv', 'curriculum'],
    'email': ['email', 'mail', 'inbox'],
    'podcast': ['podcast', 'episode'],
    'transcription': ['transcri', 'speech-to-text', 'stt', 'whisper'],
    'translation': ['translat', 'localiz', 'multilingual'],
    'summar': ['summar', 'abstract', 'digest'],
    'database': ['database', 'sql', 'data store'],
    'spreadsheet': ['spreadsheet', 'excel', 'sheet'],
    'diagram': ['diagram', 'chart', 'flowchart', 'visualization'],
    'mind-map': ['mind map', 'mindmap', 'concept map'],
    'whiteboard': ['whiteboard', 'collaboration board'],
    'survey': ['survey', 'poll', 'questionnaire'],
    'analytics': ['analytics', 'metric', 'dashboard', 'insight'],
    'crm': ['crm', 'customer relationship'],
    'ecommerce': ['ecommerce', 'e-commerce', 'shop', 'store'],
    'payment': ['payment', 'billing', 'invoice', 'stripe'],
    'security': ['security', 'cyber', 'threat', 'vulnerability'],
    'monitoring': ['monitor', 'observability', 'logging'],
    'deployment': ['deploy', 'devops', 'ci/cd', 'kubernetes'],
    'testing': ['test', 'qa', 'quality assurance'],
    'design': ['design', 'ui', 'ux', 'figma'],
    'prototype': ['prototype', 'mockup', 'wireframe'],
    'cad': ['cad', 'computer-aided design'],
    'render': ['render', 'rendering', 'ray tracing'],
    'texture': ['texture', 'material', 'pbr'],
    'rigging': ['rigging', 'skeleton', 'animation rig'],
    'motion-capture': ['motion capture', 'mocap'],
    'lip-sync': ['lip sync', 'lip-sync', 'dubbing'],
    'voice-cloning': ['voice clon', 'voice replica', 'deepfake voice'],
    'voice-changer': ['voice chang', 'voice modul', 'pitch shift'],
    'background-removal': ['background remov', 'matting', 'segmentation'],
    'upscale': ['upscale', 'super-resolution', 'enhance'],
    'inpainting': ['inpaint', 'fill', 'remove object'],
    'face-swap': ['face swap', 'deepfake', 'face replacement'],
    'character': ['character', 'persona', 'npc'],
    'game': ['game', 'gaming', 'unity', 'unreal'],
    'nft': ['nft', 'blockchain', 'web3'],
    'data-labeling': ['data label', 'annotation', 'tagging'],
    'training-data': ['training data', 'dataset', 'corpus'],
    'fine-tuning': ['fine-tun', 'finetun', 'lora', 'peft'],
    'prompt': ['prompt', 'prompting', 'in-context'],
    'rag': ['rag', 'retrieval augmented', 'retrieval-augmented'],
    'embedding': ['embedding', 'vector', 'semantic search'],
    'multimodal': ['multimodal', 'vision-language', 'vlm'],
    'reasoning': ['reasoning', 'chain of thought', 'cot'],
    'math': ['math', 'mathematical', 'gsm8k', 'minerva'],
    'coding': ['coding', 'code generation', 'humaneval', 'swe-bench'],
    'vibe-coding': ['vibe coding', 'ai coding', 'copilot'],
    'no-code': ['no-code', 'nocode', 'low-code', 'visual programming'],
    'automation': ['automation', 'automate', 'rpa', 'workflow'],
    'robot': ['robot', 'robotics', 'embodied'],
    'drone': ['drone', 'uav', 'aerial'],
    'satellite': ['satellite', 'remote sensing', 'earth observation'],
    'weather': ['weather', 'forecast', 'climate'],
    'fitness': ['fitness', 'workout', 'exercise', 'health'],
    'nutrition': ['nutrition', 'diet', 'meal', 'food'],
    'travel': ['travel', 'trip', 'itinerary', 'booking'],
    'real-estate': ['real estate', 'property', 'housing'],
    'finance': ['finance', 'financial', 'investment', 'trading'],
    'accounting': ['accounting', 'bookkeep', 'ledger'],
    'tax': ['tax', 'taxation'],
    'insurance': ['insurance', 'underwriting', 'claims'],
    'customer-support': ['customer support', 'helpdesk', 'ticketing', 'csat'],
    'live-chat': ['live chat', 'messaging', 'chat widget'],
    'social-media': ['social media', 'instagram', 'twitter', 'tiktok', 'facebook'],
    'content-calendar': ['content calendar', 'editorial calendar', 'scheduling content'],
    'newsletter': ['newsletter', 'email marketing', 'substack'],
    'landing-page': ['landing page', 'conversion', 'lead capture'],
    'ab-testing': ['a/b test', 'ab test', 'experiment', 'split test'],
    'personalization': ['personaliz', 'recommendation', 'recommend'],
    'sentiment': ['sentiment', 'opinion mining', 'emotion'],
    'fraud': ['fraud', 'anomaly', 'detection'],
    'compliance': ['compliance', 'regulatory', 'gdpr', 'hipaa'],
    'contract': ['contract', 'agreement', 'clause'],
    'patent': ['patent', 'intellectual property', 'ip '],
    'meeting': ['meeting', 'conference', 'video call', 'zoom'],
    'transcription-meeting': ['meeting transcript', 'meeting notes'],
    'knowledge-base': ['knowledge base', 'wiki', 'documentation'],
    'wiki': ['wiki', 'knowledge management'],
    'onboarding': ['onboarding', 'employee onboarding', 'training'],
    'learning-management': ['lms', 'learning management', 'e-learning'],
    'quiz': ['quiz', 'assessment', 'test maker'],
    'flashcard': ['flashcard', 'spaced repetition', 'anki'],
    'language-learning': ['language learning', 'duolingo', 'vocabulary'],
    'tutor': ['tutor', 'tutoring', 'personalized learning'],
    'homework': ['homework', 'assignment', 'study'],
    'research-paper': ['research paper', 'academic paper', 'citation'],
    'citation': ['citation', 'bibliography', 'reference manager'],
    'plagiarism': ['plagiarism', 'originality', 'duplicate content'],
    'grammar': ['grammar', 'spell check', 'proofread'],
    'paraphrase': ['paraphrase', 'rewrite', 'rephrase'],
    'headshot': ['headshot', 'portrait', 'professional photo'],
    'background-music': ['background music', 'royalty-free', 'stock music'],
    'sound-effect': ['sound effect', 'sfx', 'foley'],
    'noise-cancellation': ['noise cancel', 'denois', 'audio clean'],
    'podcast-editing': ['podcast edit', 'audio edit'],
    'video-editing': ['video edit', 'post-production', 'premiere'],
    'subtitle': ['subtitle', 'caption', 'closed caption'],
    'screen-recording': ['screen record', 'screencast', 'capture'],
    'thumbnail': ['thumbnail', 'preview image', 'cover art'],
    'gif': ['gif', 'animated image'],
    'meme': ['meme', 'viral content'],
    'infographic': ['infographic', 'data visualization', 'visual content'],
    'chart': ['chart', 'graph', 'plot'],
    'map': ['map', 'mapping', 'cartograph'],
    'floor-plan': ['floor plan', 'architectural', 'blueprint'],
    'interior-design': ['interior design', 'room design', 'home decor'],
    'landscape': ['landscape', 'garden', 'outdoor design'],
    'architecture': ['architect', 'building design', 'bim'],
    'fashion-design': ['fashion design', 'apparel design', 'clothing design'],
    'jewelry': ['jewelry', 'jewellery', 'accessory'],
    'packaging': ['packaging', 'label design', 'product design'],
    'mockup': ['mockup', 'product mockup', 'scene generator'],
    'font': ['font', 'typography', 'typeface'],
    'color-palette': ['color palette', 'color scheme', 'colour'],
    'icon': ['icon', 'icon set', 'glyph'],
    'pattern': ['pattern', 'seamless', 'tile'],
    'sticker': ['sticker', 'emoji', 'decal'],
    'wallpaper': ['wallpaper', 'background image'],
    'qr-code': ['qr code', 'barcode'],
    'business-card': ['business card', 'contact card'],
    'invoice-generator': ['invoice', 'billing document'],
    'receipt': ['receipt', 'expense'],
    'contract-generator': ['contract generat', 'legal document'],
    'terms-of-service': ['terms of service', 'privacy policy', 'legal document'],
    'privacy-policy': ['privacy policy', 'gdpr', 'data protection'],
  };

  // Check expansions for slug parts
  for (const kw of keywords) {
    if (expansions[kw]) {
      for (const term of expansions[kw]) {
        if (text.includes(term)) hits += 2;
      }
    }
  }

  const ratio = keywords.length > 0 ? hits / keywords.length : 0;

  if (ratio >= 1.5) return { relevant: true, confidence: 'high' };
  if (ratio >= 0.8) return { relevant: true, confidence: 'medium' };
  if (ratio >= 0.3) return { relevant: false, confidence: 'low', reason: 'Weak keyword overlap with page slug' };
  return { relevant: false, confidence: 'high', reason: 'Zero/minimal topic relevance to page slug' };
}

// ── Audit single reference ───────────────────────────────────────────
function auditReference(pageKey, item, idx) {
  const slug = getSlug(pageKey);
  const { title, url, description } = item;
  const reasons = [];
  let verdict = 'KEEP';

  // 1. Generic GVR reports
  const gvrMatch = matchesGenericGVR(title, url);
  const llmPages = ['llm', 'llm-for-coding', 'llm-for-math', 'llm-for-reasoning', 'multimodal-llm'];
  if (gvrMatch) {
    if (gvrMatch === 'llm-market' && llmPages.includes(slug)) {
      reasons.push('LLM market report on LLM page — acceptable');
    } else if (gvrMatch === 'genai-market' && ['text-generator', 'image-generator', 'productivity'].includes(slug)) {
      reasons.push('GenAI market on closely related page — REVIEW');
      verdict = 'REVIEW';
    } else {
      reasons.push(`FORBIDDEN: Generic GVR report (${gvrMatch})`);
      verdict = 'DELETE';
    }
  }

  // 2. Forbidden roundup domains
  if (FORBIDDEN_ROUNDUP_DOMAINS.some(d => url.toLowerCase().includes(d))) {
    reasons.push('FORBIDDEN: Third-party roundup (codepick/hyscaler)');
    verdict = 'DELETE';
  }

  // 3. Paid catalog pages
  if (isPaidCatalog(url)) {
    const relevance = checkTopicRelevance(slug, title, url, description);
    if (verdict !== 'DELETE') {
      if (!relevance.relevant) {
        reasons.push('Paid report catalog + topic mismatch');
        verdict = 'DELETE';
      } else {
        reasons.push('Paid report catalog page — topic matched but prefer free source');
        if (verdict === 'KEEP') verdict = 'REVIEW';
      }
    }
  }

  // 4. Topic relevance
  const relevance = checkTopicRelevance(slug, title, url, description);
  if (!relevance.relevant && verdict === 'KEEP') {
    reasons.push(relevance.reason || 'Not directly relevant to page topic');
    verdict = relevance.confidence === 'high' ? 'DELETE' : 'REVIEW';
  }

  // 5. Vendor blog as only source (flag in page-level, not here)

  if (reasons.length === 0) {
    const tier = getSourceTier(url, title);
    reasons.push(`OK (${tier})`);
  }

  return { idx, pageKey, slug, title, url, verdict, reason: reasons.join('; ') };
}

// ── Filter tools pages ───────────────────────────────────────────────
const toolsPages = Object.entries(data.pages || {})
  .filter(([key]) => /^\/(zh\/)?tools\//.test(key))
  .sort((a, b) => a[0].localeCompare(b[0]));

console.error(`Found ${toolsPages.length} tools pages`);

// ── Audit all references ─────────────────────────────────────────────
const allResults = [];
const urlToPages = new Map(); // url -> Set of slugs

for (const [pageKey, pageData] of toolsPages) {
  const slug = getSlug(pageKey);
  const items = pageData.items || [];
  for (let i = 0; i < items.length; i++) {
    const result = auditReference(pageKey, items[i], i + 1);
    allResults.push(result);
    const normUrl = items[i].url.replace(/[?#].*$/, '').toLowerCase();
    if (!urlToPages.has(normUrl)) urlToPages.set(normUrl, new Set());
    urlToPages.get(normUrl).add(slug);
  }
}

// ── Page-level flags ───────────────────────────────────────────────────
const pageResults = {};
for (const [pageKey, pageData] of toolsPages) {
  const slug = getSlug(pageKey);
  const items = pageData.items || [];
  const refs = allResults.filter(r => r.pageKey === pageKey);
  const deleteCount = refs.filter(r => r.verdict === 'DELETE').length;
  const reviewCount = refs.filter(r => r.verdict === 'REVIEW').length;
  const keepCount = refs.filter(r => r.verdict === 'KEEP').length;

  const allPaid = items.length > 0 && items.every(it => isPaidCatalog(it.url));
  const lowCount = items.length > 0 && items.length < 3;

  const tiers = items.map(it => getSourceTier(it.url, it.title));
  const uniqueTiers = new Set(tiers.filter(t => t !== 'L4-paid'));
  const tierCoverage = uniqueTiers.size;

  pageResults[pageKey] = {
    slug,
    locale: pageKey.startsWith('/zh/') ? 'zh' : 'en',
    count: items.length,
    deleteCount,
    reviewCount,
    keepCount,
    allPaid,
    lowCount,
    tierCoverage,
    refs,
  };
}

// ── Cross-page URL analysis ────────────────────────────────────────────
const crossPageUrls = [];
for (const [url, slugs] of urlToPages) {
  if (slugs.size >= 3) {
    // Check if slugs are related (same category prefix)
    const slugArr = [...slugs];
    const categories = slugArr.map(s => s.split('-')[0]);
    const uniqueCats = new Set(categories);
    const unrelated = uniqueCats.size >= 3 || slugs.size >= 5;
    crossPageUrls.push({ url, count: slugs.size, slugs: slugArr, unrelated });
  }
}

// ── P0: Generic GVR still present ────────────────────────────────────
const p0Pages = new Set();
for (const r of allResults) {
  const gvr = matchesGenericGVR(r.title, r.url);
  if (gvr) {
    const slug = getSlug(r.pageKey);
    const llmPages = ['llm', 'llm-for-coding', 'llm-for-math', 'llm-for-reasoning', 'multimodal-llm'];
    if (!(gvr === 'llm-market' && llmPages.includes(slug))) {
      p0Pages.add(r.pageKey);
    }
  }
}

// ── Group pages with identical reference sets ──────────────────────────
function refSetKey(pageKey) {
  const items = data.pages[pageKey]?.items || [];
  return items.map(it => it.url).sort().join('|');
}

const refSetGroups = new Map();
for (const [pageKey] of toolsPages) {
  const key = refSetKey(pageKey);
  if (!refSetGroups.has(key)) refSetGroups.set(key, []);
  refSetGroups.get(key).push(pageKey);
}

// ── Output ─────────────────────────────────────────────────────────────
const output = {
  summary: {
    totalPages: toolsPages.length,
    pagesWithReferences: toolsPages.filter(([k, v]) => (v.items || []).length > 0).length,
    pagesWithoutReferences: toolsPages.filter(([k, v]) => (v.items || []).length === 0).length,
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
    },
    p0GenericGVR: {
      pagesStillAffected: [...p0Pages],
      count: p0Pages.size,
    },
    crossPageUrls: crossPageUrls
      .filter(c => c.unrelated)
      .sort((a, b) => b.count - a.count)
      .slice(0, 50),
    identicalRefSets: [...refSetGroups.entries()]
      .filter(([, pages]) => pages.length > 1)
      .map(([key, pages]) => ({ pages, urlCount: key.split('|').filter(Boolean).length }))
      .sort((a, b) => b.pages.length - a.pages.length),
  },
  perPage: pageResults,
  allReferences: allResults,
};

// Write JSON report
const outPath = path.join(path.dirname(fileURLToPath(import.meta.url)), 'audit-tools-references-output.json');
fs.writeFileSync(outPath, JSON.stringify(output, null, 2));
console.error(`Written to ${outPath}`);

// Print summary to stdout
console.log(JSON.stringify(output.summary, null, 2));
