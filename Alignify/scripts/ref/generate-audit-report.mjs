#!/usr/bin/env node
/** Generate markdown audit report from audit-tools-references-output.json */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const inPath = path.join(path.dirname(fileURLToPath(import.meta.url)), 'audit-tools-references-output.json');
const data = JSON.parse(fs.readFileSync(inPath, 'utf8'));

const { summary, perPage, allReferences } = data;

// Group EN pages only for main table (ZH mirrors EN)
const enPages = Object.entries(perPage)
  .filter(([k]) => k.startsWith('/tools/') && !k.startsWith('/zh/'))
  .sort((a, b) => a[0].localeCompare(b[0]));

const zhOnlyPages = Object.entries(perPage)
  .filter(([k]) => k.startsWith('/zh/tools/'))
  .filter(([k]) => !perPage[k.replace('/zh', '')]);

let md = `# Alignify Tools References Audit Report\n\n`;
md += `> Generated: 2026-08-27 | Data: references-data.json | Rules: references.md §8–§11\n\n`;

// Summary
md += `## Summary Statistics\n\n`;
md += `| Metric | Value |\n|--------|-------|\n`;
md += `| Total tools pages (EN+ZH) | ${summary.totalPages} |\n`;
md += `| EN pages | ${enPages.length} |\n`;
md += `| ZH-only pages (no EN mirror) | ${zhOnlyPages.length} |\n`;
md += `| Pages with references | ${summary.pagesWithReferences} |\n`;
md += `| Pages without references | ${summary.pagesWithoutReferences} |\n`;
md += `| Total reference items | ${summary.totalReferences} |\n`;
md += `| **DELETE** | ${summary.verdicts.DELETE} (${(summary.verdicts.DELETE/summary.totalReferences*100).toFixed(1)}%) |\n`;
md += `| **REVIEW** | ${summary.verdicts.REVIEW} (${(summary.verdicts.REVIEW/summary.totalReferences*100).toFixed(1)}%) |\n`;
md += `| **KEEP** | ${summary.verdicts.KEEP} (${(summary.verdicts.KEEP/summary.totalReferences*100).toFixed(1)}%) |\n`;
md += `| Pages with DELETE items | ${summary.pageFlags.hasDeleteItems} |\n`;
md += `| Pages with REVIEW items | ${summary.pageFlags.hasReviewItems} |\n`;
md += `| Pages with <3 refs | ${summary.pageFlags.lowReferenceCount} |\n`;
md += `| Pages with ONLY paid catalog | ${summary.pageFlags.allPaidOnly} |\n\n`;

// P0
md += `## P0: Generic GVR Reports (ConvAI / LLM / GenAI)\n\n`;
if (summary.p0GenericGVR.count === 0) {
  md += `✅ **CLEAN** — 三条泛 AI 市场报告组合（Conversational AI / LLM / Generative AI from GVR/giiresearch）已不在任何 tools 页出现。\n\n`;
} else {
  md += `❌ **${summary.p0GenericGVR.count} pages still affected:**\n\n`;
  for (const p of summary.p0GenericGVR.pagesStillAffected) {
    md += `- ${p}\n`;
  }
  md += `\n`;
}

// Cross-page URLs
md += `## Cross-Page URL Reuse (3+ unrelated pages)\n\n`;
if (summary.crossPageUrls.length === 0) {
  md += `No URLs found on 3+ unrelated tool pages.\n\n`;
} else {
  md += `| URL | Count | Slugs |\n|-----|-------|-------|\n`;
  for (const c of summary.crossPageUrls) {
    md += `| ${c.url} | ${c.count} | ${c.slugs.join(', ')} |\n`;
  }
  md += `\n`;
}

// Identical ref sets (excluding EN/ZH pairs)
md += `## Identical Reference Sets (Cross-Category Reuse)\n\n`;
const suspiciousSets = summary.identicalRefSets.filter(g => {
  if (g.urlCount === 0) return g.pages.length > 2;
  const enSlugs = g.pages.filter(p => p.startsWith('/tools/') && !p.startsWith('/zh/'));
  return enSlugs.length > 2;
});

