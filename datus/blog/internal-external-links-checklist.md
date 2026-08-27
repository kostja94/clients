# Datus Blog 分类与内链

公开 URL：`/blog/{slug}`。主题文件夹只用于本地分簇，不进入公开路径。#12 为空号（已并入 #06）。

## 内链位置规则

| 区域 | 做什么 | 上限 |
|------|--------|------|
| Lede（第一个 `##` 前） | 默认 0；必要时只链本簇 Hub 或上位词 | ≤1 |
| TL;DR | 最多 1 条 Hub / 上位概念 | 与 lede 合计 ≤2 |
| 正文各 `##` | 术语第一次被解释时链 canonical | 每节 ≤2 unique |
| Conclusion | Hub、1 个兄弟 spoke、必要时 1 条跨簇 | ≤3 |
| FAQ | 问题本身需要那篇文时才链；不引入新 unique | 已在正文出现过的可以再点 |

同一 slug 正文优先只链一次；Conclusion 允许作为收束再链 2–3 条 next-read。

| 角色 | unique 目标 |
|------|-------------|
| 簇 Hub | 4–6，以本簇 spoke 为主 |
| Spoke Glossary / Research | 3–5 |
| Comparison / ToolsList | 4–6（含被比较对象） |
| Product | 3–4 |

OSI 对比文默认不链 DEA 定义；仅 `#36`（warehouse-native / agent grounding）保留。

当前图：48 篇；无站内死链；无零入链稿。先前孤立的 `#13` / `#27` / `#32` 已分别由 `#01`、`#31`、`#07` 接入。Features Hub `#46` 由 `#10` 接入；`#47` 由 `#24` / `#46` 接入；`#48` 由 `#14` / `#46` 接入。

---

## 分类结构

`category` = 主题簇；`secondaryCategory` = 体裁。根目录散篇只有 `category: Glossary`。

| 主题簇 | 目录 | `category` | Hub slug | 篇数 |
|--------|------|------------|----------|:---:|
| Data Agent | `data-agent/` | `Data Agent` | `what-is-data-agent` | 4 |
| Data Engineering Agent | `data-engineering-agent/` | `Data Engineering Agent` | `what-is-data-engineering-agent` | 18 |
| Semantic Layer | `semantic-layer/` | `Semantic Layer` | `what-is-semantic-layer` | 11 |
| OSI | `osi/` | `OSI` | `open-semantic-interchange-osi` | 8 |
| Features | `features/` | `Features` | `introducing-datus-knowledge` | 3 |
| 未归簇 | `blog/` 根 | `Glossary` | — | 3 |

**体裁**：`Glossary` | `Research` | `Comparison` | `ToolsList` | `Product`

```
Data Agent
  23 Hub ── 43 Genie Agent / 44 Cortex Analyst / 45 Claude Data plugin

Data Engineering Agent
  01 Hub ── 03 叙事 / 04 榜单 / 05 开源 / 06 教程 / 07·08 vs / 09 场景
            10 Context / 11 MCP / 13 企业 / 14 Subagent / 15–17 术语
            28 AI-native / 29 平台原生 DEA / 32 Cursor

Semantic Layer
  02 Hub ── 20 Metric layer / 21 Semantic model / 22 vs ontology / 40 Ontology
            25 dbt / 26 Cube / 27 GoodData / 41 Timbr / 42 AtScale / 31 ToolsList

OSI
  24 Hub ── 33 Snowflake OSI / 34 vs MetricFlow / 35 vs LookML
            36 vs warehouse-native / 37 semantic vs syntactic
            38 vs RDF/OWL / 39 vs Cube

Features
  46 Hub Introducing Datus Knowledge ── 47 OSI adapter / 48 Task Subagents
                                      /init+build-kb / Dashboard Copilot（计划）

根目录
  18 Data catalog / 19 Data mesh / 30 Lakehouse
```

---

## 内链一览

「互链」为正文 `/blog/{slug}` 去重后的目标。

### Data Agent

