# Datus — 竞品分析

> **本文档职责**：真实竞品矩阵、三圈竞争态势、差异化定位。  
> **引用**：[datus.md](./datus.md) 概览 | [datus-positioning.md](./datus-positioning.md) 定位 | [datus-features.md](./datus-features.md) 功能

**最近更新**：2026-07-03（新增 Seek AI / Prophecy / Microsoft Fabric Copilot / AWS SageMaker Data Agent / Devin，新增替代路径分析章节，新增组合替代方案视角）

---

## 前置说明

Datus.ai 太新，SEO 流量极低，Semrush 等工具的有机竞争对手数据在此无参考价值——匹配出的全是同名域名（datus.io、datus.tech 等）和泛流量站（Yelp、GitHub），不是品类竞品。以下按产品定位（AI 数据工程 Agent + 现代数据栈统一客户端 + Context/Memory Engine）梳理严格意义上的竞品，分三圈。

> **状态标注**：以下标注了各竞品的当前状态（活跃 / 关停 / 被收购 / 开源归档），供策略参考。

---

## 一、最直接竞品：AI 数据工程 / SQL Agent（同品类，正面竞争）

### 严格竞品矩阵

| 维度 | Datus | Wren AI | Altimate.ai | TextQL（Ana） | Cube.dev | Defog.ai |
|------|-------|---------|-------------|--------------|---------|----------|
| **定位** | Context Engineering Agent | 开源 GenBI / text-to-SQL + 语义层 | 开源 Agentic Data Engineering Harness for dbt | Enterprise AI data scientist（Ana） | Semantic Layer + Agentic Analytics | SQL agent + 企业数据 copilot |
| **状态** | 🟢 活跃 | 🟢 活跃 | 🟢 活跃 | 🟢 活跃 | 🟢 活跃 | 🟢 活跃 |
| **开源** | ✅ Apache 2.0 | ✅ | ✅ MIT | ❌（Ana Small 开源） | ✅ Apache 2.0 | ✅ SQLCoder 开源 |
| **GitHub Stars** | ~1.2K | ~15.5K | ~660 | — | ~20K | ~4K |
| **语义层** | ✅ 双维度 Context Tree | ✅ MDL-based | ❌（dbt manifest 驱动） | ✅ 集成式（Cube/Looker/dbt） | ✅ 核心能力 | 部分 |
| **交付形态** | CLI + Chat + API + MCP | Web + SDK | CLI + VS Code + npm | Web + Slack + Teams | REST + GraphQL + SQL | Cloud / Self-Hosted / Slack Bot |
| **Subagent** | ✅ 核心概念 | ❌ | ❌ | ✅ 多 Agent（Ana instances） | ❌ | ❌ |
| **Feedback Loop** | ✅ 持续进化 | ❌（静态） | ✅ ADE-Bench 74% F1 | 部分 | ❌ | ✅ 用户反馈学习 |
| **定价** | 开源 + Cloud Personal 免费 + Enterprise | 开源免费 + Cloud | 开源免费 | Free ($100/mo) / Team ($250/mo) / Enterprise | 开源免费 + Cloud | $5K/月起（企业） |

#### 已退出独立竞争的同品类产品

| 竞品 | 原定位 | 状态 | 对 Datus 的意义 |
|------|--------|------|----------------|
| **Dataherald** | 开源 NL→SQL agent 企业级 | 🔴 **关停**（2024-12 Out of Business） | 赛道清洗——NL-to-SQL 纯引擎模式难以独立生存 |
| **Numbers Station** | AI data analytics agent | 🟡 **被 Alation 收购**（2025-05） | 赛道验证——「Agent + Metadata」路径被 $1.7B 平台认可 |
| **Secoda** | AI-first Data Workspace | 🟡 **被 Atlassian 收购**（2025-12） | 方向收敛——AI data workspace 独立生存难度增加 |
| **Vanna.ai** | RAG-based text-to-SQL（~23.7K stars） | ⚠️ **开源归档**（2026-03），Cloud 仍可用 | 开源社区清洗——纯 RAG+NL2SQL 框架难以为继 |
| **Seek AI**（新增） | AI-native NL→SQL agent（SEEKER-1 自研模型，Spider 90%+） | 🟡 **被 IBM 收购**（2025-06），整合进 watsonx | 赛道验证——「NL→SQL + 语义建模」方向被 IBM 认可；Acquired 后独立竞争终止，向 IBM 生态靠拢 |

