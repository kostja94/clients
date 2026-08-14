# Workflow 系统

## 工作流类型

### 1. Fixed Workflow
**用途**: 简单、直接问题的确定性 SQL 生成

**节点序列**: `Schema Linking → Generate SQL → Execute SQL → Output`

**特点**:
- 可预测：始终遵循相同执行路径
- 快速：无 reflection 开销
- 最适合：简单查询、定义明确的数据需求

---

### 2. Reflection Workflow
**用途**: 智能、自我改进的 SQL 生成，自适应行为

**节点序列**: `Schema Linking → Generate SQL → Execute SQL → Reflect → Output`

**特点**:
- 自我评估：Reflect 节点评估结果并决定下一步
- 自适应：可根据执行结果动态添加新节点
- 最适合：复杂业务查询、需要多次尝试的场景

**Real-world 示例**:
```
User: "Show me quarterly revenue trends by product category"

Process:
1. Schema Linking: 找到 orders, products, categories 表
2. Generate SQL: 创建初始季度营收查询
3. Execute SQL: 运行查询
4. Reflect: 注意缺少季节性调整逻辑
5. Add Fix Node: 使用季节性计算修正查询
6. Output: 最终结果
```

---

### 3. Metric-to-SQL Workflow
**用途**: 从预定义业务指标生成 SQL

**节点序列**: `Schema Linking → Search Metrics → Date Parser → Generate SQL → Execute SQL → Output`

**特点**:
- 指标驱动：从业务指标开始而非原始 SQL
- 时间感知：包含日期解析
- 最适合：BI 报表、KPI 计算、时间序列分析

---

## 内置工作流节点

### Control Nodes
| 节点 | 用途 |
|------|------|
| Reflect | 评估结果，决定下一步（核心智能：实现自适应 SQL 生成） |
| Parallel | 同时执行多个子节点 |
| Selection | 从多个候选中选择最佳结果 |
| Subworkflow | 执行嵌套工作流 |

### Action Nodes
| 节点 | 用途 |
|------|------|
| Schema Linking | 理解用户查询，找到相关数据库模式 |
| Generate SQL | 基于需求生成 SQL 查询 |
| Execute SQL | 安全执行 SQL 查询 |
| Output | 格式化并呈现结果 |
| Reasoning | 深度分析和推理 |
| Fix | 修复有问题的 SQL |
| Generate Metrics | 从 SQL 创建业务指标 |
| Search Metrics | 查找相关业务指标 |
| Compare | 比较 SQL 结果与预期结果 |
| Date Parser | 解析用户查询中的时间表达式 |
| Document Search | 查找相关文档和上下文 |

### Agentic Nodes
| 节点 | 用途 |
|------|------|
| Chat Agentic | 对话式 AI 交互，支持工具调用 |

---

## 工作流编排

### 自定义工作流 (agent.yml)
```yaml
agent:
  workflow:
    plan: custom_analytics  # 设为默认

    custom_analytics:
      - schema_linking
      - search_metrics
      - generate_sql
      - execute_sql
      - compare
      - output
```

### 并行执行
```yaml
bird_para:
  - schema_linking
  - parallel:
    - generate_sql
    - reasoning
  - selection
  - execute_sql
  - output
```

### Sub-workflows
```yaml
main_workflow:
  - schema_linking
  - parallel:
    - subworkflow1
    - subworkflow2
  - selection
  - execute_sql
  - output

subworkflow1:
  - search_metrics
  - generate_sql

subworkflow2:
  - search_metrics
  - reasoning
```

### Sub-workflows with Custom Config
```yaml
multi_agent:
  - schema_linking
  - parallel:
    - agent1_workflow
    - agent2_workflow
  - selection
  - output

agent1_workflow:
  steps:
    - search_metrics
    - generate_sql
  config: multi/agent1.yaml
```

### Reflection Nodes 配置
```yaml
reflection_nodes:
  schema_linking:
    - schema_linking
    - generate_sql
    - execute_sql
    - reflect
  doc_search:
    - doc_search
    - generate_sql
    - execute_sql
    - reflect
  simple_regenerate:
    - execute_sql
    - reflect
  reasoning:
    - reasoning
    - execute_sql
    - reflect
```

---

## Workflow API

### 启动服务
```bash
python -m datus.api.main --host 0.0.0.0 --port 8000
python -m datus.api.main --workers 4 --port 8000
python -m datus.api.main --daemon --port 8000
```

### 认证 (OAuth2 Client Credentials)
```bash
# 获取 token
curl -X POST "http://localhost:8000/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=your_client_id&client_secret=your_client_secret&grant_type=client_credentials"

# 使用 token
curl -X POST "http://localhost:8000/workflows/run" \
  -H "Authorization: Bearer your_jwt_token" \
  -H "Content-Type: application/json" \
  -d '{"workflow": "fixed", "namespace": "your_db", "task": "Show me users"}'
```

### 请求参数
| 参数 | 类型 | 必填 | 描述 |
|------|------|:---:|------|
| `workflow` | string | ✅ | nl2sql, reflection, fixed, metric_to_sql |
| `namespace` | string | ✅ | 数据库 namespace |
| `task` | string | ✅ | 自然语言任务描述 |
| `mode` | string | ✅ | sync 或 async |
| `catalog_name` | string | ❌ | 数据库 catalog |
| `database_name` | string | ❌ | 数据库名 |
| `current_date` | string | ❌ | 时间参考 |
| `domain`/`layer1`/`layer2` | string | ❌ | 业务领域分层 |
| `ext_knowledge` | string | ❌ | 额外业务上下文 |

### 同步模式 (mode: "sync")
```json
{
  "task_id": "client_20240115143000",
  "status": "completed",
  "sql": "SELECT ... FROM orders ...",
  "result": [...],
  "metadata": {
    "execution_time": 12.5,
    "nodes_executed": 5,
    "reflection_rounds": 0
  }
}
```

### 异步模式 (mode: "async") - SSE 事件流
```
event: started → {task_id, workflow}
event: progress → {message, progress}
event: node_progress → {node, status, progress}
event: sql_generated → {sql}
event: output_ready → {result, metadata}
event: done → {task_id, status, total_time}
```
