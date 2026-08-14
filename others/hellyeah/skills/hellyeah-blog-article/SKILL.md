---
name: hellyeah-blog-article
description: >
  Load when user asks to create, draft, or outline a Hellyeah blog article
  for hellyeahai.com/blog — GEO, experimentation, agentic growth, AI ads
  education, platform explainers, alternatives, compliance, etc.
  Do NOT load for title/description-only tasks (future hellyeah-meta-title-description).
metadata:
  version: 2.0.0
  project: hellyeahai.com
  locale: en
  market: B2B enterprise growth (US/global)
  load-rule: progressive-disclosure
  max-primary-lines: 500
  self-contained: true
  forbidden-reads:
    - hellyeah.md
    - hellyeah-*.md
    - ../../blog/README.md
---

# Hellyeah Blog Article Creation

为 **https://www.hellyeahai.com/blog/** 从选题到英文成稿。**范围**：仅英文 `/blog/{slug}`。

**硬性规则**：Agent 执行本 skill 时只读本文件夹内文件，禁止读取仓库内 `hellyeah.md`、`hellyeah-*.md` 或其他外部文档。

---

## 渐进式加载规则（硬性）

```
Agent 默认只读本文件。
Phase 需要细节时，按指针读取 references/{file}.md（一次最多 2 个）。
禁止一次性加载全部 references。
读完用完即弃——不跨 Phase 保留 reference 上下文。
```

---

## §0 如何使用

### 触发语

```
按 hellyeah-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Pillar|Framework|CommercialEducational|PlatformExplainer|Alternative|UseCase|Diagnosis|Compliance} 文章。
发布目的：{SEO|品牌|Demo|AIMA Free}。目标读者：{描述}。
```

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| 仅优化已有文章的 title/description | 未来 `hellyeah-meta-title-description` 或手动 |
| 非 hellyeahai.com 博客 | 通用 blog skill |
| 非英文内容 | 另建 ZH skill |
| Capability / 平台落地页正文 | 站点页面模板，非 blog skill |

### 输出（Phase 6 交付物）

1. **Article Brief**（Markdown 摘要）
2. **完整稿** `hellyeah/blog/NN-{slug}.md`（NN 见 `references/content-graph.md`，当前 **02** 起新稿；**01 已占用**）
3. **SelfCheck 表**（12 维加权 + 2 Gate Check + Hard Gates）
4. **Source Map**（内部，不发布）
5. **SERP Fit 审计表**（Phase 0 输出，Phase 5 复核）
6. **提示人类**更新 `hellyeah/blog/README.md`

与用户沟通可用中文；**正文必须为英文**。

---

## §1 项目配置与 Gate 清单

> **完整配置 + G1–G7 → `references/project-config.md`**
> **P1–P5 Proof Gate → `references/proof-gate.md`**

**Phase 0 / Phase 5 前加载 project-config + proof-gate。**

| Gate | 项数 | 阻断条件 |
|------|:---:|------|
| **G1–G7** | 7 | 事实错误 / 死链 / 无来源数字 / 竞品状态错误 / 产品夸大 / 内链未上线 / 品牌风险 |
| **P1–P5** | 5 | 案例无溯源 / SOC2 误写 / Déjà Vu GA / agentic 夸大 / GEO 未链 canonical |

G1–G7 + P1–P5 全部 Pass 方可交付。

---

## §2 文章类型路由

> **8 类路由表 + H2 模板 + Voice → `references/article-types.md`**
> **CTA 分层 → `references/platform-routing.md`**

**Phase 0 / Phase 3 前加载。** 速查：

| 类型 | 词数 | 产品提及上限 | 路由示例 |
|------|------|-------------|---------|
| Pillar | 3500–5000 | ≤20% | programmatic GEO |
| Framework | 2500–3200 | ≤25% | continuous growth experiments |
| CommercialEducational | 2800–3800 | ≤30% | AI ads manager |
| PlatformExplainer | 2200–3000 | ≤35% | AIMA vs Forge |
| Alternative | 2500–3500 | ≤30% | vs agency |
| UseCase | 2200–3000 | ≤30% | growth for mobile apps |
| Diagnosis | 2500–3200 | ≤25% | ROAS decline |
| Compliance | 2000–2800 | ≤20% | SOC 2 marketing platform |

**GEO 话题**：任何类型须 P5 链 `/capabilities/seo-geo`。

---

## §3 创作工作流（8 Phase + 3 Gate）

### 流程总览

