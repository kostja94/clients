---
title: "Agentic Commerce Supported PSP Payment Processors — 2026 Reference"
description: "Agentic commerce supported PSP payment processors in 2026: Stripe ACS, Adyen Agentic, Worldpay, Nuvei, Antom, and more with live status, protocols, and regions."
slug: "agentic-commerce-merchant-stack-psp"
date: "2026-09-15"
updated: "2026-09-01"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 14
---

## TL;DR

- **Agentic commerce supported PSP payment processors** are acquirers and payment service providers that expose named agentic products—translation layers between open protocols ([ACP](/blog/what-is-agentic-commerce-protocol), [UCP](/blog/what-is-universal-commerce-protocol), [AP2](/blog/what-is-ap2-agent-payments-protocol)) and your existing card rails—not merely "stores that already accept cards through Stripe."
- As of **September 2026**, **Stripe Agentic Commerce Suite (ACS)** is **Live** in the U.S., Canada, and parts of Europe; **Adyen Agentic** is **Limited availability** for U.S. enterprise; **Worldpay** ships **Live** ACP integration docs; **Nuvei Agentic** is in **PoC** with a **Rolling out** target for H2 2026; **Airwallex**, **Checkout.com**, and **EBANX** remain **Thought leadership only** without a GA agentic SKU; **Antom EasySafePay** is a **Published solution** narrative for APAC merchants.
- A PSP row on a deck does not replace [storefront enablement on Shopify, Adobe, or headless stacks](/blog/agentic-commerce-merchant-stack-cms) or [buyer-surface coverage on ChatGPT and Gemini](/blog/agentic-commerce-agent-channels)—ACS live status does not syndicate your catalog to ChatGPT, and a Shopify Agentic toggle does not mint Shared Payment Tokens without the right PSP path.
- This list covers **retail agentic commerce PSPs** only—not [Machine Payments Protocol (MPP)](/blog/what-is-machine-payments-protocol) or x402 for API sellers. Visa Intelligent Commerce and Trusted Agent Protocol (TAP) sit adjacent as card-network identity layers, not PSP rows.
- **Last verified: September 2026.** Confirm waitlists, regions, and product names on linked Tier 0 sources before production commitments.

---

## What Is the PSP Layer in Agentic Commerce?

The **PSP layer** in agentic commerce is where protocol messages become settlement: delegated checkout sessions, Shared Payment Tokens, UCP payment handlers, and agent-aware fraud signals translated into the card and wallet rails you already operate. It sits between [where buyers initiate checkout in ChatGPT, Copilot, or Gemini](/blog/agentic-commerce-agent-channels) and the [catalog and cart APIs your commerce platform exposes](/blog/agentic-commerce-merchant-stack-cms).

In a typical retail stack, an agent channel sends a structured checkout request under ACP or UCP. Your CMS or headless API assembles line items, tax, and inventory. The **PSP agentic product** validates the request, tokenizes payment credentials for agent completion, and routes authorization to your acquirer relationship. Without that translation layer, "we process cards" stops at a human clicking Pay on your website—the agent never receives a documented endpoint to complete payment on the buyer's behalf.

This distinction drives most 2026 procurement confusion. **Stripe** as a card processor is not the same as **Stripe ACS** as an ACP/UCP enablement suite. **Adyen** as a global acquirer is not the same as **Adyen Agentic** as a modular Feed + Cart + Payments API for enterprise agent surfaces. Industry decks that list eight PSP logos under "merchant stack" often collapse card acceptance, protocol translation, and card-network agent identity into one checkbox—engineering teams then discover, during Copilot waitlist review, that delegated payment was never wired.

The PSP layer also differs from **orchestration** and from **machine payments**. Multi-PSP routing products connect several acquirers for retry and cost optimization; agentic PSP products add protocol-specific endpoints and token semantics for retail agent checkout. [MPP and x402](/blog/what-is-machine-payments-protocol) address agent-to-service micro-transactions and API billing—adjacent vocabulary, different integration checklist. For stack diagrams and how retail agentic commerce fits together, start with the [agent payments](/blog/agent-payments) hub.

