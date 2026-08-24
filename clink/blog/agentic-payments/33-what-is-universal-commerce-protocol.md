---
title: "What Is Universal Commerce Protocol UCP? — Google and Shopify"
description: "UCP is Google and Shopify's open standard for agentic commerce—full-journey checkout, embedded payments, and multi-transport APIs."
slug: "what-is-universal-commerce-protocol"
date: "2026-09-11"
updated: "2026-08-24"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 11
---

## TL;DR

- **UCP (Universal Commerce Protocol)** is an open standard **co-developed by Google and Shopify** (announced January 2026) for AI agents to **discover, negotiate, and transact** with any merchant across the full shopping journey.
- UCP supports **capability negotiation**—merchants declare what they offer (checkout, loyalty, fulfillment extensions); agents and merchants agree on handlers per transaction, including **Google Pay**, **Shop Pay**, and third-party PSPs.
- Transports include **REST**, **GraphQL**, **JSON-RPC**, **MCP**, and **A2A**; UCP is compatible with [AP2](/blog/what-is-ap2-agent-payments-protocol), MCP, and A2A per Google's launch materials.
- **Google AI Mode** and **Gemini** checkout for eligible U.S. retailers is the first major consumer surface; **Microsoft Copilot** embedded checkout and **Shopify Agentic Storefronts** extend distribution.
- For Shopify merchants, UCP is the **default agent commerce rail** for Google surfaces—distinct from [ACP](/blog/what-is-agentic-commerce-protocol)'s ChatGPT-first checkout model.

---

## What Is UCP? — A Working Definition

