---
title: "What Is Today? — An AI Personal Agent for Your Whole Day"
description: "Today is an AI personal agent with living memory—it remembers your life, notices changes, and acts before you ask. Free Beta on Mac, iOS, and Android."
slug: what-is-today
date: 2026-08-03
author: Today Team
category: Product
secondary_category: AI Personal Agent
---

## TL;DR

- **Today** is an **AI personal agent**—not a chat window you reopen from zero. It keeps a **living, inspectable memory** of your life, notices when your day changes, and can **finish work** in calendar, mail, and notes after you confirm.
- **Living memory** holds people, projects, preferences, and promises between sessions. You can read, edit, or delete any fact.
- **Proactive by default** means a morning brief and evening close-out, held to a strict bar: only what you would have wanted a person to tell you.
- **Connectors** turn suggestions into done—optional, revocable, and scoped to actions Today can actually complete.
- Today is **free during early-access Beta** on Mac, iPhone, and Android.

**Today is an AI personal agent built for continuity, not one-off answers.** Where a chatbot forgets you when the tab closes, Today carries durable context across days and devices, opens onto your schedule instead of a blank prompt, and behaves like an agent that drafts, reschedules, and follows through—always with your confirmation before anything external sends. For the founder's why behind that bet, read [Meet Today](/blog/meet-today).

Most AI tools are brilliant strangers. You open a blank box, re-explain your life, get a paragraph back, and close the window. **Today** is built to break that loop: memory that persists, initiative that respects your attention, and execution that lands in the apps your day already runs on.

## 1. Why We Built an AI Personal Agent

We kept watching the same failure, and it was never a failure of intelligence. People have plenty of model capability on tap; what they lack is **continuity**. Real life is scattered—a trip on the calendar, intent in a note, a promise in a chat from nine days ago, exhaustion in a health app nothing else reads. A tool that only answers prompts cannot see that picture unless you rebuild it every session.

That fragmentation shows up in small ways that compound. You accept a meeting on mobile, but your laptop chat never learns it. You tell one app you are vegetarian and another app suggests steakhouses. You promised a collaborator a draft by Friday in a thread you will not open until Thursday night. Each failure is harmless alone; together they tax the same cognitive budget **personal agents** are meant to return to you.

That is the cost of the blank box: the hardest work—deciding what matters, noticing the 9am move that breaks the next block, remembering the contract due before a flight—stays on you. Generating text afterward is the easy part, and it is the only part most chatbots do. Industry writing increasingly blurs "assistant" and "agent," but the practical split is familiar: reactive help when you drive each turn versus software that pursues goals across tools with your approval. <a href="https://www.ibm.com/think/topics/ai-agents-vs-ai-assistants" rel="nofollow noopener">IBM's distinction between AI assistants and AI agents</a> captures that gap well—assistants answer; agents plan, remember, and act in scope.

An **AI personal agent** is different by design. It is present across time: it remembers, watches for meaningful change, and can act inside your systems when you approve. That is closer to a good human assistant than a smarter search box—and it is the model we built Today around.

> We did not want a smarter chatbot. We wanted an AI personal agent that is with you through the day.

## 2. What Today Actually Is

**Today is an AI personal agent**—a personal AI that combines living memory, proactive signals, and cross-app execution on Mac, iPhone, and Android. The same memory follows you between devices, so a decision on your phone at a bus stop is context your laptop already has an hour later. You are not managing two products; you are carrying one thread through the day.

Three choices define the agent behavior, and each one trades a familiar chat pattern for something harder to build but easier to live with. Memory persists as facts you can inspect, not as an unsearchable scroll. The first screen reflects what is coming and what changed—not a cursor waiting for you to brief the model again. And when Today proposes action, it drafts, finds the slot, or reshuffles the afternoon, then waits for your yes before anything external sends.

Under the hood, that agent loop combines **frontier models**, **task execution**, and **always-on cloud computers** so multi-step work can continue while you are offline. **Community Skills** extend what the agent can do without forcing you to rewrite prompts—install a skill once, and the agent inherits a repeatable workflow. During Beta, which connectors and skills are available may expand; the architecture assumption stays the same: **scoped actions, human confirm, memory that updates after each run.** Reliable agent stacks depend on disciplined scoping and human checkpoints—<a href="https://www.anthropic.com/research/building-effective-agents" rel="nofollow noopener">Anthropic's guidance on building effective agents</a> mirrors the same instincts we apply to calendar and mail. Product demos—living memory, proactive help, and execution capabilities—live on the [Today landing page](/landing).

