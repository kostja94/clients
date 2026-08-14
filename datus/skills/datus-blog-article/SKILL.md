---
name: datus-blog-article
description: >
  Create Datus blog articles outside Glossary — ToolsList (best X / tools
  directory) first. category: Semantic Layer | Data Engineering Agent.
  Do NOT load for what-is-* or *-vs-* glossary terms.
metadata:
  version: 0.1.0
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

# Datus Blog Article Creation (ToolsList MVP)

为 **https://datus.ai/blog/** 产出 **非 Glossary** 榜单/目录文。

**本期范围**：仅 **ToolsList**（`best X` / `X tools list` / directory）。  
**未实现（backlog）**：Tutorial、Case Study、vs 竞品长文、平台对比长文。

**硬性规则**：Agent 执行本 skill 时只读本文件夹内文件，禁止读取仓库内 `datus.md`、`datus-*.md`、`blog/README.md`、`blog/keyword-cluster-*.md`、`blog/internal-external-links-checklist.md` 或其他外部文档。

**术语定义 / 概念对比** → 用 `datus-glossary-article`（`what-is-*` / `*-vs-*`，`category: Glossary`）。

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
按 datus-blog-article skill，为 "{primary keyword}" 创建一篇
ToolsList 文章。category：{Semantic Layer|Data Engineering Agent}。
发布目的：{SEO|品牌}。目标读者：{描述}。
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| 主关键词 / 品类 | ✅ | 如 semantic layer tools、best data engineering agents |
| 文章类型 | 可选 | 未给则按 §2 推断；本期仅 ToolsList |
| category | 推荐 | 见 §2 category 路由 |
| SERP 竞品 URL | 推荐 | Phase 0 信息增量 |

### 输出（Phase 5 交付物）

1. **Article Brief**（Markdown）
2. **完整稿** `datus/blog/NN-{slug}.md`
3. **SelfCheck 表**（Hard Gates + 加权维度摘要）
4. **提示人类**更新 `blog/README.md` 与 `internal-external-links-checklist.md`

与用户沟通可用中文；**正文必须为英文**。

### 何时不用本 skill

| 场景 | 改用 |
|------|------|
| `what is` / 单术语定义 | `datus-glossary-article` → GlossaryTerm |
| `X vs Y` 两概念对比 | `datus-glossary-article` → GlossaryComparison |
| Tutorial / Case Study / vs 竞品长文 | 本 skill backlog（尚未实现）→ 勿硬套 ToolsList |

---

## §1 项目配置与 Gate

> **完整配置 + G1–G7 + T1–T4 → `references/project-config.md`**

**Phase 0 / Phase 4 前加载 project-config。**

| Gate | 项数 | 阻断条件 |
|------|:---:|------|
| **G1–G7** | 7 | 事实 / 死链 / 无来源数字 / 竞品状态 / 夸大 / forbidden URL / 品牌风险 |
| **T1–T4** | 4 | category / 表格预算 / 内链 / Datus 占比 |

全部 Pass 方可交付。

---

## §2 文章类型与 category 路由

> **H2 模板 + 表格预算 → `references/article-types.md`**

| 类型 | 路由信号 | 词数 | Slug 模式 | Datus 占比 |
|------|---------|------|----------|:---:|
| **ToolsList** | `best` / `tools list` / `directory` / `complete list` | 2800–4000 | `{topic}-tools-list` 或 `best-{topic}` | ≤25% |

**本期仅产出 ToolsList。** 其他类型收到请求时 STOP 并说明未实现。

### Category 路由（ToolsList）

| 主题簇 | frontmatter `category` |
|--------|------------------------|
| Semantic layer / MetricFlow / Cube / OSI 工具目录 | **`Semantic Layer`** |
| Data engineering agent 榜单（如 best agents） | **`Data Engineering Agent`** |
| 任何 ToolsList | **禁止** `Glossary` |

---

## §3 创作工作流（6 Phase）

```
Phase 0 — Intake & SERP Fit
Phase 1 — Article Brief
Phase 2 — Outline
Phase 3 — Draft
Phase 4 — SelfCheck & Gates
Phase 5 — Delivery
```

---

### Phase 0 — Intake & SERP Fit

**加载**：`project-config.md`

#### 0.1 四必问

| # | 问题 |
|---|------|
| 1 | 品类 / 主关键词 + ToolsList 确认？ |
| 2 | category：`Semantic Layer` 或 `Data Engineering Agent`？ |
| 3 | 与已有 blog 关系？（链哪些 hub；勿重写 glossary 定义全文） |
| 4 | SERP Top 3 竞品 URL？ |

**第一行输出**：`## Topic Scope: {keyword} · ToolsList · category {Semantic Layer|Data Engineering Agent}`

