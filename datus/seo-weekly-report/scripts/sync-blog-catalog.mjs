#!/usr/bin/env node
/**
 * Sync datus/blog/*.md frontmatter → ../blog-catalog.yaml
 *
 * Usage:
 *   npm run sync-blog
 *   BLOG_DIR=../../blog npm run sync-blog
 */

import { writeFileSync } from 'fs';
import { join, dirname, resolve } from 'path';
import { fileURLToPath } from 'url';
import { stringify as stringifyYaml } from 'yaml';
import { scanBlogDirectory, buildCatalogPayload } from './lib/blog-catalog.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const defaultBlogDir = resolve(ROOT, '..', 'blog');
const blogDir = resolve(process.env.BLOG_DIR || defaultBlogDir);
const outPath = join(ROOT, 'blog-catalog.yaml');

console.log('═══ Datus Blog Catalog 同步 ═══');
console.log(`  扫描: ${blogDir}`);

const posts = scanBlogDirectory(blogDir);
const payload = buildCatalogPayload(posts, blogDir);

writeFileSync(outPath, stringifyYaml(payload), 'utf8');

console.log(`  文章数: ${payload.meta.totalPosts}（含 draft: ${posts.filter((p) => p.status === 'draft').length}）`);
console.log(`  保存 → ${outPath} ✓`);
