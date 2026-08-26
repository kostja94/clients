# Blog / Tools 页面架构（Markdown 时代）

> **新文（2026-08+）**：`content/blog/{locale}/{slug}.md` 或 `content/tools/{locale}/{slug}.md` + 动态路由。**禁止** frontmatter `heroHtml` / `heroContent`（E44）。  
> **Meta**：`blog-meta.ts` / `tools-meta.ts` + md frontmatter `title` / `description`。  
> **TL;DR / FAQ / References**：**仅 JSON 侧车渲染**（[`anatomy.md`](../anatomy.md) §二·一）；Brief 采用 → Step 08 注册。

---

## 路由与 Meta

| 类型 | 正文路径 | URL | Meta 注册 |
|------|----------|-----|-----------|
| blog 新文 | `content/blog/{locale}/{slug}.md` | `/blog/{slug}` · `/zh/blog/{slug}` | `blog-meta.ts` + `blog-pages-config.ts` |
| Tools 存量 | `content/tools/{locale}/{slug}.md` | `/tools/{slug}` · `/zh/tools/{slug}` | `tools-meta.ts` + `tools-pages-config.ts` |
| marketing 存量 | `content/marketing/{locale}/{slug}.md` | `/marketing/{slug}` · `/zh/marketing/{slug}` | `marketing-meta.ts` |
| seo 存量 | `content/seo/{locale}/{slug}.md` | `/seo/{slug}` · `/zh/seo/{slug}` | `seo-meta.ts` |

由 `app/[locale]/blog/[slug]/page.tsx`（及 tools 等价路由）的 `generateMetadata()` 读取 Meta。**无需** per-slug `page.tsx`。

---

## frontmatter（H1 / excerpt）

```yaml
title: "H1 文案"
description: "excerpt 级摘要"
slug: "{slug}"
date: "2026年8月26日"
updated: "2026年8月26日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/blog/{slug}"
locale: "zh"
category: "marketing"
```

白名单与禁止键：[`anatomy.md`](../anatomy.md) §二。

---

## 正文结构

- `<!-- block:section -->` + Markdown `##` / `###` + `{#anchor}`
- 列表 / 表格 / 复杂 HTML → `childrenHtml`（[`anatomy.md`](../anatomy.md) §四·一）
- 导语、姊妹链 → **首节 BLUF**（非 frontmatter HTML）
- 结论收束 md 正文（FAQ 在页底全局组件，若两者皆有）

---

## Step 08 同批注册

除 Meta 外，Brief 采用 TL;DR / FAQ / References 时须注册 JSON 侧车（见 [`08-meta-config.md`](../../08-meta-config.md)）+ `cta-config.json`。

验收：`audit-frontmatter.py` · `npm run verify:content-json` · `merge-cta-slugs.mjs --check`。

---

*bloglayout · v2.0 · 2026-08-27*
