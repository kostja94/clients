---
title: "Agent Skills for People Search: What They Are, How They Differ from Web Search APIs, and What to Use in 2026"
description: "Defines agent skills for people search (SKILL.md, tools, return shape), contrasts generic web research with a governed people row, and shows how Lessie Skills & CLI runs find → enrich → review in the agent—plus optional reading on a public reference skill."
slug: "agent-skills-for-people-search"
date: 2026-04-28
author: "Kostja"
image: "/blog/images/agent-skills-people-search-2026.jpg"
keywords:
  [
    "agent skills people search",
    "people search AI agent",
    "Claude skills people research",
    "MCP people search",
    "Lessie Skills CLI",
    "People Search AI Agent",
  ]
related:
  - "how-to-find-influencers"
  - "best-ai-tools-for-influencer-marketing"
  - "ai-in-influencer-marketing"
  - "influencer-outreach-email-templates"
  - "influencer-marketing-checklist"
---

# Agent Skills for People Search: What They Are, How They Differ from Web Search APIs, and What to Use in 2026

If you have spent more than a week in **Claude Code**, **Cursor**, or any MCP-driven agent, you have already felt the gap. A model can *sound* like a researcher: it can quote a blog, draft a polite email, summarize a PDF. What it often cannot do, reliably, is *behave* like one—repeatable steps, a stable output contract, consistent tool use, and clear stop conditions when the web is noisy or paywalled. The rest of this article turns that job into a named idea—**agent skills for people search**—and shows how to run it in production, not only in a demo chat.

