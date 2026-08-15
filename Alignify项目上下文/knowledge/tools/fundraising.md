# AI Fundraising · 知识块（非线性笔记）

**叙述主词**：**AI fundraising / AI 融资工具**——面向创始人、GP 和非营利筹款人的「找钱→联系→管理→交割」全链路 AI 辅助产品。与 **AI lead generation**（`lead-generation`，侧重 B2B 销售拓客）、**LinkedIn 工具谱系**（`linkedin`）和 **AI recruiting**（`recruiting`，侧重招聘）相邻但**买家问题与验收核心不同**——见下「与相邻 slug 分流」。

**材料范围**：公开网络检索（各产品官网、行业评测博客、YC 目录、科技媒体报道）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/fundraising](https://alignify.co/tools/fundraising) · `/tools/fundraising` · [alignify.co/zh/tools/fundraising](https://alignify.co/zh/tools/fundraising) · `/zh/tools/fundraising` · `content/tools/zh/fundraising.json`、`content/tools/en/fundraising.json` · slug **`fundraising`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#fundraising-tools`](../../keywords/alignify-keywords-tools.md#fundraising-tools)

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`fundraising`（本页）** | **`lead-generation`** | **`linkedin`** | **`recruiting`** |
|------|--------------------------|----------------------|----------------|-----------------|
| **典型买家问题** | 找谁投我、怎么联系、怎么管 pipeline、怎么并表？ | 找谁买我的产品、怎么规模化触达？ | LinkedIn 上的 AI 工具有哪些、合规边界在哪？ | 怎么用 AI 筛简历、约面试？ |
| **交付形态** | 投资人数据库 + CRM + 数据室 + cap table | 潜客数据库 + 邮件序列 + 评分 | 个人品牌 / 销售插件 / 自动化 | ATS + 候选人匹配 + 面试安排 |
| **验收核心** | 匹配准确率、回复率、round close 速度 | SQL 转化率、序列打开率 | 账号安全、合规边界 | 候选人质量、offer 接受率 |
| **易混带** | Lessie 的人脉搜索能力可被用于销售拓客，但产品首页锚定「找投资人」 | — | — | AngelList/Wellfound 跨越融资与招聘两端 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI investor matching / AI 投资人匹配**：用机器学习或 LLM 分析投资人的历史 portfolio、阶段偏好、行业聚焦和近期出手，将创业者与最可能感兴趣的投资者自动配对。与「关键词搜索投资人数据库」的区别在于：AI 匹配考虑**隐性偏好**（如「只投有 ex-Stripe 创始人的团队」）而非仅按行业/阶段标签过滤。
- **Warm introduction pathing / 人脉路径映射**：扫描创业者团队的 email、LinkedIn 和社交图谱，找出「你的二度人脉里有谁认识目标投资人」，从而走 warm intro 而非冷邮件。核心指标是**路径长度**（几度分隔）和**关系强度**（互动频率）。
- **Deal room / 交易室**：带访问分析与权限控制的可分享链接，集中存放 pitch deck、财务模型、尽职调查文件。投资人点击后，创始人可看到**谁看了、看了多久、翻到第几页停止**——这是传统 email 附件无法提供的行为信号。
- **Pipeline management / 融资管道管理**：将投资人按「触达→感兴趣→尽调→谈判→打款」分阶段追踪的 CRM。与传统 CRM 的关键差异在于**自动阶段推进**（如投资人打开 deal room 后自动从「Sent」移入「Engaged」）。
- **SPV / RUV（Special Purpose Vehicle / Roll Up Vehicle）**：将多个小额天使投资人合并为 cap table 上**一行**的法律实体。AI 工具在此的作用是自动生成法律文件、KYC/AML 验证、资金归集。概念上属于**法务基建**而非融资策略。
- **Pitch deck analytics / 融资演示分析**：追踪投资人看 pitch deck 的行为数据（打开率、每页停留时长、回看页面）。AI 增强版可额外做**逐页内容评审**，标注投资人常质疑的薄弱环节（如市场大小未量化、GTM 模糊）。
- **Donor intelligence / 捐赠者智能分析**：非营利领域的 AI 预测分析——从历史捐赠数据中识别**高潜力大额捐赠人**、**流失风险**和**升级时机**。VC 融资领域的对应物是**investor qualification**（投资人资质评分）。
- **Agentic fundraising / 代理式融资**：2026 年新建构——AI agent 不只给建议，而是自动执行多步融资动作（识别投资人→生成个性化邮件→发送→跟踪→推进 pipeline）。Bloomerang Penny、Moore/SimioAccelerate、Blackbaud Development Agent 是此范式的代表。
- **中文圈融资数据平台**：与英文圈 AI 匹配工具不同，国内以 **IT 桔子**（企业/投资事件数据库 + 产业图谱）、**鲸准**（双边交易撮合，3 万+认证机构）、**烯牛数据**（FA/VC/银行/券商/母基金分角色数据洞察）为核心基础设施。这些平台侧重**多维度筛选与智能推荐**而非端到端 AI agent 自动化，触达层仍以微信社群和人工 FA 为主导。

---

## 专题对照 / 扩展定义

本节处理本领域最常见的三类混淆——读完应能判断「当前需求落在哪个格子里」。

### A. 创始人融资 vs 投资人找项目（供需两侧工具对照）

同一品类里同时存在「帮创始人找钱」和「帮 VC 找项目」的工具，检索时极易混为一谈：

| 维度 | **创始人侧（融资端）** | **投资人侧（投资端）** |
|------|----------------------|----------------------|
| **核心问题** | 谁可能投我？怎么联系？ | 哪些创业公司在我的 thesis 内？ |
| **典型工具** | Evalyze、OpenVC、Lessie、Finta、Metal、PropelRx | Harmonic、Affinity、SheetVenture（投资端视角） |
| **验收指标** | 回复率、intro 转化率、close 速度 | 标的发现速度、信号时效性、deal flow 质量 |
| **数据方向** | 从投资人数据库 → 筛选匹配 → 外发 | 从公司数据库 → 信号监测 → 入站 |
| **易混带** | Harmonic 也被创始人用来研究投资人，但产品设计主轴是投资端 | SheetVenture 的「追踪实际 check-writing」对两端都有用 |

### B. 英文圈 AI 匹配 vs 中文圈数据平台（生态差异）

| 维度 | **英文圈 AI Fundraising** | **中文圈融资数据平台** |
|------|--------------------------|---------------------|
| **核心交互** | AI 匹配→个性化邮件→deal room→pipeline | 多维度筛选→项目/机构详情页→一键约谈/微信联系 |
| **数据基础** | Crunchbase、PitchBook、LinkedIn、SEC | IT 桔子、鲸准、烯牛数据 |
| **触达方式** | 冷邮件（email-first） | 微信社群 + 人工 FA 撮合（IM-first） |
| **AI 深度** | Agentic——部分工具已能自动推进 pipeline | 辅助型——智能推荐和筛选，不替代人工撮合 |
| **代表产品** | Lessie、Finta、Metal、Evalyze | IT 桔子、鲸准、烯牛数据 |
| **适用场景** | 面向美元基金 / 全球投资人 | 面向人民币基金 / 国内机构 |
| **迁移风险** | 英文工具的中文投资人数据覆盖弱 | 中文平台不含海外机构深度数据 |

### C. 融资工具 vs 融资准备度工具（何时上工具）

| 维度 | **融资执行工具** | **融资准备度工具** |
|------|----------------|------------------|
| **核心问题** | 我已经准备好，找谁、怎么联系？ | 我是否真的准备好了？ |
| **典型工具** | OpenVC、Lessie、Finta、Metal | PropelRx、SeedBlink CORE、Evalyze（deck 评审功能） |
| **使用时机** | pitch deck 已定稿、数据室就绪 | pitch deck 还在迭代、财务模型未做投资者适配 |
| **典型产出** | 投资人名单、个性化邮件、pipeline 看板 | 准备度评分、逐页 deck 反馈、财务模型差距清单 |
| **建议路径** | 先用准备度工具做 gap check → 修正硬伤 → 再上执行工具 outreach |

---

## 问题域（为何会出现这类产品）

- **冷邮件回复率低于 1%**：传统做法是手动从 Crunchbase 筛名单、写模板邮件、群发后石沉大海。AI 工具试图通过**个性化触达**（引用投资人具体 portfolio 和近期言论）和**warm intro 路径挖掘**解决回复率问题。
- **投资人数据库静态过时**：传统数据库（PitchBook、Crunchbase）存在信息滞后，且只显示「投过什么」而非「现在正在投什么」。SheetVenture、Harmonic 等工具转向实时信号追踪（招聘激增、域名注册、近期 check-writing 记录）。
- **融资是低频高摩擦流程**：多数创始人数年才融一次资，缺乏系统化方法论。Evalyze、PropelRx、SeedBlink CORE 将「融资准备度」拆为可评测的维度，在正式 outreach 前降低结构性硬伤。
- **信息不对称与网络壁垒**：VC 融资史上依赖「你认识谁」。AI 正试图用匹配算法和人脉图谱将这一过程民主化——ThatRound 62% 的 AI 匹配率、OpenVC 的永久免费模式都是此逻辑的产物。
- **多天使并表的法务成本**：种子轮引入 10-30 个天使意味着 cap table 上多出 10-30 行。AngelList Rollups、Allocations 用 AI 和法律自动化将这些人并成一行，降低后续轮次的治理复杂度。
- **非营利筹款的低效手工流程**：多数中小 NGO 仍靠直觉和 Excel 管理捐赠关系。Dataro、Bloomerang Penny 等将预测分析带入这个传统上「重关系、轻数据」的领域。

---

## 能力栈（概念拆分，非厂商功能表）

- **投资人发现**：数据库 vs 实时信号（后者追踪招聘、域名注册、近期 check-writing）。英文圈主要数据源包括 Crunchbase、PitchBook、LinkedIn、SEC filings；中文圈核心数据源为 **IT 桔子**（1732 家 AI Agent 产业链公司 + 3117 起投资事件）、**鲸准**（3 万+认证机构 + 100 万+项目库，偏双边交易撮合）、**烯牛数据**（按 FA/股权投资/银行/证券/母基金五身份入口重构，偏全链条数据洞察）。中文圈工具普遍不以「AI 匹配」为核心卖点，而是提供多维度筛选和智能推荐。
- **匹配与评分**：简单筛选（行业×阶段×地域）→ 规则引擎（多维度加权）→ LLM 语义匹配（理解投资人 thesis 叙述）→ 预测模型（估算投资概率）。层级越高，对训练数据的质量和体量要求越高。
- **联系人获取**：邮箱推测算法（pattern matching → SMTP 验证）、数据库直接提供、LinkedIn 解析。核心指标是**准确率**——95% 是部分厂商的市场宣称（如 Lessie），独立评测显示实战准确率约 80-85%，非英语地区和种子期投资人的退回率更高。
- **触达与个性化**：从「Hi {name}」到引用投资人具体 portfolio 和近期推文/访谈。AI 个性化邮件打开率约 45-65%（Lessie 官方 FAQ 引用的典型区间），远高于通用冷邮件的 15-20%。部分厂商的市场材料宣称 85% 打开率，属最佳情景而非典型结果。
- **人脉图谱**：email 收件箱扫描 → 社交图谱映射 → 二度人脉路径计算。企业级方案（Affinity）还可跨团队成员图谱做并集运算。
- **Pipeline 管理**：阶段推进 + 行为触发自动化 + 团队协作。高端方案（Finta）支持「投资人打开 deal room → 自动推进阶段 → 触发 NLP 生成 follow-up 草稿」。
- **数据室与材料分发**：文档托管 + 逐页访问分析 + 权限控制 + 水印。AI 增强版可标记「投资人在哪页停留最久/最早退出」。
- **法务与交割**：SPV 设立、KYC/AML、cap table 管理、电子签约。AngelList Rollups 和 Allocations 在此层占据主导。
- **投后关系管理**：KPI 追踪看板 → 定期投资人更新 → 后续轮次信号。Visible.vc 在此层定位明确（与「找新投资人」的能力栈不重叠）。

---

## 形态谱系（与具体品牌解耦）

1. **纯匹配型**（Evalyze、Qubit Capital、SheetVenture、OpenVC 基础层）：核心交付是「推荐一份投资人名单」。不做 CRM，不做 outreach，不做数据室。适合有自己 outreach 能力的连续创业者。
2. **人脉搜索型**（Lessie）：核心交付是「找到投资人的联系方式 + 生成个性化邮件」。不管理 pipeline，不追踪 deck 分析。适合需要规模化 cold-but-personalized outreach 的创始团队。
3. **全流程 OS 型**（Finta、Metal）：覆盖从投资人发现→匹配→CRM→数据室→交割的全链路。适合首次融资的 solo founder 或小团队——不需要组合多个单点工具。
4. **企业级关系智能型**（Affinity）：面向**VC/PE 机构**而非个人创始人。核心是自动捕获 email/日历数据构建全机构的关系图谱。$2,000–$2,700/用户/年（年付制，无月付选项），小团队（5-15 人）年费约 $12K–$45K，不适合 3 人以下创业团队。
5. **情报/监测型**（Harmonic）：核心用户是**VC 做 deal sourcing**，而非创始人融资。但创始人也用它研究「哪些 VC 在投我的赛道」。需注意其默认对话界面可能返回投资端视角的信息。
6. **投后管理型**（Visible.vc）：融资**后**工具——KPI 看板、投资人更新、数据室。如果处于「还没找到投资人」阶段，不应作为首要工具。
7. **法务基建型**（AngelList Rollups）：解决的是「融到钱以后」的问题——多天使并表、cap table 管理、KYC/AML。与融资策略工具互补而非替代。
8. **准备度评估型**（PropelRx、SeedBlink CORE）：先评测「你准备好融了吗？」再进入 outreach。8 维度评分、Pitch 教练、AI CFO。适合首次融资或换赛道融资的团队。
9. **非营利捐赠分析型**（Dataro、Bloomerang Penny、DonorSearch AI）：面向 NGO 和公益组织，核心是捐赠人流失预测、大额捐赠人识别、筹款策略生成。

---

## 风险 · 合规 · 数据隐私与治理（外部框架可对照，非法律意见）

- **数据准确性与幻觉**：AI 生成的投资人匹配结果和个性化邮件可能包含**事实错误**（引用已关闭的基金、错误的 portfolio 公司）。Lessie 评测显示约 20% 的「已验证」投资人邮箱可能退回。建议关键 outreach 前人工 double-check。
- **邮箱抓取与反垃圾法**：自动采集投资人邮箱并群发可能违反 CAN-SPAM（美国）、GDPR（欧洲）、PIPL（中国）。个性化 ≠ 非垃圾——各国对「事先同意」标准不同。
- **LinkedIn 爬虫合规**：大多数工具以某种形式依赖 LinkedIn 数据（直接爬取或间接解析）。LinkedIn 的 ToS 明确禁止自动数据采集，hiQ Labs 案确立了一定程度的公共数据爬取合法性（美国法），但欧洲和中国的边界更模糊。
- **敏感信息在第三方平台留存**：上传 pitch deck、财务模型、cap table 至 SaaS 平台意味着核心商业信息在第三方服务器上存储。SOC 2、数据加密、数据驻留（data residency）是基本要求——选型时应要求对方出具合规证明。
- **代理式自动化过头**：2026 年出圈的 agentic fundraising（SimioAccelerate、Blackbaud Development Agent）可能在没有人类审批的情况下**自动发送投资人邮件或执行捐赠人 outreach**。建议始终保持 human-in-the-loop，尤其是大额交易和非营利场景。
- **非营利募资道德风险**：AI 预测「大额捐赠潜力」涉及对个人的财富评估和行为预测，若缺乏透明度可能导致**隐私侵犯**和**信任崩塌**。Bloomerang Penny、Dataro 等平台声称基于公开捐赠数据与行为信号，但具体算法和数据来源需审慎查证。
- **Warm intro 路径的隐私边界**：人脉图谱功能需扫描团队 email 收件箱和社交图谱。团队成员可能不愿让自己的私人人脉暴露于平台。需明确**opt-in 粒度**——「全员开放图谱」vs「仅共享我的联系人」。
- **跨境融资与制裁筛查**：非美国创始人面向美国投资人融资，或反之，涉及 OFAC 制裁名单、CFIUS 审查。AI 工具通常**不会**做制裁筛查——这是法务团队的职责。

---

## 落地碎片（无先后）

- 先判断阶段：**Pre-seed/Seed** → 优先用匹配型 + 人脉搜索型（Lessie、Evalyze、OpenVC）；**Series A+** → 全流程 OS 型（Finta、Metal）；**投后** → Visible.vc。
- 不要同时付费订阅 3+ 个融资工具——投资人联系人库高度重叠，差异主要在 UX 和 AI 匹配算法。
- AI 生成的投资人邮件**必须人工修改**——直接粘贴发送违背「个性化」初衷，且 AI 常引用错误的 portfolio 公司。
- 将 pitch deck 上传至数据室前，确认平台**是否将文档纳入 AI 训练集**。这在服务条款中通常以模糊语言表述，必要时发邮件确认。
- 人脉图谱开之前先和团队对齐——「谁愿意共享联系人」vs「谁要保护个人隐私」。大团队建议只开创始人的图谱。
- 非营利组织选型时优先看**捐赠数据所有权**——你是否能随时导出完整亲本数据迁移？Dataro、Bloomerang 在此维度区别明显。
- 中国境内的融资工具生态以 IT 桔子（数据洞察+产业图谱）、鲸准（双边撮合+一键约谈）、烯牛数据（全链条数据洞察，按 FA/投资/银行/证券/母基金五身份入口）为数据基础，以微信社群和人工 FA 为触达渠道——与英文圈「AI 匹配→个性化邮件→deal room」的工具逻辑和触达方式不同，不应直接平移方法论。

## 选型速查（按创始人场景）

| 你现在的状态 | 优先看 | 理由 |
|-------------|--------|------|
| 完全不知道从哪开始，deck 还没定稿 | PropelRx / SeedBlink CORE / Evalyze | 先诊断准备度，再 outreach |
| deck 已有，需要一份投资人名单 | OpenVC（免费）/ Evalyze / SheetVenture | 纯匹配型，零门槛起步 |
| 有名单但没有联系方式 | Lessie | 人脉搜索 + 邮箱挖掘专用 |
| 有联系方式但不知道怎么写出高回复率邮件 | Lessie + Finta | Lessie 生成个性化邮件，Finta 管 pipeline |
| 第一次融资，需要一站式工具 | Finta / Metal | 全流程 OS，不拼装多个工具 |
| 已有多个天使要并表（融后） | AngelList Rollups | 法务基建，与融资策略工具互补 |
| 已融完，需要管投资人关系 | Visible.vc | 投后 KPI 看板 + 定期更新 |
| 面向国内人民币基金 | IT 桔子 / 鲸准 + 人工 FA | 中文圈不走 email outreach 逻辑 |
| 面向美元基金 / 全球投资人 | OpenVC + Lessie + Finta 组合 | 英文圈 AI 工具链完整 |

---

## 工具与产品类型（「AI fundraising」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 面向谁 | 备注 |
|----------------------|--------------|--------|------|
| **AI investor matching** | 算法推荐投资人名单、匹配评分 | 创始人 | 与「投资人数据库」（无AI）相邻但不同 |
| **People search / contact finder** | 邮箱推测、个性化 cold email 生成 | 创始人、销售 | Lessie 可跨场景使用，但主阵地锚定融资 |
| **Fundraising CRM / deal room** | Pipeline 管理、数据室、cap table | 创始人、GP | Finta 为全流程 OS 代表 |
| **Relationship intelligence** | email/日历图谱、warm intro 映射 | VC/PE 机构 | Affinity ~$2,000/用户/年，小团队年费 $12K+ |
| **Deal sourcing intelligence** | 创业公司发现、实时信号追踪 | VC/PE 机构 | Harmonic 为代表 |
| **Post-raise IR / investor updates** | KPI 看板、定期投资人更新 | 已融资创业者 | Visible.vc，不要与「找投资人」混淆 |
| **Donor intelligence** | 捐赠人预测分析、流失预警 | 非营利组织 | Dataro、Bloomerang Penny |
| **Grant writing AI** | AI 资助提案撰写、资助方匹配 | 非营利、科研机构 | Grantboost、Bonterra Grantmaker |
| **Crowdfunding AI** | 众筹活动创建优化、捐赠人触达 | 个人 / 组织 | GoFundMe AI Coach、Wadiz WAi |
| **SPV / cap table infra** | 多天使并表、KYC/AML | 已融资创始人 | AngelList Rollups、Allocations |
| **Pitch deck AI** | AI 生成/评审 pitch deck，模拟投资人问答 | 创始人（准备材料阶段） | PitchBob、checkmypitch、Ada Deck Genius；与融资执行工具互补 |

---

## 外链索引

### 初创企业 VC 融资工具

| 名称 | 一句话 | URL |
|------|--------|-----|
| Lessie | AI 人脉搜索引擎，5000 万投资人档案 + 95% 合伙人邮箱准确率 + 个性化邮件生成 | https://lessie.ai/investor-scouting |
| Harmonic | AI 创业情报平台，跟踪 3500 万公司 + 1.95 亿人，VC 端 deal sourcing 为主 | https://harmonic.ai/ |
| Evalyze | AI 投资人匹配 + 逐页 pitch deck 评审，基于 8000+ 成功案例训练 | https://www.evalyze.ai/ |
| OpenVC | 免费融资平台，20000+ 投资人 + 内置 CRM + deck 追踪分析 | https://www.openvc.app/ |
| Finta | AI 融资 OS（Aurora Agent），CRM + deal room + 人脉图谱 + cap table | https://www.trustfinta.com/ |
| Metal | YC W23 + a16z 支持，AI 投资者匹配 + warm intro 路径映射 + Round Coach | https://www.metal.so/ |
| PropelRx | 融资准备度评估 + AI CFO + Pitch 教练 + 投资人发现 Agent | https://propelrx.com/ |
| SeedBlink CORE | 欧洲数字融资副驾驶，pitch 评审 + Spotlight 档案 + 72 小时开轮 | https://seedblink.com/ |
| SheetVenture | 30000+ 活跃投资人实时数据库，仅追踪近 18 月实际 check-writing 的机构 | https://sheetventure.com/ |
| Qubit Capital | AI 创业-投资人撮合，已促成 $215M 融资，全球覆盖 | https://qubit.capital/ |
| ThatRound | 英国 AI 融资市场，62% AI 匹配获投资人主动 intro，500+ 创始人在用 | https://thatround.com/ |
| Raizer | 55000+ VC/天使数据库 + AI 匹配评分 + 个性化邮件（raizer.app） | https://raizer.app/ |
| Angel Match | 110000+ 天使/VC/PE 数据库 + 内置 CRM | https://www.angelmatch.io/ |

### Pitch Deck 创建与评审

| 名称 | 一句话 | URL |
|------|--------|-----|
| PitchBob | AI 副驾驶：pitch deck + one-pager + business plan + VC 式辅导 | https://pitchbob.io/ |
| checkmypitch | AI pitch deck 逐页分析 + 硅谷 VC 分析师级反馈 | https://checkmypitch.com/ |
| Ada Deck Genius | Ada Ventures 免费 AI 工具，slide-by-slide VC 级 deck 反馈（3 维度评审） | https://www.adaventures.com/ |

### 企业级 / 投资端工具

| 名称 | 一句话 | URL |
|------|--------|-----|
| Affinity | 关系智能 CRM，自动捕获 email/日历数据构建全机构关系图谱 | https://www.affinity.co/ |
| AngelList / Rollups | SPV + cap table + KYC/AML，$171B 资产在平台，RUV 将天使并成一行 | https://www.angellist.com/ |

### 投后管理

| 名称 | 一句话 | URL |
|------|--------|-----|
| Visible.vc | 投资人关系管理，KPI 看板 + 定期更新 + 数据室 + deck 逐页分析 | https://visible.vc/ |

### 非营利筹款

| 名称 | 一句话 | URL |
|------|--------|-----|
| Dataro | AI 捐赠者智能分析，300+ 组织使用，$14.28M A 轮 | https://dataro.io/ |
| Bloomerang Penny | 首个 AI 筹款策略师，基于数千真实咨询案例训练 | https://bloomerang.com/ |
| Moore × Microsoft SimioAccelerate | Agentic 筹款平台（Azure），AI 代理自动化全流程：洞察→内容→多渠道执行 | https://wearemoore.com/simioaccelerate |
| Blackbaud Raiser's Edge NXT | Development Agent + AI Chat + Cultivation Assistant | https://www.blackbaud.com/ |
| Avid | 首个 AI 筹款操作系统，$6.5M 种子轮（Silverton Partners 领投） | https://www.avidai.com/ |
| Kindora | Claude 三模型驱动（Sonnet/Opus/Haiku），328 非营利 + 2x 月增，$100K 首年自筹验证 | https://www.kindora.co/ |

### 资助写作

| 名称 | 一句话 | URL |
|------|--------|-----|
| Grantboost | #1 AI 资助写作平台，定制提案 + 提交管理 | https://www.grantboost.com/ |
| Bonterra Grantmaker | AI 原生资助管理平台，智能匹配 + 自动评分 | https://www.bonterra.com/ |

### 中文圈融资数据平台

| 名称 | 一句话 | URL |
|------|--------|-----|
| IT 桔子 | 创投数据平台，1732 家 AI Agent 产业链公司 + 3117 起投资事件 + 机构偏好分析 | https://www.itjuzi.com/ |
| 鲸准 | 3 万+认证机构 + 100 万+项目库，AI 双边撮合 + 一键约谈投资人 | https://www.jingdata.com/ |
| 烯牛数据 | AI 智能商业数据，按 FA/投资/银行/证券/母基金五身份入口，全链条洞察 | https://www.xiniudata.com/ |

### 众筹

| 名称 | 一句话 | URL |
|------|--------|-----|
| GoFundMe AI Coach | AI 辅助全流程众筹创建，预计带来 $1.25 亿增量 | https://www.gofundme.com/ |
| Wadiz WAi | 韩国众筹 AI Agent，基于 90000+ 项目训练，实时建议 | https://www.wadiz.kr/ |

### 对比与测评（第三方；观点非官方）

- **Vynta AI 2026 指南**：系统性对比 10 款 AI 融资平台（含 Harmonic、Affinity、DonorSearch AI、Bloomerang、Fundraise Up、Gravyty 等），侧重投资人匹配转化率和 ROI 框架（https://vynta.ai/blog/top-ai-powered-fundraising-platforms/）
- **极客公园 Lessie 评测**：中文深度评测，评分 7.8/10——指出小众地区数据弱、信用消耗不透明（3-5 积分/人）、约 20% 邮箱可退回、无原生 CRM 同步。建议 50% 熟人引荐 + 50% 精准冷邮件平衡策略（https://w.geekpark.net/news/354516）
- **AI Founder Kit Lessie 独立测试**：14 天 Growth 计划实测——15-20% 邮箱"陈旧"（6 个月内换工作）、20% 种子投资人邮箱退回、15% 活跃 Gmail 被误标"风险"。结论：自然语言搜索体验优于传统工具，但 email 准确率未达厂商宣称水平（https://aifounderkit.com/ai-tools/lessie-ai-people-search/）
- **ToolMage 2026 年度榜单**：按用户点赞排序的 AI fundraising 工具目录，覆盖 VC 融资、非营利、Pitch Deck 等全品类（https://www.toolmage.com/en/tag/fundraising/?sort=likes&type=website）
- **Funraise 2026 非营利工具大全**：108+ 非营利 tech tools 汇总，按功能分类，含 AI 和传统工具对比（https://funraise.org/blog/top-tech-tools-for-nonprofits）
- **Dataro「Four Levels of AI Adoption」框架**：Level 1 基础 chat 起草 → Level 2 带数据上下文的 chat → Level 3 生成 HTML/PDF → Level 4 构建他人可用的工具——适用于评估非营利组织 AI 采用深度（https://dataro.io/blog/build-fundraising-tools-with-ai）

---

## 延伸阅读与参考材料

- ThatRound 融资公告（2026-05）：产品定位、AI 匹配逻辑与 UK 市场数据（[barchart.com](https://www.barchart.com/story/news/1775854/thatround-closes-pre-seed-funding-round-to-improve-startup-fundraising-in-the-uk)）
- Evalyze 产品发布（2025-12）：AI 匹配引擎的 pitch deck 评审方法论（[markets.businessinsider.com](https://markets.businessinsider.com/news/stocks/evalyze-launches-ai-investor-matching-engine-to-help-startups-fundraise-faster-1035623223)）
- AngelList Rollups 2026 分析：Allocations 对比 SPV 选型指南，含定价拆解（[allocations.com](https://www.allocations.com/blog/angellist-founder-spv-vs.-allocations-founder-spv-which-is-right-for-your-startup-in-2026)）
- LangChain × Harmonic 案例：Harmonic Scout AI Agent 的技术架构（[langchain.com](https://www.langchain.com/blog/customers-harmonic)）
- 烯牛数据 2025 AI 投融资全景：2025 年 AI 融资破 2000 起、占整体市场 17%、具身智能同比增长 3 倍（[jixin.tech](https://jixin.tech/mobile/show.php?classid=1&id=6729)）
- IT 桔子 AI Agent 产业全景洞察（2026-05）：1732 家公司 + 3117 起投资事件的结构化图谱（[itjuzi.com](https://www.itjuzi.com/industry_ai_agent)）
- AI Founder Kit Lessie 独立评测（7.8/10）：信用消耗、邮箱准确率、实际使用体验的详细记录（[aifounderkit.com](https://aifounderkit.com/ai-tools/lessie-ai-people-search/)）