```
Phase 0 — Intake & Gate A ─── 不通过 → STOP
Phase 1 — Article Brief
Phase 2 — Slug Design & Gate B ─── 不通过 → 重选 slug
Phase 3 — Outline
Phase 4 — Draft
Phase 5 — SelfCheck & Gate C ─── 不通过 → 修复
Phase 5.5 — Cross-Article Audit ─── 批量创作时触发
Phase 6 — Delivery
```

---

### Phase 0 — Intake & Gate A

#### 0.0 话题范围判定

Agent 第一行输出 `## Topic Scope: {scope}`（如 GEO / AI ads / experimentation / compliance / platform OS）。

#### 0.1 SERP Fit 审计

> **完整模板 → `references/serp-audit.md` §1**

必须输出：Top 5 分析表 + Common Coverage Gaps + Our Unique Contribution（≥2 项）+ Snippet-Ready Definition（40–60 词）。识别竞争强度等级（低/中/高）。

#### 0.2 KEEP/MERGE + 信息增量

对照 `references/content-graph.md` §4.5：

- KEEP：3 条件满足 ≥2（意图独立 / 读者阶段不同 / 深度不可压缩）
- 信息增量：相对 SERP Top 3 至少 **2 项**独有（框架 / 决策表 / 方法论观察 / 新边界 / 原创对比维度）→ 否则 **STOP**
- **信息增量结构化方法**：逐段标记冗余度——"这段读者可在竞品中找到等效内容吗？" 若冗余段 >60% → 增量不足

#### 0.3 五必问

| # | 问题 |
|---|------|
| 1 | 主关键词 + search intent？ |
| 2 | 发布目的？SEO / 品牌 / Demo / AIMA Free |
| 3 | 目标读者 persona？ |
| 4 | 应链哪条平台/能力线？ |
| 5 | 相对 SERP / capability 页的信息增量？ |

#### 0.4 Gate A 额外项

- GEO 话题 → 声明 canonical `/capabilities/seo-geo`
- Blog 未上线 → frontmatter `status: draft`
- Déjà Vu 话题 → 声明 private alpha（P3）
- 竞争强度高（Top 5 ≥4 高 DA）→ 差异化角度须在标题和首段可见

---

### Phase 1 — Article Brief

> **模板 → `references/article-types.md` §2.11 · 范例 → `references/mini-example.md`**

---

### Phase 2 — Slug Design & Gate B

> **7 原则 + 12 反模式 + 6 问 → `references/slug-gate.md`**

Gate B：6 问全 Pass + 0 反模式 → 定 slug。禁止 Flag 过关。

---

### Phase 3 — Outline

按 `references/article-types.md` 对应类型 H2 模板展开。标注：词数、关键词、内链、Hellyeah 出现计划、**Who/How/Why 段落计划**（Pillar/Framework 强制）。

---

### Phase 4 — Draft

> **Voice → `references/article-types.md` §8**
> **EEAT 信号 → `references/eeat-framework.md`** ⭐NEW
> **引用 → `references/citations.md`**
> **表现节奏 → `references/presentation-rhythm.md`** ⭐NEW（替代旧 `presentation.md`）
> **内链 → `references/platform-routing.md`**

**Phase 4 加载顺序**：article-types + eeat-framework → citations + presentation-rhythm → platform-routing（分三次，每次 ≤2 文件）。

**核心约束**：
- P0 案例指标链 `/customers/{slug}`；P5 GEO 链 seo-geo
- 长段落 ≥3；列表占比 ≤ 类型上限；**衔接率 ≥70%**；**连续短段 ≤2**
- CTA ≤2；spend caps / approvals 叙事（P4）
- Who/How/Why（Pillar/Framework 强制）
- **段落长度标准差 ≥1.5**；**0 碎片化集群（≥2 处 → FAIL）**
- **每节至少 1 个 ≥3 句段落**

---

### Phase 5 — SelfCheck（12 维加权评分 + 2 项 Gate Check）

#### 5.1 Hard Gates（一票否决，不计分）

| Gate | Pass? | 任一 Fail → STOP |
|------|:---:|------|
| G1–G7 | | |
| P1–P5 | | |
| Slug Gate B | | |

#### 5.2 十二维加权评分

> **评分范围 1–10，加权合计 100 分。总分 <70 → 不得进入 Phase 6。**
> **#13 FAQ / #14 Platform Status 为 Gate Check——任一项 Fail 则不得进入 Phase 6，不计入加权分。**