The **Universal Commerce Protocol (UCP)** is an open standard for integrating commerce with AI agents—"forged from billions of transactions and supported by millions of merchants," in [Shopify's framing](https://www.shopify.com/ucp). Google and Shopify co-developed UCP to solve a structural problem: every agent surface (Search, Gemini, Copilot, ChatGPT) should not require a bespoke merchant integration per platform.

UCP models commerce as **negotiated capabilities** rather than a fixed checkout form. Merchants publish a **profile** (conventionally at `/.well-known/ucp`) advertising supported capabilities, payment handlers, and extensions. Agents discover the profile, negotiate what both sides can handle for a given cart context, and execute transactions—including **Embedded Checkout Protocol (ECP)** experiences where agents render merchant checkout UI with bidirectional messaging for payment and address selection.

Version **2026-01-11** is the cited baseline in Shopify engineering materials. UCP is public, Apache-licensed, and designed for contribution from retailers, PSPs, and agent platforms.

---

## How UCP Works: Capabilities, Handlers, and Checkout

UCP separates **what commerce means** from **how bits move**:

**Core capabilities** cover proven workflows: product discovery, checkout sessions, orders, post-purchase support. **Extensions** handle retailer-specific rules—discounts, loyalty points (`com.loyaltyprovider.points` style capability IDs), subscriptions, fulfillment options.

**Payment handlers** invert the usual "protocol picks Visa" model. Each provider (Google, Shopify, regional PSPs) publishes handler specifications; merchants advertise accepted handlers; agents pick one per transaction based on buyer wallet, region, and cart. Adding Google Pay or a new BNPL option does not require a UCP core version bump—handlers grow organically.

Checkout APIs follow session patterns familiar from modern commerce platforms:

- Create and update **checkout sessions**
- Negotiate totals as cart, buyer region, or discounts change
- **Complete** orders with the selected payment handler
- Support **escalation** to human-in-the-loop when automation cannot finish

**ECP (Embedded Checkout Protocol)**, distilled from Shopify's Checkout Kit, lets agents embed merchant checkout with UI extensions and delegation for payment/address—so agent-branded experiences do not feel disjoint from merchant trust signals. **Microsoft Copilot Checkout** uses the ECP path; **Google AI Mode/Gemini** default to **Native REST checkout** where Google renders buyer UI and sensitive payment steps stay in Google's trusted surface.

Merchants publish a **`/.well-known/ucp`** profile advertising capabilities; agents negotiate handler and transport intersections per transaction. Google Native checkout requires **Merchant Center**, a qualified product feed, **`/.well-known/ucp`**, REST checkout implementation, and **waitlist approval**—rollout remained **selective U.S. merchants** as of mid-2026.

---

## Transports: REST, MCP, A2A, and Beyond

UCP explicitly supports multiple transports with the same business logic:

| Transport | Use case |
|-----------|----------|
| REST | Traditional merchant integrations |
| GraphQL / JSON-RPC | Platform-native stacks |
| **MCP** | Tool-centric agent runtimes |
| **A2A** | Agent-to-agent commerce orchestration |

Google's [January 2026 announcement](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/) states UCP works across verticals and is compatible with **A2A**, **[AP2](/blog/what-is-ap2-agent-payments-protocol)**, and **MCP**—positioning UCP as the **commerce layer** agents compose with payment authorization (AP2) and tool access (MCP).

This matters for architects: you can swap transport without rewriting checkout semantics—similar in spirit to how [x402](/blog/what-is-x402) stays HTTP-native while [MPP](/blog/what-is-machine-payments-protocol) adds merchant lifecycle on top.

---

## Google, Shopify, and the Endorser Ecosystem

UCP launched with unusual retail and payments breadth:

**Co-developers:** Google, Shopify

**Retail endorsers cited at launch:** Etsy, Wayfair, Target, Walmart—and millions of Shopify merchants via platform tooling

**Payments and platforms:** Adyen, American Express, Best Buy, Flipkart, Macy's, Mastercard, Stripe, The Home Depot, Visa, Zalando, and others across 20+ organizations

**UCP Tech Council** expanded in **April 2026** to include **Amazon, Meta, Microsoft, Salesforce, and Stripe** alongside founding retailers—bringing governance to 16 seats and signaling cross-platform commitment beyond the Google–Shopify launch coalition.

**Consumer surfaces:**

- **Google AI Mode** in Search and **Gemini app** checkout for eligible U.S. retailers (Google Pay from Google Wallet; PayPal expanding)
- **Microsoft Copilot** embedded checkout via Shopify integration updates
- **Shopify Agentic Storefronts**—central admin for AI channel distribution including ChatGPT (Shopify's multi-channel strategy spans UCP and partner protocols)

[Ashish Gupta, VP/GM Merchant Shopping at Google](https://www.shopify.com/news/ai-commerce-at-scale), described UCP as "a shared language across the ecosystem"—signaling intent to make agent commerce interoperable rather than walled per assistant.

---

## UCP vs ACP: Google/Shopify vs OpenAI/Stripe

Both protocols enable agent checkout; coalition and scope differ:

| | **UCP** | **[ACP](/blog/what-is-agentic-commerce-protocol)** |
|---|---------|------|
| Leaders | Google + Shopify | OpenAI + Stripe |
| Journey scope | Full commerce (discovery → post-purchase) | Checkout sessions + delegated payment |
| Checkout UX | ECP embedded merchant checkout | Instant Checkout in ChatGPT |
| Payment model | Negotiated handlers | Shared Payment Tokens via Stripe |
| Spec site | ucp.dev / Shopify UCP hub | agenticcommerce.dev |

Merchants already on Shopify get UCP pathways for Google surfaces through platform updates; Stripe-heavy merchants lean on ACP for ChatGPT. **Dual implementation** is plausible for large brands—not a forced standard war.

---

## UCP vs AP2, x402, and MPP

UCP addresses **retail commerce semantics** (carts, loyalty, fulfillment)—not raw HTTP micropayments:

- **[AP2](/blog/what-is-ap2-agent-payments-protocol):** Authorization mandates; Google states UCP compatibility—AP2 evidence can accompany UCP checkout completion.
- **[x402](/blog/what-is-x402) / [MPP](/blog/what-is-machine-payments-protocol):** Pay-per-HTTP-resource for APIs and tools. UCP may consume these for digital goods, but core UCP is sku-and-cart commerce.
- **[agent payments](/blog/agent-payments) essay:** UCP assumes agents eventually spend within delegated authority; AP2 and wallet guardrails ([Cloudflare Wallets](/blog/cloudflare-wallets-agent-payments)) supply the buyer-side policy envelope.

SaaS companies selling **API access** should implement MPP/x402 first. **Shopify DTC brands** should implement UCP for Google agent discovery. Enterprise platforms may implement all layers.

---

## What UCP Means for Shopify Merchants

For **Shopify merchants**, UCP is the structural bridge to **agentic discovery and checkout** without rebuilding commerce backends:

- Sell in **Google AI Mode** and **Gemini** with merchant as seller of record
- Manage integrations via **Agentic Storefronts** in Shopify Admin
- Participate in pilots like **Direct Offers** (exclusive deals in AI Mode for select merchants)
- Access **Shopify Catalog** and Agentic plan options for AI-readable product data—even for some non-Shopify brands listing agentically

Requirements echo classic commerce hygiene: normalized catalog, accurate inventory, tax/shipping rules, and webhook-ready order ops. Agents amplify bad data faster than humans tolerate—stale SKUs become agent-visible errors at scale.

UCP does **not** replace Shopify Payments or human checkout; it adds **agent-addressable endpoints** parallel to your storefront. Payment reconciliation still flows through chosen handlers (Shop Pay, Google Pay, etc.).

---

## Conclusion

UCP is Google's and Shopify's bid to make **agent commerce a protocol problem, not an N×M integration problem**. Capability negotiation, handler extensibility, and multi-transport support reflect real retail complexity—discounts, loyalty, regional payments—that thin HTTP 402 models alone do not capture.

Treat UCP as the **full-journey commerce standard** for Google-aligned surfaces; pair it with [AP2](/blog/what-is-ap2-agent-payments-protocol) for authorization evidence and with [MPP](/blog/what-is-x402)/[x402](/blog/what-is-x402) where API micropayments matter. The agentic payments stack is complementary by design—UCP is the retail spine for merchants who already live in Shopify and Google ecosystems.

---

## FAQ

### What does UCP stand for?

**Universal Commerce Protocol**—an open standard co-developed by Google and Shopify for agent-to-merchant commerce.

### When was UCP announced?

**January 2026**, with Shopify engineering documentation dated January 11, 2026 and Google's retail announcement in the same window.

### Is UCP only for Shopify stores?

Shopify co-developed UCP and provides the primary merchant tooling, but the spec is **open**. Google launch materials emphasize cross-retailer endorsers (Target, Walmart, Etsy, etc.). Shopify also opened Catalog/agentic listing paths for some non-Shopify brands.

### How is UCP different from ACP?

[ACP](/blog/what-is-agentic-commerce-protocol) is OpenAI/Stripe's checkout protocol for ChatGPT Instant Checkout. UCP is Google/Shopify's broader **full-journey commerce** protocol for AI Mode, Gemini, Copilot, and multi-transport integrations. Many large merchants may support both over time.

### Does UCP replace AP2 or x402?

No. UCP handles **commerce sessions and capabilities**. [AP2](/blog/what-is-ap2-agent-payments-protocol) handles **authorization mandates**; [x402](/blog/what-is-x402)/[MPP](/blog/what-is-machine-payments-protocol) handle **HTTP-native machine payments**. Google describes them as compatible layers.

### Where can I read the UCP specification?

Start at [shopify.com/ucp](https://www.shopify.com/ucp) and Shopify's [engineering blog post](https://shopify.engineering/UCP); follow links to the public spec repository and capability handler documentation for implementers.
