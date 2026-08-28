
# CLI 命令参考

## 三大魔法命令

| 命令 | 前缀 | 用途 |
|------|------|------|
| Chat | `/` | 多轮对话，自然语言交互 |
| Context | `@` | 按需唤起元数据/指标上下文 |
| Execution | `!` | 确定性、可脚本化的工具操作 |

---

## Chat Command (`/`)

### 基本用法
```
/ How many orders were placed last week?
/ Filter only for VIP customers
```

### Context Injection
- **Browse Mode**: 输入 `@` + Tab，按目录结构浏览并选择
- **Fuzzy Search Mode**: 输入 `@` + 关键词 + Tab，模糊搜索匹配

### Session Commands
| 命令 | 功能 |
|------|------|
| `.clear` | 清除当前 session 上下文 |
| `.compact` | 压缩历史轮次以降低内存（自动触发于 90% 上下文使用） |
| `.chat_info` | 显示当前活跃上下文（消息、表、指标） |
| `.resume [session_id]` | 恢复之前的 session |
| `.rewind [turn_number]` | 回退到指定用户轮次，创建分支 session |

### 其他功能
- 按 **ESC** 或 **Ctrl+C** 中断执行
- 按 **Ctrl+O** 切换 trace 显示模式（compact / verbose）

---

## Context Command (`@`)

### 三种上下文树
- `@catalog` — 物理数据结构（数据库、模式、表）
- `@subject` — 语义/业务层（领域、层、语义模型、指标）
- `@sql` — 历史 SQL 查询（仅内联注入）

### 上下文注入模式
- **Browse**: `@catalog` + Tab → 逐节点导航
- **Fuzzy Search**: `@revenue` + Tab → 跨所有上下文字段搜索
- **Inline**: `/ pay attention to @Table @Metrics @Sql @File`

### 编辑功能
- `@catalog` 面板: Ctrl+e 修改语义模型
- `@subject` 领域树: Ctrl+e 修改领域层和名称
- `@subject` 指标详情: Ctrl+e 修改指标

---

## Execution Command (`!`)

### Schema Discovery
| 命令 | 功能 |
|------|------|
| `!sl` / `!schema_linking` | 智能模式链接，发现相关表和列 |
| `!sm` / `!search_metrics` | 自然语言搜索指标 |
| `!sq` / `!search_sql` | 自然语言搜索历史 SQL |

### Utilities
| 命令 | 功能 |
|------|------|
| `!save` | 保存最后查询结果（json/csv/sql/all） |
| `!bash` | 执行安全 bash 命令 |

### `!bash` 白名单
`pwd`, `ls`, `cat`, `head`, `tail`, `echo`  
超时 10 秒，非白名单命令被拒绝。

---

## SQL Execution

直接运行 SQL 查询（不依赖 Agent）：

```
Datus-sql> SELECT * FROM users WHERE status = 'active';
```

### 元数据命令
| 命令 | 功能 |
|------|------|
| `.databases` | 列出所有数据库 |
| `.database <name>` | 切换当前数据库 |
| `.schemas` | 列出所有模式 |
| `.schema <name>` | 切换当前模式 |
| `.tables` | 列出当前模式下的所有表 |
| `.table_schema <table>` | 显示表结构 |
| `.indexes <table>` | 显示表索引 |

### 查询历史
- 所有执行的查询自动保存
- 上下箭头键访问历史
- 跨 session 持久化
- 与 `@sql` 上下文系统集成

---

## MCP Extensions

### Subcommands
| 命令 | 功能 |
|------|------|
| `.mcp add <name> <command>` | 添加 MCP 服务器（stdio/http/sse） |
| `.mcp list` | 列出所有服务器和状态 |
| `.mcp check <name>` | 检查连接和可用工具 |
| `.mcp call <name>.<tool>` | 调用服务器工具 |
| `.mcp remove <name>` | 移除服务器 |
| `.mcp filter set/get/remove` | 工具过滤（include/exclude） |

### Server Types
- **stdio** — 启动本地子进程，通过 stdin/stdout 通信
- **http** — 连接可流式传输的 HTTP 端点
- **sse** — 连接 Server-Sent Events 端点

### 存储
- 所有 MCP 配置存储在 `~/.datus/conf/.mcp.json`
- 支持环境变量扩展: `${VAR}` 或 `${VAR:-default}`

---

## Plan Mode (Beta)

按 **Shift+Tab** 切换 Plan Mode，将复杂任务分解为可审查步骤。

### 三阶段工作流
1. **Plan Generation** — AI 分析需求，创建分步计划
2. **User Confirmation** — 选择执行模式
3. **Execution** — 按选择模式执行

### 四种执行模式
| 模式 | 适用场景 |
|------|---------|
| Manual Confirm | 需要逐步审查的任务 |
| Auto Execute | 定义明确、无需逐步审查的任务 |
| Revise | 提供反馈重新生成计划 |
| Cancel | 安全退出 |

### 进度追踪
- ✓ 绿色勾 — 已完成
- ▶ 黄色箭头 — 当前步骤
- ○ 白色圆圈 — 待处理步骤

---

## CLI Commands 配置命令

### Setup
| 命令 | 功能 |
|------|------|
| `datus configure` | 交互式配置 LLM provider、数据库连接、工作区设置 |
| `datus init` | 初始化项目工作区，生成 `AGENTS.md` |

### Service Management
| 命令 | 功能 |
|------|------|
| `datus service list` | 列出所有数据库、BI 工具、调度器 |
| `datus service add` | 交互式添加数据库连接 |
| `datus service delete` | 交互式删除数据库连接 |

### Database Selection
```bash
datus-cli --database my_duckdb
datus run --database my_duckdb --task "show tables" --task_db_name demo
```
自动选择逻辑：标记了 `default: true` 的数据库 → 唯一配置的数据库 → 显示可用列表

### 配置迁移
```bash
# 预览迁移（dry run）
python -m datus.configuration.config_migrator --config conf/agent.yml --dry-run

# 迁移（备份原文件到 agent.yml.bak）
python -m datus.configuration.config_migrator --config conf/agent.yml
```

---

## Skill Command (CLI)

### Subcommands
| 命令 | 功能 |
|------|------|
| `datus skill login` | 认证 Town Marketplace |
| `datus skill logout` | 清除认证 token |
| `datus skill list` | 列出本地技能 |
| `datus skill search <query>` | 搜索 Marketplace |
| `datus skill install <name> [version]` | 安装技能 |
| `datus skill publish <dir> [--owner]` | 发布技能到 Marketplace |
| `datus skill info <name>` | 查看技能详情 |
| `datus skill update` | 更新所有 marketplace 技能 |
| `datus skill remove <name>` | 移除本地技能 |

### REPL 等价
```
datus> .skill list
datus> .skill search sql
datus> .skill install sql-optimization
datus> .skill publish ./skills/my-skill
datus> .skill update
```

### 配置
```yaml
skills:
  directories:
    - ~/.datus/skills
    - ./skills
  marketplace_url: "http://localhost:9000"
  auto_sync: false
  install_dir: "~/.datus/skills"
```
