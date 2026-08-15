# AI HR Assistant · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页与官方文档、[Product Hunt](https://www.producthunt.com/search?q=HR+assistant+AI) / G2 条目、HR.com / HR Lineup 品类分析、Wisq / Leena AI / Gloat 等厂商博客、企业软件评测站点、法律媒体合规分析）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。**主轴词**：**AI HR assistant** / **AI HR chatbot** / **AI employee self-service** / **AI HR agent**；中文语境常称 **AI HR 助手** / **AI 员工自助服务** / **智能 HR 问答**，与 **recruiting**（雇主侧招聘工具）、**chatbot**（通用对话 AI）、**productivity**（通用效率工具）在用户角色与场景上根本不同。

**站内对照**：[alignify.co/tools/hr-assistant](https://alignify.co/tools/hr-assistant) · [alignify.co/zh/tools/hr-assistant](https://alignify.co/zh/tools/hr-assistant) · slug **`hr-assistant`** · `content/tools/en|zh/hr-assistant.json`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#hr-assistant-tools`](../../product/alignify-keywords-tools.md#hr-assistant-tools)）

**关联关键词（跨品类检索术语，本知识块需覆盖但非专属）**：

| 角色 | 英文关键词 / 短语 | 中文关键词 / 短语 |
|------|-------------------|-------------------|
| 核心品类 | AI HR assistant, AI HR chatbot, AI employee assistant, HR virtual assistant, employee self-service AI, AI HR agent | AI HR 助手、AI 员工自助、智能 HR 问答、AI 人事助手、HR 虚拟助手 |
| 子功能 | HR service delivery AI, HR knowledge management AI, employee policy Q&A, HR ticket automation, AI HR generalist | HR 服务交付 AI、员工政策问答、HR 工单自动化、AI HR 通才 |
| 架构/交付 | HCM-embedded AI, standalone HR copilot, cross-functional enterprise assistant, Teams/Slack bot, proprietary HR LLM | HCM 内嵌 AI、独立 HR 副驾驶、跨职能企业助手、Teams/Slack 机器人、自研 HR 大模型 |
| 竞品检索 | Wisq vs Leena AI, Moveworks alternative, ServiceNow HRSD vs Aisera, Workday Sana vs SAP Joule | Wisq 对比 Leena AI、HR 虚拟助手对比、AI 员工服务台选型 |
| 相邻品类（分流用） | AI recruiting, AI chatbot (general), HRIS/HCM, AI productivity, IT service desk AI | AI 招聘、通用 AI 聊天机器人、HRIS、AI 生产力、IT 服务台 AI |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流（品类易混时必读）

本知识块描述的是**面向员工入职后的 AI 助手**——用于回答政策问题、处理 HR 工单、引导自助服务、辅助绩效与合规场景。它不是招聘工具，不是通用聊天机器人，也不负责算薪或排班。下表厘清与本目录及其他知识块内相关 slug 的边界：

| slug / 品类 | 典型买家问题 | 用户角色 | 与本 slug 的边界 |
|------|-------------|---------|------------------|
| **`hr-assistant`（本页）** | 「员工每天反复问同样的 HR 政策问题，怎么用 AI 自动回答？怎么把 HR 工单从 500 降到 100？怎么让 AI 在 8 秒内给出合规准确的答案？」 | HR 运营 / HRBP / HRIS 经理 / CHRO | — |
| **`recruiting`** | 「我用什么工具找到对的人？」 | TA / 招聘经理 | recruiting 是**录用前**（找人→筛人→发 offer）；hr-assistant 是**录用后**（员工已有工号，有问题找 AI）。分界线是入职日 |
| **通用 AI chatbot** | 「我要一个能聊天的 AI」 | 任何用户 | 通用 chatbot 没有 HR 领域知识——不知道 FMLA 和 ADA 的交互、不知道 PTO 跨年结转规则。hr-assistant 的差异化在于**领域深度**（政策合规、劳动法、多系统数据）而非对话能力 |
| **HRIS / HCM** | 「我要一套管员工档案、薪酬、绩效的系统」 | HR 总监 / IT | HRIS 是**记录系统**（数据在哪）；hr-assistant 是**服务层**（员工怎么获取这些数据/政策）。Workday Sana 和 SAP Joule 就是 HRIS 厂商自己在记录系统上加的服务层——二者正在融合 |
| **IT service desk AI** | 「我电脑连不上 VPN」 | 全体员工 | IT 服务台和 HR 服务台是不同的知识域（网络拓扑 vs 劳动法），但交付形式趋同（Slack/Teams bot + 工单路由）。Moveworks 和 Aisera 是跨界玩家——同时做 IT + HR。选择跨界方案时需评估 HR 领域的实际深度 |

---

## 词汇锚点

- **AI HR assistant / AI HR 助手（本知识块的主标签）**：以 AI 技术自动化 HR 服务交付（HR Service Delivery, HRSD）的软件工具品类。核心能力包括：自然语言理解员工 HR 问题、查找并解释公司政策、引导自助服务流程、在授权范围内执行系统操作（如发起 PTO 申请、更新个人信息）、对无法自动处理的问题智能路由到人工 HR。与通用 AI chatbot 的关键区别：HR assistant 必须有**领域知识库**（公司政策 + 劳动法规 + 系统数据）和**合规护栏**（不能给出违反劳动法的建议）。
- **HR Service Delivery (HRSD) / HR 服务交付**：Gartner 定义的 HR 职能域——通过何种渠道（门户、电话、聊天、工单）向员工提供 HR 服务。传统 HRSD 依赖 HR 共享服务中心（Shared Service Center）+ Tier 0-3 工单路由；AI HRSD 将 Tier 0（自助）和 Tier 1（一线解答）的 40-80% 自动化。市场正从「工单管理系统 + 知识库」向「AI Agent + 对话界面 + 自治执行」演进。
- **Employee self-service (ESS) / 员工自助服务**：员工不通过 HR 中介、直接在系统内完成 HR 相关操作（查政策、改地址、选福利、申 PTO）。AI 将 ESS 从「自己翻门户网站找表单」升级为「用自然语言说需求，AI 帮你找到答案或执行操作」。关键指标：自助率（self-service ratio）——Leena AI 合同承诺 70%，Wisq 实际运行达 80%。
- **Proprietary HR LLM / 自研 HR 大模型**：区别于在通用 LLM（GPT-4/Claude）上做 prompt engineering 的方案，自研 HR LLM 用 HR 领域专有数据（政策文档、法规文本、历史工单、SHRM 知识体系）进行预训练或深度微调。Wisq 的 HRLM 和 Leena AI 的 WorkLM 是这一策略的代表——核心主张是通用 LLM 在 HR 合规场景下的可靠性不足。HRLM 在 SHRM-CP 考试上达 94%，据称推理成本为通用模型 1/60。
- **Agentic AI in HR / HR 智能体**：2026 年最新范式——AI 不再只是「问答机器」，而是能在多个 HR 系统中**执行操作**的自主智能体。例如：员工说「我想请 3 天病假」→ Agent 自动检查病假余额→判断是否符合 FMLA 条件→在 Workday 中发起申请→通知经理审批→在 Slack 中回复员工确认。与 chatbot 的关键区别：Agent 调用 API 写入系统（create, update, route），chatbot 只检索和生成文本（read, summarize, reply）。
- **Knowledge orchestration / 知识编排**：AI HR assistant 将分散在多个系统中的政策、流程、FAQ、合规文档统一索引并交叉引用的能力。例如员工问「我在加州远程工作，产假政策是什么」，AI 需要同时调取：公司总部产假政策 + 加州补充条款 + 远程员工适用性规则 + 当前 PTO 余额。知识编排深度决定了答案的准确性和完整性——不是说「请参考员工手册第 47 页」就算答完了。
- **Ticket deflection / 工单偏转**：通过 AI 自主解决员工问题，避免生成人工 HR 工单。这是 HR 服务台 AI 最核心的 ROI 指标。Leena AI 实现 40-60% 偏转率；Wisq 实现约 40% 全自主解决 + 额外 40% AI 辅助人工。每偏转一个工单节省 HR 约 15-45 分钟处理时间。
- **Multi-system integration depth / 多系统集成深度**：AI HR assistant 对接的 HR 系统数量和质量。关键级别：浅（只读知识库，不能查实时数据）→ 中（只读 HRIS API，可查 PTO 余额/个人信息）→ 深（双向读写，可发起申请、更新记录、触发工作流）。Leena AI 的 1,000+ 集成连接器是行业最多，但数量不等同于深度——需逐系统验证读/写能力和实时性。

---

## 专题对照 / 扩展定义

本笔记用法：厘清 AI HR assistant 品类的两大核心二分——「HCM 内嵌 vs 独立平台」以及「纯问答 vs 执行型 Agent」。

**HCM 内嵌 vs 独立平台**（两种根本不同的架构哲学）：

| 维度 | **HCM 内嵌型** | **独立跨平台型** |
|------|--------------|----------------|
| **代表** | Workday Sana, SAP Joule, ADP Assist, Oracle HCM AI | Wisq (Harper), Leena AI, Aisera, Moveworks |
| **核心优势** | 与自己 HCM 的数据模型、权限、工作流零摩擦集成——不用建连接器 | 可跨多个 HR 系统编排——Workday 的 PTO + SAP 的薪酬 + ServiceNow 的工单 |
| **核心局限** | 离开自有 HCM 生态后能力骤降——SAP Joule 读不到 Workday 的数据 | 需要大量集成工作——每个新系统都是一个连接器项目 |
| **典型买家** | 「我们已经是 Workday/SAP 全家桶了，不想再买一个独立工具」 | 「我们有 5 个 HR 系统，需要一个统一的 AI 层」 |
| **AI 成熟度** | 通常落后 AI-native 厂商 1-2 代——这些是 HCM 公司的 AI 功能，不是 AI 公司的 HCM 功能 | 通常领先——AI 是核心产品，不是附加功能 |
| **2026 趋势** | 在追赶中：Workday 收购 Paradox（2025.10），SAP 加大 Joule 投入 | 在防御中：Wisq 自研 HRLM 建护城河，Leena 靠 1,000+ 集成规模筑墙 |

**纯问答 vs 执行型 Agent**（能力层级递进）：

| 层级 | 能力描述 | 代表产品 | 典型场景 |
|------|---------|---------|---------|
| Level 1：FAQ 检索 | 从知识库中找到匹配的政策文档段落 | BambooHR "Ask BambooHR" | 「产假有几天？」→ 返回员工手册相关段落 |
| Level 2：个性化问答 | 检索 + 理解员工个人数据（部门、职级、地点）给出个性化答案 | Leena AI, ADP Assist | 「我在加州的产假政策？」→ 结合总部政策 + 加州法规 + 员工档案 |
| Level 3：引导式自助 | 问答 + 引导员工完成多步自助流程（但不执行系统写入） | ServiceNow HRSD + Now Assist | 「我要更新 W-4」→ 引导员工到正确的 ESS 页面 |
| Level 4：执行型 Agent | 理解意图 → 自主执行跨系统操作 → 确认完成 | Wisq (Harper), Moveworks | 「我下周一请病假」→ 查余额 → 满足条件 → 在 Workday 发起 → 通知经理 |

2026 年的竞争焦点是 Level 3 → Level 4 的跨越——谁能从「告诉你该做什么」进化到「帮你做完了」，谁就定义了下一代的用户体验。

---

## 问题域（为何会出现这类产品）

- **HR 服务台的「重复性问题」困境**：HR 服务台收到的工单中 40-60% 是重复性政策问答——「我有多少天 PTO？」「产假怎么申请？」「牙科保险覆盖什么？」。传统模式是 HR 手动回复每一张工单，耗时 15-45 分钟/条。AI 将这些工单的自主解决率推到 40-80%，释放的 HR 工时转向策略性工作。
- **员工期望已从「门户自助」升级为「对话即服务」**：员工不再接受「去内网 HR 门户搜 FAQ」的体验——他们习惯了 ChatGPT 式的自然语言即时回答。企业如果继续提供 SharePoint 时代的知识库体验，员工满意度会持续下降，而 HR 收到的抱怨工单越来越多。
- **合规风险的「长尾」问题**：HR 政策与联邦/州/地方法规的交叉越来越复杂——FMLA + ADA + 各州 Paid Leave + 公司政策 + 工会合同。人工 HR 在处理边缘案例时出错的概率不低，而一次错误回答可能引发诉讼。AI 在「复杂政策交叉引用」场景上的一致性优于疲劳或经验不足的 HR Generalist——前提是模型经过足够的领域训练。
- **跨系统数据碎片化**：中大型企业通常有 5-15 个 HR 相关系统（HRIS + Payroll + Benefits + LMS + Performance + Time Tracking + Service Desk）。员工的一个简单问题（「我还有多少 PTO，如果我下周五请假会不会影响我的项目交付？」）需要跨 3 个系统查询。AI assistant 的知识编排能力把分散数据聚合成一个自然语言答案。
- **AI 预算正在从实验走向规模部署**：ISG 2025 调查显示企业 HR 的 AI 预算均值已达 $1.6M（2026 年），较 2023 年增长 10 倍。超过 2/3 的企业将 AI 列为 HR 前三大优先级。预算从「试点一个 chatbot」升级为「部署一个能执行操作的 HR Agent 平台」时，对产品深度和集成能力的要求完全不同——这催生了专业 AI HR assistant 品类的独立。
- **「AI HR 通才」vs「水平 AI 助手」的落差**：Microsoft 365 Copilot 和 Google Gemini 可以帮员工写邮件、做 PPT、总结会议——但它们回答不了「我在新泽西远程工作的 FMLA 资格是什么」或「如果我 12 月离职，未用 PTO 的跨年结转规则是什么」。企业发现通用 AI 在 HR 场景中给出的答案不可靠、不可审计、不引用具体政策——这为专用 AI HR assistant 创造了需求空间。

---

## 能力栈（概念拆分，非厂商功能表）

- **HR 领域知识深度**：通用 LLM 的基础 HR 知识 → 公司政策文档的 RAG 检索 → 劳动法规的结构化理解（联邦/州/地方法规层级） → 专有 HR 推理模型（HRLM, WorkLM）。2026 年的分水岭是第三→第四层的跨越——从「检索文档 + LLM 总结」升级到「用专门训练过的模型做合规性推理」。
- **个性化上下文拼接**：无上下文（返回通用答案）→ 基于员工角色/部门（「经理的 PTO 审批流程」vs「个人贡献者的 PTO 申请流程」）→ 基于员工实时数据（PTO 余额、工作地点、适用的法规）→ 跨系统上下文（PTO + 项目交付日期 + 团队人员配置）。层级越高，答案越精准，但隐私和权限控制越复杂。
- **系统集成读写能力**：只读知识库（FAQ 文档）→ 只读 HRIS API（可查但不能写）→ 受限写入（在批准流程内写入 HRIS——如发起 PTO 申请）→ 全自主写入（处理合规检查后自动执行——如更新 W-4、选择福利计划）。风险随写入能力指数增长——每一层都需要更严格的审计追踪。
- **合规护栏强度**：无护栏（LLM 自由生成）→ 提示词约束（「请保持合规」）→ 检索约束（必须引用文档后才可回答）→ 策略引擎（规则引擎 + AI 推理的双层架构——规则引擎做「硬」合规阻断，AI 做「软」解释）。Wisq 的 HRLM 和 Leena AI 的 WorkLM 都属于策略引擎层——在模型层面内嵌了合规约束而非事后检查。
- **多语言与多法规辖区支持**：单语言/单国家 → 多语言（100+ 语言表面翻译）→ 多法规（同一问题在不同州/国家返回不同合规答案）→ 动态法规更新（法律变了，AI 的答案次日自动更新）。Leena AI 的 100+ 语言覆盖和多国部署是行业标杆；Wisq 在法规推理的自动化更新上更强。
- **渠道覆盖**：Web 门户 widget → Slack/Teams bot → 邮件 → SMS/WhatsApp → 语音电话。大多数企业从 Slack/Teams 起步（员工已经在那），然后扩展到 Web 和邮件。语音渠道（HR 服务热线）的 AI 化是 2026 年的新兴趋势。
- **可解释性与审计准备**：黑盒（AI 给出答案但不说明来源）→ 引用来源（附链接到政策文档段落）→ 决策追溯（完整记录检索到的文档、应用的规则、AI 的推理路径）→ 合规报告导出（一键生成供第三方审计使用的偏差/准确性报告）。EU AI Act（2026.08）和 NYC Law 144 的衍生压力将第三层变为企业采购的最低门槛。
- **人工升级与协作**：纯 AI 自主 → AI 回答 + 不满意可转人工 → AI 先回答 + 人工审核后再发出 → 智能路由（AI 判断自己搞不定的问题自动升级，附上已收集的上下文）。Leena AI 的「AI 先草拟 → HR 审批 → 发送」模式在敏感场景（如解雇政策问答）中更受欢迎。

---

## 形态谱系（与具体品牌解耦）

- **Type I：HCM 内嵌 AI 助手**——Workday Sana, SAP Joule, ADP Assist, Oracle HCM AI。在自己的 HCM 生态内提供问答和有限执行。优势是数据模型和权限天然打通；劣势是离开自家生态后能力骤降，AI 技术栈落后于 AI-native 厂商。适合「已经 All-in 一个 HCM 平台」的大型企业。2026 趋势：Workday 收购 Paradox（2025.10）可能加速 Type I 的 AI 能力追赶。
- **Type II：独立 AI HR 通才平台**——Wisq (Harper), Leena AI。自研或不依赖单一 HCM，以「对整个 HR 职能域的深度理解」为核心竞争力。Wisq 走自研 HRLM 路线，强调「HR 推理优于通用生成」；Leena AI 走广泛集成路线，强调「连接一切 + 保证自助率」。适合「HR 系统多且杂、需要统一 AI 层」的企业。
- **Type III：跨职能企业助手**——Moveworks, Aisera。从 IT 服务台起步，扩展到 HR、Finance、Legal 等领域。核心优势是「一个 bot 解决所有员工问题」的统一体验；劣势是 HR 领域深度不如 Type I/II 专业——在处理复杂的劳动法交叉场景时可能过于泛化。Moveworks 2024 年被 ServiceNow 收购后加速 HRSD 集成。
- **Type IV：HR 服务台 AI 增强**——ServiceNow HRSD (Now Assist), Salesforce HR Agentforce。在已有的 HR 服务台/工单系统上叠加 AI 层——而不是替换整个服务台。优势是与现有 HR 工单系统无缝衔接；劣势是 AI 能力受限于底层平台的架构。「AI 增强现有系统」的叙事更适合不愿大幅改变 HR 运营模式的企业。
- **Type V：Teams/Slack 原生轻量 HR Bot**——Rezolve.ai, AskPorter（注：AskPorter 实际是物业管理 AI，非 HR，此处仅 Rezolve.ai 为代表）。专为 Microsoft Teams 或 Slack 生态设计，在员工已经工作的地方提供 HR 自助。轻量级部署（几周内上线），功能深度有限，适合中小企业和部门级试点。
- **Type VI：水平 AI 助手的 HR 用例**——Microsoft 365 Copilot, Google Gemini for Workspace, ChatGPT Enterprise。HR 团队或员工在工作中顺手用通用 AI 处理 HR 任务——写 JD、总结面试反馈、起草政策文档。不是真正的「HR 助手产品」，但正在抢占部分轻量 HR 场景。对 Type I-V 的真正威胁取决于通用 AI 能否在未来 2 年内解决「HR 合规可靠性」问题。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **合规建议的法律效力风险**：AI HR assistant 给出的政策解释如果被员工视为「公司官方立场」，而答案有误，公司可能面临劳动法诉讼。Wisq 的 Harper 和 Leena AI 都在答案中附加了「AI 生成、仅供参考」的免责声明，但法院是否会接受这一免责仍不确定。最佳实践：对敏感 HR 主题（解雇、歧视投诉、FMLA 资格）设置硬性人工审核环节。
- **数据隐私与跨系统访问权限**：AI assistant 需要读取 PTO 余额、薪酬等级、健康保险选择等敏感数据才能给出个性化答案——但哪些数据可以被 AI 索引？AI 在回答员工 A 的问题时会不会意外暴露员工 B 的薪酬数据？GDPR 和 CCPA 要求数据最小化和目的限制——AI assistant 的数据访问范围必须精确限定，且有完整的审计日志。
- **EU AI Act 高风险分类**：HR 领域的 AI 用途（招聘、绩效评估、晋升决策、任务分配）被 EU AI Act 明确列为「高风险」。2026 年 8 月 2 日完全执行。AI HR assistant 如果仅仅回答政策问题（不做评估或决策），可能不触发高风险分类——但如果它开始辅助绩效预校准（Wisq 的 Harper 有此功能），就可能进入高风险范围。合规策略需要基于实际功能逐项评估。
- **代理变量偏差放大**：即使 AI HR assistant 不直接做招聘决策，它在回答「谁符合晋升条件」「内部转岗需要什么资格」等问题时，答案可能隐含对某些受保护群体的系统性不利。这类偏差更难检测——因为它不像「筛掉所有女性候选人」那样明显，而是通过微妙的「推荐路径差异」体现。
- **工单偏转过度的员工体验风险**：将 HR 工单偏转率推到 80% 可能看起来很高效——但有些员工问题**需要**与真人对话（丧假、职场冲突、心理健康资源）。如果 AI 过度拦截，员工可能感到被去人性化。Wisq 的「AI First & Deeply Human」定位就是尝试在高效和人性化之间找平衡——但平衡点是组织决策而非技术决策。
- **模型更新与政策同步的时效性**：劳动法规变动（如某州通过新 Paid Leave 法案）后，AI assistant 的答案需要在生效日当天更新。依赖通用 LLM（更新周期为月级）的方案无法满足这一需求；自研模型（如 HRLM）的更新频率取决于厂商的资源投入。购买前需考察厂商的「法规→答案」更新 SLA。
- **卖方锁定与切换成本**：如果企业在 Leena AI 上投入 18 个月建立了 30+ 个系统的集成 + 500 条自定义政策 + 团队培训——切换到 Wisq 或 Moveworks 的成本可能超过最初采购成本的 3 倍。HCM 内嵌型（Type I）的锁定风险最高——因为你已经被 Workday/SAP 绑定了。独立平台型（Type II）至少在 AI 层保留了切换可能。

---

## 落地碎片（实践建议）

- 选型前先量化你的工单结构：拉最近 6 个月的 HR 服务台工单数据，按类别统计——政策问答占多少？流程引导占多少？系统操作占多少？情感/复杂场景占多少？如果政策问答 + 流程引导不到 40%，AI assistant 的 ROI 很难达标。如果超过 60%，基本上任何一款 Type I-IV 产品都能在 6 个月内回收成本。
- **从「一个高频率、低风险」用例开始试点**：PTO 政策问答是最安全的切入点——数据容易获取、答案有明确对错（对照员工手册）、合规风险低、员工满意度影响立即可感知。积累 3 个月数据和员工反馈后再扩展到薪酬、福利、绩效等敏感领域。
- **准备「政策文档卫生」工作**：AI assistant 的输出质量直接取决于输入的政策文档质量。如果员工手册是 3 年前的 PDF，远程办公政策散落在 5 封全员邮件里，不同部门的 PTO 规则不一致——AI 的答案也会不一致。AI 部署前先做一轮政策文档审计和统一是 ROI 最高的准备工作。
- **不要把 HR 团队的 adoption 视为理所当然**：HR 人员可能是 AI assistant 的最大阻力——「这个 AI 会不会替代我的工作？」「我用 10 年经验判断的事，AI 凭什么 8 秒给答案？」。成功的 adoption 策略：让 HR 从「工单处理者」转型为「AI 训练师 + 例外场景专家 + 员工体验设计师」——给他们升维而非替代的叙事。
- **中国市场优先看 AI 与现有钉钉/飞书/企业微信生态的整合**：Wisq 和 Leena AI 主要覆盖欧美市场。国内 HR 服务台 AI 在钉钉（阿里生态）、飞书（字节生态）、企业微信（腾讯生态）上的集成深度比产品功能本身更关键——因为中国员工不在 Slack/Teams 上。北森和 Moka 的 HR 助手模块是在中国市场的接近选择。
- **构建「AI 信心」而非「AI 依赖」**：在 AI 答案旁边显示置信度、引用来源、以及「如有疑问请联系 HR [姓名]」的快捷方式。员工对 AI 答案的信任是逐步建立的——过早隐藏人工 HR 的联系方式会适得其反。

---

## 工具与产品类型（检索词常混在一起的品类）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|-------------|------|
| **AI HR assistant / AI HR chatbot** | Wisq (Harper), Leena AI, Rezolve.ai | 本知识块的核心品类——专注 HR 域的自然语言问答与自助服务 |
| **HCM-embedded AI copilot** | Workday Sana, SAP Joule, ADP Assist, Oracle HCM AI | HCM 厂商内嵌的 AI 助手——深度绑定单一生态 |
| **Cross-functional enterprise AI assistant** | Moveworks, Aisera, IBM watsonx Orchestrate | 跨 IT+HR+Finance 的统一助手——HR 只是领域之一 |
| **HR service desk AI (HRSD AI)** | ServiceNow HRSD (Now Assist), Salesforce HR Agentforce | 在已有服务台产品上叠加 AI 层 |
| **水平 AI 助手（HR 用例）** | Microsoft 365 Copilot, Google Gemini, ChatGPT Enterprise | 通用 AI 被 HR 团队顺手使用——非专用产品 |
| **IT service desk AI（跨界竞争）** | Moveworks (IT 起步), ServiceNow ITSM, Aisera | IT 服务台 AI 正在向 HR 领域扩张——2026 的关键跨界趋势 |

---

## 外链索引

### 本文重点覆盖产品（未来 Alignify hr-assistant 页 bestTools 候选）

| 名称 | 一句话 | URL |
|------|--------|-----|
| Wisq (Harper) | 自研 HRLM 垂直模型的 AI HR 通才；SHRM-CP 94% 正确率，80% 自主解决率，Fast Company 2026 HR #2；$55M 融资（Norwest/Shasta/True） | https://www.wisq.com/ |
| Leena AI | 企业级虚拟助手，自研 WorkLM；500+ 客户（Nestlé/Coca-Cola/Sony），1000+ 集成，合同承诺 70% 自助率；年费 ~$300K/千用户起 | https://leena.ai/ |
| ServiceNow HRSD + Now Assist | HR 服务交付 + AI 增强；工作流编排骨架 + 生成式 AI；与 ITSM 天然互通 | https://www.servicenow.com/products/hr-service-delivery.html |
| Moveworks | 跨职能企业助手（IT+HR+Finance）；2024 年被 ServiceNow 收购，已集成 HRSD | https://www.moveworks.com/ |
| Aisera | 自研 LLM 的智能体 AI；覆盖 HR/IT/CS；强调「AI 不只是回答，还能执行」 | https://aisera.com/ |
| IBM watsonx Orchestrate | 多智能体 HR 工作流编排；80+ 企业应用连接器；无代码 Agent Builder；面向受监管行业 | https://www.ibm.com/products/watsonx-orchestrate |
| Workday Sana | Workday HCM 原生 AI 助手；Skills Cloud 驱动个性化；深度薪酬/绩效/招聘集成 | https://www.workday.com/ |
| SAP Joule | SAP SuccessFactors 内嵌 AI 助手；SAP 生态全产品线嵌入策略 | https://www.sap.com/products/artificial-intelligence/ai-assistant.html |
| ADP Assist | ADP 薪酬/HR 平台内嵌 AI；薪酬+合规+HR 政策一站式 | https://www.adp.com/ |
| Rezolve.ai | Microsoft Teams 原生员工服务台 AI；轻量部署（几周上线），面向中端市场 | https://www.rezolve.ai/ |

### 品类内其他值得关注的产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| Gloat + Loomra | 自研 Knowledge Graph 的 AI Agent 平台；29 个 Agent、4 类、跨 HCM 写入；模型无关（Anthropic/Google/IBM） | https://gloat.com/ |
| Microsoft 365 Copilot | 水平 AI 助手；在 Teams/Outlook/Office 内处理 HR-adjacent 任务；非专业 HR 工具但正在抢占轻量场景 | https://www.microsoft.com/en-us/microsoft-365/copilot |
| BambooHR "Ask BambooHR" | SMB HRIS 内嵌 AI 问答；功能较基础（Level 1 FAQ） | https://www.bamboohr.com/ |
| HiBob AI | 中端市场 HRIS + AI 助手；DecisionIQ 合规护栏，InsightsIQ 情绪洞察 | https://www.hibob.com/ |
| Personio AI | 欧洲 SMB HR 平台内嵌 AI 助手；GDPR 原生，Slack/Teams bot，EU 数据驻留 | https://www.personio.com/ |
| Rippling | 统一 HR+IT+Finance 平台；AI 驱动的绩效评估 + 自动化入职/离职工作流 + 185+ 国家 EOR | https://www.rippling.com/ |
| Lattice AI Agent | 持续绩效管理平台 + AI Agent + Knowledge Vault 政策问答 | https://lattice.com/ |

### 对比与测评（第三方；观点非官方）

- Wisq "20 Best AI HR Software in 2026" ——按 HR 问题类型（政策问答、运营碎片化、绩效模糊、员工流失等）分类推荐，覆盖 20+ 产品；Wisq 自身列入多个类别但标注了利益冲突。
- HR Lineup "Top 5 AI Chatbots for Employee Self-Service HR 2026" ——聚焦员工自助服务场景的 5 款 chatbot 横向对比，含自助率、集成深度、定价。
- Gloat Agentic HR Academy "The vendor landscape: Joule, Illuminate, Copilot, and beyond" ——六维度评估框架（Context Breadth, Autonomy Spectrum, Skills Intelligence, Delivery Model, Governance, Integration Philosophy），最系统的企业选型指南。
- monday.com "15 Best AI for HR Platforms for Smarter People Operations" ——15 款 AI HR 平台综述，强调跨部门工作上下文和 AI 治理。
- TTMS "10 Best AI Tools Supporting HR in 2026" ——排名式 listicle，从 AI 简历筛选到员工自助全覆盖。
- Flow Agency "How Google AI Mode Is Shifting HR and Work Tech Visibility"（2026）——5,000 关键词研究，揭示 HR SaaS 在 AI Mode 中的可见性规律：仅 25% 的 top-ranking 页面出现在 AI Mode 中，需独立 GEO 策略。
- ISG "Enterprises Shift to AI and SaaS to Drive Strategic HR Services"（2025.11）——企业 AI HR 预算和采纳率数据，AI 预算均值 $1.6M（2026），10 倍于 2023 年。

---

## 延伸阅读与参考材料

- **市场数据**：TBRC "Generative AI in Human Resources (HR) Market Report 2026"（GenAI in HR: $0.75B→$0.88B, 18.1% CAGR）；TBRC "Artificial Intelligence in HR Global Market Report 2026"（AI in HR 整体：$6.99B→$8.3B, 18.7% CAGR）；Fortune Business Insights "Human Capital Management (HCM) Market"（$34.12B→$37.22B，2025-2026，9.4% CAGR）。
- **品类分析**：Gloat "Agentic HR Academy"——对 AI Agent 在 HR 中的六维度评估框架，目前最深入的企业选型参考；Wisq "20 Best AI HR Software in 2026"——按 HR 问题类型组织的产品地图。
- **合规框架**：EU AI Act 正式文本（OJEU，2024.07.12）——HR 用途（招聘、绩效评估等）属高风险分类，2026.08.02 完全执行；Flow Agency "AI Mode for HR Tech SEO"——AI 搜索可见性的独立策略需求。
- **行业趋势**：SHRM 2025 Talent Trends——43% 企业在 HR 中使用 AI；ISG 2025 企业调查——AI HR 预算均值 $1.6M，10 倍增长；Forbes "How AI Is Reshaping The Human Resources Profession"（2026.04）。
- **技术架构**：Gloat 的 Knowledge Graph + Agent 架构白皮书——2.4M 实体、18.7M 边的跨系统知识图谱；Wisq HRLM vs Leena AI WorkLM——两种自研 HR 垂直模型的架构对比。
