---
title: "What Is Machine Payments Protocol MPP? — Stripe Agent Rails"
description: "MPP is Stripe and Tempo's open HTTP standard for agent payments—402 challenges, Shared Payment Tokens, subscriptions, and stablecoin settlement."
slug: "what-is-machine-payments-protocol"
date: "2026-09-09"
updated: "2026-08-24"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 11
---

## TL;DR

- **MPP (Machine Payments Protocol)** is an open, HTTP-native standard **co-authored by Stripe and Tempo**, launched **March 18, 2026**, for programmatic agent-to-service payments.
- MPP uses **`402 Payment Required`** challenges like [x402](/blog/what-is-x402), but adds **lifecycle primitives**: subscriptions, streaming usage, cancellations, and reconciliation—plus **multi-method settlement** (stablecoins, cards via Shared Payment Tokens, BNPL).
- **Tempo**, a payments-focused L1 blockchain, is MPP's default stablecoin settlement network (~500ms finality, sub-cent fees); Stripe merchants can accept MPP via **PaymentIntents** in a few lines of code.
- MPP sits in Stripe's **Agentic Commerce Suite** alongside [ACP](/blog/what-is-agentic-commerce-protocol), MCP integrations, and x402 support—MPP is the **merchant-grade machine payment wire** for existing Stripe accounts.
- For B2B SaaS on Stripe, MPP is the path to **bill agents** without rebuilding fraud, dispute, and accounting plumbing.

---

## What Is MPP? — A Working Definition

