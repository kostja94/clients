# Subagent 系统

## Subagent Introduction

Subagents are specialized AI assistants in Datus that focus on specific tasks. Unlike the default chat assistant that handles general SQL queries, subagents are optimized for particular workflows.

### What is a Subagent?
A subagent is a task-specific AI assistant with:
- **Specialized System Prompts**: Optimized instructions for specific tasks
- **Custom Tools**: Tailored toolset for the task (e.g., file operations, validation)
- **Scoped Context**: Optional dedicated context (tables, metrics, reference SQL)
- **Independent Sessions**: Separate conversation history from main chat
- **Task-Focused Workflow**: Guided steps for completing specific objectives

### Available Subagents

| # | Subagent | Purpose |
|---|----------|---------|
| 1 | gen_semantic_model | Generate MetricFlow semantic models from database tables |
| 2 | gen_metrics | Convert SQL queries into reusable MetricFlow metric definitions |
| 3 | gen_sql_summary | Analyze and catalog SQL queries for knowledge reuse |
| 4 | gen_ext_knowledge | Generate and manage business concepts and domain-specific definitions |
| 5 | explore | Read-only data exploration subagent for gathering context before SQL generation |
| 6 | gen_sql | Generate optimized SQL queries through a specialized SQL expert subagent |
| 7 | gen_report | Flexible report generation assistant combining semantic, database, and context search tools |
| 8 | Custom | User-defined subagents in agent.yml for organization-specific workflows |

### Three Ways to Use Subagents

1. **CLI Command** (Recommended): Use slash commands like `/gen_metrics`, `/gen_semantic_model`
2. **Web Interface**: Access via `http://localhost:8501/?subagent=gen_metrics`
3. **Automatic Delegation**: Chat agent transparently delegates to subagents via `task()` tool

### Automatic Delegation Flow
```
User Question → Chat Agent → {Complex?} → No → Direct Response
                                      → Yes → Delegate to Subagent (explore/gen_sql/etc.)
                                                → Result returned to Chat Agent
```

When does the chat agent delegate?
- Simple questions (SELECT, COUNT, GROUP BY on known tables) → Handles directly
- Need to discover tables/columns or understand domain terms → Delegates to `explore`
- Complex SQL with multi-table joins or domain-specific logic → Delegates to `gen_sql`

### Configuration
```yaml
agentic_nodes:
  gen_metrics:
    model: claude
    system_prompt: gen_metrics
    prompt_version: "1.0"
    tools: generation_tools.*, filesystem_tools.*, semantic_tools.*
    hooks: generation_hooks
    max_turns: 40
    workspace_root: /path/to/workspace
    agent_description: "Metric generation assistant"
    rules:
      - Use check_metric_exists to avoid duplicates
      - Validate with validate_semantic tool
```

### Tool Patterns
- `db_tools.*`: Database operations (list tables, get DDL, execute queries)
- `generation_tools.*`: Generation helpers (check duplicates, context preparation)
- `filesystem_tools.*`: File operations (read, write, edit files)
- `context_search_tools.*`: Knowledge Base search (find metrics, semantic models)
- `semantic_tools.*`: Semantic layer operations (list metrics, query metrics, validate)
- `date_parsing_tools.*`: Date/time parsing and normalization

### MCP Servers
MCP (Model Context Protocol) servers provide additional tools:
- `filesystem_mcp`: File system operations within workspace
- Note: MetricFlow integration now uses native `semantic_tools.*`, not MCP servers

---

## Customized Subagents

The `.subagent` command provides full lifecycle management of sub‑agents.

### Subcommands
- **add** — Interactive wizard to add a new sub‑agent
- **list** — Lists all configured sub‑agents with details (scoped context, tools, MCP, rules)
- **remove** — Removes a specified sub‑agent from configuration
- **update** — Interactive wizard to update an existing sub‑agent (triggers KB rebuild if context changes)
- **bootstrap** — Builds or simulates building a scoped knowledge base

