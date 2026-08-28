# 多智能体系统 · 知识块（非线性笔记）

**材料范围**：公开网络检索（LangGraph/CrewAI/OpenAI Agents SDK/Google ADK 官方文档、Microsoft Copilot Studio 与 IBM watsonx Orchestrate 产品页、Multica/Moxt/Clawith 官网与文档、Google A2A 协议说明、Anthropic MCP 文档、arXiv 多智能体综述与行业分析）；归纳 **Multi-Agent Systems / 多智能体系统**——多个 AI Agent 在任务分解、角色分工、状态共享、工具路由与组织治理上的编排框架、企业平台与团队工作空间。**未**引用 Alignify 站内文章或站内 JSON 内容稿。具体定价、部署方式与协议支持以各官网为准。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/multi-agent](https://alignify.co/blog/multi-agent) · [alignify.co/zh/blog/multi-agent](https://alignify.co/zh/blog/multi-agent) · 正文 md 已同步至部署仓 `alignify-by-kostja/content/blog/{en|zh}/multi-agent.md` · slug **`multi-agent`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#multi-agent-tools`](../../product/alignify-keywords-tools.md#multi-agent-tools)）· `keywordEn`: **Multi-Agent Systems** · `keywordZh`: **多智能体系统（底层：多智能体协作 / Agent 编排）

## 与相邻 slug 分流

| 维度 | **multi-agent（本文）** | **workflow** | **agent-for-desktop** | **openclaw-alternatives** | **agent-skills** |
|------|-------------------------|--------------|----------------------|----------------------------|------------------|
| 核心问题 | 多个 Agent **谁做什么、如何 handoff 与治理**——含 Swarm 范式 | 多步流程 **IF/THEN 自动化** | **单人**本机 Agent 操作文件/GUI | OpenClaw **生态替代与 Gateway** | Agent **能力包**如何安装/发现 |
| 典型读者 | 架构师、平台负责人、Team Lead | 运营/集成工程师 | 知识工作者、个人 Power User | OpenClaw 自托管用户 | 开发者、Agent 构建者 |
| 交付形态 | 编排图、Supervisor/Crew、Swarm、A2A/MCP、团队 Workspace | Zapier/n8n 式流程 | 桌面客户端、本地文件夹 | Gateway/Channel 栈 | SKILL.md、MCP Server |
| 验收核心 | 任务分解质量、Agent 间协作、权限与审计 | 流程成功率、异常分支 | 本机/GUI 操作成功率 | 自托管、Channel 覆盖 | 技能命中率、工具调用 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Multi-Agent System / 多智能体系统**：由两个及以上自主或半自主 Agent 协作完成复杂任务的架构——含角色定义、任务路由、共享状态与失败恢复。与「单 Agent + 长上下文」相对：当子任务可并行、需专长分工或组织权限隔离时，多 Agent 成为默认设计。
- **Agent Orchestration / Agent 编排**：定义 Agent 拓扑（顺序、并行、层级 Supervisor）与 handoff 条件的控制层——LangGraph 图状态机、CrewAI Crew、OpenAI Agents SDK handoff 均属此层。与 **workflow** 的区别：编排对象是可推理的 Agent，而非固定 API 节点。
- **Supervisor / Worker 模式**：一个协调 Agent 分解任务并分派给 specialist Worker——常见于企业平台与框架默认模板。风险：Supervisor 成为单点瓶颈与成本中心。
- **Handoff / 任务移交**：Agent A 将子任务与上下文打包交给 Agent B——OpenAI Agents SDK 与 LangGraph 均为一等概念。Handoff 质量取决于状态 schema 与 trace 可观测性。
- **A2A（Agent-to-Agent Protocol）**：Google 等推动的 Agent 互操作协议——描述 Agent 卡片、任务委托与跨运行时消息。与 MCP 互补：MCP 连工具与数据，A2A 连 Agent 实体。**勿与** slug **`agent-to-agent`**（消费级 Agent 社交/广播网络）混谈——后者是产品形态谱系，见 [agent-to-agent.md](agent-to-agent.md)。
- **MCP（Model Context Protocol）**：Agent 调用外部工具/数据源的协议层——多 Agent 栈中常由共享或 per-agent MCP Server 提供能力。见 [agent-skills.md](agent-skills.md)。
- **Multi-Agent Workspace / 多 Agent 工作空间**：为团队设计的 Agent-native 协作界面——人类与 Agent 共享任务、权限、记忆与文件树（Multica、Moxt、Clawith）。与「旧协作 SaaS + AI 侧边栏」相对：Agent 是一等成员而非插件。
- **Human-in-the-Loop Governance**：敏感 handoff、工具调用与跨 Agent 数据流需人工审批——企业平台（Copilot Studio、watsonx Orchestrate）与 Clawith 等强调 RBAC、审计日志。
- **Agent-native Harness**：为 Agent 持久身份、记忆、触发器与工具发现而设计的运行时外壳——单 Agent harness 壁垒有限，**多 Agent 协调层**（组织关系、权限、信任）更难被模型权重 alone 替代。

---

## 专题对照 / 扩展定义

| 二分维度 | A 方向 | B 方向 |
|------|------|------|
| **买家路径** | **L1 自建框架**（LangGraph、CrewAI、OpenAI Agents SDK） | **L2 企业平台**（Copilot Studio、watsonx Orchestrate） |
| **协作界面** | **L3 Agent Workspace**（Multica、Moxt、Clawith） | **L4 功能内嵌**（IDE/PPT 内 multi-agent——**不归本文 BestTools**） |
| **拓扑** | **Supervisor 层级** | **对等 Crew / 流水线 Sequential** |
| **运行位置** | **本地 daemon + 云端控制面**（Multica） | **全托管 SaaS**（部分 Moxt/Clawith 部署选项） |
| **协议** | **MCP 工具层** | **A2A Agent 互操作层** |

---

## 问题域（为何会出现这类产品）

- **单 Agent 上下文与注意力瓶颈**：复杂项目需并行研究、编码、测试、审核——一个 Agent 的长上下文无法同时保持全链路状态。
- **组织级权限与信任**：企业内「每人一个 Agent」后，跨部门 handoff、数据分级与审计成为采购硬需求——模型能力无法替代 IAM 与 org chart。
- **框架碎片化**：2024–2026 开源框架爆发（LangGraph、CrewAI、AutoGen/AG2、ADK），买家需要 **选型地图** 而非单一脚本。
- **协作 SaaS 的 Agent 原生缺口**：Notion/Slack 加 AI 侧边栏是改良；Floatboat/Moxt/Clawith 等主张 **为 Agent 设计的工作空间**（文件、触发器、持久记忆并列）。
- **协议标准化窗口**：MCP 统一工具接入，A2A 尝试统一 Agent 互操作——降低多厂商 Agent 混编成本。
- **OpenClaw 个人→团队扩展**：个人 Gateway 难以承载组织关系——Clawith 等「OpenClaw for Teams」补 Crew、Plaza、RBAC。
- **可观测与成本失控**：多 Agent 循环对话、重复 tool call 可指数级烧钱——生产栈需 trace、预算 cap 与降级策略。

---

## 能力栈（概念拆分，非厂商功能表）

- **任务分解与规划**：将用户目标拆为可验收子任务——Planner/Supervisor 的职责边界需产品化。
- **角色与 Prompt 模板**：Researcher、Coder、Reviewer 等 persona——CrewAI 以此命名，企业平台以「预制 Agent 类型」出售。
- **共享状态与记忆**：线程级、Agent 级、Workspace 级记忆分层——Clawith soul.md/memory.md、Moxt 团队共享记忆为代表叙事。
- **工具路由与 MCP**：每 Agent 可见工具集不同——最小权限原则在多 Agent 场景更关键。
- **Handoff 与消息总线**：Agent 间结构化消息（非纯自然语言聊天）——减少歧义与循环对话。
- **触发与自主性**：Cron、Webhook、事件感知（Clawith Aware、OpenClaw heartbeat 升级）——从「用户 @ 才动」到「持续感知」。
- **治理与审计**：RBAC、审批流、quota、租户隔离——L2/L3 企业向核心卖点。
- **可观测性**：OpenTelemetry、LangSmith 类 trace——调试 multi-agent 生产故障的必需品。

---

## 形态谱系（与具体品牌解耦）

- **Lane 1 — 编排框架 / SDK**：开发者自建，图或 Crew 定义拓扑；部署在自有云或 laptop。代表：LangGraph、CrewAI、OpenAI Agents SDK、Google ADK、AutoGen/AG2。
- **Lane 2 — 企业多 Agent 平台**：低代码/无代码 Agent 编排，绑定 Microsoft 365、IBM 企业连接器与合规。代表：Copilot Studio、watsonx Orchestrate、CrewAI Enterprise。
- **Lane 3 — Multi-Agent Workspace**：团队任务、Agent 一等成员、本地或混合运行时。代表：Multica、Moxt、Clawith、MateClaw、Eigent（团队向）；Floatboat 团队协议（Selfware/IACT）偏 L3 但个人向见 [agent-for-desktop.md](agent-for-desktop.md)。
- **Lane 4 — 功能内嵌型多 Agent**：垂直产品内多 Agent 引擎（Pi 演示、Windsurf Multi-Agent Editor、Medo 全栈生成）——**正文分流，不进本文 8 款主榜**。

---

## Agent Swarms / 智能体蜂群（Multi-Agent 的去中心化子范式）

### 与传统编排的区分

Agent Swarms（智能体蜂群）是 Multi-Agent Systems 的一种**去中心化子范式**——与 Supervisor/Worker 层级编排不同，Swarm 中的 Agent **没有中央控制器**，靠简单规则自组织、涌现式完成协作。所有 Swarm 都是 Multi-Agent，但不是所有 Multi-Agent 都是 Swarm。

| 维度 | **传统 Multi-Agent 编排** | **Agent Swarms（蜂群范式）** |
|------|------|------|
| **控制方式** | Supervisor 分配、图状态机、静态角色 | **去中心化**——无中央控制器，自组织涌现 |
| **拓扑** | 显式定义（层级/顺序/对等 Crew） | **动态自主**——Agent 自行决定参与/退出/委托/终止 |
| **适应性** | 通过 handoff schema 与 checkpoint 伸缩 | **运行时自重构**——可动态生成新 Agent、调整通信拓扑 |
| **设计哲学** | 组织治理优先——角色、权限、审计、RBAC | **仿生集体智能**——蚁群/蜂群式简单规则→复杂行为 |
| **典型场景** | 企业 IT、合规敏感流程、团队协作 | 大规模并行探索、持续自适应系统、博弈仿真 |
| **代表框架** | LangGraph、CrewAI、OpenAI Agents SDK | SwarmAgentic、AgentSpawn、DynaSwarm、Agent Swarm（desplega） |

### 关键特征

- **自组织**：无 Supervisor 调度，Agent 间通过对等消息或共享环境自主协调。
- **涌现行为**：整体行为从简单 Agent 规则中"涌现"——更灵活，但也更难预测和调试。
- **动态规模**：运行时可对等加入/退出，适合输入负载波动或未知任务结构的场景。
- **类比**：传统编排像「项目经理分活给团队成员」；Swarm 像「蚂蚁找食物——没有谁指挥，但整体找到最优路径」。

### 主流 Swarm 产品与框架（知名大模型/AI 公司）

| 名称 | 背后公司 | 一句话 | 类型 | 可用性 | URL |
|------|:--------:|------|------|:------:|-----|
| **Kimi Agent Swarm** | **Moonshot AI（月之暗面）** | 模型内生 Swarm 能力——通过 PARL 训练，单次自动调度最多 300 子 Agent、4,000 步并行执行，速度提升 4.5×。K2.5 起原生支持，不需要手动编排 | 模型原生能力 | Beta，Kimi Web/App/API | [kimi.com](https://www.kimi.com/zh-cn/help/agent/agent-swarm) |
| **OpenAI Swarm** | **OpenAI** | 轻量级多 Agent 编排实验框架——Agent + handoff 原语，22K GitHub Stars。2025 年已被 Agents SDK 取代，但作为 Swarm 概念推手有历史地位 | 教育框架 | 已归档（Archived） | [github.com/openai/swarm](https://github.com/openai/swarm) |
| **Anthropic Dynamic Workflows** | **Anthropic** | Claude Code / Opus 4.8 内置的模型原生 Swarm 编排——Claude 自主分解目标、派生成百上千并行 subagent，在单会话内协调完成大规模任务 | 模型原生能力 | Claude Code CLI/Desktop/API | [claude.com](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) |
| **Claude Research** | **Anthropic** | Anthropic 的多 Agent 研究系统——orchestrator-worker 模式，并行 subagent 搜索+验证，用于复杂开放调研 | 产品功能 | Claude 内置 | [anthropic.com](https://www.anthropic.com/engineering/multi-agent-research-system) |
| **Google ADK + A2A** | **Google** | Agent Development Kit 层级委托 + A2A 协议跨框架互操作——Google 推动的 Agent 间任务委托标准 | 框架 + 协议 | 开源 | [google.github.io/adk-docs](https://google.github.io/adk-docs/) |
| **SwarmAgentic** | 学术研究 | 语言驱动 PSO 全自动生成并优化多 Agent 系统——给定任务描述自动产出功能+协作策略，EMNLP 2025 | 研究框架 | 开源 | [github.com/SwarmAgentic](https://github.com/SwarmAgentic) |

> **注**：Kimi Agent Swarm 是目前唯一将 "Agent Swarm" 作为产品名、且以「模型内生能力」交付的商业产品——它不是一个需要开发者手动编排的框架，而是 Kimi K2.5/K2.6 模型在遇到复杂任务时自动触发的能力。OpenAI Swarm 虽已归档，但作为该命名的行业推手仍有历史参考价值。

### 与本文 Lane 分类的关系

- **Lane 1（编排框架）补充**：传统图状态机/Crew 聚焦显式拓扑；Swarm 提供**对等去中心化/模型内生拓扑**选项。Kimi Agent Swarm 和 Anthropic Dynamic Workflows 代表了「编排不再需要单独框架，模型自己就会」的方向。
- **胖模型 vs 胖框架之争**：2026 年一个关键趋势——当 Kimi K2.6 和 Claude Opus 4.8 自身就能 Swarm，LangGraph/CrewAI 这类编排框架的定位从「必需」退为「可选的精细控制层」。
- **OpenAI Swarm 到 Agents SDK 的演进**：从 Swarm 的实验性去中心化原语，到 Agents SDK 的生产级 handoff + guardrails——反映了 Swarm 理念从研究验证到工程化的路径。
- **SwarmAgentic** 偏学术，推动从「静态配置」到「PSO 自动化搜索最优拓扑」的前沿方向。

### 风险提示（Swarm 特有）

- **涌现不可预测**：Swarm 行为是涌现结果，golden task 回归更难设计，错误模式更隐蔽。
- **成本更难 cap**：无 Supervisor 兜底 → 多 Agent 可能无限循环对齐，预算 cap 与 max turns 设计更复杂。
- **可观测性挑战**：传统 trace 工具假设显式拓扑；对等 Swarm 需要新的通信图可视化与死锁检测方法。
- **安全面扩大**：每个 Agent 可自主委托其他 Agent → 最小权限原则更难静态分析。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **越权 handoff**：Agent A 将含 PII 的上下文交给无权限的 Agent B——需数据标签与策略引擎。
- **循环与死锁**：Agent 互相等待或重复确认——需 max turns、超时与 supervisor 强制终止。
- **成本失控**：多 Agent × 多轮 × 大模型 = 不可预测账单——需 per-workflow budget 与模型降级。
- **供应链**：第三方 MCP、A2A endpoint 扩大攻击面——固定 allowlist 与版本 pinning。
- **劳动与自动化条款**：Agent 代操作 SaaS/内部系统可能触及 ToS——企业 IT 需白名单。
- **开源自托管责任**：Clawith、Multica 等自托管时，租户隔离与密钥管理归买家运维。

---

## 落地碎片（无先后）

- 先选 **Lane**：有工程团队 → L1；要 M365/合规无代码 → L2；要团队共享 Agent 状态 → L3。
- 从 **2-Agent Supervisor** 试点，再扩 Crew——避免一上来 10 Agent 不可调试。
- 协议层优先 **MCP +（可选）A2A 可互操作** 产品，降低未来换框架成本。
- 与 [workflow.md](workflow.md) 分流：固定 API 链用 workflow；需推理与角色分工用 multi-agent。
- Floatboat/Clawith 与 [openclaw-alternatives.md](openclaw-alternatives.md)、[agent-for-desktop.md](agent-for-desktop.md) 交叉阅读，避免重复选型叙事。
- 生产必配 **trace + golden task** 回归——多 Agent 行为非确定性高于单 Agent。

---

## 工具与产品类型（「multi-agent framework」「agent orchestration」「agent workspace」检索常混；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Graph / State 编排框架** | LangGraph、LangGraph Platform | 图状态机、checkpoint、HITL |
| **Role-based Crew 框架** | CrewAI、CrewAI Enterprise | 角色化 Crew、快速原型 |
| **Vendor SDK** | OpenAI Agents SDK、Google ADK | 绑定 GPT/Gemini 栈 |
| **Legacy / 演进框架** | AutoGen、AG2、Microsoft Agent Framework | AutoGen 维护模式变化，选型看官方路线图 |
| **企业 Agent 平台** | Copilot Studio、watsonx Orchestrate | 连接器、RBAC、无代码 |
| **Agent Workspace** | Multica、Moxt、Clawith | 团队任务 + 持久 Agent |
| **个人桌面 Agent** | Floatboat、OpenClaw | 见 agent-for-desktop / openclaw-alternatives |
| **SaaS 工作流** | Zapier、n8n AI | 见 workflow，非 Agent 编排主路径 |

---

## 外链索引（工具与平台；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **LangGraph** | LangChain 生态图状态机编排，生产向 checkpoint/HITL | [langchain.com/langgraph](https://www.langchain.com/langgraph) |
| **CrewAI** | 角色化 Crew 多 Agent 框架，开源 + Enterprise | [crewai.com](https://www.crewai.com/) |
| **OpenAI Agents SDK** | Handoff、guardrails、tracing 的 GPT 原生多 Agent SDK | [openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python/) |
| **Google ADK** | Gemini 栈 Agent Development Kit，层级委托与 A2A 叙事 | [google.github.io/adk-docs](https://google.github.io/adk-docs/) |
| **Microsoft Copilot Studio** | M365 生态低代码多 Agent 与自动化 | [microsoft.com/microsoft-copilot/microsoft-copilot-studio](https://www.microsoft.com/en-us/microsoft/copilot/microsoft-copilot-studio) |
| **IBM watsonx Orchestrate** | 企业 HR/IT 等多 Agent 工作流，80+ 连接器 | [ibm.com/products/watsonx-orchestrate](https://www.ibm.com/products/watsonx-orchestrate) |
| **Multica** | Linear 式 PM + Agent 一等成员，本地 daemon 驱动 CLI Agent | [multica.ai](https://www.multica.ai/) |
| **Moxt** | Agent-native Workspace，Markdown/Skills/Slack 集成 | [moxt.ai](https://moxt.ai/) |
| **Clawith** | 开源 OpenClaw for Teams，Aware 感知、Plaza、RBAC | [clawith.ai](https://www.clawith.ai/) |
| **AutoGen / AG2** | 微软系对话式多 Agent（维护状态以官方为准） | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/) |
| **Google A2A** | Agent-to-Agent 互操作协议公开说明 | [developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) |
| **Model Context Protocol** | Anthropic 发起的 Agent 工具协议 | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |

### 对比与测评（第三方；观点非官方）

2025–2026 **multi-agent** 检索混四层：框架（Lane 1 最多）、企业平台（Lane 2 中等）、Agent Workspace（Lane 3 **偏少但在涨**）、产品内嵌功能（Lane 4 极多但非独立品类）。LangGraph 与 CrewAI 在开发者社区能见度最高；OpenAI Agents SDK 与 Google ADK 绑定各自模型栈。企业买家常 **Copilot Studio vs watsonx Orchestrate** 与现有 IT 栈绑定选型。

**Multica** 差异化在「Agent 像同事一样被 assign issue」+ 本地 daemon 执行——控制面在云端、算力与密钥在本地。**Moxt** 强调 Agent-native 文件格式（md/csv/html）与 Slack 内 momo。**Clawith** 将 OpenClaw 个人能力扩展为 Crew + Aware + 企业治理——与 [openclaw-alternatives.md](openclaw-alternatives.md) 互补而非替代。

**常见误购**：把 **workflow** 自动化当 multi-agent；把 **IDE 内 multi-agent 编辑** 当组织级协调层；把 **单 Agent 长 prompt** 当 Crew——应先用 Lane 三分法定位买家 moment。

*本小节为网摘与行业观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **Multi-Agent Systems survey**（arXiv 等综述类论文）——理解拓扑与通信模式术语。
- **Google A2A announcement** — Agent 互操作协议背景。
- **LangGraph documentation** — StateGraph、checkpoint、human-in-the-loop 模式。
- **OpenAI Agents SDK docs** — Handoff 与 tracing 实践。
- **Alignify · Agent Skills**：[agent-skills.md](agent-skills.md)——能力层 MCP/Skill。
- **Alignify · Workflow**：[workflow.md](workflow.md)——固定流程自动化分流。
- **Alignify · Agent on Desktop**：[agent-for-desktop.md](agent-for-desktop.md)——单人本机 Agent。
- **Alignify · OpenClaw 系谱**：[openclaw-alternatives.md](openclaw-alternatives.md)——Gateway 与个人栈。
- **Alignify · Agent-to-Agent Network**：[agent-to-agent.md](agent-to-agent.md)——Agent 社交/广播网络（≠ 本文 A2A Protocol 任务委托）。
