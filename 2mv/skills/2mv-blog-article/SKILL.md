---
name: 2mv-blog-article
description: Create 2mv blog articles (2mv.ai/insights) from brief to draft. v1.0 adapts the vatt/luciusai 9-Phase + 5-Gate + Mode system for an agentic growth agency / viral research SaaS.
metadata:
  version: 1.0.0
  project: 2mv.ai
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 600
  complements: ~
  forbidden-reads:
    - ../2mv-competitors.md
    - ../2mv-features.md
    - ../blog/README.md
---

# 2mv Blog Article Creation

为 **https://2mv.ai/insights/** 从选题到英文成稿。**硬性规则：Agent 只读本 SKILL + `references/`（含 `references/portable/`），禁止读 skill 文件夹外文档。**

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
按 2mv-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Research|Comparison|Product|Alternative|Announcement} 文章。
发布目的：{SEO|品牌|转化|社区}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Mode | 可选 | 未指定→**standard**；Announcement 自动 lite，Research/Comparison 自动 flagship |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |

### 输出（交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief（含 SuccessMetric、MoatAssetPlanned、AnswerBlocks） | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis） | 简 | ✅ | ✅ 完整 |
| 3 | 成稿 `2mv/blog/NN-{slug}.md`（NN 见 content-graph，当前 **02**） | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表（Hard Gates + 12 维 Pass/Fail） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | OG Image Prompt（1200×630） | ✅ | ✅ | ✅ |
| 8 | Internal Link Plan | — | ✅ | ✅ |
| 9 | templates 审核指令（复制即用） | ✅ | ✅ | ✅ |
| 10 | Post-publish Metric Spec | — | ✅ | ✅ |
| 11 | 提示人类更新 `blog/README.md` | ✅ | ✅ | ✅ |

与用户沟通策略说明可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `2mv-meta-title-description` |
| 非 2mv.ai 博客 | 对应项目的 blog skill |
| 中文站内容 | 另建 ZH skill |
| 已发稿回溯审计 | `references/portable/retro-audit.md` |

---

## §1 项目配置速查

> **完整配置 + G1–G8 + URL 白名单 → `references/project-config.md`**
> Phase 0R 加载。Phase 4/5 按需重载。

