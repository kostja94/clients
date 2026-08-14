---
name: clink-blog-article
description: >
  Create Clink blog articles (clinkbill.com/blog) from brief to draft.
  Covers BrandIntroduction, Comparison, Product, Opinion, EvaluationComparison,
  and GlossaryTerm (category: Glossary). v1.0 adds Mode system, Phase 0R Research,
  Investment Score, BLUF, Gate backtracking, tools.
metadata:
  version: 1.0.0
  project: clinkbill.com
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 600
  complements: ~
  forbidden-reads:
    - ../clink.md
    - ../clink-*.md
    - ../blog/README.md
---

# Clink Blog Article Creation

为 **https://clinkbill.com/blog/** 从选题到英文成稿。**硬性规则：Agent 只读本 SKILL + `references/`（含 `references/portable/`），禁止读 skill 文件夹外文档。**

**渐进式加载**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md`（一次最多 2 个）。读完用完即弃——不跨 Phase 保留 reference 上下文。禁止一次性加载全部 references。

**六角色换帽**（同一 Agent 分 Phase 执行）：

| Phase | 角色 |
|-------|------|
| 0 | Strategist |
| 0R | Researcher |
| 1–3 | Strategist + SME |
| 4 | Writer |
| 5 / audit | Editor / Auditor |

---

## §0 如何使用

### 触发语

```
按 clink-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{BrandIntroduction|Comparison|Product|Opinion|EvaluationComparison|GlossaryTerm} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{全球 SaaS / AI-native / 支付工程师}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

> **GlossaryTerm**：财务/计费术语定义文（如 burn rate、ARR、MRR、runway）。路径仍为 `/blog/{slug}`，frontmatter `category: Glossary`，**slug 用纯术语全称 kebab-case（不加 `what-is-` 前缀、不用缩写，如 `burn-rate`、`monthly-recurring-revenue`）**，Clink 占比 ≤15%、FAQ 前 ≤3 段。路由见 §2。

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | 未指定→**standard**；BrandIntroduction/Comparison/EvaluationComparison 默认 flagship |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |

### 输出（交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief（含 SuccessMetric、MoatAssetPlanned、AnswerBlocks） | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ 完整 |
| 3 | 成稿 `clink/blog/NN-{slug}.md`（NN 见 content-graph，当前 **05**） | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表（Hard Gates + 12 维 Pass/Fail） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | OG Image Prompt（1200×630） | ✅ | ✅ | ✅ |
| 8 | Internal Link Plan（正文互链） | — | ✅ | ✅ |
| 9 | templates 审核指令（复制即用） | ✅ | ✅ | ✅ |
| 10 | Post-publish Metric Spec | — | ✅ | ✅ |
| 11 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通策略说明可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `clink-meta-title-description` |
| 非 clinkbill.com 博客 | 对应项目的 blog skill |
| 中文站内容 | 另建 ZH skill |
| 已发稿回溯审计 | `references/portable/retro-audit.md`（若存在）或 `final-audit.md` |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + C1–C4 + URL 白名单 → `references/project-config.md`**
> Phase 0R 加载。Phase 4/5 按需重载。

| 配置项 | Clink 值 |
|--------|---------|
| **品牌/产品名** | Clink |
| **主域名** | clinkbill.com |
| **文档** | docs.clinkbill.com |
| **博客路径前缀** | `/blog/` |
| **产品定位** | Payment Infrastructure for an AI-Native World |
| **品类 one-liner** | Subscription billing + multi-PSP orchestration + tax + agent payments |
| **四产品线** | Global Payments · Smart Routing · Billing · Clink for Claw |
| **目标用户** | 全球 SaaS、AI-native、支付/RevOps 工程师 |
| **接入** | Contact Sales（无公开定价页，截至 2026-06） |
| **署名默认** | `Clink Team` |
| **语言** | 英文正文；中文仅沟通用 |
| **禁止内链** | `/vs/*`、`/pricing`、`/for/*`、`/learn/*`、`/customers/*` |

