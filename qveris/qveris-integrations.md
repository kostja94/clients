# QVeris — 支持的 Agent 与集成方式

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[主文档](./qveris.md) | [features](./qveris-features.md) | [site-structure](./qveris-site-structure.md)

**Last updated**: 2026-08-03

## 1. 支持概览

QVeris 支持 **14+ 种 Agent 平台/客户端**，接入方式分为四类：**CLI**、**MCP Server**、**SDK**（Python/TS）、**REST API**。几乎所有具备 shell 或 MCP 能力的 Agent 均可接入。

| 类别 | 客户端/产品 | 接入方式 | 官方页面 |
|------|------------|---------|---------|
| 第一方产品 | QVeris CLI | 独立安装（全局可用） | [/cli](https://qveris.ai/cli) |
| 第一方产品 | QVerisBot | 独立安装（多消息渠道） | [/qverisbot](https://qveris.ai/qverisbot) |
| 第一方产品 | QVerisFlow | 独立安装（多 Agent 工作流） | [/ecosystem](https://qveris.ai/ecosystem) |
| Agent 客户端 | **Claude Code** | CLI（推荐）/ MCP / Skill | [/docs/claude-code-setup](https://qveris.ai/docs/claude-code-setup) |
| Agent 客户端 | **Cursor** | MCP | [/docs/mcp-server](https://qveris.ai/docs/mcp-server) |
| Agent 客户端 | **OpenCode** | MCP / CLI / Skill | [/docs/opencode-setup](https://qveris.ai/docs/opencode-setup) |
| Agent 客户端 | **OpenClaw** | 插件（推荐）/ Skill | [/docs/openclaw-setup](https://qveris.ai/docs/openclaw-setup) |
| Agent 客户端 | **Hermes Agent** | CLI（内置沙盒） | [/for-agents](https://qveris.ai/for-agents) |
| Agent 客户端 | **Trae** | MCP | [/docs/ide-cli-setup](https://qveris.ai/docs/ide-cli-setup) |
| Agent 客户端 | **VS Code** | 插件 / MCP | [/docs/ide-cli-setup](https://qveris.ai/docs/ide-cli-setup) |
| Agent 客户端 | **Codex（含 ChatGPT Desktop）** | MCP / Skill | [/docs/ide-cli-setup](https://qveris.ai/docs/ide-cli-setup) |
| 通用接入 | 任意 MCP 兼容客户端 | MCP Server | [/docs/mcp-server](https://qveris.ai/docs/mcp-server) |
| 通用接入 | 任意支持 shell 的 Agent | CLI | [/cli](https://qveris.ai/cli) |
| 通用接入 | 任意编程环境 | Python SDK / TS SDK / REST API | [/docs/rest-api](https://qveris.ai/docs/rest-api) |

## 2. 第一方产品

### 2.1 QVeris CLI
- **定位**：零 Token 工具调用——以子进程方式执行，schema 不进入 LLM 上下文
- **安装**：`curl -fsSL https://qveris.ai/cli/install | bash` 或 `npm install -g @qverisai/cli`（或 `npx @qverisai/cli`）
- **版本**：v0.8.0
- **特性**：交互式 REPL、`--json` 结构化输出、`--codegen`（curl/Python/JS）、`qveris doctor` 自检、`qveris usage/ledger` 账单审计
- **适用**：有 shell 访问权限的 Agent（Claude Code、OpenClaw、Hermes 等）

### 2.2 QVerisBot
- **定位**：基于 OpenClaw 引擎的生产级 AI 助手，原生集成 QVeris 工具箱（qveris_discover/inspect/call）
- **安装**：`npm i -g @qverisai/qverisbot && qverisbot onboard`
- **渠道**：WhatsApp、Telegram、Slack、Discord、飞书、iMessage、Teams 及 20+ 更多平台
- **特性**：会话级 Tool Rolodex、跨会话记忆、多渠道收件箱；接入 500+ 数据提供商、10,000+ 能力

### 2.3 QVerisFlow
- **定位**：基于 LangGraph 的多 Agent 工作流引擎
- **特性**：自然语言建工作流、可视化画布编辑器（ReactFlow）、Meta Agent 自动生成 Agent 定义、多模型支持（Qwen/DeepSeek/GPT/GLM/Kimi）、三层验证
- **适用**：金融分析、研究自动化、数据处理等复杂多 Agent 管线

## 3. Agent 客户端接入详情

### 3.1 Claude Code
| 项 | 内容 |
|----|------|
| 接入方式 | CLI（推荐，零 Token）/ MCP / Skill |
| 官方教程 | https://qveris.ai/docs/claude-code-setup |
| MCP 配置 | `claude mcp add qveris --transport stdio --scope user --env QVERIS_API_KEY=xxx -- npx -y @qverisai/mcp`（Windows 用 `cmd /c npx ...` 包裹） |
| 自动生成 | `qveris mcp configure --target claude-code` |
| Skill 安装 | 从 GitHub `qveris-agent-toolkit` 下载 SKILL.md 至 `~/.claude/skills/qveris/` |

### 3.2 Cursor
| 项 | 内容 |
|----|------|
| 接入方式 | MCP |
| 官方教程 | https://qveris.ai/docs/mcp-server |
| MCP 配置 | `mcpServers.qveris = { command: "npx", args: ["-y", "@qverisai/mcp"], env: { QVERIS_API_KEY: "xxx" } }` |
| 自动生成 | `qveris mcp configure --target cursor [--write --include-key]`；`qveris mcp validate --target cursor --probe` 校验 |

### 3.3 OpenCode
| 项 | 内容 |
|----|------|
| 接入方式 | MCP / CLI / Skill |
| 官方教程 | https://qveris.ai/docs/opencode-setup |
| MCP 配置 | `~/.config/opencode/opencode.json` 中添加 `mcp.qveris`（type: local, command: npx @qverisai/mcp）+ `tools["qveris*"]: true` |
| Skill 安装 | 下载 SKILL.md 至 `~/.config/opencode/skill/qveris/` |

### 3.4 OpenClaw
| 项 | 内容 |
|----|------|
| 接入方式 | **插件（推荐）** / Skill |
| 官方教程 | https://qveris.ai/docs/openclaw-setup |
| 插件安装 | `openclaw plugins install @qverisai/qveris`，并在 `openclaw.json` 配置 `plugins.allow` / `plugins.entries` / `tools.alsoAllow` |
| Skill 安装 | `openclaw skills install qveris-official`（ClawHub），配置 `skills.entries["qveris-official"]` |
| 特性 | 插件为运行时级工具注册，不受上下文长度影响 |

### 3.5 Hermes Agent
| 项 | 内容 |
|----|------|
| 接入方式 | CLI（内置 shell 沙盒） |
| 官方教程 | https://qveris.ai/for-agents |
| 安装 | `curl -fsSL https://qveris.ai/cli/install | bash && qveris login` |
| 特性 | 装一次 CLI 即原生可用，零 Hermes 侧配置；凭证存于 `~/.qveris/config` 跨会话持久 |

### 3.6 Trae / VS Code / Codex（IDE 与 CLI 工具系列）
| 项 | 内容 |
|----|------|
| 接入方式 | MCP / 插件 / Skill |
| 官方教程 | https://qveris.ai/docs/ide-cli-setup |
| 说明 | GUI IDE（VS Code 等）按 Plugins 页装插件；CLI 工具（Codex、ChatGPT Desktop、Claude Code、OpenCode）有独立配置页 |
| 自动安装 | 可让编码 Agent 自动配置：`Configure this for me <配置指南 URL>。The API key is <key>` |

## 4. 通用接入方式

| 方式 | 适用场景 | 说明 | 页面 |
|------|---------|------|------|
| **MCP Server**（@qverisai/mcp v0.12.0） | 任何 MCP 兼容客户端（Cursor、Claude Desktop、OpenCode 等） | 提供 6 个工具：discover/inspect/probe/call/usage_history/credits_ledger；另提供远程 Hosted MCP（`https://mcp.qveris.ai/mcp`） | [/docs/mcp-server](https://qveris.ai/docs/mcp-server) |
| **CLI**（@qverisai/cli v0.8.0） | 有 shell 的 Agent / 终端开发者 | 零 Token、--json 结构化输出、--dry-run、stdin 管道、结构化退出码 | [/cli](https://qveris.ai/cli) |
| **Python SDK**（pip install qveris v0.3.1） | Python Agent / 后端 | 全类型化 API、异步支持、重试逻辑、流式输出 | [/docs/python-sdk](https://qveris.ai/docs/python-sdk) |
| **TypeScript SDK**（@qverisai/sdk v0.4.0） | JS/TS 环境（Node/Deno/Edge） | 零依赖类型化客户端、原生 fetch | [/docs](https://qveris.ai/docs) |
| **REST API** | 任意语言/后端服务 | `POST /search`、`POST /tools/by-ids`、`POST /tools/execute`；Bearer Token 认证 | [/docs/rest-api](https://qveris.ai/docs/rest-api) |

## 5. 协议工具矩阵（MCP ↔ REST）

| 协议动作 | MCP 工具 | REST API |
|---------|---------|---------|
| 发现 | discover | POST /search |
| 检查 | inspect | POST /tools/by-ids |
| 预验证 | probe | POST /tools/probe |
| 调用 | call | POST /tools/execute |
| 用量审计 | usage_history | GET /auth/usage/history/v2 |
| 账本 | credits_ledger | GET /auth/credits/ledger |

## 6. 生态与社区

| 资源 | 说明 | 链接 |
|------|------|------|
| ClawHub Skills | OpenClaw / Claude 的社区技能包（qveris-official 等） | https://qveris.ai/skills |
| GitHub Org | 全部开源仓库（CLI、MCP server、Python SDK、示例 Agent、skills） | https://github.com/QVerisAI |
| npm | @qverisai/cli / @qverisai/mcp / @qverisai/sdk / @qverisai/qverisbot | https://www.npmjs.com |
| PyPI | qveris（Python SDK） | https://pypi.org |
| Plugins | OpenClaw 插件页 | https://qveris.ai/plugins |

## 7. 待验证项

- [ ] "14+ 平台"的确切总数与完整清单（官网仅列出主要客户端，完整列表 ⚠️ 待验证）
- [ ] Trae / VS Code 插件安装的具体步骤（IDE 系列页仅指引至 Plugins 页）
- [ ] QVerisFlow 是否已有独立产品页或仅见于 ecosystem 页
- [ ] 各 npm 包版本号以官网 /ecosystem 与 /docs 最新声明为准（本文档记录 2026-08-03 抓取值：cli v0.8.0、mcp v0.12.0、sdk v0.4.0、python v0.3.1）

---

*Last updated 2026-08-03 · 数据来源：/ecosystem、/docs、/docs/claude-code-setup、/docs/opencode-setup、/docs/ide-cli-setup、/for-agents（访问日期 2026-08-03）*
