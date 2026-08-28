# Datus — 集成（Integrations）

> **本文档职责**：Datus 对接的所有外部系统、服务与协议——LLM / 数据库 / 存储 / 语义层 / BI 平台 / MCP / Skills / Embedding 等。  
> **引用**：[datus-features.md](./datus-features.md) 功能 | [datus.md](./datus.md) 概览

**最近更新**：2026-07-03（从 datus-features.md 中提取 + docs.datus.ai 爬取补全：新增 Embedding Providers / Semantic Adapters / LangSmith / Tavily；新增 §十一 事实数据附录：GitHub 指标、PyPI 数据、Benchmark 分数、数据库能力矩阵等营销可用素材）

---

## 一、LLM Providers（AI 模型）

Datus 通过统一的 `agent.yml` 模型配置层对接 6 家 LLM 厂商，支持按节点/Subagent 粒度指定不同模型。

| Provider | 模型 | Interface Type | 接入版本 | 说明 |
|----------|------|:---:|:---:|------|
| **OpenAI** | GPT-4, GPT-5, GPT-4-turbo | `openai` | 原生 | 默认主力模型 |
| **Anthropic** | Claude 4 (Sonnet, Opus), Claude 3 | `claude` | 原生 | Agentic 场景推荐 |
| **DeepSeek** | DeepSeek Chat, DeepSeek Reasoner | `deepseek` | 原生 | 高性价比选择 |
| **Qwen（通义千问）** | Qwen-Turbo, Qwen3-Coder-Plus | `openai` (兼容) | 原生 | 中文场景优化 |
| **Kimi（Moonshot）** | Kimi-K2.5, Kimi-k2-turbo-preview | `openai` (兼容) | v0.2.5 | 长上下文场景 |
| **Gemini（Google）** | Gemini-2.5-flash, Gemini-3 系列 | `gemini` | v0.2.5 | Google 生态 |

### 认证方式

| Provider | 支持的认证类型 | 说明 |
|----------|-------------|------|
| OpenAI / DeepSeek / Qwen / Kimi / Gemini | API Key (`${ENV_VAR}`) | 标准方式，所有 provider 支持环境变量注入 |
| Claude | API Key 或 Subscription Token | 支持 `auth_type: subscription`，自动检测本地 credential |
| Codex | OAuth | 使用本地 Codex OAuth credential 验证连接 |
| Azure OpenAI | API Key | Enterprise 部署，需配置 endpoint + deployment name |
| 自托管模型 | 自定义 API Key | 任何 OpenAI 兼容接口均可配置 `base_url` + `api_key` |

### 可观测性集成

| 工具 | 用途 | 配置方式 |
|------|------|---------|
| **LangSmith** | LLM 调用追踪与调试 | `LANGSMITH_TRACING=true` + `LANGSMITH_API_KEY` + `LANGSMITH_PROJECT` |
| **Langfuse** | Agent/Tool 全链路追踪 | `LANGFUSE_PUBLIC_KEY` + `LANGFUSE_SECRET_KEY` + `LANGFUSE_HOST`；支持 OTel (OpenInference) |
| **LLM Trace** | 本地 YAML 调试输出 | `--save_llm_trace` flag，输出到 `{agent.home}/trajectory/` |

### 配置示例

```yaml
agent:
  target: openai                     # 默认模型

models:
  openai:
    type: openai
    base_url: https://api.openai.com/v1
    api_key: ${OPENAI_API_KEY}
    model: gpt-4-turbo

  anthropic:
    type: claude
    base_url: https://api.anthropic.com
    api_key: ${ANTHROPIC_API_KEY}
    model: claude-sonnet-4-20250514

  deepseek:
    type: deepseek
    base_url: https://api.deepseek.com
    api_key: ${DEEPSEEK_API_KEY}
    model: deepseek-chat

  gemini:
    type: gemini
    base_url: https://generativelanguage.googleapis.com/v1beta
    api_key: ${GEMINI_API_KEY}
    model: gemini-2.5-flash

  kimi:
    type: openai                    # OpenAI 兼容接口
    base_url: https://api.moonshot.cn/v1
    api_key: ${KIMI_API_KEY}
    model: kimi-k2-turbo-preview

  qwen:
    type: openai                    # OpenAI 兼容接口
    base_url: https://dashscope.aliyuncs.com/compatible-mode/v1
    api_key: ${QWEN_API_KEY}
    model: qwen-turbo
```

