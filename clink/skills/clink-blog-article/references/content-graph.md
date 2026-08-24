# Clink Blog — Content Graph

> 加载时机：Phase 0（选题）· Phase 2（路径/日期）· Phase 5.5
> 主文件：SKILL.md §4 · 下一序号：**24**（根目录）；agentic-payments 协议 definition 系列 **26–29, 33**

---

## 1. 文件表

| NN | 文件 | slug | 类型 | category | 日期 | 主关键词 |
|----|------|------|------|----------|------|---------|
| 01 | 01-what-is-clink.md | what-is-clink | BrandIntroduction | Product | 2026-06-23 | Clink, payment infrastructure |
| 02 | 02-mor-vs-psp.md | mor-vs-psp | Comparison | Comparison | 2026-06-29 | MoR vs PSP |
| 03 | 03-smart-routing.md | smart-routing | Product | Product | 2026-06-29 | smart payment routing |
| 04 | agentic-payments/04-agent-payments.md | agent-payments | Opinion | Agentic Payments | 2026-06-29 | agent payments |
| 05 | 05-how-to-add-payments-lovable-app.md | how-to-add-payments-lovable-app | Product | Product | 2026-07-22 | how to add payments to lovable app |
| 06 | 06-integrate-stripe-lovable.md | integrate-stripe-lovable | Product | Product | 2026-07-23 | integrate stripe lovable |
| 07 | 07-how-to-add-payments-bolt-app.md | how-to-add-payments-bolt-app | Product | Product | 2026-07-24 | how to add payments to bolt.new app |
| 08 | 08-how-to-add-payments-v0-app.md | how-to-add-payments-v0-app | Product | Product | 2026-07-25 | how to add payments to v0 app |
| 09 | 09-how-to-add-payments-replit-app.md | how-to-add-payments-replit-app | Product | Product | 2026-07-26 | how to add payments to replit app |
| 10 | 10-burn-rate.md | burn-rate | GlossaryTerm | Glossary | 2026-07-27 | what is a burn rate |
| 11 | 11-annual-recurring-revenue.md | annual-recurring-revenue | GlossaryTerm | Glossary | 2026-07-28 | arr meaning |
| 12 | 12-monthly-recurring-revenue.md | monthly-recurring-revenue | GlossaryTerm | Glossary | 2026-07-29 | what is mrr |
| 13 | 13-net-revenue-retention.md | net-revenue-retention | GlossaryTerm | Glossary | 2026-07-30 | what is nrr |
| 14 | 14-runway.md | runway | GlossaryTerm | Glossary | 2026-07-31 | what is runway |
| 15 | industry-news/15-cloudflare-wallets-agent-payments.md | cloudflare-wallets-agent-payments | IndustryNews | Industry News | 2026-08-04 | Cloudflare Wallets, agent payments |
| 26 | agentic-payments/26-what-is-ap2-agent-payments-protocol.md | what-is-ap2-agent-payments-protocol | Research | Agentic Payments | 2026-09-07 | AP2 agent payments protocol |
| 27 | agentic-payments/27-what-is-x402.md | what-is-x402 | Research | Agentic Payments | 2026-09-08 | x402 agent payments |
| 28 | agentic-payments/28-what-is-machine-payments-protocol.md | what-is-machine-payments-protocol | Research | Agentic Payments | 2026-09-09 | Machine Payments Protocol MPP |
| 29 | agentic-payments/29-what-is-agentic-commerce-protocol.md | what-is-agentic-commerce-protocol | Research | Agentic Payments | 2026-09-10 | Agentic Commerce Protocol ACP |
| 33 | agentic-payments/33-what-is-universal-commerce-protocol.md | what-is-universal-commerce-protocol | Research | Agentic Payments | 2026-09-11 | Universal Commerce Protocol UCP |
| 31 | agentic-payments/31-how-to-sell-on-chatgpt.md | how-to-sell-on-chatgpt | HowTo | Agentic Payments | 2026-09-12 | how to sell on ChatGPT merchant |
| 16 | 16-what-is-skill-marketplace.md | what-is-skill-marketplace | Product | Product | 2026-08-05 | what is a skill marketplace |
| 17 | 17-clink-launches-skill-marketplace.md | clink-launches-skill-marketplace | Product | Product | 2026-08-06 | monetize agent skills |
| 18 | industry-news/18-stripe-openrouter-acquisition.md | stripe-openrouter-acquisition | IndustryNews | Industry News | 2026-08-18 | Stripe OpenRouter acquisition |
| 19 | 19-best-ai-companies-by-arr.md | best-ai-companies-by-arr | Comparison | Comparison | 2026-08-19 | AI companies by ARR |
| 20 | 20-fastest-growing-ai-companies-arr.md | fastest-growing-ai-companies-arr | Comparison | Comparison | 2026-08-20 | fastest growing AI companies ARR |
| 21 | stripe-risk/21-what-is-stripe-dispute.md | what-is-stripe-dispute | StripeRisk | Stripe Risk | 2026-09-04 | what is a Stripe dispute |
| 22 | stripe-risk/22-how-to-dispute-stripe-charge.md | how-to-dispute-stripe-charge | StripeRisk | Stripe Risk | 2026-09-05 | how to dispute Stripe charge |
| 23 | stripe-risk/23-stripe-chargeback-prevention.md | stripe-chargeback-prevention | StripeRisk | Stripe Risk | 2026-09-06 | Stripe chargeback prevention |
| 25 | stripe-risk/25-stripe-account-suspended.md | stripe-account-suspended | StripeRisk | Stripe Risk | 2026-09-01 | Stripe account suspended |
| 30 | stripe-risk/30-why-stripe-closes-accounts.md | why-stripe-closes-accounts | StripeRisk | Stripe Risk | 2026-09-02 | why Stripe closed my account |
| 32 | stripe-risk/32-how-to-appeal-stripe-account-closure.md | how-to-appeal-stripe-account-closure | StripeRisk | Stripe Risk | 2026-09-03 | appeal Stripe account closed |

