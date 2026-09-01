---
title: "Agentic Commerce Supported Platforms CMS — Merchant Stack (2026 Reference)"
description: "Agentic commerce supported platforms CMS in 2026: verified enablement paths for Shopify, Adobe, WooCommerce, Wix, 91APP, SHOPLINE, and custom stacks."
slug: "agentic-commerce-merchant-stack-cms"
date: "2026-09-14"
updated: "2026-09-01"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 14
---

## TL;DR

- **Agentic commerce supported platforms CMS** refers to the e-commerce and content-management systems that expose catalog, checkout, or payment surfaces an AI agent can call—via open protocols ([ACP](/blog/what-is-agentic-commerce-protocol), [UCP](/blog/what-is-universal-commerce-protocol), MCP) or platform-native channels—not merely "stores that accept Stripe."
- As of **September 2026**, **Shopify** is the only major SaaS platform with **live** multi-channel agentic storefronts (ChatGPT discovery, Copilot Checkout, Google UCP); **Adobe Commerce**, **Wix**, and **WooCommerce** are **partial or rolling out**; **91APP AgentOne** is an **enterprise operations agent**, not an ACP/UCP consumer storefront; **SHOPLINE** has **no official agentic enablement** found in public documentation.
- **Custom**, **POS**, and **booking** stacks can participate by publishing a UCP profile at `/.well-known/ucp` and wiring checkout REST or MCP endpoints—typically with a PSP translation layer such as Stripe ACS.
- This list covers the **CMS / commerce platform layer** only. Which AI surfaces your buyers use is in our [ChatGPT, Copilot, and Gemini channel status list](/blog/agentic-commerce-agent-channels); which PSP translates protocol messages is in our [Stripe ACS, Adyen Agentic, and Worldpay enablement list](/blog/agentic-commerce-merchant-stack-psp).
- **Last verified: September 2026.** Protocol status changes quickly; confirm against platform changelogs before production commitments.

---

## What Is the Merchant Stack in Agentic Commerce?

The **merchant stack** in agentic commerce is everything on the seller side that lets an AI agent—or an agent channel acting on behalf of a buyer—discover products, negotiate a cart, and complete payment without breaking merchant-of-record rules. It sits below buyer surfaces such as [ChatGPT discovery and Copilot Checkout](/blog/agentic-commerce-agent-channels) and above the [PSP rails that mint Shared Payment Tokens](/blog/agentic-commerce-merchant-stack-psp).

A complete stack typically includes four layers: your **commerce platform** (Shopify, Adobe Commerce, headless CMS, custom API), a **catalog syndication or feed path** (Shopify Catalog, OpenAI product feed, Google Merchant Center), a **checkout or delegated-payment interface** (ACP checkout sessions, UCP native checkout, MCP tools), and a **PSP or tokenization layer** (Stripe Agentic Commerce Suite, Adyen Agentic, Visa Intelligent Commerce). The CMS row in industry decks is the first layer—whether your storefront software ships agentic enablement or forces you to build it.

This matters because search intent around **agentic commerce supported platforms CMS** often collapses two different questions: "Does my platform integrate with Stripe?" and "Can buyers complete an agent journey on ChatGPT or Gemini through my platform without a six-month custom project?" The first is necessary but not sufficient. Agent readiness requires documented protocol endpoints, sales-channel enrollment, or a published UCP profile—not just a working card form on your website.

For the broader architecture—including how this differs from [machine/API payments (MPP)](/blog/what-is-machine-payments-protocol)—start with the [agent payments](/blog/agent-payments) hub. Retail agentic commerce and API micropayments share vocabulary but not the same integration checklist.

---

## How to Read This List

Each row in the main table below reports four fields: **Platform**, **Enablement path** (how a merchant on that platform actually turns agentic commerce on), **Protocol** (which open or proprietary standards are involved), and **Status** (what public Tier 0 documentation supports as of September 2026).

Status values use a fixed taxonomy:

| Status | Meaning |
|--------|---------|
| **Live** | Production or general-availability enablement documented by the platform operator; merchants can enroll or are auto-enrolled under stated conditions |
| **Partial** | Some protocol surfaces shipped; others depend on extensions, waitlists, or third-party modules |
| **Committed / Rolling out** | Public commitment and engineering in progress; no full native GA module yet |
| **Gradual rollout** | Live for eligible cohorts; not all merchants or regions |
| **Enterprise agent (not storefront)** | Platform offers an AI agent product for merchant operations—not consumer-facing ACP/UCP checkout |
| **Not found** | No official agentic commerce enablement page, protocol implementation, or signatory status located in public documentation |