### 节点级模型分配策略

不同节点可按需指定不同模型：
- **Schema Linking**: 用快速、经济的模型（如 `deepseek-chat`, `gpt-3.5-turbo`）
- **SQL Generation**: 用强模型（如 `deepseek-chat`, `gpt-4-turbo`, `claude-4-sonnet`）
- **Reasoning**: 用最强模型（如 `claude-4-sonnet`, `claude-4-opus`）
- **Output/Chat**: 推荐 `claude-4-sonnet`, `gpt-4-turbo`

```yaml
nodes:
  schema_linking:
    model: openai
  generate_sql:
    model: deepseek_v3
  reasoning:
    model: anthropic
  output:
    model: anthropic
```

---

## 二、数据库适配器（Database Adapters）

插件化架构（v0.2.3），安装即自动注册（Python entry points）。Built-in 默认可用，Plugin 按需安装。

### 2.1 Built-in（核心自带）

| 数据库 | 类型 | 说明 |
|--------|------|------|
| **SQLite** | 文件型 | 本地开发与测试 |
| **DuckDB** | 嵌入式 | 分析工作负载 |

### 2.2 Plugin（按需安装）

| 数据库 | 包名 | 安装 | 类型 | 说明 |
|--------|------|------|------|------|
| **PostgreSQL** | datus-postgresql | `pip install datus-postgresql` | 关系型 | 支持 SSL、多 schema、物化视图 |
| **MySQL** | datus-mysql | `pip install datus-mysql` | 关系型 | INFORMATION_SCHEMA 查询 |
| **Snowflake** | datus-snowflake | `pip install datus-snowflake` | 云数仓 | Arrow 格式高效传输 |
| **StarRocks** | datus-starrocks | `pip install datus-starrocks` | 实时分析 | 多 Catalog 支持 |
| **ClickZetta** | datus-clickzetta | `pip install datus-clickzetta` | Lakehouse | 深度集成合作伙伴（云器） |
| **Hive** | datus-hive | `pip install datus-hive` | 大数据 | HiveServer2/Thrift 协议，多认证机制 |
| **Spark** | datus-spark | `pip install datus-spark` | 分布式计算 | Spark Thrift Server |
| **ClickHouse** | datus-clickhouse | `pip install datus-clickhouse` | 列存分析 | HTTP 协议连接 |
| **Trino** | datus-trino | `pip install datus-trino` | 分布式查询 | 3 层结构（catalog → schema → table），跨 catalog 查询 |

*v0.2.6 新增：Hive / Spark / ClickHouse / Trino。*

### 2.3 各适配器特定能力

| 数据库 | 独有能力 | 认证机制 | 协议/驱动 |
|--------|---------|---------|----------|
| **PostgreSQL** | 6 级 SSL（disable/allow/prefer/require/verify-ca/verify-full）；物化视图；多 schema | user/password | SQLAlchemy (psycopg2) |
| **MySQL** | INFORMATION_SCHEMA；SHOW CREATE TABLE/VIEW | user/password | SQLAlchemy (pymysql) |
| **Snowflake** | Arrow 格式高效传输；多 database + schema；物化视图；Native SDK | user/password 或 key-pair | Native SDK (snowflake-connector-python) |
| **StarRocks** | 多 Catalog 支持；物化视图；MySQL 协议兼容 | user/password | MySQL 协议 (pymysql) |
| **ClickZetta** | Workspace + Schema 管理；Volume/Stage 文件操作 | user/password + instance/workspace/vcluster | Native SDK |
| **Hive** | HiveServer2/Thrift 协议；4 种认证（NONE/LDAP/CUSTOM/KERBEROS）；session 配置 | user/password 或 Kerberos | PyHive + Thrift |
| **Spark** | Spark Thrift Server（HiveServer2 协议）；3 种认证（NONE/PLAIN/KERBEROS） | user/password 或 Kerberos | PyHive + Thrift |
| **ClickHouse** | HTTP 协议；无 schema 层（database = schema）；轻量 DELETE | user/password | clickhouse-sqlalchemy |
| **Trino** | 3 层结构（catalog→schema→table）；跨 catalog 查询；HTTP/HTTPS SSL | user/password | trino-python-client |
| **SQLite** | 本地文件；零配置 | 无 | Built-in |
| **DuckDB** | 嵌入式 OLAP；零配置 | 无 | Built-in |

