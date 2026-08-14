# Integration

## 1. MCP Server

Expose Datus's database and context search tools via the Model Context Protocol (MCP).

### Server Modes
- **Static Mode**: Single namespace, suitable for Claude Desktop, CLI tools, or single-tenant HTTP/SSE server
- **Dynamic Mode**: Multi-namespace HTTP/SSE server, supports all namespaces via URL path

### Transport Modes
- `http`: Streamable HTTP (bidirectional, default)
- `sse`: Server-Sent Events over HTTP (for web clients)
- `stdio`: Standard input/output (for Claude Desktop and CLI tools)

### Quick Start
```bash
# Static Mode: Single namespace
datus-mcp --namespace <your namespace>
datus-mcp --namespace <your namespace> --transport http --host 127.0.0.1 --port 8000

# Dynamic Mode: Multi-namespace HTTP/SSE server
datus-mcp --dynamic --transport http --host 127.0.0.1 --port 8000
datus-mcp --dynamic --transport sse --host 127.0.0.1 --port 8000
```

### Claude Code Integration
```bash
# Start server (SSE mode)
datus-mcp --dynamic --transport sse --port 8000

# Add to Claude Code
claude mcp add --transport sse datus http://127.0.0.1:8000/sse/<your namespace>
```

### Claude Desktop Integration
```json
{
  "mcpServers": {
    "datus-agent": {
      "command": "npx",
      "args": [
        "mcp-remote@latest",
        "http://127.0.0.1:8000/sse/<your namespace>",
        "--transport",
        "sse-only"
      ]
    }
  }
}
```

### Dynamic Mode URL Patterns
- HTTP: `http://localhost:8000/mcp/{namespace}`
- SSE: `http://localhost:8000/sse/{namespace}`
- With subagent: `http://localhost:8000/mcp/{namespace}?subagent={subagent_name}`
- Info: `http://localhost:8000/` — Server info and available namespaces
- Health: `http://localhost:8000/health`

### Available Tools
| Category | Tools |
|----------|-------|
| Database | `list_databases`, `list_schemas`, `list_tables`, `search_table`, `describe_table`, `get_table_ddl`, `read_query` |
| Context Search | `list_subject_tree`, `search_metrics`, `get_metrics`, `search_reference_sql`, `get_reference_sql`, `search_semantic_objects`, `search_knowledge`, `get_knowledge` |

---

## 2. Auto Memory

Auto Memory is a persistent memory system for Datus-agent that enables agents to automatically retain valuable information across conversations.

### Key Characteristics
- **File-based**: Memory stored as plain Markdown files, no vector DB or embedding required
- **Two-layer structure**: Concise `MEMORY.md` main file auto-loaded into context, plus optional topic sub-files
- **Per-subagent isolation**: Each subagent has its own memory directory
- **Zero configuration**: No setup needed — eligible agents are automatically enabled

### Memory Directory Structure
```
{workspace_root}/
└── .datus/
    └── memory/
        ├── chat/                    # Built-in chat agent
        │   ├── MEMORY.md           # Main file: auto-loaded (≤200 lines)
        │   ├── patterns.md         # Sub-file: read on demand
        │   └── conventions.md
        └── my_custom_agent/        # Custom subagent
            ├── MEMORY.md
            └── domain.md
```

### Which Agents Have Memory?
| Agent Type | Memory Enabled |
|------------|:---:|
| `chat` (built-in main agent) | ✅ |
| Custom subagents | ✅ |
| Built-in system subagents (`gen_sql`, `gen_report`, etc.) | ❌ |
| `explore` | ❌ |

### Two-Layer Memory
**L1: MEMORY.md** (Main File)
- Automatically loaded at start of every conversation
- Capped at 200 lines
- Best for: user preferences, key project structure, frequently referenced conventions, links to L2 files

**L2: Topic Sub-files**
- Read by agent on demand via `read_file`
- No line limit
- Best for: detailed debugging notes, complex domain patterns, extended decision records

### Usage Examples
```bash
> Remember that I prefer DuckDB
> Remember the project uses snake_case naming convention
> Forget my DuckDB preference
> That's wrong, our project uses PostgreSQL, not DuckDB
> Read your current memory file
```

### Memory Behavior
The agent automatically decides what is worth saving:
- ✅ Stable patterns confirmed across interactions
- ✅ Key decisions and project structure
- ✅ User preferences and workflow habits
- ✅ Solutions to recurring problems
- ❌ Temporary details of current task
- ❌ Incomplete, unverified information
- ❌ Speculative conclusions from one interaction
- ❌ In-progress work state

---

## 3. Skills

Skills is a skill discovery and loading system for Datus-agent, following the agentskills.io specification.

### Quick Start

**1. Create a Skill**
```
~/.datus/skills/
└── report-generator/
    ├── SKILL.md
    └── scripts/
        ├── generate_report.py
        ├── analyze_data.py
        └── validate.sh
```

**SKILL.md format:**
```markdown
---
name: report-generator
description: Generate analysis reports from SQL query results
tags: [report, analysis, visualization, export]
version: "1.0.0"
allowed_commands:
  - "python:scripts/*.py"
  - "sh:scripts/*.sh"
---

# Report Generator Skill
...
```

**2. Configure in agent.yml:**
```yaml
skills:
  directories:
    - ~/.datus/skills
    - ./skills
  warn_duplicates: true

permissions:
  default: allow
  rules:
    - tool: skills
      pattern: "*"
      permission: ask
    - tool: skill_bash
      pattern: "*"
      permission: ask
```

### Permission System
| Level | Behavior |
|-------|----------|
| `allow` | Skill available and can be used freely |
| `deny` | Skill hidden from agent |
| `ask` | User confirmation required before each use |

### Using Skills in Subagents
```yaml
agentic_nodes:
  school_report:
    node_class: gen_report
    tools: db_tools.*, context_search_tools.*
    mcp: metricflow_mcp
    skills: "report-*, data-*"
    model: deepseek
```

### Skills in Isolated Subagent
```yaml
---
name: deep-analysis
description: Perform comprehensive data analysis
tags: [analysis, research]
context: fork
agent: Explore
---
```
Available subagent types: `Explore`, `Plan`, `general-purpose`

### Invocation Control
| Field | Default | Description |
|-------|---------|-------------|
| `disable_model_invocation` | `false` | If true, only user can invoke via `/skill-name` |
| `user_invocable` | `true` | If false, hidden from CLI menu |

### Skill Marketplace CLI
```bash
datus skill login --marketplace http://datus-marketplace:9000
datus skill search sql
datus skill install sql-optimization
datus skill publish ./skills/my-skill --owner "murphy"
datus skill info sql-optimization
datus skill update
datus skill remove sql-optimization
```

**REPL equivalents:**
```
datus> .skill list
datus> .skill search sql
datus> .skill install sql-optimization
datus> .skill publish ./skills/my-skill
datus> .skill info sql-optimization
datus> .skill update
datus> .skill remove sql-optimization
```

### Skill Frontmatter Fields
| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique skill identifier |
| `description` | Yes | Brief description shown in available skills list |
| `tags` | No | List of tags for categorization |
| `version` | No | Semantic version string |
| `allowed_commands` | No | List of permitted script patterns |
| `context` | No | Set to `"fork"` to run in subagent |
| `agent` | No | Subagent type: `Explore`, `Plan`, `general-purpose` |
| `disable_model_invocation` | No | If true, only user can invoke |
| `user_invocable` | No | If false, hidden from CLI menu |