### G1–G7 + C1–C4 阻断速查

| # | 阻断条件 |
|---|---------|
| G1 | 事实错误 |
| G2 | 死链 |
| G3 | 无来源数字 |
| G4 | 竞品状态错误 |
| G5 | 产品能力夸大 |
| G6 | 内链未上线页面 |
| G7 | 品牌风险 / 贬低竞品 |
| C1 | 无来源的具体 Clink 费率 |
| C2 | MoR/tax 超范围 claim 无限定语 |
| C3 | 证言夸大无 as-of |
| C4 | Clink for Claw 未标 Early Access |

### 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇 |
| **错开方向** | 从锚点日往前排 |
| **避让** | 对照 `content-graph.md` 日期表 |

---

## §1B Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | 短帖、轻量更新 | 最小 Research + BLUF |
| **standard** | Product / Opinion | 完整 Research 三角 |
| **flagship** | BrandIntroduction / Comparison / EvaluationComparison | 全流程 + Moat + Excellence |

默认：用户未指定 → **standard**。ArticleType 路由表指定默认 Mode。

---

## §2 文章类型路由

> **5 类路由表 + H2 模板 → `references/article-types.md`**
> Phase 0 加载路由表。Phase 3/4 加载模板。

### 路由速查

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | 增长职能 |
|------|--------|------|:---:|:---:|------|
| BrandIntroduction | 品牌/定义 | 2500–3500 | ≤30% | flagship | CategoryPOV |
| Comparison | 商业调查 | 2500–3500 | ≤35% | flagship | EvaluationComparison |
| Product | 产品/场景 | 2200–3200 | ≤40% | standard | SearchCapture |
| Opinion | 趋势/POV | 2000–2800 | ≤35% | standard | CategoryPOV |
| EvaluationComparison | vs 竞品 | 2500–3500 | ≤45% | flagship | EvaluationComparison |
| **GlossaryTerm** | 财务/计费术语定义 | 2200–3200 | **≤15%** | standard | SearchCapture |

**路由**：`what is clink`→BrandIntroduction · `X vs Y`→Comparison · `clink vs`/`alternative`→EvaluationComparison · routing/churn→Product · agent economy→Opinion · `what is` + 财务指标（burn rate/ARR/MRR/churn 等）→**GlossaryTerm**

### 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullet；bullet 1 为 snippet 定义句 |
| **H2** | 英文描述性标题；**不编号** |
| **FAQ** | **固定 6 题**（2026-08-11 定标）；`## FAQ`；**全部内容相关**（基于本文主题，禁止通用模板题）；≥1 题覆盖边界/异议；**前一节必须为 `## Conclusion`** |
| **CTA** | Contact Sales / docs；≤2 次 |
| **内链** | blog 正文互链 ≥2 |

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  ─ Intake & Gate A         (§3.0：Mode + Investment Score + 六必问)
    ↓ PASS
Phase 0R ─ Research 三角 & Gate 0R  (§3.0R：R1→R2→R3→Synthesis)
    ↓ PASS / ❌ → §3.G 回溯
Phase 1  ─ Article Brief           (§3.1)
Phase 2  ─ Slug、Date & Gate B     (§3.2)
    ↓ PASS / ❌ → §3.G 回溯
Phase 3  ─ Outline                 (§3.3)
Phase 3.5─ Outline 交叉检查        (§3.3.5：同批 ≥2 篇强制)
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft                   (§3.4)
    ↓
Phase 5  ─ SelfCheck & Gate C      (§3.5：H0–H4 + C1–C4 + 12 维)
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit     (§3.5.5：同批 ≥2 篇强制)
Phase 6  ─ Delivery                (§3.6)
```

---

### Phase 0 — Intake & Gate A

> **Investment Score → `references/portable/investment-score.md`**
> **Gate 细则 → `references/gates.md`**

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: BrandIntroduction | Comparison | Product | Opinion | EvaluationComparison
## InvestmentScore: {1.0–5.0} — {五因子摘要}
## Category: {Product | Comparison | Opinion}
## Author: Clink Team
## Gate A: KEEP | MERGE → {target slug} | STOP
```

