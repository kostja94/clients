# Datus Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro、Lovable 等）。

**线上 URL 模式**：`https://datus.ai/blog/{slug}`（Lovable 预览：`datus.lovable.app/blog/{slug}`）

URL 仍按 `slug` 路由，**不**把主题文件夹写入公开路径。文件夹只用于本地选题簇管理。

---

## 目录结构总览

```
blog/
├── README.md
├── internal-external-links-checklist.md
│
├── 18-what-is-data-catalog.md          ← 根目录：基础设施 Glossary（未归入主题簇）
├── 19-what-is-data-mesh.md
├── 30-what-is-lakehouse.md
│
├── data-agent/                        ← Data Agent 簇（父词 Hub）
├── data-engineering-agent/            ← Data Engineering Agent 簇
├── semantic-layer/                    ← Semantic Layer 簇
├── osi/                               ← OSI / Apache Ossie 簇
├── features/                          ← Features 簇（产品能力；Hub = Introducing Datus Knowledge）
│
└── （创作 Skill 在 ../skills/）
```

---

## 主题簇与双分类

与 Floatboat 的 `claude/` / `deepseek/` / `worldcup/` 相同：**`category` = 主题，`secondaryCategory` = 体裁**。

| 主题簇 | 目录 | `category` | Hub slug |
|--------|------|------------|----------|
| Data Agent | `data-agent/` | `Data Agent` | `what-is-data-agent` |
| Data Engineering Agent | `data-engineering-agent/` | `Data Engineering Agent` | `what-is-data-engineering-agent` |
| Semantic Layer | `semantic-layer/` | `Semantic Layer` | `what-is-semantic-layer` |
| OSI | `osi/` | `OSI` | `open-semantic-interchange-osi` |
| Features | `features/` | `Features` | `introducing-datus-knowledge` |
| 未归簇（根目录） | `blog/` | `Glossary`（无 `secondaryCategory`） | — |

**`secondaryCategory` 取值**：`Glossary` | `Research` | `Comparison` | `ToolsList` | `Product`

> **Data Agent 簇**：`category: "Data Agent"`，`secondaryCategory` 保留体裁。父词截流；不要把 Cube/AtScale/Timbr 放进本目录。
>
> **Data Engineering Agent 簇**：`category: "Data Engineering Agent"`，`secondaryCategory` 保留体裁。
>
> **Semantic Layer 簇**：`category: "Semantic Layer"`，`secondaryCategory` 保留体裁。
>
> **OSI 簇**：`category: "OSI"`，`secondaryCategory` 保留体裁。
>
> **Features 簇**：`category: "Features"`，`secondaryCategory: Product`。产品能力与版本更新；**不要**重写 glossary 术语。选题见 [features/README.md](./features/README.md)。
>
> **根目录散篇**：不进主题簇的基础设施术语，仅 `category: "Glossary"`。

---

## Frontmatter 示例

主题簇文章：

```yaml
---
title: "Title Case — Subtitle"
description: "120–160 chars..."
slug: "kebab-case-slug"          # 不含年份，常青 URL
date: 2026-05-28
author: "Kostja"
category: "Data Engineering Agent"   # 或 Data Agent | Semantic Layer | OSI | Features
secondaryCategory: "Research"        # Glossary | Research | Comparison | ToolsList | Product
---
```

根目录 Glossary：

```yaml
---
title: "What Is a Lakehouse? ..."
slug: "what-is-lakehouse"
category: "Glossary"
---
```

## 正文规范

- 主节 H2 使用英文编号：`## 1.` … `## 7.`
- `## Conclusion`、`## Frequently asked questions` **不加**序号
- 站外链接使用 HTML：`<a href="URL" rel="nofollow noopener">锚文本</a>`
- 站内 Blog 互链：`/blog/{slug}`；Glossary 索引：`/glossary`（分类与互链见 [internal-external-links-checklist.md](./internal-external-links-checklist.md)）

---

## 文章列表

