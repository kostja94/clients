# Scheduling Agent / Agentic Calendar — 文章构建方案

> 基于 Floatboat 主题簇策略与 12 维度模板体系，为 5 篇系列文章提供完整构建规范。
>
> **关联文档**：[floatboat.md](../floatboat.md) · [floatboat-keywords.md](../floatboat-keywords.md) · [floatboat-features.md](../floatboat-features.md) · [floatboat-use-cases.md](../floatboat-use-cases.md) · [floatboat-competitors.md](../floatboat-competitors.md) · [floatboat-site-structure.md](../floatboat-site-structure.md) · [README.md](./README.md)
>
> **Last updated**: 2026-06-11

---

## 0. 系列总览

### 0.1 5 篇文章矩阵

| # | 标题 | 类型 | 词数目标 | 主关键词 | 文章角色 |
|---|------|------|---------|---------|---------|
| 01 | Best AI Scheduling Assistants in 2026 | Comparison | 2800–3500 | `best AI scheduling assistant` | 漏斗顶端 — 品类入口，承接搜索需求 |
| 02 | How AI Meeting Prep Actually Works | Product tutorial / Scenario | 2000–2500 | `AI meeting preparation` | 漏斗中端 — 场景共鸣 → 产品认知 |
| 03 | AI Follow-Up Automation After Meetings | Product tutorial / Scenario | 2000–2500 | `AI follow-up automation` | 漏斗中端 — 场景共鸣 → 产品认知 |
| 04 | Calendar-Driven AI vs Chat-Based AI | Research / Category definition | 2800–3500 | `calendar-driven AI vs chat AI` | 品类定义 — 建立 Floatboat 叙事框架 |
| 05 | What Is an Agentic Calendar | Research / Glossary | 2400–3000 | `agentic calendar` | 品类定义 — 独占关键词，锚定品牌 |

### 0.2 主题簇结构

```
                    ┌──────────────────────────────┐
                    │  05 Agentic Calendar (Hub)    │
                    │  Category definition, pillar  │
                    └────────────┬─────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
     ┌────────▼────────┐ ┌──────▼──────┐ ┌────────▼────────┐
     │ 04 Calendar-     │ │ 01 Best AI  │ │ 02/03 Scenario  │
     │  Driven vs Chat  │ │ Scheduling  │ │ Articles        │
     │  (对比框架)       │ │ Assistants  │ │ (产品能力展示)   │
     └─────────────────┘ └─────────────┘ └─────────────────┘
```

- **05 → all spokes**：定义 category 后，每篇 spoke 引用 05 的定义（1-2 句 + internal link）
- **04 ↔ 05**：双向互链，04 提供对比框架，05 提供品类锚点
- **02 ↔ 03**：prep → follow-up 闭环，双向互链
- **01 → 02/03**：01 的 comparison 结论自然指向产品能力文章

### 0.3 合规性约定（全系列通用）

| 规则 | 说明 |
|------|------|
| 不声称"全球首个" | 技术上可验证的"首个"需提供证据链；模糊宣称使用替代表述（"在桌面端首次"、"一类新的"） |
| 竞品描述引用公开来源 | 所有竞品能力描述指向官网/GitHub/公开 PR；不基于个人使用经验推断 |
| 商标类比合规 | Slack/Discord/微信仅在旁白中出现，不作为标题主体；不使用竞品商标作为 SEO 锚文本 |
| 信息披露 | Comparison 和 Research 文章必须有 disclosures 段落 |
| AI 生成声明 | 不必要（本文档为人工策划框架），具体文章撰写时如使用 AI 辅助需标注 |

---

## 0.4 跨文章一致性框架

### 0.4.1 Canonical Concept Registry

每个核心概念只在一篇文章中完整定义，其他文章引用 1-2 句 + internal link。

| 概念 | Canonical 文章 | 定义位置 | 引用文章 |
|------|---------------|---------|---------|
| Agentic Calendar | 05 — H2 "Agentic Calendar Defined" | 完整定义（150-200 words） | 01, 02, 03, 04 |
| Calendar-Driven AI | 04 — H2 "What Calendar-Driven AI Means" | 完整定义 | 01, 05 |
| Chat-Based AI (对比) | 04 — H2 "The Chat-Based Paradigm" | 对比框架 | 01, 05 |
| AI Scheduling 四代演进 | 01 — H2 "The Four Generations of AI Scheduling" | 演化框架 | 04, 05 |
| Meeting Prep Pipeline | 02 — H2 "The Pre-Meeting Workflow" | 流程定义 | 03 |
| Follow-Up Automation Pipeline | 03 — H2 "The Post-Meeting Workflow" | 流程定义 | 02 |
| Floatboat 4-Step Mechanism | 02 / 03 | 各引用 1-2 句 | 01, 04, 05 |

