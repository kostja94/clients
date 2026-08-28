# Datus — 应用场景

> **本文档职责**：人物画像、典型场景、使用旅程、竞品定位、选型建议；链至 Features。  
> **引用**：[datus.md](./datus.md) 概览 | [datus-features.md](./datus-features.md) 功能 | [datus-keywords.md](./datus-keywords.md) 关键词 | [datus-integrations.md](./datus-integrations.md) 集成

**最近更新**：2026-07-03（重写 P4 为「企业评估用户」并标注 POC 状态；新增竞品定位与选型章节；新增背景章节「从 Data Engineering 到 Contextual Data Engineering」；新增已知限制章节；ROI 数据标注来源）

---

## 〇、背景：从 Data Engineering 到 Contextual Data Engineering

2026 年，数据工程正在经历范式转移——从"建表建 Pipeline"转向"为 AI Agent 构建可进化的上下文层"。行业内多个玩家从不同角度切入同一方向：

- **Atlan**：企业级 Context Engineering 框架，强调治理与编排
- **Datafold**：Data Knowledge Graph，AI 自动收集 lineage + 业务逻辑 + 使用统计
- **Datus**：聚焦于让**数据工程师主动构建、迭代并交付 Scoped Context** 给分析师和其他 Agent

Datus 的独特之处在于：它不是黑盒 Agent，也不是平台锁定的内置工具，而是一个开源的、工程师可控的上下文构建系统——你将 SQL 历史、表结构、指标定义、业务规则持续注入，系统持续进化，最终以 Subagent 形态交付。

---

## 一、人物画像（Personas）

### P1：数据工程师（Data Engineer）

- **身份**：10 人以上数据团队的数据工程师、数据架构师
- **场景**：日常取数需求对接、数据口径管理、新表探索、SQL Review、Pipeline 维护
- **痛点**：不断变化的新需求沟通成本高、繁琐的数据验证流程、面对不熟悉表结构与血缘时的理解成本高、SQL 开发效率并非核心瓶颈
- **关键诉求**：**快速召回与复用历史 SQL 与口径沉淀**、上下文的系统化管理与持续进化、将重复性工作封装为可交付的 Chatbot
- **触发搜索**：*data engineering agent*、*data context system*、*NL2SQL CLI*、*context engineering*、*modern data stack agent*
- **产品触点**：Datus-CLI + Context Engine + Subagent 创建

### P2：数据分析师（Data Analyst）

- **身份**：数据分析师、BI 分析师、业务分析师
- **场景**：自助取数、临时分析、指标查询、周报/月报数据准备
- **痛点**：不会 SQL 或不熟悉复杂的表结构、每次取数都要找工程师沟通口径、等待排期时间长
- **关键诉求**：**自然语言自助查询**、多轮对话校正意图、理解业务术语（GMV/UV/DAU 等）、可导出结果
- **触发搜索**：*AI data analyst*、*chat with database*、*natural language SQL*、*self-service analytics*
- **产品触点**：Datus-Chat + Scoped Context Subagent

### P3：数据团队 Leader / CDO

- **身份**：数据团队负责人、数据总监、CDO
- **场景**：推动团队 AI 化转型、评估 ROI、数据治理规划
- **痛点**：团队隐性知识（数据潜规则、指标黑话、SQL 标准）散落在人脑中无法系统化；数据分析自助率低、查询响应时间慢
- **关键诉求**：**可量化的 ROI**（自助率提升、查询时间缩短）、数据治理规则从「事后」转向「事中」、Agent 交付而非工具交付
- **触发搜索**：*AI data team transformation*、*data engineering agent ROI*、*data self-service platform*、*contextual data engineering*
- **产品触点**：企业版 + 案例研究（云器 Lakehouse 生产部署：自助率 15%→60%，查询时间 30min→3min ⚠️ *单一客户案例，不具备普遍性*）

### P4：企业评估用户（POC → Enterprise）

*注意：以下企业目前处于**概念验证（POC）阶段**，并非已签约付费客户。*

- **身份**：LinkedIn、Expedia、Coinbase 等大型企业数据平台团队（POC 阶段）
- **场景**：评估 AI Agent 在企业数据栈中的可行性、验证安全合规边界、测试多数据源统一查询
- **痛点**：复杂血缘关系、安全合规要求、多租户管理、大模型在企业环境中的可审计性
- **关键诉求**：**安全稳定可审计**的 Agent 交付、Subagent 粒度的权限隔离、与现有数据栈集成（Snowflake 等）
- **触发搜索**：*enterprise data agent*、*data engineering agent for Snowflake*、*secure NL2SQL enterprise*
- **产品触点**：Enterprise 评估版 + Native DB Adapter + Subagent 权限管理
- **产品成熟度说明**：当前为 Alpha 阶段（PyPI 标记 "3 - Alpha"），**SSO、审计日志、SLA 等企业级特性仍在规划中**。

### P5：开源社区用户

