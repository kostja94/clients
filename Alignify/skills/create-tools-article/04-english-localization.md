# Step 4 — 创建英文 Markdown

> **前置条件**：Step 2–3 完成（中文 md + blog-meta.ts + blog-pages-config.ts + 集中 JSON 就绪）
> **产出**：`content/blog/en/{slug}.md` + 集中 JSON 英文键同步
> **参照**：`content/templates/template-tools.md` §十四、[`references/section-word-counts.md`](./references/section-word-counts.md)

---

## 4.1 核心原则

- **意译，不逐句翻译**：理解中文含义后用自然英文表达
- **信息深度相当，字数不机械对齐**：英文自然比中文长 1.2–1.8×
- **本地化差异**：示例、定价、地区适用性可根据英文市场调整
- **FAQ 可不同**：英文 FAQ 可覆盖与中文不同的问题（数量保持 **7 问**，与线上一致）

---

## 4.2 创建英文 Markdown

### 文件位置
```
content/blog/en/{slug}.md
```

### 建议流程

1. **先读中文 md**：理解全文结构和信息层次
2. **复制 frontmatter 骨架**，改 locale / pageUrl / 日期展示格式
3. **逐 section 翻译**：保持 `<!-- block:section -->` 与 H2/H3 锚点 id 一致
4. **同步集中 JSON**：`tldr-data.json`、`faq-data.json`、`references-data.json` 的英文键

---

## 4.3 Frontmatter 模板

```yaml
---
title: "{Tool Type}: {Core Value Proposition}"
description: "Three-paragraph excerpt, 200–250 characters…"
slug: "{slug}"
date: "June 23, 2026"
updated: "June 23, 2026"
readingMinutes: "18 min read"
pageUrl: "https://alignify.co/blog/{slug}"
locale: "en"
category: "coding-dev"
categorySecondary: ""
heroImage: "/blog/{slug}/hero.jpg"
heroImageAlt: "…"
---
```

---

## 4.4 各章节英文注意事项

### H1（frontmatter `title`）
- 40–60 字符；不写年份
- 格式：`{Tool Type}: {Core Value Proposition}`

### Excerpt（frontmatter `description`）
- 200–250 字符；三段式

### TL;DR（`tldr-data.json`）
- introduction 30–60 词
- items 4–5 条，每条 10–25 词

### 什么是 XXX / 如何工作 / Best 榜单 / 对比 / 场景
- 均为 `<!-- block:section -->` + Markdown 段落
- 中文信息深度对等；Best 产品段 EN ≥280 字符
- 定价改用 USD、示例换英文市场案例

### 如何选择（How to Choose）
- H2：`## How to Choose {Category} {#how-to-choose-{slug}}`
- 3–5 个 `###` 步骤；每步 ≥80 词
- **禁止** frontmatter `howTo:`

### 结论
- 在 FAQ 之前（正文顺序 + 集中 JSON 注册顺序）

### FAQ（`faq-data.json`）
- **7 问**（线上标准）
- 答案 40–80 词；plain text，**无内链**

### References（`references-data.json`）
- 与中文条目对应或本地化来源

---

## 4.5 英文 vs 中文差异

| 项目 | 中文 | 英文 |
|------|------|------|
| Hero 日期展示 | `2026年6月23日` | `June 23, 2026` |
| H2 分割线 | 有 | 无，仅 `pt-8` |
| 产品定价 | 人民币示例 | USD 示例 |
| 内链文本 | 中文锚文本 | 英文锚文本 |

---

## 4.6 Step 4 完成检查

- [ ] `npm run verify:content-json` 通过
- [ ] 英文与中文 10 节顺序一致
- [ ] frontmatter `pageUrl` 无 `/zh/` 前缀
- [ ] Best 产品段 EN 字数达标
- [ ] FAQ 7 问；答案无内链
- [ ] 集中 JSON 英文键与 `pageUrl` 一致
- [ ] 英文自然流畅（非机器翻译腔）

---

*04-english-localization · v3.0 · 2026-08-23*
