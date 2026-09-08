---
title: "MeDo Speaks SKILL.md: Custom Skills for Any AI Workflow"
description: "Upload a standard SKILL.md and MeDo turns it into a usable capability — in chat, in app building, or from external agents like OpenClaw."
slug: "medo-launches-custom-skills"
date: 2026-09-11
author: "Kostja"
category: "Product"
secondary_category: "Features"
---

# MeDo Speaks SKILL.md: Custom Skills for Any AI Workflow

## TL;DR

- **Custom skills on MeDo run on the open SKILL.md format the rest of the agent ecosystem uses**: upload a `.zip` skill package or a single `SKILL.md`, and MeDo parses it into a usable capability you call in chat or while building an app.
- **The standard works both ways**: MeDo imports SKILL.md packages as custom skills, and its own App Builder skill on ClawHub lets self-hosted OpenClaw agents create, update, and publish MeDo apps through natural language.
- **Official skills are Prompt-based or API-based** and cover AI, voice, image, payment, search, and office productivity; credit-consuming ones come with a daily free quota — one video-generation call, five image calls, and 100 for everything else.
- **The entry points got faster**: `@` invocation and a skill picker below the chat box arrived in August; in-chat skill configuration followed in September.

The bottom line: a capability in the standard format now moves into MeDo and out of it — bring a SKILL.md and MeDo runs it; run MeDo's App Builder skill and your own agent builds apps. The symmetry is the point: one format, two directions.

If you have spent time with any AI coding agent this year, you already know the shape: a folder containing a `SKILL.md` — frontmatter with a name and description, plain-Markdown instructions, and optionally supporting scripts and references. That folder is a *skill*, a reusable capability an agent loads only when a task calls for it. What began as one vendor's internal format has, in under a year, become the closest thing agent workflows have to a shared language.

MeDo has been building on that language since June, and the pattern runs in both directions: packages come in, a skill goes out. This article connects those releases into one picture — MeDo consumes the open standard, and MeDo ships on it.

## 1. How a Markdown file became the common language of agent capabilities

SKILL.md became a standard because capabilities needed to travel between agents the way files travel between computers — and the ecosystem agreed on the container within about three months. A skill is a directory that must contain `SKILL.md`, whose frontmatter requires only `name` and `description`; license, compatibility, and metadata fields are optional, and supporting files live in optional `scripts/`, `references/`, and `assets/` folders.

The load model is what made adoption painless. Agents see only a short metadata block for every installed skill up front, load the full body when a skill matches the task, and read reference files on demand — so you can install hundreds of skills without drowning the model's context, per the <a href="https://agentskills.io/specification" rel="nofollow noopener">open agent-skills specification</a>. Anthropic introduced the format in October 2025 and opened it as a vendor-neutral standard in December 2025; OpenAI, Microsoft, and Google's Gemini CLI followed within weeks, and a <a href="https://denser.ai/blog/agent-skills-guide/" rel="nofollow noopener">community survey</a> counted more than 280,000 published skills by February 2026 across more than two dozen agents. Vercel's `npx skills` CLI became a common way to install a skill straight from a Git repository — write once, run in any supporting agent.

## 2. What Skills looks like inside MeDo

Inside MeDo, Skills is a first-class surface rather than a developer setting: browse official skills in the Skill Center, add your own custom skills, and use any of them in a conversation or while generating an app. For people who direct an AI builder in plain language — the [vibe-coding workflow](/blog/what-is-vibe-coding) MeDo is built around — a skill removes the need to re-describe your workflow each time: you invoke one packaged capability that already knows the details.

Official skills come in two kinds. Prompt-based skills carry a predefined prompt that keeps the model focused on a type of task, such as translation or OCR. API-based skills connect to external services for real-time data or third-party capabilities, and they can be wired into an app so the product you generate uses the service too. Together they span AI, voice, image, payment, search, and office productivity; MeDo picks the right one from context, or you specify it yourself with `@`.

Credit-consuming official skills run against a daily free quota — one video-generation call, five image calls, and 100 calls for everything else, as of September 2026. The free allowance is used first, resets at 00:00, and does not carry over; once exhausted, skills that normally consume credits charge their standard credit price, which the Skill Center shows.

## 3. Custom Skills: bring your own SKILL.md

A custom skill starts with a file you may already own. Under **Skills → My Skills → Create Skill**, you upload a `.zip` skill package or a bare `SKILL.md`; MeDo parses it — usually within a minute — and generates the skill definition and configuration for you:

1. Upload the `.zip` package or `SKILL.md` file.
2. Review the generated name, icon, and description, and add environment variables the skill needs, such as an API key.
3. Create the skill and invoke it with `@` to test it.
4. Check the Used Skills list, then reuse it across apps and tasks — or manage and delete it later in My Skills.

Two details shape what you can upload. The package must follow the ecosystem's standard structure: `SKILL.md` is required, `scripts/`, `references/`, and `assets/` are optional, the file name is case-sensitive, and a `.zip`'s root directory must match the lowercase-hyphen `name` in the frontmatter. The skill definition MeDo generates is derived from the package rather than hand-editable — if the result does not fit, you adjust the source files and re-upload, as the <a href="https://docs.medo.dev/11-integrations/03-custom-skills.html" rel="nofollow noopener">Custom Skills guide</a> details.

