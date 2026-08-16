---
title: "Introducing Oginify: Open Graph Cards, Instantly"
description: "Introducing Oginify — the AI Open Graph image generator that turns any URL into four 1200×630 cards in 30 seconds. Free to try, pay per card."
slug: "introducing-oginify"
date: 2026-08-18
author: "Oginify"
category: "Product"
secondary_category: "Open Graph"
---

# Introducing Oginify: Open Graph Cards, Instantly

Oginify is live. Paste any URL — your homepage, a blog post, a product page — and the tool reads your page's brand, palette, and headline, then paints four 1200×630 Open Graph cards in about thirty seconds. One is on-brand; the other three are creative wildcards in editorial, terminal, and Swiss-minimal directions. Pick whichever wins on click-through, download the PNG, and paste the ready-made Open Graph and Twitter Card tags into your page head. No prompt, no template picker, no signup for the free quota. This post is the launch announcement: what we built, the problem it solves, and how to try it.

## TL;DR

- **Oginify is live** — paste a URL, get four 1200×630 Open Graph cards in about thirty seconds, one on-brand and three wildcards.
- It is **URL-first**: the URL is the entire input. No prompt, no template picker, no design work — the tool reads your page's title, palette, and logo.
- **Free to try**: up to six generations a day without an account or a card on file, watermark-free.
- **Pay per card, not per seat**: single $0.99, ten for $7.90, fifty for $29 — credits never expire, no subscription.
- **Open by default**: the same engine ships as social-cards-skills, an MIT-licensed Agent Skills spec you can run on your own infrastructure.

The short version: the Open Graph protocol gave every page the ability to declare a preview card, but the design work kept most of the web on grey placeholders and generic logo cards. Oginify removes the design step — the input is a URL, the output is a finished, brand-matched card with the meta tags already wired.

## 1. Oginify is live

Oginify is now available at [oginify.com](/) — no waitlist, no invite, no signup required to try the core flow. Paste a live page's URL, wait about thirty seconds, and get four 1200×630 PNG cards. The one that matches your brand best is yours to keep, and the other three are honest creative alternatives you can A/B against it in a feed.

It is built to be deliberately small: one URL in, four cards out, meta tags ready. There is no prompt box on the home page and no template gallery to pick from, because the page you paste already contains everything a good card needs — its title, its palette, its logo, its tone. Oginify reads those signals and paints from them.

