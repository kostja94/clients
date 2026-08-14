# 博客 Meta Title & Description

> Phase 2（frontmatter）/ 独立「只改 title·description」任务时加载。  
> 仅覆盖 `/blog/{slug}`。全站其他页面（首页 / TVG / 工具 / 法务）规则已归档至 `skills/_archive/meta-title-description/`。

---

## 硬性长度（输出前必计字符）

| 字段 | 目标 | 硬上限 | 说明 |
|------|------|--------|------|
| **title** | 45–60 | 65 | editorial；Pillar 可含年份；通常 **不加** `\| Moras` |
| **description** | 140–160 | 160 | 读者将得到什么 + 主关键词（P1） |

超限 = 未完成。输出时标注实际字符数。

---

## 核心原则（主题–关键词强相关）

| 规则 | 说明 |
|------|------|
| **一页一词一组** | title/description 的 P1 来自该文 `content-graph` 主关键词或 Brief |
| **主题词入 title** | 文章核心主题必须在 title 中显性出现 |
| **description 展开** | 写该文独有框架/路径/诊断结果，不整句重复 title |
| **与 H1 同主题** | frontmatter `title` = 页面 H1；SERP 与正文同一件事 |
| **美区限定** | TikTok Shop 文 description 宜含 US TikTok Shop 或等价语义 |
| **联盟客优先** | 默认面向 affiliate；seller 不作 title 主称谓（品牌 ICP 文如 #09 除外） |
| **品牌** | 博客通常不加 `\| Moras`；若加品牌仍用 `{Title} \| Moras` |
| **Moras 提及** | 主题相关时在 description 轻提；避免硬广；**不写收益保证 / GMV 数字承诺** |
| **唯一性** | 全站无 duplicate title/description |

**自检（四条）**：

1. 若去掉品牌名，title 能否让人猜出 **这是哪一篇**？
2. description 是否至少含 **1 个该文专属主题词**？
3. P1 是否在 title 中出现？读者收益是否在 description 中？
4. title ≤65、description ≤160？

---

## Title vs Description 分工

| | 职责 |
|--|------|
| **Title** | 搜索意图标签 + 主题词（名词性 / how-to / framework 句式） |
| **Description** | 「读完能做什么」+ 主关键词变体 + 可选轻提 Moras |

Description 用 generate / diagnose / map / compare 等 **动词变体**，勿整句重复 title。  
博客 description **一般不加** `Download Moras.`（工具/TVG 页才用硬 CTA）。

---

## Frontmatter = SERP metadata

```yaml
---
title: "How to Make TikTok Shop Videos Without Filming in 2026"
description: "Four paths for TikTok Shop videos without filming—from AI voiceover to product-link automation, with cost and conversion benchmarks."
slug: "/blog/faceless-tiktok-shop-videos"
date: "June 11, 2026"
isoDate: "2026-06-11"
updated: "2026-06-11"
author: "Kostja"
---
```

| 项 | 规则 |
|----|------|
| title | = H1；45–65 chars；通常不加 `\| Moras` |
| description | 140–160 chars |
| slug | 常青；已含 `/blog/`；**不含年份** |
| 集群 | metadata 不抢同簇其他文的 P1 |

**公式示例**：

- Pillar：`How to Make Money on TikTok in 2026`
- Production：`How to Make TikTok Shop Videos Without Filming in 2026`
- Framework：`TikTok Shop Hooks That Actually Convert: A Framework, Not a List`
- Diagnosis：`Why You Are Not Making Sales on TikTok Shop — A Diagnosis Framework`

**新文 Fallback**：从 Brief working title / 首屏主题提炼；description = 读完能做什么 + 1 个主关键词。

P1 清单见 `content-graph.md` §4.1；标题角度随类型（Pillar / Setup / Framework…）见 `article-types.md`。

---

## Cannibalization（博客侧）

| 对比 | 博客 metadata | 对方 |
|------|---------------|------|
| vs TVG Vertical | how-to / framework 教育意图 | `{category} + AI TikTok generator` 交易意图 |
| vs `/product-research` 等工具页 | guide / framework P1 | transactional tool P1 |
| vs 同簇 Spoke | 各文 P1 侧重不同意图，不互抢同一主词 |

完整表见 `product-competitors.md` §6.5。

---

## 独立任务工作流（只改 title/description）

1. 读目标 `.md` 的 frontmatter + H1/TL;DR（确认主题）
2. 查 `content-graph.md` 主关键词；对照 cannibalization
3. Draft title + description → **计字符**
4. 跑四条自检 + 合规（无收益保证、US-only、Affiliate-first）
5. **只改** frontmatter `title` / `description`（及必要时 `updated`）；禁止改 H2 / TL;DR / FAQ / 正文

### Output Format

```markdown
### {Article} — `{/blog/slug}`

**Primary keyword (P1)**: …

**Recommended title** ({n} chars)
> …

**Recommended meta description** ({n} chars)
> …

**Theme-keyword fit**: {1 sentence}
**Notes**: {cannibalization / compliance}
```

批量：表格列 `slug | Title (chars) | Description (chars)`。

### GSC（可选）

高展示低 CTR → 优先改 title/description → 2–4 周再看；用实际 query 校正 P1，避免频繁改动。

---

*迁自 archived `moras-meta-title-description` v1.2.1 · 仅保留博客相关规则*