| # | 维度 | 权重 | 要点 | 参考 |
|---|------|:---:|------|------|
| 1 | **EEAT & Fact** | **20%** | Source Map 完整；Claim 按证据分级；Who/How/Why；≥1 非自有推荐 | eeat-framework + citations |
| 2 | **Information Gain** | **14%** | ≥2 条 SERP 增量；结构化差异方法；冗余段 <40% | serp-audit + content-graph |
| 3 | **Presentation & Rhythm** | **12%** | 长段 ≥3；连续短段 ≤2；段落标准差 ≥1.5；衔接率 ≥70%；0 碎片化集群；列表 ≤ 上限 | presentation-rhythm ⭐ |
| 4 | **Writing & Voice** | **11%** | 品牌 Voice 5 项满足；禁止措辞 0 触犯；空泛句 ≤2 处；段落 60–90 词；句子 15–24 词 | article-types §8 |
| 5 | **SERP Fit** | **8%** | SERP 审计完整；关键词覆盖到位；snippet-ready 定义；PAA 覆盖；meta 精准 | serp-audit ⭐ |
| 6 | **SEO & Strategy Fit** | **7%** | intent 类型正确；Hub-Spoke 角色清晰；与 Pillar 形成互补 | serp-audit + content-graph |
| 7 | **Structure & Scannability** | **7%** | Lead ≤250w；H2 可扫描；Conclusion；FAQ（固定 6 题）；无 "表格+一句话" 空壳 | article-types §2.2 |
| 8 | **Objectivity** | **7%** | 产品提及 ≤ 类型上限；竞品公平描述；无贬低措辞；署名真实；定位语言与功能事实区分 | project-config §1.6 |
| 9 | **Internal Links** | **5%** | 白名单内链 ≥2；P5 GEO 必链；0 `forthcoming`；锚文本语义化 | platform-routing |
| 10 | **CTA / Conversion** | **4%** | CTA ≤2；匹配读者阶段（Demo vs AIMA） | platform-routing §4 |
| 11 | **Depth & Density** | **3%** | 每 500 词 ≥1 具体例子；Why 内容 ≥30%；FAQ 独立于正文；无空壳段落 | eeat-framework |
| 12 | **Slug / H1 对齐** | **2%** | Gate B 已通过；Slug 可读、含关键词、无年份/架构词 | slug-gate |
| — | **FAQ Quality** | Gate | 固定 6 题；非重复正文；覆盖 PAA ≥2 题；答案 40–80 词 | serp-audit §3.3 |
| — | **Platform Status** | Gate | Déjà Vu private alpha；SOC 2 in flight；alpha/in-flight 标注正确 | proof-gate |

**交付标准**：Hard Gates 全 Pass + 总分 ≥70 + 无评分维度 <3/10 + FAQ 与 Platform Status Gate 全 Pass。

#### 5.3 总分等级

| 等级 | 分数 | 含义 |
|------|:---:|------|
| **S** | 90–100 | 标杆稿，立即发布 |
| **A** | 80–89 | 质量扎实，修 1–3 处后发布 |
| **B** | 70–79 | 需一轮精修 |
| **C** | 60–69 | 结构或可信度有明显缺口，不建议发布 |
| **D** | <60 | 需重写 |

#### 5.4 SelfCheck 输出格式

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| G1–G7 | Pass | |
| P1–P5 | Pass | |
| Slug | Pass | |

### Weighted Scoring (12 dimensions)
| # | Dimension | Weight | Score | Weighted | Notes |
|---|-----------|:---:|:---:|:---:|-------|
| 1 | EEAT & Fact | 20% | 8 | 1.60 | |
| 2 | Information Gain | 14% | 9 | 1.26 | |
| 3 | Presentation & Rhythm | 12% | 7 | 0.84 | |
| 4 | Writing & Voice | 11% | 8 | 0.88 | |
| 5 | SERP Fit | 8% | 8 | 0.64 | |
| 6 | SEO & Strategy Fit | 7% | 8 | 0.56 | |
| 7 | Structure & Scannability | 7% | 7 | 0.49 | |
| 8 | Objectivity | 7% | 9 | 0.63 | |
| 9 | Internal Links | 5% | 8 | 0.40 | |
| 10 | CTA / Conversion | 4% | 8 | 0.32 | |
| 11 | Depth & Density | 3% | 7 | 0.21 | |
| 12 | Slug / H1 | 2% | 9 | 0.18 | |
| **Total** | | **100%** | | **8.01 / 10** | |

### Gate Checks
| # | Check | Pass/Fail | Notes |
|---|-------|-----------|-------|
| 13 | FAQ Quality | ✅ Pass | |
| 14 | Platform Status | ✅ Pass | Déjà Vu = private alpha; SOC 2 = in flight |

