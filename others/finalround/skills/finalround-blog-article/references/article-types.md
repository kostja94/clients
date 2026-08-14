# FinalRound Article Types（Skill reference）

> **7 类文章路由 + H2 模板 + Slug + Frontmatter。** Phase 0 加载路由表；Phase 3/4 加载模板。

---

## 1. 路由表

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | category |
|------|--------|------|:---:|:---:|------|
| **Announcement** | 产品发布/更新 | 1200–1800 | 不限 | lite | Product |
| **Review** | 竞品评测 | 1500–2500 | ≤45% | flagship | Comparison |
| **Alternative** | 竞品替代/VS | 2000–3000 | ≤50% | standard | Comparison |
| **CommercialRoundup** | best X / 工具选型 | 2500–3500 | ≤45% | flagship | Comparison |
| **InterviewPrep** | how to / 面试准备 | 1800–2600 | ≤35% | standard | Product |
| **ResearchDefinition** | what is / 术语/概念 | 1800–2800 | ≤25% | standard | Research |
| **Industry** | 行业趋势/新闻 | 2000–3000 | ≤30% | standard | Research |

**路由规则**：

- `best` + 品类/工具 → **CommercialRoundup**
- `{competitor} review` → **Review**
- `{competitor} alternative(s)` / `vs` + 单竞品 → **Alternative**
- `how to` + 面试/求职场景 → **InterviewPrep**
- `what is` / 概念/术语 → **ResearchDefinition**
- 裁员/招聘趋势/行业新闻 → **Industry**
- 产品发布/更新/新功能 → **Announcement**

---

## 2. 全类型通用模块

| 模块 | 要求 |
|------|------|
| **Key takeaways** | **= TL;DR**；`## Key takeaways` 为正文**第一块**（frontmatter 之后）；3–6 bullet；独立传达 ~80% 价值；bullet 1 为 snippet 定义句（40–60 词） |
| **Introduction** | **必填** `## Introduction`；Key takeaways 之后、第一个正文主题 H2 之前；≤200 words；BLUF（直接答 primary intent）+ 路线图；Introduction **首段** ≥1 内链 |
| **H1** | **禁止** Markdown `# H1` 重复 frontmatter `title`（页面 title 由 CMS 渲染）；开篇一律用 `## Introduction` |
| **H2** | 英文 `##` 标题；描述性标题，不编号（对齐官网既有文章风格） |
| **FAQ** | **固定 6 题**（2026-08-11 定标）；正文 `## FAQ` + `###` 小题或 `**Q?**` 粗体题；**全部内容相关**（基于本文已覆盖的主题），禁止通用模板题（如 "What is X?" 泛答、平台/工具通用 Q、Google helpful-content 元问题）；首句即答 |
| **内链** | Introduction 首段 ≥1；body blog 1–4；产品/场景 0–2；上下文分布 |
| **外链** | 权威 2–6；竞品/数据源 `rel="nofollow noopener"` HTML |
| **列表比例** | CommercialRoundup/Alternative ≤30%；InterviewPrep ≤35%；Research ≤25% |
| **长段落** | ≥3 段 4–8 句（80–200 词）；避免连续 3+ 短段簇 |
| **CTA** | **由独立按钮/CTA block 承载，不入正文内链**（2026-08-11 决策）；文案 Download App / Get Interview CoPilot™ / See Plans；正文提及用纯文本；**无免费试用类文案** |
| **category** | frontmatter 必填：`Product` \| `Comparison` \| `Research` |

---

## 3. 各类 H2 模板

### 3.1 Announcement（产品发布/更新）

**叙事弧线**：背景/痛点 → 更新概览 → 逐个变化 → 对用户意味着什么 → FAQ。

```
## Key takeaways
## Introduction
## The short version: what changed
## {Change 1}: …
## {Change 2}: …
## {Change 3}: …
## What this means for you
## FAQ
```

**要点**：更新稿不是新品发布稿——老用户知道能力没丢，只是形态/流程/付费方式变了。每个变化给"before → after"对比，并落到用户视角（"Dana 的例子"）。产品形态（桌面应用）、Goal、Preflight、Screen Help、Practice Interview、定价变化（无免费试用）是核心叙事单元。**避免**"SEO implication"等内部语言（F4）。

**示例 slug**：`whats-new-interview-copilot`（已发布）。

### 3.2 Review（竞品评测）

**叙事弧线**：竞品定位 → 核心功能 → 定价 → 优缺点 → 与 FinalRound 对比（1 段，自然过渡）→ 结论 → FAQ。