### 0.4.2 产品描述跨文章重复率控制

Floatboat 产品描述在 5 篇文章中均会出现。控制策略：

- **01**：产品在一段 comparison table 中以行级出现，不做独立 feature 段落
- **02/03**：产品作为 workflow 方案的核心呈现（自然出现，不受比例限制）
- **04**：产品在"Calendar-Driven 范式下的工具示例"中出现，不超过 2 段
- **05**：产品在 Glossary 定义之后、FAQ 之前的"工具形态"段落出现，不超过 3 段
- **重复率上限**：产品描述句子级重复 across articles ≤ 2 句（canonical product description 在 02 中定义）

### 0.4.3 叙事模式差异化

防止 5 篇文章共享同一叙事弧线（education → neutral → "but X changes everything" → product as answer）。

| 文章 | 叙事结构 | 检验 |
|------|---------|------|
| 01 | "市场有 N 种工具，怎么选 → 按 X 维度拆解 → 每种适合什么场景" | 结论不导向单一产品，承认不同工具适合不同场景 |
| 02 | "会议准备的实际痛点 → AI 怎么解决每个环节 → 一套完整的 prep workflow" | 以 workflow 为主线，产品是实现 workflow 的工具 |
| 03 | "会后跟进的塌陷地带 → 为什么自动化比手动好 → follow-up pipeline 的 3 个阶段" | 以 pipeline 为主线 |
| 04 | "两种范式的根本差异 → 不是更好/更差，是根本不同的设计哲学 → 什么场景各适合" | 对比框架保持中立，结尾给出选择指南而非推荐 |
| 05 | "概念溯源 → 技术边界 → 与邻近概念的区分 → 未来方向" | 定义性文章，不设 funnel，不 push 产品 |

### 0.4.4 主关键词防冲突

| 文章 | 主关键词 | 搜索意图 | 与谁可能冲突 |
|------|---------|---------|------------|
| 01 | `best AI scheduling assistant` | 商业调查/比较 | 05（scheduling vs calendar 意图不同 → 不冲突） |
| 02 | `AI meeting preparation` | 信息/操作指南 | 03（prep vs follow-up 意图不同 → 不冲突） |
| 03 | `AI follow-up automation` | 信息/操作指南 | 02（同上） |
| 04 | `calendar-driven AI vs chat AI` | 概念比较/信息 | 05（对比 vs 定义 → 声明边界，互链） |
| 05 | `agentic calendar` | 定义/概念查询 | 04（互链 + scope 声明） |

**04 ↔ 05 边界声明**：04 开头声明"这篇文章对比两种范式，如果你想先了解 Agentic Calendar 是什么，请阅读 [05]"，05 开头声明"这篇文章定义概念，如果你想看这个范式与 Chat-Based AI 的对比，请阅读 [04]"。

---

## 1. Article 01 — Best AI Scheduling Assistants in 2026

### 1.1 基础规格

| 维度 | 规格 |
|------|------|
| **类型** | Comparison（横向对比） |
| **词数目标** | 2800–3500 words |
| **文章角色** | 漏斗顶端 — 品类入口 |
| **目标读者** | 搜索 "best AI scheduling assistant/tool" 的购买意向用户 |
| **读者阶段** | Consideration / Evaluation |

### 1.2 Slug 设计

**`best-ai-scheduling-assistants`**

设计决策：
- `best` + 核心品类词 — 匹配搜索意图（商业调查/比较）
- 不含 `2026` — 常青 slug，发布后定期更新内容即可
- 不含 `tools` — `assistants` 覆盖工具 + 代理两个层级
- 长度 5 词 — 在 12-design-principles 的可读范围内

### 1.3 搜索意图与 SERP 定位

| 维度 | 分析 |
|------|------|
| **主关键词** | `best AI scheduling assistant` |
| **搜索意图** | 商业调查 — 用户准备选择/购买，想了解市场上有哪些选项 |
| **SERP 特征** | 列表型文章（"X Best AI Scheduling Tools"），含 affiliate link 的居多 |
| **Top 排名页面共性** | 简单罗列 + 一句话介绍；缺少演化框架和决策框架 |
| **我们的差异化** | 用四代演化框架组织工具 → 给出按场景选择矩阵 → 不以 affiliate 为导向 |

