---
title: "MeDo Components: AI-Generated UI Blocks for Any Builder"
description: "MeDo Components is live: type a prompt and get a production-ready React + Tailwind UI block — navbar, pricing table, hero — for any AI builder."
slug: "medo-components"
date: 2026-08-14
author: "Kostja"
category: "Product"
secondary_category: "Components"
---

# Describe It Once, Use It Anywhere: MeDo Components Is Now Live

Every website you have built with an AI tool — or watched someone else build in a tweet — is assembled from the same handful of blocks. A navbar, a hero, a feature grid, a pricing table, a testimonial strip, a footer. These six blocks account for most landing pages on the internet, and you have described each one to an AI builder a dozen times already. That tedium is what **MeDo Components** removes. Launching today at [the components page](/components), it lets you copy a production-ready React + Tailwind block with a live preview and drop it into whatever project you are working on — instead of re-describing the same navbar and hoping for the same result.

The core idea is that the prompt is the artifact. Ask an AI builder to "make a pricing table" twice in a row and you get two different tables: different spacing, different cards, different hover states. MeDo Components treats the prompt itself as the deliverable — a precise, state-by-state description of what the component must do — so the same prompt produces the same component every time, in MeDo, Lovable, Bolt, v0, or Cursor.

## TL;DR

- **MeDo Components is a prompt-first component generator**: describe a navbar, pricing table, hero, or any other UI block and you get production-ready React + Tailwind code with a live preview — no copying from a docs site, no reverse-engineering someone else's prop API.
- **The prompt is the deliverable**: the same focused prompt yields the same component on every run, which fixes the "the AI redrew my navbar differently again" problem in vibe coding.
- **It works where you already build**: blocks copy into MeDo, Lovable, Bolt, v0, or Cursor, and come out themeable through design tokens rather than hardcoded colors.
- **Accessibility ships inside the generated code**: focus trapping for modals, live-region politeness for toasts, hidden labels for icon-only buttons — written into the generation, not bolted on later.
- **Thirty components are live today** across UI primitives, navigation, page sections, and a complete 404 page — and the generator takes any description you throw at it.

The promise in one sentence: a website stops being a blank canvas and becomes a set of blocks you pick, snap together, and ship — and consistency is what makes the blocks snap rather than fight. This article covers what the feature is, what is inside the gallery, why consistency matters, how it differs from a kit or a registry, and how to use a block in the builder you already work in.

## 1. What MeDo Components is

MeDo Components turns a plain-language description into a finished UI block in roughly three minutes. You type something like "a pricing table with three tiers and a monthly-yearly toggle," and the generator returns the React and Tailwind code with a live preview beside it. The output covers the states you usually have to ask for separately — hover, focus, loading, disabled — because the prompt for each component names those states explicitly rather than hoping the model happens to include them.

The workflow is a four-step loop, and each step is short enough to keep you in flow:

1. **Describe** — type the component you want, or start from the written prompt on any component page (~30 seconds).
2. **Preview and iterate** — a live preview renders next to the code; refine with follow-up prompts, adjust the theme tokens, or edit the JSX directly, whichever is faster.
3. **Copy or import** — paste the prompt into Lovable, Bolt, v0, or Cursor, take the raw code, or keep building in MeDo, where the component lands as a real file with its dependencies wired up.
4. **Ship it** — publish from MeDo to a live URL, or commit the component into your own repository.

None of it requires MeDo at runtime. The generated code is plain React and Tailwind — you own it, and it runs wherever you deploy it.

## 2. What's inside the gallery

Thirty components are live today, split across three layers plus one complete page. The layers map to how you actually assemble a site — primitives for the reusable parts, navigation and feedback for the frame, and page sections for the full-width blocks that stack into a landing page.