MeDo does not yet offer a create-from-blank form for custom skills. If you have no package, you scaffold one conversationally: mention the `@Skill Creation & Editing` skill with an API description or documentation link, and MeDo produces a downloadable skill package you then import — or, for a single API, hand MeDo the API description directly in chat to integrate the service. The file becomes the artifact you keep and version, exactly as in the rest of the ecosystem.

## 4. Two faster ways to reach a skill: `@` and in-chat configuration

You should not have to remember which skills exist mid-request, so MeDo surfaces them where you type. Since August, the toolbar below the chat box opens the Skills list in one tap, and typing `@` in the conversation does the same — official and custom skills both appear, custom first.

September added configuration without leaving the thread: when a conversation needs a user or custom skill, the Skills configuration entry inside the conversation manages it on the spot. The changes are tracked in the <a href="https://docs.medo.dev/changelog.html" rel="nofollow noopener">MeDo changelog</a>; together they complete the loop — import once, reach a skill in seconds, tune it mid-conversation.

## 5. The other direction: MeDo ships as a skill other agents install

The ecosystem story is not one-way. The <a href="https://docs.medo.dev/13-medo-skill.html" rel="nofollow noopener">MeDo App Builder skill</a> is published on <a href="https://docs.openclaw.ai/tools/clawhub" rel="nofollow noopener">ClawHub</a>, the skill registry for OpenClaw, a self-hosted open-source agent. An OpenClaw user installs it from the CLI — `openclaw skills install @seiriosplus/medo-app-builder` — sets a `MEDO_API_KEY` in the environment, and then talks to their agent in natural language to list apps, inspect projects, create new MeDo apps, iterate on them, and publish to a production URL.

The capability set matters less than what it proves. The same folder standard that lets MeDo parse a third-party package is what lets a third-party agent load MeDo — identical conventions, identical expectations about discovery and invocation. MeDo is not an island that imports the format; it is a node on the same network, publishing to the same registries its users pull from. That is the part no proprietary integration could replicate as cleanly.

## 6. Managed parsing, not blind installs: where the boundary sits

One distinction deserves to be explicit because "skills" covers two operating models that behave differently. When you upload a package to MeDo, the platform parses the definition, stores credentials through its own configuration, and runs the capability in the managed builder environment — the same trust posture as any MeDo feature. When a local agent downloads third-party skill packages and executes their scripts on your machine, the trust boundary sits on your computer instead.

The community survey cited earlier also notes that a meaningful share of published skills carry vulnerabilities, so the standing advice for local agents is to review a skill's source before running it, as you would any installed code. That is not a claim that managed platforms are risk-free, nor a critique of local agents — it is simply where each model puts the boundary. The files are identical; the environment that executes them is not.

## Conclusion

Three releases over one summer — Custom Skills in June, `@` invocation in August, in-chat configuration in September — add up to one capability: MeDo treats the open SKILL.md standard as its skill format, and the open ecosystem treats MeDo as a skill. Knowledge you already packaged for other agents is no longer stranded when you build an app, and the agents you run locally can reach the apps you build here. It pairs with the [built-in SEO Agent](/blog/medo-launches-ai-seo-agent), covered in its own post earlier this week — agent capabilities are becoming a product line of their own rather than a footnote to the builder.

The fastest way to feel the difference is small: take a SKILL.md you already use elsewhere, upload it under My Skills, and ask MeDo to apply it to a task or an app. Then install the MeDo App Builder skill into a self-hosted agent and see the same standard from the other side. Everything you need is on the [MeDo features page](/features).

## Frequently asked questions

### Can I create a custom skill from scratch inside MeDo, or is a file required?

A file is the starting point today — MeDo has no create-from-blank form. Upload a `.zip` skill package or a bare `SKILL.md`, and MeDo builds the skill definition and configuration from it. If you do not have a package, start the other way: mention the `@Skill Creation & Editing` skill with an API description or documentation link, and MeDo generates a downloadable package you then import.

### Is uploading a SKILL.md to MeDo the same as installing a skill into a local agent?

Not quite — the same file, two different execution models. Uploading to MeDo puts the parsed definition and any credentials into platform configuration, and the skill runs in MeDo's managed environment. Installing locally downloads the package and executes its scripts on your machine. Review the source either way; with a local agent the review is on you, because the trust boundary sits on your computer rather than on the platform.

### Will a custom skill I upload also work in Claude Code, Cursor, or other agents?

The package is the standard format, so the same files can be loaded by any agent that supports SKILL.md — MeDo does not lock the format you bring in. The skill definition and configuration MeDo generates are specific to how MeDo runs the skill; the uploaded package itself stays portable, which is the point of the open standard.

### Do official skills cost anything?

Only beyond a daily free allowance. Credit-consuming official skills include free quota — one video-generation call, five image calls, and 100 calls for other skills per day, as of September 2026. MeDo spends the free allowance first; it resets at 00:00 and does not roll over. Once exhausted, a skill charges its normal credit price, listed in the Skill Center, and you can cap a project's use by setting a daily invocation limit.

### Do my custom skills need API keys?

Only when a skill calls an external service that requires one. After parsing, MeDo shows an environment-variables section for keys defined in the package; fill them in at creation, or leave them empty and configure them later when the skill is used in a project. Values are read securely at run time and are not exposed in the conversation.

### Can I use a custom skill inside the apps I build, not just in chat?

Yes. Invoke the skill while describing an app and MeDo uses it during generation; the project's Used Skills list shows which skills fired. Removing a skill from an app stops the app from using it, and deleting a custom skill in My Skills prevents new projects from using it while existing ones keep working.
