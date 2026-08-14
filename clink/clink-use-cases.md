# Clink 使用场景

> **本文档职责**：**谁**在**什么情境**用；能力见 [clink-features.md](./clink-features.md)。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[clink.md](./clink.md) | [clink-keywords.md](./clink-keywords.md)

**Last updated**: 2026-07-21 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [clink.md](./clink.md) |
| 功能 | [clink-features.md](./clink-features.md) |
| 关键词 | [clink-keywords.md](./clink-keywords.md) |
| 竞品 | [clink-competitors.md](./clink-competitors.md) |
| 网站结构 | [clink-site-structure.md](./clink-site-structure.md) |
| 增长策略 | [clink-growth-strategy.md](./clink-growth-strategy.md) |

---

## 一、Persona（≥3）

### Persona 1：全球 SaaS 增长负责人（RevOps）

| 字段 | 内容 |
|------|------|
| **谁** | VP Growth / Head of RevOps，ARR $1M–$50M，多国客户 |
| **目标** | 提升续费成功率、减少 involuntary churn |
| **痛点** | 单 PSP 区域失败率高；续费重试策略分散 |
| **常用功能** | Smart Routing、Automatic Retries、Billing |
| **落地页** | `/for/saas` |
| **关键词** | reduce failed subscription payments, payment orchestration |

**JTBD**

1. 某国卡组织 decline 率高 → 配置 backup gateway + 重试规则  
2. 财报前要统一订阅与支付报表 → 单一 Dashboard  

### Persona 2：支付工程师 / 后端 Tech Lead

| 字段 | 内容 |
|------|------|
| **谁** | 负责支付栈的 Senior Engineer |
| **目标** | 接 API、Webhook、沙箱、少踩 PCI 坑 |
| **痛点** | 多 PSP 集成重复劳动；UAT/Prod 环境混乱 |
| **常用功能** | Checkout Session API、Link PSP、Test Clock、Webhook |
| **落地页** | `/developers`（建议）→ docs |
| **关键词** | clink api, checkout session, link stripe airwallex |

**JTBD**

1. 两天内上线 Hosted Checkout → Quickstart + SDK  
2. 生产前模拟订阅续费 → Test Clock advance  

### Persona 3：AI / Agent 产品负责人

| 字段 | 内容 |
|------|------|
| **谁** | AI App、Agent 运行时（如 OpenClaw 生态）PM |
| **目标** | 用户 Agent 余额不足时自动充值，有预算上限 |
| **痛点** | 自建支付风控复杂；人工充值打断任务 |
| **常用功能** | Agent Payment Session、Agentic Payments、Spend limits |
| **落地页** | `/agentic-payment`、`/skills` |
| **关键词** | agentic payment, autonomous top-up |

**JTBD**

1. 图像生成任务中途余额不足 → 60 秒内完成 top-up 恢复（官网流程叙事）  
2. 设每日充值上限防 Agent 超支 → Risk rules  

### Persona 4：亚太出海 Indie / 小团队创始人

| 字段 | 内容 |
|------|------|
| **谁** | 国内或亚太注册主体，面向全球卖 SaaS/工具 |
| **目标** | 快速接美元收款、托管页、少碰税务坑 |
| **痛点** | Stripe 主体门槛；从零拼 Tax + Webhook |
| **常用功能** | Hosted Checkout、Tax、Contact/KYB |
| **落地页** | `/for/indie` |
| **关键词** | global saas payments, hosted checkout |

**JTBD**

1. Vibe Coding 平台（Lovable 等）一天接支付 → docs + Agent playbook  
2. 要链接既有 Stripe 账户 → Link PSP  

---

## 二、场景-功能-关键词映射

| 场景 | Persona | 功能 | 关键词 | URL |
|------|---------|------|--------|-----|
| 续费失败挽回 | RevOps | Routing/Retries | automatic payment retry | /products/routing |
| 多国标价订阅 | RevOps | Billing multi-currency | multi currency subscription | /products/billing |
| 自助升降级 | CS/RevOps | Customer Portal | subscription customer portal | /products/billing |
| 促销上线 | Marketing | Coupon | subscription coupon software | /products/billing |
| Agent 充值 | AI PM | Agentic Payments | agentic payment | /agentic-payment |
| 双 PSP 容灾 | Engineer | Link PSP + Routing | payment failover | docs/link_psp |
| 快速首单 | Indie | Checkout Session | hosted checkout api | docs/quickstart |

---

## 三、/for/* 规划

| 路径 | Persona | 优先级 |
|------|---------|--------|
| `/for/saas` | RevOps | P0 |
| `/for/ai-apps` | AI 产品 | P0 |
| `/for/indie` | 亚太 indie | P1 |
| `/for/agencies` | Agency（官网 Customers） | P2 |
| `/for/gaming` | 游戏（官网列举） | P2 |

---

## 四、用户旅程（SaaS 订阅）

```mermaid
flowchart LR
  A[选型对比] --> B[Contact / Sign up]
  B --> C[Link PSP + KYB]
  C --> D[Create Product/Price]
  D --> E[Checkout Session 上线]
  E --> F[Webhook 驱动权益]
  F --> G[Routing 优化续费]
```

---

## 五、缺口识别

| 缺口 | 建议 |
|------|------|
| 缺公开 /pricing | 拦截 commercial 意图 |
| /for/* 未上线 | 用 Customers 证言块临时承接 |
| 中文信任内容少 | 亚太案例页（GeeLark、Linkloud） |

---

*与 [clink-growth-strategy.md](./clink-growth-strategy.md) 对齐*