| # | 文章 | slug | 体裁 | 互链 |
|---|------|------|------|------|
| 23 | What Is a Data Agent | `what-is-data-agent` | Glossary | `what-is-databricks-genie`, `what-is-cortex-analyst`, `what-is-claude-data-plugin`, `what-is-semantic-layer`, `what-is-data-engineering-agent`, `contextual-data-engineering` |
| 43 | What Is Databricks Genie | `what-is-databricks-genie` | Research | `what-is-data-agent`, `platform-native-data-agents-compared`, `what-is-cortex-analyst`, `what-is-claude-data-plugin`, `what-is-data-engineering-agent` |
| 44 | What Is Cortex Analyst | `what-is-cortex-analyst` | Research | `what-is-data-agent`, `what-is-snowflake-osi`, `what-is-claude-data-plugin`, `what-is-databricks-genie`, `what-is-data-engineering-agent` |
| 45 | What Is the Claude Data Plugin | `what-is-claude-data-plugin` | Research | `what-is-data-agent`, `data-engineering-agent-vs-claude-code`, `what-is-databricks-genie`, `what-is-cortex-analyst`, `what-is-data-engineering-agent` |

### Data Engineering Agent

| # | 文章 | slug | 体裁 | 互链 |
|---|------|------|------|------|
| 01 | What Is a Data Engineering Agent | `what-is-data-engineering-agent` | Research | `what-is-semantic-layer`, `contextual-data-engineering`, `best-data-engineering-agents`, `enterprise-data-engineering-agent` |
| 03 | Contextual Data Engineering | `contextual-data-engineering` | Research | `what-is-semantic-layer`, `what-is-data-engineering-agent`, `context-engine-data-engineering-agent-accuracy` |
| 04 | Best Data Engineering Agents | `best-data-engineering-agents` | ToolsList | `what-is-data-engineering-agent`, `contextual-data-engineering`, `open-source-data-engineering-agents`, `platform-native-data-agents-compared` |
| 05 | Open Source Data Engineering Agents | `open-source-data-engineering-agents` | Comparison | `what-is-data-engineering-agent`, `contextual-data-engineering`, `best-data-engineering-agents`, `build-your-first-data-engineering-agent` |
| 06 | Build Your First DE Agent | `build-your-first-data-engineering-agent` | Product | `what-is-data-engineering-agent`, `contextual-data-engineering`, `best-data-engineering-agents`, `open-source-data-engineering-agents` |
| 07 | DE Agent vs Claude Code | `data-engineering-agent-vs-claude-code` | Comparison | `what-is-data-engineering-agent`, `contextual-data-engineering`, `cursor-for-data-engineering` |
| 08 | DE Agent vs SQL Copilot | `data-engineering-agent-vs-sql-copilot` | Comparison | `contextual-data-engineering`, `best-data-engineering-agents`, `what-is-data-engineering-agent` |
| 09 | One-Person Data Team | `one-person-data-team` | Product | `what-is-data-engineering-agent`, `contextual-data-engineering`, `subagents-domain-specific-data-agents`, `build-your-first-data-engineering-agent` |
| 10 | Context Engine Accuracy | `context-engine-data-engineering-agent-accuracy` | Research | `what-is-data-engineering-agent`, `what-is-semantic-layer`, `best-data-engineering-agents`, `contextual-data-engineering`, `introducing-datus-knowledge` |
| 11 | MCP and Data Engineering | `mcp-data-engineering` | Research | `what-is-data-engineering-agent`, `best-data-engineering-agents`, `contextual-data-engineering` |
| 13 | Enterprise DE Agent | `enterprise-data-engineering-agent` | Research | `contextual-data-engineering`, `mcp-data-engineering`, `open-source-data-engineering-agents`, `what-is-data-engineering-agent` |
| 14 | Subagents | `subagents-domain-specific-data-agents` | Research | `what-is-data-engineering-agent`, `one-person-data-team`, `contextual-data-engineering`, `enterprise-data-engineering-agent`, `introducing-datus-subagents` |
| 15 | What Is Text-to-SQL | `what-is-text-to-sql` | Glossary | `what-is-schema-linking`, `what-is-data-engineering-agent`, `what-is-semantic-layer`, `rag-data-engineering`, `contextual-data-engineering` |
| 16 | What Is Schema Linking | `what-is-schema-linking` | Glossary | `what-is-text-to-sql`, `rag-data-engineering`, `what-is-semantic-layer`, `what-is-data-catalog`, `what-is-data-engineering-agent` |
| 17 | RAG for Data Engineering | `rag-data-engineering` | Glossary | `what-is-schema-linking`, `contextual-data-engineering`, `what-is-semantic-layer`, `what-is-text-to-sql`, `what-is-data-engineering-agent` |
| 28 | AI-Native Data Platforms | `ai-native-data-platforms` | Research | `what-is-metric-layer`, `what-is-semantic-model`, `what-is-data-engineering-agent` |
| 29 | Platform-Native DE Agents Compared | `platform-native-data-agents-compared` | Comparison | `what-is-databricks-genie`, `what-is-cortex-analyst`, `what-is-data-engineering-agent`, `open-source-data-engineering-agents`, `ai-native-data-platforms` |
| 32 | Cursor for Data Engineering | `cursor-for-data-engineering` | Product | `what-is-data-engineering-agent`, `contextual-data-engineering`, `data-engineering-agent-vs-sql-copilot`, `one-person-data-team` |

