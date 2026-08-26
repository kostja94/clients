const fs = require('fs');
const path = require('path');

const base = 'E:/自有部署项目/alignify production';
const refs = JSON.parse(fs.readFileSync(`${base}/src/data/references-data.json`, 'utf8'));
const blogDir = `${base}/content/blog`;

const titles = {};
for (const lang of ['en', 'zh']) {
  const dir = path.join(blogDir, lang);
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.md'))) {
    const content = fs.readFileSync(path.join(dir, f), 'utf8');
    const fm = content.match(/^---\n([\s\S]*?)\n---/);
    const slug = f.replace('.md', '');
    const pageKey = lang === 'en' ? `/blog/${slug}` : `/zh/blog/${slug}`;
    let title = slug;
    if (fm) {
      const t = fm[1].match(/^title:\s*(.+)$/m);
      if (t) title = t[1].replace(/^["']|["']$/g, '').trim();
    }
    titles[pageKey] = title;
  }
}

// Audit rules - aggressive DELETE
function auditItem(item, pageKey) {
  const url = (item.url || '').toLowerCase();
  const title = item.title || '';
  const desc = (item.description || '').toLowerCase();
  const combined = `${title} ${desc} ${url}`.toLowerCase();

  // Forbidden URL patterns
  const forbiddenUrls = [
    'codepick.dev', 'hyscaler.com', 'stripe.com/resources', 'intercom.com/learning-center',
    'devcenter.heroku.com', 'lennysnewsletter', 'hubspot.com/blog', 'gartner.com',
    'nimdzi.com', 'hashmeta.com', 'trakkr.ai', 'crossmint.com/learn', 'gitlab.com/compare',
    'ibm.com/think/topics', 'klasresearch.com/report/best-in'
  ];
  for (const p of forbiddenUrls) {
    if (url.includes(p)) return { verdict: 'DELETE', type: 'D', reason: `Forbidden URL pattern: ${p}` };
  }

  if (url.includes('crossmint.com') && combined.includes('compared')) {
    return { verdict: 'DELETE', type: 'D', reason: 'Crossmint protocol comparison (forbidden)' };
  }

  // Static docs patterns
  const staticPatterns = [
    '/docs/', '/help/', '/overview', 'platform.openai.com/docs', 'developers.google.com/search/docs',
    'docs.github.com', 'docs.aws.amazon.com', 'docs.vllm.ai', 'docs.stripe.com',
    'docs.bigmodel.cn', 'platform.minimaxi.com/docs', 'help.aliyun.com', 'cursor.com/docs',
    'langchain-ai.github.io', 'openai.github.io/openai-agents', 'modelcontextprotocol.io',
    'firecrawl.dev/glossary', 'jina.ai/reader', 'github.com/open-spaced-repetition/fsrs',
    'aws.amazon.com/what-is', 'artificialintelligenceact.eu', 'www.uspto.gov/trademarks/basics',
    'www.coe.int', 'www.lexiconbranding.com/service', 'ahrefs.com/ai-visibility-checker',
    'thetawave.ai/feature', 'www.autodesk.com/products/fusion/overview', 'www.x402.org',
    'github.com/google-agentic-commerce/ap2'
  ];
  for (const p of staticPatterns) {
    if (url.includes(p)) return { verdict: 'DELETE', type: 'C', reason: `Static docs/overview/help: ${p}` };
  }

  // arxiv - methodology unless event-specific media
  if (url.includes('arxiv.org')) {
    return { verdict: 'DELETE', type: 'D', reason: 'arXiv paper used as methodology/benchmark, not event source' };
  }

  // Nature reviews
  if (url.includes('nature.com/articles')) {
    return { verdict: 'DELETE', type: 'D', reason: 'Nature review article (Type D academic review)' };
  }

  // Academic/journal methodology
  if (url.includes('journals.sagepub.com') || url.includes('bjorklab.psych.ucla.edu') ||
      url.includes('routledge.com') || url.includes('hup.harvard.edu')) {
    return { verdict: 'DELETE', type: 'D', reason: 'Academic theory/framework citation (Type D)' };
  }

  // Type A - keep candidates (official event/policy)
  const typeA = [
    { match: () => url.includes('cloud.baidu.com/doc/qianfan/s/emqsyd7yj'), reason: 'Baidu Coding Plan discontinuation/migration announcement (2026-06-25)' },
    { match: () => url.includes('dlthub.com/blog/introducing-dlthub-pro'), reason: 'dltHub Pro product launch announcement' },
    { match: () => url.includes('github.blog') && url.includes('welcome-home-agents'), reason: 'GitHub Agent HQ official announcement (2025)' },
    { match: () => url.includes('about.gitlab.com/blog/gitlab-transcend'), reason: 'GitLab Transcend product announcements (2026)' },
    { match: () => url.includes('zed.dev/blog/introducing-delta'), reason: 'Zed Delta product launch announcement' },
    { match: () => url.includes('blog.cloudflare.com/markdown-for-agents'), reason: 'Cloudflare Markdown-for-agents feature announcement (2026)' },
    { match: () => url.includes('developers.openai.com/codex/pricing'), reason: 'OpenAI Codex official pricing/reset policy page' },
    { match: () => url.includes('help.openai.com') && combined.includes('reset'), reason: 'OpenAI Help Center Codex usage limits reset policy' },
    { match: () => url.includes('developers.googleblog.com') && combined.includes('a2a'), reason: 'Google A2A protocol launch announcement (2025)' },
    { match: () => url.includes('garanteprivacy.it') || (combined.includes('gdpr') && combined.includes('fine')), reason: 'Italian GDPR enforcement action against Replika (May 2025)' },
  ];
  for (const a of typeA) {
    if (a.match()) return { verdict: 'KEEP', type: 'A', reason: a.reason };
  }

  // Type B - tier-1 media on specific events
  const typeB = [
    { match: () => url.includes('techcrunch.com/2026/03/10/meta-acquired-moltbook'), reason: 'TechCrunch: Meta acquires Moltbook (2026-03-10)' },
    { match: () => url.includes('techcrunch.com/2025/07/28/anthropic'), reason: 'TechCrunch: Anthropic weekly rate limits announcement (2025-07-28)' },
    { match: () => url.includes('businessinsider.com/openai-codex-usage-limit'), reason: 'Business Insider: Codex quota incident & warroom fix (2026-06)' },
    { match: () => url.includes('medcitynews.com/2026/02/ambient-scribe'), reason: 'MedCity News: ambient scribe startups vs Epic (2026-02)' },
  ];
  for (const b of typeB) {
    if (b.match()) return { verdict: 'KEEP', type: 'B', reason: b.reason };
  }

  // Default aggressive patterns - D
  const dPatterns = [
    'compared', 'comparison', 'guide', 'roundup', 'best ', 'landscape', 'vs ', 'review',
    'benchmark', 'methodology', 'overview', 'explainer', 'how-to', 'how to', 'playbook',
    'a16z.com', 'forrester.com', 'seoturtle.com', 'rye.com/blog', 'rywalker.com',
    'work-bench.com', 'atlan.com', 'peliqan.io', 'futurumgroup.com', 'sdxcentral.com',
    'technologyadvice.com', 'ibrahimfurkanozcelik.com', 'detailed.com', '5wpr.com',
    'goodie.digital', 'conductor.com/academy', 'fungies.io', 'vibecoder.me', 'creem.io/blog',
    'xploitscan.com', 'vibedoctor.io', 'cybersecify.com', 'youngju.dev', 'vibeusers.io',
    'tinyfish.ai/blog', 'cursor.com/blog/git-at-any-scale', 'nar.realtor', 'ahundredmonkeys.com',
    'developers.redhat.com/articles', 'klasresearch.com'
  ];
  for (const p of dPatterns) {
    if (combined.includes(p) || url.includes(p)) {
      return { verdict: 'DELETE', type: 'D', reason: `Third-party strategy/guide/roundup/benchmark: matches "${p}"` };
    }
  }

  // GKE/AWS sandbox docs missed
  if (url.includes('cloud.google.com') && url.includes('docs')) {
    return { verdict: 'DELETE', type: 'C', reason: 'Static Google Cloud documentation' };
  }

  return { verdict: 'DELETE', type: 'D', reason: 'No specific dated event/policy narrative; default aggressive DELETE' };
}

const blogPages = Object.entries(refs.pages).filter(([k]) => k.includes('/blog/'));
let globalIdx = 0;
const rows = [];
const pageSummaries = {};

for (const [pageKey, page] of blogPages.sort((a, b) => a[0].localeCompare(b[0]))) {
  const items = page.items || [];
  const pageRows = [];
  let deleteCount = 0, keepCount = 0, reviewCount = 0;

  items.forEach((item, i) => {
    globalIdx++;
    const audit = auditItem(item, pageKey);
    if (audit.verdict === 'DELETE') deleteCount++;
    else if (audit.verdict === 'KEEP') keepCount++;
    else reviewCount++;

    pageRows.push({
      num: globalIdx,
      pageKey,
      title: item.title,
      url: item.url,
      verdict: audit.verdict,
      type: audit.type,
      reason: audit.reason,
      articleTitle: titles[pageKey] || pageKey
    });
  });

  pageSummaries[pageKey] = {
    total: items.length,
    delete: deleteCount,
    keep: keepCount,
    review: reviewCount,
    afterCleanup: keepCount + reviewCount,
    over6: items.length > 6
  };
  rows.push(...pageRows);
}

const totals = rows.reduce((a, r) => {
  a.total++;
  a[r.verdict.toLowerCase()]++;
  return a;
}, { total: 0, delete: 0, keep: 0, review: 0 });

const zeroAfter = Object.entries(pageSummaries)
  .filter(([, s]) => s.afterCleanup === 0)
  .map(([k]) => k);

// Manual REVIEW overrides (aggressive audit edge cases)
const reviewOverrides = {
  'https://www.garanteprivacy.it/': {
    verdict: 'REVIEW',
    type: 'A',
    reason: 'Description cites Replika GDPR fine (May 2025) but URL is org homepage, not dated enforcement decision; replace with primary decision URL or move inline',
  },
};

rows.forEach((row) => {
  const o = reviewOverrides[row.url];
  if (o && row.pageKey.includes('ai-language-learning')) Object.assign(row, o);
});

const totals2 = rows.reduce(
  (a, r) => {
    a.total++;
    a[r.verdict.toLowerCase()]++;
    return a;
  },
  { total: 0, delete: 0, keep: 0, review: 0 },
);

Object.values(pageSummaries).forEach((s) => {
  s.keep = 0;
  s.review = 0;
  s.delete = 0;
});
rows.forEach((row) => {
  pageSummaries[row.pageKey][row.verdict.toLowerCase()]++;
  pageSummaries[row.pageKey].afterCleanup =
    pageSummaries[row.pageKey].keep + pageSummaries[row.pageKey].review;
});

const zeroAfter2 = Object.entries(pageSummaries)
  .filter(([, s]) => s.afterCleanup === 0)
  .map(([k]) => k);

fs.writeFileSync(
  'E:/clients/audit-results.json',
  JSON.stringify({ totals: totals2, pageSummaries, rows, zeroAfter: zeroAfter2 }, null, 2),
  'utf8',
);

let md = `# Alignify Blog References Audit\n\n`;
md += `## Summary\n\n| Metric | Count |\n|--------|-------|\n| Total items | ${totals2.total} |\n| DELETE | ${totals2.delete} |\n| KEEP | ${totals2.keep} |\n| REVIEW | ${totals2.review} |\n\n`;
md += `### Pages with >6 references (flagged)\n\n`;
Object.entries(pageSummaries)
  .filter(([, s]) => s.over6)
  .forEach(([k, s]) => {
    md += `- \`${k}\`: ${s.total} items\n`;
  });

md += `\n## Per-item audit (grouped by pageKey)\n\n`;
let cur = '';
for (const row of rows) {
  if (row.pageKey !== cur) {
    cur = row.pageKey;
    const s = pageSummaries[row.pageKey];
    md += `\n### ${row.pageKey}\n\n**Article:** ${row.articleTitle}  \n**Current:** ${s.total} items | **After cleanup:** ${s.afterCleanup}${s.over6 ? ' | ⚠️ **>6 items**' : ''}\n\n`;
    md += `| # | pageKey | title | url | verdict | type | reason |\n|---|---------|-------|-----|---------|------|--------|\n`;
  }
  const esc = (x) => String(x).replace(/\|/g, '\\|').replace(/\n/g, ' ');
  md += `| ${row.num} | ${row.pageKey} | ${esc(row.title)} | ${row.url} | **${row.verdict}** | ${row.type} | ${esc(row.reason)} |\n`;
}

md += `\n## Pages with 0 items after cleanup\n\n`;
zeroAfter2.forEach((k) => {
  md += `- \`${k}\`\n`;
});

fs.writeFileSync('E:/clients/audit-table.md', md, 'utf8');
console.log(JSON.stringify({ totals: totals2, zeroAfterCount: zeroAfter2.length }, null, 2));
