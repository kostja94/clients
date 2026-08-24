---
title: "GPT-5.6 in Floatboat — Built-In Sol, Terra, Luna"
description: "GPT-5.6 Sol, Terra, and Luna are already built into Floatboat with no API key needed. How each tier maps to the calendar events your agents already run."
slug: "gpt-5-6-floatboat"
date: 2026-07-12
author: "Floatboat Team"
category: "Product"
---

## TL;DR

- GPT-5.6 Sol, Terra, and Luna are **already built into Floatboat** — no API keys to configure, no model routing to set up, no external accounts. They appear alongside DeepSeek, Claude, Gemini, MiniMax, Kimi, and GLM in your agent workspace.
- Sol handles the hardest calendar-driven agent tasks: complex meeting preparation with multi-document synthesis, long-horizon deliverable drafting, and multi-step agent orchestration. Luna handles the high-volume work: event classification, action item extraction, and content routing. Terra sits between them as the everyday default.
- The tiered pricing — Sol at $5/$30, Terra at $2.50/$15, Luna at $1/$6 per million tokens — means a solopreneur running 30–50 agent tasks per week can match model cost to task complexity without thinking about which model to call.
- This article maps each GPT-5.6 tier to the calendar events your agents already handle, so you know which one to reach for — or let Floatboat's Auto Mode decide for you.

---

## 1. Why Built-In Matters — No API Keys, No Routing, No Decision Fatigue

Most AI tools that offer multiple models make you earn the privilege. You find the API key on a settings page. You paste it into a configuration field. You decide which model should handle which task, write a routing layer, and hope you picked right. If a better model ships next month, you repeat the process.

That workflow assumes the person running the agent is also the person managing the infrastructure. For solopreneurs — the people Floatboat is built for — that assumption doesn't hold. You don't have time to be an MLOps engineer. You have meetings to prepare for, deliverables to produce, and follow-ups to send. The model is a means to the work, not the work itself.

