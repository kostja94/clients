# AI Workflow · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Workflow automation / 工作流自动化**——通过预设规则在多个应用或服务之间自动传递数据、触发动作；验收以**连接器广度、逻辑路由复杂度、确定性 vs agentic 节点边界**为主。本页为 **Workflow / iPaaS 产品 SSOT**（完整 URL 表仅此一处）；Agent 技能 → [agent-skills.md](agent-skills.md)；多 Agent 编排 → [multi-agent.md](multi-agent.md)；Work Agent → [work-agent.md](work-agent.md)。

**材料范围**：公开网络检索（厂商官方文档与产品页、Gartner/Forrester 分析师报告摘要、社区讨论与评测、Wikipedia 条目）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-05-10**。

**站内对照**：[alignify.co/tools/workflow](https://alignify.co/tools/workflow) · slug **`workflow`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#workflow-tools`](../../keywords/alignify-keywords-tools.md#workflow-tools)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Workflow automation / 工作流自动化**：通过预设规则在多个应用或服务之间自动传递数据、触发动作的系统。与「一次性脚本」的差异在于**可复用性**和**非开发者可维护性**。
- **iPaaS（Integration Platform as a Service）**：Gartner 2011 年正式定义的品类。提供云端集成能力（连接器、数据映射、流程编排）的平台。与 workflow automation 的边界在 2025–2026 年快速模糊。
- **Trigger → Action（触发器 → 动作）**：工作流的基本原子单元。Zapier 将这对关系品牌化为 "Zap"，Make 称为 "Scenario"，n8n 称 "Workflow"。
- **Node-based（节点式编辑器）**：在画布上拖放模块并以连线定义数据流。Make、n8n、Gumloop、Opal 均采用此形态。
- **No-code / Low-code automation**：No-code 强调业务用户无需写代码；Low-code 保留代码注入能力（n8n 的 Code 节点）。2025–2026 年 AI 辅助正在模糊二者边界。
- **Agentic workflow / 智能体工作流**：在链路中嵌入 LLM/AI agent 节点，由 agent 自主决定下一步路由、选择工具、动态生成输出内容。
- **RPA（Robotic Process Automation）**：通过模拟人类在 GUI 上的鼠标点击和键盘输入来自动化遗留系统。与 workflow 的核心差异：RPA 操作**界面层**，workflow 操作**API 层**。
- **Self-hosted / Fair-code**：工作流引擎可在自有基础设施上部署（n8n 为代表）。Fair-code 允许自托管免费使用，但对商业再分发设限。
- **API integration vs Native connector**：API integration 通过 HTTP 请求节点调用任何 REST/GraphQL 接口；Native connector 是厂商预封装的连接器。

---

## 专题对照 / 扩展定义

**Workflow vs iPaaS vs RPA vs Agentic AI**（术语见 §词汇锚点；形态 Type 见 §形态谱系）：

| 维度 | **Workflow Automation** | **iPaaS** | **RPA** | **Agentic AI** |
|------|-------------------------|-----------|---------|----------------|
| **操作层** | API 层（结构化 JSON） | API 层 + 数据管道 | GUI 层（像素、点击） | API 层 + 自然语言推理 |
| **典型买家** | 运营、市场、中小企业 | IT 集成团队、大型企业 | 财务、HR、遗留系统迁移 | 工程团队、AI-native 初创 |
| **确定性** | 高（规则驱动） | 高（规则 + 数据契约） | 低到中（UI 变化易断） | 低（LLM 非确定性输出） |
| **代表产品** | Zapier、Make、n8n | Boomi、Workato、MuleSoft | UiPath、Automation Anywhere | Opal Agent Step、CrewAI |

*边界融合趋势（2025–2026）*：Gartner 2025 Magic Quadrant 中 iPaaS 领导者均内建 AI agent builder；Zapier 推出 Central 和 Agents；n8n 集成 LangChain。四列边界正在塌缩为**统一的 AI 编排层**。

---

## 与相邻 slug 分流（品类易混时阅读）

| slug | 典型买家问题 | 与本 slug 的边界 |
|------|-------------|------------------|
| **`workflow`（本页）** | 「A 应用的数据自动同步到 B，并在 C 发通知」 | — |
| **`vibe-coding`** | 「用自然语言生成可运行的 Web 应用」 | 产出**应用** vs **跨应用管道** |
| **`agent-skills`** | 「Agent 如何学会执行特定任务」 | **技能包** vs **执行管道** |
| **`agent-for-desktop`** | 「AI 能否操控桌面应用和本地文件」 | **本地 GUI** vs **云端 API** |
| **`multi-agent`** | 「多个 Agent 如何分工、handoff」 | **确定性 SaaS 管道** vs **可推理 Agent 拓扑** |
| **`workspace-agent`** | 「把团队 SOP 做成共享 Agent」 | **固定 API 图** vs **LLM playbook + org 治理** |
| **`work-agent`** | 「帮我做完这一份 deck/报告」 | **不**以「交稿」为默认成功标准 |
| **`ai-employee`** | 「在 Slack 里 @ 一个共享同事干活」 | **IM 协作面** vs **跨 SaaS API 管道** |
| **`backend-as-a-service`** | 「App 的库/鉴权/实时托管在哪？」 | **应用态 BaaS** vs **跨应用自动化管道** |
| **`browser`** | 「AI 能否帮我浏览网页、填表」 | **人向浏览体验** vs **自动化后台管线** |

---

## 问题域（为何会出现这类产品）

- **SaaS 碎片化**：平均每个企业使用 130–2000+ 个 SaaS 应用，数据孤岛使跨系统操作成为运营常态。
- **API 经济成熟**：RESTful API 的标准化使「连接任意两个服务」从定制开发变为配置化操作。
- **公民开发者运动**：Gartner 预测到 2026 年超过 80% 的新数字化项目将使用低代码/无代码平台。
- **人力成本与错误率**：Workflow 把重复性操作标准化并消除人为失误。
- **AI agent 的落地管道**：LLM 能力成熟后，Workflow 平台从「连接 SaaS」升级为「AI agent 的执行层」。
- **合规与审计**：Workflow 平台提供执行历史、步骤级日志、错误通知——满足 SOC2、GDPR 等合规要求。

---

## 能力栈（概念拆分，非厂商功能表）

- **集成广度**：预置连接器数量与质量——Zapier 8000+ vs n8n 通用 HTTP 节点。
- **逻辑与路由**：从简单线性到多分支、条件路由、循环、子流程、并行执行、错误重试策略。
- **数据转换**：字段映射、类型转换、JSON 解析——从「配置级」到「代码级」的转换能力梯度。
- **错误处理与可观测性**：步骤级重试、错误路由、执行日志与可视化。
- **AI 增强**：自然语言生成工作流、AI 节点、agentic 决策——2026 年此维度从「加分项」变为「入场券」。
- **部署模型**：纯 SaaS vs 自托管 vs 混合（本地执行器 + 云端控制面）。
- **协作与治理**：团队工作空间、角色权限、工作流版本管理、环境隔离（dev/staging/prod）。
- **触发机制**：Polling vs Webhook vs Manual。
- **定价模型**：按任务/步骤数（Zapier）vs 按 operation（Make）vs 按 execution（n8n）——直接影响选型成本。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 企业 iPaaS；重集成、事务、治理 | Enterprise iPaaS | Boomi、Workato、MuleSoft、Tray.ai、Celigo |
| **B** | 轻量、即用、线性为主；最大集成生态 | SMB workflow / Zap | Zapier、IFTTT |
| **C** | 画布式拖放 + 实时执行视图 | Visual orchestration | Make |
| **D** | 开源 fair-code；自托管免费；全代码注入 | Self-hosted workflow | n8n、Temporal、Prefect、Airflow |
| **E** | 从 LLM agent 编排出发；自然语言生成工作流 | AI-native workflow | Gumloop、Stepper、Dify |
| **F** | 大厂实验；依托大模型 + 自家生态 | Labs / experimental | Opal（Google） |
| **G** | 垂直创意/行业工作流 | Vertical workflow | Weavy（Figma Weave） |
| **H** | GUI 层自动化；与 API 工作流互补 | RPA | UiPath、Automation Anywhere、Power Automate |
| **I** | 面向开发者；无预置连接器；需自行接 API | Agent orchestration framework | CrewAI、AutoGen、LangGraph |

**Type B vs C vs D**（社区最频繁三方比较）：B 入门最快但复杂场景成本飙升；C 编辑体验与调试可视化最佳；D 自托管在 10 步以上、月执行 5000+ 次场景成本优势可达 5–10×。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **数据隐私与 PII 泄漏**：工作流本质是将数据在不同 SaaS 之间搬运；需核对各连接器 DPA 与数据驻留区域。
- **API 凭证管理**：最小权限原则、定期轮换凭证、审计实际 API 调用范围。
- **供应商锁定**：工作流配置通常不可跨平台导出；迁移 500 条 Zap 几乎是重做。
- **AI 幻觉在自动化链路中的传导**：agentic workflow 中 LLM 节点输出非确定性——需输出校验规则、human-in-the-loop、异常阈值告警。
- **合规可审计性**：金融、医疗、法律等受监管行业要求步骤级执行日志。
- **定价失控风险**：按任务/步骤计费在复杂场景下月费可从数十美元飙升至数千。
- **Agent 自主权边界**：Forrester 预计超过 40% 的 agentic AI 项目将在 2027 年前因治理缺失被取消。

---

## 落地碎片（无先后）

- 先用简单场景验证平台适配性：连接 2–3 个日常高频应用，用免费额度跑通完整链路。
- 多步骤复杂工作流，优先用 Make 或 n8n 的可视化节点——分支和错误路由在节点视图中更直观。
- 若有数据驻留或合规需求，优先评估 n8n 自托管方案。
- 涉及 LLM 调用的工作流，在 AI 节点之后加校验步骤——尤其是外发邮件或付款操作前。
- 定价对比时用自己的真实工作流计算：Zapier 按 task、Make 按 operation、n8n 按 execution——10 步工作流每月 1000 次费用可差 5–10 倍。
- 企业选型额外关注：SSO/SCIM、RBAC、连接器审批流、环境隔离。
- 不要把所有自动化押在一个平台上：核心业务关键链路保留可切换备份或手动 SOP。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Zapier** | B | 无代码工作流自动化鼻祖，8000+ 应用连接 | [zapier.com](https://zapier.com/) |
| **Make** | C | 可视化画布式场景编辑器，实时执行视图，2000+ 集成 | [make.com](https://www.make.com/en) |
| **n8n** | D | 开源 fair-code 工作流引擎，自托管免费，400+ 原生节点 + LangChain AI 集成 | [n8n.io](https://n8n.io/) · [n8n AI](https://n8n.io/ai/) |
| **Opal** | F | Google Labs 无代码 AI mini-app 与工作流构建器，自然语言驱动 + agent step | [opal.google](https://opal.google/) |
| **Gumloop** | E | AI-native 工作流自动化平台，侧重 AI agent 编排 | [gumloop.com](https://www.gumloop.com/) |
| **Stepper** | E | AI 工作流自动化平台，面向可复用业务流程 | [stepper.io](https://stepper.io/) |
| **Dify** | E | AI 应用开发与编排平台（LLMOps），可视化构建 RAG/Chatbot/Agent 管道 | [dify.ai](https://dify.ai/) |
| **Linear（Agent）** | — | 2026-03 推出 Linear Agent 实现 issue 自动处理——属项目管理而非通用工作流 | [linear.app/ai](https://linear.app/ai) |
| **Weavy（Figma Weave）** | G | 垂直创意工作流平台，节点式连接 AI 图像/视频模型（2025-10 被 Figma 收购） | [weavy.ai](https://www.weavy.ai/) |
| **Workato** | A | Gartner Leader 级企业 iPaaS，连续 7 年 Leader | [workato.com](https://www.workato.com/) |
| **Boomi** | A | iPaaS 品类开创者，Gartner Leader 连续 11 年，2025–2026 推 Agentstudio | [boomi.com](https://boomi.com/) |
| **Tray.ai** | A | AI 编排优先的 iPaaS（2025 Gartner Visionary）；Merlin agent builder | [tray.ai](https://tray.ai/) |
| **Celigo** | A | 2025 年新晋 Gartner Leader；Ora AI copilot | [celigo.com](https://www.celigo.com/) |

### 对比与测评（第三方；观点非官方）

Zapier / Make / n8n 三条产品线构成社区最频繁的三方比较——三角权衡见 §形态谱系 **Type B vs C vs D** 注。

2025–2026 年的核心分歧在 **AI agent 编排**：传统平台（Zapier Central、Make Agents）在现有架构上加 AI 层，而 AI-native 平台（Gumloop、Stepper、Dify）从 LLM 出发向下生长连接器生态。目前 AI-native 在集成广度上远不及传统平台，但在 agent 推理链路的灵活度上有天然优势。

Opal（Google）差异化在 Gemini 模型的原生集成和 Google 生态深度绑定——但其 Labs 实验性质意味着企业级合规、SLA、数据驻留等承诺尚不明确。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- Gartner Magic Quadrant for iPaaS, 2025 — Boomi 连续 11 年 Leader / Workato 连续 7 年 / Celigo 升至 Leader
- Forrester: Predictions 2026 — 超过 40% agentic AI 项目将在 2027 年前因治理缺失被取消
- "The Last Magic Quadrant for iPaaS and the Rise of AI Orchestration" — Tray.ai CEO Rich Waldron（2026-02）
- Google Blog: "Build dynamic agentic workflows in Opal"（2026-02）
- Wikipedia: "Cloud-based integration"（iPaaS 条目）

**站内**

- 多 Agent：[multi-agent.md](multi-agent.md)
- Work Agent：[work-agent.md](work-agent.md)
- AI Employee（IM 协作）：[ai-employee.md](ai-employee.md)
- Agent Skills：[agent-skills.md](agent-skills.md)
- BaaS / App 态：[backend-as-a-service.md](../infrastructure/backend-as-a-service.md)