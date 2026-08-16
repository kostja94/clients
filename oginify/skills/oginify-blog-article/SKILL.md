---
name: oginify-blog-article
description: >
  Create Oginify blog articles (oginify.com/blog) from brief to draft.
  Covers Ranking/Comparison, HowTo, Glossary/Research, SizeGuide, MetaGuide,
  Alternative, ToolGuide, DeveloperGuide, UseCase, TrendAnalysis,
  OpenSourceGuide, and Announcement for the Open Graph image category.
  Covers Track S (strategic SEO) and Track T (tool/reference long-tail).
  Do NOT load for title/description-only tasks (future oginify-meta-title-description).
metadata:
  version: 1.0.4
  project: oginify.com
  locale: en
  market: B2B2C founders/marketers/devs (global)
  load-rule: progressive-disclosure
  max-primary-lines: 560
  self-contained: true
  forbidden-reads:
    - oginify.md
    - oginify-*.md
    - blog/README.md
    - blog/blog-structure-internal-links.md
---

# Oginify Blog Article Creation

为 **https://oginify.com/blog/** 从选题到英文成稿。**范围**：英文 `/blog/{slug}`，双轨 Track S（战略 SEO）+ Track T（工具/参考长尾）。**硬性规则**：Agent 执行本 skill 时只读本 skill 文件夹内文件（含 `references/`、`references/portable/`、`tools/`、`evals/`），禁止读取 skill 文件夹外的仓库文档（`oginify.md`、`oginify-*.md`、`blog/README.md` 等，见 `forbidden-reads`）。

**本文件夹自包含**：项目配置、G1–G7 + P1–P6 + C1–C4 阻断规则、12 类路由、内容图谱、引用分级、碎片化防护、双轨工作流、加权 12 维评分、evals 回归套件、tools/ 验证脚本均在内联或 `references/` 中。

