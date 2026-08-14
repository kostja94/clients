# Clink 网站结构

> **本文档职责**：URL、导航、阶段规划；来源 [clinkbill.com](https://clinkbill.com/)（**复核 2026-07-21**）。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[clink.md](./clink.md) | [clink-keywords.md](./clink-keywords.md)

**Last updated**: 2026-07-21 | 模式：冷启动 → 线上 IA 已扩充

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [clink.md](./clink.md) |
| 关键词 | [clink-keywords.md](./clink-keywords.md) |
| 增长策略 | [clink-growth-strategy.md](./clink-growth-strategy.md) |
| 文档站 IA | 本文 §七（[docs.clinkbill.com](https://docs.clinkbill.com/)） |

---

## 一、当前线上 IA（2026-07-21 实测）

### 已上线页面总表

| 路径 | 标题 / 用途 | Sitemap | 备注 |
|------|-------------|---------|------|
| [/](https://clinkbill.com/) | 首页 | ✅ | 默认 locale `en-US`（无前缀） |
| [/products/billing](https://clinkbill.com/products/billing) | Subscription Billing | ✅ | |
| [/products/payment](https://clinkbill.com/products/payment) | Global Payment Infrastructure | ✅ | 2026-06 文档缺失，已上线 |
| [/products/routing](https://clinkbill.com/products/routing) | Smart Routing | ✅ | |
| [/agentic-payment](https://clinkbill.com/agentic-payment) | Agent Economy / Agentic Payments | ❌ | **canonical**；Early Access |
| [/skills](https://clinkbill.com/skills) | Skill Marketplace | ❌ | Agent Payment skills 聚合页 |
| [/contact](https://clinkbill.com/contact) | Contact us | ✅ | |
| [/privacy](https://clinkbill.com/privacy) | Privacy Policy | ✅ | |
| [/terms](https://clinkbill.com/terms) | Terms of Service | ✅ | |

**Sitemap**：`https://www.clinkbill.com/sitemap.xml`（18 URL，`lastmod` 2026-01-04，滞后于 Agent/Skills 页面上线）。

### 重定向

| 源路径 | 目标 | 类型 |
|--------|------|------|
| `/clink-for-claw` | `/agentic-payment` | 308 Permanent |
| `/products` | `/products/billing` | 307 Temporary |

内链与 SEO **canonical 一律用 `/agentic-payment`**，勿再写 `/clink-for-claw` 为新链。

### 主导航

| 标签 | 路径 / 目标 |
|------|-------------|
| Home | `/` |
| Skill Marketplace | `/skills`（带 New 角标） |
| Products | 下拉 → Billing / Payment / Routing |
| Contact us | `/contact` |
| Login | `https://uat-dashboard.clinkbill.com/auth/register` |

**Products 下拉**

| 标签 | 路径 |
|------|------|
| Billing | `/products/billing` |
| Payment | `/products/payment` |
| Smart Routing | `/products/routing` |

**Support**：无独立页（`/support` → 404）；页脚链到 docs。

首页 Hero CTA「Explore Agentic Payments」→ `/agentic-payment`。

### 页脚信息架构

| 分组 | 链接项（目标路径） |
|------|-------------------|
| **Billing** | [Subscription](/products/billing#subscription-management)、[Customer Portal](/products/billing#customer-portal)、[Coupon](/products/billing#coupon)、[Tax Compliance](/products/billing#tax-compliance) |
| **Smart Routing** | [Dynamic Routing](/products/routing#dynamic-routing)、[Automatic Retries](/products/routing#automatic-retries)、[Customizable Rules](/products/routing#customizable-routing-rules-with-priority) |
| **Payment** | [Hosted Checkout](/products/payment#hosted-checkout)、[Global Coverage](/products/payment#global-coverage)、[PCI Compliant](/products/payment#pci-compliant)、[Fraud Prevention](/products/payment#fraud-prevention) |
| **Support** | [API Reference](https://docs.clinkbill.com/api-reference)、[Documentation](https://docs.clinkbill.com/) |
| 社交 | [LinkedIn](https://www.linkedin.com/company/clinkbill)、[X](https://x.com/clinkglobal)、[小红书](https://www.xiaohongshu.com/user/profile/69b258ef000000003302109e) |
| Legal | [Privacy](/privacy)、[Terms](/terms) |

### 多语言（i18n）

| 配置 | 说明 |
|------|------|
| 默认 locale | `en-US`（URL 无前缀） |
| 中文 | `/zh-CN` 前缀镜像全站路径（如 `/zh-CN/products/billing`） |
| Sitemap | **未收录** locale 变体；需 hreflang / canonical 策略跟进 |

### 外部触点

| 触点 | URL |
|------|-----|
| 文档 | https://docs.clinkbill.com/ |
| API / OpenAPI | https://docs.clinkbill.com/api-reference |
| LLM 索引 | https://docs.clinkbill.com/llms.txt |
| 商户后台（Login CTA） | https://uat-dashboard.clinkbill.com/auth/register |
| Agent Skill 仓库 | https://github.com/clinkbillcom/agentic-payment-skills |

> 文档站完整 IA 见 **§七**。

### 确认未上线（404）

| 路径 | 说明 |
|------|------|
| `/blog`、`/blog/*` | 本地有草稿，线上未发布 |
| `/support` | 无独立页 |
| `/pricing` | Phase 2 规划 |
| `/vs/stripe`、`/vs/paddle` | Phase 2 |
| `/for/saas`、`/for/ai-apps` | Phase 2 |
| `/developers`、`/learn/*`、`/customers/*` | Phase 2/3 |

---

## 二、核心路径表

| 路径 | 用户目标 | 现状 |
|------|----------|------|
| 品牌 | 了解 Clink → Contact / Login | 首页完整 |
| 选型 | billing vs stripe → `/products/billing` | 有产品页 |
| 支付覆盖 | 全球支付方式 → `/products/payment` | 已上线 |
| 性能 | 降失败率 → `/products/routing` | 有产品页 |
| Agent | Agent 充值 / OpenClaw → `/agentic-payment` | Early Access；旧 URL 308 |
| Skills | 浏览 Agent Payment skills → `/skills` | 已上线 |
| 商务 | 联系销售 → `/contact` | 已上线 |
| 开发 | 集成 → docs Quickstart | 有文档 |
| 信任 | 案例 → 首页 Testimonials | 已有多条 |
| 法务 | Privacy / Terms | 已上线 |

---

## 三、首页模块（内容架构）

1. Hero：Subscriptions & Payments Solution + CTA（Contact Now / Explore Agentic Payments）  
2. Why Clink：Global Coverage、Secure、Optimize Costs、Seamless Integration  
3. 价值块：All-in-One Billing、Subscription Support、Merchant of Record 叙事、One Integration Boundless Connections  
4. Cooperation partners（Logo 墙：Stripe、Adyen、Airwallex 等）  
5. Trusted by Product Builders（证言轮播）  
6. Footer 四列（Billing / Routing / Payment / Support）+ Legal + 版权  

---

## 四、分阶段建议（SEO 增量）

### Phase 1 — 已有，优化内链

- 三大产品页 + `/agentic-payment` + `/skills` 互链 + 统一 CTA（Contact / Login）  
- 首页 Feature / Hero 锚点链到对应子页 H2  
- **补 sitemap**：`/agentic-payment`、`/skills`  
- **旧链迁移**：全站 `/clink-for-claw` → `/agentic-payment`（含 docs、blog 草稿）

### Phase 2 — 建议新建

| 路径 | 目的 |
|------|------|
| `/pricing` | 商业意图 |
| `/vs/stripe` | 对比 |
| `/vs/paddle` | 对比 |
| `/for/saas` | 场景 |
| `/for/ai-apps` | 场景 |
| `/developers` | 枢纽链 docs |

### Phase 3 — 内容与 GEO

| 路径 | 目的 |
|------|------|
| `/blog` | 长尾、路由最佳实践 |
| `/learn/mor-vs-orchestration` | 教育 |
| `/customers/{slug}` | 案例详情（BlockSec 等） |

---

## 五、技术架构（推断）

| 层 | 说明 |
|----|------|
| 营销站 | Next.js SPA/静态站；i18n（en-US / zh-CN） |
| 商户后台 | `uat-dashboard.clinkbill.com`（Login CTA 指向 register） |
| API | REST + Webhook；UAT/Production 分离 |
| 文档 | Mintlify 类站（llms.txt 特征） |
| CDN | CloudFront（响应头可见） |

---

## 六、SEO 建议

| 项 | 建议 |
|----|------|
| Title | 各产品页独立 title（已具备） |
| Schema | Organization、SoftwareApplication、Review（证言） |
| docs ↔ marketing | 双向链接，避免 docs 抢品牌词 |
| Agent 页 | FAQPage + HowTo（4 步 flow，页面已有） |
| canonical | 主域 `clinkbill.com` / `www.clinkbill.com` 共存；robots Host 指向 www |
| sitemap | 补录 agentic-payment、skills；更新 lastmod；评估 zh-CN hreflang |
| 301/308 | 保留 `/clink-for-claw` → `/agentic-payment`；内链统一 canonical |

---

## 七、文档站 IA（docs.clinkbill.com）

> 来源：[llms.txt](https://docs.clinkbill.com/llms.txt)（**复核 2026-07-21**）。Mintlify 类文档站，与营销站分离；页脚 Support 列链入。

### 与营销站映射

| 营销站 | 文档承接 |
|--------|----------|
| `/products/payment` | [Checkout Session](https://docs.clinkbill.com/guides/payments/checkout_session)、[Currencies](https://docs.clinkbill.com/guides/payments/currencies) |
| `/products/routing` | 路由能力以 API + Dashboard 为主；无独立 routing 指南页 |
| `/products/billing` | [Subscription](https://docs.clinkbill.com/guides/resources/subscription)、[Customer Portal](https://docs.clinkbill.com/guides/billing/customer_portal)、[Coupon](https://docs.clinkbill.com/guides/resources/coupon) |
| `/agentic-payment` | [Create Agent Payment Session](https://docs.clinkbill.com/api-reference/endpoint/create-agent-payment-session) API |
| `/skills` | [Skill Marketplace 指南](https://docs.clinkbill.com/guides/agent/skill_marketplace) |
| 开发集成 | [Quickstart](https://docs.clinkbill.com/quickstart)、[Integration](https://docs.clinkbill.com/integration) |
| Link PSP | [Link External Account](https://docs.clinkbill.com/guides/payments/link_psp) |

### 入门

| 页面 | URL | 用途 |
|------|-----|------|
| Introduction | [/index](https://docs.clinkbill.com/index) | 文档首页 |
| Quickstart | [/quickstart](https://docs.clinkbill.com/quickstart) | 首笔 Checkout Session |
| Integration | [/integration](https://docs.clinkbill.com/integration) | Test → Production 环境切换 |

### 指南（Guides）

| 分组 | 页面 | URL |
|------|------|-----|
| **Account** | Merchant | [/guides/account/merchant](https://docs.clinkbill.com/guides/account/merchant) |
| | User | [/guides/account/user](https://docs.clinkbill.com/guides/account/user) |
| **Billing** | Customer Portal | [/guides/billing/customer_portal](https://docs.clinkbill.com/guides/billing/customer_portal) |
| **Payments** | Checkout Session | [/guides/payments/checkout_session](https://docs.clinkbill.com/guides/payments/checkout_session) |
| | Currencies | [/guides/payments/currencies](https://docs.clinkbill.com/guides/payments/currencies) |
| | Link External Account | [/guides/payments/link_psp](https://docs.clinkbill.com/guides/payments/link_psp) |
| **Resources** | Subscription | [/guides/resources/subscription](https://docs.clinkbill.com/guides/resources/subscription) |
| | Product & Price | [/guides/resources/product](https://docs.clinkbill.com/guides/resources/product) |
| | Customer | [/guides/resources/customer](https://docs.clinkbill.com/guides/resources/customer) |
| | Order | [/guides/resources/order](https://docs.clinkbill.com/guides/resources/order) |
| | Refund | [/guides/resources/refund](https://docs.clinkbill.com/guides/resources/refund) |
| | Coupon | [/guides/resources/coupon](https://docs.clinkbill.com/guides/resources/coupon) |
| **Agent** | Skill Marketplace | [/guides/agent/skill_marketplace](https://docs.clinkbill.com/guides/agent/skill_marketplace) |

### 财务（Finance）

| 页面 | URL |
|------|-----|
| Balance | [/finance/balance](https://docs.clinkbill.com/finance/balance) |
| Payout | [/finance/payout](https://docs.clinkbill.com/finance/payout) |

### API Reference

| 类别 | 页面 | URL |
|------|------|-----|
| 总览 | Introduction | [/api-reference/introduction](https://docs.clinkbill.com/api-reference/introduction) |
| OpenAPI | openapi.json | [/api-reference/openapi.json](https://docs.clinkbill.com/api-reference/openapi.json) |
| SDK | TypeScript SDK | [/api-reference/SDK](https://docs.clinkbill.com/api-reference/SDK) |
| | JavaScript SDK | [/api-reference/javascript_sdk](https://docs.clinkbill.com/api-reference/javascript_sdk) |
| | Clink CLI | [/api-reference/clink_cli](https://docs.clinkbill.com/api-reference/clink_cli) |

**核心 Endpoints（按域）**

| 域 | 代表 Endpoint |
|----|---------------|
| 支付 | Create/Get Checkout Session、Create Payment、Create Payment Instrument |
| 订阅 | Create/Cancel/Get Subscription、Create Product/Price |
| 计费 | Customer Portal Session、Create Coupon/Promotion Code |
| Agent | Create/Get Agent Payment Session |
| 测试 | Test Clock（create/advance/complete/list） |
| Webhook | Create/List/Update Webhook Endpoint；Events 列表 |
| 退款 | Create/Get Refund |

完整 Endpoint 列表见 [llms.txt](https://docs.clinkbill.com/llms.txt)（40+ 页）。

### Webhook 事件

| 事件 | URL |
|------|-----|
| session | [/api-reference/webhook/session](https://docs.clinkbill.com/api-reference/webhook/session) |
| subscription | [/api-reference/webhook/subscription](https://docs.clinkbill.com/api-reference/webhook/subscription) |
| invoice | [/api-reference/webhook/invoice](https://docs.clinkbill.com/api-reference/webhook/invoice) |
| order | [/api-reference/webhook/order](https://docs.clinkbill.com/api-reference/webhook/order) |
| refund | [/api-reference/webhook/refund](https://docs.clinkbill.com/api-reference/webhook/refund) |
| dispute | [/api-reference/webhook/dispute](https://docs.clinkbill.com/api-reference/webhook/dispute) |
| customer.verify | [/api-reference/webhook/customer.verify](https://docs.clinkbill.com/api-reference/webhook/customer.verify) |

### docs SEO / 内链建议

| 项 | 建议 |
|----|------|
| 营销 ↔ docs | 产品页 CTA 链 Quickstart；docs 首页链回 clinkbill.com 产品页 |
| llms.txt | 已上线，利于 Agent/GEO 索引；保持与 sitemap 同步 |
| 品牌词 | docs 标题避免抢「Clink billing」等品牌 SERP |
| Agent | Quickstart 旁链 `/agentic-payment` 与 Skill Marketplace 指南 |

---

*与 [clink-keywords.md](./clink-keywords.md) 状态列同步维护*
