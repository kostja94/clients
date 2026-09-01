---
title: "What Is x402 Agent Payments? — HTTP 402 Protocol Explained"
description: "x402 is the open HTTP payment protocol for AI agents and APIs. Learn the 402 flow, facilitators, stablecoins, and Linux Foundation governance."
slug: "what-is-x402"
date: "2026-09-08"
updated: "2026-08-24"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 11
---

## TL;DR

- **x402** is an open standard for **internet-native payments over HTTP**, built around the **`402 Payment Required`** status code with machine-readable headers—not a redefinition of HTTP itself.
- Coinbase incubated x402; on **April 2, 2026** the protocol moved to the **Linux Foundation x402 Foundation**, with **40+ member organizations** including Stripe, Visa, Google, Cloudflare, and Shopify by July 2026.
- The flow is client–server native: a **resource server** returns payment terms; the **client** (human, app, or agent) signs a payload; a **facilitator** verifies and settles—often in stablecoins on networks like Base or Solana.
- x402 complements [AP2](/blog/what-is-ap2-agent-payments-protocol) (authorization evidence), [MPP](/blog/what-is-machine-payments-protocol) (Stripe lifecycle extensions), and commerce protocols like [UCP](/blog/what-is-universal-commerce-protocol)—it is the **wire format for paying over HTTP**.
- For API and SaaS sellers, x402 is the fastest path to **per-request micropayments** without API keys, billing accounts, or human checkout—when your buyers are agents.

---

## What Is x402? — A Working Definition

**x402** is an open payment protocol that embeds payment capability directly into HTTP request–response cycles. Created at Coinbase and [contributed to the Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol) in April 2026, x402 aims to let AI agents, APIs, and web applications **transact value as seamlessly as they exchange data**.

