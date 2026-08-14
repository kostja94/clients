# Clink Blog — Content Graph

> 加载时机：Phase 0（选题）· Phase 2（日期）· Phase 5（Cross-Article）
> 主文件：SKILL.md §4 指针

---

## 文件表

| NN | 文件 | slug | 类型 | category | 日期 | 主关键词 |
|----|------|------|------|----------|------|---------|
| 01 | 01-what-is-clink.md | what-is-clink | BrandIntroduction | Product | 2026-06-23 | Clink, payment infrastructure |
| 02 | 02-mor-vs-psp.md | mor-vs-psp | Comparison | Comparison | 2026-06-29 | MoR vs PSP |
| 03 | 03-smart-routing.md | smart-routing | Product | Product | 2026-06-29 | smart payment routing |
| 04 | 04-agent-payments.md | agent-payments | Opinion | Opinion | 2026-06-29 | agent payments |
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
| 15 | 15-cloudflare-wallets-agent-payments.md | cloudflare-wallets-agent-payments | Opinion | Opinion | 2026-08-04 | Cloudflare Wallets, agent payments |
| 16 | 16-what-is-skill-marketplace.md | what-is-skill-marketplace | Product | Product | 2026-08-05 | what is a skill marketplace |
| 17 | 17-clink-launches-skill-marketplace.md | clink-launches-skill-marketplace | Product | Product | 2026-08-06 | monetize agent skills |

**下一序号：18**

**S-grade rewrite (2026-07-23)**: Titles normalized to em dash form; slugs unchanged. Anti-clone contract for 05–09: `clink/blog/_series-canonical-ownership.md`.

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
 ├── agent-payments (Opinion)
 ├── cloudflare-wallets-agent-payments (Opinion) → agent-payments + smart-routing + hub
 ├── what-is-skill-marketplace (Product) → hub + agent-payments + cloudflare-wallets-agent-payments + clink-launches-skill-marketplace
 ├── clink-launches-skill-marketplace (Product) → hub + agent-payments + what-is-skill-marketplace
 ├── how-to-add-payments-lovable-app (Product) → hub + mor-vs-psp + smart-routing
 ├── integrate-stripe-lovable (Product) → how-to-add-payments-lovable-app + mor-vs-psp + hub
 ├── how-to-add-payments-bolt-app (Product) → hub + mor-vs-psp + smart-routing + how-to-add-payments-lovable-app
 ├── how-to-add-payments-v0-app (Product) → hub + mor-vs-psp + smart-routing + how-to-add-payments-lovable-app + how-to-add-payments-bolt-app
 ├── how-to-add-payments-replit-app (Product) → hub + mor-vs-psp + smart-routing + how-to-add-payments-lovable-app + how-to-add-payments-bolt-app + how-to-add-payments-v0-app

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
| agent-payments | what-is-clink |
| cloudflare-wallets-agent-payments | agent-payments, smart-routing, what-is-clink |
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

*content-graph · v1.0.0 · 2026-07-21*
