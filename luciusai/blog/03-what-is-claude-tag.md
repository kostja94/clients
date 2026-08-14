---
title: "What Is Claude Tag? — Anthropic's AI Teammate Inside Slack"
description: "What Claude Tag is, how @Claude works in Slack as a shared AI teammate, and how it differs from Slack AI, Cowork, and community bots."
slug: "what-is-claude-tag"
date: 2026-07-27
author: "Lucius AI Team"
category: "Research"
---

## TL;DR

- **Claude Tag** is Anthropic's Slack-native AI teammate: anyone in a configured channel can tag `@Claude`, hand it a task, and watch it plan and execute work using organization-provisioned tools—visible to the whole channel, not locked in a private chat.
- It runs under an **organization-level agent identity** (not each person's Claude account), keeps channel memory across days, can work asynchronously for hours or days, and—when ambient mode is enabled—can follow up without being tagged again.
- Claude Tag launched in beta on June 23, 2026 for Claude Team and Enterprise customers, runs on Claude Opus 4.8, and replaces the older per-user Claude in Slack app (migration deadline August 3, 2026).
- It is built for **internal team execution** in Slack—engineering, ops, metrics, ticket triage—not for Discord/Telegram community support or multi-platform member identity.
- For how Claude Tag compares to other AI teammates and when a community-native option fits better, see our companion guide to the [best Claude Tag alternatives](/blog/best-claude-tag-alternatives).

---

## 1. Why Teams Are Talking About Claude Tag

For most of the last few years, "AI in Slack" meant a bot you pinged for a summary, a draft, or a search result. Useful, but still single-player: your thread, your context, your private session. The work of turning that answer into a pull request, a metrics pull, or a multi-step investigation stayed with humans.

Anthropic's answer is to stop treating Claude as a chat window bolted onto Slack and start treating it as a **shared teammate** that already lives where the team works. On June 23, 2026, the company [introduced Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) as a beta for Claude Team and Enterprise customers: grant Claude access to selected channels and tools, then anyone can `@Claude` and delegate real work while they move on.

That framing matters because it changes the unit of collaboration. Instead of "I asked the AI privately," the pattern becomes "we handed work to the same Claude everyone can see, steer, and continue." Anthropic reports that tagging `@Claude` is now one of the main ways work gets done inside the company, and that 65% of its product team's code is created by an internal version of Claude Tag—a claim that sits in the launch announcement and signals how seriously the company takes the multiplayer agent pattern. [Source: https://www.anthropic.com/news/introducing-claude-tag]

Community and customer-success teams should still pay attention, even if they never open Claude Tag. The product popularizes a category language—"AI teammate"—that buyers will bring into Discord, Telegram, and Slack Connect conversations. Understanding what Claude Tag *is* (and what it is not) keeps those evaluations honest.

There is also a timing reason the conversation spiked in mid-2026. Anthropic did not invent Slack bots, and it did not invent agentic coding. What it did was merge a familiar `@` mention with a stronger claim: one shared agent, scoped tools, persistent channel memory, and asynchronous follow-through. Press coverage framed Tag as an always-on coworker that learns from the channels it can see. That story is exciting for internal productivity leaders and slightly misleading for community operators who hear "teammate" and picture a Discord mod that never sleeps. Separating those reactions is the point of a clear definition.

---

## 2. What Is Claude Tag — The Core Definition

Claude Tag is Claude working inside your team's Slack channels under a shared, admin-provisioned identity. An organization Owner connects tools, data, and repositories; scopes which channels Claude can enter; and sets spend limits. After that, people in those channels tag `@Claude` with plain-language tasks. Claude breaks the work into stages, uses the tools it has been given, and posts results back into the thread for everyone to see.

Anthropic's help center puts the same idea more tightly: tag `@Claude` into a conversation and it takes on real work using your organization's tools and the shared context around it; it works under its own identity, remembers relevant channel information, and can follow up on its own. [Source: https://support.claude.com/en/articles/15594475-what-is-claude-tag]

Three design choices define the product more than any single feature list:

**One Claude per channel, not one Claude per person.** Within a given Slack channel there is a single Claude that interacts with everyone. Anyone can see what it is working on and pick up where the last person left off. That is the multiplayer property Anthropic emphasizes in the launch post—and the main reason Claude Tag feels more like a teammate than a private assistant.

**Organization identity, not personal connectors.** Channel work runs on credentials and tool access an admin sets for the agent. Direct messages to Claude still use a person's own claude.ai account and connectors; channel tagging is billed to the organization. Mixing those two surfaces is a common source of confusion during migration.

**Async execution, not only instant replies.** You can assign a task and leave. Claude Tag can pursue work over hours or days, schedule follow-ups for itself, and—when ambient behavior is enabled—proactively flag stalled threads or relevant updates from channels and tools it can reach.

Put together: Claude Tag is an **internal, Slack-first, agentic teammate**—shared, tool-connected, and built for delegated execution—not a FAQ bot and not a personal desktop agent.

---

## 3. How Claude Tag Works in Slack

Operationally, Claude Tag starts with admin setup, not individual installs. A Primary Owner or Owner pairs Claude Tag with the Slack workspace, provisions the agent's identity, connects organization tools and repositories, chooses channels, and sets monthly spend limits. Anthropic's getting-started path is deliberately short for end users: once a channel is ready, teammates do not configure anything themselves. [Source: https://support.claude.com/en/articles/15594475-what-is-claude-tag]

When someone tags `@Claude` with a task, a working session starts for that thread. Claude reads the conversation context, plans stages, runs in Anthropic-hosted infrastructure using allowed tools, and posts progress and results back into the thread. The older Claude in Slack experience answered more like a reactive assistant tied to each user's account. Claude Tag replaces that model: same `@Claude` handle in many workspaces, different identity and memory model underneath. Anthropic has set August 3, 2026 as the switchover date for the earlier Claude in Slack app. [Source: https://support.claude.com/en/articles/15594475-what-is-claude-tag]

Memory and scoping are part of the security story, not just convenience. Claude builds context from the channels it is allowed into. Admins can create separate Claude identities for different uses so that memories and tool access stay scoped—for example, a sales-scoped Claude should not leak sales tools or memories into an engineering channel. Anthropic also notes that Claude does not report from private channels it is not permitted to use.

Ambient mode is optional and consequential. With it enabled, Claude can check in without a fresh `@` mention—surfacing updates, flagging quiet threads, or pulling relevant signals from connected systems. Teams that want a quieter teammate leave ambient off and keep Claude Tag in a pure "tag to delegate" mode. Either way, administrators can review activity logs of what Claude did and who requested each task.

If you have used Claude Code or Cowork, the task loop will feel familiar: describe an outcome, Claude plans and executes with tools, then returns an artifact. The difference is location and audience. Tag runs in Slack, in public view of the channel, under org credentials. Cowork and Code remain personal or developer-centered surfaces for individual sessions.

Day-to-day usage is intentionally low-friction once provisioning is done. A teammate can paste `@Claude` mid-thread on a messy discussion, ask for a summary plus next actions, or hand over a longer task—"pull last week's funnel numbers and draft a note for the channel"—without opening a separate product window. Because the session is tied to the thread, the next person on shift inherits both the human conversation and Claude's progress. That inheritance is what makes Tag feel operational rather than ornamental: the agent is part of the team's shared work surface, not a side quest each person runs alone.

Governance remains the constraint that makes the model viable for enterprises. Spend caps at org and channel level, activity logs that show who requested each task, and scoped identities for different departments are not optional polish. They are how Anthropic answers the multiplayer permission problem: when three people steer one agent, you cannot safely borrow any one human's personal OAuth for every tool call. Agent identity—admin-defined access for the agent itself—is the access model behind Tag's channel work.

---

## 4. Claude Tag vs Related Concepts

Buyers often collapse every Slack AI into one bucket. Separating Claude Tag from its neighbors prevents bad product choices.

| Concept | What it is | How it differs from Claude Tag |
|---------|------------|--------------------------------|
| **Legacy Claude in Slack** | Earlier per-user Slack app | Personal identity, little shared memory; retiring August 3, 2026 in favor of Tag |
| **Slack AI / Slackbot** | Native Slack productivity layer | Strong at search, summaries, and catch-up; not an org-identity agent that executes multi-step external work the way Tag does |
| **Claude Code** | Developer agent (terminal / IDE / web) | Built for software engineering sessions; Tag brings a related agentic pattern into shared Slack channels |
| **Claude Cowork** | Personal agent for knowledge-work deliverables | User-initiated desktop/web sessions for files and apps; not a shared channel teammate |
| **Community AI bots** | Discord/Telegram/Slack bots for member support | Grounded FAQ answer, moderation, onboarding, human handoff across community surfaces—not Slack-only internal execution |

The important boundary for community operators is the last row. Claude Tag can help with internal support tickets when those tickets live in Slack and tools are connected, and Anthropic even mentions support workflows in its launch narrative. That still does not make Claude Tag a **community-native** system: it does not unify member identity across Discord and Telegram, it is not designed as a moderation and onboarding stack for public communities, and it is gated to Claude Team/Enterprise with Slack as the first home.

A second boundary is "AI teammate" as marketing language. Claude Tag genuinely earns the teammate metaphor for internal Slack work: shared identity, visible tasks, handoff between humans mid-thread. Other products use the same phrase for very different jobs—knowledge search, ticket deflection, Discord moderation, or personal desktop agents. When someone says they need an AI teammate, ask which audience the teammate serves and which platforms it must live on before comparing feature lists.

For teams that care about resolving repeat questions where members already gather—and about keeping humans in the loop when answers are incomplete—patterns like [call deflection](/blog/what-is-call-deflection) and [community support automation](/blog/automate-customer-support-in-community) describe a different problem than Tag's internal delegation loop.

---

## 5. Where Community AI Teammates Fit

Claude Tag pushes the industry toward agents that sit in the channel, remember context, and do work. Community teams feel that pressure too: members expect fast answers in Discord, Telegram, and Slack Connect, not a ticket form three clicks away. The mistake is assuming the same product shape solves both problems.

An **internal agentic teammate** (Claude Tag's center of gravity) optimizes for employees who share a workspace, admins who provision org tools, and tasks that produce artifacts—code changes, analyses, follow-ups. A **community AI teammate** optimizes for members and customers who ask product questions, need consistent answers grounded in docs, and occasionally need a human handoff with full context. The second shape also tends to span multiple platforms and to treat knowledge freshness, spam judgment, and onboarding as first-class work—not as afterthoughts.

Lucius is built for that second shape: a cross-platform AI teammate for community that auto-answers from your knowledge, filters spam with contextual judgment, personalizes onboarding, and keeps a self-updating knowledge base—with a Connect → Detect → Handoff workflow when the bot should stop and escalate. It is not a substitute for Claude Tag's Slack-native coding and tool-execution loop, and Claude Tag is not a substitute for multi-platform community operations.

If you are evaluating Tag because your team lives in Slack and needs shared agentic execution, stay in that lane and compare like-for-like Slack coworkers. If you are evaluating Tag because "AI teammate" showed up in a budget conversation about Discord or customer communities, widen the lens. Our [Claude Tag alternatives](/blog/best-claude-tag-alternatives) roundup uses that split as the primary decision frame.

---

## 6. Conclusion

Claude Tag is Anthropic's bet that the most useful place for Claude is not another chat tab—it is a shared seat in Slack, with its own identity, memory, and permission to act. Tag `@Claude`, hand off a multi-step task, and the channel watches the work happen. That is a real category move for internal collaboration.

It is also a product with clear edges: Team and Enterprise beta, Slack-first, org-billed channel work, and a design center in employee execution rather than community member support. Treat those edges as features of the definition, not as footnotes.

If you need the mechanism spelled out for stakeholders, this article is the canonical overview. If you need to choose among Tag-like coworkers, community teammates, and support agents, continue to the alternatives guide—and match the teammate to the audience, not only to the model name.

Ready to try a community-native AI teammate across Discord, Telegram, and Slack? Start at [luciusai.com](https://luciusai.com/).

---

## FAQ

### Is Claude Tag the same as Claude in Slack?

No. Claude Tag is the next-generation experience that replaces the earlier per-user Claude in Slack app. The older app answered under individual accounts; Claude Tag uses a shared organization identity, channel memory, and stronger async/ambient behavior. Anthropic plans to switch remaining workspaces to the Tag experience on August 3, 2026. [Source: https://support.claude.com/en/articles/15594475-what-is-claude-tag]

### Who can use Claude Tag today?

Claude Tag is available in beta for Claude Team and Enterprise customers, with Slack as the initial surface. Individual Free or Pro users without a Team/Enterprise org cannot turn on channel Tag the same way. Direct messages to Claude in Slack still follow personal account rules and billing.

### Does Claude Tag replace Slack AI?

No. Slack's native AI features and Claude Tag solve different jobs. Slack AI is strong for summarizing and searching what already happened in Slack. Claude Tag is built to take delegated tasks, use connected tools, and produce work under an org-scoped agent identity. Many teams will run both.

### Is Claude Tag a good Discord community bot?

Not as a primary fit. Claude Tag is Slack-first and oriented toward internal teammates with admin-provisioned tools. Public Discord communities that need FAQ answering, moderation judgment, member onboarding, and cross-platform identity need a community AI teammate designed for those surfaces—not a Slack channel agent with a different job description.

### How is Claude Tag billed?

Channel tagging is billed to the organization (usage-based, with admin spend caps). Direct messages use the individual's Claude account. Anthropic has offered introductory launch credits to eligible Team and Enterprise orgs for Tag usage; treat credit amounts as promotional and verify in your admin console before budgeting. [Source: https://www.anthropic.com/news/introducing-claude-tag]

### How does Claude Tag remember context and what can it see?

Claude builds its memory from the channels admins allow it into, and it keeps channel context across days so a task continues where an earlier conversation left off. Admins can create separate Claude identities for different uses so memories and tool access stay scoped — a sales-scoped Claude shouldn't leak sales tools into an engineering channel. Claude does not report from private channels it isn't permitted to use, and administrators can review activity logs of what it did and who requested each task.