- **身份**：个人开发者、小型团队、学生、数据工程师（个人使用）
- **场景**：探索 AI Agent 在数据工程中的应用、个人项目、学习 Context Engineering
- **痛点**：想体验「builds evolvable context for your data systems」的概念、需要低成本试用的方案
- **关键诉求**：**免费开源**、pip install 一键安装、内置教程数据集、清晰的文档
- **触发搜索**：*open source data engineering agent*、*GitHub data engineering agent*、*evolvable context for data*
- **产品触点**：GitHub 开源版 + docs.datus.ai + Quickstart Guide
- ⚠️ **平台限制**：当前仅正式支持 macOS / Linux，Windows 理论可行但未充分测试

---

## 二、典型使用旅程

### 旅程 A：数据工程师沉淀上下文并交付 Subagent

1. 数据工程师发现团队频繁被问「某业务线的 GMV 是多少」
2. 打开 Datus-CLI → `datus-agent bootstrap-kb` 从历史 SQL 和 Success Stories 冷启动知识库
3. `@catalog` 浏览该业务线涉及的表 → `/gen_semantic_model` 自动生成 Semantic Model
4. `@subject` 浏览语义维度 → `/gen_metrics` 自动生成 GMV 相关指标
5. `/gen_sql_summary` 自动总结高价值历史 SQL
6. `.subagent add` 创建 Scoped Context Subagent（选定 ~10 张表、~20 个指标、~30 条 SQL）
7. 将 Subagent 部署为 Datus-Chat → 分享链接给分析师
8. 分析师自助查询 → Upvote/Issue Report 回流 → 工程师根据反馈优化 Context
9. Subagent 成熟后导出为 Datus API → 供其他系统调用

### 旅程 B：数据分析师自助查询

1. 收到工程师分享的 Subagent 链接 → 打开 Datus-Chat
2. 输入自然语言问题：「上周各渠道的 GMV 对比，包含环比变化」
3. Subagent 自动检索 Scoped Context → 生成 SQL → 执行 → 返回结果表格
4. 发现结果中缺少某渠道 → 查看是否在 Scoped Context 覆盖范围内
5. 确认结果没有问题 → 点 Upvote；确认有误 → 提交 Issue Report（含 session link）
6. 导出结果 CSV → 用于 Excel 进一步分析
7. 工程师收到 Issue Report → 调整 Subagent Context，补充缺失的表和指标

### 旅程 C：数据团队 Leader 评估与采购

1. 搜索 *data engineering agent* / *AI data team transformation* → 发现 Datus
2. 阅读创始人博客「裸辞半年，我终于把 data engineering agent 开源了」→ 认同 Bitter Lessons
3. 查看云器 Lakehouse 案例：自助率 15%→60%，查询时间 30min→3min（⚠️ *单一客户案例，实际效果因团队和数据环境而异*）
4. Star GitHub → `pip install datus-agent` 试用内置教程数据集（California Schools）
5. 在团队内部用测试库跑通 → 确认满足需求
6. 联系 Datus 团队 → 进入 POC → 企业版评估
7. 部署到生产环境 → 逐步将各业务线封装为 Subagent → 交付给分析师

### 旅程 D：开源贡献者参与社区

1. 在 Hacker News / Reddit r/dataengineering 看到 Datus
2. Star + Fork GitHub → `pip install datus-agent`
3. 跑通 Quickstart Guide（内置 California Schools 数据集）
4. 发现 Bug 或 Feature Request → 提 Issue / PR
5. 开发自定义 DB Adapter → 提交 PR
6. 参与社区讨论（Discord/GitHub Discussions）

---

## 三、场景覆盖度评估

| 场景 | 产品匹配度 | 内容缺口 |
|------|-----------|----------|
| 数据工程师上下文管理 | 高（核心场景，CLI + Context Engine） | 更多数据库适配器、RBAC 权限管理 |
| 数据分析师自助查询 | 中高（Datus-Chat + Subagent） | 图表可视化、多轮对话体验优化 |
| 企业级多租户部署 | 中低（Alpha 阶段，POC 进行中） | SSO、审计日志、SLA、专属支持 |
| 数据治理自动化 | 中（规则内化到 Agent） | 数据质量工具 MCP 集成（soda-core 等） |
| 开源社区贡献 | 中（GitHub + Docs） | 贡献者指南、开发者文档、Community Call |
| BI Dashboard Copilot | 中（v0.2.4 Dashboard Copilot） | 更多 BI 工具适配（目前仅 Superset） |
| dbt 工作流集成 | 低（无原生 dbt 集成） | 当前需通过 MCP 或手动导入 SQL；深度 dbt 集成用户建议考虑 Altimate |

---

## 四、竞品定位与选型建议

### 4.1 赛道格局（2026）

2026 年 Data Engineering Agent 赛道可分四类：