### 2.4 迁移能力（跨数据库 DDL 验证）

所有适配器统一实现 `MigrationTargetMixin`：
- `get_migration_capabilities()` — 返回目标库的方言特征（`requires` / `forbids` / `type_hints`）
- `suggest_table_layout()` — 生成 OLAP 优化建议（如 StarRocks: `DUPLICATE KEY` + `DISTRIBUTED BY HASH ... BUCKETS`；ClickHouse: `ENGINE` + `ORDER BY`）
- `validate_ddl()` — 结构验证 + 可选 dry-run（CREATE + DROP 到临时表）

### 2.5 配置示例

```yaml
agent:
  service:
    databases:
      # Snowflake
      production:
        type: snowflake
        account: ${SNOWFLAKE_ACCOUNT}
        username: ${SNOWFLAKE_USER}
        password: ${SNOWFLAKE_PASSWORD}
        warehouse: ${SNOWFLAKE_WAREHOUSE}
        database: ${SNOWFLAKE_DATABASE}

      # PostgreSQL
      analytics:
        type: postgresql
        host: ${PG_HOST}
        port: 5432
        username: ${PG_USER}
        password: ${PG_PASSWORD}
        database: mydb
        schema: public

      # DuckDB (本地)
      local_demo:
        type: duckdb
        uri: ./data/demo.duckdb
        default: true

      # SQLite (多文件 glob)
      bird_benchmark:
        type: sqlite
        path_pattern: benchmark/bird/**/*.sqlite
```

### 2.4 适配器架构

```
datus-agent (Core)
├── Built-in Adapters: SQLite, DuckDB
└── Plugin System (Entry Points)
    ├── datus-sqlalchemy (Base layer)
    │   ├── datus-mysql / datus-postgresql / datus-starrocks
    │   ├── datus-hive / datus-spark / datus-clickhouse / datus-trino
    └── Native SDK Adapters
        ├── datus-snowflake
        └── datus-clickzetta
```

---

## 三、存储后端（Storage Backends）

双轨存储（Vector + Relational），可插拔架构。

| 后端 | 向量存储 | 关系型存储 | 适用场景 | 安装 |
|------|---------|-----------|---------|------|
| **LanceDB + SQLite**（默认） | LanceDB | SQLite | 零配置，开发/单机部署 | 内置 |
| **PostgreSQL (pgvector)** | pgvector | PostgreSQL | 生产环境，多租户 schema 隔离 | `pip install datus-storage-postgresql` |
| **Milvus** | Milvus | — | 大规模向量检索 | v0.2.6 插件化 |

### 默认后端

```yaml
storage:
  embedding_device_type: cpu    # cpu / cuda / mps / auto
```

零配置：LanceDB（向量）+ SQLite（关系型），数据存储在 `data/datus_db_<namespace>/`。

### PostgreSQL 后端

```yaml
storage:
  rdb:
    type: postgresql
    host: ${PG_HOST}
    port: 5432
    user: ${PG_USER}
    password: ${PG_PASSWORD}
    dbname: datus
    pool_min_size: 1
    pool_max_size: 10

  vector:
    type: postgresql
    host: ${PG_HOST}
    port: 5432
    user: ${PG_USER}
    password: ${PG_PASSWORD}
    dbname: datus
```