**渐进式加载（硬性）**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md`（一次最多 2 个）。读完用完即弃——不跨 Phase 保留 reference 上下文。禁止一次性加载全部 references。

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
按 oginify-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Ranking|Comparison|HowTo|Glossary|SizeGuide|MetaGuide|Alternative|ToolGuide|DeveloperGuide|UseCase|TrendAnalysis|OpenSourceGuide|Announcement} 文章。
Track：{S|T|auto}。发布目的：{SEO|品牌|转化|趋势}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Track | 可选 | 未给则 Agent 按 §2 路由（Ranking/HowTo/Glossary→S；SizeGuide/ToolGuide→T） |
| Mode | 可选 | 未指定→**standard**；Ranking/Comparison/Glossary 自动 flagship |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |

### 输出（Phase 6 交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief（含 SuccessMetric、MoatAssetPlanned、AnswerBlocks） | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ 完整 |
| 3 | 成稿 `oginify/blog/NN-{slug}.md`（NN 见 content-graph，当前 **05**） | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表（Hard Gates + 12 维加权评分） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | OG Image Prompt（1200×630，oginify.com/blog 专用） | ✅ | ✅ | ✅ |
| 8 | Internal Link Plan | — | ✅ | ✅ |
| 9 | Post-publish Metric Spec | — | ✅ | ✅ |
| 10 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通策略说明可用中文；**正文必须为英文**（上线稿）。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `oginify-meta-title-description` |
| 非 oginify.com 博客 | 对应项目的 blog skill |
| 中文站内容 | 另建 ZH skill |
| 已发稿回溯审计 | `references/retro-audit.md` |
| 产品页/落地页文案 | 非博客渠道 |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + C1–C4 + URL 白名单 → `references/project-config.md`**
> **产品事实 + 竞品矩阵 → `references/product-competitors.md`**
> **P1–P6 Proof Gate → `references/proof-gate.md`**

**Phase 0 / Phase 5 前加载 project-config + proof-gate。** 核心速查：

| 配置项 | Oginify 值 |
|--------|-----------|
| **品牌/产品名** | Oginify |
| **主域名** | oginify.com |
| **博客路径前缀** | /blog/ |
| **品类 one-liner** | Open Graph cards, instantly — AI OG image generator from any URL |
| **核心机制** | 粘贴 URL → 读取页面品牌色/标题/logo/语气 → 4 张 1200×630 卡片（1 on-brand + 3 wildcards） |
| **作者/创始人** | Kostja（alignify.co）· Built with Lovable |
| **开源版** | social-cards-skills（MIT）— 同一引擎的 Agent Skills 发行版 |
| **目标用户** | 独立创始人 / 内容营销 / 开发者（需快速发布链接分享卡片者） |
| **署名默认** | `Oginify`（作者池：Kostja / Oginify Team） |
| **语言** | 英文正文；中文仅沟通用 |
| **日期策略** | 一天一篇；错开日期 |

### 可链接 URL 白名单（内链优先）

| 类型 | 路径示例 |
|------|---------|
| 博客 | `/blog/{slug}` — 见 `references/content-graph.md` |
| 首页 | `/` |
| 免费工具 | `/text-to-og-image` · `/image-to-og-image` · `/bulk-og-image-generator` · `/twitter-card-generator` · `/github-social-preview-generator` |
| 免费检查 | `/og-scorer` · `/open-graph-validator` · `/free-og-image-maker` |
| 探索 | `/pages/{page-type}` · `/websites/{site-type}` · `/styles/{style}` · `/gallery` · `/explore` |
| 集成/用例 | `/integrations` · `/use-cases` |

**G6 规则**：不链未上线路径；forthcoming ≤1 且仅脚注；正文核心流程不用 forthcoming 链接。

### G1–G7 + P1–P6 + C1–C4 阻断速查

| # | 阻断条件 | 说明 |
|---|---------|------|
| G1 | 事实错误 | 产品能力、免费额度、定价与 oginify.com 现网矛盾 |
| G2 | 死链 | 内链 404；产品页路径错误 |
| G3 | 无来源数字 | 量化 claim 无 attribution（6 张/天、$0.99、$7.90、$29、竞品定价） |
| G4 | 竞品/产品状态错误 | GA/Beta/Deprecated 与官方公告矛盾 |
| G5 | 产品能力夸大 | 禁「唯一支持」「全球首个」「唯一能生成」 |
| G6 | 内链指向未上线页面 | 对照 §1.3 白名单；forthcoming >1 → Fail |
| G7 | 品牌/合规风险 | 对比文贬低竞品；无来源的 CTR 承诺 |
| P1 | 产品数字无 as-of | 免费额度/定价/生成时长 claim 无 `as of {month} {year}` |
| P2 | URL-first vs prompt 边界错误 | 将通用生图（Gemini/GPT Image/Midjourney）写成「不适用于 OG」；或将 Oginify 写成「唯一无需 prompt」 |
| P3 | 1200×630 规格无来源 | 尺寸 claim 无官方来源（oginify.com 或 ogp.me） |
| P4 | SaaS vs 开源混淆 | social-cards-skills 与 Oginify 边界写错（开源版自带模型/资产，SaaS 托管） |
| P5 | 竞品不公平 | Comparison/Alternative 缺竞品 ≥1 真实优势；或缺 ≥1 非 Oginify 更合适场景 |
| P6 | 禁夸大措辞 | magic / zero-work / promptless / 自动提升 CTR 至 300% 等无来源承诺 |
| C1 | slug 冲突未声明 | 与 content-graph 冲突表重叠未声明 |
| C2 | Hub 抢词 | 新稿 title/H1 抢 `what-is-open-graph-image` Hub 的 P0 词 |
| C3 | 程序化页 duplicate | 与 `/free-og-image-maker` 等工具页内容重复 |
| C4 | 301 目标冲突 | slug 已被 301 到别处仍新建 |

---

## §1B 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **错开方向** | 从锚点日**往前**排，越重要的文章排越近 |
| **避让已占用日** | 已有文章的日期不重复使用 |

---

## §1C Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Announcement、短帖、低风险文 | 最小 Research + BLUF；不追求 Excellence |
| **standard** | HowTo / Alternative / UseCase / ToolGuide | 完整 Research 三角 + Extractability |
| **flagship** | Ranking / Comparison / Glossary / DeveloperGuide | 全流程 + Moat + Excellence **必须 Yes** |

默认：用户未指定 → **standard**。ArticleType 路由表指定默认 Mode。

---

## §2 文章类型路由

> **12 类路由表 + H2 模板 + Frontmatter → `references/article-types.md`**

收到任务后**先匹配类型**，再跳转对应 H2 模板与约束。

| 类型 | 触发 | 词数 | 产品提及 | 默认 Mode | Track | 增长职能 | 参考 slug |
|------|------|------|:---:|:---:|:---:|------|-----------|
| **Ranking / Comparison** | `best` / `top` + ≥3 竞品 | 2400–3400 | ≤40% | flagship | S | SearchCapture | `best-ai-og-image-generators`（#01） |
| **HowTo / Tutorial** | `how to` + OG 生成步骤 | 2000–3000 | ≤40% | standard | S | ActivationTutorial | `how-to-create-open-graph-image` |
| **Glossary / Research** | `what is open graph image` | 2000–3200 | ≤20% | flagship | S | CategoryPOV | `what-is-open-graph-image`（Hub） |
| **SizeGuide / Reference** | `og image size` / `twitter card size` | 1200–2000 | ≤15% | lite | T | SearchCapture | `open-graph-image-size` |
| **MetaGuide** | `og:image meta tags` / validator | 1500–2500 | ≤30% | standard | S | ActivationTutorial | `open-graph-meta-tags-guide` |
| **Alternative** | `vs vercel og` / `alternative` | 2200–3000 | ≤45% | standard | S | SearchCapture | `oginify-vs-vercel-og` |
| **ToolGuide** | `free og image maker` / `bulk generator` | 1000–1800 | ≤35% | lite | T | ActivationTutorial | `bulk-og-image-generator` |
| **DeveloperGuide** | `dynamic og image next.js` / `API` / `social-cards-skills` | 2000–3000 | ≤35% | flagship | S | EvaluationComparison | `social-cards-skills-guide` |
| **UseCase / Scenario** | `launch feature` / `refresh blog` | 1500–2500 | ≤50% | standard | S | ActivationTutorial | `refresh-blog-og-images` |
| **TrendAnalysis** | `og image CTR` / `2026 趋势` | 1800–2600 | ≤25% | standard | S | CategoryPOV | `og-image-click-through-rate` |
| **OpenSourceGuide** | `social-cards-skills` / `open source og` | 1500–2500 | ≤50% | standard | S | EvaluationComparison | `social-cards-skills-guide` |
| **Announcement** | 产品发布/更新 | 1200–1800 | 不限 | lite | S | OpinionNarrative | `oginify-twitter-card-generator` |

**路由规则**：

- `best` / `top` + ≥3 具名竞品 → **Ranking**（编号 H3 + `articleFormat: Ranking`）
- `vs` / 双产品 head-to-head → **Comparison / Alternative**
- `how to` + 端到端步骤 → **HowTo**
- `what is` / `meaning` → **Glossary**
- `size` / `dimensions` / `dimension` → **SizeGuide（Track T）**
- `meta tags` / `validator` / `test` → **MetaGuide**
- `free tool` / `bulk` / `twitter card` / `maker` → **ToolGuide（Track T）**
- `next.js` / `API` / `satori` / `vercel` / `open source` → **DeveloperGuide**
- `CTR` / `click-through` / `share` → **TrendAnalysis**
- 产品发布/更新 → **Announcement**

### 增长职能

| 职能 | 核心目标 | 成功指标（Brief 必填） |
|------|---------|---------------------|
| **CategoryPOV** | 建品类认知（AI OG image generation） | 被引用/转发、品牌搜索增长 |
| **SearchCapture** | 承接明确搜索需求（best / size / how to） | 排名、CTR、低跳出 |
| **EvaluationComparison** | 影响选型（Oginify vs 通用生图 / vs Vercel OG） | 注册、生成量 |
| **ActivationTutorial** | 帮用户上手（paste URL → ship card） | 生成量、免费额度使用率 |
| **OpinionNarrative** | 建立品牌人格（Announcement） | 社区讨论、Newsletter 订阅 |

### 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 紧跟 H1、正文最上方；3–5 bullet；独立传达 ~80% 价值；bullet 1 = snippet 定义句 |
| **H2** | 编号 `## 1.` … `## N.`；Conclusion/FAQ 不编号 |
| **Conclusion** | `## Conclusion`；CTA → `/` 或对应工具页 |
| **FAQ** | `## Frequently asked questions`；**固定 6 题**；全部内容相关；≥1 题覆盖边界/异议 |
| **CTA** | 单一主行动（`/` 或工具页），正文 ≤2 次 |
| **内链** | 全部为**上下文内链**；blog ≥2 互链；Spoke 链回 Hub `what-is-open-graph-image` |
| **外链** | 权威 2–5；竞品 `rel="nofollow noopener"` |
| **三分类** | Comparison/Ranking/Alternative 须含 URL-first / 通用生图 / 代码驱动 三分类框架 |

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
Phase 3.5─ Outline 交叉检查        (§3.3.5：同批 ≥2 篇强制；单篇跳过)
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft                   (§3.4)
    ↓
