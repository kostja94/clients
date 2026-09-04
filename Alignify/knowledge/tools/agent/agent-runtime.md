# AI Agent 运行时 · 知识块（非线性笔记）

**材料范围**：公开网络检索（LangGraph/LangChain、OpenAI Agents SDK、Microsoft Agent Framework、AWS Bedrock AgentCore、Google Cloud Agent Runtime、Temporal、LangSmith Agent Server 等官方文档；InfoQ/TechCrunch 行业报道；HN 社区讨论；**未**引用 Alignify 站内文章或站内 JSON 内容稿。具体定价、配额与 GA 阶段以各官网为准。网摘整理日期 **2026-09-02**。

**站内对照**：slug **`agent-runtime`** · KB only（发文走 `/blog/agent-runtime`）

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) · `keywordEn`: **AI Agent Runtime** · `keywordZh`: **AI Agent 运行时**

## 与相邻 slug 分流

| 维度 | **agent-runtime（本文）** | **backend-as-a-service** | **agent-sandbox** | **agent-memory** | **multi-agent** | **workflow** | **inference-infrastructure** |
|------|---------------------------|--------------------------|-------------------|------------------|-----------------|--------------|--------------------------------|
| 核心问题 | Agent **如何可靠执行**（loop、state、部署、recovery、观测） | **App 共享状态**托管在哪（BaaS） | **在哪隔离跑**不可信代码/Shell | Agent **跨会话记住什么** | 多 Agent **谁做什么、如何 handoff** | **IF/THEN** 确定性流程自动化 | **模型推理**在哪跑（GPU/token） |
| 典型读者 | Agent 平台工程师、架构师 | 全栈 / Vibe / Agent 写 App | 安全/基础设施工程师 | Agent 应用开发者 | 架构师、Team Lead | 运营/集成工程师 | MLOps、平台架构师 |
| 交付形态 | Runtime SDK、托管 Agent Server、云 Runtime API | Auth+DB+Storage+Realtime SDK | 隔离 VM/容器 API | Memory SDK/MCP | 编排图、Supervisor、A2A | Zapier/n8n 式流程 | 推理端点、GPU 集群 |
| 验收核心 | 耐久性、HITL、多租户、trace、部署 SLA | 数据模型、realtime、锁定 | 隔离等级、冷启动、TTL | 检索准确率、scope 治理 | 任务分解、handoff 质量 | 流程成功率 | TTFT、$/1M tokens |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agent Runtime / Agent 运行时**：智能体在 **production** 中的 **执行层基础设施**——托管 agent loop，在多次 LLM 调用之间管理 state、tool invocation、memory、lifecycle、streaming、human-in-the-loop、fault recovery 与 telemetry。回答「Agent 如何**可靠跑完**」，而非「Agent 逻辑怎么写」。
- **Agent Framework / 智能体框架**：编程库，定义 agent 逻辑——tools、graphs、handoffs、prompt 模板。代表：LangChain、CrewAI、AutoGen、Google ADK。**不负责**托管 hosting、跨 crash 恢复、企业 IAM（除非叠托管 runtime）。
- **Agent Harness / 智能体 harness**：比 framework 更高层的 **开箱即用 agent 应用层**——默认 prompt、规划、文件系统、子 agent、guardrails。代表：DeepAgents、Claude Code、Microsoft Agent Harness。**仍需要** runtime 或 sandbox 在其下执行。
- **Execution Loop / Agent Loop**：模型 → tool call → 观察结果 → 再模型，直到终止条件（final tool、无 tool 输出、步数上限、人工审批）。OpenAI **Runner**、Microsoft **Agent Pipeline**、LangGraph **Pregel super-step** 均实现此 loop 的不同形态。
- **Durable Execution / 耐久执行**：进程 crash、网络超时、机器断电后，agent 从 checkpoint **续跑**而非从头重来——Temporal Workflow、LangGraph checkpoint + 外接 DB、AgentCore 托管 session 均属此问题域。社区共识：**框架自带 checkpoint ≠ 完整 production durability**（见 HN + Temporal 官方互证）。
- **Managed Agent Runtime / 托管运行时**：云厂商提供的 framework-agnostic hosting——部署、scaling、identity、memory、observability 一体。代表：Bedrock AgentCore Runtime、Google Agent Runtime、Microsoft Foundry Hosted Agents、LangSmith Agent Server。
- **Sandbox-as-tool vs Harness-outside-sandbox**：OpenAI 2026 架构叙事——**Harness 在可信应用侧**，Sandbox 是被调用的隔离计算面；Claude Agent SDK 旧模式则是 harness 跑在 sandbox 内。Runtime 边界设计受此影响。

---

## 专题对照

