# Floatboat Article Types — Full Routing & Templates

> 加载时机：Phase 0（类型路由）· Phase 3（slug/frontmatter）· Phase 4（Outline）
> 主文件：SKILL.md §2 指针

---

## 1. 路由表

| 类型 | 典型 intent | 词数 | 产品提及上限 | category | 参考 slug |
|------|------------|------|-------------|----------|-----------|
| **Research / Glossary** | 定义/概念/框架 | 2400–3500 | ≤15% | Research | `what-is-agentic-calendar`, `ai-scheduling-agent` |
| **Comparison** | 商业调查/列表 | 2800–3500 | ≤40% | Comparison | `best-ai-scheduling-assistants` |
| **Alternative** | 竞品替代/迁移 | 2200–3000 | ≤35% | Comparison | *(new)* |
| **Product / Scenario** | 场景/workflow | 2000–2700 | ≤50% | Product | `ai-meeting-preparation`, `ai-follow-up-automation` |
| **Product Announcement** | 产品发布 | 1500–2000 | 不限 | Product | `introducing-floatim` |

**路由规则**：
- 含 `best` / `top` + **≥3 个具名竞品** → **Ranking / Listing**（默认，见 §4B）
- 含 `best` / `vs` + **2 个产品 head-to-head** → **Comparison**
- 含 `alternative` / `vs` + 特定竞品名（单对手深度对比） → **Alternative**
- 含 `what is` / 品类定义 / 范式对比（非购买） → **Research**
- 含 pipeline / workflow / how X works（单场景） → **Product**
- 新产品上线 / 重大发布 → **Announcement**

---

## 2. 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 正文第一个 section；3–5 bullet；独立传达 ~80% 价值 |
| **H2 编号** | 英文编号 `## 1.` `## 2.`；FAQ 不编号 |
| **Conclusion** | `## N. Conclusion` 或 *Bottom line*；用多样收束方式 |
| **FAQ** | ≥3 题；≥1 题覆盖竞品/边界/objection；问题用 `### ` 不带编号 |
| **CTA** | 单一主行动 |

---

## 3. Research / Glossary — H2 模板

**叙事弧线**：概念溯源 → 技术边界 → 邻近概念区分 → 未来方向。**禁止** education → neutral → product as answer 漏斗。
**Voice**：清楚、教学、低营销 — 先建立读者理解再提产品；每 300-500 词出现具体对象。

```
## TL;DR
## 1. {Problem or Context — why this category matters}
## 2. {Core Term} Defined          ← canonical 定义节，150–200 words
   ### 2.1 The Core Definition     ← snippet-ready
   ### 2.2 {N} Defining Properties
   ### 2.3 What {Term} Is Not      ← 边界：vs 邻近概念
## 3. {Technology Stack / How It Works}
## 4. How It Compares to Related Concepts
## 5. {Future Direction / Market State}
## N. Conclusion
## FAQ（≥3）
```

**Glossary 专属**：产品仅在定义之后、FAQ 之前「工具形态」段出现，≤3 段。

---

## 4. Comparison — H2 模板

**叙事弧线**：市场有 N 种工具 → 按维度/代际拆解 → 各场景适合什么 → **不导向单一产品**。
**Voice**：公平、克制 — 竞品至少 1 个优势；不写"唯一推荐"；用 Wirecutter 式对比。

```
## TL;DR
## 1. The {Category} Problem That AI Is Solving
## 2. The Four Generations of {Category}
## 3. Head-to-Head: {N} Tools Compared
   ### 3.1 Comparison Table（≥5 维度/行；表前后有分析段）
## 4. How to Choose the Right {Tool Type}
## 5. What's Next for {Category}
## FAQ（≥4）
```

**Floatboat 出现方式**：Comparison Table 一行 + Gen 3/4 段落与同类并列；不做「唯一推荐」。

---

## 4B. Ranking / Listing — H2 模板

**何时用**：`best X alternatives`、`top X tools`、`X ranked` 等搜索意图，且正文需覆盖 **≥3 个具名第三方产品** + 1 个 reference row（被替代的原产品）。

**与 Comparison 的区别**：

