# Step 4 — Meta 注册 + Config 注册

> **产出**：对应频道的 `*-meta.ts` + `*-pages-config.ts` + 图片映射（如适用）
> **引用**：Blog 新文复用 [`create-tools-article/03-meta-and-config.md`](../create-tools-article/03-meta-and-config.md)

---

## 前置条件

- [ ] 中文 md + 集中 JSON 已完成
- [ ] 文章类型与内容路径已确定（Step 1）
- [ ] frontmatter `category` 已填；Hub 分组字段已选定

---

## 按频道注册

| 类型 | Meta | Config | 图片 |
|------|------|--------|------|
| Blog 新文 | `blog-meta.ts` | `blog-pages-config.ts` | `blog-article-images.ts` |
| SEO | `seo-meta.ts` | `seo-pages-config.ts` | `seo-article-images.ts` |
| Marketing | `marketing-meta.ts` | `marketing-pages-config.ts` | — |
| Insights | `insights-meta.ts` | `insights-pages-config.ts` | `insights-article-images.ts` |

---

## blog-meta.ts 示例（Blog 新文）

```ts
"{slug}": {
  en: { title: "… | Alignify", description: "…" },
  zh: { title: "… | Alignify", description: "…" },
  publishDate: "2026-07-16T00:00:00+08:00",
  modifiedDate: "2026-07-16T00:00:00+08:00",
},
```

日期格式以部署仓源文件为准（当前 ISO +08:00）。

---

## blog-pages-config.ts（Blog 新文）

**无 `routeCategory` 字段**。Hub 频道由 frontmatter `category` → `ARTICLE_CATEGORY_MAP` → `categoryToChannel` 推导。

```ts
{
  slug: "{slug}",
  shortTitleEn: "…",
  shortTitleZh: "…",
  toolsHubCategory: "dev-coding",   // channel=tools 时
  hubKeywordEn: "…",
  hubKeywordZh: "…",
}
```

hub 分组键须 Read 对应 `*-pages-config.ts` 现有分组，**禁止编造**。

---

## Meta 四要素 vs Frontmatter

| 要素 | SEO meta | 页面展示 |
|------|----------|---------|
| title / description | `*-meta.ts` | — |
| H1 / excerpt | — | md `title` / `description` |

详见 [`references/meta-requirements.md`](./references/meta-requirements.md)。

---

## 日期双源

| 位置 | 格式 |
|------|------|
| `*-meta.ts` publishDate/modifiedDate | ISO |
| md frontmatter `date`/`updated` | 展示格式（中文/英文） |

---

## 输出清单

- [ ] 对应 `*-meta.ts` 已注册
- [ ] 对应 `*-pages-config.ts` 已注册
- [ ] frontmatter `pageUrl` 与频道一致
- [ ] meta 与 frontmatter 日期同一日历日
- [ ] `npm run build` 通过

---

*04-meta-and-config · v2.0 · 2026-08-23*