### 五个活跃严格竞品深度分析

#### 1. Wren AI — 最接近的竞品 🟢

**重叠**：开源 + 语义层 + Text-to-SQL Agent，定位最接近 Datus。  
**Wren AI 优势**：Star 数 ~13x Datus、MDL 语义建模工具更成熟、文档和社区更完善、已有 Cloud 托管版。  
**Datus 优势**：Context 是「活的」——可从历史 SQL 自动提取、随用户反馈持续更新，而非一次性建好；Subagent 将语义层封装为可交付的 Chatbot；CLI First 面向 Data Engineer 而非纯 Analyst。  
**关键差异**：Wren AI 是「建好语义模型 → 查询」的静态模式；Datus 是「上下文持续进化 → Subagent 交付 → Feedback 回流」的动态闭环。

#### 2. Altimate.ai 🟢（新增）

**重叠**：开源 + agentic data engineering + CLI + 多模型支持，**非常直接的同品类竞品**。Altimate Code 是 MIT 许可的 agentic data engineering harness，与 Datus 的定位高度相似。  
**Altimate 优势**：ADE-Bench 74.42%（超越 dbt Labs 团队 58.14%）；SQL 反模式检测 100% F1（1,077 条查询零误报）；**dbt 原生集成**（解析 dbt manifest）；从 VS Code dbt Power User 延伸的社区基础；MIT 许可。  
**Datus 优势**：Context Engine（双维度 Context Tree + 自动生成 + 持续进化）；Subagent 交付模型（Altimate 无此概念）；Apache 2.0 许可对企业更友好；覆盖 dbt 和非 dbt 生态。  
**关键差异**：Altimate 是「dbt 生态的 agentic harness」，Datus 是「跨栈的数据工程 Agent 平台」。Altimate 赢在 dbt 深度，Datus 赢在 Context 体系化。

#### 3. TextQL（Ana）🟢（新增）

**重叠**：NL→SQL + 语义层集成 + 多数据源，**直接竞品**。Ana 定位为"AI data scientist"，覆盖查询→分析→可视化的全链路。  
**TextQL 优势**：$17M 融资（Blackstone 领投），9x YoY 增长，>300% NDR；已有 Amazon、Dropbox、Scale AI 等头部客户；Dropbox 场景跨 400K+ 表、100K+ dashboards；SOC 2 Type II / HIPAA-ready；定价清晰（Free/Team/Enterprise）。  
**Datus 优势**：开源第一（TextQL 仅 Ana Small 开源）；工程侧定位（DE → Subagent 交付 vs TextQL 分析侧）；CLI First 开发者体验；Context Engine 持续进化。  
**关键差异**：TextQL 偏「分析端——AI data scientist」，Datus 偏「工程端——data engineering agent」。v0.3 framing：TextQL 类似 ChatBI 层，Datus 是系统层。

#### 4. Cube.dev 🟢（新增）

**重叠**：Semantic Layer + AI Agent，**方向收敛**。Cube 从语义层往上加 Agentic Analytics（Semantic Model Agent、Analytics Chat），Datus 从 Agent 往下做上下文。  
**Cube 优势**：~20K GitHub stars，成熟语义层产品（20+ 数据源、多重 API），Agentic Analytics GA（2025），$25M 融资（Databricks），~$7.9M ARR。  
**Datus 优势**：Context 是活的（持续进化 vs Cube 静态模型）；Subagent 交付；CLI First；AgentSkills 系统而非仅 Chat。  
**关键差异**：v0.3 framing——「Datus 不反 semantic layer，而是它的放大器和执行层」。但 Cube 不只是语义层（已在做 Agent），需关注双向挤压。

