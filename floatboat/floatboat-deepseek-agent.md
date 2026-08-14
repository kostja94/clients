# Floatboat × DeepSeek Agent — SEO 与竞品简报

> **本文职责**：汇总 DeepSeek Agent 小产品的 SEO 关键词、DeepSeek 原生竞品格局与内容机会。不含通用「可接 DeepSeek」编排平台（Dify / Coze / FastGPT 等）。  
> 关联：[floatboat.md](./floatboat.md) | [floatboat-keywords.md](./floatboat-keywords.md) | [floatboat-competitors.md](./floatboat-competitors.md) | [README.md](./README.md)

**产品假设**：基于 DeepSeek API + Floatboat 编排，构建以 DeepSeek 为核心卖点的 Agent 产品。  
**Last updated**: 2026-07-23  
**信息来源**：DeepSeek 官方 docs / awesome-deepseek-agent、公开竞品站与社区项目调研（会话整理）

---

## 1. 一句话结论

| 维度 | 结论 |
|------|------|
| 品类现状 | 「DeepSeek Agent」仍是**品类搜索词**，尚未被成熟商业 SaaS 独占 |
| 真实竞品 | 几乎全是 **DeepSeek 原生 Coding Agent（终端/CLI）**，非业务编排平台 |
| SEO 窗口 | 品牌词 + 搭建教程 + 成本/替代对比，现在占位成本最低 |
| 产品差异化 | 避开「又一个终端 Coding Agent」；做 **DeepSeek API + Floatboat 编排** 的产品化 Agent |

---

## 2. SEO 关键词

### 2.1 核心品牌 / 品类词（优先占位）

| 关键词 | 意图 | 说明 |
|--------|------|------|
| DeepSeek Agent | 品牌/品类 | 主词，竞争升温中，需尽早做落地页 |
| DeepSeek 智能体 | 中文主词 | 国内常用说法 |
| DeepSeek Agent 平台 | 产品词 | 适合产品首页 |
| Floatboat DeepSeek Agent | 品牌组合 | 建立 Floatboat 与品类关联 |

### 2.2 高转化商业词（落地页 / 产品页）

- DeepSeek Agent 搭建
- DeepSeek 智能体 搭建 / 创建
- DeepSeek API Agent
- DeepSeek 智能体开发平台
- 无代码 DeepSeek Agent
- DeepSeek Agent 编排 / workflow / 工作流
- DeepSeek 多智能体 / multi-agent DeepSeek

### 2.3 技术开发词（教程 / 文档引流）

- DeepSeek Function Calling
- DeepSeek Tool Calls / 工具调用
- DeepSeek API Agent 教程
- DeepSeek ReAct Agent
- DeepSeek V4 Agent / DeepSeek V4 API Agent
- DeepSeek OpenAI compatible Agent
- DeepSeek MCP Agent
- DeepSeek coding agent / DeepSeek 编程智能体
- DeepSeek agent loop / 智能体循环

> 说明：`Function Calling` + 搭建教程往往是稳定流量入口，再内链到产品页。

### 2.4 对比替代词（决策期，转化高）

- DeepSeek Agent vs Claude Code
- DeepSeek 替代 Claude Agent
- DeepSeek Agent vs DeepSeek-TUI / Reasonix / Deep Code
- Claude Code DeepSeek 替代
- 便宜的 AI Agent（DeepSeek）
- DeepSeek-TUI 替代 / 对比

### 2.5 场景与成本长尾

**场景**：DeepSeek 代码审查 Agent · 数据分析 Agent · SQL Agent · 客服智能体 · RAG / 知识库智能体 · Git 自动化 Agent  

**成本 / 接入**：DeepSeek Agent 成本 · DeepSeek API 价格 Agent · 低成本 AI Agent DeepSeek · DeepSeek V4 Flash Agent · DeepSeek API Key Agent · 国内调用 DeepSeek Agent

### 2.6 英文市场补充

- DeepSeek AI agent
- build DeepSeek agent
- DeepSeek agent framework / agent builder
- DeepSeek tool calling agent
- DeepSeek agentic workflow
- cheap AI agent DeepSeek
- DeepSeek coding agent
- DeepSeek multi-agent orchestration

### 2.7 内容优先级

**P0（先做 3–5 页）**

1. `DeepSeek Agent` / `DeepSeek 智能体`（品牌落地页）
2. `DeepSeek Agent 搭建` / `DeepSeek API Agent`
3. `DeepSeek Function Calling`（教程引流 → 产品）
4. `DeepSeek Agent vs Claude Code`（替代决策）
5. `低成本 DeepSeek Agent` / `DeepSeek Agent 平台`

**P1**：按场景拆编程 / 数据分析 / 客服 / RAG / 工作流编排；每篇 1 主词 + 3–5 长尾。

**市场差异**：国内偏「智能体 / 搭建 / API / Function Calling」；海外偏 `agent`、`coding agent`、`tool calling`、`vs Claude`。

---

## 3. DeepSeek 原生竞品（重点）

> **范围**：DeepSeek 原生 / 专属 Agent。  
> **排除**：Dify、Coze、FastGPT、n8n，以及 Claude Code / Cline「换模型接 DeepSeek」类通用 Agent。

### 3.1 官方 awesome 清单中的 DeepSeek-native（核心 3 个）

来源：[deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent)

