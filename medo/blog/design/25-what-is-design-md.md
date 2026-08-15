---
title: "What Is DESIGN.md? Google's Format for AI Design Systems"
description: "DESIGN.md is Google's open file format that describes a visual identity to AI coding agents — machine-readable tokens plus human-readable rules in one file."
slug: "what-is-design-md"
date: 2026-08-20
author: "Kostja"
category: "Guide"
secondary_category: "AI Frontend Design"
---

# What Is DESIGN.md? Google's Format for AI Design Systems

You have probably seen the pattern if you have built anything with an AI tool: the agent writes working code, and the output does not match your brand. The colors are close but not yours, the type is a font you would never pick, and every screen makes the same decisions over again. DESIGN.md is Google's answer to that problem — an open-source file format for describing a visual identity to a coding agent. It is a single Markdown file that combines machine-readable design tokens with human-readable rules, so an agent like Claude Code or Cursor reads your palette, typography, and constraints once and generates every screen against them. This guide explains what DESIGN.md is, how the format works, what the tooling does, and how it differs from the skills and tokens it is often confused with.

## TL;DR

- **DESIGN.md is an open file format, originally built for Google Stitch and now open-sourced, that describes a visual identity to AI coding agents.**
- **It has two layers in one file**: YAML front matter carries machine-readable design tokens, and Markdown prose below carries the reasoning and the rules — the "why" and the "never do this."
- **Sections follow a fixed order** — Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, and Do's and Don'ts — so any agent parses an unfamiliar file the same way.
- **An official CLI lints, diffs, and exports**: it validates structure, checks WCAG contrast ratios, compares token changes, and converts tokens to Tailwind, CSS, or the W3C DTCG format.
- **It is a context file, not a skill**: skills orchestrate behavior, while DESIGN.md informs judgment — which is why the two work together rather than replacing each other.

DESIGN.md is the same idea as a CLAUDE.md or an AGENTS.md, but for design: a standing reference the agent reads every session, so "what the product looks like" stops being re-described and starts being a file. Its adoption has been notable for a format with no executable code — the repository reached roughly 18,700 stars in its first two months, and third-party directories like designmd.app now index hundreds of documented design systems you can drop into any project.

## 1. Where DESIGN.md came from

DESIGN.md grew out of Google's Stitch — the AI design tool where Google Labs first experimented with giving generated UI a persistent visual identity. The format proved valuable enough that Google open-sourced the draft specification, in the company's own words, "so it can be used across any tool or platform." David East, the Google engineer behind it, describes it plainly: a text file that describes a visual identity and gives agents a persistent, structured understanding of a design system — the colors and what they are for, the typography and why you are using it, and the rules around how it all fits together.

What made it a standard rather than a Stitch feature is that it is tool-agnostic. The <a href="https://github.com/google-labs-code/design.md" rel="nofollow noopener">specification and CLI</a> live on GitHub under an open license, the format deliberately follows the W3C Design Tokens structure rather than reinventing it, and any agent that can read Markdown can consume the file. The community ecosystem grew quickly around it — the awesome-design-md collection passed 64,000 stars, and designmd.app built a directory of documented design systems, each a ready-made DESIGN.md you can copy into a project. The pattern it formalizes — one file at the project root that encodes visual identity — is the same instinct behind the [frontend-design skill](/blog/what-is-frontend-design-skill) and the [Figma design token guide](/blog/figma-design-tokens), but as a file rather than a behavior or a tool feature.

## 2. The two layers: tokens and rationale

A DESIGN.md file combines two kinds of content because agents need both. The **YAML front matter** at the top carries machine-readable design tokens — exact values for colors, typography, rounded corners, spacing, and component properties. The **Markdown body** below carries the human-readable rationale — why those values were chosen, what constraints they encode, and what the UI must never do. The tokens are the normative values; the prose tells the agent how to apply them.