---

## How to Read This List

Each row in the main table reports six fields: **PSP**, **Agentic product / enablement path**, **Protocol**, **Status**, **Region**, and **Source**. Status reflects **public Tier 0 documentation** as of September 2026—not partner slide decks, press releases without product pages, or SEO aggregators listing logos without enablement paths.

**Status taxonomy:**

| Status | Meaning |
|--------|---------|
| **Live** | Named agentic product documented for production or broad merchant enrollment |
| **Limited availability** | Official product exists; cohort, enterprise, or regional gates apply |
| **PoC** | Documented proof-of-concept or pilot; not GA for general merchants |
| **Rolling out** | Public roadmap with partial availability; full GA still pending |
| **Thought leadership only** | Blog, report, or strategy content without a named GA agentic product |
| **Published solution (no GA product name)** | Documented solution narrative or regional product without Stripe/Adyen-class global GA |

**Protocol** lists open standards the PSP publicly supports in agentic context—ACP, UCP, AP2, MCP, or card-network programs (Visa Intelligent Commerce). **Region** follows operator-stated geographic limits, not inferred global coverage.

**Confidence:** Rows marked Live, Limited availability, or PoC are backed by PSP operator documentation (Stripe, Adyen, Worldpay, Nuvei, Antom). Thought leadership rows (Airwallex, Checkout.com, EBANX) reflect absence of a named GA agentic SKU in public docs after targeted search—not a claim that engineering is impossible.

When comparing PSPs for a go-to-market memo, ask **journey type** first: **ACP-aligned** surfaces (ChatGPT discovery, Meta Facebook Buy now via Stripe ACS) versus **UCP-aligned** surfaces (Gemini, Copilot Checkout) versus **dual-protocol** merchants who need both. A PSP that excels on ACP delegate payment may still require separate UCP handler work—or a modular product like Adyen Agentic that advertises cross-protocol compatibility.

---

## Supported Payment Processors (MAIN TABLE)