| 产品 | 类型 | DeepSeek 绑定 | 要点 | SEO 相关词 |
|------|------|---------------|------|------------|
| **DeepSeek-TUI** | 终端 Coding Agent（Rust） | 面向 V4 Pro/Flash | 1M 上下文、Plan/Agent/YOLO、沙盒、MCP、子 Agent；社区热度最高 | DeepSeek-TUI、DeepSeek coding agent |
| **Reasonix** | 终端 Coding Agent | **自称 DeepSeek-native** | 围绕 prefix cache 做长会话低成本；Flash 默认、可升 Pro | Reasonix、DeepSeek native agent |
| **Deep Code** | 终端 + VS Code | 面向 DeepSeek-V4 | thinking / reasoning effort / Agent Skills | Deep Code、DeepSeek V4 agent |

这三者是 SEO 对比页与竞品文的**主对标对象**。

### 3.2 社区 DeepSeek-first（次级对标）

| 产品 | 特点 |
|------|------|
| **deepx-code** | DeepSeek 标配 Coding Agent；缓存友好、CodeGraph、OCR；亦扩 MiMo |
| **DeepseekNova** | Rust 框架，「为 DeepSeek 量身打造」；CLI / TUI / Desktop |
| **DeepSeekCode / dsc** | DeepSeek-first 终端 Agent；部分带 Web / Desktop |

形态仍高度同质：**开发者本地 Coding Agent**，不是面向业务的 DeepSeek Agent 平台。

### 3.3 官方未上线产品（品牌威胁最大）

| 名称 | 状态 | 含义 |
|------|------|------|
| **DeepSeek Code / Code Harness** | 招人中；桌面端 Agent，对标 Claude Code | 上线后将直接抢占 `DeepSeek Agent` / `DeepSeek Code` 等品牌搜索 |

媒体已有「DeepSeek 智能体产品要来了」类报道 → **品牌词窗口期有限**。

### 3.4 易误判对象（不算同类产品）

| 对象 | 为何排除 |
|------|----------|
| deepseekagent.io | SEO 导流站（教把 Codex/Claude Code 接到 DeepSeek），本身不是产品 |
| Claude Code / Cline / OpenCode + DeepSeek | 通用 harness 换模型 |
| Dify / Coze / FastGPT | 编排平台，DeepSeek 仅为可选后端 |

### 3.5 SEO 对标清单（建议只盯这些）

**主盯**：DeepSeek-TUI · Reasonix · Deep Code  

**次级**：deepx-code · DeepseekNova  

**预埋**：DeepSeek Code / DeepSeek Harness（官方）

---

## 4. 竞争含义与 Floatboat 机会

| 赛道 | 竞品密度 | 建议 |
|------|----------|------|
| Coding CLI Agent | 很卷（TUI / Reasonix / Deep Code） | 不宜再做「又一个终端 Agent」 |
| DeepSeek 深度编排 + 场景 Agent | 相对空 | **主战场**：API + Floatboat 编排 + 明确场景 |
| 官方 Code Harness | 未来威胁大 | 避开纯 coding harness；偏业务编排与产品化体验 |

**可写进对外叙事的差异点：**

1. 重点是 **DeepSeek**（模型与成本优势），不是泛多模型平台话术。
2. **编排层是 Floatboat**（工作流 / Agent 产品化），不是裸 API 或纯终端 harness。
3. 用品牌页承接 `DeepSeek Agent`，用教程（Function Calling）与对比页（vs TUI / Reasonix / Claude Code）截流。

---

## 5. 建议落地动作（内容）

| 优先级 | 页面 / 内容 | 主词 | 目的 |
|--------|-------------|------|------|
| P0 | 产品落地页 | DeepSeek Agent / DeepSeek 智能体 | 占品类品牌词 |
| P0 | 搭建指南 | DeepSeek Agent 搭建、DeepSeek API Agent | 高意图转化 |
| P0 | Function Calling 教程 | DeepSeek Function Calling | 技术流量 → 产品 |
| P0 | 对比页 | vs Claude Code / vs DeepSeek-TUI / vs Reasonix | 决策截流 |
| P1 | 成本专题 | 低成本 DeepSeek Agent、V4 Flash | 商业意图 |
| P1 | 场景矩阵 | 编程以外的垂直场景（按产品实际能力选） | 长尾与差异化 |

---

## 6. 资料索引

| 资源 | URL / 路径 |
|------|------------|
| Awesome DeepSeek Agent（官方） | https://github.com/deepseek-ai/awesome-deepseek-agent |
| DeepSeek Agent 工具接入文档 | https://api-docs.deepseek.com/zh-cn/guides/coding_agents |
| Tool Calls 文档 | https://api-docs.deepseek.com/zh-cn/guides/tool_calls |
| Reasonix 接入 | https://api-docs.deepseek.com/zh-cn/quick_start/agent_integrations/reasonix/ |
| Floatboat 主文档 | [floatboat.md](./floatboat.md) |
| Floatboat 关键词总表 | [floatboat-keywords.md](./floatboat-keywords.md) |
| Floatboat 竞品总表 | [floatboat-competitors.md](./floatboat-competitors.md) |

---

*整理自 2026-07-23 内部调研会话；后续若官方 DeepSeek Code 上线或 awesome 清单变更，应同步更新 §3。*