The official example shows the pattern in miniature. The front matter defines a palette — `#1A1C1E` for primary ink, `#B8422E` for tertiary accent — a type scale in Public Sans with a Space Grotesk label style, and spacing and radius units. The body then explains what the tokens mean in use: "deep ink for headlines and core text," "Boston Clay — the sole driver for interaction," "warm limestone foundation, softer than pure white." An agent reading the file produces a UI with deep ink headlines, a limestone background, and Boston Clay call-to-action buttons — and, just as important, it knows not to use Boston Clay for body text, because the prose says so.

The two layers solve the two failure modes of a design system handed to an AI. A bare `tokens.json` gives exact values but no rules — it cannot express "use primary only for the main CTA." A prose-only style guide gives rules but no exact values — the agent must infer the hex codes. DESIGN.md keeps both in one file, in context of one another, which is precisely why the [best AI design skills comparison](/blog/best-ai-design-skills) and the [design token guide](/blog/figma-design-tokens) treat it as the contract layer that ties the workflow together.

## 3. The section order and what it encodes

Sections use standard `##` headings, and they must appear in a fixed order. The order is Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, and Do's and Don'ts. Sections can be omitted, but any section that appears must appear in that sequence — a rule the linter enforces, because it is what lets an agent parse a file it has never seen without ambiguity.

The order is a design argument in itself. Overview establishes the personality first — the same way a human designer frames the brief. Colors and Typography come next because they are the identity carriers. Layout, Elevation, and Shapes progressively define space, depth, and form. Components then map those values onto real interface pieces — a button token references `{colors.tertiary}` for its background and `{rounded.sm}` for its corners, using the format's token-reference syntax to point at values defined higher in the file. Do's and Don'ts closes with the judgment rules that tokens cannot express: no purple gradients, no centered body text, no generic SaaS grid.

The token schema is deliberately aligned with the wider ecosystem. Color accepts any CSS color format, from hex to `oklch()`. Dimensions carry units. Typography is a structured object with font family, size, weight, line height, and letter spacing. Component tokens map a name to sub-properties like `backgroundColor`, `textColor`, `padding`, and `rounded`, with hover and active variants expressed as separate named entries. Because the schema draws from the W3C Design Tokens Format, a DESIGN.md reads naturally to anyone familiar with Figma variables or Tailwind themes — and it exports into those formats when a build pipeline needs them.

## 4. The CLI: lint, diff, and export

The format ships with an official command-line tool that turns the file from documentation into a checkable contract. The `@google/design.md` package provides four commands. **Lint** validates a file against the spec — it catches broken token references (a `{colors.primary}` that points nowhere), missing primary or typography tokens, out-of-order sections, and even checks WCAG contrast ratios between component text and background pairs, reporting each finding with a severity. **Diff** compares two versions of a design system and reports token-level changes — which colors were added, removed, or modified — and flags regressions where the "after" file has more errors or warnings than the "before." **Export** converts tokens to the formats a project actually consumes: a Tailwind theme config, a Tailwind v4 CSS `@theme` block, or a W3C DTCG `tokens.json`. **Spec** outputs the format specification itself, which is how an agent can inject the rules into its own context.

The accessibility check is worth calling out specifically. Contrast validation is part of the linter's default rules, not an optional add-on — a component pair that fails WCAG AA appears as a warning with the measured ratio. The practical effect is that accessibility becomes a property of the design system rather than a post-hoc audit: the same file that tells the agent the colors also tells it whether those colors are readable in the combinations the agent will generate. David East's walkthrough of the format highlights this as a core design decision — agents tend to ignore contrast unless they are forced to consider it, and the format forces it at the source.

The Windows caveat is a small real-world detail worth knowing: the CLI binary is named `design.md`, which collides with the Windows Markdown file association, so on Windows you invoke the dot-free alias — `npx -p @google/design.md designmd lint DESIGN.md` — instead. It resolves to the same entrypoint; it just avoids the filename clash. This kind of tooling polish is exactly why the format's proponents argue it will outlast the tools that created it — a file every agent can read is more durable than any single product's feature set.

## 5. DESIGN.md versus skills and tokens

