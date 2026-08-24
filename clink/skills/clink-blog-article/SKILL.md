---
name: clink-blog-article
description: >
  Clink L1 project skill — payment/fintech brand facts, GlossaryTerm routing,
  C1–C4 compliance gates, cluster folders (stripe-risk/agentic-payments).
  MUST load with E:\Agent执行\blog-create (L0 engine) for full 9 Phase workflow.
metadata:
  version: 2.2.0
  project: clinkbill.com
  locale: en
  self-contained: false
  complements: blog-create
  engine: E:\Agent执行\blog-create\SKILL.md
  audit: E:\Agent执行\blog-audit\SKILL.md
  load-rule: progressive-disclosure
  max-primary-lines: 420
  forbidden-reads:
    - ../../clink.md
    - ../../clink-*.md
    - ../../blog/README.md
---

# Clink Blog Article Creation（L1 项目层）

为 **https://clinkbill.com/blog/** 从选题到英文成稿。

**硬性规则**：执行本 skill 时**必须同时加载 L0 引擎** `E:\Agent执行\blog-create\SKILL.md`。工作流（9 Phase + 5 Gate）、Mode、Investment Score、BLUF、Gate 回溯 → **L0**；品牌事实、类型路由、C1–C4、集群路径、Conclusion→FAQ → **本 skill（L1）**。

**渐进式加载**：默认读本文件 + L0 SKILL 摘要。Phase 细节按指针读取 `references/` 或 L0 `references/portable/`（一次 ≤2 个）。禁止读 `forbidden-reads` 列表外文档。

**六角色换帽**（与 L0 一致；Phase 4 与 Phase 5 **分轮**）：

| Phase | 角色 |
|-------|------|
| 0 / 0R | Strategist / Researcher |
| 1–3 | Strategist + SME |
| 4 | Writer |
| 5 / 6 | Editor / Auditor |

---

## §0 如何使用

### 触发语（双 skill）