For the canonical category definition—memory, initiative, confirmation—see [what an AI personal agent is](/blog/what-is-ai-personal-agent). That post names the three-part frame this product implements; this one shows how Today applies it day to day.

## 3. Living Memory: Your Agent Remembers Your Life

Most AI products treat memory as chat history you cannot search—or as vendor-owned context you cannot edit. A personal agent needs something sturdier: facts that persist across weeks, sync across devices, and stay legible when something goes wrong. That is why Today stores **living memory** as structured rows you control, not as an opaque transcript dump.

![A memory panel listing durable facts — a person, a project, a preference, a recurring run — each with edit and delete controls](/blog/images/what-is-today/memory-graph.jpg)

Living memory means your AI personal agent keeps structured facts about your life—not raw chat logs you cannot inspect. Say once that you are vegetarian, that Maya is your co-founder, that you run on Tuesdays and Thursdays; six weeks later, when Today plans a working dinner with Maya, those facts are already in the room. It will not book Tuesday evening, suggest a steakhouse, or ask who Maya is.

Legible memory is non-negotiable for a personal agent. You can open what Today believes about you in plain language, correct any row, or delete a fact—and it stops influencing suggestions immediately. When something surprises you, you can trace which memory row drove it and fix it in seconds. That audit trail is how trust compounds: you are not guessing why the agent behaved a certain way, and you are not locked into facts you outgrew months ago.

Memory rows are stable facts—people, preferences, promises—not verbatim transcripts you cannot search. That distinction matters for privacy and for debugging: when Today misfires, you fix a row, not a vibe. Ecosystem assistants are adding personal context retrieval—<a href="https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/" rel="nofollow noopener">Apple positions Siri AI</a> as grounded in messages, mail, and photos on device—but a personal agent product still has to make those facts **yours to edit**, not buried in vendor silos you cannot inspect.

See [Privacy](/privacy) for HealthKit, Health Connect, and AI provider handling.

## 4. Proactive by Default: The Agent Speaks First

Reactive AI waits for you to notice what broke. A personal agent inverts that posture—within limits. Today speaks first at two daily anchors, morning and evening, because the highest-value moments are often the ones you would have missed until it was too late to fix cheaply.

![A phone showing a morning brief with three highlighted lines and everything else collapsed](/blog/images/what-is-today/morning-brief.jpg)

A personal agent that only answers is a search box with manners. Today speaks first at two daily anchors—not continuously. The morning brief covers the few items that will actually shape the day: a moved meeting, a flight check-in, a deadline that became tomorrow. The evening close-out rolls forward what slipped and asks the one question that decides where it goes.

Restraint matters as much as detection. An agent that surfaces everything it notices becomes notification spam. Our bar: every proactive message must be something you would have wanted a person to tell you. The brief stays short; everything else stays collapsed unless it changed since you last looked and affects a decision you still have time to make. That discipline is why people keep opening Today before mail instead of muting it by Wednesday.

Proactivity here is not autonomy. Today will not send email, move calendar events, or message others without your explicit confirm. The agent's job is to **notice and propose** at the right moment; your job is to apply judgment in one tap or one edit. That line protects trust and keeps the product on the right side of "helpful companion" versus "software that acts on your behalf."

## 5. Connectors: Where Advice Becomes Action

Advice without execution leaves the hard part on you—copy, paste, find the thread, hunt for a slot. Connectors are how a personal agent closes that gap: scoped permissions, confirm-before-send, and actions tied to apps your day already runs on. Today connects to calendar, mail, notes, files, and health sources; each is optional and revocable.

![A suggestion card, a confirm button, then a calendar entry and email draft](/blog/images/what-is-today/connector-action.jpg)

Memory tells the agent what matters; connectors determine what it can finish. Every suggestion is scoped to an action the agent can complete once you say yes—which is why it never proposes moving a meeting it cannot actually move.

