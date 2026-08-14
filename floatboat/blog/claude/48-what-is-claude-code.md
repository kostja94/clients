---
title: "What Is Claude Code — Anthropic's Terminal Coding Agent"
description: "Claude Code explained: Anthropic's terminal coding agent, its plan mode, sub-agents, and MCP — and how it differs from Cowork, Tag, and Chat."
slug: "what-is-claude-code"
date: 2026-08-14
author: "Floatboat Team"
category: "Claude"
secondaryCategory: "Research"
---

## TL;DR

- **Claude Code** is Anthropic's agentic coding tool that runs in a terminal, the Claude desktop app, and IDEs like VS Code and JetBrains — you describe an outcome, and it reads the repo, plans, edits files, runs commands, and commits.
- It is the reference implementation of the **local coding agent**: single-player, repo-scoped, and built so a human can intervene at arm's length. Plan mode and permission prompts are the safety layer between "autonomous" and "unreviewed."
- Its defining mechanics are **plan mode** (read-only research before edits), **sub-agents** (isolated workers that return summaries instead of bloat), **MCP** (Model Context Protocol for external tools), and **skills / hooks** for reusable workflows.
- Claude Code is **not** Cowork (local knowledge-work agent), **not** Tag (multiplayer Slack coworker), and **not** Chat. It is the surface you use when the artifact is code in a repository.
- For how it fits against the other Anthropic surfaces, see <a href="/blog/claude-code-vs-cowork-vs-tag">Claude Code vs Cowork vs Tag</a>. Switching the model inside the same harness is a separate question.

---

## 1. Why Claude Code Exists Now

Before Claude Code, "AI coding" mostly meant autocomplete: a model suggested the next line inside an editor, and the human still drove every file, every test, every commit. The last mile — actually running the toolchain — stayed manual. Claude Code reversed that. It packaged the agentic loop that was emerging in Anthropic's research into a terminal tool that can read a codebase, write changes across many files, run tests, read the failures, and iterate until the tests pass. The human moves from "typing the code" to "reviewing the work."

That shift matters because it changes where a developer spends attention. Autocomplete optimizes keystrokes. Claude Code optimizes a loop: plan, execute, verify, revise. The artifact is a diff and a green test run, not a suggested snippet. Anthropic shipped Claude Code as a research preview in early 2025 and, by mid-2026, it had become the reference implementation of a local coding agent — the surface other terminal and IDE agents are measured against.

The timing is not an accident. Coding was the natural first home for agentic work because a repository is a closed world: files, tests, diffs, a CI status. The model gets a sandbox with a success signal. That is far more tractable than open-ended office work, which is why coding agents matured before their knowledge-work equivalents. Claude Code's success is the proof that the same loop works, and it is the architecture <a href="/blog/what-is-claude-cowork">Claude Cowork</a> reused for files and connectors, and that <a href="/blog/what-is-claude-tag">Claude Tag</a> reused for Slack channels. In each case the loop is identical; only the object and the audience change.

---

## 2. Claude Code Defined

Claude Code is a local, single-player coding agent. You invoke it in a terminal or IDE, it works against a repository using your credentials and your filesystem, and the session belongs to you. It reads files, plans an approach, edits code, runs shell commands and tests, and produces commits and pull requests — all while asking for approval at the boundaries you configure. That last clause is the definition, not a footnote: Claude Code is built to be autonomous *with checkpoints*, not autonomous *without review*. The difference is the whole point of a local coding agent — the human stays in the loop, but the loop, not the typing, is the work.

### 2.1 The Core Definition

A **local coding agent** is an agent that runs beside one developer, on their machine or against their repository, with the job of turning a request into reviewable code. Claude Code is Anthropic's implementation of that form. It differs from a chat assistant (which only answers) and from a multiplayer coworker (which shares a channel and acts on its own initiative). Claude Code is private, repo-scoped, and user-initiated.

### 2.2 Five Defining Properties

**Terminal-native, then everywhere.** Claude Code began in the terminal, which is why it is associated with shell-first developers. It now also runs in the Claude desktop app and inside IDEs, including VS Code and JetBrains. The interface changes; the loop stays the same.