**下一序号：24**（根目录 pipeline；stripe-risk 账户子系列保留 25/30/32 跳号）

**序号规则（2026-08-24）**：
- **19–20** 根目录 Comparison（AI ARR 双文）
- **21–23** `stripe-risk/` 争议/拒付子系列（Hub → HowTo → Prevention）
- **25/30/32** `stripe-risk/` 账户限制子系列（已入库，序号不变）

**S-grade rewrite (2026-07-23)**: Titles normalized to em dash form; slugs unchanged. Anti-clone contract for 05–09: `references/series-canonical-ownership.md`.

---

## 1B. Cluster 注册表（文件路径路由）

> Phase 0/2 对照本表决定 `clink/blog/[{folder}]NN-{slug}.md`。
> 公开 URL 始终 `/blog/{slug}`。规则详见 `E:\Agent执行\blog-create\references\topic-cluster-layout.md`。

| Cluster ID | folder | Hub slug | 主 category | 说明 |
|------------|--------|----------|-------------|------|
| core | *(root)* | what-is-clink | Product / Comparison / Opinion | 01–03, 16–17, 19–20 |
| glossary-metrics | *(root)* | burn-rate | Glossary | 10–14 |
| lovable-series | *(root)* | how-to-add-payments-lovable-app | Product | 05–09 |
| agentic-payments | `agentic-payments/` | agent-payments | Agentic Payments + secondaryCategory | 04, 26–29, 33 |
| industry-news | `industry-news/` | stripe-openrouter-acquisition | Industry News + secondaryCategory | 15, 18 |
| stripe-risk-disputes | `stripe-risk/` | what-is-stripe-dispute | Stripe Risk + secondaryCategory | 21–23 争议/拒付 |
| stripe-risk-accounts | `stripe-risk/` | stripe-account-suspended | Stripe Risk + secondaryCategory | 25, 30, 32 账户限制 |