| 维度 | Comparison | Ranking / Listing |
|------|------------|-------------------|
| 产品数量 | 通常 2 个或维度并列 | **≥3 个排名** + reference row |
| 结构 | 维度表 + 公平分析 | **编号 H3（### 1. …）** + 快查表 |
| 叙事 | Wirecutter 式「场景适合什么」 | **有序清单** + job-shape taxonomy |
| Schema | （站点侧；Agent 不生成 JSON-LD） | （站点侧；Agent 不生成 ItemList 文件） |
| frontmatter | `category: Comparison` | `category: Comparison` + `articleFormat: Ranking` |

**叙事弧线**：为何搜索 alternative → job-shape 分类法 → **编号排名逐产品** → 互补工具（非排名）→ 如何选择 → 趋势。

**Voice**：Wirecutter 排名式 — 每档至少 1 个优势 + 1 个「不适合」；reference row 公平写原产品强项；禁「唯一最佳」。

```
## TL;DR
## 1. Why People Search for {Product} Alternatives
## 2. How This Ranking Works (Job Shape, Not Keywords)
   ### 2.1 Job-shape taxonomy table
## 3. The Best {Product} Alternatives, Ranked
   ### 1. {Product A} — Best for {job shape}
   ### 2. {Product B} — Best for …
   …（≥3  numbered H3）
   ### Ranked listing — quick reference（表格 + reference row）
## 4. Complementary Tools (Not Ranked Substitutes)（可选）
## 5. How to Choose From This Ranking
## 6. What's Next for {Category}
## Conclusion
## FAQ（≥5）
```

**硬性规则**：
- §3 标题必须含 **Ranked** 或 **ranked listing** 语义
- 每个排名 H3 以 **`### {n}. {Product} — Best for {job shape}`** 开头
- **#1 产品** 必须写 ≥1 个「不适合」场景（同 Alternative §4.1 规则）
- 被替代产品放在表格 **reference row**（`—` rank），不单列第一名之上
- **勿**生成 `@type: ItemList` 的 `blog/schema/*.json`（schema 交付已停用；见 `floatboat-blog-schema.md` 归档说明）
- TL;DR 第二条 bullet 声明 **ranked listing / ranked by job fit**

**Floatboat 出现方式**：按 job shape 排 #1（如 FloatIM 于 Tag 簇、Floatboat 于 Cowork 簇）；全文禁「drop-in replacement」除非 FAQ 明确否定。

---

## 5. Alternative — H2 模板

**叙事弧线**：用户为何搜索 alternative → 竞品是什么 → 公平对比 → **必须写 ≥1 个「Floatboat 不适合」场景**。
**Voice**：直接、公平 — 承认竞品优势 ≥1 处；明确写何时不选 Floatboat。

```
## TL;DR
## 1. Why People Look for {Competitor} Alternatives
   ### 1.1 What {Competitor} Gets Right
   ### 1.2 The Gaps That Drive Users Away
## 2. What a Calendar-Driven Approach Changes
## 3. Head-to-Head: Floatboat vs {Competitor}
   ### 3.1 Comparison Table（≥6 维度/行）
   ### 3.2 Where {Competitor} Still Wins
   ### 3.3 Where Floatboat Adds the Most Value
## 4. When to Stay with {Competitor}（≥1 场景）
## 5. Setting Up Floatboat for {Use Case}
## FAQ（≥4）
```

**硬性规则**：必须写 ≥1 个「Floatboat 不适合」场景（§4.1），写在正文非脚注。竞品措辞禁 "just" / "merely" / "only does X"。必须链 Pillar Hub。

**段落格式（Alternative 专用 — 防碎段化）**：