#### 0.2 信息增量 Gate

相对 SERP Top 3，至少 **2 项**独有，否则 STOP：

- OSI / 互通性状态矩阵（或等价评估维度）
- 架构分类 prose + 唯一主对比表
- 选型 scorecard / 决策框架
- Agent + context 连接
- Converter / 成熟度分级（intent ≠ shipped）

#### 0.3 SERP Fit（简表）

```markdown
## SERP Fit — {primary keyword}
Primary keyword:
Search intent: ToolsList / commercial investigation
Top 3 ranking pages: ...
Our unique contribution: (≥2)
**People Also Ask** (top 3 → FAQ):
```

---

### Phase 1 — Article Brief

须含：Article type = ToolsList、category、hub links、information increment ≥2、table budget plan（哪 1–3 张表）。

---

### Phase 2 — Outline

**加载**：`article-types.md` + `presentation-rhythm.md`

编号 H2 骨架；标注每节词数、表位置、内链占位。结构硬要求：

Excerpt（1–2 句）→ TL;DR（5 bullets）→ `## 1.`…`## N.` → Conclusion → FAQ（固定 6 题，内容相关）。

**表格计划必须写清**：产品目录表恰好 1；全文表 ≤3。

---

### Phase 3 — Draft

**加载**：`project-config.md` + `presentation-rhythm.md`（可分两轮）

| 规则 | 执行 |
|------|------|
| 语言 | 英文正文 |
| 站外 | `<a href="..." rel="nofollow noopener">` |
| Datus | ≤25%；FAQ 前 ≤4 段 |
| Canonical 术语 | 已有 `what-is-*` → 1–2 句 + link，不重写全文 |
| 段落节奏 | 长段 ≥3；列表 ≤30%；裸表格 0；衔接率 ≥70% |
| 分类节 | **散文**；禁止每架构类一张产品表 |

样板节奏：`04-best-data-engineering-agents`（分类长段 → 1 主表 → 可选深度段）。

---

### Phase 4 — SelfCheck

#### 4.1 Hard Gates（一票否决）

| Gate | 任一 Fail → STOP |
|------|------|
| G1–G7 | 见 project-config |
| T1–T4 | category / 表预算 / 链接 / Datus % |

#### 4.2 加权评分（简化 8 维，满分 100）

总分 **<70 → 不得交付**。任一维 <3/10 → 修复。

| # | 维度 | 权重 | 要点 |
|---|------|:---:|------|
| 1 | EEAT & Fact | 22% | 量化 claim 有来源；POC≠GA；竞品可核实 |
| 2 | Information Gain | 16% | ≥2 项 SERP 增量 |
| 3 | Presentation & Rhythm | 14% | 长段≥3；列表≤30%；表≤3；0 裸表格 |
| 4 | ToolsList structure | 12% | 分类 prose；1 主产品表；表后读表分析 |
| 5 | Writing & Voice | 10% | Wirecutter 客观；0 贬低措辞 |
| 6 | SERP Fit / FAQ | 10% | FAQ 固定 6 题；PAA≥2 |
| 7 | Internal Links | 8% | blog≥2；外链 2–5；0 forbidden |
| 8 | Slug / Meta | 8% | title 45–70；desc 120–160；slug 无年份 |

#### 4.3 输出格式

```markdown
## SelfCheck — {slug}
### Hard Gates
| Gate | Pass/Fail | Notes |
### Weighted Scoring
| # | Dimension | Weight | Score | Weighted | Notes |
| **Total** | | 100% | | X.XX / 10 |
### Table Budget
| Table | Type | Counts toward product-directory? |
| Total tables | N / 3 max |
```

---

### Phase 5 — Delivery

1. 写入 `datus/blog/NN-{slug}.md`
2. 输出 Brief + SelfCheck
3. 提示人类更新 README / checklist（category、链接计数）

---

## §6 references 索引

| 文件 | 加载 Phase |
|------|-----------|
| project-config.md | 0, 3, 4 |
| article-types.md | 1, 2, 3 |
| presentation-rhythm.md | 2, 3, 4 |

---

## Changelog

| 版本 | 日期 | 变更 |
|------|------|------|
| **0.1.0** | 2026-07-20 | MVP：ToolsList only；category Semantic Layer / Data Engineering Agent；表预算 ≤3 |

---

## Backlog

| # | 项目 | 状态 |
|---|------|------|
| 1 | Tutorial 类型 | 未做 |
| 2 | Case Study 类型 | 未做 |
| 3 | vs 竞品 / 平台对比长文 | 未做 |
| 4 | 完整 10 维 SelfCheck + portable bundle 对齐 | 未做 |

---

*datus-blog-article · v0.1.0 · 2026-07-20 · ToolsList MVP · datus.ai/blog*