#### 5. Defog.ai / Introspect 🟢（SQLCoder）

**重叠**：SQL agent + 企业数据 copilot。Defog 自研 SQLCoder 模型系列（7B-2 / 70B / 34B），偏分析端。  
**Defog 优势**：自有模型（SQLCoder 可控）；$5K/月企业定价已验证；YC 背景。  
**Datus 优势**：开源 Agent 平台 vs 模型授权；Context Engine 体系化；多模型灵活选择。

### 其他同圈竞品（简要）

| 竞品 | 定位 | 状态 | 与 Datus 关系 |
|------|------|------|-------------|
| **Vanna.ai** | RAG-based text-to-SQL（~23.7K stars） | ⚠️ **开源归档**（2026-03），Vanna Cloud 仍可用 | 「上下文累积」思路高度相似，但 Vanna 是 Library 而非 Agent 产品；开源归档后社区可能向 Datus 迁移 |
| **Prophecy**（新增） | AI 数据准备与分析平台（v4 2026-02），基于 Claude Code Agent 生成可视数据工作流 | 🟢 活跃 | NL→代码（SQL/Spark）+ Git 存储 + Human-in-the-loop 验证；原生运行在 Databricks/Snowflake/BigQuery；偏 Analyst 侧可视画布 vs Datus CLI-first Engineer 定位 |
| **Julius AI / Hex Magic / Mode AI** | AI 数据分析助手 | 🟢 活跃 | 偏分析端，与 Datus 的 engineering 侧部分重叠 |
| **AskYourDatabase / SQLChat** | 轻量 NL-to-SQL | 🟢 活跃 | Datus 的功能子集 |

---

## 二、大公司平台绑定数据工程 Agent（正面竞争 + 结构性威胁）

> **关键变化**：2025-2026 年，五大云数据平台密集推出数据工程 Agent 产品——Databricks Genie Code（2026-03 GA）、Snowflake Cortex Code CLI（2025-11 发布，2026-02 跨栈扩展）、Google BigQuery Data Engineering Agent（2025-11 Preview → 2026-04 GA）、Microsoft Fabric Copilot（Preview）、AWS SageMaker Data Agent（2025-11 → 2026-03 扩展至 Query Editor）。这不再是"横向挤压"，而是**直接的同品类正面竞争**。

| 竞品 | 发布时间 | 核心能力 | 定价 | 威胁等级 |
|------|---------|---------|------|---------|
| **Databricks Genie Code** | 2026-03 GA | 自主 Pipeline 开发（Spark Declarative Pipelines）、24/7 主动监控、Unity Catalog 深度集成、MCP、Agent Skills、Memory、Agent Plan；内部测试 77.1% vs 通用 Agent 32.1% | **免费**（仅收 compute） | 🔴 高 |
| **Snowflake Cortex Code CLI** | 2025-11 → 2026-02 大幅扩展 | dbt + Airflow 支持、DS/ML Skill（Preview）、**独立订阅**（无需 Snowflake 账号！）、Claude Opus 4.6 / GPT-5.2 多模型选择、4,400+ 用户 | 独立订阅 + 按使用 | 🔴 高 |
| **Google BigQuery Data Engineering Agent** | 2025-11 Preview → **2026-04 GA** | NL Pipeline 创建、Knowledge Catalog 集成、Data Vault/Star Schema 建模、Data Agent Kit（MCP + VS Code + Claude Code + Gemini CLI）、BigQuery remote MCP Server；Vodafone **90%** ETL 迁移时间缩减 | 按 BigQuery 使用计费 | 🔴 高 |
| **Microsoft Fabric Copilot**（新增） | Preview（截至 2026-05） | Notebook 内嵌 Copilot（chat pane + in-cell）、Lakehouse schema 感知、多步代码生成与重构、Spark job 失败根因分析（"Fix with Copilot"）、跨 cell 端到端工作流 | 需 F2+ Capacity | 🟡 中高 |
| **AWS SageMaker Data Agent**（新增） | 2025-11 → 2026-03 扩展至 Query Editor | Glue Data Catalog 上下文感知、SQL + Python + PySpark 多语言生成、Redshift/Athena/S3 多数据源、"Fix with AI" 错误诊断、MCP 工具集成 | 按 AWS 使用计费 | 🟡 中高 |