When OpenAI released GPT-5.6 Sol, Terra, and Luna to general availability on July 9, 2026, Floatboat made them available inside your calendar-driven agent workspace the same day — not as a configurable integration, but as a built-in model option alongside the existing model roster, per [OpenAI](https://openai.com/index/gpt-5-6/). No deployment pipeline. No API key rotation. No routing logic to write. Open the agent workspace, select the tier for the event type, and the model runs. If you don't want to think about which tier to use, Auto Mode handles the selection based on the event's complexity, context, and timing.

The practical difference is this: on platforms where GPT-5.6 requires integration, the decision about which tier to use is a technical choice you make before you start working. On Floatboat, it's an operational choice you make while you're already running. One keeps you in setup mode. The other keeps you in flow.

---

## 2. Sol, Terra, and Luna — Which One Fits Which Calendar Event

The three GPT-5.6 tiers map naturally to the three tiers of calendar events that every solopreneur deals with. The fit is not accidental — OpenAI designed Sol, Terra, and Luna as capability tiers rather than speed tiers, and calendar-driven agent pipelines happen to need exactly this capability hierarchy.

### 2.1 Sol — The Tier for Events That Require Real Work

Sol is the flagship tier at $5 per million input tokens and $30 per million output tokens. On Terminal-Bench 2.1, which tests multi-step command-line agent workflows, Sol scores 88.8% — and Sol Ultra reaches 91.9% using subagent orchestration across parallel workstreams, per [OpenAI's Terminal-Bench 2.1 results](https://openai.com/index/gpt-5-6/). On the Artificial Analysis Coding Agent Index, Sol with max reasoning sets a new state of the art at 80, 2.8 points above Claude Fable 5, while using less than half the output tokens and costing about one-third less.

In calendar-driven agent terms, Sol is the tier for events where the output quality determines whether the meeting or deadline succeeds or fails. A client strategy review that requires reading three previous meeting notes, cross-referencing the CRM for recent interactions, and generating a structured brief with prioritized talking points — that is a Sol task. A project retrospective where the agent needs to synthesize feedback from multiple stakeholders and produce a findings document with actionable recommendations — that is a Sol task. Any calendar event where you would spend more than 30 minutes preparing manually is a candidate for Sol.

Sol also unlocks the `ultra` mode, which coordinates multiple sub-agents in parallel. For a complex meeting brief, this means the agent can pull last meeting's notes, check the CRM, scan recent email threads, and draft the talking points simultaneously rather than sequentially. The result arrives faster, and the parallel structure means each sub-task gets focused model attention rather than competing for the same reasoning budget.

### 2.2 Terra — The Everyday Default for Routine Agent Work

Terra is the balanced tier at $2.50 per million input tokens and $15 per million output tokens — exactly half the cost of Sol while delivering performance competitive with GPT-5.5, which was OpenAI's flagship model just two months ago. On Terminal-Bench 2.1, Terra scores 82.5%, which puts it ahead of Claude Opus 4.8 (78.9%) and effectively ties Claude Fable 5 (83.4%), per [OpenAI](https://openai.com/index/gpt-5-6/).

For calendar-driven agents, Terra is the sensible default for the majority of events. Standard follow-up drafts after a client call, daily status summaries that compile updates from multiple sources, calendar conflict resolution that checks availability across your tools, routine document summarization — none of these need Sol-level reasoning, and running them on Sol would be more expensive without delivering meaningfully better output. Terra gives you GPT-5.5-class capability at roughly the cost that GPT-5.4 would have cost you three months ago.

The typical solopreneur workflow benefits most from Terra as the default tier. If you run 30 agent tasks per week, roughly 20–25 of them will be Terra-level work: well-defined, bounded in scope, and cheap to verify. Setting Terra as the default for your agent workspace means those tasks run at the lowest cost that still delivers reliable output, without requiring a per-event decision.

### 2.3 Luna — Fast Classification and Routing at Near-Zero Cost

Luna is the fastest and cheapest tier at $1 per million input tokens and $6 per million output tokens. The surprising benchmark result is that Luna scores 84.3% on Terminal-Bench 2.1 — matching Claude Mythos 5, a model that was considered frontier-level before its government-mandated restrictions, per [OpenAI](https://openai.com/index/gpt-5-6/).

In a calendar-driven agent setup, Luna handles the invisible work that runs on every new calendar event without you noticing. When a new event appears on your calendar, something needs to classify it: is this a client meeting, an internal sync, a deadline, or a reminder? That classification determines which agent pipeline should handle it, what preparation is needed, and whether it needs human attention at all. Luna can run that classification pass on every incoming event at negligible cost. It can also extract action items from meeting transcripts, categorize email threads by urgency, and decide whether an event needs to be escalated to a Terra or Sol agent pipeline. The AI Scheduling <a href="/blog/ai-scheduling-agent">scheduling agent</a> ecosystem benefits from this kind of cheap preprocessing layer — it means Sol and Terra only touch events that genuinely need their capability, and the high-volume routine work never reaches them.

For a solopreneur receiving 50–100 calendar events per month, the cost of running Luna on every one is trivial — roughly $1–2 in token costs for a month of classification and routing. The alternative, which is manually triaging every event, costs attention instead of money. Attention is more expensive.

---

## 3. What It Looks Like in Practice — Calendar Events Mapping to Tiers

The framework above maps to real calendar events in a way that becomes intuitive after a few uses. Here are the common patterns.

**A client quarterly review** arriving on your calendar triggers a Sol agent pipeline. The agent reads the previous quarter's notes from the event workspace, pulls recent client communications from your email, cross-references the CRM for open items, and generates a structured brief with a status summary, talking points, and identified risks. If Sol Ultra is enabled, these sub-tasks run in parallel and the brief arrives in minutes rather than tens of minutes. The result is preparation that would have taken an hour of manual work, delivered before the meeting starts.

**A standard weekly team sync** routes to Terra. The agent scans the past week's project updates, identifies blockers, and drafts a one-page status summary. It checks your calendar for scheduling conflicts in the coming week and flags any that need resolution. The entire pipeline runs in the background and the output appears in your agent workspace before the sync begins. The cost per event is roughly one-third of what it would be on Sol, and the output quality is indistinguishable for this level of task.

**A new event appearing on your calendar** — a meeting invite from someone you haven't worked with before — triggers Luna. The agent classifies the event type, checks whether you have existing context with this contact, and routes it to the appropriate pipeline: a Terra agent for standard preparation if it's a client meeting, or a Sol agent if the meeting description suggests high-stakes content. Luna does this in seconds at a cost measured in fractions of a cent. Without this layer, every event would need manual triage or would default to an expensive model for simple classification.

The <a href="/blog/what-is-agentic-calendar">agentic calendar paradigm</a> works best when each layer handles what it is best at rather than pushing everything to the most capable model. Built-in GPT-5.6 tiers make this structure available without any configuration overhead.

---

## 4. What Different Tier Choices Cost — Real Numbers for Solo Operators

The cost difference between tiers matters most when agents run continuously rather than on-demand. A solopreneur running calendar-driven agents for client meetings, follow-ups, and deadline tracking will accumulate token usage steadily. The numbers below show what different tier strategies cost per month at moderate usage (roughly 50 agent-driven events, 8 million input tokens, 1.5 million output tokens).

| Strategy | Monthly cost | Notes |
|----------|-------------|-------|
| All tasks on Sol | ~$85 | Maximum capability, premium cost |
| All tasks on Terra | ~$43 | Half the cost, GPT-5.5-class output |
| All tasks on Luna | ~$17 | Fast and cheap, misses complex reasoning |
| **Luna+Terra combo** (recommended default) | **~$40** | Luna for routing + Terra for daily work |
| **Full tier stack** (Sol for complex + Terra for daily + Luna for routing) | **~$55** | Covers all event types efficiently |

The recommended full-tier stack — Sol for the handful of high-stakes events each month, Terra for the daily routine, Luna for always-on classification — comes to roughly $55 per month for a moderate-usage solopreneur. At GPT-5.5 pricing, running the same workload entirely on the flagship model would have cost about $85. The tiered approach saves roughly 35% while actually improving output quality on the events that matter most, because Sol handles the hard cases instead of a single model doing everything.

Floatboat's built-in prompt caching with GPT-5.6's redesigned cache system — 90% discount on cached reads and a 30-minute minimum cache lifetime — reduces these numbers further for users running recurring agent pipelines with stable system prompts, per [OpenAI](https://openai.com/index/gpt-5-6/).

---

## 5. Getting Started — Your First Calendar Agent with GPT-5.6

If you already use Floatboat, GPT-5.6 is available now. Open any agent workspace in the desktop app. When selecting the model for a pipeline or event, you will see GPT-5.6 Sol, Terra, and Luna listed alongside the existing model options — no different from selecting DeepSeek or Claude, except that no API key is needed. For users who prefer not to choose, Auto Mode routes tasks to the appropriate GPT-5.6 tier based on the event's complexity, context length, and timing.

If you are new to Floatboat, the setup is: download the desktop app, connect your calendar, and create your first agent pipeline. GPT-5.6 is available from the first agent you configure. There is no separate integration step, no API key to provision, and no model routing layer to build. The model selection appears in the agent workspace alongside the other built-in models. For the first few weeks, setting the agent to Terra as the default and letting Sol handle the occasional complex event is a safe starting point that keeps costs predictable while you explore the capability range.

The broader GPT-5.6 release also brought **ChatGPT Work** — an agent that gathers context across connected apps and files to create documents, spreadsheets, and presentations — alongside the merger of **Codex** into the ChatGPT desktop app, as reported by [Axios](https://www.axios.com/2026/07/09/ai-openai-gpt-release). On Floatboat, the same GPT-5.6 models power your calendar agents without needing to navigate a separate code environment or work app — the models are embedded directly where your calendar events live.

For a deeper understanding of how Sol, Terra, and Luna compare on benchmarks, pricing, and safety evaluations, see the full <a href="/blog/gpt-5-6-sol-terra-luna">GPT-5.6 model family overview</a>. If you want to understand the calendar-driven paradigm that makes tiered agents useful, the <a href="/blog/what-is-agentic-calendar">agentic calendar explanation</a> covers the category from the ground up.

---

## 6. Conclusion

The interesting thing about GPT-5.6 being built into Floatboat is not the technical integration — that part is invisible to users. It is that the three-tier design aligns with how calendar-driven agents actually work. Sol, Terra, and Luna map to real differences in calendar events: the client review that needs deep synthesis, the weekly sync that needs reliable output at low cost, and the classification pass that runs on every event and needs to be nearly free. When the model family matches the work structure, choosing the right tier stops being a configuration decision and becomes a natural part of how you run your day. That is the shift — not from one model to three, but from managing models to managing work.

---

## FAQ

### Do I need an OpenAI API key to use GPT-5.6 in Floatboat?

No. GPT-5.6 Sol, Terra, and Luna are built into Floatboat with zero configuration. You do not need to provision an API key, set up a billing account with OpenAI, or configure a routing layer. The models appear in your agent workspace automatically alongside DeepSeek, Claude, Gemini, MiniMax, Kimi, and GLM.

### Does Floatboat automatically switch between Sol, Terra, and Luna based on the task?

Auto Mode routes tasks to the appropriate GPT-5.6 tier based on event complexity, context length, and timing. You can also select a specific tier for each agent pipeline if you prefer manual control. The default configuration uses Terra as the baseline, which handles most routine agent work efficiently.

### Can I use GPT-5.6 Sol Ultra mode in Floatboat?

Sol Ultra mode — which coordinates multiple sub-agents across parallel workstreams — is available through Sol-tier model selection for complex agent pipelines. It is best suited for events requiring multi-document synthesis, such as client meeting preparation with cross-referenced research or deliverable generation with multiple interdependent outputs.

### What happens when OpenAI releases the next GPT generation?

When OpenAI releases the next model generation, Floatboat follows the same pattern as this release — built-in availability without configuration steps. The Sol, Terra, and Luna naming convention is designed as a durable capability tier that can advance on its own schedule, which means the tier names will remain stable even as the underlying model improves.

### How do I know which tier to use for a specific calendar event?

Start with Terra as the default. For complex events — client reviews, project retrospectives, high-stakes meetings — switch to Sol. For high-volume routine events — recurring status updates, standard follow-ups, event triage — use Luna. After two to three weeks of use, the pattern becomes intuitive. If you prefer not to decide, Auto Mode handles the selection.

### How much does running GPT-5.6 agents in Floatboat cost per month?

At moderate usage — roughly 50 agent-driven events, 8 million input tokens, and 1.5 million output tokens per month — running everything on Sol costs about $85, everything on Terra about $43, and everything on Luna about $17. The recommended full tier stack (Sol for high-stakes events, Terra for daily routine, Luna for classification) comes to roughly $55 — about 35% less than running the same workload on a single flagship model, while delivering better output on the events that matter most.