### 数据库隔离

- LanceDB: 每个 namespace 一个独立目录
- PostgreSQL: 每个 namespace 一个独立 schema
- 无跨 namespace 数据交叉污染

---

## 四、Embedding Providers（嵌入模型）

用于 Knowledge Base 的向量化存储和语义搜索。

| Provider | 类型 | 模型 | 维度 | 说明 |
|----------|------|------|:---:|------|
| **OpenAI Embeddings** | 云端 | `text-embedding-3-small` | 1536 | 高质量，需 API key |
| | | `text-embedding-3-large` | 3072 | 最高质量 |
| **sentence-transformers**（默认） | 本地 | `all-MiniLM-L6-v2` (~100MB) | 384 | 极致性能 |
| | | `intfloat/multilingual-e5-large-instruct` (~1.2GB) | 1024 | 多语言，质量平衡 |
| | | `BAAI/bge-large-en-v1.5` (~1.2GB) | 1024 | 英文优化 |
| | | `BAAI/bge-large-zh-v1.5` (~1.2GB) | 1024 | 中文优化 |

### 配置示例

```yaml
storage:
  # 数据库元数据嵌入（云端）
  database:
    registry_name: openai
    model_name: text-embedding-3-small
    dim_size: 1536
    batch_size: 10
    target_model: openai

  # 文档嵌入（本地）
  document:
    model_name: intfloat/multilingual-e5-large-instruct
    dim_size: 1024

  # 指标嵌入（本地）
  metric:
    model_name: all-MiniLM-L6-v2
    dim_size: 384
```

---

## 五、语义层适配器（Semantic Adapters）

插件化架构，将外部语义层集成到 Datus 的指标发现、查询和验证流程中。

| 语义层 | 包名 | 安装 | 状态 |
|--------|------|------|:---:|
| **MetricFlow** | datus-semantic-metricflow | `pip install datus-semantic-metricflow` | ✅ Ready |

### 架构

```
datus-agent (Core)
├── Semantic Tools Layer
│   ├── BaseSemanticAdapter (Abstract)
│   ├── SemanticAdapterRegistry (Factory)
│   └── Data Models (MetricDefinition, QueryResult, etc.)
└── Plugin System (Entry Points)
    └── datus-semantic-metricflow → MetricFlowAdapter
```

### 配置

```yaml
semantic:
  type: metricflow
  namespace: my_project
  timeout: 30
```

### 核心接口

| 方法 | 说明 | 返回类型 |
|------|------|---------|
| `list_metrics(path, limit, offset)` | 列出可用指标（支持过滤） | `List[MetricDefinition]` |
| `get_dimensions(metric_name, path)` | 获取指标的维度 | `List[DimensionInfo]` |
| `query_metrics(metrics, dimensions, ...)` | 查询指标（支持过滤器、时间范围、where 子句） | `QueryResult` |
| `validate_semantic()` | 验证语义层配置 | `ValidationResult` |

### 自定义适配器

通过 Python entry points 注册自定义适配器：

```toml
# pyproject.toml
[project.entry-points."datus.semantic_adapters"]
myservice = "datus_semantic_myservice:register"
```

*参考实现: datus-semantic-metricflow*

---

## 六、BI 平台（Dashboard Copilot）

从 BI Dashboard 自动生成 Subagent，当前唯一支持 **Apache Superset**。

### 工作流程

```
Superset Dashboard 配置 → 提取所有图表的 SQL → 构建 Metadata + Reference SQL
  → 生成 Semantic Model → 提取 Metrics
    → 输出两个 Subagent: GenSQL + GenReport（归因分析）
```

### 部署与使用

```bash
# 1. 部署 Superset + PostgreSQL
minikube start --driver=docker
helm upgrade --install superset superset/superset -f examples-values.yaml

# 2. 配置连接
# agent.yml:
#   service.databases.superset: { type: postgresql, host: ..., port: 15432, ... }
#   dashboard.superset: { username: admin, password: admin }

# 3. 一键生成
datus-agent bootstrap-bi --database superset
```