### Framework · Harness · Runtime · Sandbox 栈

| 层级 | 职责 | 典型代表 | 不保证什么 |
|------|------|----------|------------|
| Model API | 产生 token / tool-call proposal | OpenAI Responses、Bedrock InvokeModel | 业务 tool 执行、durability |
| **Agent Framework** | 组合 agent 逻辑 | LangChain、CrewAI、ADK | 托管 ops、crash recovery |
| **Agent Harness** |  opinionated 完整 agent | DeepAgents、Copilot Harness | 安全/耐久执行环境 |
| **Agent Runtime** | 执行、state、部署、观测 | LangGraph、AgentCore、Temporal | 完整 governance 平台（视实现） |
| **Sandbox** | 隔离代码/Shell/Browser | E2B、AgentCore microVM | 授权、业务校验 |
| Control Plane | 版本、策略、治理 | Foundry、LangSmith | 低延迟 loop 本身 |

> LangChain 官方口径：LangChain = framework，LangGraph = runtime，DeepAgents = harness——**行业尚无统一定义**，边界仍模糊。

### Runtime 类型谱系（按部署形态）

| 类型 | 特征 | 代表 | 最佳买家 |
|------|------|------|----------|
| **Type I — 框架内嵌 OSS Runtime** | 与框架/SDK 紧耦合；自管部署 | LangGraph (Pregel)、OpenAI Agents SDK Runner、Microsoft Agent Pipeline | 要最大控制、可接受自建 infra |
| **Type II — 框架对齐托管平台** | 框架原生 serving + checkpoint + 部署 | LangSmith Agent Server、DeepAgents deploy | LangGraph 栈、快速上生产 |
| **Type III — 云托管 Agent Runtime** | framework-agnostic；identity/memory/obs  bundled | Bedrock AgentCore、Google Agent Runtime、Foundry Hosted Agents | 企业合规、已有云生态 |
| **Type IV — 耐久 Workflow Runtime** | Workflow/Activity 模型；跨框架 | Temporal (+ LangGraph/OpenAI/ADK 插件) | 长时任务、HITL 等数天、强 SLA |
| **Type V — Serverless Agent 宿主** | 事件触发、scale-to-zero | Azure Functions `.agent.md` runtime | 已有 Functions 团队、轻量 agent |

### 会话时间尺度（2026 云厂商双轨）

| 子类型 | 特征 | 代表 |
|--------|------|------|
| **短会话 Serverless microVM** | 冷启动快、按用量计费、会话隔离；通常 ≤8h | AgentCore microVM、Azure Functions Agents |
| **长会话 Persistent Instance** | EC2/GPU、共享 FS、多 agent 同机；可达 14d | AgentCore Runtime Instances |

---

## 问题域（为何会出现这类产品）

- **从 Demo 到 Production 的鸿沟**：Framework 能跑通 agent loop，但 production 还需 retries、state persistence、crash recovery、observability、multi-tenancy、approval gates——团队否则 **自建 runtime**（Temporal、自建 queue worker 等）。
- **Agent 会话非 HTTP 请求**：传统 serverless 为短、无状态请求设计；agent 会话可持续 **分钟到数天**、跨数十次 tool call——需要 purpose-built runtime（AgentCore、LangGraph durable execution 叙事）。
- **Framework 与 Durability  tradeoff**：LangGraph/CrewAI/ADK 等实现 reasoning loop，但进程 crash 后常需外接 checkpointer 或 Temporal——HN 与 Temporal 官方均将此列为 2026 生产痛点。
- **云厂商 bundled Runtime**：2025–2026 AWS AgentCore、Google Agent Runtime、Microsoft Foundry Runtime、Azure Functions Agents 集中 GA——「Agent 运行时」从框架附属能力升级为 **独立采购品类**。
- **Harness 与 Runtime 分离**：OpenAI、Microsoft 2026 产品将 **应用层 harness** 与 **执行/runtime** 拆开——便于 governance、审计与 sandbox 按需调用。
- **术语混乱成本**：framework/runtime/harness 混用增加架构沟通与选型错误——KB 价值在于 **分流表 + 决策树**，非 SEO 榜单。

---

## 能力栈（概念拆分，非厂商功能表）