**standalone 判定**：不在上表 cluster 内 → `folder = (root)`。

---

## 日期占用表（Phase 2 避让）

| 日期 | 已占用 slug |
|------|-----------|
| 2026-06-23 | what-is-clink |
| 2026-06-29 | mor-vs-psp, smart-routing, agent-payments |
| 2026-07-22 | how-to-add-payments-lovable-app |
| 2026-07-23 | integrate-stripe-lovable |
| 2026-07-24 | how-to-add-payments-bolt-app |
| 2026-07-25 | how-to-add-payments-v0-app |
| 2026-07-26 | how-to-add-payments-replit-app |
| 2026-07-27 | burn-rate |
| 2026-07-28 | annual-recurring-revenue |
| 2026-07-29 | monthly-recurring-revenue |
| 2026-07-30 | net-revenue-retention |
| 2026-07-31 | runway |
| 2026-08-04 | cloudflare-wallets-agent-payments |
| 2026-08-05 | what-is-skill-marketplace |
| 2026-08-06 | clink-launches-skill-marketplace |
| 2026-08-18 | stripe-openrouter-acquisition |
| 2026-08-19 | best-ai-companies-by-arr |
| 2026-08-20 | fastest-growing-ai-companies-arr |
| 2026-09-01 | stripe-account-suspended |
| 2026-09-02 | why-stripe-closes-accounts |
| 2026-09-03 | how-to-appeal-stripe-account-closure |
| 2026-09-04 | what-is-stripe-dispute |
| 2026-09-05 | how-to-dispute-stripe-charge |
| 2026-09-06 | stripe-chargeback-prevention |
| 2026-09-07 | what-is-ap2-agent-payments-protocol |
| 2026-09-08 | what-is-x402 |
| 2026-09-09 | what-is-machine-payments-protocol |
| 2026-09-10 | what-is-agentic-commerce-protocol |
| 2026-09-11 | what-is-universal-commerce-protocol |
| 2026-09-12 | how-to-sell-on-chatgpt |

新文从下一可用日错开，**每自然日 ≤1 篇**。

---

## Pipeline（待创作）

| slug | 类型 | 增长职能 | 目标关键词 | 优先级 |
|------|------|---------|-----------|--------|
| payment-orchestration-single-psp | Opinion | CategoryPOV | payment orchestration platform | P0 |
| clink-vs-stripe | EvaluationComparison | EvaluationComparison | stripe alternative subscription billing | P0 |
| reduce-involuntary-churn-routing | Product | SearchCapture | reduce failed subscription payments | P0 |

---

## 主题簇结构

