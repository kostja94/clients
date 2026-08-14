# Datus Glossary — 42 词表（distilled）

> Phase 0 加载。`blog_status: published` 的术语 **禁止** 在新文中重写完整定义（D1）。

**图例**：✅ published | 📝 backlog | 🔀 comparison-only canonical

---

## 速查表

| # | Term | Cat | Primary slug intent | blog_status | canonical_slug |
|---|------|-----|---------------------|----------------|-------------|----------------|
| 1 | Data Warehouse | A | what-is-data-warehouse | 📝 P1 | — |
| 2 | Data Lake | A | what-is-data-lake | 📝 P1 | — |
| 3 | Lakehouse | A | what-is-lakehouse | ✅ | what-is-lakehouse |
| 4 | Data Mesh | A | what-is-data-mesh | ✅ | what-is-data-mesh |
| 5 | Data Fabric | A | what-is-data-fabric | 📝 P0 | — |
| 6 | Medallion Architecture | A | what-is-medallion-architecture | 📝 P1 | — |
| 7 | Lambda vs Kappa | A | lambda-vs-kappa-architecture | 📝 P2 | — |
| 8 | Semantic Layer | B | what-is-semantic-layer | ✅ | what-is-semantic-layer |
| 9 | Metric Layer | B | what-is-metric-layer | ✅ | what-is-metric-layer |
| 10 | Dimensional Modeling | B | what-is-dimensional-modeling | 📝 P2 | — |
| 11 | Slowly Changing Dimensions | B | what-is-slowly-changing-dimensions | 📝 P2 | — |
| 12 | OBT (One Big Table) | B | what-is-one-big-table | 📝 P2 | — |
| 13 | Data Vault | B | what-is-data-vault | 📝 P2 | — |
| 14 | Columnar Storage | C | what-is-columnar-storage | 📝 P1 | — |
| 15 | Parquet | C | what-is-parquet | 📝 P1 | — |
| 16 | Apache Iceberg | C | what-is-apache-iceberg | 📝 P1 | — |
| 17 | Delta Lake | C | what-is-delta-lake | 📝 P1 | — |
| 18 | Apache Hudi | C | what-is-apache-hudi | 📝 P2 | — |
| 19 | OLAP vs OLTP | C | olap-vs-oltp | 📝 P1 | — |
| 20 | ETL vs ELT | D | etl-vs-elt | 📝 P0 | — |
| 21 | Batch vs Streaming | D | batch-vs-stream-processing | 📝 P2 | — |
| 22 | CDC | D | what-is-change-data-capture | 📝 P1 | — |
| 23 | Backfill | D | what-is-backfill-data-engineering | 📝 P2 | — |
| 24 | Idempotency | D | what-is-idempotency-data-pipeline | 📝 P2 | — |
| 25 | Materialized View | D | what-is-materialized-view | 📝 P2 | — |
| 26 | Data Catalog | E | what-is-data-catalog | ✅ | what-is-data-catalog |
| 27 | Data Contract | E | what-is-data-contract | 📝 P0 | — |
| 28 | Data Lineage | E | what-is-data-lineage | 📝 P1 | — |
| 29 | PII / Data Masking | E | what-is-data-masking | 📝 P2 | — |
| 30 | RBAC | E | what-is-rbac-data | 📝 P2 | — |
| 31 | Data Quality | E | what-is-data-quality | 📝 P1 | — |
| 32 | Text-to-SQL | F | what-is-text-to-sql | ✅ | what-is-text-to-sql |
| 33 | Schema Linking | F | what-is-schema-linking | ✅ | what-is-schema-linking |
| 34 | RAG | F | rag-data-engineering | ✅ | rag-data-engineering |
| 35 | MCP | F | what-is-mcp-data-engineering | 📝 P0 | — |
| 36 | Embedding | F | what-is-embedding-ai | 📝 P0 | — |
| 37 | Vector Search | F | what-is-vector-search | 📝 P1 | — |
| 38 | Data Observability | G | what-is-data-observability | 📝 P1 | — |
| 39 | SLA / SLO for Data | G | data-sla-slo | 📝 P2 | — |
| 40 | Anomaly Detection | G | data-anomaly-detection | 📝 P2 | — |
| 41 | Freshness | G | what-is-data-freshness | 📝 P2 | — |
| 42 | Volume / Schema / Distribution Checks | G | data-pipeline-monitoring-checks | 📝 P2 | — |

**额外 canonical（对比文，非上表独立 term）**：

| Term pair | blog_status | canonical_slug |
|-----------|-------------|----------------|
| Semantic Layer vs Ontology | ✅ | semantic-layer-vs-ontology |

---

## Datus 角度速查（写作时可自然引用）

### Category A — Architecture

**Data Warehouse** — 集中式 schema-on-write 分析仓库。Datus 通过 Native DB Adapter（Snowflake、PostgreSQL）直连，用 schema 构建 Context Tree。

**Data Lake** — schema-on-read 对象存储。Datus 通过 catalog service 读 lake metadata，生成 semantic model。

