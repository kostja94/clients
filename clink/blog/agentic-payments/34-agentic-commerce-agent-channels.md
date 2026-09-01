---
title: "Agentic Commerce Agent Channels — Supported List (2026 Reference)"
description: "A verified 2026 reference of agentic commerce agent channels—ChatGPT, Copilot, Gemini, messaging apps, and enterprise agents with live status and protocols."
slug: "agentic-commerce-agent-channels"
date: "2026-09-13"
updated: "2026-09-01"
category: "Agentic Payments"
secondaryCategory: "Research"
author: "Clink Team"
readingMinutes: 14
---

## TL;DR

- **Agent channels in agentic commerce** are the AI surfaces where a buyer—or a buyer's delegated agent—starts a retail journey: product discovery, cart assembly, checkout, and payment authorization. They sit above open protocols ([ACP](/blog/what-is-agentic-commerce-protocol), [UCP](/blog/what-is-universal-commerce-protocol), [AP2](/blog/what-is-ap2-agent-payments-protocol)) and merchant infrastructure—not inside your CMS.
- As of September 2026, **live retail agent channels** with Tier 0 documentation cluster around **ChatGPT (U.S. discovery)**, **Microsoft Copilot Checkout**, **Google AI Mode / Gemini native checkout**, and **Meta Facebook ads with Stripe ACS**—all protocol-backed paths distinct from generic chat assistants.
- **Messaging super-apps** (WhatsApp, LINE, Telegram, WeChat) support commerce through proprietary bot APIs or closed wallets; none publish official [ACP](/blog/what-is-agentic-commerce-protocol) or [UCP](/blog/what-is-universal-commerce-protocol) integrations as of this writing.
- **Claude has no consumer shopping channel**; **Manus is a merchant-side builder**, not a buyer surface. **Enterprise and custom agents** via MCP and `/.well-known/ucp` profiles are the fastest path for B2B and headless merchants.
- This list covers **retail agentic commerce only**—not [machine/API micro-payments](/blog/what-is-machine-payments-protocol) (MPP/x402). Status claims trace to official sources in the reference table below. Merchant-side enablement—[which storefront platforms expose Agentic Storefronts or UCP profiles](/blog/agentic-commerce-merchant-stack-cms) and [which PSPs ship delegated checkout products like Stripe ACS](/blog/agentic-commerce-merchant-stack-psp)—is documented in separate references scoped to those layers.

---

## What Is an Agent Channel in Agentic Commerce?

An **agent channel** is the buyer-facing AI interface where agentic commerce actually happens. When industry analysts talk about "selling in ChatGPT" or "Copilot Checkout," they mean a specific channel operator has opened (or closed) a path for delegated shopping—not that every LLM chat window is automatically a storefront.

In the retail stack, channels connect to **open protocols** and **payment rails** on the merchant side. [ACP (Agentic Commerce Protocol)](/blog/what-is-agentic-commerce-protocol), co-developed by OpenAI and Stripe, emphasizes product feeds, delegated checkout, and Stripe Shared Payment Tokens for ChatGPT-era flows. [UCP (Universal Commerce Protocol)](/blog/what-is-universal-commerce-protocol), co-developed by Google and Shopify, targets full-journey checkout on Gemini, Copilot, and merchant-published profiles. [AP2](/blog/what-is-ap2-agent-payments-protocol) adds payment mandates where Google surfaces require them. Visa Intelligent Commerce and Trusted Agent Protocol (TAP) address card-network identity and agent tokens—a layer adjacent to, not interchangeable with, any single channel UI.

The distinction matters for roadmap sequencing. A **channel operator** (OpenAI, Microsoft, Google, Meta, Tencent) decides which merchants appear, which protocols are honored, and which regions qualify. A **merchant** implements catalog feeds, checkout APIs, and payment handlers so those operators can call them safely. A **PSP** such as Stripe ACS or Adyen Agentic translates between protocol messages and your existing payment stack. None of these roles collapses into the others: Shopify Agentic Storefronts can make you discoverable on ChatGPT while a separate UCP profile unlocks Gemini—two channel paths, two integration checklists. Platform and PSP rows are documented separately in our [commerce platform enablement list](/blog/agentic-commerce-merchant-stack-cms) and [PSP agentic product list](/blog/agentic-commerce-merchant-stack-psp).

