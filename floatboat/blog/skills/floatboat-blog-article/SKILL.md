---
name: floatboat-blog-article
description: Create Floatboat blog articles (floatboat.ai/blog) from brief to draft. v4.0 merges SelfCheck into Phase 4/5 inline, removes separate deliverable files (Source Map/OG Image/schema), simplifies Phase 6.
metadata:
  version: 4.0.0
  project: floatboat.ai
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 550
  forbidden-reads:
    - ../floatboat-keywords.md
    - ../floatboat-features.md
---

# Floatboat Blog Article Creation

为 **https://floatboat.ai/blog/** 从选题到英文成稿。**硬性规则：Agent 只读本 SKILL + `references/`（含 `references/portable/`），禁止读 skill 文件夹外文档。**

**渐进式加载**：Agent 默认只读本文件。Phase 需要细节时，按指针读取 `references/{file}.md`（一次最多 2 个）。读完用完即弃——不跨 Phase 保留 reference 上下文。禁止一次性加载全部 references。

**三角色换帽**（同一 Agent 分 Phase 执行，**禁止** Draft 与 Audit 同轮自我放行）：

| Phase | 角色 |
|-------|------|
| 0 | Strategist |
| 0R | Researcher |
| 1–3 | Strategist + SME |
| 4 | Writer + Auditor（Draft 同时做 SelfCheck 内联） |
| 5 | Auditor（最终 Gate 核查） |

---

## §0 如何使用

### 触发语