In practice, the calendar connector finds real gaps and protects focus blocks you keep losing. Mail lets Today draft in your voice and resurface Friday's thread. Notes pull the right document into the moment you need it. Health signals read sleep and recovery so the plan matches the day you can actually have. Without connectors, Today still works from conversation and builds memory—but the agent does less execution for you.

Consider a client email asking for a revised timeline. Today reads the dates already in your project notes, drafts the reply with those dates—not plausible guesses—and offers to place the new milestone on the calendar in the same motion. You edit one number, confirm, send. The agent handled retrieval, drafting, and scheduling prep; you handled judgment.

Or say you tell Today you are training for a half-marathon on Tuesdays and Thursdays. Six weeks later, after a short sleep reading from HealthKit, it suggests moving a hard interval session—not because a generic template says so, but because memory ties **standing commitments** to **today's recovery signal**. That is personal-agent behavior: facts plus signals plus a scoped proposal, not a one-size wellness paragraph.

During Beta, health integrations follow platform permissions on Apple HealthKit and Android Health Connect; see [Privacy](/privacy) for how inference providers process data.

## 6. AI Personal Agent vs. Chatbot vs. Assistant

**The difference is not answer quality on a well-specified question—it is context, initiative, and execution.** On a narrow prompt, a strong chatbot and Today may sound similar. The gap shows up in everything around the answer: whether Monday's planning shapes Thursday's schedule without a re-brief, whether the product opens on what changed overnight, and whether a suggestion becomes a calendar move after you confirm.

| | Chatbot | Generic AI assistant | Today (AI personal agent) |
| --- | --- | --- | --- |
| Memory | Session-only; you re-brief | Partial / app-specific | Durable, inspectable life memory |
| Initiative | Waits for prompts | Reminders you configure | Proactive when your day changes |
| Reach | Text you execute yourself | Often single-app | Calendar, mail, notes after confirm |
| Output unit | An answer | A suggestion | A day that holds together |

### Enterprise agents, coding agents, and personal agents

**Enterprise agents** optimize shared systems—tickets, CRM stages, approvals—with org permissions. **Coding agents** optimize repositories—files, tests, terminals. A **personal agent** optimizes **individual continuity** across apps never designed to interoperate: calendar, notes, mail, recovery signals. That scope drives different product choices. Enterprise agents emphasize role-based access; coding agents emphasize repo context; personal agents emphasize **memory rows you can edit** and **confirm-before-send** on actions tied to your identity. Today sits in the third bucket.

For a head-to-head on classic assistants versus personal agents—when Siri-style help is enough and when you need living memory—read our guide on [AI personal assistant vs AI personal agent](/blog/ai-personal-assistant-vs-ai-personal-agent). For the split between whole-day continuity and Cowork-style deliverable factories, see [AI personal agent vs work agent](/blog/ai-personal-agent-vs-work-agent).

### When a chatbot is still the better tool

A normal chatbot is enough when you need a **one-off answer** with no lasting context—debugging code, drafting a single email from scratch, or brainstorming options you will paste elsewhere. If you live inside one vendor's ecosystem and rarely need cross-app execution, a general assistant may be simpler than onboarding a personal agent.

Today is built for people whose days span **many apps and many weeks of context**—founders juggling clients, parents managing schedules, anyone tired of re-briefing a blank box every morning. If your week is mostly single-shot Q&A inside one stack, start with an assistant; if dropped promises and calendar drift are the pain, you are shopping for agent behavior.

Personal agents touch sensitive surfaces—mail, health, calendar—so privacy posture matters as much as feature checklists. Today scopes memory to your account, lets you audit rows, and publishes provider handling in [Privacy](/privacy). During early-access Beta, briefs, connectors, and Skills evolve weekly; what you read here reflects direction, not a frozen enterprise SLA. [Join the waitlist](/waitlist) if your platform is not listed yet.

Morning briefs are the habit hook: open Today before mail, scan what changed overnight, approve one or two actions, then start the day. That rhythm is what separates an agent from a bookmark you open only when stuck. Over weeks, the brief learns what you always skim versus what you always act on.

## 7. A Day with Your AI Personal Agent

Here is an ordinary Tuesday, and nothing about it requires heroics—only continuity. At 7:10am Today opens with three lines: your 9am moved to 11am, the design review needs Friday's deck, and you slept five hours—so it already pulled an optional afternoon call and asks if that was right. One line came from a health signal no calendar would read. At 1:40pm a client asks for a timeline change; Today drafts using real project dates and offers to calendar the milestone, and you change one number and send.

