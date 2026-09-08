---
name: clink-blog-article
description: >
  Clink L1 project skill — payment/fintech brand facts, GlossaryTerm routing,
  C1–C4 compliance gates, cluster folders (stripe-risk/agentic-payments).
  Self-contained v3: full 9-Phase workflow inline; final audit via local
  portable/final-audit.md. Load alone — no external engine required.
metadata:
  version: 3.0.0
  project: clinkbill.com
  locale: en
  market: global SaaS / AI-native payments
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 460
  complements: final-audit
  forbidden-reads:
    - ../../clink.md
    - ../../clink-*.md
    - ../../blog/README.md
---

# Clink Blog Article Creation（自包含）

为 **https://clinkbill.com/blog/** 从选题到英文成稿。

**硬性规则**：本 skill **自包含**——只读本文件夹内文件（`references/`、`references/portable/`、`tools/`、`evals/`）。9 Phase + 5 Gate 工作流已内联于本文；通用 rubric 在本地 `references/portable/`。禁止读 skill 文件夹外文档（见 `forbidden-reads`），发布前终审用 `references/portable/final-audit.md`。

**渐进式加载**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md` 或 `references/portable/{file}.md`（**一次最多 2 个**），读完即弃，不跨 Phase 保留。禁止一次性加载全部 references。

**六角色换帽**（Phase 4 与 Phase 5 **分轮**，禁止 Draft 同轮自我放行 Gate C）：

| Phase | 角色 |
|-------|------|
| 0 / 0R | Strategist / Researcher |
| 1–3 | Strategist + SME |
| 4 | Writer |
| 5 / 6 | Editor / Auditor |

---

## §0 如何使用

### 触发语

```
按 clink-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{type} 文章。Mode：{lite|standard|flagship}（可选，默认 standard）。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

`{type}` 枚举见 §2 路由（BrandIntroduction / Comparison / Product / Opinion / EvaluationComparison / GlossaryTerm / IndustryNews / StripeRisk / AgenticPayments 簇内 Research / HowTo）。未给则 Agent 按 §2 推断。

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 | ✅ | 决定 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | 未指定默认 standard；部分类型有默认 Mode（见 article-types §1） |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |

### 输出（Phase 6 交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ 完整 |
| 3 | 成稿 `clink/blog/[{cluster}/]NN-{slug}.md` | ✅ | ✅ | ✅ |
| 4 | SelfCheck（H0–H4 + C1–C4 + 12 维） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | OG Image Prompt（1200×630） | ✅ | ✅ | ✅ |
| 8 | Internal Link Plan | — | ✅ | ✅ |
| 9 | 终审指令 → `references/portable/final-audit.md` | ✅ | ✅ | ✅ |
| 10 | Post-publish Metric Spec | — | ✅ | ✅ |
| 11 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化 title/description | `references/meta-title-description.md`（禁止改正文） |
| 已有完整稿，仅需终审 | `references/portable/final-audit.md` |
| 已发稿回溯审计 | `references/portable/retro-audit.md` |
| 非 clinkbill.com 博客 | 对应项目 blog skill |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + C1–C4 详表 → `references/project-config.md`**

| 配置项 | Clink 值 |
|--------|---------|
| **主域名 / 博客前缀** | clinkbill.com / `/blog/` |
| **blogLayout** | cluster-folders（见 §4 + `content-graph.md` §1B） |
| **品类 one-liner** | Subscription billing + multi-PSP orchestration + tax + agent payments |
| **受众** | 全球 SaaS、AI-native、支付/RevOps 工程师 |
| **署名默认** | `Clink Team` |
| **下一序号 NN** | **24**（全局连续；见 `content-graph.md`） |
| **接入模式** | Contact Sales（无公开定价页 as-of 2026-06） |

### C1–C4 阻断速查（详表 → project-config §4）

| # | 阻断条件 |
|---|---------|
| C1 | 无来源的具体 Clink 费率（禁止编造 pricing table） |
| C2 | MoR/tax 超范围 claim 无限定语或 as-of |
| C3 | 证言夸大无 as-of |
| C4 | Agentic Payments 未标 Early Access（路径 `/agentic-payment`） |

---

## §2 文章类型路由（Clink 专属）

> **路由主表 + 词数 + H2 模板 → `references/article-types.md` §1/§3**（本文件不复述主表）

**类型枚举**：BrandIntroduction · Comparison · Product · Opinion · EvaluationComparison · GlossaryTerm · IndustryNews · StripeRisk · AgenticPayments 簇内 Protocol Definition / Reference List（Research）· Merchant How-To（HowTo）。

