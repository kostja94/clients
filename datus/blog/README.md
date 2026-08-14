# Datus Blog

Markdown 格式文章，可直接导入支持 Markdown 的 CMS（Hugo、Jekyll、Next.js MDX、Astro、Lovable 等）。

**线上 URL 模式**：`https://datus.ai/blog/{slug}`（Lovable 预览：`datus.lovable.app/blog/{slug}`）

## 文件结构

- `*.md`：单篇文章，含 YAML frontmatter
- 每篇包含：`title`、`description`、`slug`、`date`、`author`、`category`、`keywords`、`related`
- **`category`** 取值：`Glossary`（术语定义型）| `Data Engineering Agent`（主簇文章）| `Semantic Layer`（语义层工具目录/选型榜单）| `Comparison`（个别对比文）| `Case Study`（案例，待写）
- **本目录文档**：`README.md`（本说明）、`internal-external-links-checklist.md`（内链外链规范）

## Frontmatter 示例

```yaml
---
title: "What Is a Data Engineering Agent? Definition, Examples & a 2026 Comparison"
description: "Meta description..."
slug: "what-is-data-engineering-agent"   # 不含年份，常青 URL
date: 2026-05-28
author: "Kostja"
category: "Data Engineering Agent"
image: "/blog/images/what-is-data-engineering-agent-2026.jpg"
---
```

## 正文规范

- 主节 H2 使用英文编号：`## 1.` … `## 7.`
- `## Conclusion`、`## Frequently asked questions` **不加**序号
- 站外链接使用 HTML：`<a href="URL" rel="nofollow noopener">锚文本</a>`
- 站内 Blog 互链：`/blog/{slug}`；Glossary：`/glossary`（**暂不**链向 `/agent`、`/features/*` 等未上线页面，见 [internal-external-links-checklist.md](./internal-external-links-checklist.md)）

## 文章列表

