/**
 * Parse datus/blog/*.md frontmatter → blog catalog entries.
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
  const entries = readdirSync(blogDir);
  const posts = [];

  for (const file of entries) {
    if (!file.endsWith('.md')) continue;
    if (SKIP_FILES.has(file)) continue;

    const fullPath = join(blogDir, file);
    if (!statSync(fullPath).isFile()) continue;

    const content = readFileSync(fullPath, 'utf8');
    const fm = parseFrontmatter(content);

    const slug = fm.slug || file.replace(/^\d+-/, '').replace(/-2026\.md$/, '.md').replace(/\.md$/, '');
    posts.push({
      file,
      slug: fm.slug || slug,
      title: fm.title || slug,
      description: fm.description || '',
      date: fm.date || null,
      author: fm.author || '',
      category: fm.category || 'Uncategorized',
      keywords: fm.keywords || '',
      status: fm.status === 'draft' ? 'draft' : 'live',
      canonicalPath: `/blog/${fm.slug || slug}`,
    });
  }

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
