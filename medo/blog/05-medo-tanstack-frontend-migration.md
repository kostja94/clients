---
title: "MeDo-Generated Apps Now Ship with TanStack SSR"
description: "MeDo now generates web apps with TanStack Start by default, replacing pure client-side rendering. How CSR-first SSR fixes SEO and AI crawler gaps."
slug: "medo-tanstack-frontend-migration"
date: 2026-06-15
author: "Kostja"
category: "Guide"
secondary_category: "Mobile App"
---

# From Empty Shell to Full HTML: How MeDo-Generated Web Apps Now Ship with Server-Side Rendering

If you have used MeDo — or any AI app builder that outputs web projects — to generate a React application in the past year, there is a simple test you can do. Open the deployed app in your browser, right-click, and select "View Page Source." Until recently, what you would have seen looked something like this:

```html
<!DOCTYPE html>
<html>
  <body>
    <div id="root"></div>
  </body>
</html>
```

That empty `<div id="root">` is the entirety of what the browser — and more importantly, every search engine and AI crawler — received from your server. Everything else: the navigation, the product table, the sign-up form, your carefully <a href="/blog/what-is-vibe-coding">vibe-coded</a> dashboard, all of it materialized later, inside the user's browser, after a JavaScript bundle downloaded, parsed, and executed. For a human on a decent connection, this happens fast enough that the delay feels like a loading spinner, not a missing page. For Google, the delay averages nine times longer than server-rendered content to reach full indexability. For AI crawlers — GPTBot, ClaudeBot, PerplexityBot, and the growing fleet of agents that determine whether your app surfaces in an AI-generated answer — the result is even simpler: they see a blank page and move on.

MeDo has now changed the default framework for generated web applications from a pure client-side Vite setup to **TanStack Start**, a full-stack React framework that ships complete HTML on the first request. This article explains what that means, why TanStack Start over the alternatives, and what changes — and does not change — for the apps you build.

## TL;DR

- **Every AI-generated web app on MeDo previously shipped as a pure client-side React bundle** — one empty `<div>`, one large JavaScript file, zero HTML content before the browser ran the script.
- **The new default is TanStack Start**, a full-stack React framework that sends a fully rendered HTML page on the first request, then transitions to client-side navigation for everything after. This is not Next.js — TanStack Start uses a CSR-first model, while Next.js routes most navigations through the server.
- **The most important beneficiary is not your users — it is every bot that decides whether your app exists.** Search engines index server-rendered pages faster. AI crawlers, which do not execute JavaScript at all, can now actually read your content.
- **Existing generated apps do not need to migrate.** MeDo provides pre-rendering that generates static HTML snapshots at build time — no code changes, no opt-in, no cost. But pre-rendered pages are static snapshots, not dynamically generated per request like full SSR.
- **Native iOS and Android output is unaffected.** The framework change applies only to web apps generated through MeDo. Swift and Kotlin exports work exactly as before.

## 1. What your AI-generated web app was running on — and what was missing

To understand why this change matters, it helps to know exactly what a "Vite-based React app" means in practice — not in terms of build configuration, but in terms of what reaches a browser or a bot when someone visits your deployed app.

When MeDo — or Lovable, Bolt, or any AI builder targeting React — generated a web project under the previous default, the output was a **client-side rendered (CSR) single-page application**. The architecture is straightforward: a build tool (Vite, in this case) bundles your React components, your routing logic, your data-fetching code, and your CSS into one or more JavaScript files. Those files are deployed to a static host. When a visitor arrives, the server sends back an HTML file containing essentially nothing but a `<div id="root">` and a `<script>` tag pointing to the JavaScript bundle. The browser downloads the bundle, executes it, and React constructs the entire page — navigation bar, content, footer, everything — inside that empty div.

This model has real advantages. It is simple to deploy — any static file host works, from Vercel to Cloudflare Pages to an S3 bucket. It is fast for users once the bundle loads, because subsequent page transitions happen entirely in the browser without server round-trips. And for the AI builders that generate this code, it is predictable: a single entry point, a single rendering path, and no server runtime to manage.

The trade-off shows up in two places that matter more than most builders realize.