### Datus v0.3 framing 应对

**对 Databricks Genie Code / Snowflake Cortex Code / BigQuery DE Agent / Fabric Copilot / SageMaker Data Agent 的统一叙事**：

> "Cortex Code and Genie Code are powerful first-party copilots for Snowflake and Databricks. Datus is for teams that want an **open, cross-stack data engineering agent** — not one bound to a single warehouse or control plane."

**关键注意事项**：
- Snowflake Cortex Code 已推出**独立订阅**（无需 Snowflake 账号），正在削弱"平台绑定"的经典 framing——Datus 需要强调"开源可自托管 vs 单一 vendor"
- Google BigQuery DE Agent + Data Agent Kit 提供 MCP 工具+IDE 集成，已直接覆盖 Datus「CLI + MCP」的价值层
- Microsoft Fabric Copilot 和 AWS SageMaker Data Agent 的加入表明**五大云平台全部入场**——差异化叙事从"我们不绑定单一平台"升级为"五大平台各有所长，只有 Datus 覆盖全部"
- 五家均免费或按使用计费——Datus 的"开源免费"不是独家优势

### 通用 Coding Agent（横向挤压）

> **组合替代方案视角**：单个通用 Agent 尚不能完全覆盖 Datus 的功能面，但组合方案可以——例如 `Cursor / Claude Code + Snowflake MCP + dbt MCP` 可覆盖 SQL 开发、Schema 探索、Pipeline 调试等多数 Datus 场景。MCP 生态越成熟，垂直 Agent 的 CLI 层越可能被通用 Agent + MCP 组合替代。

| 竞品 | 威胁点 | 威胁等级 |
|------|--------|----------|
| **Claude Code + dbt MCP** | 通用 Agent + MCP 直接覆盖 SQL 开发；v0.3 定位：不是对抗，是补位——「the data context layer for Claude Code」 | 🟡 中（已转为合作叙事） |
| **Cursor / Windsurf** | 通用 Coding Agent + MCP 可能替代 Datus CLI 层 | 🟡 中（同 Claude Code framing） |
| **Devin**（新增） | 自主 AI 软件工程师（Cognition Labs，$500/月）；已验证的数据工程案例：Nubank 6M+ 行 ETL 单体迁移（12x 效率）、AngelList 14K 仪表盘 Redshift→Snowflake 迁移（5.2x 加速）；通过 MCP 连接数据库和监控工具 | 🟡 中（自主 Agent 模式，非 IDE 插件） |
| **GitHub Copilot for Data** | 微软系生态压力 | 🟢 低中（深度不足） |
| **Continue.dev**（开源 IDE Agent，~32K stars） | 开源可定制，社区可能 fork 出数据专用分支 | 🟢 低（当前数据场景支持弱） |

---

## 三、传统现代数据栈工具（被 Datus「统一客户端」替代的对象，部分也在加 AI）