| 配置项 | 2mv 值 |
|--------|-------------|
| **品牌/产品名** | 2mv（2mv Research Lab · 公司 Fluxspark Inc.） |
| **主域名** | 2mv.ai |
| **博客路径前缀** | `/insights/`（注意：非 `/blog/`） |
| **产品定位** | 把「病毒式传播」从运气变成系统的 agentic growth agency + 病毒内容研究 SaaS——"From zero to millions of views" |
| **品类 one-liner** | An agentic growth agency that turns organic short-form views into a repeatable system — signal detection, pattern decoding, topic architecture, production at velocity, compounding growth |
| **核心能力（双形态）** | ① 代运营五引擎：Watch→Decode→Architect→Produce→Grow；② Research Lab SaaS 5 视图：Market Signals / Target Tracking / Viral Breakdown / Content Patterns / Viral Playbook |
| **目标用户** | 增长/社媒团队、DTC/消费品牌、SaaS 创始人、代理机构、UGC 创作者 |
| **画布/平台** | TikTok · Instagram Reels · YouTube Shorts（三平台） |
| **关键指标** | 官网自报（⚠️ 待验证）：12,000+ videos/day、500+ niches、100M+ organic views、170+ brands——引用时须标注"as stated on 2mv's site" |
| **定价** | Research Lab：Kick-Off $139/Pro $399/Scale $999/Custom；年付 8 折；代运营按结果报价（不公开） |
| **署名默认** | `2mv Team` |
| **语言** | 英文正文；中文仅沟通用 |
| **禁止内链** | 未上线页面（/pricing、/service、/niches/* 待建） |

### G1–G8 阻断速查

| # | 阻断条件 | 说明 |
|---|---------|------|
| G1 | 事实错误 | 产品能力、数据与官网 / 2mv-features.md 矛盾 |
| G2 | 死链 | 站内或站外链接 404 |
| G3 | 无来源数字 | 量化 claim 无 attribution；官网自报指标未标注为官网声称 |
| G4 | 竞品状态错误 | 竞品定位 / 融资 / 数据与公开来源矛盾 |
| G5 | 产品能力夸大 | self-reported 指标写成第三方验证事实；双形态描述与官网矛盾 |
| G6 | 内链指向未上线页面 | 只链白名单内路径 |
| G7 | 品牌风险 | 贬低性措辞 |
| G8 | 夸大禁令 | Claims Must Not Publish 句式（guarantees viral / guaranteed views / 无证据 "first" 断言） |

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
| **standard** | Product / Scenario、Alternative | 完整 Research 三角 + Extractability |
| **flagship** | Research / Glossary、Comparison | 全流程 + Moat + Excellence **必须 Yes** |

默认：用户未指定 → **standard**。ArticleType 路由表指定默认 Mode。

---

## §2 文章类型路由

> **5 类路由表 + H2 模板 → `references/article-types.md`**
> Phase 0 加载路由表。Phase 3/4 加载模板。

### 路由速查

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | 增长职能 |
|------|--------|------|:---:|:---:|------|
| Research / Glossary | 定义/概念 | 2000–3000 | ≤25% | flagship | CategoryPOV |
| Comparison | 商业调查 | 2500–3500 | ≤40% | flagship | EvaluationComparison |
| Alternative | 竞品替代 | 2000–2800 | ≤35% | standard | SearchCapture |
| Product / Scenario | 场景/workflow | 2000–2800 | ≤40% | standard | ActivationTutorial |
| Announcement | 产品发布 | 1200–1800 | 不限 | lite | OpinionNarrative |

**路由**：`what is`→Research · `best`→Comparison · `alternative`+竞品名→Alternative · `how to`→Product · 新品→Announcement

2mv 内容侧重点：病毒增长品类教育（Research）+ 病毒解码/选题实操（Product）+ 有机 vs 付费路线之争与 2mv-vs-竞品选型（Comparison）为核心三角。

### 增长职能

| 职能 | 核心目标 | 成功指标（Brief 必填） |
|------|---------|---------------------|
| **CategoryPOV** | 建品类认知（agentic growth agency / viral research 品类） | 被引用/转发、品牌搜索增长 |
| **SearchCapture** | 承接明确搜索需求（how to go viral 等） | 排名、CTR、低跳出 |
| **EvaluationComparison** | 影响选型（有机 vs 付费 / 2mv vs 竞品） | Demo、注册 |
| **ActivationTutorial** | 帮用户上手（病毒解码/选题工作流） | 注册、上手流程完成率 |
| **OpinionNarrative** | 建立品牌人格 | 社区讨论、Newsletter 订阅 |

### 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullet；独立传达 ~80% 价值；bullet 1 为 snippet 定义句（40–60 词） |
| **H2** | 英文描述性标题；FAQ 不编号 |
| **Conclusion** | `## N. Conclusion` |
| **FAQ** | **固定 6 题**；`## FAQ`；**全部内容相关**（基于本文主题，禁止通用模板题）；≥1 题覆盖边界/异议 |
| **CTA** | 单一主行动（/research 或 /book-a-demo），分散在正文 ≤2 次 |
| **内链** | blog ≥2 互链；product mention 1–2 次 |
| **外链** | 权威 2–6；竞品 `rel="nofollow noopener"` |

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
Phase 3  ─ Outline                 (§3.3：Reader mental state + BLUF + OG Image)
Phase 3.5─ Outline 交叉检查        (§3.3.5：同批 ≥2 篇强制；单篇跳过)
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft                   (§3.4：BLUF 三处 + 按需加载 references)
    ↓
Phase 5  ─ SelfCheck & Gate C      (§3.5：Hard Gates H0–H4 + 12 维 Pass/Fail)
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit     (§3.5.5：同批 ≥2 篇强制)
Phase 6  ─ Delivery                (§3.6：含 tools 脚本 + templates 审核指令)
```

---

### Phase 0 — Intake & Gate A

> **Investment Score 细则 → `references/portable/investment-score.md`**
> **Gate 细则 → `references/gates.md`**

**Phase 0 首行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: CategoryPOV | SearchCapture | EvaluationComparison | ActivationTutorial | OpinionNarrative
## InvestmentScore: {1.0–5.0 均分} — {五因子摘要}
## Category: {Research | Comparison | Product}
## Author: 2mv Team
## Gate A: KEEP | MERGE → {target slug} | STOP
```

#### Investment Score（选题投资分）

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

#### 六必问（信息不足时先问用户）

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 目标受众？ |
| 2 | 发布目的（品牌 / SEO / 转化 / 社区）？ |
| 3 | 与已有内容 / 竞品内容的竞争关系（2–3 个竞品 URL）？ |
| 4 | 文中内链指向的页面是否已上线？ |
| 5 | 文章署名作者？（默认 `2mv Team`） |
| 6 | 文章分类（category）：Research / Comparison / Product？ |

用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

#### KEEP / MERGE 判定

三条件满足**任意两个** → KEEP；否则 MERGE 或 STOP：

| 条件 | 判断方法 |
|------|---------|
| 搜索意图独立 | 与已有文章 primary keyword 搜索池重叠 <50% |
| 读者阶段不同 | Awareness / Consideration / Evaluation / Activation 不重叠 |
| 内容深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

**Gate A 阻断**：MERGE / STOP / Investment <3.0 / 必问缺失无法推断 → STOP。

---

### Phase 0R — Research 三角 & Gate 0R

> **完整 Research 三角 → `references/portable/research-triangle.md`**
> **SERP Fit 模板 → `references/portable/serp-fit-template.md`**

在 Gate A KEEP 之后、Brief 之前，**强制**收集外部证据——不依赖模型记忆写事实。

```
R1 — 读项目文档（project-config + product-competitors + content-graph）
    ↓
R2 — Web 搜索（primary keyword → SERP Top 5 + PAA）
    ↓
R3 — Fetch URL（官方页 https://www.2mv.ai/ + SERP Top 3–5 原文提取）
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

**Degraded 模式**：当 R2/R3 信息缺失时标注 `Research mode: Degraded — {reason}`。Degraded 下正文**不得**写 P0 级未验证 claim。

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
  — 可选：一手产品经验 / 原创框架/决策树 / 具名 workflow
**AnswerBlocks**（3–5 个可摘录 H2 子问题）:
  1. …
  2. …
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**:
**Primary keyword**:
**Search intent**: Definition | Comparison | Tutorial | Alternative | Commercial
**Category** (frontmatter): Research | Comparison | Product
**Reader stage**: Awareness | Consideration | Evaluation | Activation
**Publish goal**: SEO | Brand | Conversion | Community
**Target audience**:
**Synthesis Statement**（来自 Phase 0R）:
**One-line thesis**:
**Differentiation angle**（vs SERP top 3–5）:
**Information increment** (≥2 项，每条对应 Log + Synthesis):
  - [ ] …
  - [ ] …
**Candidate examples** (from Log):
**Word count target**: {见 §2 类型词数}
**Topic Scope / Cluster**: {hub-spoke 角色}
**Planned internal links** (≥2 blog):
**Slug candidate**: {kebab-case}
**Author**: 2mv Team（默认）
```

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 + 反模式 → `references/slug-gate.md`**
> **Gate B 细则 → `references/gates.md`**

1. 产出 2–3 slug 候选 + 推荐（对照反模式表 + 大声读测试）
2. **确定 publishDate**：读取 `references/content-graph.md` 已有日期表，从锚点日往前逐日分配，确保每自然日 ≤1 篇（§1 日期策略）
3. **Gate B**：6 项全 Pass → 继续；Fail → 重选 slug

---

### Phase 3 — Outline

> **H2 模板 → `references/article-types.md`**
> **内链规划 → `references/internal-links.md`**

每节标注目标词数、Reader mental state、内链占位、Answer block ID、snippet 定义句位置。

```markdown
## Outline — {slug}

| § | H2 | Answer block ID | Reader mental state | Target words | Links / Notes |
|---|-----|-----------------|---------------------|-------------|---------------|
| TL;DR | … | AB-0 | 刚搜进来：找对地方了吗？ | 80–120 | bullet 1 = snippet 定义句 |
| 1 | … | AB-1 | … | … | link: … |
| … | … | … | … | … | … |
| Conclusion | … | — | 准备行动 / 仍有一个顾虑 | 120–180 | CTA |
| FAQ | 6 | — | 具体异议（来自 R2 PAA，保持内容相关） | … | ≥1 objection |
**Estimated total**: N words
```

**OG Image Prompt**：在此 Phase 生成主 prompt + 2 variant（1200×630），参考 SKILL.md §5 的 image 路径规范。

---

### Phase 3.5 — Outline 交叉检查（Draft 前）

**触发**：同批规划或并行创作 **≥2 篇**（同一 cluster、同一 campaign、或 content-graph 排期相邻）。

**目的**：在只有 H2 骨架时拦截跨篇重复——比 Phase 5.5 全文审计便宜一个数量级。**不替代** Phase 5.5。

**检查项**：
- [ ] H2 标题重复度：同 cluster 内是否有 ≥2 篇同一 H2 措辞？
- [ ] 叙事弧相似：是否都是「定义→列表→对比→FAQ→CTA」且无角度差异？
- [ ] Canonical 越界：非 canon 文 Outline 是否计划展开 hub 才该全量写的概念？
- [ ] Synthesis 冲突：两篇 One-line thesis 是否互相重叠 >50%？
- [ ] **内链缺口**：对照 `references/internal-links.md`，新文章是否满足互链要求？

**Fail** → 改 Outline / 改 Synthesis / MERGE 建议 / 补内链规划 → 重过 3.5
**Pass** → 输出 `Outline cross-check: PASS — {slugs}` → Phase 4

单篇创作：跳过 3.5，标注 `N/A — single article`。

---

### Phase 4 — Draft 写作约束

> **加载顺序**（每次 ≤2 文件）：
> 1. `references/writing-constraints.md`（Voice + 引用分级 + 漏斗透明度 + **段落优先协议**）
> 2. `references/product-competitors.md`（产品事实 + 竞品对照 + Claims 禁令）
> 3. `references/project-config.md`（G1–G8 对照）

#### 4.0 创作原则

**Different, not better**：不是在 Top3 上「写得更全」，而是提供 Top3 没有的决策维度。2mv 的差异化空间：有机 vs 付费增长路线之争、五引擎复利闭环、病毒逐帧解码（vs 表面数据看板）。

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

#### 4.2 Degraded 模式意识

Phase 0R 标注 `Degraded` 时：正文无 P0 级未验证 claim；每个基于推理的断言须用限定词（"likely""emerging""in our observation"）；不确定事实标 `[internal observation]`。

#### 4.3 核心约束速查

- **引用**：只链权威来源（官方产品页/文档/官方数据）；营销 SEO 文章一律不链，改写为普通陈述（见 writing-constraints §2.1）；P0 级数字必须有权威来源，否则弱化表述
- **Claims 禁令**：零触发 G8（guarantees viral / guaranteed views / 无证据 "first" 断言）
- **漏斗**：Research 文前 70% 不可见 funnel
- **段落**：≥3 长段（4–8 句）；连续短段 ≤2；段间衔接率 ≥70%；**伪列表 = 自动 Fail**
- **内链**：blog ≥2；canonical 概念 1–2 句 + link；路径用 `/insights/{slug}`；外链 rel="nofollow noopener"
- **竞品**：每竞品 ≥1 优势；禁 just/merely/only does X
- **模块顺序**：YAML → TL;DR → H2 → Conclusion → FAQ
- **Claim 原子性**：段首 claim · 指代可解析 · chunk 可独立理解
- **Judgment J1–J2**：强判断均 scoped + 同段/前段有依据

---

### Phase 5 — SelfCheck & Gate C

> **完整 12 维 checklist + H0–H4 → `references/selfcheck.md`**
> **完整 Gate 细则 → `references/gates.md`**

#### 工具先跑

在人工 Gate C 检查前，先跑 `tools/` 脚本（**从 2mv/ 项目根目录运行**）：

```bash
python skills/2mv-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary kw}"
python skills/2mv-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {research|comparison|product|alternative|announcement}
python skills/2mv-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/service,/niches
```

#### Hard Gates（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填 |
| **H1** | P0 Gate G1–G8 | 零触发 |
| **H2** | Slug Gate B | Design-Time 六问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | 2mv-Specific | 产品提及比例合规；五引擎/5 视图描述准确；self-reported 指标标注为官网声称；Claims 禁令零触发 |

#### Pass/Fail 12 维

| # | 维度 | Pass 条件摘要 |
|---|------|-------------|
| 1 | Publishability | H0–H4 全 Pass |
| 2 | Fact / E-E-A-T | 可验证 claim 有来源；Source Map 已填 |
| 3 | Differentiation | 正文**兑现** Synthesis；IG 三问在成稿仍成立 |
| 4 | Depth / Density | 词数达标；FAQ 独立于正文 |
| 5 | Presentation / Rhythm | 长段 ≥3；列表占比合规；衔接率 ≥70%；伪列表 0 |
| 6 | Writing / Voice | Voice 5 项 + 空泛句阈值 + 禁词扫描 Pass |
| 7 | Objectivity | 产品占比合规；竞品无贬低 |
| 8 | Structure / Links | 模块完整；blog 互链 ≥2 |
| 9 | SEO / SERP | title 含 primary keyword；SERP Fit 已填；BLUF 三处 Pass |
| 10 | Conversion | CTA ≤2；匹配读者阶段 |
| 11 | Slug Design | Gate B + 反模式零触发 |
| 12 | Cross-Article | 同 cluster 无矛盾/重复（单篇 N/A） |

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**（可进入加权终审）；任一 Fail → 标注修复动作 → 按 §3.G 回溯表回退修复。

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

1. 写入 `2mv/blog/NN-{slug}.md`
2. 输出 Article Brief 最终版
3. 输出 SelfCheck 表（H0–H4 + 12 维全 Pass）
4. **Source Map**（Claim × Paragraph × Source × Confidence，≥3 行）
5. OG Image Prompt（主 prompt + 2 variant，1200×630）
6. Internal Link Plan
7. **Signal of Excellence 标注**：
   - `Excellence: Yes — {类型}`（原创框架 / 反直觉数据 / 可执行 checklist / 具名案例 / 洞见）
   - `Excellence: No — 合格但无记忆点`
8. **Moat Asset 兑现检查**：对照 Brief `MoatAssetPlanned`，成稿是否兑现？

**templates 审核指令**：

```
请按 references/portable/final-audit.md 审核 2mv/blog/NN-{slug}.md

项目配置：
- 品牌：2mv（2mv Research Lab）
- 主域名：2mv.ai
- 博客前缀：/insights/
- 受众：增长/社媒团队、DTC 品牌、SaaS 创始人、代理机构、创作者
- 禁止内链：未上线页面（/pricing、/service、/niches 待建）
- 额外：G8 夸大禁令扫描（guarantees viral / self-reported 指标标注）

要求：
1. 先过 P0 Gate G1–G8
2. 逐维评分（A–J 十维加权 → 100 分）
3. 输出十维评分 + 总分 + 等级（S/A/B/C/D）+ Excellence + Moat + Perfect gap
4. 标记 P1/P2
```

9. **提示人类**更新 `blog/README.md` 文件表

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
| **Gate C ❌ — G8 夸大** | **Phase 4** | Claims Must Not Publish 句式 | 删改 claim + 按 product-competitors.md §6 重写 |

**判定写作 vs 结构**：Fail 项落在维度 4–6、10 → 优先 Phase 4；维度 8–9、11 → 优先 Phase 2–3；维度 2 → Phase 4 + 事实核查。

---

## §4 已有内容图谱

> **→ `references/content-graph.md`**（Phase 0/0R/1/5 按需加载）

1 篇登记（`what-is-2mv`）· 下一序号 **02** · 规划主题簇见 content-graph
> 注：官网 `/insights` 另有官方文 `how-to-find-viral-content-ideas-before-they-peak`（非本 skill 产出，作 canonical 占用词）。

---

## §5 Frontmatter 与文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{slug-kebab}.md` |
| NN | 两位递增；下一号 **02** |
| slug | kebab-case；含 primary keyword；常青无年份 |

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "140–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: 2026-08-XX       # 发布时间，永不改变
updated: 2026-08-XX    # 可选；最近一次实质性内容更新；无更新则省略
author: "2mv Team"
category: "Research | Comparison | Product"
---
```

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理）。
>
> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅实质性更新时更新。页面只显示一个日期（有 `updated` 显示它）——勿同时显示两个日期。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。
>
> **官网 CMS 扩展字段**（可选，仅官网发布时使用；本仓库归档一律不写）：`metaTitle` / `excerpt` / `badge` / `breadcrumb` / `authorInitials` / `publishedAt` / `readTime` / `tldr`。TL;DR 信息一律写入正文 `## TL;DR`。

---

## §6 本 skill 内文档分工

| 阶段 | 文档 |
|------|------|
| 选题前 Strategy | 本 SKILL §2（增长职能、Mode 默认） |
| Phase 0 Intake + Investment | 本 SKILL §3.0 + `references/gates.md` |
| Phase 0R Research | `references/portable/research-triangle.md` |
| Phase 1 Brief | 本 SKILL §3.1 + `references/mini-example.md` |
| Phase 2–3 创作 | 本 SKILL §3.2–3.3 + `references/article-types.md` + `references/slug-gate.md` |
| Phase 4 Draft | 本 SKILL §3.4 + `references/writing-constraints.md` |
| Phase 5 SelfCheck | 本 SKILL §3.5 + `references/selfcheck.md` |
| 工具执行 | `tools/` 目录 Python 脚本 |
| Source Map / SERP Fit | `references/portable/source-map-template.md`、`serp-fit-template.md` |
| 发布前终审 | `references/portable/final-audit.md` |
| 发布后复盘 | `references/portable/post-publish-review.md` |

---

## Reference Index

| 文件 | 内容 | 加载时机 |
|------|------|----------|
| `references/project-config.md` | 完整配置 + G1–G8 + URL 白名单 + 日期策略 | Phase 0R / 4 / 5 |
| `references/article-types.md` | 5 类路由 + H2 模板 + Slug + Frontmatter | Phase 0 / 2 / 3 |
| `references/gates.md` | Gate A/B/0R/C + KEEP/MERGE + 冲突快查 | Phase 0 / 1 / 2 |
| `references/writing-constraints.md` | Voice + 引用分级 + 段落优先协议 + 漏斗 | Phase 4 |
| `references/selfcheck.md` | 12 维 Pass/Fail + H0–H4 Hard Gates + Perfect-Ready | Phase 5 |
| `references/content-graph.md` | 文件表 + 主题簇 + Canonical Registry + 规划队列 | Phase 0 / 0R / 1 / 5 |
| `references/internal-links.md` | 内链规则 + 锚文本标准 | Phase 3 / 3.5 / 5 |
| `references/keywords.md` | P0/P1/P2 关键词 + 禁抢词 | Phase 0 / 0R |
| `references/product-competitors.md` | 产品事实 + 竞品矩阵 + Claims 禁令 | Phase 0R / 4 |
| `references/mini-example.md` | Brief + Outline + Conclusion 示例 | Phase 1 / 3 |
| `references/slug-gate.md` | Slug 6 问 + 12 反模式 | Phase 2 |
| `references/portable/research-triangle.md` | Phase 0R Research 三角流程 | Phase 0R |
| `references/portable/investment-score.md` | 五因子 Investment Score | Phase 0 |
| `references/portable/gates-master.md` | Gate 总表速查 | Phase 0 / 5 |
| `references/portable/extractability-checklist.md` | BLUF + Claim 原子性 + Judgment | Phase 4 / 5 |
| `references/portable/source-map-template.md` | Source Map 模板 | Phase 5 / 6 |
| `references/portable/serp-fit-template.md` | SERP Fit 模板 | Phase 0R |
| `references/portable/outline-cross-check.md` | Phase 3.5 交叉检查模板 | Phase 3.5 |
| `references/portable/perfect-article-checklist.md` | S 级标杆清单 | Phase 5（flagship） |
| `references/portable/final-audit.md` | 发布前终审 | Phase 6 |
| `references/portable/post-publish-review.md` | 发布后复盘 | Phase 6（Brief 参考） |
| `tools/frontmatter_validator.py` | Frontmatter 机器检查 | Phase 5 |
| `tools/word_count_narrative.py` | 字数硬门槛 H3 检查 | Phase 5 |
| `tools/link_checker.py` | P0 G2/G6 链接检查 | Phase 5 |
| `tools/README.md` | 工具使用说明 | Phase 5 |

---

*2mv-blog-article · v1.0.0 · 2026-08-14 · fully self-contained · references/portable/* · tools/* · Mode + Investment Score + Phase 0R + BLUF + Gate Backtracking + G8 夸大禁令*
