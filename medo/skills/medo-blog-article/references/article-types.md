# MeDo Blog 文章类型、H2 模板与 Frontmatter

> Agent 在 Phase 2（Frontmatter）、Phase 3（Outline）、Phase 4（Draft）前加载。

---

## 1. 路由总表

| 类型 | MeDo category | 典型 intent | 词数 | 产品提及 | 正文政策 as-of |
|------|---------------|-------------|------|----------|---------------|
| **PillarTutorial** | Tutorial | how to build… | 2800–4000 | ≤35% | 可选 |
| **GlossaryGuide** | Guide | what is… | 1800–2800 | ≤20% | 否 |
| **Comparison** | Guide | best… | 2200–3200 | ≤40% | 否 |
| **PublishGuide** | Tutorial | publish… | 2200–3000 | ≤35% | **必填** |
| **Alternative** | Guide | vs / alternative | 2000–2800 | ≤45% | 否 |
| **DecisionGuide** | Guide | vs / cost / free | 1800–2600 | ≤30% | 可选 |
| **UseCase** | Tutorial / Case Study | build X app | 1500–2500 | ≤50% | 否 |
| **Diagnosis** | Tutorial | rejection / fix | 2000–2800 | ≤25% | **必填** |
| **Announcement** | Guide | 产品发布/更新 | 1200–1800 | 不限 | 可选 |

**产品提及**：正文中 MeDo 名称 + 功能描述 + CTA 合计篇幅占比上限（非严格计数，Phase 5 目测）。

> **正文政策 as-of**：PublishGuide / Diagnosis 须在正文含 `as of {month} {year}` 时效声明（A2 Gate），由正文承载，不入 frontmatter。

---

## 2. Frontmatter Schema

```yaml
---
title: "..."
description: "..."
slug: "..."
date: 2026-06-XX       # 发布时间，永不改变
updated: 2026-06-XX    # 可选；最近一次实质性内容更新；无更新则省略
author: "Kostja"
category: "Tutorial"
secondary_category: "Mobile App"
---
```

> **2026-08-14 起**：正文不设 `## Related articles` 区块；内链全部为上下文内链。`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords 由正文与 CMS 配置承载；related 已取消）。
>
> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

### 字段详解

| 字段 | 规则 |
|------|------|
| `title` | 45–65 chars；含主关键词；可含 2026 |
| `description` | 120–160 chars；benefit + intent |
| `slug` | 常青 kebab-case；见 slug-gate.md |
| `date` | YYYY-MM-DD |
| `author` | 默认 Kostja |
| `category` | Tutorial / Guide / Case Study |
| `secondary_category` | `Mobile App`（默认）/ `Full-stack App`（跨端功能）/ `Components`（组件主题簇）；替代原 cluster 字段 |

---

## 3. 全类型通用模块

| 模块 | 要求 |
|------|------|
| 开篇 hook | 痛点 → 2026 转折 → 本文承诺 |
| TL;DR | 紧跟 H1（正文最上方）；3–5 bullet |
| H2 编号 | `## 1.` … `## N.`；Conclusion/FAQ 不编号 |
| Conclusion | CTA → `/ai-mobile-app-builder` |
| FAQ | `## Frequently asked questions`；**固定 6 题** H3；≥1 objection；全部内容相关 |
| 内链 | 全部为**上下文内链**（正文自然嵌入，不设文末 Related articles）；≥2 blog；Spoke 链 Pillar |
| 外链 | 2–5；`rel="nofollow noopener"` |
| 三分类 | Comparison/Alternative/Decision 须含 Native/Cross-platform/Web wrapper |

---

## 4. PillarTutorial — H2 模板

| § | H2 | Words |
|---|-----|-------|
| — | TL;DR | 120 |
| 1 | What changed in {year} — and why this is suddenly possible | 350 |
| 2 | What's actually feasible (and what isn't) | 300 |
| 3 | Validate the idea before you build anything | 400 |
| 4 | Pick the right AI tool for the job | 350 |
| 5 | The {N}-step vibe coding workflow | 800 |
| 6 | What it costs in {year} | 300 |
| 7 | Five mistakes first-time builders make | 350 |
| — | Conclusion / FAQ | — |

---

## 5. GlossaryGuide — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | Where "{term}" came from | 350 |
| 2 | What {term} looks like in practice | 400 |
| 3 | How it differs from traditional coding | 300 |
| 4 | How it differs from drag-and-drop no-code | 300 |
| 5 | Why {year} is the year of mobile {term} | 350 |

---

## 6. Comparison — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | Three categories — why the distinction matters | 500 |
| 2 | Comparison table | 200 |
| 3–N | Per-tool deep dives | 1200 |
| N+1 | How to pick the right builder | 350 |

---

## 7. Alternative — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | What {A} and {B} actually are | 300 |
| 2 | Side-by-side comparison table | 200 |
| 3 | Mobile output: native vs web wrapper | 450 |
| 4 | Build, test, and ship workflow compared | 400 |
| 5 | Pricing and code ownership | 300 |
| 6 | When to choose {A} over {B} — and vice versa | 400 |

---

## 8. PublishGuide — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | Before you publish — pre-flight checklist | 450 |
| 2 | Developer accounts | 350 |
| 3 | Beta testing (TestFlight / internal track) | 400 |
| 4 | Store assets | 350 |
| 5 | Privacy, account deletion, compliance | 450 |
| 6 | Submitting and review timeline | 300 |
| 7 | Common rejections — and fixes | 400 |

---

## 9. DecisionGuide — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | Why this decision matters | 300 |
| 2 | Option A explained | 350 |
| 3 | Option B explained | 350 |
| 4 | Decision table in prose | 300 |
| 5 | Cost breakdown (if applicable) | 400 |
| 6 | Recommendation by persona | 350 |

---

## 10. UseCase — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | Why {app type} is a good first AI app | 250 |
| 2 | Define the core loop | 300 |
| 3 | Build step by step | 600 |
| 4 | Test and iterate | 300 |
| 5 | Optional publish path | 250 |

---

## 11. Diagnosis — H2 模板

| § | H2 | Words |
|---|-----|-------|
| 1 | Why AI-built apps get rejected more often | 350 |
| 2–5 | Four rejection reasons + fixes | 1400 |
| 6 | Resubmission checklist | 300 |

---

## 12. Voice 速查

| 正向 | 禁止 |
|------|------|
| 非开发者友好 | revolutionary / guaranteed |
| 诚实边界 | only platform / unbeatable |
| Wirecutter 式 | just / merely 贬低竞品 |
| 可执行步骤 | click here |