```
按 E:\Agent执行\blog-create\SKILL.md + clink-blog-article skill 执行：
- 项目 skill：e:\clients\clink\skills\clink-blog-article
- 关键词："{primary keyword}"
- 类型：{BrandIntroduction|Comparison|Product|Opinion|EvaluationComparison|GlossaryTerm|IndustryNews|StripeRisk}（可选）
- Mode：{lite|standard|flagship}（可选，默认 standard）
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 | ✅ | 决定 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | BrandIntroduction/Comparison/EvaluationComparison 默认 flagship |
| 竞品参考 URL | 推荐 | Phase 0R |

### 输出（L0 Phase 6 + L1 约束）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief | ✅ | ✅ | ✅ |
| 2 | Research Log | 简 | ✅ | ✅ |
| 3 | 成稿 `clink/blog/[{cluster}/]NN-{slug}.md` | ✅ | ✅ | ✅ |
| 4 | SelfCheck（H0–H4 + 12 维） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | OG Image Prompt（1200×630） | ✅ | ✅ | ✅ |
| 8 | Internal Link Plan | — | ✅ | ✅ |
| 9 | 终审指令 → `E:\Agent执行\blog-audit\SKILL.md` | ✅ | ✅ | ✅ |
| 10 | Post-publish Metric Spec | — | ✅ | ✅ |
| 11 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化 title/description | 未来 `clink-meta-title-description` |
| 已有完整稿，仅需终审 | `E:\Agent执行\blog-audit\SKILL.md` |
| 非 clinkbill.com 博客 | 其他项目 L1 skill + blog-create |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + C1–C4 → `references/project-config.md`**

| 配置项 | Clink 值 |
|--------|---------|
| **blogLayout** | **cluster-folders**（见 §4 + `content-graph.md` §1B） |
| **主域名** | clinkbill.com |
| **博客前缀** | `/blog/` |
| **Pillar Hub** | `what-is-clink` |
| **下一序号 NN** | **24**（见 `content-graph.md` §1） |
| **品类 one-liner** | Subscription billing + multi-PSP orchestration + tax + agent payments |
| **受众** | 全球 SaaS、AI-native、支付/RevOps 工程师 |
| **署名默认** | `Clink Team` |
| **禁止内链** | `/vs/*`、`/pricing`、`/for/*`、`/learn/*`、`/customers/*` |

### C1–C4 阻断速查

| # | 阻断条件 |
|---|---------|
| C1 | 无来源的具体 Clink 费率 |
| C2 | MoR/tax 超范围 claim 无限定语 |
| C3 | 证言夸大无 as-of |
| C4 | Agentic Payments 未标 Early Access |

---

## §2 文章类型路由（Clink 专属）

> **完整路由 + H2 模板 → `references/article-types.md`**
> **L0 Phase 流程 → `E:\Agent执行\blog-create\SKILL.md` §3**

### 路由速查

| 类型 | intent | 词数目标 | Clink 占比 | 默认 Mode | `--intent` / `--min` |
|------|--------|----------|:---:|:---:|------|
| BrandIntroduction | 品牌 hub | 2500–3500 | ≤30% | flagship | `brand` / `--min 2500` |
| Comparison | 架构选型 | 2500–3500 | ≤35% | flagship | `comparison` / `--min 1600` |
| Product | how-to / routing | 2200–3200 | ≤40% | standard | `product` / `--min 1800` |
| Opinion | category POV | 2000–2800 | ≤35% | standard | `opinion` / `--min 1800` |
| EvaluationComparison | clink vs X | 2500–3500 | ≤45% | flagship | `evaluation` / `--min 2500` |
| GlossaryTerm | 财务/计费术语 | 2200–3200 | ≤15% | standard | `glossary` / `--min 1800` |
| **IndustryNews** | 行业事件/收购 | 2000–2800 | ≤25% | standard | `opinion` / `--min 1800` |
| **StripeRisk** | Stripe 风控/申诉 | 2200–3200 | ≤30% | standard | `product` / `--min 1800` |

**Agentic Payments 集群**（`agentic-payments/`）：Hub `agent-payments`（04）+ 协议 definition 系列（26–29, 33）。**Industry News 集群**（`industry-news/`）：15、18。Skill Marketplace（16–17）在根目录。

**GlossaryTerm**：slug 纯术语 kebab-case（**不加** `what-is-`）；`category: Glossary`。

**集群双分类**（`stripe-risk/` · `agentic-payments/`）：

```yaml
category: "Stripe Risk"          # 或 "Industry News"
secondaryCategory: "Guide"       # Research | Opinion | HowTo | Product
```

### 全类型结构硬约束

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullets；bullet 1 = snippet 定义句 |
| **H2** | 英文描述性标题；**不编号** |
| **Conclusion → FAQ** | 倒数第二节 `## Conclusion`；最后一节 `## FAQ`（**6 题**） |
| **内链** | blog 正文互链 ≥2 |
| **CTA** | Contact Sales / docs；≤2 次 |

---

## §3 Clink Phase 叠加（在 L0 各 Phase 之上执行）

### Phase 0 — 六必问（L1 扩展）

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 受众？ |
| 2 | 发布目的（品牌 / SEO / 转化）？ |
| 3 | SERP Top 3 竞品 URL？ |
| 4 | 内链页面是否已上线？ |
| 5 | 与已有文章 / pipeline 关系？ |
| 6 | **category**（Product / Comparison / Opinion / Glossary / Agentic Payments / Stripe Risk / Industry News）？ |

**Phase 0 首行强制输出（L0 + L1）**：

```
## Mode: lite | standard | flagship
## ArticleType: BrandIntroduction | … | IndustryNews | StripeRisk
## InvestmentScore: {1.0–5.0}
## Cluster: {cluster-id | standalone}
## File path: clink/blog/[{cluster}/]NN-{slug}.md
## Category: {frontmatter category}
## Author: Clink Team
## Gate A: KEEP | MERGE → {slug} | STOP
```

> Gate A / Investment Score → L0 portable + `references/gates.md`

### Phase 1 — Brief 扩展

L0 Brief 基础上**必加**：`Category`、`Cluster`、`Information increment ≥2`、Planned internal links、Slug candidate。范例 → `references/mini-example.md`

### Phase 2 — Slug、Date、Path & Gate B

1. Slug → `references/slug-gate.md`（Gate B 六问）
2. **publishDate**：`content-graph.md` 日期表；**一天一篇**
3. **文件路径**（cluster-folders）：

```
读 content-graph §1B
  → folder 有值 → clink/blog/{folder}/NN-{slug}.md
  → standalone → clink/blog/NN-{slug}.md
```

4. Frontmatter 禁止：`keywords` · `related` · `disclosure`

### Phase 3 — Outline

- H2 模板 → `article-types.md`
- 内链矩阵 → `references/internal-links.md`
- OG Image Prompt（1200×630）

### Phase 4 — Draft

**加载顺序**（≤2 文件/轮）：`writing-constraints.md` → `product-competitors.md` → `project-config.md`

GlossaryTerm 选题 → 额外读 `references/glossary-terms.md`

改写/扩写 **05–09**（lovable-series）→ 额外读 `references/series-canonical-ownership.md`

### Phase 5 — SelfCheck & Gate C

1. **工具预检**（从 `clink/` 根目录）：

```bash
python skills/clink-blog-article/tools/frontmatter_validator.py blog/{path} --keyword "{kw}"
python skills/clink-blog-article/tools/word_count_narrative.py blog/{path} --intent {intent} --min {threshold}
python skills/clink-blog-article/tools/link_checker.py blog/{path}
```

2. **H0–H3 + 12 维** → L0 `E:\Agent执行\blog-create\references\selfcheck.md`
3. **H4 + C1–C4** → `references/selfcheck.md`

Gate C Pass → **audit-ready**；终审 → `E:\Agent执行\blog-audit\SKILL.md`

### Phase 6 — Delivery

1. 写入 `clink/blog/[{cluster}/]NN-{slug}.md`
2. Brief + SelfCheck + Source Map + SERP Fit
3. 复制 L0 Phase 6 终审指令（指向 **blog-audit**）
4. 提示人类更新 `blog/README.md`；金融 claim 建议法务审定

---

## §4 集群与 frontmatter

> **Cluster 注册表 → `references/content-graph.md` §1B**
> **通用规则 → `E:\Agent执行\blog-create\references\topic-cluster-layout.md`**

| Cluster ID | folder | Hub slug | 主 category |
|------------|--------|----------|-------------|
| core | *(root)* | what-is-clink | Product / Comparison / Opinion / Glossary |
| glossary-metrics | *(root)* | burn-rate | Glossary |
| lovable-series | *(root)* | how-to-add-payments-lovable-app | Product |
| agentic-payments | `agentic-payments/` | agent-payments | **Agentic Payments** — 04 Hub + 26–29, 33 |
| industry-news | `industry-news/` | stripe-openrouter-acquisition | **Industry News** — 15, 18 |
| stripe-risk-disputes | `stripe-risk/` | what-is-stripe-dispute | **Stripe Risk** — 争议/拒付 21–23 |
| stripe-risk-accounts | `stripe-risk/` | stripe-account-suspended | **Stripe Risk** — 账户限制 25/30/32 |

```yaml
category: "Agentic Payments"
secondaryCategory: "Opinion"   # 或 Product / Industry News
```

**内链**：永远 `/blog/{slug}`，禁止 `/blog/agentic-payments/{slug}` 或 `/blog/stripe-risk/{slug}`。

---

## §5 Reference 索引

| 文件 | 加载时机 | 层级 |
|------|----------|------|
| `E:\Agent执行\blog-create\SKILL.md` | Phase 0–6 | **L0** |
| `E:\Agent执行\blog-audit\SKILL.md` | 终审 | **L0** |
| `references/project-config.md` | Phase 0R, 4, 5 | L1 |
| `references/article-types.md` | Phase 0, 2, 3, 4 | L1 |
| `references/gates.md` | Phase 0, 2 | L1 |
| `references/slug-gate.md` | Phase 2 | L1 |
| `references/content-graph.md` | Phase 0, 2, 3.5, 5.5 | L1 |
| `references/internal-links.md` | Phase 3, 3.5 | L1 |
| `references/glossary-terms.md` | Phase 0（GlossaryTerm） | L1 |
| `references/series-canonical-ownership.md` | Phase 4 / 5（lovable-series 05–09） | L1 |
| `references/writing-constraints.md` | Phase 4 | L1 |
| `references/product-competitors.md` | Phase 0R, 4 | L1 |
| `references/selfcheck.md` | Phase 5（H4 + C1–C4） | L1 |
| `references/mini-example.md` | Phase 1, 3 | L1 |
| `references/portable/*` | 按 L0 指针；**同步自 SSOT** | L0 副本 |
| `tools/` | Phase 5 | L1（Clink fork + 阈值） |

**portable 同步**：

```powershell
Copy-Item "E:\Agent执行\blog-create\references\portable\*.md" `
  "e:\clients\clink\skills\clink-blog-article\references\portable\" -Force
```

---

## §6 Gotchas

- ❌ Glossary slug 加 `what-is-` 前缀
- ❌ 内链写 `/blog/agentic-payments/...` 或 `/blog/stripe-risk/...`
- ❌ 写具体 Clink 费率（C1）· MoR 全覆盖无 as-of（C2）
- ❌ FAQ 不是最后一节 · 缺 `## Conclusion`
- ❌ frontmatter 写 `keywords` / `related`
- ❌ 05–09 系列违反 `references/series-canonical-ownership.md`
- ❌ 仅加载 clink-blog-article 不加载 blog-create

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.0.0** | 2026-08-23 | L0+L1 拆分；cluster-folders（stripe-risk/agentic-payments）；selfcheck overlay |
| **2.2.0** | 2026-08-24 | 恢复 `industry-news/` 集群（15, 18）；15 主 category 改为 Industry News |
| **2.1.0** | 2026-08-24 | `agentic-payments/` 协议 definition 系列（26–29, 33） |
| 1.0.0 | 2026-07-21 | 自包含 monolith |

---

*clink-blog-article · v2.2.0 · 2026-08-24 · L1 · engine: E:\Agent执行\blog-create · audit: E:\Agent执行\blog-audit*