**Lakehouse** — lake 灵活性 + warehouse ACID/SQL；开放表格式 Iceberg/Delta/Hudi。云器 Lakehouse 案例：自助率 15%→60%。

**Data Mesh** — 域分散治理；Subject Tree 映射域结构 → 每域 Subagent。（✅ canonical）

**Data Fabric** — 元数据驱动统一访问；集中集成 vs mesh 去中心化。Datus 更贴近 mesh。

**Medallion Architecture** — Bronze/Silver/Gold 分层；agent 可跨层从 Gold 指标引导、探索 Silver 结构。

**Lambda vs Kappa** — 批流双管线 vs 单流回放。Datus 当前以批为主。

### Category B — Modeling

**Semantic Layer** — 业务表示层；Datus「活」semantic layer：Physical Catalog × Logical Subject，`/gen_semantic_model`。（✅）

**Metric Layer** — 指标子集；`/gen_metrics` → MetricFlow YAML → Subagent context。（✅）

**Dimensional Modeling** — 事实/维度；Semantic Model 理解 measures vs dimensions。

**SCD** — Type 1/2/3；Semantic Model 标注 SCD 类型。

**OBT** — 宽表反范式；Context Engine 识别宽表列语义。

**Data Vault** — hub/link/satellite；Catalog 维度建模 Vault 结构。

**Semantic Model** — （✅ canonical `what-is-semantic-model`）

### Category C — Storage / Format

**Columnar Storage** — 列存分析优化；agent SQL 受益于列存引擎。

**Parquet** — lake 主导列存格式；读 schema 建 Catalog。

**Iceberg** — 开放表格式 ACID/时间旅行；adapter 连接；schema 演化 ↔ evolvable context。

**Delta Lake** — Databricks/Spark 生态；Spark adapter v0.2.6。

**Hudi** — upsert/delete 流式；Hive/Spark adapter v0.2.6。

**OLAP vs OLTP** — Datus 面向 OLAP 分析负载。

### Category D — Processing

**ETL vs ELT** — Transform 阶段 agent 生成 SQL、捕获 Reference SQL。

**Batch vs Streaming** — 当前批为主；流式 context 为远期。

**CDC** — schema 漂移 + backfill 复杂性；Context Engine 未来变更感知。

**Backfill** — 生成 SQL 模板、血缘识别、Reference SQL 验证。

**Idempotency** — agent 应生成幂等 SQL 并标记非幂等模式。

**Materialized View** — 纳入 Catalog；避免冗余查询生成。

### Category E — Governance

**Data Catalog** — 发现元数据；Datus Catalog Service 面向 agent 消费。（✅）

**Data Contract** — 生产者/消费者协议；Subagent rules + Semantic Model 标注 ≈ 轻量 contract。

**Data Lineage** — Catalog Tree + Reference SQL 隐式血缘。

**PII / Masking** — Enterprise Subagent 作用域排除/masking PII 列。

**RBAC** — Subagent scoped context ≈ 域级 RBAC。

**Data Quality** — Evaluation Framework + Feedback Loop 应用于 AI SQL 输出。

### Category F — AI & Agents

**Text-to-SQL** — Context Engine + 反馈闭环。（✅）

**Schema Linking** — Catalog × Subject 双维度 Context Tree。（✅）

**RAG** — `@table`、`@metrics`、`@sql_history`；`@catalog`、`@subject`。（✅）

**MCP** — MCP Client + Server；扩展性 vs 原生工具核心。

**Embedding** — 向量化检索历史 SQL；LanceDB/pgvector/Milvus。

**Vector Search** — 检索 Reference SQL/指标，术语不一致仍语义匹配。

**Data Agent** — （✅ canonical `what-is-data-agent`）

### Category G — Observability

**Data Observability** — MCP 集成 soda-core；Evaluation + Feedback。

**SLA/SLO** — 长运行 agent 需知 SLO 定优先级。

**Anomaly Detection** — Feedback/Success Story 浮出异常模式。

**Freshness** — Subagent rules 检查 freshness 约束。

**Volume/Schema/Distribution** — Evaluation Framework 追踪 Schema Usage。

---

## 明确不纳入 glossary 词条

- Datus 专有：Context Engine、Subagent、Scoped Context → features 页
- 纯 CS：ACID、CAP、MapReduce
- 非 DE AI：fine-tuning、RLHF、transformer architecture

---

## Backlog 批次建议

| Batch | 术语 | 类型 |
|-------|------|------|
| **P0** | Lakehouse, ETL vs ELT, Data Contract, MCP, Embedding | Term / Comparison |
| **P0** | Data Fabric vs Data Mesh | Comparison |
| **P1** | Data Warehouse, Data Lake, Medallion, CDC, Data Quality, Iceberg, Delta, Parquet, OLAP vs OLTP, Data Lineage, Vector Search, Data Observability | Term / Comparison |
| **P2** | 其余 | Term / Comparison |