- **Agent loop 托管**：自动 tool 循环、handoff、步数/预算 cap、终止条件——OpenAI Runner、RawAgent + FunctionInvocation（Microsoft）。
- **State & Session**：thread/session ID、checkpoint、跨 turn 历史——LangGraph checkpointer、AgentCore session、Foundry Responses API。
- **Persistence & Recovery**：crash 后续跑、幂等 tool、reject 信号语义（openai-agents-js #1104 类 bug 说明 boundary 是 load-bearing contract）。
- **Human-in-the-loop**：interrupt/resume、approval gate、零成本长等待（Temporal `wait_condition`）。
- **Streaming & Concurrency**：token 流、double-texting 控制（LangSmith Deployment）。
- **Multi-tenancy & Auth**：RBAC、Agent Auth、OAuth connection——LangSmith、AgentCore Identity、Foundry。
- **Observability**：OpenTelemetry trace、time travel、run 级 audit——LangSmith、Foundry、AgentCore Observability；**Obs 平台选型 SSOT** → [llm-observability.md](../llm/llm-observability.md)（trace/cost/prompt）；**scorer/CI gate** → [evaluation.md](../llm/evaluation.md)。
- **Deployment & Scaling**：容器/zip 部署、queue worker 水平扩展、API server 与 worker 分离（LangSmith Agent Server 架构）。
- **Sandbox 集成**：Runtime 编排调用隔离执行面——见 [agent-sandbox.md](agent-sandbox.md)；AgentCore Code Interpreter/Browser 为 bundled tool runtime。

---

## 形态谱系 · 代表产品（2026-09）

> **非市场份额排名**——该品类尚无 W3Techs/Gartner 类公开份额统计；按 **场景分组** 列举。

### Lane 1 — 开源 / 框架内嵌 Runtime

| 产品 | 定位 | 备注 |
|------|------|------|
| **LangGraph** | Pregel/BSP 编排 runtime + StateGraph API | LangChain 1.0 构建其上；durable execution 需 checkpointer 或叠 Temporal |
| **OpenAI Agents SDK Runner** | SDK 托管 agent loop、handoffs、sessions | 与 Responses API「自管 loop」对照；Sandbox 分离 |
| **Microsoft Agent Framework** | 分层 pipeline：agent/chat/function middleware | 1.0 GA 2026-04；Harness 为更高层 |
| **Google ADK Runner** | 本地 Runner + 部署到 Agent Runtime | Session/Memory 可接 Vertex AI 服务 |

### Lane 2 — 托管部署 Runtime

| 产品 | 云/生态 | 备注 |
|------|---------|------|
| **LangSmith Agent Server** | LangChain | API server + queue worker；threads/runs/checkpoints |
| **AWS Bedrock AgentCore Runtime** | AWS | framework-agnostic；microVM（≤8h）+ Instances（≤14d，GPU） |
| **Google Cloud Agent Runtime** | GCP | ADK/LangGraph/CrewAI 等模板；Agent Platform SDK |
| **Microsoft Foundry Hosted Agents** | Azure | 托管 sandbox 会话 + consumption 计费 |
| **Azure Functions Serverless Agents** | Azure | `.agent.md` 声明式；Flex Consumption 按秒 |

### Lane 3 — 耐久编排 Runtime（跨框架）

| 产品 | 定位 | 备注 |
|------|------|------|
| **Temporal** | Durable Execution 平台 | OpenAI Agents SDK、LangGraph、Google ADK 均有官方集成 |
| **Temporal × LangGraph 插件** | 无需重写 LangGraph 代码 | Public Preview 2026；crash/HITL 长等待 |

### Lane 4 — 新兴 / 预览

| 产品 | 状态 | 备注 |
|------|------|------|
| **Cloudflare Computer** | 早期 preview | V8 isolate + 按需 container；非生产 |
| **CoreSpeed** 等 Agent-Native Runtime PaaS | 初创宣传 | 127ms 启动、Per-User Container——**待独立 benchmark 验证** |

---

## 架构模式（执行 substrate，非产品）

来源：COMPEL Framework、arXiv runtime patterns 综述——**分类维度：控制流 substrate**。

| 模式 | 特征 | 适用 workload |
|------|------|---------------|
| **State-graph runtime** | 图/状态机；循环、并行 super-step | 可审计 multi-step workflow |
| **Conversation-buffer runtime** | 对话历史为状态；低延迟 | Chat agent、客服 |
| **Task-queue runtime** | 工作项队列 + worker | 高吞吐、批处理型 agent |
| **Actor runtime** | 消息传递、独立 actor | 高并发 multi-agent |

LangGraph 属 **State-graph**；Temporal 常以 **Task-queue/Workflow** 包装任意框架。

---

## 选型决策树（Buyer）

