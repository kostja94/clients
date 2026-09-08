# Clink — Article Types Reference

> 加载时机：Phase 0（路由）· Phase 2（Slug）· Phase 3（Outline）
> 主文件：SKILL.md §2 指针

---

## 1. 类型路由表

| 类型 | 路由信号 | category | 增长职能 | 词数 | Clink 占比 | 默认 Mode | 样稿 |
|------|---------|----------|---------|------|:---:|------|------|
| **BrandIntroduction** | what is clink / 品牌 hub | Product | CategoryPOV | 2500–3500 | ≤30% | flagship | what-is-clink |
| **Comparison** | X vs Y / MoR vs PSP / 选型框架 | Comparison | EvaluationComparison | 2500–3500 | ≤35% | flagship | mor-vs-psp |
| **Product** | routing / retry / churn / how-to | Product | SearchCapture | 2200–3200 | ≤40% | standard | smart-routing; how-to-add-payments-lovable-app |
| **Opinion** | agent economy / orchestration POV | Opinion | CategoryPOV | 2000–2800 | ≤35% | standard | agent-payments |
| **EvaluationComparison** | clink vs stripe / alternative | Comparison | EvaluationComparison | 2500–3500 | ≤45% | flagship | clink-vs-stripe |
| **GlossaryTerm** | `what is` + 财务/计费指标术语 | Glossary | SearchCapture | 2200–3200 | ≤15% | standard | burn-rate; annual-recurring-revenue |
| **IndustryNews** | 行业收购/发布/基础设施事件 | Industry News | CategoryPOV | 2000–2800 | ≤25% | standard | stripe-openrouter-acquisition |
| **StripeRisk** | Stripe 账户限制/申诉/风控 | Stripe Risk | SearchCapture | 2200–3200 | ≤30% | standard | stripe-account-suspended |

**自动路由**：