- GlossaryTerm → 读 `article-types.md` §3 + `references/glossary-terms.md`
- AgenticPayments 簇三型 → `article-types.md` §3「AgenticPayments 簇内类型」
- 集群归属与互链 → `content-graph.md` §1B / 推荐互链表
- 重写/扩写 05–09（lovable-series）→ 额外读 `references/series-canonical-ownership.md`

**全类型结构硬约束**（FAQ/Conclusion 等，速查；通用模块表在 article-types §2）：

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullets；bullet 1 = snippet 定义句 |
| **H2** | 英文描述性标题；**不编号** |
| **Conclusion → FAQ** | 倒数第二节 `## Conclusion`；最后一节 `## FAQ`（**6 题**） |
| **内链** | blog 正文互链 ≥2（`/blog/{slug}`） |
| **CTA** | Contact Sales / docs；≤2 次 |

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  ─ Intake & Gate A         (Mode + Investment Score + 六必问)
    ↓ PASS
Phase 0R ─ Research 三角 & Gate 0R  (R1→R2→R3→Synthesis)
    ↓ PASS / ❌ → §3.G
Phase 1  ─ Article Brief
Phase 2  ─ Slug、Date、Path & Gate B
    ↓ PASS / ❌ → §3.G
Phase 3  ─ Outline
Phase 3.5─ Outline 交叉检查（同批 ≥2 篇强制）
    ↓ PASS / ❌ → §3.G
Phase 4  ─ Draft（BLUF 三处 + 段落优先 + 渐进加载）
    ↓
Phase 5  ─ SelfCheck & Gate C（H0–H4 + C1–C4 + 12 维）
    ↓ PASS / ❌ → §3.G
Phase 5.5─ Cross-Article Audit（同批 ≥2 篇强制）
Phase 6  ─ Delivery
```

---

### Phase 0 — Intake & Gate A

> **Investment Score → `references/portable/investment-score.md`**
> **Gate 细则 → `references/gates.md`**

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: {§2 枚举}
## InvestmentScore: {1.0–5.0}
## Cluster: {cluster-id | standalone}          ← content-graph §1B
## File path: clink/blog/[{cluster}/]NN-{slug}.md   ← Phase 2 确认
## Category: {frontmatter category}
## Author: Clink Team
## Gate A: KEEP | MERGE → {slug} | STOP
```

**六必问**（SSOT：`references/gates.md` §1）：

| # | 问题 |
|---|------|
| 1 | 主关键词 + search intent？ |
| 2 | 目标读者（ICP）？ |
| 3 | 发布目的（SEO / 品牌 / 转化）？ |
| 4 | SERP Top 3 竞品 URL（供 Phase 0R）？ |
| 5 | 与已有 blog / pipeline 关系？文中内链页面是否已上线？ |
| 6 | category（Product / Comparison / Opinion / Glossary / Agentic Payments / Stripe Risk / Industry News）？ |

**Gate A**：三条件（意图独立 / 读者阶段不同 / 深度不可压缩）满足 ≥2 → KEEP；信息增量相对 SERP Top 3 ≥2 项；Investment <3.0 → 降级或 STOP。GlossaryTerm 追加 D1–D4（见 gates.md §2）。

---

### Phase 0R — Research 三角 & Gate 0R

> **完整流程 → `references/portable/research-triangle.md`**
> **SERP Fit → `references/portable/serp-fit-template.md`**

```
R1 — project-config + product-competitors + content-graph
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（clinkbill.com/docs + SERP Top 3–5 原文）
    ↓
Synthesis Statement（洞察合成）+ Candidate Examples
    ↓
Research Log + SERP Fit → Gate 0R Pass → Phase 1
```

**Mode 差异**：lite 可简版 R2/R3；flagship 须完整 R3 Top5 + ≥2 Candidate Examples。

**Degraded**（WebSearch 不可用）：标注 `Research mode: Degraded — {reason}`；P0 级 claim 不得写未验证数字。

---

### Phase 1 — Article Brief

> **模板 + 范例 → `references/mini-example.md`**

Brief 通用字段之上**必加**：`Category`、`Cluster`、`Information increment ≥2`、Planned internal links、Slug candidate。Brief 输出块见 `mini-example.md`。

---

### Phase 2 — Slug、Date、Path & Gate B

1. Slug 候选 → `references/slug-gate.md`（Gate B：6 问全 Pass + 12 反模式零触发）
2. **Meta**：title / description → `references/meta-title-description.md`（公式 + 字符范围）
3. **publishDate**：对照 `content-graph.md` 日期表；**一天一篇**，错开已占用日
4. **文件路径**（cluster-folders）：

