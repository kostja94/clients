# Datus — 产品事实与竞品状态

> Phase 4 加载（产品提及、对比、案例）。本文件由人类维护，Agent 只读不追溯外部来源。

**As of June 2026 · v0.2.6**

---

## 1. 产品定位

| 项 | 内容 |
|----|------|
| **One-liner** | Open-source data engineering agent that builds evolvable context for your data systems |
| **品类** | data engineering agent（首选）、contextual data engineering、NL2SQL agent |
| **许可** | Apache 2.0 |
| **形态** | CLI + Web Chat + API + MCP Server |
| **差异化** | Context Engineering — evolvable context vs 一次性静态建模；Subagent 交付；跨栈 |

---

## 2. 核心能力（可引用）

### Context Engine

- **Physical 维度**：Catalog → Database → Schema → Table + Semantic Model
- **Logical 维度**：业务域 → Subject Tree（指标、Reference SQL、外部知识）
- **命令**：`/gen_semantic_model`, `/gen_metrics`, `/gen_sql_summary`
- **检索**：`@table`, `@metrics`, `@sql_history`, `@catalog`, `@subject`
- **冷启动**：`datus-agent bootstrap-kb` 从历史 SQL / Success Story

### Subagent

- Scoped Context 交付单元（~10 表、~20 指标、~30 Reference SQL）
- 域级 Chatbot；反馈回流优化 context
- Enterprise：RBAC 式作用域、PII 边界

### Feedback & Evaluation

- Upvote / Issue Report 闭环
- Evaluation：Exact Match, Result Count, Schema Usage, Semantic Correctness

### MCP

- **Client**：`.mcp add/remove/list/call` — 连接 Airflow 等外部工具
- **Server**：暴露 Datus DB 工具给 Claude Desktop 等
- 核心数据操作用原生工具；MCP 用于扩展

### Adapters / 跨栈

- Native DB Adapter：Snowflake, PostgreSQL, 等（10+ adapters）
- Spark adapter v0.2.6：Delta Lake, Hudi
- 向量：LanceDB, pgvector, Milvus（v0.2.4 向量化检索）

---

## 3. 可引用案例与数据

| Claim | 值 | 注意 |
|-------|-----|------|
| GitHub stars | ~1.2K | 标注 as of date |
| 云器 Lakehouse | 自助率 15%→60%；查询 30min→3min | 案例叙事；非 universal guarantee |
| POC | LinkedIn, Expedia, Coinbase | **POC 中**，非 GA  unless verified |
| 创始人 | 赵恒；前阿里 / StarRocks TSC | 背景 credibility |

---

## 4. 不是什么（写作边界）

| 禁表述 | 正确表述 |
|--------|---------|
| Datus 是 semantic layer 替代品 | Datus sits above / operationalizes semantic definitions |
| Datus 是唯一开源 DE agent | Datus is an open-source data engineering agent with evolvable context |
| 所有客户 production GA | POC / evaluation stage for enterprise names |
| Context Engine 是 glossary 词条 | 专有术语 → features 页；文中可作为实现举例 |

---

## 5. 竞品状态表

| 竞品 | 定位 | 状态 | Stars/Notes |
|------|------|------|-------------|
| **Wren AI** | GenBI / MDL semantic layer | 🟢 活跃 | ~9.8K；静态 semantic model |
| **Altimate.ai** | Agentic dbt harness | 🟢 活跃 | MIT；dbt-native |
| **TextQL (Ana)** | Enterprise AI data scientist | 🟢 活跃 | 闭源为主；Ana Small 开源 |
| **Cube.dev** | Semantic layer + Agentic Analytics | 🟢 活跃 | ~20K；Agentic Analytics GA 2025 |
| **Defog.ai** | SQLCoder / SQL agent | 🟢 活跃 | 模型+企业 copilot |
| **Dataherald** | NL→SQL | 🔴 关停 2024-12 | 赛道教训 |
| **Vanna.ai** | RAG text-to-SQL | ⚠️ 开源归档 2026-03 | Cloud 仍可用 |
| **Databricks Genie** | 平台 copilot | 🟢 平台产品 | 非独立 OSS agent |
| **Snowflake Cortex** | 平台 CLI/copilot | 🟢 平台产品 | 绑定 Snowflake |
| **dbt Labs** | dbt + MetricFlow | 🟢 活跃 | 生态 semantic layer |

**对比写作要求**：每篇须 ≥1 竞品/替代方案真实优势；≥1「何时非 Datus 更合适」场景（Glossary 可在 §5–7 或 FAQ）。

---

## 6. Datus vs 竞品一句话（中立）

| 对比 | Datus 角度 | 对方优势 |
|------|-----------|---------|
| vs Wren AI | Evolvable context + Subagent vs 静态 MDL | Wren 社区/文档成熟度 |
| vs Altimate | 跨栈 agent vs dbt harness | dbt manifest 深度集成 |
| vs Cube | Agent + living context vs semantic API + agent | Cube 语义层成熟度/stars |
| vs TextQL | 工程端 DE agent vs 分析端 AI data scientist | TextQL 企业 GTM/合规 |

---

## 7. 外部链接（CTA）

| 用途 | URL |
|------|-----|
| GitHub | https://github.com/Datus-ai/Datus-agent |
| Docs | https://docs.datus.ai |
| 官网 | https://datus.ai |
