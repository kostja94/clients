# VOMO — Article Types Reference

> 加载时机：Phase 0（类型路由）· Phase 2（Slug）· Phase 3（Outline）
> 主文件：SKILL.md §2 路由指针

---

## 1. 路由表详版

| 类型 | 词数 | 产品上限 | 默认 Mode | category | 增长职能 | Voice | 漏斗透明度 |
|------|------|:---:|:---:|------|------|------|:---:|
| Comparison | 2500–3500 | ≤40% | flagship | ai-transcription | EvaluationComparison | 公平、克制；竞品 ≥1 优势 | 可透明 |
| Alternative | 2000–2800 | ≤45% | standard | ai-insights | SearchCapture | 公平对比；≥1 场景非 VOMO 更合适 | 可透明 |
| HowTo | 1800–2600 | ≤30% | standard | ai-transcription | ActivationTutorial | 直接、可执行；步骤祈使句 | 可透明 |
| PlatformFeature | 2000–3000 | ≤35% | standard | ai-transcription | SearchCapture | 平台缺口叙事；具体操作 | 可透明 |
| ResearchGlossary | 1800–2800 | ≤20% | flagship | ai-transcription | CategoryPOV | 教学、低营销；先建立理解再提产品 | 不可见（产品在全文后 30%） |
| WorkflowUseCase | 1800–2600 | ≤35% | standard | use-cases | ActivationTutorial | 场景驱动；可执行 | 可透明 |
| Diagnosis | 2000–2800 | ≤25% | standard | ai-insights | SearchCapture | 诊断式；先给结论后给原因 | 可透明 |
| Announcement | 1200–1800 | 不限 | lite | ai-insights | OpinionNarrative | 克制、新闻式 | 直接 |

---

## 2. H2 模板

### Comparison（Best-of 榜单）

```
## TL;DR
## 1. Why {Category} Tools Matter in 2026
## 2. What Makes a Great {Category} Tool
## 3. Top {N} Tools Compared
## 4. Comparison Table
## 5. How to Choose Based on Your Use Case
## N. Conclusion
## FAQ
```

### Alternative（X vs Y / competitor alternative）

```
## TL;DR
## 1. Why People Look for {Competitor} Alternatives
## 2. Head-to-Head: VOMO vs {Competitor}
## 3. Where {Competitor} Still Wins
## 4. When to Stay with {Competitor}
## N. Conclusion
## FAQ
```

### HowTo（教程）

```
## TL;DR
## 1. The Problem: Why Manual X Doesn't Scale
## 2. What You Need Before You Start
## 3. How to {Action} — Step by Step
## 4. What to Watch Out For
## N. Conclusion
## FAQ
```

### PlatformFeature（平台绑定）

```
## TL;DR
## 1. The Platform Gap: {Platform}'s Built-in Limitation
## 2. What You Can Extract from {Platform}
## 3. How to {Transcribe/Export} — Step by Step
## 4. Formats & Use Cases
## N. Conclusion
## FAQ
```

### ResearchGlossary（what is）

```
## TL;DR
## 1. Why {Term} Matters
## 2. What Is {Term} — The Core Definition
## 3. How It Works / Key Mechanisms
## 4. {Term} vs Related Concepts
## 5. How AI Changes {Term}
## N. Conclusion
## FAQ
```

### WorkflowUseCase（场景工作流）

```
## TL;DR
## 1. The Scenario: {e.g., Podcast to Blog Workflow}
## 2. What the AI-Powered Workflow Looks Like
## 3. How to Set It Up — Step by Step
## 4. What to Watch Out For
## N. Conclusion
## FAQ
```

### Diagnosis（问题诊断）

```
## TL;DR
## 1. The Symptom: {e.g., Why Your Podcast Has No Transcript}
## 2. Root Causes (Ranked)
## 3. How to Fix Each Cause
## 4. Prevention Checklist
## N. Conclusion
## FAQ
```

### Announcement

```
## TL;DR
## 1. What's New
## 2. Why This Matters
## 3. How It Works
## 4. Getting Started
## N. Conclusion
```

---

## 3. Slug 规则

| 原则 | 执行 |
|------|------|
| 常青 | 不含年份、版本号 |
| 关键词 | **含 primary keyword 完整核心词**；HowTo 类用 `how-to-{action}` 前缀 |
| 可读 | kebab-case；5–8 词；≤60 字符 |
| 禁词 | `framework` · `strategy` · `guide` · `complete` · `ultimate` |

**反模式速查**：

| 反模式 | 错误 | 正确 |
|--------|------|------|
| 含年份 | `best-transcription-software-2026` | `best-transcription-software` |
| 含数量 | `top-5-podcast-transcription-tools` | `best-podcast-transcription-tools` |
| 内部架构词 | `podcast-transcription-framework` | `how-to-transcribe-a-podcast` |
| 连续重复词 | `transcription-transcription-tools` | `best-transcription-tools` |
| 品牌名前置 | `vomo-podcast-transcription` | `how-to-transcribe-a-podcast` |
| 禁词 | `podcast-transcription-guide` | `how-to-convert-podcast-to-blog-post` |
| 丢关键词 | `podcast-blog`（缩写丢用户搜索词） | `how-to-convert-podcast-to-blog-post` |

> 权衡原则：**关键词完整优先，可读性其次**。HowTo 类 slug 保留完整 `how-to-{action}-{object}`（7–8 词可接受），不因缩短而丢词。

---

## 4. Title 公式

- ResearchGlossary：`What Is {Term}? — {Why It Matters for X}`
- HowTo：`How to {Action} — {Benefit / Workflow}`
- Comparison：`Best {Category} — {Differentiator Frame}`
- Alternative：`{Competitor} Alternative — {Why Teams Switch}`
- PlatformFeature：`How to {Transcribe} {Platform} Content — {Benefit}`
- WorkflowUseCase：`{Scenario} Workflow — {Benefit}`
- Diagnosis：`{Problem}? Here's Why and How to Fix It`
- Announcement：`Introducing {Feature} — {Value Proposition}`

Meta description：120–160 chars · benefit + main intent keyword + 差异化一句。

---

## 5. Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: 2026-08-XX       # 发布时间，永不改变
updated: 2026-08-XX    # 可选；最近一次实质性内容更新；无更新则省略
author: "VOMO Team"
category: "ai-transcription | ai-insights | use-cases"
---
```

> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

---

## 6. 产品提及上限执行

产品上限指「全文提到 VOMO 的密度」：
- 每 ~500 词平均 1–2 次提及；不集中在开头
- ResearchGlossary 产品在全文后 30% 首次出现
- Comparison/Alternative 可贯穿，但每竞品 ≥1 优势 + ≥1 非 VOMO 场景

---

*article-types · v1.0.0 · 2026-08-03*