Three concepts in this series are easy to conflate, and the boundary is worth thirty seconds of your time. **Design tokens** are the values — named slots for colors, spacing, and type, as covered in the [Figma design token guide](/blog/figma-design-tokens). **Skills** are behavior — instructions the agent loads and executes, like the [frontend-design skill](/blog/what-is-frontend-design-skill) that forces an aesthetic plan before code. **DESIGN.md** is the contract — a context file the agent reads and applies throughout a session. Tokens answer "what are the values," skills answer "how should the agent behave," and DESIGN.md answers "what does our product look like and why."

The relationship between the three is complementary, and the confusion usually comes from thinking DESIGN.md replaces one of the others. It does not replace tokens — it *contains* them, in a format that also carries the rules tokens cannot express. It does not replace skills — a skill orchestrates behavior and can even reference a DESIGN.md as its source of truth, which is exactly the pattern the [design skills comparison](/blog/best-ai-design-skills) describes as "the skill proposes, the contract enforces." A DESIGN.md is static reference material; skills are procedural instructions; and the strongest workflow uses all three, with the file as the single source of truth that outranks whatever the skill defaults to when they conflict.

For a non-developer, the format is approachable precisely because it is a file you can read. A `DESIGN.md` written in plain language — "our palette is deep ink on warm limestone, with Boston Clay reserved for actions; never use purple gradients" — is something you can write and review yourself, and then let any agent you use build against it. The same content, expressed as a pile of tokens or a skill configuration, would be out of reach. That accessibility is the quiet reason the format has spread as fast as it has.

## Conclusion

DESIGN.md is Google's open file format for telling an AI agent what your product looks like — machine-readable tokens and human-readable rules in one Markdown file, in a fixed section order, validated by an official CLI that checks structure, contrast, and token drift. It grew out of Stitch, became an open specification, and has been adopted widely enough that directories of ready-made design systems now exist for it.

The format is the contract layer that ties the rest of the workflow together: [design skills](/blog/best-ai-design-skills) supply behavior, [Figma design tokens](/blog/figma-design-tokens) supply values, and DESIGN.md supplies the persistent identity that outranks both. If you are building with an AI tool and tired of re-describing your brand, the highest-leverage move is to write the one-page file — palette, type, spacing, and the three things you refuse to let the AI default to — and let every generation read from it. And if you would rather not maintain files at all, a prompt-first generator like [MeDo Components](/components) encodes the same consistency into the prompts themselves, so the same description renders the same themed component in any builder.

## Frequently asked questions

### Is DESIGN.md a Google product?

DESIGN.md is an open file format maintained by Google Labs, released under an open license as a draft specification. It grew out of Google's Stitch tool but is deliberately tool-agnostic — any agent or platform can read it, which is the point of open-sourcing it.

### Do I need to install anything to use DESIGN.md?

No. A DESIGN.md is a plain Markdown file you place at the project root, and agents that read context files pick it up without configuration. The official CLI is optional — you use it when you want to lint, diff, or export the tokens.

### How is DESIGN.md different from CLAUDE.md?

Both are context files the agent reads every session, but they serve different concerns. CLAUDE.md describes project setup and coding conventions; DESIGN.md describes the visual identity — palette, typography, spacing, and design rules. They sit side by side at the project root and complement each other.

### Can DESIGN.md replace design tokens or a Figma file?

It does not replace them — it formalizes them. Tokens can live inside a DESIGN.md's front matter, and Figma variables can be exported to the same W3C DTCG format the tool outputs. The difference is that DESIGN.md adds the rules and reasoning that a bare token file cannot express.

### Will an AI agent actually follow DESIGN.md?

It follows it when the file is the standing instruction, which is the same mechanism as CLAUDE.md or AGENTS.md. The more useful guarantee is the linter: it catches broken references and contrast failures before generation, so the contract stays valid even when the agent iterates.

### Does DESIGN.md work for mobile apps?

The format describes visual identity, which is platform-agnostic. The same tokens and rules that drive a web interface export to the Swift, Kotlin, or Flutter formats a mobile app consumes, and the [guide to building a mobile app with AI](/blog/how-to-build-mobile-app-with-ai) covers where design contracts sit in a native build.