```
读 content-graph §1B
  → cluster 有 folder → clink/blog/{folder}/NN-{slug}.md
  → standalone        → clink/blog/NN-{slug}.md
NN 全局连续（下一号 24），子目录不重置序号。
```

5. Frontmatter 禁止：`keywords` · `related` · `disclosure` · `image`；schema 见 `article-types.md` §4

---

### Phase 3 — Outline

- H2 模板 → `references/article-types.md` §3
- 内链矩阵 / 锚文本 → `references/internal-links.md`
- OG Image Prompt（1200×630，主 prompt + 2 variant）

---

### Phase 3.5 — Outline 交叉检查

> **检查项 → `references/portable/outline-cross-check.md`**

触发：同批 ≥2 篇。检查 H2 重复、叙事弧雷同、Canonical 越界、Synthesis 冲突、内链缺口。单篇标注 `N/A — single article`。

---

### Phase 4 — Draft

**加载顺序**（每次 ≤2 文件，读后即弃）：

1. `references/writing-constraints.md`（Voice + BLUF + 段落优先 + 引用分级）
2. `references/article-types.md` §3（当前类型的 H2 模板）
3. `references/product-competitors.md`（产品事实 + 竞品公平，对比/产品文必读）

GlossaryTerm 选题 → 额外读 `references/glossary-terms.md`；重写 05–09 → 额外读 `references/series-canonical-ownership.md`。flagship → `references/portable/extractability-checklist.md`。

**核心约束**：

- **BLUF 三处**：TL;DR 下 40–60 词直接回答；每个 major H2 首段先答；FAQ 首句即答（不得复制正文）
- **段落优先**：先 prose 后结构；禁伪列表；长段落（≥4 句）≥3；连续短段 ≤2；衔接率 ≥70%
- **P0 数字有来源**：产品 claim 引用 clinkbill.com/docs，as-of；金融表述守 C1–C4
- 竞品每方 ≥1 优势；外链 `rel="nofollow noopener"`
- 模块顺序：YAML → TL;DR → H2… → Conclusion → FAQ

---

### Phase 5 — SelfCheck & Gate C

> **H0–H4 + C1–C4 → `references/selfcheck.md`**
> **12 维通用 rubric → `references/portable/` 内（gates-master + final-audit 供对照）**

**工具先跑**（从 `clink/` 根目录；`--intent`/`--min` 见 article-types §1，`--forbidden` 见 project-config §2）：

```bash
python skills/clink-blog-article/tools/frontmatter_validator.py blog/{path} --keyword "{kw}"
python skills/clink-blog-article/tools/word_count_narrative.py blog/{path} --intent {intent} --min {threshold}
python skills/clink-blog-article/tools/link_checker.py blog/{path}
```

**Gate C**：H0–H4 + C1–C4 + 12 维全 Pass → **audit-ready**；任一 Fail → §3.G 回溯修复 → 重跑。flagship 追加 Perfect-Ready 清单（`selfcheck.md`）。

---

### Phase 5.5 — Cross-Article Audit

触发：同批 ≥2 篇。检查叙事雷同 / 互链双向 / Intro-Conclusion 模板化 / 核心概念跨篇重复 / 事实矛盾 / Cannibalization。单篇跳过标注 `N/A`。

---

### Phase 6 — Delivery

1. 写入 `clink/blog/[{cluster}/]NN-{slug}.md`
2. Article Brief 最终版 + SelfCheck 表 + Source Map + SERP Fit + Internal Link Plan
3. **终审指令**（复制给用户，指向本地 rubric）：

```
请按 clink-blog-article skill 的 references/portable/final-audit.md 执行发布前终审：
- 文件：clink/blog/[{cluster}/]NN-{slug}.md
- 类型：{Article type}
- 主关键词：{primary keyword}
- SelfCheck：audit-ready
```

4. 提示人类更新 `blog/README.md`；金融 claim 建议法务审定。

---

### §3.G — Gate 失败回溯表

| Fail 于 | 回退至 | 动作 |
|---------|--------|------|
| Gate A / Investment | Phase 0 | 改角度 / MERGE / STOP |
| Gate 0R | Phase 0R | 补 R2/R3 / 降 Degraded claim |
| Gate B | Phase 2 | 重选 slug / 改 meta |
| Gate 3.5 / 5.5 | Phase 3 / 4 | 改 Outline 或正文差异 |
| Gate C — 写作/事实类 | Phase 4 | EEAT / Voice / Presentation / 产品事实修复 |
| Gate C — 结构类 | Phase 3 | 缺模块、H2 骨架不符 |
| Gate C — Slug/Meta | Phase 2 | title/description / frontmatter |