**Search engines.** Google can render JavaScript, but it does so on a separate pass that happens minutes to hours after the initial crawl. A 2024 Vercel analysis found that client-side rendered pages take roughly nine times longer to reach full indexability compared to server-rendered equivalents. For an AI-generated habit tracker or a niche community dashboard, that delay may be tolerable. For a SaaS landing page or a marketplace that depends on organic discovery, every hour of delayed indexing is lost traffic that a server-rendered competitor captures immediately.

**AI crawlers.** This is the more acute problem in 2026. GPTBot (OpenAI), ClaudeBot (Anthropic), PerplexityBot, and the expanding roster of crawlers that feed AI search and answer engines do **not execute JavaScript**. They parse the HTML the server sends and extract text. A pure CSR app sends them one empty `<div>` — no content, no links, no structured data. Your app, as far as these increasingly influential gatekeepers are concerned, does not exist.

TanStack Start was chosen to address both problems at once — without sacrificing the client-side navigation speed that makes SPAs feel responsive.

## 2. What TanStack Start changes — and what it is not

TanStack Start is a full-stack React framework built by <a href="https://tanstack.com/start" rel="nofollow noopener">the team behind TanStack Query, TanStack Router, and TanStack Table</a>. It reached its 1.0 release in early 2026 after more than a year of active development. It is not a Vite replacement — Vite remains the build tool underneath. It is an **application architecture** layered on top: file-based routing, server functions, and a rendering model that sends complete HTML on the first visit and then hands control to the browser for everything after.

This pattern — **CSR-first SSR** — is the most important thing to understand about TanStack Start, and it is also the thing that most cleanly distinguishes it from Next.js.

In Next.js, the default rendering model is server-first. Every page navigation involves a round-trip to the server by default, with the framework providing opt-in mechanisms for client-side transitions. The optimization direction is toward reducing the amount of JavaScript shipped to the client — React Server Components, streaming, partial prerendering — all oriented around moving work off the browser and onto the server.

TanStack Start takes the inverse approach. The **first** request goes through the server, which renders the full page as HTML — solving the SEO and AI crawler problem at the point where it matters most: the initial visit. From that point forward, TanStack Router takes over in the browser, and every subsequent navigation is a client-side SPA transition — no server round-trip, no full-page refresh. The optimization direction is toward making the first impression complete while keeping the ongoing experience smooth.

This CSR-first model is not the right answer for every product. But it is a particularly good fit for the kind of applications that AI builders generate most often. When someone prompts MeDo to build a SaaS dashboard, an admin panel, a project tracker, or an interactive tool, they are creating an application that a user opens once and then navigates within extensively — switching between tables, opening detail views, filtering data. That usage pattern benefits far more from fast client-side transitions than from repeated server round-trips. A blog or a marketing site wants server-first rendering for every page. An interactive app wants its first page server-rendered for discoverability and everything after rendered in the browser for speed. That is what TanStack Start delivers.

## 3. Why TanStack Start over Next.js — the five reasons that mattered

Choosing a rendering framework for AI-generated code is different from choosing one for a hand-maintained codebase. The decision involves not just what produces the best output for a skilled engineering team, but what produces the most predictable output when an AI agent is writing the code. Here are the five factors that shaped the decision.

**First, product fit.** The majority of web apps generated through AI builders are interactive applications — dashboards, admin panels, internal tools, SaaS interfaces — not content sites. These apps share a usage pattern: a user arrives once, then navigates across many views in a single session. TanStack Start's CSR-first model means that arrival page is fully server-rendered (good for discovery and first paint), while the dozens of internal page transitions that follow happen instantly in the browser (good for perceived performance). Next.js's server-first model would route every one of those internal transitions through the server, adding latency to each navigation for a type of app that benefits least from that architecture.

**Second, compile-time type safety for AI-generated routes.** TanStack Router is unique among React routers in providing full compile-time type checking for route parameters, search parameters, and navigation targets. For human developers, this catches mistakes before they reach production. For AI-generated code, the impact is larger: when an agent writes routing logic — linking a project detail view, passing filter parameters between pages, constructing navigation from a gallery — TanStack Router validates the types at build time. A mismatched route parameter or a misspelled search param becomes a compile error, not a runtime crash that a non-technical builder discovers when their deployed app breaks. Fewer AI-generated bugs reach the user because fewer survive the build step.