### SERP Fit
{snippet-ready definition + top 5 gaps}

### Information Gain Audit
| Dimension | Unique? | Evidence |
|-----------|:---:|------|
| Framework/taxonomy | Yes | {description} |
| Comparison angle | Yes | {description} |
| Thesis/argument | Partial | {description} |
| Redundancy ratio | 35% | (<40% → Pass) |

### Source Map
{from citations.md template}

### Fragmentation Check
| Check | Result |
|-------|--------|
| Continuous short clusters | 0 |
| Transition rate | 78% |
| List ratio | 22% |
| Paragraph stddev | 1.8 |

### Cannibalization Check
| vs | Boundary | Clear? |
|----|----------|:---:|
| | | |
```

---

### Phase 5.5 — Cross-Article Audit ⭐NEW

> **批量创作（同一批次 ≥2 篇）或系列文章时触发。单篇跳过。**

#### 5.5.1 跨篇 10 项检查

| # | 检查项 | 方法 | 红线 |
|---|------|------|------|
| CA1 | 叙事模式雷同 | 3+ 篇同结构（教育→中立→"but X"→产品答案）→ 信任崩塌 | ≥3 篇 ❌ |
| CA2 | 内容网络完整性 | 互链是否双向？A 链 B，B 是否回链 A？ | 2+ 单向 ❌ |
| CA3 | 署名一致性 | 同系列是否统一署 Kostja？ | 出现虚构署名 ❌ |
| CA4 | 分类准确性 | category 标签与内容是否一致？ | 分类错误 ❌ |
| CA5 | 产品描述跨篇重复率 | 相同产品描述在多篇重复 >30%？退化为营销轰炸 | >30% ❌ |
| CA6 | 核心概念跨篇重复 | 非 canonical 文是否越界展开 >2 段？ | 2+ 越界 ❌ |
| CA7 | Intro 模板化 | 多篇 Intro 共享相同三段式结构？ | 3+ 篇 ❌ |
| CA8 | Conclusion 模板化 | 多篇 Conclusion 共享相同收束模式？ | 3+ 篇 ❌ |
| CA9 | 跨篇表现形式雷同 | 3+ 篇共享相同段落节奏模式（每篇都是"短-列表-短"） | 3+ 篇 ❌ |
| CA10 | Intro/Conclusion 内容关联度 | 删掉定义句和路标句后，剩余内容能否唯一标识该篇？ | 无法区分 ❌ |

#### 5.5.2 跨篇输出格式

```markdown
## Cross-Article Audit — Batch {name}

