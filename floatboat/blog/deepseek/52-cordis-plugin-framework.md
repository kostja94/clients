---
title: "Cordis — The Plugin Kernel Behind DeepSeek Harness"
description: "Cordis is the plugin framework powering DeepSeek Harness: reversible effects, reactive dependencies, and why 'everything is a plugin' matters for agents."
slug: "cordis-plugin-framework"
date: 2026-08-18
author: "Kostja"
category: "DeepSeek"
secondaryCategory: "Research"
---

## TL;DR

- Cordis is a **meta-framework** — a framework for building frameworks — whose core capability is a reversible plugin system: components can be mounted, unmounted, and hot-reloaded at runtime, with every side effect cleanly rolled back on removal.
- Its design is formalized in a paper, *A Programming Paradigm for Spatiotemporal Composability*, which splits dynamic composition into two dimensions: **temporal composability** (fully reverting a component's effects) and **spatial composability** (declaring and reactively managing inter-component dependencies).
- Cordis has been the foundation of the open-source chatbot framework **Koishi for four years**, and it is now the plugin kernel of **DeepSeek Harness (dsh)**, where "everything is a plugin" — the model adapter, tool registry, session log, and agent loop are all swappable components.
- The three mechanisms that make it work: `ctx.effect` for reversible side effects, lifecycle events (`ready` / `dispose` / `fork`) for clean teardown, and a service system for dependency ordering.
- For agent infrastructure, this matters because it makes **self-evolving runtimes safe**: an agent that can change its own runtime is only worth having if those changes are reversible.

---

## 1. Why a Plugin Kernel Matters for Agents

Plugin systems are not new. Every major application from IDEs to browsers has shipped with one, and the idea of hot-loading a module without restarting the host has been around for decades. So when DeepSeek announced that its open-source agent harness was built on "everything is a plugin," the initial reaction from developers was understandable: what makes this different from the plugin architecture in a text editor or a CI tool?

The difference is that agent runtimes stretch plugin systems in a direction they were never designed for. An agent loop is not a static host with extensions — it is a system that manages state across many steps, holds context, calls tools, and most importantly, can be asked to modify its own behavior mid-run. When a component in that system is removed or replaced, everything downstream that depended on it must either adapt or fail gracefully. Text editors can tolerate a plugin leaving a dangling reference; an agent that has already committed to a multi-step plan cannot.

That is the gap Cordis is built to close. Rather than treating plugin management as a convenience feature, it treats **composition itself as the problem to solve formally**. The paper behind it starts from the observation that modern software — plugin systems, self-evolving agent harnesses — increasingly requires dynamic composition, yet its formal foundations remain underdeveloped. Cordis is that foundation, and understanding it is the fastest way to understand why DeepSeek chose it as the base layer for its agent runtime rather than building a conventional plugin manager from scratch.

---

## 2. Spatiotemporal Composability, Explained

The paper's title — *A Programming Paradigm for Spatiotemporal Composability* — sounds intimidating, but the two terms in it map to two concrete problems that every dynamic system faces.

**Temporal composability** is the ability to completely revert a component's side effects upon removal. When a plugin is unloaded, everything it registered — event listeners, tool definitions, memory allocations, command handlers — must disappear with it, leaving the system exactly as if the plugin had never been loaded. Most frameworks can remove a plugin's code; very few can guarantee that its effects are fully undone, which is why repeated reload cycles in conventional systems slowly accumulate leaks.

**Spatial composability** is the ability to declare and reactively manage inter-component dependencies. When plugin A provides a service that plugin B uses, the system must ensure B loads only after A is ready, unloads before A stops, and never starts if A failed. More subtly, when the context changes — a service is replaced, a dependency shifts — every component affected must be notified and respond according to its declared contract.

Cordis formalizes both by lifting classical effect and coeffect concepts into runtime mechanisms. Every context transformation carries an inverse that the runtime tracks (the revertible effect). Every change to the context notifies components against their coeffect specifications (the reactive coeffect). The two contexts are unified into a single context type, which becomes the programming paradigm — and from there, components and a calculus of dynamic composition let the property scale from a single component to a whole system of interleaved ones.

The practical payoff is path independence: the final state of a Cordis application depends only on which plugins are enabled, not on the order they were loaded or unloaded. That property is what makes hot module replacement safe, and it is the same property an agent runtime needs if it is ever going to reconfigure itself without corrupting its own state.

---

## 3. The Three Mechanisms

Cordis implements this paradigm through three cooperating mechanisms, all exposed through a shared context object (`ctx`).

**`ctx.effect` — reversible side effects.** This is the heart of temporal composability. When a plugin registers a side effect, it calls `ctx.effect()` and provides the cleanup function — the "inverse" — as its return value. The runtime stores that inverse and executes it when the plugin unloads. Anything that needs cleaning up — connections, memory, registered handlers, subscriptions — goes in the effect, and Cordis guarantees it runs in reverse order of registration at teardown. This is the same idea as C++'s RAII or Rust's `Drop` trait, lifted from the language level to the runtime level so that even plugins written by different teams unload cleanly.

**Lifecycle events.** Cordis exposes three user-facing lifecycle events plus internal system events. `ready` fires when the lifecycle starts (or immediately if the context is already active). `dispose` fires when the context is unloaded, triggering the cleanup chain. `fork` fires every time a plugin is loaded, and it is itself a plugin function — so a reusable plugin can spawn child contexts, each with its own lifecycle. The internal events (`internal/runtime`, `internal/fork`, `internal/service`, `internal/update`) handle the bookkeeping: tracking plugin states, service changes, and configuration updates.

**Service management.** The service system handles spatial composability. Plugins declare dependencies via an `inject` property, and Cordis resolves the dependency graph: plugin B loads only after plugin A provides the service it needs, unloads before A stops, and never activates if A fails. Dependencies are expressed by service name, giving the runtime the ordering information it needs to guarantee safe teardown in any load/unload order.

Together these three mechanisms mean a Cordis developer rarely needs to reason about cleanup order, dependency race conditions, or reload leakage — the framework takes those guarantees on itself. The discipline is the cost: every plugin must declare its effects and dependencies explicitly, which is a meaningful contract to uphold, but one that pays off in exactly the environments where agents live.

There is also a configuration layer worth naming, because it is what makes the framework usable by people who do not write plugin code. Cordis ships a declarative component loader with configuration reconciliation and hot module replacement: plugins are declared in configuration rather than wired imperatively, and when a config changes, the loader diffs the declared state against the running state and mounts, unmounts, or updates only the plugins that changed. This is the mechanism behind the "select, swap, or extend any capability in configuration" claim in the DeepSeek Harness docs — the configuration file is not a settings panel bolted on top of a static system; it is the interface to the dynamic composition engine itself.

The event model deserves one more note, because it is where Cordis's guarantees get auditable. Every plugin lifecycle transition — a fork created, a runtime spawned, a service value replaced, a configuration updated — emits a typed internal event. That means an operator can observe exactly what the system did, in what order, and why. For an agent runtime, that auditability is not a nicety: if an agent reconfigures itself and the result is wrong, the event log is what lets you reconstruct the sequence and decide whether the change should be rolled back. Reversibility is only useful if you can tell what was reversed.

---

## 4. From Koishi to DeepSeek Harness

Cordis was not built for DeepSeek. It has been in production for four years as the foundation of **Koishi**, an open-source cross-platform chatbot framework created by the developer shigma. Koishi's name comes from a character in the Touhou Project franchise, and the project has accumulated roughly 6,000 GitHub stars building chat agents that run across Discord, Telegram, and other platforms. What made Koishi a useful test bed for Cordis is precisely what agent runtimes need: plugins that register commands and services, get hot-reloaded during development, and must clean up after themselves when disabled.

Koishi ran on Cordis v3. When DeepSeek Harness shipped its developer preview on August 13, 2026, it was built on **Cordis v4** — and the same day, the Cordis team published the formal paper that had been driving the v4 redesign. The timing was not incidental: v4's explicit focus on reversible effects and reactive coeffects is the machinery an agent harness needs, and the paper made that machinery legible to the broader engineering community. The connection is documented directly in the DeepSeek Harness architecture docs, which name Cordis as the framework underneath, and in the GitHub repository, which links the paper as the design's source. For the full context on what DeepSeek Harness itself does at the execution-layer level, see [our explainer on DeepSeek Harness](/blog/what-is-deepseek-harness).

The four-year provenance matters for a practical reason: Cordis is not a proof of concept that DeepSeek is betting on. It is battle-tested software with an established plugin ecosystem, a real community, and a formal spec. When you build on a harness whose kernel has survived four years of real plugin churn, the "everything is a plugin" claim carries more weight than it would for a framework that shipped last week.

---

## 5. Everything Is a Plugin

DeepSeek Harness (dsh) takes the Cordis philosophy literally. Every capability in the harness is a plugin: the model adapter, the tool registry, the session log, the sandbox, the storage layer, the agent loop, and even the UI. The harness itself is a thin kernel that mounts, unmounts, and tracks dependencies; the agent's actual capabilities live entirely in the plugins above it.

The architecture doc lays out how the pieces map onto Cordis contexts. The session subsystem owns the append-only `SessionEvent` log and in-memory store, exposed as `ctx.sessions`. The system-prompt subsystem handles prompt-section and tool-schema assembly via `ctx.systemPrompt`. The tools subsystem provides a scoped tool registry and guarded execution pipeline under `ctx.tools`. The agent subsystem exposes the `Agent` interface, live registry, and agent events through `ctx.agents`, with the default driver implementing that interface at `ctx.agentLoop`. The LLM layer contributes message and stream vocabulary plus the adapter seam at `ctx.llm`.

Plugins register capabilities against these context keys, and everything works through the Cordis service and event model. The practical result is that you can swap a model backend, replace the sandbox, or add a custom tool by mounting a plugin in configuration — no source fork, no privileged core to patch. DeepSeek ships four preset profiles out of the box: **Standard** (the full coding agent with filesystem, shell, web search, subagents, and plan mode), **Code** (model-generated code orchestrates multiple tool-call rounds), **Minimal** (only `bash` and a file editor, the configuration DeepSeek used for its own official model benchmarking), and **Creator** (for building custom presets with runtime inspection and preset-authoring guidance).

This is a meaningfully different posture from monolithic agent tools where the loop, tools, and UI are welded together. It is also the reason DeepSeek's own benchmark numbers were reproducible: the harness used for scoring V4 Pro is the same open source with a plugin configuration, which is documented in the V4 Pro 0813 release notes. That link between the benchmark and the released code is covered in our [DeepSeek V4 Pro 0813 analysis](/blog/deepseek-v4-pro-0813).

---

## 6. Why This Matters for the Agent Ecosystem

For a developer evaluating agent infrastructure, the Cordis-based design changes what "open source" means for a harness. An open license makes code inspectable; a plugin kernel makes it *transformable*. If you want a different sandbox, a custom tool, a different model backend, or a UI that matches your product, you mount a plugin instead of maintaining a fork. The plugin ecosystem becomes the moat — and DeepSeek has signaled that intent by adding the `dsh-plugin` topic on GitHub for discoverability and standing up a Discord community around the harness.

There is a second-order effect worth naming. The same property that makes Cordis good for plugin management — reversibility — is what makes an agent runtime safe to self-modify. An agent that can reconfigure its own stack, add tools mid-task, or evolve its own workflow is only worth trusting if every change can be rolled back cleanly. Cordis's revertible effects are the mechanism that turns "agents that modify their own runtime" from a research curiosity into a defensible engineering pattern.

That is also where the comparison to the closed agent products of the same week becomes instructive. The same week DeepSeek open-sourced a harness built on a reversible plugin kernel, xAI shipped Grok Bot — a product where the agent's environment is a persistent cloud computer the vendor controls. Both are bets on where agent infrastructure goes, and they could hardly differ more in philosophy: one gives you the kernel and the plugins, the other gives you the teammate and the computer. We break down the closed-product side of that comparison in [our Grok Bot explainer](/blog/grok-bot).

---

## Conclusion

Cordis is easy to underestimate because it does not do anything flashy — it manages plugin lifecycles, dependency ordering, and cleanup. But those three things are precisely where agent runtimes fail when they try to evolve themselves. The formal guarantee that a component can be removed with all its effects reversed, and that dependencies react correctly to every context change, is what makes dynamic composition safe enough to build a self-modifying agent on.

DeepSeek's choice to build its harness on a four-year-old plugin kernel, rather than a purpose-built monolith, is a statement about where the agent ecosystem is heading. The winning harnesses will not be the ones with the most tools built in — they will be the ones whose plugin ecosystems make it cheapest to compose the tools you need. Cordis gives DeepSeek that, and it gives every developer building on dsh the same leverage. Whether you are contributing a plugin, evaluating a harness, or just trying to understand why "everything is a plugin" is more than a slogan, the reversible kernel is the part worth understanding.

---

## FAQ

### Is Cordis a DeepSeek product?

No. Cordis is an independent open-source meta-framework created by the developer shigma, and it has been the foundation of the Koishi chatbot framework for four years. DeepSeek Harness is built on Cordis, which is why it appears in DeepSeek's architecture documentation.

### What is a meta-framework?

A framework for building frameworks. Instead of providing APIs for a specific domain (like chatbots or web servers), Cordis provides the fundamental mechanisms for plugin systems, dependency management, and resource lifecycle control. The name comes from the Latin *cor*, meaning "heart."

### What does "spatiotemporal composability" mean?

It is the paper's term for two properties a dynamic system needs: temporal composability (a component's side effects can be fully reverted when it is removed) and spatial composability (components can declare dependencies that the runtime manages reactively). Together they make plugin systems safe to reload and evolve.

### How does Cordis clean up plugin side effects?

Through `ctx.effect`. Every side-effect-producing call returns a cleanup function, which the runtime stores and executes in reverse registration order when the plugin unloads. This is analogous to RAII in C++ or `Drop` in Rust, but handled at the runtime level so third-party plugins unload cleanly too.

### What are the four preset modes in DeepSeek Harness?

Standard (full coding agent), Code (model-generated code orchestrates tool calls), Minimal (only `bash` and a file editor — the configuration used for DeepSeek's own official benchmarks), and Creator (for building custom presets with runtime inspection).

### Why does reversibility matter for AI agents specifically?

An agent that can modify its own runtime — add tools, change its loop, evolve its workflow — is only safe to trust if every change can be rolled back. Reversible effects are the mechanism that makes self-modifying agents an engineering pattern rather than a research risk.
