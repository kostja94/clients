---
name: datus-glossary-article
description: >
  Create Datus glossary blog articles (datus.ai/blog) — term definitions
  (what-is-*) and concept comparisons (*-vs-*). category: Glossary only.
  Do NOT load for Data Engineering Agent cluster articles or title-only tasks.
metadata:
  version: 2.0.0
  project: datus.ai
  locale: en
  load-rule: progressive-disclosure
  max-primary-lines: 500
  self-contained: true
  forbidden-reads:
    - datus.md
    - datus-*.md
    - blog/README.md
    - blog/keyword-cluster-*.md
    - blog/internal-external-links-checklist.md
---

# Datus Glossary Article Creation

为 **https://datus.ai/blog/** 产出 **`category: Glossary`** 术语定义文与概念对比文。

**硬性规则**：Agent 执行本 skill 时只读本文件夹内文件，禁止读取仓库内 `datus.md`、`datus-*.md`、`blog/README.md`、`blog/keyword-cluster-*.md`、`blog/internal-external-links-checklist.md` 或其他外部文档。

**范围外**：教程、案例、vs 竞品长文、**Tools List / 榜单**（`best X` / `X tools list` / `directory` / `complete list`）→ **`datus-blog-article`**（ToolsList MVP 已上线；其余类型仍在 backlog）。

---

## 渐进式加载规则（硬性）

```
Agent 默认只读本文件（SKILL.md）。
Phase 需要细节时，按指针读取 references/{file}.md（一次最多 2 个）。
禁止一次性加载全部 references。
读完用完即弃——不跨 Phase 保留 reference 上下文。
```

---

## §0 如何使用

### 触发语

```
按 datus-glossary-article skill，为术语 "{primary keyword}" 创建一篇
{GlossaryTerm|GlossaryComparison} 文章。
发布目的：{SEO|品牌}。目标读者：{描述}。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 术语 / 主关键词 | ✅ | 决定 intent 与 §2 类型路由 |
| 文章类型 | 可选 | 未给则 Agent 按 §2 推断 |
| Glossary 类别 A–G | 可选 | 见 glossary-terms.md |
| SERP 竞品 URL | 推荐 | Phase 0 信息增量 |

### 输出（Phase 6 交付物）

1. **Article Brief**（Markdown）
2. **完整稿** `datus/blog/NN-{slug}.md`（NN = content-graph 下一序号，当前 **31**）
3. **SelfCheck 表**（10 维加权 + 2 Gate Check + Hard Gates）
4. **Source Map**（内部，不发布）
5. **SERP Fit 审计表**（Phase 0 输出，Phase 5 复核）
6. **提示人类**更新 `blog/README.md` 与 `internal-external-links-checklist.md`

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| Tools List / `best X` / 目录榜单 | `datus-blog-article` → ToolsList |
| Tutorial / Case Study / vs 竞品长文 | `datus-blog-article` backlog（尚未实现） |
| 仅优化 title/description | 未来 `datus-meta-title-description` |
| `/glossary` 聚合页短定义 | 单独页面模板 |
| 非英文内容 | 另建 ZH skill |

---

## §1 项目配置与 Gate 清单

> **完整配置 + G1–G7 + D1–D4 → `references/project-config.md`**
> **产品事实 + 竞品 → `references/product-facts.md`**

**Phase 0 / Phase 5 前加载 project-config。**

| Gate | 项数 | 阻断条件 |
|------|:---:|------|
| **G1–G7** | 7 | 事实 / 死链 / 无来源数字 / 竞品状态 / 夸大 / forbidden URL / 品牌风险 |
| **D1–D4** | 4 | Cannibalization / link budget / product ratio / category lock |

全部 Pass 方可交付。

---

## §2 文章类型路由

> **H2 模板 + Frontmatter → `references/article-types.md`**

| 类型 | 路由信号 | 词数 | Slug | Datus 占比 |
|------|---------|------|------|:---:|
| **GlossaryTerm** | `what is` / 单术语 | 2200–3200 | `what-is-{term}` | ≤15% |
| **GlossaryComparison** | `vs` / 两概念对比 | 2400–3400 | `{a}-vs-{b}` | ≤15% |

**路由规则**：`vs` / `difference between` + 两概念 → GlossaryComparison；其余 → GlossaryTerm。
**叙事**：教育优先；Datus 仅 FAQ 前 ≤3 段；§1 须 snippet-ready 定义。

---

## §3 创作工作流（7 Phase + 3 Gate）

```
Phase 0 — Intake & Gate A ─── MERGE → 告知用户合并建议并 STOP
Phase 1 — Article Brief
Phase 2 — Slug & Gate B ─── 不通过 → 重选 slug
Phase 3 — Outline
Phase 4 — Draft
Phase 5 — SelfCheck & Gate C ─── 不通过 → 修复
Phase 5.5 — Cross-Article Audit ─── 批量产出时触发 ⭐v2.0.0
Phase 6 — Delivery
```

---

### Phase 0 — Intake & Gate A

**加载**：`glossary-terms.md` + `content-graph.md`

#### 0.1 四必问

| # | 问题 |
|---|------|
| 1 | 目标术语 + Glossary 类别 A–G？ |
| 2 | 主关键词 + search intent？ |
| 3 | 与已有 **11 篇**关系？canonical / spoke / comparison |
| 4 | SERP Top 3 竞品 URL？ |

**第一行输出**：`## Topic Scope: {term} · Category {A–G} · {GlossaryTerm|GlossaryComparison}`

