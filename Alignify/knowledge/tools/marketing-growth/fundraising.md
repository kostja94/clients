# AI Fundraising · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI fundraising / AI 融资工具**——面向创始人、GP 和非营利筹款人的「找钱→联系→管理→交割」全链路 AI 辅助产品；验收以**匹配准确率、回复率、round close 速度**为主。本页为 **融资工具 SSOT**（完整 URL 表仅此一处）；B2B 销售拓客 → [lead-generation.md](lead-generation.md)；LinkedIn 工具 → [linkedin.md](../hr-recruiting/linkedin.md)；招聘 → [recruiting.md](../hr-recruiting/recruiting.md)。

**材料范围**：公开网络检索（各产品官网、行业评测博客、YC 目录、科技媒体报道）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/fundraising](https://alignify.co/tools/fundraising) · `/tools/fundraising` · [alignify.co/zh/tools/fundraising](https://alignify.co/zh/tools/fundraising) · `/zh/tools/fundraising` · `content/tools/zh/fundraising.md`、`content/tools/en/fundraising.md` · slug **`fundraising`**

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

- **AI investor matching / AI 投资人匹配**：用机器学习或 LLM 分析投资人的历史 portfolio、阶段偏好、行业聚焦和近期出手，将创业者与最可能感兴趣的投资者自动配对。与「关键词搜索投资人数据库」的区别在于：AI 匹配考虑**隐性偏好**而非仅按行业/阶段标签过滤。
- **Warm introduction pathing / 人脉路径映射**：扫描创业者团队的 email、LinkedIn 和社交图谱，找出「你的二度人脉里有谁认识目标投资人」，从而走 warm intro 而非冷邮件。
- **Deal room / 交易室**：带访问分析与权限控制的可分享链接，集中存放 pitch deck、财务模型、尽职调查文件。投资人点击后，创始人可看到**谁看了、看了多久、翻到第几页停止**。
- **Pipeline management / 融资管道管理**：将投资人按「触达→感兴趣→尽调→谈判→打款」分阶段追踪的 CRM。与传统 CRM 的关键差异在于**自动阶段推进**（如投资人打开 deal room 后自动从「Sent」移入「Engaged」）。
- **SPV / RUV（Special Purpose Vehicle / Roll Up Vehicle）**：将多个小额天使投资人合并为 cap table 上**一行**的法律实体。AI 工具在此的作用是自动生成法律文件、KYC/AML 验证、资金归集。
- **Pitch deck analytics / 融资演示分析**：追踪投资人看 pitch deck 的行为数据（打开率、每页停留时长、回看页面）。AI 增强版可额外做**逐页内容评审**。
- **Donor intelligence / 捐赠者智能分析**：非营利领域的 AI 预测分析——从历史捐赠数据中识别**高潜力大额捐赠人**、**流失风险**和**升级时机**。
- **Agentic fundraising / 代理式融资**：2026 年新建构——AI agent 不只给建议，而是自动执行多步融资动作（识别投资人→生成个性化邮件→发送→跟踪→推进 pipeline）。Bloomerang Penny、Moore/SimioAccelerate、Blackbaud Development Agent 是此范式的代表。
- **中文圈融资数据平台**：与英文圈 AI 匹配工具不同，国内以 **IT 桔子**、**鲸准**、**烯牛数据**为核心基础设施——侧重**多维度筛选与智能推荐**而非端到端 AI agent 自动化，触达层仍以微信社群和人工 FA 为主导。

---

## 专题对照 / 扩展定义

本节处理本领域最常见的三类混淆——读完应能判断「当前需求落在哪个格子里」。产品规格 → **§外链索引**；形态路线 → **§形态谱系**。

### A. 创始人融资 vs 投资人找项目（供需两侧）

| 维度 | **创始人侧（融资端）** | **投资人侧（投资端）** |
|------|----------------------|----------------------|
| **核心问题** | 谁可能投我？怎么联系？ | 哪些创业公司在我的 thesis 内？ |
| **典型工具** | Evalyze、OpenVC、Lessie、Finta、Metal | Harmonic、Affinity、SheetVenture |
| **验收指标** | 回复率、intro 转化率、close 速度 | 标的发现速度、信号时效性、deal flow 质量 |
| **易混带** | Harmonic 也被创始人用来研究投资人，但产品设计主轴是投资端 | SheetVenture 的「追踪实际 check-writing」对两端都有用 |

### B. 英文圈 AI 匹配 vs 中文圈数据平台

| 维度 | **英文圈 AI Fundraising** | **中文圈融资数据平台** |
|------|--------------------------|---------------------|
| **核心交互** | AI 匹配→个性化邮件→deal room→pipeline | 多维度筛选→项目/机构详情页→一键约谈/微信联系 |
| **触达方式** | 冷邮件（email-first） | 微信社群 + 人工 FA 撮合（IM-first） |
| **AI 深度** | Agentic——部分工具已能自动推进 pipeline | 辅助型——智能推荐和筛选，不替代人工撮合 |
| **代表产品** | Lessie、Finta、Metal、Evalyze | IT 桔子、鲸准、烯牛数据 |
| **迁移风险** | 英文工具的中文投资人数据覆盖弱 | 中文平台不含海外机构深度数据 |

### C. 融资工具 vs 融资准备度工具

| 维度 | **融资执行工具** | **融资准备度工具** |
|------|----------------|------------------|
| **核心问题** | 我已经准备好，找谁、怎么联系？ | 我是否真的准备好了？ |
| **典型工具** | OpenVC、Lessie、Finta、Metal | PropelRx、SeedBlink CORE、Evalyze（deck 评审功能） |
| **使用时机** | pitch deck 已定稿、数据室就绪 | pitch deck 还在迭代、财务模型未做投资者适配 |
| **建议路径** | 先用准备度工具做 gap check → 修正硬伤 → 再上执行工具 outreach |

---

## 问题域（为何会出现这类产品）

- **冷邮件回复率低于 1%**：AI 工具试图通过**个性化触达**和**warm intro 路径挖掘**解决回复率问题。
- **投资人数据库静态过时**：传统数据库（PitchBook、Crunchbase）存在信息滞后，且只显示「投过什么」而非「现在正在投什么」。SheetVenture、Harmonic 等工具转向实时信号追踪。
- **融资是低频高摩擦流程**：Evalyze、PropelRx、SeedBlink CORE 将「融资准备度」拆为可评测的维度，在正式 outreach 前降低结构性硬伤。
- **信息不对称与网络壁垒**：ThatRound 62% 的 AI 匹配率、OpenVC 的永久免费模式都是试图民主化 VC 融资网络。
- **多天使并表的法务成本**：AngelList Rollups、Allocations 用 AI 和法律自动化将多天使并成一行。
- **非营利筹款的低效手工流程**：Dataro、Bloomerang Penny 等将预测分析带入传统上「重关系、轻数据」的领域。

---

## 能力栈（概念拆分，非厂商功能表）

- **投资人发现**：数据库 vs 实时信号（后者追踪招聘、域名注册、近期 check-writing）。英文圈数据源包括 Crunchbase、PitchBook、LinkedIn、SEC filings；中文圈核心数据源为 IT 桔子、鲸准、烯牛数据（具体数据点见 §外链索引 **中文圈融资数据平台**）。
- **匹配与评分**：简单筛选 → 规则引擎 → LLM 语义匹配 → 预测模型。层级越高，对训练数据的质量和体量要求越高。
- **联系人获取**：邮箱推测算法、数据库直接提供、LinkedIn 解析。核心指标是**准确率**——独立评测显示实战准确率约 80-85%（Lessie，见 §外链索引「对比与测评」），非英语地区和种子期投资人的退回率更高。
- **触达与个性化**：从「Hi {name}」到引用投资人具体 portfolio 和近期言论。AI 个性化邮件打开率约 45-65%（Lessie 官方 FAQ 引用的典型区间），远高于通用冷邮件的 15-20%。
- **人脉图谱**：email 收件箱扫描 → 社交图谱映射 → 二度人脉路径计算。企业级方案（Affinity）还可跨团队成员图谱做并集运算。
- **Pipeline 管理**：阶段推进 + 行为触发自动化 + 团队协作。高端方案（Finta）支持「投资人打开 deal room → 自动推进阶段 → 触发 NLP 生成 follow-up 草稿」。
- **数据室与材料分发**：文档托管 + 逐页访问分析 + 权限控制 + 水印。
- **法务与交割**：SPV 设立、KYC/AML、cap table 管理、电子签约。AngelList Rollups 和 Allocations 在此层占据主导。
- **投后关系管理**：KPI 追踪看板 → 定期投资人更新 → 后续轮次信号。Visible.vc 在此层定位明确。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 纯匹配型：推荐投资人名单，不做 CRM/outreach | AI investor matching | Evalyze、OpenVC、SheetVenture |
| **B** | 人脉搜索型：联系方式 + 个性化 cold email | People search / contact finder | Lessie |
| **C** | 全流程 OS：发现→匹配→CRM→数据室→交割 | Fundraising CRM / deal room | Finta、Metal |
| **D** | 企业级关系智能：email/日历图谱，面向 VC/PE | Relationship intelligence | Affinity |
| **E** | 情报/监测型：VC deal sourcing，创始人亦可用 | Deal sourcing intelligence | Harmonic |
| **F** | 投后管理型：KPI 看板、定期更新 | Post-raise IR | Visible.vc |
| **G** | 法务基建型：多天使并表、KYC/AML | SPV / cap table infra | AngelList Rollups、Allocations |
| **H** | 准备度评估型：先评测「你准备好融了吗？」 | Fundraising readiness | PropelRx、SeedBlink CORE |
| **I** | 非营利捐赠分析型 | Donor intelligence | Dataro、Bloomerang Penny |

---

## 风险 · 合规 · 数据隐私与治理（外部框架可对照，非法律意见）

- **数据准确性与幻觉**：AI 生成的投资人匹配结果和个性化邮件可能包含**事实错误**。Lessie 评测显示约 20% 的「已验证」投资人邮箱可能退回——关键 outreach 前人工 double-check。
- **邮箱抓取与反垃圾法**：自动采集投资人邮箱并群发可能违反 CAN-SPAM（美国）、GDPR（欧洲）、PIPL（中国）。
- **LinkedIn 爬虫合规**：LinkedIn 的 ToS 明确禁止自动数据采集，hiQ Labs 案确立了一定程度的公共数据爬取合法性（美国法），但欧洲和中国的边界更模糊。
- **敏感信息在第三方平台留存**：上传 pitch deck、财务模型、cap table 至 SaaS 平台——SOC 2、数据加密、数据驻留是基本要求。
- **代理式自动化过头**：2026 年出圈的 agentic fundraising 可能在没有人类审批的情况下**自动发送投资人邮件**——建议始终保持 human-in-the-loop。
- **非营利募资道德风险**：AI 预测「大额捐赠潜力」涉及对个人的财富评估和行为预测，若缺乏透明度可能导致**隐私侵犯**和**信任崩塌**。
- **Warm intro 路径的隐私边界**：人脉图谱功能需扫描团队 email 收件箱和社交图谱——需明确 **opt-in 粒度**。
- **跨境融资与制裁筛查**：AI 工具通常**不会**做制裁筛查——这是法务团队的职责。

---

## 落地碎片（无先后）

- 先判断阶段：**Pre-seed/Seed** → Type A + B（Lessie、Evalyze、OpenVC）；**Series A+** → Type C（Finta、Metal）；**投后** → Type F（Visible.vc）。
- 不要同时付费订阅 3+ 个融资工具——投资人联系人库高度重叠，差异主要在 UX 和 AI 匹配算法。
- AI 生成的投资人邮件**必须人工修改**——直接粘贴发送违背「个性化」初衷，且 AI 常引用错误的 portfolio 公司。
- 将 pitch deck 上传至数据室前，确认平台**是否将文档纳入 AI 训练集**。
- 人脉图谱开之前先和团队对齐——「谁愿意共享联系人」vs「谁要保护个人隐私」。
- 非营利组织选型时优先看**捐赠数据所有权**——你是否能随时导出完整亲本数据迁移？
- 中国境内的融资工具生态以 IT 桔子、鲸准、烯牛数据为数据基础，以微信社群和人工 FA 为触达渠道——与英文圈「AI 匹配→个性化邮件→deal room」的逻辑不同，不应直接平移方法论。

### 选型速查（按创始人场景）

| 你现在的状态 | 优先看 | 理由 |
|-------------|--------|------|
| deck 还没定稿 | PropelRx / SeedBlink CORE / Evalyze | 先诊断准备度（Type H） |
| deck 已有，需要投资人名单 | OpenVC（免费）/ Evalyze / SheetVenture | Type A，零门槛起步 |
| 有名单但没有联系方式 | Lessie | Type B |
| 第一次融资，需要一站式 | Finta / Metal | Type C |
| 已有多个天使要并表 | AngelList Rollups | Type G |
| 已融完，需要管投资人关系 | Visible.vc | Type F |
| 面向国内人民币基金 | IT 桔子 / 鲸准 + 人工 FA | 中文圈 IM-first |
| 面向美元基金 / 全球投资人 | OpenVC + Lessie + Finta 组合 | 英文圈 AI 工具链 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

### 初创企业 VC 融资工具

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| Lessie | B | AI 人脉搜索引擎，5000 万投资人档案 + 95% 合伙人邮箱准确率 + 个性化邮件生成 | https://lessie.ai/investor-scouting |
| Harmonic | E | AI 创业情报平台，跟踪 3500 万公司 + 1.95 亿人，VC 端 deal sourcing 为主 | https://harmonic.ai/ |
| Evalyze | A/H | AI 投资人匹配 + 逐页 pitch deck 评审，基于 8000+ 成功案例训练 | https://www.evalyze.ai/ |
| OpenVC | A | 免费融资平台，20000+ 投资人 + 内置 CRM + deck 追踪分析 | https://www.openvc.app/ |
| Finta | C | AI 融资 OS（Aurora Agent），CRM + deal room + 人脉图谱 + cap table | https://www.trustfinta.com/ |
| Metal | C | YC W23 + a16z 支持，AI 投资者匹配 + warm intro 路径映射 + Round Coach | https://www.metal.so/ |
| PropelRx | H | 融资准备度评估 + AI CFO + Pitch 教练 + 投资人发现 Agent | https://propelrx.com/ |
| SeedBlink CORE | H | 欧洲数字融资副驾驶，pitch 评审 + Spotlight 档案 + 72 小时开轮 | https://seedblink.com/ |
| SheetVenture | A | 30000+ 活跃投资人实时数据库，仅追踪近 18 月实际 check-writing 的机构 | https://sheetventure.com/ |
| Qubit Capital | A | AI 创业-投资人撮合，已促成 $215M 融资 | https://qubit.capital/ |
| ThatRound | A | 英国 AI 融资市场，62% AI 匹配获投资人主动 intro | https://thatround.com/ |
| Raizer | A | 55000+ VC/天使数据库 + AI 匹配评分 + 个性化邮件 | https://raizer.app/ |
| Angel Match | A | 110000+ 天使/VC/PE 数据库 + 内置 CRM | https://www.angelmatch.io/ |

### Pitch Deck 创建与评审

| 名称 | 一句话 | URL |
|------|--------|-----|
| PitchBob | AI 副驾驶：pitch deck + one-pager + business plan + VC 式辅导 | https://pitchbob.io/ |
| checkmypitch | AI pitch deck 逐页分析 + 硅谷 VC 分析师级反馈 | https://checkmypitch.com/ |
| Ada Deck Genius | Ada Ventures 免费 AI 工具，slide-by-slide VC 级 deck 反馈 | https://www.adaventures.com/ |

### 企业级 / 投资端 / 投后 / 非营利 / 中文圈

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| Affinity | D | 关系智能 CRM，自动捕获 email/日历数据构建全机构关系图谱，~$2,000/用户/年 | https://www.affinity.co/ |
| AngelList / Rollups | G | SPV + cap table + KYC/AML，$171B 资产在平台 | https://www.angellist.com/ |
| Visible.vc | F | 投资人关系管理，KPI 看板 + 定期更新 + 数据室 | https://visible.vc/ |
| Dataro | I | AI 捐赠者智能分析，300+ 组织使用，$14.28M A 轮 | https://dataro.io/ |
| Bloomerang Penny | I | 首个 AI 筹款策略师，基于数千真实咨询案例训练 | https://bloomerang.com/ |
| Moore × Microsoft SimioAccelerate | I | Agentic 筹款平台（Azure），AI 代理自动化全流程 | https://wearemoore.com/simioaccelerate |
| Blackbaud Raiser's Edge NXT | I | Development Agent + AI Chat + Cultivation Assistant | https://www.blackbaud.com/ |
| Avid | I | 首个 AI 筹款操作系统，$6.5M 种子轮 | https://www.avidai.com/ |
| Kindora | I | Claude 三模型驱动，328 非营利 + 2x 月增 | https://www.kindora.co/ |
| Grantboost | — | #1 AI 资助写作平台，定制提案 + 提交管理 | https://www.grantboost.com/ |
| Bonterra Grantmaker | — | AI 原生资助管理平台，智能匹配 + 自动评分 | https://www.bonterra.com/ |
| IT 桔子 | — | 创投数据平台，1732 家 AI Agent 产业链公司 + 3117 起投资事件 | https://www.itjuzi.com/ |
| 鲸准 | — | 3 万+认证机构 + 100 万+项目库，AI 双边撮合 + 一键约谈 | https://www.jingdata.com/ |
| 烯牛数据 | — | 按 FA/投资/银行/证券/母基金五身份入口，全链条洞察 | https://www.xiniudata.com/ |
| GoFundMe AI Coach | — | AI 辅助全流程众筹创建，预计带来 $1.25 亿增量 | https://www.gofundme.com/ |
| Wadiz WAi | — | 韩国众筹 AI Agent，基于 90000+ 项目训练 | https://www.wadiz.kr/ |

### 对比与测评（第三方；观点非官方）

- **Vynta AI 2026 指南**：系统性对比 10 款 AI 融资平台，侧重投资人匹配转化率和 ROI 框架
- **极客公园 Lessie 评测**：评分 7.8/10——指出小众地区数据弱、信用消耗不透明、约 20% 邮箱可退回、无原生 CRM 同步
- **AI Founder Kit Lessie 独立测试**：14 天 Growth 计划实测——15-20% 邮箱「陈旧」、20% 种子投资人邮箱退回
- **Dataro「Four Levels of AI Adoption」框架**：Level 1 基础 chat → Level 4 构建他人可用的工具——适用于评估非营利组织 AI 采用深度

*网摘综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- ThatRound 融资公告（2026-05）：产品定位、AI 匹配逻辑与 UK 市场数据
- Evalyze 产品发布（2025-12）：AI 匹配引擎的 pitch deck 评审方法论
- AngelList Rollups 2026 分析：Allocations 对比 SPV 选型指南
- LangChain × Harmonic 案例：Harmonic Scout AI Agent 的技术架构
- 烯牛数据 2025 AI 投融资全景：2025 年 AI 融资破 2000 起、占整体市场 17%
- IT 桔子 AI Agent 产业全景洞察（2026-05）：1732 家公司 + 3117 起投资事件的结构化图谱