| 类型 | 代表产品 | 核心特点 | 适合谁 |
|------|---------|---------|--------|
| **开源 Agent 框架** | Datus、Wren AI、Altimate | 多数据仓库、可自托管、上下文可持久化 | 异构数据栈、需要可审计上下文 |
| **平台内置 Agent** | BigQuery DEA、Snowflake Cortex Code | 零配置、深度平台集成、安全边界内运行 | 单平台全部署、追求开箱即用 |
| **Prompt-as-Agent** | Claude Code Subagent | 零基础设施、即时可用 | 临时探索、不需要持久化上下文 |
| **闭源 SaaS** | Datafold DKG、InfiniSynapse | 企业级治理、自动上下文收集 | 有预算、需要全托管方案 |

### 4.2 Datus vs. 主要竞品

| 维度 | Datus | Wren AI | Altimate | 平台内置 Agent |
|------|:---:|:---:|:---:|:---:|
| **开源协议** | Apache 2.0 | Apache 2.0 | MIT | ❌ 闭源 |
| **核心差异化** | Context Engine + Subagent 交付 | MDL 语义层 + GenBI 生成 Dashboard | dbt-native + 100+ 确定性工具 | 零配置、平台深度集成 |
| **数据源覆盖** | 11 种数据库 | 22+ 种（JDBC） | Snowflake/DuckDB/PG/MongoDB/SQLite | 单一平台 |
| **上下文持久化** | ✅ 双路召回（Tree + Vector） | ✅ MDL + 记忆（发展中） | ❌ 无独立 Context Engine | ✅ 平台元数据 |
| **Subagent 体系** | ✅ Scoped Context Subagent | ❌ 无此模式 | ❌ 无此模式 | 部分支持 |
| **生成可视化** | ❌ 不生成 Dashboard | ✅ GenBI 一键部署 | ❌ | 部分支持 |
| **dbt 集成** | ❌ 需手动导入 | ❌ | ✅ 深度集成 | 部分支持 |
| **第三方 Benchmark** | ❌ 无独立认证 | ❌ 无独立认证 | ✅ ADE-Bench/DAB #1 | 平台内 Benchmark |
| **SQL 准确率（公开数据）** | BIRD-DEV 63% (30 queries, Nov 2025) | 未公开 | ADE-Bench 78% (32/41 tasks) | 未独立公开 |
| **社区规模** | ⭐1,288  | 远大于 Datus | — | 平台驱动 |
| **成熟度** | Alpha (v0.3.5) | 活跃迭代中 | 生产可用 | 生产可用 |

### 4.3 选型决策树

```
你的场景是？
├── 全栈在单一云平台，不想折腾 → 平台内置 Agent（BigQuery DEA / Cortex Code）
├── 重度使用 dbt，需要 Agent 直接操作 dbt 模型 → Altimate
├── 需要分析师自助生成可分享的 Dashboard → Wren AI
├── 只需要偶尔探索，不需要持久化 → Claude Code Subagent
├── 多数据仓库、需要可进化的上下文、需要交付 Subagent 给分析师 → Datus ✅
└── 企业级全托管、有预算 → 联系 Datafold / InfiniSynapse
```

### 4.4 当你**不应该**选择 Datus

> 以下场景 Datus 并非最佳选择，诚实建议：

| 场景 | 推荐替代方案 | 原因 |
|------|------------|------|
| 整个数据栈仅在 BigQuery | BigQuery DEA | 零配置、IAM 原生集成，Datus 的跨仓库优势无法发挥 |
| 整个数据栈仅在 Snowflake | Snowflake Cortex Code | 安全边界内运行，省去部署运维成本 |
| 重度依赖 dbt 工作流 | Altimate | dbt-native，Benchmark 排名第一 |
| 需要分析师自助生成 Dashboard | Wren AI | GenBI 一键部署 Dashboard 到 Vercel |
| 仅需临时探索，不需要积累 | Claude Code Subagent | 零基础设施，即时可用 |
| 对产品成熟度要求高 | 平台内置 Agent / Altimate | Datus 目前为 Alpha 阶段 |

---

## 五、已知限制（v0.3.5）

*本节对照 [datus-integrations.md](./datus-integrations.md) 中的公开数据，如实列出。*

| 限制 | 影响场景 | 说明 |
|------|---------|------|
| 指标自动生成仅支持单表 | P1/P2 | `gen_metrics` 和 `gen_ext_knowledge` 不支持多表 JOIN |
| Dashboard Copilot 仅 Superset | BI 场景 | 暂无 Tableau / PowerBI / Looker / Metabase |
| 语义层仅 MetricFlow | 语义层场景 | 插件架构支持自定义适配器，但官方仅提供 MetricFlow |
| 无 SSO / 审计日志 / SLA | P3/P4 企业场景 | 当前为 Alpha，企业级特性规划中 |
| Windows 未正式支持 | P5 开源社区 | pip install 可尝试，但团队未充分测试 |
| Python ≥ 3.12 | 所有场景 | 不支持更早版本 |
| BIRD-DEV 通过率 63% | 所有 NL2SQL 场景 | 30 queries test (Nov 2025)；带上下文后准确率有显著提升 |
| 默认存储适合开发/单机 | P3/P4 企业场景 | 生产环境建议 pgvector 或 Milvus |
