---
title: "What Is the AP2 Agent Payments Protocol? — Mandates and FIDO"
description: "AP2 is Google's open Agent Payments Protocol for verifiable AI agent transactions. Learn mandates, Human Not Present flows, and FIDO Alliance governance."
slug: "what-is-ap2-agent-payments-protocol"
date: "2026-09-07"
updated: "2026-08-24"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 11
---

## TL;DR

- **AP2 (Agent Payments Protocol)** is an open standard for verifiable agent-initiated payments, originally developed by Google and donated to the **FIDO Alliance** in April 2026 to keep it platform-agnostic and community-governed.
- At its core, AP2 uses **Verifiable Digital Credentials (VDCs)** called **mandates**—cryptographically signed objects that record what a user authorized an agent to buy and how it may pay.
- **v0.2** reorganized v0.1's Intent/Cart/Payment model into **Checkout Mandates** and **Payment Mandates**, each with **Open** (pre-authorized constraints) and **Closed** (finalized transaction) states—enabling **Human Not Present** autonomous purchases.
- AP2 is a **trust and authorization layer**, not a checkout UI or HTTP transport; it complements [UCP](/blog/what-is-universal-commerce-protocol), [ACP](/blog/what-is-agentic-commerce-protocol), [x402](/blog/what-is-x402), and [MPP](/blog/what-is-machine-payments-protocol) rather than replacing them.
- For SaaS and API teams, AP2 matters when you need a **non-repudiable audit trail** linking human intent to agent execution—especially for regulated or high-value delegated spend.

---

## What Is AP2? — A Working Definition

The **Agent Payments Protocol (AP2)** is an open protocol that defines how AI agents, merchants, wallets, and payment providers coordinate around **user-authorized spending**. Google introduced AP2 in September 2025 as part of a broader push toward agentic commerce; by April 28, 2026, Google [donated AP2 to the FIDO Alliance](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/) and published **v0.2** on GitHub, with standardization continuing in FIDO's Agentic Authentication and Payments Technical Working Groups.

