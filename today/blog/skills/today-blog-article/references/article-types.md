# Today AI Blog — 文章类型、H2 模板与 Frontmatter

> Agent 在 Phase 2（Frontmatter）、Phase 3（Outline）、Phase 4（Draft）前加载。

---

## 1. 路由总表

| 类型 | category | 典型 intent | 词数 | 产品占比 | 默认 Mode |
|------|----------|-------------|------|----------|-----------|
| **BrandPillar** | Product | what is Today / proactive AI | 2500–3500 | ≤40% | flagship |
| **GlossaryGuide** | Guide | what is living memory… | 1800–2600 | ≤20% | standard→flagship |
| **Comparison** | Guide | best AI assistant / Today vs X | 2200–3200 | ≤45% | flagship |
| **Alternative** | Guide | X alternative with memory | 2000–2800 | ≤45% | flagship |
| **UseCase** | Tutorial | AI assistant for founders | 1500–2500 | ≤50% | standard |
| **HealthcareGuide** | Guide | ai meal planner / sleep coach | 2200–3000 | ≤35% | flagship |
| **HowTo** | Tutorial | how to use morning brief | 1800–2600 | ≤40% | standard |
| **Opinion** | Opinion | proactive vs reactive | 1500–2200 | ≤25% | standard |
| **Announcement** | Product | Beta launch / feature | 800–1400 | 不限 | lite |

**产品占比**：正文中 Today 名称 + 功能 + CTA 合计篇幅上限（Phase 5 目测）。

**HealthcareGuide**：全文须过 T1 Gate +  lifestyle 免责。

---

## 2. Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars, benefit + primary keyword"
slug: "kebab-case-evergreen-no-year"
date: YYYY-MM-DD
author: "Today Team"
category: "Product | Guide | Tutorial | Opinion"
secondary_category: "Proactive | Memory | Comparison | Use Cases | Healthcare"
---
```

> **禁止** frontmatter 字段：`keywords`、`related`、`image`、`disclosure`
>
> **日期**：`date` = 发布时间永不改；`updated` 仅实质性更新时加。

### 字段规则

| 字段 | 规则 |
|------|------|
| `title` | 45–65 chars；含主关键词 |
| `description` | 120–160 chars |
| `slug` | 常青 kebab-case；见 slug-gate.md |
| `author` | 默认 Today Team |
| `category` | Product / Guide / Tutorial / Opinion |
| `secondary_category` | 集群归属：Proactive / Memory / Comparison / Use Cases / Healthcare |

---

## 3. 全类型通用模块

| 模块 | 要求 |
|------|------|
| TL;DR | 3–5 bullet；bullet 1 = snippet 定义句（40–60 词） |
| H2 | 编号 `## 1.` … `## N.`；Conclusion/FAQ 不编号 |
| Conclusion | CTA → `/waitlist` 或 `/downloads` |
| FAQ | `## Frequently asked questions`；**4–6 题** H3；≥1 objection |
| 内链 | 上下文内链 ≥2 blog；Spoke 链 Hub；禁 Related articles 区块 |
| 外链 | 2–5；竞品 `rel="nofollow noopener"` |
| CTA | ≤2 次 |

---

## 4. BrandPillar — H2 模板

| § | H2 | Words |
|---|-----|-------|
| — | TL;DR | 120 |
| 1 | What {concept} means in 2026 | 350 |
| 2 | Why reactive assistants fall short | 400 |
| 3 | How Today approaches {concept} | 500 |
| 4 | What it looks like in daily life | 450 |
| 5 | Who this is for (and who it is not) | 350 |
| Conclusion | — | 150 |
| FAQ | 4–6 题 | 400 |

---

## 5. Comparison — H2 模板

| § | H2 | Words |
|---|-----|-------|
| — | TL;DR | 120 |
| 1 | What you are comparing (and why it matters) | 300 |
| 2 | Quick comparison table | 200 |
| 3 | {Product A} — strengths and limits | 450 |
| 4 | {Product B} — strengths and limits | 450 |
| 5 | Side-by-side on memory, proactive, execution | 500 |
| 6 | When to choose each option | 400 |
| Conclusion | — | 150 |
| FAQ | 4–6 题 | 400 |

**必填**：每竞品 ≥1 优势；≥1「When X is the better choice」段。

---

## 6. HealthcareGuide — H2 模板

| § | H2 | Words |
|---|-----|-------|
| — | TL;DR + lifestyle disclaimer | 150 |
| 1 | The problem with tracking without action | 350 |
| 2 | What a lifestyle health assistant does | 400 |
| 3 | How Today uses signals (not diagnoses) | 450 |
| 4 | Example workflows | 450 |
| 5 | Boundaries and what this is not | 300 |
| Conclusion | → /waitlist + /healthcare spoke | 150 |
| FAQ | 4–6 题含合规 | 450 |

**T1**：禁诊断词；FAQ 须含「Is this medical advice?」类题。

---

## 7. word_count_narrative.py intent 映射

| ArticleType | --intent 参数 |
|-------------|--------------|
| BrandPillar | brandpillar |
| GlossaryGuide | glossaryguide |
| Comparison | comparison |
| Alternative | alternative |
| UseCase | usecase |
| HealthcareGuide | healthcareguide |
| HowTo | howto |
| Opinion | opinion |
| Announcement | announcement |

*article-types · v1.0 · 2026-09-01*
