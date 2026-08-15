# Oginify Article Types — Full Routing & Templates

> 加载时机：Phase 0（类型路由）· Phase 3（H2 模板）· Phase 2（slug/frontmatter）
> 主文件：SKILL.md §2 指针

---

## 1. 路由总表

| 类型 | Track | 典型 intent | 词数 | 产品提及 | 默认 Mode | 参考 slug |
|------|:---:|------------|------|:---:|:---:|-----------|
| **Ranking / Comparison** | S | best / top / compare | 2400–3400 | ≤40% | flagship | `best-ai-og-image-generators` |
| **HowTo / Tutorial** | S | how to create / add | 2000–3000 | ≤40% | standard | `how-to-create-open-graph-image` |
| **Glossary / Research** | S | what is / meaning | 2000–3200 | ≤20% | flagship | `what-is-open-graph-image`（Hub） |
| **SizeGuide / Reference** | T | size / dimensions | 1200–2000 | ≤15% | lite | `open-graph-image-size` |
| **MetaGuide** | S | meta tags / validator | 1500–2500 | ≤30% | standard | `open-graph-meta-tags-guide` |
| **Alternative** | S | vs / alternative | 2200–3000 | ≤45% | standard | `oginify-vs-vercel-og` |
| **ToolGuide** | T | free tool / bulk / maker | 1000–1800 | ≤35% | lite | `bulk-og-image-generator` |
| **DeveloperGuide** | S | next.js / API / satori | 2000–3000 | ≤35% | flagship | `social-cards-skills-guide` |
| **UseCase / Scenario** | S | launch / refresh / workflow | 1500–2500 | ≤50% | standard | `refresh-blog-og-images` |
| **TrendAnalysis** | S | CTR / share / 2026 | 1800–2600 | ≤25% | standard | `og-image-click-through-rate` |
| **OpenSourceGuide** | S | social-cards-skills / open source | 1500–2500 | ≤50% | standard | `social-cards-skills-guide` |
| **Announcement** | S | 产品发布/更新 | 1200–1800 | 不限 | lite | `oginify-twitter-card-generator` |

**产品提及**：正文中 Oginify 名称 + 功能描述 + CTA 合计篇幅占比上限（非严格计数，Phase 5 目测）。

---

## 2. 全类型通用模块

| 模块 | 要求 |
|------|------|
| TL;DR | 正文第一个 section；3–5 bullet；bullet 1 = snippet 定义句；独立传达 ~80% 价值 |
| H2 编号 | 英文编号 `## 1.` `## 2.`；Conclusion/FAQ 不编号 |
| Conclusion | `## Conclusion`；CTA → `/` 或工具页；多样收束 |
| FAQ | `## Frequently asked questions`；**固定 6 题** H3；≥1 题覆盖竞品/边界/objection |
| 内链 | 全部为上下文内链（无 Related 区块）；≥2 blog；Spoke 链回 Hub |
| 外链 | 2–5；`rel="nofollow noopener"` |
| CTA | 单一主行动；正文 ≤2 次 |

---

## 3. Ranking / Comparison — H2 模板

**何时用**：`best` / `top` + ≥3 具名第三方竞品 → Ranking（编号 H3 + `articleFormat: Ranking`）。双产品 head-to-head → Comparison。

```
## TL;DR
## 1. Why {category} matters in 2026
## 2. How this ranking works — {job shape taxonomy}
## 3. The best {tools}, ranked
   ### 1. Oginify — Best for {job shape}
   ### 2. {Tool} — Best for …
   ### 3. …（≥3 编号 H3）
   ### Ranked listing — quick reference（表格）
## 4. How to choose the right {tool}
## 5. What's next for {category}
## Conclusion
## Frequently asked questions（6 题）
```

**硬性规则**：
- §3 标题必须含 **Ranked** 或 **ranked listing** 语义
- 每个排名 H3 以 `### {n}. {Product} — Best for {job shape}` 开头
- **#1 产品**（Oginify）必须写 ≥1 个「不适合」场景
- 三分类框架（URL-first / 通用生图 / 代码驱动）必须出现（P2）
- 每竞品 ≥1 优势 + ≥1 非 Oginify 更合适场景（P5）
- TL;DR 第二条 bullet 声明 **ranked by job fit**

---

## 4. HowTo / Tutorial — H2 模板

```
## TL;DR
## 1. What most people get wrong about {task}
## 2. What you need before you start
## 3. {N}-step workflow
## 4. What the finished card should look like
## 5. {Optional: testing / troubleshooting}
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：步骤用祈使句；每大步后接「为什么这步重要」；Oginify 相关步骤须与产品机制一致（粘贴 URL → 选变体 → 下载 PNG → 粘贴 meta tags，as-of）。

---

## 5. Glossary / Research — H2 模板（Hub）

```
## TL;DR
## 1. Where "{term}" came from
## 2. What {term} actually is（canonical 定义节，150–200 words）
## 3. How it works — the {technical mechanism}
## 4. What {term} is not（边界：vs 邻近概念）
## 5. Why {year} is the year of {term}
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：产品仅在定义之后、FAQ 之前「工具形态」段出现，≤3 段；产品提及 ≤20%。**Hub 专属**：canonical 定义，其他文 1–2 句 + link 引用。

---

## 6. SizeGuide / Reference — H2 模板（Track T）

```
## TL;DR
## 1. The size that matters（1200×630 定义）
## 2. Platform-by-platform breakdown（表格）
## 3. How to make sure your image renders correctly
## Conclusion
## Frequently asked questions（4–6 题）
```

