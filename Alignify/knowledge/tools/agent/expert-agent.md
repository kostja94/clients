# AI Expert Agent · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Expert Agent / 专家网络与 AI Agent 市场**——让 AI 扮演特定领域专家、连接人类专家或售卖专家训练的 AI 数字员工；验收以**供给形态（人的时间 vs 人的判断力 vs Agent 产出）、Expert-in-the-loop 与匹配速度**为主。本页为 **Expert Network 产品 SSOT**（完整 URL 表仅此一处）；技能生态 → [agent-skills.md](agent-skills.md)；多 Agent 编排 → [multi-agent.md](multi-agent.md)。

**材料范围**：公开网络检索（厂商官网、Crunchbase/TechCrunch 融资新闻、G2/Capterra 评测、社区讨论摘要）；SuperMem 产品资料来自客户本地文档（`customer/demo/supermem/`）。**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页 · slug **`expert-agent`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#expert-agent-tools`](../../keywords/alignify-keywords-tools.md#expert-agent-tools)

**站内相邻**：[agent-skills.md](agent-skills.md) · [multi-agent.md](multi-agent.md) · [agent-for-desktop.md](agent-for-desktop.md)

---

## 与相邻 slug 分流

| 维度 | **`expert-agent`（本页）** | **`agent-skills`** | **`multi-agent`** |
|------|---------------------------|---------------------|-------------------|
| **典型买家问题** | 「怎么让 AI 扮演特定领域的专家？」 | 「Agent 怎么扩展能力？」 | 「多 Agent 怎么分工？」 |
| **核心能力** | 领域知识注入、角色扮演、垂直场景深耕 | MCP 工具接入、技能生态 | Agent 编排与任务路由 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Expert network / 专家网络**：连接企业客户与行业专家的双边平台——传统模式（GLG、Guidepoint、AlphaSights）以人工匹配为核心，年订阅 $50K-150K+。2025-2026 年品类正经历两条裂变路径：AI 驱动的专家匹配（Ethos、NewtonX）和专家训练的 AI Agent 市场（SuperMem、Fractional OS）。
- **Expert-in-the-loop / 专家在环**：SuperMem 的核心差异化叙事——AI Agent 执行工作任务，但关键决策点需人类专家或用户审批后才生效。MDisrupt 在医疗 AI 领域将此项产品化为 Health Expert in the Loop™——4,000+ 临床专家参与 AI 模型训练、幻觉检测和边缘案例测试。
- **AI agent marketplace / AI Agent 市场**：连接人类专家**训练的 AI Agent**——用户雇佣的不是专家的时间，而是封装了专家知识的 AI 数字员工。代表：SuperMem、Fractional OS、CMOAI。
- **AI-powered expert matching / AI 驱动专家匹配**：用 AI 替代传统专家网络中的人工匹配环节——Ethos 用语音 Agent 对专家进行深度访谈并自动匹配机会；NewtonX 用机器学习实时扫描专业人群。
- **Fractional expert / 分形专家**：以兼职或项目制方式为企业提供高管级专业服务的专家。Paro 和 Toptal 是此模式的先发者；2026 年市场约 $9.4B，预计 2034 年达 $24.7B。
- **Digital employee / 数字员工**：SuperMem 的产品定位词——不是 SaaS 工具，不是 chatbot，而是由专家训练、可被"雇佣"来完成实际工作的 AI 实体。

---

## 专题对照 / 扩展定义

**Expert Network 品类内部三分**（术语见 §词汇锚点；形态 Type 见 §形态谱系；产品规格见 §外链索引）：

| 维度 | **传统专家网络（Type A）** | **AI 驱动专家匹配（Type B）** | **AI Agent 市场（Type C）** |
|------|--------------------------|------------------------------|----------------------------|
| **供给端** | 人类专家（预审数据库） | 人类专家（AI 实时匹配） | 专家训练的 AI Agent |
| **匹配方式** | 人工调研员筛选 | AI 语音访谈 + 多维信号匹配 | 专家将知识封装为 Skill/Agent |
| **交付物** | 电话咨询、调查报告 | 电话咨询、AI 训练数据、项目 | Agent 自主产出（计划/分析/工作流） |
| **审批机制** | 无（全靠专家专业度） | 无 | Expert-in-the-loop |
| **定价模型** | 年订阅 $50K-150K+ | 按项目或订阅 | 平台抽成（Agent 25%/真人 5%）或订阅 |
| **代表产品** | GLG, Guidepoint, AlphaSights | Ethos, NewtonX, CleverX, Inex One | SuperMem, Fractional OS, CMOAI |