**SERP 标题公式**（<60 chars）：
`Best AI Scheduling Assistants — From Smart Schedulers to Agentic Calendars`

**Meta Description**（120-160 chars）：
`Compare the best AI scheduling assistants across four generations of technology — from basic smart schedulers to autonomous agentic calendars. Find the right tool for your workflow.`

### 1.4 H2 结构

```
1. The Scheduling Problem That AI Is Solving
   1.1 Why Calendars Are Still Broken
   1.2 What "AI Scheduling" Actually Means in 2026

2. The Four Generations of AI Scheduling
   2.1 Gen 1: Smart Schedulers (Calendly, Doodle)
   2.2 Gen 2: AI Optimizers (Motion, Reclaim, Clockwise)
   2.3 Gen 3: Scheduling Agents (Floatboat, Accomplish, Eigent)
   2.4 Gen 4: Calendar-Driven Agent OS (emerging)

3. Head-to-Head: 8 AI Scheduling Assistants Compared
   3.1 Comparison Table
   3.2 Smart Schedulers: Best for Simple Booking
   3.3 AI Optimizers: Best for Team Time Management
   3.4 Scheduling Agents: Best for Autonomous Prep + Follow-Up
   3.5 Emerging: Calendar-Driven Agent OS

4. How to Choose the Right AI Scheduling Assistant
   4.1 By Team Size and Use Case
   4.2 By Integration Requirements
   4.3 By Automation Depth: Assisted vs Autonomous

5. What's Next for AI Scheduling
   5.1 From Scheduling to Calendar-Driven Work
   5.2 The Agentic Calendar Vision

6. FAQ
   6.1 What's the difference between a smart scheduler and a scheduling agent?
   6.2 Can AI scheduling assistants handle multi-timezone teams?
   6.3 Do these tools integrate with Google Calendar and Outlook?
   6.4 Are AI scheduling assistants worth it for solo founders?

```

### 1.5 Frontmatter 模板

```yaml
---
title: "Best AI Scheduling Assistants — From Smart Schedulers to Agentic Calendars"
description: "Compare the best AI scheduling assistants across four generations — smart schedulers, AI optimizers, scheduling agents, and calendar-driven agent OS. Choose by use case."
slug: "best-ai-scheduling-assistants"
date: 2026-06-XX
author: "Floatboat"
image: "/blog/images/scheduling-assistants-comparison-og.jpg"
category: "Comparison"
---
```

### 1.6 源需求

按 02-fact-eeat.md 最低引用标准：

| 要求 | 说明 |
|------|------|
| **竞品能力描述** | 每个竞品至少 1 个官方来源（官网/GitHub/公开 PR） |
| **数据声明** | 市场规模数据（$27.8B/29.8% CAGR）引用行业报告 |
| **四代分类** | 框架逻辑无需引用；每个工具归类需有公开资料支撑 |
| **Source Map** | 每段包含声明能力的段落需标注来源 |

### 1.7 客观性与语调

| 维度 | 规格 |
|------|------|
| **产品提及比例上限** | ≤40%（Comparison 类型） |
| **竞品公平性** | 每个竞品至少列出 1 个优势；不用 "just a"、"merely"、"only does X" |
| **Floatboat 出现方式** | 在 Comparison Table 中作为一行；在 Gen 3 Scheduling Agents 段落中与同类工具并列 |
| **叙事弧线** | 市场全景 → 分类框架 → 按场景推荐 → 不导向单一产品 |
| **声调** | Calm but opinionated — 分类框架是 opinionated 的，但推荐是 calm 的 |

### 1.8 排版约束

| 维度 | 规格 |
|------|------|
| **列表比例上限** | ≤30%（Comparison 类型） |
| **长段落（4-8 句）** | ≥3 个（每代分析至少 1 个长段落） |
| **短段落比例** | 15-25% |
| **Cohesion rate** | 10 段中 ≥7 对需有衔接手段 |
| **比较表格** | H3 "Comparison Table" 下为完整表格；每行至少 5 个比较维度 |
| **禁止模式** | "table + one sentence" 反模式（表格前后需有分析段落） |

---

## 2. Article 02 — How AI Meeting Prep Actually Works

### 2.1 基础规格

