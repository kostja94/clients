---
name: medo-blog-article
description: >
  Create MeDo blog articles (medo.dev/blog) from brief to draft. v2.0 adds Mode
  system, Investment Score, Phase 0R research triangle, BLUF, Gate backtracking,
  Phase 3.5/5.5 cross-checks, date strategy, tools/ validators.
metadata:
  version: 2.0.1
  project: medo.dev
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 600
  complements: ~
  forbidden-reads:
    - medo.md
    - medo-*.md
    - blog/README.md
    - blog/blog-structure-internal-links.md
---

# MeDo Blog Article Creation

为 **https://medo.dev/blog/** 从选题到英文成稿。**硬性规则：Agent 只读本 skill 文件夹内文件**（含 `references/`、`references/portable/`），禁止读取 skill 文件夹外的仓库文档（`medo.md`、`blog/README.md` 等，见 `forbidden-reads`）。发布前终审用 `references/portable/final-audit.md`。

**本文件夹自包含**：项目配置、G1–G7 + A1–A4 阻断规则、8 类路由、内容图谱、引用分级、碎片化防护、9 Phase 工作流、12 维创作自检、tools/ 验证脚本均在内联或 `references/` 中。

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
按 medo-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{PillarTutorial|GlossaryGuide|Comparison|PublishGuide|Alternative|DecisionGuide|UseCase|Diagnosis} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

批量示例：