This is for builders and operators who are tired of “just add web search” as a universal fix. We wrote it from influencer and GTM work, but the pattern is the same anywhere you need a *row*, not a paragraph. To put **people search inside an agent** (not a one-off session), we ship a [people- and org-search product built for influencer GTM on Lessie](https://lessie.ai/influencer-marketing) and, for the file-and-tooling side, [everything you need to add Lessie’s skills to your agent (install, CLI, and tool list)](https://lessie.ai/skills-cli).

## What we mean by *agent skills for people search*

We use three short definitions; together they are the title of the article.

1. **Agent skills** (usually `SKILL.md`, in the same “folder + `SKILL.md` + discovery” model [Cursor documents for Agent Skills](https://cursor.com/docs/skills)) are *packaged instructions* for a model with tools: which tools may run, in what order, and what shape the output must have—so the next step in your stack can trust the handoff. They are not a substitute for human judgment; they *encode* procedure.
2. **People search** here does not mean “type a name into a search box.” It means the repeat work of finding humans (and often orgs) for outreach or operations, with duplicates, paywalls, and platform rules in the way. The moving parts are *discovery*, *profiling*, *enrichment*, and *verification*. If your lens is **creator** discovery, [our field guide to finding the right influencers (before you wire an agent)](/blog/how-to-find-influencers) maps that problem; *this* post is the agent-side mechanism.
3. **Agent skills for people search** is the **intersection**: a skill whose *contract* is people-centric—merged candidates, per-field **sources**, **caveats**, and a clear stop when automation should hand off to a person.

Lessie productizes that intersection via **Lessie Skills & CLI** (`find_people` → `enrich_people` → `review_people`, credits, one install) so the model is not re-inventing the pipeline each time; the GTM and CLI entry points are linked in the introduction above. Generic web **search** APIs stay useful *upstream* for open-web facts, but a weak *sole* layer for governed people work—so the skill must still spell out verify steps and fetches for URLs you trust.

---

## What the job really is: discovery, profiling, enrichment, verification

“People search” in recruiting sounds like a database query. In sales, like a filter. In influencer work—our home turf—it is a filter *plus* taste: the right creator is rarely whoever has the most followers. In agent terms, the work still decomposes into a few recurring jobs, even in one long run:

- **Discovery** — who makes the first cut: role, region, language, niche, audience fields you may not see without tools.
- **Profiling** — what is publicly knowable without treating the open web as a CRM.
- **Enrichment** — which contact path is appropriate next, with conservative defaults when “more data” is legally or reputationally fraught.
- **Verification** — whether the “Alex Kim” in two tabs is the same person (duplicates are where naive agents burn trust).

None of that reduces to “search Google and hope.”

In production, the failure is not only wrong facts but unstable behavior: a different list every time, erratic effort, and raw HTML from dozens of tabs in the context window because nobody defined an off-ramp from retrieval to a tight summary.

## Why a people-search *skill* beats a long system prompt

It is tempting to call every file in `skills/` a “skill,” but the useful ones act like a portable SOP for a model with tools. They give a trigger the model can respect: a short `description` in the front matter that functions like an if-statement (“when the user is finding professionals by title and region…”)—the same *shape* as the Agent Skills format above for **Cursor** and **Claude Code**. They add constraints that look picky but save cost and face—an allowlist of tools (for example the `find_people` → `enrich_people` → `review_people` chain from **Lessie Skills & CLI**) beats “whatever HTTP looks tempting” and stops the model from mixing incompatible endpoints or burning tokens. They specify choreography—query variation, merge, dedupe, maybe a second pass—and a return contract: JSON or a table with sources on any fact that will drive the next step. A skill is allowed to be boring; if the next step is a CSV a human will send, that is a feature.

A long prompt can contain the same *words*; it rarely survives a team. Skills are versioned, reviewed, and reused—closer to a function than a comment in a chat.

## What usually goes into the SKILL.md

| Piece | What it is doing | Why people search cares |
|-------|------------------|-------------------------|
| **Metadata** | `name`, `description`, optional `context` | Routes the right skill when user intent is fuzzy |
| **Tool policy** | Allowlist (and sometimes denylist) | Stops the agent from “helpfully” using the wrong search mode |
| **Query strategy** | Variations, categories, `numResults` *by intent* | **Recall** for humans is harder than for pages; you need *breadth* early |
| **Context hygiene** | “Do heavy search in a sub-agent; return a digest” | Prevents 40 URLs from *becoming* your prompt **padding** |
| **Output format** | Fields + per-field source URLs | Makes downstream automation **boring and testable** |
| **Fallbacks** | “If paywalled, try X” | The web is 2026; *polite* research includes **stopping** |

That table is not a formal spec; it is what keeps skills from staying demo-grade. In people workflows, reputation and compliance sit one mistake from your brand account.

## Why “search the web” is not a people-search skill by itself

For influencer and GTM teams, the job is narrower than “answer from the open web”: you need people-and-org outcomes you can review, not only a polished paragraph. (For the **tooling** view of campaigns—not the `SKILL.md` layer—we surveyed [which AI tools are worth using for influencer marketing in 2026](/blog/best-ai-tools-for-influencer-marketing) in a separate post.) **Tavily**-style research APIs are a solid first mile for facts and docs, including third-party “web research” skills in MCP directories, but they optimize for synthesis and citations, not for a reusable **row** with enrichment and sane defaults. Neural or semantic retrieval can help propose URLs; one vendor’s public `SKILL.md` for that pattern is worth reading for *discipline*, and we give that a single section below—it is context, not the product we sell.

### Lessie Skills & CLI: the layer we want you to run

**Lessie Skills & CLI** is the governed path: `find_people`, `enrich_people`, `review_people`, organization discovery and enrichments, plus `web_search` / `web_fetch` when you need a wider net. The goal is packaging—credits, consistent behavior, and a line from shortlist to **People Search for influencer marketing** (same GTM link as in the intro) that BD and creator leads can ship. Once a row is credible, the next work is often *program* work—briefs, ICP, compensation—covered in [our guide to collaborating with influencers when the relationship is real, not hypothetical](/blog/how-to-collaborate-with-influencers). Install matches the Agent Skills flow you may already use: `npx skills add LessieAI/lessie-skill -y -g`, restart your Claude Code-style agent, then let the skill encode the allowlist and return shape so the model is not redesigning the stack on every run.

When you already trust a URL, Firecrawl-class readers (and Lessie’s fetch path) pull text and structure from the page instead of dumping raw HTML into context. Real people research is rarely one hop; Lessie sits where ops needs a list, not where chat only needs a summary.

## Same problem, two layers: generic research vs. people rows (Lessie)

| Question | Generic web + retrieval (Tavily-style, “search the web” skills, etc.) | Lessie Skills & CLI |
|----------|--------------------------------------------------------------------------|----------------------|
| What it optimizes | Open-web Q&A, snippets, citations; broad recall | People-and-org rows: find → enrich → review; web as a supporting step |
| What “good” looks like | A paragraph or URL set the model can quote or follow | A row you can put in a brief, CRM, or email, with sources and uncertainty |
| How skills help | Cap results, cite, do not stuff context | Call `find_people`, `enrich_people`, `review_people` in order (documented on **lessie.ai/skills-cli**) |
| Where it belongs | Upstream: docs, news, “what does this page say?” | Last mile: vetted people rows when find → enrich → review is the job |

Lessie does not mean deleting every other tool tomorrow. A normal week still layers open-web research, fetches for confirmation, and a shortlist step where names earn outreach. Lessie is the piece we want on that last mile when the artifact is a vetted list, not a wall of browser tabs.

## Optional reference: Exa’s public People Search skill (for patterns, not the sale)

Exa’s [public documentation for their “People Search” Claude skill](https://exa.ai/docs/reference/people-search-claude-skill) is worth skimming even if you never call their API. It is a concrete example of policy for the model: stick to `web_search_advanced_exa`, pick `people` or `news` modes on purpose, vary queries, merge and dedupe, and run heavy retrieval in a sub-agent so the parent context gets a small digest. Exa also publishes a separate “personal site” skill for another page type; the file-level lesson is the same. That lesson applies to any `SKILL.md`, including your **Lessie** install: allowlists, isolation, and a written return shape beat “use some search.” Most influencer teams that standardize on Lessie will not need Exa in production; they still benefit from the same habits—context hygiene and repeatable steps—that this doc names clearly.

## The same *agent skills for people search* file in different hosts: Cursor, Claude Code, OpenClaw

A people-search **skill** is not tied to one app. The usual shape is a folder with `SKILL.md`, optional `scripts/`, and front matter that says when to load what—the same open format Cursor documents under Agent Skills (see link in the definition list above). Cursor’s Agent loads skills from paths such as `.cursor/skills/`, `.agents/skills/`, and user-level mirrors; it can also read `.claude/skills/` and `.codex/skills/`. You can narrow-invoke with `/` in chat. In **Claude Code**, real work spans code and disk, which is where reusable procedure files beat one-off prompts; **Claude Code** users add third-party skills with `npx skills add …`, restart the agent, then use the tools the skill describes (same **Lessie Skills & CLI** link as in the intro for the package). The Claude Code *Agent Skills* material in the SDK matches what you keep in a repo `skills/` tree: packaging, metadata, invocation. Anthropic’s engineering blog has a long-form explainer on equipping agents with skills if you want the narrative version.

**OpenClaw** (open source, self‑hosted) is a different host: a personal-assistant gateway with multi-channel chat, with skills under `~/.openclaw/workspace/skills/<skill>/SKILL.md` next to prompts like `AGENTS.md`, a registry, and onboarding. A shortlist workflow might start in Slack or Telegram in one org and in an IDE in another; the skill is still the portable SOP. When *models* meet *ops* in marketing, [our overview of where AI is landing in real influencer marketing programs](/blog/ai-in-influencer-marketing) sits “above” this file—the skill layer is what makes lists reliable enough for that layer to matter.

**MCP** and **skills** solve different problems: MCP connects the model to APIs and data; skills govern *which* tools run in *what* order and *what* the row looks like. The **agentskills.io** site (referenced from Cursor’s documentation) is a useful bookmark for the shared `SKILL.md` convention.

## Patterns for people-search skills that survive production

If you are drafting your own `people-research` skill, think in *roles* more than buzzwords. A durable pattern usually includes:

- **Wide → narrow** — coarse discovery first (spelling variants, stage names), then tighten for the last few candidates.
- **Dedupe** — not a final polish: the same person may appear as a speaker, podcaster, and GitHub profile; entity resolution belongs *inside* the skill.
- **Source discipline** — if you cannot cite a URL for a claim that will drive outreach, mark the field unverified; embarrassed data beats a confident screenshot.
- **Fallback** — when paywalls and heavy JS block automation, route to a human in a real browser and log that as success, not a dirty secret.

When a row is fit for a human, the next step is often copy—you can hand it to [templated, policy-aware outreach copy for writing to creators](/blog/influencer-outreach-email-templates); the skill should feed that step with rows you can defend, not the other way around.

## Ethics and platform reality

**Public** does not mean *anything goes*. Contact data sits under law and platform rules. Hiring and health add sensitivity that a blunt “find their email” should not hand-wave. A skill is still useful if it is dull about opt-in, DNC lists where they apply, and not crossing into prohibited scraping. Google’s *helpful content* guidance for search is not legal advice, but it is a useful tone check: the web does not need another page built only to outrank someone by fear.

In influencer work you already have language for disclosure and sponsored content. People-search skills sit upstream—they should not invent incentives your compliance team would reject.

---

## Conclusion

**Agent skills for people search** are not a fashion in Markdown. They are where procedural honesty lives—the gap between a clip-friendly demo and a workflow that still runs on a bad Wednesday in quarter-end when the list is due at 4pm. The research layer will keep moving—Tavily-style snippets, fetches, retrieval APIs—but GTM still needs a governed handoff. That is what we ship: opinionated people-and-org tools through **Lessie Skills & CLI** and **People Search for influencer marketing** (entry points are linked in the opening section) on top of the open-web stack you already have. The part that should hold steady is a cited answer and a repeatable path from search to send, with **Lessie** on the last mile when the deliverable is a row, not a paragraph alone. Once a list exists, a practical *what to do next* is to walk it through [a step-by-step influencer marketing checklist (briefs, compliance, follow-through)](/blog/influencer-marketing-checklist) we keep on the blog.

When you want find → enrich → review in front of a GTM team—and not only in a terminal—start from the **Lessie** links in the introduction. You can treat this post as the theory for the engineer who keeps asking why you are not “just” calling a search API and stopping.

---

## FAQ: quick answers, honest limits

**Is a “skill” the same as an MCP tool?** No. A tool is a function the model can call. A skill is how and when to call which tools, and what the return should look like. In most real builds you want both.

**If I have Tavily, do I *need* anything else?** Often yes: something entity-aware for humans, and almost always a dedupe or verify step if the output is rows, not a paragraph of synthesis.

**Is Lessie a replacement for a web search or retrieval API?** Not in a “uninstall everything else” sense. Lessie is the layer we use when the job is people-and-org rows, credits, and enrichment; install and docs are at **lessie.ai/skills-cli** (also linked in the intro). You can still use Tavily-style search for facts and docs; the usual mistake is stopping there and calling it a shortlist.

**What is the #1 way these projects fail?** Unbounded context—paste the SERP into chat and hope. A sound `SKILL.md` says no: cap retrieval, isolate long jobs, return a small structured digest the parent can use.

**Can I use this in hiring without HR review?** Not as a substitute for policy. Skills speed up public research; they do not grant a license to use sensitive attributes your jurisdiction forbids. When in doubt, narrow the skill and widen the human.