| 维度 | 规格 |
|------|------|
| **类型** | Product tutorial / Scenario narrative |
| **词数目标** | 2000–2500 words |
| **文章角色** | 漏斗中端 — 场景共鸣 → 产品认知 |
| **目标读者** | 搜索 "AI meeting prep" / "how to prepare for meetings with AI" 的效率导向用户 |
| **读者阶段** | Consideration / Activation |

### 2.2 Slug 设计

**`ai-meeting-preparation`**

设计决策：
- 直接匹配搜索意图词 `AI meeting preparation`
- 不含 `how-to` — 保持 slug 为概念锚点而非教程标记
- 不含 `guide` — 属于 internal architecture 禁词
- 长度 3 词 — 极简

### 2.3 搜索意图与 SERP 定位

| 维度 | 分析 |
|------|------|
| **主关键词** | `AI meeting preparation` |
| **搜索意图** | 信息/操作指南 — 用户想知道 AI 怎么帮他们准备会议，有什么工具/方法 |
| **SERP 特征** | 多为碎片化文章（"5 AI tools for meeting prep"）或 AI 功能列表，缺少端到端 workflow |
| **Top 排名页面共性** | 列出 AI note-taker 功能；不涉及 brief generation, context gathering, pre-read 生成 |
| **我们的差异化** | 端到端 prep pipeline（30 min → meeting start），不是工具列表 |

**SERP 标题公式**（<60 chars）：
`How AI Meeting Prep Actually Works — A Full Pre-Meeting Pipeline`

**Meta Description**（120-160 chars）：
`AI meeting prep goes beyond note-taking. See how an end-to-end pre-meeting pipeline works — from context gathering to brief generation, automated before every meeting.`

### 2.4 H2 结构

```
1. What Most People Get Wrong About AI Meeting Prep
   1.1 It's Not Just an AI Note-Taker
   1.2 The 30 Minutes Before a Meeting Matter More Than the Meeting Itself

2. The Pre-Meeting Pipeline: 4 Stages
   2.1 Stage 1: Context Gathering — Who, What, Why
   2.2 Stage 2: Document Surfacing — Relevant Files, Past Notes, Threads
   2.3 Stage 3: Brief Generation — A One-Page Pre-Read
   2.4 Stage 4: Action Item Carry-Over — What Was Left from Last Time

3. What a Calendar-Driven AI Does Differently
   3.1 Triggered by the Calendar, Not a Chat Prompt
   3.2 Prep Happens Whether You Remember to Ask or Not

4. Setting This Up for Your Own Workflow
   4.1 Connecting Your Calendar, Email, and Docs
   4.2 Customizing the Prep Brief Template
   4.3 Automating Recurring Prep for Weekly Standups and Client Calls

5. FAQ
   5.1 How is this different from an AI note-taker like Fireflies or Otter?
   5.2 Can this work with confidential meetings?
   5.3 What integrations do I need to make this work?
   5.4 Does the AI need access to all my emails and files?

```

### 2.5 Frontmatter 模板

```yaml
---
title: "How AI Meeting Prep Actually Works — A Full Pre-Meeting Pipeline"
description: "AI meeting prep goes beyond note-taking. Learn the 4-stage pre-meeting pipeline — context gathering, document surfacing, brief generation, and action item carry-over."
slug: "ai-meeting-preparation"
date: 2026-06-XX
author: "Floatboat"
image: "/blog/images/ai-meeting-prep-og.jpg"
category: "Product"
---
```

### 2.6 源需求

| 要求 | 说明 |
|------|------|
| **产品能力** | 基于当前版本文档（floatboat-features.md）。不做前瞻性声称 |
| **竞品提及** | 提到 Fireflies/Otter 仅用于区分定位（note-taker vs full prep），不做能力对比 |
| **数据** | 时间节省声明需用内部数据格式："Based on internal analysis of [N] meeting prep workflows across [time period], [finding]" |

### 2.7 客观性与语调

| 维度 | 规格 |
|------|------|
| **产品提及比例** | 自然出现，不设硬上限（Product tutorial 类型 ≤50%） |
| **声调** | Practitioner-grade — 使用行业术语（brief generation, context gathering），不做过度解释 |
| **禁止模式** | 不用 "Imagine…" 开头段落；不用 "In today's fast-paced world…" |
| **叙事弧线** | 痛点 → 4 阶段 pipeline → Calendar-Driven 的差异化 → 实操 → 非"教育→中立→产品=答案"公式 |

### 2.8 排版约束

