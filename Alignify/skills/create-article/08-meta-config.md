# Step 8 — Meta + Config 注册

> **规范**：[`rules/meta.md`](./rules/meta.md)  
> **部署仓**：`src/data/*-meta.ts` · `*-pages-config.ts` · `*-article-images.ts`

---

## 按 articleType 注册

| articleType | Meta | Config | 图片 |
|-------------|------|--------|------|
| best-ranking | `blog-meta.ts` | `blog-pages-config.ts` | `blog-article-images.ts` |
| best-ranking-legacy | `tools-meta.ts` | `tools-pages-config.ts` | tools 映射 |
| seo-guide | `seo-meta.ts` | `seo-pages-config.ts` | `seo-article-images.ts` |
| marketing-strategy | `marketing-meta.ts` | `marketing-pages-config.ts` | — |
| insights-analysis | `insights-meta.ts` | `insights-pages-config.ts` | `insights-article-images.ts` |

---

## blog-meta.ts 示例

```ts
"{slug}": {
  en: { title: "Best … (2026): … | Alignify", description: "…" },
  zh: { title: "最佳…（2026）：… | Alignify", description: "探索2026年最佳…" },
  publishDate: "2026-06-23T00:00:00+08:00",
  modifiedDate: "2026-06-23T00:00:00+08:00",
},
```

- `publishDate` / `modifiedDate` 为 **slug 级** ISO 字段
- Hub 归属由 frontmatter `category` 推导；**无** `routeCategory`

---

## 日期双源

| 位置 | 格式 |
|------|------|
| `*-meta.ts` | ISO `+08:00` |
| md frontmatter `date`/`updated` | `"2026年8月26日"` / `"August 26, 2026"` |

同一日历日须一致。

### 新 slug：publishDate 全站唯一（Step 08 注册前）

**禁止**手写日期或复制邻近 slug。注册前必跑：

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --check YYYY-MM-DD
```

- **新 slug**：`publishDate` = `modifiedDate` = 脚本输出的空闲日；md `date` / `updated` 同日历日  
- **改版 slug**：`publishDate` / md `date` **不变**；仅 `modifiedDate` / md `updated` → 锚定日（实际执行日 UTC+8）

细则：[`11-publish-dates.md`](./11-publish-dates.md)

---

## 检查

- [ ] Meta title/description 符合 [`rules/meta.md`](./rules/meta.md)
- [ ] **新 slug**：`next-publish-date.mjs --check` Pass；publishDate 全站唯一
- [ ] **改版 slug**：publishDate 未改；modifiedDate = 锚定日
- [ ] `*-pages-config.ts` 已注册
- [ ] frontmatter `pageUrl` 与频道一致
- [ ] sitemap 自动从 config 生成，无需手改

下一步：[09-en-content.md](./09-en-content.md)
