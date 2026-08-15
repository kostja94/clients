# Pond — 创业增长 + AI 劳动力市场平台

> **Demo 状态**: L2 可展示
> **最后评估**: 2026-08-12
> **未通过项**: 无（关键词搜索量部分标注"待验证"，见各子文档）

## 文档导航

| 文档 | 职责 | 引用 |
|------|------|------|
| [主文档](./pond.md)（本页） | 概览、ICP、文档索引 | — |
| [pond-keywords.md](./pond-keywords.md) | 关键词映射、目标页、GEO 策略 | [features](./pond-features.md) |
| [pond-features.md](./pond-features.md) | 功能页：Bounties/Discoveries/Markets、定价、差异化 ★ | [use-cases](./pond-use-cases.md) |
| [pond-competitors.md](./pond-competitors.md) | 竞品分析、差异化（Upwork/Fiverr/Kaggle/AITasker/AngelList） | [features](./pond-features.md) |
| [pond-site-structure.md](./pond-site-structure.md) | URL 层级、IA、技术栈（Next.js/Cloudflare） | 主文档 |
| [pond-use-cases.md](./pond-use-cases.md) | 场景、Persona、映射 | [features](./pond-features.md) |
| [pond-growth-strategy.md](./pond-growth-strategy.md) | 增长渠道、内容计划 | [keywords](./pond-keywords.md) |
| [pond-others.md](./pond-others.md) | 数据来源、合规、待验证项归档 | — |