### 生成产物

| Subagent | 说明 |
|----------|------|
| `{superset}_{dashboard}_s` | GenSQL——在仪表盘语义范围内生成 SQL |
| `{superset}_{dashboard}_s_attribution` | GenReport——指标对比 + 归因分析（根因定位、维度贡献量化） |

### 归因分析能力

- 自动维度重要性排序
- Delta 贡献计算（量化每个因素对整体变化的影响）
- 根因识别（定位驱动指标变动的具体值）

---

## 七、MCP 协议（Model Context Protocol）

Datus 双向支持 MCP 协议。

### 7.1 MCP Client（接入外部工具）

Datus 可通过 CLI 接入外部 MCP Server，扩展 Agent 能力。

| 传输方式 | 说明 |
|---------|------|
| **stdio** | 本地子进程，最快 |
| **http** | 持久化 HTTP 服务器 |
| **sse** | Server-Sent Events（远程云服务） |

```bash
# 添加 MCP Server
.mcp add --transport stdio sqlite uv -- -m mcp_sqlite_server
.mcp add --transport sse api-server https://api.example.com/mcp/sse --header "Authorization: Bearer token"
.mcp add --transport http metricflow https://localhost:9000/mcp

# 管理
.mcp list                         # 列表 + 状态
.mcp check <name>                 # 连接测试
.mcp call <name>.<tool> <args>    # 调用工具
.mcp remove <name>                # 移除
.mcp filter set <name> include|exclude <tool_list>  # 工具过滤

# 存储
~/.datus/conf/.mcp.json           # 所有 MCP 配置
```

### 7.2 MCP Server（暴露 Datus 能力）

将 Datus 的数据库和上下文搜索能力作为 MCP Server 暴露，供外部 Agent 调用。

**两种模式**：

| 模式 | 说明 | URL 模式 |
|------|------|---------|
| **Static** | 单 namespace | `/mcp` 或 `/sse` |
| **Dynamic** | 多 namespace，通过 URL 路径路由 | `/mcp/{namespace}` 或 `/sse/{namespace}` |

```bash
# Static Mode
datus-mcp --namespace my_db --transport http --port 8000

# Dynamic Mode
datus-mcp --dynamic --transport http --port 8000
datus-mcp --dynamic --transport sse --port 8000
```

**暴露的工具**：

| 类别 | 工具 |
|------|------|
| Database | `list_databases`, `list_schemas`, `list_tables`, `search_table`, `describe_table`, `get_table_ddl`, `read_query` |
| Context Search | `list_subject_tree`, `search_metrics`, `get_metrics`, `search_reference_sql`, `get_reference_sql`, `search_semantic_objects`, `search_knowledge`, `get_knowledge` |

**客户端集成**：

- **Claude Code**: `claude mcp add --transport sse datus http://127.0.0.1:8000/sse/<namespace>`
- **Claude Desktop**: 通过 `mcp-remote` 连接（stdio/SSE 两种方式）
- **Cursor IDE / 其他 MCP 客户端**: 标准 stdio/http/sse JSON 配置
- **Static 模式暴露工具**: 8 个数据库工具 + 8 个上下文搜索工具
- **Dynamic 模式**: 单一服务实例支持多 namespace 及带 subagent 参数的路由 (`?subagent=...`)

> **设计原则**：MCP 定位为「扩展层」——用于第三方 API 与非关键路径操作，核心链路使用 Native Tools。

---

## 八、AgentSkills + Skill Marketplace

v0.2.5 引入的模块化能力扩展系统，遵循 agentskills.io 规范。

### 8.1 技能类型