| 维度 | 规格 |
|------|------|
| **列表比例上限** | ≤35%（Tutorial 类型） |
| **长段落** | ≥3 个（4 个 pipeline stage 各需 1 个分析段落） |
| **段落长度标准差** | ≥1.5 |
| **禁止** | 连续 3+ 短段落簇 |
| **Pipeline 呈现** | 4 stage 用编号 H3，不用列表承载流程 |

---

## 3. Article 03 — AI Follow-Up Automation After Meetings

### 3.1 基础规格

| 维度 | 规格 |
|------|------|
| **类型** | Product tutorial / Scenario narrative |
| **词数目标** | 2000–2500 words |
| **文章角色** | 漏斗中端 — 场景共鸣 → 产品认知；与 02 形成 prep→follow-up 闭环 |
| **目标读者** | 搜索 "automated meeting follow-up" / "AI follow-up after meetings" 的用户 |
| **读者阶段** | Consideration / Activation |

### 3.2 Slug 设计

**`ai-follow-up-automation`**

设计决策：
- 直接匹配搜索意图词
- 不含 `meeting`（文章内容覆盖 meetings + deadlines + tasks，不只会议）
- 不含 `guide` / `how-to`
- 长度 4 词

### 3.3 搜索意图与 SERP 定位

| 维度 | 分析 |
|------|------|
| **主关键词** | `AI follow-up automation` |
| **搜索意图** | 信息/操作指南 — 用户想自动化会后跟进（总结、action items、提醒） |
| **SERP 特征** | 多为 email automation 工具文章或 CRM follow-up，缺少会议 follow-up 的端到端方案 |
| **我们的差异化** | 不是 email follow-up，是 post-meeting pipeline（notes → actions → next meeting prep chain） |

**SERP 标题公式**（<60 chars）：
`AI Follow-Up Automation — Turn Meeting Outcomes Into Action`

**Meta Description**（120-160 chars）：
`AI follow-up automation closes the gap between meetings and execution. See how notes become tasks, reminders, and prep for the next meeting — automatically.`

### 3.4 H2 结构

```
1. The Follow-Up Gap
   1.1 Why Action Items Die Between Meetings
   1.2 Manual Follow-Up Doesn't Scale for Solo Founders

2. The Post-Meeting Pipeline: 3 Stages
   2.1 Stage 1: Decision Capture — What Was Actually Decided
   2.2 Stage 2: Action Extraction — Tasks, Owners, Deadlines
   2.3 Stage 3: Prep Chain — Feeding the Next Meeting's Pipeline

3. Automation That Feels Invisible
   3.1 Triggered When the Meeting Ends, Not When You Remember
   3.2 From Notes to Tasks Without Copy-Paste

4. Connecting the Full Loop: Prep → Meet → Follow-Up → Prep
   4.1 How the Pre-Meeting Pipeline (Article 02) and Post-Meeting Pipeline Work Together
   4.2 The Calendar as the Central Runtime

5. FAQ
   5.1 How does AI follow-up handle vague or unstructured meetings?
   5.2 Can the AI distinguish between decisions and small talk?
   5.3 What tools do I need for end-to-end meeting automation?

```

### 3.5 Frontmatter 模板

```yaml
---
title: "AI Follow-Up Automation — Turn Meeting Outcomes Into Action"
description: "Close the gap between meetings and execution. Learn the 3-stage post-meeting pipeline: decision capture, action extraction, and automated prep for the next meeting."
slug: "ai-follow-up-automation"
date: 2026-06-XX
author: "Floatboat"
image: "/blog/images/ai-follow-up-automation-og.jpg"
category: "Product"
---
```

### 3.6 源需求

| 要求 | 说明 |
|------|------|
| **产品能力** | 基于 floatboat-features.md 的 Calendar-Driven 4-step mechanism |
| **H2 "Connecting the Full Loop"** | 引用 02 的 1-2 句 pipeline 定义 + internal link |
| **时间节省声明** | 使用内部数据格式 |

### 3.7 客观性与语调

| 维度 | 规格 |
|------|------|
| **产品提及比例** | 自然出现（Product tutorial ≤50%） |
| **声调** | Practitioner-grade |
| **与 02 的叙事差异** | 02 以 "prep pipeline" 为主线，03 以 "follow-up gap → pipeline → closed loop" 为主线；不做 education→neutral→product 弧线 |
| **禁止** | "Imagine finishing a meeting and…" 虚构场景开头 |

### 3.8 排版约束

