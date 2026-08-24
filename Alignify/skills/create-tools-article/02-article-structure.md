# Step 2 — 创建中文文章（Markdown + 集中 JSON）

> **前置条件**：Step 1 完成；Step 2a 截图已落盘（Best Ranking 文章）
> **产出**：`content/blog/zh/{slug}.md` + `tldr-data.json` / `faq-data.json` / `references-data.json` 对应键
> **HowTo（2026-08-23）**：仅正文 `## 如何选择…` + `###` 步骤；**禁止** frontmatter `howTo:`。规范：`E:/clients/Alignify/content/sections/section-how-to.md`
> **参照**：[`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md)、[`references/product-screenshot-pages.md`](./references/product-screenshot-pages.md)

---

## 2.1 准备工作

### 阅读以下文件（仅限本节需要）

| 文件 | 阅读重点 |
|------|---------|
| `content/templates/template-tools.md` | §一（页面结构）、§五（各章节规范） |
| `knowledge/tools/{slug}.md` | 知识块全文——提取产品数据、词汇定义、竞品对比 |
| `content/sections/section-tldr.md` | TL;DR 格式 |
| `content/sections/section-best-tools.md` | Best 榜单正文 section 规范 |
| `content/sections/section-faq.md` | FAQ 规范（`faq-data.json`） |

**禁止**：从知识块直接复制段落到文章。知识块是非线性笔记体例，文章需要按叙事线重组。

---

## 2.2 创建 Markdown 文件

### 文件位置
```
content/blog/zh/{slug}.md
```

### 参考已有文章
建议先 Read 结构相似的已有 Blog Markdown：
- `content/blog/zh/web-fetch.md`（Best Ranking + 产品截图）
- `content/blog/zh/agent-sandbox.md`

### Best Ranking Meta（frontmatter + blog-meta.ts）
- **Meta title**（`blog-meta.ts`）：必须含「**最佳**」+ `（2026）` + 冒号副线 + 列举代表产品
- **Meta description**：以「探索2026年最佳…」开头，列举 2–3 个产品名
- **H1**（frontmatter `title`）：**不含**「最佳」与年份
- **Best 榜单 H2**：`## 2026 年最好的 {品类} {#best-...}`

---

## 2.2b 产品截图（Step 2a 详规）

见 [`references/product-screenshot-pages.md`](./references/product-screenshot-pages.md)。

**硬规则**：截图 URL = 该条目介绍的产品/能力页。多产品厂商（如 Cursor IDE + Origin）**禁止**统一截首页。

```markdown
![Cursor Origin 文档页截图](/blog/git-hosting/cursor-origin.jpg)
```

部署仓脚本：`scripts/permanent/capture-blog-screenshots.py --slug {slug}`

---

## 2.3 Frontmatter + 正文骨架

完整 10 节映射见 [`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md)。

```yaml
---
title: "{工具类型}：{核心价值}"
description: "三段式摘要…"
slug: "{slug}"
date: "2026年6月23日"
updated: "2026年6月23日"
readingMinutes: "18 分钟阅读"
pageUrl: "https://alignify.co/zh/blog/{slug}"
locale: "zh"
category: "coding-dev"
heroImage: "/blog/{slug}/hero.jpg"
heroImageAlt: "…"
---

<!-- block:section -->
## 什么是 {工具类型} {#section-1}
…

<!-- block:section -->
## {工具类型}是如何工作的 {#how-it-works}
…

<!-- block:section -->
## 2026 年最好的 {分类} {#best-{slug}-2026}
### 产品名 {#product-slug}
…

<!-- block:section -->
## 如何选择 {品类} {#how-to-choose-{slug}}
### 步骤1 {#step-1}
…

<!-- block:section -->
## 结论 {#conclusion}
…
```

TL;DR / FAQ / References 写入 `src/data/tldr-data.json`、`faq-data.json`、`references-data.json`（键 = `pageUrl` 路径）。

### `category` 字段
frontmatter `category` 为 12 统一分类 ID（见 `src/data/category-config.ts`）。驱动 Hub 归属；**非** config 中的 `routeCategory`。

---

## 2.4 从知识块提取内容

### TL;DR 怎么写
从知识块的「问题域」和「对比与测评」中提取 4–5 条核心发现，改写为一句话要点。每条 8–25 字。

**内链**：TLDR intro **0–1 条**站内链（Hub 页建议 0 链、纯文本列子品类）；items 不放链。邻居链从「什么是」第二段起首次出现。见 [`02c-internal-links-drafting.md`](./02c-internal-links-drafting.md)。

### 什么是 XXX 怎么写
从知识块的「词汇锚点」第一条改写——删去英文术语加粗格式，转为叙事段落。可引用知识块中的市场规模数据。

### 如何工作怎么写
从知识块的「能力栈」提取概念拆分，重组为面向读者的技术概述。知识块的能力栈是概念架构，文章需要解释"这些概念对用户意味着什么"。

### Best 榜单（正文 section）怎么写
从知识块的「外链索引」提取产品名称、URL 和一句话描述，扩充为包含核心定位、关键差异、最佳适用场景的完整条目。**需要联网验证当前定价和功能描述**。

### 对比表格怎么写
从知识块的「工具与产品类型表」提取分类，简化为一页对比。

### FAQ 怎么写
从知识块的「词汇锚点」、「问题域」、「风险合规」中提取读者最可能搜索的问题。**FAQ 答案为独立撰写，不复制正文**。

### 如何选择（正文 section）怎么写

五步采购决策树，对齐 `content/sections/section-how-to.md`（**正文 only，无 frontmatter howTo:**）：

1. H2：`## 如何选择 {品类} {#how-to-choose-{slug}}`
2. intro 段：选型框架（可 1 条内链）
3. 3–5 个 `###` 步骤标题 + 段落（中文每步 ≥80 字；写评估维度、可执行动作、失败信号）
4. 标杆：`content/blog/zh/web-fetch.md`、`content/tools/zh/text.md`

> 旧 JSON `howToChoose` block 与 frontmatter `howTo:` **已废弃**（2026-08-23）。

---

## 2.5 内容质量要求

### 每个产品描述必须包含
1. **核心定位**：这个工具是什么、解决什么问题（第 1 段）
2. **关键差异**：与同类比它独特在哪（第 2 段）
3. **最佳适用场景**：谁应该用它、什么时候用它（第 3 段）

### 禁止
- 空洞副词（"非常强大""极其优秀"）
- 万能结尾（"总之这是一个很好的工具"）
- 从知识块直接复制段落
- 产品描述仅罗列功能名

---

## 2.6 Step 2 完成检查

- [ ] `npm run verify:content-json` 通过；frontmatter **无** `howTo:`
- [ ] frontmatter `title` 不含年份；`description` / excerpt 三段式
- [ ] 10 节 section 顺序正确（结论在 FAQ 前）
- [ ] TL;DR / FAQ / References 已写入对应 `src/data/*-data.json`
- [ ] FAQ **7 问**；FAQ 答案无内链
- [ ] Best 产品段字数达标（ZH ≥100 字 / EN ≥280 字符）
- [ ] HowTo：`## 如何选择` + 3–5 个 `###` 步骤（见 `section-how-to.md`）

---

*02-article-structure · v3.0 · 2026-08-23*
