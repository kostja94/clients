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

**Today is an AI personal agent built for continuity, not one-off answers.** Where a chatbot forgets you when the tab closes, Today carries durable context across days and devices, opens onto your schedule instead of a blank prompt, and behaves like an agent that drafts, reschedules, and follows through—always with your confirmation before anything external sends. If you want the category defined first, read [what an AI personal agent is](/blog/what-is-ai-personal-agent); for the founder's why, see [Meet Today](/blog/meet-today).

Most AI tools are brilliant strangers. You open a blank box, re-explain your life, get a paragraph back, and close the window. **Today** is built to break that loop: memory that persists, initiative that respects your attention, and execution that lands in the apps your day already runs on.

## 1. Why We Built an AI Personal Agent

We kept watching the same failure, and it was never a failure of intelligence. People have plenty of model capability on tap; what they lack is **continuity**. Real life is scattered—a trip on the calendar, intent in a note, a promise in a chat from nine days ago, exhaustion in a health app nothing else reads. A tool that only answers prompts cannot see that picture unless you rebuild it every session.

That fragmentation shows up in small ways that compound. You accept a meeting on mobile, but your laptop chat never learns it. You tell one app you are vegetarian and another app suggests steakhouses. You promised a collaborator a draft by Friday in a thread you will not open until Thursday night. Each failure is "harmless" alone; together they tax the same cognitive budget **personal agents** are meant to return to you.

That is the cost of the blank box: the hardest work—deciding what matters, noticing the 9am move that breaks the next block, remembering the contract due before a flight—stays on you. Generating text afterward is the easy part, and it is the only part most chatbots do.

An **AI personal agent** is different by design. It is present across time: it remembers, watches for meaningful change, and can act inside your systems when you approve. That is closer to a good human assistant than a smarter search box—and it is the model we built Today around.

> We did not want a smarter chatbot. We wanted an AI personal agent that is with you through the day.

## 2. What Today Actually Is

**Today is an AI personal agent**—a personal AI that combines living memory, proactive signals, and cross-app execution on Mac, iPhone, and Android. The same memory follows you between devices, so a decision on your phone at a bus stop is context your laptop already has an hour later.

Three choices define the agent behavior:

**Memory, not transcripts.** What persists is a small set of durable facts about people, projects, and preferences—not an unsearchable chat scroll.

**Day-first, not prompt-first.** The first screen reflects what is coming, what changed, and what needs a decision—not a cursor waiting for you to brief the model again.

**Agent, not oracle.** Today drafts the reply, finds the slot, reshuffles the afternoon, and asks you to confirm before anything leaves your hands.