**Plan mode.** Plan mode is a read-only state: the agent analyzes the codebase and drafts a plan using only read tools, then presents it before any file changes. On a migration or a multi-file refactor where the right approach is genuinely unclear, plan mode forces the research to happen before the edits. It is the concrete mechanism behind "think before you write."

**Sub-agents.** Claude Code can spawn isolated workers that each get their own context window, do a side task — a targeted search, a parallel research pass — and return only a summary. That keeps a long session from drowning in logs and search results. It is the local, single-player ancestor of the many-Claudes pattern Tag turns into a team feature.

**MCP and skills.** The Model Context Protocol lets Claude Code reach external systems — databases, issue trackers, browsers — through configured servers. Skills capture reusable workflows. Hooks run automation around the session. These are the extension points that turned Claude Code from a coding tool into a harness other models and workflows plug into.

**Permission prompts and approval gates.** Before running a command or editing a file, Claude Code surfaces the action for approval according to your permission mode. This is the developer-facing version of the identity question Tag answers at the organization level: who is allowed to touch what, and who sees the trace.

### 2.3 What Claude Code Is Not

Claude Code is **not Claude Cowork**. Cowork is the same local-agent loop aimed at knowledge work — files, folders, and connected apps — rather than repositories. Code targets engineers and trees of source files; Cowork targets researchers and analysts and their documents. They are siblings on the same rung, not two names for one product. The full distinction is covered in the three-way comparison linked above.

Claude Code is **not Claude Tag**. Tag is the multiplayer, asynchronous surface: one Claude per Slack channel, organization identity, ambient follow-up. Code may open a PR; Tag lives in the channel where the decision to merge was made. Code is where one engineer ships. Tag is where a team delegates.

Claude Code is **not Chat**. Chat is the low-friction, turn-based surface for drafting and Q&A. Code executes against a repository with tools and test runs. Chat answers; Code does.

Claude Code is **not an autocomplete plugin**. Copilot-style inline suggestions fill a line; Claude Code runs an agentic loop. Autocomplete optimizes keystrokes; Code optimizes verified changes. Teams often run both — autocomplete for flow, an agent for the hard, multi-step problems.

---

## 3. How Claude Code Works

The loop is plan, execute, verify, revise. On a nontrivial task, Claude Code first reads enough of the codebase to understand the change, typically drafting a plan in plan mode. It then executes: editing files, running commands, running tests. It reads the results — the failing test, the linter output, the type error — and revises until the artifact is reviewable. That feedback loop, not any single generation, is what separates an agent from a smarter autocomplete.

Concretely: ask Claude Code to fix a bug that spans a service and its client. It greps for the call site, reads both sides of the contract, drafts a plan in plan mode, then edits the two files, runs the relevant tests, and reacts to the failure. A developer who used to do that in a morning now reviews a diff in minutes. The value is not that the model wrote the lines; it is that the loop closed without the human babysitting each step.

Sub-agents make the loop scale. Rather than carrying every search result and log line in the main context, Claude Code dispatches a sub-agent that researches a specific question and returns a summary. This is how a session stays coherent across a long refactor instead of degrading into a pile of half-remembered context. The mechanics documented in Anthropic's docs — plan mode's read-only toolset, the `Task` tool for dispatch, the separate context windows — are the parts users should understand before trusting the tool with a large repo.

Extensibility is the second half. Through MCP, Claude Code can query a database, read a ticket, or drive a browser. Through skills, teams encode how they want common tasks done. Through hooks, they wire the session into lint, format, or CI. These are the same primitives that make Claude Code a harness rather than a closed product — which is why it can also be pointed at a different model family, as the <a href="/blog/deepseek-agent-vs-claude-code">DeepSeek Agent vs Claude Code</a> comparison walks through.

The cost profile is worth stating plainly. Claude Code runs on Claude models — Opus for the hardest reasoning — and agentic sessions consume far more tokens than chat, because every tool call and every test rerun is a fresh round of inference. A single agentic task can cost a few dollars on a frontier model, and a team of developers running it daily spends real money. That is the trade-off the terminal hides: the value is verified work, not words per dollar.

---

## 4. How It Compares to Related Concepts

The cleanest frame is Anthropic's four surfaces: **Chat** for conversation, **Claude Code** for repositories, **Claude Cowork** for files and connectors, **Claude Tag** for Slack channels. Code sits on the local, single-player rung with Cowork, aimed at engineers rather than knowledge workers. The three-way split and when to use each surface is covered in the comparison linked above.

