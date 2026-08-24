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
| **FAQ** | `## FAQ` — ≥3 个 `###` 问答；首句即答；**必须为全文最后一个 H2** |
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
- Clink 正文占比 ≤15%；定义与计算章节不出现产品
- 深度节按术语定制：计算工作示例 / 决策表 / 陷阱清单
- 与已有 blog canon（what-is-clink 等）互链 ≥2；本簇 glossary 互链 ≤3

---

## 4. Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: "2026-07-XX"
updated: "2026-07-XX"
category: "Product | Comparison | Opinion | Glossary"
author: "Clink Team"
image: /blog/images/{slug}.jpg   # 可选：不生成 OG 图时可省略
readingMinutes: 12
---
```

| 字段 | 规则 |
|------|------|
| title | 45–70 chars 优先（硬上限 90）；含 primary keyword |
| description | 120–160 chars 优先（硬上限 280） |
| category | Product \| Comparison \| Opinion \| Glossary |
| image | `/blog/images/{slug}.jpg`；**可选**——不生成 OG 图时省略 |
| keywords / related / disclosure | **禁止** |

---

## 5. 文件名

`clink/blog/NN-{slug}.md` — NN 两位递增，下一号见 `content-graph.md`。

---

*article-types · v1.1.0 · 2026-07-21*