Under the hood, that agent loop combines **frontier models**, **task execution**, and **always-on cloud computers** (described on the [capabilities section](/landing#capabilities)) so multi-step work can continue while you are offline. **Community Skills** extend what the agent can do without forcing you to rewrite prompts—install a skill once, and the agent inherits a repeatable workflow. During Beta, which connectors and skills are available may expand; the architecture assumption stays the same: **scoped actions, human confirm, memory that updates after each run.**

For a full definition of the category—agent vs assistant vs chatbot—see [what is an AI personal agent](/blog/what-is-ai-personal-agent). For product demos, visit the [Today landing page](/landing): [living memory](/landing#memories), [proactive help](/landing#proactive), and [capabilities](/landing#capabilities).

## 3. Living Memory: Your Agent Remembers Your Life

![A memory panel listing durable facts — a person, a project, a preference, a recurring run — each with edit and delete controls](/blog/images/what-is-today/memory-graph.jpg)

**Living memory means your AI personal agent keeps structured facts about your life—not raw chat logs you cannot inspect.** Say once that you are vegetarian, that Maya is your co-founder, that you run on Tuesdays and Thursdays; six weeks later, when Today plans a working dinner with Maya, those facts are already in the room. It will not book Tuesday evening, suggest a steakhouse, or ask who Maya is.

Legible memory is non-negotiable for a personal agent. You can open what Today believes about you in plain language, correct any row, or delete a fact—and it stops influencing suggestions immediately. When something surprises you, you can trace which memory row drove it and fix it in seconds.

**Memory rows are not chat exports.** They are stable facts—people, preferences, promises—not verbatim transcripts you cannot search. That distinction matters for privacy and for debugging: when Today misfires, you fix a row, not a vibe.

See [Privacy](/privacy) for HealthKit, Health Connect, and AI provider handling.

## 4. Proactive by Default: The Agent Speaks First

![A phone showing a morning brief with three highlighted lines and everything else collapsed](/blog/images/what-is-today/morning-brief.jpg)

**A personal agent that only answers is a search box with manners.** Today speaks first at two daily anchors—not continuously. The morning brief covers the few items that will actually shape the day: a moved meeting, a flight check-in, a deadline that became tomorrow. The evening close-out rolls forward what slipped and asks the one question that decides where it goes.

Restraint matters as much as detection. An agent that surfaces everything it notices becomes notification spam. Our bar: every proactive message must be something you would have wanted a person to tell you. The brief stays short; everything else stays collapsed unless it changed since you last looked and affects a decision you still have time to make.

## 5. Connectors: Where Advice Becomes Action

![A suggestion card, a confirm button, then a calendar entry and email draft](/blog/images/what-is-today/connector-action.jpg)

**Memory tells the agent what matters; connectors determine what it can finish.** Today connects to calendar, mail, notes, files, and health sources (each optional and revocable). Every suggestion is scoped to an action the agent can complete once you say yes—which is why it never proposes moving a meeting it cannot actually move.

In practice: the calendar connector finds real gaps and protects focus blocks you keep losing; mail lets Today draft in your voice and resurface Friday's thread; notes pull the right document into the moment you need it; health signals read sleep and recovery so the plan matches the day you can actually have. Without connectors, Today still works from conversation and builds memory—but the agent does less execution for you.

**Example:** A client email arrives asking for a revised timeline. Today reads the dates already in your project notes, drafts the reply with those dates—not plausible guesses—and offers to place the new milestone on the calendar in the same motion. You edit one number, confirm, send. The agent handled retrieval, drafting, and scheduling prep; you handled judgment.

**Example:** You tell Today you are training for a half-marathon on Tuesdays and Thursdays. Six weeks later, after a short sleep reading from HealthKit, it suggests moving a hard interval session—not because a generic template says so, but because memory ties **standing commitments** to **today's recovery signal**. That is personal-agent behavior: facts plus signals plus a scoped proposal, not a one-size wellness paragraph.

During Beta, health integrations follow platform permissions on Apple HealthKit and Android Health Connect; see [Privacy](/privacy) for how inference providers process data.

## 6. AI Personal Agent vs. Chatbot vs. Assistant

**The difference is not answer quality on a well-specified question—it is context, initiative, and execution.** On a narrow prompt, a strong chatbot and Today may sound similar. The gap shows up in everything around the answer.

| | Chatbot | Generic AI assistant | Today (AI personal agent) |
| --- | --- | --- | --- |
| Memory | Session-only; you re-brief | Partial / app-specific | Durable, inspectable life memory |
| Initiative | Waits for prompts | Reminders you configure | Proactive when your day changes |
| Reach | Text you execute yourself | Often single-app | Calendar, mail, notes after confirm |
| Output unit | An answer | A suggestion | A day that holds together |

### Enterprise agents, coding agents, and personal agents

**Enterprise agents** optimize shared systems—tickets, CRM stages, approvals—with org permissions. **Coding agents** optimize repositories—files, tests, terminals. A **personal agent** optimizes **individual continuity** across apps never designed to interoperate: calendar, notes, mail, recovery signals.

That scope drives different product choices. Enterprise agents emphasize role-based access; coding agents emphasize repo context; personal agents emphasize **memory rows you can edit** and **confirm-before-send** on actions tied to your identity. Today sits in the third bucket—the category frame is in [What is an AI personal agent?](/blog/what-is-ai-personal-agent).

### When a chatbot is still the better tool

A normal chatbot is enough when you need a **one-off answer** with no lasting context—debugging code, drafting a single email from scratch, or brainstorming options you will paste elsewhere. If you live inside one vendor's ecosystem and rarely need cross-app execution, a general assistant may be simpler than onboarding a personal agent.

Today is built for people whose days span **many apps and many weeks of context**—founders juggling clients, parents managing schedules, anyone tired of re-briefing a blank box every morning. A deeper head-to-head comparison is planned; until then, see [landing use cases](/landing#use-cases) for role-based examples.

**Privacy posture matters in this comparison.** Personal agents touch sensitive surfaces—mail, health, calendar. Today scopes memory to your account, lets you audit rows, and publishes provider handling in [Privacy](/privacy). Choose tools that document inference and connection policies, not only feature checklists.

**Beta expectations:** Today is early-access software. Briefs, connectors, and Skills evolve weekly; what you read here reflects direction, not a frozen enterprise SLA. Join the [waitlist](/waitlist) if your platform is not listed yet.

For the category definition behind this product—memory, initiative, confirmation—read [What Is an AI Personal Agent?](/blog/what-is-ai-personal-agent). For the founder story, read [Meet Today](/blog/meet-today).

**Who should wait:** If you need a stateless Q&A bot for one-off research, a personal agent adds weight you do not need. If your week repeats across people, promises, and calendars, the overhead pays back quickly.

Morning briefs are the habit hook: open Today before mail, scan what changed overnight, approve one or two actions, then start the day. That rhythm is what separates an agent from a bookmark you open only when stuck. Over weeks, the brief learns what you always skim versus what you always act on.

## 7. A Day with Your AI Personal Agent

Here is an ordinary Tuesday. At 7:10am Today opens with three lines: your 9am moved to 11am, the design review needs Friday's deck, and you slept five hours—so it already pulled an optional afternoon call and asks if that was right. One line came from a health signal no calendar would read.

At 1:40pm a client asks for a timeline change. Today drafts using real project dates and offers to calendar the milestone. You change one number and send.

At 9:20pm Today asks whether a contract moves to tomorrow or Thursday, remembers you fly Thursday, suggests tomorrow. You tap once. Notice → remember → propose → confirm: the agent loop in miniature.

The same loop applies when nothing dramatic happens—when the agent's value is **preventing** the six manual checks you used to run before breakfast. That prevention is harder to demo in a screenshot but easier to feel after a week of trustworthy briefs.

**Midweek example:** Wednesday afternoon, no crisis—only a gentle nudge that tomorrow's first meeting conflicts with your standing school run, a reminder that a draft is still unshared, and a suggestion to block forty minutes for deep work because sleep was mediocre. None of those require genius; they require **remembering** and **caring about timing**. That is the boring superpower personal agents are for.

## 8. Who Today Is For (and Who Should Wait)

**Today fits knowledge workers and creators whose days mix work, health, and life admin**—founders tracking clients and travel, writers rebuilding research trails, marathoners balancing training and recovery, young parents calibrating routines. The [landing use cases](/landing#use-cases) spell out nine role sketches with the same agent pattern: memory plus proactive help.

**Writers and researchers** benefit when the agent rebuilds citation trails and resurfaces sources you saved weeks ago—not when it generates another generic outline. **Founders** benefit when investor updates, hiring threads, and product deadlines share one memory graph instead of three siloed chats. **Health-minded users** benefit when sleep and movement signals reshape today's plan—but only within lifestyle boundaries, not medical claims.

**Today may not be the right first step if:**

- You only need occasional Q&A with no memory or execution across apps.
- You want a fully autonomous agent with no confirmation step—Today always asks before external actions send.
- You need medical diagnosis or clinical advice—Today provides **lifestyle support**, not medical diagnosis (see [Healthcare](/healthcare) for health workflows with appropriate boundaries).

**Agents earn trust slowly.** If you prefer to experiment without connecting personal data, start with conversation-only mode and add calendar or mail when the memory panel and briefs feel right. That staged onboarding matches how human assistants earn access—not all-at-once blanket permissions.

**Community Skills** (see [capabilities](/landing#capabilities)) extend the agent without prompt engineering: install a workflow once, reuse it when similar tasks appear. That composability is part of why we classify Today as an agent rather than a static assistant.

Today is in **early-access Beta** on Mac, iOS, and Android. Features may change; the product is currently free during Beta ([Terms](/terms)).

## Conclusion

Beta is opening in waves. We are deepening connector coverage, exploring shared memory for households, and investing in voice as a first-class input—not a dictation afterthought. Paid plans will come later; Beta users will hear well before anything changes.

If you want an **AI personal agent** that remembers your life and acts before you ask—not another chat tab—explore [how Today works](/landing), read [what an AI personal agent is](/blog/what-is-ai-personal-agent), or try the [AI fitness coach](/healthcare/fitness-coach) lifestyle workflow. [Join the waitlist](/waitlist) for early access.

The category will keep evolving as models improve. Our bet is stable: **continuity beats cleverness**, **restraint beats noise**, and **finished beats suggested** when an agent earns access to your calendar and mail. If that matches how you want to live with AI, Today is built for you.

## Frequently asked questions

### What is Today?

Today is an AI personal agent with living memory of your life. It remembers people, projects, and preferences, notices changes across calendar, mail, and health data, and helps proactively—finishing work in your apps after you confirm.

### Is Today an AI assistant or an AI agent?

Both terms appear in marketing, but **agent** is more accurate for what Today does: it persists memory, takes initiative when your day changes, and executes multi-step work with confirmation—not just return text. See [what is an AI personal agent](/blog/what-is-ai-personal-agent) for how we define the category.

### Is Today free?

Yes during early-access Beta. Paid plans will come later with advance notice to Beta users. Features may change during Beta—see [Terms](/terms).

### Which platforms does Today run on?

Mac (macOS 15+), iPhone/iPad (TestFlight), and Android (APK). Memory syncs across devices. Get builds on the [downloads page](/downloads).

### How is my data used?

Memory is scoped to your account and editable by you. See [Privacy](/privacy) for HealthKit, Health Connect, and third-party AI providers used for inference.

### Does Today work without calendar or email connected?

Yes—it builds memory from conversation alone. Connectors unlock execution; each connection is optional and revocable.

### How is Today different from ChatGPT?

ChatGPT excels at open-ended Q&A when you supply context each time. Today keeps durable life memory, opens onto your day, and acts in calendar and mail after you confirm—closer to a personal agent than a blank chat box.

### What makes an AI personal agent different from a workflow automation tool?

Workflow tools like Zapier excel when triggers and actions are **fixed**. Personal agents handle **ambiguous life context**—the meeting move that implies three downstream changes, the email that only makes sense beside last week's notes. Today combines memory, judgment, and connectors instead of a rigid if-this-then-that graph you maintain yourself.

### Does Today replace my existing AI tools?

Not necessarily. Many people keep a general chat model for one-off research and use Today as the **personal agent layer** for days, memory, and cross-app execution. The category definition in [What is an AI personal agent?](/blog/what-is-ai-personal-agent) explains when each tool type fits.