| # | 文件 | slug | 主题 | category | secondary | 状态 |
|---|------|------|------|----------|-----------|:---:|
| 1 | [data-engineering-agent/01-…](./data-engineering-agent/01-what-is-data-engineering-agent-2026.md) | `what-is-data-engineering-agent` | 品类定义 Hub | Data Engineering Agent | Research | ✅ |
| 2 | [semantic-layer/02-…](./semantic-layer/02-what-is-semantic-layer-2026.md) | `what-is-semantic-layer` | Semantic layer 术语定义 Hub | Semantic Layer | Glossary | ✅ |
| 3 | [data-engineering-agent/03-…](./data-engineering-agent/03-contextual-data-engineering-2026.md) | `contextual-data-engineering` | Contextual Data Engineering | Data Engineering Agent | Research | ✅ |
| 4 | [data-engineering-agent/04-…](./data-engineering-agent/04-best-data-engineering-agents-2026.md) | `best-data-engineering-agents` | 七大 Agent 横向对比 | Data Engineering Agent | ToolsList | ✅ |
| 5 | [data-engineering-agent/05-…](./data-engineering-agent/05-open-source-data-engineering-agents.md) | `open-source-data-engineering-agents` | 开源 Agent 三选一 | Data Engineering Agent | Comparison | ✅ |
| 6 | [data-engineering-agent/06-…](./data-engineering-agent/06-build-your-first-data-engineering-agent.md) | `build-your-first-data-engineering-agent` | 15 分钟教程 + CLI 工作流 | Data Engineering Agent | Product | ✅ |
| 7 | [data-engineering-agent/07-…](./data-engineering-agent/07-data-engineering-agent-vs-claude-code.md) | `data-engineering-agent-vs-claude-code` | vs Claude Code | Data Engineering Agent | Comparison | ✅ |
| 8 | [data-engineering-agent/08-…](./data-engineering-agent/08-data-engineering-agent-vs-sql-copilot.md) | `data-engineering-agent-vs-sql-copilot` | Agent vs Copilot | Data Engineering Agent | Comparison | ✅ |
| 9 | [data-engineering-agent/09-…](./data-engineering-agent/09-one-person-data-team.md) | `one-person-data-team` | 一人数据团队 | Data Engineering Agent | Product | ✅ |
| 10 | [data-engineering-agent/10-…](./data-engineering-agent/10-context-engine-data-engineering-agent-accuracy.md) | `context-engine-data-engineering-agent-accuracy` | Context Engine 准确率 | Data Engineering Agent | Research | ✅ |
| 11 | [data-engineering-agent/11-…](./data-engineering-agent/11-mcp-data-engineering.md) | `mcp-data-engineering` | MCP 与数据工程 | Data Engineering Agent | Research | ✅ |
| 12 | —（空号，已并入 #06） | — | — | — | — | — |
| 13 | [data-engineering-agent/13-…](./data-engineering-agent/13-enterprise-data-engineering-agent.md) | `enterprise-data-engineering-agent` | 企业级 Agent 需求 | Data Engineering Agent | Research | ✅ |
| 14 | [data-engineering-agent/14-…](./data-engineering-agent/14-subagents-domain-specific-data-agents.md) | `subagents-domain-specific-data-agents` | Subagent 交付模型 | Data Engineering Agent | Research | ✅ |
| 15 | [data-engineering-agent/15-…](./data-engineering-agent/15-what-is-text-to-sql.md) | `what-is-text-to-sql` | Text-to-SQL | Data Engineering Agent | Glossary | ✅ |
| 16 | [data-engineering-agent/16-…](./data-engineering-agent/16-what-is-schema-linking.md) | `what-is-schema-linking` | Schema linking | Data Engineering Agent | Glossary | ✅ |
| 17 | [data-engineering-agent/17-…](./data-engineering-agent/17-rag-data-engineering.md) | `rag-data-engineering` | RAG for data engineering | Data Engineering Agent | Glossary | ✅ |
| 18 | [18-what-is-data-catalog.md](./18-what-is-data-catalog.md) | `what-is-data-catalog` | Data catalog | Glossary | — | ✅ |
| 19 | [19-what-is-data-mesh.md](./19-what-is-data-mesh.md) | `what-is-data-mesh` | Data mesh | Glossary | — | ✅ |
| 20 | [semantic-layer/20-…](./semantic-layer/20-what-is-metric-layer-2026.md) | `what-is-metric-layer` | Metric layer | Semantic Layer | Glossary | ✅ |
| 21 | [semantic-layer/21-…](./semantic-layer/21-what-is-semantic-model-2026.md) | `what-is-semantic-model` | Semantic model | Semantic Layer | Glossary | ✅ |
| 22 | [semantic-layer/22-…](./semantic-layer/22-semantic-layer-vs-ontology-2026.md) | `semantic-layer-vs-ontology` | vs ontology | Semantic Layer | Glossary | ✅ |
| 23 | [data-agent/23-…](./data-agent/23-what-is-data-agent-2026.md) | `what-is-data-agent` | Data agent 父词 Hub | Data Agent | Glossary | ✅ |
| 24 | [osi/24-…](./osi/24-open-semantic-interchange-osi-2026.md) | `open-semantic-interchange-osi` | OSI 标准 Hub | OSI | Research | ✅ |
| 25 | [semantic-layer/25-…](./semantic-layer/25-dbt-semantic-layer-metricflow-2026.md) | `dbt-semantic-layer-metricflow` | dbt MetricFlow | Semantic Layer | Research | ✅ |
| 26 | [semantic-layer/26-…](./semantic-layer/26-cube-dev-agentic-analytics-2026.md) | `cube-agentic-analytics` | Cube.dev | Semantic Layer | Research | ✅ |
| 27 | [semantic-layer/27-…](./semantic-layer/27-gooddata-ai-native-analytics-2026.md) | `what-is-gooddata` | GoodData.AI | Semantic Layer | Research | ✅ |
| 28 | [data-engineering-agent/28-…](./data-engineering-agent/28-ai-native-data-platforms-2026.md) | `ai-native-data-platforms` | AI-native 数据平台 | Data Engineering Agent | Research | ✅ |
| 29 | [data-engineering-agent/29-…](./data-engineering-agent/29-platform-native-data-engineering-agents-compared-2026.md) | `platform-native-data-agents-compared` | Cortex / Genie / BigQuery DEA | Data Engineering Agent | Comparison | ✅ |
| 30 | [30-what-is-lakehouse.md](./30-what-is-lakehouse.md) | `what-is-lakehouse` | Lakehouse | Glossary | — | ✅ |
| 31 | [semantic-layer/31-…](./semantic-layer/31-semantic-layer-tools-list-osi.md) | `semantic-layer-tools-list-osi` | 语义层工具目录 + OSI 状态 | Semantic Layer | ToolsList | ✅ |
| 32 | [data-engineering-agent/32-…](./data-engineering-agent/32-cursor-for-data-engineering.md) | `cursor-for-data-engineering` | Cursor for data engineering | Data Engineering Agent | Product | ✅ |
| 33 | [osi/33-…](./osi/33-what-is-snowflake-osi.md) | `what-is-snowflake-osi` | Snowflake OSI / Ossie | OSI | Glossary | ✅ |
| 34 | [osi/34-…](./osi/34-osi-vs-dbt-metricflow.md) | `osi-vs-dbt-metricflow` | OSI vs MetricFlow | OSI | Glossary | ✅ |
| 35 | [osi/35-…](./osi/35-osi-vs-lookml.md) | `osi-vs-lookml` | OSI vs LookML | OSI | Glossary | ✅ |
| 36 | [osi/36-…](./osi/36-osi-vs-warehouse-native-semantics.md) | `osi-vs-warehouse-native-semantics` | OSI vs warehouse-native | OSI | Glossary | ✅ |
| 37 | [osi/37-…](./osi/37-semantic-vs-syntactic-interoperability.md) | `semantic-vs-syntactic-interoperability` | Semantic vs syntactic | OSI | Glossary | ✅ |
| 38 | [osi/38-…](./osi/38-osi-vs-rdf-owl.md) | `osi-vs-rdf-owl` | OSI vs RDF/OWL | OSI | Glossary | ✅ |
| 39 | [osi/39-…](./osi/39-osi-vs-cube.md) | `osi-vs-cube` | OSI vs Cube | OSI | Glossary | ✅ |
| 40 | [semantic-layer/40-…](./semantic-layer/40-what-is-ontology.md) | `what-is-ontology` | Ontology 定义 Hub | Semantic Layer | Glossary | ✅ |
| 41 | [semantic-layer/41-…](./semantic-layer/41-what-is-timbr.md) | `what-is-timbr` | What Is Timbr | Semantic Layer | Research | ✅ |
| 42 | [semantic-layer/42-…](./semantic-layer/42-what-is-atscale.md) | `what-is-atscale` | What Is AtScale | Semantic Layer | Research | ✅ |
| 43 | [data-agent/43-…](./data-agent/43-what-is-databricks-genie.md) | `what-is-databricks-genie` | Databricks Genie / Genie Agent | Data Agent | Research | ✅ |
| 44 | [data-agent/44-…](./data-agent/44-what-is-cortex-analyst.md) | `what-is-cortex-analyst` | Snowflake Cortex Analyst | Data Agent | Research | ✅ |
| 45 | [data-agent/45-…](./data-agent/45-what-is-claude-data-plugin.md) | `what-is-claude-data-plugin` | Claude Data plugin | Data Agent | Research | ✅ |
| 46 | [features/46-introducing-datus-knowledge.md](./features/46-introducing-datus-knowledge.md) | `introducing-datus-knowledge` | Introducing Datus Knowledge（产品 Hub） | Features | Product | ✅ |
| 47 | [features/47-datus-osi-semantic-adapter.md](./features/47-datus-osi-semantic-adapter.md) | `datus-osi-semantic-adapter` | OSI Semantic Adapter（产品连接） | Features | Product | ✅ |
| 48 | [features/48-introducing-datus-subagents.md](./features/48-introducing-datus-subagents.md) | `introducing-datus-subagents` | Task Subagents（AskMetrics 主例子） | Features | Product | ✅ |

