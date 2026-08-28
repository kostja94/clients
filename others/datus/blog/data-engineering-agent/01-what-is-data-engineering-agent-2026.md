---
title: "What Is a Data Engineering Agent? Definition, Examples & Comparison"
description: "Data engineering agent definition and examples: platform agents, Claude Code, open-source frameworks, and how persistent context separates agents from copilots."
slug: "what-is-data-engineering-agent"
date: 2026-05-28
author: "Kostja"
category: "Data Engineering Agent"
secondaryCategory: "Research"
---

# What Is a Data Engineering Agent? Definition, Examples & Comparison

A data engineering agent turns natural-language intent into executable data work — SQL, pipelines, quality checks — against a real stack, with enough context to skip translating every column name by hand. As of August 2026, the label covers platform features, vertical SaaS tools, prompt personas, warehouse-native coding agents, and open-source frameworks — not one interchangeable product.

## TL;DR

- A **data engineering agent** turns natural-language intent into **executable data work** — SQL, transformations, pipelines, quality checks — against a **real stack**, with enough context to skip translating every column name by hand.
- Examples diverge on **environment lock-in**, **execution depth**, and especially **persistent context** — not on whether they can draft SQL once.
- **Platform-embedded** agents (BigQuery, Adobe) and **warehouse-native coding agents** (Snowflake Cortex Code, Databricks Genie Code) excel when your stack lives inside one vendor.
- **Prompt-as-agent** recipes (Claude Code subagent) excel for ad-hoc local work with no infrastructure setup.
- **Open-source frameworks** (Datus) target plural stacks and treat **context as the product** — Knowledge storage, feedback loops, and scoped delivery — not a chat session that resets every morning.

In practice, the four products competing for the label today are not the same thing: one is a cloud feature, one is a SaaS capability, one is an agent persona, and one is an open-source agent framework. Here is how to tell them apart.

## 1. Data engineering agent: a working definition

"Data engineering agent" is a phrase that started showing up in product launches around late 2024, and by 2026 four very different things wear the label: Google's <a href="https://docs.cloud.google.com/bigquery/docs/data-engineering-agent-pipelines" rel="nofollow noopener">BigQuery Data Engineering Agent</a>, Adobe's <a href="https://business.adobe.com/blog/unlock-your-datas-full-potential-with-adobe-data-engineering-agent" rel="nofollow noopener">Data Engineering Agent</a> inside Experience Platform, a community-maintained <a href="https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/categories/05-data-ai/data-engineer.md" rel="nofollow noopener">Claude Code "data-engineer" subagent</a>, and the open-source Datus project. Read their docs back-to-back and the surface promise sounds identical — "describe what you want, the agent builds it." Run them, and the experiences barely overlap.

Strip the marketing away and the useful working definition is narrower than any single vendor implies. A data engineering agent is software that does four things together:

1. **Understands intent in natural language** — a question, a goal, a half-written specification — instead of requiring a complete DDL or DAG up front.
2. **Produces executable data artifacts** — SQL queries, transformations, pipeline definitions, schema changes, test cases — not just prose explanations.
3. **Operates against a real stack** with credentials and side effects: a warehouse, a lakehouse, a catalog, an orchestrator. Agents that only suggest code in a chat window are copilots, not engineering agents.
4. **Carries reusable context across runs** — past queries, schema knowledge, metric definitions, business rules — so the second task is cheaper than the first.

That fourth point is where most of the disagreement hides, and the rest of this piece is mostly about it. A SQL copilot that forgets your metric definitions after every session fails the fourth test even if it writes brilliant one-off queries.

## 2. What every data engineering agent does

Before pulling them apart, it's worth being precise about what the four agents legitimately share. Each one will, in some form:

- **Translate natural language to SQL or pipeline code.** "Build me a daily revenue model joined to customer segments" is a valid input.
- **Inspect schema metadata** from a target system to ground its suggestions — column names, types, lineage where available.
- **Compose multi-step plans**: choose tables, draft a query, run it, react to errors, refine, and present a result.
- **Reduce repetitive engineering toil** — boilerplate joins, type casts, partition predicates, basic transformations.
- **Use an LLM as the planner**, not just as a text-generation endpoint, with at least one feedback step before the answer is returned.