**Third, deployment portability without compromise.** TanStack Start runs on <a href="https://nitro.build/" rel="nofollow noopener">Nitro</a>, a server runtime that produces identical output across Node.js, Cloudflare Workers, Deno, Bun, and AWS Lambda. Next.js is deeply integrated with Vercel's infrastructure — features like incremental static regeneration, image optimization, and server actions behave differently or degrade on non-Vercel hosts. For an AI builder that gives users the ability to deploy wherever they choose, a framework that runs the same way everywhere removes an entire category of "works in preview, breaks on my host" support issues.

**Fourth, TanStack Query integration.** Many AI-generated apps are data-intensive — they fetch from Supabase, call Stripe APIs, sync project state. TanStack Query's caching, background refetch, and streaming SSR support are built into TanStack Start's data loading model rather than bolted on. When an app's data layer uses TanStack Query, the framework can stream that data during the initial SSR render, hydrate it on the client, and keep it fresh through the session — all without the agent needing to write custom data-fetching plumbing for each project.

**Fifth, Vite's cold-start advantage for real-time preview.** This matters less for the deployed app than for the build experience inside MeDo itself, but it shapes what builders see while they work. Vite's development server cold-starts in 300–500 milliseconds in typical projects. Turbopack, which Next.js uses, takes 2–5 seconds on a cold start according to public benchmarks from both projects. In a vibe-coding loop — prompt, preview, tweak, preview again — that per-iteration difference accumulates into a noticeably faster feedback cycle. Builders see their changes sooner, which makes the iteration loop tighter and the building experience more responsive.

None of this is an argument that TanStack Start is universally better than Next.js. For a content-heavy marketing site maintained by a frontend team, Next.js's server-first architecture and Vercel ecosystem remain strong choices. For the specific profile of AI-generated interactive applications — code written by agents, deployed on diverse hosts, opened by users who navigate extensively within a single session — TanStack Start's CSR-first SSR model is the more natural fit.

## 4. The numbers behind the migration

Framework choices involve trade-offs that resist simple quantification, but the TanStack team published performance benchmarks in March 2026 that give a sense of what the architecture delivers under load.

On their standard benchmark suite, TanStack Start moved from 427 requests per second to 2,357 requests per second over the course of the 1.0 stabilization — a 5.5× improvement in throughput. Average latency dropped from 424 milliseconds to 43 milliseconds, a 9.9× reduction. The p99 latency — the number that matters most for the slowest 1% of your users — fell from 6,558 milliseconds to 928 milliseconds, a 7.1× improvement.

A third-party benchmark from <a href="https://platformatic.dev/" rel="nofollow noopener">Platformatic</a> tested TanStack Start against Next.js v16 under identical conditions — the same e-commerce application, no caching, increasing request rates. At 1,000 requests per second, TanStack Start maintained a 100% success rate. Next.js v16 succeeded on approximately 64% of requests at the same load, with errors climbing as concurrency increased. This is a synthetic benchmark and real-world results depend on application structure, hosting configuration, and traffic patterns — but the gap in headroom under load is meaningful for platforms that need to serve many deployed applications from shared infrastructure.

For the individual builder, these numbers are background noise. You will not measure your habit tracker's p99 latency. What they translate to in practice is this: your app's first page loads with complete HTML content that search engines and AI crawlers can immediately parse, and the subsequent pages your users navigate through respond without server round-trips — a combination that neither pure CSR nor pure SSR delivers alone.

## 5. What happens to your existing web apps

If you already generated and deployed a web app through MeDo under the previous Vite-based CSR default, you have a straightforward question: do you need to rebuild?

The short answer is no. MeDo provides a **pre-rendering** path for existing projects: at build time, the framework generates a static HTML snapshot of each page in your application. These snapshots are deployed alongside the JavaScript bundle. When a bot or a search engine crawls your existing app, it now receives a pre-rendered HTML page with full content — not an empty `<div>`. This is not full SSR, where each request dynamically generates fresh HTML from live data, but it closes the blank-page gap for discovery and indexing. There is no opt-in required, no migration step, no code changes on your end, and no additional cost — it happens automatically at the next build.

