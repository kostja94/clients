---
title: "What Is Agentic Commerce Protocol ACP? — Instant Checkout"
description: "ACP is OpenAI and Stripe's open agent commerce standard—checkout APIs, delegated payment tokens, and product feeds for ChatGPT discovery."
slug: "what-is-agentic-commerce-protocol"
date: "2026-09-10"
updated: "2026-08-24"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 11
---

## TL;DR

- **ACP (Agentic Commerce Protocol)** is an open standard, co-developed by **OpenAI and Stripe**, that defines how AI agents discover products, run checkout sessions, and complete delegated payments with merchants.
- **Instant Checkout** ("Buy it in ChatGPT") launched in **September 2025** with **Etsy live day one**; by **March 2026** OpenAI **deprioritized standalone in-chat checkout** in favor of **product discovery + merchant-owned checkout**—the **ACP protocol itself continues** on [agenticcommerce.dev](https://agenticcommerce.dev).
- Stable spec **2026-04-17** adds cart, product feed, orders, authentication, and MCP bindings; merchants implement five **`/checkout_sessions`** REST endpoints and accept **Shared Payment Tokens (SPT)** at `complete`.
- Shopify announced **1M+ merchants** in the pipeline, but only roughly **12–30 Shopify brands** ever went live for in-chat checkout before the pivot—feed syndication (Shopify/Etsy auto-integrated as of mid-2026) matters more than raw pipeline size.
- ACP is **retail agent commerce**—distinct from [x402](/blog/what-is-x402)/[MPP](/blog/what-is-machine-payments-protocol) API micropayments and from [UCP](/blog/what-is-universal-commerce-protocol)'s Google-led full-journey model. For which ChatGPT and Meta surfaces are live today, see our [AI channel status list](/blog/agentic-commerce-agent-channels).

---

## What Is ACP? — A Working Definition

The **Agentic Commerce Protocol (ACP)** is an interaction model and open standard for connecting **buyers, their AI agents, and businesses** to complete purchases seamlessly. [OpenAI and Stripe announced ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout) alongside **Instant Checkout** in **September 2025**, describing it as "the language that lets AI agents and businesses work together to complete a purchase for a user."

ACP specifies **merchant-side checkout APIs**, **delegated payment mechanics**, **product feeds**, and **order notification webhooks**—not LLM prompts or agent reasoning. The agent surface (ChatGPT today, potentially others) calls a merchant's ACP-compliant gateway; the merchant remains **seller of record** with authoritative cart state, tax, and inventory.

The canonical spec lives at [agenticcommerce.dev](https://agenticcommerce.dev) with OpenAPI and JSON Schema artifacts versioned by date. Stable snapshot **2026-04-17** covers checkout, cart, product feed, orders, delegate authentication, and MCP bindings. The protocol is marked **beta**—implement against published specs, not assumptions about universal consumer adoption.

---

## How ACP Works: Checkout Sessions and Delegated Payment

ACP's merchant integration centers on **checkout sessions**—stateful objects representing a cart negotiation between agent and merchant.

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/checkout_sessions` | Create session |
| GET | `/checkout_sessions/{id}` | Retrieve authoritative state |
| POST | `/checkout_sessions/{id}` | Update line items, buyer info |
| POST | `/checkout_sessions/{id}/complete` | Charge via delegated payment token |
| POST | `/checkout_sessions/{id}/cancel` | Cancel session |

Every request requires **Bearer authentication**, an **`API-Version`** header, and **`Idempotency-Key`** on POSTs. Responses return session objects with **integer-cent totals**, status, policy links, and messages—merchants own price integrity; agents cannot unilaterally discount.

The **`complete`** endpoint is the payment moment. The platform sends **`payment_data`** containing a **Shared Payment Token (SPT)**—a bounded credential (`max_amount`, `currency`, `merchant_id`, `expires_at`, `reason: one_time`) minted by the buyer's wallet or Stripe—plus optional billing address. The merchant validates the session, applies tax from buyer location, charges the token, marks the session completed, and fires **order webhooks**.

Declines map to structured errors: `payment_declined`, `requires_3ds`, `invalid`. The merchant never sees the buyer's full PAN; the agent never holds spendable credentials outside the token envelope.

---

## Instant Checkout, the February 2026 Push, and the March Pivot

On **September 29, 2025**, OpenAI and Stripe launched **Instant Checkout** with **U.S. Etsy sellers live the same day**. Shopify announced a **one-million-plus merchant pipeline** (Glossier, SKIMS, Spanx, Vuori among cited brands), but operational reality lagged marketing scale: industry reporting placed roughly **12–30 Shopify merchants** live for in-chat checkout before OpenAI changed course.

On **February 16, 2026**, OpenAI expanded ["Buy it in ChatGPT"](https://openai.com/index/buy-it-in-chatgpt/) to **Free, Plus, and Pro U.S. users**—widening demand-side access while checkout remained **single-item** with multi-item carts still on the roadmap. PayPal and Walmart partnership announcements reinforced the agentic commerce narrative through early 2026.

By **March 2026**, OpenAI **deprioritized standalone Instant Checkout**, citing merchant-side complexity—inventory accuracy, tax remittance, and catalog freshness—as bottlenecks harder than demand generation. The product shifted to **product discovery in ChatGPT** with buyers completing purchases on **merchant-owned checkout** (in-app browser or merchant sites). Per [OpenAI's merchant page](https://chatgpt.com/merchants/) as of mid-2026, **Shopify and Etsy catalogs are auto-integrated** for discovery; implementing ACP alone does **not** guarantee ChatGPT placement without platform approval.

**Critical distinction:** the **ACP protocol did not sunset**—checkout specs, delegate payment, and feed schemas continue on GitHub. Merchants building for agent commerce should plan for **feed quality + optional checkout APIs**, not assume a permanent in-chat "Buy" button for every brand.

Stripe's **Agentic Commerce Suite (ACS)** remains the fastest integration path for Stripe merchants, with platform partners including Wix, WooCommerce, BigCommerce, Squarespace, and commercetools.

---

## Shared Payment Tokens and the Security Model

ACP's delegated payment model mirrors patterns across the agent stack:

- Humans authorize spend in a wallet or Stripe surface
- Platforms mint **SPTs** scoped to merchant and amount
- Merchants charge SPTs through familiar payment processors
- Agents orchestrate checkout but **do not custody** payment credentials

This aligns with [MPP](/blog/what-is-machine-payments-protocol) SPT demonstrations at Stripe Sessions 2026 and with the guardrails philosophy in [agent payments](/blog/agent-payments): **policy-time authorization, machine-time execution**.

ACP also specifies **product feeds** (JSONL/CSV) so agents can discover catalog data, plus webhook events (`checkout.session.created`, `checkout.session.completed`, etc.) for order sync. Reference gateway implementations (for example, community ACP Checkout Gateway projects) show how to deploy compliant HTTP services on serverless infrastructure.

---

## ACP vs UCP: Two Agent Checkout Camps

Two open protocols dominate **retail agent checkout** in 2026, from overlapping but distinct coalitions:

| Dimension | **ACP** | **[UCP](/blog/what-is-universal-commerce-protocol)** |
|-----------|---------|--------|
| Maintainers | OpenAI, Stripe | Google, Shopify |
| Primary surfaces | ChatGPT discovery (+ historic Instant Checkout) | Google AI Mode, Gemini, Copilot |
| Scope | Checkout sessions + delegated payment | Full commerce journey (discovery, loyalty, post-purchase) |
| Transport | REST (OpenAPI) | REST, MCP, A2A, GraphQL |
| Payment handlers | Stripe SPTs, expanding | Negotiated handlers (Google Pay, Shop Pay, etc.) |

Both are **pilot-stage** as of mid-2026. Merchant groundwork overlaps: clean catalog data, accurate inventory, fresh pricing, webhook reliability. Brands on Shopify may implement **UCP for Google** and **ACP for ChatGPT**—not necessarily one exclusive protocol.

ACP does not replace your existing storefront; it adds an **agent-addressable checkout API** alongside human web checkout.

---

## ACP vs x402, MPP, and AP2

- **ACP vs [x402](/blog/what-is-x402)/[MPP](/blog/what-is-machine-payments-protocol):** ACP is **retail cart checkout** with line items and orders. x402/MPP gate **individual HTTP resources**—API calls, files, tool invocations. A SaaS API company bills agents via MPP; a DTC brand sells via ACP.
- **ACP vs [AP2](/blog/what-is-ap2-agent-payments-protocol):** AP2 provides mandate-based authorization evidence; ACP provides checkout session APIs. Future compositions may attach AP2 mandates to ACP `complete` calls for audit-heavy enterprise retail.

If your product is **B2B subscription software**, ACP is rarely the first integration—unless you distribute through agent marketplaces selling packaged offerings. Your core billing remains subscriptions, [smart routing](/blog/smart-routing), and human checkout; ACP is a **new demand channel**, not a billing replacement.

---

## What ACP Means for Merchants and SaaS Teams

**Retail and DTC brands** on Stripe or Shopify should monitor ACP/UCP rollouts as **discovery and conversion channels**—analogous to early mobile commerce, but with agent-mediated intent.

**Marketplace operators** may expose ACP gateways so third-party sellers accept agent checkout without each seller building custom integrations.

**SaaS and API companies** should prioritize [MPP](/blog/what-is-machine-payments-protocol) or [x402](/blog/what-is-x402) for metered access; ACP only matters if you sell **sku-shaped products** through ChatGPT-class surfaces.

**Compliance and ops teams** should note: seller of record stays with the merchant; platform fees and dispute paths follow Stripe/OpenAI published terms—verify current fee schedules and pilot eligibility rather than assuming GA economics.

---

## Conclusion

ACP is the **open commerce protocol for ChatGPT-era agent retail**—checkout APIs, delegated payment tokens, and product feeds that let merchants keep backend systems while agents handle discovery and (where enabled) purchase orchestration. After the **March 2026 product pivot**, the durable merchant play is **feed quality and syndication**, with checkout APIs ready when platforms re-enable in-chat completion.

Build ACP feeds if ChatGPT discovery is a channel you can serve with accurate catalog data. Build MPP/x402 if your buyers are agents consuming APIs. Build [UCP](/blog/what-is-universal-commerce-protocol) alongside ACP if Google and Copilot surfaces matter too. The agent economy is multi-protocol by design—not a single checkout winner.

To see which surfaces, platforms, and PSPs are **Live versus waitlist** as of September 2026—without rereading every operator changelog—use our [AI channel status list](/blog/agentic-commerce-agent-channels), [commerce platform enablement list](/blog/agentic-commerce-merchant-stack-cms), and [PSP agentic product list](/blog/agentic-commerce-merchant-stack-psp). For feed mechanics, continue to our [ChatGPT merchant setup guide](/blog/how-to-sell-on-chatgpt).

---

## FAQ

### Who maintains ACP?

**OpenAI and Stripe** are founding maintainers per the [GitHub repository](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol). Meta is also listed as a governance partner in some industry summaries; verify MAINTAINERS.md for current roles.

### Is ACP the same as ChatGPT Instant Checkout?

No. **Instant Checkout** was ChatGPT's in-chat purchase product (September 2025–March 2026 era); **ACP** is the underlying open protocol. As of mid-2026, OpenAI prioritizes **product discovery** via ACP feeds; standalone in-chat checkout is deprioritized, though checkout APIs remain maintained.

### What happened to Instant Checkout in March 2026?

OpenAI **deprioritized standalone in-chat checkout** after roughly a dozen to thirty Shopify merchants went live—far below the million-merchant pipeline announced at launch. Buyers now typically **discover in ChatGPT and checkout on merchant sites**; discovery via ACP feeds continues without a platform completion fee on merchant-owned checkout (per OpenAI merchant FAQ, mid-2026).

### What is a Shared Payment Token?

An SPT is a **scoped, limited-use payment credential** (`vt_…`) authorizing a merchant to charge up to a defined amount before expiry—without exposing full card details to the agent or merchant checkout code.

### Do Shopify merchants need a separate ACP integration?

Shopify's agent strategy spans **ACP (ChatGPT)** and **[UCP](/blog/what-is-universal-commerce-protocol) (Google)**. Implementation paths differ; many merchants will enable agent checkout through platform tooling rather than raw REST gateways.

### Is ACP production-ready for all merchants?

ACP specs are **beta** and actively maintained (stable **2026-04-17**). ChatGPT **discovery** is live for approved feeds and auto-integrated Shopify/Etsy catalogs; **in-chat checkout** is not broadly available post-March 2026 pivot. Treat Instant Checkout-era pipeline numbers as historical marketing scale, not operational coverage.

### Can B2B SaaS use ACP for subscription billing?

ACP models **checkout sessions and one-time/delegated charges** for agent retail—not recurring B2B subscription lifecycle (dunning, seat expansion, invoicing). SaaS teams should use existing billing infrastructure for core revenue and [MPP](/blog/what-is-machine-payments-protocol) for agent API access where relevant.
