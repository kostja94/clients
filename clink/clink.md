# Clink

> 遵循 [客户文档规范](../../client-template.md) | 基于 [clinkbill.com](https://clinkbill.com/)（**复核 2026-07-21**）

**Last updated**: 2026-07-21

---

## 文档体系（六主文档）

| 文档 | 职责 | 引用 |
|------|------|------|
| **clink.md**（本文） | 产品概览、定位、ICP、摘要 | 详述见各专项 |
| [clink-features.md](./clink-features.md) | 支付、路由、计费、Agent 支付能力 | keywords、use-cases |
| [clink-use-cases.md](./clink-use-cases.md) | Persona、情境、/for/* 规划 | features |
| [clink-keywords.md](./clink-keywords.md) | 关键词、目标页、承接载体 | site-structure |
| [clink-competitors.md](./clink-competitors.md) | 竞品矩阵、差异化 | features |
| [clink-site-structure.md](./clink-site-structure.md) | URL、IA、文档站结构、分阶段落地 | keywords、growth-strategy |
| [clink-growth-strategy.md](./clink-growth-strategy.md) | 渠道、内容战役、实验 | keywords、site-structure |

**原则**：每条重要信息**一处详述**、他处摘要 + 链接。

*产品入口*：Web [clinkbill.com](https://clinkbill.com/) | 文档 [docs.clinkbill.com](https://docs.clinkbill.com/) | Login（`uat-dashboard.clinkbill.com`）

---

## 1. 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2B / **FinTech / Payments & Subscription Billing** / Payment Orchestration |
| 网站 | https://clinkbill.com/ |
| 文档 | https://docs.clinkbill.com/ |
| 当前阶段 | 增长期（三大产品页 + Agentic Payments + Skill Marketplace 已上线） |
| 核心产品 | **Clink**：面向全球 SaaS 与 AI 原生产品的 **订阅计费 + 支付编排** 平台——一次接入，路由多 PSP，内置税务与本地化收款 |
| Slogan（首页） | **Payment Infrastructure for an AI-Native World**；页脚 *Scale Global, Bill Local.* |
| 目标市场 | 全球化 SaaS、AI App、游戏、市场平台、Fintech、电商、Creator、Agency（官网 Customers 叙事） |
| 产品形态 | **Dashboard + API + Hosted Checkout + SDK**（TypeScript / JavaScript / CLI）；可链接外部 PSP（Stripe、Airwallex、Adyen 等） |
| 关键差异化 | **订阅数据与 PSP 解耦** + **智能路由/重试** + **135+ 币种 / 100+ 本地支付方式** + **Agentic Payments** |
| 更新日期 | 2026-07-21 |

### 能力与边界（Scope）

| 维度 | 说明 |
|------|------|
| **提供** | Checkout Session、订阅生命周期、Customer Portal、Coupon、税务合规、多 PSP 链接与路由、Webhook、Test Clock、Agent Payment Session |
| **不提供** | 替代持牌银行身份的法律角色说明需以合同为准；Clink 作为编排/计费层，**底层清算仍依赖所连 PSP**（见 [Link PSP 文档](https://docs.clinkbill.com/guides/payments/link_psp)） |
| **合规** | 宣称 **PCI DSS 4.0.1**、欺诈防护、保险库托管卡数据（官网 + 文档） |

### 商业摘要

- **定价**：官网强调 **Unified Costs**、无隐藏费用（具体费率表 **待验证** 是否公开）
- **接入**：Contact us / Login；文档 Quickstart 创建首笔 Checkout Session
- **Agent 线**：Agentic Payments — Early Access（[/agentic-payment](https://clinkbill.com/agentic-payment)；旧 URL `/clink-for-claw` 308 重定向）

*功能详表* → [clink-features.md](./clink-features.md)

---

## 2. 产品定位

### 产品摘要

**Clink** 将 **全球收款、订阅计费、税务与支付编排** 收敛为单一平台：商户可保留对订阅数据的控制，同时把交易路由到已连接的 Stripe、Airwallex 等处理器，用 **动态路由与自动重试** 提升成功率。面向 **AI 原生时代**，新增 **Agent 自动充值、预算与风控**（Agentic Payments），服务 OpenClaw 等 Agent 运行时场景。

### 一句话定位

> **Connect once, route anywhere** — 可移植的订阅与支付基础设施，让团队把时间花在产品上，而不是拼接 PSP、税表与计费逻辑。

### 首页价值主张（原文要点）

| 卖点 | 说明 |
|------|------|
| 100+ Local Payment Methods | 本地化支付方式覆盖 |
| Usage-Based Pricing | 用量计费支持 |
| Built-in Tax Handling | 内置税务处理 |
| Your Data, Any Processor | 数据独立、可换可组合 PSP |
| Get Agent-Ready in 1-Click | Agent 经济相关 CTA |

*Persona* → [clink-use-cases.md](./clink-use-cases.md)

---

## 3. 目标受众 / ICP

- **全球 SaaS 创始人 / RevOps**：要扩多国、降支付失败率、统一订阅账单
- **支付/财务工程**：需多 PSP、路由规则、Webhook 与沙箱（Test Clock）
- **AI / Agent 产品团队**：Agent 任务中自动充值、Spend limit、风险规则
- **中国/亚太主体出海团队**：需链接海外 PSP、Hosted Checkout、文档与客服（生态案例含 BlockSec、GeeLark、Linkloud 等）
- **合作伙伴 / Reseller**：平台型客户（证言中「trusted long-term partner」表述）

---

## 4. 核心产品线（摘要）

| 模块 | 线上路径 | 说明 |
|------|----------|------|
| **Global Payments** | [/products/payment](https://clinkbill.com/products/payment) | Hosted Checkout、全球覆盖、PCI、反欺诈 |
| **Smart Routing** | [/products/routing](https://clinkbill.com/products/routing) | 动态路由、自动重试、自定义规则 |
| **Billing** | [/products/billing](https://clinkbill.com/products/billing) | 订阅、Portal、Coupon、税务 |
| **Agentic Payments** | [/agentic-payment](https://clinkbill.com/agentic-payment) | Agent 充值、预算、风控；Early Access |
| **Skill Marketplace** | [/skills](https://clinkbill.com/skills) | Agent Payment skills 聚合 |
| **Developer** | [docs.clinkbill.com](https://docs.clinkbill.com/) | API、SDK、CLI、Webhook、Quickstart |

*完整能力与文档 IA* → [clink-features.md](./clink-features.md) · [clink-site-structure.md §七](./clink-site-structure.md)

---

## 5. 关键词摘要

| 类型 | 示例 |
|------|------|
| **品牌** | Clink, clinkbill, Clink billing |
| **Primary** | subscription billing software, payment orchestration, global payment platform |
| **Secondary** | payment routing, automatic payment retry, hosted checkout SaaS |
| **Long-tail** | stripe alternative subscription billing, multi PSP payment routing, AI agent payments |
| **Agent** | agentic payment, claw payment integration, autonomous top-up |

*完整映射* → [clink-keywords.md](./clink-keywords.md)

---

## 6. 竞品摘要

- **支付处理器**：Stripe、Adyen、Airwallex
- **MoR / 税务代缴**：Paddle、Lemon Squeezy
- **纯编排**：Spreedly、Primer（**待验证** 功能重叠度）
- **计费专精**：Chargebee、Recurly、Stripe Billing

**差异化（一句）**：Clink = **编排 + 计费 + 全球本地化 + Agent 支付** 一体，而非单一 PSP 或纯 MoR。

*矩阵* → [clink-competitors.md](./clink-competitors.md)

---

## 7. 网站结构（摘要）

| 路径 | 说明 |
|------|------|
| `/` | 首页：Feature + 客户证言 + 合作伙伴 |
| `/products/billing` | Billing |
| `/products/payment` | Global Payments |
| `/products/routing` | Smart Routing |
| `/agentic-payment` | Agent 经济（canonical） |
| `/skills` | Skill Marketplace |
| `/contact` | Contact us |
| 导航 | Home · Skill Marketplace · Products · Contact · Login |
| 页脚 | Billing / Routing / Payment / Support → docs |
| 文档 | docs.clinkbill.com（Quickstart、Guides、API Reference） |

*完整 IA 与文档站结构* → [clink-site-structure.md](./clink-site-structure.md)

---

## 8. 社会证明（官网证言，2026-06-04）

| 客户/发言人 | 公司（官网展示） | 主题 |
|-------------|------------------|------|
| Ruby Xu | BlockSec | 全球 SaaS、多支付方式、响应快 |
| Dominic | GeeLark | 编排 + 订阅、成功率与合规协作 |
| JK | Linkloud | 跨境运营效率、转化与收入增长 |
| Silvirex | VoiSpark | 一体化支付与订阅 |
| Veritas | Gazolab | 路由与重试减少收入损失 |
| Kevin | Virax.ai | 本地化支付加速国际化 |
| Ronald | ZingFront | 运营效率、统一平台 |
| Silas | NovaSonic | 订阅场景深度理解 |

*对外引用建议标注「来源：clinkbill.com 官网证言，日期 2026-06-04」*

---

## 9. 优化建议

1. **补 sitemap**：`/agentic-payment`、`/skills`；更新 lastmod。
2. **定价页**：拦截 *subscription billing pricing*；当前费率 **待验证** 公开程度。
3. **对比内容**：`/vs/stripe`、`/vs/paddle` 承接商业意图（见 keywords）。
4. **开发者 SEO**：docs 与 `llms.txt` 已友好，可增加 `/developers` 营销枢纽链到 Quickstart。
5. **中文内容**：`/zh-CN` 镜像已上线；可优化 hreflang 与 sitemap 收录。

---

## 10. 调研 Backlog

| ID | 需查证 | 优先级 |
|----|--------|--------|
| R1 | 公开定价表、费率 vs Stripe/Paddle | P0 |
| R2 | MoR 与否及税务代缴司法范围 | P0 |
| R3 | 完整 PSP 支持列表（文档 dropdown） | P1 |
| R4 | Agentic Payments GA 时间与 Skill 仓库维护方 | P1 |
| R5 | 与 Chargebee 的功能边界（纯计费 vs 全栈） | P2 |

---

*文档创建：2026-06-04 | 最近复核：2026-07-21 | 来源： [clinkbill.com](https://clinkbill.com/)、[docs.clinkbill.com](https://docs.clinkbill.com/)、[clink-site-structure.md](./clink-site-structure.md)*