1. **已在哪家云？** AWS → AgentCore；Azure → Foundry/Functions Agents；GCP → Agent Runtime；多云/自托管 → LangGraph + LangSmith 或 Temporal。
2. **会话多长？** 分钟级交互 → microVM/serverless；数小时~数天 + GPU → Runtime Instances 或 Temporal。
3. **要多 durable？** 必须 crash-safe + 长 HITL → **Temporal**（可叠 LangGraph/OpenAI SDK）；可接受自建 checkpointer → LangGraph + Postgres。
4. **框架绑定度？** 已选 LangGraph → LangSmith Deployment 或 AgentCore entrypoint；要框架无关 → AgentCore、Temporal。
5. **与 sandbox 关系？** 仅需隔离 tool 执行 → [agent-sandbox.md](agent-sandbox.md)；要 full stack → AgentCore（Runtime + 沙箱能力 bundled）。

---

## 风险 · 争议 · 社区反响

- **Durability 误解**：误以为 LangGraph InMemory/PostgresSaver 即 production fault tolerance——crash 后 worker 进程丢失时仍需 Temporal 类编排（HN 偏 skeptical，Temporal 官方互证）。
- **Checkpointer 运维成本**：PostgresSaver 连接池、schema、migration——HN 热帖反映「加 memory 即 database setup hell」。
- **Vendor lock-in**：托管 runtime 绑定云 IAM、计费、API 形态——AgentCore/Foundry 的 framework-agnostic 叙事部分缓解，但仍非完全可移植。
- **术语边界模糊**：LangGraph 同时被称 runtime 与 framework——采购与架构文档需 **显式分层**（logic vs execution）。
- **「Agent」定义分歧**：部分开发者认为 predetermined graph = workflow 非 true agent——不影响 runtime 品类 engineering 定义（multi-step + tools + state）。

---

## 产品候选与部署对照（2026-09）

| 产品 | 类型 | 部署 | 最佳买家 |
|------|------|------|----------|
| **LangGraph** | OSS runtime | 自托管 / LangSmith / AgentCore | 要图级控制、混合 deterministic+agentic |
| **LangSmith Agent Server** | 托管 | LangSmith Cloud / 自托管 | LangGraph 栈生产部署 |
| **OpenAI Agents SDK** | SDK runtime | 自有 server | 最快跑通 handoffs + guardrails |
| **Bedrock AgentCore Runtime** | 云托管 | AWS | 企业 AWS 栈、framework-agnostic |
| **Google Agent Runtime** | 云托管 | GCP | ADK 深度集成 |
| **Foundry Hosted Agents** | 云托管 | Azure | Microsoft 365 生态 |
| **Temporal** | 耐久编排 | Cloud / 自托管 | 长任务、强 SLA、跨框架 |
| **Azure Functions Agents** | Serverless | Azure | 事件驱动、`.agent.md` 声明式 |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| LangGraph | OSS orchestration runtime；Pregel | https://docs.langchain.com/oss/python/langgraph/overview |
| LangSmith Agent Server | 托管 Agent Server 架构 | https://docs.langchain.com/langsmith/agent-server |
| OpenAI Agents SDK | Runner 托管 agent loop | https://developers.openai.com/api/docs/guides/agents |
| Microsoft Agent Framework | Agent pipeline 架构 | https://learn.microsoft.com/en-us/agent-framework/agents/agent-pipeline |
| Bedrock AgentCore Runtime | AWS 托管 agent hosting | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html |
| Google Agent Runtime | GCP 托管 Agent Runtime | https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime |
| Temporal AI | Durable execution for agents | https://docs.temporal.io/ai |
| LangChain: Frameworks vs Runtimes | 官方 taxonomy 说明 | https://www.langchain.com/blog/agent-frameworks-runtimes-and-harnesses-oh-my |

---

## 延伸阅读 · 站内外

**站内**

- [agent-identity.md](agent-identity.md) — **Agent IAM / 凭证层**（L1–L3）；与 runtime **正交**
- [agent-sandbox.md](agent-sandbox.md) — Runtime 栈中的 **Execute（隔离）** 层；microVM/Devbox
- [agent-memory.md](agent-memory.md) — Runtime 的 **Memory** 组件；Mem0/Zep/Letta
- [multi-agent.md](multi-agent.md) — 多 Agent **编排拓扑**；与 runtime 执行基底分工
- [workflow.md](workflow.md) — **确定性**流程自动化；非 agent loop
- [backend-as-a-service.md](../infrastructure/backend-as-a-service.md) — **App 态** BaaS（Convex/Supabase）；非 Agent Runtime
- [agent-skills.md](agent-skills.md) — MCP/技能层；Runtime 调用的能力面
- [llm-observability.md](../llm/llm-observability.md) — **Observe 层** SSOT：trace/span/cost/prompt；与 runtime **telemetry 出口**对齐
- [evaluation.md](../llm/evaluation.md) — **Eval 层**：scorer/CI；生产 trace 采样打分（与 obs 接缝）
- [inference-infrastructure.md](../infrastructure/inference-infrastructure.md) — **模型推理**托管；与 agent orchestration 分流