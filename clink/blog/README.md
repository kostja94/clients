# Clink Blog

> Blog content for [clinkbill.com](https://clinkbill.com/) blog section.

**Last updated**: 2026-08-11  
**Note**: All nine published articles received an S-grade structural rewrite on 2026-07-23 (slugs frozen; titles normalized to `Title — Subtitle`). Series anti-clone contract: [`_series-canonical-ownership.md`](./_series-canonical-ownership.md). GlossaryTerm entries (10–14, `category: Glossary`) published 2026-07-27/28/29/30/31 under `/blog/`. Skill Marketplace 双文（16–17, `category: Product`）published 2026-08-05/06 under `/blog/`. **Images removed 2026-08-11** — no article uses an `image` field.

---

## Published Articles

| # | Title | Slug | Type | Date |
|---|-------|------|------|------|
| 01 | [What Is Clink — Payment Infrastructure for an AI-Native World](./01-what-is-clink.md) | what-is-clink | Brand Introduction | 2026-06-23 |
| 02 | [MoR vs PSP — How to Choose the Right Payment Infrastructure Model](./02-mor-vs-psp.md) | mor-vs-psp | Comparison | 2026-06-29 |
| 03 | [Smart Payment Routing — How Multi-PSP Orchestration Recovers 3–5% Revenue](./03-smart-routing.md) | smart-routing | Product | 2026-06-29 |
| 04 | [AI Agents Need Payments Too — Agent-Native Transaction Rails](./04-agent-payments.md) | agent-payments | Opinion | 2026-06-29 |
| 05 | [How to Add Payments to a Lovable App — Paddle, Stripe, or Clink](./05-how-to-add-payments-lovable-app.md) | how-to-add-payments-lovable-app | Product | 2026-07-22 |
| 06 | [Integrate Stripe with Lovable Apps — Built-in Payments and Go-Live Guide](./06-integrate-stripe-lovable.md) | integrate-stripe-lovable | Product | 2026-07-23 |
| 07 | [How to Add Payments to Bolt.new Apps — Stripe Built-in, Then Clink](./07-how-to-add-payments-bolt-app.md) | how-to-add-payments-bolt-app | Product | 2026-07-24 |
| 08 | [How to Add Payments to v0 Apps — Stripe, Paddle Kit, Then Clink](./08-how-to-add-payments-v0-app.md) | how-to-add-payments-v0-app | Product | 2026-07-25 |
| 09 | [How to Add Payments to Replit Apps — Stripe, Whop, Then Clink](./09-how-to-add-payments-replit-app.md) | how-to-add-payments-replit-app | Product | 2026-07-26 |
| 10 | [What Is a Burn Rate? — Definition, Formula, and Runway](./10-burn-rate.md) | burn-rate | Glossary | 2026-07-27 |
| 11 | [ARR Meaning — Annual Recurring Revenue, Explained](./11-annual-recurring-revenue.md) | annual-recurring-revenue | Glossary | 2026-07-28 |
| 12 | [What Is MRR? — Monthly Recurring Revenue, Explained](./12-monthly-recurring-revenue.md) | monthly-recurring-revenue | Glossary | 2026-07-29 |
| 13 | [What Is NRR? — Net Revenue Retention, Explained](./13-net-revenue-retention.md) | net-revenue-retention | Glossary | 2026-07-30 |
| 14 | [What Is Runway? — How Startup Cash Runway Works](./14-runway.md) | runway | Glossary | 2026-07-31 |
| 15 | [Cloudflare Wallets and Agent Payments — Why Wallets Are Becoming Agent Accounts](./15-cloudflare-wallets-agent-payments.md) | cloudflare-wallets-agent-payments | Opinion | 2026-08-04 |
| 16 | [What Is a Skill Marketplace? — How AI Agents Discover, Install, and Pay for Skills](./16-what-is-skill-marketplace.md) | what-is-skill-marketplace | Product | 2026-08-05 |
| 17 | [Clink Launches Skill Marketplace — Monetize Agent Skills Natively](./17-clink-launches-skill-marketplace.md) | clink-launches-skill-marketplace | Product | 2026-08-06 |

**下一序号**：18

---

## Content Pipeline

| Status | Title | Slug | Type | Target Date |
|--------|-------|------|------|-------------|
| Planned | Payment Orchestration: Why Single PSP Is No Longer Enough | payment-orchestration-single-psp | Opinion / CategoryPOV | TBD |
| Planned | Clink vs Stripe: Payment Orchestration Meets Billing | clink-vs-stripe | EvaluationComparison | TBD |
| Planned | How to Reduce Involuntary Churn with Smart Payment Routing | reduce-involuntary-churn-routing | Product / SearchCapture | TBD |

**Glossary backlog**（`category: Glossary`，路径 `/blog/`）：术语库见 `skills/clink-blog-article/references/glossary-terms.md`。P0 候选：`what-is-involuntary-churn`、`what-is-soft-decline`（与 smart-routing 强互链）。

---

## How to create new articles

使用 skill：[`../skills/clink-blog-article/SKILL.md`](../skills/clink-blog-article/SKILL.md)

```
按 clink-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{BrandIntroduction|Comparison|Product|Opinion|EvaluationComparison} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
Mode：{lite|standard|flagship}
```

**流程摘要**：Phase 0 Intake → 0R Research → Brief → Slug/Date → Outline → Draft → tools 预检 + SelfCheck → Delivery。

**成稿路径**：`clink/blog/NN-{slug}.md`（NN 两位递增）。

**发布后**：更新本 README 的 Published Articles 表；对照 `skills/clink-blog-article/references/content-graph.md` 更新日期与正文互链。

**金融合规**：涉及费率、MoR/tax 覆盖、证言数字的 claim，建议法务审定后再上线。

---

## Content Pillars

1. **Payment Infrastructure** — orchestration, routing, multi-PSP architecture
2. **Subscription Billing** — lifecycle management, usage-based pricing, portals
3. **Agent Economy** — Clink for Claw, autonomous payments, AI-native commerce
4. **Global Expansion** — multi-currency, local payment methods, tax compliance

---

## Style Notes

- **Voice**: Professional, precise, data-informed. No hype or vague superlatives.
- **Evidence**: All product claims referenced to clinkbill.com or docs.clinkbill.com as of stated date.
- **Competitors**: Fair treatment — describe differences, not deficiencies.
- **Series (05–09)**: Respect [`_series-canonical-ownership.md`](./_series-canonical-ownership.md)—Clink full integrate path only in 05; Beyond sections must be platform-unique.
