---
title: "How to Sell on ChatGPT in 2026 — Merchant Setup Guide"
description: "Sell on ChatGPT via Shopify Agentic Storefronts, Etsy auto-sync, or an OpenAI product feed—discovery in chat, checkout on your site, and you stay merchant of record."
slug: "how-to-sell-on-chatgpt"
date: "2026-09-12"
updated: "2026-08-24"
category: "Agentic Payments"
secondaryCategory: "HowTo"
author: "Clink Team"
readingMinutes: 12
---

## TL;DR

- **To sell on ChatGPT in 2026**, merchants optimize for **product discovery in chat** and **checkout on merchant-owned sites or apps**—OpenAI [deprioritized standalone in-chat Instant Checkout](https://chatgpt.com/merchants/) in **March 2026** after catalog, tax, and inventory complexity stalled rollout.
- **Shopify merchants**: check **Settings → Sales channels → Agentic**—eligible U.S.-buyer stores are often **already syndicated** to ChatGPT via Shopify Catalog; ChatGPT sends buyers to your store checkout (in-app browser), not a mandatory in-chat cart.
- **Etsy sellers**: catalogs are **auto-integrated**—no separate application at chatgpt.com/merchants.
- **Everyone else**: apply at [chatgpt.com/merchants](https://chatgpt.com/merchants/), build an [OpenAI product feed](https://developers.openai.com/commerce/specs/file-upload/products), allow **`OAI-SearchBot`** in robots.txt, and refresh inventory at least daily.
- You remain **merchant of record (MoR)**—refunds, chargebacks, and PSP fees stay on your stack; for MoR vs PSP framing see [MoR vs PSP](/blog/mor-vs-psp). Retail protocols ([ACP](/blog/what-is-agentic-commerce-protocol), [UCP](/blog/what-is-universal-commerce-protocol)) sit under the broader [agent payments](/blog/agent-payments) stack.

---

## What "Sell on ChatGPT" Means in 2026

Most merchants search **"how to sell on ChatGPT"** expecting a new marketplace signup. The actual workflow is closer to **AI search distribution**: your structured catalog reaches ChatGPT shoppers; when they buy, they typically **complete payment where you already process cards**—Shopify checkout, your Stripe stack, or your app—not inside OpenAI's walled cart.

OpenAI's merchant FAQ (mid-2026) states explicitly that the company is **moving away from standalone Instant Checkout** and prioritizing **product discovery plus merchant-owned checkout**. Users discover and compare products in ChatGPT; purchases finish on **merchant websites or apps**. OpenAI also states there are **no fees for purchases made on your site or app** when buyers convert there after discovery.

That pivot matters for planning. The September 2025 launch narrative—"Buy it in ChatGPT" with Etsy live day one and a million-plus Shopify pipeline—shifted by March 2026 when industry reporting placed only roughly **12–30 Shopify merchants** live for in-chat checkout before OpenAI changed course. The **Agentic Commerce Protocol ([ACP](/blog/what-is-agentic-commerce-protocol))** did not sunset; **feed quality and syndication** became the durable merchant play.

Shopping is **U.S. buyer–focused** as of mid-2026, with OpenAI planning broader merchant self-serve and regions over time. Treat availability as **pilot-stage**, not guaranteed placement for every SKU on every query.

Beyond organic discovery, OpenAI describes additional surfaces merchants may evaluate over time: **ChatGPT Apps** (retailer-run experiences inside the assistant—Walmart cited as a launch example), **ChatGPT Ads** with product-feed campaigns (enterprise budgets), and deeper **ACP** checkout integrations for large approved retailers. Most SMB merchants should treat **feed + owned checkout** as phase one before committing engineering to a custom App.

---

## Pick Your Path in Thirty Seconds

| You are… | Fastest path | First action |
|----------|--------------|--------------|
| **Shopify** store selling to U.S. buyers | Agentic Storefronts + Catalog | Admin → **Settings → Sales channels → Agentic** |
| **Etsy** seller | Auto-integrated catalog | Improve listings; no OpenAI application |
| **Stripe retail** (headless, Wix, WooCommerce, BigCommerce) | [Agentic Commerce Suite](https://docs.stripe.com/agentic-commerce/for-sellers) waitlist | [Join waitlist](https://go.stripe.global/agentic-commerce-contact-sales) → Dashboard **Agentic commerce** |
| **Custom storefront** (Magento, DTC, non-Shopify) | OpenAI merchant feed | [chatgpt.com/merchants](https://chatgpt.com/merchants/) application → SFTP feed |
| **API / SaaS seller** (not retail SKUs) | Machine payments, not ChatGPT retail feeds | [MPP / x402](/blog/what-is-machine-payments-protocol)—different problem |

If you also want **Buy buttons inside Google AI Mode**, that is a separate **[UCP](/blog/what-is-universal-commerce-protocol)** track (Merchant Center + engineering waitlist)—not required to appear in ChatGPT discovery.

---

## Shopify Merchants: Agentic Storefronts

Shopify is the lowest-friction path for most DTC brands asking how to sell on ChatGPT. **Agentic Storefronts** syndicate eligible catalog data to AI channels—including ChatGPT, Microsoft Copilot, and (for select merchants) Google AI Mode and Gemini—through **Shopify Catalog**.

### Requirements (Shopify Help Center)

- Sell to **customers in the United States** (your store can be based outside the U.S.)
- Products **eligible for Shopify Catalog**
- **Shop Pay** active
- Completed **Terms of service**, **Privacy policy**, and **Return and refund policy**
- Agreement to **Agentic Storefronts Supplemental Terms of Service**

### Setup steps

1. In Shopify admin, go to **Settings → Sales channels → Agentic** (or **Sales channels → Agentic**).
2. Review **Allow Shopify to manage for me**—when on, Shopify enrolls channels and syndicates Catalog access; many eligible merchants were **auto-enrolled from late March 2026** and may not realize they are live.
3. Audit which **AI channels** are active and whether **direct checkout** is enabled per channel:
   - **ChatGPT**: discovery in chat; buyers typically checkout via **in-app browser on your Shopify store**—not a merchant toggle for in-chat-only mode.
   - **Copilot / Google AI Mode / Gemini**: you can choose **purchase directly in the AI channel** vs **redirect to your online store** per channel settings.
4. Fix **Catalog ineligible SKUs** silently excluded from AI surfaces—no error banner, just absence from results.
5. Optimize titles, descriptions, variants, GTINs, and **real-time inventory**—AI recommendations punish stale price or stock once.

**You do not need** a separate chatgpt.com/merchants application if you sell on Shopify—OpenAI's merchant page states Shopify catalogs are already integrated.

### Attribution

Add UTM parameters or monitor referrals from **chatgpt.com** in GA4 or Shopify Analytics so discovery traffic is measurable—not assumed.

---

## Etsy Sellers

OpenAI's merchant program states that if you **sell through Etsy**, your catalog is **already integrated** and **no additional setup or application is required**. Focus on listing quality, U.S. availability, accurate inventory, and policies—same fundamentals as any marketplace SEO, but the syndication layer is platform-handled.

Purchases complete through **Etsy's native checkout flow** after discovery in ChatGPT, consistent with the broader **merchant-owned checkout** direction.

---

## Non-Shopify Retail: OpenAI Product Feed

Merchants on WooCommerce, Magento, custom stacks, or DTC sites without Shopify/Etsy auto-sync must **apply** to share product data.

### Step 1 — Apply

Complete the form at **[chatgpt.com/merchants](https://chatgpt.com/merchants/)** with your merchant website and catalog context. If you have already applied, you are on the **waitlist** until OpenAI activates your account. OpenAI describes a **self-serve merchant platform later in 2026**; as of mid-2026, onboarding is **approval-gated**, not instant public upload.

### Step 2 — Allow AI crawling

Add to **robots.txt** (unless you block all bots):

```
User-agent: OAI-SearchBot
Allow: /
```

If **OAI-SearchBot** is blocked, products can remain invisible even with a perfect feed—crawl and feed are complementary discovery paths.

### Step 3 — Structured pages

Implement **JSON-LD Product** schema on product URLs with fields consistent with your feed (title, price, availability, images). ChatGPT uses structured data alongside feed ingestion; mismatches between page schema and feed erode trust.

### Step 4 — Build the feed

Follow OpenAI's [Product Feed Spec](https://developers.openai.com/commerce/specs/file-upload/products). Supported formats include **CSV, TSV, XML, and JSON**. Required flags include:

- **`is_eligible_search`** — whether the SKU can appear in ChatGPT search results
- **`is_eligible_checkout`** — whether in-chat purchase is allowed (requires `is_eligible_search=true`; most merchants post-pivot set checkout false and rely on site conversion)

Include identifiers (**GTIN, UPC, MPN** where applicable), pricing, availability, images, shipping regions, and seller policy URLs. For checkout-eligible rows, seller ToS and privacy URLs are mandatory.

### Step 5 — Deliver and refresh

After approval, OpenAI provides a **secure SFTP endpoint and credentials**—there is no public pull URL on your site. Overwrite the same filename on each update; OpenAI recommends **at least daily** full snapshots, with support for updates as often as **~15 minutes** for fast-moving catalogs.

### Step 6 — Checkout on your site

When a shopper converts, send them to **your existing checkout**—Stripe, Adyen, Shopify Buy Button on a subdomain, etc. OpenAI states **no platform fee on purchases completed on your site or app** (merchant FAQ, mid-2026). Your normal **PSP processing fees** still apply.

**Optional provider path:** OpenAI names **Salesforce and Stripe** as feed delivery examples; Stripe's **[Agentic Commerce Suite](https://stripe.com/blog/agentic-commerce-suite)** can syndicate catalogs to agents for merchants already on Stripe or platform partners (Wix, WooCommerce, BigCommerce, commercetools).

---

## Stripe Merchants: Agentic Commerce Suite

If your commerce stack runs on **Stripe** but not Shopify's one-click Agentic channel, the **Agentic Commerce Suite (ACS)** is Stripe's modular path to **discovery, checkout, and agentic payments** through a Dashboard workflow rather than hand-building all five [ACP](/blog/what-is-agentic-commerce-protocol) checkout endpoints on day one.

As of mid-2026, ACS is in **private preview**:

1. **[Join the waitlist](https://go.stripe.global/agentic-commerce-contact-sales)**
2. Activate Stripe payments, 2FA, and payout bank account
3. Open **[Agentic commerce](https://dashboard.stripe.com/agentic-commerce)** → create a **Stripe Profile** (terms, privacy, returns)
4. Upload a **catalog feed**; configure tax codes— incomplete tax config can **fail checkouts**
5. Select AI **agents** and **Request connection** (agents must accept)
6. Fulfill orders via your existing OMS; you remain **MoR**

**Custom / headless merchants** with engineering bandwidth can implement ACP checkout APIs directly and use ACS only for SPT confirmation hooks—see Stripe's [custom seller docs](https://docs.stripe.com/agentic-commerce/for-sellers/custom).

**WooCommerce note:** WooCommerce is **not** Shopify-simple. Native **[MCP](https://developer.woocommerce.com/docs/features/mcp/)** helps agents read catalog data; **Stripe for WooCommerce** plus ACS is the practical checkout path. Plan developer time—there is no single Admin toggle equivalent to Agentic Storefronts.

---

## Fees, MoR, and What Changed About the 4% Narrative

| Scenario | Platform fee (OpenAI / channel) | You still pay |
|----------|--------------------------------|---------------|
| Discovery → buyer checks out **on your website/app** | OpenAI: **no fee on those purchases** (merchant FAQ) | Your PSP processing |
| **Product feed** submission for discovery | No per-transaction feed fee stated on merchant page | Feed ops / engineering |
| Historic **Instant Checkout** inside ChatGPT (pre-pivot, limited merchants) | Industry reporting cited **~4%** OpenAI platform fee on completed in-chat orders (Shopify spokesperson, Jan 2026) plus processing | Largely **deprecated path** for most brands |

**Merchant of record does not change.** OpenAI is **not** MoR. You handle **refunds, chargebacks, tax remittance where applicable, and customer support** on your existing PSP relationship—same as your web store. Delegated payment tokens ([Shared Payment Tokens](/blog/what-is-agentic-commerce-protocol)) scope agent-initiated charges; they do not transfer legal seller obligations to OpenAI.

When **human web checkout** and **agent-surfaced orders** share one Stripe or multi-PSP stack, reconciliation and routing complexity rises—teams evaluating orchestration should read [smart payment routing](/blog/smart-routing) alongside this guide. Clink's human billing layer is separate from ChatGPT retail discovery; do not conflate **selling SKUs in ChatGPT** with **agents paying your API** ([MPP](/blog/what-is-machine-payments-protocol)).

---

## Week-One Checklist (Every Merchant)

1. **Confirm platform path**—Shopify Agentic, Etsy auto-sync, OpenAI feed, or Stripe ACS waitlist.
2. **Audit top 50 SKUs** for price, stock, images, and identifiers—AI surfaces amplify catalog errors publicly.
3. **Unblock OAI-SearchBot** if you rely on crawl + feed (non-Shopify).
4. **Verify policy URLs** resolve (ToS, privacy, returns)—required for feeds and Stripe Profile.
5. **Instrument referrals** from chatgpt.com and AI channels in analytics—tag campaigns if your team runs paid or owned media elsewhere.
6. **Align support and finance** on MoR, refund ownership, and that discovery traffic may not match last-click attribution models.

---

## Common Mistakes

**Assuming Instant Checkout is the default.** Post–March 2026, plan for **discovery + your checkout** unless you are on a platform channel that still offers embedded AI checkout (Copilot/Google toggles on Shopify).

**Ignoring silent Catalog exclusions.** Ineligible Shopify SKUs simply never appear—no admin error.

**Set-and-forget feeds.** Stale inventory causes oversells and damages brand trust in conversational recommendations harder than in traditional SERPs.

**Blocking OAI-SearchBot** while submitting feeds—dual-path discovery fails.

**Applying retail feed logic to API businesses.** SaaS and API monetization for agents belongs on **machine payment rails**, not chatgpt.com/merchants retail onboarding.

**Expecting guaranteed ranking.** Feed compliance enables eligibility; **which products surface for which queries** is platform-determined and competitive.

---

## Conclusion

Selling on ChatGPT in 2026 is a **distribution and catalog hygiene** project first and a **new checkout UI** project second. Shopify and Etsy merchants should **verify Agentic or auto-sync status** before building custom feeds. Everyone else should **apply early**, **allow OAI-SearchBot**, and treat **fresh structured catalog data** as the product. Checkout stays **on your turf**—you keep MoR, your PSP, and your customer relationship; OpenAI's pivot made that explicit.

For protocol depth behind the merchant surface, read [ACP](/blog/what-is-agentic-commerce-protocol) and the [agent payments](/blog/agent-payments) hub. For Google-native embedded checkout, see [UCP](/blog/what-is-universal-commerce-protocol)—a parallel track, not a substitute for ChatGPT discovery.

---

## FAQ

### Do I need to apply to sell on ChatGPT if I use Shopify?

No separate OpenAI application is required for **Shopify** (or **Etsy**) merchants—OpenAI states those catalogs are **already integrated**. You should still confirm **Agentic Storefronts** settings, Catalog eligibility, Shop Pay, and U.S. buyer requirements in Shopify admin.

### Can customers still buy inside ChatGPT without visiting my website?

OpenAI **deprioritized standalone Instant Checkout** for most merchants. The default model is **discovery in ChatGPT, purchase on your site or app**. Some **Shopify + Copilot/Google** configurations still support **direct checkout in the AI channel** when enabled; ChatGPT specifically routes to **merchant-owned checkout** via in-app browser for typical Shopify flows post-pivot.

### How much does it cost to sell on ChatGPT?

OpenAI's merchant FAQ states **no fees for purchases made on your site or app** after discovery. You pay normal **payment processing** on your checkout. A **~4% OpenAI platform fee** applied to historic **in-chat Instant Checkout** orders for some Shopify merchants (reported January 2026)—that path is **not** the mainstream 2026 model for most brands.

### What is a product feed and do I need one on Shopify?

A **product feed** is a structured file (or platform syndication) with titles, prices, availability, images, and eligibility flags OpenAI indexes for shopping results. **Shopify Catalog** syndicates on your behalf—you optimize products in admin rather than hand-uploading SFTP files. Non-Shopify merchants must build and deliver feeds after merchant approval.

### Who handles refunds and chargebacks?

**You do.** Merchants remain **merchant of record**; OpenAI does not assume seller-of-record obligations. Chargebacks and refunds flow through your existing PSP and policies—same as web orders.

### Is selling on ChatGPT the same as agent payments for my API?

No. **ChatGPT retail discovery** targets **physical and digital goods sold as SKUs** via feeds and commerce protocols. **Agents paying for API usage** uses **[MPP](/blog/what-is-machine-payments-protocol)**, **[x402](/blog/what-is-x402)**, or similar **HTTP 402 / machine payment** flows—covered in the [agent payments](/blog/agent-payments) stack, not this merchant feed guide.
