# Step 8 — Meta + Config + Final CTA 注册

> **规范**：[`rules/meta.md`](./rules/meta.md) · [`rules/sections.md`](./rules/sections.md) Part 5  
> **部署仓**：`src/data/*-meta.ts` · `*-pages-config.ts` · `*-article-images.ts` · **`src/data/cta-config.json`**

---

## 按 articleType 注册

| articleType | Meta | Config | 图片 |
|-------------|------|--------|------|
| best-ranking | `blog-meta.ts` | `blog-pages-config.ts` | `blog-article-images.ts` |
| best-ranking-legacy | `tools-meta.ts` | `tools-pages-config.ts` | tools 映射 |
| seo-guide | `blog-meta.ts`（**新文**） | `blog-pages-config.ts` | `blog-article-images.ts` |
| marketing-strategy | `blog-meta.ts`（**新文**） | `blog-pages-config.ts` | — |
| insights-analysis | `blog-meta.ts`（**新文**） | `blog-pages-config.ts` | `insights-article-images.ts` |

> **存量不重迁**：仍挂在 `content/marketing/`、`content/seo/` 等的 slug 继续用对应 `*-meta.ts`；**新 slug 一律** `blog-meta.ts` + `blog-pages-config.ts`。详见 [`article-types.md`](./rules/article-types.md)。

---

## TL;DR / FAQ / References JSON（Step 08 · 与 meta 同批）

**线上 SSOT = JSON 侧车**（见 [`anatomy.md`](./rules/anatomy.md) §二·一）。**Brief 采用 FAQ/TL;DR/References 时**，Step 08 注册（**不写 md**）：

| 文件 | 键 | 内容 |
|------|-----|------|
| `src/data/tldr-data.json` | `pages["{pageUrl路径}"]` | `introduction` + `items[]` |
| `src/data/faq-data.json` | 同上 pathname | `items[]` × **7** |
| `src/data/references-data.json` | 同上 pathname | `items[]` |

**键示例**：blog 新文 EN `/blog/{slug}` · ZH `/zh/blog/{slug}`；tools 存量 `/tools/{slug}` · `/zh/tools/{slug}`；seo `/seo/{slug}` · `/zh/seo/{slug}`。

**Brief 省略** TL;DR/FAQ/Refs → 三 JSON **不得**留对应键（否则页面上仍会显示）。

验收：人工核对 JSON 键与 Brief；`npm run verify:content-json` 实际跑 `verify-content-md.py`（**不验 JSON/E10**）。

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

## Final CTA（页底 SecondaryCta）

与 meta **同批**写入 `src/data/cta-config.json` → `slugs.{slug}`：

```json
"{slug}": {
  "zh": {
    "title": "一句 punchline（Brief Final CTA 草案）",
    "description": "1–2 句，承接结论或 Author POV",
    "cta": "开始合作"
  },
  "en": {
    "title": "English punchline (draft OK; finalize after Step 09)",
    "description": "1–2 sentences tied to EN conclusion",
    "cta": "Work with us"
  }
}
```

- Brief **Step 02** 须含 **Final CTA** 四字段（见 [`rules/article-brief.md`](./rules/article-brief.md)）
- Step 09 EN 完稿后更新 `en.title` / `en.description`
- 验收：`node E:\clients\Alignify\scripts\ops\merge-cta-slugs.mjs --check` → `Missing: 0`

细则：[`rules/sections.md`](./rules/sections.md) Part 5

---

## 检查

- [ ] Meta title/description 符合 [`rules/meta.md`](./rules/meta.md)
- [ ] **新 slug**：`next-publish-date.mjs --check` Pass；publishDate 全站唯一
- [ ] **改版 slug**：publishDate 未改；modifiedDate = 锚定日
- [ ] `*-pages-config.ts` 已注册
- [ ] **`cta-config.json`** 已注册 `slugs.{slug}`（ZH + EN；非 fallback）
- [ ] frontmatter `pageUrl` 与频道一致
- [ ] sitemap 自动从 config 生成，无需手改

下一步：若 EN 轨尚未完成 → [`rules/content-locale.md`](./rules/content-locale.md) Part 4（Step 09）；否则 → Part 5（09c 对等对比）→ [10-quality-gates.md](./10-quality-gates.md)