```
按 floatboat-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Research|Comparison|Ranking|Alternative|Product|Announcement} 文章。
发布目的：{SEO|品牌|转化|社区}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主题 / 主关键词 | ✅ | 决定 intent 与类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 路由表推断 |
| Mode | 可选 | 未指定→**standard**；Announcement 自动 lite，Comparison/CategoryPOV 自动 flagship |
| Topic Scope | 推荐 | scheduling-agent / floatim / combo-skills |
| 系列 / 簇 | 可选 | hub-spoke 定位；默认 Scheduling Agent 簇 |
| 竞品参考 URL | 推荐 | Phase 0R 信息增量判断 |

### 输出（交付物，按 Mode）

| # | 交付物 | lite | standard | flagship |
|---|--------|:----:|:--------:|:--------:|
| 1 | Article Brief（含 SuccessMetric、MoatAssetPlanned、AnswerBlocks） | ✅ | ✅ | ✅ |
| 2 | Research Log（R1–R3 + Synthesis，在对话中输出） | 简 | ✅ | ✅ 完整 |
| 3 | 成稿 `floatboat/blog/NN-{slug}.md`（NN 见 content-graph，当前 **41**） | ✅ | ✅ | ✅ |

**不再产出独立文件**：SelfCheck / Source Map / SERP Fit / OG Image Prompt / Schema JSON — 这些质量检查在 Phase 4/5 内联执行，不再生成单独文件。SelfCheck 结果以表格形式在对话中报告即可。

与用户沟通策略说明可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `floatboat-meta-title-description` |
| 非 floatboat.ai 博客 | 对应项目的 blog skill |
| 中文站 `/zh/` 内容 | 另建 ZH skill |
| HTML→MD 迁移 | 独立脚本 |
| 发布前终审评分 | 已停用 — SelfCheck 在 Phase 4/5 内联执行 |
| Phase 0R Research | `references/portable/research-triangle.md` |

---

## §1 项目配置

> **详细配置 + URL 白名单 + Topic Scope + G1–G7 → `references/project-config.md`**
> Phase 0R 加载。Phase 4/5 按需重载。

**速查**：

| 配置项 | 值 |
|--------|-----|
| 品牌 | Floatboat、FloatIM、Combo Skills、Tacit Engine™、Selfware |
| 域名 | floatboat.ai |
| 博客前缀 | /blog/ |
| 运营主体 | AOE Tech Labs Limited（© 2026） |
| Pillar Hub | `what-is-agentic-calendar` |
| 品类表述 | *The Proactive Agent OS that Runs Work from the Calendar* |
| 受众 | solopreneur / solo founder |
| 署名默认 | `Floatboat`；Research 优先 `Tan Shaoqing` |
| **作者池** | 每次创作时应提问：① Kostja（增长顾问）② Floatboat Team ③ 团队具体成员（如 Tan Shaoqing） |
| 语言 | 英文正文；中文仅沟通用 |
| 禁止内链 | 未上线产品页 |
| **日期错开** | 一天一篇：每自然日最多1篇新文章；不准集中在同一天上线 |

---

## §1B 日期发布策略

> **原则来源**：自然发布节奏，避免站点看起来"同一天突然上线十几篇"。

### 核心规则

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **publishDate 创建后慎重更改** | 首次发布日设定后尽量不改；仅在未上线阶段可调整 |
| **modifiedDate** | 上线后内容实质更新时才修改（非仅 typo 修正）；**≤ 今天**、**≥ publishDate** |
| **错开方向** | 从锚点日（通常为目标上线日）**往前**排，越重要的文章排越近 |
| **避让已占用日** | 已有文章的日期不重复使用 |

### 执行

Phase 2（Slug & Gate B）同时确定日期：对照已有文章日期表，从锚点日往前逐日分配，确保每自然日 ≤1 篇。

### 已有文章日期速查

Agent 在 Phase 2 应读取 `references/content-graph.md` 中已发布文章的日期，避免冲突。

---

## §2 文章类型路由

> **5 类路由表 + H2 模板 + Slug 规则 + Frontmatter → `references/article-types.md`**
> Phase 0 加载路由表。Phase 3/4 加载模板。

### 路由速查

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | 增长职能 |
|------|--------|------|:---:|:---:|------|
| Research / Glossary | 定义/概念 | 2400–3500 | ≤15% | flagship | CategoryPOV |
| Comparison | 双产品 head-to-head | 2800–3500 | ≤40% | flagship | EvaluationComparison |
| Ranking / Listing | 多产品排名清单 | 2400–3200 | ≤40% | flagship | SearchCapture |
| Alternative | 竞品替代 | 2200–3000 | ≤35% | standard | SearchCapture |
| Product / Scenario | 场景/workflow | 2000–2700 | ≤50% | standard | ActivationTutorial |
| Product Announcement | 产品发布 | 1500–2000 | 不限 | lite | OpinionNarrative |

**路由**：`best`/`top`+≥3竞品→**Ranking** · `vs`/双产品→Comparison · `alternative`+单竞品→Alternative · `what is`→Research · pipeline→Product · 新品→Announcement

> **Ranking vs Comparison**：多竞品「best X alternatives」用 **Ranking / Listing**（编号 H3 + `articleFormat: Ranking`），不是 Comparison 的 head-to-head 模板。详见 `references/article-types.md` §4B。**勿**再生成 ItemList JSON-LD 文件。

### 增长职能（来自 Strategy Layer）

| 职能 | 核心目标 | 成功指标（Brief 必填） |
|------|---------|---------------------|
| **CategoryPOV** | 建品类认知 | 被引用/转发、品牌搜索增长 |
| **SearchCapture** | 承接明确搜索需求 | 排名、CTR、低跳出 |
| **EvaluationComparison** | 影响选型 | Demo、GitHub、Docs 点击 |
| **ActivationTutorial** | 帮用户上手 | 命令执行、注册、文档路径点击 |
| **OpinionNarrative** | 建立品牌人格 | 社区讨论、Newsletter 订阅 |

Phase 0 输出 `ArticleType` + 增长职能；Brief 填写 `SuccessMetric`（可量化）。

---

## §3 创作工作流（8 Phase + 4 Gate）

```
Phase 0 — Intake & Gate A         §3.0（Mode + Investment Score + 六必问）
    ↓ PASS
Phase 0R — Research 三角 & Gate 0R  §3.0R（R1→R2→R3→Synthesis；Degraded 可选）
    ↓ PASS / ❌ → §3.G 回溯
Phase 1 — Article Brief           §3.1（SuccessMetric + Moat + AnswerBlocks）
Phase 2 — Slug & Gate B           §3.2
    ↓ PASS / ❌ → §3.G 回溯
Phase 3 — Outline                 §3.3（含 Reader mental state + BLUF 占位 + 内链规划）
Phase 3.5 — Outline 交叉检查      §3.3.5（同批 ≥2 篇强制；单篇跳过）
    ↓ PASS / ❌ → §3.G 回溯
Phase 4 — Draft + 内联 SelfCheck  §3.4（BLUF 三处 + Hard Gates + 12 维，对话中报告）
    ↓ PASS / ❌ → §3.G 回溯