| 类别 | 代表竞品 | AI 化进展 | 与 Datus 关系 |
|------|----------|----------|-------------|
| **SQL IDE / 开发** | DataGrip, DBeaver, Hex, Deepnote, Querybook | Hex/Deepnote 已大力加 AI（Magic AI、AI block） | 被替代对象；Datus 的 CLI + Chatbot 是对 SQL IDE 的 Agent 化替代 |
| **dbt 生态** | dbt Cloud + dbt Copilot, Paradime（DinoAI v3.0 2026-04） | **dbt Copilot 是最大威胁**——同样做 SQL 开发 + 治理 + AI，且拥有 30K+ 客户的生态护城河；Altimate.ai 在此生态内竞争；Paradime 定位为「Cursor for Data」+ end-to-end DE Agent | 结构性威胁：dbt 生态太强，Datus 应定位为「dbt 的 Agent 层补充」而非替代；SDF（已退出独立竞争——2025-01 被 dbt Labs 收购，技术整合进 dbt Fusion） |
| **Semantic Layer → Agent** | **Cube.dev（新增）** | Cube 2025 年推出 Agentic Analytics（Semantic Model Agent、Analytics Chat），从语义层向 Agent 层挤压 | 方向收敛——v0.3 framing：Datus "sits above and around the semantic layer"，但 Cube 已不只是语义层 |
| **数据可观测 / 质量** | Monte Carlo, Bigeye, Elementary, Soda | 均加入 AI 异常检测和自然语言查询 | 覆盖 Datus 的 Quality / Monitoring 模块；当前 Datus 通过 MCP 集成（soda-core） |
| **Catalog** | DataHub, Atlan, Select Star | 均在加 AI copilot | 偏治理，与 Datus 互补 > 竞争 |
| **编排** | Airflow, Dagster, Prefect | Dagster 已加 AI agent，Prefect 有 AI workflow | 部分重合；Datus 的 Agent 编排 vs 传统 Pipeline 编排方向不同 |

---

## 四、竞争态势总结

### 真正的活跃贴身竞品（5 个）

| 竞品 | 定位 | 状态 |
|------|------|------|
| **Wren AI**（~15.5K stars） | 开源 + 语义层 + Text-to-SQL Agent | 🟢 活跃 |
| **Altimate.ai**（新增） | 开源 Agentic Data Engineering Harness for dbt | 🟢 活跃 |
| **TextQL / Ana**（新增） | Enterprise AI data scientist，$17M 融资 | 🟢 活跃 |
| **Cube.dev**（~20K stars，新增） | Semantic Layer + Agentic Analytics | 🟢 活跃 |
| **Defog.ai** | SQL agent + SQLCoder 模型 | 🟢 活跃 |

### 已退出独立竞争的赛道验证者

| 竞品 | 退出时间 | 状态 | 对 Datus 的价值 |
|------|---------|------|----------------|
| **Dataherald** | 2024-12 | 🔴 **关停** | 纯 NL-to-SQL 引擎模式难独立生存 |
| **Numbers Station** | 2025-05 收购 | 🟡 **被 Alation 收购**（$1.7B） | 「Agent + Metadata」赛道被头部验证 |
| **Seek AI**（新增） | 2025-06 收购 | 🟡 **被 IBM 收购**，整合进 watsonx | 「NL→SQL + 语义建模」被 IBM 认可；收购后独立竞争终止 |
| **Secoda** | 2025-12 收购 | 🟡 **被 Atlassian 收购** | AI data workspace 独立难 |
| **Vanna.ai** | 2026-03 归档 | ⚠️ **开源归档**，Cloud 仍可用 | 纯 RAG+NL2SQL 框架难持续 |

### 结构性威胁（7 个）

1. **Databricks Genie Code**（2026-03 GA）— **免费** + 自主 Pipeline + Unity Catalog 深度集成
2. **Snowflake Cortex Code CLI**（2026-02 跨栈扩展）— **独立订阅**、dbt/Airflow 支持、正在打破平台绑定
3. **Google BigQuery Data Engineering Agent**（2026-04 GA）— Data Agent Kit + MCP + 90% ETL 缩减
4. **Microsoft Fabric Copilot**（Preview）— Notebook 内嵌 + Lakehouse 感知 + Fix with Copilot 根因分析
5. **AWS SageMaker Data Agent**（2026-03 扩展）— Glue Catalog 感知 + 多语言代码生成 + MCP 集成
6. **dbt Cloud + Copilot** — 30K+ 客户生态护城河
7. **Cursor + MCP（通用 Agent 下沉）** — MCP 生态成熟时可能替代垂直 Agent CLI 层

### Datus 的竞争护城河（v0.3 更新版）