| 维度 | 规格 |
|------|------|
| **列表比例上限** | ≤35% |
| **长段落** | ≥3 个 |
| **段落长度标准差** | ≥1.5 |
| **与 02 的排版一致性** | 两篇文章的 FAQ 数量一致（4 个），H2 数量接近 |

---

## 4. Article 04 — Calendar-Driven AI vs Chat-Based AI

### 4.1 基础规格

| 维度 | 规格 |
|------|------|
| **类型** | Research / Category definition |
| **词数目标** | 2800–3500 words |
| **文章角色** | 品类定义 — 建立 Floatboat 叙事框架 |
| **目标读者** | 搜索 "calendar-driven AI" / "proactive agent vs chat AI" 的概念探索用户 |
| **读者阶段** | Awareness / Consideration |

### 4.2 Slug 设计

**`calendar-driven-ai-vs-chat-ai`**

设计决策：
- `calendar-driven-ai` + `chat-ai` — 直接匹配两个核心概念
- `vs` — 匹配对比搜索意图
- 不含 `proactive` — 虽然品牌关联，但 search intent 更集中在 "calendar-driven"
- 不含 `comparison` / `difference` — `vs` 已足够表达
- 长度 5 词

### 4.3 搜索意图与 SERP 定位

| 维度 | 分析 |
|------|------|
| **主关键词** | `calendar-driven AI vs chat AI` |
| **搜索意图** | 概念比较 — 用户想理解两种 AI 交互范式的区别 |
| **SERP 特征** | 此类对比文章极少，多为碎片化的 "proactive vs reactive AI" 泛文 |
| **我们的差异化** | 用具体的工作流对比（同一场景下两种范式的行为差异）+ 设计哲学层面的分析 |

**SERP 标题公式**（<60 chars）：
`Calendar-Driven AI vs Chat-Based AI — Two Different Paradigms`

**Meta Description**（120-160 chars）：
`Calendar-driven AI and chat-based AI represent fundamentally different design philosophies. See how they compare on workflow, proactivity, and who initiates the interaction.`

### 4.4 H2 结构

```
1. Two Ways AI Shows Up to Work
   1.1 The Chat Window: AI Waits for You
   1.2 The Calendar: AI Runs on Your Schedule

2. What Calendar-Driven AI Actually Means
   2.1 Proactive, Not Just Responsive
   2.2 Calendar Events as Triggers, Not Just Time Slots
   2.3 The Runtime Metaphor: Calendar as OS

3. The Chat-Based Paradigm
   3.1 Strengths: Flexibility, Conversational Depth, Exploration
   3.2 Limitations: Reactive-Only, Session-Based, Context Resets

4. Head-to-Head: Same Scenario, Different Approaches
   4.1 Scenario 1: Preparing for a Client Call
   4.2 Scenario 2: Following Up After a Team Standup
   4.3 Scenario 3: Managing a Project Deadline

5. When Each Paradigm Fits Best
   5.1 Chat-Based AI Excels At: Creative Exploration, Deep Research, Ad-Hoc Problem Solving
   5.2 Calendar-Driven AI Excels At: Recurring Workflows, Deadline-Driven Tasks, Meeting Lifecycle

6. FAQ
   6.1 Can I use both calendar-driven and chat-based AI together?
   6.2 Is calendar-driven AI just scheduled prompts?
   6.3 Which paradigm is better for solo founders?
   6.4 Does calendar-driven AI need access to my entire calendar?

```

### 4.5 Frontmatter 模板

```yaml
---
title: "Calendar-Driven AI vs Chat-Based AI — Two Different Paradigms"
description: "Calendar-driven AI and chat-based AI represent fundamentally different design philosophies. Compare how they differ on workflow, proactivity, and who initiates the interaction."
slug: "calendar-driven-ai-vs-chat-ai"
date: 2026-06-XX
author: "Floatboat"
image: "/blog/images/calendar-driven-vs-chat-og.jpg"
category: "Research"
---
```

### 4.6 源需求

| 要求 | 说明 |
|------|------|
| **最低引用数** | 4-6 个，其中 ≥2 个 primary source |
| **两个范式定义** | 需有公开可查的参考依据（如 Anthropic/OpenAI 文档描述 chat AI 的定位，Floatboat 文档描述 calendar-driven 的定位） |
| **竞品描述** | 提到 ChatGPT/Claude/Gemini 时引用官方文档 |
| **场景对比** | 场景本身不需要引用；行为描述基于公开产品文档 |

### 4.7 客观性与语调