Phase 5  ─ SelfCheck & Gate C      (§3.5：H0–H4 + 加权 12 维)
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit     (§3.5.5：同批 ≥2 篇强制)
Phase 6  ─ Delivery                (§3.6)
```

---

### Phase 0 — Intake & Gate A

> **Investment Score 细则 → `references/portable/investment-score.md`**
> **Gate 细则 → `references/portable/gates-master.md`**

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## Track: S | T
## ArticleType: {见 §2}
## InvestmentScore: {1.0–5.0 均分} — {五因子摘要}
## Topic Scope: og-image / {cluster}
## Author: {Oginify | Kostja | {具体成员}}
## Gate A: KEEP | MERGE → {target slug} | STOP
```

#### 0.1 信息收集（先从触发语提取，缺一再问）

| # | 信息项 | 来源 | 何时问 |
|---|--------|------|--------|
| 1 | 主关键词 + 搜索意图 | 触发语 | 未给或模糊时问 |
| 2 | 文章类型 | 触发语 / §2 推断 | 未给时 Agent 自行推断并告知 |
| 3 | Track | 触发语 / §2 推断 | 未给时 Agent 按 §2 路由推断 |
| 4 | 目标读者 | 触发语（默认 ICP） | 未给时默认目标用户 |
| 5 | 发布目的 | 触发语 | 未给时默认 SEO |
| 6 | 竞品 SERP Top 3 URL | **必问** | 每次确认；供 Phase 0R R3 Fetch |

必问项（5、6）不可跳过。用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

#### 0.2 Investment Score（选题投资分）

五因子各 1–5，取**算术平均**：

| 因子 | 1 分 | 5 分 |
|------|------|------|
| 搜索需求 | 几乎无搜索量 | 稳定或上升 |
| 商业相关性 | 与 ICP/产品路径无关 | 靠近生成/注册路径 |
| 差异化能力 | 只能复述 SERP | 有 Moat / Proof 可引用 |
| 证据可得性 | 无法验证强 claim | R3 可支撑 |
| 内容生命周期 | <3 月过时 | 2+ 年常青 |

| 均分 | 动作 |
|------|------|
| **≥4.0** | KEEP，按声明 Mode 执行 |
| **3.0–3.9** | KEEP 但**降级 Mode** 或改角度 |
| **<3.0** | MERGE / STOP / 降级为 FAQ·短帖 |

#### 0.3 Gate A — KEEP/MERGE

三条件满足 ≥2 → KEEP；否则 MERGE 到已有 slug 或 STOP。

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与已有 slug 关键词重叠 ≤50%（对照 `content-graph.md` 冲突表） |
| 读者旅程阶段不同 | Awareness → Tool selection → Build → Publish → Diagnosis |
| 深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

#### 0.4 信息增量 Gate（KEEP 后预检）

相对 SERP Top 3，本篇须至少提供 **1 项** Oginify 独有增量（**Phase 0R 须用 R2+R3 验证**）：

- URL-first vs 通用生图（Gemini/GPT Image/Midjourney）vs 代码驱动（Vercel OG）三分类决策框架
- 1200×630 规格 + 各平台裁剪行为时效段落（含 `as of {month} {year}`）
- Wirecutter 式对比表（≥1 竞品优势 + ≥1 非 Oginify 更合适场景）
- 免费额度/定价 as-of 表（6 张/天、$0.99、$7.90、$29）

---

### Phase 0R — Research 三角 & Gate 0R

