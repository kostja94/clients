# Knowledge Base 总览

## 核心概念

Datus Agent Knowledge Base 是一个多模态智能系统，将分散的数据资产转化为统一的、可搜索的存储库。

### 核心组件

| # | 组件 | 用途 |
|---|------|------|
| 1 | Schema Metadata | 理解数据库结构，提供智能表推荐 |
| 2 | Semantic Models | 用语义信息丰富数据库模式，提升 SQL 生成质量 |
| 3 | Business Metrics | 管理和查询标准化业务 KPI |
| 4 | Reference SQL | 捕获、分析、搜索 SQL 专业知识 |
| 5 | Reference Template | 管理参数化 Jinja2 SQL 模板 |
| 6 | External Knowledge | 处理和索引领域特定的业务知识 |
| 7 | Platform Documentation | 提供官方平台文档用于 SQL 生成和验证 |

### 存储后端

**双轨存储架构：**
- **Vector Database**: 存储嵌入向量，支持语义搜索
- **Relational Database (RDB)**: 存储结构化元数据

**可插拔后端（通过 Registry + entry-point 机制）：**

| 后端 | 向量 | 关系型 | 适用场景 |
|------|------|--------|---------|
| LanceDB + SQLite | LanceDB | SQLite | 开发环境，零配置 |
| PostgreSQL (pgvector) | pgvector | PostgreSQL | 生产环境 |

### Namespace 隔离
每个 namespace 独立存储：
- LanceDB: 每个 namespace 一个目录
- PostgreSQL: 每个 namespace 一个 schema

---

## Metadata

`bootstrap-kb` 初始化 SQL 语句和示例数据到向量数据库。

### 数据字段
**Table Definition:**
- `catalog_name`, `database_name`, `schema_name`: 层级标识
- `table_type`: `table`, `view`, `mv`（物化视图）
- `table_name`, `definition`(DDL), `identifier`

**Sample Data:**
- `sample_rows`: 通常为前 5 行数据

### 构建命令
```bash
datus-agent bootstrap-kb --database <your_namespace> --kb_update_strategy [check/overwrite/incremental]
```
- `check`: 检查当前构建的数据条目数
- `overwrite`: 完全覆盖已有数据
- `incremental`: 增量更新

---

## Semantic Models

从 v0.2.4 起，语义模型作为模式扩展独立运行，通过字段级存储提供维度和度量信息。

### 存储结构
```yaml
# 存储对象 (kind field):
- "table": 表级元数据
- "column": 列级元数据（带语义标记）
- "entity": 关系实体定义

# 列的语义标记:
- is_dimension: 用于分组/过滤
- is_measure: 用于聚合
- is_entity_key: 用于表连接
```

### 数据源格式

**CSV:**
```csv
question,sql
How many orders per customer?,SELECT customer_id, COUNT(*) as order_count FROM orders GROUP BY customer_id;
```

**YAML (MetricFlow compatible):**
```yaml
data_source:
  name: orders
  identifiers:
    - name: order
      type: PRIMARY
      expr: id
    - name: customer
      type: FOREIGN
      expr: customer_id
  dimensions:
    - name: status
      type: CATEGORICAL
    - name: created_at
      type: TIME
  measures:
    - name: amount
      agg: sum
    - name: order_count
      agg: count
```

---

## Metrics

从 v0.2.4 起，Metrics 组件专注于创建可查询的标准化业务指标，可直接通过 MetricFlow 执行。

### Metrics-First Strategy
当用户查询涉及 KPI 时：
1. 使用 `search_semantic_objects` 搜索匹配指标
2. 找到则通过 `query_metrics` 执行（优先）
3. 不存在时回退到临时 SQL 生成

### 查询指标
```python
# 搜索指标
search_semantic_objects(query="daily active users", kinds=["metric"])

# 执行指标查询
query_metrics(
    metrics=["daily_active_users"],
    group_by=["platform", "country"],
    start_time="2024-01-01",
    end_time="2024-01-31"
)
```

### Subject Tree 分类
格式: `domain/layer1/layer2`
- **Predefined Mode**: `--subject_tree "Sales/Reporting/Daily,Finance/Revenue/Monthly"`
- **Learning Mode**: 省略参数，复用已有分类或创建新分类

### YAML 格式
```yaml
metric:
  name: total_revenue
  description: "Total revenue from all transactions"
  type: simple
  type_params:
    measure: amount
  filter: "amount > 0"
  locked_metadata:
    tags:
      - "Finance"
      - "subject_tree: Finance/Revenue/Total"
```

---

## Reference SQL

