# Clink 关键词映射

> **本文档职责**：搜什么、意图、目标 URL/载体、优先级。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[clink.md](./clink.md) | [clink-features.md](./clink-features.md) | [clink-site-structure.md](./clink-site-structure.md)

**Last updated**: 2026-07-21 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [clink.md](./clink.md) |
| 功能 | [clink-features.md](./clink-features.md) |
| 使用场景 | [clink-use-cases.md](./clink-use-cases.md) |
| 竞品 | [clink-competitors.md](./clink-competitors.md) |
| 网站结构 | [clink-site-structure.md](./clink-site-structure.md) |
| 增长策略 | [clink-growth-strategy.md](./clink-growth-strategy.md) |

---

## 一、品牌词

| 关键词 | 意图 | 目标页 | 优先级 | 状态 |
|--------|------|--------|--------|------|
| Clink | 品牌 | / | P0 | 已承接 |
| clinkbill | 品牌 | / | P0 | 已承接 |
| Clink billing | 品牌 | /products/billing | P0 | 已承接 |
| clink payment | 品牌 | / | P0 | 已承接 |
| docs clinkbill | 支持 | docs.clinkbill.com | P1 | 已承接 |

---

## 二、核心定位（Primary）

| 关键词 | 意图 | 目标页 | 优先级 | 状态 |
|--------|------|--------|--------|------|
| subscription billing software | 商业 | /products/billing | P0 | 已承接 |
| payment orchestration platform | 商业 | /products/routing | P0 | 已承接 |
| global payment platform | 商业 | / | P0 | 已承接 |
| recurring billing platform | 商业 | /products/billing | P0 | 已承接 |
| payment routing software | 商业 | /products/routing | P1 | 已承接 |
| hosted checkout SaaS | 商业 | /products/payment + docs/checkout_session | P1 | 已承接 |
| subscription management platform | 商业 | /products/billing | P1 | 已承接 |
| multi currency billing | 商业 | /products/billing | P1 | 已承接 |

---

## 三、Secondary

| 关键词 | 意图 | 目标页 | 优先级 | 状态 |
|--------|------|--------|--------|------|
| automatic payment retry | 商业 | /products/routing | P0 | 已承接 |
| dynamic payment routing | 商业 | /products/routing | P0 | 已承接 |
| customer portal subscription | 商业 | /products/billing | P1 | 已承接 |
| global tax compliance billing | 商业 | /products/billing | P1 | 已承接 |
| usage based billing platform | 商业 | / | P1 | 首页提及 |
| PCI compliant payment gateway | 信任 | / | P1 | 已承接 |
| payment failover gateway | 商业 | /products/routing | P2 | 已承接 |
| local payment methods SaaS | 商业 | / | P1 | 已承接 |
| clink for claw | 品牌/产品 | /agentic-payment | P0 | 已承接 |
| agentic payment | 商业 | /agentic-payment | P0 | 已承接 |

---

## 四、Long-tail

| 关键词 | 意图 | 目标页 | 优先级 | 状态 |
|--------|------|--------|--------|------|
| stripe alternative subscription billing | 对比 | /vs/stripe | P0 | 待建 |
| paddle alternative | 对比 | /vs/paddle | P1 | 待建 |
| connect multiple payment processors | 教程 | docs/link_psp | P1 | 已承接 |
| reduce failed subscription payments | 商业 | /products/routing | P0 | 已承接 |
| SaaS billing for global expansion | 商业 | /for/saas | P1 | 待建 |
| AI agent automatic top up payment | 商业 | /agentic-payment | P0 | 已承接 |
| payment orchestration vs payment gateway | 教育 | /learn/orchestration-vs-gateway | P2 | 待建 |
| subscription billing for indie developers | 商业 | /for/indie | P2 | 待建 |
| openclaw payment integration | 商业 | /agentic-payment | P1 | 已承接 |
| clink checkout session api | 技术 | docs/quickstart | P1 | 已承接 |

---

## 五、意图分类（≥4 类）

| 意图类型 | 代表词量 | 主承接 |
|----------|----------|--------|
| **品牌** | 5+ | /、docs |
| **计费/订阅** | 8+ | /products/billing |
| **支付编排** | 7+ | /products/routing |
| **对比/选型** | 5+ | /vs/*、/alternatives |
| **开发者** | 6+ | docs、Quickstart |
| **Agent/AI** | 5+ | /agentic-payment |

---

## 六、JTBD → 承接

| JTBD | 典型问法 | 优先级 | 建议承接 |
|------|----------|--------|----------|
| 降低跨境支付失败率 | improve payment success rate saas | P0 | /products/routing |
| 统一订阅与收款 | all in one billing and payments | P0 | /products/billing |
| 接 Stripe 但想加备用通道 | multi psp stripe airwallex | P1 | docs/link_psp |
| Agent 运行中要自动充值 | agent payment claw top up | P0 | /agentic-payment |
| 全球税务不想自己搞 | saas tax compliance billing | P1 | /products/billing#tax |
| 快速上线结账 | hosted checkout api minutes | P1 | docs/quickstart |

---

## 七、待办

| 待办 | 说明 |
|------|------|
| 创建 /vs/stripe、/vs/paddle | P0 对比流量 |
| /pricing 公开页 | 拦截 pricing 意图 |
| /for/saas、/for/ai-apps | 对齐官网 Customers 叙事 |
| 博客：orchestration vs MoR vs PSP | 教育长尾 |
| GEO：best payment orchestration platform 2026 | 结构化 FAQ |

---

*与 [clink-competitors.md](./clink-competitors.md) 对比词联动*
