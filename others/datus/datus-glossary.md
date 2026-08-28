# Datus — Glossary 策略

> **本文档职责**：`/glossary` 页面的策略设计——关键词簇、术语选择逻辑、内容网络位置；并与线上 [datus.ai/glossary/](https://datus.ai/glossary/) 保持词表同步。  
> **引用**：[datus.md](./datus.md) 概览 | [datus-site-structure.md](./datus-site-structure.md) 站点结构 | [datus-keywords.md](./datus-keywords.md) 关键词 | [datus-positioning.md](./datus-positioning.md) 定位 | [datus-competitors.md](./datus-competitors.md) 竞品

**最近更新**：2026-06-24（词表同步线上 · 46 词 · §四 全量 blog 承接对照 · 补「线上实现差距」）

**线上页面**：[datus.ai/glossary/](https://datus.ai/glossary/) — 7 categories · 46 terms · Updated June 2026（**单页聚合**，术语为页内 H3 定义，非独立 URL）

---

## 一、为什么做 Glossary

Glossary 不是流量页——单页 glossary 的搜索量本身很低。它的三层目的：

| 层级 | 目的 | 说明 |
|------|------|------|
| **SEO 长尾聚合** | **46** 个术语（线上为单页聚合 + 部分 `/blog/{slug}/` 长文），系统性截获定义型搜索的零散流量（"what is semantic layer"、"ETL vs ELT explained"），聚合成 SEO 权重页，通过内链分发权重给 `/agent`、`/products/*` 等转化页 |
| **品类叙事锚定** | 术语选择本身就是产品定位——选 Lakehouse 不选传统 EDW，选 Data Mesh 不选 Centralized Data Platform，选 Text-to-SQL + Schema Linking 而不是只写 NL2SQL。词表即立场 |
| **内容网络根节点** | 每个术语定义中埋 inline chip（`dbt`、`MetricFlow`、`RAG`）→ 未来作为内链入口指向 blog、features、vs 页。Glossary 是内容网络的根，后续所有落地页从这里长出链接 |

---

## 二、术语选择逻辑

不是「所有 data engineering 术语」——只选与 Datus 产品定位相关的那一批。选择标准三条：

1. **与 Datus 产品直接相关**：术语必须能自然连接到 Datus 的 Context Engine、Subagent、Feedback Loop、多模型支持、跨栈适配器
2. **有搜索量或搜索意图**：以定义型（"what is X"）和对比型（"X vs Y"）为主——这些是 glossary 擅长承接的搜索意图
3. **叙事需要而非教科书法则**：选 Lakehouse 而不是传统 EDW，选 Data Mesh 而不是 Centralized Platform，选 OBT + Data Vault 补充 Star Schema——词表即产品立场

**明确不选**：
- Datus 专有术语（Context Engine、Subagent、Scoped Context）→ 归 `/products/*` 系列，不放 glossary
- 纯计算机科学概念（ACID、CAP theorem、MapReduce）→ 太通用，无差异化
- 非数据工程 AI 概念（fine-tuning、RLHF、transformer architecture）→ 归 AI glossary，不混淆

**线上已纳入、策略需知**：
- **Data Engineering Agent** 作为**行业通用品类词**列入 AI & Agents（非 Datus 专有名词；Datus 专有实现仍归产品页）
- **dbt** 从原规划的 inline chip 升级为 Processing **独立词条**（见 §三 Category D）

---

## 三、术语表（7 类 46 词）

以下术语按 7 个类别组织，与线上 [glossary](https://datus.ai/glossary/) **词表对齐**（2026-06-24 审计）。每个术语在本文档含：**策略定义（2-3 句）** + **Datus 关联** + **目标关键词簇** + **线上状态**（如已有 blog 长文）。

**分类命名（线上）**：Architecture · Modeling · **Storage & Formats** · Processing · **Governance & Quality** · AI & Agents · Observability

| 分类 | 词数 | 锚点 |
|------|:---:|------|
| A Architecture | 7 | `#architecture` |
| B Modeling | 7 | `#modeling` |
| C Storage & Formats | 6 | `#storage-formats` |
| D Processing | 7 | `#processing` |
| E Governance & Quality | 6 | `#governance-quality` |
| F AI & Agents | 7 | `#ai-agents` |
| G Observability | 6 | `#observability` |

---

### Category A: Architecture（7 词）— 数据系统怎么组织

**叙事目的**：建立 Datus 「跨栈」的语境基础——如果用户不理解 Lakehouse、Data Mesh、Medallion，就无法理解 Datus 为什么强调「不绑定单一 warehouse」。

#### Data Warehouse
面向结构化数据的集中式查询仓库，schema-on-write，优化 SQL 分析速度。Datus 通过 Native DB Adapter（`Snowflake`、`PostgreSQL`）直连数仓，用其 schema 构建 Context Tree。

**关键词簇**：`data warehouse definition`、`what is a data warehouse`、`cloud data warehouse`

#### Data Lake
以原生格式存储原始数据的对象存储系统，schema-on-read，牺牲查询速度换灵活性和低成本。Datus 通过 catalog service 读取 lake metadata，从 lake 表结构生成 semantic model。

**关键词簇**：`data lake definition`、`data lake vs data warehouse`、`what is a data lake`

#### Lakehouse
融合 data lake 灵活性与 warehouse ACID 事务和 SQL 性能的混合架构，核心支撑是开放表格式（`Iceberg`、`Delta Lake`、`Hudi`）。Datus 已落地云器 Lakehouse 生产案例（自助率 15%→60%）。

**关键词簇**：`lakehouse architecture`、`lakehouse vs data warehouse`、`what is a lakehouse`、`open table format lakehouse`  
**线上 · blog**：[`/blog/what-is-lakehouse/`](https://datus.ai/blog/what-is-lakehouse/) · **唯一**已挂「Read the full guide →」深链

#### Data Mesh
按业务域分散治理的数据架构——每个域拥有并服务自己的数据产品，强调联邦治理和自助数据基础设施。Datus 的 Subject Tree 天然映射 mesh 域结构：每个业务域 = 一个一级主题节点 + 独立 Subagent。

**关键词簇**：`data mesh explained`、`data mesh vs data fabric`、`data mesh principles`、`what is data mesh`  
**线上 · blog**：[`/blog/what-is-data-mesh/`](https://datus.ai/blog/what-is-data-mesh/) · 聚合页待加深链

#### Data Fabric
通过元数据驱动自动化，在异构数据源之上提供统一访问层的架构。与 mesh 的区别：fabric 是技术中心（集中式集成），mesh 是组织中心（去中心化治理）。Datus 更贴近 mesh 理念——Subagent 作用域天然映射域边界。

**关键词簇**：`data fabric definition`、`data fabric vs data mesh`、`what is data fabric`

#### Medallion Architecture
多层数据组织模式：Bronze（原始摄入）、Silver（清洗+关联）、Gold（业务聚合）。源自 Databricks，现为通用 lakehouse 模式。Datus agent 可跨层运作——从 Gold 层指标引导 context，同时探索 Silver 层表结构。

**关键词簇**：`medallion architecture`、`bronze silver gold data`、`medallion lakehouse`  
**线上**：标题为 Medallion Architecture（Bronze/Silver/Gold 在正文说明）

#### Lambda vs Kappa
两种流处理架构模式：Lambda 维护独立批和流管线再合并结果；Kappa 用单一流管线处理所有数据，需要重新处理时从 event log 回放。与 Datus 的关联：agent 需要理解指标来自批处理还是实时源——但目前 Datus 以批为主，Kappa 场景是远期方向。

**关键词簇**：`lambda vs kappa architecture`、`lambda architecture explained`、`kappa architecture streaming`

---

### Category B: Modeling（7 词）— 数据怎么被组织成业务语言

**叙事目的**：这是 Datus Semantic Model 和 Context Engine 的理论基础。讲清楚 Star Schema、OBT、Data Vault，用户才能理解 Datus 的「双维度 Context Tree」在消除什么建模歧义。

#### Semantic Layer
将复杂表结构映射为业务术语（指标、维度、实体）的业务表示层——原始数据和业务用户之间的翻译层。Datus 构建的是「活的」semantic layer：双维度（Physical Catalog × Logical Subject），通过 `/gen_semantic_model` 和 `/gen_metrics` 自动生成，通过反馈持续进化。与 `dbt` 或 `Cube.dev` 的静态 semantic layer 形成对比。

**关键词簇**：`semantic layer definition`、`what is a semantic layer`、`semantic layer data engineering`、`semantic layer vs metric layer`  
**线上 · blog**：[`/blog/what-is-semantic-layer/`](https://datus.ai/blog/what-is-semantic-layer/) · 聚合页待加深链

#### Metric Layer
Semantic layer 中专攻业务指标的子集——指标定义、计算逻辑、维度、归属。Datus 从历史 SQL 和 Success Story 自动生成指标（`/gen_metrics`），存储为 MetricFlow 兼容 YAML，注入 Subagent Scoped Context。

**关键词簇**：`metric layer definition`、`metric layer vs semantic layer`、`what is a metrics layer`、`headless BI metrics`  
**线上 · blog**：[`/blog/what-is-metric-layer/`](https://datus.ai/blog/what-is-metric-layer/) · 聚合页待加深链

#### Dimensional Modeling
Kimball 式建模：将数据组织为事实表（度量）和维度表（描述属性）。Star 与 Snowflake 为其两种主要形态——前者反范式化维度，后者将维度范式化为子维度。Datus 的 Semantic Model 贴附到事实/维度表对上，理解哪些列是 measures vs. dimensions。

**关键词簇**：`dimensional modeling`、`what is dimensional modeling`、`fact table vs dimension table`  
**线上**：页内定义 · 无独立 blog

#### Star Schema
事实表 surrounded by 反范式化维度表——BI 最常见布局，查询简单、性能好。与 Snowflake schema 对比时强调反范式 vs 范式化维度。Datus agent 需识别 star 结构以正确生成 join 与聚合。

**关键词簇**：`star schema definition`、`star schema vs snowflake schema`、`what is star schema`  
**线上**：页内定义（自 Dimensional Modeling 拆分，2026-06）· 无独立 blog

#### Slowly Changing Dimensions (SCD)
处理维度属性随时间变化的一组技术——Type 1（覆写）、Type 2（版本化行+生效日期）、Type 3（前值列）。管理 SCD 表的数据工程师需要知道哪种类型生效——Datus 将其捕获在 Semantic Model 标注中。

**关键词簇**：`slowly changing dimensions`、`SCD type 1 vs type 2`、`what is SCD`  
**线上**：页内定义 · 无独立 blog

#### OBT (One Big Table)
将所有相关列（事实+维度）放在一张宽表中的反范式化建模方法——牺牲存储效率换取查询简单。在 BI 工具和 metric layer 中常见。Datus agent 需要识别 OBT 模式——Context Engine 识别宽表并帮助用户导航其中的列语义。

**关键词簇**：`one big table modeling`、`OBT vs star schema`、`wide table data modeling`  
**线上**：页内定义 · 无独立 blog

#### Data Vault
面向企业级数仓的建模方法论，围绕 hub（业务键）、link（关系）、satellite（描述属性）组织——强调可审计性和并行加载。Datus 可以在 Catalog 维度中建模 Data Vault 结构——理解 hub/link/satellite 关系帮助 agent 追踪血缘和生成正确连接。

**关键词簇**：`data vault modeling`、`data vault vs star schema`、`what is data vault`  
**线上**：页内定义 · 无独立 blog

---

### Category C: Storage & Formats（6 词）— 数据怎么存

**叙事目的**：Datus 定位「跨栈」——如果 glossary 不讲清楚底层存储格式，就无法解释 Datus 的 10 个 DB Adapter 有何存在理由。这也是区分「随便一个 NL2SQL 工具」和「真正的 data engineering agent」的技术基底。

#### Columnar Storage
按列而非按行存储数据值——实现高压缩比和仅读取相关列的快速分析查询。现代分析数据库（`ClickHouse`、`Snowflake`）的基础。Datus agent 生成的 SQL 受益于列存引擎优化——理解列存 vs 行存帮助解释查询性能差异。

**关键词簇**：`columnar storage definition`、`columnar vs row storage`、`what is columnar database`

#### Parquet
开源列存文件格式，支持丰富 schema 和谓词下推——data lake 和 lakehouse 环境中的主导格式。Datus 读取 Parquet schema 构建 Catalog 条目，在为 lake-based 数据生成查询时使用 schema 元数据。

**关键词簇**：`parquet file format`、`what is parquet`、`parquet vs CSV`、`parquet vs Avro`

#### Apache Iceberg
面向大型分析数据集的开放表格式，提供 ACID 事务、时间旅行和 schema 演化——在对象存储上实现。被 `Snowflake`、`Spark`、`Trino` 和多数 lakehouse 平台使用。Datus 通过 DB adapter 连接 Iceberg 表——Iceberg 的 schema 演化能力与 Datus "evolvable context" 理念对齐。

**关键词簇**：`apache iceberg`、`iceberg table format`、`iceberg vs delta lake`、`what is iceberg`

#### Delta Lake
开源存储层（Linux Foundation），为 data lake 带来 ACID 事务、版本控制和统一批流处理。与 `Databricks` 和 Spark 生态深度集成。Datus 的 Spark adapter（v0.2.6）支持 Delta Lake 表。

**关键词簇**：`delta lake definition`、`delta lake vs iceberg`、`what is delta lake`

#### Apache Hudi
面向流数据摄取和增量处理的开放表格式，支持 data lake 上的 upsert 和 delete。Datus 的 Hive 和 Spark adapter（v0.2.6）覆盖 Hudi 管理表。与 agent 处理 CDC 或近实时数据管线的场景相关。

**关键词簇**：`apache hudi`、`hudi vs iceberg vs delta`、`what is hudi`

#### OLAP vs OLTP
两类数据库负载：OLTP（在线事务处理）优化快速小事务（INSERT/UPDATE）；OLAP（在线分析处理）优化复杂读重分析查询。Datus 面向 OLAP 负载——生成分析 SQL、在 warehouse/lakehouse schema 上构建 context、面向数据工程师和分析师而非应用开发者。

**关键词簇**：`OLAP vs OLTP`、`what is OLAP`、`OLTP definition`、`analytical vs transactional database`

---

### Category D: Processing（7 词）— 数据怎么被操作和转换

**叙事目的**：这是数据工程师的日常——CDC、Backfill、Idempotency 是真正的痛点词。把 Datus 放进这些概念的定义里，等于告诉用户「Datus 不是玩具，是处理真实 production 问题的工具」。

#### ETL vs ELT
两种数据集成模式：ETL（Extract → Transform → Load）在加载前转换；ELT（Extract → Load → Transform）先加载原始数据，在 warehouse 内利用其计算能力转换。Datus agent 工作在两者中的 Transform 阶段——生成转换 SQL，在转换后表上构建 context，从 ELT 管线中捕获 Reference SQL。

**关键词簇**：`ETL vs ELT`、`what is ETL`、`what is ELT`、`ETL pipeline definition`

#### Batch vs Streaming
两种数据处理范式：batch 按调度处理有限数据集（每小时/每天）；streaming 持续处理近实时无界数据。Datus 当前面向批处理场景。流式 context——理解实时指标 vs 批指标——是长运行 agent 场景的未来考量。

**关键词簇**：`batch vs stream processing`、`batch processing definition`、`stream processing explained`

#### CDC (Change Data Capture)
跟踪和捕获源数据变更（INSERT/UPDATE/DELETE）并传播到下游系统的技术——通常通过日志解析实现。CDC 管线引入 schema 漂移和 backfill 处理复杂性。管理 CDC 馈送表的 Datus agent 需要变更模式感知——Context Engine 的未来考量。

**关键词簇**：`change data capture`、`CDC database`、`what is CDC`、`CDC vs batch ETL`

#### Backfill
重新处理历史数据的过程——通常用于填充新表、修复数据质量问题或追溯应用更新后的业务逻辑。数据工程中常见且易出错的场景。Datus 可辅助 backfill：生成 SQL 模板、通过血缘识别受影响的表、引用历史 Reference SQL 验证正确性。

**关键词簇**：`data backfill`、`backfill pipeline`、`what is backfill in data engineering`

#### Idempotency
操作的可重复执行属性——无论执行多少次都产生相同结果，对可靠数据管线至关重要。幂等管线可以安全地重跑而不重复或损坏数据。Datus agent 应生成幂等 SQL 模式并在生成代码中标记非幂等方法。

**关键词簇**：`idempotency data pipeline`、`idempotent SQL`、`what is idempotency in data engineering`

#### Materialized View
存储查询预计算结果的数据对象——以存储和刷新维护为代价加速读取。在 `PostgreSQL`、`Snowflake`、`ClickHouse` 中常见。Datus 可以将物化视图纳入 Catalog 维度——了解哪些视图存在及其含义，避免冗余查询生成，帮助用户导航数据环境。

**关键词簇**：`materialized view definition`、`materialized view vs view`、`what is a materialized view`  
**线上**：页内定义 · 无独立 blog

#### dbt
在 warehouse 内以版本控制 SQL model 定义转换的框架——现代 ELT 栈中 「T」的事实标准。Datus 与 dbt 生态互补：agent 可读取 dbt 模型/metadata 构建 context，生成与现有 dbt 项目一致的 SQL。相关叙事见 blog [`dbt-semantic-layer-metricflow`](https://datus.ai/blog/dbt-semantic-layer-metricflow/)。

**关键词簇**：`what is dbt`、`dbt data transformation`、`dbt vs ETL`  
**线上**：**独立词条**（2026-06 新增；原策略为 inline chip）· blog 为生态对比文，非 what-is-dbt 定义页

---

### Category E: Governance & Quality（6 词）— 数据怎么被管理和控制

**叙事目的**：这是 Datus Enterprise 价值主张的理论地基。Data Contract、RBAC、Data Quality 等概念为企业版 "shared context, governance, and long-running data agents" 定位提供概念支撑。企业买家通过这些词判断 Datus 是否「enterprise-ready」。

#### Data Catalog
盘点数据资产、跟踪 schema、提供跨组织搜索和发现能力的元数据管理系统。代表工具：`DataHub`、`Atlan`、`Select Star`。Datus 的 Catalog Service 和 Context Engine 功能类似——但面向 AI agent 消费而非人工浏览。Catalog 服务是 Datus 的数据源，不是竞品。

**关键词簇**：`data catalog definition`、`what is a data catalog`、`data catalog vs data dictionary`  
**线上 · blog**：[`/blog/what-is-data-catalog/`](https://datus.ai/blog/what-is-data-catalog/) · 聚合页待加深链

#### Data Contract
数据生产者和消费者之间的正式协议——定义数据资产的 schema、语义和质量保证。contract 编码预期如「此列永不为 NULL」或「行在源提交后 5 分钟内到达」。Datus 的 Subagent rules 和 Semantic Model 标注功能上等同于轻量 data contract——编码 agent 对数据可做出的假设。

**关键词簇**：`data contract definition`、`what is a data contract`、`data contract data engineering`

#### Data Lineage
追踪数据在管线中的起源、转换和依赖——回答「这些数据从哪里来？」和「哪些下游系统依赖此表？」。Datus 的 Context Engine 通过 Catalog Tree 和 Reference SQL 关系隐式构建血缘。完整的血缘可视化是潜在未来能力。

**关键词簇**：`data lineage definition`、`what is data lineage`、`data lineage vs data provenance`

#### PII / Data Masking
PII（个人可识别信息）是可识别个人的数据——姓名、邮件、电话。Data masking 为非生产环境替换敏感值为虚拟但真实的替代值。Datus Enterprise 的访问控制模型支持 PII 感知的 subagent 作用域——Subagent 可配置为排除 PII 列或应用 masking 规则。

**关键词簇**：`PII data definition`、`data masking explained`、`what is data masking`

#### RBAC (Role-Based Access Control)
将权限分配给角色而非个人的安全模型——在大规模场景中简化访问管理。常见模式：按数据域映射 reader/writer/admin 角色。Datus Enterprise 利用 Subagent 作用域权限作为 RBAC 的一种形式——每个 Subagent 具有定义好的 context 边界，天然形成访问边界。

**关键词簇**：`RBAC definition`、`role based access control data`、`what is RBAC`

#### Data Quality
数据适应性的度量和执行——各维度：freshness（数据是否及时？）、completeness（值是否完整？）、uniqueness（键是否重复？）、accuracy（值是否正确？）、consistency（跨系统值是否一致？）。Datus 的 Evaluation Framework（Exact Match、Result Count、Schema Usage、Semantic Correctness）和 Feedback Loop（Upvote/Issue Report）是应用于 AI 生成 SQL 输出的质量度量机制。

**关键词簇**：`data quality definition`、`data quality dimensions`、`what is data quality`、`data freshness completeness`

---

### Category F: AI & Agents（7 词）— AI 怎么改变数据工程

**叙事目的**：这是 Datus 的核心品类词簇。Text-to-SQL、Schema Linking、RAG、MCP 不是「AI 通用概念」——它们构成了 Datus 技术栈的每一层。Glossary 定义这些词时，自然地把 Datus 写进去，等于告诉搜索引擎「Datus = 这些概念的产品化实现」。

#### Text-to-SQL
将自然语言问题转换为可执行 SQL 查询的任务——NL2SQL agent 的核心 AI 能力。现代 text-to-SQL 系统依赖 schema context、few-shot 示例和反馈闭环来提升准确率。Datus 通过 Context Engine（将 Schema + Semantic Model + Reference SQL 注入每轮 prompt）和持续学习（用户 upvote 优化未来生成）提升 text-to-SQL 准确率。

**关键词簇**：`text-to-SQL definition`、`what is text-to-SQL`、`NL2SQL explained`、`natural language to SQL AI`  
**线上 · blog**：[`/blog/what-is-text-to-sql/`](https://datus.ai/blog/what-is-text-to-sql/) · 聚合页待加深链

#### Schema Linking
将自然语言引用（"各渠道上周收入"）映射到具体数据库列和表（`fact_revenue.channel_id`、`dim_channel.name`）的子任务。Schema linking 准确率是大多数 NL2SQL 系统的瓶颈。Datus 的 Catalog + Subject 双维度 Context Tree 专门为此设计——同时提供物理列引用和业务术语别名。

**关键词簇**：`schema linking definition`、`schema linking text-to-SQL`、`what is schema linking`  
**线上 · blog**：[`/blog/what-is-schema-linking/`](https://datus.ai/blog/what-is-schema-linking/) · 聚合页待加深链

#### Retrieval-Augmented Generation (RAG)
从外部源检索相关文档或数据并注入 LLM prompt 的技术——用事实上下文锚定回答。在数据工程中，RAG 检索 schema 定义、历史 SQL 和指标定义。Datus 通过 Context Engine 实现 RAG：`@table`、`@metrics`、`@sql_history` 命令注入相关上下文；`@catalog` 和 `@subject` 作为可导航检索界面。

**关键词簇**：`RAG definition`、`retrieval-augmented generation explained`、`RAG data engineering`、`what is RAG`  
**线上 · blog**：[`/blog/rag-data-engineering/`](https://datus.ai/blog/rag-data-engineering/) · 聚合页待加深链

#### MCP (Model Context Protocol)
标准化 AI agent 连接外部工具和数据源方式的开源协议（Anthropic），通过 client-server 模型实现跨厂商 agent-工具互操作。Datus 同时实现 MCP Client（`.mcp add/remove/list/call` 连接外部工具如 `Airflow`）和 MCP Server（将 Datus 数据库工具暴露给外部 agent 如 `Claude Desktop`）。MCP 用于可扩展性；核心数据操作使用 Datus 原生工具。

**关键词簇**：`MCP protocol explained`、`model context protocol definition`、`what is MCP`、`MCP server data engineering`  
**线上 · blog**：[`/blog/mcp-data-engineering/`](https://datus.ai/blog/mcp-data-engineering/) · 聚合页待加深链

#### Embedding
文本、代码或其他数据的数值向量表示，捕获语义含义——相似概念具有相近向量位置。Embedding 为语义搜索和 RAG 检索提供动力。Datus 的向量化知识检索（v0.2.4）使用 embedding 查找语义相关的历史 SQL 和 context，存储在支持的向量数据库（`LanceDB`、`pgvector`、`Milvus`）中。

**关键词簇**：`embedding definition AI`、`what is embedding`、`vector embedding explained`

#### Vector Search
通过语义相似度（基于 embedding）而非精确关键词匹配查找条目——例如找到 "revenue by geography" 与 "sales by region" 语义相似。Datus 在 Context Engine 中使用 vector search 检索与用户查询最相关的 Reference SQL 和指标，即使术语与已存储示例不一致。

**关键词簇**：`vector search definition`、`what is vector search`、`vector search vs keyword search`、`vector database search`  
**线上**：页内定义 · 无独立 blog

#### Data Engineering Agent
LLM 驱动的系统，端到端规划并执行数据工作流——schema 发现、SQL 生成、校验与迭代——而非仅做单条 query 补全。Datus 品类锚点；与 SQL copilot / text-to-SQL 工具的区别在于**持久 context** 与**可进化知识库**。

**关键词簇**：`what is a data engineering agent`、`data engineering agent vs copilot`、`AI data engineering agent`  
**线上 · blog**：[`/blog/what-is-data-engineering-agent/`](https://datus.ai/blog/what-is-data-engineering-agent/) · hub [`/blog/data-engineering-agent/`](https://datus.ai/blog/data-engineering-agent/) · 聚合页待加深链

---

### Category G: Observability（6 词）— 数据是否健康、可靠

**叙事目的**：Datus 的 Feedback Loop + Evaluation Framework 本质上是一个「AI 生成的 SQL 的可观测性层」。讲清楚行业通用的 observability 概念，等于告诉用户 Datus 不只是在生成 SQL——它在测量和改进 SQL 质量。这是从「NL2SQL 工具」升级到「data engineering agent」的关键叙事台阶。

#### Data Observability
跨 freshness、volume、schema、distribution 和 lineage 维度监控数据健康的一组实践和工具——借鉴自软件可观测性（logs、metrics、traces）。代表工具：`Monte Carlo`、`Bigeye`、`Elementary`、`Soda`。Datus 通过 MCP 集成数据可观测性工具（如 `soda-core`），并通过其 Evaluation Framework 和 Feedback Loop 贡献可观测性——随时间测量和改进 SQL 准确率。

**关键词簇**：`data observability definition`、`what is data observability`、`data observability vs data quality`  
**线上**：页内定义 · 无独立 blog

#### Freshness
衡量数据时效性的数据质量维度——数据从源头创建到可供查询之间的时间间隔。陈旧数据（高 freshness 延迟）是最常见的数据工程事故之一。Datus agent 可配置为在 Subagent rules 中检查 freshness——例如在查询具有已知 freshness 约束的表时向用户发出警告。

**关键词簇**：`data freshness definition`、`what is data freshness`、`data freshness monitoring`  
**线上**：页内定义 · 无独立 blog

#### Volume Checks
行数/摄入量趋势监控——例如某表今日行数是否较历史区间骤降 90%，常为上游 job 部分失败的早期信号。

**关键词簇**：`data volume check`、`volume anomaly data pipeline`  
**线上**：独立词条（自原「Volume / Schema / Distribution Checks」拆分，2026-06）

#### Schema Drift
列类型、名称或存在性的未公告变更——常 silently 破坏下游 model，直到 dashboard 出现 NULL。与 CDC、Data Observability 叙事衔接。

**关键词簇**：`schema drift detection`、`what is schema drift`  
**线上**：独立词条（2026-06 新增；原合并在 Volume/Schema/Distribution 项内）

#### Anomaly Detection
自动识别数据中异常模式——突然的 volume 下降、schema 变更、distribution 偏移——可能表明管线故障或数据质量问题。Datus 的 Feedback Loop 和 Success Story 机制可浮出异常模式：当一条成熟查询突然产生不同结果时，agent 标记复核。

**关键词簇**：`data anomaly detection`、`what is anomaly detection in data`、`anomaly detection pipeline`  
**线上**：页内定义 · 无独立 blog

#### Data SLA / SLO
SLA（服务水平协议）：对数据消费者的正式承诺（如「销售看板每日 8 点前刷新」）。SLO（服务水平目标）：内部可衡量指标（如「99.5% 日常 ETL 作业在 2 小时内完成」）。Datus 的长运行 agent 和 Enterprise 编排能力与此概念相关——agent 需要了解 SLO 以判断优先级和监控工作。

**关键词簇**：`data SLA SLO`、`what is a data SLA`、`SLO vs SLA data engineering`  
**线上**：标题 Data SLA / SLO（原策略稿 SLA / SLO for Data）

> **词表变更说明（2026-06-02 → 线上 2026-06）**：原 Category G 第 5 项「Volume / Schema / Distribution Checks」拆为 **Volume Checks** + **Schema Drift**；**Distribution** 无独立词条（内容分散在 Data Observability / Data Quality）。

---

## 四、Glossary 在 Datus 内容网络中的位置

### URL 模型（与 [datus-site-structure.md](./datus-site-structure.md) 一致）

| 层级 | 路径 | 说明 |
|------|------|------|
| **聚合索引** | `/glossary/` | 46 词页内 H3 定义 + 分类锚点 |
| **独立长文** | `/blog/{slug}/` | Glossary 术语 deep-dive 的 canonical URL |
| **品类 hub** | `/blog/data-engineering-agent/` | DE Agent 专题（非 glossary 词条，但互链） |

### 作为内容根节点

Glossary 不是终点，是起点。每个术语定义中埋 inline chip → 内链指向 blog、products、案例页：

```
/glossary
  ├── semantic layer ──→ /blog/what-is-semantic-layer/
  ├── lakehouse ──→ /blog/what-is-lakehouse/（✅ 已深链）
  ├── text-to-SQL ──→ /blog/what-is-text-to-sql/
  ├── MCP ──→ /blog/mcp-data-engineering/
  ├── RAG ──→ /blog/rag-data-engineering/
  ├── data engineering agent ──→ /blog/data-engineering-agent/（hub）
  ├── dbt ──→ /blog/dbt-semantic-layer-metricflow/（生态文，非 what-is-dbt）
  ├── data contract ──→ /products/enterprise/（Governance 价值主张）
  └── ...
```

### 与现有内容资产的关系

| 现有资产 | Glossary 如何强化它 |
|----------|-------------------|
| `/products/*` 系列 | Glossary 提供行业语境——用户先理解 Semantic Layer，再理解 Datus 实现 |
| `/vs/*` 对比页（规划） | Glossary 定义竞品相关术语（`dbt`、`MetricFlow`、`Cube.dev`），对比页直接引用 |
| `/blog/*` 系列 | Blog 链回 glossary 术语而非重复定义；**glossary 应为已有 blog 挂「Read the full guide →」** |
| `/agent` 品类锚点页（规划） | 长尾定义型搜索经 glossary → `/agent` 或 `/blog/data-engineering-agent/` |
| `/integrations/` | Storage & Formats 分类为集成页提供技术基底 |

### 术语 × Blog 承接对照（全量 46 词）

**数据来源**：[blog/sitemap.xml](https://datus.ai/blog/sitemap.xml)（2026-06-24）· Glossary 聚合页内链审计

**状态说明**：

| 标记 | 含义 |
|------|------|
| ✅ 专用 | 存在以该术语为主角的 `/blog/{slug}/`（canonical 长文） |
| ◐ 相关 | 有 blog 但未按该词建专用定义页（生态/角度文） |
| ❌ 无 | sitemap 中无专用或强相关 slug |
| 深链 | Glossary 聚合页是否已挂「Read the full guide →」 |

**汇总**：

| 状态 | 词数 |
|------|:---:|
| ✅ 已有专用 `/blog/` 文 | 10 |
| ◐ 有相关文（非专用） | 1 |
| ❌ 尚无 blog 文 | 35 |
| Glossary 已挂深链 | 1（仅 Lakehouse） |

#### Category A — Architecture（7）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| Data Warehouse | ❌ | — | — |
| Data Lake | ❌ | — | — |
| Lakehouse | ✅ | [`what-is-lakehouse`](https://datus.ai/blog/what-is-lakehouse/) | ✅ |
| Data Mesh | ✅ | [`what-is-data-mesh`](https://datus.ai/blog/what-is-data-mesh/) | ❌ |
| Data Fabric | ❌ | — | — |
| Medallion Architecture | ❌ | — | — |
| Lambda vs Kappa | ❌ | — | — |

#### Category B — Modeling（7）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| Semantic Layer | ✅ | [`what-is-semantic-layer`](https://datus.ai/blog/what-is-semantic-layer/) | ❌ |
| Metric Layer | ✅ | [`what-is-metric-layer`](https://datus.ai/blog/what-is-metric-layer/) | ❌ |
| Dimensional Modeling | ❌ | — | — |
| Star Schema | ❌ | — | — |
| Slowly Changing Dimensions (SCD) | ❌ | — | — |
| OBT (One Big Table) | ❌ | — | — |
| Data Vault | ❌ | — | — |

#### Category C — Storage & Formats（6）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| Columnar Storage | ❌ | — | — |
| Parquet | ❌ | — | — |
| Apache Iceberg | ❌ | — | — |
| Delta Lake | ❌ | — | — |
| Apache Hudi | ❌ | — | — |
| OLAP vs OLTP | ❌ | — | — |

#### Category D — Processing（7）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| ETL vs ELT | ❌ | 角度文 [`agentic-etl-what-changes-beyond-traditional-etl`](https://datus.ai/blog/agentic-etl-what-changes-beyond-traditional-etl/)（非定义页） | — |
| Batch vs Streaming | ❌ | — | — |
| CDC (Change Data Capture) | ❌ | — | — |
| Backfill | ❌ | — | — |
| Idempotency | ❌ | — | — |
| Materialized View | ❌ | — | — |
| dbt | ◐ | [`dbt-semantic-layer-metricflow`](https://datus.ai/blog/dbt-semantic-layer-metricflow/)（生态文，非 `what-is-dbt`） | — |

#### Category E — Governance & Quality（6）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| Data Catalog | ✅ | [`what-is-data-catalog`](https://datus.ai/blog/what-is-data-catalog/) | ❌ |
| Data Contract | ❌ | — | — |
| Data Lineage | ❌ | — | — |
| PII / Data Masking | ❌ | — | — |
| RBAC | ❌ | — | — |
| Data Quality | ❌ | — | — |

#### Category F — AI & Agents（7）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| Text-to-SQL | ✅ | [`what-is-text-to-sql`](https://datus.ai/blog/what-is-text-to-sql/) | ❌ |
| Schema Linking | ✅ | [`what-is-schema-linking`](https://datus.ai/blog/what-is-schema-linking/) | ❌ |
| RAG | ✅ | [`rag-data-engineering`](https://datus.ai/blog/rag-data-engineering/) | ❌ |
| MCP | ✅ | [`mcp-data-engineering`](https://datus.ai/blog/mcp-data-engineering/) | ❌ |
| Embedding | ❌ | — | — |
| Vector Search | ❌ | — | — |
| Data Engineering Agent | ✅ | [`what-is-data-engineering-agent`](https://datus.ai/blog/what-is-data-engineering-agent/) · hub [`data-engineering-agent`](https://datus.ai/blog/data-engineering-agent/) · ⚠️ 并存 [`what-is-data-engineering-agent-2026`](https://datus.ai/blog/what-is-data-engineering-agent-2026/) | ❌ |

#### Category G — Observability（6）

| 术语 | Blog 状态 | slug / URL | Glossary 深链 |
|------|:---:|------|:---:|
| Data Observability | ❌ | — | — |
| Freshness | ❌ | — | — |
| Volume Checks | ❌ | — | — |
| Schema Drift | ❌ | — | — |
| Anomaly Detection | ❌ | — | — |
| Data SLA / SLO | ❌ | — | — |

#### 补充：Blog 已有 · 不在 Glossary 46 词表内

| Blog slug | 说明 | 建议互链 |
|-----------|------|---------|
| [`what-is-semantic-model`](https://datus.ai/blog/what-is-semantic-model/) | 无独立 Glossary 词条 | → Semantic Layer |
| [`what-is-data-agent`](https://datus.ai/blog/what-is-data-agent/) | 词表为 Data **Engineering** Agent | → DE Agent 词条 / hub |
| [`what-is-gooddata`](https://datus.ai/blog/what-is-gooddata/) | 不在 46 词表 | 可选 chip |
| [`semantic-layer-vs-ontology`](https://datus.ai/blog/semantic-layer-vs-ontology/) | 对比文 | → Semantic Layer |

### 内容 backlog 优先级

| 优先级 | 动作 | 范围 |
|:---:|------|------|
| **P0** | Glossary 聚合页补「Read the full guide →」深链 | 已有专用文的 **9** 词（除 Lakehouse 外）：Data Mesh · Semantic Layer · Metric Layer · Data Catalog · Text-to-SQL · Schema Linking · RAG · MCP · Data Engineering Agent |
| **P1** | 新写 `what-is-*` 专用文 | dbt · Data Warehouse · Data Lake · ETL vs ELT · Data Quality · Data Observability |
| **P2** | 整类空白补文 | Storage & Formats 全 6 词 · Observability 全 6 词 · Modeling 剩余 5 词 |

---

## 五、SEO 策略

### 词簇×意图矩阵

Glossary 按搜索意图承接三类关键词：

| 意图类型 | 示例 | 数量 | Glossary 如何承接 |
|---------|------|------|------------------|
| **定义型** | "what is semantic layer"、"data mesh explained" | ~32 词 | 每术语 H3 + 1–2 句定义；策略层 2–3 句 + Datus 关联待写入线上 |
| **对比型** | "ETL vs ELT"、"iceberg vs delta lake"、"star schema vs snowflake" | ~10 组 | 定义中自然嵌入对比；Dimensional Modeling / Star Schema 拆分后更易命中 |
| **关联型** | `MetricFlow`、`Cube.dev`、`DataHub` 等 | ~12 词 | 仍以 inline chip 出现在相关定义中；**dbt 已升为独立 term** |

### 结构化数据

JSON-LD `DefinedTermSet` + `DefinedTerm`——每个 term 一个 `DefinedTerm` 节点，含 `name`、`description`、`inDefinedTermSet`。作用：
- Google AI Overview 和 LLM 搜索引擎优先引用结构化 glossary 内容
- 提升 featured snippet 抓取率——定义型搜索的 glossary 页面天然适合回答框
- 未来 voice search（"Hey Google, what is a semantic layer?"）更可能取 glossary 结果

### 内链权重策略

- 每个术语：**聚合页短定义** → 「Read the full guide →」→ **`/blog/{slug}/`**
- Glossary 页面整体 → 向 `/products/*`、`studio.datus.ai`、docs 导流（线上页底已部分实现）
- 反向：blog 引用 glossary 锚点（`#modeling` 等）→ glossary 获反向权重
- 目标：glossary 在发布 6 个月后成为 Datus 站点中 backlink 最多的页面之一

---

## 六、线上实现状态与策略差距（2026-06-24）

| 维度 | 策略目标 | 线上现状 | 优先级 |
|------|---------|---------|:---:|
| **词表** | 46 词 · 7 类 | ✅ 已对齐 | — |
| **定义文案** | 2–3 句 + Datus 关联 | 通用英文短定义，**无** Datus 产品挂钩 | 高 |
| **Blog 深链** | 有长文的术语均挂链 | **10** 篇专用文 · **1** 篇已深链（Lakehouse） | 高 |
| **Inline chip** | dbt、MetricFlow 等互链 | **未实现** | 中 |
| **JSON-LD** | DefinedTermSet | **待验证 / 未实现** | 中 |
| **Datus 叙事** | 词表即立场 | 中立教科书语气 | 中 |
| **转化导流** | → `/agent`、`/products/*` | 页底 CTA → GitHub + Docs + Studio | 中 |
| **语言** | 策略中文 · 页面 EN | 线上纯英文 | 低 |

**近期待办（内容）**：

1. **P0**：为 §四对照表中 9 个已有专用 blog 的术语补 Glossary「Read the full guide →」深链  
2. 将策略层 Datus 关联句渐进写入聚合页定义（或仅在 blog 长文承载）  
3. 修复 hub 页 docs 死链：`/concepts/architecture/` → `/develop/Architecture/`（见 site-structure）  
4. 评估 JSON-LD `DefinedTermSet` 上线  
5. **P1–P2**：按 §四 backlog 为剩余 **35** 词（+ dbt 专用文）产出 `/blog/what-is-*` 或约定 slug

---

## 七、竞品视角

主流竞品中**没有一家建有公开 glossary**：

| 竞品 | 是否有 Glossary | Datus 机会 |
|------|:---:|------|
| Wren AI | ❌ 无 | 定义 "semantic layer"、"MDL"、"text-to-SQL"——在 Wren 还没做之前占位 |
| Cube.dev | ❌ 无 | 定义 "semantic layer"、"headless BI"、"metrics layer"——Cube 文档讨论这些概念但无结构化的 glossary |
| Altimate.ai | ❌ 无 | 定义 "data engineering harness"、"agentic dbt"——品类仍在成形 |
| TextQL / Ana | ❌ 无 | 定义 "AI data scientist"——概念仍有解释需求 |
| dbt Labs | 部分（docs glossary 仅 20 词） | dbt 的 glossary 严重偏 dbt 生态自指（dbt-specific 术语）——Datus 可做更大的行业通用 glossary |
| Databricks | 部分（docs glossary，但分散在多个页面） | 未做专门 /glossary 落地页——Datus 有机会在数据工程 glossary 这个品类率先卡位 |

**结论**：数据工程 glossary 是一个**未占领的品类空间**。Datus 先做就是品类定义者——后来者只能做「Datus glossary 的变体」。

---

## 八、成功指标

| 指标 | 6 个月目标 | 衡量方式 |
|------|-----------|---------|
| Glossary 页面月活 | 2K+ | Analytics |
| Featured snippet 占位 | 10+ 术语在 Google 回答框中出现 | Google Search Console |
| 内链导出 | 20+ 条 glossary → `/blog/`、`/products/*` | Crawl 分析（**当前 1/10 专用文已深链**） |
| JSON-LD 引用率 | 被至少 3 个外部 LLM 或搜索引擎引用 | 间接（可观测引用增长） |
| Backlink | 10+ 个外部引用（社区文章、Reddit 讨论） | Ahrefs / Search Console |
| 品牌搜索 | 「data engineering glossary」搜索结果前 3 | 手动搜索 |

---

*Glossary 策略 · Datus · https://datus.ai/glossary/ · 词表同步于 2026-06-24*