> **完整 Research 三角 → `references/portable/research-triangle.md`**
> **SERP Fit 模板 → `references/portable/serp-fit-template.md`**

**加载**：`references/proof-library.md`（R1 第一步）

```
R1 — 读项目文档（project-config + product-competitors + content-graph + proof-library）
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（官方页 oginify.com + SERP Top 3–5 原文提取）
    ↓
Synthesis Statement（洞察合成）+ Candidate Examples（≥1）
    ↓
输出 Research Log + SERP Fit 表
    ↓
Gate 0R Pass → Phase 1 Brief
```

**Mode 差异**：

| R 步骤 | lite | standard | flagship |
|--------|------|----------|----------|
| R2 Top5 | 可选 | ✅ | ✅ |
| R3 Top3–5 | 可选 | Top3 | Top5 + 官方页 |
| Synthesis | 简版（1–2 句） | 完整 | 完整 + Moat 验证 |
| Candidate Examples | 0–1 | ≥1 | ≥2 |

**Gate 0R-6**：One-line thesis 不得在 SERP Top5 找到同句。

**Oginify 降级**（WebSearch 不可用）：标注 `Research mode: Degraded`；用 Phase 0 竞品 URL + `content-graph` 推演 SERP Fit；Top pages 填 `[estimated from known competitors]`；Gate 0R 仍可 Pass，SelfCheck H0 注明 Degraded；政策/定价类 P0 claim 不得写未验证数字。

**Gate 0R 阻断**：R2 未搜 / R3 未 Fetch / 无 Synthesis / 事实不可验证且需写 P0 claim → 回退补 R2/R3 或 STOP。

---

### Phase 1 — Article Brief

> **Brief 模板 + 示例 → `references/mini-example.md`**

```markdown
## Article Brief

**Mode**: lite | standard | flagship
**Track**: S | T
**ArticleType**: {见 §2}
**InvestmentScore**: {1.0–5.0}
**SuccessMetric**: {可量化，来自 §2 增长职能表}
**MoatAssetPlanned**: {类型，standard/flagship 必填}
  — 可选：一手产品经验 / 原创三分类框架 / 具名 workflow / 时效定价表
**AnswerBlocks**（3–5 个可摘录 H2 子问题）:
  1. …
  2. …
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**:
**Primary keyword**:
**Article type**: {见 §2}
**MeDo category**: Tutorial | Guide | Case Study | Reference | Product
**Search intent**: Informational | Commercial | Transactional | Navigational
**Reader stage**: Awareness | Tool selection | Build | Publish | Diagnosis
**Publish goal**: SEO | Brand | Conversion | Trend
**Target audience**:
**Synthesis Statement**（来自 Phase 0R）:
**One-line thesis**:
**Word count target**: {见 §2 类型词数}
**Cluster role**: Hub | Spoke | Standalone
**Pillar link**: /blog/what-is-open-graph-image（Spoke 必填）
**Differentiation angle** (vs SERP top 3):
**Information increment** (≥1 item):
**Planned internal links** (≥2 blog + ≥1 product, 全部上下文内链):
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Author**: {Oginify | Kostja | {具体成员}}
```

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 + 反模式 → `references/slug-gate.md`**
> **H2 模板 + Frontmatter → `references/article-types.md`**

1. 2–3 slug 候选 + 推荐（Gate B：6 问全 Pass + 反模式零触发）
2. title（45–65 chars）+ description（120–160 chars）
3. **确定 publishDate**：读取 `references/content-graph.md` 已有日期表，从锚点日往前逐日分配，确保每自然日 ≤1 篇（§1B 日期策略）
4. 完整 frontmatter
5. **复核** Phase 0R SERP Fit（有变则更新 Research Log）

**Slug 硬规则**：常青 kebab-case，**slug 不含年份**；5–8 词，≤60 字符。

---

### Phase 3 — Outline

> **H2 模板 → `references/article-types.md`**
> **内链规划 → `references/content-graph.md`**

每节标注目标词数、Reader mental state、内链占位、Answer block ID、snippet 定义句位置。

```markdown
## Outline — {slug}

| § | H2 | Answer block ID | Reader mental state | Target words | Links / Notes |
|---|-----|-----------------|---------------------|-------------|---------------|
| TL;DR | 3–5 bullet | AB-0 | 找对地方了吗？ | 120 | bullet 1 = snippet 定义句 |
| Open | hook | AB-0 | 刚搜进来：找对地方了吗？ | 120–180 | 痛点 → 2026 转折 → 本文承诺 |
| 1 | … | AB-1 | … | … | link: /blog/... |
| … | … | … | … | … | … |
| Conclusion | 无序号 | — | 准备行动 / 仍有一个顾虑 | 150 | CTA → / |
| FAQ | 固定 6 题 | — | 具体异议（来自 R2 PAA） | 400 | ≥1 objection |
```

**结构硬要求**：
- `## TL;DR`（3–5 bullet，紧跟 H1、正文最上方）
- 编号主节 `## 1.` … `## N.`
- `## Conclusion`（无序号）
- `## Frequently asked questions`（无序号，H3 每题，固定 6 题）
- 无 `## Related articles`——所有内链均为上下文内链

---

### Phase 3.5 — Outline 交叉检查（Draft 前）

**触发**：同批规划或并行创作 **≥2 篇**（同一 cluster、同一 campaign、或 content-graph 排期相邻）。