Phase 5 — Gate C & Cross-Article  §3.5（最终核查 + Cross-Article Audit，同批 ≥2 篇）
    ↓ PASS / ❌ → §3.G 回溯
Phase 6 — Write File              §3.6（写入文件 + 提示人类更新 README）
```

---

### Phase 0 — Intake & Gate A

> **详细 Gate → `references/gates.md`**（首次加载）
> **Investment Score 细则 → `references/portable/investment-score.md`**

**Phase 0 第一行强制输出**：

```
## Mode: lite | standard | flagship
## ArticleType: CategoryPOV | SearchCapture | EvaluationComparison | ActivationTutorial | OpinionNarrative
## InvestmentScore: {1.0–5.0 均分} — {五因子摘要}
## Topic Scope: scheduling-agent | floatim | combo-skills
## Category: {Research | Comparison | Product | Reference}
## Author: {Kostja | Floatboat Team | {specific name}}
## Gate A: KEEP | MERGE → {target slug} | STOP
```

### 三模式（Mode）

| Mode | 适用 | Phase 深度 |
|------|------|-----------|
| **lite** | Announcement、短帖、低风险文 | 最小 Research + BLUF；不追求 Excellence |
| **standard** | 常规 SEO 文、Product/Scenario、Alternative | 完整 Research 三角 + Extractability |
| **flagship** | pillar、Research/Glossary、Comparison、CategoryPOV | 全流程 + Moat + Excellence **必须 Yes** |

默认：用户未指定 → **standard**。ArticleType 路由表指定默认 Mode。

### Investment Score（选题投资分）

五因子各 1–5，取**算术平均**：

| 因子 | 1 分 | 5 分 |
|------|------|------|
| 搜索需求 | 几乎无搜索量 | 稳定或上升 |
| 商业相关性 | 与 ICP/产品路径无关 | 靠近购买或使用路径 |
| 差异化能力 | 只能复述 SERP | 有 Moat / Proof 可引用 |
| 证据可得性 | 无法验证强 claim | Proof Library 或 R3 可支撑 |
| 内容生命周期 | <3 月过时 | 2+ 年常青 |

| 均分 | 动作 |
|------|------|
| **≥4.0** | KEEP，按声明 Mode 执行 |
| **3.0–3.9** | KEEP 但**降级 Mode** 或改角度 |
| **<3.0** | MERGE / STOP / 降级为 FAQ·短帖 |

### 六必问（信息不足时先问用户）

| # | 问题 |
|---|------|
| 1 | 目标 SEO 关键词 + 目标受众？ |
| 2 | 发布目的（品牌 / SEO / 转化 / 社区 / 招聘）？ |
| 3 | 与已有内容 / 竞品内容的竞争关系（2–3 个竞品 URL）？ |
| 4 | 文中内链指向的页面是否已上线？ |
| 5 | **文章署名作者**：① Kostja（增长顾问）② Floatboat Team ③ 团队具体成员（如 Tan Shaoqing）？ |
| 6 | **文章分类（category）**：Research / Comparison / Product / Reference？Agent 应参考已有文章分类给出建议（见下表），再请用户确认。 |

### 已有文章分类速查

> 以下表列出本地有稿件的文章及其集群归属，新文章分类应与所在集群一致。完整线上清单（87篇）在项目文档中维护，不在本 skill 内。

| slug | category | 集群 |
|------|----------|------|
| `introducing-floatim` | Product | FloatIM / 产品公告 |
| `ai-scheduling-agent` | Research | Scheduling Agent |
| `what-is-agentic-calendar` | Research | Scheduling Agent |
| `calendar-driven-ai-vs-chat-ai` | Research | Scheduling Agent |
| `best-ai-scheduling-assistants` | Comparison | Scheduling Agent |
| `ai-meeting-preparation` | Product | Scheduling Agent |
| `ai-follow-up-automation` | Product | Scheduling Agent |
| `what-is-claude-cowork` | Research | Claude Cowork / Hub |
| `best-claude-cowork-alternatives` | Ranking | Claude Cowork |
| `what-is-claude-tag` | Research | Claude Tag / FloatIM |
| `best-claude-tag-alternatives` | Ranking | Claude Tag / FloatIM |
| `world-cup-2026-guide` | Research | World Cup 2026 |
| `world-cup-2026-schedule` | Reference | World Cup 2026 |
| `world-cup-2026-google-calendar-ics` | Product | World Cup 2026 |
| `floatcup-world-cup-2026-calendar-subscribe` | Product | World Cup 2026 |
| `world-cup-2026-schedule-usa` | Reference | World Cup 2026 |
| `what-is-deepseek-agent` | Research | DeepSeek Agent / Hub |
| `how-to-build-deepseek-agent` | Product | DeepSeek Agent |
| `deepseek-agent-function-calling` | Product | DeepSeek Agent |
| `deepseek-agent-vs-claude-code` | Comparison | DeepSeek vs Claude Code |
| `what-is-deepseek-harness` | Research | DeepSeek Harness / Hub |
| `deepseek-v4-pro-0813` | Research | DeepSeek V4 Pro / GA |
| `cordis-plugin-framework` | Research | Cordis / DeepSeek Harness 内核 |
| `grok-4-6` | Research | Grok / xAI Model |
| `grok-bot` | Research | Grok Bot / xAI Agent |
| `what-is-minimax-h3` | Research | MiniMax / Model |

### 集群 → 分类映射

Agent 判断新文章归属集群后，按以下映射推荐分类：

| 集群 | 默认 category | 说明 |
|------|:---:|------|
| Scheduling Agent / Agentic Calendar | Research | 品类定义与教育内容 |
| World Cup 2026 | Reference / Product | 参考/数据页用 Reference，工具/操作指南用 Product |
| DeepSeek Agent / Harness / V4 | Research / Product | 品类定义用 Research，教程/实操用 Product |
| Cordis / 插件内核 | Research | 技术机制与范式拆解 |
| Grok / xAI Model | Research | 模型发布与能力评估 |
| Grok Bot / xAI Agent | Research | agent 产品与安全模型评估 |
| FloatIM / 产品公告 | Product | 产品发布与功能介绍 |
| AI Agent 基础 | Research | 概念定义与品类教育 |
| AI Tools / Platform | Comparison | 工具选型与平台对比 |
| Solo Operator | Product | 实操指南与工作流 |
| Calendar / Productivity | Comparison | 日历对比与效率工具 |
| Browser / Workspace Agent | Research | 品类定义与对比 |
| Model / API | Product | 模型接入实践 |
| Comparison / Alternative | Comparison | 横向对比 |
| Reviews | Comparison | 产品评测 |
| HTML / Markdown | Research | 输出格式对比 |
| Other | 按实际内容判断 | 如 `feishu-cli-solo-work-setup` → Product |

**分类建议逻辑**：Agent 先根据文章类型路由推断集群归属，再按上表映射 category，输出建议 + 理由，等待用户通过第六必问确认。

用户只给 topic 时：Agent 自行 R2 SERP Top3；竞品 URL 缺失 → Log 标注 `competitor:TBD`；必问无法推断 → **AskUserQuestion**。

### KEEP / MERGE 判定

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

**Degraded 模式**：当 R2/R3 信息缺失时标注 `Research mode: Degraded — {reason}`。Degraded 下正文**不得**写 P0 级未验证 claim。竞品 URL 缺失 → Draft 前必须补 R3。

**Gate 0R 阻断**：R2 未搜 / R3 未 Fetch / 无 Synthesis / 事实不可验证且需写 P0 claim → ❌ 回退补 R2/R3 或 STOP。

---

### Phase 1 — Article Brief

输出 Brief，参照 `references/mini-example.md`。**必含以下新增字段**：

```markdown
## Article Brief