#### 0.2 Gate A — KEEP/MERGE

对照 glossary-terms.md + content-graph.md：

| 结果 | 条件 | Agent 动作 |
|------|------|-----------|
| **MERGE** | 术语已有 `blog_status: published` | 输出 `## Gate A: MERGE → {canonical_slug}`，说明合并理由，**STOP** |
| **MERGE** | 对比 topic 已有 canonical | 同上 |
| **KEEP** | 新术语或新对比 intent | 输出 `## Gate A: KEEP`，继续 Phase 1 |

**Agent 必须在第一行输出 KEEP/MERGE 判定**，不可跳过。MERGE 时须给出建议合并到的具体 canonical slug。

#### 0.3 信息增量 Gate

相对 SERP Top 3，至少 **2 项**独有，否则 STOP：
- 工程向 case walkthrough / 失败模式 taxonomy
- 决策表 / 对比框架（≥6 行维度）
- Agent + context 连接（Datus 品类角度）
- 边界声明（what X is not）
- Production readiness checklist

#### 0.4 SERP Fit 审计 ⭐v2.0.0

```markdown
## SERP Fit — {primary keyword}
Primary keyword:
Search intent:
Top 3 ranking pages:
  1. URL — covers:
  2. URL — covers:
  3. URL — covers:
Common coverage:
What they miss:
Our unique contribution:
Snippet-ready definition (40–60 words):
**People Also Ask** (top 3 PAA questions to cover in FAQ):
  1.
  2.
  3.
Competitive intensity: Low / Medium / High
```

---

### Phase 1 — Article Brief

**加载**：`mini-example.md`

须含：Article type、Glossary category A–G、Hub link、planned internal links、Information increment ≥2 items、KEEP/MERGE。

---

### Phase 2 — Slug & Gate B

**加载**：`slug-gate.md` + `article-types.md`

1. 2–3 slug 候选 + 推荐
2. Gate B：6 问 + 12 反模式
3. title（45–70 chars）+ description（120–160 chars）
4. 完整 frontmatter 骨架

---

### Phase 3 — Outline

**加载**：`article-types.md` + `presentation.md`（Voice / 链接规范）

编号 H2 骨架，每节标注词数、内链占位、snippet 位置。结构硬要求：Excerpt（1–2 句）→ TL;DR → `## 1.`…`## N.` → Conclusion → FAQ。

---

### Phase 4 — Draft

**加载**：`product-facts.md` + `eeat-framework.md`（第一轮），`citations.md` + `presentation-rhythm.md`（第二轮）。分两轮，每轮 ≤2 文件。