**检查项**（详见 `references/portable/outline-cross-check.md`）：
- [ ] H2 标题重复度：同 cluster 内是否有 ≥2 篇同一 H2 措辞？
- [ ] 叙事弧相似：是否都是「定义→列表→对比→FAQ→CTA」且无角度差异？
- [ ] Canonical 越界：非 canon 文 Outline 是否计划展开 hub 才该全量写的概念？
- [ ] Synthesis 冲突：两篇 One-line thesis 是否互相重叠 >50%？
- [ ] **内链缺口**：新文章是否满足互链要求（Spoke 链回 Hub）？

**Fail** → 改 Outline / 改 Synthesis / MERGE 建议 / 补内链规划 → 重过 3.5
**Pass** → 输出 `Outline cross-check: PASS — {slugs}` → Phase 4

单篇创作：跳过 3.5，标注 `N/A — single article`。

---

### Phase 4 — Draft

> **加载顺序**（每次 ≤2 文件）：
> 1. `references/presentation-rhythm.md`（Voice + 碎片化 + 段落优先协议 + FAQ 固定 6 题）
> 2. `references/product-competitors.md`（产品事实 + 竞品矩阵）
> 3. `references/project-config.md`（G1–G7 + P1–P6 + C1–C4 对照）

**flagship Mode 额外加载**：`references/portable/extractability-checklist.md` + `references/portable/perfect-article-checklist.md`

#### 4.0 创作原则

**Different, not better**：不是在 Top3 上「写得更全」，而是提供 Top3 没有的决策维度。Oginify 的差异化空间：URL-first 三分类框架（URL-first vs 通用生图 vs 代码驱动）、1200×630 规格 + 平台裁剪时效表、免费额度/定价 as-of 表。

#### 4.0B BLUF 三处（Bottom-Line Up Front）

| # | 位置 | 要求 |
|---|------|------|
| **B1** | TL;DR 下 | 40–60 词直接回答 primary keyword |
| **B2** | 每个 major H2 首段 | 先答后铺背景 |
| **B3** | FAQ 每问 | 首句即答，再展开；**不得**从正文复制粘贴 |

#### 4.1 段落优先起草协议

1. **先写 prose，后加结构** — 每个 H2 section 第一稿必须是连续段落；表格/列表/步骤追加
2. **禁伪列表** — 不得用 `**Bold label.**` + 单句 × N 替代列表
3. **起草后即时计数** — 全文完成后数长段落（≥4 句）数量；若 <3 → 合并短段重写

#### 4.2 核心约束速查

| 规则 | 执行 |
|------|------|
| 语言 | 英文正文 |
| 开篇 | 痛点场景 → 2026 转折 → 本文承诺 |
| 站外链 | `<a href="URL" rel="nofollow noopener">` |
| 站内 | `/blog/{slug}`、`/`、`/open-graph-validator`、`/bulk-og-image-generator` 等白名单 |
| Comparison / Ranking / Alternative | 三分类框架 + 对比表 + ≥1「何时不选 Oginify」（P5） |
| Tutorial | 步骤用祈使句；每大步后接「为什么这步重要」 |
| 引用 | 按 `references/citations.md` P0/P1/P2 分级；P0 数字必须使用**上下文描述性内链**（`<a href="URL" rel="nofollow noopener">描述性锚文本</a>` 或站内 `[锚文本](/path)`），禁 `[Source: URL]` 后缀 |
| 产品提及 | 不超过 §2 类型上限 |
| 段落 | ≥3 长段（4–8 句）；连续短段 ≤2；段间衔接率 ≥70%；伪列表 = 自动 Fail |
| 内链 | blog ≥2；Spoke 链回 Hub；canonical 概念 1–2 句 + link |
| 竞品 | 每竞品 ≥1 优势；禁 just/merely/only does X |
| 模块顺序 | YAML → H1 → TL;DR → 开篇 hook → H2 → Conclusion → FAQ |

---

### Phase 5 — SelfCheck & Gate C

> **完整加权 12 维 checklist + H0–H4 → 见下**

#### 工具先跑

在人工 Gate C 检查前，先跑 `tools/` 脚本（**从 oginify/ 项目根目录运行**）：

```bash
python skills/oginify-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary kw}"
python skills/oginify-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {ranking|howto|glossary|sizeguide|metaguide|alternative|toolguide|developerguide|usecase|trendanalysis|opensourceguide|announcement}
python skills/oginify-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/vs,/templates
```

#### Hard Gates（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填（或 Degraded 已标注且无未验证 P0 claim） |
| **H1** | P0 Gate G1–G7 + P1–P6 + C1–C4 | 零触发 |
| **H2** | Slug Gate B | Design-Time 六问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | Oginify-Specific | 产品提及比例合规；URL-first vs 通用生图 vs 代码驱动 叙事一致；无 Hub 抢词（C2） |

#### 加权 12 维评分（Track S — 100%）

