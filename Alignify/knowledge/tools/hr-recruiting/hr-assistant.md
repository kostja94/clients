# AI HR Assistant · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI HR assistant / AI HR 助手**——面向员工**入职后**的 AI 助手，用于回答政策问题、处理 HR 工单、引导自助服务；验收以**自助率、工单偏转、答案合规准确**为主。本页为 **HR 助手 SSOT**（完整 URL 表仅此一处）；录用前招聘 → [recruiting.md](recruiting.md)；通用 chatbot → 非本页。

**材料范围**：公开网络检索（厂商产品页与官方文档、HR.com / HR Lineup 品类分析、Wisq / Leena AI 等厂商博客、企业软件评测站点、法律媒体合规分析）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/hr-assistant](https://alignify.co/tools/hr-assistant) · [alignify.co/zh/tools/hr-assistant](https://alignify.co/zh/tools/hr-assistant) · slug **`hr-assistant`** · `content/tools/en|zh/hr-assistant.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#hr-assistant-tools`](../../product/alignify-keywords-tools.md#hr-assistant-tools))

## 与相邻 slug 分流（品类易混时必读）

| slug / 品类 | 典型买家问题 | 与本 slug 的边界 |
|------|-------------|------------------|
| **`hr-assistant`（本页）** | 「员工反复问 HR 政策，怎么用 AI 自动回答？怎么把 HR 工单从 500 降到 100？」 | — |
| **`recruiting`** | 「我用什么工具找到对的人？」 | recruiting 是**录用前**；hr-assistant 是**录用后**。分界线是入职日 |
| **通用 AI chatbot** | 「我要一个能聊天的 AI」 | 通用 chatbot 没有 HR 领域知识——不知道 FMLA 和 ADA 的交互 |
| **HRIS / HCM** | 「我要一套管员工档案、薪酬、绩效的系统」 | HRIS 是**记录系统**；hr-assistant 是**服务层** |
| **IT service desk AI** | 「我电脑连不上 VPN」 | IT 与 HR 知识域不同，但 Moveworks、Aisera 等跨界玩家同时做 IT + HR |

**recruiting vs HR Ops 边界**：Wisq（Harper AI HR Generalist，$55M 总融资）是 **AI HR 运营平台**，不是招聘工具——它解决员工**入职后**的问题。recruiting 覆盖**录用前的漏斗**；HR Ops 覆盖**录用后的生命周期**。Wisq 应属于 hr-assistant 品类而非 recruiting（详见 [recruiting.md](recruiting.md) §recruiting vs HR Ops）。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI HR assistant / AI HR 助手（本知识块的主标签）**：以 AI 技术自动化 HR 服务交付（HR Service Delivery, HRSD）的软件工具品类。核心能力包括：自然语言理解员工 HR 问题、查找并解释公司政策、引导自助服务流程、在授权范围内执行系统操作、对无法自动处理的问题智能路由到人工 HR。与通用 AI chatbot 的关键区别：**领域知识库**（公司政策 + 劳动法规 + 系统数据）和**合规护栏**。
- **HR Service Delivery (HRSD) / HR 服务交付**：Gartner 定义的 HR 职能域——通过何种渠道向员工提供 HR 服务。传统 HRSD 依赖 HR 共享服务中心 + Tier 0-3 工单路由；AI HRSD 将 Tier 0 和 Tier 1 的 40-80% 自动化。
- **Employee self-service (ESS) / 员工自助服务**：员工不通过 HR 中介、直接在系统内完成 HR 相关操作。AI 将 ESS 从「自己翻门户网站找表单」升级为「用自然语言说需求，AI 帮你找到答案或执行操作」。关键指标：自助率——Leena AI 合同承诺 70%，Wisq 实际运行达 80%。
- **Proprietary HR LLM / 自研 HR 大模型**：用 HR 领域专有数据预训练或深度微调。Wisq 的 HRLM 和 Leena AI 的 WorkLM 是代表——HRLM 在 SHRM-CP 考试上达 94%，据称推理成本为通用模型 1/60。
- **Agentic AI in HR / HR 智能体**：2026 年最新范式——AI 能在多个 HR 系统中**执行操作**（如发起 PTO 申请、更新个人信息），而非只检索和生成文本。
- **Knowledge orchestration / 知识编排**：AI HR assistant 将分散在多个系统中的政策、流程、FAQ、合规文档统一索引并交叉引用的能力。
- **Ticket deflection / 工单偏转**：通过 AI 自主解决员工问题，避免生成人工 HR 工单——Leena AI 实现 40-60% 偏转率；Wisq 实现约 40% 全自主解决 + 额外 40% AI 辅助人工。
- **Multi-system integration depth / 多系统集成深度**：浅（只读知识库）→ 中（只读 HRIS API）→ 深（双向读写，可发起申请、更新记录、触发工作流）。Leena AI 的 1,000+ 集成连接器是行业最多。

---

## 专题对照 / 扩展定义

**HCM 内嵌 vs 独立平台** 与 **纯问答 vs 执行型 Agent** 是本品类两大核心二分——术语见 §词汇锚点；下表只列**架构哲学与能力层级**。

### HCM 内嵌 vs 独立平台

| 维度 | **HCM 内嵌型** | **独立跨平台型** |
|------|--------------|----------------|
| **代表** | Workday Sana, SAP Joule, ADP Assist | Wisq (Harper), Leena AI, Aisera, Moveworks |
| **核心优势** | 与自己 HCM 的数据模型、权限、工作流零摩擦集成 | 可跨多个 HR 系统编排 |
| **核心局限** | 离开自有 HCM 生态后能力骤降 | 需要大量集成工作 |
| **AI 成熟度** | 通常落后 AI-native 厂商 1-2 代 | 通常领先 |

### 纯问答 vs 执行型 Agent（能力层级）

| 层级 | 能力描述 | 代表产品 |
|------|---------|---------|
| Level 1：FAQ 检索 | 从知识库中找到匹配的政策文档段落 | BambooHR "Ask BambooHR" |
| Level 2：个性化问答 | 检索 + 理解员工个人数据给出个性化答案 | Leena AI, ADP Assist |
| Level 3：引导式自助 | 问答 + 引导员工完成多步自助流程（但不执行系统写入） | ServiceNow HRSD + Now Assist |
| Level 4：执行型 Agent | 理解意图 → 自主执行跨系统操作 → 确认完成 | Wisq (Harper), Moveworks |

2026 年的竞争焦点是 Level 3 → Level 4 的跨越。形态路线 → **§形态谱系**；产品规格 → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **HR 服务台的「重复性问题」困境**：HR 服务台收到的工单中 40-60% 是重复性政策问答——「我有多少天 PTO？」「产假怎么申请？」。AI 将这些工单的自主解决率推到 40-80%。
- **员工期望已从「门户自助」升级为「对话即服务」**：员工习惯了 ChatGPT 式的自然语言即时回答。
- **合规风险的「长尾」问题**：HR 政策与联邦/州/地方法规的交叉越来越复杂——AI 在「复杂政策交叉引用」场景上的一致性优于疲劳或经验不足的 HR Generalist。
- **跨系统数据碎片化**：中大型企业通常有 5-15 个 HR 相关系统——员工的一个简单问题需要跨 3 个系统查询。
- **AI 预算正在从实验走向规模部署**：ISG 2025 调查显示企业 HR 的 AI 预算均值已达 $1.6M（2026 年），较 2023 年增长 10 倍。
- **「AI HR 通才」vs「水平 AI 助手」的落差**：Microsoft 365 Copilot 和 Google Gemini 回答不了「我在新泽西远程工作的 FMLA 资格是什么」——这为专用 AI HR assistant 创造了需求空间。

---

## 能力栈（概念拆分，非厂商功能表）

- **HR 领域知识深度**：通用 LLM 基础 HR 知识 → 公司政策 RAG → 劳动法规结构化理解 → 专有 HR 推理模型（HRLM, WorkLM）。2026 年分水岭是第三→第四层。
- **个性化上下文拼接**：无上下文 → 基于员工角色/部门 → 基于员工实时数据（PTO 余额、工作地点）→ 跨系统上下文。
- **系统集成读写能力**：只读知识库 → 只读 HRIS API → 受限写入 → 全自主写入。风险随写入能力指数增长。
- **合规护栏强度**：无护栏 → 提示词约束 → 检索约束 → 策略引擎（规则引擎 + AI 推理的双层架构）。
- **多语言与多法规辖区支持**：单语言/单国家 → 多语言 → 多法规 → 动态法规更新。
- **渠道覆盖**：Web 门户 widget → Slack/Teams bot → 邮件 → SMS/WhatsApp → 语音电话。
- **可解释性与审计准备**：黑盒 → 引用来源 → 决策追溯 → 合规报告导出。EU AI Act（2026.08）和 NYC Law 144 的衍生压力将第三层变为企业采购的最低门槛。
- **人工升级与协作**：纯 AI 自主 → AI 回答 + 不满意可转人工 → AI 先回答 + 人工审核后再发出 → 智能路由。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | HCM 内嵌 AI 助手：在自己 HCM 生态内提供问答和有限执行 | HCM-embedded AI copilot | Workday Sana, SAP Joule, ADP Assist, Oracle HCM AI |
| **B** | 独立 AI HR 通才：自研 HR LLM 或广泛集成 | AI HR assistant / HR generalist | Wisq (Harper), Leena AI |
| **C** | 跨职能企业助手：IT+HR+Finance 统一 | Cross-functional enterprise assistant | Moveworks, Aisera, IBM watsonx Orchestrate |
| **D** | HR 服务台 AI 增强：在已有服务台上叠加 AI 层 | HR service desk AI (HRSD AI) | ServiceNow HRSD (Now Assist), Salesforce HR Agentforce |
| **E** | Teams/Slack 原生轻量 HR Bot | Teams/Slack HR bot | Rezolve.ai |
| **F** | 水平 AI 助手的 HR 用例（非专用产品） | Horizontal AI assistant | Microsoft 365 Copilot, Google Gemini, ChatGPT Enterprise |

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **合规建议的法律效力风险**：AI HR assistant 给出的政策解释如果被员工视为「公司官方立场」，而答案有误，公司可能面临劳动法诉讼。
- **数据隐私与跨系统访问权限**：AI assistant 需要读取 PTO 余额、薪酬等级、健康保险选择等敏感数据——GDPR 和 CCPA 要求数据最小化和目的限制。
- **EU AI Act 高风险分类**：HR 用途（招聘、绩效评估、晋升决策）被 EU AI Act 明确列为「高风险」。2026 年 8 月 2 日完全执行。若 AI 开始辅助绩效预校准（Wisq 的 Harper 有此功能），就可能进入高风险范围。
- **代理变量偏差放大**：即使 AI HR assistant 不直接做招聘决策，它在回答「谁符合晋升条件」等问题时，答案可能隐含对某些受保护群体的系统性不利。
- **工单偏转过度的员工体验风险**：将 HR 工单偏转率推到 80% 可能让一些员工问题**需要**与真人对话（丧假、职场冲突、心理健康资源）。
- **模型更新与政策同步的时效性**：劳动法规变动后，AI assistant 的答案需要在生效日当天更新。
- **卖方锁定与切换成本**：HCM 内嵌型（Type A）的锁定风险最高；独立平台型（Type B）至少在 AI 层保留了切换可能。

---

## 落地碎片（实践建议）

- 选型前先量化你的工单结构：拉最近 6 个月的 HR 服务台工单数据——如果政策问答 + 流程引导不到 40%，AI assistant 的 ROI 很难达标。
- **从「一个高频率、低风险」用例开始试点**：PTO 政策问答是最安全的切入点。
- **准备「政策文档卫生」工作**：AI 部署前先做一轮政策文档审计和统一是 ROI 最高的准备工作。
- **不要把 HR 团队的 adoption 视为理所当然**：让 HR 从「工单处理者」转型为「AI 训练师 + 例外场景专家 + 员工体验设计师」。
- **中国市场优先看 AI 与现有钉钉/飞书/企业微信生态的整合**：Wisq 和 Leena AI 主要覆盖欧美市场。国内 HR 服务台 AI 在钉钉、飞书、企业微信上的集成深度比产品功能本身更关键——北森和 Moka 的 HR 助手模块是在中国市场的接近选择。
- **构建「AI 信心」而非「AI 依赖」**：在 AI 答案旁边显示置信度、引用来源、以及「如有疑问请联系 HR」的快捷方式。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| Wisq (Harper) | B | 自研 HRLM 垂直模型；SHRM-CP 94% 正确率，80% 自主解决率，Fast Company 2026 HR #2；$55M 融资 | https://www.wisq.com/ |
| Leena AI | B | 企业级虚拟助手，自研 WorkLM；500+ 客户，1000+ 集成，合同承诺 70% 自助率；年费 ~$300K/千用户起 | https://leena.ai/ |
| ServiceNow HRSD + Now Assist | D | HR 服务交付 + AI 增强；与 ITSM 天然互通 | https://www.servicenow.com/products/hr-service-delivery.html |
| Moveworks | C | 跨职能企业助手（IT+HR+Finance）；2024 年被 ServiceNow 收购 | https://www.moveworks.com/ |
| Aisera | C | 自研 LLM 的智能体 AI；覆盖 HR/IT/CS | https://aisera.com/ |
| IBM watsonx Orchestrate | C | 多智能体 HR 工作流编排；80+ 企业应用连接器 | https://www.ibm.com/products/watsonx-orchestrate |
| Workday Sana | A | Workday HCM 原生 AI 助手；Skills Cloud 驱动个性化 | https://www.workday.com/ |
| SAP Joule | A | SAP SuccessFactors 内嵌 AI 助手 | https://www.sap.com/products/artificial-intelligence/ai-assistant.html |
| ADP Assist | A | ADP 薪酬/HR 平台内嵌 AI | https://www.adp.com/ |
| Rezolve.ai | E | Microsoft Teams 原生员工服务台 AI；轻量部署 | https://www.rezolve.ai/ |
| Gloat + Loomra | B | 自研 Knowledge Graph 的 AI Agent 平台；29 个 Agent | https://gloat.com/ |
| Microsoft 365 Copilot | F | 水平 AI 助手；非专业 HR 工具但正在抢占轻量场景 | https://www.microsoft.com/en-us/microsoft-365/copilot |
| BambooHR "Ask BambooHR" | A | SMB HRIS 内嵌 AI 问答；功能较基础（Level 1 FAQ） | https://www.bamboohr.com/ |
| HiBob AI | A | 中端市场 HRIS + AI 助手；DecisionIQ 合规护栏 | https://www.hibob.com/ |
| Personio AI | A | 欧洲 SMB HR 平台内嵌 AI 助手；GDPR 原生 | https://www.personio.com/ |
| Rippling | A | 统一 HR+IT+Finance 平台；AI 驱动的绩效评估 + 自动化入职/离职 | https://www.rippling.com/ |
| Lattice AI Agent | D | 持续绩效管理平台 + AI Agent + Knowledge Vault 政策问答 | https://lattice.com/ |

### 对比与测评（第三方；观点非官方）

- Wisq "20 Best AI HR Software in 2026" ——按 HR 问题类型分类推荐 20+ 产品（注意利益冲突）
- HR Lineup "Top 5 AI Chatbots for Employee Self-Service HR 2026" ——聚焦员工自助服务场景的 5 款 chatbot 横向对比
- Gloat Agentic HR Academy "The vendor landscape: Joule, Illuminate, Copilot, and beyond" ——六维度评估框架，最系统的企业选型指南
- ISG "Enterprises Shift to AI and SaaS to Drive Strategic HR Services"（2025.11）——AI 预算均值 $1.6M（2026），10 倍于 2023 年

*网摘综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- **市场数据**：TBRC "Generative AI in Human Resources (HR) Market Report 2026"（GenAI in HR: $0.75B→$0.88B, 18.1% CAGR）；TBRC "Artificial Intelligence in HR Global Market Report 2026"（$6.99B→$8.3B, 18.7% CAGR）
- **品类分析**：Gloat "Agentic HR Academy"——六维度评估框架；Wisq "20 Best AI HR Software in 2026"
- **合规框架**：EU AI Act 正式文本（OJEU，2024.07.12）——2026.08.02 完全执行
- **行业趋势**：SHRM 2025 Talent Trends——43% 企业在 HR 中使用 AI；Forbes "How AI Is Reshaping The Human Resources Profession"（2026.04）