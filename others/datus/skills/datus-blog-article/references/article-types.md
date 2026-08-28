# Datus Blog — 文章类型路由（基于内容意图）

> Phase 0 / 2 / 3 / 4 按需加载。**先判 ArticleType，再定 `category` + `secondaryCategory` + H2 模板。**
> 不再按 skill 文件夹或旧 Glossary/ToolsList 双 skill 分流。

---

## 1. 两层分类

| 层 | frontmatter 字段 | 含义 | 决定方式 |
|----|------------------|------|----------|
| **主题簇** | `category` | 内容网络位置（SEO 簇） | 由 **Topic Cluster** 决定（见 `content-graph.md`） |
| **文章体裁** | `secondaryCategory` | 写作模板与 Gate | 由 **ArticleType** 决定（本节路由） |

**示例**：

```yaml
category: "Semantic Layer"          # 主题簇
secondaryCategory: "Glossary"       # 体裁 = GlossaryTerm
```

```yaml
category: "Data Engineering Agent"
secondaryCategory: "ToolsList"
```

---

## 2. ArticleType 路由表（当前 + 可扩展）

收到任务后 **按下列优先级匹配**（从上到下，首个命中为准）：

| 优先级 | ArticleType | secondaryCategory | 典型搜索/内容信号 | 词数 | Datus 占比 | 默认 Mode |
|:---:|:---|:---|:---|:---:|:---:|:---:|
| 1 | **Product** | Product | `introducing` / 产品发布 / 能力官宣 / changelog 叙事 | 1800–2800 | ≤40% | lite |
| 2 | **ToolsList** | ToolsList | `best` / `tools list` / `directory` / `complete list` / 横向榜单 | 2800–4000 | ≤25% | standard |
| 3 | **GlossaryComparison** | Glossary | `X vs Y` / `difference between` + **两概念**（非产品对标页） | 2400–3400 | ≤15% | flagship |
| 4 | **Comparison** | Comparison | `X vs Y` + **产品/平台/实现**（MetricFlow、LookML、Cube…） | 2200–3200 | ≤20% | standard |
| 5 | **GlossaryTerm** | Glossary | `what is` / 单术语定义 / 标准科普 | 2200–3200 | ≤15% | flagship |
| 6 | **Tutorial** | Product | `build your first` / `step-by-step` / `how to set up` / 15-min guide | 2500–3500 | ≤30% | standard |
| 7 | **Research** | Research | 深度指南 / 案例研究叙事 / `how {vendor} works` / 品类深潜 | 2800–4500 | ≤25% | flagship |
| 8 | **Pillar** | Research | 品类 Hub / `what is {category}` + 多产品对比框架 | 3200–4800 | ≤20% | flagship |

### 2.1 歧义消解规则

| 场景 | 判定 |
|------|------|
| `semantic layer vs ontology` | **GlossaryComparison**（概念对比） |
| `osi vs dbt metricflow` | **Comparison**（产品/栈对比） |
| `what is semantic layer` | **GlossaryTerm** |
| `what is data engineering agent` + 多产品例子 | **Pillar** |
| `best data engineering agents` | **ToolsList** |
| `introducing datus knowledge` | **Product** |
| `dbt semantic layer metricflow` 长指南 | **Research** |
| `build your first data engineering agent` | **Tutorial** |
| 用户只给关键词，类型不明 | Agent **推断 ArticleType 并告知用户**，写入 Phase 0 首行 |

### 2.2 Topic Cluster → `category` 映射

ArticleType **不**决定 `category`。对照 `content-graph.md` Cluster 注册表：

| folder | `category` |
|--------|------------|
| `data-agent/` | Data Agent |
| `data-engineering-agent/` | Data Engineering Agent |
| `semantic-layer/` | Semantic Layer |
| `osi/` | OSI |
| `dosi/` | Dosi |
| `features/` | Features |
| 根目录散篇 | Glossary（`secondaryCategory: Glossary` 时可无 secondary 以外的体裁约束） |

**Phase 0 输出**：`## ArticleType: {type} · category: {cluster} · secondaryCategory: {体裁}`

---

## 3. 全类型通用模块

