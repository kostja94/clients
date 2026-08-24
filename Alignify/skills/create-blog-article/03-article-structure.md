# Step 3 — 创建中文 Markdown + 集中 JSON

> **产出**：`content/{blog|seo|marketing|insights}/{locale}/{slug}.md` + `tldr-data.json` / `faq-data.json` / `references-data.json`
> **引用**：Tools 型复用 [`create-tools-article/02-article-structure.md`](../create-tools-article/02-article-structure.md)；类型结构见 [`references/article-types.md`](./references/article-types.md)

---

## 前置条件

- [ ] Step 1 Gate A 已通过（类型与内容路径已判定）
- [ ] Step 2 Research Log 完整
- [ ] 已阅读对应类型的章节结构

---

## 内容路径（按类型）

| 类型 | 正文路径 | 路由 |
|------|---------|------|
| Tools（新文） | `content/blog/zh/{slug}.md` | `/blog/{slug}` |
| SEO | `content/seo/zh/{slug}.md` | `/seo/{slug}` |
| Marketing | `content/marketing/zh/{slug}.md` | `/marketing/{slug}` |
| Insights | `content/insights/zh/{slug}.md` | `/insights/{slug}` |

Meta/Config 注册到对应 `*-meta.ts` / `*-pages-config.ts`（Step 4）。

---

## Frontmatter 骨架

```yaml
---
title: "H1 标题（不写年份）"
description: "三段式摘要"
slug: "{slug}"
date: "2026年7月16日"
updated: "2026年7月16日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/{channel}/{slug}"
locale: "zh"
category: "marketing"
categorySecondary: ""
heroImage: "/blog/{slug}/hero.jpg"
heroImageAlt: "…"
# heroHtml: |          # Marketing 可选，与 heroImage 二选一
#   <div>…</div>
---
```

- `pageUrl` 须与频道一致（`/zh/blog/`、`/zh/seo/`、`/zh/marketing/`、`/zh/insights/`）
- `category`：12 统一分类 ID；Blog 新文的 Hub 归属由此推导（**非** config 里的 `routeCategory`）

---

## 正文区块

使用 `<!-- block:section -->` / `<!-- block:html -->`。TL;DR / FAQ / References 写入集中 JSON（键 = `pageUrl` 路径）。

### Tools 型（新 Blog 文）

复用 `create-tools-article` 10 节结构；HowTo = 正文 `## 如何选择…` section（**禁止** frontmatter `howTo:`）。

### Marketing 型

概念 section → 策略 sections → 场景 → 结论；可选 `heroHtml` frontmatter。

### SEO 型

概念 → 操作 sections（H3 subSections）→ 场景 → 结论；代码/表格用 `html` block。

### Insights 型

主体可用大段 `html` block（`prose` class）或 section 组合 + 结论 section。

---

## 写作原则

> **知识块是非线性笔记，文章需改写为叙事线。**

- BLUF：TL;DR 先给结论；每 H2 首段先答后证
- FAQ 首句即答；**7 问**（Tools/Blog/SEO/Marketing 线上标准）
- 避免 AI 腔模板句

---

## 内链初稿

见 [`create-tools-article/02c-internal-links-drafting.md`](../create-tools-article/02c-internal-links-drafting.md)。

验收：`python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --violations-only`

---

## 输出清单

- [ ] 中文 md 已创建（正确 content 子目录）
- [ ] frontmatter 完整；**无** `howTo:`
- [ ] TL;DR / FAQ（7 问）/ References 已写入集中 JSON
- [ ] 结论 section 在 FAQ 之前（正文顺序）
- [ ] `npm run verify:content-json` 通过

---

*03-article-structure · v2.0 · 2026-08-23*
