---
title: "Why AI Websites Look the Same (and How to Fix It)"
description: "AI websites converge because models output the average of their training data. Here's why, the visible tells, and a constraint-first fix."
slug: "why-ai-websites-look-the-same"
date: 2026-08-22
author: "Kostja"
category: "Guide"
secondary_category: "AI Frontend Design"
---

# Why AI Websites Look the Same (and How to Fix It)

You have probably seen it — or shipped it. The purple gradient hero, the three identical cards, the headline in a font you have seen on a hundred other sites. Ask Lovable, Bolt, v0, Cursor, or any AI builder for a landing page and the result is statistically the same page, and by 2026 the sameness itself has become a signal users actively use to discount a product. The reason is not a lack of talent or a bad prompt — it is mechanical. An AI model is a prediction engine, and the design it predicts is the average of everything it trained on. This guide explains why convergence happens, the five visible tells that give it away, why prompting harder does not fix it, and the constraint-first approach that actually does — the same design-system pillars this series has been building toward.

## TL;DR

- **AI websites converge because models output the statistical average of their training data** — Inter fonts, purple gradients, and three-card grids dominate the corpus, so the average looks like all of them.
- **It is a mechanism called mode collapse**: a model that should produce variety instead collapses to a narrow set of "safe" outputs, because safety is what got rewarded in training.
- **Better prompts are not the fix**: the model is excellent at executing a system and terrible at inventing one — so hand it the system.
- **The fix is constraints, not freedom**: a `DESIGN.md` contract, semantic tokens, and design skills force the output off the median.
- **Generic is sometimes fine**: internal tools, dashboards, and MVPs do not need to stand out — knowing when not to care is part of the discipline.

The good news is that the fix is well understood and cheap. The bad news is that it requires a shift from "describe what I want" to "hand it the system" — which is a different skill, and one you can learn in an afternoon.

## 1. Why AI websites converge: the math of the average

A large language model is not a taste engine — it is a probability engine. When you ask it for "a landing page," it does not consult a sense of what looks good; it computes the statistically most likely arrangement of elements given its training data, and returns it. That corpus is shockingly narrow. As the Rottoways analysis documents, it is roughly: Tailwind documentation examples, shadcn/ui component libraries, the top templates on Vercel, the public landing pages of YC-backed startups from 2022 to 2024, and a long tail of design systems that all reference the same canonical patterns. Train a model on that and ask it for variety — you get the average of the input.

The convergence is not a bug; it is the math. The average of every landing page in the corpus is, by definition, the least distinctive option available. And the problem compounds through a feedback loop: developers use Tailwind, Tailwind's defaults appear in training data, AI generates Tailwind defaults, developers ship that code, and that code becomes the next round of training data. Sailop's analysis of the loop found the tells are specific enough to measure — Inter or system-ui appears in roughly 73% of AI-generated frontends, blue-500 or indigo-500 as the primary color, white or slate-50 backgrounds, rounded-lg everywhere, shadow-md on every card. The model is not choosing these; it is averaging them.

This is a recent and specific form of a well-known failure mode. In machine learning, mode collapse describes a generative model that produces near-identical output regardless of input variation. AI coding tools exhibit design mode collapse: the prompt can say "SaaS landing page," "portfolio," or "e-commerce site," and the visual output converges on the same template anyway. The root causes are consistent — a training distribution dominated by one stack, a safety bias that rewards output that "cannot look broken" over output that could look wrong, and no aesthetic memory between generations unless the project hands the model a style guide to anchor it.

## 2. The five visible tells

The sameness is not abstract — it resolves into five specific patterns, and being able to name them is the first half of fixing them. The lists from Rottoways and Sailop converge on the same five:

1. **The purple or indigo gradient hero.** Blue-500 and indigo-500 as the primary color, often as a gradient on the first screen. It is the single most recognizable AI tell, and it persists because it was the safest, most-approved pattern in the training corpus.
2. **Three identical feature cards.** A `grid-cols-3` of cards with the same shape, icon, and padding, no hierarchy between them. The eye reads it as filler before it reads any of the three.
3. **Inter at weight 700 for every headline.** The display font that every model reaches for, set at the heaviest weight it knows — which reads as "trying" rather than "considered." The fix is restraint: weight 500, or a characterful face used with discipline.
4. **Centered everything.** Centered hero text, centered cards, centered CTAs. The default layout carries no information hierarchy, which is why every centered page looks interchangeable.
5. **The gradient "Most popular" pricing pill.** The highlighted middle plan with a gradient badge — a pattern so common it has become a meme, and users' eyes skip it automatically.

