# Step 3 — Meta 注册 + 配置注册

> **前置条件**：Step 2 完成（中文 Markdown + 集中 JSON 已创建）
> **产出**：`blog-meta.ts`（或 `tools-meta.ts`）更新 + `blog-pages-config.ts`（或 `tools-pages-config.ts`）更新
> **参照**：[`references/meta-requirements.md`](./references/meta-requirements.md)

---

## 3.0 路由决策（先读此节）

**新文章默认走 `/blog/{slug}`**。旧 `/tools/{slug}` 路由保持不变（108 篇存量仍活跃）。

| 路由 | 内容目录 | Meta 注册 | Config 注册 | 适用 |
|------|---------|-----------|-------------|------|
| `/blog/{slug}` | `content/blog/{en,zh}/{slug}.md` | `src/data/blog-meta.ts` | `src/data/blog-pages-config.ts` | **新文章（默认）** |
| `/tools/{slug}` | `content/tools/{en,zh}/{slug}.md` | `src/data/tools-meta.ts` | `src/data/tools-pages-config.ts` | 旧文章（保持不变） |

**架构说明**：
- **不存在**每 slug 一个 `page.tsx`。路由使用单个动态路由：`app/[locale]/blog/[slug]/page.tsx`（或 `tools/[slug]/page.tsx`）。
- Meta 由 `generateMetadata()` 从 `BLOG_META[slug]`（或 `TOOLS_META[slug]`）读取。
- 正文由 `getPageData("blog"|"tools", slug, locale)` 加载 Markdown；遗留 JSON 仅 glossary / media-kit。
- **Hub 归属**：由 frontmatter `category` → `ARTICLE_CATEGORY_MAP` → `categoryToChannel` **推导**；`blog-pages-config.ts` **无** `routeCategory` 字段。

---

## 3.1 注册 blog-meta.ts（新文章）

在 `src/data/blog-meta.ts` 中新增 slug 条目。**注意**：`publishDate` / `modifiedDate` 是 **slug 级字段**，不在 `en` / `zh` 内。

```ts
export const BLOG_META: Record<string, PageMeta> = {
  "{slug}": {
    en: {
      title: "Best {Tool Type} (2026): {Subtitle} | Alignify",
      description: "Explore the best {tool type} in 2026: {Product A}, {Product B}, and more. Compare {key features} and find the right tool for {use case}. Free guide — read now.",
    },
    zh: {
      title: "最佳{工具类型}（2026）：{2-4个标签，顿号分隔} | Alignify",
      description: "探索2026年最佳{工具类型}：{产品A}、{产品B}等。比较{核心功能}，{用户收益}。立即探索站内完整指南，免费阅读。",
    },
    publishDate: "2026-06-23T00:00:00+08:00",
    modifiedDate: "2026-06-23T00:00:00+08:00",
  },
};
```

**publishDate 规则**：已上线 slug 永不更改。格式以部署仓源文件为准（当前为 **ISO 8601 +08:00**）。成批 deploy 前执行 Step 6 错开未上线 slug 的日期。`modifiedDate` 每次内容更新时修改。

---

## 3.2 注册 blog-pages-config.ts（新文章）

在 `src/data/blog-pages-config.ts` 中新增条目。**创建前先 Read 源文件确认 `BlogPageItem` 接口**。

```ts
export const BLOG_PAGES: BlogPageItem[] = [
  {
    slug: "{slug}",
    shortTitleEn: "{Short English Title}",
    shortTitleZh: "{简短中文标题}",
    toolsHubCategory: "dev-coding",       // channel=tools 时填；Read tools-pages-config 分组键
    hubKeywordEn: "{Hub keyword}",
    hubKeywordZh: "{Hub 关键词}",
    // marketingHubCategory: "affiliate", // channel=marketing 时填
  },
];
```

**shortTitle**：Hub 导航用简短标题，非完整 SEO title。

**无 `routeCategory`**：Hub 展示频道由 frontmatter `category` 推导（如 `coding-dev` → tools hub；`marketing` → marketing hub）。

---

## 3.3 注册 blog-article-images.ts（OG / 封面图）

