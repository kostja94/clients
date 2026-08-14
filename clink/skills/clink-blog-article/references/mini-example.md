# Clink — Mini Example（Brief + Outline）

> 加载时机：Phase 1 / Phase 3
> Golden brief：`clink-vs-stripe`（pipeline P0）

---

## Brief 示例 — EvaluationComparison

```markdown
## Article Brief

**Mode**: flagship
**ArticleType**: EvaluationComparison
**InvestmentScore**: 4.4 — high search (stripe alternative) / close to purchase path /
  Moat (orchestration + portable billing) / R3 verifiable / evergreen
**SuccessMetric**: Demo/Contact clicks from article; ranking for
  "stripe alternative subscription billing"
**MoatAssetPlanned**: Hybrid architecture frame (keep Stripe + add failover) +
  decision table (when Clink vs when Stripe-only)
**AnswerBlocks**:
  1. Does Clink replace Stripe?
  2. How does Clink sit above Stripe and other PSPs?
  3. When is Stripe-only enough?
  4. How to migrate without ripping out Stripe?
**PostPublishReviewDates**: T+7 / T+30 / T+90 / T+180

**Working title**: Clink vs Stripe: Payment Orchestration Meets Billing
**Primary keyword**: stripe alternative subscription billing
**Search intent**: Commercial investigation / Comparison
**Category**: Comparison
**Reader stage**: Evaluation
**Publish goal**: SEO + Conversion
**Target audience**: Global SaaS teams already on Stripe facing multi-region declines
**Synthesis Statement**:
  SERP "Stripe alternative" pages push full rip-and-replace. Clink's unique angle:
  orchestration that keeps Stripe as a processor while adding multi-PSP routing,
  unified billing, and (where relevant) agent payments — without requiring MoR
  brand sacrifice.
**One-line thesis**: The question is not "leave Stripe" — it is whether one processor
  should remain a single point of failure for recurring revenue.
**Differentiation angle**: Connect Stripe + second PSP vs switch billing vendor
**Information increment**:
  - [ ] Architecture diagram in prose: app → Clink → Stripe/Airwallex/Adyen
  - [ ] Decision framework: single-market Stripe-only vs multi-region orchestration
**Candidate examples**: BlockSec / GeeLark multi-region coverage themes (as-of site testimonials)
**Word count target**: 2500–3500
**Topic Scope / Cluster**: EvaluationComparison spoke under what-is-clink hub
**Planned internal links** (≥2 blog):
  - /blog/what-is-clink
  - /blog/mor-vs-psp
  - /blog/smart-routing
**Slug candidate**: clink-vs-stripe
**Author**: Clink Team
**Compliance notes**: C1 no Clink fee %; do not link /vs/stripe; Claw only if relevant + Early Access
```

---

## Outline 示例 — clink-vs-stripe

```markdown
## Outline — clink-vs-stripe

| § | H2 | Answer block ID | Reader mental state | Target words | Links / Notes |
|---|-----|-----------------|---------------------|-------------|---------------|
| TL;DR | — | AB-0 | Am I in the right place? | 80–120 | bullet 1 = does not replace Stripe |
| 1 | Why Teams Compare Clink and Stripe | AB-1 | Why this comparison exists | 300 | link: what-is-clink |
| 2 | Architecture: Orchestration Layer vs Processor | AB-2 | How they relate | 400 | diagram in prose |
| 3 | Feature Comparison | AB-2 | Side-by-side | 450 | table + ≥3 sentences analysis |
| 4 | When Clink Is the Better Fit | AB-3 | Multi-region / churn | 350 | link: smart-routing |
| 5 | When Stripe Alone Is the Better Fit | AB-3 | Fairness (≥1 Stripe win) | 300 | single-market |
| 6 | Migration Path: Adding Clink Without Leaving Stripe | AB-4 | Risk of switching | 350 | docs link_psp |
| Conclusion | — | — | Ready to act | 120–180 | CTA ≤2 |
| FAQ | ≥3 | — | Objections | 400 | AB-1..4 |

**Estimated total**: ~2800–3200 words
**结构硬规则**：`## Conclusion` 后紧跟 `## FAQ`
**正文互链**: what-is-clink, mor-vs-psp, smart-routing
```

---

## Brief 骨架（空白模板）

```markdown
## Article Brief
**Mode**:
**ArticleType**:
**InvestmentScore**:
**SuccessMetric**:
**MoatAssetPlanned**:
**AnswerBlocks**:
**Working title**:
**Primary keyword**:
**Search intent**:
**Category**:
**Reader stage**:
**Publish goal**:
**Target audience**:
**Synthesis Statement**:
**One-line thesis**:
**Differentiation angle**:
**Information increment**:
  - [ ]
  - [ ]
**Word count target**:
**Planned internal links**:
**Slug candidate**:
**Author**: Clink Team
**Compliance notes**:
```

---

*mini-example · v1.0.0 · 2026-07-21*