```
## Key takeaways
## Introduction
## Quick Verdict（含 1 句总结 + 2–3 条 pros/cons + 可选评分）
## Table of Contents（正文 ≥1,000 字时必加；锚链接）
## What Is {Competitor}?（Answer-first；官网链接）
## Key Features（3–5 个核心功能；每项含 Evidence/Proof；可含 H3）
## Specs & What You Get（平台、语言、集成、设备）
## Who {Competitor} Is For (And Who It's Not)
## Pricing & Plans（as of [date]；链至竞品定价页）
## Pros and Cons（各 3–5 条；具体可验证；承认优势）
## {Competitor} vs FinalRound（对比表 + 1–2 段；自然过渡 CTA）
## Alternatives（简短；链至 alternatives 页）
## Verdict
## FAQ
```

**要点**：
- 竞品外链 `rel="nofollow noopener"`；每竞品 ≥1 优势；客观评测，不贬低（G7）
- 「vs FinalRound」1 段自然过渡，**不**把 FinalRound 写成唯一解
- 内链：→ `/compare/final-round-ai-vs-{competitor}`（若已发布）、→ `/interview-copilot`、→ `/ai-mock-interview`
- **CTA 红线（F1）**：**禁止** "Try free / Try Final Round AI Free / no credit card"；用 Download App / Get Interview CoPilot™ / See Plans
- **Stealth 措辞（F5）**：**禁止** "100% invisible" 当主卖点；Stealth 描述为具体功能
- 字数 1,500–2,500（目标 ~2,000）；程序化生成流程、采集字段、检查清单见 `review-programmatic.md`

### 3.3 Alternative（竞品替代/VS）

**叙事弧线**：为何搜索 alternative → 竞品是什么 → 公平对比 → 按场景推荐。

```
## Key takeaways
## Introduction
## What {Competitor} Is (and Why People Search Alternatives)
## Comparison Table (Quick Routing)
## {Alternative N} — When It Fits
## How FinalRound Fits the List
## FAQ
```

**要点**：对比表前后有分析段；≥1 场景推荐非 FinalRound 方案（E-E-A-T）；竞品描述基于官方资料；每竞品 ≥1 优势。

### 3.4 CommercialRoundup（best X / 工具选型）

**叙事弧线**：input-first 分类 → 评估标准 → 分工具 trade-off → 不导向单一产品。

```
## Key takeaways
## Introduction
## A Practical Taxonomy: {Category} by Primary Use Case
## What Makes a Great {Category} (Evaluation Criteria)
## Why "Best" Depends on {Context} (Not Hype)
## Top {Tools} (2026)
## Comparison Table
## FAQ
```

**要点**：每个工具 ≥1 优势 + 限制；FinalRound 为选项之一非唯一；FinalRound 产品提及 ≤45%。

### 3.5 InterviewPrep（面试准备指南）

**叙事弧线**：痛点 → 概念/方法 → 步骤 → 工具与工作流 → 常见错误 → FAQ。

```
## Key takeaways
## Introduction
## Why {Topic} Matters More Than …
## Step 1–N: …
## Tools and Workflows for …
## Common Mistakes
## FAQ
```

**要点**：步骤/清单/最佳实践；FinalRound 自然提及作为解决方案；不每段推产品；产品提及 ≤35%。

### 3.6 ResearchDefinition（what is / 概念）

**叙事弧线**：定义 → 类型/分类 → 如何工作 → 适用边界 → 与产品关联（后半）→ FAQ。

```
## Key takeaways
## Introduction
## What Is {Concept}?
## How {Concept} Works
## Types / Formats of {Concept}
## When to Use / When Not to
## How {Concept} Applies to Interview Prep
## FAQ
```

**要点**：产品关联放在概念教学完成之后（全文后 30%），1 段 + 链 1 个最相关产品入口；产品提及 ≤25%。

### 3.7 Industry（行业趋势/新闻）

**叙事弧线**：现象 → 数据/来源 → 对求职者的影响 → 应对 → FAQ。

```
## Key takeaways
## Introduction
## What's Happening in {Trend}
## Why It Matters for Job Seekers
## How to Prepare / Respond
## FAQ
```

**要点**：数据必须有来源（G3）；行业稿可引 Reuters、BLS、公司公告等；FinalRound 提及 ≤30%。

---

## 4. Slug、Title、Description

| 项 | 规则 |
|----|------|
| **slug** | kebab-case；**不含年份**；常青 URL → `/blog/{slug}`；5–8 词，≤60 字符；含 primary keyword 完整核心词；不含内部架构词（framework/strategy/diagnosis/guide/complete） |
| **title** | editorial；可含 `(2026)`；45–65 字符 |
| **description** | 150–160 chars；读者得到什么 + 主关键词 + 行动号召（Download / See plans） |