#### Investment Score

五因子各 1–5，取算术平均。≥4.0 KEEP 声明 Mode；3.0–3.9 降级 Mode；<3.0 MERGE/STOP。

#### 六必问

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 目标受众？ |
| 2 | 发布目的（品牌 / SEO / 转化）？ |
| 3 | SERP Top 3 竞品 URL？ |
| 4 | 内链页面是否已上线？ |
| 5 | 与已有文章 / pipeline 关系？ |
| 6 | category：Product / Comparison / Opinion？ |

#### KEEP / MERGE

三条件满足任意两个 → KEEP；对照 `content-graph.md` 冲突表。

---

### Phase 0R — Research 三角 & Gate 0R

> **→ `references/portable/research-triangle.md`**
> **→ `references/portable/serp-fit-template.md`**

```
R1 — 读 project-config + product-competitors + content-graph
R2 — Web 搜索 primary keyword → SERP Top 5 + PAA
R3 — Fetch clinkbill.com / docs + SERP Top 3–5
Synthesis + Candidate Examples
→ Research Log + SERP Fit → Gate 0R
```

**Degraded**：R2/R3 缺失时标注；正文不得写未验证 P0 claim。

---

### Phase 1 — Article Brief

> **→ `references/mini-example.md`**

须含：Mode、ArticleType、InvestmentScore、SuccessMetric、MoatAssetPlanned、AnswerBlocks、Synthesis、Information increment ≥2、Planned internal links、Slug candidate。

---

### Phase 2 — Slug、Date & Gate B

> **→ `references/slug-gate.md`**

1. 产出 2–3 slug 候选 + 推荐
2. 确定 publishDate（避让 content-graph 已占用日）
3. Gate B：6 问全 Pass

---

### Phase 3 — Outline

> **→ `references/article-types.md`**
> **→ `references/internal-links.md`**

每节标注目标词数、Reader mental state、内链占位、Answer block ID。生成 OG Image Prompt（1200×630）。

---

### Phase 3.5 — Outline 交叉检查

同批 ≥2 篇强制。单篇：`N/A — single article`。

> **→ `references/portable/outline-cross-check.md`**

---

### Phase 4 — Draft

> 每次 ≤2 文件：`writing-constraints.md` → `product-competitors.md` → `project-config.md`

#### BLUF 三处

| # | 位置 |
|---|------|
| B1 | TL;DR bullet 1 |
| B2 | 每个 major H2 首段 |
| B3 | FAQ 每问首句 |

#### 核心约束速查

- 英文正文；H2 不编号
- P0 数字有来源或 as-of；C1–C4 合规
- 长段 ≥3；伪列表 = Fail
- blog 互链 ≥2；forbidden URL = Fail
- 竞品每项 ≥1 优势
- 模块：YAML → TL;DR → H2… → Conclusion → FAQ（必须为最后两节：Conclusion 然后 FAQ）

---

### Phase 5 — SelfCheck & Gate C

> **→ `references/selfcheck.md`**

#### 工具先跑

```bash
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{primary kw}"
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {brand|comparison|product|opinion|evaluation}
python tools/link_checker.py ../../blog/NN-{slug}.md --forbidden /vs/,/pricing,/for/,/learn/,/customers/
```

#### Hard Gates

| # | 检查项 |
|---|--------|
| H0 | Research 三角完整 |
| H1 | G1–G7 零触发 |
| H2 | Slug Gate B Pass |
| H3 | 词数达类型下限 |
| H4 | C1–C4 + 产品占比 + Conclusion→FAQ 结构 |

**Gate C**：H0–H4 + 12 维全 Pass → audit-ready。

---

### Phase 5.5 — Cross-Article Audit

同批 ≥2 篇强制。检查叙事雷同、互链、canonical 越界。