| # | 维度 | 权重 | 10 分标准 | 参考文档 |
|---|------|:---:|------|------|
| 1 | **EEAT & Fact** | 20% | 每个可验证 claim 有来源；竞品描述基于官方资料；产品数字 as-of；≥1 竞品优势段 | `eeat-framework.md` · `citations.md` · `proof-gate.md` |
| 2 | **Information Gain** | 14% | 核心论点在 SERP top 5 找不到等效替代；≥40% 内容为独有框架/分类法/对比维度 | `serp-audit.md` |
| 3 | **Presentation & Rhythm** | 12% | 长/中/短段落自然交替；列表占比 ≤类型上限；衔接率 ≥70%；0 处碎片化 | `presentation-rhythm.md` |
| 4 | **Writing & Voice** | 11% | 品牌 Voice 5 项全满足；空泛句 ≤2；≥1 具名竞品+workflow；句段达标 | `writing-style.md` |
| 5 | **SERP Fit** | 8% | title 45–65 chars 含主词；desc 120–160 chars；snippet-ready 定义 | `serp-audit.md` |
| 6 | **SEO & Hub-Spoke** | 7% | 正文 blog 互链 ≥2；Spoke 链回 Hub；关键词自然分布 | `content-graph.md` |
| 7 | **Structure** | 7% | TL;DR + 编号 H2 + Conclusion + FAQ（固定 6 题）；无 Related 区块 | `article-types.md` |
| 8 | **Objectivity** | 7% | Comparison/Ranking: ≥1 竞品优势 + ≥1 非 Oginify 场景（P5） | `proof-gate.md` P5 |
| 9 | **Internal Links** | 5% | 内链白名单；无死链；无 forthcoming >1；锚文本描述性；外链 nofollow | `project-config.md` |
| 10 | **CTA / Conversion** | 4% | CTA ≤2；匹配读者阶段；无虚假承诺 | `platform-routing.md` |
| 11 | **Depth** | 3% | 每 500 词 ≥1 具体例子；无「表格+一句话」空壳；FAQ 非正文复制 | `presentation-rhythm.md` |
| 12 | **Slug / H1** | 2% | 常青无年份；Gate B 全 Pass；无 Hub 抢词（C2） | `slug-gate.md` |

**评分细则**（每维 1–10）：10 = Wirecutter 标杆 · 7 = 合格 minor 修订 · 4 = 明显缺口 · 1 = 系统性失败

**交付**：Hard Gates 全 Pass + 总分 ≥70 + 无维度 <3/10

**等级**：

| 等级 | 分数 | 含义 |
|------|:---:|------|
| **S** | 90–100 | 标杆稿，立即发布 |
| **A** | 80–89 | 质量扎实，修 1–3 处后发布 |
| **B** | 70–79 | 内容可用，需一轮精修 |
| **C** | 60–69 | 结构或可信度有明显缺口，不建议发布 |
| **D** | <60 | 需重写 |

#### Track T — 8 维 Pass/Fail

| # | 维度 | Pass 标准 |
|---|------|----------|
| 1 | Publishability | H0–H4 全 Pass |
| 2 | Fact / E-E-A-T | 可验证 claim 有来源；产品数字 as-of |
| 3 | Differentiation | 相对 SERP Top3 有增量；工具页无 duplicate（C3） |
| 4 | Topic Fit | 与 Track T 长尾意图匹配 |
| 5 | Product Tie-in | 产品提及比例合规（≤35%）；链对应工具页 |
| 6 | Links | 内链白名单；锚文本描述性；外链 nofollow |
| 7 | Voice | 简短直接；无 hype；FAQ 独立 |
| 8 | No Cannibalization | 与已有 slug 无关键词重叠（C1） |

**Track T 等级**：A = 8/8 Pass · B = 7/8 Pass · Fail = ≤6/8 Pass

**Gate C**：H0–H4 + 加权评分全达标 → **audit-ready**（可进入终审，≠ publish-ready）。任一 Fail → 标注修复动作 → 按 §3.G 回溯表回退修复。

#### Perfect-Ready 附加清单（flagship 专用）

- [ ] Moat Asset 已在正文兑现
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 类型已标注
- [ ] Post-publish Metric Spec 已写入 Brief

---

### Phase 5.5 — Cross-Article Audit

**触发**：同批创作 ≥2 篇。**不替代** Phase 3.5（Outline 级），此为全文级。

> **完整 CA1–CA10 → `references/cross-article-audit.md`**

| 跨文章检查点 | 检测方法 |
|-------------|---------|
| 叙事模式雷同 | 多篇是否共享相同叙事弧？3+ 篇 → 标记 |
| 内容网络完整性 | 互链是否双向？ |
| 核心概念跨篇重复 | 每概念只一篇 canonical |
| Intro 模板化检测 | 多篇 intro 是否共享相同三段式结构？ |
| Conclusion 模板化检测 | 多篇 conclusion 是否可互换首段？ |

Fail → 改文或标注差异原因。

---

### Phase 6 — Delivery

1. 写入 `oginify/blog/NN-{slug}.md`
2. 输出 Article Brief 最终版
3. 输出 SelfCheck 表（H0–H4 + 加权评分 + 等级）
4. **Source Map**（Claim × Paragraph × Source × Confidence，≥3 行）
5. **Internal Link Plan**
6. **Signal of Excellence 标注**：
   - `Excellence: Yes — {类型}`（原创框架 / 反直觉数据 / 可执行 checklist / 具名案例 / 洞见）
   - `Excellence: No — 合格但无记忆点`
7. **Moat Asset 兑现检查**：对照 Brief `MoatAssetPlanned`，成稿是否兑现？

**终审指令模板**（复制给用户，需另一 Agent 或人工执行）：

```markdown
请用本 skill 内 references/portable/final-audit.md 对以下文章做发布前终审：
- 文件：oginify/blog/{NN}-{slug}.md
- 类型：{Article type}
- 主关键词：{primary keyword}
- SelfCheck 摘要：{等级}（{分数}/100）

要求：
1. 先过 P0 Gate G1–G7 + P1–P6 + C1–C4
2. 逐维评分（加权 12 维 → 100 分）
3. 输出总分 + 等级（S/A/B/C/D）+ Excellence + Moat + Perfect gap
4. 标记 P1/P2
```

8. **提示人类**更新 `blog/README.md` 文章表

---

### §3.G — Gate 失败回溯表