新文章序号：**49**。成稿后请更新本表与 [internal-external-links-checklist.md](./internal-external-links-checklist.md)。

#12（CLI workflow）已合并入 #06。榜单类用 `datus-blog-article` skill（ToolsList）；术语定义 / 概念对比用 `datus-glossary-article`；产品能力用 Features 簇 brief（[features/README.md](./features/README.md)）。

---

## 主题簇结构

### Data Agent（4 篇）

父词 Hub + 仓内 query-agent 标本 + 通用模型侧 plugin。后续类型/场景 spoke（catalog / BI agent）进本目录；语义层竞品与 DE-agent 平台对比不进。

```
                    ┌──────────────────────────────────┐
                    │  23 What Is a Data Agent (Hub)    │
                    │  父词 → 链 01 DEA 子类            │
                    └────────────────┬─────────────────┘
              ┌──────────┼──────────┬──────────┐
              ▼          ▼          ▼          ▼
        43 Genie   44 Cortex   45 Claude    (类型 spoke)
        Agent      Analyst     Data plugin
```

### Data Engineering Agent（18 篇）

围绕品类词 `data engineering agent` 的 hub-spoke。Hub 为 #01。

```
                    ┌──────────────────────────────────┐
                    │  01 What Is a Data Engineering    │
                    │  Agent (Hub)                      │
                    └────────────────┬─────────────────┘
         ┌───────────┬───────────┬───┴────┬───────────┬───────────┐
         ▼           ▼           ▼        ▼           ▼           ▼
       03 叙事     04 榜单     05 开源   06 教程     07/08 vs    09 场景
       10 Context  11 MCP      13 企业   14 Subagent 15–17 术语
       28 AI-native 29 平台原生  32 Cursor
```