| 维度 | 护城河深度 | 说明 |
|------|-----------|------|
| **Context Engine（双维度 Tree + 持续进化）** | 中 | 设计独特——"自动生成 + 人工校准 + 持续进化"三位一体；Altimate 和 Cube 无等效能力 |
| **Subagent 交付模型** | 中 | 活跃竞品中仅 TextQL/Ana 有类似概念（多 Agent），但 Datus 的"Scoped Context → Chatbot → API"路径更完整 |
| **Feedback Loop 闭环** | 中高 | 持续进化是 Datus 核心理念——竞品多为静态模式；Altimate 有 ADE-Bench 但非持续反馈 |
| **开源跨栈（vs 大公司平台绑定）** | **中高🆕** | Genie Code/Cortex Code 各自平台绑定，Datus 是唯一开源跨栈选择 |
| **CLI First + 开发者体验** | 中 | "Run the modern data stack like a one-man data team"定位独特 |
| **GitHub Stars** | 🟡 低（当前） | 1.2K vs Wren 15.5K / Cube 20K，需加速 |

### Datus 的独特定位（一句话）

**Datus is the open-source data engineering agent that builds evolvable context for your data systems. From one-man data teams to enterprise agent teams, Datus turns data work into reliable, reusable agent systems.**

### 推荐策略（v0.3 更新）

1. **品类叙事第一**：「Contextual Data Engineering」和「Subagent 交付」是 Datus 独有的概念组合——竞品要么做语义层（Wren AI）、要么做 dbt harness（Altimate）、要么做 SQL 引擎（Dataherald 已关停）、要么做分析侧（TextQL），无人站在「工程侧 Agent 交付 + 开源跨栈」的交汇点
2. **不正面打功能矩阵**：通用能力（SQL 生成、多模型、MCP）终将成为 table stakes——重心放在「Context 进化」和「Subagent 交付闭环」
3. **借力竞品关停/收购**：Dataherald 关停 + Vanna 归档 + Numbers Station/Secoda 收购 → 赛道清洗期，Datus 是少数仍活跃的独立开源选择
4. **大公司平台：开放跨栈叙事**：vs Genie Code / Cortex Code / BigQuery DE Agent / Fabric Copilot / SageMaker Data Agent——Datus 不绑定任何单一 warehouse 或 control plane；五大云平台各自为战，多平台现实是 Datus 的天然护城河
5. **与 dbt 生态合作而非对抗**：Altimate 的 dbt 深度是差异化，Datus 覆盖 dbt 和非 dbt 生态
6. **加速 GitHub Star 增长**：当前 1.2K 从竞品对标看是最短板的短板

---

## 五、替代路径分析

Datus 被替代的真实路径不是"某个单一竞品赢了"，而是以下三种结构性替代路径之一：

### Path 1：平台吞掉 Agent 层

**路径**：Databricks Genie Code / Snowflake Cortex Code / BigQuery DE Agent / Microsoft Fabric Copilot / AWS SageMaker Data Agent → 凭借 warehouse 数据所有权 + 免费/按用量定价 + 原生分销优势 → Agent 层失去独立价值。

**触发条件**：任一平台将 data engineering agent 做到"足够好"且成本为零时，独立 Agent 产品的价值主张被严重削弱。

**Datus 防御**：开源跨栈——不绑定任何单一 warehouse 或 control plane；企业的多平台现实（multi-cloud / multi-warehouse）是天然护城河。

---

### Path 2：通用 Agent + MCP 塌缩垂直 Agent

**路径**：Cursor / Claude Code / Devin + Snowflake MCP + dbt MCP + warehouse tools → MCP 生态足够成熟时 → 通用 Agent 通过组合方案覆盖数据工程场景 → 垂直 Agent 不再必要。

**触发条件**：MCP 工具链达到"开箱即用"成熟度，数据团队无需额外配置即可让通用 Agent 完成数据任务。

**Datus 防御**：Context Engine ——通用 Agent 缺少持久化的数据上下文（Schema、Metric、Lineage、Business Logic），每次运行从零开始。Context 的积累和进化是通用 Agent 无法通过 MCP 简单替代的。

---

### Path 3：语义层向上吞掉 Context 层

