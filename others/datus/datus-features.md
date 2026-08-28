# Datus — 功能

> **本文档职责**：核心功能模块（Subagent、Knowledge Base、Workflow、Memory 等），不含外部集成（LLM/数据库/存储/MCP 等见 [datus-integrations.md](./datus-integrations.md)）。  
> **引用**：[datus.md](./datus.md) 概览 | [datus-use-cases.md](./datus-use-cases.md) 场景 | [datus-site-structure.md](./datus-site-structure.md) 站点结构 | [datus-integrations.md](./datus-integrations.md) 集成

**最近更新**：2026-07-03（从 features.md 中提取集成相关内容到独立文档 datus-integrations.md；本文件仅保留核心功能）

---

## 一、产品矩阵（接口概览）

| 组件 | 形态 | 受众 | 说明 |
|------|------|------|------|
| **Datus-CLI** | 命令行工具 | Data Engineer | 交互式 SQL、Subagent 创建、Context 构建、MCP 工具调用 |
| **Datus-Chat** | Web Chatbot | Data Analyst / Business User | 多轮对话、Subagent 选择、反馈（Upvote/Issue Report） |
| **Datus API** | HTTP API | 其他 Agent / 微服务 | 稳定数据服务 API，从成熟 Subagent 导出，支持 SSE 流式 |
| **Datus MCP Server** | MCP 协议 | 外部 Agent | 将 Datus 的数据库和上下文搜索能力暴露为 MCP 工具 |

---

## 二、Context Engine（上下文引擎）

Datus 的核心基础层。从两个维度构建「活语义地图」：

### 物理维度（Physical / Catalog）

```
Catalog Service → Database → Schema → Table
                                      └── Semantic Model（维度、度量、口径说明）
```

- 从 Catalog Service 或数据库获取真实表结构，按层级自动构建
- Semantic Model 可贴附到 Table/View，补充业务语义（MetricFlow 兼容 YAML 格式）

### 语义维度（Logical / Subject）

```
业务域 → 一级主题 → 二级主题
                    └── 细粒度指标
                    └── 可复用 Reference SQL
                    └── 外部文本知识
```

- 围绕业务域构建主题树，承载指标、SQL 与外部知识
- 支持模型自动生成 + 工程师人工编辑

### 双路召回机制

| 召回方式 | 说明 |
|---------|------|
| **Tree 树形分类** | 精确层级匹配（domain → layer1 → layer2） |
| **Vector 向量语义搜索** | 跨所有上下文字段的语义匹配 |

### CLI 上下文命令

| 命令 | 说明 |
|------|------|
| `@catalog` | 浏览与编辑数据库 Schema / Table 上下文 |
| `@subject` | 浏览与编辑语义模型、指标、SQL 摘要 |
| `@table` / `@file` / `@metrics` / `@sql_history` | 注入特定上下文到对话 |
| `/gen_semantic_model` / `/gen_metrics` / `/gen_sql_summary` | 自动生成对应资产 |
| `datus-agent bootstrap-kb` | 批量冷启动知识库 |

---

## 三、Knowledge Base（知识库）

独立于 Context Engine 的多模态智能系统——将分散的数据资产转化为统一、可搜索的存储库。**7 个组件**：

### 3.1 Schema Metadata

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| 数据库结构理解与智能表推荐 | 表定义 DDL + 列信息 + 前 5 行示例数据 + 统计信息 | 按业务含义查表、语义搜索 |

**构建**: `datus-agent bootstrap-kb --database <ns> --components metadata --kb_update_strategy [check/overwrite/incremental]`

### 3.2 Semantic Models

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| 用语义信息丰富数据库模式 | 表结构、维度和度量标记、实体关系 | Schema Linking、智能 Join 构建、列使用模式（如 `FIND_IN_SET` 过滤） |

**存储粒度**：字段级（table / column / entity），标记 is_dimension / is_measure / is_entity_key。

**生成**: `/gen_semantic_model generate a semantic model for table <name>`