The distinction between pre-rendering and SSR is worth keeping straight. Pre-rendering produces a **static snapshot** — the HTML reflects the state of your app at build time. If your app displays data that changes frequently, the pre-rendered HTML will show whatever was current when the build ran, not what is current at the moment a visitor arrives. Full SSR generates fresh HTML on every request, so dynamic data is always up to date. For apps that are mostly layout, navigation, and forms — a project dashboard, a settings interface, a gallery — pre-rendering covers the discovery use case well. For apps where every page load depends on fresh backend data, the TanStack Start SSR default is the stronger solution, and new projects get it automatically.

New projects generated through MeDo as of June 2026 default to TanStack Start with full SSR. Existing projects continue to work as before, with pre-rendering filling the gap that pure CSR left open.

## Conclusion

The shift from a Vite-based CSR default to TanStack Start with SSR is not a headline feature. It does not add a new capability to the MeDo builder interface, introduce a new export format, or change how you describe what you want your app to do. What it changes is what happens after you deploy — whether a search engine can find your app, whether an AI crawler can read your content, and whether the first page your users see loads as a complete experience or as a blank shell waiting for JavaScript.

If you are evaluating <a href="/ai-mobile-app-builder">AI mobile app builders</a>, judge them on output — native code, real-device testing, and store publishing paths, as covered in [how to build a mobile app with AI](/blog/how-to-build-mobile-app-with-ai) — not on whether they use one JavaScript framework or another. But for the web apps you generate along the way, the difference between an empty `<div>` and a fully rendered page is the difference between being visible to the web and being invisible to the growing share of it that does not run JavaScript at all.

## Frequently asked questions

### Does this affect my existing generated web apps?

Your existing apps continue to work exactly as deployed. The pre-rendering system generates static HTML snapshots at build time so that bots and crawlers receive full content instead of an empty shell. There is nothing you need to configure or change — it activates automatically on your next build. If you want full SSR with dynamically generated HTML on every request, create a new project, which defaults to the TanStack Start setup.

### Do I need to learn TanStack Start to keep building with MeDo?

No. MeDo is designed for builders who describe apps in plain language, not for people who configure routers by hand. TanStack Start is an internal framework choice that shapes what your generated web app ships — you do not need to write a single line of TanStack configuration. Your workflow stays the same: describe your app, preview it, iterate, and deploy.

### Is TanStack Start better than Next.js?

"Better" depends on what kind of app you are building and who is writing the code. Next.js has a larger ecosystem, more third-party tutorials, and deeper Vercel integration. TanStack Start prioritizes deployment portability, compile-time type safety for routes, and a CSR-first rendering model that keeps internal navigation fast after the first server-rendered page. For the interactive web apps that AI builders generate most often — dashboards, tools, admin panels — TanStack Start's architectural choices are a strong fit. For a content-heavy marketing site maintained by a frontend team, Next.js remains an excellent choice.

### Does this change affect native iOS and Android output?

No. Native Swift and Kotlin generation, QR-based device testing, and the <a href="/blog/publish-ai-app-app-store">App Store publishing workflow</a> are completely separate from the web framework. This change applies only to web applications generated through MeDo. If you are building a mobile app for the App Store or Google Play, nothing about your output has changed.

### What is the difference between pre-rendering and full SSR?

Pre-rendering generates static HTML files at build time — one snapshot per page, reflecting the state of your app when the build ran. Full SSR generates fresh HTML on every request, pulling current data from your backend in real time. Pre-rendering solves the blank-page problem for discovery and indexing, but the HTML can become stale if your app's content changes frequently. Full SSR keeps every page load current but requires a server runtime. Existing projects get pre-rendering automatically; new projects get full SSR by default through TanStack Start.

### Why did MeDo choose TanStack Start over the previous Vite setup?

Vite remains the build tool underneath — TanStack Start is an application architecture layered on top. The reason for the change is output, not tooling: pure client-side rendering delivered an empty `<div id="root">` to search engines and AI crawlers. TanStack Start's CSR-first SSR sends complete HTML on the first request while keeping client-side navigation for everything after. That combination solves the indexing gap without slowing down the interactive apps MeDo generates.