| 类型 | 说明 | 执行方式 |
|------|------|---------|
| **Bash Skills** | Shell 脚本扩展 | `skill_execute_command`（权限可控，白名单匹配） |
| **Function Skills** | Python 函数扩展 | `load_skill()` 后调用 |
| **Isolated Subagent Skills** | 在独立 Subagent 上下文中运行 | `context: fork` + `agent: Explore/Plan/general-purpose` |

### 8.2 SKILL.md 格式

```yaml
---
name: report-generator
description: Generate analysis reports from SQL query results
tags: [report, analysis, visualization, export]
version: "1.0.0"
allowed_commands:
  - "python:scripts/*.py"
  - "sh:scripts/*.sh"
context: fork            # 可选：在独立 Subagent 中运行
agent: Explore           # 可选：指定 Subagent 类型
---

# Report Generator Skill
...
```

### 8.3 权限管控

| 级别 | 行为 |
|------|------|
| `allow` | 可自由使用 |
| `deny` | 对 Agent 隐藏 |
| `ask` | 每次使用需用户确认 |

### 8.4 Subagent 中的技能加载

```yaml
agentic_nodes:
  school_report:
    node_class: gen_report
    tools: db_tools.*, context_search_tools.*
    mcp: metricflow_mcp
    skills: "report-*, data-*"    # glob 模式匹配
    model: deepseek
```

*Chat Subagent 默认加载所有发现的技能；其他 Subagent 需显式配置 `skills` 字段。*

### 8.5 Skill Marketplace CLI

内置 Town Marketplace——搜索、安装、发布、管理社区技能：

```bash
# 认证
datus skill login --marketplace http://datus-marketplace:9000

# 搜索与安装
datus skill search sql
datus skill install sql-optimization
datus skill install sql-optimization 1.0.0   # 指定版本

# 发布
datus skill publish ./skills/my-skill --owner murphy

# 管理
datus skill list
datus skill info sql-optimization
datus skill update          # 更新所有 marketplace 技能
datus skill remove sql-optimization
```

**REPL 等价命令**：`.skill list` / `.skill search` / `.skill install` / `.skill publish` / `.skill update` / `.skill remove`

---

## 九、可选集成（Optional）

### 9.1 LangSmith（LLM 调用追踪）

可选的 LLM 调用调试与追踪工具。

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_ENDPOINT=https://api.smith.langchain.com
export LANGCHAIN_API_KEY=xxx
export LANGSMITH_PROJECT=Datus-agent
```

### 9.2 Tavily（Web 搜索回退）

Platform Documentation 功能的 Web 搜索回退——当本地向量库无匹配时，通过 Tavily API 在线搜索。

```yaml
agent:
  document:
    tavily_api_key: ${TAVILY_API_KEY}
```

### 9.3 LLM Trace（本地调试追踪）

`--save_llm_trace` 参数将 LLM 的 I/O 保存为 YAML 文件，用于本地调试：

```bash
datus-cli --database my_db --save_llm_trace
python -m datus.main benchmark --database bird_sqlite --benchmark bird_dev --save_llm_trace
```

输出目录：`{agent.home}/trajectory/{namespace}/{timestamp}/{node_id}.yml`

每条 trace 包含：`system_prompt`, `user_prompt`, `reason_content`（推理模型）, `output_content`

### 9.4 GitHub Token（Platform Doc 来源）

从 GitHub 拉取平台文档时，设置 `GITHUB_TOKEN` 避免 API 限流：

```yaml
agent:
  document:
    starrocks:
      type: github
      source: StarRocks/starrocks
      github_token: ${GITHUB_TOKEN}
      paths: ["docs/sql-reference"]
