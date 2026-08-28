# Advertising Agent · 知识块（非线性笔记）

**叙述主词**：**Advertising Agent / AI 广告投放 Agent**——以 AI Agent 形态自主/半自主管理付费广告全生命周期的系统，涵盖策略诊断→受众定向→创意生成→跨平台投放→实时出价优化→效果归因的端到端闭环。与单点广告工具（创意生成、Spy 情报、追踪器、联盟平台）的核心分界在于：Advertising Agent 是「AI 替你管广告账户」，单点工具是「AI 帮你做广告里某一件具体的事」。

**材料范围**：公开网络检索（Albert.ai / Smartly.io / Madgicx / Hyper / Ryze AI / Synter / Percuity / Hawky / Navos Agent / Omni-Growth Agent 等厂商官网、G2 社区评分、HyperFX 2026 评测排行、Omniconvert 对比报告、AI-Ready CMO 工具对比、CSDN Multi-Agent 投放案例、36Kr 出海营销分析）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-07-01**。

**站内对照**：待上线 Blog 正式页时与 slug **`advertising-agent`**、`content/blog/en|zh/advertising-agent.md` 对齐（新文走 `/blog`，见 [README.md §路由与发布策略](./README.md#路由与发布策略2026-06)）。

**Tools 关键词与意图**：归属「企业销售与营销」Territory，与 `affiliate-marketing`、`b2b`、`lead-generation`、`influencer-marketing` 相邻——面向品牌方增长负责人、电商运营和代理商的技术选型知识。

## 与相邻 slug 分流（企业销售与营销集群）

| 维度 | **`advertising-agent`（本页）** | **`affiliate-marketing`** | **`b2b`** | **`lead-generation`** |
|------|-------------------------------|---------------------------|-----------|----------------------|
| **买家问题** | 「能不能用 AI Agent 替我 7×24 管广告？」 | 「怎么用 AI 管理和放大联盟推广项目？」 | 「AI 如何提升整个 B2B 营销管线？」 | 「怎么用 AI 找到更多高质量销售线索？」 |
| **核心交付** | AI 自主执行广告投放——策略→创意→出价→优化→归因闭环 | 联盟项目管理——追踪、佣金结算、推广者招募 | B2B 销售与营销全栈——数据→触达→分析 | 潜客发现、验证、富集 |
| **自主程度** | **高自主**——Agent 自动调整出价、暂停低效广告、重分配预算 | 低自主——工具辅助人管联盟项目 | 中低自主——AI 辅助但策略决策由人做 | 低自主——工具辅助人找线索 |
| **典型工具** | Albert.ai, Smartly.io, Madgicx, Hyper | Rewardful, Tolt, Voluum, Spy.House | Apollo, Demandbase, 6sense | Apollo, Lusha, Hunter.io, Clay |
| **不与…混买** | 广告创意生成工具（AdCreative.ai）、广告追踪器（Voluum）、广告情报（Spy.House）——这些是「单点广告工具」而非 Agent | 广告创意生成工具（AdCreative.ai 等——联盟营销领域会用到，但非联盟管理平台） | CRM、邮件序列工具（Instantly/Outreach——b2b 页覆盖） | 广告投放 Agent 本身 |

## 专题对照：Advertising Agent vs 单点广告工具（易混品类）

> 这是本知识块最重要的品类分界——市场上大量产品都叫「AI 广告工具」，但「Agent 替你管账户」和「工具帮你做广告里某一件事」是两种完全不同的采购决策。

| 维度 | **Advertising Agent** | **广告创意 AI 工具** | **广告追踪/归因工具** | **广告情报 Spy 工具** |
|------|----------------------|---------------------|---------------------|---------------------|
| **核心问题** | 「谁能替我 7×24 管广告？」 | 「谁能帮我做广告图/视频？」 | 「哪个渠道/素材带来了转化？」 | 「竞争对手在投什么？」 |
| **工作方式** | 连接广告账户 API，自主决策+执行 | 输入 brief→输出素材，不连接广告账户 | 追踪点击→落地页→转化漏斗 | 抓取广告库，索引素材和 offer |
| **是否管账户** | **是**——读/写广告账户，调整出价/预算/状态 | 否——产出文件/URL 交给人上传 | 否——只追踪不执行 | 否——只读不写 |
| **典型代表** | Albert.ai, Madgicx, Hyper | AdCreative.ai, Arcads, Jasper | Voluum, RedTrack, AnyTrack | Spy.House, AdPlexity, BigSpy |
| **采购者** | 品牌方增长负责人、电商运营、代理商 | 创意团队、设计师、media buyer | media buyer、效果营销团队 | media buyer、联盟推广者 |
| **在本知识库的归属** | **本页** | [ugc.md](ugc.md)（AI UGC / 创意生成主谱系）；联盟交叉见 [affiliate-marketing.md](affiliate-marketing.md) | [affiliate-marketing.md](affiliate-marketing.md) §媒体采买追踪器型 | [affiliate-marketing.md](affiliate-marketing.md) §Spy 广告情报型 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Advertising Agent / AI 广告投放 Agent**：在本文中专指以 AI Agent 形态连接广告平台 API、自主执行广告全生命周期的系统。与「AI 广告工具」（泛指所有带 AI 的广告相关软件）的核心差异在于**自主决策 + 账户写入**——不止分析或推荐，而是真正操作广告账户（调整出价、暂停广告、重分配预算、创建新 Campaign）。英文社区常以「autonomous ad agent」「AI media buying agent」「agentic advertising」指代。
- **Agentic Advertising / 智能体驱动广告投放**：区别于传统「广告管理平台」（如 Facebook Ads Manager、Google Ads 后台，人类手动操作）、「规则型自动化」（如 Revealbot 的 if-then 规则）和「平台原生 AI」（Meta Advantage+、Google AI Max，平台自带黑盒优化）。Agentic Advertising 强调：(a) 跨平台统一操作、(b) 白盒化决策可审计、(c) 自主目标驱动（给定 ROAS/CPA 目标，Agent 自主规划执行路径）。
- **Autonomous vs Advisory / 全自主 vs 顾问式**：该品类的关键二分——全自主型 Agent 无需人工审批即执行操作（Albert.ai、Hyper）；顾问式 Agent 每日分析账户 → 生成建议列表 → 人类审批后执行（Madgicx 的 AI Marketer、Omni-Growth Agent 的 HITL 模式）。选型时这是第一个要回答的问题：「愿意放权到什么程度？」
- **Campaign Lifecycle Automation / 广告全生命周期自动化**：从「策略诊断 → 受众定向 → 创意生成 → 多平台投放 → 实时出价优化 → A/B 测试 → 效果归因 → 预算重分配」的端到端闭环。不是所有 Agent 都覆盖全周期——Smartly.io 强于创意生产，Albert.ai 强于跨渠道买量，Madgicx 强于 Meta 生态内优化。
- **Human-in-the-Loop (HITL) / 人机协作**：Agent 做分析+建议，人在关键节点审批执行。这是 2026 年多数产品的主流模式——平衡自主性与风险控制的中间态。与全自主模式的选择通常取决于：月投放预算量级、行业监管要求、团队对 AI 的信任度。
- **Platform-native AI vs Agent Overlay / 平台原生 AI vs Agent 叠加层**：Meta Advantage+、Google AI Max、TikTok GMV Max 是平台自带的 AI 优化能力——在单平台内效果强但不可跨平台、不可审计、不可定制。Advertising Agent 作为叠加层跨越多个广告平台，统一策略和归因——代价是需要通过 API 间接操作，不如平台原生 AI 深度集成。2026 年最佳实践通常是「平台原生 AI 做单平台底层优化 + Agent 做跨平台策略协同」的组合。

---

## 问题域（为何会出现这类产品）

- **广告平台数量膨胀使人工管理不可持续**：2026 年一个典型 DTC 品牌可能同时在 Meta、Google、TikTok、Pinterest、Snapchat、Reddit、Amazon 七个平台投放——每个平台有独立的 Ads Manager、独立的出价逻辑、独立的归因模型。人工跨平台协调出价和预算分配已超出单个优化师的认知负荷。
- **广告平台的 AI 化倒逼广告主也 AI 化**：Meta Advantage+ 和 Google AI Max 将广告优化从「人调参数」变为「AI 黑盒调控」——广告主面临的新问题是「我的 AI 怎么跟平台的 AI 博弈？」Advertising Agent 的出现是对平台 AI 化的对称回应。
- **创意消耗速度远超人类生产能力**：一个优化师每周手工做 5-10 套新素材已是极限——但 2026 年 Meta 推荐每周 20+ 创意变体、TikTok 推荐每天 3-5 条新视频。Agent 批量生成和测试创意变体是刚需。
- **归因碎片化催生跨平台统一视角需求**：iOS ATT、Safari ITP、第三方 cookie 消亡使得单平台归因越来越不可靠——品牌方需要一个跨平台的统一归因视图和策略层，这是 Agent 的天然优势（跨越围墙花园）。
- **优化师人才成本高且流失快**：一个有经验的广告优化师年薪 $80K-150K，跳槽周期 12-18 个月——每次人员变动意味着广告账户的「知识断档」。Agent 把投放知识留在系统里而非人脑里，是应对人员流失的防御性投资。
- **LLM 在多步推理和工具调用上的成熟**：2025-2026 年，LLM 的能力从「写好一条广告文案」进化到「理解一个广告账户的全部数据→诊断问题→规划多步优化方案→通过 API 执行」——这是 Advertising Agent 可行性的技术临界点。

---

## 能力栈（概念拆分，非厂商功能表）

- **全域诊断与策略规划层**：Agent 在操作账户之前先进行全局诊断——分析品牌增长阶段（冷启动/放量/盈利优化）、各渠道角色（搜索捕获意图 vs 社交创造需求 vs 再营销收割）、预算分配合理性。Omni-Growth Agent 的「先全域诊断，后渠道执行」是本层最有方法论特色的实现。进阶形态：机会发现引擎——Hellyeah 扫描 1,284+ 跨渠道信号，按预期价值排序，主动向人推荐下一增长动作（如「Reddit r/devtools CPM 仅为 Meta 的 1/4，CPA 预估 $3.10」）。非 Agent 类工具不具备此层——它们把渠道当孤立单元操作。
- **受众定向与人群智能层**：Agent 自主创建和管理受众——包括 Lookalike/类似受众、Custom Audience 上传、再营销受众圈选、跨平台受众同步。Amazon Ads Agent 可自动从数万个人群中筛选最优组合。与平台原生受众工具的差异：Agent 可以在不同平台间迁移「哪些人群特征在 A 平台有效、在 B 平台是否值得测试」的经验。
- **创意生成与批量测试层**：Agent 自动生成广告文案、图片、视频变体——基于品牌素材 + 历史高转化创意特征 + 平台最佳实践。Smartly.io 的 Predict Studio 是创意 Agent 的标杆——批量生成数百个变体并自动测试。注意：独立的 AdCreative.ai / Arcads 也做创意生成，但它们不管理广告账户——创意生成是 Agent 的能力栈之一，而非全部。
- **跨平台投放与 Campaign 管理层**：Agent 通过官方 Marketing API 创建、管理、暂停、复制 Campaign/Ad Set/Ad——在多个广告平台之间统一操作。Hawky 和 Synter 在这一层做了深入的 API 限频保护和防封号机制——直接让裸 LLM 操作广告 API 极容易触发平台风控。
- **实时出价与预算动态分配层**：Agent 基于 CPA/ROAS 目标实时调整出价——发现低效广告自动暂停或降低预算，将预算重分配给高转化广告——跨 Campaign、跨 Ad Set、乃至跨平台。这是 Agent 区别于「分析工具」的最核心能力——它不仅分析，它还把钱挪过去。Albert.ai 和 Hyper 在这一层以全自主执行著称。
- **效果归因与跨平台分析层**：Agent 整合多平台数据，提供统一的 ROAS/CPA 视图——区别于单平台归因。部分 Agent（Percuity、Ryze AI）内置报告自动生成——从「人花 3 小时做周报」变成「Agent 自动生成 + 人审阅 10 分钟」。差异化趋势：增长记忆（Growth Memory）——Hellyeah 将每次循环的结果写入持久记忆，新 Campaign 继承历史胜出经验，实现 ROAS 的跨循环复合增长（同一预算下从 1.2× 提升到 4.1×）。多数 Agent 目前不具备跨 Campaign 记忆传承能力。
- **异常检测与风险预警层**：Agent 7×24 监控广告账户——发现成本突增、转化骤降、受众疲劳、平台拒审、预算超支等异常时自动告警或自动干预。Omni-Growth Agent 的三层预算保护（双转化追踪 + 实时止损 + 冷启动保护）是本层较系统的安全设计。

---

## 形态谱系（与具体品牌解耦）

- **全自主跨平台 Agent（Fully Autonomous Cross-Platform）**：Agent 连接多个广告平台 API，设定 ROAS/CPA 目标后自主执行全链路操作——创建 Campaign、调整出价、暂停低效广告、跨平台重分配预算——不需人工逐项审批。适合月投放 $50K+、有多平台需求的品牌。代表模式：Albert.ai（2018 年起步，金融/保险行业标杆）、Hyper（2026 年 HyperFX 评测 9.7/10 排名第一）。
- **顾问式单平台 Agent（Advisory Platform-Specific）**：Agent 每日深度分析单个广告账户，生成具体操作建议（「暂停这个 Ad Set」「给这个 Campaign 加 20% 预算」「测试这组新受众」），由人类审批后一键执行。模式优势：风险可控、适合对 AI 放权持谨慎态度的团队。代表模式：Madgicx（Meta 专用，$44/月起，AI Marketer 每日诊断）。
- **创意优先 Agent（Creative-First Agent）**：以批量创意生产 + 自动化测试为核心差异化——Agent 的核心价值不在出价优化，而在「用 AI 替代创意团队的重复性产出」。通常面向企业级品牌（月投放 $100K+）。代表模式：Smartly.io Predict Studio（企业级创意编排，数百变体自动测试）。
- **Campaign 启动与管理 Agent（Launch & Manage Agent）**：以将广告快速推到线上为核心场景——从落地页 URL 出发，Agent 自动分析业务、生成创意、创建 Campaign 并上线——面向无专职优化师的中小企业或代理商。代表模式：Hawky（Agentic Launch，批量推创意到 Meta/Google）、Percuity（"Leo" AI Agent，$229/月包 $50K 投放额度）。
- **MCP 开放协议 Agent（MCP-Native Agent）**：将广告投放能力封装为 MCP Server——任何支持 MCP 的 AI 助手（Claude Desktop、Cursor 等）都可以连接并操控广告账户。面向技术团队和「用 AI 工作流替代 SaaS」的早期采用者。代表模式：Synter（开放 MCP 协议 + Python/JS SDK + 40+ Agent Skills，覆盖 20+ 广告平台）。
- **平台原生 AI Agent（Platform-Native）**：广告平台自带的 AI Agent——亚马逊的 Ads Agent 是最典型的例子（免费、自然语言操作、降低 CPM 和 CPA）。Meta Advantage+ / Google AI Max / TikTok GMV Max 也属于此范畴但更偏向「自动化功能」而非「对话式 Agent」。优势是免费且与平台深度集成——代价是只在该平台内有效、不可审计、不可跨平台协同。
- **出海/全域营销 Agent（Outbound / Global Marketing Agent）**：面向中国企业出海场景——不仅管广告投放，还整合竞品分析、市场洞察、多语言本地化、跨媒体矩阵管理。与海外 Agent 的核心差异：① 中文原生界面和支持 ② 深度整合中国出海常用渠道 ③ 定价更灵活（效果分润模式）。代表模式：Navos Agent（钛动科技，策略+创意+投放+分析四引擎）、Omni-Growth Agent（神策团队，HITL 全域诊断）。
- **CLI-First 增长引擎（Growth Engine / CLI-Native Agent）**：以命令行（CLI/SDK）为一级交互界面的全栈增长 Agent——不仅管广告投放，还覆盖 SEO/GEO、生命周期自动化、红人营销、落地页 A/B 测试。核心差异化：(a) 增长记忆（Growth Memory）跨 Campaign 持久学习——ROAS 从第 1 周 1.2× 复合增长到第 12 周 4.1×；(b) 机会发现引擎——扫描数千信号，自动推荐下一增长动作；(c) 可嵌入 CI/CD 流水线——`npm install` 即用，面向增长工程师和 AI-native 团队。代表模式：Hellyeah（Research→Create→Launch→Learn 四原语循环，覆盖 Meta/Google/TikTok/Reddit/Klaviyo 等）。

---

## 风险 · 合规 · 账户安全与信任（外部框架可对照，非法律意见）

- **广告账户被封风险是行业第一杀手**：将广告账户的 API 密钥交给第三方 Agent，意味着该 Agent 的每一次 API 调用都在消耗平台的「信任额度」——频率过高、操作过快、生成内容触发审核都会导致账户被标记乃至封禁。Hawky 的策略是「批处理和限频，远离平台风控红线」——选型时应要求厂商明确说明 API 限频策略和账户安全机制。
- **全自主执行的不可逆风险**：一旦 Agent 获得「不经审批直接调整出价/预算」的权限——错误决策的代价可能是数万美元/小时。Albert.ai 和 Hyper 的全自主模式在大型账户上有长期验证记录，但中小企业如果月预算仅 $5K，一个错误出价可能消耗掉一周预算。多数厂商推荐从 HITL（人审批执行）模式开始，逐步建立信任后再提升自主性。
- **跨平台归因的「围墙花园」问题**：每个广告平台都有自己的归因模型——Meta 归因偏向 Meta，Google 归因偏向 Google。Agent 声称的「统一归因」实际上只能做近似估算——选型时需问清楚「你们的统一 ROAS 是怎么算的？用了什么归因模型？」
- **创意合规与平台审核风险**：Agent 自动生成的广告文案和视频可能触及平台的内容审核红线（夸大宣传、受限品类、版权素材）——一旦拒审量过大，账户健康度下降。这是 Agent 创意生成层的安全短板——部分 Agent 已内置「预审合规检查」功能，但覆盖面参差不齐。
- **数据隐私与跨平台数据聚合**：Agent 需要聚合多个平台的广告数据、转化数据乃至 CRM 数据——这意味着 GDPR/CCPA 合规边界大幅扩展。自托管部署或私有化方案是数据敏感企业的首选路径。Omni-Growth Agent 强调「通过 Google OAuth 2.0 标准授权，不存储密码」——这是合规的最低基线。
- **LLM 幻觉在广告场景的独特风险**：Agent 可能「幻觉」出不存在的广告指标、错误放大「看起来有效但实际是虚假转化」的模式、或者在效果差时「编造」一个看似合理的解释。Madgicx 的「AI Marketer 给建议→人审→执行」模式是降低幻觉风险的务实中间态——人始终是最后一道防线。
- **效果归因的道德风险**：Agent 厂商的商业模式与广告投放效果深度绑定——部分 Agent 采用「按广告花费比例收费」或「按增量 ROAS 分润」，这需要独立第三方验证基线。Omni-Growth Agent 的「基线算法公开可审计」和 Percuity 的「$229 固定月费不挂钩花费」是两种不同的利益对齐策略——前者透明但需信任方法论，后者简单但可能缺乏激励。

---

## 落地碎片（无先后）

- 先回答「放权程度」——这是选型的第一决策点：如果团队对 AI 管理广告有信任顾虑，从 Madgicx 或 Omni-Growth Agent 的 HITL 模式开始；如果已经有成熟的投放 SOP 且愿意尝试全自主，从 Albert.ai 或 Hyper 开始。不是「越自主越好」——匹配团队的信任度和投放体量最重要。
- 月投放预算 < $10K 的团队：直接用平台原生 AI（Meta Advantage+ / Google AI Max）通常已足够——引入第三方 Agent 的额外费用（$44-$499/月）可能不如把预算直接投在广告上。或者在 Madgicx ($44/月) 和 Ryze AI（免费试用）之间选一个轻量方案起步。
- 月投放预算 $10K-$50K 的团队：这是 Agent ROI 最明显的区间——人工优化师的成本（年薪 $60-120K）vs Agent 订阅费（$44-$499/月）的差距最大。Hawky（批量推创意+管理）、Percuity（$229 包 $50K 投放额度）是这个区间的典型选择。
- 月投放预算 $50K+ 的团队：考虑「Agent 组合」而非「一个 Agent 做所有」——例如 Madgicx 管 Meta 创意优化 + Albert.ai 或 Hyper 做跨平台预算调度。企业级品牌可评估 Smartly.io 的创意编排能力。技术团队可关注 Hellyeah——CLI-first 可嵌入 CI/CD，且增长记忆使每次循环比前一次更智能。
- 出海场景的特别考量：如果主要投放市场在海外但团队在中国——Omni-Growth Agent 和 Navos Agent 提供原生中文支持和出海渠道适配。海外 Agent（Albert.ai / Madgicx / Hyper）的功能更深但缺乏中文服务——如果团队没有英文投放经验，出海 Agent 是更务实的起点。
- 评估时的关键测试：(1) 让 Agent 对一个真实的历史账户做"事后诊断"——它能否发现当时人没发现的问题？(2) 让 Agent 生成一套广告建议——在审批前，你的优化师是否认可这些建议的质量？(3) 检查 API 限频和账户安全机制——如果没有明确说明，是红旗。
- 不要期望 Agent 完全替代优化师——2026 年的现实是：Agent 替代 60-80% 的重复性操作（盯盘、调出价、生成报表、批量做素材变体），但策略层判断（进入新市场、品牌定位、大促策略）仍需要人类优化师和增长负责人的决策。Agent 是「超级助理」，不是「完全替代」。

---

## 工具与产品类型（「AI advertising agent」「autonomous ad management」「AI media buying」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| Fully Autonomous Cross-Platform Agent | Albert.ai, Hyper | 跨 Google/Meta/TikTok/LinkedIn 等多平台，全自主执行，不需人工逐项审批 |
| Advisory Platform-Specific Agent | Madgicx (Meta), Revealbot (Meta/Google/Snap) | 每日诊断+建议，人工审批后执行；风险更可控 |
| Creative-First Enterprise Agent | Smartly.io Predict Studio | 以批量创意生产+测试为核心，面向企业级品牌 |
| Launch & Manage Agent (SMB-friendly) | Hawky, Percuity, Ryze AI | 快速上线+日常管理，面向中小企业或代理商 |
| MCP-Native / Developer-First Agent | Synter | 开放 MCP 协议+SDK，面向技术团队的自定义工作流 |
| Platform-Native AI Agent | Amazon Ads Agent, Meta Advantage+, Google AI Max, TikTok GMV Max | 平台自带，免费，不可跨平台，不可审计 |
| Outbound / Global Marketing Agent | Navos Agent, Omni-Growth Agent, 通投互动 | 面向中国出海企业，中文原生，效果分润定价 |
| CLI-First Growth Engine | Hellyeah | CLI/SDK 一级界面，四原语循环，增长记忆跨循环复合 |

---

## 外链索引（公开可获得；非广告、无排序优先级）

### 全自主跨平台 Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Albert.ai** | 全自主跨渠道媒体买量平台，2018 年起步，金融/保险/企业级标杆，不需人工审批 | https://albert.ai/ |
| **Hyper** | 2026 年 HyperFX 评测 #1（9.7/10），跨 Meta/Google/TikTok/LinkedIn/Amazon 全自主 Agent | https://www.hyperfx.ai/ |

### 顾问式单平台 Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Madgicx** | Meta 专用 AI 广告优化，AI Marketer 每日诊断+建议，$44/月起，DTC 电商标杆 | https://madgicx.com/ |
| **Revealbot** | Meta/Google/Snap 自动化规则引擎 + AI 建议，$99/月起，适合需要精细控制的高级用户 | https://revealbot.com/ |

### 创意优先企业级 Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Smartly.io** | 企业级创意编排+投放自动化，Predict Studio 批量生成数百创意变体并自动测试 | https://www.smartly.io/ |

### Campaign 启动与管理 Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Percuity** | 自主广告 Agent「Leo」——策略→创意→投放→优化闭环，$229/月包 $50K 投放额度，覆盖 Meta/Google/LinkedIn/TikTok/Reddit | https://percuity.ai/ |
| **Hawky** | Agentic Launch + Campaign Control——批量生成创意直接推送到 Meta/Google 账户，官方 Marketing API，防封号限频 | https://hawky.ai/ |
| **Ryze AI** | 广告+SEO+网站三合一 Agent，据说平均 ROAS 4.2x，覆盖 Google/Meta/TikTok/LinkedIn | https://get-ryze.ai/ |

### MCP / 开发者优先 Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Synter** | 覆盖 20+ 广告平台的 Agent 操作器，开放 MCP 协议+Python/JS SDK+40+ Agent Skills，面向技术团队 | https://syntermedia.ai/ |

### 平台原生 AI Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Amazon Ads Agent** | 亚马逊官方 AI 广告 Agent，自然语言操作，免费，降低 CPM 和 CPA，面向 AMC/DSP 广告主 | https://advertising.amazon.com/solutions/products/ads-agent |

### 出海/全域营销 Agent

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Navos Agent** | 钛动科技，策略+创意+投放+分析四引擎闭环，1000+ 广告活动验证，面向出海品牌 | https://www.navosagent.ai/ |
| **Omni-Growth Agent** | 神策团队，HITL 人机协作，「先全域诊断后渠道执行」，$49/月起+效果分润，三层预算保护 | https://omni-growth.ai/ |

### CLI-First 增长引擎

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Hellyeah** | CLI-first AI 增长引擎——`npm install` 即用，Research→Create→Launch→Learn 四原语循环，覆盖 Meta/Google/TikTok/Reddit/Klaviyo 等，增长记忆（Growth Memory）使 ROAS 从第 1 周 1.2× 复合增长至第 12 周 4.1×，案例含 Final Round AI ($12M ARR) / Viggle (#2 App Store) / Fish Audio (340% MoM)，自带预算上限+审批门+可回滚 | https://hellyeahai.com/ |

### 对比与测评（第三方；观点非官方）

- HyperFX（2026-06）：12 平台 Meta Ads AI Agents 排名——Hyper 9.7/10、Madgicx Cortex 9.1/10、Ryze AI 8.8/10、Smartly.io 8.5/10、Albert.ai 8.0/10。HyperFX 非独立第三方（Hyper 自己排第一），但评测维度（自主程度、跨平台支持、创意能力）可作为选型框架参考 — https://www.hyperfx.ai/blog/best-meta-ads-ai-agents-2026
- Omniconvert（2026）：Albert.ai vs Madgicx vs Nexus 三方对比——Albert 全自主跨渠道、Madgicx 顾问式 Meta 专精。关键洞察：「全自主 vs 顾问式不是优劣之分，而是放权程度和组织信任度的匹配」 — https://www.omniconvert.com/nexus/compare/albert-ai-vs-madgicx/
- AI-Ready CMO（2026）：Albert AI vs Smartly.io 对比——Albert 替人做决策，Smartly 增强人的能力。两个完全不同的设计哲学 — https://hub.aireadycmo.com/tools/compare/albert-ai-vs-smartly-io
- CSDN AI Agent 社区（2026）：企业级 Multi-Agent 智能营销投放系统落地案例拆解——7 个 Agent 协同完成全链路自动化（年 5 亿投放预算验证） — https://agent.csdn.net/6a17f02010ee7a33f27605d9.html
- 36Kr（2026-06）：出海 2026——AI 在红人营销、精准投放、独立站电商三大场景渗透率分别达 73%/85%/70% — https://m.36kr.com/p/3629148508505088

### 市场数据

- G2 AI Advertising 品类（2026）：Albert.ai、Smartly.io、Madgicx 三家占据主要评分量 — https://www.g2.com/categories/ai-advertising
- Research & Markets（2025）：AI in Marketing 市场 2024 $21.9B → 2030 $107.4B，30.4% CAGR——Advertising Agent 是其中增速最快的子领域之一

### 能力相邻知识块

- [affiliate-marketing.md](affiliate-marketing.md)（联盟营销——含广告创意 AI 工具、广告追踪器、Spy 广告情报）
- [b2b.md](b2b.md)（B2B 营销全栈——含 ABM 程序化广告投放）
- [lead-generation.md](lead-generation.md)（潜客发现——广告投放的下游转化场景）
- [influencer-marketing.md](influencer-marketing.md)（红人营销——替代性营销渠道）
- [ugc.md](ugc.md)（UGC / AI UGC 素材层——Agent 上游创意供给）
- [short-drama.md](../video/short-drama.md)（AI 短剧——含投流变现分析）
- [multi-agent.md](../agent/multi-agent.md)（多智能体系统——Advertising Agent 常采用 Multi-Agent 架构）