将原始 SQL 文件转化为结构化知识库，支持语义搜索。

### SQL 文件格式
```sql
-- Daily active users count
-- Count unique users who logged in each day
SELECT
    DATE(created_at) as activity_date,
    COUNT(DISTINCT user_id) as daily_active_users
FROM user_activity
WHERE created_at >= '2025-01-01'
GROUP BY DATE(created_at)
ORDER BY activity_date;
```

### 命令
```bash
datus-agent bootstrap-kb \
    --database <your_namespace> \
    --components reference_sql \
    --sql_dir /path/to/sql/directory \
    --kb_update_strategy overwrite \
    --subject_tree "Analytics/User/Activity,Analytics/Revenue/Daily"
```

---

## Reference Template

管理参数化 Jinja2 SQL 模板，用于稳定、可重复的查询生成。

### 模板模式
**Template-Only Mode** — 限制 Agent 只执行预批准模板（不生成临时 SQL）：
```yaml
agentic_nodes:
  template_executor:
    model: deepseek-v3
    system_prompt: ref_tpl
    tools: context_search_tools.list_subject_tree, 
           reference_template_tools.search_reference_template,
           reference_template_tools.get_reference_template,
           reference_template_tools.execute_reference_template
```

### 参数类型系统
| 类型 | 检测方式 | 富化内容 |
|------|---------|---------|
| `dimension` | `WHERE col = '{{param}}'` | `column_ref` + `sample_values` (Top 10) |
| `column` | `GROUP BY {{param}}` 或 `SELECT {{param}}` | `table_refs` + `sample_values` |
| `keyword` | `ORDER BY expr {{param}}` | `allowed_values` (e.g. `ASC`, `DESC`) |
| `number` | `LIMIT {{param}}` 或比较运算符 | — |

### 可用工具
- `search_reference_template`: 自然语言搜索模板
- `get_reference_template`: 通过 subject_path + name 获取
- `render_reference_template`: 渲染模板为 SQL
- `execute_reference_template`: 渲染并立即执行（只读）

---

## External Knowledge

将业务规则和概念转化为结构化知识库。支持两种导入模式：

### 双导入模式
1. **Direct CSV Import**: 预定义知识条目
2. **AI Generation from Success Stories**: 从问答 SQL 对自动生成

### CSV 格式 (Direct)
```csv
subject_path,name,search_text,explanation
Finance/Revenue/Metrics,GMV Definition,GMV,"Gross Merchandise Volume represents..."
```

### CSV 格式 (AI Generation)
```csv
question,sql,subject_path
"What is the total GMV?","SELECT SUM(amount) FROM orders...",Finance/Revenue/Metrics
```

### AI 生成的验证循环
1. 分析问答对
2. 提取业务概念
3. 生成知识条目 YAML
4. **verify_sql**: 验证 AI 生成的 SQL 与隐藏参考 SQL
5. **自动重试**: 验证失败重试最多 3 次

### 两种使用方式对比
| 方面 | Bootstrap (batch) | Subagent (interactive) |
|------|-------------------|----------------------|
| 用例 | 从已有 Q&A 对批量导入 | 临时知识创建/改进 |
| 输入 | CSV 文件 | REPL 中的自由格式消息 |
| Gold SQL | 直接传递结构化字段 | 从用户消息中 LLM 解析 |
| DB 保存 | 自动（无需确认） | 用户通过 hook 提示确认 |
| 验证 | 自动重试循环 | 自动重试循环 |

---

## Platform Documentation

将官方平台文档（Snowflake, StarRocks, Polaris 等）摄入专用向量存储。

### 管道
```
Fetch → Parse → Clean → Chunk → Embed → Store
```

### Command
```bash
datus-agent platform-doc \
  --platform <platform_name> \
  --source <source> \
  --source-type <github|website|local> \
  --update-strategy <check|overwrite>
```

### 三种来源
1. **Github**: `--source StarRocks/starrocks --source-type github --paths docs/en`
2. **Website**: `--source https://docs.snowflake.com/en/sql-reference --source-type website --max-depth 2`
3. **Local**: `--source /path/to/duckdb-docs --source-type local`

### 可用工具
| 工具 | 用途 |
|------|------|
| `list_document_nav` | 浏览导航树 |
| `get_document` | 按层级路径获取文档 |
| `search_document` | 语义关键词搜索 |
| `web_search_document` | Web 回退搜索（需 Tavily API key） |

### Namespace 独立性
- Platform docs 跨 namespace 共享，按 platform 存储
- 默认位置: `~/.datus/data/document/<platform>/<version>/`