**Title 公式示例**：

- Announcement：`What's New in {Product}: {Biggest Change}`
- Review：`{Competitor} Review 2026: Features, Pricing & Verdict`
- Alternative：`Best {Competitor} Alternatives in 2026: {Hook}`
- CommercialRoundup：`Best {Category} in 2026: {Differentiator}`
- InterviewPrep：`How to {Action} (2026)`
- ResearchDefinition：`What Is {Concept}? A {Audience} Guide`
- Industry：`{Trend} in 2026: What Job Seekers Should Know`

**Slug 反模式速查**：

| 反模式 | 错误示例 | 正确示例 |
|--------|---------|---------|
| 含年份 | `whats-new-interview-copilot-2026` | `whats-new-interview-copilot` |
| 含数量 | `top-5-ai-interview-tools` | `best-ai-interview-tools` |
| 内部架构词泄漏 | `interview-prep-framework` | `how-to-prepare-for-interviews` |
| 分类前缀沉积 | 多篇全以 `ai-interview-` 开头 | 各篇以搜索词开头 |

---

## 5. Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword + light CTA"
slug: "kebab-case-slug"
date: 2026-08-XX        # 发布时间（首次发布，永不改变）
updated: 2026-08-XX     # 可选；最近一次实质性内容更新；无更新则省略
author: "Kostja"
category: "Product"     # Product | Comparison | Research（映射 JSON-LD articleSection）
tags: ["interview-copilot", "desktop-app"]  # 3–6 个，与内容相关的关键词
reading_time: 8         # 分钟（整数），映射 JSON-LD timeRequired (PT{N}M)
---
```

**必填**：`title`、`description`、`slug`、`date`、`author`、`category`、`tags`、`reading_time`。  
**可选**：`updated`。  
**禁止**：`image`、`keywords`、`related`（2026-08-11 起从全部成稿移除；`image` 暂无封面资产暂不加入；`keywords`/`related` 由 `tags`+`category` 替代——相关文章由分类/标签聚合驱动，不手写数组；内链建议见 `internal-links.md`）。

### 5.0 category / tags / reading_time 规范（2026-08-11 加入）

| 字段 | 规则 | 映射 |
|------|------|------|
| `category` | 三选一：`Product` \| `Comparison` \| `Research`（对应 skill 文章类型路由，见 §1） | JSON-LD `articleSection`、面包屑、归档页 |
| `tags` | 3–6 个 kebab-case 词；与正文内容相关（非通用）；用于 Related 推荐聚合 | JSON-LD `keywords`、标签页 |
| `reading_time` | 正整数（分钟），按正文叙事词数估算（≈180 词/分钟） | JSON-LD `timeRequired`（ISO 8601 `PT{N}M`） |

**tags 反模式**：禁通用词（interview、AI、guide 等单篇无区分度的词）、禁超 6 个、禁大写/空格。

### 5.1 日期字段最佳实践（2026-08-11 采纳）

| 字段 | 语义 | 映射 | 更新规则 |
|------|------|------|---------|
| `date` | 首次**公开发布**时间（非创建/写稿时间） | JSON-LD `datePublished` | **永不改变** |
| `updated` | 最近一次**实质性**内容更新 | JSON-LD `dateModified` | 仅在**实质更新**（新增数据/章节/修正事实）时更新；错别字、换图、样式调整**不更新** |

**格式**：`YYYY-MM-DD`（ISO 8601 日期；如做 JSON-LD 建议补时区，如 `2026-08-11T09:00:00+08:00`）。**禁止未来日期**——必须是页面实际发布/更新时间，不能是内容所描述事件的日期。

**页面渲染规则（CTR 关键）**：
- 页面**只显示一个日期**（有 `updated` 显示它，否则显示 `date`）——**不要同时显示**两个日期。
- 依据：Search Engine Land 案例显示，同时显示 "Published + Updated" 导致 Google 显示旧日期、**CTR 掉 22%**；Google 官方建议移除页面上多余日期。
- **JSON-LD 中保留 `datePublished` + `dateModified` 两个字段**（schema 不伤 CTR，页面显示才伤）；只有 `date` 时 `dateModified` 可省略（引擎会推断等于 `datePublished`，属正常）。

**sitemap `lastmod`**：与 `updated` 一致（无 `updated` 则用 `date`）。

---

*article-types · FinalRound · 7 类 · 对齐既有 11 篇成稿；Review 程序化规范见 review-programmatic.md*
