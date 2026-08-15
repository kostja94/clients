# AI Recruiting · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、[Product Hunt](https://www.producthunt.com/search?q=HR+assistant) / G2 条目、行业对比文与社区讨论、HR.com / TechTarget / Weekday 品类分析、市场研究机构报告、法律媒体合规分析）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**（本次更新：修正 Clado/Carv/Moonhub/Brix/JuiceBox/Jack & Jill 产品数据，新增 Wisq 与 HR Ops 边界说明）。**主轴词**：**AI recruiting** / **AI talent acquisition** / **AI recruitment platform**；中文语境常称 **AI 招聘** / **智能招聘** / **AI 人才获取**，与 **interview-assistant**（候选人侧面试准备）、**productivity**（通用效率工具）、**note-taker**（面后复盘）在用户角色与意图上根本不同。

**站内对照**：[alignify.co/tools/recruiting](https://alignify.co/tools/recruiting) · [alignify.co/zh/tools/recruiting](https://alignify.co/zh/tools/recruiting) · slug **`recruiting`**。

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#recruiting-tools`](../../keywords/alignify-keywords-tools.md#recruiting-tools)）

**关联关键词（跨品类检索术语，本知识块需覆盖但非专属）**：

| 角色 | 英文关键词 / 短语 | 中文关键词 / 短语 |
|------|-------------------|-------------------|
| 核心品类 | AI recruiting tools, AI talent acquisition, AI recruitment software, AI hiring platform, intelligent recruiting | AI 招聘工具、智能招聘、AI 人才获取、AI 招聘软件 |
| 子功能 | AI candidate sourcing, AI resume screening, AI candidate matching, AI interview automation, AI skills assessment | AI 候选人搜索、AI 简历筛选、AI 人岗匹配、AI 面试自动化、AI 技能测评 |
| 架构/交付 | AI-powered ATS, talent intelligence platform, conversational AI recruiting, recruitment CRM, AI recruiting agent | AI 驱动的 ATS、人才智能平台、对话式 AI 招聘、招聘 CRM、招聘 Agent |
| 竞品检索 | HireEZ alternative, SeekOut competitor, Gem vs Weekday, Eightfold AI, Paradox Olivia, MokaHR | HireEZ 替代品、Moka vs 北森、AI 招聘工具对比 |
| 相邻品类（分流用） | AI interview assistant, AI productivity, AI note taker, HR tech, HRIS/HCM | AI 面试助手、AI 生产力工具、AI 会议记录、HR SaaS、HRIS |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流（品类易混时必读）

本知识块描述的是**面向雇主/招聘方**的 AI 工具——用于搜人、筛人、评人、管人。它不是候选人用来准备面试的，也不是通用的任务管理。下表厘清与本目录内其他相关 slug 的边界：

| slug | 典型买家问题 | 用户角色 | 与本 slug 的边界 |
|------|-------------|---------|------------------|
| **`recruiting`（本页）** | 「我用什么工具在海量候选人里找到最匹配的那个？怎么自动筛简历、自动发消息、自动评估技能？」 | HR / TA / 招聘经理 / 猎头 | — |
| **`interview-assistant`** | 「我明天有面试，需要一个帮我模拟面试、实时提示答案、分析问题的 AI」 | **候选人**（求职者） | recruiting 是**雇主侧**工具（筛人、管人）；interview-assistant 是**候选人侧**工具（备考、辅答）。二者是招聘炉子的两端——recruiting 是进炉口，interview-assistant 是出炉口 |
| **`productivity`** | 「我要管项目、排日程、写周报」 | 任何知识工作者 | recruiting 是**垂直行业工具**（招聘场景专用），productivity 是**通用工具**。recruiting 的自动化是"自动给 100 个候选人发个性化 outreach"，不是"把我的任务卡片挪到 done" |
| **`note-taker`** | 「我要记录面试对话、生成面评、同步到 ATS」 | HR / 面试官 | note-taker 是**面试后**的转录与总结工具；recruiting 覆盖**面试前**（搜索→筛选→联系→排面）全流程。二者是上下游互补（搜人→排面→用 note-taker 记→发 offer） |
| **`notes-generator`** | 「我要把课件/JD 自动转成备考笔记」 | 求职候选人 / 学生 | notes-generator 是**学习内容生成**工具，与 recruiting 的招聘流程管理完全无关 |

## recruiting vs HR Ops（人力资源运营）边界——为什么 Wisq 不属于 recruiting

Wisq（Harper AI HR Generalist，$55M 总融资，Fast Company 2026 HR 创新 #2）是一个 **AI HR 运营平台**，不是招聘工具。它解决的是员工**入职后**的问题——合规与政策问答、绩效管理预校准、教练辅导、工单分流、员工支持——即「员工已经在公司了，怎么管理」。「怎么找到并录用这个人」不属于 Wisq 的核心场景。recruiting 覆盖**录用前的漏斗**（寻源→筛选→评估→发 offer），AI HR Ops 覆盖**录用后的生命周期**（入职→管理→发展→离职）。二者是 HCM（人力资本管理）大伞下的相邻但根本不同的两个品类。如果 Alignify 未来要扩展 HR Tech 全品类，Wisq 应属于独立的 HR Ops / HR Tech 类别，而非 recruiting。

---

## 词汇锚点

- **AI recruiting / AI 招聘（本知识块的主标签）**：以 AI 技术自动化、增强或替代招聘流程中一项或多项环节的软件工具品类。覆盖范围从**候选人搜索**（sourcing）→**简历/画像筛选**（screening）→**技能/文化匹配**（matching）→**面试排程与执行**（interview automation）→**录用决策支持**（decision support）。与 ATS（Applicant Tracking System）的关系：传统 ATS 是"记录系统"（谁投了、到哪一步了），AI recruiting 是"行动系统"（帮你去哪找人、谁值得面、怎么联系）。
- **Candidate sourcing / 候选人搜索**：主动从多个公开/付费渠道（LinkedIn、GitHub、Stack Overflow、专业数据库）发现被动候选人（passive candidates）的过程。传统 sourcing 靠人工 Boolean 搜索 + 手动逐一联系；AI sourcing 自动跨平台扫描、语义匹配、批量外联。2025–2026 年的竞争关键从「搜得多」转向「搜得准+联系得上」——数据库大小从 800M 降到 250M 但 contact accuracy 从 85% 升到 99% 就是这一趋势的缩影。
- **Candidate screening / 简历筛选**：对主动投递或被动发现的候选人进行第一轮合格性判断。AI screening 用 NLP 解析简历和 JD，计算语义匹配度（非关键词匹配），按 fit score 排序。顶级 AI screening 工具的简历解析准确率可达 97%（如 MokaHR），但需注意**代理变量偏差**——AI 可能将 ZIP 码、毕业年份等与受保护特征关联。
- **Talent intelligence platform / 人才智能平台**：超越"搜人→筛人"的更高层概念——用 AI 构建全组织技能图谱（skills ontology），支持外部招聘 + 内部转岗 + 继任规划 + 劳动力规划。Eightfold AI 的 "talent graph" 是此概念的最完整实现。与纯 sourcing 工具的区别：后者只解决"现在要填这个坑"，前者解决"组织现在和未来需要什么能力"。
- **Conversational AI recruiting / 对话式 AI 招聘**：用实时语音或文本对话代替传统表单/异步视频的候选人交互方式。2025–2026 年正从异步单向视频面试（HireVue 经典模式）向**实时语音 AI 面试**演进——AI 在候选人提交申请的 90 秒内拨打电话，进行 15–20 分钟结构化对话。Paradox 的 Olivia 和 Skillora 的 LiveKit 方案是此范式的代表。招聘聊天机器人市场预计从 $2.03B（2025）增长到 $5.41B（2030）。
- **AI recruiting agent / 招聘 Agent**：2026 年最新演进——从"辅助 recruiter 做每一步"升级为"半自主执行多步工作流"。Agent 自主完成搜索→评估→外联→排面→跟进，recruiter 从操作者变为监督者。HireEZ 的 EZ Agent、Recruiterflow 的 AIRA、Workable 的 Agent 嵌入标志着这一转折。与 chatbot 的关键区别：Agent **执行动作**（发邮件、排日历、更新 CRM），chatbot **交换信息**（回答问题、收集数据）。
- **Bias audit / 偏差审计**：对 AI 招聘工具的筛选/匹配/排序结果进行统计分析，检查是否对不同种族、性别、年龄等受保护群体产生**差异性影响**（disparate impact）。NYC Local Law 144（2023）是全球首个强制要求年度独立偏差审计的法规；California FEHA（2025）、Colorado CAIA（2026.06）、EU AI Act（2026.08）构成日益严格的审计义务矩阵。
- **ATS integration / ATS 集成**：AI 招聘工具与传统申请人跟踪系统的对接深度。关键区分层级：浅集成（单向导出 CSV）→ 中集成（API 实时同步候选人状态）→ 深集成（AI 工具直接写入 ATS、触发工作流、更新 pipeline stage）。Gem 的 20+ ATS 集成和 JuiceBox 的 40+ ATS/CRM 集成代表深度集成派。

---

## 专题对照 / 扩展定义

本笔记用法：厘清 AI 招聘工具的四大核心功能域，以及「AI 招聘 vs AI 面试助手」的根本边界。

| 维度 | **AI Sourcing（搜索）** | **AI Screening（筛选）** | **AI Assessment（评估）** | **AI Interview Automation（面试自动化）** |
|------|------------------------|------------------------|--------------------------|----------------------------------------|
| **核心问题** | 去哪找到对的人？ | 这 500 份简历里谁值得面？ | 这个人的真实能力是什么？ | 怎么高效、公平、可追溯地完成初面？ |
| **AI 技术** | 语义搜索 + 多平台扫描 + 自动外联 | NLP 解析 + 语义匹配 + fit score 排序 | 自适应测评 + 编程测试 + 行为分析 | 语音 AI + 结构化提问 + 实时评分 |
| **输出** | 候选人列表 + 已发消息 | 按匹配度排序的短名单 | 能力画像 + 分数 + 面试建议 | 面试记录 + 评分 + 通过/不通过建议 |
| **代表** | Weekday, HireEZ, Gem, SeekOut, Fetcher, JuiceBox | MokaHR, Humanly, Eightfold AI, Greenhouse | HackerRank, TestGorilla, Pymetrics | Paradox Olivia, Skillora, HireVue |
| **适合谁** | 需要主动挖人的 recruiter | 收到海量投递的 HR | 需要验证硬技能的团队 | 高频批量招聘（零售/餐饮/客服） |

**recruiting vs interview-assistant 的根本差异**（用户不同，意图相反）：

| 维度 | **recruiting（本页）** | **interview-assistant** |
|------|----------------------|------------------------|
| **谁在用** | HR / TA / 招聘经理 / 猎头 | 求职候选人 |
| **要达成什么** | 从 500 人中选出最好的 3 个 | 从 50 个候选人中让自己被选中 |
| **AI 帮谁** | 帮雇主省时间、提质量 | 帮候选人提表现、增信心 |
| **交互方向** | AI 评估候选人 | AI 辅导候选人 |
| **合规关注** | 不能歧视候选人 | 不能替考/作弊 |

---

## 问题域（为何会出现这类产品）

- **投递量爆炸**：候选人平均一次投递 40+ 岗位，传统人工筛选完全不敌——一份简历平均被阅读 6 秒。AI screening 将"不可能看完"变成"5 分钟内排出前 20"。
- **被动候选人是主力**：70%+ 的优质候选人不在主动求职状态。传统 sourcing 靠 recruiter 手动 Boolean 搜索 + 逐一 InMail，效率天花板极低。AI sourcing 跨 45+ 平台自动扫描 + 批量个性化外联，把 sourcing 从"打猎"变成"养殖"。
- **招聘漏斗每一层都在泄漏**：从投递到入职，传统招聘漏斗转化率仅 3–5%。AI 在每一层精确测量和优化（为什么候选人在这里 drop？JD 哪里吓跑了人？什么时间发消息回复率最高？），把招聘从"凭感觉"变成"可度量"。
- **技能通胀与岗位演化**：岗位所需的技能组合每 3–5 年大幅变化。传统关键词匹配（"5 年 Python"）既漏掉有潜力的人，又筛进简历造假的人。AI 技能匹配（skills-based matching）把评估从"你做过什么 title"转向"你能做什么"。
- **偏见不是 bug 而是特性**：人类 recruiter 的决策受大量无意识偏见影响（姓名、学校、照片、年龄）。AI 在**理想情况下**能标准化评估——但在**现实情况下**可能放大训练数据里的历史偏见。需求来自两股相反的力："用 AI 消除人类偏见"和"防止 AI 固化历史偏见"。
- **分布式团队 + 跨时区招聘**：远程/混合办公成为常态（美国~19.5% 远程工作），传统"来公司面半天"的流程瓦解。AI 排面 + 异步/实时 AI 面试填补了地理和时区鸿沟。
- **合规压力从可有可无变成生死攸关**：NYC Law 144（2023 生效，2025 年审计发现执法不力后加压）、California FEHA（2025.10）、Colorado CAIA（2026.06）、EU AI Act（2026.08）——四重法规叠加，任何使用 AI 筛人的雇主都必须有审计、有披露、有人工干预。这催生了"合规即服务"型 AI 招聘工具（Humanly 的审计就绪方案）。

---

## 能力栈（概念拆分，非厂商功能表）

- **数据源广度与质量**：从单平台（LinkedIn）→ 多平台（LinkedIn + GitHub + Stack Overflow + Twitter + 专利数据库）→ 专有数据库（Weekday 的 250M 自建库，非公开爬取）。关键不在数量而在**联系人准确性**——800M 公共数据但 email bounce rate 30% 远不如 250M 验证过的数据。2026 年的共识："数据库大小 ≠ 产出"。
- **匹配粒度**：关键词匹配（"5 年 Python"）→ 语义匹配（理解"构建过分布式系统"≈"后端架构经验"）→ 技能图谱匹配（推断可迁移技能——"做过销售工程师"可能适合"解决方案顾问"）→ 职业轨迹预测（基于 career trajectory 模型预测成功率）。Eightfold AI 是第四层的代表。
- **外联自动化层级**：无（只搜不发）→ 模板化批量邮件 → 个性化 AI 撰写 + A/B 测试 → 多渠道自主外联（邮件 + LinkedIn + WhatsApp + 电话）。Weekday 的多渠道 30–50% 回复率是第四层的标杆数据点。
- **评估模态**：纯文本简历解析 → 异步视频面试（HireVue 经典模式）→ 实时语音 AI 面试（Skillora、Paradox Olivia）→ 多模态评估（语音 + 代码 + 行为 + 情景模拟）。实时语音 AI 面试的关键技术指标是延迟——<800ms 才能维持自然对话节奏。
- **公平性与可解释性**：无 → 事后统计偏差检测 → 代理变量监控（检测模型是否在用 ZIP 码、毕业年份等代理受保护特征）→ 实时偏差审计 + 人工干预工作流。Colorado CAIA 和 EU AI Act 将最低门槛推到了第三层。
- **ATS/HRIS 集成深度**：浅（CSV 导出）→ 中（REST API 同步候选人状态）→ 深（双向写入，触发 ATS 工作流，更新 pipeline stage）。深度集成是实现"AI 搜到的人直接出现在 recruiter 的日常 ATS 界面里"的前提——无缝体验直接决定 adoption。
- **Agent 自主性**：Level 0（纯工具——用户点哪 AI 做哪）→ Level 1（建议——AI 推荐候选人，用户决定）→ Level 2（半自主——AI 自动搜+筛+写消息，用户审核后发出）→ Level 3（全自主——AI 端到端执行，用户只看异常报告）。2026 年头部产品达到 Level 2，Level 3 仍在早期试点。
- **内部流动性支持**：从纯外部招聘 → 内外混合（同时匹配外部候选人和内部员工）→ 人才市场（将内部员工自动匹配到新开岗位，先内后外）。Eightfold AI 和 Beamery 在此维度领先。2026 年趋势：企业在招聘预算收紧时会优先部署内部流动模块。

---

## 形态谱系（与具体品牌解耦）

- **Type I：AI Sourcing 专用工具**——Weekday, HireEZ, Fetcher, SeekOut。唯一焦点是"找到对的人并建立联系"。通常集成 20–45+ 数据源，提供批量个性化外联。轻量 ATS 集成，适合已有 ATS 但 sourcing 环节薄弱的中大型 TA 团队。竞争差异在数据质量（准确率、覆盖面）和外联转化率，而非功能广度。Clado 和 Lessie 也可归入此类，但它们是更宽泛的"人员搜索引擎"——不只服务招聘，也服务销售和营销。
- **Type II：端到端 AI 招聘平台**——Gem, JuiceBox。提供"搜人 → 筛人 → 管人 → 看数据"全流程。通常自建 CRM 层（候选人关系管理），支持长期培育。适合内部 TA 团队规模较大、需要统一"招聘操作系统"的企业。~~Moonhub（2025.06 停运，团队被 Salesforce acqui-hire）原属此类型。~~ Carv（2025 收购 Recrubo 后）正在从 Type V 向此类型演进——从纯评估扩展为全栈批量招聘。
- **Type III：AI Screening & Matching 层**——MokaHR, Humanly, Eightfold AI（匹配模块）, Greenhouse（结构化面试模块）。核心价值在"筛得准、评得公"。强调简历解析精度（MokaHR 97%）、匹配一致性（Humanly 的审计就绪架构）、公平性（Greenhouse 的结构化评分卡）。通常不自己做 sourcing，而是对接已有的 sourcing 和 ATS 层。
- **Type IV：语音/对话式 AI 面试**——Paradox Olivia, Skillora, HireVue（转型中）。2026 年最热的子品类——从异步单向视频面试向实时语音 AI 面试师转型。核心场景：高量级小时工/前线岗招聘（零售、餐饮、客服）的初筛自动化。Paradox 被 Workday 收购（2025.10）标志着此品类进入主流 HCM 生态。（注：Clado 实为 AI 人员搜索平台，非面试工具——其站内产品卡被误标为"AI 面试自动化"，需修正。）
- **Type V：技能评估与测评**——HackerRank, TestGorilla, Pymetrics, CodeSignal。专注于"候选人的真实能力是什么"这一单一问题。提供编程测试、认知测评、情景判断、行为评估。与 Type III 的区别：Type III 用 AI 判断"简历和 JD 有多匹配"，Type V 用测评判断"这个人实际会什么"——两者在招聘漏斗中先后接续。
- **Type VI：企业 HCM Suite 内嵌 AI 招聘**——Workday, SAP SuccessFactors, Oracle HCM, 北森, 金蝶。在传统 HR 系统里嵌入 AI 招聘模块。优势是与薪酬、绩效、入职无缝衔接；劣势是 AI 能力通常落后于 AI-native 竞品 1–2 代。适合"不想另买一个工具"的大型企业。
- **Type VII：招聘 Agent / 自主招聘**——Recruiterflow AIRA, Anna AI (PSG/TP), MeritFinder。2026 年最前沿的品类——AI 不再只是工具，而是自主执行招聘任务的数字员工。目前处于早期试水阶段，多数产品还在 Level 1–2 自主性。发展方向是"设定目标→AI 自主搜→自主筛→自主排面→人做最终决定"。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **算法歧视与代理变量偏差**：AI 筛人最大的法律/伦理风险。即使剔除了种族、性别等显性特征，模型可能通过代理变量（ZIP 码→种族，毕业年份→年龄，就业间隔→性别/育儿假）间接歧视。关键防御机制：定期独立偏差审计 + 代理变量检测 + 人工干预阀门。NYC Law 144、California FEHA、Colorado CAIA 和 EU AI Act 的四重法规框架意味着**偏差审计不再是 best practice，而是法律义务**。
- **联邦与州法规碎片化**：美国在 2025–2026 年间从"无联邦法"进入"各州分别立法 + 联邦预判威胁"的混乱期。California FEHA（2025.10 生效，最严）vs Texas TRAIGA（2026.01 生效，最松）→ Colorado CAIA（2026.06 生效，最全面）。DOJ 的 AI Litigation Task Force 正在以 Dormant Commerce Clause 为由挑战各州法律——未来 1–2 年的法律走向高度不确定。实务建议：按最高标准（California/Colorado）构建合规体系。
- **EU AI Act 的域外效力**：无论公司注册地在哪里，只要 AI 系统的输出在欧盟境内使用或影响欧盟境内人员，就需要合规。招聘用途被明确归为"高风险"类。2026 年 8 月 2 日为完全执行日。关键义务：风险评估、技术文档、偏差监测、人类监督、透明度披露。罚款最高 €35M 或全球营业额 7%。
- **卖方责任（Vendor Liability）**：传统观念"我们只是用了供应商的工具"正在被法院和监管机构突破。California FEHA 明确"供应商在代理原则下可能承担雇主同等的歧视责任"。NYC Law 144 的审计义务由**雇主**（deployer）承担——即使偏差来自第三方工具。实务影响：采购 AI 招聘工具时，合同必须含偏差审计结果分享、及时通知发现的偏差、合同责任条款。
- **候选人数据隐私与同意**：AI sourcing 从 45+ 公开平台抓取候选人数据，这些数据的收集、存储和使用是否获得有效同意？GDPR 要求有合法基础（同意或正当利益），CCPA 赋予删除权。FCRA（公平信用报告法）的新兴法律理论——2026 年 1 月诉讼主张 AI 招聘工具汇总公共数据构成"消费者报告"——可能彻底改变 sourcing 类工具的合规方式。
- **深度伪造与候选人侧 AI 欺诈**：2025–2026 年，候选人使用 AI 辅助面试（实时提示答案、换脸、变声）的现象呈爆发式增长。招聘方开始部署反向 AI 检测工具，形成 AI vs AI 的军备竞赛。这对 AI 招聘工具提出了新挑战——如何在"候选人用了 AI 辅助"和"候选人在作弊"之间划出伦理边界。
- **裁员偏见与反馈回路**：如果 AI 模型用历史录取数据训练，而历史上的录取决策本身就带有偏见，模型会**强化和放大**这些偏见——形成一个自我实现的预言循环。打破这个循环需要**刻意引入反偏见训练数据和人工干预训练标签**，但目前只有极少数工具公开声明了这种做法。

---

## 落地碎片（实践建议）

- 选型第一步是画出你的**招聘量级 × 角色复杂度矩阵**：高量级+低复杂度（零售店员、客服）→ 优先看 Type IV 语音 AI 面试工具（Paradox Olivia）；高量级+高复杂度（软件工程师）→ 优先看 Type I AI Sourcing（Weekday/HireEZ）+ Type V 技能评估（HackerRank）；低量级+高复杂度（高管）→ AI 工具作用有限，人工猎头为主 + AI 辅助搜索。
- **数据质量 > 数据库大小**：不要被"800M profiles"的宣传数字迷惑。要求供应商提供**实际使用数据**——email bounce rate、平均回复率、候选人数据平均新鲜度（最近一次更新时间）。如果供应商拒绝提供，就是一个红旗。
- **合规不是事后补丁**：在采购 AI 招聘工具前，先确认：① 供应商是否提供独立偏差审计报告？② 是否支持定期重审计？③ 工具的决策过程是否可解释（你能看到为什么候选人 A 排在 B 前面）？④ 是否有明确的人工干预机制？如果你自己无法回答"这个工具怎么决定谁排第一"，就不要买。
- **用 pilot 验证，不要用 demo 评估**：用你自己的 20 个真实岗位，用自己的 recruiter 跑 2 周的并行流程（一半岗位用 AI 工具 + 人工，一半纯人工），对比：时间到第一批合格候选人的速度、候选人回复率、最终 offer 接受率、recruiter 满意度。这也是目前唯一有效判断 sourcing 数据质量的途径。
- **中国市场优先看 Moka 和北森**：Moka 在招聘流程协同和候选人体验上打磨最深，适合招聘量大节奏快的互联网/科技企业；北森在一体化 HCM + 人才测评基因上领先，适合 500 人以上中大型集团。两者均已推出 AI Agent 向的招聘功能（2026）。
- **ATS 深度集成是不可谈判项**：如果你的 AI 招聘工具不能在你现有的 ATS 里"无缝出现"——意味着 recruiter 需要额外开一个 tab、复制粘贴数据、手动同步状态——adoption rate 会在 2 周内跌到零。采购前做一次"15 分钟 recruiter 日常流程"的集成 walkthrough。

---

## 工具与产品类型（检索词常混在一起的品类）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|-------------|------|
| **AI candidate sourcing** | Weekday, HireEZ, SeekOut, Fetcher, Gem, JuiceBox, Jack & Jill, Lessie, HeroHunt | 主动搜索+联系被动候选人；本知识块的核心品类之一 |
| **AI people search / 人员搜索引擎** | Clado, Lessie | 自然语言→跨平台人员发现，不限于招聘（也用于销售、营销、投资）；强调搜索广度与联系信息准确性 |
| **AI resume screening & matching** | MokaHR, Humanly, Eightfold AI, Findem | 解析→匹配→排序主动投递的简历；招聘漏斗的第二关 |
| **AI interview automation** | Paradox Olivia, Skillora, HireVue, Talview | 结构化 AI 面试（文本/异步视频/实时语音）；2026 年向语音转型 |
| **Agentic AI 批量招聘** | Carv（收购 Recrubo 后扩展）, Paradox Olivia | 全栈自动化：sourcing + 对话筛选 + 面试调度 + ATS 更新；面向高量级前线岗位 |
| **AI skills assessment** | HackerRank, TestGorilla, Pymetrics, CodeSignal | 硬技能/软技能/认知测评；验证而非猜测能力 |
| **Talent intelligence platform** | Eightfold AI, Beamery, Phenom People | 技能图谱 + 外部招聘 + 内部流动 + 劳动力规划 |
| **Conversational AI recruiting** | Paradox Olivia, Skillora, Anna AI, MeritFinder | 实时语音 AI 面试师；2026 最热品类 |
| **Recruitment CRM** | Gem, Beamery | 候选人长期关系管理 + 培育 + pipeline 分析 |
| **Enterprise HCM Suite (AI module)** | Workday, SAP SuccessFactors, Oracle HCM, 北森, 金蝶 | AI 招聘是 HCM 套件的模块之一 |
| **AI-powered ATS** | Greenhouse, Lever, Ashby, SmartRecruiters, Workable, Manatal | ATS 本身嵌入了 AI 筛选/排程功能 |

---

## 外链索引

### 本文重点覆盖产品（与 Alignify 站内 recruiting 页 bestTools 对齐）

| 名称 | 一句话 | URL |
|------|--------|-----|
| Weekday | 专有 250M+ 数据库，99% 联系人准确率，多渠道自主外联（邮件+WhatsApp+电话），30–50% 回复率，66% fill rate；技术岗 sourcing 2026 领导者 | https://www.weekday.works/ |
| Gem | 全栈招聘平台（ATS+CRM+Sourcing+Analytics），20+ ATS 集成，学习型 AI 随使用改进，企业级安全和多元化分析 | https://www.gem.com/ |
| HireEZ | 800M+ 聚合数据库，45+ 平台，Chrome 扩展浏览器内 sourcing，内置 email sequencing；中端市场最友好 | https://hireez.com/ |
| SeekOut | 700–750M+ 数据，GitHub/专利/出版物深度搜索，行业最强 DEI 过滤器；企业技术/多元化招聘 | https://seekout.com/ |
| Eightfold AI | 人才智能平台（非纯 sourcing），1.5B+ profiles 技能图谱，内部流动性+外部招聘+继任规划；六位数企业合同 | https://eightfold.ai/ |
| Fetcher | 轻量 AI 候选人推荐工具，每日自动推送候选人，不需专门 sourcing 团队；面向早期创业公司 | https://fetcher.ai/ |
| Paradox Olivia | 对话式 AI 招聘助手（被 Workday 2025.10 收购），语音/文字全渠道，高量级小时工招聘首选 | https://www.paradox.ai/ |
| MokaHR | 中国 ATS 招聘专精型平台，97% 简历解析精度，端到端招聘流程协同；AI Agent 功能上线（2026）；适合互联网/科技企业 | https://mokahr.io/ |
| Humanly | 审计就绪型 AI 筛选+互动+排程平台，全证据保留（转录+时间戳+路由），4.8/5 候选人评分 | https://www.humanly.io/ |
| Skillora | 实时语音 AI 面试师，LiveKit 堆栈，次秒级延迟，面向高量级初筛；2026 转型潮流代表 | https://skillora.ai/ |

### 品类内其他值得关注的产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| Jack & Jill | 对话式 AI 招聘平台（伦敦，$20M 种子轮，2025.10）；双智能体模型——Jack（候选人侧 AI 职业教练，免费）+ Jill（雇主侧 AI 招聘官，10% 年薪佣金）；49,000+ 候选人已与 Jack 对话；客户含 Airtable, Airwallex, TrueLayer | https://jackandjill.ai/ |
| JuiceBox (PeopleGPT) | Sequoia + DST Global 投 $80M（2026.03 Series B），估值 $850M，5,000+ 客户（含 Ramp, Cursor, Cognition, Perplexity）；800M+ profiles 自然语言搜索，40+ ATS/CRM 集成，24/7 AI Agent 自主运行 | https://juicebox.ai/ |
| Clado | AI 人员搜索平台（"Deep Research for People"），10 万+ AI Agent 跨 800M+ profiles 自然语言找人；YC S25，$2M 种子轮（Valor Equity）；月增长 60%，客户含 Turing, Mercor；招聘 + 销售/GTM 双场景——**非**面试工具（站内页面描述有误） | https://www.clado.ai/ |
| Carv | Agentic AI 批量招聘全栈平台（阿姆斯特丹，$10M 种子轮，GFC 投）；2025.03 收购 Recrubo 扩展为 sourcing + 对话筛选（WhatsApp）+ 面试调度 + ATS 更新；ManpowerGroup 战略合作；客户含 DHL, Randstad, Jumbo（730 店同日招聘试点）——**非**纯技能评估工具（站内页面描述过窄） | https://www.carv.com/ |
| Brix | AI 跨境招聘 + 工程师众包平台（旧金山+南京双实体，HF0 孵化，NVIDIA Inception）；Brix Recruiter 做 JD 生成、简历筛选、人岗匹配；同时运营远程工程师 marketplace（时薪 $12–55） | https://joinbrix.com/ |
| Moonhub | ~~已停运（2025.06）~~——原"世界首个 AI Recruiter"（$14.4M 融资，Khosla/GV/Salesforce 投），团队被 Salesforce acqui-hire 转入 Agentforce 平台；PitchBook 状态"Out of Business"；不再作为独立产品运营——站内页面需移除 | https://www.moonhub.ai/ |
| Greenhouse | 结构化招聘标杆，评分卡+面试套件，DEI 内置；AI 功能仍在早期 | https://www.greenhouse.com/ |
| Beamery | 人才生命周期管理，技能智能+CRM+内部流动 | https://beamery.com/ |
| Findem | 属性式 sourcing（非关键词），职业轨迹评分，3x Lighthouse Award；企业级 | https://www.findem.ai/ |
| Recruiterflow AIRA | 内嵌 Agent 的招聘管理平台，自动 CRM 更新+职位变动提醒+通话摘要；代理机构向 | https://recruiterflow.com/ |
| 北森 | 中国一体化 HCM + 人才测评/盘点基因，AI 面试官+全渠道招聘 Agent；500 人以上集团 | https://www.beisen.com/ |
| Mercor | AI-native 面试平台，$10B 估值（2025.10），服务 OpenAI/Anthropic 等 AI 实验室 | https://mercor.com/ |
| Pymetrics | 游戏化行为评估（偏差友好），软技能匹配 | https://www.pymetrics.ai/ |
| TestGorilla | 技能测评平台，300+ 测试模板，$70M Series A (2022) | https://www.testgorilla.com/ |
| HackerRank | 技术技能评估标杆，编程测试+真实开发环境 | https://www.hackerrank.com/ |
| Textio | AI 增强型 JD 撰写与沟通，偏差检测 | https://textio.com/ |
| Manatal | 经济型 ATS+AI，$15/用户/月起，面向小型代理机构 | https://www.manatal.com/ |

### 对比与测评（第三方；观点非官方）

- Weekday 的 2026 年 AI Candidate Sourcing Tools 专家排名——当前最系统的英语圈横向对比，覆盖 sourcing/screening/automation 三维度，含详细的响应率、填充率、定价对照。需注意其自然倾向于 Weekday。
- HR.com 2025–26 年"Future of Recruitment Technologies"报告——基于大规模 HR 从业者调研，提供 adoption rate 差距、leader vs laggard 对照、具体使用场景排名（67% 用 AI 生成面试题、65% 写 JD、44% 筛简历）。
- TechTarget "Top AI recruiting tools and software of 2026"——编辑精选，偏企业采购决策导向，覆盖 12 款产品。
- Humanly 的 "Best AI Recruiting Software Tools for 2026" 博客——从 audit-ready 视角评测，强调合规与证据保留维度。
- Everworker.ai "Best AI Candidate Sourcing Platforms for CHROs: 2026 Vendor Guide"——面向 CHRO 的采购框架，含评估标准和供应商筛选矩阵。
- Crustdata "Best AI Sourcing Tools to Find Candidates Faster (2026)"——以数据质量为评测轴心，揭示了"数据库大小 ≠ 结果"的关键洞察。
- 什么值得买 "2026年AI招聘选购：5大品牌核心差异对比"——中文视角下 Moka、北森、金蝶、红海云、KNX 的横向对比。
- DLA Piper "Critical audit of NYC's AI hiring law signals increased risk for employers"（2026.01）——法律视角分析 NYC Law 144 审计失效后的加严趋势。
- Akerman "HRDef: AI in Hiring — Emerging Legal Developments and Compliance Guidance for 2026"——美国 AI 招聘法律合规全景。
- AI Journal "Why Voice AI Is Quietly Eating HR Tech"——实时语音 AI 面试师趋势分析。

---

## 延伸阅读与参考材料

- **市场数据**：TBRC "AI in Talent Acquisition Global Market Report 2026"（$1.60B，18.5% CAGR）；SkyQuest "AI Recruitment Market 2026–2033"（$656M→$1.23B，7.2% CAGR）；Fortune Business Insights "Online Recruitment Technology Market"（$15.18B→$17.48B，12.9% CAGR）。
- **品类分析**：Weekday "Top AI Candidate Sourcing Tools: Expert Rankings 2026"——最全面的 sourcing 横向对比；HR.com "Future of Recruitment Technologies 2025–26"——行业采纳率与成熟度数据。
- **合规框架**：EU AI Act 正式文本（OJEU，2024.07.12）——招聘属高风险分类，2026.08.02 完全执行；NYC DCWP Local Law 144 规则文本 + 2025.12 Comptroller 审计报告——评估执法效果；California Civil Rights Council FEHA Automated Decision Systems Regulations（2025.10 生效）。
- **中国市场**：MokaHR "Best AI Recruitment Tools in 2026: Top 8 Platforms Ranked for Enterprise Hiring"——含 Moka 的中国市场视角；什么值得买 "2026年AI招聘选购"——Moka/北森/金蝶横向对比。
- **学术与行业研究**：NIST AI Risk Management Framework (AI RMF 1.0)——可用于构建 AI 招聘系统的风险管理流程；Brookings "Algorithmic bias in hiring"——代理变量偏差与检测方法综述。