**路径**：dbt / Cube.dev / Wren AI → 从语义层/建模层向上扩展 Agent 能力 → "Context" 不再是独立产品 → 被上游语义层吸收为功能模块。

**触发条件**：语义层产品将 Agent 能力作为内置功能（如 Cube Agentic Analytics GA），用户无需独立 Agent 层。

**Datus 防御**：Context 是"活的"——自动提取 + 人工校准 + Feedback Loop 持续进化，而非一次性建模后的静态语义模型。Datus 不反 semantic layer，而是它的放大器和执行层。

---

### 核心问题

三条路径的防御最终都指向同一个问题：

> **"Datus 的 Context Engine 是否能成为独立护城河？"**

如果答案是 yes——Datus 有机会成为 category leader。
如果答案是 no——它会被平台型玩家或通用 Agent 吞掉。

---

## 六、内容机会（竞品对比页）

| 路径 | 内容 | 优先级 | 策略 |
|------|------|--------|------|
| `/vs/wren-ai` | Datus vs Wren AI | 高 | 「动态进化 vs 静态建模」 |
| `/vs/altimate` | Datus vs Altimate.ai | 高🆕 | 「跨栈 Agent 平台 vs dbt 生态 harness」 |
| `/vs/textql` | Datus vs TextQL（Ana） | 高🆕 | 「工程侧 Agent 平台 vs 分析侧 AI data scientist」 |
| `/vs/cube` | Datus vs Cube.dev | 中高🆕 | 「Agent-first 上下文系统 vs 语义层 + Agentic Analytics」 |
| `/vs/defog` | Datus vs Defog.ai | 中 | 「工程侧 vs 分析侧」 |
| `/alternatives/vanna` | Vanna AI 替代品 | 中高🆕 | Vanna 开源归档——截获 23K Star 流量向 Datus 迁移 |
| `/alternatives/dataherald` | Dataherald 替代品 | 中🆕 | Dataherald 关停——截获历史流量 |
| `/alternatives/numbers-station` | Numbers Station 替代品 | 中高 | 「被收购了？开源替代方案」 |
| `/blog/datus-vs-dbt-copilot` | Datus 与 dbt Copilot 的关系 | 中 | 「不是替代，是 Agent 层补充」 |
| `/blog/datus-claude-code` | Datus vs Claude Code | 中高 | 「通用 coding agent vs 数据工程专用 context system」 |
| `/blog/datus-chatbi` | Datus vs ChatBI | 中 | 「ChatBI is the interface. Datus builds the system behind it.」 |
| `/blog/datus-semantic-layer` | Datus vs Semantic Layer | 中 | 「Semantic layers define metrics. Datus operationalizes them.」 |
| `/vs/databricks-genie-code` | Datus vs Databricks Genie Code | 中高🆕 | 「开源跨栈 vs 平台绑定 Agent」 |
| `/vs/snowflake-cortex-code` | Datus vs Snowflake Cortex Code | 中高🆕 | 「自托管开源 vs 独立订阅 + vendor 锁定」 |
| `/vs/bigquery-de-agent` | Datus vs Google BigQuery DE Agent | 中高🆕 | 「跨栈开源 vs BigQuery 生态 Agent」 |
| `/vs/fabric-copilot` | Datus vs Microsoft Fabric Copilot | 中🆕 | 「开源跨栈 vs Microsoft Fabric Notebook 内嵌 Copilot」 |
| `/vs/aws-sagemaker-agent` | Datus vs AWS SageMaker Data Agent | 中🆕 | 「独立 Agent 平台 vs AWS 生态 Data Agent」 |
| `/alternatives/seek-ai` | Seek AI 替代品 | 中🆕 | Seek AI 被 IBM 收购——截获"NL→SQL + 语义建模"历史流量 |
| `/vs/prophecy` | Datus vs Prophecy | 中🆕 | 「CLI-first 工程侧 vs 可视画布分析侧」 |
| `/blog/datus-devin` | Datus vs Devin | 中🆕 | 「数据工程专用 Context System vs 通用自主 Coding Agent」 |