---

## 问题域（为何会出现这类产品）

- **专家时间无法规模化**：AI Agent 市场试图用「封装专家知识的 Agent」突破物理限制——一个专家的知识可同时服务 100 家企业。这是品类从「卖时间」到「卖判断力」的范式转换。
- **传统专家网络的匹配效率瓶颈**：GLG/Guidepoint 的人工调研员筛选需要 24-72 小时——而 Ethos 的 AI 语音 Agent 可同时访谈数万名专家并实时匹配。
- **CV 是专家能力的糟糕代理**：Ethos 用 AI 语音访谈和多维信号（论文、代码、播客、社交）重建专家画像。
- **企业需要专家判断力但雇不起全职**：中小企业和初创公司需要顶级 CMO/CFO/CTO 的判断力但无法承担 $400K+ 的年薪。
- **AI 取代执行，但无法取代判断**：Expert-in-the-loop 解决了 AI 执行 80% 工作量、人类在关键节点审批的矛盾。

---

## 能力栈（概念拆分，非厂商功能表）

- **专家画像与发现层**：传统 CV 数据库 vs AI 深度访谈 + 公开作品抓取 vs 专家知识转化为 Skill/Agent。
- **匹配与路由层**：人工调研员筛选 vs NLP/语义匹配自动路由——匹配精度与速度（分钟 vs 天）。
- **交付与产出层**：通话时间/书面报告 vs Agent 自主产出计划/分析/工作流——两种完全不同的质量保障模型。
- **审批与治理层（仅 AI Agent 市场有）**：Expert-in-the-loop 的审批粒度与审批人（供给端专家 vs 需求端用户）。
- **集成与上下文层**：连接器层（Google Suite、Notion 等）与结构化记忆——上下文深度决定 Agent 产出相关性上限。
- **市场与交易层**：供给端准入、定价（抽成 vs 订阅 vs 按次）、纠纷处理、质量评级。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 预建专家数据库，人工调研员匹配，年订阅制 | Legacy expert network | GLG、Guidepoint、AlphaSights、Third Bridge |
| **B** | AI 替代人工匹配；语音 Agent 访谈、实时语义匹配 | AI-powered expert matching | Ethos、NewtonX、CleverX |
| **C** | 售卖封装专家知识的 AI 数字员工；Expert-in-the-loop | Expert-trained agent marketplace | SuperMem、Fractional OS、CMOAI |
| **D** | 按需雇佣兼职高管——真人交付 | Fractional expert platform | Paro、Toptal |
| **E** | 面向受监管行业的专家审批基础设施 | Vertical expert-in-the-loop | MDisrupt |
| **F** | 聚合多个专家网络供给让客户比价 | Marketplace aggregator | Inex One |

**Type C vs D**：C 为 **Agent 替代低复杂度工作**；D 为 **真人分形高管**——2026 年尚互补，C 正从下往上吞噬 D 的部分场景。

---

## 风险 · 合规 · 专家信任与 AI 幻觉（外部框架可对照，非法律意见）

- **AI Agent 产出质量的问责链**：策略失败时责任归属于平台、训练 Agent 的专家、审批专家还是客户——法律灰色地带。
- **专家身份验证与 AI 生成假专家**：AI 语音访谈能否有效区分真实专家和 AI 生成的虚假身份。
- **Expert-in-the-loop 的「审批疲劳」风险**：AI Agent 每天生成大量产出等专家审批——审批质量随疲劳而下降。
- **AI Agent 输出的幻觉与合规**：Fundraising Agent 场景下错误的法律条款可能导致数百万美元损失。
- **数据隐私与跨客户知识污染**：Agent 从一个客户学习后如何确保知识不「泄露」到另一客户。

---

## 落地碎片（无先后）