### Bootstrap Parameters
```
.subagent bootstrap <agent_name> [--components metadata,metrics,reference_sql] [--plan]
```
- `--components`: Comma‑separated list (metadata, metrics, reference_sql)
- `--plan`: Simulation mode — calculates plan without writing files

### Namespace‑level Rebuild
```
python -m datus.main bootstrap-kb
```
All sub‑agents under the current namespace with scoped context will rebuild their knowledge bases.

---

## gen_semantic_model

Purpose: Generate MetricFlow semantic models from database tables.

### Command
```
/gen_semantic_model generate a semantic model for table <table_name>
```

### Workflow
```
User Request → DDL Analysis → YAML Generation → Validation → User Confirmation → Storage
```

### Semantic Model Structure
```yaml
data_source:
  name: table_name
  description: "Table description"
  sql_table: schema.table_name
  
  measures:
    - name: total_amount
      agg: SUM
      expr: amount_column
      create_metric: true
      description: "Total transaction amount"
  
  dimensions:
    - name: created_date
      type: TIME
      type_params:
        is_primary: true
        time_granularity: DAY
    - name: status
      type: CATEGORICAL
      description: "Order status"
  
  identifiers:
    - name: order_id
      type: PRIMARY
      expr: order_id
    - name: customer
      type: FOREIGN
      expr: customer_id
```

### Configuration (minimal)
```yaml
agentic_nodes:
  gen_semantic_model:
    model: claude        # Optional
    max_turns: 30        # Default: 30
```

---

## gen_metrics

Purpose: Convert SQL queries into reusable MetricFlow metric definitions.

### Important Limitation
⚠️ Single Table Queries Only — Multi-table JOINs are NOT supported.

### Command
```
/gen_metrics Generate a metric from this SQL: SELECT SUM(amount) FROM transactions
```

### Workflow
```
User provides SQL + question → Agent analyzes logic → Finds semantic model → 
Reads measures → Checks for duplicates → Generates metric YAML → 
Appends to file → Validates → User confirms → Syncs to Knowledge Base
```

### Metric Types
- **simple**: Direct aggregation (SUM, COUNT, AVG, etc.)
- **ratio**: Derived metrics like `SUM(revenue) / COUNT(DISTINCT customer_id)`
- **measure_proxy**: Metrics that pass through an existing measure

### Storage
- Semantic Model: `{table_name}.yml` — data_source with measures and dimensions
- Metrics: `metrics/{table_name}_metrics.yml` — metric definitions only

### Configuration
```yaml
agentic_nodes:
  gen_metrics:
    model: claude
    max_turns: 40        # Default: 30
```

---

## gen_sql_summary

Purpose: Analyze, classify, and catalog SQL queries for knowledge reuse.

### Command
```
/gen_sql_summary Analyze this SQL: SELECT SUM(revenue) FROM sales GROUP BY region
```

### Workflow
```
User provides SQL + description → Agent analyzes query → 
Automatically retrieves context (taxonomy + similar queries) →
Generates unique ID → Creates YAML → Saves file → User confirms → Syncs to KB
```

### YAML Structure
```yaml
id: "abc123def456..."           # Auto-generated MD5 hash
name: "Revenue by Region"       # Max 20 chars
sql: "SELECT ..."               # Complete SQL query
comment: "Calculate total revenue grouped by region"
summary: "This query aggregates..."  # For vector search
filepath: "/path/to/file.yml"
domain: "Sales"
layer1: "Reporting"
layer2: "Revenue Analysis"
tags: "revenue, region, aggregation"
```

### Subject Tree Categorization
- **Predefined Mode**: `--subject_tree "Sales/Reporting/Daily,Finance/Revenue/Monthly"`
- **Learning Mode**: Auto-suggest categories based on existing KB entries

### Configuration
```yaml
agentic_nodes:
  gen_sql_summary:
    model: deepseek
    max_turns: 30
```