```
Hub: what-is-clink (Brand canon)
 ├── mor-vs-psp (Comparison)
 ├── smart-routing (Product) ↔ mor-vs-psp
 ├── what-is-skill-marketplace (Product) → hub + agent-payments + clink-launches-skill-marketplace
 ├── clink-launches-skill-marketplace (Product) → hub + what-is-skill-marketplace
 ├── how-to-add-payments-lovable-app (Product) → hub + mor-vs-psp + smart-routing
 ├── integrate-stripe-lovable (Product) → how-to-add-payments-lovable-app + mor-vs-psp + hub
 ├── how-to-add-payments-bolt-app (Product) → hub + mor-vs-psp + smart-routing + how-to-add-payments-lovable-app
 ├── how-to-add-payments-v0-app (Product) → hub + mor-vs-psp + smart-routing + how-to-add-payments-lovable-app + how-to-add-payments-bolt-app
 ├── how-to-add-payments-replit-app (Product) → hub + mor-vs-psp + smart-routing + how-to-add-payments-lovable-app + how-to-add-payments-bolt-app + how-to-add-payments-v0-app

Agentic Payments cluster (`agentic-payments/`):
 Hub: agent-payments (04)
 └── Protocol definition series (Research, secondaryCategory):
     ├── what-is-ap2-agent-payments-protocol (26) → hub + x402 + mpp + acp + ucp
     ├── what-is-x402 (27) → hub + ap2 + mpp + cloudflare-wallets
     ├── what-is-machine-payments-protocol (28) → hub + x402 + ap2 + acp
     ├── what-is-agentic-commerce-protocol (29) → hub + ucp + mpp + ap2
     └── what-is-universal-commerce-protocol (33) → hub + acp + ap2 + agent-payments
 └── Merchant how-to (HowTo, secondaryCategory):
     └── how-to-sell-on-chatgpt (31) → hub + acp + ucp + mor-vs-psp + agent-payments

Industry News cluster (`industry-news/`):
 Hub: stripe-openrouter-acquisition (18)
 ├── cloudflare-wallets-agent-payments (15) → agent-payments + what-is-x402 + hub
 └── stripe-openrouter-acquisition (18) → agent-payments + cloudflare-wallets + what-is-clink

Pipeline spokes:
 ├── payment-orchestration-single-psp → hub + smart-routing
 ├── clink-vs-stripe → hub + mor-vs-psp + smart-routing
 └── reduce-involuntary-churn-routing → hub + smart-routing

Glossary cluster (category: Glossary):
 ├── annual-recurring-revenue ↔ burn-rate ↔ monthly-recurring-revenue ↔ net-revenue-retention ↔ runway（指标簇闭环）
 ├── burn-rate → what-is-clink + mor-vs-psp + annual-recurring-revenue + runway
 ├── annual-recurring-revenue → burn-rate + monthly-recurring-revenue + net-revenue-retention + smart-routing + what-is-clink
 ├── monthly-recurring-revenue → annual-recurring-revenue + burn-rate + what-is-clink
 ├── net-revenue-retention → annual-recurring-revenue + smart-routing + what-is-clink
 └── runway → burn-rate + annual-recurring-revenue + smart-routing + what-is-clink
```

---

## Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| What is Clink / 四产品线 | what-is-clink | 1–2 句 + related；禁止全文重写 |
| MoR vs PSP 选型 | mor-vs-psp | Comparison 文引用框架，不重复五维表全文 |
| Smart routing / multi-PSP | smart-routing | Product 文引用 3-5% 论证，不重复案例全文 |
| Agent-native payments | agent-payments | Opinion 文引用 Harness 模型摘要 |
| AP2 / x402 / MPP / ACP / UCP 协议定义 | what-is-ap2-agent-payments-protocol 等 26–29, 33 | Research 文互链；禁止重复 stack 表全文 |
| Skill marketplace 概念/生命周期 | what-is-skill-marketplace | Product 文引用类型学摘要，不重写状态机全文 |
| Skill 变现机制 | clink-launches-skill-marketplace | Product 文引用 webhook 结算摘要 |

---

## 冲突表（KEEP/MERGE 预检）

| 新选题 | vs 已有 | 判定 |
|--------|---------|------|
| what is clink | what-is-clink | **MERGE** |
| MoR vs PSP | mor-vs-psp | **MERGE** |
| smart payment routing | smart-routing | **MERGE** |
| clink vs stripe | clink-vs-stripe (pipeline) | KEEP if not yet written |
| payment orchestration | payment-orchestration-single-psp | KEEP（CategoryPOV 角度） |
| reduce involuntary churn | reduce-involuntary-churn-routing | KEEP（实操 SearchCapture） |
| what is skill marketplace | what-is-skill-marketplace | **MERGE** |
| clink launches / monetize agent skills | clink-launches-skill-marketplace | KEEP（发布/变现角度） |

---

## 推荐正文互链（非 frontmatter）

