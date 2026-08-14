# Clink 功能与产品能力

> **本文档职责**：产品**能做什么**、模块、API 面、集成方式；情境见 [clink-use-cases.md](./clink-use-cases.md)。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[clink.md](./clink.md) | [clink-keywords.md](./clink-keywords.md) | [clink-competitors.md](./clink-competitors.md)

**Last updated**: 2026-07-21 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [clink.md](./clink.md) |
| 关键词 | [clink-keywords.md](./clink-keywords.md) |
| 使用场景 | [clink-use-cases.md](./clink-use-cases.md) |
| 竞品 | [clink-competitors.md](./clink-competitors.md) |
| 网站结构 | [clink-site-structure.md](./clink-site-structure.md) |
| 增长策略 | [clink-growth-strategy.md](./clink-growth-strategy.md) |

---

## 一、功能概览与建议 URL

| 产品线 | 官网/文档路径 | 目标关键词（示例） |
|--------|---------------|-------------------|
| **Global Payments** | [/products/payment](https://clinkbill.com/products/payment) | global payment gateway, hosted checkout |
| **Smart Routing** | [/products/routing](https://clinkbill.com/products/routing) | payment orchestration, automatic payment retry |
| **Billing** | [/products/billing](https://clinkbill.com/products/billing) | subscription billing software, recurring billing |
| **Agentic Payments** | [/agentic-payment](https://clinkbill.com/agentic-payment) | agentic payment, AI agent billing |
| **Skill Marketplace** | [/skills](https://clinkbill.com/skills) | agent payment skills |
| **Link PSP** | docs/guides/payments/link_psp | connect stripe airwallex |
| **Developer** | docs.clinkbill.com | clink api, checkout session api |

---

## 二、三大产品柱（官网 Feature Overview）

### 2.1 Global Payments

| 能力 | 说明 |
|------|------|
| **统一网关界面** | 多网关收敛为一界面，确保合适支付方式可用 |
| **Hosted Checkout** | 托管结账（文档 [Checkout Session](https://docs.clinkbill.com/guides/payments/checkout_session)） |
| **全球覆盖** | **135+ 币种**、**100+ 本地支付方式**（首页） |
| **安全** | PCI 合规保险库、欺诈防护（首页 *Secure & Stable*） |
| **集成** | Developer-friendly API 或预构建托管方案；*go live in minutes*（首页） |

### 2.2 Smart Routing

来源：[products/routing](https://clinkbill.com/products/routing)

| 能力 | 说明 |
|------|------|
| **Dynamic Routing** | 智能路由以最大化效率；**费用最小化**路径；**网关备份**即时 failover |
| **Automatic Retries** | 失败交易智能重试；提升 acceptance rate |
| **Customizable Rules** | 可优先级配置的流量分配；**可行动的数据分析** |

### 2.3 Billing

来源：[products/billing](https://clinkbill.com/products/billing)

| 能力 | 说明 |
|------|------|
| **Subscription Management** | 复杂订阅与生命周期；灵活定价与试用；多币种定价；自定义账单周期 |
| **Customer Portal** | 自助升降级、发票下载、支付方式更新 |
| **Coupon** | 动态优惠码；可按产品/价格/客户定向 |
| **Tax Compliance** | 自动合规、精确计税、**申报与代缴**（Automatic Filing and Remittance，具体法域 **待验证**） |

---

## 三、差异化能力（≥5 条）

| # | 能力 | 用户价值 | 对外表达簇 |
|---|------|----------|------------|
| 1 | **Your Data, Any Processor** | 换 PSP 不重写订阅逻辑 | *Connect once, route anywhere* |
| 2 | **Smart Routing + Retries** | 降低失败交易造成的收入漏损 | *Recover lost revenue on autopilot* |
| 3 | **Unified Billing + Payments** | 一个 Dashboard 管订阅与收款 | *Entire revenue lifecycle* |
| 4 | **Built-in Tax** | 减少多国税务拼接 | *Built-in tax handling* |
| 5 | **Usage-Based Pricing** | 适配 AI/API 按量计费 | *Usage-based pricing* |
| 6 | **Agentic Payment** | Agent 任务中自动充值与限额 | *Get Agent-Ready in 1-Click* |
| 7 | **Test Clock** | 订阅沙箱时间推进 | 开发者文档 API 列表 |

---

## 四、开发者与集成面

基于 [docs.clinkbill.com/llms.txt](https://docs.clinkbill.com/llms.txt)（2026-07-21 索引）；完整 IA 见 [clink-site-structure.md §七](./clink-site-structure.md)：

| 类别 | 能力 |
|------|------|
| **支付会话** | Create/Get Checkout Session；Create Payment（一次性） |
| **订阅** | Create/Cancel/Get Subscription；Create Product/Price |
| **客户** | Customer；Payment Instrument；Customer Portal Session |
| **Agent** | Create/Get **Agent Payment Session** |
| **测试** | Test Clock（create/advance/complete/list） |
| **Webhook** | session, subscription, invoice, order, refund, dispute, customer.verify |
| **SDK** | TypeScript SDK、JavaScript SDK（浏览器 redirect/embedded） |
| **CLI** | clink-cli：钱包、支付、退款、风控规则 |
| **集成** | UAT / Production 环境；[Integration 指南](https://docs.clinkbill.com/integration.md) |

### 链接外部 PSP

- 路径：Settings → Merchant → Linked Payment Service Providers  
- 支持 **Stripe、Airwallex、Adyen** 等（文档示例）；**PCI DSS 4.0.1**  
- **无有效连接时**：所有支付与续订失败（文档明确）

---

## 五、Agentic Payments（Agent 经济）

来源：[agentic-payment](https://clinkbill.com/agentic-payment)（旧 URL `/clink-for-claw` 308 重定向）

| 步骤 | 行为 |
|------|------|
| 1 | Claw 检测余额不足 → 暂停任务 |
| 2 | 用户绑定支付方式并设 **Agent spending limits** |
| 3 | **Smart automatic top-up** 达阈值自动充值 |
| 4 | AI 风险评分 + Merchant guardrails |

| 卖点 | 说明 |
|------|------|
| 24/7 autonomous top-ups | 用户绑卡后 Agent 无需人工充值 |
| 一行 SDK / Skill | Agent 声明需资金，Clink 处理后续 |
| 安全 | PCI vault、tokenized cards、per-task limits |
| Skill 仓库 | [github.com/clinkbillcom/agentic-payment-skills](https://github.com/clinkbillcom/agentic-payment-skills) |

**状态**：Early Access — *Request Early Access* 表单（年处理量 USD）

---

## 六、费用与商业（公开信息有限）

| 项 | 官网表述 | 备注 |
|----|----------|------|
| 定价模型 | Unified Costs、transparent、no hidden fees | 具体 % **待验证** |
| 生态参考 | 仓库内 Oginify 案例写 Clink **4.5% + $0.30/笔** | **非官网**，仅作内部参考，对外需客户确认 |

---

## 七、功能 ↔ 关键词承接

| 功能模块 | 用户口语 | 主承接载体 |
|----------|----------|------------|
| Routing | reduce failed payments | /products/routing |
| Billing | manage SaaS subscriptions | /products/billing |
| Checkout | hosted payment page | /products/payment + docs/checkout_session |
| Agent | pay with agents | /agentic-payment |
| Multi-PSP | connect stripe and airwallex | docs/link_psp |

---

*与 [clink-keywords.md](./clink-keywords.md) 交叉引用*
