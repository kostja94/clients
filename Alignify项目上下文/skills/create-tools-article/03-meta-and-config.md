# Step 3 — Meta 注册 + 配置注册

> **前置条件**：Step 2 完成（中文 JSON 已创建）
> **产出**：`blog-meta.ts`（或 `tools-meta.ts`）更新 + `blog-pages-config.ts`（或 `tools-pages-config.ts`）更新
> **参照**：[`references/meta-requirements.md`](./references/meta-requirements.md)

---

## 3.0 路由决策（先读此节）

**所有新文章走 `/blog/{slug}` 路由**。旧 `/tools/` 路由保持不变，仅新增文章统一进 Blog。

| 路由 | 内容目录 | Meta 注册 | Config 注册 | 适用 |
|------|---------|-----------|-------------|------|
| `/blog/{slug}` | `content/blog/{en,zh}/{slug}.json` | `src/data/blog-meta.ts` | `src/data/blog-pages-config.ts` | **新文章（默认）** |
| `/tools/{slug}` | `content/tools/{en,zh}/{slug}.json` | `src/data/tools-meta.ts` | `src/data/tools-pages-config.ts` | 旧文章（保持不变） |

**架构说明**（2026-05-20 迁移后）：
- **不存在**每 slug 一个 `page.tsx`。路由使用**单个动态路由文件**：`app/[locale]/blog/[slug]/page.tsx`（或 `app/[locale]/tools/[slug]/page.tsx`）。
- Meta 由 `generateMetadata()` 从 `BLOG_META[slug]`（或 `TOOLS_META[slug]`）读取，**无需**创建新的 page.tsx 文件。
- 正文由 `getPageData("blog", slug, locale)`（或 `getPageData("tools", slug, locale)`）加载 JSON。

---

## 3.1 注册 blog-meta.ts（新文章）

在 `src/data/blog-meta.ts` 中新增 slug 条目。**注意**：`publishDate` / `modifiedDate` 是 **slug 级字段**，不在 `en` / `zh` 内。

```ts
export const BLOG_META: Record<string, PageMeta> = {
  // ... existing entries ...

  "{slug}": {
    en: {
      title: "Best {Tool Type} (2026): {Subtitle} | Alignify",
      description: "Explore the best {tool type} in 2026: {Product A}, {Product B}, and more. Compare {key features} and find the right tool for {use case}. Free guide — read now.",
    },
    zh: {
      title: "最佳{工具类型}（2026）：{2-4个标签，顿号分隔} | Alignify",
      description: "探索2026年最佳{工具类型}：{产品A}、{产品B}等。比较{核心功能}，{用户收益}。立即探索站内完整指南，免费阅读。",
    },
    publishDate: "2026-06-23",
    modifiedDate: "2026-06-23",
  },
};
```

**publishDate 规则**：创建后**已上线** slug 永不更改。成稿阶段可暂用同一天；**成批 deploy 前**必须执行 Step 6（`06-publish-date-stagger.md`），未上线文章从锚点日往前**一天一篇**，并避让 `origin/main` 已占用日期。`modifiedDate` 每次内容更新时修改；未上线批次错开时可与 `publishDate` 相同。格式：日期字符串 `"YYYY-MM-DD"`（BLOG_META）或 ISO `"2026-06-23T00:00:00+08:00"`（TOOLS_META）。**创建前 Read 部署仓源文件确认当前格式**。

---

## 3.2 注册 blog-pages-config.ts（新文章）

在 `src/data/blog-pages-config.ts` 中新增条目。**字段为** `{ slug, shortTitleEn, shortTitleZh }`，**没有** `keywordEn` / `keywordZh` / `category`。

```ts
export const BLOG_PAGES: BlogPageItem[] = [
  // ... existing entries ...

  { slug: "{slug}", shortTitleEn: "{Short English Title}", shortTitleZh: "{简短中文标题}" },
];
```

**shortTitle 规则**：简洁描述性标题（非完整 SEO title），用于 Hub 页面展示和导航链接。例如 `shortTitleEn: "AI Inference Infrastructure Guide"`、`shortTitleZh: "AI推理基础设施指南"`。

> **重要**：创建前先 Read `src/data/blog-pages-config.ts` 确认当前接口定义，不可凭记忆填写。

---

## 3.3 注册 blog-article-images.ts（OG / 封面图）

在 `src/data/blog-article-images.ts` 中新增 slug 条目：

```ts
export const BLOG_ARTICLE_IMAGES: Record<string, string> = {
  // ... existing entries ...
  "{slug}": `${BASE}/blog/{slug}/hero.jpg`,
};
```

**图片要求**：实际文件须存在于 `public/blog/{slug}/` 下。格式为 JPG 或 PNG。`getBlogArticleImage(slug)` 自动读取此映射用于 Article Schema 和封面图显示。

---

## 3.4 Meta 四要素填写

按 [`references/meta-requirements.md`](./references/meta-requirements.md) 填写 `blog-meta.ts` 中的 en/zh 条目：