The name references [HTTP 402 Payment Required](https://www.rfc-editor.org/rfc/rfc9110.html#name-402-payment-required), which RFC 9110 reserves for future use without defining payment semantics. x402 supplies the **application-layer schemas, headers, and settlement flow** on top of ordinary HTTP— it does not change HTTP itself. The [GitHub repository](https://github.com/x402-foundation/x402/) describes x402 as supporting multiple networks (crypto and fiat), value forms (stablecoins, tokens, fiat), and extensible settlement **schemes** such as `exact` (pay a fixed amount) and `upto` (authorize a cap, settle actual usage).

x402 is not a payment processor. It is a **protocol** that facilitators, wallets, and resource servers implement. Think of it as TLS for money at the HTTP boundary: standardized handshakes, vendor-neutral governance, composable with MCP tool servers and agent runtimes.

---

## How x402 Works: The 402 Handshake

x402 defines roles and a minimal multi-request pattern:

| Role | Responsibility |
|------|----------------|
| **Resource server** | HTTP endpoint that gates content or API access behind payment |
| **Client** | Browser, app, or agent that wants the resource |
| **Facilitator** | Service that verifies signed payment payloads and executes settlement |

A typical flow:

1. Client requests a protected resource.
2. Server responds with **`402 Payment Required`** and a **`PAYMENT-REQUIRED`** header describing price, scheme, network, and destination.
3. Client constructs a signed payment payload and retries with **`PAYMENT-SIGNATURE`**.
4. Facilitator verifies and settles; server returns the resource, optionally with **`PAYMENT-RESPONSE`** confirmation.

The design goal is **transport-native**: payment should not require out-of-band OAuth flows, hosted checkout redirects, or separate billing portals when a machine is the buyer. That is why x402 pairs naturally with [agent payments](/blog/agent-payments)—agents already speak HTTP; adding settlement to the same conversation removes the "human session" bottleneck.

**x402 V2** (December 2025) standardized **`PAYMENT-REQUIRED`**, **`PAYMENT-SIGNATURE`**, and **`PAYMENT-RESPONSE`** headers with CAIP-2 network IDs, plus wallet **session** support for repeat access without full payment handshakes each time. Coinbase CDP reported **100M+** facilitated transactions on Base and Solana by early 2026—though Tier 1 media note much early volume may be test traffic; treat adoption metrics with source and date context.

**AWS Bedrock AgentCore Payments** reached GA in **August 2026**, supporting x402 alongside [MPP](/blog/what-is-machine-payments-protocol) with a gateway catalog of paid endpoints—enterprise agents can pay for third-party APIs without custom billing integrations per vendor.

**Schemes** extend settlement patterns: `exact` (fixed price per access), `upto` (cap with usage-based settlement), and batch variants for high-frequency calls.

---

## Facilitators, Networks, and Stablecoins

x402 deliberately separates **protocol** from **settlement infrastructure**. A **facilitator** verifies signatures, submits transactions, and may perform compliance screening—without necessarily taking custody of buyer funds.

Coinbase's [CDP facilitator](https://docs.cdp.coinbase.com/x402/core-concepts/facilitator) is the most documented production path, supporting networks including Base, Polygon, Arbitrum, and Solana with varying EIP-3009, Permit2, and SPL capabilities. Pricing models (for example, free tiers plus per-transaction fees) are facilitator-specific, not protocol-mandated.

**Important operational caveat:** the public `x402.org/facilitator` endpoint is widely documented as **testnet-oriented**; production deployments typically require CDP credentials or another facilitator from the [Facilitators directory](https://docs.x402.org/dev-tools/facilitators). Teams should confirm network, token, scheme, and gas sponsorship per deployment—not assume a single global default.

Stablecoins (especially USDC) dominate early agent micropayment examples because settlement can complete in seconds with predictable fees—properties that match per-request API pricing. x402's roadmap explicitly includes fiat and card paths through extensible schemes and member contributions from traditional payment providers.

---

## x402 Foundation and Industry Membership

Governance moved to neutral ground when Coinbase completed its contribution and the [x402 Foundation became fully operational](https://www.prnewswire.com/news-releases/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications-302824778.html) in July 2026. Premier members at launch included Adyen, AWS, American Express, Circle, Cloudflare, Coinbase, Google, Mastercard, Shopify, Solana Foundation, Stripe, and Visa—signaling that x402 is intended as **industry infrastructure**, not a single-vendor rail.

[Cloudflare's Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) (July 2026) and [Cloudflare Wallets](/blog/cloudflare-wallets-agent-payments) (August 2026) illustrate the two-sided market x402 enables: sellers price resources in HTTP; buyers (including agents) pay in the same request flow. The pattern matches what SaaS teams need for **usage-based API monetization** without standing up a full billing portal for every micro-transaction.

---

## x402 vs MPP, AP2, and Commerce Protocols

Agent payment standards stack rather than collide:

- **x402 vs [MPP](/blog/what-is-machine-payments-protocol):** x402 defines HTTP payment headers and settlement schemes; MPP (Stripe + Tempo) shares signature substrates (EIP-3009, Permit2) but adds **subscriptions, streaming charges, cancellations, and Stripe merchant tooling**. MPP is multi-method (stablecoin, card via Shared Payment Tokens, BNPL); x402 alone is the thinnest HTTP layer.
- **x402 vs [AP2](/blog/what-is-ap2-agent-payments-protocol):** x402 moves value over HTTP; AP2 provides **verifiable mandate credentials** proving human-delegated authorization. Composable in high-compliance flows.
- **x402 vs [ACP](/blog/what-is-agentic-commerce-protocol) / [UCP](/blog/what-is-universal-commerce-protocol):** Commerce protocols model retail checkout sessions, carts, and orders. x402 models **pay-per-request** at any HTTP addressable endpoint—including MCP tools and raw APIs.

Choose x402 when the buyer is a machine, the unit of sale is a request or file, and you want payment inline with HTTP—not when you are building a full retail checkout inside ChatGPT or Google AI Mode.

---

## MCP, A2A, and SaaS Billing Scenarios

x402 integrates where agents already work. **MCP tool servers** can return 402 challenges per tool invocation; agents with funded wallets retry with payment signatures. **A2A** agents can treat paid HTTP resources as capabilities in multi-step tasks.

For **B2B SaaS and API businesses**, x402 enables:

- **Per-call pricing** without API key provisioning or prepaid balance dashboards
- **Agent-to-service micropayments** where neither party wants a traditional merchant contract for every micro-transaction
- **Headless monetization** of datasets, model inference endpoints, and premium documentation

Limitations remain real: dispute handling, tax, invoicing, and enterprise procurement often still require a human billing layer—[smart routing](/blog/smart-routing) and subscription infrastructure do not disappear. x402 is best understood as a **new collection surface** for agent traffic, not a replacement for recurring revenue systems.

---

## Conclusion

x402 turns HTTP into a payment-capable transport for the agent era. Neutral Linux Foundation governance, broad industry membership, and production facilitators make it the default reference for **machine-native micropayments** in 2026.

API sellers should evaluate x402 when agent buyers cannot complete human checkout. Platform teams should treat it as complementary to [MPP](/blog/what-is-machine-payments-protocol) for Stripe-native lifecycle needs and to [AP2](/blog/what-is-ap2-agent-payments-protocol) when authorization audit trails matter. The protocol is mature enough to build against; operational details (facilitator choice, network, compliance) remain deployment-specific.

**Retail agentic commerce**—product feeds and delegated checkout on consumer AI surfaces—uses [ACP](/blog/what-is-agentic-commerce-protocol) and [UCP](/blog/what-is-universal-commerce-protocol), not x402 per SKU. If you sell SKUs through ChatGPT or Gemini, check [which AI surfaces are live](/blog/agentic-commerce-agent-channels), [whether your storefront platform is enrolled](/blog/agentic-commerce-merchant-stack-cms), and [which PSP exposes delegated checkout](/blog/agentic-commerce-merchant-stack-psp)—separate questions from HTTP 402 micropayments.

---

## FAQ

### Is x402 an official HTTP standard?

No. RFC 9110 reserves status code 402 but does not define payment semantics. x402 is an **application-layer protocol** using HTTP 402 with custom headers (`PAYMENT-REQUIRED`, `PAYMENT-SIGNATURE`, `PAYMENT-RESPONSE`).

### Who maintains x402 today?

The **x402 Foundation** under the Linux Foundation, following Coinbase's April 2026 contribution. Specifications and SDKs live at [x402.org](https://x402.org) and [github.com/x402-foundation/x402](https://github.com/x402-foundation/x402/).

### Do I need cryptocurrency to use x402?

Early implementations emphasize **stablecoins** on L2 networks for speed and cost. The protocol is designed to support fiat and card schemes through extensible settlement methods; check your facilitator's supported networks and tokens.

### How is x402 different from Stripe billing?

Stripe Billing manages human subscriptions, invoices, and dunning. x402 gates **individual HTTP requests** with inline payment—closer to pay-per-call API monetization. Stripe also supports x402 and [MPP](/blog/what-is-machine-payments-protocol) as part of its agentic commerce stack.

### Can x402 work with MCP tools?

Yes. MCP servers that expose HTTP-backed tools can respond with 402 challenges; agent clients with payment credentials retry authenticated requests—Cloudflare and others document this pattern for monetized tool access.

### Is the public x402.org facilitator production-ready?

Treat the public facilitator as **testnet-oriented**. Production deployments typically use Coinbase CDP or another listed facilitator with appropriate credentials and network configuration.
