# Tools 文章 10 节结构 × Markdown 映射

> **来源**：`content/templates/template-tools.md` §一
> **版本**：v3.0 · 2026-08-23
> **格式**：`content/{blog|tools}/{locale}/{slug}.md` + 集中 JSON（TL;DR / FAQ / References）

---

## 一、结构顺序（不可变）

| 序号 | 章节 | 存储位置 | 渲染方式 | 必需 |
|------|------|---------|---------|------|
| 1 | 核心要点 | `src/data/tldr-data.json` | `Tldr.tsx` 按 `pageUrl` 注入 | ✅ |
| 2 | 什么是 XXX | md `<!-- block:section -->` | `Section.tsx` | ✅ |
| 3 | XXX 如何工作 | md section | `Section.tsx` | ✅ |
| 4 | 各类型工具介绍 | md section + 产品 H3 | `Section.tsx` + `childrenHtml` / 段落 | ✅ |
| 5 | 工具对比表格 | md `<!-- block:html -->` 或 section 内 table | `html` block 或 Section children | 推荐 |
| 6 | 应用场景 | md section + H3 场景 | `Section.tsx` | ✅ |
| 7 | 如何选择 | md section + H3 步骤 | `Section.tsx`（**无** HowToChoose 组件） | ✅ |
| 8 | 结论 | md section | `Section.tsx` | ✅ |
| 9 | FAQ | `src/data/faq-data.json` | 全局 `FAQ.tsx`（ConditionalChrome） | ✅（**7 问**） |
| 10 | 参考文献 | `src/data/references-data.json` | `References.tsx` 按 `pageUrl` 注入 | 推荐 |

**硬约束**：结论（8）必须在 FAQ（9）之前（正文区块顺序；FAQ 由全局组件渲染在文末）。

> **已废弃**：JSON block 类型 `howItWorks` / `bestTools` / `useCases` / `howToChoose` / `comparisonSection`；对应 React 组件已从部署仓删除。

---

## 二、Frontmatter（页面 H1 / 摘要 / 分类）

```yaml
---
title: "H1：不写年份，推荐「类型：核心价值」"
description: "三段式摘要，中文 80–150 字，避免通用结尾"
slug: "{slug}"
date: "2026年6月23日"
updated: "2026年6月23日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/blog/{slug}"
locale: "zh"
category: "coding-dev"
categorySecondary: "ai-agents"
heroImage: "/blog/{slug}/hero.jpg"
heroImageAlt: "…"
---
```

- `title` / `description` → 解析为内部 `blogLayout.title` / `blogLayout.excerpt`
- `category` → Hub 归属（经 `ARTICLE_CATEGORY_MAP`）；**非** config 里的 `routeCategory`
- SEO title/description → `blog-meta.ts`（或 `tools-meta.ts`），与 frontmatter 主题一致、不必同文

---

## 三、各章节 Markdown 写法

### 1. TL;DR（集中 JSON）

键：`tldr-data.json` → `pages["/blog/{slug}"]` 或 `pages["/tools/{slug}"]`

```json
{
  "title": "核心要点",
  "introduction": "40-80字中文简介",
  "items": ["要点1", "要点2", "要点3", "要点4"]
}
```

规则：items 4–5 条；md 中 `<!-- block:tldr -->` **已废弃**（解析器 skip）。

内链（R-TLDR）：TLDR intro **0–1 链**；items 无链。见 [`02c-internal-links-drafting.md`](../02c-internal-links-drafting.md)。

### 2–3. 什么是 / 如何工作

```markdown
<!-- block:section -->
## 什么是 {工具类型} {#section-1}

段落1…

段落2…
```

规则：2–4 段；中文每段 60–120 字；可含 1–2 内链。

### 4. Best 榜单（正文 section，非 BestTools 组件）

```markdown
<!-- block:section -->
## 2026 年最好的 {分类} {#best-{slug}-2026}

引导段…

### 产品名 {#product-slug}

![截图 alt](/blog/{slug}/product.jpg)

段落1：核心定位…
段落2：关键差异…
段落3：最佳适用场景…
```

规则：每产品 ZH description ≥100 字 / EN ≥280 字符；shortDescription 写在首段或 H3 下首句。

### 5. 对比表格

```markdown
<!-- block:html -->
<table>…</table>
```

或 section 内 Markdown 表格（GFM）。4 列标准：工具名称、核心特点、主要应用场景、定价模式。

### 6. 应用场景

```markdown
<!-- block:section -->
## {工具类型}都能做什么 {#use-cases}

引导段…

### 1. 场景名 {#use-case-1}

100–260 字描述…
```

规则：4–6 个 H3 场景。

### 7. 如何选择（正文 only）

> SSOT：[section-how-to.md](../../content/sections/section-how-to.md)

```markdown
<!-- block:section -->
## 如何选择 {品类} {#how-to-choose-{slug}}

选型框架 intro（可 1 内链）…

### 明确使用需求 {#step-1}

≥80 字实操说明…

### 评估输出质量 {#step-2}
…
```

规则：3–5 个 `###` 步骤；**禁止** frontmatter `howTo:`；**无** HowTo JSON-LD。

标杆：`content/blog/zh/web-fetch.md`、`content/tools/zh/text.md`

### 8. 结论

```markdown
<!-- block:section -->
## 结论 {#conclusion}

段落1…
段落2…
```

### 9. FAQ（集中 JSON）

```json
{
  "items": [
    { "question": "问题1？", "answer": "答案1" }
  ]
}
```

规则：**7 问**（线上标准）；答案 plain text，**无内链**；独立撰写，不复制正文。

### 10. References（集中 JSON）

```json
{
  "items": [
    { "title": "来源标题", "url": "https://..." }
  ]
}
```

---

## 四、Meta 注册（blog-meta.ts 示例）

```ts
export const BLOG_META: Record<string, PageMeta> = {
  "{slug}": {
    en: { title: "Best …", description: "…" },
    zh: { title: "最佳…", description: "…" },
    publishDate: "2026-06-23T00:00:00+08:00",
    modifiedDate: "2026-06-23T00:00:00+08:00",
  },
};
```

`publishDate` 创建后永不更改。Hub 配置见 `blog-pages-config.ts`（无 `routeCategory`）。

---

## 五、验收命令

```bash
npm run verify:content-json
npm run build
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

> **已废弃**：`npm run audit:howto-choose`、JSON `howToChoose` block、frontmatter `howTo:`

---

*tools-article-anatomy · v3.0 · 2026-08-23*