| 要素 | 位置 | 约束 |
|------|------|------|
| title（en） | `BLOG_META[slug].en.title` | 必须含 `Best`、`(2026)`、冒号副线 |
| title（zh） | `BLOG_META[slug].zh.title` | 必须含「最佳」、`（2026）`、冒号副线 |
| description（en） | `BLOG_META[slug].en.description` | 列举 ≥2 产品名、120–160 字符 |
| description（zh） | `BLOG_META[slug].zh.description` | 列举 ≥2 产品名、60–80 字 |
| H1（en） | `content/blog/en/{slug}.json` → `blogLayout.title` | 40–60 字符、不写年份 |
| H1（zh） | `content/blog/zh/{slug}.json` → `blogLayout.title` | 不写年份 |
| Excerpt（en） | `content/blog/en/{slug}.json` → `blogLayout.excerpt` | 200–250 字符、三段式 |
| Excerpt（zh） | `content/blog/zh/{slug}.json` → `blogLayout.excerpt` | 三段式、80–150 字、禁用通用结尾 |

**publishDate 双重位置**：
- `blog-meta.ts`（slug 级字段）：日期格式 `"2026-06-23"`，用于 SEO（`<meta>` 标签、sitemap `<lastmod>`）
- JSON `blogLayout`：展示用日期（中文 `"2026年6月23日"`、英文 `"June 23, 2026"`），用于页面 Hero 区域

---

## 3.5 JSON blogLayout 中的 pageUrl

Blog 文章的 `blogLayout.pageUrl` 应为 `/blog/` 路径：

```json
{
  "blogLayout": {
    "pageUrl": "https://alignify.co/zh/blog/{slug}"
  }
}
```

中英文 JSON 各设各的 locale 前缀。

---

## 3.6 Sitemap 覆盖

部署仓 sitemap 已从 `BLOG_PAGES` / `TOOLS_PAGES` 自动生成，**无需手动修改** `sitemap.ts`。确认：

- [ ] Blog 文章：`blog-pages-config.ts` 已注册 → sitemap 自动收录
- [ ] Tools 文章：`tools-pages-config.ts` 已注册 → sitemap 自动收录

---

## 3.7 重定向：两种注册模式

### 模式 A：全新 slug（默认）

适用于**全新创建的 Blog 文章**。只需注册 Blog 侧，不进 Tools 配置。

| 注册位置 | 操作 |
|---------|------|
| `blog-meta.ts` | 新增 slug 条目（en/zh title/description + publishDate/modifiedDate） |
| `blog-pages-config.ts` | 新增 `{ slug, shortTitleEn, shortTitleZh }` |
| `blog-article-images.ts` | 新增 `{slug}: BASE/blog/{slug}/hero.jpg` |
| `tools-meta.ts` | **不操作** |
| `tools-pages-config.ts` | **不操作** |

### 模式 B：从 Tools 迁移

适用于**原 `/tools/{slug}` 文章迁到 `/blog/{slug}`**。需同时在两套配置中注册。

| 注册位置 | 操作 |
|---------|------|
| `blog-meta.ts` | 新增 slug 条目 |
| `blog-pages-config.ts` | 新增 `{ slug, shortTitleEn, shortTitleZh }` |
| `blog-article-images.ts` | 新增图片映射 |
| `tools-meta.ts` | **保留**原条目（否则 `/tools/{slug}` 静态路由不生成） |
| `tools-pages-config.ts` | **保留**原条目（Tools Hub 仍展示此文章） |

**Redirect 机制**：动态路由文件 `app/[locale]/tools/[slug]/page.tsx` 检查 `BLOG_META[slug]`——若存在，自动将 `/tools/{slug}` redirect 到 `/blog/{slug}`。**无需手写 redirect 逻辑**。

> 参考案例：`data-engineering-agent` — 同时存在于 `TOOLS_META`、`BLOG_META`、`TOOLS_PAGES`、`BLOG_PAGES`。旧 URL 自动 redirect，新 URL 为 `/blog/data-engineering-agent`。

### 如何判断用哪种模式

- 全新文章、从未有过 `/tools/` URL → 模式 A
- 已有 `/tools/{slug}` 文章、需要迁移到 `/blog/` → 模式 B
- 不确定 → 先 Read `tools-meta.ts` 和 `tools-pages-config.ts` 搜索该 slug

---

## 3.8 Step 3 完成检查

- [ ] `blog-meta.ts` 中 en/zh 双向条目完整；`publishDate` / `modifiedDate` 为 slug 级字段
- [ ] title 含 `Best`/「最佳」、年份、冒号副线
- [ ] description 列举 ≥2 个产品名
- [ ] `blog-pages-config.ts` 中 `{ slug, shortTitleEn, shortTitleZh }` 已填写
- [ ] `blog-article-images.ts` 中图片映射已注册
- [ ] `blogLayout.pageUrl` 为 `/blog/` 路径
- [ ] publishDate 两处（meta.ts slug 级 + JSON blogLayout）已同步
- [ ] **Tools 更新**：`modifiedDate` 三处已同步（meta + en/zh JSON）；见 Step 7 [`07-tools-modified-date.md`](./07-tools-modified-date.md)
- [ ] JSON 文件位于 `content/blog/{en,zh}/{slug}.json`
- [ ] 确认使用模式 A（全新）还是模式 B（迁移），按对应模式注册

---

*03-meta-and-config · v2.1 · 2026-06-25*