```ts
export const BLOG_ARTICLE_IMAGES: Record<string, string> = {
  "{slug}": `${BASE}/blog/{slug}/hero.jpg`,
};
```

图片文件须存在于 `public/blog/{slug}/`。

---

## 3.4 Meta 四要素 + Frontmatter 对应

| 要素 | SEO 位置 | 页面 H1 / 摘要位置 |
|------|---------|-------------------|
| Meta title | `BLOG_META[slug].en/zh.title` | — |
| Meta description | `BLOG_META[slug].en/zh.description` | — |
| H1 | — | md frontmatter `title` |
| Excerpt | — | md frontmatter `description` |

完整约束见 [`references/meta-requirements.md`](./references/meta-requirements.md)。

---

## 3.5 Frontmatter 中的 pageUrl 与 category

```yaml
---
title: "AI 组件库：Vibe Coding 的 Prompt 模板与 Registry"
description: "三段式摘要，80–150 字…"
slug: "ai-components"
date: "2026年7月10日"
updated: "2026年7月10日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/blog/ai-components"
locale: "zh"
category: "coding-dev"
categorySecondary: ""
heroImage: "/blog/ai-components/hero.jpg"
heroImageAlt: "…"
---
```

- `pageUrl`：Blog 新文用 `/blog/` 路径；英文 md 用 `https://alignify.co/blog/{slug}`。
- `category`：12 统一分类 ID（与 `src/data/category-config.ts` 一致）；驱动 Hub 归属与 `ARTICLE_CATEGORY_MAP` 生成。

---

## 3.6 日期双源同步

| 位置 | 格式 | 用途 |
|------|------|------|
| `blog-meta.ts` → `publishDate` / `modifiedDate` | ISO `2026-06-23T00:00:00+08:00` | SEO、sitemap、OG |
| md frontmatter `date` / `updated` | 中文 `"2026年6月23日"` / 英文 `"June 23, 2026"` | Hero 展示 |

**同一日历日，两处须一致。** 创建后 `publishDate`（meta）不变；内容更新时改 `modifiedDate` + frontmatter `updated`。

---

## 3.7 Sitemap

sitemap 从 `BLOG_PAGES` / `TOOLS_PAGES` 自动生成，**无需**手改 `sitemap.ts`。

---

## 3.8 重定向：两种注册模式

### 模式 A：全新 slug（默认）

| 注册位置 | 操作 |
|---------|------|
| `blog-meta.ts` | 新增 slug |
| `blog-pages-config.ts` | 新增 `BlogPageItem` |
| `blog-article-images.ts` | 新增图片映射 |
| `tools-meta.ts` / `tools-pages-config.ts` | **不操作** |

### 模式 B：从 Tools 迁移到 Blog

| 注册位置 | 操作 |
|---------|------|
| `blog-meta.ts` | 新增 slug |
| `blog-pages-config.ts` | 新增条目 |
| `blog-article-images.ts` | 新增映射 |
| `tools-meta.ts` / `tools-pages-config.ts` | **保留**原条目 |

**Redirect**：`app/[locale]/tools/[slug]/page.tsx` 检查 `BLOG_META[slug]`——若存在，自动 redirect 到 `/blog/{slug}`。

参考：`data-engineering-agent` 同时存在于两套 meta/config；访问 `/tools/data-engineering-agent` 会 redirect。

---

## 3.9 Step 3 完成检查

- [ ] `blog-meta.ts` en/zh 完整；日期为 slug 级 ISO 字段
- [ ] title 含 `Best`/「最佳」、年份、冒号副线
- [ ] description 列举 ≥2 产品名
- [ ] `blog-pages-config.ts` 已注册（含 hub 分组字段）
- [ ] `blog-article-images.ts` 已注册
- [ ] md frontmatter `pageUrl` 为 `/blog/` 路径
- [ ] frontmatter `date`/`updated` 与 meta 日历一致
- [ ] frontmatter `category` 已填
- [ ] md 位于 `content/blog/{en,zh}/{slug}.md`
- [ ] 模式 A 或 B 已确认

---

*03-meta-and-config · v3.0 · 2026-08-23*