**Region notes:** Most live U.S. retail agentic paths (ChatGPT shopping discovery, Copilot Checkout, Google AI Mode native checkout) target **U.S. buyers** first even when the merchant is based elsewhere. APAC-native platforms may offer strong local commerce tooling without joining global ACP/UCP coalitions—do not assume cross-listing on a slide deck equals protocol support.

**Confidence:** Rows marked Live or Partial are backed by platform operator documentation (Shopify, Adobe, Wix, WooCommerce, 91APP). SHOPLINE's "Not found" reflects absence of an official agentic page after targeted search—not a claim that engineering is impossible.

---

## Supported CMS and Commerce Platforms (MAIN TABLE)

| Platform | Enablement path | Protocol | Status |
|----------|-----------------|----------|--------|
| **Shopify** | **Agentic Storefronts** sales channel; Shopify Catalog syndication to ChatGPT, Microsoft Copilot Checkout, Google UCP (select merchants); Stripe ACS for ACP surfaces | **UCP** (co-founder) · **ACP** (via Stripe ACS) · **MCP** | **Live** — millions of U.S.-buyer-eligible merchants; multi-channel enrollment via Admin → Sales channels → Agentic |
| **Adobe Commerce (Magento)** | Public commitment to UCP, ACP, AP2; **Commerce MCP Server** (Summit 2026); partner/custom modules for UCP profile—no native GA UCP module mid-2026 | **UCP** · **ACP** · **AP2** · **MCP** | **Committed / Rolling out** — enterprise roadmap live; production UCP profile typically requires SI or custom work today |
| **WooCommerce** | WordPress **MCP** (WP 6.9 / WC 10.3); **Google for WooCommerce** for Merchant Center / UCP-adjacent feeds; **Stripe agentic extension** announced, not GA | **MCP** · **UCP** (via Google Merchant Center) · **ACP** (via Stripe, coming) | **Partial** — MCP and Google path shipped; Stripe ACS agentic bundle still rolling out |
| **Wix** | First major CMS **ACP signatory**; **Stripe ACS** + PayPal; Site **MCP** / NLWeb for agent-readable storefront | **ACP** · **UCP** (platform-layer) · **MCP** | **Gradual rollout** — eligible merchants; not universal auto-enrollment |
| **91APP** | **AgentOne** — enterprise retail/food OMO operations agent (inventory, marketing, customer ops); Commerce Cloud API | Proprietary **AgentOne** — **not** ACP/UCP consumer checkout | **Enterprise agent (not storefront)** — launched July 2026; distinct from Shopify-style agentic storefronts |
| **SHOPLINE** | No agentic commerce product page or protocol signatory found; migration tooling from 91APP exists | — | **Not found** — no official ACP/UCP enablement in public docs |
| **POS systems** | Typically **headless/API** checkout exposed through PSP agentic layer or custom UCP profile; no major POS vendor ships native ChatGPT/Copilot channel as of Sept 2026 | **UCP** · **ACP** (via PSP) · proprietary POS APIs | **Varies by implementation** — treat as custom integration |
| **Booking / services** | Third-party connectors (e.g., SimplyBook via CDH APIs); **not** UCP-native out of the box | Proprietary APIs · optional custom **UCP** | **Varies by implementation** — services merchants usually custom-build |
| **Custom / headless** | Publish **`/.well-known/ucp`** profile; implement checkout REST/MCP; OpenAI product feed at [chatgpt.com/merchants](https://chatgpt.com/merchants/); Stripe ACS waitlist for non-Shopify retail | **UCP** · **MCP** · **ACP** (optional) · **AP2** (when mandated by handler) | **Live path exists** — engineering-owned; no platform toggle |

Sources: [Shopify Agentic Commerce](https://www.shopify.com/blog/how-agentic-commerce-works), [Adobe Commerce commitment](https://business.adobe.com/blog/adobe-commerce-commits-to-agentic-commerce-standards), [WooCommerce Agentic](https://woocommerce.com/agentic-commerce/), [Wix Agentic Commerce](https://www.wix.com/blog/agentic-commerce-on-wix), [91APP AgentOne](https://91app.com/en/blog/91app-202607-agentone-en/), [Google UCP native checkout guide](https://developers.google.com/merchant/ucp/guides/checkout/native), [UCP spec](https://ucp.dev/).

---

## Platform Categories: SaaS vs Vertical vs Custom

Agentic enablement clusters into three merchant archetypes. The category determines whether you flip a sales-channel switch or staff a protocol engineering project.

**Global SaaS storefronts (Shopify, Wix, WooCommerce on managed hosting)** optimize for self-serve enrollment. Shopify leads because Agentic Storefronts bundles catalog syndication, channel toggles, and payment handler relationships into one admin surface—reducing the coordination tax that broke early OpenAI Instant Checkout pilots. Wix follows as an ACP signatory with Stripe ACS, but rollout is cohort-based. WooCommerce splits the difference: MCP and Google paths are real today; full Stripe agentic parity is still "coming" on the official agentic commerce page.

**Enterprise commerce suites (Adobe Commerce / Magento)** orient toward committed standards participation and MCP for B2B/custom workflows. Adobe's public blog commits to UCP, ACP, and AP2 with a Commerce MCP Server—a credible enterprise signal—but mid-2026 production deployments still lean on systems integrators rather than a click-to-enable UCP module. For Magento merchants, "committed" means budget for partner modules and a UCP profile audit, not a free upgrade toggle.

**Vertical APAC platforms (91APP, SHOPLINE)** illustrate a common deck-versus-docs gap. **91APP AgentOne** is a serious enterprise AI product for retail operations—inventory, campaigns, OMO workflows—released July 2026. It is **not** the same category as Shopify Agentic Storefronts or an ACP checkout gateway. Merchants evaluating Taiwan or Southeast Asia stacks should not conflate "our platform has an AI agent" with "our platform syndicates catalog to ChatGPT under UCP." **SHOPLINE**, despite brand proximity to 91APP in migration tooling, shows **no official agentic commerce announcement** in public documentation as of September 2026—plan for custom UCP/feed work or a platform switch if global agent channels are strategic.

**Custom, POS, and booking** merchants inherit maximum flexibility and maximum responsibility. Google's [UCP native checkout guide](https://developers.google.com/merchant/ucp/guides/checkout/native) and Microsoft's [Dynamics 365 Commerce MCP](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/06/29/dynamics-365-commerce-introduces-agentic-capabilities-with-model-context-protocol-mcp/) demonstrate that any catalog with a stable API can expose agentic surfaces—provided engineering publishes a valid UCP profile, keeps inventory fresh, and connects a mandated payment handler. POS-heavy retailers usually route through headless cart APIs plus a PSP agentic translation layer rather than waiting for a terminal vendor to ship Copilot Checkout.

---

## Shopify vs Headless vs APAC Platforms

Choosing among Shopify, headless/custom, and APAC vertical platforms is really choosing among **enablement ownership**, **agent channel coverage**, and **regional buyer reality**.

**Shopify** is the reference implementation for multi-channel agentic retail in 2026. Agentic Storefronts enrolls eligible U.S.-buyer stores into ChatGPT product discovery (with checkout typically on the merchant's Shopify site), Microsoft Copilot Checkout (UCP), and select Google AI Mode / Gemini native checkout paths. Shopify co-founded UCP and routes ACP-oriented flows through Stripe ACS—so a merchant on Shopify can pursue both major protocol camps without maintaining separate feed pipelines for each. Tradeoffs: Shopify Pay and Catalog eligibility gates exclude some SKUs silently; international discovery expansion lags U.S. live status; you accept platform channel policy, not fully self-hosted protocol control. For a step-by-step ChatGPT path, see our [ChatGPT merchant setup guide](/blog/how-to-sell-on-chatgpt).

**Headless and custom stacks** suit brands that already invested in composable commerce—Magento Open Source without Adobe's enterprise bundle, commercetools, Medusa, bespoke DTC. The enablement path is OpenAI's merchant feed application plus optional Stripe ACS waitlist, combined with a hand-rolled UCP profile at `/.well-known/ucp` and MCP tools for enterprise agents. Microsoft and Google documentation assumes engineering ownership of Merchant Center feeds, checkout REST endpoints, and AP2 handler wiring. Advantage: no platform gate on catalog semantics or checkout UX. Cost: every agent channel is a project, and feed freshness becomes your on-call problem—the same inventory drift that pushed OpenAI to [deprioritize standalone Instant Checkout](https://openai.com/index/powering-product-discovery-in-chatgpt/) in March 2026.

**APAC vertical platforms** optimize for local super-app and OMO workflows, not necessarily Google/OpenAI U.S. discovery. 91APP's AgentOne helps large retailers run AI-assisted operations inside the 91APP ecosystem; it does not substitute for UCP enrollment on Gemini. SHOPLINE merchants lack even that public agentic narrative—treat agent channels as greenfield. If your buyers live on WeChat or LINE proprietary commerce, global ACP/UCP may be irrelevant near-term; if you sell to U.S. buyers through a SHOPLINE storefront, assume custom integration or migrate catalog to a globally syndicated platform.

**Decision heuristic:** If U.S. AI-surface discovery is a 2026 revenue bet and you are not already headless-composable, Shopify's live Agentic Storefronts minimize time-to-syndication. If you are enterprise Magento with SI relationships, Adobe's committed MCP/UCP roadmap may fit existing contracts—budget six-plus months for production hardening. If you are APAC-native with no cross-border agent strategy, verify local agent payment paths before forcing ACP/UCP compliance that your platform never advertised.

---

## Common Mistakes

The most expensive mistake in 2026 agentic commerce planning is equating **"we use Stripe"** with **"we are agent-ready."** Stripe processes cards; **Stripe Agentic Commerce Suite (ACS)** exposes delegated checkout, catalog upload, and ACP endpoint translation for agent channels. A standard Stripe Checkout integration does not automatically register your SKUs on ChatGPT, satisfy UCP's `/.well-known/ucp` schema, or mint Shared Payment Tokens for agent completion. ACS has geographic and waitlist constraints—U.S./Canada and parts of Europe for live Dashboard enrollment; custom integrations queue separately.

A second mistake is treating **protocol acronyms as interchangeable**. [ACP](/blog/what-is-agentic-commerce-protocol) (OpenAI/Stripe) optimizes for discovery plus delegated payment on ChatGPT and Meta embedded checkout. [UCP](/blog/what-is-universal-commerce-protocol) (Google/Shopify) targets full-journey native checkout on Gemini, AI Mode, and Copilot. Implementing one does not satisfy the other. Shopify merchants are the clearest dual-protocol case; WooCommerce merchants may have Google feed coverage without ACP until Stripe's extension ships.

Third, **confusing enterprise ops agents with consumer storefront agents**. 91APP AgentOne automates merchant-side tasks—closer to an internal copilot than a buyer-facing "Buy in ChatGPT" surface. Sales decks that list 91APP alongside Shopify under "merchant stack" blur this line. Ask: does this product put my catalog in front of a buyer's AI assistant, or does it help my staff run the business?

Fourth, **ignoring feed and inventory SLAs**. OpenAI's March 2026 pivot toward merchant-owned checkout cited catalog accuracy, tax, and stock sync—not lack of buyer demand. Platforms with live discovery (Shopify Catalog, OpenAI JSONL feeds) still drop ineligible SKUs without loud errors. Agentic commerce is an operational discipline, not a marketing toggle.

Fifth, **bounding retail vs API sellers incorrectly**. SaaS and API products billing developers belong under [MPP / x402](/blog/what-is-machine-payments-protocol)—machine payments for agent-to-service spend—not retail CMS enablement. Listing your API on a ChatGPT retail feed is the wrong integration model.

---

## What This List Does Not Cover

This article maps **CMS and commerce platforms**—the software where merchants manage catalog, cart, and storefront policy. Two adjacent layers have their own reference tables and should not be inferred from the rows above.

**Payment processors and acquirers.** A WooCommerce store might process cards through Stripe but still lack WooCommerce's Stripe agentic extension; conversely, live Stripe ACS does not auto-enroll Shopify Agentic Storefronts. See our [processor-by-processor breakdown of Stripe ACS, Adyen Agentic, Nuvei, and Antom](/blog/agentic-commerce-merchant-stack-psp) for regions, waitlists, and product names.

**Buyer-facing AI surfaces.** ChatGPT, Gemini, Copilot, and messaging apps each impose different protocol and regional requirements. Our [channel-by-channel live status list](/blog/agentic-commerce-agent-channels) covers those surfaces—not repeated here to avoid stale duplication.

**Identity and card-network layers.** Visa Intelligent Commerce, Trusted Agent Protocol (TAP), and Mastercard Agent Pay sit beneath PSP tokenization for many in-agent payment flows. Merchants rarely integrate these directly from a CMS admin panel; PSPs and platforms abstract them.

**Clink and third-party orchestration.** Payment orchestration and agentic payment infrastructure providers may connect multiple PSPs to agent protocols—that is a routing layer, not a CMS category. No inference should be drawn that any orchestration vendor natively enables every platform in the table unless publicly documented per platform.

When scoping a project, sequence the checklist: (1) target [AI shopping surfaces from our live-status list](/blog/agentic-commerce-agent-channels), (2) confirm your platform row in the table above, (3) [enroll a PSP agentic product such as Stripe ACS or Adyen Agentic](/blog/agentic-commerce-merchant-stack-psp), (4) feed/inventory ops. Skipping step 2 and jumping to PSP signup is how teams discover—months later—that catalog never syndicated.

---

## Conclusion

**Agentic commerce supported platforms CMS** is not a yes/no property of your e-commerce vendor—it is a matrix of **enablement path**, **protocol**, and **verified status** that changes by platform and by quarter. Shopify remains the only major SaaS platform with live, multi-channel Agentic Storefronts spanning UCP and ACP as of September 2026. Adobe Commerce, Wix, and WooCommerce occupy partial or rolling-out territory worth tracking if you are already on those stacks. 91APP AgentOne and SHOPLINE illustrate APAC deck entries that do **not** map one-to-one to global consumer agent checkout—AgentOne is enterprise operations; SHOPLINE lacks public agentic documentation.

Before committing engineering budget, confirm your platform row matches the [AI shopping surfaces you are targeting](/blog/agentic-commerce-agent-channels), then verify your [PSP exposes a named agentic product—not just card processing](/blog/agentic-commerce-merchant-stack-psp). Custom and headless merchants can participate today via UCP profiles and OpenAI feeds, but ownership of feed freshness and checkout APIs stays in-house. Retail agentic commerce rewards operational rigor more than protocol logos on a slide.

For how the platform, channel, and PSP layers fit together, see the [agent payments hub](/blog/agent-payments).

Teams building agent payment guardrails alongside commerce enablement can explore [Clink's agentic payment infrastructure](https://clinkbill.com/agentic-payment) (Early Access as of mid-2026)—a routing and policy layer adjacent to, not a replacement for, platform-native Agentic Storefronts or ACS enrollment.

---

## FAQ

### Which CMS platforms fully support agentic commerce today?

**Shopify** is the only major SaaS commerce platform with **live**, documented, multi-channel agentic storefront enablement (Agentic Storefronts) as of September 2026. **Wix** and **WooCommerce** offer partial paths; **Adobe Commerce** is committed and rolling out but lacks a native GA UCP module mid-year. **SHOPLINE** has no official public enablement found.

### Does using Stripe mean my store is agent-ready?

**No.** Standard Stripe card processing is separate from **Stripe Agentic Commerce Suite (ACS)**, which provides ACP endpoints, delegated checkout, and catalog tooling for agent channels. You also need CMS-level enrollment (e.g., Shopify Agentic, Wix ACP signatory) or a custom UCP profile and feeds.

### What is the difference between ACP and UCP for platform choice?

**ACP** (OpenAI/Stripe) emphasizes product discovery and delegated payment—primary surfaces include ChatGPT and Meta embedded checkout. **UCP** (Google/Shopify) targets native checkout on Google AI Mode, Gemini, and Microsoft Copilot. Platforms like Shopify support both; others may support only one path via extensions or feeds.

### Is 91APP AgentOne the same as Shopify Agentic Storefronts?

**No.** **91APP AgentOne** is an **enterprise operations agent** for retail and OMO workflows inside the 91APP ecosystem—it is not a consumer-facing ACP/UCP storefront syndicating catalog to ChatGPT or Gemini. Treat it as a different product category from agentic storefront enablement.

### Can SHOPLINE merchants sell through ChatGPT or Google AI Mode natively?

**Not via documented SHOPLINE enablement.** Public SHOPLINE materials located in September 2026 do not announce ACP, UCP, or agentic commerce products. Merchants would need custom feeds, a UCP profile, and PSP agentic integration—or migrate to a platform with live agentic channels.

### How do custom or headless stores enable agentic commerce?

Publish a valid **`/.well-known/ucp`** profile, implement checkout REST or **MCP** tools, maintain Google Merchant Center or [OpenAI product feeds](https://developers.openai.com/commerce/specs/file-upload/products), and connect a mandated payment handler—often through **Stripe ACS** waitlist or custom ACP endpoints. Engineering owns feed freshness and inventory accuracy; there is no platform sales-channel toggle.