### Semantic Layer

| # | 文章 | slug | 体裁 | 互链 |
|---|------|------|------|------|
| 02 | What Is a Semantic Layer | `what-is-semantic-layer` | Glossary | `what-is-data-engineering-agent`, `what-is-semantic-model`, `what-is-ontology`, `open-semantic-interchange-osi`, `what-is-metric-layer` |
| 20 | What Is a Metric Layer | `what-is-metric-layer` | Glossary | `what-is-semantic-layer`, `what-is-semantic-model`, `what-is-data-engineering-agent`, `dbt-semantic-layer-metricflow` |
| 21 | What Is a Semantic Model | `what-is-semantic-model` | Glossary | `what-is-metric-layer`, `open-semantic-interchange-osi`, `what-is-semantic-layer` |
| 22 | Semantic Layer vs Ontology | `semantic-layer-vs-ontology` | Glossary | `what-is-semantic-model`, `what-is-semantic-layer`, `what-is-ontology` |
| 25 | dbt Semantic Layer & MetricFlow | `dbt-semantic-layer-metricflow` | Research | `what-is-semantic-layer`, `open-semantic-interchange-osi`, `cube-agentic-analytics`, `what-is-metric-layer` |
| 26 | Cube.dev Agentic Analytics | `cube-agentic-analytics` | Research | `what-is-data-agent`, `open-semantic-interchange-osi`, `what-is-semantic-layer`, `osi-vs-cube` |
| 27 | What Is GoodData | `what-is-gooddata` | Research | `what-is-semantic-model`, `open-semantic-interchange-osi`, `what-is-semantic-layer` |
| 31 | Semantic Layer Tools List | `semantic-layer-tools-list-osi` | ToolsList | `what-is-semantic-layer`, `open-semantic-interchange-osi`, `what-is-gooddata`, `what-is-data-engineering-agent` |
| 40 | What Is an Ontology | `what-is-ontology` | Glossary | `what-is-semantic-layer`, `semantic-layer-vs-ontology`, `osi-vs-rdf-owl`, `what-is-timbr`, `what-is-atscale` |
| 41 | What Is Timbr | `what-is-timbr` | Research | `what-is-semantic-layer`, `what-is-ontology`, `semantic-layer-vs-ontology`, `what-is-data-engineering-agent`, `cube-agentic-analytics` |
| 42 | What Is AtScale | `what-is-atscale` | Research | `what-is-semantic-layer`, `semantic-layer-tools-list-osi`, `cube-agentic-analytics`, `what-is-timbr` |

### OSI