| Layer | Components | What it's for |
|-------|-----------|---------------|
| **UI primitives** (13) | Button, Input, Card, Modal, Tooltip, Toast, Alert, Badge, Avatar, Tabs, Accordion, Search Bar, Dropdown Menu | The reusable parts you drop in anywhere |
| **Navigation & feedback** (8) | Navbar, Header, Sidebar, Breadcrumb, Footer, Contact Form, Cookie Banner, Loading Spinner | Framing and connecting pages |
| **Page sections** (8) | Hero Section, Feature Grid, Testimonials, Gallery, Blog Section, Pricing Table, CTA Section, Newsletter Signup | Full-width blocks that stack into a landing page |
| **Complete page** (1) | 404 page | For visitors who wander off |

The component pages do more than show a finished screenshot. Each one documents the states and edge cases a production component has to handle — the part usually missing when you copy from a template or an internal library. The Button prompt, for instance, generates primary, secondary, ghost, and destructive variants at three sizes, with hover, focus, loading, and disabled states. The Modal prompt includes focus trapping, focus restore on close, body scroll lock, and a mobile bottom-sheet variant. Those requirements live inside the prompts, so they land in the generated code rather than becoming a follow-up task.

## 3. What it fixes — and why consistency matters

The problem MeDo Components solves is not "I don't have a navbar." Every AI builder can give you a navbar. The problem is that the navbar you get changes every time you ask. In a vibe coding loop — describe, preview, tweak, preview again — that instability compounds: you spend a session re-aligning spacing on a component that regenerated slightly differently than it did five minutes earlier. If you are new to the concept, see our [guide to vibe coding](/blog/what-is-vibe-coding).

Consistency is what turns components into building blocks instead of lottery tickets. When the same prompt reliably produces the same navbar, a navbar becomes a solved problem — you grab it once and move on to the part of the site that actually needs thinking. This is the LEGO principle: the value is not that any single block is stunning on its own, but that every block snaps together with every other block, sharing the same spacing, radius, and color tokens.

The gallery also plugs into how MeDo generates apps in the first place. Every app you describe to the builder is internally composed of components — a dashboard is a sidebar, a data table, stat cards, a settings form. Components is the surface where those blocks become something you can pick up and reuse across projects, instead of staying locked inside a single generated app. For the full picture, the [how-to-build-mobile-app-with-ai](/blog/how-to-build-mobile-app-with-ai) walkthrough shows where components sit in the build flow.

## 4. What makes these components different

Four choices separate this from a Tailwind UI kit or a community component registry. The table below positions MeDo Components against the two things it is most often confused with.

| Dimension | UI kit (e.g. Tailwind Plus) | Community registry (e.g. 21st.dev) | MeDo Components |
|-----------|----------------------------|------------------------------------|-----------------|
| **What you get** | A fixed catalogue of components to copy | Authored components + AI-ready prompts | A generator: describe, get code |
| **When your case differs** | You edit someone else's code | You search for a closer match | You edit the description and regenerate |
| **Consistency** | Fixed by the kit | Varies by component author | Prompt-as-artifact: same prompt, same result |
| **Who it serves** | Designers and agencies | Developers using AI agents | Non-developers and vibe coders |
| **Accessibility** | Best-effort per component | Varies by contributor | Written into the generation contract |

First, the prompt is the deliverable, not a fixed catalogue. A kit gives you a list of components to copy from; when your case is slightly different, you are editing someone else's code. Here you edit the description and regenerate, so the component matches your situation instead of the nearest catalogue entry. This is the same gap that community registries like <a href="https://21st.dev" rel="nofollow noopener">21st.dev</a> address for developers — MeDo's version makes the prompt itself the product, so a non-technical builder never has to inspect a component's props to adapt it.

Second, accessibility is part of the generation contract. Each component page states what the component must handle — focus trapping and restore for modals, live-region politeness for toasts, hidden text labels for anything that would otherwise convey meaning through color alone. Because those requirements are written into the prompts, they appear in the generated code rather than being a follow-up audit item.

Third, the output is themeable through design tokens, not hardcoded colors. Styled with Tailwind tokens, a component drops into your project without dragging a foreign palette along — you retheme it, not rewrite it.