| 维度 | 规格 |
|------|------|
| **产品提及比例** | ≤15%（Research 类型） |
| **叙事中立性** | 文章结论不导向 "calendar-driven is better"；给出场景指南（5.1/5.2） |
| **竞品公平性** | Chat-based AI 的优势（灵活性、探索深度）获得独立 H2 段落 |
| **声调** | Category-building — 独立价值在前，产品在后 |
| **Disclosure** | 必须声明 Floatboat 属于 calendar-driven 范式（已在 frontmatter 中） |

### 4.8 排版约束

| 维度 | 规格 |
|------|------|
| **列表比例上限** | ≤25%（Research 类型） |
| **长段落** | ≥3 个（每个哲学分析点至少 1 个） |
| **场景对比格式** | 每个 scenario 用段落叙述，不用表格替代分析 |
| **禁止** | "table + one sentence" 反模式 |

---

## 5. Article 05 — What Is an Agentic Calendar

### 5.1 基础规格

| 维度 | 规格 |
|------|------|
| **类型** | Research / Glossary |
| **词数目标** | 2400–3000 words |
| **文章角色** | 品类定义 Hub — 独占关键词，所有 spoke 文章的锚点 |
| **目标读者** | 搜索 "agentic calendar" / "what is agentic calendar" 的概念探索用户 |
| **读者阶段** | Awareness |

### 5.2 Slug 设计

**`what-is-agentic-calendar`**

设计决策：
- `what-is` 前缀 — Group 决定（SERP 中 "what is X" 模式强匹配定义意图）
- `agentic-calendar` — 核心概念词，Floatboat 品类独占
- 不含 `definition` / `explained` / `guide` — 避免冗余
- 长度 4 词

### 5.3 搜索意图与 SERP 定位

| 维度 | 分析 |
|------|------|
| **主关键词** | `agentic calendar` |
| **搜索意图** | 定义/概念查询 — 用户想理解这个新概念是什么 |
| **SERP 特征** | 几乎没有直接竞争（蓝海词），搜索结果多为 calendar tool 而不是概念定义 |
| **我们的差异化** | 第一个给出完整定义的页面（品类定义权） |

**SERP 标题公式**（<60 chars）：
`What Is an Agentic Calendar? The Next Step Beyond Smart Scheduling`

**Meta Description**（120-160 chars）：
`An agentic calendar doesn't just schedule time — it acts on your schedule. Learn what defines this new category of proactive AI and how it differs from smart schedulers.`

### 5.4 H2 结构

```
1. Beyond Smart Scheduling
   1.1 Smart Calendars Solved Booking — Agentic Calendars Solve Action
   1.2 The Shift from "When" to "What Happens Before and After"

2. Agentic Calendar Defined
   2.1 The Core Definition (40-60 words, snippet-ready)
   2.2 Three Defining Properties: Proactive, Event-Triggered, Autonomous
   2.3 What an Agentic Calendar Is Not (Not a Scheduler, Not a Chatbot, Not a Zap)

3. The Technology Stack
   3.1 Calendar APIs and Event Hooks
   3.2 Multi-Model AI Integration
   3.3 Tool and Integration Layer (MCP, IACT)

4. How It Compares to Related Concepts
   4.1 Agentic Calendar vs Smart Scheduler
   4.2 Agentic Calendar vs AI Note-Taker
   4.3 Agentic Calendar vs Workflow Automation

5. Who Needs an Agentic Calendar
   5.1 Solo Founders and Solopreneurs
   5.2 Distributed Teams
   5.3 Anyone Who Lives by Their Calendar

6. FAQ
   6.1 Is an agentic calendar the same as an AI scheduling assistant?
   6.2 Do I need to change my existing calendar to use one?
   6.3 How is this different from having a ChatGPT window open during meetings?
   6.4 What's the difference between agentic calendar and calendar-driven AI?
   6.5 Can an agentic calendar actually execute tasks, or just remind me?

```

### 5.5 Frontmatter 模板

```yaml
---
title: "What Is an Agentic Calendar? The Next Step Beyond Smart Scheduling"
description: "An agentic calendar acts on your schedule, not just tracks it. Learn the definition, three defining properties, technology stack, and how it compares to smart schedulers."
slug: "what-is-agentic-calendar"
date: 2026-06-XX
author: "Floatboat"
image: "/blog/images/agentic-calendar-definition-og.jpg"
category: "Research"
---
```

### 5.6 源需求