Confusing a **channel** with a **merchant tool** is the most common planning mistake in 2026 decks. Manus builds Shopify sites; Claude runs enterprise workflows; neither is a consumer checkout surface today. Likewise, connecting Stripe alone does not make you "agent-ready"—you still need ACS/ACP endpoints, a UCP profile, or a PSP translation layer documented for agent surfaces. Teams that treat "we use Stripe" as sufficient often discover—during Copilot or Gemini waitlist review—that delegated checkout and handler manifests were never implemented. The [agent payments hub](/blog/agent-payments) maps how these pieces fit together for engineering and RevOps teams evaluating 2026 roadmaps.

---

## How to Read This List

This reference answers one question: **where can a buyer agent realistically complete (or hand off) a retail transaction in September 2026?** Each row reflects **public, operator-published status**—not roadmap slides, partner press releases without Tier 0 corroboration, or SEO aggregators.

**Status values** use a fixed vocabulary:

| Status | Meaning |
|--------|---------|
| **Live** | Operator documents a production or broad rollout path merchants can target now |
| **Beta** | Documented limited/partner program; not default GA for all merchants |
| **Waitlist** | Official enrollment required before integration |
| **Messaging-only** | Commerce via proprietary bot/wallet APIs; no ACP/UCP agent checkout |
| **Not supported** | No public consumer agentic commerce product (may still support MCP for custom builds) |
| **Deprioritized** | Formerly promoted path explicitly de-emphasized in favor of another model |

**Protocol** lists the primary open standard where Tier 0 docs exist; "Proprietary" means closed-platform APIs (WeChat Pay, Telegram Bot Payments, etc.). **Region** reflects documented geographic limits as of verification—not inferred global availability.

**Last verified: September 2026.** Operator policies change quickly; confirm feed requirements, waitlists, and payment handler mandates on the linked Source before committing engineering sprints. We exclude [MPP/x402 machine payments](/blog/what-is-machine-payments-protocol) from this table—they serve API and agent-wallet micro-transactions, not catalog retail checkout on consumer AI surfaces.

When comparing channels for a go-to-market memo, use **buyer journey** rather than logo count. **Discovery-in-AI, checkout-on-merchant** describes ChatGPT after March 2026: the agent recommends and compares, but payment often completes on a merchant domain or inside a ChatGPT App with account linking. **In-agent retail checkout** describes Copilot Checkout and Gemini native flows where the buyer finishes payment inside the AI surface subject to UCP/AP2 rules. **Embedded ads/social checkout** covers Meta Facebook Buy now units that never touch a messaging thread. **Enterprise/custom** covers Dynamics 365 Commerce MCP servers and headless merchants publishing UCP profiles—buyer agents may be internal procurement bots, not consumer chat brands. Mapping your SKUs to journey type prevents the classic error of staffing a WhatsApp bot project when your U.S. revenue goal actually requires Merchant Center and UCP REST checkout.

---

## Agent Channels Reference Table