```

---

## 十、营销可用事实数据（Marketing-Ready Facts）

以下所有数据均来自 GitHub / PyPI / docs.datus.ai 公开信息，截止 2026-07-03。

### 11.1 项目概览

| 指标 | 数据 | 来源 |
|------|------|------|
| **GitHub Stars** | 1,288 | [GitHub](https://github.com/Datus-ai/Datus-agent) |
| **GitHub Forks** | 205 | 同上 |
| **Open Issues** | 18 | 同上 |
| **Public Repos** | 10 | [Datus-ai org](https://github.com/Datus-ai) |
| **Top Contributors** | stukid (345), liuyufei9527 (156), Louis-Law (145), arnozhang (80), Dshadowzh (62) | 同上 |
| **许可证** | Apache 2.0 | PyPI |
| **Python 要求** | >= 3.12 | PyPI |
| **开发状态** | 3 - Alpha | PyPI |
| **首个版本** | v0.1.0 (2025) | GitHub Releases |
| **最新稳定版** | v0.3.5 (2026-05-28) | PyPI |
| **总发布数** | 20+ 版本（v0.2.0→v0.3.5, 8 个月） | PyPI |
| **PyPI Wheel 大小** | ~5 MB (v0.3.2) | PyPI |
| **平台支持** | macOS + Linux（Windows 理论可行，未正式支持） | docs |
| **组织创建时间** | 2025-03-21 | GitHub org |
| **仓库创建时间** | 2025-07-04 | GitHub repo |

### 11.2 安装方式

| 方式 | 命令 | 说明 |
|------|------|------|
| **一键安装** | `curl -fsSL https://...install.sh \| sh` | 自动创建 venv、安装、配置 PATH |
| **One-liner（指定版本）** | `...install.sh \| DATUS_VERSION=0.2.6 sh` | 锁定版本 |
| **pip** | `pip install datus-agent` | 标准方式 |
| **开发版** | `curl -fsSL https://...install-dev.sh \| sh` | 从 GitHub main 分支 |
| **开发版（指定分支）** | `...install-dev.sh \| DATUS_REF=feature/foo sh` | 测试未发布功能 |

### 11.3 数据库适配器能力矩阵

| 数据库 | 类型 | 安装 | 协议 | 认证 | 独有特性 |
|--------|------|------|------|------|---------|
| SQLite | Built-in | 无需 | 文件 | 无 | 零配置 |
| DuckDB | Built-in | 无需 | 文件 | 无 | 嵌入式 OLAP |
| PostgreSQL | Plugin | `pip install datus-postgresql` | psycopg2 | user/password | 6 级 SSL；物化视图 |
| MySQL | Plugin | `pip install datus-mysql` | pymysql | user/password | SHOW CREATE 语句 |
| Snowflake | Plugin | `pip install datus-snowflake` | Native SDK | user/password 或 key-pair | Arrow 格式传输 |
| StarRocks | Plugin | `pip install datus-starrocks` | MySQL 协议 | user/password | 多 Catalog |
| ClickZetta | Plugin | `pip install datus-clickzetta` | Native SDK | user/pass + instance | Volume/Stage 操作 |
| Hive | Plugin (v0.2.6) | `pip install datus-hive` | Thrift | NONE/LDAP/CUSTOM/KERBEROS | Session 配置 |
| Spark | Plugin (v0.2.6) | `pip install datus-spark` | Thrift | NONE/PLAIN/KERBEROS | Spark SQL 方言 |
| ClickHouse | Plugin (v0.2.6) | `pip install datus-clickhouse` | HTTP | user/password | Database = Schema |
| Trino | Plugin (v0.2.6) | `pip install datus-trino` | HTTP/HTTPS SSL | user/password | 跨 Catalog 查询 |

**所有适配器通用能力**：CRUD SQL、DDL 操作、Metadata 检索（表/视图/schema）、示例数据抽样、连接池、超时管理。

### 11.4 LLM Provider 认证矩阵

| Provider | 认证方式 | Azure 支持 | 自托管兼容 |
|----------|---------|:---:|:---:|
| OpenAI | API Key | ✅ Azure OpenAI endpoint | ✅ 任意 OpenAI 兼容接口 |
| Claude | API Key / Subscription Token / OAuth (Codex) | — | — |
| DeepSeek | API Key | — | ✅ |
| Qwen | API Key | — | ✅ |
| Kimi | API Key | — | ✅ |
| Gemini | API Key | — | — |