Against **other coding agents**, Claude Code's edge is depth and reasoning on large, messy codebases — the repo-scale refactor, the architectural change that touches dozens of files. Its cost is a terminal-first UX and Claude-model lock-in for the deepest quality. IDE-native tools like Cursor win on daily flow; open-source options like Cline and Aider win on model choice and price. That landscape, ranked by job shape, is in <a href="/blog/best-claude-code-alternatives">best Claude Code alternatives</a>. The recurring pattern across 2026 comparisons is that serious teams run two: an IDE agent for the everyday, and a terminal agent for the hard problem. The reason is the same job-shape split as everywhere else in this cluster — one surface cannot be both the fastest way to write the next line and the deepest way to rearchitect a module.

Against **desktop and cloud agents**, Claude Code is the narrow, deep choice. Manus and Devin-style cloud agents delegate whole tasks and come back later; Claude Code stays beside you in the repo. The difference is the same horizon question the product-form ladder keeps returning to: Code assumes you are near enough to review and redirect. Cloud agents assume you have stepped away and want a result when you return. Neither is superior; they occupy different points on the same ladder, and the point you pick should follow how long the work actually takes and how close you need to be while it runs.

---

## 5. What's Next for Claude Code

Three directions are visible in mid-2026. **Harness over model.** Claude Code is increasingly a shell that other models can run inside — the DeepSeek endpoint route is the clearest example — which reframes it from "Anthropic's product" toward "the default terminal harness." **Convergence with Cowork and Tag.** The same loop now powers all three surfaces, so the boundary that matters is no longer "is it agentic" but "whose context and whose audience." **Multiplayer coding.** Agent teams and dynamic workflows inside Code are the local preview of the multiplayer pattern Tag turns into a product; the line between "my repo session" and "the team's channel" is where the next form of coding work is being negotiated.

The durable takeaway: Claude Code defined what a local coding agent looks like. What changes next is less the loop than the surface it runs in — terminal, IDE, desktop, channel — and who is in the room when the agent works. For teams deciding whether the next hire is another engineer or a shared agent, that surface question is the same one the whole Claude cluster is organized around: whether the work is still a solo session or already a team object.

---

## Conclusion

Claude Code is Anthropic's local coding agent: single-player, repo-scoped, and built around a plan-execute-verify loop with approval checkpoints. Its defining mechanics are plan mode, sub-agents, MCP, and skills. It is not Cowork (knowledge work), Tag (multiplayer Slack), or Chat (conversation), and it is not an autocomplete plugin. The loop is what you are buying, not the next-line suggestion.

Pick Claude Code when the artifact is code in a repository and you want to review each step. Pick Claude Cowork when the object is your files. Pick Claude Tag when the work is owned by a channel. The surface should match the job's horizon and audience — not brand habit.

---

## FAQ

### Is Claude Code the same as an AI autocomplete?

No. Autocomplete suggests the next line while you type. Claude Code is an agent that reads the repo, plans, edits across files, runs tests, and iterates. You review the diff; you do not drive every keystroke.

### How is Claude Code different from Claude Cowork?

Both are local, single-player agents. Code targets repositories and engineering. Cowork targets files, folders, and connectors for knowledge work. Same loop, different object. See the three-way comparison linked above for the split.

### Does Claude Code only run in the terminal?

No. It started in the terminal but now runs in the Claude desktop app and inside IDEs including VS Code and JetBrains. The interface changes; the agentic loop stays the same.

### Can Claude Code use models other than Claude?

Yes, in practice it can be pointed at Anthropic-compatible endpoints, including DeepSeek's, which changes cost and capability trade-offs. The DeepSeek Agent vs Claude Code comparison covers the model swap in detail.

### Why is Claude Code expensive compared to autocomplete?

Agentic work spends tokens on every tool call and test rerun, not just the final answer. Verified multi-step changes cost more than single-line suggestions. The value is the verified diff, not words per dollar.

### Should I switch from Cursor to Claude Code?

They solve different jobs. Cursor wins on IDE-native daily flow; Claude Code wins on deep, repo-scale reasoning from a terminal. Many teams run both rather than switching. The ranked job-shape breakdown is in the alternatives list linked above.
