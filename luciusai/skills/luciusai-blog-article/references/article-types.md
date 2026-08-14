# Lucius AI — Article Types Reference

> 加载时机：Phase 0（类型路由）· Phase 2（Slug）· Phase 3（Outline）
> 主文件：SKILL.md §2 路由指针

---

## 1. 路由表详版

| 类型 | 词数 | 产品上限 | 默认 Mode | category | 增长职能 | Voice | 漏斗透明度 |
|------|------|:---:|:---:|------|------|------|:---:|
| Research/Glossary | 2000–3000 | ≤25% | flagship | Research | CategoryPOV | 教学、低营销；先建立理解再提产品 | 不可见（产品在全文后 30%） |
| Comparison | 2500–3500 | ≤40% | flagship | Comparison | EvaluationComparison | 公平、克制；竞品 ≥1 优势 | 可透明 |
| Product/Scenario | 2000–2800 | ≤40% | standard | Product | ActivationTutorial | 直接、可执行；pipeline 术语 | 可透明 |
| Alternative | 2000–2800 | ≤35% | standard | Comparison | SearchCapture | 公平对比；≥1 场景非 Lucius 更合适 | 可透明 |
| Announcement | 1200–1800 | 不限 | lite | Product | OpinionNarrative | 克制、新闻式 | 直接 |

---

## 2. H2 模板

### Research / Glossary

```
## TL;DR
## 1. {Problem — why this concept matters}
## 2. What Is {Term} — The Core Definition
## 3. How It Works / Key Mechanisms
## 4. {Term} vs Related Concepts（区分邻近概念）
## 5. How AI Changes {Term}
## N. Conclusion
## FAQ
```

### Product / Scenario

```
## TL;DR
## 1. The Problem: {Why manual X doesn't scale}
## 2. What {Scenario} Looks Like with AI
## 3. How to Set It Up — Step by Step
## 4. What to Watch Out For
## N. Conclusion
## FAQ
```

### Comparison

```
## TL;DR
## 1. Why Community Teams Are Looking for AI
## 2. What Makes a Great Community AI Bot
## 3. Top {N} Tools Compared
## 4. Comparison Table
## 5. How to Choose
## N. Conclusion
## FAQ
```

### Alternative

```
## TL;DR
## 1. Why People Look for {Competitor} Alternatives
## 2. Head-to-Head: Lucius vs {Competitor}
## 3. Where {Competitor} Still Wins
## 4. When to Stay with {Competitor}
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
| 关键词 | 含 primary keyword 核心词 |
| 可读 | kebab-case；5–8 词；≤60 字符 |
| 禁词 | `framework` · `strategy` · `guide` · `complete` · `ultimate` |

**反模式速查**：

| 反模式 | 错误 | 正确 |
|--------|------|------|
| 含年份 | `call-deflection-2026` | `what-is-call-deflection` |
| 含数量 | `top-5-community-bots` | `best-ai-community-bots` |
| 内部架构词 | `community-bot-framework` | `how-to-choose-community-bot` |
| 连续重复词 | `community-community-bot` | `community-ai-bot` |
| 品牌名前置 | `lucius-ai-call-deflection` | `what-is-call-deflection` |

---

## 4. Title 公式

- Research：`What Is {Term}? — {Why It Matters for X}`
- Product：`How to {Action} — {Benefit / Workflow}`
- Comparison：`Best {Category} — {Differentiator Frame}`
- Alternative：`{Competitor} Alternative — {Why Teams Switch}`
- Announcement：`Introducing {Feature} — {Value Proposition}`

Meta description：120–160 chars · benefit + main intent keyword + 差异化一句。

---

## 5. Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "140–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: 2026-07-XX       # 发布时间，永不改变
updated: 2026-07-XX    # 可选；最近一次实质性内容更新；无更新则省略
author: "Lucius AI Team"
category: "Research | Comparison | Product"
---
```

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理）。
>
> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期（实证导致 CTR 下跌）。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

---

*article-types · v2.0.0 · 2026-07-06*