AP2 is not a payment processor, a wallet product, or a merchant checkout page. It is the **trust layer** that sits between agent reasoning and settlement rails—the cryptographic evidence that a specific agent acted within bounds a human (or policy engine) defined in advance. The [official documentation](https://ap2-protocol.org/) describes AP2 as designed for "secure, reliable, and interoperable agent commerce," available as an extension to the Agent2Agent (A2A) protocol and Universal Commerce Protocol (UCP), with more integrations in progress.

If your mental model of agent payments starts at "the agent swipes a card," AP2 starts earlier: **what did the user authorize, in a form a merchant and issuer can verify?** That question becomes load-bearing the moment an agent buys a limited-run ticket, tops up an API balance, or completes a purchase while the user is asleep.

---

## How AP2 Works: Mandates, VDCs, and the Open-to-Closed Flow

AP2 engineers trust using **Verifiable Digital Credentials (VDCs)**—tamper-evident, cryptographically signed digital objects that chain together into an auditable transaction record. The protocol centers on two mandate types, each operating in two stages.

**Checkout Mandate** captures what the user wants to buy. In **Open** form, it records constraints and goals before a specific cart exists—budget ceilings, allowed categories, merchant boundaries—for autonomous execution. In **Closed** form, it binds to a finalized checkout: specific items, prices, and merchant confirmation.

**Payment Mandate** captures how the user wants to pay—amount, instrument, timing, and conditions. Open Payment Mandates express spending constraints (for example, a $200 daily cap on approved instruments). Closed Payment Mandates authorize a specific amount tied to a finalized checkout.

The v0.2 redesign consolidated v0.1's three mandate concepts (Intent, Cart, Payment) into this two-type model—**Intent semantics map to Open Checkout**; **Cart semantics map to Closed Checkout**. Mandates use **SD-JWT** (Selective Disclosure JWT) with ECDSA signatures; Payment Mandates bind to Checkout JWT hashes so payment cannot detach from cart state.

Verifiers can then answer: Was the agent authorized? Did the final transaction stay within the granted constraints? Is there a cryptographic link between authorization, checkout, and payment? AP2 v0.2 also introduces explicit **Checkout Receipts** and **Payment Receipts**, mandate versioning, agent key binding, and constraint evaluation as first-class verification steps.

Google co-developed **Verifiable Intent (VI)** with Mastercard as an AP2-compatible framework for tamper-proof logs of user-authorized agent actions; both AP2 and VI were contributed to FIDO alongside the April 2026 donation. FIDO hosts two working groups: **Agentic Authentication TWG** (agent delegation identity) and **Payments TWG** (co-chaired by Mastercard and Visa) to mature AP2/VI into industry standards.

AP2 defines five core roles—**Shopping Agent**, **Credential Provider**, **Merchant**, **Merchant Payment Processor**, and **Trusted Surface** (a non-agentic UI for human consent)—though a single entity may hold multiple roles.

---

## Human Present vs Human Not Present

AP2 explicitly supports two transaction modes.

**Human Present** flows resemble assisted shopping: the user is available to confirm at critical moments. Mandates may transition quickly from Open to Closed because the user can approve the specific cart and payment in real time.

**Human Not Present** flows enable autonomous execution against pre-authorized constraints—the scenario Google highlights for securing limited-availability inventory the moment it goes on sale. Here, Open Checkout and Payment Mandates carry the full policy envelope; the agent acts without per-step approval; Closed mandates prove the final transaction matched what was authorized.

This distinction matters for risk and compliance teams. Human Present maps to familiar step-up authentication patterns. Human Not Present requires policy-time governance—caps, merchant allowlists, velocity limits, revocation—because there is no human in the loop at settlement time. The broader category argument in [agent payments](/blog/agent-payments) applies: infrastructure must express delegated authority with bounds, not impersonate a cardholder in a browser.

---

## Who Built AP2 and Who Supports It

Google originated AP2 and remains a major contributor through the FIDO transition. The [FIDO Alliance](https://fidoalliance.org/building-the-trust-layer-for-agentic-payments-with-ap2-and-verifiable-intent/) now hosts specification work, positioning AP2 alongside identity and authentication standards FIDO is known for.

Industry support spans payments networks, merchants, and technology platforms. Google's launch materials reference growing participation across the ecosystem; AP2 is designed to interoperate with **A2A** (agent-to-agent messaging), **MCP** (tool and context access), and **UCP** (full-journey commerce). Mastercard's Verifiable Intent contribution signals issuer-side interest in accountable agent authorization.

AP2 does not mandate a single payment instrument. The protocol's roadmap accommodates cards, bank transfers, stablecoins, and other methods through credential providers and payment processors—AP2 defines *authorization evidence*, not which rail clears funds.

---

## Where AP2 Sits in the Agent Payments Stack

Agentic payments in 2026 are a **stack of complementary protocols**, not a winner-take-all standard. AP2 occupies the **authorization and audit** layer.

| Layer | Role | Examples |
|-------|------|----------|
| Commerce / checkout | Cart, catalog, order lifecycle | [UCP](/blog/what-is-universal-commerce-protocol), [ACP](/blog/what-is-agentic-commerce-protocol) |
| Transport / settlement | Machine-readable payment over HTTP | [x402](/blog/what-is-x402), [MPP](/blog/what-is-machine-payments-protocol) |
| Trust / authorization | Verifiable user intent and agent authority | **AP2**, Verifiable Intent |
| Agent tooling | Tools, context, inter-agent messaging | MCP, A2A |

[x402](/blog/what-is-x402) answers "how does an HTTP client pay for a 402 response?" [MPP](/blog/what-is-machine-payments-protocol) extends that transport with subscriptions, streaming, and Stripe merchant rails. [ACP](/blog/what-is-agentic-commerce-protocol) and [UCP](/blog/what-is-universal-commerce-protocol) define how agents complete retail checkout with merchants. **AP2** answers "can you prove the human authorized this agent to spend this much, on this merchant, for this cart?"

Implementations can compose these layers. A UCP checkout on Google AI Mode might use AP2 mandates for authorization evidence and Google Pay for settlement. An API seller using x402 might reference AP2-compatible credentials where audit requirements demand human-delegated spend proof.

---

## AP2 vs x402, MPP, and ACP — One-Line Differences

- **AP2 vs x402:** x402 is HTTP-native payment transport; AP2 is cryptographic authorization evidence—x402 moves value, AP2 proves delegated intent.
- **AP2 vs MPP:** MPP is Stripe and Tempo's machine-payment wire format with lifecycle primitives; AP2 is the trust layer that can wrap either card or stablecoin settlement.
- **AP2 vs ACP:** ACP is OpenAI and Stripe's retail checkout API for agent surfaces; AP2 is cross-platform mandate semantics that ACP/UCP implementations can adopt for verifiable authorization.

None of these replace [smart routing](/blog/smart-routing) or human subscription billing—they address a different buyer: software runtimes spending on behalf of users.

---

## What AP2 Means for SaaS and API Businesses

Most SaaS teams will encounter AP2 indirectly, through platforms and wallets that adopt FIDO-hosted specifications—not by implementing mandate issuance on day one. The near-term implications are still concrete.

**Audit and finance** will ask for machine-readable proof linking agent actions to human policy. AP2-shaped receipts give security and RevOps a vocabulary beyond "the agent had an API key."

**Delegated spend products**—agent budgets, virtual wallets, harness payments—benefit from a shared mandate model rather than proprietary capability tokens per vendor. [Cloudflare Wallets](/blog/cloudflare-wallets-agent-payments) expresses a similar guardrails pattern; AP2 standardizes the evidence chain.

**High-value or regulated flows** (travel, healthcare APIs, financial data) will likely require Human Not Present support with explicit Open-to-Closed mandate transitions, not ad hoc pre-auth flags.

Teams building agent-native billing should monitor FIDO working group outputs and plan for **policy-time constraints** in product design now, even if full AP2 verification lands later. Clink's [Agentic Payments](https://clinkbill.com/agentic-payment) (Early Access) already treats scoped caps and machine-readable audit as first-class requirements—the same operating model AP2 formalizes at the protocol level.

---

## Conclusion

AP2 is the industry’s bet that agent commerce needs a **shared trust layer** before autonomous spending scales. By moving the protocol to the FIDO Alliance and shipping v0.2 with Human Not Present mandates, Google and partners are trying to ensure authorization evidence stays open, verifiable, and portable across checkout standards and payment rails.

For infrastructure teams, the actionable frame is layered: implement commerce with UCP or ACP, implement transport with x402 or MPP, and implement accountability with AP2-compatible mandates when auditors, issuers, or enterprise buyers require proof that an agent stayed inside human-defined bounds. The protocols stack; they do not compete for a single checkbox on a roadmap.

---

## FAQ

### What does AP2 stand for?

AP2 stands for **Agent Payments Protocol**. It is an open standard for verifiable, agent-initiated payments, now stewarded by the FIDO Alliance after Google's April 2026 donation.

### Is AP2 the same as Google Pay?

No. Google Pay is a consumer wallet and checkout product. AP2 is an open protocol defining mandate-based authorization for agent transactions; Google Pay may participate as a credential provider or settlement method within AP2 flows, but AP2 is not a Google-exclusive product.

### What changed in AP2 v0.2?

Version 0.2 reorganized mandates into **Checkout** and **Payment** types, each with **Open** and **Closed** states, replacing v0.1's Intent/Cart/Payment trio. It adds explicit support for **Human Not Present** autonomous transactions and clearer receipt and verification chains.

### Do I need AP2 if I already use x402 or MPP?

Not necessarily. x402 and MPP solve HTTP payment transport and merchant settlement. AP2 adds verifiable authorization evidence for delegated spend. Use AP2 when you need cryptographic proof of user intent; use x402/MPP when you need machines to pay for API resources.

### How is AP2 related to UCP and ACP?

UCP and ACP define **commerce checkout** between agents and merchants. AP2 defines **payment authorization credentials** that those flows can consume. Google has stated UCP is compatible with AP2; implementations can compose both.

### Is AP2 production-ready?

AP2 is actively standardizing under FIDO with public specifications and SDKs on GitHub. Adoption is early—treat it as an emerging standard with reference implementations, not a finished universal requirement for every agent payment as of mid-2026.
