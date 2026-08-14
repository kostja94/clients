# Datus — 站点结构

> **本文档职责**：三域 URL 层级、信息架构、线上页面清单（datus.ai / docs.datus.ai / studio.datus.ai）。  
> **引用**：[datus.md](./datus.md) 概览 | [datus-growth-strategy.md](./datus-growth-strategy.md) 增长策略 | [datus-i18n-spec.md](./datus-i18n-spec.md) 主站 `/zh` i18n

**最近更新**：2026-08-04（中文站条目对齐 i18n 规范：非 Blog 营销页 `/zh` 镜像）

**数据来源**：

| 域名 | Sitemap | lastmod |
|------|---------|---------|
| datus.ai | [sitemap index](https://datus.ai/sitemap.xml) → [sitemap-pages.xml](https://datus.ai/sitemap-pages.xml) + [blog/sitemap.xml](https://datus.ai/blog/sitemap.xml) | 2026-06-11 |
| docs.datus.ai | [sitemap.xml](https://docs.datus.ai/sitemap.xml) | 2026-04-13 |
| studio.datus.ai | [sitemap.xml](https://studio.datus.ai/sitemap.xml) | 无 lastmod |

---

## URL 架构（站点约定）

datus.ai 采用 **两层 URL 模型**：

| 层级 | 路径模式 | 用途 | 示例 |
|------|----------|------|------|
| **顶层页** | `/`、`/products/*`、`/pricing/`、`/integrations/`、`/faq/` 等 | 产品、定价、集成等营销/功能落地页 | `/products/cli/` |
| **聚合索引** | `/glossary/`、`/blog/` | 列表/索引页，**不是**单篇内容的 canonical URL | `/glossary/` → 链向各术语文 |
| **独立内容 URL** | **`/blog/{slug}/`** | 所有可独立访问的长文：Glossary 术语、DE Agent 主簇、对比文、教程、发布说明、专题 hub | `/blog/what-is-semantic-layer/` |

**关键约定**：

- **独立 URL 一律挂在 `/blog` 下**——不存在 `/glossary/{term}`、`/agent/{slug}` 等内容型子路径。
- **`/glossary/` 仅为聚合页**：线上 **47 词**（7 类）为页内定义；已发布长文的 canonical 地址是 `/blog/what-is-*`、`/blog/*-vs-*` 等 slug。截至 2026-06-24，聚合页仅 **Lakehouse** 有「Read the full guide →」深链至 `/blog/what-is-lakehouse/`。
- **Blog 内链规范**：正文互链用 `/blog/{slug}`；链向 Glossary 索引用 `/glossary`（可选，术语首次出现更常见的是直接链 `/blog/{term-slug}`）。
- **Sitemap 分工**：顶层页 → `sitemap-pages.xml`（9 URL）；全部独立内容 → `blog/sitemap.xml`（57 URL）。

```
datus.ai/
├── /                          首页
├── /products/*                产品页（4）
├── /pricing/  /integrations/  /faq/
├── /glossary/                 术语聚合索引（→ 指向 /blog/{slug}）
└── /blog/
    ├── /                      文章列表
    └── /{slug}/               独立内容 canonical（Glossary + 主簇 + 早期稿 + hub）
        └── /{hub}/{slug}/     例外：少数专题嵌套（如 data-engineering-agent/…）
```


## 一、域名体系

| 域名 | 定位 | 说明 |
|------|------|------|
| [datus.ai](https://datus.ai/) | 品牌官网 | 产品主页、Blog、Glossary、Pricing |
| [docs.datus.ai](https://docs.datus.ai/) | 文档站 | 产品文档（56 EN + 56 `/zh/` 镜像；**不在** datus.ai sitemap 内） |
| [studio.datus.ai](https://studio.datus.ai/overview) | 云端产品 | Studio 营销页 + 登录后 Web App（独立 sitemap） |
| [github.com/Datus-ai/Datus-agent](https://github.com/Datus-ai/Datus-agent) | 开源仓库 | 代码 + Issues + Discussions |
| 微信公众号「数据杂货铺」 | 中文内容 | 创始人博客 + 中文社区运营 |

*主站中文：非 Blog 营销路径规划 `/zh` + 同 path 镜像（规范见 [datus-i18n-spec.md](./datus-i18n-spec.md)；**不含** `/blog/**`，**不管** docs）。docs.datus.ai 自有 `/zh/*`。公众号仍可承担额外中文分发。*

---

## 二、导航结构（线上）

根据 sitemap 与页面路径推断的主导航：

| 导航项 | 目标 | 状态 |
|--------|------|------|
| **Home** | `/` | ✅ 已上线 |
| **Products** | `/products/*` | ✅ 已上线（CLI / VS Code / Studio / Enterprise） |
| **Integrations** | `/integrations/` | ✅ 已上线 |
| **Pricing** | `/pricing/` | ✅ 已上线 |
| **Glossary** | `/glossary/` | ✅ 已上线（**聚合索引**；术语正文在 `/blog/{slug}/`） |
| **FAQ** | `/faq/` | ✅ 已上线 |
| **Blog** | `/blog/` + `/blog/{slug}/` | ✅ 已上线（56 篇独立内容 URL，含 Glossary 与主簇） |
| **Documentation** | 外链 `docs.datus.ai` | ✅ 已确认 |
| **GitHub** | 外链 `github.com/Datus-ai/Datus-agent` | ✅ 已确认 |
| **Get started / Login / Sign Up** | `studio.datus.ai/overview` → `/login` / `/register` | ✅ 已确认（**不在** datus.ai sitemap） |
| **Slack Community** | 外链 Slack invite | ✅ 已确认（页脚 / Blog） |

---

## 三、线上 URL 清单（sitemap）

| 域名 | Sitemap URL 数 | 说明 |
|------|:---:|------|
| datus.ai | **70+** | 9 顶层 + 60+ blog（§3.1–3.2） |
| docs.datus.ai | **112** | 56 EN + 56 `/zh/`（§3.3） |
| studio.datus.ai | **2**（sitemap）+ **5**（路由探测） | 公开 2 + 认证路由（§3.4） |

### 3.1 产品与其他页面（9 页）

| 路径 | 完整 URL | lastmod | 说明 |
|------|----------|---------|------|
| `/` | https://datus.ai/ | 2026-06-11 | 品牌首页 |
| `/products/cli/` | https://datus.ai/products/cli/ | 2026-06-11 | Datus CLI |
| `/products/vscode/` | https://datus.ai/products/vscode/ | 2026-06-11 | VS Code 扩展 |
| `/products/studio/` | https://datus.ai/products/studio/ | 2026-06-11 | Datus Studio（云端） |
| `/products/enterprise/` | https://datus.ai/products/enterprise/ | 2026-06-11 | Enterprise 版 |
| `/integrations/` | https://datus.ai/integrations/ | 2026-06-11 | 集成与连接器 |
| `/pricing/` | https://datus.ai/pricing/ | 2026-06-11 | 定价页 |
| `/glossary/` | https://datus.ai/glossary/ | 2026-06-11 | 术语表**聚合索引**（单篇术语 → `/blog/{slug}/`） |
| `/faq/` | https://datus.ai/faq/ | 2026-06-11 | 常见问题 |

> **路径变更说明**：策略文档中曾规划 `/features/*`，线上实际为 **`/products/*`**。内链与 SEO 目标页以 sitemap 为准。

### 3.2 Blog — 全部独立内容 URL（57 个）

`blog/sitemap.xml` 收录 **站内所有独立内容页**：1 个列表索引 + **56** 个内容 URL（Glossary 术语、DE Agent 主簇、早期内容、专题 hub 均在此，**不**另设 `/glossary/{term}` 路径）。

#### Blog 索引

| 路径 | 完整 URL | lastmod |
|------|----------|---------|
| `/blog/` | https://datus.ai/blog/ | 2026-06-11 |

#### Blog 文章与专题页

| slug / 路径 | 完整 URL | lastmod | 备注 |
|-------------|----------|---------|------|
| `welcome` | https://datus.ai/blog/welcome/ | 2026-02-26 | 站点欢迎文 |
| `meet_datus` | https://datus.ai/blog/meet_datus/ | 2026-02-26 | 创始人开源宣言 |
| `what-is-data-engineering-agent` | https://datus.ai/blog/what-is-data-engineering-agent/ | 2026-03-02 | 早期品类文 |
| `data-engineering-agent-architecture` | https://datus.ai/blog/data-engineering-agent-architecture/ | 2026-03-02 | 架构 |
| `data-engineering-agent-use-cases` | https://datus.ai/blog/data-engineering-agent-use-cases/ | 2026-03-02 | 用例 |
| `agentic-data-stack` | https://datus.ai/blog/agentic-data-stack/ | 2026-03-12 | 早期内容 |
| `agentic-data-engineering-vs-traditional-data-engineering` | https://datus.ai/blog/agentic-data-engineering-vs-traditional-data-engineering/ | 2026-03-16 | 早期内容 |
| `agentic-etl-what-changes-beyond-traditional-etl` | https://datus.ai/blog/agentic-etl-what-changes-beyond-traditional-etl/ | 2026-03-16 | 早期内容 |
| `ai-data-pipeline-automation-use-cases-architecture-and-tradeoffs` | https://datus.ai/blog/ai-data-pipeline-automation-use-cases-architecture-and-tradeoffs/ | 2026-03-16 | 早期内容 |
| `how-mcp-changes-data-workflow-automation` | https://datus.ai/blog/how-mcp-changes-data-workflow-automation/ | 2026-03-16 | 早期内容 |
| `how-structured-context-improves-ai-agent-output` | https://datus.ai/blog/how-structured-context-improves-ai-agent-output/ | 2026-03-16 | 早期内容 |
| `semantic-modeling-for-agentic-analytics-workflows` | https://datus.ai/blog/semantic-modeling-for-agentic-analytics-workflows/ | 2026-03-16 | 早期内容 |
| `the-operating-model-of-an-agentic-data-team` | https://datus.ai/blog/the-operating-model-of-an-agentic-data-team/ | 2026-03-16 | 早期内容 |
| `using-mcp-extensions-in-data-engineering-workflows` | https://datus.ai/blog/using-mcp-extensions-in-data-engineering-workflows/ | 2026-03-16 | 早期内容 |
| `what-autonomous-data-engineering-actually-looks-like-in-practice` | https://datus.ai/blog/what-autonomous-data-engineering-actually-looks-like-in-practice/ | 2026-03-16 | 早期内容 |
| `why-ai-agents-need-semantic-context-to-work-reliably` | https://datus.ai/blog/why-ai-agents-need-semantic-context-to-work-reliably/ | 2026-03-16 | 早期内容 |
| `why-data-engineering-needs-agents-not-just-copilots` | https://datus.ai/blog/why-data-engineering-needs-agents-not-just-copilots/ | 2026-03-16 | 早期内容 |
| `why-reliable-data-agents-need-more-than-good-prompts` | https://datus.ai/blog/why-reliable-data-agents-need-more-than-good-prompts/ | 2026-03-16 | 早期内容 |
| `datus-0-2-6-release-equipping-the-agent-with-a-brain` | https://datus.ai/blog/datus-0-2-6-release-equipping-the-agent-with-a-brain/ | 2026-03-20 | 版本发布 |
| `datus-storage-layer` | https://datus.ai/blog/datus-storage-layer/ | 2026-03-25 | 产品深潜 |
| `meet-the-general-chat-agent` | https://datus.ai/blog/meet-the-general-chat-agent/ | 2026-03-25 | 产品深潜 |
| `beyond-sql-how-datus-integrates-with-your-entire-data-toolchain` | https://datus.ai/blog/beyond-sql-how-datus-integrates-with-your-entire-data-toolchain/ | 2026-04-02 | 产品深潜 |
| `make-data-agents-truly-usable-ask-explore-and-control-with-confidence` | https://datus.ai/blog/make-data-agents-truly-usable-ask-explore-and-control-with-confidence/ | 2026-04-02 | 产品深潜 |
| `what-is-data-engineering-agent-2026` | https://datus.ai/blog/what-is-data-engineering-agent-2026/ | 2026-05-31 | ⚠️ 带年份 slug（与常青 URL 并存） |
| `what-is-semantic-layer` | https://datus.ai/blog/what-is-semantic-layer/ | 2026-05-31 | 仓库 `02-*` |
| `best-data-engineering-agents-2026` | https://datus.ai/blog/best-data-engineering-agents-2026/ | 2026-06-02 | ⚠️ 带年份 slug（与常青 URL 并存） |
| `mcp-data-engineering` | https://datus.ai/blog/mcp-data-engineering/ | 2026-06-02 | 仓库 `11-*` |
| `open-source-data-engineering-agents` | https://datus.ai/blog/open-source-data-engineering-agents/ | 2026-06-02 | 仓库 `05-*` |
| `context-engine-data-engineering-agent-accuracy` | https://datus.ai/blog/context-engine-data-engineering-agent-accuracy/ | 2026-06-01 | 仓库 `10-*` |
| `contextual-data-engineering` | https://datus.ai/blog/contextual-data-engineering/ | 2026-06-01 | 仓库 `03-*` |
| `build-your-first-data-engineering-agent` | https://datus.ai/blog/build-your-first-data-engineering-agent/ | 2026-06-03 | 仓库 `06-*` |
| `data-engineering-agent-vs-claude-code` | https://datus.ai/blog/data-engineering-agent-vs-claude-code/ | 2026-06-03 | 仓库 `07-*` |
| `enterprise-data-engineering-agent` | https://datus.ai/blog/enterprise-data-engineering-agent/ | 2026-06-03 | 仓库 `13-*` |
| `data-engineering-agent-vs-sql-copilot` | https://datus.ai/blog/data-engineering-agent-vs-sql-copilot/ | 2026-06-04 | 仓库 `08-*` |
| `one-person-data-team` | https://datus.ai/blog/one-person-data-team/ | 2026-06-04 | 仓库 `09-*` |
| `subagents-domain-specific-data-agents` | https://datus.ai/blog/subagents-domain-specific-data-agents/ | 2026-06-04 | 仓库 `14-*` |
| `ai-native-data-platforms` | https://datus.ai/blog/ai-native-data-platforms/ | 2026-06-10 | 仓库 `28-*` |
| `best-data-engineering-agents` | https://datus.ai/blog/best-data-engineering-agents/ | 2026-06-10 | 仓库 `04-*`（canonical 常青 slug） |
| `cube-agentic-analytics` | https://datus.ai/blog/cube-agentic-analytics/ | 2026-06-10 | 仓库 `26-*` |
| `dbt-semantic-layer-metricflow` | https://datus.ai/blog/dbt-semantic-layer-metricflow/ | 2026-06-10 | 仓库 `25-*` |
| `open-semantic-interchange-osi` | https://datus.ai/blog/open-semantic-interchange-osi/ | 2026-06-10 | 仓库 `24-*` |
| `platform-native-data-agents-compared` | https://datus.ai/blog/platform-native-data-agents-compared/ | 2026-06-10 | 仓库 `29-*` |
| `rag-data-engineering` | https://datus.ai/blog/rag-data-engineering/ | 2026-06-10 | 仓库 `17-*` |
| `semantic-layer-vs-ontology` | https://datus.ai/blog/semantic-layer-vs-ontology/ | 2026-06-10 | 仓库 `22-*` |
| `what-is-data-agent` | https://datus.ai/blog/what-is-data-agent/ | 2026-06-10 | 仓库 `23-*` |
| `what-is-data-catalog` | https://datus.ai/blog/what-is-data-catalog/ | 2026-06-10 | 仓库 `18-*` |
| `what-is-data-mesh` | https://datus.ai/blog/what-is-data-mesh/ | 2026-06-10 | 仓库 `19-*` |
| `what-is-gooddata` | https://datus.ai/blog/what-is-gooddata/ | 2026-06-10 | 仓库 `27-*` |
| `what-is-metric-layer` | https://datus.ai/blog/what-is-metric-layer/ | 2026-06-10 | 仓库 `20-*` |
| `what-is-schema-linking` | https://datus.ai/blog/what-is-schema-linking/ | 2026-06-10 | 仓库 `16-*` |
| `what-is-semantic-model` | https://datus.ai/blog/what-is-semantic-model/ | 2026-06-10 | 仓库 `21-*` |
| `what-is-text-to-sql` | https://datus.ai/blog/what-is-text-to-sql/ | 2026-06-10 | 仓库 `15-*` |
| `sql-was-never-the-hard-part` | https://datus.ai/blog/sql-was-never-the-hard-part/ | 2026-06-11 | 线上独有 |
| `data-engineering-agent/` | https://datus.ai/blog/data-engineering-agent/ | 2026-06-11 | Blog 专题 hub |
| `data-engineering-agent/data-engineering-agent-layered-subagent` | https://datus.ai/blog/data-engineering-agent/data-engineering-agent-layered-subagent/ | 2026-06-11 | 嵌套路径专题文 |
| `what-is-lakehouse` | https://datus.ai/blog/what-is-lakehouse/ | 2026-06-18 | 仓库 `30-*` |

**Blog 统计**：60+ 内容 URL + 1 索引 = **60+**；其中与仓库 Markdown 对应 **29** 篇，**31+** 篇为早期/发布/线上独有内容。

**线上新增（仓库外）**：
| slug | 主题 | 上线日期 |
|------|------|---------|
| `what-is-change-data-capture-cdc` | Change Data Capture 定义 | 2026-07-17 |
| `what-is-data-contract` | Data Contract 定义 | 2026-07-10 |
| `what-is-medallion-architecture` | Medallion Architecture 定义 | 2026-07-10 |
| `what-is-apache-hudi` | Apache Hudi 表格式 | 2026-06-30 |
| `what-is-apache-iceberg` | Apache Iceberg 表格式 | 2026-06-30 |
| `what-is-lakehouse-catalog` | Lakehouse Catalog 对比 | 2026-06-26 |
| `what-is-data-warehouse` | Data Warehouse 定义 | 2026-06-24 |
| `what-is-data-lake` | Data Lake 定义 | 2026-06-24 |
| `osi-vs-metricflow` | OSI vs MetricFlow 对比 | 2026-06-25 |

**Blog 索引 vs sitemap**：`/blog/` 列表页展示 **54** 篇；以下 **2** 篇仅在 sitemap 与 hub 内链中出现，**未**列入 Blog 列表：

| 路径 | 说明 |
|------|------|
| `/blog/data-engineering-agent/` | 专题 hub（长文 landing） |
| `/blog/data-engineering-agent/data-engineering-agent-layered-subagent/` | hub 嵌套专题文 |

**按内容类型（frontmatter `category` / 用途）**：

| 类型 | 线上 slug 示例 | 约数 | canonical 模式 |
|------|----------------|:---:|----------------|
| Glossary 术语/对比 | `what-is-semantic-layer`、`semantic-layer-vs-ontology`、`what-is-lakehouse`、`what-is-data-warehouse`、`what-is-data-lake` | 20+ | `/blog/{slug}/` |
| DE Agent 主簇 | `contextual-data-engineering`、`best-data-engineering-agents`、`one-person-data-team` | 17+ | `/blog/{slug}/` |
| 早期 / 发布 / 产品 | `meet_datus`、`datus-0-2-6-release-*`、`sql-was-never-the-hard-part` | 20+ | `/blog/{slug}/` |
| 专题 hub | `data-engineering-agent/` | 1 | `/blog/data-engineering-agent/` |

*Glossary 策略稿（[datus-glossary.md](./datus-glossary.md)）已与线上 **46 词**对齐；新术语长文发布 slug 仍为 `/blog/{slug}/`，在 `/glossary/` 聚合页登记并加深链即可。*

**Slug 重复（需 canonical 决策）**：

| 主题 | 并存 URL | 建议 canonical |
|------|----------|----------------|
| What is DE agent | `what-is-data-engineering-agent` / `what-is-data-engineering-agent-2026` | 以常青 slug `what-is-data-engineering-agent` 为准 |
| Best DE agents | `best-data-engineering-agents` / `best-data-engineering-agents-2026` | 以 `best-data-engineering-agents` 为准 |

### 3.3 文档站（docs.datus.ai）

独立域名，[sitemap.xml](https://docs.datus.ai/sitemap.xml) 收录 **112 URL**：**56** 英文 + **56** 中文镜像（`/zh/{path}`，与英文路径一一对应，`hreflang` 互链）。**不在** datus.ai sitemap 内。

#### 文档首页

| 路径 | 完整 URL | lastmod |
|------|----------|---------|
| `/` | https://docs.datus.ai/ | 2026-04-13 |
| `/zh/` | https://docs.datus.ai/zh/ | 2026-04-13 |

#### getting_started（4）

| 路径 | 说明 |
|------|------|
| `/getting_started/Quickstart/` | 快速开始 |
| `/getting_started/Datus_tutorial/` | 完整教程 |
| `/getting_started/contextual_data_engineering/` | Contextual Data Engineering 概念 |
| `/getting_started/dashboard_copilot/` | Dashboard Copilot |

#### cli（9）+ cli-commands（1）

| 路径 | 说明 |
|------|------|
| `/cli/introduction/` | CLI 概览 |
| `/cli/chat_command/` | Chat 命令 |
| `/cli/context_command/` | Context 命令 |
| `/cli/execution_command/` | Execution 命令 |
| `/cli/skill_command/` | Skill 命令 |
| `/cli/sql_execution/` | SQL 执行 |
| `/cli/mcp_extensions/` | MCP 扩展 |
| `/cli/plan_mode/` | Plan 模式 |
| `/cli/reference/` | CLI 参考 |
| `/cli-commands/` | 命令总览索引 |

#### configuration（7）

| 路径 | 说明 |
|------|------|
| `/configuration/introduction/` | 配置概览 |
| `/configuration/agent/` | Agent 配置 |
| `/configuration/storage/` | Storage 配置 |
| `/configuration/namespace/` | Namespace |
| `/configuration/nodes/` | Nodes |
| `/configuration/workflow/` | Workflow 配置 |
| `/configuration/benchmark/` | Benchmark 配置 |

#### knowledge_base（8）

| 路径 | 说明 |
|------|------|
| `/knowledge_base/introduction/` | 知识库概览 |
| `/knowledge_base/metadata/` | 元数据 |
| `/knowledge_base/semantic_model/` | 语义模型 |
| `/knowledge_base/metrics/` | 指标 |
| `/knowledge_base/reference_sql/` | 参考 SQL |
| `/knowledge_base/reference_template/` | 参考模板 |
| `/knowledge_base/ext_knowledge/` | 外部知识 |
| `/knowledge_base/platform_doc/` | 平台文档 |

#### subagent（6）

| 路径 | 说明 |
|------|------|
| `/subagent/introduction/` | Subagent 概览 |
| `/subagent/builtin_subagents/` | 内置 Subagent |
| `/subagent/customized_subagent/` | 自定义 Subagent |
| `/subagent/gen_semantic_model/` | 生成语义模型 |
| `/subagent/gen_metrics/` | 生成指标 |
| `/subagent/gen_sql_summary/` | 生成 SQL 摘要 |

#### workflow（4）

| 路径 | 说明 |
|------|------|
| `/workflow/introduction/` | Workflow 概览 |
| `/workflow/nodes/` | 节点 |
| `/workflow/orchestration/` | 编排 |
| `/workflow/api/` | Workflow API |

#### integration（3）

| 路径 | 说明 |
|------|------|
| `/integration/mcp/` | MCP 集成 |
| `/integration/memory/` | Memory 集成 |
| `/integration/skills/` | Skills 集成 |

#### API（3）

| 路径 | 说明 |
|------|------|
| `/API/introduction/` | API 概览 |
| `/API/chat/` | Chat API |
| `/API/deployment/` | 部署 API |

#### adapters（2）

| 路径 | 说明 |
|------|------|
| `/adapters/db_adapters/` | 数据库适配器 |
| `/adapters/semantic_adapters/` | 语义层适配器 |

#### develop（3）

| 路径 | 说明 |
|------|------|
| `/develop/` | 开发者入口 |
| `/develop/Architecture/` | 架构概览 |
| `/develop/Contributing/` | 贡献指南 |

#### 其他（5）

| 路径 | 说明 |
|------|------|
| `/release_notes/` | 版本发布说明 |
| `/benchmark/benchmark_manual/` | Benchmark 手册 |
| `/metricflow/introduction/` | MetricFlow 介绍 |
| `/training/llm_trace_usage/` | LLM Trace 用法 |
| `/web_chatbot/introduction/` | Web Chatbot |

> **内链审计（2026-06-24）**：`/blog/data-engineering-agent/` hub 页链向 `docs.datus.ai/concepts/architecture/` → **404**。正确路径为 [`/develop/Architecture/`](https://docs.datus.ai/develop/Architecture/)。

### 3.4 Studio 应用（studio.datus.ai）

云端 Web App + 营销落地页，独立 [sitemap.xml](https://studio.datus.ai/sitemap.xml)（仅 **2** 公开 URL，无 `lastmod`，协议为 `http://`）。

#### Sitemap 收录（2）

| 路径 | 完整 URL | 访问 | 说明 |
|------|----------|------|------|
| `/overview` | https://studio.datus.ai/overview | 公开 | 营销落地页；datus.ai 全站「Get started」主 CTA |
| `/releases` | https://studio.datus.ai/releases | 需登录 | 版本 / 发布说明（未登录显示 Sign in） |

#### 路由探测（未进 sitemap）

| 路径 | 完整 URL | 访问 | 说明 |
|------|----------|------|------|
| `/login` | https://studio.datus.ai/login | 公开 | 登录（Google OAuth + 邮箱） |
| `/register` | https://studio.datus.ai/register | 公开 | 注册 |
| `/try-studio` | https://studio.datus.ai/try-studio | → 重定向 | CTA 入口，重定向至 `/login?url=/dashboard` |
| `/dashboard` | https://studio.datus.ai/dashboard | 需登录 | 主应用工作台 |
| `/feedback` | https://studio.datus.ai/feedback | 需登录 | 用户反馈 |

> datus.ai 营销页 [`/products/studio/`](https://datus.ai/products/studio/) 描述产品能力；实际试用入口为 **`studio.datus.ai`**，非 datus.ai 子路径。

---

## 四、规划中 / 未出现在 sitemap 的路径

### 4.1 datus.ai（策略规划，截至 2026-06-24 仍为 404）

以下 URL 在策略文档（[datus-keywords.md](./datus-keywords.md)、[datus-growth-strategy.md](./datus-growth-strategy.md)）中仍有规划，**未出现在 datus.ai sitemap**：

| 路径 | 内容 | 优先级 |
|------|------|--------|
| `/agent` | 品类锚点页（data engineering agent / data agent） | 高 |
| `/use-cases` | 场景页总览 | 中高 |
| `/use-cases/full-stack-data-engineer` | Full stack data engineer 场景 | 中高 |
| `/use-cases/one-person-data-team` | One-person data team 场景 | 中高 |
| `/use-cases/data-engineers` | 数据工程师场景 | 中高 |
| `/use-cases/analysts` | 分析师场景 | 中 |
| `/vs/wren-ai` | Datus vs Wren AI | 中 |
| `/vs/dataherald` | Datus vs Dataherald | 中 |
| `/vs/secoda` | Datus vs Secoda | 中 |
| `/vs/defog` | Datus vs Defog.ai | 低中 |
| `/alternatives/vanna` | Vanna AI 替代品 | 中 |
| `/case-studies/yunqi-lakehouse` | 云器 Lakehouse 案例 | 高 |
| `/download` | CLI 下载/安装指南 | 中 |

> `/pricing/`、`/glossary/` 已上线；`/features/*` 规划已让位于 **`/products/*`**。  
> **`/login`、`/signup`** 不在 datus.ai——已迁移至 **`studio.datus.ai/login`**、**`/register`**（见 §3.4）。

---

## 五、技术栈推断

| 维度 | 推断 | 依据 |
|------|------|------|
| 官网前端 | Lovable / 现代 SSG（Next.js 类） | Blog 统一 `/blog/{slug}/`；sitemap 分 `sitemap-pages` + `blog/sitemap` |
| 文档站 | Docusaurus 类（Mintlify / Docusaurus / VitePress） | 路径格式 + `/zh/` hreflang 镜像 |
| Studio 前端 | SPA（登录门控） | `/login` → `/dashboard`；sitemap 仅收录 marketing 页 |
| CLI 语言 | Python（`pip install datus-agent`，>= 3.12） | PyPI + GitHub |
| AI 模型 | OpenAI、Claude、Qwen、DeepSeek、Kimi-2.5、Gemini-3 | 官方文档 + Changelog |
| 数据库 | ClickZetta、Snowflake、PostgreSQL、MySQL、DuckDB、StarRocks、Hive、Spark、ClickHouse、Trino | GitHub |
| MCP 框架 | 自研 MCP Server + Client 实现 | GitHub |
| Agent 框架 | OpenAI Agent SDK 0.7.0 + litellm_adapter | v0.2.5 Changelog |
| 向量数据库 | LanceDB、pgvector、Milvus（v0.2.6 Storage 插件化） | v0.2.6 Changelog |
| CI/CD | GitHub Actions | GitHub |
| 社区 | GitHub Discussions + [Slack](https://join.slack.com/t/datus-ai/shared_invite/zt-3g6h4fsdg-iOl5uNoz6A4GOc4xKKWUYg) | 页脚 / Blog 内链 |

---

## 六、内容机会（相对 sitemap 基线）

| 缺口 | 建议 | 优先级 |
|------|------|--------|
| **案例研究落地页** | `/case-studies/yunqi-lakehouse` 未上线；Blog 已有大量 DE Agent 内容但缺独立案例页 | 高 |
| **品类锚点页** | `/agent` 未上线；Blog 已有 `data-engineering-agent/` hub | 高 |
| **场景页** | `/use-cases/*` 未上线；Blog 有 `one-person-data-team` 等可链回 | 中高 |
| **对比页** | `/vs/*`、`/alternatives/*` 未上线 | 中高 |
| **Slug canonical** | `*-2026` 与常青 slug 并存，需 301 或 canonical 统一 | 中 |
| **Glossary 术语 backlog** | 线上 46 词页内定义，11+ 篇已以 `/blog/{slug}/` 上线；仅 Lakehouse 有聚合页深链；其余待补 `/blog/` 与 `/glossary/` 互链 | 中高 |
| **Blog hub discoverability** | `data-engineering-agent/` hub 及嵌套文未出现在 `/blog/` 列表，仅靠 sitemap 与 hub 内链 | 中 |
| **Docs 死链** | hub 页 → `/concepts/architecture/` 404，应改为 `/develop/Architecture/` | 中 |
| **Blog 内链白名单** | 独立内容互链 `/blog/{slug}`；可链 `/glossary/`（索引）、`/products/*`、`/pricing/`；面包屑与 FAQ 见 [datus-breadcrumb-spec.md](./datus-breadcrumb-spec.md)、[datus-faq-spec.md](./datus-faq-spec.md) | 中 |
| **中文站** | 非 Blog 营销页 `/zh` 镜像（规则见 [datus-i18n-spec.md](./datus-i18n-spec.md)）；Blog/docs 不在该规范范围；公众号可继续中文分发 | 中 |
| **Studio sitemap** | 认证路由（login/register/dashboard）未收录；sitemap 使用 http 协议 | 低 |

---

*站点结构 · Datus · https://datus.ai/ · sitemap 同步于 2026-06-24（datus.ai / docs.datus.ai / studio.datus.ai）*