**数据源**: CSV（历史 SQL）或 YAML（MetricFlow 兼容格式）

### 3.3 Business Metrics

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| 标准化、可查询的业务 KPI | MetricFlow 指标定义 + subject tree 分类 | 直接通过 `query_metrics` 执行，消除重复 SQL |

**Metrics-First Strategy**: Agent 优先搜索已有指标 → 命中则直接执行指标查询 → 未命中才生成临时 SQL。

**生成**: `/gen_metrics Generate a metric from this SQL: SELECT ...`

**注意**: 当前仅支持单表查询生成指标，不支持多表 JOIN。

### 3.4 Reference SQL

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| 捕获、分析、搜索 SQL 专业知识 | 历史 SQL + LLM 摘要 + 标签分类 + subject tree | 按意图找 SQL、获取相似查询、学习模式 |

**构建**: `datus-agent bootstrap-kb --components reference_sql --sql_dir <path>`

**SQL 文件格式**: 每条 SQL 以 `;` 结束，注释行（`--`）自动关联为描述。

### 3.5 Reference Template

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| 生产级稳定 SQL 输出 | Jinja2 `.j2` 模板 + 参数元数据 + LLM 摘要 | 模板搜索、服务端渲染、参数值自动采样 |

**为何需要此组件**: LLM 生成的 SQL 每次可能不同——模板确保输出稳定。详见 [§九 Reference Template](#九reference-template-参数化模板)。

### 3.6 External Knowledge

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| 处理业务规则与概念 | 业务术语、规则、概念 + 层级分类 | 语义搜索、Agent 上下文增强、术语消歧 |

**两种构建模式**:
- **Direct CSV Import**: 预定义知识条目（subject_path, name, search_text, explanation）
- **AI Generation from Success Stories**: 从问答 SQL 对自动生成 + SQL 验证循环（最多重试 3 次）

**生成**: `/gen_ext_knowledge Extract knowledge from this sql: ...`

### 3.7 Platform Documentation

| 用途 | 存储内容 | 能力 |
|------|---------|------|
| SQL 生成前验证平台语法 | 官方文档按 platform + version 分块 | 导航浏览、文档检索、语义搜索、Web 回退 |

**管道**: `Fetch → Parse → Clean → Chunk → Embed → Store`

**三种来源**: GitHub repo、Website 爬取、本地目录。跨 namespace 共享存储。

> **存储后端**（LanceDB/SQLite、pgvector、Milvus）、**嵌入模型**（OpenAI / sentence-transformers）、**数据库适配器**、**LLM Provider** 等外部集成细节见 [datus-integrations.md](./datus-integrations.md)。

---

## 四、Subagent 系统

Subagent 是 Datus 的**核心交付单元**——面向具体场景的、Scoped Context 的专用 AI 助手。

### 4.1 Subagent 组成

| 组件 | 典型规模 | 说明 |
|------|----------|------|
| **Scoped Context** | ~10 张关键表 | 从全局上下文精选与业务域强相关的子集 |
| **核心指标** | ~20 个 | 从历史 SQL 与 Success Stories 自动抽取，MetricFlow 格式 |
| **Reference SQL** | ~30 条 | 高价值历史 SQL，自动分类标注 |
| **规则** | 若干 | 权限边界、数据质量规则、业务逻辑约束 |
| **专属工具** | 若干 | 从 db_tools / context_search_tools / semantic_tools / filesystem_tools 等按需组合 |
| **MCP Server** | 0~N | 可选接入外部 MCP 服务器扩展能力 |
| **Skills** | 0~N | 按 glob 模式匹配加载的技能（如 `report-*`, `sql-*`） |

### 4.2 内置 Subagent（8 种）

| Subagent | 用途 | 启动命令 |
|----------|------|---------|
| `gen_sql` | SQL 专家，处理复杂多表 JOIN，执行前自动验证 | 自动委托或手动调用 |
| `explore` | 只读探索 Agent，收集 Schema / 数据样本 / 知识库上下文 | 自动委托（写 SQL 前自动调用） |
| `gen_semantic_model` | 从 DDL 自动生成 MetricFlow 语义模型 YAML | `/gen_semantic_model` |
| `gen_metrics` | 从 SQL 自动提取可执行指标定义（单表限定） | `/gen_metrics` |
| `gen_sql_summary` | 分析和分类 SQL 查询，生成可搜索摘要 | `/gen_sql_summary` |
| `gen_ext_knowledge` | 从问答对中提取业务知识（双重验证循环） | `/gen_ext_knowledge` |
| `gen_report` | 生成结构化分析报告（可扩展子类如归因分析） | `/gen_report` |
| **自定义** | 用户通过 `agent.yml` 定义的领域专用 Subagent | `.subagent add` |

### 4.3 自动委托机制

Chat Agent 作为**编排层**，透明地决定何时将任务委派给 Subagent：

```
用户提问 → Chat Agent → {简单查询？} → 直接回答
                        → {需要探索表结构？} → 委托 explore
                        → {复杂多表 SQL？} → 委托 gen_sql
                        → {指标查询？}   → 优先 query_metrics
```

用户无需手动切换模式——自动路由。Subagent 事件通过 `depth` 和 `parent_action_id` 在 SSE 流中形成层级树结构。

### 4.4 Subagent 生命周期

```
Ad-hoc 探索与开发
  → 生成场景指标与 Reference SQL
    → 配置 Subagent 并交付 Chatbot（Web 界面，URL 直达）
      → 用户对话与反馈回流（Upvote / Issue / Success Story）
        → 优化与固化 Data Context
          → 导出为 API 供更大范围复用
```

### 4.5 CLI 管理命令

| 命令 | 说明 |
|------|------|
| `.subagent add` | 交互式创建 Subagent（名称、工具、规则、Scoped Context） |
| `.subagent list` | 列出已有 Subagent，含 Scoped Context / KB 路径 / 工具 / MCP / 规则 |
| `.subagent update <name>` | 更新配置，若影响 Scoped Context 自动触发 KB 重建 |
| `.subagent remove <name>` | 删除指定 Subagent |
| `.subagent bootstrap <name> [--components ...] [--plan]` | 构建/模拟 Scoped Context（metadata/metrics/reference_sql） |

### 4.6 配置示例

```yaml
agentic_nodes:
  school_report:
    node_class: gen_report
    tools: db_tools.*, context_search_tools.*
    mcp: metricflow_mcp
    skills: "report-*, data-*"
    model: deepseek
    max_turns: 30
    agent_description: "学校数据分析助手"
    rules:
      - 优先使用 context_search_tools 搜索已有指标
      - 查询前验证表是否存在
```

---

## 五、Workflow 引擎

将节点编排为可执行流水线，支持两种运行模式（Agentic / Workflow）。

### 5.1 三种内置工作流

| 工作流 | 节点序列 | 适用场景 |
|--------|---------|---------|
| **Fixed** | Schema Linking → Generate SQL → Execute SQL → Output | 简单查询，快速确定 |
| **Reflection** | Schema Linking → Generate SQL → Execute SQL → **Reflect** → Output | 复杂查询，自动修正 |
| **Metric-to-SQL** | Schema Linking → Search Metrics → Date Parser → Generate SQL → Execute SQL → Output | 标准化 KPI 报表 |

### 5.2 Reflection 机制

Reflection 工作流的核心智能。Reflect 节点评估执行结果后，可动态修改执行路径：

```
Reflect → 结果正确？→ Output
        → SQL 有误？→ Fix → Execute SQL → Reflect
        → 需要更多信息？→ Doc Search → Generate SQL → ...
        → 模式链接不精确？→ Schema Re-analysis → ...
```

### 5.3 高级编排能力

**并行执行** — 多策略竞品对比选择最佳结果：
```yaml
bird_para:
  - schema_linking
  - parallel:
    - generate_sql
    - reasoning
  - selection        # 从两个结果中选择更好的
  - execute_sql
  - output
```

**Sub-workflows** — 模块化复用，每个 sub-workflow 可独立配置文件：
```yaml
multi_agent:
  - schema_linking
  - parallel:
    - agent1_workflow   # 可使用独立的 agent1.yaml 配置
    - agent2_workflow
  - selection
  - output
```

### 5.4 工作流节点类型

| 类别 | 节点 | 说明 |
|------|------|------|
| **控制** | Reflect / Parallel / Selection / Subworkflow | 流程控制与决策 |
| **动作** | Schema Linking / Generate SQL / Execute SQL / Output / Reasoning / Fix / Compare / Date Parser / Doc Search | 数据处理与 SQL 任务 |
| **智能** | Chat Agentic / Gen Metrics / Gen Semantic Model / Search Metrics | AI 驱动的对话与生成 |

### 5.5 Workflow API

将工作流暴露为 REST API：
```json
// POST /workflows/run
{
  "workflow": "reflection",
  "namespace": "your_db",
  "task": "Show me quarterly revenue trends",
  "mode": "sync"     // 或 "async"（SSE 流式事件）
}
```

**异步模式 SSE 事件流**: `started → progress → node_progress → sql_generated → output_ready → done`

---

## 六、Continuous Learning Loop（持续学习闭环）

每次用户交互都回流到 Context Engine 与 Knowledge Base：

| 信号类型 | 来源 | 作用 |
|----------|------|------|
| **Upvote** | Datus-Chat | 正样本，强化该查询的 SQL 模式 |
| **Issue Report** | Datus-Chat | 负样本，标记为待修复（含 session link） |
| **Success Story** | 用户手动标记 | 高质量 SQL 对 → 纳入 Reference SQL 和 Metric 生成 |
| **Correction** | 多轮对话 | 语义校正，更新指标口径 |

**成功故事 CSV 格式**: `session_link, session_id, subagent_name, user_message, sql, timestamp`

**反馈写给数据工程师**: 收到 Issue Link → 修正 SQL → 更新规则与元数据 → 构建更多指标 → 扩展 Scoped Context → Subagent 持续改进。

---

## 七、Auto Memory（自动记忆）

无需配置的持久记忆系统——Agent 自动识别并记住有价值的信息。

### 架构

```
{workspace}/.datus/memory/
├── chat/                  # 内置 Chat Agent
│   ├── MEMORY.md         # L1 主文件：自动加载到上下文（≤200 行）
│   ├── patterns.md       # L2 子文件：按需读取
│   └── conventions.md    # L2 子文件
└── my_custom_agent/      # 自定义 Subagent（独立目录）
    ├── MEMORY.md
    └── domain.md
```

### 两层设计

| 层级 | 文件 | 限制 | 适合存储 |
|------|------|------|---------|
| **L1** | `MEMORY.md` | ≤200 行，每次对话自动加载 | 用户偏好、项目结构、常用规范、L2 链接 |
| **L2** | 主题子文件 | 无限制 | 详细调试笔记、复杂领域模式、长决策记录 |

### 启用范围

| Agent 类型 | 是否启用 |
|-----------|:---:|
| 内置 Chat Agent | ✅ |
| 自定义 Subagent | ✅ |
| 内置系统 Subagent（gen_sql, gen_report 等） | ❌ |
| explore | ❌ |

### 使用方式

```
> Remember that I prefer DuckDB
> Remember the project uses snake_case naming convention
> Forget my DuckDB preference
> That's wrong, our project uses PostgreSQL, not DuckDB   # 即时纠正
```

### Agent 自主判断存储规则

| ✅ 值得存储 | ❌ 不值得存储 |
|---|---|
| 多次交互确认的稳定模式 | 当前任务的临时细节 |
| 关键决策与项目结构 | 不完整、未验证的信息 |
| 用户偏好与工作流习惯 | 单次互动的推测性结论 |
| 重复出现问题的解决方案 | 进行中的工作状态 |

---

## 八、Plan Mode（计划模式）

交互式工作流功能——将复杂任务分解为可审查步骤，执行前人工确认。

### 激活方式

在 CLI 中按 **Shift+Tab** 切换 Plan Mode，再提交消息。

### 三阶段工作流

```
1. Plan Generation  → AI 分析需求，创建分步计划
2. User Confirmation → 选择执行模式
3. Execution        → 按选定模式执行
```

### 四种执行模式

| 模式 | 适用场景 |
|------|---------|
| **Manual Confirm** | 逐步审查——每步执行前显示进度（✓ 已完成 / ▶ 当前 / ○ 待处理），可继续/切换自动/修订/取消 |
| **Auto Execute** | 自动执行——定义明确、无需逐步审查 |
| **Revise** | 提供反馈重新生成计划（已完成步骤保留） |
| **Cancel** | 安全退出，不执行任何步骤 |

### 错误处理

步骤失败时：标记失败 → 手动模式暂停 → 可修订计划 → 已完成步骤保留。

---

## 九、Reference Template（参数化模板）

将 Jinja2 参数化 SQL 模板转化为智能可搜索知识库，确保**生产环境 SQL 输出稳定**。

### 解决的问题

- LLM 每次生成的 SQL 可能不同——模板确保一致性
- LLM 不知道参数有效值——模板自动推断类型并从数据库采样

### 模板示例

```sql
SELECT `Free Meal Count (Ages 5-17)` / `Enrollment (Ages 5-17)` AS free_rate
FROM frpm
WHERE `Educational Option Type` = '{{school_type}}'
  AND `Free Meal Count (Ages 5-17)` / `Enrollment (Ages 5-17)` IS NOT NULL
ORDER BY free_rate {{sort_order}}
LIMIT {{limit}}
```

### 参数自动推断

| 参数 | 自动识别类型 | 自动富化 |
|------|------------|---------|
| `school_type` | **dimension** (WHERE col = '{{...}}') | 解析 column_ref，查询 Top 10 常见值 |
| `group_column` | **column** (GROUP BY {{...}}) | 列出所有可用列名 |
| `sort_order` | **keyword** (ORDER BY ... {{...}}) | 推断允许值 `["ASC", "DESC"]` |
| `limit` | **number** (LIMIT {{...}}) | — |

### 四件套工具

| 工具 | 功能 |
|------|------|
| `search_reference_template` | 自然语言搜索模板（不返回 body 节省 token） |
| `get_reference_template` | 按 subject_path + name 获取完整模板 |
| `render_reference_template` | Jinja2 渲染为纯 SQL |
| `execute_reference_template` | 渲染并立即只读执行（一步到位） |

### Template-Only Mode

限制 Agent **只能**执行预批准模板（不自生成 SQL）：

```yaml
agentic_nodes:
  template_executor:
    system_prompt: ref_tpl     # 专用系统提示
    tools: reference_template_tools.*   # 仅模板工具，无 db_tools
```

---

## 十、集成与平台能力

Datus 依赖一系列可替换的底层基础设施和外部对接能力：

### 平台基础设施（Platform Capabilities）

Datus 在这些维度上**不是绑定单一供应商，而是让用户自己选配**：

| 维度 | 可选范围 | 详细文档 |
|------|---------|---------|
| **AI 引擎** | 6 家 LLM（OpenAI / Claude / DeepSeek / Qwen / Kimi / Gemini），按节点/Subagent 粒度指定不同模型 | [integrations §一](./datus-integrations.md#一llm-providersai-模型) |
| **存储引擎** | 3 种存储后端（LanceDB+SQLite / pgvector / Milvus），向量 + 关系型双轨 | [integrations §三](./datus-integrations.md#三存储后端storage-backends) |
| **嵌入引擎** | OpenAI Embeddings 或 sentence-transformers 本地模型，按数据层独立配置 | [integrations §四](./datus-integrations.md#四embedding-providers嵌入模型) |

### 外部工具连接（External Integrations）

| 维度 | 对接系统 | 详细文档 |
|------|---------|---------|
| **数据库** | 11 种数据库（Snowflake / PostgreSQL / MySQL / StarRocks / DuckDB / ClickHouse / Hive / Spark / Trino / ClickZetta / SQLite） | [integrations §二](./datus-integrations.md#二数据库适配器database-adapters) |
| **语义层** | MetricFlow（插件化架构，可自定义适配器） | [integrations §五](./datus-integrations.md#五语义层适配器semantic-adapters) |
| **BI 平台** | Apache Superset（Dashboard Copilot 一键生成 Subagent） | [integrations §六](./datus-integrations.md#六bi-平台dashboard-copilot) |
| **协议扩展** | MCP Client/Server（接入外部工具 + 暴露自身能力） | [integrations §七](./datus-integrations.md#七mcp-协议model-context-protocol) |
| **技能系统** | AgentSkills + Town Marketplace（社区技能发布/安装） | [integrations §八](./datus-integrations.md#八agentskills--skill-marketplace) |
| **第三方服务** | LangSmith / Tavily / LLM Trace / GitHub Token | [integrations §九](./datus-integrations.md#九可选集成optional) |

> 完整清单、配置示例、架构图和集成总览见 **[datus-integrations.md](./datus-integrations.md)**。

---

## 十一、Benchmark & Evaluation（评测体系）

### 支持的基准数据集

| 数据集 | 说明 |
|--------|------|
| **BIRD-DEV** | 复杂 SQL 生成综合测试（1533 任务） |
| **Spider2** | 高级多数据库 SQL 测试 |
| **Semantic Layer** | 业务指标和语义理解测试 |

### 评测维度

| 指标 | 说明 |
|------|------|
| **Exact Match** | SQL 文本精确匹配 |
| **Result Match** | 返回表格完全一致 |
| **Table Match** | 是否正确识别并使用相关表 |
| **Column Match** | 列级别是否匹配 |
| **Row Count Match** | 行数一致但值不同 |

### 多轮 Benchmark

支持重复执行基准测试 + 评估，自动生成跨轮次对比 Excel 报告：

```bash
datus-agent multi-round-benchmark \
  --database bird_sqlite --benchmark bird_dev \
  --workflow chat_agentic --round 4 --workers 2
```

*内置 California Schools 教程数据集，无需下载即可快速试跑。*

---

## 十二、发版记录（关键版本）

| 版本 | 日期 | 关键更新 |
|------|------|----------|
| v0.2.0 | 2025 | Agentic 执行、自动 KB 构建、MCP 扩展、Plan Mode（beta） |
| v0.2.3 | 2025 | 插件化 DB Adapter、内置教程数据集、评测框架 |
| v0.2.4 | 2025 | Dashboard Copilot、Semantic Adapter、向量化知识检索 |
| v0.2.5 | 2026 | OpenAI Agent SDK 0.7.0、Kimi-2.5 & Gemini-3、AgentSkills、MCP Server 导出、Reference SQL 并行化 |
| v0.2.6 | 2026 | AskUser Tool、Storage 插件化（LanceDB/pgvector/Milvus）、Session Resume/Rewind、Skill Marketplace CLI、Hive/Spark/ClickHouse/Trino 适配器 |
| v0.3.x（规划） | 2026 | 长期记忆增强、ChatBI API（一行 JS 嵌入）、数据工程全生命周期管理 |

---

## 十三、定价

| 版本 | 价格 | 说明 |
|------|------|------|
| **Open Source** | 免费 / Apache 2.0 | 核心 CLI + Context Engine + Subagent + 多模型 |
| **Cloud Personal** | 免费（云端） | 免安装体验，快速探索与试用 |
| **Enterprise** | 未公开（联系邮件） | 团队协作、企业访问控制、共享 Context Store、审计日志、SLA |

---

## 十四、平台覆盖

| 平台 | 状态 |
|------|------|
| **macOS / Linux** | 正式支持（`pip install datus-agent`） |
| **Web（Datus-Chat）** | 正式支持 |
| **MCP Client** | Claude Desktop / Claude Code 等 |
