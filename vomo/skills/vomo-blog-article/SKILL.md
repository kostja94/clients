---
name: vomo-blog-article
description: >
  Create VOMO blog articles (vomo.ai/guide) from brief to draft. Fully self-contained
  skill folder; Phase 0R and final audit via references/portable/. 8 article types,
  Mode system, Gate A/0R/B/C, 12-dim SelfCheck, tools/ validators.
metadata:
  version: 1.0.0
  project: vomo.ai
  locale: en
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 600
  forbidden-reads:
    - blog/README.md
  allow-extra-reads:
    - vomo/vomo.md
    - vomo/vomo-keywords.md
    - vomo/vomo-features.md
    - vomo/vomo-competitors.md
    - vomo/vomo-site-structure.md
    - vomo/vomo-use-cases.md
    - vomo/vomo-growth-strategy.md
---

# VOMO Blog Article Creation

为 **https://vomo.ai/guide/** 从选题到英文成稿。**硬性规则：Agent 默认只读本 SKILL + `references/`（含 `references/portable/`）。** 禁止读 `blog/README.md`；Phase 0R R1 阶段**允许**读 `vomo/` 下项目文档（`vomo.md`、`vomo-keywords.md` 等，见 frontmatter `allow-extra-reads`）作为项目事实补充。

**本文件夹自包含**：项目配置、G1–G7 + 8 类路由、内容图谱、引用分级、8 Phase 工作流、12 维创作自检均在内联或 `references/` 中。

**渐进式加载**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md`（一次最多 2 个）。读完用完即弃——不跨 Phase 保留 reference 上下文。禁止一次性加载全部 references。

---

## §0 如何使用

### 触发语

```
按 vomo-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Comparison|Alternative|HowTo|PlatformFeature|ResearchGlossary|WorkflowUseCase|Diagnosis|Announcement} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

批量示例：