Fourth, the markup is framework-agnostic. Components are authored in React and TypeScript, but each page shows the same component mounted in Next.js, Vue 3, SvelteKit, Astro, and plain HTML. That is why the same prompt runs equally well in Lovable, Bolt, v0, and Cursor — and why the feature pairs naturally with the [web apps MeDo now ships with server-side rendering](/blog/medo-tanstack-frontend-migration).

## 5. How to use a component in any builder

If you build in MeDo, the component lands as a real file in your project with its dependencies wired up — the lowest-friction path. If you live in another tool, the copy button gives you the same prompt you would have written yourself, but sharper. Specificity is the point: a vague prompt produces a different component on every run, while these prompts name the states and edge cases explicitly, so the result stays consistent in any editor.

The user this is built for is broader than a developer audience:

- **Indie hackers** skip a week of layout work and ship a landing page tonight.
- **Vibe coders** on Lovable and Bolt stop asking their editor to redraw the same navbar and getting a different answer each time.
- **Agencies** start every client site from the same vetted set and retheme rather than rebuild.
- **Non-technical founders** never learn React or Tailwind — they describe the section they want in plain English and keep editing the same way.

If you are still deciding which AI builder to commit to, the [best AI mobile app builders](/blog/best-ai-mobile-app-builders) comparison covers how these tools differ on mobile output specifically.

## 6. What it costs

Generating and previewing components runs on the same credits as the rest of the MeDo builder, and there is a free allowance to start with, as of August 2026. Downloading the full source of an entire project is a separate credit cost. This is a feature inside the builder you already pay for — not a separate product.

## Conclusion

The pitch of MeDo Components is that a website stops being a blank canvas and becomes a set of blocks you can pick, snap together, and ship. That framing only holds if the blocks are consistent — and consistency is exactly what a prompt-first generator delivers where a re-describe-every-time workflow cannot.

The honest test is simple: next time you describe a navbar or a pricing table from scratch, copy one of these prompts instead and see which result you keep. [Try MeDo Components](/components). And if you came here for mobile rather than web, the builder story is unchanged — native Swift and Kotlin from prompts, tested on your phone, with a path to the App Store, starting at the [AI mobile app builder](/ai-mobile-app-builder).

## Frequently asked questions

### Is MeDo Components different from a Tailwind UI kit or a component library?

Yes. A kit is a fixed catalogue: when your case differs slightly from the examples, you edit someone else's code. MeDo Components is prompt-first — you edit the description and regenerate, so the component matches your situation. The output is plain React and Tailwind with no runtime dependency on MeDo.

### Which frameworks do the components support?

Components are authored as React and TypeScript with Tailwind CSS — the same stack used by Lovable, Bolt, v0, and Cursor projects. Each component page also shows the component mounted in Next.js, Vue 3, SvelteKit, Astro, and plain HTML, because the markup itself is framework-agnostic.

### Can I use these prompts in Lovable, Bolt, v0, or Cursor?

Yes. The prompts are plain English with no MeDo-specific syntax, so they run in any AI editor, and every component page has a copy button for exactly this. Specificity is what makes it work: these prompts name states and edge cases explicitly, so you get a consistent result instead of whatever the model happens to produce from a one-line request.

### What does generating a component cost?

Generating and previewing components runs on the same credits as the rest of the MeDo builder, with a free allowance to start, as of August 2026. Downloading the full source of a project is a separate credit cost. The pricing page carries the current numbers.

### Do the generated components handle accessibility?

Yes, by default. Each component page states its accessibility contract — focus trapping and restore for modals, live-region politeness for toasts, hidden text labels for anything that conveys meaning through color alone. Those requirements live in the prompts, so they appear in the generated code rather than becoming a follow-up task.

### Can MeDo generate a component that is not listed here?

Yes. The listed pages cover the components people reach for most, but the generator takes any description. If you need something unusual, describe it directly instead of hunting for the closest listed match.