| Channel | Operator | Status | Protocol | Region | Source |
|---------|----------|--------|----------|--------|--------|
| **ChatGPT** | OpenAI | **Live** (U.S. shopping discovery); **Deprioritized** (standalone Instant Checkout); **Beta** (embedded payment sheet for select marketplace apps) | ACP; MCP / `requestCheckout`; Stripe SPT | Shopping discovery **U.S.** live; self-serve feed expansion later 2026 | [OpenAI discovery](https://openai.com/index/powering-product-discovery-in-chatgpt/) · [Checkout API](https://developers.openai.com/plugins/build/monetization) · [TechCrunch pivot (Mar 2026)](https://techcrunch.com/2026/03/24/openais-plans-to-make-chatgpt-more-like-amazon-arent-going-so-well/) |
| **Microsoft Copilot** | Microsoft | **Live** | UCP (Microsoft also documents ACP onboarding for merchants) | Copilot Checkout **U.S.**; requires UCP-ready Merchant Center feed | [Microsoft Agentic Commerce](https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce) |
| **Google AI Mode / Gemini** | Google | **Live** (selective U.S. retailer rollout) | UCP; AP2; Google Pay handler | **U.S.** native checkout; waitlist for Merchant Center + `/.well-known/ucp` | [Google agentic commerce blog](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/) · [UCP FAQ](https://developers.google.com/merchant/ucp/faq) |
| **Meta Facebook (ads)** | Meta + Stripe | **Live** | ACP via Stripe ACS | U.S. ad native checkout (e.g., Fanatics, Quince) | [Stripe × Meta checkout](https://stripe.com/newsroom/news/checkout-for-facebook) |
| **Claude** | Anthropic | **Not supported** (no public consumer shopping checkout) | MCP for enterprise custom agents only—not a Claude consumer commerce surface | Global Claude product; no retail agent channel | [Project Vend research](https://www.anthropic.com/research/project-vend-1) · [Managed Agents](https://www.anthropic.com/engineering/managed-agents) |
| **Manus** | Manus AI | **Not supported** as buyer channel (merchant-side site builder) | Proprietary Shopify connector; checkout delegated to Shopify/Stripe | Global users; commerce is seller tooling | [Manus × Shopify](https://manus.im/blog/manus-shopify-connector) · [Payments docs](https://manus.im/docs/website-builder/payments) |
| **WhatsApp** | Meta | **Messaging-only** | WhatsApp Business Cloud API; Meta Business Agent architecture—**no** official UCP/ACP docs | Global; Meta AI assistant is not retail checkout | [Meta AI on WhatsApp](https://ai.meta.com/learn/ai-basics/how-to-use-meta-ai-on-whatsapp/) · [Business Agent architecture](https://developers.meta.com/resources/videos/architecture-meta-business-agent-whatsapp/) |
| **LINE** | LINE Plus | **Messaging-only** | Proprietary ActEngine (merchant support/sales agents) | Asia (Thailand, Japan, etc.) | [LINE Plus ActEngine](https://ecommercenews.asia/story/line-plus-unveils-actengine-ai-for-merchant-support) |
| **Telegram** | Telegram | **Live** (Bot Payments for physical goods); **Messaging-only** relative to ACP/UCP | Proprietary Bot Payments API + PSP integrations | Global | [Telegram Bot Payments](https://core.telegram.org/bots/payments) |
| **WeChat** | Tencent | **Live** (China agent + WeChat Pay loop) | Proprietary WeChat ecosystem + WeChat Pay | **Mainland China** | [Caixin WorkBuddy × WeChat Pay (Jun 2026)](https://www.caixinglobal.com/2026-06-17/tencent-lets-ai-agent-make-purchases-through-wechat-pay-102455141.html) |
| **Enterprise & custom agents** | Merchants / ISVs | **Live / Beta** (deployment-dependent) | UCP (`/.well-known/ucp`); MCP; ACP (if OpenAI-integrated); AP2 mandates; Visa TAP for agent identity | Varies by merchant stack | [Dynamics 365 Commerce MCP](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/06/29/dynamics-365-commerce-introduces-agentic-capabilities-with-model-context-protocol-mcp/) · [UCP profile guide](https://developers.google.com/merchant/ucp/guides/overview/ucp-profile) · [Visa TAP](https://developer.visa.com/use-cases/trusted-agent-protocol) |

For ChatGPT-specific merchant onboarding—feeds, Apps, and the post-March 2026 discovery-first model—see our [ChatGPT merchant setup guide](/blog/how-to-sell-on-chatgpt).

**Enterprise & custom agents** deserve explicit planning even when they do not appear on consumer marketing sites. Microsoft Dynamics 365 Commerce MCP, Adobe Commerce MCP servers, and self-hosted UCP profiles let buyers interact through **your** branded agent or procurement copilot while still speaking UCP or MCP on the wire. Status is inherently **Live / Beta** at the deployment level: the channel is only as real as your published profile, REST checkout, and payment handler coverage.

---

## Channel Categories Explained (ACP vs UCP vs Proprietary Messaging)

Retail agent channels in 2026 fall into three buckets that behave differently in procurement, engineering, and compliance reviews.

**ACP-aligned surfaces** treat OpenAI and Stripe as the reference stack. ChatGPT shopping discovery in the United States, Meta Facebook native checkout through Stripe Agentic Commerce Suite (ACS), and delegated payment flows documented on [agenticcommerce.dev](https://www.agenticcommerce.dev/docs) share feed semantics, Shared Payment Token (SPT) patterns, and a deliberate shift—after [OpenAI's March 2026 pivot](https://openai.com/index/powering-product-discovery-in-chatgpt/)—toward **merchant-owned checkout** rather than ChatGPT-as-marketplace. If your GTM deck says "ACP," assume Stripe ACS or an approved delegate partner is in scope, and assume discovery may outpace in-chat payment sheet availability.

**UCP-aligned surfaces** prioritize negotiated capabilities between agents and merchant profiles. Google AI Mode and Gemini native checkout, Microsoft Copilot Checkout (Embedded Checkout Protocol path), and any merchant publishing `/.well-known/ucp` participate here. UCP's strength is **multi-surface checkout** with handler choice—Google Pay, Shop Pay, regional PSPs—without rewriting integrations per agent brand. Shopify Agentic Storefronts often expose both UCP and ACP depending on buyer surface, which is why "Shopify enabled" alone is not a single-protocol answer.

**Proprietary messaging commerce** remains enormous in user minutes but **orthogonal to ACP/UCP**. Telegram Bot Payments, WeChat WorkBuddy with WeChat Pay, LINE ActEngine, and WhatsApp Business Agent flows run on platform APIs and local wallets. They can drive GMV and support agent-like automation, yet they do not appear in Google's UCP retailer lists or OpenAI's ACP feed documentation. Teams planning "one protocol to rule messaging" should budget separate integrations—or route messaging leads to the web checkout your UCP/ACP stack already serves.

Hybrid patterns are already common in production pilots. A shopper discovers on ChatGPT (ACP feed), clicks through to a Shopify checkout (merchant-owned), and pays with a wallet tokenized for future delegated flows—that is still **agentic commerce**, but the **channel contribution** is discovery, not payment sheet custody. Conversely, a Copilot session may complete the entire cart without leaving Microsoft's embedded checkout UI, which makes **UCP handler coverage** (Google Pay, Shop Pay, or your PSP's published handler) a gating item on day one. Document which of your 2026 targets require **full in-agent settlement** versus **qualified handoff**; the reference table's Status column is only meaningful when paired with that journey decision.

---

## Channels Often Confused With Buyer Surfaces (Manus, Claude)

Two names appear on almost every agentic commerce slide—and both mislead if labeled "buyer channels."

**Claude (Anthropic)** ships powerful agent tooling for enterprises and documents internal commerce experiments such as [Project Vend](https://www.anthropic.com/research/project-vend-1). None of that constitutes a **public consumer shopping lane** inside claude.ai comparable to ChatGPT discovery or Gemini checkout. Anthropic's [managed agents engineering](https://www.anthropic.com/engineering/managed-agents) guidance targets builders wiring MCP tools to **their own** systems. For retail, Claude belongs in the "custom agent" row of the table—only if **you** publish commerce endpoints—not as a distribution channel you list in a marketplace admin console.

**Manus** is explicitly **merchant-side**: a Shopify connector and website builder where checkout completes on Shopify/Stripe rails Manus does not custody. [Manus documentation](https://manus.im/docs/website-builder/payments) describes claimable Stripe sandboxes and delegated storefront creation, not a Manus-owned buyer wallet or ACP feed endpoint. Decks that pair "Manus" with "ChatGPT" as parallel buyer channels confuse **site generation** with **demand aggregation**. Manus may help you become merchant-ready; it is not where shoppers open an agent to pay you.

Procurement teams should ask channel vendors one litmus question: **does your operator publish a merchant integration guide that names ACP, UCP, or an equivalent checkout API?** Anthropic and Manus fail that test for consumer retail today. Perplexity and other AI search products sometimes appear on industry slides but lacked consistent Tier 0 commerce documentation in our September 2026 verification pass—omitted here until operators publish stable merchant programs. When in doubt, default to the reference table's Source links rather than conference slide logos.

---

## What Changed in 2026 (OpenAI March Pivot, Copilot/Gemini UCP Rollout)

Three shifts between January and September 2026 explain why this list looks different from late-2025 roadmaps.

**OpenAI's March 2026 pivot** downgraded standalone Instant Checkout as the default ChatGPT commerce story. Official posts emphasize **product discovery**, ChatGPT Apps with deep merchant linking (e.g., Walmart account linking), and checkout that returns buyers to **merchant-controlled** payment surfaces—corroborated by [TechCrunch reporting](https://techcrunch.com/2026/03/24/openais-plans-to-make-chatgpt-more-like-amazon-arent-going-so-well/) on strategic friction with a fully in-chat marketplace. ACP did not disappear; the **center of gravity moved** from "ChatGPT is the cart" to "ChatGPT is the research and referral layer." Merchants still need ACP feeds and Stripe ACS for discovery eligibility, but should not assume universal in-agent payment sheets.

**Microsoft Copilot Checkout went live in January 2026** with explicit **UCP requirements**—Merchant Center feeds, UCP profiles, and Embedded Checkout Protocol support—documented on [Microsoft's agentic commerce hub](https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce). For many Adobe and Dynamics retailers, Copilot became the first **non-Google** UCP buyer surface worth prioritizing alongside Gemini.

**Google's UCP native checkout rollout on AI Mode and Gemini** accelerated through 2026 with [AP2 payment mandates](https://developers.google.com/merchant/ucp/faq) for eligible U.S. retailers. Selective waitlisting remained in effect mid-year: native checkout is **Live** for named brands, **Waitlist** for the long tail still implementing REST checkout and `/.well-known/ucp`. Shopify's co-founder role in UCP means Shopify merchants often inherit Copilot and Google paths faster than custom headless stacks—another reason channel lists must be separated from CMS enablement lists.

Asia-Pacific operators followed a parallel but **protocol-split** path. Tencent's WeChat Pay integration with WorkBuddy agents (reported [June 2026](https://www.caixinglobal.com/2026-06-17/tencent-lets-ai-agent-make-purchases-through-wechat-pay-102455141.html)) demonstrates live **closed-loop** agent purchasing inside a super-app—valuable for China GTM, irrelevant for UCP Merchant Center enrollment in the U.S. LINE ActEngine and WhatsApp Business Agent content skew toward **merchant automation** (support, lead qualification) rather than open-catalog checkout. Decks that flatten "APAC messaging" into a single checkbox hide the integration cost: none of those platforms shipped the same `/.well-known/ucp` discovery contract Google documents for Gemini.

Visa Intelligent Commerce and TAP expanded the **identity and token** layer (early partners include Stripe, Adyen, Shopify, Checkout.com, Nuvei per [Visa's TAP announcement](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html)). That infrastructure supports multiple channels; it does not replace reading each operator's commerce docs. Third-party payment enablers may advertise agent readiness—always cross-check against operator Tier 0 lists before treating any vendor claim as channel access. Payment infrastructure vendors—including Early Access programs such as [Clink for Claw](https://clinkbill.com/agentic-payment) for agent authorization orchestration—sit downstream of channel choice, not upstream of it.

---

## What This List Does Not Cover

This article maps **buyer-facing agent channels**—where a shopper or buyer-agent starts a retail journey. Merchant-side rows live elsewhere; do not infer platform or PSP status from the channel table above.

**Commerce platforms and storefronts.** Whether Shopify Agentic Storefronts is Live, Adobe Commerce is rolling out UCP, or SHOPLINE has no public path—all of that is in our [CMS and commerce platform enablement reference](/blog/agentic-commerce-merchant-stack-cms).

**Payment processors.** Whether Stripe ACS is Live in your region, Adyen Agentic is enterprise-only, or Worldpay documents ACP delegate APIs—that breakdown is in our [PSP agentic product reference](/blog/agentic-commerce-merchant-stack-psp). A Live ChatGPT row does not mean your acquirer enrolled ACS.

**Machine and API payments.** SaaS API billing and agent-wallet micro-transactions belong under [MPP and x402](/blog/what-is-machine-payments-protocol)—not consumer AI shopping surfaces.

**Operational setup.** Channel status tells you *where* to sell, not *how* to turn feeds on. After you pick a channel, follow our [ChatGPT merchant setup guide](/blog/how-to-sell-on-chatgpt) for syndication, OAI-SearchBot, and Shopify Agentic toggles.

When scoping work, sequence: (1) channels from this table, (2) [storefront enablement on your CMS](/blog/agentic-commerce-merchant-stack-cms), (3) [PSP agentic enrollment](/blog/agentic-commerce-merchant-stack-psp), (4) feed and inventory ops.

---

## Conclusion

**Agentic commerce agent channels** are not interchangeable chat apps—they are operator-specific buyer surfaces with different protocol contracts, regions, and 2026 status lines. For U.S. retail with open standards, prioritize evidence-backed paths: **ChatGPT discovery (ACP)**, **Copilot Checkout (UCP)**, **Gemini / AI Mode (UCP + AP2)**, and **Meta Facebook ads (ACP via Stripe ACS)**—then layer messaging platforms only where your buyers already live, accepting proprietary stacks.

Build your merchant stack **from channel requirements backward**: feeds and ACS for ACP surfaces, UCP profiles and handlers for Google/Microsoft, and MCP or custom REST for enterprise agents. Revisit this table quarterly; OpenAI already pivoted once in 2026. If you are sequencing Q4 work, a pragmatic default for U.S. DTC brands is **parallel ACP discovery + UCP checkout**: ChatGPT and Meta ads on the ACP/Stripe ACS rail, Copilot and Gemini on UCP—accepting that handler manifests, tax display rules, and fraud signals differ per operator even when the same PSP backs both.

For protocol definitions, see [ACP](/blog/what-is-agentic-commerce-protocol) and [UCP](/blog/what-is-universal-commerce-protocol) on the [agent payments hub](/blog/agent-payments). Once your channel shortlist is set, confirm your [storefront platform supports the right syndication path](/blog/agentic-commerce-merchant-stack-cms) and your [PSP exposes the matching agentic product](/blog/agentic-commerce-merchant-stack-psp) before filing engineering estimates.

Teams evaluating payment orchestration for multi-channel agent checkout can [contact Clink](https://clinkbill.com/contact) to discuss Early Access agent payment infrastructure—after channel and protocol scope is fixed.

---

## FAQ

### What are agentic commerce agent channels?

Agentic commerce agent channels are the AI interfaces—ChatGPT, Copilot, Gemini, messaging bots, or enterprise agents—where buyers or buyer-delegated agents discover products and initiate checkout. They connect to merchant systems through protocols like ACP and UCP, distinct from payment-only layers such as AP2 or card-network agent identity (Visa TAP).

### Which agent channels support live retail checkout in the U.S. in 2026?

Tier 0 documentation supports **Live** paths on **ChatGPT** (shopping discovery and delegated checkout models), **Microsoft Copilot Checkout** (UCP), **Google AI Mode / Gemini** (UCP native checkout for eligible retailers), and **Meta Facebook ads** (ACP via Stripe ACS). Availability still depends on merchant feed approval, PSP enablement, and operator waitlists.

### Is Claude or Manus a buyer agent channel for agentic commerce?

No. **Claude** has no public consumer shopping checkout product as of September 2026. **Manus** is a merchant-side Shopify/site builder that delegates payment to Shopify and Stripe—it is not a buyer-facing agent commerce surface. Both names belong in planning docs only with that distinction.

### What is the difference between ACP and UCP agent channels?

**ACP** channels (ChatGPT discovery, Meta Facebook via Stripe ACS) follow the OpenAI/Stripe Agentic Commerce Protocol—feeds, delegated payment, SPT. **UCP** channels (Gemini, Copilot, merchant `/.well-known/ucp` profiles) follow Google's Universal Commerce Protocol—capability negotiation, multiple payment handlers, full-journey checkout. Many merchants need **both** for 2026 U.S. coverage.

### Do WhatsApp, Telegram, LINE, or WeChat use ACP or UCP?

Not officially. **Telegram** offers live Bot Payments on proprietary APIs. **WeChat** supports agent-assisted purchases via WeChat Pay in China. **WhatsApp** and **LINE** document business-agent and messaging commerce architectures without UCP/ACP agent checkout specs. Treat them as **messaging-only** relative to open agentic commerce protocols unless operators publish new Tier 0 integrations.

### How is this list different from machine payments (MPP/x402)?

This list covers **retail catalog checkout on consumer AI surfaces**. [Machine Payments Protocol (MPP)](/blog/what-is-machine-payments-protocol) and x402 address **API and agent-wallet micro-transactions** between services—not Gemini buying sneakers or Copilot completing a Merchant Center cart. Stack them separately in architecture reviews.