| 规则 | 执行 |
|------|------|
| 语言 | 英文正文 |
| 站外 | `<a href="..." rel="nofollow noopener">` |
| Datus | ≤15%；FAQ 前 ≤3 段 |
| Canonical | 已有术语 1–2 句 + link（D1） |
| **段落节奏** ⭐ | 长段 ≥3；列表 ≤25%；连续短段 ≤2；衔接率 ≥70% |
| **EEAT** ⭐ | 量化 claim 有来源；竞品可核实；POC ≠ GA |

---

### Phase 5 — SelfCheck（10 维加权 + 2 Gate Check）

#### 5.1 Hard Gates（一票否决，不计分）

| Gate | 任一 Fail → STOP |
|------|------|
| G1–G7 | |
| D1–D4 | |
| Slug Gate B | |

#### 5.2 十维加权评分 ⭐v2.0.0

> **评分 1–10，加权合计 100 分。总分 <70 → 不得进入 Phase 6。**

| # | 维度 | 权重 | 要点 | 参考 |
|---|------|:---:|------|------|
| 1 | **EEAT & Fact** | **22%** | Source Map 完整；Claim 有来源；POC≠GA；≥1 竞品优势 | eeat-framework + citations |
| 2 | **Information Gain** | **16%** | ≥2 项 SERP 增量；case/table/checklist 独有；与 canonical 不重复 | content-graph + SERP audit |
| 3 | **Presentation & Rhythm** | **14%** | 长段≥3；列表≤25%；衔接率≥70%；0 碎片化集群；段落标准差≥1.5 | presentation-rhythm ⭐ |
| 4 | **Writing & Voice** | **11%** | 工程实践深度；Wirecutter 式客观；0 空泛句；0 禁词 | presentation §1 + article-types |
| 5 | **SERP Fit** | **8%** | SERP 审计完整；snippet-ready 定义 150–200 词 + TL;DR 压缩版；PAA 覆盖 | Phase 0.4 模板 |
| 6 | **Structure & Scannability** | **8%** | Excerpt + TL;DR + 编号 H2 + Conclusion + FAQ（固定 6 题）；H2 可扫描 | article-types §2–4 |
| 7 | **Objectivity** | **7%** | Datus ≤15%；竞品公平；无贬低措辞；漏斗透明 | project-config + product-facts |
| 8 | **Internal Links** | **5%** | blog ≥2；glossary ≤3；外链 2–5；0 forbidden | project-config §1.3–1.4 |
| 9 | **Depth & Density** | **5%** | 词数达标；每 ~500 词 ≥1 具体例子；深度节有 case walkthrough | article-types + eeat-framework |
| 10 | **Slug / H1 / Meta** | **4%** | Gate B 6/6；title 45–70 chars；desc 120–160 | slug-gate + project-config §5 |
| — | **FAQ Quality** | Gate | 固定 6 题；独立内容；覆盖 PAA ≥2 题 | Phase 5 单独检查 |
| — | **Glossary Gate** | Gate | D1–D4 全部 Pass（已在 Hard Gates 中） | project-config §3 |

**交付标准**：Hard Gates 全 Pass + 总分 ≥70 + 无维度 <3/10 + FAQ Gate Pass。

#### 5.3 总分等级

| 等级 | 分数 | 含义 |
|------|:---:|------|
| **S** | 90–100 | 标杆稿 |
| **A** | 80–89 | 质量扎实 |
| **B** | 70–79 | 需精修 |
| **C** | 60–69 | 不建议发布 |
| **D** | <60 | 重写 |

#### 5.4 SelfCheck 输出格式 ⭐v2.0.0

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| G1–G7 | Pass | |
| D1–D4 | Pass | |
| Slug | Pass | |

### Weighted Scoring (10 dimensions)
| # | Dimension | Weight | Score | Weighted | Notes |
|---|-----------|:---:|:---:|:---:|-------|
| 1 | EEAT & Fact | 22% | 8 | 1.76 | |
| 2 | Information Gain | 16% | 8 | 1.28 | |
| 3 | Presentation & Rhythm | 14% | 7 | 0.98 | |
| ... | ... | ... | ... | ... | |
| **Total** | | **100%** | | **X.XX / 10** | |

