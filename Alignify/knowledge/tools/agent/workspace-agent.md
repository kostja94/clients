# Workspace Agent（工作区智能体）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Workspace Agent / 团队可复用 AI Agent**——在组织 workspace 内创建、共享、治理的 Agent，把 SOP 固化为**可重复 playbook**；验收以 **RBAC、触发器（API/定时/Slack）与 org 级审计** 为主。本页为 **Workspace Agent 产品 SSOT**（完整 URL 表仅此一处）；IM 频道协作面 → [ai-employee.md](ai-employee.md)；个人委派·交付物 → [work-agent.md](work-agent.md)；确定性自动化 → [workflow.md](workflow.md)；多 Agent 编排框架 → [multi-agent.md](multi-agent.md)。

**材料范围**：公开网络检索（OpenAI Workspace Agents、Notion Custom Agents、Copilot Studio / Gemini Enterprise Agent Platform 产品文档摘要）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-09-02**。簇边界见 [`skills/knowledge-block/references/work-agent-cluster.md`](../../skills/knowledge-block/references/work-agent-cluster.md)。

**站内对照**：**待**上线 · slug **`workspace-agent`** · 发文优先 **`/blog/workspace-agent`**

**Tools 关键词与 slug 映射**：`keywordEn`: **Workspace Agent / Team AI Agent** · `keywordZh`: **工作区智能体 / 团队 Agent 工作流** · 锚点 **`#workspace-agent-tools`**（待写入 keywords 表）

**站内相邻**：[ai-employee.md](ai-employee.md) · [work-agent.md](work-agent.md) · [workflow.md](workflow.md) · [multi-agent.md](multi-agent.md) · [agent-skills.md](agent-skills.md)

---

## 与相邻 slug 分流

| 维度 | **`workspace-agent`（本页）** | **`ai-employee`** | **`work-agent`** | **`workflow`** | **`multi-agent`** |
|------|------------------------------|-------------------|------------------|----------------|-------------------|
| **典型买家问题** | 「把这套销售/支持流程做成全组共用的 Agent」 | 「在 Slack 里 @ 一个共享同事干活」 | 「帮我做完这一份 deck/报告」 | 「当表单提交时写入 CRM 并发 Slack」 | 「多个 Agent 怎么 handoff、谁监督谁」 |
| **优化单位** | 团队 + **重复 playbook** | **IM 协作界面** | 个人 + **单次交付** | **IF/THEN 节点图** | **Agent 拓扑** |
| **触发** | 定时、事件、**API**、Slack | 频道 **@mention** | 用户当场发起 Work/Cowork | Webhook、Cron | 框架级 handoff |
| **代表产品** | OpenAI Workspace Agents、Notion Custom Agents | Claude Tag、Viktor | ChatGPT Work、Claude Cowork | Zapier、n8n | LangGraph、Raft |

**术语消歧**：OpenAI **Workspace Agents**（产品名）≠ [multi-agent.md](multi-agent.md) 中的 **Multi-Agent Workspace**（Multica/Moxt/Clawith）——前者是 ChatGPT 企业内共享 Agent，后者是独立 Agent 工作空间产品。**Claude Tag** = IM 员工（[ai-employee.md](ai-employee.md)），非 workspace playbook 主叙事；OpenAI Workspace Agents **部署进 Slack** 时 playbook 在本页、频道体验互链 ai-employee。

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Workspace Agent / 工作区智能体**：在**组织 workspace** 内创建、共享、治理的 AI Agent——把团队 SOP、最佳实践与连接器权限固化为**可重复运行**的自动化实体；OpenAI 定义为 GPTs 的演进，由 Codex 驱动，可 Slack/API 触发。
- **Build once, scale across team**：一人（或小组）维护 agent 定义，全 workspace 按同一流程执行——与每次重写 prompt 的 Work 会话相对。
- **Trigger / Schedule / API**：Workspace Agent 的典型启动方式；Work Agent 以**人工当场委派**为主（见 [work-agent.md](work-agent.md)）。
- **Playbook / 流程资产**：instructions、工具白名单、审批检查点、输出模板——组织知识的产品化容器。
- **Human-in-the-loop at org level**：发送消息、改记录、对外写入前审批——admin 可配置检查点与可见性。
- **Notion Custom Agents**：Notion 3.3（2026-02-24）发布的**团队 24/7 后台 Agent**，与 on-demand **Notion Agent**（个人、~20 分钟）分列——后者见 [work-agent.md](work-agent.md)。

---

## 专题对照 / 扩展定义

**Workspace vs Work vs Workflow vs Multi-Agent**（术语见 §词汇锚点；产品规格见 §外链索引）：

| 维度 | **Workspace Agent** | **Work Agent** | **Workflow (Zapier/n8n)** | **Multi-Agent 框架** |
|------|---------------------|----------------|---------------------------|----------------------|
| **推理** | LLM 规划 + 工具调用 | 同左 | mostly 固定节点；AI 节点可选 | 多 Agent 可推理 |
| **维护者** | 业务 owner + admin | 个人用户 | 集成工程师 | 平台/开发团队 |
| **确定性** | 中（模型 + 流程约束） | 中 | 高（规则驱动） | 低–中 |
| **最佳场景** | 重复 knowledge work + 需 LLM 判断 | 一次性重交付物 | 稳定 API 胶水 | 复杂分工与 handoff |

---

## 问题域（为何会出现这类产品）

