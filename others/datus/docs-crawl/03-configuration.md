# 配置系统

## Configuration 总览

### 配置加载优先级
1. `-f` 指定的文件
2. `./conf/agent.yml`
3. `~/.datus/conf/agent.yml`

### 配置模块
| 模块 | 用途 |
|------|------|
| Agent | 全局设置 & 模型 providers（目标 LLM、API keys、模型名） |
| Nodes | 任务级处理单元（Schema Linking、SQL 生成、推理、反射等） |
| Workflow | 节点编排（顺序、并行、sub-workflows、反射路径） |
| Storage | 嵌入模型 & 向量存储（嵌入类型、设备、维度） |
| Database | 数据库连接抽象（Snowflake, StarRocks, SQLite, DuckDB 等） |
| Benchmark | 评估 & 测试（BIRD-DEV, Spider2, Semantic Layer） |

---

## Agent 配置

### 支持的 LLM Providers
| Provider | 模型 | Interface Type |
|----------|------|:---:|
| OpenAI | GPT-4, GPT-5 | `openai` |
| Anthropic | Claude 4 (Sonnet, Opus), Claude 3 | `claude` |
| Google | Gemini (Pro, Flash, Ultra) | `gemini` |
| DeepSeek | DeepSeek Chat, DeepSeek Reasoning | `deepseek` |
| Kimi | Moonshot AI's Kimi | `openai` |
| Qwen | Alibaba's Qwen | `openai` |

### Provider 配置示例
```yaml
agent:
  target: openai  # 所有节点的默认模型

models:
  openai:
    type: openai
    base_url: https://api.openai.com/v1
    api_key: ${OPENAI_API_KEY}
    model: gpt-4-turbo

  deepseek:
    type: deepseek
    base_url: https://api.deepseek.com
    api_key: ${DEEPSEEK_API_KEY}
    model: deepseek-chat

  anthropic:
    type: claude
    base_url: https://api.anthropic.com
    api_key: ${ANTHROPIC_API_KEY}
    model: claude-sonnet-4-20250514
```

---

## Nodes 配置

### 核心节点
```yaml
nodes:
  schema_linking:
    model: openai
    matching_rate: fast    # fast/medium/slow/from_llm (返回 5/10/20/LLM 选择)
    prompt_version: "1.0"

  generate_sql:
    model: deepseek_v3
    max_table_schemas_length: 4000
    max_data_details_length: 2000
    max_context_length: 8000
    max_value_length: 500

  reasoning:
    model: anthropic
    # 与 generate_sql 相同参数，专注于迭代改进

  search_metrics:
    model: openai
    matching_rate: medium

  reflect:
    prompt_version: "1.0"

  output:
    model: anthropic
    check_result: true

  chat:
    workspace_root: sql2
    model: anthropic
    max_turns: 25
```

### 模型分配策略
- **Schema Linking**: 使用快速、经济的模型 (`gpt-3.5-turbo`, `deepseek-chat`)
- **SQL Generation**: 推荐 `deepseek-chat`, `gpt-4-turbo`, `claude-4-sonnet`
- **Reasoning**: 最佳 `claude-4-sonnet`, `gpt-4-turbo`
- **Output/Chat**: 推荐 `claude-4-sonnet`, `gpt-4-turbo`

---

## Storage 配置

### 双轨存储
- **Vector DB**: 向量搜索（LanceDB 默认 / PostgreSQL pgvector）
- **RDB**: 结构化元数据（SQLite 默认 / PostgreSQL）

### 嵌入模型
| 数据层 | 推荐模型 | 维度 |
|--------|---------|:---:|
| Database | `text-embedding-3-small` (OpenAI) | 1536 |
| Document | `all-MiniLM-L6-v2` (~100MB) | 384 |
| Metric | `all-MiniLM-L6-v2` | 384 |

### 高性能本地配置
```yaml
storage:
  embedding_device_type: auto
  database:
    registry_name: sentence-transformers
    model_name: all-MiniLM-L6-v2
    dim_size: 384
  document:
    model_name: all-MiniLM-L6-v2
    dim_size: 384
  metric:
    model_name: all-MiniLM-L6-v2
    dim_size: 384
```

### PostgreSQL 后端
```yaml
storage:
  rdb:
    type: postgresql
    host: localhost
    port: 5432
    user: postgres
    password: ${PG_PASSWORD}
    dbname: datus
  vector:
    type: postgresql
    host: localhost
    port: 5432
    user: postgres
    password: ${PG_PASSWORD}
    dbname: datus
```

---

## Service 配置 (Namespace)

```yaml
agent:
  service:
    databases:
      my_snowflake:
        type: snowflake
        account: ${SNOWFLAKE_ACCOUNT}
        username: ${SNOWFLAKE_USER}
        password: ${SNOWFLAKE_PASSWORD}
        default: true

      my_duckdb:
        type: duckdb
        uri: ./data/analytics.duckdb

      bird_benchmark:
        type: sqlite
        path_pattern: benchmark/bird/dev_20240627/dev_databases/**/*.sqlite
```

### 支持的数据库
| 数据库 | 包 | 安装 |
|--------|-----|------|
| SQLite | 内置 | 包含在核心 |
| DuckDB | 内置 | 包含在核心 |
| MySQL | datus-mysql | `pip install datus-mysql` |
| PostgreSQL | datus-postgresql | `pip install datus-postgresql` |
| Snowflake | datus-snowflake | `pip install datus-snowflake` |
| StarRocks | datus-starrocks | `pip install datus-starrocks` |
| ClickZetta | datus-clickzetta | `pip install datus-clickzetta` |
| Hive | datus-hive | `pip install datus-hive` |
| Spark | datus-spark | `pip install datus-spark` |
| ClickHouse | datus-clickhouse | `pip install datus-clickhouse` |
| Trino | datus-trino | `pip install datus-trino` |

---

## Benchmark 配置

### 支持的 Benchmarks
- **BIRD-DEV**: 复杂 SQL 生成综合测试
- **Spider2**: 高级多数据库 SQL 测试
- **Semantic Layer**: 业务指标和语义理解测试

### 配置
```yaml
benchmark:
  custom_bird:
    benchmark_path: benchmark/custom_bird/dev_data
  custom_spider:
    benchmark_path: path/to/spider/data
```

### 运行
```bash
# 按 Task ID
datus-agent benchmark --database bird_sqlite --benchmark bird_dev --benchmark_task_ids 14 15

# 全部
datus-agent benchmark --database bird_sqlite --benchmark bird_dev

# 评估
datus-agent eval --database bird_sqlite --benchmark bird_dev --output_file evaluation.json
```

### 多轮 Benchmark
```bash
datus-agent multi-round-benchmark \
  --database bird_sqlite \
  --benchmark bird_dev \
  --workflow chat_agentic \
  --round 4 \
  --workers 2
```