**环境变量注入**：所有 provider 支持 `${ENV_VAR}` 语法。多环境支持：`agent.yml.dev` / `agent.yml.staging` / `agent.yml.production`。

### 11.5 Benchmark 评测数据

| 指标 | 数据 | 来源 |
|------|------|------|
| **BIRD-DEV 样本通过率** | 63%（30 queries, Nov 2025） | [docs](https://docs.datus.ai/benchmark/benchmark_manual/) |
| **Table Mismatch 率** | 13%（表识别不准确） | 同上 |
| **Column Value Mismatch 率** | 20%（表正确但列值差异） | 同上 |
| **Empty Result 率** | 0%（无空结果） | 同上 |
| **支持的 Benchmark 数据集** | BIRD-DEV (1533 tasks)、Spider2、Semantic Layer | docs |
| **多轮 Benchmark 支持** | `--round 4` 自动跨轮次对比 Excel 报告 | docs |
| **内置教程数据集** | California Schools（无需下载即可试跑） | docs |

### 11.6 已知限制

| 维度 | 限制 | 说明 |
|------|------|------|
| **指标自动生成** | 仅支持单表 SQL，不支持 JOIN | `gen_metrics` 和 `gen_ext_knowledge` |
| **BI 平台** | 仅 Superset | 暂无 Tableau/PowerBI/Looker |
| **语义层** | 仅 MetricFlow | 插件架构支持自定义适配器 |
| **操作系统** | macOS + Linux | Windows 未正式支持 |
| **Python** | >= 3.12 | 不支持更早版本 |
| **开发状态** | Alpha | PyPI 标记 "3 - Alpha" |
| **向量存储高级功能** | 生产环境建议 pgvector 或 Milvus | 默认 LanceDB 适合开发/单机 |

### 11.7 企业客户参考

| 客户 | 状态 |
|------|------|
| **LinkedIn** | 企业 POC |
| **Expedia** | 企业 POC |
| **Coinbase** | 企业 POC |
| **云器 Lakehouse (ClickZetta)** | 落地生产案例 |

---

## 十一、集成总览

```
                        ┌──────────────────────────────┐
                        │         Datus Core           │
                        │  Context Engine + Subagent   │
                        │  Workflow + Knowledge Base   │
                        └──────────┬───────────────────┘
                                   │
        ┌──────────────┬───────────┼───────────┬──────────────┐
        ▼              ▼           ▼           ▼              ▼
   ┌─────────┐  ┌──────────┐ ┌──────────┐ ┌─────────┐  ┌──────────┐
   │LLM      │  │Database  │ │Storage   │ │MCP      │  │Semantic  │
   │Providers│  │Adapters  │ │Backends  │ │Protocol │  │Adapters  │
   │         │  │          │ │          │ │         │  │          │
   │OpenAI   │  │SQLite    │ │LanceDB   │ │Client   │  │MetricFlow│
   │Claude   │  │DuckDB    │ │+ SQLite  │ │(接入外部│  │          │
   │DeepSeek │  │PG/MySQL  │ │pgvector   │ │ MCP)    │  └──────────┘
   │Qwen     │  │Snowflake │ │+ PG      │ │Server   │
   │Kimi     │  │StarRocks │ │Milvus    │ │(暴露自身│  ┌──────────┐
   │Gemini   │  │Hive      │ │          │ │能力)    │  │BI        │
   └─────────┘  │Spark     │ └──────────┘ └─────────┘  │Platform  │
                │ClickHouse│                             │          │
   ┌─────────┐  │Trino     │  ┌──────────┐ ┌─────────┐  │Superset  │
   │Embedding│  │ClickZetta│  │Skills    │ │Tracing  │  └──────────┘
   │Providers│  └──────────┘  │System +  │ │         │
   │         │                │Marketplace│ │LangSmith│
   │OpenAI   │                └──────────┘ │Tavily   │
   │sentence │                             │LLM Trace│
   │-transf. │                             │GitHub   │
   └─────────┘                             └─────────┘
```