| PSP | Agentic product / enablement path | Protocol | Status | Region | Source |
|-----|-----------------------------------|----------|--------|--------|--------|
| **Stripe** | **Agentic Commerce Suite (ACS)**: Dashboard catalog upload, delegated checkout, Shared Payment Tokens (SPT); Meta and Google partner paths | **ACP** (co-founder) · **UCP** (Google partner) · SPT · MPP (separate machine-payments line) | **Live** | U.S., Canada, parts of Europe; custom integration **waitlist** | [ACS for sellers](https://docs.stripe.com/agentic-commerce/for-sellers) · [Sessions 2026](https://stripe.com/blog/everything-we-announced-at-sessions-2026) · [Meta checkout](https://stripe.com/newsroom/news/checkout-for-facebook) |
| **Adyen** | **Adyen Agentic**: modular Feed + Cart + Payments APIs; Meta AI checkout compatibility | **UCP** · **ACP** · **AP2** | **Limited availability** | U.S. enterprise launch (June 2026) | [Adyen Agentic press release](https://www.adyen.com/press-and-media/adyen-agentic) |
| **Airwallex** | Protocol interpretation and infrastructure positioning; **no** named agentic product GA announcement | ACP · UCP · VIC (discussed) | **Thought leadership only** | Global (blog scope) | [Airwallex agentic protocols blog](https://www.airwallex.com/global/blog/understanding-agentic-commerce-protocols) |
| **Checkout.com** | **Neutral middle layer** strategy; Vault + agent-level analytics direction; Visa TAP early partner | ACP · UCP (compatibility narrative) | **Thought leadership only** | — | [Checkout.com agentic FAQ blog](https://www.checkout.com/blog/agentic-commerce-questions-answered) · [Visa TAP announcement](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html) |
| **Worldpay** | **ACP** OpenAI Instant Checkout approved partner; delegate payment Sessions API; **UCP** collaboration with Google | **ACP** · **UCP** | **Live** | Global (ACP docs; UCP follows Google surfaces) | [Worldpay ACP docs](https://docs.worldpay.com/access/products/ai/acp) · [Worldpay × Google UCP](https://www.worldpay.com/en-CA/news/worldpay-continues-collaboration-with-google) |
| **Nuvei** | **Nuvei Agentic**: Protocol Compatibility Layer + KYA; Visa in-agent payment PoC (July 2026) | **ACP** · **AP2** · **MCP** · VIC | **PoC** (Visa pilot); product target **Rolling out** H2 2026 | Global roadmap | [Nuvei Agentic announcement](https://www.nuvei.com/posts/nuvei-completes-first-party-in-agent-payment-with-visa-unveils-merchant-led-agentic-payments-strategy) |
| **EBANX** | LATAM-focused insights on ACP ecosystem; **no** named agentic SKU | ACP (discussed) | **Thought leadership only** | LATAM perspective | [EBANX agentic commerce insights](https://www.ebanx.com/en/insights/articles/agentic-commerce-how-can-ai-agents-pay-for-things/) |
| **Antom** | **EasySafePay**; self-described UCP early certification partner; AI Payment Integration Skill | **UCP** · **AP2** (in cooperation) · proprietary ACTP (Ant ecosystem) | **Published solution (no GA product name)** | APAC / cross-border merchants | [Antom agentic commerce (CN)](https://knowledge-cn.antom.com/agentic-commerce/) · [Antom docs](https://docs.antom.com/ac/apo/cardinfocallmerchant) |

For ChatGPT-specific feed and delegated-payment mechanics once ACS is in scope, see our [step-by-step ChatGPT merchant setup guide](/blog/how-to-sell-on-chatgpt).

---

## PSP Categories: Protocol Translators vs Card Rails

Agentic PSP products in 2026 cluster into two architectural roles that procurement teams often merge incorrectly.

**Protocol translators** expose named APIs that map ACP, UCP, or AP2 messages onto your existing acquirer relationship. Stripe ACS, Adyen Agentic, Nuvei Agentic (target), and Worldpay's ACP Sessions API belong here. Their value is **surface coverage**: one integration team can answer ChatGPT delegate payment, Meta embedded checkout, and—where documented—UCP handler requirements without rewriting checkout for each agent brand. Tradeoffs include geographic enrollment gates (Stripe ACS live in North America and parts of Europe first), enterprise-only cohorts (Adyen Agentic U.S. launch), and waitlists for custom stacks not on Shopify or Wix.

**Card rails and acquirer depth** remain the settlement substrate underneath translation. Worldpay, Nuvei, Checkout.com, and EBANX bring long-standing merchant acquiring in specific regions; agentic products sit **atop** those rails rather than replacing them. A merchant already on Worldpay for U.S. card present and e-com may add ACP delegate documentation without switching acquirer—whereas a Stripe-native DTC brand might adopt ACS because OpenAI and Meta reference Stripe SPT patterns in Tier 0 docs.

**Thought-leadership-only PSPs** (Airwallex, Checkout.com, EBANX as of September 2026) publish credible protocol explainers and strategic positioning—Checkout.com's analysis of OpenAI's March 2026 pivot aligns with operator narratives—but lack a **product name and enrollment path** comparable to ACS or Adyen Agentic. Checkout.com appears on [Visa's TAP early partner list](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html) alongside Stripe, Adyen, Shopify, and Nuvei; that signals identity-layer collaboration, not a standalone "Checkout.com Agentic" GA SKU in public documentation.

**Regional published solutions** (Antom EasySafePay) target APAC and cross-border merchants with UCP-oriented narratives and Ant Group ecosystem tooling. Antom self-describes as among the first UCP-certified fintech partners in Asia; independent Google UCP partner list corroboration was not located in our verification pass—treat certification claims with the linked Antom Tier 0 sources, not as implied Gemini enrollment.

Hybrid reality: most global merchants need **translator + rail + CMS** alignment. Shopify Agentic Storefronts can auto-enroll catalog paths while Stripe ACS handles ACP payment translation—but Copilot Checkout still demands UCP profile work on the merchant side. PSP choice is necessary, not sufficient.

---

## Stripe ACS vs Adyen Agentic vs Nuvei (narrative comparison)

Three PSPs dominate English-language agentic commerce discourse in 2026; they are not interchangeable drop-in replacements.

**Stripe Agentic Commerce Suite (ACS)** is the reference implementation for **ACP-first** retail flows. Stripe co-founded [ACP](/blog/what-is-agentic-commerce-protocol) with OpenAI; ACS documentation covers catalog upload in Dashboard, delegated checkout, Shared Payment Tokens, and partner paths for Meta Facebook native checkout and Google UCP surfaces. **Live** status in the U.S., Canada, and parts of Europe makes ACS the default answer when decks say "ChatGPT checkout" or "Meta Buy now." Limitations matter: custom integrations outside Shopify/Wix cohorts often hit **waitlist** queues; ACS does not replace [UCP profile](/blog/what-is-universal-commerce-protocol) engineering for headless merchants targeting Copilot or Gemini; MPP is a **separate** Stripe product line for machine/API payments, not retail ACS.

**Adyen Agentic**, announced June 16, 2026, targets **enterprise merchants** needing modular Feed + Cart + Payments APIs with explicit **UCP, ACP, and AP2** compatibility and Meta AI checkout alignment. **Limited availability** in the U.S. at launch reflects cohort gating—not a missing product. Adyen's strength is unified global acquiring plus a stated **protocol compatibility layer** for merchants who refuse single-PSP dependency on Stripe SPT semantics. Tradeoffs: smaller merchants may lack enrollment access day one; integration depth assumes enterprise API maturity comparable to existing Adyen unified commerce deployments.

**Nuvei Agentic** occupies **PoC → Rolling out** territory. Nuvei's July 2026 announcement documents a first-party **in-agent payment proof-of-concept with Visa** and previews a merchant-led agentic strategy with Protocol Compatibility Layer and KYA (Know Your Agent) components. Public materials target **H2 2026** for broader product availability. Nuvei fits merchants already on Nuvei rails who want a documented agentic roadmap without migrating to Stripe—provided they accept pilot-stage status in September 2026 and plan engineering around ACP, AP2, MCP, and VIC adjacency.

**Decision heuristic:** If your near-term revenue bet is **U.S. ChatGPT discovery and Meta ads**, Stripe ACS is the fastest documented path—especially on Shopify or Wix where ACS enrollment is bundled with platform agentic channels. If you are **enterprise multi-region** with existing Adyen contracts and need **dual-protocol** coverage without Stripe-only token semantics, evaluate Adyen Agentic enrollment. If you are **Nuvei-native** or prioritizing **Visa in-agent PoC** learnings, track Nuvei Agentic H2 rollout while maintaining interim custom UCP/ACP work through other translators.

Worldpay remains the clearest **non-Stripe ACP delegate** option with **Live** integration documentation for OpenAI-era flows—relevant when acquirer relationship politics favor Worldpay/FIS over Stripe but agent channel requirements still cite ACP.

---

## Visa Intelligent Commerce and TAP (card network adjacent layer, not a PSP row)

**Visa Intelligent Commerce (VIC)** and **Trusted Agent Protocol (TAP)** address card-network agent identity, tokenization, and passkey-style authorization—not catalog feeds or CMS toggles. Merchants rarely integrate VIC directly from a commerce admin panel; PSPs and platforms abstract agent tokens into checkout flows.

Visa's [TAP announcement](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html) lists early partners including **Stripe, Adyen, Shopify, Checkout.com, and Nuvei**—not a exhaustive PSP enablement matrix, but a signal of who participates in agent identity experiments. Nuvei's documented Visa in-agent payment PoC connects this layer to **Nuvei Agentic** roadmap. Checkout.com's TAP listing supports its agent analytics and Vault narrative even without a named "Checkout.com Agentic" GA product.

Do **not** conflate third-party payment enabler press releases with Visa Tier 0 partnership status. Some vendors advertise Visa APAC agent programs without a matching page on visa.com or developer.visa.com—architecture reviews should treat **VIC/TAP official documentation** as the identity-layer source of truth and PSP agentic products as the settlement translation layer.

For retail planning, sequence **PSP agentic product first**, **VIC/TAP second** where mandated by handler or issuer rules—not the reverse.

---

## Common Mistakes

The most expensive mistake in 2026 remains equating **"uses Stripe"** with **"agent-ready."** Standard Stripe Checkout or Billing integrations do not register ACP endpoints, upload agentic catalogs, or mint Shared Payment Tokens. ACS enrollment is a separate Dashboard and documentation path with geographic limits. Teams that skip ACS while pursuing [ChatGPT merchant feeds](/blog/how-to-sell-on-chatgpt) often complete discovery setup without delegated payment—a partial journey that matches OpenAI's post-March 2026 **merchant-owned checkout** emphasis but fails in-agent payment sheet pilots.

A second mistake is **PSP signup without CMS enrollment**. Live ACS status does not enable [Shopify Agentic Storefronts or Wix ACP signatory paths](/blog/agentic-commerce-merchant-stack-cms) automatically. Conversely, flipping Shopify's Agentic sales channel without ACS—or an approved ACP delegate like Worldpay—leaves catalog syndication without payment translation. Sequence: pick [your target AI shopping surfaces](/blog/agentic-commerce-agent-channels), confirm [storefront enablement](/blog/agentic-commerce-merchant-stack-cms), then enroll the PSP agentic product from the table above.

Third, **treating thought-leadership blogs as product availability**. Airwallex, Checkout.com, and EBANX publish useful protocol explainers; none ship a named GA agentic SKU comparable to ACS or Adyen Agentic in September 2026 public docs. RFPs should require **product name, enrollment URL, and region table**—not blog URLs alone.

Fourth, **collapsing retail PSP agentic products into MPP/x402**. Stripe's MPP line and Coinbase x402 serve **API and agent-wallet micro-payments**—developer tool calls, not Gemini buying sneakers. API sellers belong under [Machine Payments Protocol](/blog/what-is-machine-payments-protocol), not this PSP table.

Fifth, **ignoring dual-protocol reality**. [ACP](/blog/what-is-agentic-commerce-protocol) and [UCP](/blog/what-is-universal-commerce-protocol) optimize for different operator surfaces. Implementing ACS for ChatGPT does not satisfy Copilot's UCP Merchant Center requirements. Adyen Agentic advertises cross-protocol modularity; Stripe ACS plus separate UCP handler work remains common for headless stacks.

---

## What This List Does Not Cover

This article maps **payment processors and acquirers**—the settlement and protocol translation layer. Two adjacent merchant-stack dimensions have dedicated reference articles; do not infer their rows from the PSP table above.

**CMS and commerce platforms.** Whether Agentic Storefronts is live on Shopify, Adobe Commerce MCP is rolling out, or SHOPLINE has no documented path—that is covered in our [commerce platform enablement reference](/blog/agentic-commerce-merchant-stack-cms). A live ACS row does not mean your Magento instance enrolled Copilot Checkout.

**Buyer-facing AI surfaces.** Protocol and regional requirements differ for ChatGPT, Copilot, Gemini, and messaging apps. See our [channel live-status reference](/blog/agentic-commerce-agent-channels)—not duplicated here.

**Machine and API payments.** SaaS API billing, agent-to-service micropayments, and developer wallet flows belong under [MPP and x402](/blog/what-is-machine-payments-protocol)—not retail PSP agentic products.

**Payment orchestration vendors.** Multi-PSP routing, policy guardrails, and agent authorization orchestration may sit **above** individual PSP agentic endpoints; orchestration does not replace ACS, Adyen Agentic, or Worldpay ACP documentation per acquirer relationship.

When scoping a project: (1) pick [AI shopping surfaces from the channel list](/blog/agentic-commerce-agent-channels), (2) confirm [storefront enablement on your CMS](/blog/agentic-commerce-merchant-stack-cms), (3) enroll the PSP agentic product from the table above, (4) run feed and inventory ops. Skipping step 3 after CMS enrollment syndicates catalog without settlement; skipping step 2 after PSP signup tokenizes payments without discovery.

---

## Conclusion

**Agentic commerce supported PSP payment processors** are a short list of named agentic products—not every logo on an industry deck. As of September 2026, **Stripe ACS** is the broadest **Live** retail path for ACP-oriented surfaces; **Adyen Agentic** offers **Limited availability** enterprise modularity across UCP, ACP, and AP2; **Worldpay** documents **Live** ACP delegate integration; **Nuvei Agentic** is **PoC** with **Rolling out** targets; **Antom EasySafePay** serves APAC **Published solution** narratives; and **Airwallex**, **Checkout.com**, and **EBANX** remain **Thought leadership only** without GA agentic SKUs in public documentation.

Match your PSP row to the [AI surfaces where you want discovery or checkout](/blog/agentic-commerce-agent-channels) and the [storefront platform that syndicates your catalog](/blog/agentic-commerce-merchant-stack-cms) before filing engineering estimates. Dual-protocol U.S. coverage still commonly means ACS or Worldpay for ACP surfaces plus UCP profile and handler work for Google and Microsoft—unless Adyen Agentic enrollment covers your cohort.

Protocol context: [ACP](/blog/what-is-agentic-commerce-protocol), [UCP](/blog/what-is-universal-commerce-protocol), and [AP2 mandates](/blog/what-is-ap2-agent-payments-protocol) on the [agent payments hub](/blog/agent-payments).

Teams layering agent payment policy and multi-PSP orchestration above ACS or Adyen Agentic can explore [Clink agentic payment infrastructure](https://clinkbill.com/agentic-payment) (**Early Access** as of mid-2026)—downstream of channel, CMS, and PSP scope, not a replacement for Stripe ACS enrollment or platform Agentic Storefronts.

---

## FAQ

### Which PSPs support agentic commerce in 2026?

**Stripe ACS**, **Adyen Agentic**, **Worldpay ACP APIs**, and **Nuvei Agentic** (PoC / rolling out) are the PSPs with named agentic products in public Tier 0 documentation as of September 2026. **Antom EasySafePay** publishes an APAC solution narrative. **Airwallex**, **Checkout.com**, and **EBANX** discuss agentic commerce strategically without a comparable GA product name.

### Does using Stripe automatically make my store agent-ready?

**No.** Standard Stripe card processing is separate from **Stripe Agentic Commerce Suite (ACS)**, which provides ACP endpoints, delegated checkout, catalog tooling, and Shared Payment Tokens. You also need [Agentic Storefronts or equivalent CMS enrollment](/blog/agentic-commerce-merchant-stack-cms) and [feeds on your target AI shopping surfaces](/blog/agentic-commerce-agent-channels).

### What is the difference between Stripe ACS and Adyen Agentic?

**Stripe ACS** is **Live** for ACP-first flows with OpenAI and Meta partner paths—strongest when ChatGPT discovery and Stripe SPT patterns are central. **Adyen Agentic** offers modular Feed + Cart + Payments with **UCP, ACP, and AP2** compatibility under **Limited availability** for U.S. enterprise—stronger for merchants already on Adyen seeking dual-protocol APIs without Stripe-only semantics.

### Is Checkout.com a live agentic commerce PSP?

**Not as a named GA product** in public documentation as of September 2026. Checkout.com publishes agentic commerce strategy content and appears on Visa TAP early partner lists, but lacks a standalone "Checkout.com Agentic" enrollment path comparable to Stripe ACS or Adyen Agentic.

### How does this PSP list relate to MPP and x402?

This list covers **retail catalog checkout** on consumer AI surfaces. [Machine Payments Protocol (MPP)](/blog/what-is-machine-payments-protocol) and x402 address **API and agent-wallet micro-transactions** between services—Stripe documents MPP as a separate line from ACS. Stack them separately in architecture reviews.

### Do I need a PSP agentic product if I use Shopify Agentic Storefronts?

**Usually yes for payment translation.** Shopify Agentic Storefronts handle catalog syndication and channel enrollment, but ACP delegated payment typically routes through **Stripe ACS** or an approved ACP delegate such as **Worldpay**. UCP native checkout still requires mandated payment handlers. Confirm PSP path alongside platform toggles—not instead of them.