if (suspiciousSets.length === 0) {
  md += `No suspicious cross-category identical sets.\n\n`;
} else {
  for (const g of suspiciousSets) {
    const enPages = g.pages.filter(p => p.startsWith('/tools/') && !p.startsWith('/zh/'));
    md += `### ${enPages.length} EN pages share ${g.urlCount} identical URLs\n\n`;
    md += enPages.map(p => `- \`${p}\``).join('\n') + '\n\n';
  }
}

// Pages without references
const noRefs = Object.entries(perPage).filter(([, v]) => v.count === 0);
if (noRefs.length > 0) {
  md += `## Pages With Zero References (${noRefs.length})\n\n`;
  md += noRefs.map(([k]) => `- \`${k}\``).join('\n') + '\n\n';
}

// Pages with <3 refs
const lowRefs = Object.entries(perPage).filter(([, v]) => v.lowCount);
if (lowRefs.length > 0) {
  md += `## Pages With <3 References (${lowRefs.length})\n\n`;
  md += `| pageKey | count | DELETE | REVIEW | KEEP |\n|---------|-------|--------|--------|------|\n`;
  for (const [k, v] of lowRefs.sort((a,b) => a[0].localeCompare(b[0]))) {
    md += `| ${k} | ${v.count} | ${v.deleteCount} | ${v.reviewCount} | ${v.keepCount} |\n`;
  }
  md += `\n`;
}

// Full per-page tables - EN only
md += `---\n\n## Per-Page Audit Tables (EN pages)\n\n`;

for (const [pageKey, pageData] of enPages) {
  if (pageData.count === 0) continue;

  const flag = pageData.deleteCount > 0 ? '🔴' : pageData.reviewCount > 0 ? '🟡' : '🟢';
  md += `### ${flag} ${pageKey} (${pageData.count} refs: ${pageData.keepCount} KEEP / ${pageData.reviewCount} REVIEW / ${pageData.deleteCount} DELETE)\n\n`;
  md += `| # | pageKey | title | url | verdict | reason |\n`;
  md += `|---|---------|-------|-----|---------|--------|\n`;
  for (const r of pageData.refs) {
    const title = r.title.replace(/\|/g, '\\|').slice(0, 80);
    const url = r.url.length > 60 ? r.url.slice(0, 57) + '...' : r.url;
    const reason = r.reason.replace(/\|/g, '\\|').slice(0, 100);
    md += `| ${r.idx} | ${pageKey} | ${title} | ${url} | **${r.verdict}** | ${reason} |\n`;
  }
  md += `\n`;
}

// ZH-only pages
if (zhOnlyPages.length > 0) {
  md += `---\n\n## ZH-Only Pages (no EN mirror)\n\n`;
  for (const [pageKey, pageData] of zhOnlyPages) {
    if (pageData.count === 0) {
      md += `### ${pageKey} — 0 refs\n\n`;
      continue;
    }
    md += `### ${pageKey} (${pageData.count} refs)\n\n`;
    md += `| # | title | url | verdict | reason |\n`;
    md += `|---|-------|-----|---------|--------|\n`;
    for (const r of pageData.refs) {
      const title = r.title.replace(/\|/g, '\\|').slice(0, 80);
      const url = r.url.length > 60 ? r.url.slice(0, 57) + '...' : r.url;
      md += `| ${r.idx} | ${title} | ${url} | **${r.verdict}** | ${r.reason.replace(/\|/g, '\\|').slice(0, 100)} |\n`;
    }
    md += `\n`;
  }
}

// DELETE summary by page
md += `---\n\n## DELETE Summary (sorted by delete count)\n\n`;
const deletePages = Object.entries(perPage)
  .filter(([, v]) => v.deleteCount > 0)
  .sort((a, b) => b[1].deleteCount - a[1].deleteCount || a[0].localeCompare(b[0]));

md += `| pageKey | total | DELETE | REVIEW | KEEP |\n|---------|-------|--------|--------|------|\n`;
for (const [k, v] of deletePages) {
  md += `| ${k} | ${v.count} | ${v.deleteCount} | ${v.reviewCount} | ${v.keepCount} |\n`;
}

const outPath = path.join(path.dirname(fileURLToPath(import.meta.url)), 'audit-tools-references-report.md');
fs.writeFileSync(outPath, md);
console.log(`Report written to ${outPath}`);
console.log(`EN pages with refs: ${enPages.filter(([,v]) => v.count > 0).length}`);
console.log(`Total DELETE refs: ${summary.verdicts.DELETE}`);
