/**
 * Parse datus/blog (recursive) frontmatter → blog catalog entries.
 */

import { readFileSync, readdirSync, statSync } from 'fs';
import { join } from 'path';

const SKIP_FILES = new Set([
  'README.md',
  'internal-external-links-checklist.md',
  'keyword-cluster-data-engineering-agent.md',
]);

function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return {};

  const yaml = match[1];
  const result = {};
  for (const line of yaml.split('\n')) {
    const m = line.match(/^([a-zA-Z0-9_-]+):\s*"?(.+?)"?\s*$/);
    if (m) result[m[1]] = m[2].replace(/^"|"$/g, '');
  }
  return result;
}

export function scanBlogDirectory(blogDir) {
  const posts = [];

  function walk(dir, prefix = '') {
    for (const entry of readdirSync(dir)) {
      const fullPath = join(dir, entry);
      const relPath = prefix ? `${prefix}/${entry}` : entry;

      if (statSync(fullPath).isDirectory()) {
        walk(fullPath, relPath);
        continue;
      }

      if (!entry.endsWith('.md')) continue;
      if (SKIP_FILES.has(entry)) continue;

      const content = readFileSync(fullPath, 'utf8');
      const fm = parseFrontmatter(content);

      const slug = fm.slug || entry.replace(/^\d+-/, '').replace(/-2026\.md$/, '.md').replace(/\.md$/, '');
      posts.push({
        file: relPath,
        slug: fm.slug || slug,
        title: fm.title || slug,
        description: fm.description || '',
        date: fm.date || null,
        author: fm.author || '',
        category: fm.category || 'Uncategorized',
        secondaryCategory: fm.secondaryCategory || '',
        keywords: fm.keywords || '',
        status: fm.status === 'draft' ? 'draft' : 'live',
        canonicalPath: `/blog/${fm.slug || slug}`,
      });
    }
  }

  walk(blogDir);

  posts.sort((a, b) => {
    if (a.date && b.date) return a.date.localeCompare(b.date);
    return a.file.localeCompare(b.file);
  });

  return posts;
}

export function buildCatalogPayload(posts, blogDir) {
  return {
    meta: {
      source: 'datus/blog',
      blogDir,
      syncedAt: new Date().toISOString(),
      totalPosts: posts.filter((p) => p.status !== 'draft').length,
    },
    posts,
  };
}