These five tells are the visible fingerprint of design mode collapse. They matter not because any one of them is ugly — the patterns are individually fine — but because together they signal "AI-generated" in under three seconds, and in 2026 that signal actively lowers trust. The AXE-WEB analysis frames the stakes as three tests the generic page fails: the "Know" test (it does not look like you), the "Like" test (it looks like everyone else), and the "Trust" test (sameness reads as low effort).

## 3. Why "better prompts" are not the fix

The natural instinct is to prompt harder — more adjectives, more specific requests, another round of "make it more unique." The consensus across the 2025–2026 literature is that this is the wrong investment. An LLM is not a brand designer; it lacks the eye for nuance, spacing, and emotional connection, and spending hours refining prompts yields diminishing returns. As the AXE-WEB analysis puts it, it is often faster to accept the AI's structure and apply the final styling yourself — because the structure is what the model is good at, and the taste is what it averages away.

The deeper reason prompting fails is that the model does not have a design system to draw from — it has a training-data average. No amount of "make it distinctive" can override the statistical center of the corpus, because that center is what the model produces by default. What does override it is changing the constraints the model works within. The Managed Code analysis frames the same point sharply: standing out means deliberately overriding the average, and that is a human job — but it is a job you do once, by writing the system down, not a job you do on every prompt.

This is where the diagnosis connects to the rest of this series. The fix is the design-system layer: a [DESIGN.md contract](/blog/what-is-design-md) that records your palette, type roles, and rules; semantic tokens that make the values portable and AI-readable; and design skills that add judgment. Hand the model the system — the same argument the [frontend-design skill](/blog/what-is-frontend-design-skill) makes at the aesthetic level and the [best AI design skills comparison](/blog/best-ai-design-skills) makes across the skill stack — and the output stops being the median and starts being yours.

## 4. The fix: constraints, not freedom

The principle is counterintuitive but well tested: the way to make AI output distinctive is to constrain it, not to free it. Sailop's analysis is blunt — "the solution is constraints. Not more freedom. More constraints." Tell the model to use a specific hue instead of blue, a specific heading face, a specific spacing scale, a specific easing curve, and the output stops looking generated, because the model is excellent at executing a system and terrible at inventing one. The job is to hand it the system.

For a non-developer, the system is three files and one habit. A `DESIGN.md` at your project root records the palette, typography, spacing, and the Do's and Don'ts — the three things you refuse to let the AI default to. Semantic tokens make those values portable and machine-readable, the [Figma design token guide](/blog/figma-design-tokens) and the [design tokens vs CSS variables comparison](/blog/design-tokens-vs-css-variables) cover the value layer. Design skills like `frontend-design` add the judgment to plan before building. The habit is the sequence: every generation runs against the contract, and anything that drifts is regenerated against the file rather than accepted as-is.

The same principle scales down to a single prompt. Sailop's worked fix for one of the five tells — the Inter headline — is "use Inter at weight 500 for display headlines, or replace it entirely with a serif like Fraunces or a geometric sans like Geist," and "triple your section padding; most AI sites use 64–96 pixels, use 160–200." These are constraints, and they work because they move the model off the centroid one decision at a time. A prompt-first generator applies the same logic automatically — [MeDo Components](/blog/medo-components) names the states and edge cases in the prompt itself, so the same focused prompt produces the same themed component every time, in any builder.

## 5. When generic is fine

The honest boundary cuts the other way, and naming it is part of the discipline. Generic is not always bad. For an internal tool, an admin dashboard, an MVP that needs to ship this week, or anything whose job is familiarity rather than distinction, the AI default is a feature — users recognize the patterns because they use them everywhere, and nobody cares what a settings screen looks like. The Adam Wathan framing is worth keeping: AI left alone will create something average every time, and average is sometimes exactly what the job calls for.

The decision is about stakes, not snobbery. If the page's job is to make someone feel something and remember you — a brand site, a landing page, a product's first impression — then the AI average is fatal, because the visitor decides within seconds whether you are like everyone else or something unique. If the page's job is to be efficient and familiar — a dashboard, an internal tool — the average is fine, and spending time making it distinctive is wasted effort. The trap is applying the "it must stand out" rule to everything, which burns the attention budget where it does not matter.