| 要求 | 说明 |
|------|------|
| **最低引用数** | 2-4 个（Glossary 类型下限） |
| **核心定义** | 40-60 words，直接放在 H2 "Agentic Calendar Defined" 下，snippet-ready |
| **概念区分** | H2 "How It Compares" 中每个对比项需有公开可查的定义依据 |

### 5.7 客观性与语调

| 维度 | 规格 |
|------|------|
| **产品提及比例** | ≤10%（Glossary 类型 — 最严格的限制） |
| **产品出现位置** | 仅在 H2 "The Technology Stack" 中作为 stack 实现的例子出现 |
| **声调** | Calm but opinionated — 定义本身是 opinionated 的（我们定义了品类），但表达是 calm 的 |
| **叙事弧线** | 概念溯源 → 技术边界 → 区分邻近概念 → 展望，不设 funnel |
| **禁止** | 不以 "Floatboat is an agentic calendar" 开头或结尾 |

### 5.8 排版约束

| 维度 | 规格 |
|------|------|
| **列表比例上限** | ≤25%（Glossary 类型） |
| **长段落** | ≥3 个（核心定义 + 技术栈 + 一个区分分析） |
| **snippet-ready 定义** | 40-60 words，直接置于 2.1 H3 下，单独成段 |
| **禁止** | "table + one sentence" |

### 5.9 结构化数据

建议使用 DefinedTerm schema：

```json
{
  "@type": "DefinedTerm",
  "name": "Agentic Calendar",
  "description": "A calendar-based AI system that proactively executes work before, during, and after scheduled events — going beyond time-slot management to autonomous task execution triggered by calendar events.",
  "inDefinedTermSet": "Floatboat Category Definitions"
}
```

---

## 6. 质量检查清单

### 6.1 P0 Gate 检查（每篇文章发布前）

| 检查项 | 01 | 02 | 03 | 04 | 05 |
|--------|----|----|----|----|----|
| G1 事实错误 | 0 | 0 | 0 | 0 | 0 |
| G2 死链 | 0 | 0 | 0 | 0 | 0 |
| G3 无源数据 | 0 | 0 | 0 | 0 | 0 |
| G4 竞品状态错误 | 0 | N/A | N/A | 0 | N/A |
| G5 产品能力夸大 | 0 | 0 | 0 | 0 | 0 |
| G6 内链指向未发布页面 | 0 | 0 | 0 | 0 | 0 |
| G7 品牌风险 | 0 | 0 | 0 | 0 | 0 |

### 6.2 跨文章一致性检查（全部完成后）

| 检查项 | 说明 |
|--------|------|
| 叙事模式相似度 | 5 篇文章的叙事弧线各不相同（已在上文差异化） |
| 产品描述跨文章重复 | canonical product description 在 02 中定义，其他文章引用 ≤2 句 |
| Canonical concept 定义一致 | Agentic Calendar 定义以 05 为准；Calendar-Driven AI 以 04 为准 |
| Hub-spoke 链接完整性 | 05 ←→ 01, 05 ←→ 02, 05 ←→ 03, 05 ←→ 04（全部双向） |
| 主关键词冲突 | 04 ↔ 05 已声明边界 |

---

## 7. 发布节奏建议

| 阶段 | 时间 | 文章 | 策略 |
|------|------|------|------|
| **Week 1** | 第 1-3 天 | 05 Agentic Calendar | 先建立品类定义，其他文章可引用 |
| **Week 2** | 第 4-7 天 | 04 Calendar-Driven vs Chat | 建立对比框架，与 05 互链 |
| **Week 3** | 第 8-11 天 | 01 Best AI Scheduling Assistants | 品类入口文章，承接搜索流量 |
| **Week 4** | 第 12-14 天 | 02 AI Meeting Prep + 03 AI Follow-Up | 场景文章作为 pair 同周发布，形成闭环叙事 |

理由：
- 05 和 04 先建立品类定义和对比框架，后续所有文章都可以引用它们
- 01 是搜索量最高的漏斗入口，在品类框架建立后发布可以自然承接流量
- 02/03 作为 pair 同周发布，读者可以从 prep 自然流向 follow-up

---

> **关联**：[floatboat-keywords.md](../floatboat-keywords.md) P0 关键词包含 "Agentic Calendar"、"Calendar-Driven AI"、"Proactive AI Agent"、"AI agent for solopreneurs"、"chat AI alternative" — 本系列 5 篇文章完整覆盖这 5 个 P0 关键词各至少一次。