If you stopped reading here, you would walk away believing "data engineering agent" is one product category. The differences only become obvious when you ask the boring questions: who is allowed to call it, what does it actually have access to, and what does it remember tomorrow?

## 3. A tour of today's data engineering agents

### Google BigQuery Data Engineering Agent

Google's offering is a managed capability inside BigQuery Studio and Dataform. It generates and edits pipeline code, suggests schema designs, and is wired to Google's Knowledge Catalog (formerly Dataplex) for grounding. Its strength is being absolutely native to its host: lineage, IAM, and billing all just work because everything happens inside one cloud. Its limit is the same fact — the agent is a feature *of* BigQuery, not a tool that travels with you. If your stack is Snowflake, Databricks, or anything on-premise, this agent is not the answer.

### Adobe Data Engineering Agent

Adobe's agent lives inside Adobe Experience Platform and targets a specific persona: customer-data engineers building audiences, schemas, and pipelines for marketing activation. It plans transformations, builds AEP data flows, and orchestrates work inside Adobe's own catalog. The framing is genuinely different from Google's — this is a vertical SaaS agent built for teams whose "warehouse" is AEP itself. Outside that world the product doesn't apply, and that is by design. (Note: Adobe's public materials describe the agent's capabilities in future-forward language — it is an announced product with an evolving GA timeline, not a multi-year GA product like BigQuery's agent.)

### Claude Code data-engineer subagent

The Claude Code variant is a persona configuration for Anthropic's Claude Code CLI agent — when loaded, it instructs Claude to act as a data engineer, designing pipelines, orchestration patterns, and Spark/Airflow-adjacent work against whatever files and credentials are visible in the local shell. It is the most stack-agnostic of the four: no warehouse lock-in, no platform dependency, just a terminal and an LLM. It is also the most ephemeral. Claude Code's tool-use architecture handles execution capably, but there is no dedicated context store for data artifacts, and session state does not persist between invocations in the way a data engineering team needs — schema knowledge, validated SQL, metric definitions, and business rules must be re-established or reloaded each time.

### Datus — the open-source data engineering agent

Datus is an open-source agent framework built around a persistent **Context Engine** and, as of the 0.3 product line, a structured **Knowledge** store — schema, semantic models, metrics, reference SQL, templates, and platform docs retrieved by meaning rather than stuffed into prompts. It runs as a CLI, chat, API, or hosted Studio, and connects to warehouses (Snowflake, StarRocks, BigQuery, DuckDB, Postgres, and more) rather than living inside one. Every artifact the agent touches — SQL it has written, schemas it has inspected, semantic definitions, validated metrics, feedback on corrections — becomes a recallable asset for the next run. **Task subagents** (`ask_metrics`, `gen_sql`, `explore`) handle repeatable worker patterns; **domain subagents** package scoped context for finance, growth, or other teams. Semantic execution can route through MetricFlow-compatible paths or OSI-native adapters when governed metrics arrive as portable interchange YAML. Datus-agent is Apache 2.0 and self-hostable; Studio and commercial runtime components (including Dosi for OSI execution) are separate from the open-source core. In Datus's published Lakehouse deployment narrative, the team reports that self-service analytics expanded and ad-hoc query work became materially faster; keep those figures tied to the case-study source rather than treating them as a universal benchmark.

## 4. Data engineering agents compared, side by side

Lined up against each other, the four agents diverge on almost every axis that matters operationally.

| Dimension | BigQuery DEA | Adobe DEA | Claude Code subagent | Datus |
| --- | --- | --- | --- | --- |
| Product form | Managed cloud feature | Announced SaaS capability | CLI agent persona | Open-source agent framework |
| Scope | BigQuery + Dataform | Adobe Experience Platform | Whatever is local | Stack-agnostic warehouses |
| Environment | GCP console | AEP UI | Terminal (Claude Code) | CLI · Chat · API · Studio |
| Target user | GCP data engineers | Adobe martech teams | Individual developers | Data + platform teams |
| Open source | No | No | Prompt only | Apache 2.0 |
| Persistent context | Knowledge Catalog | AEP platform state | None (no dedicated data store) | Context Engine |
| Executes pipelines | Generates; review-then-run | Yes, inside AEP | Yes, via tool use | Yes, workflow mode |
| AI / LLM | Gemini | Sensei GenAI (Adobe AI platform) | Claude | Pluggable (multi-model) |

*Table notes: Adobe's agent has been announced with "will soon" language in official materials — its GA timeline differs from the other three. BigQuery's agent generates pipeline code within a human-in-the-loop review flow; "Generates; review-then-run" reflects that nuance more accurately than a binary yes/no. "None (no dedicated data store)" for Claude Code means no persistent first-class data engineering memory layer — it does not mean Claude Code is stateless.*

The table reads as a single market only if you squint. Three of the four agents are bound to a specific environment — a cloud, a SaaS, or a CLI — and one is bound to none. Three of them treat "context" as whatever the host platform happens to know, and one treats context as the product itself.

## 5. Four categories of data engineering agent, one label

A cleaner way to think about the space is to stop comparing the four head-to-head and place them in different categories altogether. Each one is best-in-class at a different job.

- **Platform-embedded agents** (BigQuery, Adobe) make the host platform faster to use. They're the right answer when your entire data life happens inside that platform and you want zero new vendors, no new credentials, and the agent's context to ride on the platform's existing metadata.
- **Prompt-as-agent recipes** (Claude Code data-engineer) make a general-purpose coding agent behave like a data engineer for an afternoon. They're the right answer for one-off, local, exploratory work where setting up real infrastructure would cost more than the task itself.
- **Vertical SaaS agents** (Adobe's offering is the clearest example) bring agentic workflows to a specific business function. They're the right answer when the platform *is* the customer's system of record.
- **Open-source agent frameworks** (Datus) treat the agent as infrastructure that lives *between* tools rather than inside one. They're the right answer when you have more than one warehouse, more than one team, and more than one week of data work to do.

None of these are wrong. Calling them all the same product is.

## 5.1 Platform-native coding agents (warehouse DEA, 2025–2026)

A second wave of products narrows the label further: **coding agents for data engineering inside a warehouse control plane** — distinct from conversational query agents (Genie Agents, Cortex Analyst) that answer analyst questions over governed metrics. As of August 2026, the three most cited entries are **Snowflake Cortex Code**, **Databricks Genie Code**, and **Google BigQuery Data Engineering Agent**. They generate and refactor pipeline code, wire platform metadata (Unity Catalog, Knowledge Catalog, Horizon), and increasingly expose MCP hooks for external tools — but their persistent context still rides on platform catalogs, not a portable interchange file you can execute on every engine without re-authoring.

Teams already standardized on one cloud often adopt these first because IAM, billing, and lineage require no new vendor. Teams with Snowflake plus BigQuery plus a lakehouse typically still need a stack-agnostic context layer on top — or they operate three agents with three different memory models. The detailed feature matrix, GA timelines, and lock-in trade-offs for Cortex Code vs Genie Code vs BigQuery DEA belong in a dedicated platform comparison; this Hub stops at taxonomy so you know the SKU exists before evaluating products.

## 6. Context is what separates a data engineering agent from a chat window

If you only remember one thing from this article, make it this: the deepest split between today's data engineering agents is not UI or pricing or which LLM they use. It is how they handle *context*.

Data engineering is a long-running discipline. The same warehouse is queried thousands of times. The same metrics get re-derived in slightly different shapes. The same join keys, partitioning quirks, and "don't use this column, it was deprecated in March" footnotes show up in every other ticket. A human engineer accrues this knowledge in their head, in a runbook, in a wiki page nobody reads. An agent without anywhere to put that knowledge has to rediscover it on every run.

Platform-embedded agents partially solve this by leaning on their host's catalog. That works for schema metadata; it does not cover validated SQL, business definitions, or the institutional memory of which queries were trusted. Prompt-based agents don't solve it at all — they begin every session in the same blank state.

A context-first agent treats every successful run as training data for the next one. The semantic model grows. The library of validated metrics grows. The set of business rules the agent will never violate grows. Over weeks, the agent stops being a chatty SQL writer and starts being something closer to a junior engineer who has actually worked on your codebase. For what "semantic layer" means in this stack — and how it differs from a metric layer or catalog — see [what is a semantic layer](/blog/what-is-semantic-layer). Datus describes this broader approach as contextual data engineering — treating data context as a first-class, evolvable asset rather than a one-time modeling exercise.

> An agent without persistent context is a clever stranger. An agent with persistent context is a coworker.

This is also why the category will, eventually, consolidate around the agents that own their own context layer. Platform agents will keep getting smarter inside their walls. Prompt agents will keep being useful for ad-hoc work. But the load-bearing "data engineering agent" for a real organization needs to outlive a single warehouse, a single quarter, and a single set of credentials. Industry coverage of AI agents and AI-ready data has pushed the category into peak-noise territory; the agents most likely to endure are the ones that turn context into durable infrastructure rather than a prompt feature.

## 7. Where Datus, the open-source data engineering agent, fits

Datus is aimed at the open-source, stack-agnostic category: a Context Engine plus Knowledge store that turns validated SQL, schemas, semantic models, and domain rules into shared, evolvable assets. Domain subagents package scoped context for delivery; built-in task subagents handle repeatable compile-and-execute loops. When metrics are governed in OSI YAML, semantic adapters can compile them without forcing every path through a single vendor runtime — complementary to warehouse-native agents, not a replacement for teams that live entirely inside one platform console.

None of this makes Datus the right answer for every team. If you're entirely on BigQuery and never plan to leave, Google's agent is closer to home. If your entire data world is AEP, Adobe's agent is closer to home. If you want a clever assistant for an evening of exploratory work, the Claude Code subagent is closer to home. Datus is for the case where the data stack is real, plural, and durable — and where you want an agent that accumulates knowledge instead of forgetting it.

In other words: the four products called "data engineering agent" today answer four different questions. The most important question they collectively raise is the one Datus is trying to answer head-on — *where does the agent's memory live?*

## Conclusion

"Data engineering agent" is a useful label, but in 2026 it covers at least four different products with four different ambitions. Google's BigQuery Data Engineering Agent makes one warehouse faster. Adobe's makes one SaaS faster. The Claude Code subagent turns a generalist coding assistant into a data engineer for an evening. Datus treats the agent as durable infrastructure that lives between tools, with persistent context as its first-class primitive.

The next reads in this cluster: [contextual data engineering](/blog/contextual-data-engineering) (where memory lives), [platform-native agents compared](/blog/platform-native-data-agents-compared) (Cortex Code vs Genie Code vs BigQuery DEA), [best data engineering agents](/blog/best-data-engineering-agents) (full landscape), and [enterprise requirements](/blog/enterprise-data-engineering-agent). For the parent **data agent** category, see [what is a data agent](/blog/what-is-data-agent). For portable governed metrics across stacks, see [open semantic interchange (OSI)](/blog/open-semantic-interchange-osi).

## Frequently asked questions

### What is a data engineering agent, in one sentence?

A **data engineering agent** is AI software that turns natural-language goals into executable data work — SQL, pipelines, schema changes, quality checks — against your real warehouse or lakehouse, using persistent context so it does not start from zero every time.

### How is a data engineering agent different from a SQL copilot or text-to-SQL tool?

A **SQL copilot** or **text-to-SQL** tool typically generates a query and stops. A **data engineering agent** also plans multi-step work, operates with credentials against live systems, and — critically — retains reusable context (schemas, metrics, validated SQL, business rules) across sessions. Copilots answer questions; agents accumulate institutional knowledge.

### How do I evaluate which type of data engineering agent fits my team?

Start with two questions about your stack. **Single warehouse or plural?** If everything lives inside one platform (BigQuery-only, Snowflake-only), a platform-embedded or warehouse-native coding agent is the path of least resistance — see [platform-native agents compared](/blog/platform-native-data-agents-compared). If you have two or more warehouses, a lakehouse, or plans to add one, you need a stack-agnostic agent or a context layer that travels. **Ad-hoc or durable?** If the work is exploratory and session-bounded, a prompt-based agent works. If the same metrics, schemas, and rules will be queried thousands of times across months, you need persistent context — a system that remembers. The four-category breakdown in this guide (platform-embedded, prompt-as-agent, vertical SaaS, open-source framework) maps to these two axes.

### What does an agent need to know about my data to be useful?

More than column names. A useful data engineering agent needs four layers of context: **schema metadata** (tables, columns, types, join keys), **business semantics** (what "revenue" means, which dimensions are valid, which tables are deprecated), **validated SQL** (proven queries it can reuse and adapt rather than generating from scratch), and **feedback history** (which past outputs were trusted, which were corrected, and why). Without the last two layers, every query is a first attempt — and data engineering is not a discipline where first attempts are usually right.
