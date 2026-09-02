# Agent Billing · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Agent Billing / AI Agent 计费**——面向 **卖 Agent 产品的公司**，如何把 action、workflow、outcome 变成可发票、可审计、可续费的商业单元，并追踪 model 成本与 margin；验收以 **Signals/计量、定价模型、Delivered Value、平台选型** 为主。本页为 **卖方 monetization 栈 SSOT**；Agent **买方**动钱 → [agentic-payments.md](agentic-payments.md)；人类开发者给 Vibe 产品接 Stripe → [vibe-coding-payments.md](vibe-coding-payments.md)；技能目录/MCP 分发 → [agent/agent-skills.md](agent/agent-skills.md)（marketplace ≠ 计费栈）。

**材料范围**：公开网络检索（Paid.ai 官方站与 docs、witn.com、Flexprice.io、Nevermined 卖方文档、Orb「2026 state of AI agent pricing」、TechCrunch/Lightspeed 融资报道、Chargebee/Simon-Kucher/Drivetrain 定价 playbook、Stripe Agents 文档）；**未**引用 Alignify 站内 JSON 为独立事实来源。网摘整理日期 **2026-09-03**。

**站内对照**：待上线正式页时对齐（新文优先 `/blog`）· slug **`agent-billing`**

**Tools 关键词与 slug 映射**：待上线正式页时注册 · `keywordEn`: **AI agent billing**（Secondary：`AI agent billing software` · `agent monetization`）· `keywordZh`: **AI Agent 计费** / 智能体计费平台

## 与相邻 slug 分流

| slug | 典型读者问题 | 交付形态 | 与本 slug 的边界 |
|------|-------------|---------|------------------|
| **`agent-billing`（本页）** | 「我卖 Agent，怎么向客户定价、开票、算 margin、证明 ROI？」 | 计费平台、Signals、outcome/hybrid、credits、价值收据 | — |
| **`agentic-payments`** | 「Agent **买方**怎么授权、结算、走哪条支付协议？」 | x402/AP2、Agent Wallet、KYAPay | 本页 = **卖方**收客户的钱；payments = Agent **花**用户的钱 |
| **`how-to-add-payments-to-vibe-coded-app`** | 「我用 AI 搭了 SaaS，人类用户怎么付我？」 | Stripe/Paddle 集成（[vibe-coding-payments.md](vibe-coding-payments.md)） | 本页 = **Agent 产品**的 B2B 计费，非 Vibe 独立开发者接卡 |
| **`agent-skills`** | 「去哪找 skill/MCP？怎么装？」 | 目录、CLI、注册表 | marketplace 可**叠加**收费，但分发 ≠ 计费引擎 |
| **`ai-agent-pricing`（未建 · 可选 Hub）** | 「outcome vs usage vs hybrid 怎么选？」 | 定价**模型**框架 | 本页偏 **平台/工具选型**；模型专论可拆 Hub |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Agent Billing / AI Agent 计费**：Agent 公司面向 **B2B 客户** 的定价、计量、发票、续费与 margin 管理——单位是 **业务信号**（ticket resolved、meeting booked），而非仅 seat 或 raw token。
- **Agent Monetization**：与 Agent Billing **同栈不同说法**；SERP 上 `AI agent billing` / `billing software` 工具意图更强，`agent monetization` 单独检索量偏低且易歧义——**slug 用 `agent-billing`，monetization 作 Secondary keyword**。
- **Signals（Paid）**：Agent 完成工作单元时上报的 **可计费事件**；可绑 workflow 步骤、完整 outcome 或 volume；区别于 SaaS 的「预定义 API call 计数」。
- **Delivered Value / Value Receipts**：与 invoice 并行的 **客户价值证明**（省时、省钱、增收、风险规避）；支撑 pilot 与 renewal，Paid「Certified by Paid」框架。
- **Outcome-based pricing**：仅对 **可验证结果** 收费（如 resolved ticket）；行业样本纯 outcome 约 **~3.8%**（Orb 2026，80 家 Agent 公司）——讨论热、采用仍少，主因 **归因与 instrumentation**。
- **Usage-based / consumption billing**：按 token、API call、agent run 等 **消耗** 计费；Orb 2026：**~91%** Agent 公司采用（常与订阅 hybrid）。
- **Hybrid pricing**：平台费/订阅 + usage 或 outcome 尾；Orb 2026：**~95%** 为默认组合。
- **Agent-native billing platform**：为 Agent 工作流设计（Signals、outcome、多 provider 成本、margin by agent）——相对 Stripe/Chargebee **retrofit** 的品类标签（Paid 等公开叙事）。
- **Outcome-native billing（witn）**：对 **verified outcome** 计费（settlement window、可审计 event trail、ASC 606 叙事）——activity 信号喂给 billable condition，而非直接上 invoice。
- **Meter for margins, bill for outcomes（Paid）**：token/GPU **内部**追踪优化；对客 **outcome/业务单位** 定价，不把 flour+tomato 逐项标价给顾客。