---

### Phase 6 — Delivery

1. 写入 `clink/blog/NN-{slug}.md`
2. Article Brief 最终版 + SelfCheck + Source Map
3. OG Image Prompt + Internal Link Plan
4. Excellence / Moat 兑现检查
5. **templates 审核指令**：

```
请按 references/portable/final-audit.md 审核 clink/blog/NN-{slug}.md

项目配置：
- 品牌：Clink
- 主域名：clinkbill.com
- 博客前缀：/blog/
- 受众：全球 SaaS、AI-native、支付工程师
- 禁止内链：/vs/*、/pricing、/for/*、/learn/*、/customers/*

要求：
1. 先过 P0 Gate G1–G7 + C1–C4
2. 逐维评分（A–J 十维加权 → 100 分）
3. 输出等级 + Excellence + Moat + Perfect gap
```

6. **提示人类**更新 `blog/README.md`；金融合规 claim 建议法务审定

---

### §3.G — Gate 失败回溯表

| Gate / 结果 | 回退至 |
|-------------|--------|
| Gate A → STOP/MERGE | 流程结束或改选题 |
| Gate 0R ❌ | Phase 0R |
| Gate 3.5 ❌ | Phase 3 |
| Gate B ❌ | Phase 2 |
| Gate C 写作/事实 | Phase 4 |
| Gate C 结构 | Phase 3 |
| Gate C Slug/Meta | Phase 2 |

---

## §4 已有内容图谱

> **→ `references/content-graph.md`**

15 篇文章 · 下一序号 **16** · Hub：`what-is-clink`（GlossaryTerm 簇闭环：MRR↔ARR↔NRR↔burn-rate↔runway）

Pipeline：`payment-orchestration-single-psp` · `clink-vs-stripe` · `reduce-involuntary-churn-routing`

---

## §5 Frontmatter 与文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{slug-kebab}.md` |
| NN | 两位递增；下一号 **05** |
| image | `/blog/images/{slug}.jpg` |

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars preferred; benefit + keyword"
slug: "kebab-case-slug"
date: "2026-07-XX"
updated: "2026-07-XX"
category: "Product | Comparison | Opinion | Glossary"
author: "Clink Team"
readingMinutes: 12
---
```

---

## §6 本 skill 内文档分工

| 阶段 | 文档 |
|------|------|
| Phase 0 Intake | 本 SKILL §3.0 + `gates.md` + `investment-score.md` |
| Phase 0R | `portable/research-triangle.md` |
| Phase 1 Brief | `mini-example.md` |
| Phase 2–3 | `article-types.md` + `slug-gate.md` + `internal-links.md` |
| Phase 4 Draft | `writing-constraints.md` + `product-competitors.md` |
| Phase 5 | `selfcheck.md` + `tools/` |
| 终审 | `portable/final-audit.md` |

---

## Reference Index

| 文件 | 加载时机 |
|------|----------|
| `references/project-config.md` | 0R / 4 / 5 |
| `references/article-types.md` | 0 / 2 / 3 |
| `references/gates.md` | 0 / 1 / 2 / 5 |
| `references/writing-constraints.md` | 4 |
| `references/selfcheck.md` | 5 |
| `references/content-graph.md` | 0 / 0R / 1 / 5 |
| `references/internal-links.md` | 3 / 3.5 / 5 |
| `references/keywords.md` | 0 / 0R |
| `references/glossary-terms.md` | 0（GlossaryTerm 选题） |
| `references/product-competitors.md` | 0R / 4 |
| `references/mini-example.md` | 1 / 3 |
| `references/slug-gate.md` | 2 |
| `references/portable/*` | 按指针 |
| `tools/*` | Phase 5 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.0** | 2026-07-21 | 初版：完整 Mode + Phase 0R + Gate + tools；5 类路由；C1–C4 |

---

*clink-blog-article · v1.0.0 · 2026-07-21 · clinkbill.com/blog*