| Gate / 结果 | 回退至 | 典型原因 | 修复后 |
|-------------|--------|---------|--------|
| **Gate A → STOP** | 流程结束 | 增量不足、MERGE 建议、必问未确认 | 改选题或合并后重新 Phase 0 |
| **Gate A → MERGE** | 流程结束 | 搜索意图重叠、深度不可独立 | 执行合并清单，不写新稿 |
| **Gate 0R ❌** | **Phase 0R** | SERP 未搜、Top3 未 Fetch、无 Synthesis | 补 R2/R3 → 更新 Log → 重过 Gate 0R |
| **Gate 0R ❌ — 事实不可验证** | **STOP 或 Phase 0** | 官方页无法 Fetch 且需写 P0 claim | Degraded 模式不写 P0 claim，或改选题 |
| **Gate 3.5 ❌** | **Phase 3** | 同批 Outline H2/叙事/Synthesis 重叠 | 改角度或 MERGE → 重过 3.5 |
| **Gate B ❌** | **Phase 2** | Slug 反模式、关键词不对齐 | 新 slug → 重过 Gate B → 更新 Brief |
| **Gate C ❌ — 写作/事实类** | **Phase 4** | EEAT、Voice、Presentation、产品事实 | 改稿 → 重跑 Phase 5 SelfCheck |
| **Gate C ❌ — 结构类** | **Phase 3** | 缺模块、H2 骨架不符 | 改 Outline → Phase 4 重写或局部改稿 |
| **Gate C ❌ — Slug/Meta** | **Phase 2** | title/description 不合规 | 改 frontmatter → Phase 4 同步正文首段 |
| **Gate C ❌ — 混合** | **Phase 3 或 4**（以多数为准） | 多项 Fail | 先修结构再修 prose |

---

## §4 内容图谱指针

> **完整图谱、排期、Golden Examples → `references/content-graph.md`**

| 项 | 值 |
|----|-----|
| **Hub slug** | `what-is-open-graph-image` |
| **Cluster ID** | `og-image` |
| **下一文件序号** | **05** |
| **下一篇 P0 优先级** | `05-open-graph-image-size.md`（Track T SizeGuide） |
| **已发布** | 4 篇（#01 Ranking + #02 Hub + #03 HowTo + #04 Mission） |
| **规划中** | Hub #02 + Ranking/HowTo/SizeGuide/MetaGuide/DeveloperGuide/Alternative |

---

## §5 关键词速查

> **→ `references/keywords.md`**（Phase 0/0R 按需加载）

P0：best AI open graph image generator · open graph image size · what is open graph image · og image generator
P1：og:image meta tags · twitter card size · free og image generator · bulk og image generator
P2：dynamic og image next.js · vercel og alternative · social-cards-skills · og image CTR

---

## §6 产品与竞品事实边界

> **→ `references/product-competitors.md`**（Phase 0R/4 按需加载）

Oginify URL-first 机制 · 免费额度/定价 as-of · social-cards-skills 开源边界 · 竞品速览（Gemini/GPT Image/Midjourney/Vercel OG/Placid/Bannerbear/Canva/Cloudinary）· 三分类框架 · 合规红线

---

## §7 文件命名与 README 同步

- 文件名：`NN-{slug-kebab}.md`，NN 两位递增（当前下一 **05**）
- slug 与 frontmatter 一致；常青；无禁词
- 图片：frontmatter 不含 `image` 字段（图片由 CMS/OG 单独管理）
- 成稿后提示人类更新 `blog/README.md`

---

## §8 本 skill 内文档分工

| 阶段 | 文档 | 维护 |
|------|------|------|
| 选题 → 成稿 | 本 SKILL + `references/` | Agent |
| Phase 0 | `portable/investment-score.md` · `portable/gates-master.md` | Mode + Investment |
| Phase 0R | `portable/research-triangle.md` · `proof-library.md` | Synthesis + Examples |
| Phase 1 | `mini-example.md` | Brief 模板 |
| Phase 2–3 | `article-types.md` + `slug-gate.md` + `keywords.md` | 创作 |
| Phase 3.5 | `portable/outline-cross-check.md` | 同批 ≥2 篇 |
| Phase 4 | `presentation-rhythm.md` + `writing-style.md` + `citations.md` | flagship 加 `portable/extractability-checklist.md` |
| Phase 5 | `tools/` 脚本 + 本 SKILL §3.5 | H0–H4 + 加权 12 维 |
| Phase 5.5 | `cross-article-audit.md` | CA1–CA10 |
| Source Map / SERP Fit | `portable/source-map-template.md`、`portable/serp-fit-template.md` | 随 skill 分发 |
| 发布后 | `portable/post-publish-review.md` | T+7/30/90 |
| 发布前终审 | `portable/final-audit.md` | 人类 / 另一 Agent |
| 回溯审计 | `retro-audit.md` | 独立场景 |

**版本同步**：当 `blog/README.md` 文章表新增已发布稿、或关键词簇排期变更时，人类应同步更新 `references/content-graph.md` 与 `references/keywords.md`，并将 SKILL.md frontmatter `version` patch bump（如 1.0.0 → 1.0.1）。

**发布后必做 checklist**（每发布一篇须人类执行）：
1. bump 本文件 §0 输出区 + §4 的「下一文件序号」
2. bump `references/content-graph.md` §2 的「下一文件序号」
3. 更新 `references/content-graph.md` §2 已发布文章登记表（新增行）
4. 更新 `references/content-graph.md` §3 排期表（标记 ✅）
5. bump 本文件 frontmatter `version` patch（如 1.0.0 → 1.0.1）
6. 若 `references/mini-example.md` 范例对应本篇，替换为下一篇 P0