| # | 文章 | slug | 体裁 | 互链 |
|---|------|------|------|------|
| 24 | Open Semantic Interchange | `open-semantic-interchange-osi` | Research | `what-is-semantic-model`, `what-is-semantic-layer`, `what-is-snowflake-osi`, `osi-vs-dbt-metricflow`, `semantic-layer-tools-list-osi`, `datus-osi-semantic-adapter` |
| 33 | What Is Snowflake OSI | `what-is-snowflake-osi` | Glossary | `what-is-semantic-model`, `open-semantic-interchange-osi`, `what-is-semantic-layer`, `osi-vs-warehouse-native-semantics` |
| 34 | OSI vs dbt MetricFlow | `osi-vs-dbt-metricflow` | Glossary | `what-is-semantic-layer`, `open-semantic-interchange-osi`, `dbt-semantic-layer-metricflow`, `what-is-metric-layer`, `semantic-layer-tools-list-osi`, `osi-vs-lookml` |
| 35 | OSI vs LookML | `osi-vs-lookml` | Glossary | `what-is-semantic-layer`, `open-semantic-interchange-osi`, `semantic-layer-tools-list-osi`, `osi-vs-dbt-metricflow`, `semantic-vs-syntactic-interoperability` |
| 36 | OSI vs Warehouse-Native Semantics | `osi-vs-warehouse-native-semantics` | Glossary | `what-is-semantic-layer`, `open-semantic-interchange-osi`, `what-is-snowflake-osi`, `semantic-layer-tools-list-osi`, `osi-vs-dbt-metricflow`, `what-is-data-engineering-agent` |
| 37 | Semantic vs Syntactic Interoperability | `semantic-vs-syntactic-interoperability` | Glossary | `what-is-semantic-layer`, `open-semantic-interchange-osi`, `osi-vs-rdf-owl`, `what-is-semantic-model` |
| 38 | OSI vs RDF/OWL | `osi-vs-rdf-owl` | Glossary | `semantic-layer-vs-ontology`, `open-semantic-interchange-osi`, `what-is-semantic-layer`, `what-is-semantic-model` |
| 39 | OSI vs Cube | `osi-vs-cube` | Glossary | `open-semantic-interchange-osi`, `cube-agentic-analytics`, `what-is-semantic-layer`, `semantic-layer-tools-list-osi` |

### Features

| # | 文章 | slug | 体裁 | 互链 |
|---|------|------|------|------|
| 46 | Introducing Datus Knowledge | `introducing-datus-knowledge` | Product | `what-is-data-engineering-agent`, `what-is-semantic-model`, `what-is-data-catalog`, `contextual-data-engineering`, `datus-osi-semantic-adapter`, `introducing-datus-subagents` |
| 47 | Datus OSI Semantic Adapter | `datus-osi-semantic-adapter` | Product | `open-semantic-interchange-osi`, `osi-vs-dbt-metricflow`, `introducing-datus-knowledge`, `introducing-datus-subagents` |
| 48 | Introducing Datus Subagents | `introducing-datus-subagents` | Product | `what-is-data-engineering-agent`, `subagents-domain-specific-data-agents`, `introducing-datus-knowledge`, `datus-osi-semantic-adapter` |

### 根目录（未归簇）

| # | 文章 | slug | 体裁 | 互链 |
|---|------|------|------|------|
| 18 | What Is a Data Catalog | `what-is-data-catalog` | Glossary | `what-is-semantic-layer`, `contextual-data-engineering`, `rag-data-engineering`, `what-is-schema-linking`, `what-is-lakehouse` |
| 19 | What Is Data Mesh | `what-is-data-mesh` | Glossary | `subagents-domain-specific-data-agents`, `contextual-data-engineering`, `what-is-data-catalog`, `what-is-lakehouse` |
| 30 | What Is a Lakehouse | `what-is-lakehouse` | Glossary | `what-is-data-catalog`, `what-is-semantic-layer`, `what-is-data-engineering-agent`, `what-is-schema-linking`, `what-is-data-mesh` |
