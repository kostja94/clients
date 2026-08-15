# Step 2 — 创建中文文章 JSON

> **前置条件**：Step 1 完成（关键词 + README 已注册）
> **产出**：`content/blog/zh/{slug}.json`
> **参照**：[`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md)、[`references/section-word-counts.md`](./references/section-word-counts.md)、[`references/common-errors.md`](./references/common-errors.md)

---

## 2.1 准备工作

### 阅读以下文件（仅限本节需要）

| 文件 | 阅读重点 |
|------|---------|
| `content/templates/template-tools.md` | §一（页面结构）、§五（各章节规范） |
| `knowledge/tools/{slug}.md` | 知识块全文——提取产品数据、词汇定义、竞品对比 |
| `content/sections/section-tldr.md` | TL;DR 格式 |
| `content/sections/section-best-tools.md` | BestTools 组件规范 |
| `content/sections/section-faq.md` | FAQ 规范（§3.2 Tools JSON FAQ） |

**禁止**：从知识块直接复制段落到文章。知识块是非线性笔记体例，文章需要按叙事线重组。

---

## 2.2 创建 JSON 文件

### 文件位置
```
content/blog/zh/{slug}.json
```

### 参考已有文章
建议先 Read 一个结构相似的已有 Blog 文章作为格式参考：
- `content/blog/zh/data-engineering-agent.json`
- `content/blog/zh/github-for-marketing.json`

---

## 2.3 JSON 结构骨架

```json
{
  "category": "coding-dev",
  "blogLayout": {
    "title": "H1：不写年份，推荐「类型：核心价值」格式",
    "excerpt": "三段式摘要，中文约 80–150 字，避免通用结尾",
    "readTime": "XX 分钟阅读",
    "pageUrl": "https://alignify.co/zh/blog/{slug}"
  },
  "blocks": [
    { "type": "tldr", "id": "article-intro", "title": "核心要点", "introduction": "...", "items": ["...","...","...","..."] },
    { "type": "section", "title": "什么是 {工具类型}", "paragraphs": ["...","..."], "children": [] },
    { "type": "howItWorks", "id": "how-{slug}-work", "title": "...", "technologyBase": "...", "advantages": [...], "architectureDifferences": "..." },
    { "type": "bestTools", "id": "best-{slug}-2026", "title": "2026 年最好的 {分类}", "introduction": "...", "tools": [{"id": "...", "name": "...", "shortDescription": "...", "imageSrc": "...", "imageAlt": "...", "linkUrl": "https://...", "description": "..."}] },
    { "type": "comparisonSection", "h2Text": "{工具类型}对比", "introHtml": "...", "table": { "items": [{"toolName": "...", "coreFeatures": "...", "bestFor": "...", "pricing": "..."}] } },
    { "type": "useCases", "id": "use-cases", "title": "...", "introduction": "...", "useCases": [{"id": "...", "title": "1. ...", "description": "..."}] },
    { "type": "howToChoose", "id": "how-to-choose-{slug}", "title": "如何选择 {AI} {工具类型}", "introduction": "...", "steps": [{"id": "...", "title": "...", "description": "..."}] },
    { "type": "section", "title": "结论", "paragraphs": ["...","..."] },
    { "type": "faq", "items": [{"question": "...?", "answer": "..."}] },
    { "type": "references", "items": [{"title": "...", "url": "https://..."}] }
  ]
}
```

### 各 section 详细规范
见 [`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md) — 完整 JSON 字段结构。

### `category` 字段
JSON 顶层 `"category"` 用于内部路由区分。枚举与部署仓 `src/data/tools-pages-config.ts` 中的 `ToolsCategory` 一致（**创建前 Read 源文件**）。Tools 型文章常用 `"coding-dev"`、`"search-web"`、`"llms"` 等；营销类长文可用 `"marketing"`。

---

## 2.4 从知识块提取内容

### TL;DR 怎么写
从知识块的「问题域」和「对比与测评」中提取 4–5 条核心发现，改写为一句话要点。每条 8–25 字。

**内链**：TLDR intro **0–1 条**站内链（Hub 页建议 0 链、纯文本列子品类）；items 不放链。邻居链从「什么是」第二段起首次出现。见 [`02c-internal-links-drafting.md`](./02c-internal-links-drafting.md)。

### 什么是 XXX 怎么写
从知识块的「词汇锚点」第一条改写——删去英文术语加粗格式，转为叙事段落。可引用知识块中的市场规模数据。

### 如何工作怎么写
从知识块的「能力栈」提取概念拆分，重组为面向读者的技术概述。知识块的能力栈是概念架构，文章需要解释"这些概念对用户意味着什么"。

### BestTools 怎么写
从知识块的「外链索引」提取产品名称、URL 和一句话描述，扩充为包含核心定位、关键差异、最佳适用场景的完整条目。**需要联网验证当前定价和功能描述**。

### 对比表格怎么写
从知识块的「工具与产品类型表」提取分类，简化为一页对比。

### FAQ 怎么写
从知识块的「词汇锚点」、「问题域」、「风险合规」中提取读者最可能搜索的问题。**FAQ 答案为独立撰写，不复制正文**。

### 如何选择（howToChoose）怎么写
五步采购决策树，对齐 `HowToChoose.tsx` 字段（见 [`references/tools-article-anatomy.md`](./references/tools-article-anatomy.md) §7）：
1. block 级 `id`（`how-to-choose-{slug}`）+ `introduction`（选型框架，可内链）
2. 每步 **`id` + `title` + `description`**——**禁止 `name`**
3. 中文每步 description ≥80 字：写评估维度、可执行动作、失败信号；勿写「A→B」一句 stub
4. 标杆：`content/tools/zh/web-search-api.json`、`content/blog/zh/web-fetch.json`（已修复版）

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

- [ ] JSON 格式有效（可用 `jq .` 或 IDE 验证）
- [ ] blogLayout.title 不含年份
- [ ] blogLayout.excerpt 三段式（中文 80–150 字）、不出现通用结尾
- [ ] 10 个 section 按顺序排列（Conclusion 在 FAQ 前）
- [ ] 每个 section 的 type 与组件匹配
- [ ] FAQ 8 问；Tools/Blog JSON 的 FAQ 内链符合 §1.5（全文唯一、FAQ ≤3 slug）
- [ ] BestTools 字数达标（见字数速查表）
- [ ] howToChoose：block `id` + `introduction` + 5 步；每步 `id`/`title`/`description`（**禁止 `name`**）；中文每步 description ≥80 字

---

*02-article-structure · v2.0 · 2026-06-23*