| # | 文件 | slug | 主题 | category | 状态 |
|---|------|------|------|----------|------|
| 1 | [01-what-is-data-engineering-agent-2026.md](./01-what-is-data-engineering-agent-2026.md) | `what-is-data-engineering-agent` | 品类定义 + 四类对比 | Data Engineering Agent | ✅ |
| 2 | [02-what-is-semantic-layer-2026.md](./02-what-is-semantic-layer-2026.md) | `what-is-semantic-layer` | Semantic layer 术语定义 | Glossary | ✅ |
| 3 | [03-contextual-data-engineering-2026.md](./03-contextual-data-engineering-2026.md) | `contextual-data-engineering` | Contextual Data Engineering 品类定义 | Data Engineering Agent | ✅ |
| 4 | [04-best-data-engineering-agents-2026.md](./04-best-data-engineering-agents-2026.md) | `best-data-engineering-agents` | 七大 Agent 横向对比 | Data Engineering Agent | ✅ |
| 5 | [05-open-source-data-engineering-agents.md](./05-open-source-data-engineering-agents.md) | `open-source-data-engineering-agents` | 开源 Agent 三选一 | Data Engineering Agent | ✅ |
| 6 | [06-build-your-first-data-engineering-agent.md](./06-build-your-first-data-engineering-agent.md) | `build-your-first-data-engineering-agent` | 15 分钟教程 + 日常 CLI 工作流 | Data Engineering Agent | ✅ |
| 7 | [07-data-engineering-agent-vs-claude-code.md](./07-data-engineering-agent-vs-claude-code.md) | `data-engineering-agent-vs-claude-code` | vs Claude Code 互补叙事 | Data Engineering Agent | ❌ 文件缺失 |
| 8 | [08-data-engineering-agent-vs-sql-copilot.md](./08-data-engineering-agent-vs-sql-copilot.md) | `data-engineering-agent-vs-sql-copilot` | Agent vs Copilot 品类区分 | Data Engineering Agent | ✅ |
| 9 | [09-one-person-data-team.md](./09-one-person-data-team.md) | `one-person-data-team` | 一人数据团队提效场景 | Data Engineering Agent | ✅ |
| 10 | [10-context-engine-data-engineering-agent-accuracy.md](./10-context-engine-data-engineering-agent-accuracy.md) | `context-engine-data-engineering-agent-accuracy` | Context Engine 如何提升准确率 | Data Engineering Agent | ✅ |
| 11 | [11-mcp-data-engineering.md](./11-mcp-data-engineering.md) | `mcp-data-engineering` | MCP 协议在数据工程中的应用 | Data Engineering Agent | ✅ |
| 12 | [13-enterprise-data-engineering-agent.md](./13-enterprise-data-engineering-agent.md) | `enterprise-data-engineering-agent` | 企业级 Agent 六大需求 | Data Engineering Agent | ✅ |
| 13 | [14-subagents-domain-specific-data-agents.md](./14-subagents-domain-specific-data-agents.md) | `subagents-domain-specific-data-agents` | Subagent 交付模型深度解析 | Data Engineering Agent | ✅ |
| 14 | [15-what-is-text-to-sql.md](./15-what-is-text-to-sql.md) | `what-is-text-to-sql` | Text-to-SQL / NL2SQL 术语定义 | Glossary | ✅ |
| 15 | [16-what-is-schema-linking.md](./16-what-is-schema-linking.md) | `what-is-schema-linking` | Schema linking 术语定义 | Glossary | ✅ |
| 16 | [17-rag-data-engineering.md](./17-rag-data-engineering.md) | `rag-data-engineering` | RAG 在数据工程中的应用 | Glossary | ✅ |
| 17 | [18-what-is-data-catalog.md](./18-what-is-data-catalog.md) | `what-is-data-catalog` | Data catalog 术语定义 | Glossary | ✅ |
| 18 | [19-what-is-data-mesh.md](./19-what-is-data-mesh.md) | `what-is-data-mesh` | Data mesh 术语定义 | Glossary | ✅ |
| 19 | [20-what-is-metric-layer-2026.md](./20-what-is-metric-layer-2026.md) | `what-is-metric-layer` | Metric layer 术语定义 + MetricFlow 详解 | Glossary | ✅ |
| 20 | [21-what-is-semantic-model-2026.md](./21-what-is-semantic-model-2026.md) | `what-is-semantic-model` | Semantic model 术语定义 + semantic view 对比 | Glossary | ✅ |
| 21 | [22-semantic-layer-vs-ontology-2026.md](./22-semantic-layer-vs-ontology-2026.md) | `semantic-layer-vs-ontology` | Semantic layer vs ontology 概念区分 | Glossary | ✅ |
| 22 | [23-what-is-data-agent-2026.md](./23-what-is-data-agent-2026.md) | `what-is-data-agent` | Data agent 六大类型 + vs data engineering agent | Glossary | ✅ |
| 23 | [24-open-semantic-interchange-osi-2026.md](./24-open-semantic-interchange-osi-2026.md) | `open-semantic-interchange-osi` | OSI 标准解读 + 30+ 参与者分析 | Data Engineering Agent | ✅ |
| 24 | [25-dbt-semantic-layer-metricflow-2026.md](./25-dbt-semantic-layer-metricflow-2026.md) | `dbt-semantic-layer-metricflow` | dbt Semantic Layer & MetricFlow 完整指南 | Data Engineering Agent | ✅ |
| 25 | [26-cube-dev-agentic-analytics-2026.md](./26-cube-dev-agentic-analytics-2026.md) | `cube-agentic-analytics` | Cube.dev 三阶段演化 + D3 Agentic Analytics | Data Engineering Agent | ✅ |
| 26 | [27-gooddata-ai-native-analytics-2026.md](./27-gooddata-ai-native-analytics-2026.md) | `what-is-gooddata` | GoodData 17 年→GoodData.AI 案例研究 | Data Engineering Agent | ✅ |
| 27 | [28-ai-native-data-platforms-2026.md](./28-ai-native-data-platforms-2026.md) | `ai-native-data-platforms` | AI-native vs AI-augmented 数据平台定义 | Data Engineering Agent | ✅ |
| 28 | [29-platform-native-data-engineering-agents-compared-2026.md](./29-platform-native-data-engineering-agents-compared-2026.md) | `platform-native-data-agents-compared` | Cortex Code vs Genie Code vs BigQuery DEA 对比 | Data Engineering Agent | ✅ |
| 29 | [30-what-is-lakehouse.md](./30-what-is-lakehouse.md) | `what-is-lakehouse` | Lakehouse 术语定义 + 开放表格式 | Glossary | ✅ |
| 30 | [31-semantic-layer-tools-list-osi.md](./31-semantic-layer-tools-list-osi.md) | `semantic-layer-tools-list-osi` | 语义层工具目录 + OSI 支持状态 | Semantic Layer | ✅ |

> #12（CLI workflow）已合并入 #06 §What your daily workflow looks like。完整策略见 [keyword-cluster-data-engineering-agent.md](./keyword-cluster-data-engineering-agent.md)。**已落地含 #31 ToolsList**（缺 #07）；勿链向 slug `data-engineering-agent-vs-claude-code`，待稿发布后再补链。榜单类用 `datus-blog-article` skill（ToolsList），勿用 glossary skill。

## 部署

将 `blog/` 目录配置为内容源，设置 `slug` → `/blog/{slug}` URL 映射。图片路径 `image` 需对应实际 CDN 或静态资源路径。（导入 CMS 时可排除 `README.md`、`internal-external-links-checklist.md`。）

## 关联文档

- [datus.md](../datus.md) — 产品概览
- [datus-growth-strategy.md](../datus-growth-strategy.md) — 内容策略
- [datus-keywords.md](../datus-keywords.md) — 关键词映射
- [internal-external-links-checklist.md](./internal-external-links-checklist.md) — 内链外链规范