**规则**：简短直接；产品提及 ≤15%；1200×630 规格有来源（P3）；Track T 8 维 SelfCheck。

---

## 7. MetaGuide — H2 模板

```
## TL;DR
## 1. The meta tags that control your preview
## 2. How to set them up（og:title / og:description / og:image / twitter:card）
## 3. Testing before you publish（validator）
## 4. Common mistakes
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：链 `/open-graph-validator`；代码片段须正确；`og:image:alt` 建议提及。

---

## 8. Alternative — H2 模板

```
## TL;DR
## 1. Why people compare {A} and {B}
## 2. What {A} actually is
## 3. What {B} actually is
## 4. Head-to-head（对比表 ≥6 维度）
## 5. When to choose {A} — and when {B} wins
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：三分类框架；每竞品 ≥1 优势（P5）；必须写 ≥1「非 Oginify 更合适场景」（P5）；禁 just/merely。

---

## 9. ToolGuide — H2 模板（Track T）

```
## TL;DR
## 1. What {tool} does
## 2. How to use it（3 步）
## 3. What it's good for — and its limits
## Conclusion
## Frequently asked questions（4–6 题）
```

**规则**：简短；链对应工具页；不复制工具页全文（C3）。

---

## 10. DeveloperGuide — H2 模板

```
## TL;DR
## 1. The developer options for OG images
## 2. {Approach A} — code-driven（Vercel OG / Satori）
## 3. {Approach B} — agent-native（social-cards-skills）
## 4. {Approach C} — API / MCP
## 5. Choosing the right approach
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：P4 边界（SaaS vs 开源）；代码片段正确；链 GitHub repo（外链 nofollow）。

---

## 11. UseCase / Scenario — H2 模板

```
## TL;DR
## 1. The {scenario} problem
## 2. The workflow（step by step）
## 3. What changed
## 4. Variants: {other scenarios}
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：场景叙事；产品提及 ≤50%；真实工作流（launch feature / refresh blog / defend landing page / ad set）。

---

## 12. TrendAnalysis — H2 模板

```
## TL;DR
## 1. What the data says（as-of 时效）
## 2. Why {trend} is happening
## 3. What it means for {audience}
## 4. What to watch next
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：CTR/分享数字须有来源（G3）；不写无来源「提升 300%」类 claim（P6）。

---

## 13. OpenSourceGuide — H2 模板

```
## TL;DR
## 1. Why open source matters in {category}
## 2. What social-cards-skills is（P4 边界）
## 3. How to run it（agent skills / npx + Satori + fonts）
## 4. Managed vs self-hosted（对比表）
## Conclusion
## Frequently asked questions（6 题）
```

**规则**：P4 边界严格；链 GitHub（外链 nofollow）；诚实写开源版需要自带模型/资产。

---

## 14. Announcement — H2 模板

```
## TL;DR
## {Product} is live: {one-line value prop}
## The problem
## What {Product} does（in plain terms）
## How to try it
## Frequently asked questions（4–6 题）
```

**规则**：克制、新闻式；不夸大（P6）；产品提及不限。

---

## 15. Slug 与 Title 规则

### Slug 七原则

| 原则 | Oginify 执行 |
|------|-------------|
| P1 常青 | 不含年份、版本号 |
| P2 关键词 | 含 primary keyword 核心词 |
| P3 可读 | kebab-case；无连续重复词 |
| P4 长度 | 5–8 词，≤60 字符 |
| P5 集群一致 | 同簇命名模式一致 |
| P6 语义余量 | 描述主题非观点 |
| P7 搜索意图 | 像读者会搜的语言 |

**禁词**：`framework` · `strategy` · `guide` · `diagnosis` · `complete` · 年份

**反模式速查**：

| 反模式 | 错误示例 | 正确示例 |
|--------|---------|---------|
| 含年份 | `best-og-generators-2026` | `best-ai-og-image-generators` |
| 含数量 | `top-5-og-tools` | `best-og-image-generators` |
| 连续重复词 | `og-og-image-tools` | `og-image-tools` |
| 内部架构词泄漏 | `og-image-framework` | `what-is-open-graph-image` |

### Title 公式

- Ranking：`Best {Category} — {Ranked by Job Fit}`
- HowTo：`How to {Task} — {Benefit Hook}`
- Glossary：`What Is {Term} — {Scope}`
- SizeGuide：`{Platform} Image Sizes in 2026 — {Cheat Sheet}`
- Alternative：`{A} vs {B} — {Differentiator Frame}`
- DeveloperGuide：`How {Technology} {Works} — {Framework Hook}`
- TrendAnalysis：`Why {Trend} — {Data Hook}`

**Meta description**（120–160 chars）：benefit + 主 intent 词 + 差异化一句。

---

## 16. Frontmatter Schema

```yaml
---
title: "Title Case — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword for SERP"
slug: "kebab-case-slug"
date: 2026-08-XX  # 发布时间，Phase 2 确定，每自然日 ≤1 篇；永不改变
updated: 2026-08-XX  # 可选；实质性更新才改
author: "Oginify"  # 每次创作确认：Oginify | Kostja | {具体成员}
category: "Tutorial | Guide | Case Study | Reference | Product"
secondary_category: "Open Graph"
articleFormat: "Ranking | —"  # Ranking 文必填 Ranking
---
```

> **2026-08-15 起**：`image` / `keywords` / `related` 不再写入 frontmatter。页面只显示一个日期。