| slug | 建议正文链向 |
|------|-------------|
| what-is-clink | mor-vs-psp, smart-routing, agent-payments, how-to-add-payments-lovable-app |
| mor-vs-psp | what-is-clink, smart-routing |
| smart-routing | what-is-clink, mor-vs-psp |
| agent-payments | what-is-clink, what-is-ap2-agent-payments-protocol, what-is-x402 |
| cloudflare-wallets-agent-payments | agent-payments, smart-routing, what-is-clink, what-is-x402, stripe-openrouter-acquisition |
| what-is-ap2-agent-payments-protocol | agent-payments, what-is-x402, what-is-machine-payments-protocol, what-is-agentic-commerce-protocol, what-is-universal-commerce-protocol |
| what-is-x402 | agent-payments, what-is-ap2-agent-payments-protocol, what-is-machine-payments-protocol, cloudflare-wallets-agent-payments |
| what-is-machine-payments-protocol | agent-payments, what-is-x402, what-is-ap2-agent-payments-protocol, what-is-agentic-commerce-protocol |
| what-is-agentic-commerce-protocol | agent-payments, what-is-universal-commerce-protocol, what-is-machine-payments-protocol, what-is-ap2-agent-payments-protocol |
| what-is-universal-commerce-protocol | agent-payments, what-is-agentic-commerce-protocol, what-is-ap2-agent-payments-protocol, what-is-clink |
| stripe-openrouter-acquisition | agent-payments, what-is-clink, cloudflare-wallets-agent-payments, mor-vs-psp |
| best-ai-companies-by-arr | annual-recurring-revenue, fastest-growing-ai-companies-arr, what-is-clink, agent-payments |
| fastest-growing-ai-companies-arr | best-ai-companies-by-arr, annual-recurring-revenue, burn-rate, what-is-clink |
| what-is-stripe-dispute | how-to-dispute-stripe-charge, stripe-chargeback-prevention, smart-routing, mor-vs-psp |
| how-to-dispute-stripe-charge | what-is-stripe-dispute, stripe-chargeback-prevention |
| stripe-chargeback-prevention | what-is-stripe-dispute, smart-routing, how-to-dispute-stripe-charge, why-stripe-closes-accounts |
| stripe-account-suspended | why-stripe-closes-accounts, how-to-appeal-stripe-account-closure, what-is-stripe-dispute, smart-routing |
| why-stripe-closes-accounts | stripe-account-suspended, how-to-appeal-stripe-account-closure, smart-routing |
| how-to-appeal-stripe-account-closure | stripe-account-suspended, why-stripe-closes-accounts, smart-routing |
| how-to-add-payments-lovable-app | what-is-clink, mor-vs-psp, smart-routing |
| integrate-stripe-lovable | how-to-add-payments-lovable-app, what-is-clink, mor-vs-psp |
| how-to-add-payments-bolt-app | what-is-clink, mor-vs-psp, smart-routing, how-to-add-payments-lovable-app |
| how-to-add-payments-v0-app | what-is-clink, mor-vs-psp, smart-routing, how-to-add-payments-lovable-app, how-to-add-payments-bolt-app |
| how-to-add-payments-replit-app | what-is-clink, mor-vs-psp, smart-routing, how-to-add-payments-lovable-app, how-to-add-payments-bolt-app, how-to-add-payments-v0-app |
| burn-rate | what-is-clink, mor-vs-psp, annual-recurring-revenue, runway |
| annual-recurring-revenue | what-is-clink, smart-routing, burn-rate, monthly-recurring-revenue, net-revenue-retention |
| monthly-recurring-revenue | annual-recurring-revenue, burn-rate, what-is-clink |
| net-revenue-retention | annual-recurring-revenue, smart-routing, what-is-clink |
| runway | burn-rate, annual-recurring-revenue, smart-routing, what-is-clink |
| what-is-skill-marketplace | what-is-clink, agent-payments, cloudflare-wallets-agent-payments, clink-launches-skill-marketplace |
| clink-launches-skill-marketplace | what-is-clink, agent-payments, what-is-skill-marketplace |

**规则**：用正文 Markdown 互链；**不要**写 frontmatter `related`。

---

*content-graph · v2.2.0 · 2026-08-24*
