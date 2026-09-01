---
name: today-blog-article
description: >
  Create Today AI blog articles (today.ai/blog) from brief to draft. Self-contained
  v1.0 with Mode system, Investment Score, Phase 0R research triangle, BLUF,
  Gate backtracking, Phase 3.5/5.5 cross-checks, T1-T4 gates, tools/ validators.
metadata:
  version: 1.0.0
  project: today.ai
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 600
  complements: ~
  forbidden-reads:
    - today-ai.md
    - today-ai-*.md
    - blog/README.md
    - blog/blog-live-articles.md
    - _archive/**
---

# Today AI Blog Article Creation

为 **https://today.ai/blog/** 从选题到英文成稿。**硬性规则：Agent 只读本 skill 文件夹内文件**（含 `references/`、`references/portable/`），禁止读取 skill 文件夹外文档（见 `forbidden-reads`）。发布前终审用 `references/portable/final-audit.md`。

**本文件夹自包含**：项目配置、G1–G7 + T1–T4、9 类路由、内容图谱、9 Phase 工作流、12 维 SelfCheck、tools/ 均在内。

**渐进式加载**：默认只读本文件。Phase 需要细节时按指针读取 `references/{file}.md`（一次最多 2 个）。禁止一次性加载全部 references。

**六角色换帽**：Phase 0 Strategist · 0R Researcher · 1–3 Strategist+SME · 4 Writer · 5/audit Editor

---

## §0 如何使用

### 触发语

```
按 today-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{BrandPillar|GlossaryGuide|Comparison|Alternative|UseCase|HealthcareGuide|HowTo|Opinion|Announcement} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

### 输入 / 输出

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 | ✅ | 决定 intent 与 §2 路由 |
| 文章类型 | 可选 | 未给则 Agent 推断 |
| Mode | 可选 | 默认 standard；Comparison/BrandPillar 自动 flagship |
| 集群 | 可选 | 见 content-graph.md |

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief | ✅ | ✅ | ✅ |
| 2 | Research Log | 简 | ✅ | 完整 |
| 3 | 成稿 `today/blog/[{cluster}/]NN-{slug}.md` | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表 | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | Internal Link Plan | — | ✅ | ✅ |
| 8 | 终审指令 | ✅ | ✅ | ✅ |
| 9 | Post-publish Metric Spec | — | ✅ | ✅ |
| 10 | 提示更新 blog/README.md | ✅ | ✅ | ✅ |

正文英文；与用户沟通可用中文。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化 title/description | meta skill（待建） |
| 已有完整稿仅需终审 | `references/portable/final-audit.md` |
| 非 today.ai/blog | 其他项目 skill |

---

## §1 项目配置速查

> 完整配置 → `references/project-config.md` · 竞品 → `references/product-competitors.md`

| 配置项 | Today 值 |
|--------|---------|
| 品牌 | Today AI / Today |
| 域名 | today.ai |
| 博客 | /blog/{slug} |
| 品类 | Proactive personal AI assistant with living memory |
| 阶段 | Early-access Beta · 当前免费 |
| 主 CTA | /waitlist |
| 次 CTA | /downloads |
| Pillar Hub（首建） | what-is-proactive-ai-assistant |
| 署名 | Today Team |
| 下一序号 | **01** |

### URL 白名单（内链）

`/blog/{slug}` · `/landing` · `/landing#memories|#proactive|#capabilities|#use-cases` · `/downloads` · `/waitlist` · `/privacy` · `/terms` · `/healthcare` · `/healthcare/meal-planner|sleep-tracker|fitness-coach`

### G1–G7 + T1–T4 速查

| Gate | 阻断 |
|------|------|
| G1 | 事实与现网矛盾 |
| G2 | 死链 |
| G3 | 无来源数字 |
| G4 | 竞品状态错误 |
| G5 | Beta 功能标 GA / 夸大 |
| G6 | 链未上线页 / article.today.ai |
| G7 | 贬低竞品 / 合规风险 |
| T1 | Healthcare 诊断表述 |
| T2 | 定价 / 付费 GA 承诺 |
| T3 | 未经确认的硬件/GUI Agent GA |
| T4 | 健康 claim 与 Privacy 矛盾 |

---

## §1B Mode 系统

| Mode | 适用 | 深度 |
|------|------|------|
| lite | Announcement | 最小 Research |
| standard | HowTo / UseCase / Opinion | 完整 Research + BLUF |
| flagship | BrandPillar / Comparison / HealthcareGuide | Moat + Excellence 必须 Yes |

默认 **standard**。BrandPillar / Comparison / HealthcareGuide 未指定 Mode → **flagship**。

---

## §2 文章类型路由

> 完整 H2 模板 → `references/article-types.md`

| 类型 | category | 词数 | 产品占比 | 默认 Mode |
|------|----------|------|----------|-----------|
| BrandPillar | Product | 2500–3500 | ≤40% | flagship |
| GlossaryGuide | Guide | 1800–2600 | ≤20% | standard |
| Comparison | Guide | 2200–3200 | ≤45% | flagship |
| Alternative | Guide | 2000–2800 | ≤45% | flagship |
| UseCase | Tutorial | 1500–2500 | ≤50% | standard |
| HealthcareGuide | Guide | 2200–3000 | ≤35% | flagship |
| HowTo | Tutorial | 1800–2600 | ≤40% | standard |
| Opinion | Opinion | 1500–2200 | ≤25% | standard |
| Announcement | Product | 800–1400 | 不限 | lite |

**路由**：what is → BrandPillar/Glossary · best/vs → Comparison/Alternative · for founders → UseCase · meal/sleep/fitness → HealthcareGuide · how to → HowTo

### 全类型通用模块

- `## TL;DR`（3–5 bullet，snippet 定义句）
- 编号 `## 1.` … `## N.`
- `## Conclusion` · `## Frequently asked questions`（4–6 题）
- 内链 ≥2 blog（上下文嵌入）；禁 `## Related articles`
- CTA ≤2；主 CTA → `/waitlist`

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  → Intake & Gate A (Investment Score + 必问)
Phase 0R → Research 三角 & Gate 0R
Phase 1  → Article Brief
Phase 2  → Slug/Date & Gate B
Phase 3  → Outline
Phase 3.5→ Outline 交叉检查（同批≥2篇）
Phase 4  → Draft (BLUF 三处)
Phase 5  → SelfCheck & Gate C
Phase 5.5→ Cross-Article Audit（同批≥2篇）
Phase 6  → Delivery
```

### Phase 0 首行强制输出

```
## Mode: lite | standard | flagship
## ArticleType: {CategoryPOV|SearchCapture|EvaluationComparison|ActivationTutorial|OpinionNarrative}
## InvestmentScore: {1.0–5.0}
## Topic Scope: {cluster-id}
## Author: Today Team
## Gate A: KEEP | MERGE → {slug} | STOP
```

**必问（不可跳过）**：
5. 与已有文章关系（Hub/Spoke/新 Cluster）— 对照 content-graph.md
6. 竞品 SERP Top 3 URL

Investment Score ≥4.0 KEEP · 3.0–3.9 降级 Mode · <3.0 MERGE/STOP

**Today 信息增量**（KEEP 后须 ≥1）：
- Memory / Proactive / Execution 三轴框架
- Landing demo 场景（sleep+meeting、Morning Brief）
- Beta 诚实边界 + Privacy 健康数据说明
- Healthcare lifestyle 免责（HealthcareGuide）

### Phase 0R

> `references/portable/research-triangle.md` · R1 先读 `proof-library.md`

R1 SSOT → R2 SERP Top5 → R3 Fetch Top3–5 + today.ai 官方页 → Synthesis → SERP Fit

### Phase 1 Brief

> 模板 → `references/mini-example.md`

必填：SuccessMetric · MoatAssetPlanned（standard/flagship）· AnswerBlocks 3–5 · Cluster role · Planned internal links

### Phase 2

> `references/slug-gate.md` · `references/article-types.md`

- slug 常青 kebab-case，**不含年份**
- 读 content-graph 日期表，每自然日 ≤1 篇
- 路径：`blog/[{cluster}/]NN-{slug}.md`（NN 当前从 **01** 起）

### Phase 3 / 3.5

Outline 每节标注 Answer block ID、内链占位。同批 ≥2 篇 → `references/portable/outline-cross-check.md`

### Phase 4

> `references/writing-constraints.md` · `references/product-competitors.md`

**BLUF 三处**：TL;DR 下 40–60 词 · 每 major H2 首段 · FAQ 首句即答

Comparison：三轴表 + 每竞品 ≥1 优势 + When X is better

HealthcareGuide：T1 免责 + 禁诊断词

### Phase 5

> `references/selfcheck.md` · `references/portable/gates-master.md`

**工具先跑**（从 `today/` 根目录）：

```bash
python blog/skills/today-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{kw}"
python blog/skills/today-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {type}
python blog/skills/today-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/compare,article.today.ai
```

H0–H4 + 12 维全 Pass → **audit-ready**

### Phase 6

1. 写入 `today/blog/[{cluster}/]NN-{slug}.md`
2. SelfCheck + Source Map + Internal Link Plan
3. Excellence / Moat 标注
4. 终审指令（final-audit.md）
5. 提示人类更新 `blog/README.md` + content-graph

### §3.G Gate 回溯

| Fail | 回退 |
|------|------|
| Gate A STOP/MERGE | 结束 |
| Gate 0R | 补 Research |
| Gate B | Phase 2 |
| Gate 3.5 | Phase 3 |
| Gate C 写作 | Phase 4 |
| Gate C 结构 | Phase 3 |

---

## §4 内容图谱指针

> `references/content-graph.md`

| 项 | 值 |
|----|-----|
| 下一序号 | **06** |
| 已发布 | 5（#01–#05） |
| P0 首篇 | living-memory-ai-assistant (#06) |
| 概念 Hub | what-is-ai-personal-agent (#03) · folder `personal-agent/` |
| 对比 Spoke | #04 assistant vs agent · #05 agent vs work agent |
| Brand Hub | what-is-today (#01) · 根目录 |
| 集群 | **personal-agent/** · brand（根目录） |

---

## §5 Frontmatter

```yaml
---
title: "45–65 chars"
description: "120–160 chars"
slug: "kebab-case-evergreen"
date: YYYY-MM-DD
author: "Today Team"
category: "Product | Guide | Tutorial | Opinion"
secondary_category: "Proactive | Memory | Comparison | Use Cases | Healthcare"
---
```

禁止：`keywords` · `related` · `image`

---

## §6 发布后人类 checklist

1. bump SKILL §4 下一序号
2. 更新 content-graph.md 文件表 + 日期表
3. 更新 blog/README.md + blog-live-articles.md
4. bump frontmatter `version` patch
5. sitemap 提交（主域 today.ai）

---

## Gotchas

- ❌ 链 article.today.ai 规范 URL
- ❌ slug 含年份 · ❌ 诊断类 Healthcare 词
- ❌ Beta 功能标 GA · ❌ 写具体定价
- ❌ Related articles 区块 · ❌ FAQ 复制正文
- ❌ Gate 未 Pass 交付 · ❌ 读 today-ai-*.md
- ❌ 硬件 Agent 叙事未经 T3 确认

---

## §7 Reference 索引

| 文件 | Phase |
|------|-------|
| project-config.md | 0, 5 |
| product-competitors.md | 0R, 4, 5 |
| content-graph.md | 0, 2, 3 |
| keywords.md | 0, 2 |
| article-types.md | 2, 3, 4 |
| slug-gate.md | 2 |
| internal-links.md | 3, 3.5 |
| writing-constraints.md | 4, 5 |
| proof-library.md | 0R |
| citations.md | 4, 5 |
| mini-example.md | 1, 3 |
| selfcheck.md | 5 |
| portable/* | 按 Phase 指针 |
| tools/* | 5 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.5** | 2026-09-01 | #05 重命名：office agent → **work agent**；slug `ai-personal-agent-vs-work-agent` |
| **1.0.3** | 2026-09-01 | 入库 #04 assistant vs agent、#05 agent vs office agent |
| **1.0.2** | 2026-09-01 | 入库 #03 what-is-ai-personal-agent；AI personal agent 升格为概念 Hub；三篇词数达标；next NN → 04 |
| **1.0.1** | 2026-09-01 | 入库 #01 what-is-today、#02 meet-today；优化为 skill 规范格式；next NN → 03 |

---

*today-blog-article · v1.0.3 · 2026-09-01 · self-contained · next NN: 06*
