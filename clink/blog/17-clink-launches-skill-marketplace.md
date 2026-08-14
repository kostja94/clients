---
title: "Clink Launches Skill Marketplace — Monetize Agent Skills Natively"
description: "Clink Skill Marketplace is live: publish reviewed agent skills and monetize them natively — settlement, credit recharge, and tips built into the payment platform."
slug: "clink-launches-skill-marketplace"
date: "2026-08-06"
updated: "2026-08-06"
category: "Product"
author: "Clink Team"
readingMinutes: 11
---

## TL;DR

- **Clink Skill Marketplace is now live**: merchants can publish reviewed agent payment skills that AI agents discover, install, and pay for — with monetization built into the platform rather than bolted on.
- Because Clink is a payments company, skill owners get settlement infrastructure for free: `order.succeeded` webhooks, account recharge via `account.reloaded` / `account.created`, and Tips — no separate Stripe Connect or checkout stack to assemble.
- Publishers upload a `SKILL.md` ZIP, pass a review pipeline (package schema, version, security, payment behavior), and Clink generates the public CLI command and installation Prompt from the reviewed package.
- The marketplace is for payment-enabled skills: any skill that charges credits, sells per use, or accepts tips can publish — the payment behavior is part of the skill's contract, not an afterthought.
- The Agentic Payments offering is in Early Access, so this is the moment to establish distribution before the agent economy matures.

## Announcing: Clink Skill Marketplace

Clink has launched **Skill Marketplace** — a reviewed marketplace where merchants publish agent payment skills and get paid by agents that use them. It lives under **Developers > Skill Marketplace** in the Clink Dashboard, and it turns a product from "agent-compatible" into "agent-sellable."

If you are new to the concept, we recommend starting with [What Is a Skill Marketplace?](/blog/what-is-skill-marketplace), which covers the category and how reviewed marketplaces differ from open catalogs. This article is about the practical side: what launched, how monetization works, and what it takes to publish and get paid.

The launch matters because the agent economy is moving from protocol debates to actual distribution. The standards conversation — [Google's AP2, Visa's Intelligent Commerce framework, and the machine-payment protocols](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants) — is defining how agents authorize and settle. What has been missing is the commercial layer where skill owners actually get paid. Skill Marketplace is Clink's answer to that missing layer.

## Why a Payments Company Is the Natural Home for a Skills Marketplace