This is also why the trend-chasing instinct is a dead end. A site built to this season's trend is another average, just a newer one, and it looks dated by next season. Distinctiveness is intention, not novelty: choices that fit your brand and your story, which no trend and no model can generate for you. The constraint system in §4 is the durable version of that — it encodes your intention, not a trend.

## 6. A checklist to keep your site off the centroid

Run this list against your next generation, and you will catch most of the tells before they ship:

- [ ] **Is Inter (or system-ui) the display font?** Swap it for a face used with discipline, or drop the weight from 700 to 500 and let size carry the hierarchy.
- [ ] **Is the primary color blue-500 or indigo-500?** Pick a hue outside the default bands — a red-orange, a deep magenta, a yellow-green — and use it as the accent, not the whole page.
- [ ] **Are there three identical cards?** Break the grid: an asymmetric ratio, a vertical stack, or one emphasized card over two quiet ones.
- [ ] **Is everything centered?** Give the hero a deliberate information hierarchy — left-aligned claim, a single accent, no decorative filler.
- [ ] **Is there a gradient "Most popular" pricing pill?** Replace it with a checkmark, a bolder plan name, or more vertical space on the recommended plan.
- [ ] **Does a single section carry the boldness?** Restraint is the corollary: spend the memorable move in one place, keep everything around it quiet.
- [ ] **Did the AI regenerate something different than last time?** Your design system is the fix — a `DESIGN.md` and tokens make the output repeatable instead of variable.

The compounding logic behind the list is worth internalizing. One pattern alone does almost nothing; two are a coincidence; five start to feel like a system; eight to ten feel like a brand. The AI signature is a high-dimensional cluster — the model produces the centroid across many axes at once — so pulling away from it means moving on several axes together. You do not need all of them; most distinctive sites use eight to twelve in combination. But the ones you do use need to compound, which is why the checklist is best run as a set, not as isolated fixes.

## Conclusion

AI websites look the same because models output the average of their training data — and that average is the least distinctive option available. The five visible tells — purple gradients, three identical cards, Inter at 700, centered everything, the gradient pricing pill — are the fingerprint of design mode collapse, and in 2026 that fingerprint costs you trust. Better prompts do not fix it, because the model cannot invent a design system it was never handed.

The fix is constraints, not freedom: a `DESIGN.md` contract, semantic tokens, and design skills that force the output off the median — and the honest boundary that generic is fine when the page's job is familiarity, not memory. Start small: pick one tell from the checklist, write the constraint that kills it, and regenerate against it. Then carry the surviving decisions into a file your agent reads every session — the same contract-first thinking the [design tokens vs CSS variables](/blog/design-tokens-vs-css-variables) guide applies at the value layer. And if you would rather not maintain files at all, a prompt-first generator like [MeDo Components](/components) encodes the same constraints into the prompt itself, so the same description renders the same non-generic component in any builder.

## Frequently asked questions

### Why do AI websites look so similar even with different prompts?

Because the model outputs the statistical average of its training data, and that average is dominated by a narrow set of defaults — Inter fonts, purple gradients, three-card grids. Different prompts move within the same average unless constraints pull the output off it. The prompt is not the lever; the design system is.

### Is it actually a problem that AI sites look the same?

It depends on the stakes. For internal tools, dashboards, and MVPs, familiarity is a feature and generic is fine. For a brand site or a landing page — anything whose job is to be remembered — sameness costs trust, because visitors read it as low effort within seconds.

### Can I fix it with better prompts?

Largely no. The model is great at executing a system and terrible at inventing one, so hours of "make it more unique" prompt tweaking returns diminishing returns. The fix is constraints — a design system the model executes — not more adjectives.

### What are the most common AI design tells?

The five most visible: a blue or indigo gradient hero, three identical feature cards, Inter at weight 700 for headlines, centered-everything layouts, and a gradient "Most popular" pricing pill. Fixing them requires moving on several axes together — one fix alone reads as a coincidence.

### Do I need to learn design to make AI output look distinctive?

No. You need to learn to write constraints, which is a smaller and more mechanical skill. Name your palette, type roles, spacing, and the three things you refuse to let the AI default to, and put them in a file. The AI executes; you specify.

### Will this work with any AI builder?

The constraint system is tool-agnostic — a `DESIGN.md` and token file are read by any agent that loads them, and the same prompt produces consistent results in tools that treat the prompt as the artifact. The principle carries to mobile too, as the [guide to building a mobile app with AI](/blog/how-to-build-mobile-app-with-ai) shows.
