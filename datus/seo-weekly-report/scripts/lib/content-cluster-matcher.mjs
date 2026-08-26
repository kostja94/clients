/**
 * Content cluster matching — aligns GSC pages with datus/blog categories.
 */

import { normalizePath, isBlogPath } from './landing-page-classifier.mjs';

function globToRegex(glob) {
  const escaped = glob
    .replace(/[.+^${}()|[\]\\]/g, '\\$&')
    .replace(/\*\*/g, '<<GLOBSTAR>>')
    .replace(/\*/g, '[^/]*')
    .replace(/<<GLOBSTAR>>/g, '.*');
  return new RegExp(`^${escaped}$`, 'i');
}

export function buildClusterRules(registry) {
  return (registry.clusters || []).map((c) => ({
    id: c.id,
    label: c.label,
    pathPatterns: (c.pathPatterns || []).map(globToRegex),
    blogCategories: c.blogCategories || [],
  }));
}

export function matchPathToCluster(path, registry) {
  const p = normalizePath(path);
  const rules = buildClusterRules(registry);

  for (const rule of rules) {
    for (const re of rule.pathPatterns) {
      if (re.test(p)) {
        return { clusterId: rule.id, clusterLabel: rule.label };
      }
    }
  }
  return { clusterId: 'other', clusterLabel: 'Other' };
}

export function matchBlogPostToCluster(post, registry) {
  const categoryMap = registry.blogCategoryMap || {};
  const fromCategory = categoryMap[post.category];
  if (fromCategory) {
    const cluster = (registry.clusters || []).find((c) => c.id === fromCategory);
    return { clusterId: fromCategory, clusterLabel: cluster?.label || fromCategory };
  }
  return matchPathToCluster(`/blog/${post.slug}`, registry);
}

export function aggregateClusterMetrics(pages, registry) {
  const byCluster = new Map();

  for (const page of pages) {
    const path = page.url || page.path || '';
    const { clusterId, clusterLabel } = matchPathToCluster(path, registry);
    if (!byCluster.has(clusterId)) {
      byCluster.set(clusterId, {
        id: clusterId,
        label: clusterLabel,
        clicks: 0,
        impressions: 0,
        clicksPrev: 0,
        impressionsPrev: 0,
        pageCount: 0,
        topPages: [],
      });
    }
    const entry = byCluster.get(clusterId);
    entry.clicks += page.clicks || 0;
    entry.impressions += page.impressions || 0;
    entry.clicksPrev += page.clicksPrev || 0;
    entry.impressionsPrev += page.impressionsPrev || 0;
    entry.pageCount += 1;
    entry.topPages.push({
      path: normalizePath(path),
      clicks: page.clicks || 0,
      impressions: page.impressions || 0,
    });
  }

  return [...byCluster.values()]
    .map((c) => ({
      ...c,
      topPages: c.topPages.sort((a, b) => b.clicks - a.clicks).slice(0, 5),
    }))
    .sort((a, b) => b.clicks - a.clicks);
}

export function findWeeklyNewPosts(catalog, periodStart, periodEnd) {
  const start = periodStart;
  const end = periodEnd;
  return (catalog.posts || []).filter((p) => {
    if (!p.date || p.status === 'draft') return false;
    return p.date >= start && p.date <= end;
  });
}

export function attachFirstWeekGscPerformance(newPosts, gscPages, period) {
  const pageMap = new Map();
  for (const p of gscPages) {
    const path = normalizePath(p.url || p.path);
    pageMap.set(path, p);
  }

  return newPosts.map((post) => {
    const path = `/blog/${post.slug}`;
    const gsc = pageMap.get(path) || pageMap.get(`${path}/`) || null;
    return {
      slug: post.slug,
      title: post.title,
      category: post.category,
      date: post.date,
      path,
      gsc: gsc
        ? {
            clicks: gsc.clicks || 0,
            impressions: gsc.impressions || 0,
            ctr: gsc.ctr || 0,
            position: gsc.position || gsc.avgPosition || null,
            clicksPrev: gsc.clicksPrev || 0,
          }
        : { clicks: 0, impressions: 0, ctr: 0, position: null, clicksPrev: 0 },
      weeksSincePublish: computeWeeksSince(post.date, period.current.end),
    };
  });
}

function computeWeeksSince(dateStr, endStr) {
  if (!dateStr || !endStr) return null;
  const d0 = new Date(dateStr);
  const d1 = new Date(endStr);
  const diff = d1 - d0;
  return Math.max(0, Math.floor(diff / (7 * 24 * 3600 * 1000)));
}

export function summarizeBlogInventory(catalog) {
  const posts = (catalog.posts || []).filter((p) => p.status !== 'draft');
  const byCategory = {};
  for (const p of posts) {
    byCategory[p.category] = (byCategory[p.category] || 0) + 1;
  }
  return {
    totalPosts: posts.length,
    byCategory,
    lastSyncedAt: catalog.meta?.syncedAt || null,
    source: catalog.meta?.source || 'unknown',
  };
}