**Mode**: lite | standard | flagship
**ArticleType**: CategoryPOV | SearchCapture | EvaluationComparison | ActivationTutorial | OpinionNarrative
**InvestmentScore**: {1.0–5.0}
**SuccessMetric**: {可量化，来自 §2 增长职能表}
**MoatAssetPlanned**: {类型，standard/flagship 必填}
  — 可选：一手产品经验 / 内部 benchmark / 真实失败案例 / 原创框架/决策树 / 具名 workflow / SME 具体判断
**ProofLibraryRefs**: [PFL-xxx, …]
**AnswerBlocks**（3–5 个可摘录 H2 子问题）:
  1. …
  2. …
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**:
**Primary keyword**:
**Search intent**: Definition | Comparison | Tutorial | Alternative | Commercial
**Category** (frontmatter): Research | Comparison | Product | Reference — 由 Phase 0 第六问确认
**Reader stage**: Awareness | Consideration | Evaluation | Activation
**Publish goal**: SEO | Brand | Conversion | Community
**Target audience**:
**Synthesis Statement**（来自 Phase 0R，粘贴或摘要）:
**One-line thesis**:
**Differentiation angle**（vs SERP top 3–5）:
**Information increment** (≥2 项，每条对应 Log + Synthesis):
  - [ ] …
  - [ ] …
