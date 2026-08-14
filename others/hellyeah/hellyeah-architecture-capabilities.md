# Hellyeah 产品架构层与能力层

> **职责**：梳理 Hellyeah 的产品架构层（四平台）与能力层（六能力），厘清两者的层级关系及现有导航结构的分类问题。  
> **关联**：[hellyeah.md](./hellyeah.md) | [hellyeah-features.md](./hellyeah-features.md) | [hellyeah-site-structure.md](./hellyeah-site-structure.md) | [hellyeah-platform-aima.md](./hellyeah-platform-aima.md)  
> **来源**：[hellyeahai.com](https://hellyeahai.com/) 线上页面抓取（2026-07-09）

**Last updated**: 2026-07-09

---

## 一、产品架构层：四平台

Hellyeah 由四个平台构成一套四层增长操作系统。每个平台承担不同职责，共同支撑首页所述的 **Research → Create → Launch → Learn** 循环。

### 1.1 总览

| 层 | 平台 | 路径 | 一句话 |
|---|---|---|---|
| Agent 层 | **AIMA** | `/aima` | AI Marketing Assistant — 用户通过聊天（WhatsApp/Slack）下达目标，AIMA 自主编排全流程 |
| Execution 层 | **Forge** | `/forge` | Agentic Systems — 六个子系统把决策变成实际动作（数据→资产、事件触发、A/B 部署、合规审查、创意生成、Influencer 管理） |
| Intelligence 层 | **Mutation** | `/mutation` | Marketing Intelligence — 实时摄入外部信号（新闻、社媒趋势、市场数据、天气、地缘政治、消费者情绪），自动翻译为营销行动建议 |
| Experimentation 层 | **Déjà Vu** | `/deja-vu` | Continuous Experimentation — 用成千上万个合成用户在真实产品中跑实验，发现增长杠杆，结果写回系统（目前 private alpha） |

### 1.2 AIMA（Agent 层）— `/aima`

- **定位**：*"The marketing team your business never had."*
- **形态**：WhatsApp 为主（Live），iOS/Android/Slack/Web 即将上线
- **定价**：Free $0 forever；企业 Forward-Deployed Growth Pod（按 managed spend % 收费）
- **运作**：用户像发消息给同事一样下达目标 → AIMA 自主完成 Plan → Create → Launch → Optimize → Report
- **内置六 Agent**：strategos（策略）、scribe（文案）、forge（设计）、trader（投放）、lighthouse（生命周期）、oracle（分析）
- **覆盖能力**：Strategy & planning、Image & video creative、Copy、Paid media、Lifecycle & email、Organic & social、SEO & GEO、Reporting & insights
- **渠道接入**：Meta Ads, Google Ads, TikTok Ads, Reddit, Pinterest, X, LinkedIn, WhatsApp, Klaviyo, Shopify, WooCommerce, Instagram, YouTube, Mailchimp, Threads（OAuth-only，Read+write）
- **安全状态**：SOC 2 **in flight**（勿写已认证 Type II）

### 1.3 Forge（Execution 层）— `/forge`

- **定位**：*"The machine room of Hellyeah."*
- **六个子系统**：

| 系统 | 职责 |
|---|---|
| Data to Marketing Asset | 行为/产品/CRM 数据 → 自动分群、预测洞察、个性化旅程 |
| Auto Event Triggering | 库存变化、热点趋势、天气等外部信号 → 即时触发 campaign |
| Website Copy A/B Optimization | AI 持续跑 landing page 实验，自动改写、自动部署 |
| Auto Marketing Compliance Screening | 合规 agent 上线前扫描每条 campaign |
| Autonomous Creative Generation & Testing（CreateMagic） | 视觉/视频素材自动生成、测试、迭代 |
| Influencer Management Dashboard | 创作者生态量化管理，按 ROI 信号分配预算 |

### 1.4 Mutation（Intelligence 层）— `/mutation`

- **定位**：*"See what's happening. React before anyone else."*
- **信号源**：News & press wires、Social trends、Market & FX data、Weather shifts、Geopolitical events、Consumer sentiment
- **能力**：从信号检测到营销响应部署全链路（"60-second nervous system"）
- **案例**：J&T Express 捕捉全球体育事件信号，数周完成多市场 campaign；Playco 将爆款创意趋势同步到 UA 投放；Fish Audio 把文化热点导入内容管线

### 1.5 Déjà Vu（Experimentation 层）— `/deja-vu`

- **定位**：*"Synthetic intelligence for continuous growth discovery."*
- **当前状态**：Private alpha，面向 AI-first product 合作伙伴
- **四阶段循环**：

| 阶段 | 职责 |
|---|---|
| Persona Generation | 基于数据与行为模型生成成千上万个合成用户画像 |
| Exploration Simulation | Agent 在真实产品中走完整流程（注册、结账、CRM pipeline） |
| Event Intelligence | 记录每次流失点/愉悦点/摩擦点，标注信号 |
| Opportunity Extraction | 发现未触达人群、断链转化、偏差，自动通过 Mutation 和 Forge 部署修复 |

### 1.6 四层关系

```
用户 → AIMA（接收目标，对话式编排）
         ↓
       Forge（把所有决策变成实际动作）
         ↓
       Mutation（读外部世界，告诉你机会和风险在哪）
         ↓
       Déjà Vu（持续跑实验，发现增长杠杆，结果写回系统）
```

四平台共同支撑首页 RCLL 循环：
- **Research** → Mutation 信号 + Déjà Vu 探索
- **Create** → Forge 创意/内容生成
- **Launch** → Forge 多渠道投放 + AIMA 编排
- **Learn** → Déjà Vu 结果写回 + Mutation 记忆累积

---

## 二、能力层：六能力

### 2.1 现有六能力（线上 URL 均已上线）

| 能力 | URL | 页内核心统计 |
|---|---|---|
| Agentic Marketing | `/capabilities/agentic-marketing` | 8× launch；4× experiments；73% ops 痛点 |
| Performance Marketing | `/capabilities/performance-marketing` | 3.2× ROAS avg；67% wasted spend ↓ |
| SEO / GEO | `/capabilities/seo-geo` | 20–80 文/月；GEO 多模型 |
| Lifecycle Automation | `/capabilities/lifecycle-automation` | 3.4× open rate；80% manual ↓ |
| Creative Generation | `/capabilities/creative-generation` | 47% sales lift（Nielsen 引用） |
| Influencer Marketing | `/capabilities/influencer-marketing` | $24B market；73% ROI 难衡量 |

### 2.2 导航分类问题：两轴混为一轴

**现状**：官网 mega menu 的 `Capabilities` 列将上述六个能力放在同一个扁平列表里展示。

**核心问题**：这六个术语不在同一维度上。行业共识将它们划分为两个正交的轴：

| 轴 | 维度 | 回答的问题 | 包含项目 |
|---|---|---|---|
| **轴 A — Operating Paradigm（运营范式）** | "怎么跑营销" | 回答方法论/运营模型 | Agentic Marketing、Performance Marketing、Lifecycle Automation |
| **轴 B — Channel / Discipline（渠道/学科）** | "通过哪个 surface 触达" | 回答触达渠道/专项能力 | SEO、GEO、Influencer Marketing、Creative Generation |

**具体问题**：

1. **Agentic Marketing 被降级为"一个 capability"**。它是 Hellyeah 的定义性范式（defining paradigm），不是和 SEO/GEO 平级的"一个能力"。把它和 SEO 并列 = 在说"我们做 agentic marketing，顺便也做 SEO"，而不是"我们用 agentic 范式跑 SEO、跑 paid、跑 lifecycle"。

2. **Performance Marketing 和 Lifecycle Automation 定位模糊**。它们本身是横跨多重渠道的运营框架（Performance 横跨 paid search/social/affiliate，Lifecycle 横跨 email/SMS/push/in-app），不是单一的"能力"。和 SEO/Influencer 放在同一列，用户无法直观判断它们是并列、包含还是替代关系。

3. **列表扁平化导致认知负担高**。六个来自完全不同维度、不同抽象层次的术语被塞进同一列，用户需要自己在脑中重新归类。

**推荐分类**：

```
运营范式（Axis A）                | 渠道/学科（Axis B）
"怎么跑营销"                      | "通过哪个 surface"
─────────────────────────────────────────────────
├── Agentic Marketing             ├── SEO
├── Performance Marketing         ├── GEO
└── Lifecycle Automation          ├── Influencer Marketing
                                  ├── Creative Generation
                                  └── View all →
```

---

## 三、架构层与能力层的关系

### 3.1 关系对照

| 维度 | 产品架构层（四平台） | 能力层（六能力） |
|---|---|---|
| 回答的问题 | "Hellyeah 怎么做到的？" | "Hellyeah 能做什么？" |
| 内容性质 | 产品模块、技术实现 | 营销领域、业务能力 |
| 在导航中的位置 | `Platforms` 菜单 | `Capabilities` 菜单 |
| 用户视角 | 技术团队、集成方 | 营销/增长负责人 |

### 3.2 交叉关系

- **Agentic Marketing**（能力）由 **AIMA**（平台）实现——AIMA 是 agentic 范式的落地产品
- **Performance Marketing**（能力）依赖 **Forge**（执行）+ **Mutation**（归因信号）
- **Lifecycle Automation**（能力）依赖 **Forge**（自动触发 + 数据转资产）+ **AIMA**（编排）
- **SEO / GEO / Influencer / Creative**（能力）作为渠道能力，由 **Forge** 的子系统承载执行，**AIMA** 负责编排
- **Déjà Vu** 对所有能力提供实验反馈，形成能力层的 learn 环

### 3.3 与 Solutions 层的关系

Solutions（5 个，如 Automate Marketing、Reduce CAC）是面向业务结果的落地页，属于"用户想要什么结果"——能力层和架构层共同支撑这些 outcome。

---

## 四、现有页面骨架参考

### 4.1 平台页模板

Hero outcome → 子系统/Agent → 渠道或信号 → 对比表 → 定价（若 AIMA）→ CTA `/demo` → FAQ

### 4.2 能力页模板

Hero（H1 + 3 stats）→ Definition → Traditional vs AI（✕/✓）→ How it works（Step 01–04）→ Use cases（5 条）→ Three layers. One growth engine → Who it's for（3 persona）→ Industries 标签 → FAQ（~8）→ Related capabilities → CTA

### 4.3 Solutions 页模板

Hero（outcome H1 + 3 stats）→ The Problem → How Hellyeah solves it（Step 01–04，对应四平台）→ Use Cases（5 条匿名 vignette）→ Powered By（3 capability 卡片）→ FAQ（10+）→ Related solutions → CTA

### 4.4 Arena 页模板

Hero（垂直 KPI）→ Challenge（4 条）→ How Hellyeah solves it（4 capability 链）→ How it works（3 steps）→ Results → Three platforms → FAQ → Related → CTA

---

## 五、安全与信任

- 首页标注：ISO 27001、GDPR、CCPA、DPF、HIPAA-ready
- Trust Center：`/security`
- AIMA：SOC 2 **in flight**
- 其余平台页未标注独立安全认证

---

*本文档基于 2026-07-09 线上内容整理，随网站更新同步维护。*