- `what is` + Clink → BrandIntroduction（已有 canon → MERGE）
- `what is` + 支付概念 → Comparison
- `what is` + 财务/计费指标术语 → GlossaryTerm
- `vs` / `alternative` + 竞品名 → EvaluationComparison
- `reduce` / `how to` + payment → Product
- `orchestration` + category POV → Opinion
- Stripe + suspended / closed / appeal / risk → **StripeRisk**（`stripe-risk/`）
- agent payments / guardrails / Cloudflare Wallets → **industry-news/**（15）或 agentic-payments Hub（04）
- `what is` + agent 协议（AP2 / x402 / MPP / ACP / UCP）→ **Protocol Definition**（`agentic-payments/`，secondaryCategory Research）
- `supported list` / `merchant stack` / `channels` → **Reference List**（`agentic-payments/`，secondaryCategory Research）
- `how to sell on` + 渠道 → **Merchant How-To**（`agentic-payments/`，secondaryCategory HowTo）→ 模板见 §3「AgenticPayments 簇内类型」
- skill marketplace → 根目录 Product（16–17）
- 行业收购/基础设施发布 → **industry-news/**（如 15, 18）

---

## 2. 全类型通用模块

| 模块 | 要求 |
|------|------|
| **Frontmatter** | title, description, slug, date, updated, category, author, image；可选 readingMinutes |
| **禁止字段** | `keywords` · `related` · `disclosure`（不得写入 frontmatter） |
| **TL;DR** | `## TL;DR` — 3–5 bullets；bullet 1 含核心结论 |
| **H2** | **描述性标题，不编号** |
| **分隔** | 大节之间可用 `---` |
| **正文收束** | 倒数第二个 H2 必须为 **`## Conclusion`**（CTA / thesis / 选型收束写在此节） |
| **FAQ** | `## FAQ` — **固定 6 题** `###` 问答；首句即答、内容相关（非通用模板题）；**必须为全文最后一个 H2** |
| **内链** | 正文 blog 互链 ≥2（Markdown 链接，不靠 frontmatter） |
| **外链** | 权威 2–6 |
| **CTA** | Contact Sales / docs；≤2 次；写在 Conclusion（或更早正文）中 |

---

## 3. H2 模板

### BrandIntroduction

```
## TL;DR
## The Fragmentation Tax: Why Global SaaS Payments Stay Broken
## What Clink Actually Does
## The Four Products
## Who Already Uses Clink
## What Makes Clink Different
## The Agent Economy Bet
## How to Get Started
## Conclusion
## FAQ
```

### Comparison

```
## TL;DR
## The Architecture Difference
## The Decision Framework
## What Nobody Tells You About {Side A}
## What Nobody Tells You About {Side B}
## The Third Option: Unified Payment Infrastructure
## How to Decide: A Step-by-Step Playbook
## Case Study: The "Hybrid" Pattern
## Conclusion
## FAQ
```

### Product

```
## TL;DR
## {Problem / Why It Matters}
## {Path or Mechanism sections}
## Decision Framework
## Step-by-Step / How to Tell If You Need X
## Common Pitfalls（可选）
## Conclusion
## FAQ
```

### Opinion

```
## TL;DR
## {Narrative hook}
## Why Traditional Approaches Fail
## Requirements / Framework
## Product angle（若相关）
## Market Signal
## Conclusion
## FAQ
```

### EvaluationComparison

```
## TL;DR
## Why Teams Compare Clink and {Competitor}
## Architecture
## Feature Comparison
## When Clink Is the Better Fit
## When {Competitor} Is the Better Fit
## Migration Path
## Conclusion
## FAQ
```

---

### AgenticPayments 簇内类型（category: Agentic Payments + secondaryCategory）

用于 `agentic-payments/` 子簇。frontmatter 一律 `category: "Agentic Payments"` + `secondaryCategory`（见 §4）。内链仍走 `/blog/{slug}`。

**Protocol Definition（secondaryCategory: Research；26–29, 33 系列）**：

```
## TL;DR
## What Is {Protocol}? — A Working Definition
## How {Protocol} Works: {Mandates / Flows / Key Mechanisms}
## {Key Constraint}: Human Present vs Human Not Present
## Who Built {Protocol} and Who Supports It
## Where {Protocol} Sits in the Agent Payments Stack
## {Protocol} vs x402 / MPP / ACP — One-Line Differences
## What {Protocol} Means for SaaS and API Businesses
## Conclusion
## FAQ
```

> 全簇协议互为 canonical——禁止在单篇展开 stack 全表（见 content-graph Canonical Registry）；互链 ≥2（hub + 相邻协议 + reference lists 34–36）。

**Reference List（secondaryCategory: Research；34–36 系列）**：

```
## TL;DR
## What Is the {Scope} in Agentic Commerce?
## How to Read This List
## {Scope} — MAIN TABLE
## Platform / Category Dimensions
## {Segment A} vs {Segment B} vs {Segment C}
## Common Mistakes
## What This List Does Not Cover
## Conclusion
## FAQ
```

> 数据纪律：每行标 as-of 日期 + 验证状态；`How to Read This List` 说明判定标准与更新频率；边界节（Not Cover）必需。

**Merchant How-To（secondaryCategory: HowTo；31 系列）**：

```
## TL;DR
## What "Sell on {Channel}" Means in {Year}
## Pick Your Path in Thirty Seconds
## {Path A}: {Merchant Type}
## {Path B}: {Merchant Type}
## {Path C}: {Merchant Type}
## Fees, MoR, and What Changed About {Narrative}
## Week-One Checklist (Every Merchant)
## Common Mistakes
## Conclusion
## FAQ
```

> Fee/MoR 表述守 C2：as-of + 限定语 + Contact Sales；不写无来源具体费率（C1）。

### GlossaryTerm

**叙事弧线**：定义 → 边界/计算 → 动机 → 财务场景 → 深度（案例/陷阱）→ 结论。教育优先；Clink 仅 FAQ 前 ≤3 段。

```
## TL;DR
## What Is {Term}? — A Working Definition
## How to Calculate {Term}
## {Term} vs {Related Metric A} vs {Related Metric B}
## Why {Term} Matters for Subscription Businesses
## Common Misconceptions About {Term}
## How {Term} Connects to {Billing / Payment Infrastructure}（可选，≤3 段 Clink）
## Conclusion
## FAQ
```

**GlossaryTerm 特有约束**：
- category 固定 `Glossary`（D4）
- **slug 用纯术语全称 kebab-case，不加 `what-is-` 前缀、不用缩写**（`burn-rate`、`annual-recurring-revenue`、`monthly-recurring-revenue`、`net-revenue-retention`、`runway`）；标题仍保留 "What Is {Term}?" 可读形式
- Clink 正文占比 ≤15%；定义与计算章节不出现产品（教育优先）
- **客观权威**：承认 Carta / Stripe / Investopedia 等既有定义，不贬低（Wirecutter 式）
- 深度节按术语定制：计算工作示例 / 决策表 / 陷阱清单
- 与已有 blog canon（what-is-clink 等）互链 ≥2；本簇 glossary 互链 ≤3
- **指标簇闭环**：财务术语互相成簇互链，并向 blog canon（smart-routing 等）输送流量（见 content-graph Glossary 簇）
- P0 数字有来源或 as-of；不写无来源的 Clink 费率（C1）

---

## 4. Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: "2026-07-XX"
updated: "2026-07-XX"        # 仅实质性内容更新时写；必须 ≥ date
category: "Product | Comparison | Opinion | Glossary | Agentic Payments | Stripe Risk | Industry News"
secondaryCategory: "Guide | Research | Opinion | HowTo | Product"   # 仅 cluster 双分类文
author: "Clink Team"
readingMinutes: 10
---
```

| 字段 | 规则 |
|------|------|
| title | 45–70 chars 优先（硬上限 90）；含 primary keyword |
| description | 120–160 chars 优先（硬上限 280） |
| date | 发布时间，**永不改变**；每自然日 ≤1 篇（见 content-graph 日期表） |
| updated | 可选；仅实质性更新时加，且**不得早于 date**；页面只显示最近一个日期 |
| category | 见 SKILL.md §4 集群表；根目录文用 Product / Comparison / Opinion / Glossary |
| secondaryCategory | **仅 cluster 双分类文**（Agentic Payments / Stripe Risk / Industry News 主类 + 次类 Research / HowTo / Guide / Opinion / Product） |
| image | **已停用（2026-08-11）**——不写入 frontmatter；封面由 OG 流程单独管理 |
| keywords / related / disclosure | **禁止** |

---

## 5. 文件名

`clink/blog/NN-{slug}.md` — NN 两位递增，下一号见 `content-graph.md`。

---

*article-types · v1.2.0 · 2026-09-08 · 新增 Agentic Payments 簇 Research/HowTo 用例 · FAQ 固定 6 题 · image 停用*
