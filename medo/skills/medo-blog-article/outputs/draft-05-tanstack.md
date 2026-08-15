---
title: "MeDo Migrated to TanStack Start: What It Means for Your Apps"
description: "MeDo rebuilt its frontend with TanStack Start — what the migration means for your AI apps: faster loads, smoother navigation, more reliable builds."
slug: "medo-tanstack-frontend-migration"
date: 2026-06-15
author: "Kostja"
category: "Guide"
image: "/blog/images/medo-tanstack-frontend-migration.jpg"
keywords:
  - "MeDo TanStack frontend migration"
  - "vite to tanstack"
  - "medo frontend upgrade"
  - "tanstack start"
  - "AI app builder performance"
  - "medo platform update 2026"
related:
  - "how-to-build-mobile-app-with-ai"
  - "what-is-vibe-coding"
  - "best-ai-mobile-app-builders"
secondary_category: "Mobile App"
---

# MeDo Migrated to TanStack Start: What It Means for Your Apps

If you have built an app on MeDo in the past few weeks, you might have noticed something: the builder feels a little faster. Pages load with less of that half-second hesitation. Navigating between your project dashboard and the build canvas no longer triggers that flicker you had learned to ignore.

You are not imagining it. Behind the scenes, MeDo retired the frontend framework it was built on and replaced it with something newer — a move that took months of engineering work and, if we did it right, is mostly invisible to you. That is the point.

This article explains what changed, why the timing matters, and what the upgrade actually means for the apps you build on MeDo. No code examples, no config diffs — just the parts that affect your experience.

## TL;DR

- **MeDo migrated its frontend from a Vite-based custom setup to TanStack Start**, a modern full-stack React framework built by the team behind TanStack Query and TanStack Router.
- The migration is already live. If you used MeDo recently, you have been running on TanStack without noticing — which is exactly how infrastructure upgrades should feel.
- The three things you are most likely to notice: faster page loads inside the builder, smoother navigation between views, and a more stable app preview experience.
- TanStack Start gives MeDo a foundation that scales with user growth — fewer build failures, faster iteration on new features, and no dependency on a single hosting vendor.
- **Nothing changes for your existing apps.** The migration affects MeDo's own builder interface, not the iOS and Android apps you generate and publish.

## 1. What actually changed — in plain English

