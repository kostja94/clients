# 多智能体系统 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Multi-Agent Systems / 多智能体系统**——多个 AI Agent 在任务分解、角色分工、状态共享、工具路由与组织治理上的编排；验收以 **handoff 质量、Lane 选型、Swarm vs Supervisor 拓扑** 为主。本页为 **Multi-Agent 框架与 Workspace 产品 SSOT**（完整 URL 表仅此一处）；A2A 消费社交网络 → [agent-to-agent.md](agent-to-agent.md)；Workflow 确定性管道 → [workflow.md](workflow.md)；OpenClaw Gateway → [openclaw-alternatives.md](openclaw-alternatives.md)。

**材料范围**：公开网络检索（LangGraph/CrewAI/OpenAI Agents SDK/Google ADK 官方文档、Copilot Studio / watsonx Orchestrate 产品页、Multica/Moxt/Clawith 官网、Google A2A 协议说明、arXiv 综述）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/multi-agent](https://alignify.co/blog/multi-agent) · slug **`multi-agent`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#multi-agent-tools`](../../product/alignify-keywords-tools.md#multi-agent-tools)）

---

## 与相邻 slug 分流

| 维度 | **multi-agent（本文）** | **ai-employee** | **workflow** | **work-agent** | **workspace-agent** | **agent-for-desktop** | **openclaw-alternatives** | **agent-skills** |
|------|-------------------------|-----------------|--------------|----------------|---------------------|----------------------|----------------------------|------------------|
| 核心问题 | 多个 Agent **谁做什么、如何 handoff 与治理** | **IM 频道**里共享同事协作 | 多步 **IF/THEN 自动化** | 个人 **委派交付物** | 团队 **共享 playbook** | **单人**本机 Agent | OpenClaw **Gateway** | Agent **能力包** |
| 典型读者 | 架构师、平台负责人、Team Lead | 销售/支持/运营 Lead | 运营/集成工程师 | PM、分析师 | Sales ops、IT admin | 知识工作者 | 自托管 OpenClaw 用户 | 开发者 |
| 验收核心 | 任务分解、协作、权限与审计 | thread 交活 + 审批 | 流程成功率 | 交付物可编辑 | 流程稳定、API/审计 | 本机/GUI 成功率 | 自托管、Channel 覆盖 | 技能命中率 |

**禁写注记**：**Raft**（Botiverse）= 多 Agent 编排/监督框架，canonical 归属 **`multi-agent`**，**勿**当 IM AI Employee 写入 [ai-employee.md](ai-employee.md)。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Multi-Agent System / 多智能体系统**：由两个及以上自主或半自主 Agent 协作完成复杂任务的架构——含角色定义、任务路由、共享状态与失败恢复。
- **Agent Orchestration / Agent 编排**：定义 Agent 拓扑（顺序、并行、层级 Supervisor）与 handoff 条件的控制层——LangGraph、CrewAI、OpenAI Agents SDK 均属此层。与 **workflow** 的区别：编排对象是可推理的 Agent，而非固定 API 节点。
- **Supervisor / Worker 模式**：一个协调 Agent 分解任务并分派给 specialist Worker——风险：Supervisor 成为单点瓶颈与成本中心。
- **Handoff / 任务移交**：Agent A 将子任务与上下文打包交给 Agent B——Handoff 质量取决于状态 schema 与 trace 可观测性。
- **A2A（Agent-to-Agent Protocol）**：Google 等推动的 Agent 互操作协议——描述 Agent 卡片、任务委托与跨运行时消息。与 MCP 互补：MCP 连工具与数据，A2A 连 Agent 实体。**勿与** slug **`agent-to-agent`**（消费级 Agent 社交/广播网络）混谈。
- **MCP（Model Context Protocol）**：Agent 调用外部工具/数据源的协议层——见 [agent-skills.md](agent-skills.md)。
- **Multi-Agent Workspace / 多 Agent 工作空间**：为团队设计的 Agent-native 协作界面——人类与 Agent 共享任务、权限、记忆与文件树（Multica、Moxt、Clawith）。**勿与** OpenAI **Workspace Agents**（[workspace-agent.md](workspace-agent.md)）混谈。
- **Human-in-the-Loop Governance**：敏感 handoff、工具调用与跨 Agent 数据流需人工审批。
- **Agent-native Harness**：多 Agent 协调层（组织关系、权限、信任）比单 Agent harness 更难被模型权重 alone 替代。

---

## 专题对照 / 扩展定义

**Lane 与拓扑二分**（术语见 §词汇锚点；Lane 定义见 §形态谱系）：

| 二分维度 | A 方向 | B 方向 |
|------|------|------|
| **买家路径** | **L1 自建框架**（LangGraph、CrewAI、OpenAI Agents SDK） | **L2 企业平台**（Copilot Studio、watsonx Orchestrate） |
| **协作界面** | **L3 Agent Workspace**（Multica、Moxt、Clawith） | **L4 功能内嵌**（IDE/PPT 内 multi-agent——**不归本文 BestTools**） |
| **拓扑** | **Supervisor 层级** | **对等 Crew / 流水线 Sequential / Swarm 去中心化** |
| **协议** | **MCP 工具层** | **A2A Agent 互操作层** |

---

## 问题域（为何会出现这类产品）

- **单 Agent 上下文与注意力瓶颈**：复杂项目需并行研究、编码、测试、审核——一个 Agent 的长上下文无法同时保持全链路状态。
- **组织级权限与信任**：企业内「每人一个 Agent」后，跨部门 handoff、数据分级与审计成为采购硬需求。
- **框架碎片化**：2024–2026 开源框架爆发，买家需要 **选型地图** 而非单一脚本。
- **协作 SaaS 的 Agent 原生缺口**：Notion/Slack 加 AI 侧边栏是改良；Multica/Moxt/Clawith 等主张 **为 Agent 设计的工作空间**。
- **协议标准化窗口**：MCP 统一工具接入，A2A 尝试统一 Agent 互操作。
- **OpenClaw 个人→团队扩展**：Clawith 等「OpenClaw for Teams」补 Crew、Plaza、RBAC。
- **可观测与成本失控**：多 Agent 循环对话、重复 tool call 可指数级烧钱——生产栈需 trace、预算 cap 与降级策略。

---

## 能力栈（概念拆分，非厂商功能表）

- **任务分解与规划**：将用户目标拆为可验收子任务。
- **角色与 Prompt 模板**：Researcher、Coder、Reviewer 等 persona。
- **共享状态与记忆**：线程级、Agent 级、Workspace 级记忆分层。
- **工具路由与 MCP**：每 Agent 可见工具集不同——最小权限原则。
- **Handoff 与消息总线**：Agent 间结构化消息——减少歧义与循环对话。
- **触发与自主性**：Cron、Webhook、事件感知（Clawith Aware、OpenClaw heartbeat）。
- **治理与审计**：RBAC、审批流、quota、租户隔离。
- **可观测性**：OpenTelemetry、LangSmith 类 trace。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Lane | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **L1** | 开发者自建，图或 Crew 定义拓扑 | Graph / Crew / SDK orchestration | LangGraph、CrewAI、OpenAI Agents SDK、Google ADK、AutoGen/AG2 |
| **L2** | 低代码/无代码 Agent 编排，绑定企业连接器与合规 | Enterprise agent platform | Copilot Studio、watsonx Orchestrate、CrewAI Enterprise |
| **L3** | 团队任务、Agent 一等成员、本地或混合运行时 | Multi-agent workspace | Multica、Moxt、Clawith、MateClaw、Eigent（团队向） |
| **L4** | 垂直产品内多 Agent 引擎 | Embedded multi-agent | Pi、Windsurf Multi-Agent Editor——**正文分流，不进主榜** |

**Swarm 子范式**（Lane 1 补充，详见 §Agent Swarms）：去中心化、无中央 Supervisor——与 L1 层级编排正交；Kimi Agent Swarm、Anthropic Dynamic Workflows 代表「模型内生 Swarm」方向。

---

## Agent Swarms / 智能体蜂群（Multi-Agent 的去中心化子范式）

**与传统编排的区分**（Supervisor 定义见 §词汇锚点）：Swarm 中的 Agent **没有中央控制器**，靠简单规则自组织、涌现式完成协作。所有 Swarm 都是 Multi-Agent，但不是所有 Multi-Agent 都是 Swarm。

| 维度 | **传统 Multi-Agent 编排（L1 层级）** | **Agent Swarms（蜂群范式）** |
|------|------|------|
| **控制方式** | Supervisor 分配、图状态机、静态角色 | **去中心化**——无中央控制器，自组织涌现 |
| **拓扑** | 显式定义（层级/顺序/对等 Crew） | **动态自主**——Agent 自行决定参与/退出/委托/终止 |
| **设计哲学** | 组织治理优先——RBAC、审计 | **仿生集体智能**——简单规则→复杂行为 |
| **代表** | LangGraph、CrewAI、OpenAI Agents SDK | Kimi Agent Swarm、Anthropic Dynamic Workflows、OpenAI Swarm（已归档） |

**Swarm 特有产品（规格见 §外链索引 Swarm 表）**：Kimi Agent Swarm 是目前唯一将 "Agent Swarm" 作为产品名、且以「模型内生能力」交付的商业产品。OpenAI Swarm 虽已归档，但作为该命名的行业推手仍有历史参考价值。

**胖模型 vs 胖框架之争（2026）**：当 Kimi K2.6 和 Claude Opus 4.8 自身就能 Swarm，LangGraph/CrewAI 等编排框架的定位从「必需」退为「可选的精细控制层」。

**Swarm 特有风险**：涌现不可预测（golden task 回归难设计）；成本更难 cap（无 Supervisor 兜底）；可观测性挑战（需新通信图可视化）；安全面扩大（每个 Agent 可自主委托）。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **越权 handoff**：Agent A 将含 PII 的上下文交给无权限的 Agent B。
- **循环与死锁**：需 max turns、超时与 supervisor 强制终止。
- **成本失控**：多 Agent × 多轮 × 大模型 = 不可预测账单。
- **供应链**：第三方 MCP、A2A endpoint 扩大攻击面。
- **开源自托管责任**：Clawith、Multica 等自托管时，租户隔离与密钥管理归买家运维。

---

## 落地碎片（无先后）

- 先选 **Lane**：有工程团队 → L1；要 M365/合规无代码 → L2；要团队共享 Agent 状态 → L3。
- 从 **2-Agent Supervisor** 试点，再扩 Crew——避免一上来 10 Agent 不可调试。
- 协议层优先 **MCP +（可选）A2A 可互操作** 产品。
- 与 [workflow.md](workflow.md) 分流：固定 API 链用 workflow；需推理与角色分工用 multi-agent。
- Floatboat/Clawith 与 [openclaw-alternatives.md](openclaw-alternatives.md)、[agent-for-desktop.md](agent-for-desktop.md) 交叉阅读。
- 生产必配 **trace + golden task** 回归。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

### 编排框架与 Workspace（Lane 1–3）

| 名称 | Lane | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **LangGraph** | L1 | LangChain 生态图状态机编排，生产向 checkpoint/HITL | [langchain.com/langgraph](https://www.langchain.com/langgraph) |
| **CrewAI** | L1/L2 | 角色化 Crew 多 Agent 框架，开源 + Enterprise | [crewai.com](https://www.crewai.com/) |
| **OpenAI Agents SDK** | L1 | Handoff、guardrails、tracing 的 GPT 原生多 Agent SDK | [openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python/) |
| **Google ADK** | L1 | Gemini 栈 Agent Development Kit，层级委托与 A2A 叙事 | [google.github.io/adk-docs](https://google.github.io/adk-docs/) |
| **Microsoft Copilot Studio** | L2 | M365 生态低代码多 Agent 与自动化 | [microsoft.com/microsoft-copilot/microsoft-copilot-studio](https://www.microsoft.com/en-us/microsoft/copilot/microsoft-copilot-studio) |
| **IBM watsonx Orchestrate** | L2 | 企业 HR/IT 等多 Agent 工作流，80+ 连接器 | [ibm.com/products/watsonx-orchestrate](https://www.ibm.com/products/watsonx-orchestrate) |
| **Multica** | L3 | Linear 式 PM + Agent 一等成员，本地 daemon 驱动 CLI Agent | [multica.ai](https://www.multica.ai/) |
| **Moxt** | L3 | Agent-native Workspace，Markdown/Skills/Slack 集成 | [moxt.ai](https://moxt.ai/) |
| **Clawith** | L3 | 开源 OpenClaw for Teams，Aware 感知、Plaza、RBAC | [clawith.ai](https://clawith.ai/) |
| **AutoGen / AG2** | L1 | 微软系对话式多 Agent（维护状态以官方为准） | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) |
| **Google A2A** | 协议 | Agent-to-Agent 互操作协议公开说明 | [developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) |
| **Model Context Protocol** | 协议 | Anthropic 发起的 Agent 工具协议 | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |

### Swarm 产品与框架

| 名称 | 背后公司 | 一句话 | 可用性 | URL |
|------|:--------:|------|:------:|-----|
| **Kimi Agent Swarm** | Moonshot AI | 模型内生 Swarm；PARL 训练；最多 300 子 Agent、4,000 步并行 | Beta | [kimi.com/zh-cn/help/agent/agent-swarm](https://www.kimi.com/zh-cn/help/agent/agent-swarm) |
| **OpenAI Swarm** | OpenAI | 轻量级多 Agent 编排实验框架；2025 已被 Agents SDK 取代 | 已归档 | [github.com/openai/swarm](https://github.com/openai/swarm) |
| **Anthropic Dynamic Workflows** | Anthropic | Claude Code / Opus 4.8 内置模型原生 Swarm 编排 | Claude Code/API | [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) |
| **Claude Research** | Anthropic | orchestrator-worker 模式，并行 subagent 搜索+验证 | Claude 内置 | [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) |
| **SwarmAgentic** | 学术研究 | 语言驱动 PSO 全自动生成并优化多 Agent 系统；EMNLP 2025 | 开源 | [github.com/SwarmAgentic](https://github.com/SwarmAgentic) |

### 对比与测评（第三方；观点非官方）

2025–2026 **multi-agent** 检索混四层：框架（L1 最多）、企业平台（L2 中等）、Agent Workspace（L3 **偏少但在涨**）、产品内嵌功能（L4 极多但非独立品类）。LangGraph 与 CrewAI 在开发者社区能见度最高；OpenAI Agents SDK 与 Google ADK 绑定各自模型栈。

Multica 差异化在「Agent 像同事一样被 assign issue」+ 本地 daemon 执行。Moxt 强调 Agent-native 文件格式与 Slack 内 momo。Clawith 将 OpenClaw 个人能力扩展为 Crew + Aware + 企业治理——与 [openclaw-alternatives.md](openclaw-alternatives.md) 互补而非替代。

**常见误购**：把 **workflow** 自动化当 multi-agent；把 **IDE 内 multi-agent 编辑** 当组织级协调层；把 **单 Agent 长 prompt** 当 Crew——应先用 Lane 三分法定位买家 moment。

*本小节为网摘与行业观点综合，非 Alignify 实测。*

---
## 延伸阅读 · 站内外

**站外**

- Multi-Agent Systems survey（arXiv 等综述类论文）
- Google A2A announcement · LangGraph documentation · OpenAI Agents SDK docs

**站内**

- Agent Runtime：[agent-runtime.md](agent-runtime.md)——生产执行层（loop、state、部署）；Sandbox 为其 Execute 层
- Agent Identity：[agent-identity.md](agent-identity.md)——企业 Agent IAM / handoff 身份链
- Agent Skills：[agent-skills.md](agent-skills.md)
- Workflow：[workflow.md](workflow.md)
- Agent on Desktop：[agent-for-desktop.md](agent-for-desktop.md)
- OpenClaw 系谱：[openclaw-alternatives.md](openclaw-alternatives.md)
- Agent-to-Agent Network：[agent-to-agent.md](agent-to-agent.md)——Agent 社交/广播网络（≠ 本文 A2A Protocol 任务委托）