```
按 medo-blog-article skill，为 C2 对比选择补一篇 Alternative（medo-vs-lovable）。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | 未指定→**standard**；Comparison/GlossaryGuide 自动 flagship |
| 系列 / 簇 | 可选 | hub-spoke 定位；默认 `ai-mobile-app` |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |

### 输出（Phase 6 交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief（含 SuccessMetric、MoatAssetPlanned、AnswerBlocks） | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ 完整 |
| 3 | 成稿 `medo/blog/NN-{slug}.md`（NN 见 content-graph，当前 **06**） | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表（H0–H4 + 12 维 Pass/Fail） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | Internal Link Plan | — | ✅ | ✅ |
| 8 | 终审指令（`references/portable/final-audit.md`） | ✅ | ✅ | ✅ |
| 9 | Post-publish Metric Spec | — | ✅ | ✅ |
| 10 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通策略说明可用中文；**正文必须为英文**（上线稿）。

### Agent 执行顺序

```
§2 类型路由 → §3 Phase 0 → 0R → 1–6 顺序执行 → 缺信息时先问 Phase 0 必问
```

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `medo-meta-title-description` |
| 已有完整稿，仅需发布前终审 | `references/portable/final-audit.md` |
| 非 medo.dev 博客 | 通用 blog skill |
| 非英文内容 | 另建 ZH skill |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + A1–A4 + URL 白名单 → `references/project-config.md`**
> **产品事实 + 竞品矩阵 → `references/product-competitors.md`**

**Phase 0 / Phase 5 前加载 project-config。** 核心速查：

| 配置项 | MeDo 值 |
|--------|---------|
| **品牌/产品名** | MeDo、MeDo by Baidu |
| **文档代号** | MIAODA（Baidu AI Cloud 文档体系） |
| **主域名** | medo.dev |
| **博客路径前缀** | /blog/ |
| **品类 one-liner** | Build full-stack Apps With No-Code AI Platform |
| **Blog 叙事主轴** | Ship real native iOS/Android apps with AI vibe coding |
| **消费单位** | **Credits**（定价随版本变化，须标注 as of {date}） |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **Primary ICP** | 从未打开 Xcode 的非开发者、Indie/Solo 创始人 |
| **Secondary ICP** | PM/设计师、教培机构、Affiliate/KOL |
| **Pillar Hub** | `how-to-build-mobile-app-with-ai` |
| **署名默认** | Kostja |
| **差异化核心** | 真原生 Swift/Kotlin，非 PWA/Capacitor 包装 |

### 可链接 URL 白名单（内链优先）

| 类型 | 路径示例 |
|------|---------|
| 博客 | `/blog/{slug}` — 见 `references/content-graph.md` |
| 移动构建工具页 | `/ai-mobile-app-builder` |
| 功能页 | `/features` |
| 首页 / 广场 | `/` |

**G6 规则**：不链未上线路径（`/pricing`、`/vs/*` 等待建）；forthcoming ≤1 且仅 Related 脚注；正文核心流程不用 forthcoming 链接。

### G1–G7 + A1–A4 阻断速查

| # | 阻断条件 | 说明 |
|---|---------|------|
| G1 | 事实错误 | 产品能力、Credits、移动输出类型与 medo.dev 现网矛盾 |
| G2 | 死链 | 内链 404；产品页路径错误 |
| G3 | 无来源数字 | 量化 claim 无 attribution（17k+ apps、竞品定价、市占） |
| G4 | 竞品/产品状态错误 | GA/Beta/Deprecated 与官方公告矛盾 |
| G5 | 产品能力夸大 | 禁「唯一支持」「全球首个」「唯一能上架 App Store」 |
| G6 | 内链指向未上线页面 | 对照 §1.3 白名单；forthcoming >1 → Fail |
| G7 | 品牌/合规风险 | 对比文贬低竞品；App Store 政策无来源；误导性上架承诺 |
| A1 | 平台分类错误 | 将 Web wrapper 描述为「真原生」；Swift/Kotlin vs RN vs Capacitor 分类错误 |
| A2 | 政策无时效 | App Store / Play 政策 claim 无 `as of {month} {year}` 或无可追溯官方链 |
| A3 | 对比不客观 | Comparison/Alternative 缺竞品 ≥1 真实优势；或缺 ≥1 非 MeDo 更合适场景 |
| A4 | 工具页抢词 | 博客 H1/title 抢 `/ai-mobile-app-builder` 工具页 P0 词 |

### 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **错开方向** | 从锚点日**往前**排，越重要的文章排越近 |
| **避让已占用日** | 已有文章的日期不重复使用 |

---

## §1B Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Announcement、短帖 | 最小 Research + BLUF；不追求 Excellence |
| **standard** | PublishGuide / Alternative / DecisionGuide / UseCase / Diagnosis | 完整 Research 三角 + Extractability |
| **flagship** | PillarTutorial / GlossaryGuide / Comparison | 全流程 + Moat + Excellence **必须 Yes** |

默认：用户未指定 → **standard**。ArticleType 路由表指定默认 Mode。

---

## §2 文章类型路由

> **8 类路由表 + H2 模板 + Frontmatter Schema → `references/article-types.md`**

收到任务后**先匹配类型**，再跳转对应 H2 模板与约束。

| 类型 | MeDo category | 典型 intent | 词数 | 产品提及 | 默认 Mode | 增长职能 | 参考 slug |
|------|---------------|-------------|------|----------|:---:|------|-----------|
| **PillarTutorial** | Tutorial | how to build mobile app with AI | 2800–4000 | ≤35% | flagship | ActivationTutorial | `how-to-build-mobile-app-with-ai` |
| **GlossaryGuide** | Guide | what is vibe coding | 1800–2800 | ≤20% | flagship | CategoryPOV | `what-is-vibe-coding` |
| **Comparison** | Guide | best AI mobile app builders | 2200–3200 | ≤40% | flagship | EvaluationComparison | `best-ai-mobile-app-builders` |
| **PublishGuide** | Tutorial | publish AI app App Store | 2200–3000 | ≤35% | standard | ActivationTutorial | `publish-ai-app-app-store` |
| **Alternative** | Guide | medo vs lovable / lovable alternative | 2000–2800 | ≤45% | standard | SearchCapture | `medo-vs-lovable`（待写 #06） |
| **DecisionGuide** | Guide | native vs PWA / cost / free tier | 1800–2600 | ≤30% | standard | EvaluationComparison | `native-app-vs-pwa-ai-builder` |
| **UseCase** | Tutorial / Case Study | habit tracker / app ideas | 1500–2500 | ≤50% | standard | ActivationTutorial | `build-habit-tracker-app-ai` |
| **Diagnosis** | Tutorial | app store rejection AI | 2000–2800 | ≤25% | standard | SearchCapture | `app-store-rejection-ai-apps` |
| **Announcement** | Guide | 产品发布/更新（如 TanStack SSR） | 1200–1800 | 不限 | lite | OpinionNarrative | `medo-tanstack-frontend-migration` |

**路由规则**：

- `how to` + 端到端流程 → PillarTutorial / PublishGuide / UseCase
- `what is` / `meaning` → GlossaryGuide
- `best` / 多工具列表 → Comparison
- `vs` / `alternative` → Alternative
- `native vs` / `cost` / `free` → DecisionGuide
- `rejection` / `fix` / `why rejected` → Diagnosis
- 新品 / 产品更新 → Announcement（lite；无 §2 模板，参照 Project-config 叙事）

### 增长职能

| 职能 | 核心目标 | 成功指标（Brief 必填） |
|------|---------|---------------------|
| **CategoryPOV** | 建品类认知（AI mobile app building） | 被引用/转发、品牌搜索增长 |
| **SearchCapture** | 承接明确搜索需求（how to / cost / free） | 排名、CTR、低跳出 |
| **EvaluationComparison** | 影响选型（native vs web wrapper / vs 竞品） | 注册、Demo |
| **ActivationTutorial** | 帮用户上手（build → test → publish） | 注册、上手流程完成率 |
| **OpinionNarrative** | 建立品牌人格（Announcement） | 社区讨论、Newsletter 订阅 |

### 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullet；独立传达 ~80% 价值；bullet 1 为 snippet 定义句（40–60 词） |
| **H2** | 编号 `## 1.` … `## N.`；Conclusion/FAQ/Related 不编号 |
| **Conclusion** | `## Conclusion`；CTA → `/ai-mobile-app-builder` |
| **FAQ** | `## Frequently asked questions`；**固定 6 题**；**全部内容相关**（基于本文主题，禁止通用模板题）；≥1 题覆盖边界/异议 |
| **Related** | 2–4 条；与正文互链一致（frontmatter 不含 `related`） |
| **CTA** | 单一主行动（`/ai-mobile-app-builder`），正文 ≤2 次 |
| **内链** | blog ≥2 互链；Spoke 链回 Pillar；产品页 `/ai-mobile-app-builder`、`/features` |
| **外链** | 权威 2–5；竞品 `rel="nofollow noopener"` |
| **三分类** | Comparison/Alternative/Decision 须含 Native/Cross-platform/Web wrapper 三分类框架 |

---

## §3 创作工作流（9 Phase + 5 Gate）

```
Phase 0  ─ Intake & Gate A         (§3.0：Mode + Investment Score + 六必问)
    ↓ PASS
Phase 0R ─ Research 三角 & Gate 0R  (§3.0R：R1→R2→R3→Synthesis；Degraded 可选)
    ↓ PASS / ❌ → §3.G 回溯
Phase 1  ─ Article Brief           (§3.1：SuccessMetric + Moat + AnswerBlocks)
Phase 2  ─ Slug、Date & Gate B     (§3.2)
    ↓ PASS / ❌ → §3.G 回溯
Phase 3  ─ Outline                 (§3.3：Reader mental state + Answer block ID)
Phase 3.5─ Outline 交叉检查        (§3.3.5：同批 ≥2 篇强制；单篇跳过)
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft                   (§3.4：BLUF 三处 + 段落优先协议)
    ↓
Phase 5  ─ SelfCheck & Gate C      (§3.5：Hard Gates H0–H4 + 12 维 Pass/Fail)
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit     (§3.5.5：同批 ≥2 篇强制)
Phase 6  ─ Delivery                (§3.6：含 tools 脚本 + 终审指令)
```

---

### Phase 0 — Intake & Gate A

> **Investment Score 细则 → `references/portable/investment-score.md`**
> **Gate 细则 → `references/portable/gates-master.md`**

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: CategoryPOV | SearchCapture | EvaluationComparison | ActivationTutorial | OpinionNarrative
## InvestmentScore: {1.0–5.0 均分} — {五因子摘要}
## Topic Scope: ai-mobile-app / {cluster}
## Author: Kostja
## Gate A: KEEP | MERGE → {target slug} | STOP
```

#### 0.1 信息收集（先从触发语提取，缺一再问）

触发模板已覆盖主关键词、文章类型、发布目的、目标读者。Agent 先提取已提供信息，**仅问缺失项**：

| # | 信息项 | 来源 | 何时问 |
|---|--------|------|--------|
| 1 | 主关键词 + 搜索意图 | 触发语 | 未给或模糊时问 |
| 2 | 文章类型 | 触发语 / §2 推断 | 未给时 Agent 自行推断并告知 |
| 3 | 目标读者 | 触发语（默认 ICP） | 未给时默认 Primary ICP |
| 4 | 发布目的 | 触发语 | 未给时默认 SEO |
| 5 | 与已有文章的关系 | **必问** | 每次确认：Pillar 拆文 / 新 Cluster / 竞品拦截 |
| 6 | 竞品 SERP Top 3 URL | **必问** | 每次确认；供 Phase 0R R3 Fetch |

必问项（5、6）不可跳过——即使用户已提供部分上下文，Agent 仍需显式确认 hub-spoke 定位和竞品参考。

用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

#### 0.2 Investment Score（选题投资分）

五因子各 1–5，取**算术平均**：

| 因子 | 1 分 | 5 分 |
|------|------|------|
| 搜索需求 | 几乎无搜索量 | 稳定或上升 |
| 商业相关性 | 与 ICP/产品路径无关 | 靠近购买或使用路径 |
| 差异化能力 | 只能复述 SERP | 有 Moat / Proof 可引用 |
| 证据可得性 | 无法验证强 claim | R3 可支撑 |
| 内容生命周期 | <3 月过时 | 2+ 年常青 |

| 均分 | 动作 |
|------|------|
| **≥4.0** | KEEP，按声明 Mode 执行 |
| **3.0–3.9** | KEEP 但**降级 Mode** 或改角度 |
| **<3.0** | MERGE / STOP / 降级为 FAQ·短帖 |

#### 0.3 Gate A — KEEP/MERGE

**三条件满足 ≥2 → KEEP**；否则 **MERGE** 到已有 slug 或 STOP。

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与已有 slug 关键词重叠 ≤50%（对照 `content-graph.md` 冲突表） |
| 读者旅程阶段不同 | Awareness → Tool selection → Build → Publish → Diagnosis |
| 深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

#### 0.4 信息增量 Gate（KEEP 后预检）

相对 SERP Top 3，本篇须至少提供 **1 项** MeDo 独有增量（**Phase 0R 须用 R2+R3 验证**，不得仅凭推断）：

- 「Native vs Cross-platform vs Web wrapper」三分类决策框架
- 真机 QR 测试 → TestFlight → 上架的串联路径
- App Store 政策时效段落（含 `as of {month} {year}`）
- Wirecutter 式对比表（≥1 竞品优势 + ≥1 非 MeDo 更合适场景）

---

### Phase 0R — Research 三角 & Gate 0R

> **完整 Research 三角 → `references/portable/research-triangle.md`**
> **SERP Fit 模板 → `references/portable/serp-fit-template.md`**

**加载**：`references/proof-library.md`（R1 第一步）

在 Gate A KEEP 之后、Brief 之前，**强制**收集外部证据——不依赖模型记忆写事实。

```
R1 — 读项目文档（project-config + product-competitors + content-graph + proof-library）
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（官方页 medo.dev + SERP Top 3–5 原文提取）
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

**MeDo 降级**（WebSearch 不可用）：标注 `Research mode: Degraded`；用 Phase 0 竞品 URL + `content-graph` 推演 SERP Fit；Top pages 填 `[estimated from known competitors]`；Gate 0R 仍可 Pass，SelfCheck H0 注明 Degraded；政策/定价类 P0 claim 不得写未验证数字。

**Gate 0R 阻断**：R2 未搜 / R3 未 Fetch / 无 Synthesis / 事实不可验证且需写 P0 claim → 回退补 R2/R3 或 STOP。

---

### Phase 1 — Article Brief

> **Brief 模板 + 示例 → `references/mini-example.md`**

```markdown
## Article Brief

**Mode**: lite | standard | flagship
**ArticleType**: CategoryPOV | SearchCapture | EvaluationComparison | ActivationTutorial | OpinionNarrative
**InvestmentScore**: {1.0–5.0}
**SuccessMetric**: {可量化，来自 §2 增长职能表}
**MoatAssetPlanned**: {类型，standard/flagship 必填}
  — 可选：一手产品经验 / 原创三分类框架 / 具名 workflow / 政策时效表
**AnswerBlocks**（3–5 个可摘录 H2 子问题）:
  1. …
  2. …
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**:
**Primary keyword**:
**Article type**: PillarTutorial | GlossaryGuide | Comparison | PublishGuide | Alternative | DecisionGuide | UseCase | Diagnosis
**MeDo category**: Tutorial | Guide | Case Study
**Search intent**: Informational | Commercial | Transactional | Navigational
**Reader stage**: Awareness | Tool selection | Build | Publish | Diagnosis
**Publish goal**: SEO | Brand | Conversion
**Target audience**:
**Synthesis Statement**（来自 Phase 0R）:
**One-line thesis**:
**Word count target**: {见 §2 类型词数}
**Cluster role**: Hub | Spoke | Standalone
**Cluster ID**: ai-mobile-app
**Secondary category**: mobile app
**Pillar link**: /blog/how-to-build-mobile-app-with-ai（Spoke 必填）
**Differentiation angle** (vs SERP top 3):
**Information increment** (≥1 item):
**Planned internal links** (≥2 blog + ≥1 product):
**正文互链（原 related，2–4）**:
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Disclosure needed**: Required | Recommended | Optional
**Author**: Kostja（默认）
```

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 + 反模式 → `references/slug-gate.md`**
> **H2 模板 + Frontmatter → `references/article-types.md`**

1. 2–3 slug 候选 + 推荐（Gate B：6 问全 Pass + 12 反模式零触发）
2. title（45–65 chars）+ description（120–160 chars）
3. **确定 publishDate**：读取 `references/content-graph.md` 已有日期表，从锚点日往前逐日分配，确保每自然日 ≤1 篇（§1 日期策略）
4. 完整 frontmatter
5. **复核** Phase 0R SERP Fit（有变则更新 Research Log）

**Slug 硬规则**：常青 kebab-case，**slug 不含年份**（title 可含 `for 2026`）；5–8 词，≤60 字符。

---

### Phase 3 — Outline

> **H2 模板 → `references/article-types.md`**
> **内链规划 → `references/content-graph.md`**

每节标注目标词数、Reader mental state、内链占位、Answer block ID、snippet 定义句位置。

```markdown
## Outline — {slug}

| § | H2 | Answer block ID | Reader mental state | Target words | Links / Notes |
|---|-----|-----------------|---------------------|-------------|---------------|
| Open | hook | AB-0 | 刚搜进来：找对地方了吗？ | 120–180 | 痛点 → 2026 转折 → 本文承诺 |
| TL;DR | 3–5 bullet | AB-0 | 找对地方了吗？ | 120 | bullet 1 = snippet 定义句 |
| 1 | … | AB-1 | … | … | link: /blog/... |
| … | … | … | … | … | … |
| Conclusion | 无序号 | — | 准备行动 / 仍有一个顾虑 | 150 | CTA → /ai-mobile-app-builder |
| FAQ | 固定 6 题 | — | 具体异议（来自 R2 PAA） | 400 | ≥1 objection；内容相关 |
| Related | 2–4 条 | — | — | — | 与正文互链一致 |

**Estimated total**: N words
```

**结构硬要求**：
- `## TL;DR`（3–5 bullet）
- 编号主节 `## 1.` … `## N.`
- `## Conclusion`（无序号）
- `## Frequently asked questions`（无序号，H3 每题，固定 6 题）
- `## Related articles`（与正文互链一致）

---

### Phase 3.5 — Outline 交叉检查（Draft 前）

**触发**：同批规划或并行创作 **≥2 篇**（同一 cluster、同一 campaign、或 content-graph 排期相邻）。

**目的**：在只有 H2 骨架时拦截跨篇重复——比 Phase 5.5 全文审计便宜一个数量级。**不替代** Phase 5.5。

**检查项**（详见 `references/portable/outline-cross-check.md`）：
- [ ] H2 标题重复度：同 cluster 内是否有 ≥2 篇同一 H2 措辞？
- [ ] 叙事弧相似：是否都是「定义→列表→对比→FAQ→CTA」且无角度差异？
- [ ] Canonical 越界：非 canon 文 Outline 是否计划展开 hub 才该全量写的概念？
- [ ] Synthesis 冲突：两篇 One-line thesis 是否互相重叠 >50%？
- [ ] **内链缺口**：新文章是否满足互链要求（Spoke 链回 Pillar）？

**Fail** → 改 Outline / 改 Synthesis / MERGE 建议 / 补内链规划 → 重过 3.5
**Pass** → 输出 `Outline cross-check: PASS — {slugs}` → Phase 4

单篇创作：跳过 3.5，标注 `N/A — single article`。

---

### Phase 4 — Draft

> **加载顺序**（每次 ≤2 文件）：
> 1. `references/presentation.md`（Voice + 碎片化 + 段落优先协议 + FAQ 固定 6 题）
> 2. `references/product-competitors.md`（产品事实 + 竞品矩阵）
> 3. `references/project-config.md`（G1–G7 + A1–A4 对照）

**flagship Mode 额外加载**：`references/portable/extractability-checklist.md`（BLUF + Claim + Judgment）+ `references/portable/perfect-article-checklist.md`

#### 4.0 创作原则

**Different, not better**：不是在 Top3 上「写得更全」，而是提供 Top3 没有的决策维度。MeDo 的差异化空间：真原生 vs Web wrapper 路线之争、真机 QR → TestFlight → 上架串联路径、App Store 政策时效分析。

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
| 站内 | `/blog/{slug}`、`/ai-mobile-app-builder`、`/features` |
| Comparison / Alternative | 开篇后 Disclosure；三分类框架 + 对比表 + ≥1「何时不选 MeDo」（A3） |
| Tutorial | 步骤用祈使句；每大步后接「为什么这步重要」 |
| Publish / Diagnosis | 加载 `references/app-store-compliance.md`；政策 claim 含 as-of（A2） |
| 引用 | 按 `references/citations.md` P0/P1/P2 分级；P0 数字必须 `[Source: URL]` |
| 产品提及 | 不超过 §2 类型上限 |
| 段落 | ≥3 长段（4–8 句）；连续短段 ≤2；段间衔接率 ≥70%；**伪列表 = 自动 Fail** |
| 内链 | blog ≥2；Spoke 链回 Pillar；canonical 概念 1–2 句 + link |
| 竞品 | 每竞品 ≥1 优势；禁 just/merely/only does X |
| 模块顺序 | YAML → TL;DR → H2 → Conclusion → FAQ → Related |

---

### Phase 5 — SelfCheck & Gate C

> **完整 12 维 checklist + H0–H4 → 见下**
> **完整 Gate 细则 → `references/portable/gates-master.md`**

#### 工具先跑

在人工 Gate C 检查前，先跑 `tools/` 脚本（**从 medo/ 项目根目录运行**）：

```bash
python skills/medo-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary kw}"
python skills/medo-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {pillartutorial|glossaryguide|comparison|publishguide|alternative|decisionguide|usecase|diagnosis|announcement}
python skills/medo-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/vs,/templates
```

#### Hard Gates（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填（或 Degraded 已标注且无未验证 P0 claim） |
| **H1** | P0 Gate G1–G7 + A1–A4 | 零触发 |
| **H2** | Slug Gate B | Design-Time 六问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | MeDo-Specific | 产品提及比例合规；Native vs PWA 叙事一致；secondary_category 一致；无工具页抢词 |

#### Pass/Fail 12 维

| # | 维度 | Pass 标准（摘要） |
|---|------|------------------|
| 1 | **Publishability** | H0–H4 全 Pass |
| 2 | **Fact / E-E-A-T** | P0 数字有来源；政策有 as-of + 官方链 |
| 3 | **Differentiation** | ≥1 项 SERP 独有增量；正文**兑现** Synthesis |
| 4 | **Depth** | 词数达 §2 类型阈值；FAQ 独立于正文 |
| 5 | **Presentation & Rhythm** | 长段落 ≥3；列表比例合规；衔接率 ≥70%；伪列表 0 |
| 6 | **Writing / Voice** | 非开发者友好；禁 hype（revolutionary/game-changing） |
| 7 | **Objectivity** | 对比文：≥1 竞品优势 + ≥1 非 MeDo 场景（A3） |
| 8 | **Structure / Links** | ≥2 blog 内链；Spoke 链回 Pillar；模块顺序正确 |
| 9 | **SEO / SERP** | title 45–65；description 120–160；关键词自然分布；BLUF 三处 Pass |
| 10 | **Conversion** | CTA ≤2；主 CTA → `/ai-mobile-app-builder` |
| 11 | **Slug Design** | Gate B 6 问 + 12 反模式零触发 |
| 12 | **MeDo-Specific** | Native vs PWA 叙事一致；secondary_category 一致；无工具页抢词（A4） |

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**（可进入终审，≠ publish-ready）。任一 Fail → 标注修复动作 → 按 §3.G 回溯表回退修复。

#### Perfect-Ready 附加清单（flagship 专用）

- [ ] Moat Asset 已在正文兑现
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 类型已标注
- [ ] Post-publish Metric Spec 已写入 Brief

---

### Phase 5.5 — Cross-Article Audit

**触发**：同批创作 ≥2 篇。**不替代** Phase 3.5（Outline 级），此为全文级。

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

1. 写入 `medo/blog/NN-{slug}.md`
2. 输出 Article Brief 最终版
3. 输出 SelfCheck 表（H0–H4 + 12 维全 Pass）
4. **Source Map**（Claim × Paragraph × Source × Confidence，≥3 行）
5. **Internal Link Plan**
6. **Signal of Excellence 标注**：
   - `Excellence: Yes — {类型}`（原创框架 / 反直觉数据 / 可执行 checklist / 具名案例 / 洞见）
   - `Excellence: No — 合格但无记忆点`
7. **Moat Asset 兑现检查**：对照 Brief `MoatAssetPlanned`，成稿是否兑现？

**终审指令模板**（复制给用户）：

```markdown
请用本 skill 内 references/portable/final-audit.md 对以下文章做发布前终审：
- 文件：medo/blog/{NN}-{slug}.md
- 类型：{Article type}
- 主关键词：{primary keyword}
- SelfCheck 摘要：{Pass 数}/12

要求：
1. 先过 P0 Gate G1–G7 + A1–A4
2. 逐维评分（A–J 十维加权 → 100 分）
3. 输出十维评分 + 总分 + 等级（S/A/B/C/D）+ Excellence + Moat + Perfect gap
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

**判定写作 vs 结构**：Fail 项落在维度 4–6、10 → 优先 Phase 4；维度 8–9、11 → 优先 Phase 2–3；维度 2 → Phase 4 + 事实核查。

---

## §4 内容图谱指针

> **完整图谱、排期、Golden Examples → `references/content-graph.md`**

| 项 | 值 |
|----|-----|
| **Hub slug** | `how-to-build-mobile-app-with-ai` |
| **Cluster ID** | `ai-mobile-app` |
| **下一文件序号** | **06** |
| **下一篇 P0 优先级** | `06-medo-vs-lovable.md` |
| **已发布** | 5 篇（#01–#05） |
| **规划中** | #06–#13 + Batch 4 候选 |

---

## §5 Frontmatter 与文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{slug-kebab}.md` |
| NN | 两位递增；下一号 **06** |
| slug | kebab-case；含 primary keyword；常青无年份 |

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: 2026-08-XX       # 发布时间，永不改变
updated: 2026-08-XX    # 可选；最近一次实质性内容更新；无更新则省略
author: "Kostja"
category: "Tutorial | Guide | Case Study"
secondary_category: "mobile app"
disclosure: "..."      # Comparison/Alternative 必填
---
```

> **2026-08-11 起废弃**：`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords/related 由正文内链与 CMS 配置承载）。
>
> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅**实质性更新**（新增数据/章节/修正事实）时更新，错别字/样式不动它。页面**只显示一个日期**（有 `updated` 显示它）——勿同时显示两个日期。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

---

## §6 本 skill 内文档分工

| 阶段 | 文档 | 维护 |
|------|------|------|
| 选题 → 成稿 | 本 SKILL + `references/` | Agent |
| Phase 0 | `investment-score.md` · `gates-master.md` | Mode + Investment |
| Phase 0R | `research-triangle.md` + `proof-library.md` | Synthesis + Examples |
| Phase 1 | `mini-example.md` | Brief 模板 |
| Phase 2–3 | `article-types.md` + `slug-gate.md` + `keywords.md` | 创作 |
| Phase 3.5 | `outline-cross-check.md` | 同批 ≥2 篇 |
| Phase 4 | `presentation.md` + `extractability-checklist.md` | flagship 加 `perfect-article-checklist.md` |
| Phase 5 | `tools/` 脚本 + 本 SKILL §3.5 | H0–H4 + 12 维 |
| Source Map / SERP Fit | `source-map-template.md`、`serp-fit-template.md` | 随 skill 分发 |
| 发布后 | `post-publish-review.md` | T+7/30/90 |
| 发布前终审 | `final-audit.md` | 人类 / 另一 Agent |
| 策略文档 | `medo-keywords.md`、`blog-structure-internal-links.md`、`blog/README.md` | 人类；变更时 bump skill `version` |

**版本同步**：当 `blog/README.md` 文章表新增已发布稿、或关键词簇排期变更时，人类应同步更新 `references/content-graph.md` 与 `references/keywords.md`，并将 SKILL.md frontmatter `version` patch bump（如 2.0.0 → 2.0.1）。

**发布后必做 checklist**（每发布一篇须人类执行）：
1. bump 本文件 §0 输出区 + §4 的「下一文件序号」（当前 **06**）
2. bump `references/content-graph.md` §2 的「下一文件序号」
3. 更新 `references/content-graph.md` §2 已发布文章登记表（新增行）
4. 更新 `references/content-graph.md` §3 排期表（标记 ✅）
5. bump 本文件 frontmatter `version` patch（如 2.0.0 → 2.0.1）
6. 若 `references/mini-example.md` 范例对应本篇，替换为下一篇 P0

**Agent 防护**：若 Phase 0 发现用户请求的序号与 §4 序号不一致，须先确认是否已有人类更新的文章未反映在 skill 中。

---

## Gotchas — 禁止项（精选）

**结构**：❌ 编号 H2 用于 Conclusion/FAQ/Related · ❌ TL;DR 仅重复 title · ❌ FAQ <6 题 · ❌ FAQ 用通用模板题 · ❌ 连续 3+ 短段 · ❌ 列表占比超类型上限
**写作**：❌ revolutionary/game-changing/seamless/magic · ❌ just/merely 贬低竞品 · ❌ 假装零工作量 · ❌ 空泛句（generic claims）
**Slug/链接**：❌ slug 含年份 · ❌ slug 含内部架构词（framework/strategy/diagnosis/complete-guide）· ❌ 链 `/pricing`、`/vs/*`、`/templates/*` 未上线路径 · ❌ forthcoming >1 · ❌ 锚文本 click here/learn more
**产品/Proof**：❌ 17k+ apps 无来源限定 · ❌ Credits 写死价格（须 as of date）· ❌ 待验证声明用确定性语气（须 "reportedly"/"claims to offer"）
**流程**：❌ Gate 未全 Pass 交付 · ❌ 一次加载全部 references · ❌ 运行时读 medo-*.md · ❌ 跨篇 ≥2 篇但未跑 Phase 3.5/5.5

---

## §7 Reference 文件索引

| 文件 | 加载时机 | 内容 |
|------|----------|------|
| `references/proof-library.md` | Phase 0R, 4, 5 | Product Fact Ledger、Proof ID |
| `references/project-config.md` | Phase 0, 0R, 5 | 品牌、URL、G1–G7、A1–A4 |
| `references/product-competitors.md` | Phase 0R, 4, 5 | MeDo 事实表、竞品矩阵（R3 验证） |
| `references/content-graph.md` | Phase 0, 0R, 3, 4 | Hub-Spoke、已发/待写、内链、Golden |
| `references/keywords.md` | Phase 0, 2 | P0/P1/P2、禁抢词 |
| `references/article-types.md` | Phase 2, 3, 4 | 8 类 H2 模板、Frontmatter |
| `references/slug-gate.md` | Phase 2 | Slug 6 问、12 反模式 |
| `references/app-store-compliance.md` | Phase 4 | 上架、拒审、TestFlight |
| `references/citations.md` | Phase 4, 5 | P0/P1/P2、Source Map |
| `references/presentation.md` | Phase 4, 5 | Voice、碎片化、对比表、段落优先协议、FAQ |
| `references/mini-example.md` | Phase 1, 3 | Brief + Outline 范例（#06） |
| `references/portable/research-triangle.md` | Phase 0R | Research 三角流程 |
| `references/portable/investment-score.md` | Phase 0 | 五因子 Investment Score |
| `references/portable/gates-master.md` | Phase 0, 5 | Gate 总表速查 |
| `references/portable/extractability-checklist.md` | Phase 4, 5 | BLUF + Claim 原子性 + Judgment |
| `references/portable/source-map-template.md` | Phase 5, 6 | Source Map 模板 |
| `references/portable/serp-fit-template.md` | Phase 0R | SERP Fit 模板 |
| `references/portable/outline-cross-check.md` | Phase 3.5 | 交叉检查模板 |
| `references/portable/perfect-article-checklist.md` | Phase 5（flagship） | S 级标杆清单 |
| `references/portable/final-audit.md` | Phase 6 | 发布前终审 |
| `references/portable/post-publish-review.md` | Phase 6（Brief 参考） | 发布后复盘 |
| `references/portable/retro-audit.md` | 独立场景 | 已发布稿回溯审计 |
| `tools/frontmatter_validator.py` | Phase 5 | Frontmatter 机器检查 |
| `tools/word_count_narrative.py` | Phase 5 | 字数硬门槛 H3 检查 |
| `tools/link_checker.py` | Phase 5 | P0 G2/G6 链接检查 |
| `tools/README.md` | Phase 5 | 工具使用说明 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.0.1** | 2026-08-14 | Frontmatter schema 调整：`cluster` 字段改为 `secondary_category: "mobile app"`；移除 `platform_note` 字段（政策时效改由正文 as-of 引用块承载，A2 Gate 不变）。同步更新 validator F5b、article-types、mini-example、project-config、content-graph、app-store-compliance、README、outputs |
| **2.0.0** | 2026-08-14 | 对齐 v2 标准模板：9 Phase + 5 Gate；新增 Mode 系统（lite/standard/flagship）+ Investment Score 五因子 + BLUF 三处 + §3.G Gate 回溯 + H0–H4 Hard Gates + Phase 3.5/5.5 交叉检查 + 日期发布策略 + tools/ 验证脚本 + 交付物扩展（Source Map/Internal Link Plan/Excellence/Moat）+ Changelog/Gotchas + 六角色换帽 |
| **1.1.0** | — | 初代结构：7 Phase + 3 Gate + 8 类路由 + G1–G7 + A1–A4 + references/portable/ |

---

## v2.1 Backlog

| # | 项目 | 优先级 |
|---|------|:---:|
| 1 | `medo-meta-title-description` skill | P1 |
| 2 | 12 维 SelfCheck 加权评分（对齐 dubbingai/hellyeah S/A/B/C/D） | P2 |
| 3 | Cross-Article Audit 扩展 CA1–CA10 完整版 | P2 |

---

*medo-blog-article · v2.0.1 · 2026-08-14 · fully self-contained · references/portable/* · tools/* · 8 article types + Mode + Investment Score + Phase 0R + BLUF + Gate Backtracking*