**Candidate examples** (from Log):
**Word count target**: {见 §2 类型词数}
**Topic Scope / Cluster**: {hub-spoke 角色}
**Pillar link** (Spoke 必填): /blog/{hub-slug}
**Planned internal links** (≥2 blog):
**Slug candidate**: {kebab-case}
**Author**: {Kostja | Floatboat Team | {specific team member}} — 由 Phase 0 确认
```

---

### Phase 2 — Slug、Date & Gate B

> **Slug 规则 → `references/article-types.md` §9**
> **Gate B 细则 → `references/gates.md` §5**

1. 产出 2–3 slug 候选 + 推荐（对照反模式表 + 大声读测试）
2. **确定 publishDate**：读取 `references/content-graph.md` 已有日期表，从锚点日往前逐日分配，确保每自然日 ≤1 篇（§1B 日期策略）
3. **Gate B**：6 项全 Pass → 继续；Fail → 重选 slug

---

### Phase 3 — Outline + SERP Fit + Frontmatter

1. 用 `references/article-types.md` 对应 H2 模板，每节标注目标词数、**段落目标（≥N 长段 / 禁伪列表）**、内链占位、snippet 定义句位置、canonical 引用计划、**Reader mental state**（该节前读者的具体心理状态，如「怀疑：这类工具真的能在生产环境用吗？」而非空泛「Interested」）
2. title + description + 完整 frontmatter YAML
3. SERP Fit mini-audit（对话中报告）

**Outline 输出格式**：

```markdown
## Outline — {slug}