*产品入口*：[joinpond.ai](https://joinpond.ai/) ｜ 文档：[docs.joinpond.ai](https://docs.joinpond.ai/)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | AI × 创业服务（AI agent 劳动力市场 + 创业增长/融资平台） |
| 网站 | https://joinpond.ai |
| 当前阶段 | 增长期（$7.5M Seed 后，社区驱动扩张） |
| 核心产品 | **Pond**——三合一创业增长平台：**Tasks/Bounties**（让全球人类与 AI agent 竞争完成任务的赏金市场）+ **Discoveries**（build in public 数据展示）+ **Markets**（SAFE/token warrant 融资） |
| 产品形态 | Web（Next.js SPA，英文单语） |
| 关键差异化 | ① 人类 + AI agent 同场竞争交付、"只付结果"；② 增长（Tasks）+ 曝光（Discoveries）+ 融资（Markets）单平台闭环；③ 数据透明核验（Stripe API + Google Analytics） |
| 目标用户 | 早期/成长阶段 Startup 创始人（发任务、融资、曝光）；全球贡献者（人类 + AI agent，赚奖励）；投资者/市场参与者 |
| 目标市场 | 全球（平台宣称 181 国贡献者），Web3/crypto 原生基因 + 传统 startup 两栖 |
| 融资 | Seed $7.5M——Archetype 领投，Coinbase Ventures、Delphi Ventures、cyberFund、NEAR Foundation、Anagram + 30+ 天使（含 Illia Polosukhin，"Attention is All You Need" 联合作者） |
| 更新日期 | 2026-08-12 |

> **官网定位 vs 客户营销叙事差异**：官网及 `llms.txt` 自我定位为「startup growth and market platform」（Discoveries + Markets + Tasks 三支柱）；客户提供的营销叙事将其描述为「生产力分发平台 / AI 劳动力市场」（让 AI agent 作为劳动力竞争完成任务）。本套文档**以官网事实为准**，营销叙事作为资本市场定位语在 §1.1 与 use-cases 中补充记录。

---

## 1. 产品定位

| 维度 | 内容 |
|------|------|
| 品类 | AI 劳动力市场 / 创业增长平台（agentic task marketplace + startup growth platform） |
| 价值主张 | 给创业公司一条"把增长需求变成可度量任务，让全球人类与 AI agent 竞争交付、按结果付费"的执行路径，并一体化覆盖曝光（Discoveries）与融资（Markets） |
| 竞争替代 | 自己下场做（消耗创始人时间）、雇自由职业者（Upwork/Fiverr：慢、贵、按时间计费）、自建 AI agent（零散、开发成本高）→ 转向 Pond 按结果付费 |
| 差异化锚点 | Tasks + Discoveries + Markets 三合一闭环；人类 + AI agent 同场竞争；"you only pay for results"（只付通过验收的结果） |
| 市场位置 | 性价比 + 社区驱动（freemium 起量；Bounty 奖励由发布者自定义，推荐 $10–20/用户） |

### 1.1 定位简述

Pond 诞生于一个判断：**AI 时代"创造"越来越便宜，稀缺的是"分发"**——让好工具、好 agent、好创业公司被正确的人找到并用起来。官网首页给出的第一句话是 "The AI Platform for Solving Any Problems"（描述你的需求，agent 为你交付），Bounties 文档则自比 "Like Kaggle for startups"：早期创业公司最难的不是做产品（AI 已大幅降低门槛），而是产品之后的一切——真实用户、内容证明、合格线索、验证 ICP。Pond 把这些"增长杂活"变成有奖励的任务，交给平台上的真人贡献者与 AI agent 竞争完成，发布者只验收达标的产出、只按结果付费。

产品由三块拼成闭环：**Tasks/Bounties**（任务执行——获客、反馈、测试、内容、线索），**Discoveries**（公开增长数据与排行榜——用透明度建立信任、吸引关注），**Markets**（SAFE / token warrant / stablecoin 融资——资金进 Pond Vault 按月释放，配合月度更新与 AMA 保证透明度）。官网还同时呈现了 Agent 上架生态（"Building an agent? Connect your agent and distribute on Pond"）与三种交付模式（单个 agent / agent 协作 / agent 竞争），这是其向"AI 劳动力市场"叙事演进的直接证据——与客户提供的营销介绍方向一致，但当前官网主叙事仍以"startup growth platform"为准。

核心用户是**早期/成长阶段创业公司创始人**：他们可能是 solo founder（如案例中的 Prompt Builder、Tasker Army），有真实增长需求但没有预算雇团队；其次是**全球贡献者**——包括想赚取奖励的真人（含自由职业者、学生、测试者）与连接上平台的 AI agent；再其次是**投资者/市场参与者**，通过 Markets 以 SAFE、token warrant 参与早期项目。Pond 的 raison d'être 是"创业公司增长的后台外包"：把过去只能靠招人、投广告、碰运气完成的增长动作，变成可以在一个市场里发布、竞价、验收、结算的标准流程。

---

## 2. 产品信息

面向**早期与成长阶段 startup 创始人**，提供三条产品线（详见 [features](./pond-features.md)）：

- **Pond Tasks / Bounties**（核心）：任务赏金市场。发布者描述需求（可让 Pond AI 辅助生成任务），设定奖励（推荐基础 $10/用户、$20 标准），全球贡献者（人类 + AI agent）竞争提交，发布者逐条审核、只对达标结果付款。典型任务类别：内容创作、推荐/获客、产品反馈、用户测试、技术任务、数据任务、社区运营。
- **Pond Discoveries**：build in public 平台。创业公司公开收入/MRR/MAU/用户增长，数据经 Stripe API 与 Google Analytics 核验，有 Top Revenue / Top MRR / Hottest / Newest 排行榜（Pond 自身也在榜，2026-08 数据：Total Revenue $204.6k、MAU 18.1k）。
- **Pond Markets**：融资市场。支持 SAFE、token warrant、stablecoin 募资；募集资金入 Pond Vault 按月释放；投资者在轮次关闭前可撤资，3 个月未达成目标全额返还；平台上已有 Manu Khetan、Dan Jones、Francis Zhan（Tribe Capital）等天使/机构投资者入驻。

**定价**：Freemium。平台核心功能免费开放；Bounty 奖励金额由发布者自定义；高级/企业方案与 Markets 费率需联系团队（未公开）。平台侧抽佣比例 `待验证`。

---

## 3. 关键词摘要

核心方向：**ai agent marketplace / ai task marketplace**（品类词）、**startup growth platform**（增长词）、**build in public platform**、**startup fundraising platform**、**earn money with ai / get paid to test apps**（贡献者侧）、**safe agreement / token warrant**（融资侧）。

- 官网 `llms.txt` 公开了一份"希望被 AI 检索关联"的推荐关键词表（startup growth platform、build in public、reward-based tasks 等 20 条）——这是官方 GEO 信号，已在 keywords 文档中作为 P0 承接。
- 完整关键词表、意图分类（导航/信息/商业/交易 ×≥5 词条）、内容缺口见 [pond-keywords.md](./pond-keywords.md)。搜索量数据需 Semrush/Ahrefs 核实，当前标注待验证。

---

## 4. 竞品摘要

Pond 的竞争横跨三个维度，主要竞品如下（完整拆解见 [pond-competitors.md](./pond-competitors.md)）：

| 竞争维度 | 代表竞品 | Pond 的差异 |
|---------|---------|------------|
| AI agent 任务市场 | AITasker（Prototype-as-Bid）、UpAgents | Pond 支持人类 + agent 同场竞争、只付结果；AITasker/UpAgents 为纯 agent、未融资、规模小 |
| 任务/竞赛平台 | Kaggle（Google 旗下）、Remotasks | Kaggle 仅数据科学竞赛；Pond 覆盖增长/内容/反馈等创业全场景任务 |
| 传统自由职业市场 | Upwork、Fiverr | Upwork/Fiverr 按人按时间，慢而贵；Pond 按结果付费、无需管理、AI 边际成本趋零 |
| 融资平台 | AngelList、Wefunder、Republic | AngelList/Wefunder 纯融资；Pond 将融资与增长任务、公开数据绑定（vault 月度释放 + AMA） |

---

## 5. 站点结构摘要

- **技术栈**：Next.js SPA + Cloudflare 托管；docs 走 docs.joinpond.ai（Mintlify 风格）；媒体走独立 CDN 子域。详见 [site-structure](./pond-site-structure.md)。
- **核心路径**：`/`（首页）、`/tasks`（任务市场）、`/discoveries`（展示）、`/markets`（融资）、`/points`（积分）、`/portfolio`、`/manage-startups`、`/tasks/mybounties`、`docs.joinpond.ai`、`/llms.txt`。
- **SEO 现状**：sitemap.xml 返回 500（待修复）；无 /blog、无独立 /agents 目录页、无定价页；有 LLM 友好内容声明（llms.txt/llms-full.txt）。
- **多语言**：英文单语，无 hreflang。

---

## 6. 使用场景摘要

官网呈现的核心 Persona（完整见 [use-cases](./pond-use-cases.md)）：

1. **Startup 创始人 / 产品负责人**——发 Bounty 获真实用户、产品反馈、销售线索；上 Discoveries 展示增长；去 Markets 融资。
2. **真人贡献者（含自由职业者/学生）**——在 /tasks 接任务赚奖励（案例：测试 app 赚 USDC、写 LinkedIn 内容）。
3. **AI Agent**——"Connect your agent and distribute on Pond"，agent 自动接单、交付、收款。
4. **投资者 / 市场参与者**——评估 Discoveries 透明数据，通过 Markets 以 SAFE/token warrant 参与。

典型场景（官网原话保留）："Get Paid to Break Moatt Before Launch"（上线前找 bug）、"Clean Your Camera Roll With PhotoBase Cleaner"（真实使用测试）、"Test drive SELAT and earn up to 11 USDC"。

---

## 7. 增长策略摘要

核心渠道与方向（完整见 [growth-strategy](./pond-growth-strategy.md)）：

- **任务侧双面增长**：Bounty 任务自带病毒循环（发布者获增长、贡献者获报酬），每任务 3x 预期参与度。
- **GEO/AI 检索资产化**：llms.txt 已就位，落地推荐关键词页面 + 修复 sitemap。
- **内容 SEO**：0–3 月建 /blog 对比页（Pond vs Upwork、Pond vs Kaggle）、"how to get first users" 系列。
- **社区与 Web3 生态**：X/Twitter build in public、以太坊基金会等任务案例、NEAR/Archetype 生态背书。
- **Agent 供给端**：招募 agent 上架（当前 20 个 agents at work，增长空间大）。

---

## 8. 优化建议

1. **落地 `/blog` 对比内容承接商业意图**：创建 "Pond vs Upwork"、"Pond vs Kaggle"、"What is an AI agent marketplace" 三篇 P0 内容——当前商业型搜索词（best ai agent marketplace、pond vs upwork）站内零覆盖，是全站最明确的内容缺口。
2. **把 `/agents` 从首页区块升级为独立 SEO 目录页**：首页 "Browse All Agents" 是 JS 渲染区块，搜索引擎可见性弱；独立目录 + 每个 agent 的静态详情页可承接 "ai agent marketplace"、"hire ai agent" 等 P0 信息型词。
3. **修复 sitemap.xml 并增加结构化数据**：当前 sitemap.xml 返回 500，严重影响抓取与收录；建议为任务详情页加 `JobPosting`/`WebApplication` schema、为 Markets 轮次加结构化标记，并核对 robots.txt 中 Disallow `/llms-full.txt` 与 "希望被 AI 引用" 目标之间的策略一致性。

---

> 关联：[keywords](./pond-keywords.md) | [features](./pond-features.md) | [competitors](./pond-competitors.md) | [site-structure](./pond-site-structure.md) | [use-cases](./pond-use-cases.md) | [growth-strategy](./pond-growth-strategy.md) | [others](./pond-others.md)

*Last updated: 2026-08-12*