| 节 | 错误写法 | 正确写法 |
|----|---------|---------|
| §1.1 / §1.2 | 每优势/缺口一行短段 | 各小节 ≥2 个 ≥4 句分析段；缺口可用 1 组正式 bullet（≤5 条）+ 段后 ≥2 句分析 |
| §3.2 Where {Competitor} Wins | `**Label.**` + 单句 × N | **1 个 ≥5 句段落**公平陈述竞品优势，段内枚举；禁伪列表 |
| §3.3 Where Floatboat Adds Value | `**Label.**` + 单句 × N | **1–2 个 ≥4 句段落**；价值点作段内论证，非独立短段 |
| §4 When to Stay | 场景标签 + 单句列表 | **≥2 个 ≥4 句段落**叙述「谁应留下」；§4.1 不适合场景用 1 个 ≥4 句段 |
| §5 Setup / Migration | `Step 1–4` 各 1 句 | **1 个 ≥4 句迁移叙事段** + 可选 1 组编号列表（≤4 步，每步 ≥2 句或列表前后各有分析段） |

---

## 6. Product / Scenario — H2 模板

**叙事弧线**：痛点 → pipeline 各阶段 → Calendar-Driven 差异 → 可执行设置。**禁止** "Imagine…" 虚构开头。
**Voice**：直接、可执行 — 用 pipeline/workflow 术语；少形容词；每步说清"为什么这步重要"。

```
## TL;DR
## 1. What Most People Get Wrong About {Scenario}
## 2. The {Pre|Post}-Meeting Pipeline: {N} Stages
## 3. What a Calendar-Driven AI Does Differently
## 4. Setting This Up for Your Own Workflow
## 5. {Connecting the Full Loop}
## FAQ（≥4）
```

---

## 7. Product Announcement — H2 模板

**叙事弧线**：问题 → 产品做什么 → 与矩阵关系 → 协议/场景 → FAQ。
**Voice**：克制、新闻式 — 品牌内容不言自明；不夸大；简洁直接。

```
## TL;DR
## {Product} is live: {one-line value prop}
## The problem: {wrong center of gravity}
## What {Product} does (in plain terms)
## One network, two apps（如适用）
## {Protocols / Architecture / Scenario}
## FAQ
## {Try link}
```

---

## 8. 叙事模式差异化

| 禁止模式 | 替代 |
|---------|------|
| 5 篇共享 education → neutral → "but X changes everything" → product | 每篇选对应弧线 |
| 连续 3+ 短段落簇 | 长/中/短交替 |
| Intro 三段式模板（行业综述→路标→论点） | 首段含本篇独有具体细节 |
| Conclusion 统一定论→局限→产品位置 | 留给读者本篇独有认知动作 |

---

## 9. Slug 与 Title 规则

### Slug 七原则

| 原则 | Floatboat 执行 |
|------|---------------|
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
| 含年份 | `best-ai-scheduling-2026` | `best-ai-scheduling-assistants` |
| 含数量 | `top-5-ai-tools` | `best-ai-scheduling-assistants` |
| 连续重复词 | `ai-scheduling-scheduling-tools` | `ai-scheduling-tools` |
| 内部架构词泄漏 | `agentic-calendar-framework` | `what-is-agentic-calendar` |

**"大声读"测试**：去掉连字符大声读出来 → 通顺 → 通过；不通顺 → 改。

### Title 公式

- Research：`{Primary Keyword} — {Benefit or Scope}`
- Comparison：`{A} vs {B} — {Differentiator Frame}`（双产品）
- Ranking：`Best {Category} — {Ranked by Job Shape}` 或 `Best {Product} Alternatives — {Differentiator Frame}`
- Alternative：`{Competitor} Alternative for {Use Case} — {Differentiator}`
- Product：`How {Scenario} Actually Works — {Pipeline Hook}`

**Meta description**（120–160 chars）：benefit + 主 intent 词 + 差异化一句。

---

## 10. Frontmatter Schema

```yaml
---
title: "Title Case — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword for SERP"
slug: "kebab-case-slug"
date: 2026-06-XX  # 发布时间，由 Phase 2 确定，每自然日 ≤1 篇；永不改变
updated: 2026-06-XX  # 可选；最近一次实质性内容更新；无更新则省略
author: "Floatboat"  # 每次创作时确认：Kostja | Floatboat Team | Tan Shaoqing | {具体成员}
category: "Research | Comparison | Product | Reference"
articleFormat: "Ranking | Listing | HeadToHead | —"  # Ranking 文必填 Ranking；Research/Product 可省略
---
```

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理，validator F6 已改为检查该字段**缺失**）。
>
> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。