### Semantic Layer（11 篇）

Hub 为 #02。Ontology 定义 Hub 为 #40；Cube / Timbr / AtScale 为产品深潜。

```
                    ┌──────────────────────────────────┐
                    │  02 What Is a Semantic Layer      │
                    │  (Hub)                            │
                    └────────────────┬─────────────────┘
         ┌───────────┬───────────┬───┴────┬───────────┐
         ▼           ▼           ▼        ▼           ▼
       20 Metric   21 Model    22 vs     25 dbt      26 Cube
       layer                   ontology  40 Ontology 41 Timbr
                               27 GoodData           42 AtScale
                                                 31 ToolsList
```

### OSI（8 篇）

Hub 为 #24。对比系列（#34–#39）与 Snowflake spoke（#33）全部进本簇。

```
                    ┌──────────────────────────────────┐
                    │  24 Open Semantic Interchange     │
                    │  (Hub)                            │
                    └────────────────┬─────────────────┘
         ┌───────────┬───────────┬───┴────┬───────────┐
         ▼           ▼           ▼        ▼           ▼
       33 Snowflake  34 vs      35 vs    36 vs       37 semantic vs
       OSI           MetricFlow LookML   warehouse   syntactic
                     38 vs RDF/OWL       39 vs Cube
```

### Features（3 篇已发 · Hub #46）

产品能力。Hub 为 Introducing Datus Knowledge。`#48` 是任务型 worker，不搬 `#14` 领域交付。规则见 [features/README.md](./features/README.md)。

```
                    ┌──────────────────────────────────┐
                    │  46 Introducing Datus Knowledge   │
                    │  (Hub)                            │
                    └────────────────┬─────────────────┘
         ┌───────────┬───────────┬───┴────┐
         ▼           ▼           ▼        ▼
       47 OSI        48 Task     /init +   Dashboard
       adapter       Subagents   build-kb  Copilot
       （已发）       （已发）    （计划）   （计划）
```

### 根目录（3 篇）

基础设施 Glossary，暂不归入三大主题：#18 Data catalog、#19 Data mesh、#30 Lakehouse。

---

## 部署

将 `blog/` 目录配置为内容源，设置 `slug` → `/blog/{slug}` URL 映射。主题子目录**不**进入 URL。导入 CMS 时可排除 `README.md`、`internal-external-links-checklist.md`。

## 关联文档

- [datus.md](../datus.md) — 产品概览
- [datus-keywords.md](../datus-keywords.md) — 关键词映射
- [internal-external-links-checklist.md](./internal-external-links-checklist.md) — 文章分类与内链
- [../skills/datus-blog-article/SKILL.md](../skills/datus-blog-article/SKILL.md) — ToolsList
- [../skills/datus-glossary-article/SKILL.md](../skills/datus-glossary-article/SKILL.md) — Glossary
- [features/README.md](./features/README.md) — 产品能力选题
- [../docs-crawl/README.md](../docs-crawl/README.md) — docs 摘录