---

## 专题对照：卖方栈 vs 买方栈 vs 通用 UBB

| 层 | 典型产品/协议 | 解决什么 |
|----|--------------|---------|
| **Agent 卖方计费（本页）** | Paid、witn、Flexprice（Agent 向） | 向 **企业客户** 开发票、证明 ROI |
| **API/MCP 按次卖钱（重叠）** | Nevermined Paywall、x402 + metering | Agent **买家**付给 API 卖方；与 [agentic-payments.md](agentic-payments.md) 重叠——本页只写 **「你卖 Agent 给客户的 billing」** |
| **通用 usage billing 基建** | Metronome、Orb、Lago | 高吞吐事件、企业合同；2026 Stripe 收 Metronome、Adyen 收 Orb |
| **人类 SaaS 接卡** | Stripe Billing、Chargebee | Vibe/传统 SaaS；见 [vibe-coding-payments.md](vibe-coding-payments.md) |

---

## 问题域（为何 2025–2026 爆发）

- **Seat 失效**：客户可部署可变数量 Agent，不按「人登录」创造价值；quiet agent 难续费（Paid/TechCrunch 叙事）。
- **成本不可预测**：单次 workflow 可触发多 model、tool、RAG——纯订阅或 flat usage 易 **margin 被吃光**。
- **Pilot 难转 production**：企业质疑「AI slop」；需 **价值收据** 而非仅 usage 账单（MIT 等称大量 pilot 无 ROI）。
- **Retrofit SaaS billing 不够**：Metronome/Orb 擅 **meter**，但 outcome 归因、Human-equivalent value、agent-level margin 需 **Agent-native** 层（行业文共识，Vendor 单源待交叉）。
- **定价模型实验频繁**：hybrid 成默认；平台需 **无代码改价**，避免每次改 pricing 都 engineering sprint。

---

## 能力栈（概念拆分）

- **Signal 架构**：命名规范、metadata、与 product attribute 绑定——计费与 Delivered Value 共用同一事件流（Paid docs）。
- **多 vendor 成本归因**：OpenAI/Anthropic/自托管/tool API → **per customer · per agent · per action** margin（非仅 aggregate token）。
- **定价引擎**：credits、subscription、usage、outcome、hybrid；**overage · rollover · wallet**（Flexprice/Hyperline 类）。
- **Outcome 验证**：settlement window、reversal、contractual success criteria（witn 叙事；finance ASC 606）。
- **客户门户**：usage、ROI、value breakdown、renewal 对话素材。
- **非破坏性集成**：与现有 Stripe/Chargebee/Zuora **并存**（Paid 公开主张 layer alongside）。

---

## 形态谱系

- **Type A — Agent-native monetization**：Paid（Signals + Delivered Value + billing 一体）；witn（outcome-native）。
- **Type B — 开源/可自托管 UBB + credits**：Flexprice（agent workflow metering、outcome 事件可配置）。
- **Type C — 通用 enterprise UBB**：Metronome、Orb、Lago——Agent 公司 **infra _meter** 层，常与 A/B 叠加或 buy 替代自建。
- **Type D — 支付+计量一体（卖方 API）**：Nevermined——Agent 买 API 时 meter；**非**典型「卖 Agent SaaS 给客户」选型，见 payments 分流。
- **Type E — 定价模型 Hub（无平台榜）**：Orb/Chargebee/Simon-Kucher 研究文——未来可选 `ai-agent-pricing` slug。

---

## 风险 · 合规 · 治理

- **Outcome 归因争议**：谁定义「resolved」、failed attempt 谁买单——HubSpot/Intercom 等需 **双定义**（confirmed vs assumed resolution）。
- **Revenue recognition**：outcome 作 **variable consideration**（ASC 606）；需 reversal window 与 audit trail（witn 公开论述，非法律意见）。
- **Vendor 案例夸大**：build-vs-buy、+20–60% revenue 等多来自 **Paid 等 Vendor blog**——正文须标注单源。
- **与 payments 混淆**：对客户 **invoice** vs Agent **花卡买 API**——选型文档必须分流，避免混为一谈。
- **纯 token 对客计价**：易引发「为什么为失败付费」——行业倾向 hybrid + 内部 meter only。

---

## 落地碎片