| # | Check | Result | Notes |
|---|-------|--------|-------|
| CA1 | Narrative pattern | ✅ Pass | |
| CA2 | Link reciprocity | ⚠️ 1 way | #02 → #01 but no backlink |
| ... | ... | ... | |
```

**CA1–CA6 任一项 ❌ → 批量交付前必修。**

---

### Phase 6 — Delivery

1. 写入 `hellyeah/blog/NN-{working-slug}.md`
2. Article Brief 最终版
3. SelfCheck 完整输出（15 维加权 + Source Map + SERP Fit + Fragmentation Check）
4. Cross-Article Audit（如有批量）
5. 提示人类更新 `hellyeah/blog/README.md`
6. **Meta 预留**（v1 无 meta skill）：

```
Title: 45–65 chars；Pillar 可含 (2026)；通常不加 | Hellyeah
Description: 140–160 chars；主关键词在前 80 chars 内
```

---

## §4 内容图谱

> **`references/content-graph.md`** — Phase 0 / Phase 5 加载

当前：**01** PlatformExplainer `what-is-hellyeah-ai` ✅ draft。下一序号 **02**。

---

## §5 关键词

> **`references/keywords.md`** — Phase 0 加载

---

## §6 产品与竞品

> **`references/product-competitors.md`** — Phase 4 / Phase 5 加载

---

## Gotchas — 禁止项（精选 30 条）

**结构**：❌ TL;DR 模块 · ❌ 编号 H2 · ❌ Framework 写成可复制清单 · ❌ 连续 3+ 短段 · ❌ 衔接率 <50%

**表现节奏** ⭐NEW：❌ 连续短段集群 ≥2 处 · ❌ 列表轰炸（相邻 2+ H2 各含列表无分析） · ❌ 裸表格/列表 · ❌ 段落标准差 <1.0 · ❌ H2 后直接列表无过渡

**Slug/链接**：❌ slug 缺 `/blog/` · ❌ 内部架构词 slug（framework/guide） · ❌ 链 `/platforms/*` `/trust-center` `/arenas/*` · ❌ forthcoming >1

**品牌/Proof**：❌ SOC 2 Type II certified · ❌ Déjà Vu GA · ❌ $1,500 AIMA · ❌ 案例指标无链 · ❌ guaranteed ROAS

**GEO**：❌ GEO 同义词全文无 `/capabilities/seo-geo` 内链（P5）

**EEAT** ⭐NEW：❌ 无来源量化 claim · ❌ 竞品描述无官方验证 · ❌ 署名虚构 · ❌ 绝对化营销语（revolutionary/game-changing/unlock/seamless/magic） · ❌ 空泛句 >3 处

**流程**：❌ Gate 未全 Pass 交付 · ❌ 一次加载全部 references · ❌ 运行时读 hellyeah-*.md

---

## Reference Index

| 文件 | 内容 | 加载时机 | 版本 |
|------|------|------|:---:|
| `references/project-config.md` | 配置 + G1–G7 + URL 白名单 | Phase 0 / 5 | 1.0 |
| `references/proof-gate.md` | P1–P5 + 案例表 | Phase 0 / 5 | 1.0 |
| `references/platform-routing.md` | CTA + 四平台 + Persona | Phase 0 / 4 | 1.0 |
| `references/article-types.md` | 8 类 + H2 + Voice + Brief | Phase 0 / 3 / 4 | 1.0 |
| `references/content-graph.md` | 文件表 + hub-spoke | Phase 0 / 5 | 1.0 |
| `references/keywords.md` | 主题桶 + JTBD | Phase 0 | 1.0 |
| `references/product-competitors.md` | 竞品 + battlecard | Phase 4 / 5 | 1.0 |
| `references/citations.md` | P0/P1/P2 + Source Map | Phase 4 / 5 | 1.0 |
| `references/slug-gate.md` | Gate B | Phase 2 | 1.0 |
| `references/mini-example.md` | Pillar Brief 范例 | Phase 1 / 3 | 1.0 |
| `references/eeat-framework.md` ⭐ | EEAT 四信号 + Claim 分级 + 引用优先级 | Phase 4 / 5 | v1.0 |
| `references/presentation-rhythm.md` ⭐ | 段落节奏 + 列表策略 + 碎片化检测 + 衔接率 + 12 项 Checklist | Phase 4 / 5 | v1.0 |
| `references/serp-audit.md` ⭐ | SERP Fit 审计 + Information Gain + Featured Snippet + PAA + 竞争评估 | Phase 0 / 5 | v1.1 |
| `references/presentation.md` | ⚠️ **已废弃** — 内容已迁移至 presentation-rhythm.md | 不再加载 | deprecated |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.0.0** | 2026-06-15 | 重大升级：12 维加权 SelfCheck（100% 合计）+ 2 Gate Check；新增 Phase 5.5 跨文章审计（CA1–CA10）；新增 eeat-framework + presentation-rhythm + serp-audit；Voice 扩展至 5 正向+5 禁止+空泛句 10 项；碎片化 6 类型检测；段落衔接率 ≥70%；SERP Fit 审计模板；Information Gain 结构化审计；Google HCU 2025 对齐 |
| **2.0.0-rc1** | 2026-06-15 | 原始 v2：15 维评分，权重 99%（已修复为 12 维 100%） |
| **1.0.0** | 2026-06-15 | 初版：8 类路由 + 7 Phase + G1–G7 + P1–P5 + 12 维 SelfCheck + references + evals |

---

## v2.1 Backlog

| # | 项目 | 优先级 | 说明 |
|---|------|:---:|------|
| 1 | `hellyeah-meta-title-description` skill | P1 | 独立 skill 处理 title/description 优化（E02 当前只能 manual） |
| 2 | Schema markup 实现指导 | P2 | serp-audit.md §5 仅为预留清单，需补充 Hellyeah Next.js 实际实现 |
| 3 | Content freshness 策略 | P2 | updated date + 实质性修订标注策略，影响 Google QRG 评估 |
| 4 | `presentation.md` 完全删除 | P3 | 当前仅 deprecated 标注，确认无引用后可删 |
| 5 | Information Gain 段落级冗余率自动化 | P3 | Phase 0.2 的逐段冗余标记目前依赖人工判断 |

---

*hellyeah-blog-article · v2.0.0 · 2026-06-15 · B2B enterprise growth*