- **个人 Work 模式无法规模化**：销售、支持、Ops 需要**同一套**线索分级、周报、工单路由——每人每次 prompt 不可审计、不可迭代。
- **GPTs 不够「企业」**：缺少 org RBAC、API 触发、Slack 内共享、审计日志——Workspace Agents 补这一层（OpenAI 2026 GA）。
- **Notion/Slack 原生**：知识已在 workspace；Custom Agents 让自动化**不离开**协作面（Notion 2026-02）。
- **与 iPaaS 合流**：Workato/Boomi/Zapier 加 agent builder——但 workspace agent 强调 **LLM-native playbook + 协作入口**；与 [workflow.md](workflow.md) 的 API 图边界见 §专题对照。

---

## 能力栈（概念拆分）

- **Agent 定义**：模型、reasoning effort、system instructions、示例。
- **工具与连接器**：CRM、邮件、文档、Slack——继承 org 已启用 connector 白名单。
- **触发器**：Cron、业务事件、Incoming webhook/API（OpenAI cookbook：Workspace Agents API trigger）。
- **协作编辑**：多成员可维护同一 agent（OpenAI Help：workspace 内 co-edit）。
- **发布与版本**：测试 → 发布 → workspace 或 group 可见。
- **观测**：运行日志、Credits 消耗（Notion Credits、Copilot Credits 等——以各平台为准）。
- **与 Codex 关系**：OpenAI Workspace Agents **由 Codex 驱动**——执行层与 [coding.md](../coding/coding.md) 相邻，但买家是**业务工作流**而非仓库。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | ChatGPT Enterprise 内共享 agent；Slack/API trigger | Workspace Agents | OpenAI Workspace Agents |
| **B** | 协作面内触发；handoff 到其他 Custom Agents | Custom Agents / team agent | Notion Custom Agents |
| **C** | 低代码/平台层构建组织 agent 目录 | Copilot Studio / Agent Platform | Microsoft Copilot Studio、Gemini Enterprise |
| **D** | 企业 IM 栈内嵌 agent 分发 | Team admin / managed agents | WorkBuddy Team、钉钉/飞书企业入口 |

**Type A vs D**：A 为 **ChatGPT 租户内**；D 为 **中国 IM/套件上下文**——个人桌面委派仍归 [work-agent.md](work-agent.md)。

---

## 风险 · 合规 · 治理

- **错误 playbook 全组放大**：一次 bad instruction → 全员错误输出；需 staging、审批、抽样审计。
- **过度自主写入**：发错邮件、改错记录——强制 approval gate。
- **Credits 失控**：Custom Agents / Copilot 用量需 admin dashboard 与 cap。
- **权限继承**：Agent 只能访问创建者/组被授权的 connector；最小权限原则。
- **与 HR/合规**：客户 PII、财务数据流经 agent 时的 DPA 与日志保留。

---

## 落地碎片

- **何时从 Work 毕业到 Workspace Agent**：同一 prompt 第三周仍在复制粘贴；或需要 API/Slack 无人值守触发。
- **先窄后宽**：一个 workflow（如 inbound lead 简报）跑稳再扩工具权限。
- **与 workflow 分工**：API 步骤固定、无 LLM 判断 → Zapier/n8n；需读邮件语义、起草多变回复 → workspace agent。
- **与 multi-agent 分工**：要 **LangGraph 自定义拓扑** → 框架；要 **业务用户在 ChatGPT 里点选发布** → 本页产品。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **OpenAI Workspace Agents** | A | GPTs 演进；Codex 驱动；Schedule/API/Slack 触发；Business/Edu admin | [openai.com/index/introducing-workspace-agents-in-chatgpt](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) · [Help](https://help.openai.com/en/articles/20001143/) · [API trigger cookbook](https://developers.openai.com/cookbook/examples/chatgpt/workspace_agents/workspace-agents-api-trigger) |
| **Notion Custom Agents** | B | Notion 3.3 团队 24/7 后台 Agent；Credits 计费 | [notion.com/releases/2026-02-24](https://www.notion.com/releases/2026-02-24) · [Help](https://www.notion.com/help/custom-agents) |
| **Copilot Studio agents** | C | M365 多渠道；DLP 合规 | [microsoft.com/microsoft-copilot/microsoft-copilot-studio](https://www.microsoft.com/en-us/microsoft/copilot/microsoft-copilot-studio) |
| **Gemini Enterprise Agent Platform** | C | Agent Registry、Gateway | [cloud.google.com](https://cloud.google.com/) |
| **WorkBuddy Team / Managed Agents** | D | 腾讯企业向托管 agent 分发 | 见 [work-agent.md](work-agent.md) §WorkBuddy |

### 对比与测评（第三方；观点非官方）

- **Playbook 持久化 vs 单次 Chat**：OpenAI Workspace Agents / Notion Custom Agents 强调可调度、可 API 触发——与 ai-employee 单次 @ 不同轴。
- **与 workflow 分工**：固定 API 无 LLM → [workflow.md](workflow.md)；需读上下文起草 → 本页 Type 产品。

*观点非官方。*

---

## 延伸阅读 · 站内外

**站内**

- IM 协作面：[ai-employee.md](ai-employee.md)
- Hub（交付物）：[work-agent.md](work-agent.md)
- 簇边界（skills）：[`skills/knowledge-block/references/work-agent-cluster.md`](../../skills/knowledge-block/references/work-agent-cluster.md) · [`ai-employee-cluster.md`](../../skills/knowledge-block/references/ai-employee-cluster.md)
- 确定性管道：[workflow.md](workflow.md)
- 编排框架：[multi-agent.md](multi-agent.md)