```
按 vomo-blog-article skill，为 "podcast transcript generator" 补一篇 Comparison（best-podcast-transcription-tools）。
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
| 3 | 成稿 `vomo/blog/NN-{slug}.md`（NN = 本地新建稿序号，从 **01** 起，当前 **01**，见 content-graph） | ✅ | ✅ | ✅ |
| 4 | SelfCheck 表（Hard Gates + 12 维 Pass/Fail） | ✅ | ✅ | ✅ |
| 5 | Source Map | ✅ | ✅ | ✅ |
| 6 | SERP Fit | 简 | ✅ | ✅ |
| 7 | Internal Link Plan | — | ✅ | ✅ |
| 8 | final-audit 审核指令（复制即用） | ✅ | ✅ | ✅ |
| 9 | Post-publish Metric Spec | — | ✅ | ✅ |
| 10 | 提示人类更新 `vomo/blog/README.md` 文章表 | ✅ | ✅ | ✅ |

与用户沟通策略说明可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `vomo-meta-title-description` |
| 已有完整稿，仅需发布前终审 | `references/portable/final-audit.md` |
| Tools 落地页（`/tools/*`、`/use-case/*`） | Tools 楔子规范（见 growth-strategy §3） |
| 非 vomo.ai 博客 | 对应项目的 blog skill |
| 中文站内容 | 另建 ZH skill |

---

## §1 项目配置速查

> **完整配置 + G1–G7 + URL 白名单 → `references/project-config.md`**
> Phase 0R 加载。Phase 4/5 按需重载。

| 配置项 | VOMO 值 |
|--------|-------------|
| **品牌/产品名** | VOMO（VOMO AI） |
| **主域名** | vomo.ai |
| **博客路径前缀** | `/guide/`（非 `/blog/`） |
| **产品定位** | AI 会议笔记与音频转录 — Bot-free（不加入会议） |
| **品类 one-liner** | Record → Transcribe → Smart Notes → Ask AI；Bot-free 录音、双引擎 ASR |
| **核心能力** | AI 转录（Whisper+Nova-2 双引擎）、Smart Notes、Ask AI（GPT-4o）、说话人识别、多格式导出、VOMO CLI |
| **输入方式** | 实时录音、文件上传（MP3/WAV/M4A/MP4 等，最多 10 个）、粘贴 YouTube 链接 |
| **目标用户** | 知识工作者、远程团队、销售、内容创作者、学生/研究者、专业服务人士 |
| **关键指标** | 400K+ 用户、转录 1,000,000+ 小时、95–99% 准确率、90+ 语言、App Store 4.4★ |
| **定价** | Free 30 分钟/周；Pro $1.92/周（≈$8.32/月） |
| **署名默认** | `VOMO Team` |
| **语言** | 英文正文；中文仅沟通用 |
| **禁止内链** | 未上线产品页（G6）；`/notes`（产品区，robots Disallow） |

### G1–G7 阻断速查

| # | 阻断条件 | 说明 |
|---|---------|------|
| G1 | 事实错误 | 产品能力、数据与官网矛盾 |
| G2 | 死链 | 站内或站外链接 404 |
| G3 | 无来源数字 | 量化 claim 无 attribution |
| G4 | 竞品状态错误 | 竞品状态与官网矛盾 |
| G5 | 产品能力夸大 | 定位语言 ≠ 已实现功能 |
| G6 | 内链指向未上线页面 | 只链白名单内路径 |
| G7 | 品牌风险 | 贬低性措辞 |

### 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **节奏** | 博客目标约 10 篇/周（growth-strategy §5） |
| **错开方向** | 从锚点日**往前**排，越重要的文章排越近 |
| **避让已占用日** | 已有文章的日期不重复使用 |

---

## §1B Mode 系统

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Announcement、短帖 | 最小 Research + BLUF；不追求 Excellence |
| **standard** | Alternative / HowTo / PlatformFeature / WorkflowUseCase / Diagnosis | 完整 Research 三角 + Extractability |
| **flagship** | Comparison / ResearchGlossary | 全流程 + Moat + Excellence **必须 Yes** |

默认：用户未指定 → **standard**。ArticleType 路由表指定默认 Mode。

---

## §2 文章类型路由

> **8 类路由表 + H2 模板 + Frontmatter Schema → `references/article-types.md`**
> Phase 0 加载路由表。Phase 3/4 加载模板。

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | 增长职能 | category |
|------|--------|------|:---:|:---:|------|------|
| **Comparison** | best X / top X | 2500–3500 | ≤40% | flagship | EvaluationComparison | ai-transcription |
| **Alternative** | X alternative / vs Y | 2000–2800 | ≤45% | standard | SearchCapture | ai-insights |
| **HowTo** | how to / step-by-step | 1800–2600 | ≤30% | standard | ActivationTutorial | ai-transcription |
| **PlatformFeature** | {platform} transcription（YouTube/Spotify/Apple） | 2000–3000 | ≤35% | standard | SearchCapture | ai-transcription |
| **ResearchGlossary** | what is / meaning | 1800–2800 | ≤20% | flagship | CategoryPOV | ai-transcription |
| **WorkflowUseCase** | 场景工作流（meeting/podcast/lecture） | 1800–2600 | ≤35% | standard | ActivationTutorial | use-cases |
| **Diagnosis** | why not working / fix / 拒审 | 2000–2800 | ≤25% | standard | SearchCapture | ai-insights |
| **Announcement** | 产品发布/更新 | 1200–1800 | 不限 | lite | OpinionNarrative | ai-insights |

**路由**：`best`→Comparison · `alternative`+竞品名→Alternative · `vs`→Alternative · `how to`→HowTo · `{平台} transcript`→PlatformFeature · `what is`→ResearchGlossary · `{场景} workflow`→WorkflowUseCase · `why not`/`fix`→Diagnosis · 新品→Announcement

### 增长职能

| 职能 | 核心目标 | 成功指标（Brief 必填） |
|------|---------|---------------------|
| **CategoryPOV** | 建品类认知 | 被引用/转发、品牌搜索增长 |
| **SearchCapture** | 承接明确搜索需求 | 排名、CTR、低跳出 |
| **EvaluationComparison** | 影响选型 | Demo、注册点击 |
| **ActivationTutorial** | 帮用户上手 | 注册、上手流程完成率 |
| **OpinionNarrative** | 建立品牌人格 | 社区讨论、Newsletter 订阅 |

### 全类型通用模块

| 模块 | 要求 |
|------|------|
| **TL;DR** | 3–5 bullet；独立传达 ~80% 价值；bullet 1 为 snippet 定义句（40–60 词） |
| **H2** | 英文描述性标题；FAQ 不编号 |
| **Conclusion** | `## N. Conclusion` |
| **FAQ** | **固定 6 题**（2026-08-11 定标）；`## FAQ`；**全部内容相关**（基于本文主题，禁止通用模板题）；≥1 题覆盖边界/异议 |
| **CTA** | 单一主行动，分散在正文 ≤2 次 |
| **内链** | blog ≥2 互链 + **≥1 主 Tools/楔子页**（G6 白名单）；product mention 1–2 次 |
| **外链** | 权威 2–6（研究机构/官方统计/权威媒体）；竞品与工具**纯文本提及不链接** |

---

## §3 创作工作流（8 Phase + 5 Gate）

```
Phase 0  ─ Intake & Gate A         (§3.0：Mode + Investment Score + 五必问)
    ↓ PASS
Phase 0R ─ Research 三角 & Gate 0R  (§3.0R：R1→R2→R3→Synthesis；Degraded 可选)
    ↓ PASS / ❌ → §3.G 回溯
Phase 1  ─ Article Brief           (§3.1：SuccessMetric + Moat + AnswerBlocks)
Phase 2  ─ Slug、Date & Gate B     (§3.2)
    ↓ PASS / ❌ → §3.G 回溯
Phase 3  ─ Outline                 (§3.3：Reader mental state + BLUF)
Phase 3.5─ Outline 交叉检查        (§3.3.5：同批 ≥2 篇强制；单篇跳过)
    ↓ PASS / ❌ → §3.G 回溯
Phase 4  ─ Draft                   (§3.4：BLUF 三处 + 按需加载 references)
    ↓
Phase 5  ─ SelfCheck & Gate C      (§3.5：Hard Gates H0–H4 + 12 维 Pass/Fail)
    ↓ PASS / ❌ → §3.G 回溯
Phase 5.5─ Cross-Article Audit     (§3.5.5：同批 ≥2 篇强制)
Phase 6  ─ Delivery                (§3.6：含 tools 脚本 + final-audit 审核指令)
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
## Category: {ai-transcription | ai-insights | use-cases}
## Author: VOMO Team
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

#### 五必问（信息不足时先问用户）

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 目标受众？ |
| 2 | 发布目的（品牌 / SEO / 转化 / 社区）？ |
| 3 | 与已有内容 / 竞品内容的竞争关系（2–3 个竞品 URL）？ |
| 4 | 文中内链指向的页面是否已上线？（G6 预检） |
| 5 | 文章分类（category）？ |

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
R3 — Fetch URL（官方页 + SERP Top 3–5 原文提取）
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
  — 可选：一手产品经验 / 内部数据 / 原创框架/决策树 / 具名 workflow
**AnswerBlocks**（3–5 个可摘录 H2 子问题）:
  1. …
  2. …
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**:
**Primary keyword**:
**Search intent**: Definition | Comparison | Tutorial | Alternative | Commercial
**Category** (frontmatter): ai-transcription | ai-insights | use-cases
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
**Planned internal links** (≥2 blog + ≥1 Tools):
  - /guide/…
  - /tools/…
**Slug candidate**: {kebab-case}
**Author**: VOMO Team（默认）
```

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 + 反模式 → `references/slug-gate.md`**
> **Gate B 细则 → `references/gates.md`**

1. 产出 2–3 slug 候选 + 推荐（对照反模式表 + 大声读测试）
2. **确定 publishDate**：读取 `references/content-graph.md` 已有日期表，从锚点日往前逐日分配，确保每自然日 ≤1 篇（§1 日期策略）
3. **Gate B**：6 项全 Pass → 继续；Fail → 重选 slug

**Slug 硬规则**：常青 kebab-case，**slug 不含年份**（title 可含 `for 2026`）；5–8 词，≤60 字符；**含 primary keyword 完整核心词**（HowTo 类用 `how-to-{action}` 前缀，关键词完整优先、可读性其次）。

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
| 1 | … | AB-1 | … | … | link: /tools/… |
| … | … | … | … | … | … |
| Conclusion | … | — | 准备行动 / 仍有一个顾虑 | 120–180 | CTA |
| FAQ | 6 | — | 具体异议（来自 R2 PAA，保持内容相关） | … | ≥1 objection |
**Estimated total**: N words
```

**结构硬要求**：
- `## TL;DR`（3–5 bullet）
- 编号主节 `## 1.` … `## N.`
- `## N. Conclusion`（无序号）
- `## FAQ`（无序号，H3 每题，**固定 6 题**，全部内容相关）

---

### Phase 3.5 — Outline 交叉检查（Draft 前）

**触发**：同批规划或并行创作 **≥2 篇**（同一 cluster、同一 campaign、或 content-graph 排期相邻）。

**检查项**（详见 `references/portable/outline-cross-check.md`）：
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
> 2. `references/product-competitors.md`（产品事实 + 竞品对照）
> 3. `references/project-config.md`（G1–G7 对照）

#### 4.0 创作原则

**Different, not better**：不是在 Top3 上「写得更全」，而是提供 Top3 没有的决策维度。

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

- **引用**：P0 级数字必须 `[Source: URL]`；P1 级链接或限定词；P2 级标注 "internal observation, n=X"
- **漏斗**：Research 文前 70% 不可见 funnel
- **段落**：≥3 长段（4–8 句）；连续短段 ≤2；段间衔接率 ≥70%；**伪列表 = 自动 Fail**
- **内链**：blog ≥2 + **≥1 主 Tools/楔子页**（见 `references/internal-links.md`）；canonical 概念 1–2 句 + link；外链只链权威来源且已验证存活（`--check-live`）
- **竞品**：每竞品 ≥1 优势；禁 just/merely/only does X
- **模块顺序**：YAML → TL;DR → H2 → Conclusion → FAQ
- **Claim 原子性**：段首 claim · 指代可解析 · chunk 可独立理解
- **Judgment J1–J2**：强判断均 scoped + 同段/前段有依据

---

### Phase 5 — SelfCheck & Gate C

> **完整 12 维 checklist + H0–H4 → `references/selfcheck.md`**
> **完整 Gate 细则 → `references/gates.md`**

#### 工具先跑

在人工 Gate C 检查前，先跑 `tools/` 脚本：

```bash
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{primary kw}"
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {comparison|alternative|howto|platform|research|workflow|diagnosis|announcement}
python tools/link_checker.py ../../blog/NN-{slug}.md --forbidden /notes --check-live
```

#### Hard Gates（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填 |
| **H1** | P0 Gate G1–G7 | 零触发 |
| **H2** | Slug Gate B | Design-Time 六问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | VOMO-Specific | 产品提及比例合规；Bot-free/双引擎/Ask AI/CLI 描述准确 |

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
| 8 | Structure / Links | 模块完整；blog 互链 ≥2 + Tools 主链 ≥1 |
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

1. 写入 `vomo/blog/NN-{slug}.md`
2. 输出 Article Brief 最终版
3. 输出 SelfCheck 表（H0–H4 + 12 维全 Pass）
4. **Source Map**（Claim × Paragraph × Source × Confidence，≥3 行）
5. Internal Link Plan
6. **Signal of Excellence 标注**：
   - `Excellence: Yes — {类型}`（原创框架 / 反直觉数据 / 可执行 checklist / 具名案例 / 洞见）
   - `Excellence: No — 合格但无记忆点`
7. **Moat Asset 兑现检查**：对照 Brief `MoatAssetPlanned`，成稿是否兑现？

**final-audit 审核指令**：

```
请按 vomo-blog-article skill 内 references/portable/final-audit.md 审核 vomo/blog/NN-{slug}.md

项目配置：
- 品牌：VOMO（VOMO AI）
- 主域名：vomo.ai
- 博客前缀：/guide/
- 受众：知识工作者、远程团队、销售、内容创作者、学生/研究者
- 禁止内链：未上线产品页、/notes

要求：
1. 先过 P0 Gate G1–G7
2. 逐维评分（A–J 十维加权 → 100 分）
3. 输出十维评分 + 总分 + 等级（S/A/B/C/D）+ Excellence + Moat + Perfect gap
4. 标记 P1/P2
```

9. **提示人类**更新 `vomo/blog/README.md` 文件表

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

## §4 已有内容图谱

> **→ `references/content-graph.md`**（Phase 0/0R/1/5 按需加载）

线上存量 38 篇（NN = —，见 site-structure §1.2）· 本地新建稿 NN 从 **01** 起（当前 **01**，下一篇 **02**）· 主题簇见 content-graph

---

## §5 Frontmatter 与文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{slug-kebab}.md` |
| NN | 本地新建稿序号，两位递增，从 **01** 起；下一篇 **02** |
| slug | kebab-case；含 primary keyword；常青无年份 |

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

> **日期最佳实践（2026-08-11 采纳）**：`date` = 发布时间，永不改变；`updated` 仅实质性更新时更新。页面只显示一个日期（有 `updated` 显示它）——勿同时显示两个日期。JSON-LD 保留 `datePublished` + `dateModified`；sitemap `lastmod` 与 `updated` 一致。

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

## §7 Reference 文件索引

| 文件 | 内容 | 加载时机 |
|------|------|----------|
| `references/project-config.md` | 完整配置 + G1–G7 + URL 白名单 + 日期策略 | Phase 0R / 4 / 5 |
| `references/article-types.md` | 8 类路由 + H2 模板 + Slug + Frontmatter | Phase 0 / 2 / 3 |
| `references/gates.md` | Gate A/B/0R/C + KEEP/MERGE + 冲突快查 | Phase 0 / 1 / 2 |
| `references/writing-constraints.md` | Voice + 引用分级 + 段落优先协议 + 漏斗 | Phase 4 |
| `references/selfcheck.md` | 12 维 Pass/Fail + H0–H4 Hard Gates + Perfect-Ready | Phase 5 |
| `references/content-graph.md` | 文件表 + 主题簇 + Canonical Registry | Phase 0 / 0R / 1 / 5 |
| `references/internal-links.md` | 内链规则 + 锚文本标准 | Phase 3 / 3.5 / 5 |
| `references/keywords.md` | P0/P1/P2 关键词 + 禁抢词 | Phase 0 / 0R |
| `references/product-competitors.md` | 产品事实 + 竞品矩阵 | Phase 0R / 4 |
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

*vomo-blog-article · v1.0.0 · 2026-08-03 · fully self-contained · references/portable/* · tools/* · 8 article types + Mode + Investment Score + Phase 0R + BLUF + Gate Backtracking*
