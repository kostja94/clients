/**
 * Audita campos SEO (seo_title, seo_description) em content JSON files.
 * Verifica comprimento de título e descrição contra limites recomendados.
 *
 * Uso:
 *   node scripts/audit-seo-meta.js
 *   node scripts/audit-seo-meta.js --min-title 50 --max-title 60 --min-desc 120 --max-desc 158
 *   node scripts/audit-seo-meta.js --dir content/topics
 *
 * Limites padrão para pt-BR:
 *   seo_title: 50–60 caracteres
 *   seo_description: 120–158 caracteres
 */

const fs = require('fs');
const path = require('path');
const { getDeployRoot } = require('../lib/deploy-root');

// ── CLI args ──────────────────────────────────────────────
const args = process.argv.slice(2);
function getArg(flag, fallback) {
  const i = args.indexOf(flag);
  return i >= 0 && i + 1 < args.length ? args[i + 1] : fallback;
}

const ROOT = getDeployRoot();
const TARGET_DIR = getArg('--dir', 'content');
const MIN_TITLE = parseInt(getArg('--min-title', '50'), 10);
const MAX_TITLE = parseInt(getArg('--max-title', '60'), 10);
const MIN_DESC = parseInt(getArg('--min-desc', '120'), 10);
const MAX_DESC = parseInt(getArg('--max-desc', '158'), 10);
const ONLY_VIOLATIONS = args.includes('--only-violations');

// ── Scan JSON files ──────────────────────────────────────
function collectJsonFiles(dir) {
  const full = path.join(ROOT, dir);
  const files = [];
  function walk(d) {
    if (!fs.existsSync(d)) return;
    for (const name of fs.readdirSync(d, { withFileTypes: true })) {
      if (name.isDirectory() && !name.name.startsWith('.')) {
        walk(path.join(d, name.name));
      } else if (name.name.endsWith('.json')) {
        // Skip non-content JSON files
        const rel = path.relative(full, path.join(d, name.name));
        files.push({ abs: path.join(d, name.name), rel });
      }
    }
  }
  walk(full);
  return files;
}

// ── Validate a single file ───────────────────────────────
function auditFile(filePath, relPath) {
  const issues = [];
  try {
    const raw = fs.readFileSync(filePath, 'utf-8');
    const data = JSON.parse(raw);

    const title = data?.seo_title;
    const desc = data?.seo_description;
    const slug = data?.slug || relPath.replace(/\.json$/, '');

    // Check title
    if (title === undefined || title === null || title === '') {
      issues.push({ field: 'seo_title', issue: 'missing', slug });
    } else if (typeof title !== 'string') {
      issues.push({ field: 'seo_title', issue: 'not a string', slug });
    } else {
      const len = title.length;
      if (len < MIN_TITLE) {
        issues.push({ field: 'seo_title', issue: `too short (${len} chars, min ${MIN_TITLE})`, slug, value: title });
      } else if (len > MAX_TITLE) {
        issues.push({ field: 'seo_title', issue: `too long (${len} chars, max ${MAX_TITLE})`, slug, value: title });
      }
    }

    // Check description
    if (desc === undefined || desc === null || desc === '') {
      issues.push({ field: 'seo_description', issue: 'missing', slug });
    } else if (typeof desc !== 'string') {
      issues.push({ field: 'seo_description', issue: 'not a string', slug });
    } else {
      const len = desc.length;
      if (len < MIN_DESC) {
        issues.push({ field: 'seo_description', issue: `too short (${len} chars, min ${MIN_DESC})`, slug, value: desc });
      } else if (len > MAX_DESC) {
        issues.push({ field: 'seo_description', issue: `too long (${len} chars, max ${MAX_DESC})`, slug, value: desc.substring(0, 120) + '…' });
      }
    }

    return { slug, file: relPath, issues, titleLen: typeof title === 'string' ? title.length : null, descLen: typeof desc === 'string' ? desc.length : null };
  } catch (e) {
    return { slug: relPath, file: relPath, issues: [{ field: 'parse', issue: e.message.split('\n')[0] }], titleLen: null, descLen: null };
  }
}

