# AI Recruiting · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI recruiting / AI 人才获取**——面向**雇主/招聘方**的 AI 工具，用于搜人、筛人、评人、管人；验收以**匹配准确率、回复率、fill rate、合规审计**为主。本页为 **AI 招聘 SSOT**（完整 URL 表仅此一处）；候选人侧面试准备 → [interview-assistant.md](interview-assistant.md)；录用后 HR 服务 → [hr-assistant.md](hr-assistant.md)；会议记录 → [note-taker.md](../productivity/note-taker.md)。

**材料范围**：公开网络检索（厂商产品页、G2 条目、行业对比文与社区讨论、HR.com / TechTarget / Weekday 品类分析、市场研究机构报告、法律媒体合规分析）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**（本次更新：修正 Clado/Carv/Moonhub/Brix/JuiceBox/Jack & Jill 产品数据，新增 Wisq 与 HR Ops 边界说明）。

**站内对照**：[alignify.co/tools/recruiting](https://alignify.co/tools/recruiting) · [alignify.co/zh/tools/recruiting](https://alignify.co/zh/tools/recruiting) · slug **`recruiting`**。

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#recruiting-tools`](../../keywords/alignify-keywords-tools.md#recruiting-tools))

## 与相邻 slug 分流（品类易混时必读）

| slug | 典型买家问题 | 用户角色 | 与本 slug 的边界 |
|------|-------------|---------|------------------|
| **`recruiting`（本页）** | 「我用什么工具在海量候选人里找到最匹配的那个？」 | HR / TA / 招聘经理 / 猎头 | — |
| **`interview-assistant`** | 「我明天有面试，需要模拟面试、实时提示答案」 | **候选人**（求职者） | recruiting 是**雇主侧**；interview-assistant 是**候选人侧**——招聘炉子的两端 |
| **`note-taker`** | 「我要记录面试对话、生成面评、同步到 ATS」 | HR / 面试官 | note-taker 是**面试后**转录与总结；recruiting 覆盖**面试前**全流程——上下游互补 |
| **`hr-assistant`** | 「员工入职后怎么自动回答 HR 政策问题？」 | HR 运营 / HRBP | hr-assistant 是**录用后**；recruiting 是**录用前**。分界线是入职日 |
| **`productivity`** | 「我要管项目、排日程、写周报」 | 任何知识工作者 | recruiting 是**垂直行业工具**，productivity 是**通用工具** |

**recruiting vs HR Ops（Wisq 不属于 recruiting）**：Wisq（Harper AI HR Generalist，$55M 总融资）是 **AI HR 运营平台**，解决员工**入职后**的问题——「怎么找到并录用这个人」不属于 Wisq 的核心场景。详见 [hr-assistant.md](hr-assistant.md) §与 adjacent slug 分流。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI recruiting / AI 招聘（本知识块的主标签）**：以 AI 技术自动化、增强或替代招聘流程中一项或多项环节的软件工具品类。覆盖范围从**候选人搜索**（sourcing）→**简历/画像筛选**（screening）→**技能/文化匹配**（matching）→**面试排程与执行**（interview automation）→**录用决策支持**（decision support）。与 ATS 的关系：传统 ATS 是"记录系统"，AI recruiting 是"行动系统"。
- **Candidate sourcing / 候选人搜索**：主动从多个公开/付费渠道发现被动候选人的过程。2025–2026 年的竞争关键从「搜得多」转向「搜得准+联系得上」——数据库大小从 800M 降到 250M 但 contact accuracy 从 85% 升到 99% 就是这一趋势的缩影。
- **Candidate screening / 简历筛选**：对主动投递或被动发现的候选人进行第一轮合格性判断。顶级 AI screening 工具的简历解析准确率可达 97%（如 MokaHR），但需注意**代理变量偏差**。
- **Talent intelligence platform / 人才智能平台**：超越"搜人→筛人"的更高层概念——用 AI 构建全组织技能图谱，支持外部招聘 + 内部转岗 + 继任规划。Eightfold AI 的 "talent graph" 是此概念的最完整实现。
- **Conversational AI recruiting / 对话式 AI 招聘**：2025-2026 年正从异步单向视频面试向**实时语音 AI 面试**演进——AI 在候选人提交申请的 90 秒内拨打电话，进行 15–20 分钟结构化对话。Paradox 的 Olivia 和 Skillora 的 LiveKit 方案是代表。
- **AI recruiting agent / 招聘 Agent**：2026 年最新演进——Agent 自主完成搜索→评估→外联→排面→跟进，recruiter 从操作者变为监督者。与 chatbot 的关键区别：Agent **执行动作**，chatbot **交换信息**。
- **Bias audit / 偏差审计**：对 AI 招聘工具的筛选/匹配/排序结果进行统计分析，检查是否对不同受保护群体产生**差异性影响**（disparate impact）。NYC Local Law 144（2023）、California FEHA（2025）、Colorado CAIA（2026.06）、EU AI Act（2026.08）构成日益严格的审计义务矩阵。
- **ATS integration / ATS 集成**：浅集成（单向导出 CSV）→ 中集成（API 实时同步）→ 深集成（AI 工具直接写入 ATS、触发工作流）。Gem 的 20+ ATS 集成和 JuiceBox 的 40+ ATS/CRM 集成代表深度集成派。

---

## 专题对照 / 扩展定义

**四大功能域对照**——术语见 §词汇锚点；下表只列**核心问题→输出→代表**。

| 维度 | **AI Sourcing** | **AI Screening** | **AI Assessment** | **AI Interview Automation** |
|------|----------------|-----------------|-------------------|----------------------------|
| **核心问题** | 去哪找到对的人？ | 这 500 份简历里谁值得面？ | 这个人的真实能力是什么？ | 怎么高效、公平、可追溯地完成初面？ |
| **输出** | 候选人列表 + 已发消息 | 按匹配度排序的短名单 | 能力画像 + 分数 + 面试建议 | 面试记录 + 评分 + 通过/不通过建议 |
| **代表** | Weekday, HireEZ, Gem, SeekOut | MokaHR, Humanly, Eightfold AI | HackerRank, TestGorilla, Pymetrics | Paradox Olivia, Skillora, HireVue |

**recruiting vs interview-assistant**（用户不同，意图相反）：雇主用 recruiting **评估**候选人；候选人用 interview-assistant **提升表现**——详见 [interview-assistant.md](interview-assistant.md) §专题对照。

产品规格 → **§外链索引**；形态路线 → **§形态谱系**。

---

## 问题域（为何会出现这类产品）

- **投递量爆炸**：一份简历平均被阅读 6 秒。AI screening 将"不可能看完"变成"5 分钟内排出前 20"。
- **被动候选人是主力**：70%+ 的优质候选人不在主动求职状态。AI sourcing 跨 45+ 平台自动扫描 + 批量个性化外联。
- **招聘漏斗每一层都在泄漏**：传统招聘漏斗转化率仅 3–5%。AI 在每一层精确测量和优化。
- **技能通胀与岗位演化**：AI 技能匹配（skills-based matching）把评估从"你做过什么 title"转向"你能做什么"。
- **偏见不是 bug 而是特性**：需求来自两股相反的力："用 AI 消除人类偏见"和"防止 AI 固化历史偏见"。
- **分布式团队 + 跨时区招聘**：AI 排面 + 异步/实时 AI 面试填补了地理和时区鸿沟。
- **合规压力从可有可无变成生死攸关**：NYC Law 144、California FEHA、Colorado CAIA、EU AI Act——四重法规叠加，任何使用 AI 筛人的雇主都必须有审计、有披露、有人工干预。

---

## 能力栈（概念拆分，非厂商功能表）

- **数据源广度与质量**：关键不在数量而在**联系人准确性**——800M 公共数据但 email bounce rate 30% 远不如 250M 验证过的数据。2026 年共识："数据库大小 ≠ 产出"。
- **匹配粒度**：关键词匹配 → 语义匹配 → 技能图谱匹配 → 职业轨迹预测。Eightfold AI 是第四层的代表。
- **外联自动化层级**：无 → 模板化批量邮件 → 个性化 AI 撰写 + A/B 测试 → 多渠道自主外联。Weekday 的多渠道 30–50% 回复率是第四层的标杆数据点。
- **评估模态**：纯文本简历解析 → 异步视频面试 → 实时语音 AI 面试 → 多模态评估。实时语音 AI 面试的关键技术指标是延迟——<800ms 才能维持自然对话节奏。
- **公平性与可解释性**：无 → 事后统计偏差检测 → 代理变量监控 → 实时偏差审计 + 人工干预工作流。Colorado CAIA 和 EU AI Act 将最低门槛推到了第三层。
- **ATS/HRIS 集成深度**：浅（CSV 导出）→ 中（REST API 同步）→ 深（双向写入，触发 ATS 工作流）。深度集成是 adoption 的前提——术语见 §词汇锚点 **ATS integration**。
- **Agent 自主性**：Level 0（纯工具）→ Level 1（建议）→ Level 2（半自主）→ Level 3（全自主）。2026 年头部产品达到 Level 2，Level 3 仍在早期试点。
- **内部流动性支持**：从纯外部招聘 → 内外混合 → 人才市场。Eightfold AI 和 Beamery 在此维度领先。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **I** | AI Sourcing 专用：找到对的人并建立联系 | AI candidate sourcing | Weekday, HireEZ, Fetcher, SeekOut, Gem, JuiceBox |
| **II** | 端到端 AI 招聘平台：搜人→筛人→管人→看数据 | End-to-end recruiting platform | Gem, JuiceBox；Carv 正从 V 向此演进 |
| **III** | AI Screening & Matching：筛得准、评得公 | AI resume screening | MokaHR, Humanly, Eightfold AI, Greenhouse |
| **IV** | 语音/对话式 AI 面试：实时语音 AI 面试师 | Conversational AI recruiting | Paradox Olivia, Skillora, HireVue |
| **V** | 技能评估与测评：验证真实能力 | AI skills assessment | HackerRank, TestGorilla, Pymetrics, CodeSignal |
| **VI** | 企业 HCM Suite 内嵌 AI 招聘 | Enterprise HCM AI recruiting | Workday, SAP SuccessFactors, 北森, 金蝶 |
| **VII** | 招聘 Agent / 自主招聘：半自主执行多步工作流 | AI recruiting agent | Recruiterflow AIRA, Anna AI, MeritFinder |

**易混纠正**：Clado 是 AI 人员搜索平台（Type I 邻域），**非**面试工具；Moonhub 已停运（2025.06），团队被 Salesforce acqui-hire。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **算法歧视与代理变量偏差**：即使剔除了种族、性别等显性特征，模型可能通过代理变量（ZIP 码→种族，毕业年份→年龄）间接歧视。NYC Law 144、California FEHA、Colorado CAIA 和 EU AI Act 的四重法规框架意味着**偏差审计不再是 best practice，而是法律义务**。
- **联邦与州法规碎片化**：California FEHA（2025.10 生效，最严）vs Texas TRAIGA（2026.01 生效，最松）→ Colorado CAIA（2026.06 生效，最全面）。实务建议：按最高标准（California/Colorado）构建合规体系。
- **EU AI Act 的域外效力**：招聘用途被明确归为"高风险"类。2026 年 8 月 2 日为完全执行日。罚款最高 €35M 或全球营业额 7%。
- **卖方责任（Vendor Liability）**：California FEHA 明确"供应商在代理原则下可能承担雇主同等的歧视责任"。采购 AI 招聘工具时，合同必须含偏差审计结果分享、及时通知发现的偏差。
- **候选人数据隐私与同意**：AI sourcing 从 45+ 公开平台抓取候选人数据——FCRA 的新兴法律理论——2026 年 1 月诉讼主张 AI 招聘工具汇总公共数据构成"消费者报告"——可能彻底改变 sourcing 类工具的合规方式。
- **深度伪造与候选人侧 AI 欺诈**：2025-2026 年，候选人使用 AI 辅助面试的现象呈爆发式增长——招聘方开始部署反向 AI 检测工具，形成 AI vs AI 的军备竞赛。
- **裁员偏见与反馈回路**：如果 AI 模型用历史录取数据训练，而历史上的录取决策本身就带有偏见，模型会**强化和放大**这些偏见。

---

## 落地碎片（实践建议）

- 选型第一步是画出你的**招聘量级 × 角色复杂度矩阵**：高量级+低复杂度 → Type IV；高量级+高复杂度 → Type I + Type V；低量级+高复杂度 → AI 工具作用有限，人工猎头为主。
- **数据质量 > 数据库大小**：要求供应商提供**实际使用数据**——email bounce rate、平均回复率、数据平均新鲜度。
- **合规不是事后补丁**：采购前确认：① 供应商是否提供独立偏差审计报告？② 是否支持定期重审计？③ 决策过程是否可解释？④ 是否有明确的人工干预机制？
- **用 pilot 验证，不要用 demo 评估**：用你自己的 20 个真实岗位跑 2 周并行流程。
- **中国市场优先看 Moka 和北森**：Moka 适合招聘量大节奏快的互联网/科技企业；北森适合 500 人以上中大型集团。
- **ATS 深度集成是不可谈判项**：如果你的 AI 招聘工具不能在你现有的 ATS 里"无缝出现"——adoption rate 会在 2 周内跌到零。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

### 本文重点覆盖产品

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| Weekday | I | 专有 250M+ 数据库，99% 联系人准确率，多渠道自主外联，30–50% 回复率，66% fill rate | https://www.weekday.works/ |
| Gem | I/II | 全栈招聘平台（ATS+CRM+Sourcing+Analytics），20+ ATS 集成 | https://www.gem.com/ |
| HireEZ | I | 800M+ 聚合数据库，45+ 平台，Chrome 扩展浏览器内 sourcing | https://hireez.com/ |
| SeekOut | I | 700–750M+ 数据，GitHub/专利/出版物深度搜索，行业最强 DEI 过滤器 | https://seekout.com/ |
| Eightfold AI | III | 人才智能平台，1.5B+ profiles 技能图谱，内部流动性+外部招聘+继任规划 | https://eightfold.ai/ |
| Fetcher | I | 轻量 AI 候选人推荐工具，每日自动推送候选人 | https://fetcher.ai/ |
| Paradox Olivia | IV | 对话式 AI 招聘助手（被 Workday 2025.10 收购），高量级小时工招聘首选 | https://www.paradox.ai/ |
| MokaHR | III | 中国 ATS 招聘专精型平台，97% 简历解析精度；AI Agent 功能上线（2026） | https://mokahr.io/ |
| Humanly | III | 审计就绪型 AI 筛选+互动+排程平台，全证据保留，4.8/5 候选人评分 | https://www.humanly.io/ |
| Skillora | IV | 实时语音 AI 面试师，LiveKit 堆栈，次秒级延迟 | https://skillora.ai/ |

### 品类内其他值得关注的产品

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| Jack & Jill | IV | 对话式 AI 招聘平台（伦敦，$20M 种子轮）；Jack（候选人侧）+ Jill（雇主侧）双智能体 | https://jackandjill.ai/ |
| JuiceBox (PeopleGPT) | I/II | Sequoia + DST Global 投 $80M，800M+ profiles 自然语言搜索，40+ ATS/CRM 集成 | https://juicebox.ai/ |
| Clado | I | AI 人员搜索（"Deep Research for People"），YC S25；**非**面试工具 | https://www.clado.ai/ |
| Carv | II/V | Agentic AI 批量招聘全栈平台；2025.03 收购 Recrubo 扩展全栈 | https://www.carv.com/ |
| Brix | I | AI 跨境招聘 + 工程师众包平台 | https://joinbrix.com/ |
| Moonhub | — | ~~已停运（2025.06）~~——团队被 Salesforce acqui-hire | https://www.moonhub.ai/ |
| Greenhouse | III | 结构化招聘标杆，评分卡+面试套件，DEI 内置 | https://www.greenhouse.com/ |
| Beamery | III | 人才生命周期管理，技能智能+CRM+内部流动 | https://beamery.com/ |
| Findem | I | 属性式 sourcing，职业轨迹评分，3x Lighthouse Award | https://www.findem.ai/ |
| Recruiterflow AIRA | VII | 内嵌 Agent 的招聘管理平台，自动 CRM 更新+通话摘要 | https://recruiterflow.com/ |
| 北森 | VI | 中国一体化 HCM + 人才测评/盘点基因，AI 面试官+全渠道招聘 Agent | https://www.beisen.com/ |
| Mercor | V | AI-native 面试平台，$10B 估值（2025.10） | https://mercor.com/ |
| Pymetrics | V | 游戏化行为评估（偏差友好），软技能匹配 | https://www.pymetrics.ai/ |
| TestGorilla | V | 技能测评平台，300+ 测试模板 | https://www.testgorilla.com/ |
| HackerRank | V | 技术技能评估标杆 | https://www.hackerrank.com/ |
| Textio | III | AI 增强型 JD 撰写与沟通，偏差检测 | https://textio.com/ |
| Manatal | II | 经济型 ATS+AI，$15/用户/月起 | https://www.manatal.com/ |

### 对比与测评（第三方；观点非官方）

- Weekday 的 2026 年 AI Candidate Sourcing Tools 专家排名——当前最系统的英语圈横向对比（需注意其自然倾向于 Weekday）
- HR.com 2025–26 年"Future of Recruitment Technologies"报告——67% 用 AI 生成面试题、65% 写 JD、44% 筛简历
- TechTarget "Top AI recruiting tools and software of 2026"——编辑精选，偏企业采购决策导向
- DLA Piper "Critical audit of NYC's AI hiring law"（2026.01）——NYC Law 144 审计失效后的加严趋势
- AI Journal "Why Voice AI Is Quietly Eating HR Tech"——实时语音 AI 面试师趋势分析

*网摘综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- **市场数据**：TBRC "AI in Talent Acquisition Global Market Report 2026"（$1.60B，18.5% CAGR）；SkyQuest "AI Recruitment Market 2026–2033"（$656M→$1.23B，7.2% CAGR）
- **合规框架**：EU AI Act 正式文本（OJEU，2024.07.12）——2026.08.02 完全执行；NYC DCWP Local Law 144 规则文本 + 2025.12 Comptroller 审计报告
- **中国市场**：MokaHR "Best AI Recruitment Tools in 2026"；什么值得买 "2026年AI招聘选购"
- **学术与行业研究**：NIST AI Risk Management Framework (AI RMF 1.0)；Brookings "Algorithmic bias in hiring"