The product is the managed version of the engine we open-sourced as [social-cards-skills](https://github.com/kostja94/social-cards-skills), an MIT-licensed Agent Skills spec. If you would rather run the same generation logic in your own pipeline — with your own model and assets — that path is free and available today. Oginify is the hosted version: paste a URL, get cards in seconds, no setup.

## 2. The problem we built it for

Every shared link is a small piece of your brand's surface area. When someone drops your URL into X, LinkedIn, Slack, Discord, WhatsApp, or iMessage, the platform fetches your `og:image` and renders a 1200×630 card next to your headline — the only one of the four required Open Graph properties that is a visual asset, per the [Open Graph protocol](https://ogp.me/). That card is often the first impression a new visitor gets of your product.

Yet most shared links still show one of three failures: a grey placeholder, a random hero image cropped at the wrong angle, or a static site-wide logo card that says the same thing for every page on the site. None of those look like a mistake the team noticed; they look like a decision the team never made. The root cause is not the protocol — it has been stable since 2010. It is the design work: a blog with forty posts needs forty distinct, on-brand cards, and that requires a designer, a template pipeline, or an afternoon of manual exports. Most teams cannot justify that cost, so they ship one generic card and move on.

2026 is the year that trade-off broke. AI generation crossed the quality bar where a brand-matched card can be produced in seconds rather than hours, and the models became good enough to read a page — its title, description, primary color, and logo — and paint from that read. The gap was a tool where the URL is the entire input. Oginify is that tool. If you are new to what these images are and why they matter, our [guide to what an Open Graph image is](/blog/what-is-open-graph-image) covers the protocol and the mechanics in depth.

## 3. What Oginify does

The mechanism is simple enough to describe in one sentence: paste a URL, wait about thirty seconds, get four cards. The honest version adds the details that matter. Oginify fetches your page's HTML and reads four signals — the title, the description, the primary color, and the logo — and uses those to paint one on-brand card plus three wildcards that push in different creative directions. It then hands you the full Open Graph and Twitter markup with width, height, and `og:image:alt` already wired the way the spec recommends. You host the PNG wherever you like; Oginify hosts nothing unless you ask it to.

Because every card is generated from the actual page it represents, per-page cards are finally practical. A founder can give every product page its own card in an afternoon; a content team can backfill old posts that shipped without any image. And because the tool reads the live page, the card stays correct when you rebrand: re-run the URL the same day and the crawler picks up the new colors from your HTML.

The pricing is a deliberate statement of the same philosophy. There is a free tier — up to six generations a day for signed-in accounts, no card on file — and beyond that you buy credits per card: $0.99 for a single, $7.90 for ten, $29 for fifty, with credits that never expire and no subscription, per the [Oginify pricing page](https://oginify.com/pricing). You pay for the cards you actually ship, not for a seat you might use. For a full ranked comparison of how this sits against the other approaches — prompt-driven models like Gemini and GPT Image, code-driven options like Vercel OG — our [best AI open graph image generators](/blog/best-ai-og-image-generators) guide is the honest map.

## 4. How to try it

The fastest way to judge the product is to paste your own homepage. Go to [oginify.com](/) and drop your root domain into the box — no account, no signup. In about thirty seconds you will have four brand-matched 1200×630 cards: one on-brand, three wildcards. Keep the one that wins, regenerate the ones that do not, and download the PNG at native resolution.

If you want to understand the protocol your card has to hit before you generate, the [Open Graph validator](/open-graph-validator) reads your live page the way a platform would and shows exactly what your links look like today. The [card gallery](/gallery) shows what a single URL produces across page types. And when you are ready to ship more than a handful of cards, the [bulk generator](/bulk-og-image-generator) and [Twitter Card generator](/twitter-card-generator) cover the adjacent jobs.

## 5. Open source & what's next

The mission behind the product is the same one as the Open Graph protocol itself, updated for 2026: make the web presentable when it travels. Where the protocol gave every page the ability to declare a preview, Oginify gives every page the default of a good one. That is why the engine ships open source — good defaults should be replicable, and if the hosted version ever stopped being the best way to get a card, the codebase is there for anyone to run.

The direction of the category is the direction of the product: the input to a good card is moving from templates and prompts toward the URL itself, because a live page already contains everything a card needs. Over the next year we expect per-page Open Graph images to become the default for sites that care about how they look when shared — the same way responsive design moved from a nice-to-have to an assumption. The open-source engine will keep tracking the hosted product, and the free tools around it will keep serving the adjacent jobs. If the web's default for a shared link becomes a card that looks designed, the mission is done.

## Conclusion

Oginify is live. It is a URL-first Open Graph image generator: paste any URL, get four brand-matched 1200×630 cards in about thirty seconds, and ship the ready-made meta tags. It is free to try, priced per card with no subscription, and open by default — the same engine is available as an MIT-licensed Agent Skills spec. The problem it solves is the one that left most of the web on grey placeholders: the design work between a page and a good preview card. Oginify removes that step. The input is the URL you already have; the card follows.

Paste your homepage into [Oginify](/) and judge it yourself — four on-brand card variants in about thirty seconds, no signup required for the free daily quota. Browse the [card gallery](/gallery) to see what a single URL produces across page types.

## Frequently asked questions

### Is Oginify really free?

For the core job, yes. You can generate up to six images per day without an account or a card on file, cards are watermark-free, and you can download them as native 1200×630 PNGs to host anywhere. Beyond the daily quota, you buy one-time credit packs — $0.99 for a single, $7.90 for ten, $29 for fifty — and credits never expire. There is no subscription you forget to cancel.

### How is Oginify different from a general AI image tool?

General-purpose tools like Gemini, GPT Image, and Midjourney paint a beautiful image from a prompt, but they do not read your page, enforce the 1200×630 size, or hand you the meta tags. Oginify reads your actual URL — real palette, real logo, real headline — and produces four brand-matched cards with the Open Graph and Twitter markup already wired. The input is your URL, not a description of what you want.

### What counts as one generation?

One generation is one URL that produces two card variants you can pick from, per the [Oginify pricing page](https://oginify.com/pricing) as of August 2026. Regenerating a card you do not like spends another credit. Switching templates or re-cropping is free — only clicking Generate or Regenerate spends a credit.

### Is Oginify open source?

The engine is. Oginify is the managed SaaS — paste a URL, get cards in seconds, no setup. The same engine ships as [social-cards-skills](https://github.com/kostja94/social-cards-skills), an MIT-licensed Agent Skills spec on GitHub, which you can run yourself in Cursor, Claude Code, or any Agent Skills runtime with your own model and assets. The hosted product is not open source; the engine behind it is.

### What are the correct Open Graph image dimensions in 2026?

1200×630 pixels at a 1.91:1 aspect ratio is the large-card size that X, LinkedIn, Slack, Discord, iMessage, and Facebook all render. Anything narrower than 600px on the long edge falls back to a small thumbnail. Oginify exports strict 1200×630 cards by default, so you do not need to think about the size — the card ships at the spec.

### Do I still need og:image if my page already has a hero image?

Yes. Hero images live inside your HTML and render for human visitors; social crawlers only render what you declare in `<meta property="og:image">`. Without the tag, X falls back to a plain link, LinkedIn shows a domain snippet, and Slack renders a grey placeholder — regardless of how good the hero looks on the actual page. The Open Graph image is the one preview your crawlers actually read, and it is independent of whatever the hero looks like on the page.