| § | H2 | Answer block ID | Reader mental state | Target words | Links / Notes |
|---|-----|-----------------|---------------------|-------------|---------------|
| TL;DR | … | AB-0 | 刚搜进来：找对地方了吗？ | 80–120 | 3-5 bullet；bullet 1 = snippet 定义句 |
| 1 | … | AB-1 | … | … | link: … |
| … | … | … | … | … |
| Conclusion | … | — | 准备行动 / 仍有一个顾虑 | 120–180 | CTA |
| FAQ | 6 | — | 具体异议（来自 R2 PAA，保持内容相关） | … | ≥1 objection |
**Estimated total**: N words
```

---

### Phase 3.5 — Outline 交叉检查（Draft 前）

**触发**：同批规划或并行创作 **≥2 篇**（同一 cluster、同一 campaign、或 content-graph 排期相邻）。

**目的**：在只有 H2 骨架时拦截跨篇重复——比 Phase 5.5 全文审计便宜一个数量级。**不替代** Phase 5.5。

**步骤**（5–10 分钟）：

1. 并排放置各篇 Outline 的 H2 列 + Reader mental state 列
2. 检查：
   - [ ] H2 标题重复度：同 cluster 内是否有 ≥2 篇同一 H2 措辞？
   - [ ] 叙事弧相似：是否都是「定义→列表→对比→FAQ→CTA」且无角度差异？
   - [ ] Canonical 越界：非 canon 文 Outline 是否计划展开 hub 才该全量写的概念？
   - [ ] Synthesis 冲突：两篇 One-line thesis 是否互相重叠 >50%？
   - [ ] **内链缺口**：对照 `references/internal-links.md` §三 集群矩阵，新文章是否满足 R1（≥2 出链）+ R2（≥1 入链）+ R6（hub-spoke 双向）？
3. **Fail** → 改 Outline / 改 Synthesis / MERGE 建议 / 补内链规划 → 重过 3.5
4. **Pass** → 输出 `Outline cross-check: PASS — {slugs}` → Phase 4

单篇创作：跳过 3.5，标注 `N/A — single article`。

---

### Phase 4 — Draft + 内联 SelfCheck

> **加载顺序**（每次 ≤2 文件）：
> 1. `references/writing-constraints.md`（Voice + 引用分级 + 漏斗透明度 + **§4 段落优先协议**）
> 2. `references/product-competitors.md`（产品事实 + 竞品对照）
> 3. `references/project-config.md`（G1–G7 对照）

#### 4.0 创作原则（Draft 前必读）

**Different, not better**：不是比 Top3「写得更全」，而是提供 Top3 没有的决策维度。对照 Research Log 的 Synthesis one-line thesis。

#### 4.0B BLUF 三处（Bottom-Line Up Front）

| # | 位置 | 要求 |
|---|------|------|
| **B1** | TL;DR 下 | 40–60 词直接回答 primary keyword |
| **B2** | 每个 major H2 首段 | 先答后铺背景 |
| **B3** | FAQ 每问 | 首句即答，再展开；**不得**从正文复制粘贴 |

**执行顺序**：写完 TL;DR 后立刻对照 B1；每写完一个 H2 section 立刻对照 B2；FAQ 整体写完后对照 B3。

#### 4.1 段落优先起草协议

1. **先写 prose，后加结构** — 每个 H2 section 第一稿必须是连续段落；表格/列表/步骤追加
2. **禁伪列表** — 不得用 `**Bold label.**` + 单句 × N 替代列表
3. **起草后即时计数** — 全文完成后数长段落（≥4 句）数量；若 <3 → 合并短段重写

#### 4.2 Degraded 模式意识

Phase 0R 标注 `Degraded` 时：正文无 P0 级未验证 claim；每个基于推理的断言须用限定词（"likely""emerging""in our deployment"）；不确定事实标 `[internal observation]`。

#### 4.3 核心约束速查

- **引用**：P0 级数字必须 `[Source: URL]`；P1 级链接或限定词；P2 级标注 "internal observation, n=X"
- **漏斗**：Research 文前 70% 不可见 funnel
- **段落**：≥3 长段（4–8 句）；连续短段 ≤2；段间衔接率 ≥70%；**伪列表 = 自动 Fail**
- **内链**：blog ≥2；canonical 概念 1–2 句 + link；外链 rel="nofollow noopener"
- **竞品**：每竞品 ≥1 优势；禁 just/merely/only does X
- **模块顺序**：YAML → TL;DR → H2 → Conclusion → FAQ
- **Claim 原子性**：段首 claim · 指代可解析 · chunk 可独立理解
- **Judgment J1–J2**：强判断均 scoped（含范围/立场标记）+ 同段/前段有依据

#### 4.4 内联 SelfCheck（Draft 完成后立即执行，对话中报告）

##### Hard Gates（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research / Gate 0R | Research Log 完整；Synthesis + SERP Fit 已填；R3 官方 ≥1 + Top3 已 Fetch（或 Degraded 已标注且无未验证 P0 claim） |
| **H1** | P0 Gate G1–G7 | 零触发（事实错误 / 死链 / 无来源量化 claim / 竞品状态错误 / 产品能力夸大 / 内链指向未上线页 / 品牌法律风险） |
| **H2** | Slug Gate B | Design-Time 六问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | 特定项目检查 | 产品提及比例合规；品牌措辞正确 |

##### 12 维速查

| # | 维度 | Pass 条件摘要 |
|---|------|-------------|
| 1 | Publishability | H0–H4 全 Pass |
| 2 | Fact / E-E-A-T | 可验证 claim 有来源 |
| 3 | Differentiation | 正文**兑现** Synthesis；Moat 已交货 |
| 4 | Depth / Density | 无空壳 section ≥3 处；FAQ 独立于正文 |
| 5 | Presentation | 长段 ≥3；列表占比合规；衔接率 ≥70%；Claim 原子性 Pass |
| 6 | Writing / Voice | Voice 5 项 + 空泛句阈值 + 禁词扫描 Pass；Judgment J1–J2 Pass |
| 7 | Objectivity | 产品占比合规；竞品无贬低 |
| 8 | Structure / Links | 模块顺序正确；内链 ≥2 blog；canonical 1-2 句+link |
| 9 | SEO / SERP | Frontmatter F1–F8；snippet-ready 定义；**BLUF 三处** Pass；desc ≤160c |
| 10 | Conversion | CTA ≤2；匹配读者阶段 |
| 11 | Slug / Meta | title <60c / desc <160c |
| 12 | Cross-Article | 同 cluster 无矛盾/重复（单篇 N/A） |

**SelfCheck 报告格式**（对话中输出，不存文件）：

```
## SelfCheck — {slug}
### Hard Gates: H0 ✅ | H1 ✅ | H2 ✅ | H3 ✅ (~N words) | H4 ✅
### 12 维: 全 Pass ✅（或标注 Fail 项 + 修复动作）
### Gate C: PASS → 进入 Phase 5
```

##### Excellence 标注（flagship 专用，对话中报告）

- `Excellence: Yes — {类型}`（原创框架 / 反直觉数据 / 高可执行 checklist / 具名案例 / 洞见）
- `Excellence: No — 合格但无记忆点`
- No 不 Fail——仅 S 级要求 Yes

---

### Phase 5 — Gate C 终审 & Cross-Article Audit

Draft + 内联 SelfCheck 完成后，最终核查：

1. **Gate C**：H0–H4 + 12 维全 Pass → 可写入文件；任一 Fail → 按 §3.G 回溯
2. **Cross-Article Audit**（同批 ≥2 篇触发）：

| 检查点 | 方法 |
|--------|------|
| 叙事模式雷同 | 多篇是否共享相同叙事弧？3+ 篇 → 标记 |
| 内容网络完整性 | 互链是否双向？ |
| 核心概念跨篇重复 | 每概念只一篇 canonical |
| Intro / Conclusion 模板化 | 多篇是否可互换首段？ |

Fail → 改文或标注差异原因。单篇 → 标注 `N/A`。

---

### Phase 6 — Write File

1. 写入 `floatboat/blog/NN-{slug}.md`
2. 对话中报告最终状态：Mode / ArticleType / 字数 / Gate C / Excellence / Moat
3. 提示人类更新 `blog/README.md` 文件表
4. **禁止**生成：`blog/schema/*.json`（JSON-LD）/ `blog/images/` / Source Map 文件 / SERP Fit 文件 / OG Image Prompt 文件

---

### §3.G — Gate 失败回溯表

创作非严格线性。Gate 失败后按下表回退。

| Gate / 结果 | 回退至 | 典型原因 | 修复后 |
|-------------|--------|---------|--------|
| **Gate A → STOP** | 流程结束 | 增量不足、MERGE 建议、必问未确认 | 改选题或合并后重新 Phase 0 |
| **Gate A → MERGE** | 流程结束 | 搜索意图重叠、深度不可独立 | 执行合并清单，不写新稿 |
| **Gate 0R ❌** | **Phase 0R** | SERP 未搜、Top3 未 Fetch、无 Synthesis | 补 R2/R3 → 更新 Log → 重过 Gate 0R |
| **Gate 3.5 ❌** | **Phase 3** | 同批 Outline H2/叙事/Synthesis 重叠 | 改角度或 MERGE |
| **Gate B ❌** | **Phase 2** | Slug 反模式、关键词不对齐 | 新 slug → 重过 Gate B |
| **Phase 4 SelfCheck ❌** | **Phase 4** | 写作/事实/结构 Fail | 改稿 → 重跑 SelfCheck |
| **Gate C ❌** | **Phase 4 或 5** | Cross-Article 冲突或终审 Fail | 改文或标注差异 |

---

## §4 已有内容图谱

> **→ `references/content-graph.md`**（Phase 0R/1/5 按需加载）

8 篇文章 · 下一序号 **09** · Hub: `what-is-agentic-calendar`

---

## §5 关键词速查

> **→ `references/keywords.md`**（Phase 0/0R 按需加载）

P0：Proactive AI Agent · Calendar-Driven AI · Agentic Calendar · Claude Cowork alternative
P1：AI scheduling · meeting prep · follow-up · Combo Skills
P2：Manus/Accomplish/Slock alternative

---

## §6 产品与竞品事实边界

> **→ `references/product-competitors.md`**（Phase 0R/4 按需加载）

Floatboat 四步机制 · Calendar-Driven vs Chat-Based · 竞品速览 · AI Scheduling 四代框架 · 合规红线

---

## §7 文件命名与 README 同步

- 文件名：`NN-{slug-kebab}.md`，NN 两位递增（当前 **09**）
- slug 与 frontmatter 一致；常青；无禁词
- 图片：2026-08-11 起 frontmatter 不再含 `image` 字段（图片由 CMS/OG 单独管理）
- 成稿后提示人类更新 `blog/README.md`

---

## §8 本 skill 内文档分工

| 阶段 | 文档 |
|------|------|
| 选题前 Strategy | 本 Skill §2（增长职能、Mode 默认） |
| Phase 0 Intake + Investment | 本 Skill §3.0 + `references/gates.md` |
| Phase 0R Research | `references/portable/research-triangle.md` |
| Phase 1 Brief | 本 Skill §3.1 + `references/mini-example.md` |
| Phase 2–3 Slug + Outline | 本 Skill §3.2–3.3 + `references/article-types.md` |
| Phase 3.5 交叉检查 | `references/internal-links.md`（集群矩阵 + Phase 3.5 规划） |
| Phase 4 Draft + SelfCheck | 本 Skill §3.4（含内联 SelfCheck 表） + `references/writing-constraints.md` |
| Phase 5 Gate C + Cross-Article | 本 Skill §3.5 |
| Phase 6 Write File | 本 Skill §3.6 |

**已停用 / 不再引用**：
- `references/selfcheck.md`：SelfCheck 逻辑已合并到本 Skill §3.4
- `references/portable/source-map-template.md`：Source Map 不再单独生成
- `references/portable/serp-fit-template.md`：SERP Fit 在 Phase 0R 对话中输出
- `references/floatboat-og-image-prompts.md`：OG Image 不再由 skill 生成
- `references/portable/final-audit.md`：终审已合并到 Phase 4/5 内联
- `tools/` Python 脚本：废弃，Machine check 改为 Agent 内联执行

---

## §9 配套文档 + Mini Example

> **Brief/Outline 示例 + Conclusion 多样结尾 → `references/mini-example.md`**（Phase 1/3 按需加载）

---

## Reference Index

| 文件 | 内容 | 加载时机 |
|------|------|----------|
| `references/project-config.md` | 配置 + G1–G7 + URL 白名单 + Topic Scope | Phase 0R / 4 |
| `references/article-types.md` | 5 类路由 + H2 模板 + Slug + Frontmatter | Phase 0 / 2 / 3 |
| `references/gates.md` | Gate A/B + KEEP/MERGE + 信息增量 + 冲突快查 | Phase 0 / 1 / 2 |
| `references/writing-constraints.md` | Voice + 引用分级 + 漏斗 + 碎片化 + 内链 + 段落优先协议 | Phase 3 / 4 |
| `references/content-graph.md` | 文件表 + Hub-Spoke + Canonical Registry | Phase 0R / 1 |
| `references/internal-links.md` | 内链规则 R1-R7 + 锚文本标准 + 集群矩阵 + Phase 3.5 规划 | Phase 3 / 3.5 |
| `references/keywords.md` | P0/P1/P2 关键词 + FloatIM 词表 | Phase 0 / 0R |
| `references/product-competitors.md` | 产品事实 + 四步机制 + 竞品 + 四代框架 | Phase 0R / 4 |
| `references/mini-example.md` | Brief + Outline + Conclusion 示例 | Phase 1 / 3 |
| `references/floatboat-blog-schema.md` | **归档**：原 JSON-LD 规则；**禁止**加载 | 勿加载 |
| `references/portable/research-triangle.md` | Phase 0R Research 三角流程 | Phase 0R |
| `references/portable/investment-score.md` | 五因子 Investment Score 详解 | Phase 0 |
| `references/portable/extractability-checklist.md` | BLUF + Claim 原子性 + Judgment 速查 | Phase 4 |
| `references/portable/outline-cross-check.md` | Phase 3.5 交叉检查模板 | Phase 3.5 |
| `references/portable/post-publish-review.md` | 发布后 7/30/90/180 天复盘 | Phase 6（交付时参考） |
| `references/portable/retro-audit.md` | 已发布稿回溯审计 | 独立场景 |

**以下文件已停用，不在 v4.0 加载路径中**：
- `references/selfcheck.md` — 逻辑已合并到 SKILL.md §3.4
- `references/portable/source-map-template.md` — Source Map 不再生成
- `references/portable/serp-fit-template.md` — SERP Fit 在对话中输出
- `references/portable/final-audit.md` — 终审已合并到 Phase 4/5
- `references/portable/gates-master.md` — 逻辑已合并
- `references/portable/perfect-article-checklist.md` — 逻辑已合并
- `references/floatboat-og-image-prompts.md` — OG Image 不再由 skill 生成
- `tools/` — 废弃

---

*floatboat-blog-article · v4.0.0 · 2026-07-31 · SelfCheck 内联 · 交付物简化 · 文件不再生成