// ── Main ─────────────────────────────────────────────────
function main() {
  const dirs = TARGET_DIR.split(',').map(d => d.trim());
  const allFiles = [];
  for (const d of dirs) {
    allFiles.push(...collectJsonFiles(d));
  }

  console.log(`Auditando ${allFiles.length} arquivos em "${TARGET_DIR}"…\n`);
  console.log(`Limites: title ${MIN_TITLE}–${MAX_TITLE} chars | description ${MIN_DESC}–${MAX_DESC} chars\n`);

  const results = allFiles.map(f => auditFile(f.abs, f.rel));
  const violations = results.filter(r => r.issues.length > 0);
  const clean = results.filter(r => r.issues.length === 0);

  // ── Summary table (all files) ──────────────────────────
  if (!ONLY_VIOLATIONS) {
    console.log('─'.repeat(80));
    console.log('SUMMARY (all files)');
    console.log('─'.repeat(80));
    for (const r of results) {
      const titleOk = r.titleLen !== null && r.titleLen >= MIN_TITLE && r.titleLen <= MAX_TITLE;
      const descOk = r.descLen !== null && r.descLen >= MIN_DESC && r.descLen <= MAX_DESC;
      const tMark = titleOk ? '✓' : '✗';
      const dMark = descOk ? '✓' : '✗';
      const tLen = r.titleLen !== null ? String(r.titleLen) : '—';
      const dLen = r.descLen !== null ? String(r.descLen) : '—';
      console.log(`  ${tMark} ${dMark}  ${r.slug.padEnd(35)}  title: ${tLen.padStart(3)}  desc: ${dLen.padStart(3)}`);
    }
  }

  // ── Violations detail ──────────────────────────────────
  if (violations.length > 0) {
    console.log('\n' + '═'.repeat(80));
    console.log(`VIOLATIONS (${violations.length} arquivos)`);
    console.log('═'.repeat(80));
    for (const r of violations) {
      console.log(`\n📄 ${r.file}`);
      for (const iss of r.issues) {
        console.log(`   ❌ ${iss.field}: ${iss.issue}`);
        if (iss.value) {
          const preview = iss.value.length > 100 ? iss.value.substring(0, 100) + '…' : iss.value;
          console.log(`      "${preview}"`);
        }
      }
    }
    console.log('');
  }

  const totalIssues = violations.reduce((sum, r) => sum + r.issues.length, 0);

  // ── Stats ──────────────────────────────────────────────
  const stats = {
    total: results.length,
    clean: clean.length,
    violations: violations.length,
    totalIssues,
    titleTooShort: violations.reduce((c, r) => c + r.issues.filter(i => i.field === 'seo_title' && i.issue.startsWith('too short')).length, 0),
    titleTooLong: violations.reduce((c, r) => c + r.issues.filter(i => i.field === 'seo_title' && i.issue.startsWith('too long')).length, 0),
    titleMissing: violations.reduce((c, r) => c + r.issues.filter(i => i.field === 'seo_title' && i.issue === 'missing').length, 0),
    descTooShort: violations.reduce((c, r) => c + r.issues.filter(i => i.field === 'seo_description' && i.issue.startsWith('too short')).length, 0),
    descTooLong: violations.reduce((c, r) => c + r.issues.filter(i => i.field === 'seo_description' && i.issue.startsWith('too long')).length, 0),
    descMissing: violations.reduce((c, r) => c + r.issues.filter(i => i.field === 'seo_description' && i.issue === 'missing').length, 0),
  };

  console.log(`📊 Stats: ${stats.clean}/${stats.total} OK | ${stats.violations} files with ${stats.totalIssues} issues`);
  console.log(`   Títulos: ${stats.titleTooShort} short | ${stats.titleTooLong} long | ${stats.titleMissing} missing`);
  console.log(`   Descrições: ${stats.descTooShort} short | ${stats.descTooLong} long | ${stats.descMissing} missing`);

  if (violations.length > 0) {
    process.exit(1);
  }
  console.log('\n✅ Todos os campos SEO dentro dos limites!');
}

main();