### Gate Checks
| Check | Pass/Fail | Notes |
|-------|-----------|-------|
| FAQ Quality | ✅ Pass | |
| Glossary Gate | ✅ Pass | |

### SERP Fit
{snippet-ready definition + top 3 gaps}

### Source Map
| Claim | § | Source | Checked | Confidence |
|------|------|------|------|:---:|

### Fragmentation Check
| Check | Result |
|-------|--------|
| Continuous short clusters | 0 |
| Transition rate | XX% |
| List ratio | XX% |

### Cannibalization Check
| vs | Boundary | Clear? |
|----|----------|:---:|
```

---

### Phase 5.5 — Cross-Article Audit ⭐v2.0.0

> **批量产出（同一批次 ≥2 篇 glossary 文）时触发。**

| # | 检查项 | 红线 |
|---|------|------|
| CA1 | Excerpt 模式雷同 | 3+ 篇同 excerpt 模式（A/B/C 重复）→ ❌ |
| CA2 | 产品描述跨篇重复 | Datus Context Engine 描述重复 >30% → ❌ |
| CA3 | 叙事模式雷同 | 3+ 篇同结构（定义→对比→agent→结论）→ ❌ |
| CA4 | 署名一致性 | 全部署 Kostja |
| CA5 | 核心概念跨篇重复 | 非 canonical 文越界展开 >2 段 → ❌ |
| CA6 | 深度节选题雷同 | 3+ 篇选同一深度节模式 → ⚠️ |

---

### Phase 6 — Delivery

1. 写入 `datus/blog/NN-{slug}.md`
2. 输出 Brief + SelfCheck（10 维加权） + Source Map + Cross-Article Audit（如有）
3. 提示人类更新 README / checklist

---

## §6 references 索引

| 文件 | 加载 Phase | 版本 |
|------|-----------|:---:|
| project-config.md | 0, 5 | 1.0 |
| glossary-terms.md | 0 | 1.0 |
| content-graph.md | 0, 3 | 1.0 |
| article-types.md | 1, 2, 3, 4 | 1.0 |
| slug-gate.md | 2 | 1.0 |
| product-facts.md | 4 | 1.0 |
| citations.md | 4 | 1.0 |
| mini-example.md | 1, 3 | 1.0 |
| eeat-framework.md ⭐ | 4, 5 | v1.0 |
| presentation.md | Voice / 链接规范（非 deprecated） | 3 | 1.0 |
| presentation-rhythm.md ⭐ | 段落节奏 + 列表策略 + 碎片化检测 + 衔接率 | 4, 5 | v1.0 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **2.0.0** | 2026-06-15 | 重大升级：10 维加权 SelfCheck（100%）+ 2 Gate Check；新增 Phase 5.5 跨文章审计（CA1–CA6）；新增 eeat-framework + presentation-rhythm 两个 reference；碎片化 6 类型检测；段落衔接率 ≥70%；SERP Fit 审计 + PAA 字段；空泛句 10 项检测（presentation.md §1.2）；统一外链 2–5 |
| **1.0.0** | 2026-06-15 | 初版：2 类路由 + 6 Phase + G1–G7 + D1–D4 + 6 维 Pass/Fail SelfCheck |

---

## v2.1 Backlog

| # | 项目 | 说明 |
|---|------|------|
| 1 | `datus-meta-title-description` skill | title-only 任务独立 skill |
| 2 | `datus-blog-article` skill | **partially shipped（ToolsList MVP，2026-07-20）**；Tutorial / Case Study / vs 竞品长文未做 |
| 3 | Schema markup 指导 | FAQ schema 对 glossary 文有价值 |
| 4 | `presentation.md` 精简 | 仅保留 Voice/链接规范，删节奏旧内容 |

---

*datus-glossary-article · v2.0.0 · 2026-06-15 · datus.ai/blog · category: Glossary only*