| 模块 | 要求 |
|------|------|
| **H1** | `# {Title}` — 含 primary keyword |
| **TL;DR** | `## TL;DR` — 3–5 bullets；首条含 BLUF / snippet-ready 摘要 |
| **H2 编号** | `## 1.` … `## N.`；Conclusion / FAQ **不**编号 |
| **Conclusion** | `## Conclusion` |
| **FAQ** | `## Frequently asked questions` — 4–6 题；独立内容，不得从正文复制 |
| **内链** | blog ≥2；`/glossary` ≤3（Glossary 体裁）；上下文自然 |
| **外链** | 2–5；HTML `<a href="..." rel="nofollow noopener">` |
| **段落** | 长段 ≥3；列表比例见 `presentation-rhythm.md`；衔接率 ≥70% |

---

## 4. 各类型 H2 模板（摘要）

完整模板见各节；Phase 3 须按 ArticleType 选用。

### 4.1 GlossaryTerm

定义 → 边界/对比 → 动机 → agent 连接 → 深度节（2–3）→ Conclusion → FAQ。

Canonical 节：`{Term}: a working definition`（400–500 词 + blockquote 定义）。

### 4.2 GlossaryComparison

Term A 定义 → Term B 定义 → 对比表（≥6 行）→ 决策框架 → agent 语境 → FAQ。

若 A/B 已有 canonical → 1–2 句 + link（D1）。

### 4.3 ToolsList

市场分类（**散文**，禁每类一张产品表）→ **唯一**产品目录主表 → 评估维度深潜 → 选型框架 → agent 连接 → FAQ。

**表格预算**：全文 ≤3 表；产品目录表 = 1。见 `project-config.md` T1–T4。

### 4.4 Comparison

TL;DR → 两者各是什么 → 对比表 → 选型场景 → agent/栈语境 → FAQ。

### 4.5 Research

TL;DR → 背景/为什么现在 → 架构或演化 → 能力深潜 → 与 Datus/开源栈关系（克制）→ 结论 → FAQ。

### 4.6 Product

TL;DR → 问题/痛点 → 能力拆解 → 如何使用（链 docs）→ 与品类关系 → FAQ。

### 4.7 Tutorial

TL;DR → 前置条件 → 分步操作 → 日常 workflow → 故障排查 → FAQ。

### 4.8 Pillar

TL;DR → 工作定义 → 类型/架构分节 → 代表产品对比框架 → 与 contextual DE 叙事 → FAQ。

---

## 5. Frontmatter Schema

```yaml
---
title: "Title Case — Subtitle After Em Dash"
description: "120–160 chars"
slug: "kebab-case-evergreen-no-year"
date: YYYY-MM-DD
author: "Kostja"
category: "{Data Agent|Data Engineering Agent|Semantic Layer|OSI|Dosi|Features|Glossary}"
secondaryCategory: "{Glossary|Research|Comparison|ToolsList|Product}"
---
```

- **禁止**（除非人类显式要求）：`keywords`、`related`、`image`
- **slug** 不含年份、不含子目录前缀
- **文件名**：`blog/{cluster}/NN-{slug}.md` 或 `blog/NN-{slug}.md`（见 `topic-cluster-layout.md`）

---

## 6. 类型专属 Gate 速查

| ArticleType | 专属 Gate | 见 |
|-------------|-----------|-----|
| GlossaryTerm / GlossaryComparison | D1–D4 | `project-config.md` §3 |
| ToolsList | T1–T4 | `project-config.md` §4 |
| Product / Tutorial | P1–P3 | `project-config.md` §5 |
| Comparison / Research / Pillar | R1–R2 | `project-config.md` §6 |

**G1–G7 全类型通用**。

---

## 7. Backlog 类型（路由预留，尚未写模板）

以下类型 **Phase 0 可识别**，若用户请求且无模板 → STOP 并说明需先扩展 `article-types.md`：

| 预留 ArticleType | 信号 |
|------------------|------|
| **CaseStudy** | `/case-studies/`、`customer story`、named production rollout |
| **Alternative** | `alternatives to {vendor}` |
| **PlatformOps** | 单平台操作指南（非 Tutorial 深度） |

---

*article-types · v2.0.0 · 2026-08-28 · content-intent routing · single skill*