---

## §4 集群与 frontmatter

> **Cluster 完整注册表 → `references/content-graph.md` §1B**

| Cluster ID | folder | Hub slug | 主 category |
|------------|--------|----------|-------------|
| core | *(root)* | what-is-clink | Product / Comparison / Opinion / Glossary |
| glossary-metrics | *(root)* | burn-rate | Glossary |
| lovable-series | *(root)* | how-to-add-payments-lovable-app | Product |
| agentic-payments | `agentic-payments/` | agent-payments | Agentic Payments — 04 Hub + 26–29, 31, 33–36 |
| industry-news | `industry-news/` | stripe-openrouter-acquisition | Industry News — 15, 18 |
| stripe-risk-disputes | `stripe-risk/` | what-is-stripe-dispute | Stripe Risk — 争议/拒付 21–23 |
| stripe-risk-accounts | `stripe-risk/` | stripe-account-suspended | Stripe Risk — 账户限制 25/30/32 |

**双分类 frontmatter**（cluster 文）：

```yaml
category: "Agentic Payments"          # 或 Stripe Risk / Industry News
secondaryCategory: "Research"         # Research | HowTo | Guide | Opinion | Product
```

**内链**：永远 `/blog/{slug}`，禁止 `/blog/agentic-payments/{slug}` 等子目录路径。

---

## §5 Reference 索引（均在本文件夹内）

| 文件 | 加载时机 |
|------|----------|
| `references/project-config.md` | Phase 0R / 4 / 5（品牌 + G1–G7 + C1–C4 + URL 白名单） |
| `references/article-types.md` | Phase 0 / 2 / 3 / 4（路由主表 + H2 模板 + frontmatter schema） |
| `references/gates.md` | Phase 0 / 0R / 2 / 5（Gate 细则 + 六必问 + D1–D4） |
| `references/content-graph.md` | Phase 0 / 2 / 3 / 5.5（文件表 + cluster + 日期 + 互链） |
| `references/internal-links.md` | Phase 3 / 3.5 / 5 |
| `references/glossary-terms.md` | Phase 0（GlossaryTerm） |
| `references/series-canonical-ownership.md` | Phase 4 / 5（05–09） |
| `references/writing-constraints.md` | Phase 4 |
| `references/product-competitors.md` | Phase 0R / 4 / 5 |
| `references/selfcheck.md` | Phase 5（H4 + C1–C4） |
| `references/meta-title-description.md` | Phase 2 / title-only 任务 |
| `references/mini-example.md` | Phase 1 / 3 |
| `references/slug-gate.md` | Phase 2 |
| `references/keywords.md` | Phase 0 |
| `references/portable/*` | 按 Phase 指针（本地镜像，self-contained） |
| `tools/` | Phase 5 |
| `evals/` | skill 变更后回归 |

---

## §6 Gotchas

- ❌ Glossary slug 加 `what-is-` 前缀
- ❌ 内链写 `/blog/agentic-payments/...` 或 `/blog/stripe-risk/...`
- ❌ 写具体 Clink 费率（C1）· MoR 全覆盖无 as-of（C2）
- ❌ FAQ 不是最后一节 · 缺 `## Conclusion` · FAQ 不是 6 题
- ❌ frontmatter 写 `keywords` / `related` / `image`
- ❌ 05–09 系列违反 `references/series-canonical-ownership.md`
- ❌ 一次加载全部 references / 读 skill 文件夹外文档
- ❌ Gate 未全 Pass 交付 / 混淆 SelfCheck 与终审

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **3.0.0** | 2026-09-08 | **自包含化**：内联完整 9 Phase 工作流；移除全部外部 L0 引擎依赖；终审指本地 `portable/final-audit.md`；type 枚举并入 AgenticPayments 簇 Research/HowTo；新增 `meta-title-description.md` + `evals/`；NN 表述改全局连续；FAQ 统一 6 题 |
| **2.2.0** | 2026-08-24 | 恢复 `industry-news/` 集群（15, 18）；15 主 category 改为 Industry News |
| **2.1.0** | 2026-08-24 | `agentic-payments/` 协议 definition 系列（26–29, 33） |
| **2.0.0** | 2026-08-23 | L0+L1 拆分；cluster-folders（stripe-risk/agentic-payments）；selfcheck overlay |
| 1.0.0 | 2026-07-21 | 自包含 monolith |

---

*clink-blog-article · v3.0.0 · 2026-09-08 · self-contained · engine: inline · audit: references/portable/final-audit.md*