There are skill marketplaces that are not run by payment companies. [SkillExchange](https://skillexchange.market/creators) offers native MCP and A2A support with per-use, subscription, and tiered pricing, and [Agensi](https://www.agensi.io/learn/monetize-ai-skills-2026) pays creators a revenue share on each sale. Both are legitimate and useful channels, and both solve distribution well. The difference is architectural: in those models, monetization is assembled on top of the marketplace through an external payment stack such as Stripe Connect, with its own onboarding, payout schedule, and compliance surface.

Clink starts from the opposite direction. Payment is the product. The company's core stack — [payment infrastructure for an AI-native world](/blog/what-is-clink) — already handles checkout, billing, routing, and settlement across 135+ currencies and 100+ local payment methods. A skill marketplace built on top of that stack inherits the financial layer instead of wrapping it. The consequence for skill owners is that monetization is not a feature they integrate; it is the platform's default behavior.

That distinction is not cosmetic. When settlement, recharge, and tips are marketplace infrastructure, a publisher answers fewer questions: no separate payout onboarding, no reconciling one marketplace's ledger against another processor's, no building a credit system from scratch. This is the [deeper argument for agent payment rails](/blog/agent-payments) applied at the skill level — the financial complexity is handled behind one integration.

It is also why the marketplace can afford to be selective in what it lets through. Because payment behavior is part of every reviewed package, Clink can check that a skill's payment-trigger and user-confirmation logic is explicit and verifiable before it appears publicly. A general skill catalog has no reason to examine how a skill charges money; a payment-native marketplace treats that examination as the whole point. The result is a catalog where the payment contract is inspectable — a meaningful difference when the buyer is an autonomous agent that cannot read the fine print on its own.

## How Skill Owners Monetize: Settlement, Recharge, and Tips

The monetization model on Skill Marketplace is built around the way agents actually spend. When an agent needs credits to continue using a skill, Clink completes a recharge order and notifies the merchant's server via webhook; the merchant applies the result and responds with the account state. The settlement loop is defined in Clink's [Skill Marketplace guide](https://docs.clinkbill.com/guides/agent/skill_marketplace).

Concretely, three revenue paths are available to published skills:

- **Credit recharge.** When a user buys credits for a skill, Clink registers an `order.succeeded` event and delivers it to the merchant webhook. The merchant reconciles the order, resolves the account by `data.object.customerEmail`, applies the recharge, and returns HTTP 200 with `account.reloaded` (existing account) or `account.created` (new account).
- **Per-use and subscription pricing.** Because the recharge flow is native, skills that charge per invocation or per period reuse the same settlement loop — the order event is the same, and the merchant applies the purchased value to the account.
- **Tips.** Published skills can enable Tips, with suggested amounts and a public note. Tips appear publicly only after the related Clink check passes, keeping the payment behavior reviewable.

The webhook mechanics matter for anyone building a skill that charges credits. Requests must be verified against `X-Clink-Timestamp`, `X-Clink-Signature`, and `X-Clink-SignType` before the body is read. The event `id` is the idempotency key, with the original response stored for retries — processing the same event twice must not create a duplicate account or apply credits twice. The response echoes `data.customerEmail`, the merchant's `userId`, `amount`, and `currency`, and success is returned only after the local account change is committed; a non-2xx response lets the event be retried safely.

Two design choices in that flow are worth calling out, because they are what "payment-native" actually means in practice. First, the merchant implements only the handler logic — Clink Marketplace pre-registers the order webhook and prepares the endpoint configuration, so publishers do not create endpoints, change event subscriptions, or manage signing-secret rotation. Second, out-of-order delivery is handled by construction: recharges are applied only after a valid `order.succeeded` event, and a unique merchant-account constraint on normalized email prevents concurrent deliveries from creating duplicate users.

## From Package to Published: What You Ship, What Clink Generates

Publishing on Skill Marketplace follows a managed pipeline. You prepare a ZIP package containing the current `SKILL.md`, then submit a name, version, category, and one-sentence marketplace summary from **Developers > Skill Marketplace**.

The package moves through a defined status lifecycle. **Uploaded** means the ZIP was submitted and is waiting for processing. **Polishing** means Clink is reviewing it. **Ready** means the skill passed review but still needs you to publish it. **Published** is the only state that appears in the public marketplace. **Failed** means one or more review checks did not pass, and you get failure details — the failed check, the file it was detected in, and a fix suggestion — before reuploading. [Source: docs.clinkbill.com](https://docs.clinkbill.com/guides/agent/skill_marketplace)

Three details are worth understanding before you submit your first package.

First, **versions are enforced at submission time**. The version declared in `SKILL.md` must exactly match the version in the submission form, and any update must use a version newer than the current one. That constraint keeps the listing, the package, and the version history aligned.

Second, **installation methods are generated, not hand-written**. Clink generates the public CLI command and the installation Prompt from the reviewed package, and both are read-only for publishers. If the generated output is wrong, you correct the package and submit a new version — you do not edit the listing text. Agents execute these instructions, so the instructions should come from a reviewed artifact rather than free-text marketing copy.

Third, **Tips and payment behavior are gated on additional checks**. Enabling Tips in the form does not make the Tips panel public by itself; a related Clink check must also pass. If your skill uses agent payment, the payment-trigger and user-confirmation behavior must be explicit and reviewable before publication.

The practical takeaway for a first submission is to treat the package as a product, not paperwork. The summary should explain what the skill does and who should use it; the version in `SKILL.md` must match the form exactly; and if the skill charges credits, the payment-trigger and confirmation steps need to be written so a reviewer can trace them. Review failures return with a failed check, the file it was detected in, and a fix suggestion — so the loop from **Failed** back to **Ready** is a debugging cycle, not a mystery. Clink also runs version comparison and package schema checks, which means keeping the ZIP structure clean and the instructions self-contained saves resubmission rounds.

## Who Should Publish First

The marketplace rewards skills that fit the agent-spending pattern. Work through a short fit check before packaging your first submission.

**You sell per-use or per-task value.** Skills that charge credits fit flows where usage is measurable — API calls, image generations, compute minutes, task completions. If your product only sells annual seats with no usage dimension, a skill marketplace is probably not your first channel.

**You can package the capability as a `SKILL.md`.** The unit of distribution is the reviewed package. If your capability can be described in instructions an agent can execute, you have a publishable skill; if it needs a human in every loop, the marketplace adds little.

**You want payment to be infrastructure, not integration.** If you would rather not operate a separate checkout and settlement stack, Skill Marketplace is the fit — settlement, recharge, and tips are platform behavior, and the only code you write is the webhook handler that applies an `order.succeeded` event.

For teams still evaluating whether the model fits their go-to-market, the [Skill Marketplace guide](https://docs.clinkbill.com/guides/agent/skill_marketplace) documents the full publication checklist, and the [Agentic Payments offering](https://clinkbill.com/agentic-payment) explains the underlying top-up and authorization flow.

There is also a fair counter-case worth stating plainly: not every product belongs in a skill marketplace. If your pricing has no usage dimension, if your buyers are enterprises that purchase through formal procurement rather than agent runtimes, or if your capability fundamentally requires a human at the decision point, then a direct integration or a conventional checkout remains the right path. Marketplaces are a distribution channel, not a business model by themselves — they work when the buyers are agents and the spend is measurable per task. The teams that will see the strongest results are those that already sell per-use value and are packaging it as an agent-callable capability.

## Conclusion

Skill Marketplace is Clink's answer to a concrete gap: the agent economy has protocols for how agents pay, but skill owners need a commercial layer where that payment becomes revenue. Because Clink is a payments company, that layer ships with settlement, recharge, and Tips built in — the monetization loop is part of the platform, not a set of integrations each publisher assembles alone.

For skill owners, the case for publishing now is distribution timing. The Agentic Payments offering is in Early Access, and the merchants who establish their skills in the marketplace early will be the ones agents discover first as the economy scales. Publishing requires a `SKILL.md` package, a review pass, and a small webhook handler — the review pipeline and generated install methods do the heavy lifting.

If you are building an AI-native product and want to monetize agent usage, the Skill Marketplace is live, the [Agentic Payments offering is in Early Access](https://clinkbill.com/agentic-payment), and the publishing mechanics are documented in the [Skill Marketplace guide](https://docs.clinkbill.com/guides/agent/skill_marketplace).

## FAQ

### How does monetization work for skill owners on Clink Skill Marketplace?

When an agent needs credits to continue using a skill, Clink completes a recharge order and delivers an `order.succeeded` webhook. The merchant reconciles the order, resolves the account by `customerEmail`, applies the recharge, and returns `account.reloaded` or `account.created`. Per-use and subscription pricing reuse the same settlement loop, and Tips are supported as an additional revenue path.

### Do I need to build payment infrastructure to monetize my skill?

No. Settlement, recharge, and Tips are platform infrastructure on Skill Marketplace. Clink pre-registers the order webhook and prepares the endpoint configuration; publishers implement only the handler logic that applies the recharge. You do not integrate a separate checkout or payment processor.

### What are the fees and revenue share for publishing on Skill Marketplace?

Fees, settlement terms, revenue sharing, and refund policies are defined by Clink's commercial terms rather than by the publishing guide. For current policy on marketplace fees and payouts, contact Clink support directly.

### How do Tips work for published skills?

Tips can be enabled per skill with suggested amounts and a public note. Enabling Tips in the submission form does not make the Tips panel public by itself — the related Clink check must also pass, and a reviewable tip payment handler must be present in the package.

### What happens if I publish a skill and the credits flow has a problem?

The webhook flow is designed for reliability. Requests must pass signature verification, the event `id` is the idempotency key, and success is returned only after the local account change is committed. If local fulfillment fails, a non-2xx response lets the event be retried safely, and a unique merchant-account constraint prevents duplicate users from concurrent deliveries.

### How do I start publishing and monetizing on the marketplace?

Prepare a ZIP containing the current `SKILL.md` with a matching version, submit it from **Developers > Skill Marketplace**, and pass the review pipeline. Once the skill is **Ready**, publish it, and Clink generates the public CLI command and installation Prompt from the reviewed package. The full checklist is in the [Skill Marketplace guide](https://docs.clinkbill.com/guides/agent/skill_marketplace).
