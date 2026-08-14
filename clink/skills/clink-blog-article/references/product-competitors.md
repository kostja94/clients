# Clink — Product Facts & Competitors

> 加载时机：Phase 0R（R1）· Phase 4（Draft）
> as-of: 2026-07（蒸馏自官网与客户文档；对外写作以可核实来源为准）

---

## 1. 四产品线

| 产品线 | 路径 | 能力摘要 |
|--------|------|---------|
| **Global Payments** | `/products/payment` | Hosted Checkout；135+ 币种；100+ 本地支付方式；PCI；反欺诈 |
| **Smart Routing** | `/products/routing` | Dynamic routing；automatic retries；failover；可配置规则 |
| **Billing** | `/products/billing` | 订阅生命周期；Portal；Coupon；usage-based；tax calculation |
| **Agentic Payments** | `/agentic-payment` | Agent 充值、预算、风控；Early Access（旧 URL `/clink-for-claw` 308 到此） |
| **Skill Marketplace** | `/skills` | Agent Payment skills 聚合展示 |

### 开发者面

- REST API + TypeScript / JavaScript SDK + CLI
- Webhooks：session, subscription, invoice, order, refund, dispute
- Test Clock；UAT / Production
- Link PSP：Stripe、Airwallex、Adyen 等（文档示例）
- docs：https://docs.clinkbill.com/ · llms.txt

### 商业

- Contact Sales；Unified Costs / no hidden fees（具体费率 **待验证**，禁止对外编造）
- 内部参考费率（**非官网**）：勿写入对外 blog

---

## 2. 客户证言（官网 as of 2026-06）

| 客户 | 垂类 | 可用主题 |
|------|------|---------|
| BlockSec | Web3 security | 多区域支付覆盖、响应 |
| GeeLark | anti-detect browser | orchestration + subscription |
| Linkloud | cross-border growth | 运营效率 |
| ModelMax | LLM API gateway | Clink for Claw top-up |
| PollyReach | AI voice | agent-initiated payments |
| 其他 logo | VoiSpark, Gazolab, Virax.ai, ZingFront, NovaSonic | 品牌背书，勿编造细节 |

**C3**：证言须 as-of；不夸大 GMV/成功率百分比除非有可核实来源。

---

## 3. 竞品矩阵（公平摘要）

### Stripe（+ Billing）

| 维度 | 说明 |
|------|------|
| 角色 | PSP + 可选 Billing |
| 优势 | 生态、文档、开发者心智第一 |
| 与 Clink | Clink **可连接** Stripe；不替代清算 |
| 写法 | 「stop being dependent on one processor」非「leave Stripe」 |

### Paddle / Lemon Squeezy

| 维度 | 说明 |
|------|------|
| 角色 | Merchant of Record |
| 优势 | 全球 VAT 省心、零合规团队可上线 |
| 与 Clink | Clink 强调品牌留在商户 + 便携数据；MoR 覆盖范围 **待验证（C2）** |

### Chargebee / Recurly

| 维度 | 说明 |
|------|------|
| 角色 | 订阅计费专精 |
| 优势 | 复杂定价、RevRec |
| 与 Clink | Clink 叠加 routing / multi-PSP |

### Spreedly / Primer

| 维度 | 说明 |
|------|------|
| 角色 | 纯编排 |
| 优势 | 路由/tokenization 深度 |
| 与 Clink | Clink 含 Billing + Tax + Portal 一体 |

### Agent 支付

| 维度 | 说明 |
|------|------|
| 竞品 | 新兴/自建为主 |
| Clink | Clink for Claw — Early Access（C4） |

---

## 4. 待验证清单（写作红线）

| 项 | Gate | 写法 |
|----|------|------|
| Clink 具体费率 % | C1 | Contact Sales |
| MoR 法律角色全覆盖 | C2 | 限定语 + Contact Sales 确认 |
| Tax filing 司法辖区列表 | C2 | as-of + 确认 |
| 第三方成功率白皮书 | G3 | 用客户区间 + industry estimates |
| GitHub Skill 仓库维护状态 | G1 | 官网链接，勿断言维护方 |

---

## 5. 定位语言（可用）

- Connect once, route anywhere
- Your Data, Any Processor
- Payment Infrastructure for an AI-Native World
- Scale Global, Bill Local

## 6. 禁止语言

- Clink replaces Stripe
- 无证据「唯一」「全球首个」
- 暗示 Clink 是持牌银行/清算机构

---

*product-competitors · v1.0.0 · 2026-07-21*