- 选型时先判断你需要的是「人的判断力」还是「AI 的效率」：前者走 Type A/B；后者走 Type C。
- 核心痛点是「需要顶尖 CMO/CFO 但雇不起全职」→ 先试 Type D，再评估 Type C 能否覆盖低复杂度工作。
- 受监管行业（医疗、金融、法律）构建 AI → Type E 是合规必需品。
- 评估 AI Agent 市场产品时，用真实工作场景测试 Agent 产出——关键测试：产出是否需要你重做 50% 以上。
- 传统专家网络年订阅 $50K-150K 壁垒正在被按需模式瓦解——年咨询量少于 20 次不要签年度订阅。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **SuperMem** | C | 专家训练 AI Agent 市场，5 类 Agent，Expert-in-the-loop；平台抽成真人 5%/Agent 25% | https://www.supermem.io/ |
| **Ethos** | B | AI 驱动专家匹配，语音 Agent 深度访谈；$22.75M a16z 领投（2026-05）；35K 专家/周 | https://askethos.com/ |
| **GLG** | A | 全球最大专家网络，900K+ 专家，年订阅 $50K-150K+ | https://glginsights.com/ |
| **Guidepoint** | A | 1M+ 专家，灵活定价 $20K-80K+ | https://www.guidepoint.com/ |
| **AlphaSights** | A | 速度最快的传统专家网络，AI 辅助搜索，小时级匹配 | https://www.alphasights.com/ |
| **Third Bridge** | A | 1.5M 专家，Forum 深度访谈记录，PE/并购尽调首选 | https://www.thirdbridge.com/ |
| **Tegus** | A | 200K+ 专家通话记录 + AI 搜索（AskTegus）；2024 与 AlphaSense 合并 | https://www.tegus.com/ |
| **NewtonX** | B | AI 实时扫描匹配，无固定数据库，ML 驱动合规监控 | https://www.newtonx.com/ |
| **Fractional OS** | C | 专家训练 AI Agent 订阅市场，$97-$4,497/月 | https://www.fractionalos.com/ |
| **MDisrupt** | E | 医疗 AI 专家在环平台，4,000+ 临床专家 | https://www.mdisrupt.com/ |
| **Inex One** | F | 专家网络聚合竞价平台 | https://www.inex.one/ |
| **CleverX** | B | AI 驱动 B2B 研究 + 用户研究 + AI 训练数据 | https://cleverx.com/ |
| **Paro** | D | 分形财务专家平台，<2% 接受率 | https://www.paro.com/ |
| **Toptal** | D | Top 3% 人才市场，14 天试用 | https://www.toptal.com/ |

### 对比与测评（第三方；观点非官方）

2025-2026 年专家网络赛道正在经历分裂：**传统专家网络卖人的时间，AI Agent 市场卖人的判断力**。GLG 的 900K+ 专家不是任何 AI 初创公司能在 12 个月内复制的防御壁垒。Ethos 的 $22.75M a16z 融资（2026-05）押注「AI 取代人工匹配环节」而非「AI 取代专家」——与 SuperMem 的「Agent 替代专家做执行」是不同叙事。

SuperMem 和 Fractional OS 代表的 AI Agent 市场是品类中最激进的方向——2026 年 Beta 阶段面临的最大挑战不是技术而是信任：企业愿意把增长策略交给一个 AI Agent 吗？即使有专家审批？

传统专家网络年订阅 $50K-150K 定价正在被两面夹击：从下方，按需付费的 AI 匹配方案（Ethos、NewtonX）；从上方，AI Agent 市场以订阅制（$97-$4,497/月）提供「无限次使用专家知识」的价值主张。

*网摘综合第三方评测与社区讨论，非本站实测。*

---

## 延伸阅读 · 站内外

**站外**

- Ethos $22.75M Series A (a16z lead, 2026-05) — https://techcrunch.com/2026/05/06/ethos-raises-22-75m-from-a16z-for-its-expert-network-with-voice-onboarding/
- SuperMem 产品资料 — `customer/demo/supermem/`
- MDisrupt Health Expert in the Loop（2026-01）— https://www.businesswire.com/news/home/20260108529541/en/

**站内**

- [recruiting.md](../hr-recruiting/recruiting.md) · [fundraising.md](../marketing-growth/fundraising.md) · [productivity.md](../productivity/productivity.md)