The **Machine Payments Protocol (MPP)** is an open standard for agents and services to coordinate payments programmatically over HTTP. [Stripe announced MPP](https://stripe.com/blog/machine-payments-protocol) on March 18, 2026—the same day Tempo's mainnet went live—describing it as an "internet-native way for agents to pay" for microtransactions, recurring charges, streaming usage, and more.

MPP is not a Stripe-only proprietary API, though Stripe is a primary implementer. Tempo co-authored the normative specification and documents MPP as the default way to charge on Tempo's chain. The protocol extends the bare [x402](/blog/what-is-x402) pattern with **payment lifecycle semantics** merchants need in production: not just "pay once per request," but subscriptions, session-based streaming, balance reconciliation, and cancellation.

If x402 is the HTTP payment handshake, MPP is the **full merchant stack expression** of that handshake for teams already on Stripe—or willing to settle stablecoins on Tempo.

---

## How MPP Works: Challenges, Credentials, and Receipts

MPP follows an inline payment pattern familiar from x402:

1. A **client** (agent, app, or human) requests a paid resource.
2. The **server** responds with **`402`** and a **Challenge** describing price, currency, and accepted payment methods.
3. The **client** pays and retries with a **Credential** (signed authorization).
4. The **server** verifies payment and returns the resource with a **Receipt**.

Tempo's documentation distinguishes two intent patterns on-chain:

| Pattern | Latency | Best for |
|---------|---------|----------|
| **Charge** | ~500ms on-chain confirmation | Single API calls, one-off content access |
| **Session** | Near-zero via off-chain vouchers | LLM APIs, metered services, streaming usage |

**Session** billing amortizes on-chain cost across many requests—critical for inference and token-metered APIs where per-request chain settlement would be uneconomical.

Stripe's implementation exposes MPP through libraries like **mppx**, registering payment methods (Stripe Shared Payment Tokens, Tempo charges) and wrapping handlers that return 402 challenges or settled responses.

---

## Shared Payment Tokens and Multi-Method Settlement

MPP's differentiation from "402 only" is **multi-method settlement** through a common wire shape:

- **Stablecoins** via x402-compatible signatures on Tempo (and extensible to other networks)
- **Cards** via **Shared Payment Tokens (SPTs)**—scoped, limited-use tokens that relay a buyer's payment method to a seller without exposing PAN data to the agent
- **BNPL** via Klarna or Affirm where supported

**Shared Payment Tokens** carry scoped limits merchants can introspect before charging—Visa card SPTs enforce amount caps at the network level (Stripe Sessions 2026 demo: a $25 token rejects a $50 charge). Card SPT minimum is **$0.50**; stablecoin minimum is **0.01 USDC**. Merchants validate with `npx mppx validate` for end-to-end discovery, challenge, and settlement testing.

**Session intent** (formalized on [mpp.dev](https://mpp.dev/intents/session)) supports streaming LLM and metered APIs via off-chain vouchers, with on-chain settlement batched—paired at Stripe Sessions 2026 with **Metronome** usage metering. **`subscription` intent** remains in spec development as of mid-2026; recurring SaaS billing still flows through Stripe Billing for most merchants today.

---

## Tempo, Streaming, and Stripe Dashboard Integration

**Tempo** launched mainnet alongside MPP as a payments-optimized L1 (co-developed with Paradigm, Stripe-backed). Sub-cent fees and ~500ms finality target agent micropayments and per-request billing—constraints general-purpose chains handle poorly at scale.

At **Sessions 2026** (April 29–30, 2026), Stripe added **streaming payments** as a first-class MPP primitive: real-time billing against a stablecoin balance for AI products that consume resources continuously.

For **Stripe merchants**, acceptance is intentionally low-friction: enable MPP via **PaymentIntents API** and existing Dashboard workflows—inheriting Stripe's fraud, dispute, and accounting machinery rather than standing up parallel agent billing ops. That is MPP's core B2B SaaS value proposition: **agent buyers, human merchant rails**.

---

## MPP in Stripe's Agentic Commerce Suite

Stripe positions MPP inside a broader **Agentic Commerce Suite**:

| Component | Role |
|-----------|------|
| [ACP](/blog/what-is-agentic-commerce-protocol) | Retail checkout sessions for ChatGPT Instant Checkout |
| **MPP** | HTTP-native machine payments for APIs and services |
| x402 support | Interop with Linux Foundation x402 ecosystem |
| MCP integrations | Tool-level commerce for agent runtimes |
| Agentic Commerce Suite | Merchant onboarding for agent channels |

Teams selling **through** ChatGPT implement ACP; teams selling **API access to agents** implement MPP or x402. Many will need both surfaces over time.

MPP shares signature substrates with x402 (**EIP-3009**, **Permit2** for off-chain authorization)—the protocols are **compatible at the crypto layer**, not forked competitors.

---

## MPP vs x402 and AP2

- **MPP vs x402:** Same HTTP 402 transport idiom; MPP adds Stripe/Tempo lifecycle (subscriptions, streaming, SPT cards) and merchant Dashboard integration. Pure x402 is thinner and facilitator-agnostic.
- **MPP vs [AP2](/blog/what-is-ap2-agent-payments-protocol):** MPP settles payment; AP2 proves delegated human authorization via mandates. High-trust enterprise flows may compose both.

For **agent-to-agent micropayments** where neither party is a registered Stripe merchant, x402 alone may suffice. For **registered merchants** billing agent traffic with card and stablecoin options plus dispute handling, MPP is the pragmatic choice.

---

## What MPP Means for B2B SaaS Merchants

MPP matters when your product is consumed by **software runtimes**, not only human users in a dashboard.

**Metered APIs and MCP tools** map cleanly to Charge or Session intents—agents pay per call without OAuth signup flows.

**Existing Stripe merchants** avoid parallel billing systems; MPP charges flow through PaymentIntents with familiar reconciliation.

**Risk teams** get SPT limits and merchant scoping instead of sharing raw payment methods with agent code.

**Gaps remain:** enterprise procurement, tax invoicing, and multi-currency accounting may still require your existing subscription stack—[smart routing](/blog/smart-routing) for human renewals and MPP for agent usage can coexist. MPP does not replace [MoR vs PSP](/blog/mor-vs-psp) decisions; it adds a collection mode.

Clink's [Agentic Payments](https://clinkbill.com/agentic-payment) (Early Access) addresses the **buyer-side harness**—scoped caps and audit for agents spending on third-party APIs—while MPP addresses the **seller-side** HTTP charge. Complementary layers in a growing stack.

---

## Conclusion

MPP is Stripe and Tempo's answer to a specific question: **how do registered merchants bill agents with the same fraud, dispute, and ops tooling they use for humans—without a checkout page?** HTTP 402 challenges, Shared Payment Tokens, and Tempo stablecoin settlement make that answer concrete.

Evaluate MPP if you are on Stripe and agent traffic is becoming material. Evaluate [x402](/blog/what-is-x402) if you need maximum facilitator neutrality or lightweight agent-to-agent transfers. Evaluate [AP2](/blog/what-is-ap2-agent-payments-protocol) when authorization audit trails are non-negotiable. The agent payment future is layered; MPP is the merchant-native layer.

**Retail catalog checkout** on ChatGPT, Gemini, or Copilot uses [ACP](/blog/what-is-agentic-commerce-protocol) and [UCP](/blog/what-is-universal-commerce-protocol)—not MPP. For live enablement by surface, platform, and processor, see our [AI shopping channel list](/blog/agentic-commerce-agent-channels), [commerce platform enablement list](/blog/agentic-commerce-merchant-stack-cms), and [PSP agentic product list](/blog/agentic-commerce-merchant-stack-psp) rather than inferring status from MPP documentation alone.

---

## FAQ

### What does MPP stand for?

**Machine Payments Protocol**—an open HTTP standard co-authored by Stripe and Tempo for agent and programmatic payments.

### When did MPP launch?

**March 18, 2026**, alongside Tempo mainnet. Stripe added streaming payments at Sessions 2026 (April 29–30, 2026).

### Is MPP the same as x402?

Related but not identical. Both use HTTP 402; MPP extends x402-style transport with subscriptions, streaming, Shared Payment Tokens, and Stripe merchant integration. They share signature approaches (EIP-3009, Permit2).

### Do I need Tempo to use MPP?

Tempo is the default stablecoin settlement chain, but MPP supports **multiple methods** including cards via SPTs on Stripe. Method availability depends on your Stripe configuration and implementation.

### How does MPP relate to ACP?

[ACP](/blog/what-is-agentic-commerce-protocol) handles **retail checkout sessions** for agent surfaces like ChatGPT. MPP handles **HTTP resource payments** for APIs and services. Stripe ships both; use case determines which to implement first.

### Can small API providers use MPP without Stripe?

MPP is designed for Stripe merchant accounts and Tempo settlement. Lightweight sellers may start with [x402](/blog/what-is-x402) facilitators; graduate to MPP when Stripe merchant tooling becomes necessary.