Think of a frontend framework as the chassis and drivetrain of a car. The engine (MeDo's AI generation pipeline, the native Swift and Kotlin output) stayed the same. What changed is how the dashboard, the build canvas, the project settings, and every other screen you interact with gets assembled and delivered to your browser.

MeDo previously used a custom setup built on <a href="https://vite.dev" rel="nofollow noopener">Vite</a>, a fast build tool that has been the default choice for React projects for several years. Vite is excellent at what it does — starting a development server in milliseconds and bundling code for production with minimal configuration. But a build tool is only one piece of the puzzle. As MeDo's interface grew more complex — real-time build logs, multi-step project wizards, live app previews — the team found themselves writing more and more custom plumbing to connect Vite to the routing, data fetching, and server-side rendering layers the builder needed.

TanStack Start replaces that custom plumbing with a set of purpose-built components. Specifically, it brings three things under one roof: **TanStack Router** for type-safe page navigation, **TanStack Query** for fetching and caching data from MeDo's backend, and **TanStack Start** itself as the framework that ties them together. The result is fewer hand-rolled solutions, fewer edge cases, and a codebase that is easier to extend without introducing regressions.

If you are not a developer, here is the one-sentence version: MeDo swapped out a collection of custom-built parts for a unified system that the broader React ecosystem has been refining for years. The same way you would rather drive a car with an integrated transmission than one assembled from mismatched components, MeDo's builder now runs on a foundation designed to work as a whole.

## 2. Why now — the timing behind the migration

TanStack Start reached its 1.0 release in early 2026 after more than a year in active development. Before 1.0, migrating a production application to it would have meant betting on unstable APIs and incomplete documentation — a risk not worth taking for a platform that thousands of people rely on to ship real apps.

The 1.0 milestone changed the calculus. The API surface stabilized. The deployment story matured — TanStack Start apps now run on Vercel, Cloudflare Workers, Netlify, and plain Node.js servers without vendor-specific configuration. The community around TanStack Router and TanStack Query had already proven itself on projects larger than MeDo.

At the same time, MeDo's user base was growing in ways that exposed the limits of the old setup. More concurrent builds meant more opportunities for the builder UI to fall out of sync with backend state. More pages in the dashboard meant more routes to maintain by hand. The migration was not a rewrite driven by shiny-new-thing syndrome — it was a calculated bet that the ecosystem had finally caught up to what MeDo needed.

## 3. What you will notice as a MeDo user

The migration touched three areas where users are most likely to feel the difference. These are not benchmarks you need to measure — they are the kind of improvements you notice by their absence.

**Page loads inside the builder are faster.** TanStack Start uses Vite under the hood for development and production builds, but adds server-side rendering and automatic code splitting that the old custom setup handled inconsistently. When you open your project dashboard, the initial paint happens in roughly half the time it used to take on a typical connection. Subsequent navigations — switching from the dashboard to the build canvas, opening project settings — feel closer to a native app than a web page because TanStack Router prefetches linked pages before you click.

**Navigation between views is smoother.** The old setup sometimes showed a brief white flash between routes — a common artifact of client-side routing without proper loading states. TanStack Router handles route transitions with built-in loading boundaries, which means MeDo was able to remove the custom transition code that was responsible for most of those flickers. The result is a builder that feels less like a website and more like a tool.

**App previews are more stable.** This one is less visible but more important. The old custom data-fetching layer occasionally let the build canvas show stale state — your app said "build complete" but the preview still showed the previous version. TanStack Query's cache invalidation model makes it explicit when data is fresh and when it needs to be refetched. The MeDo team rewired the real-time build log and preview components to use this model, which eliminated an entire class of "it says done but it is not done" bugs.

## 4. Why TanStack Start over the alternatives

A natural question: why not Next.js? It is the default React framework, the one most developers reach for first, and the one with the largest ecosystem of tutorials and third-party libraries.

The short answer is that TanStack Start gives MeDo something Next.js cannot: deployment portability without compromise. Next.js is deeply integrated with Vercel's infrastructure. You can run it elsewhere — on Node servers, on Cloudflare, on Netlify — but the further you drift from Vercel, the more of Next.js's optimizations stop working. Image optimization, incremental static regeneration, and server actions each have deployment-specific behavior that made MeDo's infrastructure team nervous about long-term lock-in.

TanStack Start builds to standard JavaScript that runs identically on any Node-compatible host. For MeDo, which runs its own infrastructure rather than depending on a single platform vendor, that portability matters more than the ecosystem convenience Next.js offers.

There is also a philosophical fit. TanStack's libraries share a design philosophy: explicit over implicit, type-safe over stringly-typed, composable over monolithic. MeDo's engineering team found that this philosophy produced fewer "works in development, breaks in production" surprises than the alternatives they evaluated. For a platform that cannot afford to ship builder regressions — every bug in the builder is a bug in someone's app-building session — that predictability was the deciding factor.

## 5. The bigger picture — infrastructure you do not have to think about

There is a pattern in how MeDo talks about itself: the platform handles the complexity so you do not have to. You do not need to learn Swift to ship an iOS app. You do not need to configure Xcode to test on a real device. You do not need to understand App Store Connect provisioning to publish.

The TanStack migration extends that pattern to the builder itself. When you open MeDo and start a new project, you are running on a frontend infrastructure that a team of engineers spent months selecting, testing, and deploying — and you do not need to know any of it. The same way you trust that the native iOS and Android output is real Swift and Kotlin without inspecting the generated code, you can trust that the builder's interface is running on a modern, well-maintained foundation without reading a single config file.

This is not the last infrastructure upgrade MeDo will make. As the user base grows and the product surface expands, the underlying technology will keep evolving. The commitment is that those changes will feel like this one: noticeable only in the ways that matter, invisible everywhere else.

## Conclusion

MeDo's migration from Vite to TanStack Start is the kind of change that most users will never read about — and that is by design. You are here to build apps, not to audit frontend frameworks. But the next time you open your project dashboard and everything just works a little faster than you remember, you will know why.

If you have not tried building on MeDo yet — or if you last tried before the migration — there has never been a better time to start. The builder is faster, the platform is more reliable, and the same <a href="/ai-mobile-app-builder">AI mobile app builder</a> that generates native iOS and Android from conversation is running on an infrastructure built to scale.

## Frequently asked questions

### Does the TanStack migration affect my existing apps?

No. This migration affects MeDo's own builder interface — the dashboard, the build canvas, the project settings you use to create and manage apps. The iOS and Android apps you generate with MeDo are completely separate codebases that compile to native Swift and Kotlin. Nothing about your published apps changes.

### Is TanStack better than Next.js?

"Better" depends on what you are optimizing for. Next.js has a larger ecosystem and more third-party integrations. TanStack Start prioritizes deployment portability and explicit data flow — it runs the same way on any Node-compatible host without vendor-specific behavior. For MeDo's use case — running its own infrastructure with a growing user base — TanStack Start was the stronger fit. For a different product with different constraints, Next.js might be the right call.

### Will MeDo get slower during future migrations?

The TanStack migration happened with zero downtime for MeDo users. The engineering team ran the old and new frontend in parallel during a phased rollout, routing a small percentage of users to the new version and monitoring for regressions before switching over entirely. Future infrastructure upgrades will follow the same pattern.

### Does this mean MeDo is moving away from Vite entirely?

TanStack Start uses Vite as its underlying build tool, so Vite is still part of MeDo's stack — it is just no longer the framework layer. Think of it as Vite getting a promotion from "the whole frontend setup" to "the build engine inside a larger system."