**Agent 防护**：若 Phase 0 发现用户请求的序号与 §4 序号不一致，须先确认是否已有人类更新的文章未反映在 skill 中。

---

## Gotchas — 禁止项（精选）

**结构**：❌ 编号 H2 用于 Conclusion/FAQ · ❌ 设 `## Related articles` 区块 · ❌ TL;DR 仅重复 title · ❌ FAQ <6 题 · ❌ FAQ 用通用模板题 · ❌ 连续 3+ 短段 · ❌ 列表占比超类型上限
**写作**：❌ revolutionary/game-changing/seamless/magic · ❌ just/merely 贬低竞品 · ❌ 假装零工作量 · ❌ 空泛句
**Slug/链接**：❌ slug 含年份 · ❌ slug 含内部架构词（framework/strategy/diagnosis/complete-guide）· ❌ 链未上线路径 · ❌ forthcoming >1 · ❌ 锚文本 click here/learn more
**产品/Proof**：❌ 6 张/天、$0.99、$7.90、$29 无 as-of · ❌ 「唯一无需 prompt」/「自动提升 CTR 300%」 · ❌ 把 Gemini/GPT Image 写成不能做 OG · ❌ social-cards-skills 与 Oginify 混淆
**流程**：❌ Gate 未全 Pass 交付 · ❌ 一次加载全部 references · ❌ 运行时读 oginify-*.md · ❌ 跨篇 ≥2 篇但未跑 Phase 3.5/5.5

---

## §9 Reference 文件索引

| 文件 | 加载时机 | 内容 |
|------|----------|------|
| `references/proof-library.md` | Phase 0R, 4, 5 | Product Fact Ledger、Proof ID |
| `references/project-config.md` | Phase 0, 0R, 5 | 品牌、URL 白名单、G1–G7、C1–C4 |
| `references/product-competitors.md` | Phase 0R, 4, 5 | Oginify 事实表、竞品矩阵（R3 验证） |
| `references/proof-gate.md` | Phase 0, 5 | P1–P6 产品 Gate |
| `references/content-graph.md` | Phase 0, 0R, 3, 4 | Hub-Spoke、已发/待写、内链、Golden |
| `references/keywords.md` | Phase 0, 2 | P0/P1/P2、禁抢词 |
| `references/article-types.md` | Phase 2, 3, 4 | 12 类 H2 模板、Frontmatter |
| `references/slug-gate.md` | Phase 2 | Slug 6 问、反模式 |
| `references/citations.md` | Phase 4, 5 | P0/P1/P2、Source Map |
| `references/serp-audit.md` | Phase 0R, 5 | SERP Fit + 信息增量审计 |
| `references/eeat-framework.md` | Phase 4, 5 | EEAT 四信号 |
| `references/presentation-rhythm.md` | Phase 4, 5 | Voice、碎片化、段落协议、FAQ |
| `references/writing-style.md` | Phase 4, 5 | Voice 标准、禁词、句段指标 |
| `references/platform-routing.md` | Phase 4 | CTA + 意图→落地页 |
| `references/cross-article-audit.md` | Phase 5.5 | CA1–CA10 |
| `references/retro-audit.md` | 独立场景 | 已发布稿回溯审计 |
| `references/mini-example.md` | Phase 1, 3 | Brief + Outline 范例 |
| `references/portable/*` | 按指针 | 12 个便携参考 |
| `tools/frontmatter_validator.py` | Phase 5 | Frontmatter 机器检查 |
| `tools/word_count_narrative.py` | Phase 5 | 字数硬门槛 H3 |
| `tools/link_checker.py` | Phase 5 | P0 G2/G6 链接检查 |
| `evals/eval-manifest.yaml` | 质量回归 | 20 个 Eval 用例 |
| `evals/golden-brief-*.md` | 质量回归 | 黄金样本 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **1.0.4** | 2026-08-15 | #04 重构：`oginify-mission` → `introducing-oginify`（Mission → Announcement，lite Mode）；content-graph/README 同步 |
| **1.0.3** | 2026-08-15 | 引用规范修订：P0 改为**上下文描述性内链**（HTML `<a rel="nofollow noopener">` 或站内 markdown），禁 `[Source: URL]` 后缀；同步 4 篇文章全部引用；link_checker 增加 HTML 链接检查，word_count 去除 HTML 标签 |
| **1.0.2** | 2026-08-18 | dogfood #03 `how-to-create-open-graph-image`（HowTo）+ #04 `oginify-mission`（Announcement）；content-graph 下一序号 05 |
| **1.0.1** | 2026-08-16 | dogfood #02 `what-is-open-graph-image`（Hub Glossary）；content-graph 下一序号 03 |
| **1.0.0** | 2026-08-15 | 初版：双轨 Track S/T · 12 类路由 · G1–G7 + P1–P6 + C1–C4 · 9 Phase + 5 Gate · Mode + Investment Score + BLUF · 加权 12 维评分（S/A/B/C/D）· tools/ 验证脚本 · evals 回归套件 · 基于 oginify.com 现网事实（免费 6 张/天、$0.99/$7.90/$29 定价、social-cards-skills 开源） |

---

## v1.1 Backlog

| # | 项目 | 优先级 |
|---|------|:---:|
| 1 | `oginify-meta-title-description` skill | P1 |
| 2 | 加权 SelfCheck 脚本化（tools/scorer.py） | P2 |
| 3 | Cross-Article Audit 扩展 CA11–CA20 | P2 |

---

*oginify-blog-article · v1.0.0 · 2026-08-15 · fully self-contained · references/portable/ · tools/ · evals/ · 12 article types + Mode + Investment Score + BLUF + Gate Backtracking*