- **先 map value stream → 再定 Signals**：哪些 step 可收费、哪些只追踪成本（Paid playbook）。
- **默认 hybrid**：可预测 base + usage/outcome tail（Orb 2026 行业默认）。
- **Build vs buy**：90 天内要开票 → 买平台；2–3 工程师全职一年才考虑自建（Paid 公开 checklist，Vendor 视角）。
- **Nevermined 场景**：若核心是 **卖 API/MCP 给 Agent** 按次收费，读 [agentic-payments.md](agentic-payments.md)；若核心是 **卖 Agent 给企业**，读本页 Type A/B。
- **Skills marketplace**：分发在 [agent-skills.md](agent/agent-skills.md)；收费仍走本页 billing 栈或自建 Stripe。

---

## 工具与产品类型

| 类型 | 代表 | 备注 |
|------|------|------|
| Agent-native 计费 | **Paid** | Signals、Delivered Value、credits/outcome/hybrid；$33.3M 融资（2025，TechCrunch） |
| Outcome-native | **witn** | Verified outcome + settlement window；与 UBB 分流 |
| 开源 Agent/AI UBB | **Flexprice** | credits、usage、outcome 事件；可自托管 |
| 通用 UBB | Metronome、Orb、Lago | 大规模 event；Stripe/Adyen 收购中 |
| API paywall + meter | Nevermined | 卖方 API——**adjacent**，canonical 支付栈见 agentic-payments |
| 策略/模型研究 | Orb 2026 pricing study | 非产品选型 SSOT |

**成文默认 Best H3 候选（3 款）**：Paid · witn · Flexprice（发文前须部署仓 product exclusivity 查重）。

---

## 代表产品速查

### Paid

- **定位**：The Monetization Platform for AI Agents——定价、credits/outcome、margin、value receipts、billing 一体。
- **融资**：€10M pre-seed（2025-03）+ $21.6M seed（2025-09，Lightspeed）；累计约 $33.3M（TechCrunch）。
- **客户**：Artisan、IFS、Logic、HappyRobot 等（官方/Tier 1）。
- **官方**：https://paid.ai/ · https://docs.paid.ai/

### witn

- **定位**：Outcome-based billing infrastructure——定义 billable condition，event trail，settlement 后确认才入账。
- **差异**：Usage 平台 meter **activity**；witn bill **verified results**（官网对比 Metronome/Orb）。
- **官方**：https://www.thewitn.com/

### Flexprice

- **定位**：开源/云 UBB + credits + outcome 事件；Agent workflow 级 metering；Stripe/Razorpay 等集成。
- **官方**：https://flexprice.io/

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| Paid | Agent-native monetization platform | https://paid.ai/ |
| Paid · Agent Signals | Signals 计费概念 | https://paid.ai/blog/billing/introduction-to-agent-signals-the-key-to-billing-ai-agents |
| Paid · Delivered Value | 价值收据框架 | https://docs.paid.ai/documentation/getting-started/delivered-value.md |
| witn | Outcome-native billing | https://www.thewitn.com/ |
| Flexprice | 开源 AI/agent UBB | https://flexprice.io/ |
| Orb · 2026 AI agent pricing | 80 家样本：95% hybrid、91% usage、3.8% outcome | https://www.withorb.com/blog/2026-state-of-ai-agent-pricing-models-trends-and-whats-working |
| TechCrunch · Paid seed | $21.6M seed 报道 | https://techcrunch.com/2025/09/28/paid-the-ai-agent-results-based-billing-startup-from-manny-medina-raises-huge-21m-seed/ |
| Lightspeed · Paid | 投资叙事 | https://lsvp.com/stories/the-ai-agent-economy-has-a-19-trillion-problem-our-investment-in-paid/ |
| Chargebee · AI agent pricing playbook | outcome/action/hybrid 框架 | https://www.chargebee.com/blog/pricing-ai-agents-playbook/ |
| Stripe · How agents work | Billing vs commerce vs dev tools 三分 | https://docs.stripe.com/agents/how-it-works |

### 对比与测评（第三方；观点非官方）

- Orb 2026：**hybrid 已饱和**；pure outcome **未增长**——瓶颈在 instrumentation，非需求（Orb 研究，单源 Tier 1 级行业稿）。
- Paid：**meter for margins, bill for outcomes**；retrofit Stripe/Zuora 不适配 Agent（Vendor blog，作观点引用）。
- Flexprice vs Paid vs Nevermined 等 listicle 文常见，但多含 Vendor/SEO 利益——**不作**独家事实源。

---

## 延伸阅读 · 站内外

**站内**

- [agentic-payments.md](agentic-payments.md) · [agentic-commerce.md](agentic-commerce.md) · [vibe-coding-payments.md](vibe-coding-payments.md) · [agent/agent-skills.md](agent/agent-skills.md)

**站外**

- Simon-Kucher · Monetizing GenAI and AI Agents（2026 WP，定价模型采用率）
- Drivetrain · outcome-based pricing playbook（hybrid 实践）