At 9:20pm Today asks whether a contract moves to tomorrow or Thursday, remembers you fly Thursday, suggests tomorrow, and you tap once. Notice → remember → propose → confirm: the agent loop in miniature. The same loop applies when nothing dramatic happens—when the agent's value is **preventing** the six manual checks you used to run before breakfast. That prevention is harder to demo in a screenshot but easier to feel after a week of trustworthy briefs.

Wednesday afternoon might bring no crisis—only a gentle nudge that tomorrow's first meeting conflicts with your standing school run, a reminder that a draft is still unshared, and a suggestion to block forty minutes for deep work because sleep was mediocre. None of those require genius; they require **remembering** and **caring about timing**. That is the boring superpower personal agents are for.

## 8. Who Today Is For (and Who Should Wait)

Today fits knowledge workers and creators whose days mix work, health, and life admin—founders tracking clients and travel, writers rebuilding research trails, marathoners balancing training and recovery, young parents calibrating routines. The pattern is the same across roles: memory plus proactive help plus confirm-gated execution. Writers and researchers benefit when the agent rebuilds citation trails and resurfaces sources you saved weeks ago—not when it generates another generic outline.

Founders benefit when investor updates, hiring threads, and product deadlines share one memory graph instead of three siloed chats. Health-minded users benefit when sleep and movement signals reshape today's plan—but only within lifestyle boundaries, not medical claims. If any of that sounds like your week, you are the audience we built for; if not, a lighter assistant may be the smarter first step. Today may not be the right fit when:

- You only need occasional Q&A with no memory or execution across apps.
- You want a fully autonomous agent with no confirmation step—Today always asks before external actions send.
- You need medical diagnosis or clinical advice—Today provides **lifestyle support**, not medical diagnosis (see [Healthcare](/healthcare) for health workflows with appropriate boundaries).

Agents earn trust slowly. If you prefer to experiment without connecting personal data, start with conversation-only mode and add calendar or mail when the memory panel and briefs feel right. That staged onboarding matches how human assistants earn access—not all-at-once blanket permissions. Today is in **early-access Beta** on Mac, iOS, and Android; features may change, and the product is currently free during Beta ([Terms](/terms)).

## Conclusion

Beta is opening in waves. We are deepening connector coverage, exploring shared memory for households, and investing in voice as a first-class input—not a dictation afterthought. Paid plans will come later; Beta users will hear well before anything changes. If you want an **AI personal agent** that remembers your life and acts before you ask—not another chat tab—explore [how Today works on the landing page](/landing), or try the [AI fitness coach](/healthcare/fitness-coach) lifestyle workflow. [Join the waitlist](/waitlist) for early access.

The category will keep evolving as models improve. Our bet is stable: **continuity beats cleverness**, **restraint beats noise**, and **finished beats suggested** when an agent earns access to your calendar and mail. If that matches how you want to live with AI, Today is built for you.

## Frequently asked questions

### What is Today?

Today is an AI personal agent with living memory of your life. It remembers people, projects, and preferences, notices changes across calendar, mail, and health data, and helps proactively—finishing work in your apps after you confirm.

### Is Today an AI assistant or an AI agent?

Both terms appear in marketing, but **agent** is more accurate for what Today does: it persists memory, takes initiative when your day changes, and executes multi-step work with confirmation—not just return text. Assistants excel at on-demand answers; agents carry context forward and act in your apps after you approve.

### Is Today free?

Yes during early-access Beta. Paid plans will come later with advance notice to Beta users. Features may change during Beta—see [Terms](/terms).

### How is my data used?

Memory is scoped to your account and editable by you. See [Privacy](/privacy) for HealthKit, Health Connect, and third-party AI providers used for inference.

### Does Today work without calendar or email connected?

Yes—it builds memory from conversation alone. Connectors unlock execution; each connection is optional and revocable.

### How is Today different from ChatGPT?

ChatGPT excels at open-ended Q&A when you supply context each time. Today keeps durable life memory, opens onto your day, and acts in calendar and mail after you confirm—closer to a personal agent than a blank chat box.
