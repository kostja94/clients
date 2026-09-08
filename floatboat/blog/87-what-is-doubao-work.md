---
title: "What Is Doubao Work? ByteDance's AI Office Agent, Explained"
description: "Doubao Work is ByteDance's AI office agent - Windows desktop control, Feishu integration, cloud-PC tasks - compared with WorkBuddy, Qwen Work, and Floatboat."
slug: "what-is-doubao-work"
date: 2026-08-26
author: "Kostja"
category: "Research"
standalone: true
---

## TL;DR

- **Doubao Work** is ByteDance's standalone AI office product at doubao.com/work. ByteDance took the "work tasks" capability buried inside Doubao and made it its own brand: not just answering questions, but planning steps, calling tools, operating software, and handing back usable deliverables.
- You describe a goal in natural language, and the agent keeps executing on your **local computer** (a Windows virtual desktop), in a **cloud PC**, or in the browser.
- Versus chat-first Doubao, the difference is the **execution layer**; versus domestic rivals Tencent WorkBuddy and Alibaba Qwen Work, the difference is the **Feishu ecosystem**; versus [Floatboat](https://floatboat.ai/), it is **Feishu/IM context versus calendar-driven, proactive execution**.
- The **Team edition** signs in with Feishu enterprise accounts and inherits organizational permissions and collaboration context — ByteDance's main vehicle for enterprise AI office.
- **There is no international version of Doubao Work.** The overseas general assistant is Dola (dola.com), which does not offer office agents or Feishu integration at Doubao Work's level.

---

## 1. Why Doubao Work Exists

### 1.1 From "chatting" to "doing"

Plenty of AI assistants can already write a report or produce an image, yet the everyday workflow still ends the same way: copy and paste, open WPS yourself, file folders manually, create the task in Feishu by hand. The model gives you an answer — **the last few steps are still yours**.

ByteDance Seed's official explanation is blunt about it: once you enter productivity scenarios, users rarely need a single answer; they need a model that **keeps working toward a goal and produces a usable result**. Real work also doesn't happen in one interface — it jumps between chat, search, the browser, code repositories, files, and external tools. Doubao Work exists to close that gap between **suggestion and delivery**.

When you send a task instruction and enable local-computer or browser automation permissions, Doubao understands the instruction, plans the steps, and executes them itself — file reads and writes, web actions, software automation, batch processing. These instructions count as authorization from you; anything touching money, identity, or high-risk system access still requires your own sign-off.

### 1.2 How Doubao Work Differs From Doubao and Dola

| Product | For whom | What it mainly does |
|------|----------|------------|
| **Doubao** | Mainland China users | Chat, search, creation, light office work |
| **Doubao Work** | Individuals and Feishu teams | Complex task execution, local/cloud-PC control, enterprise collaboration |
| **Dola** | Overseas users | Multilingual chat, writing, translation, image and creation |

**Dola is not the overseas version of Doubao Work.** Dola is a general everyday assistant — no office-agent entry point, and none of Doubao Work's local computer control or Feishu team integration. The accurate framing is: **ByteDance has Dola, but there is no overseas Doubao Work.**

Doubao Work does not replace Doubao. It is the **office-specific entry point** extending from it — heavy execution, desktop control, and Feishu context live in Doubao Work; everyday Q&A and creation stay in Doubao.

---

## 2. Why ByteDance Made It a Separate Product

This is the key to understanding Doubao Work: **it is not another mode inside the Doubao app — it is ByteDance's product split in the AI office race.**

### 2.1 Chat Products and Work Products Set Different Expectations

Inside Doubao, the implicit contract is "quick Q&A, interruptible anytime, lightweight creation." An office agent has the opposite contract: "hand over a goal, walk away, come back to inspect results." Tasks can run ten minutes or half an hour, manipulate local files, span multiple applications, and read and write Feishu data within team permission boundaries.

Squeezing both expectations into one entry point creates three problems:

**High discovery cost** — a user who wants "AI to operate my computer" has to dig a "work tasks" feature out of a chat app's menu tree. **Blurry brand** — it is hard to say in one sentence whether Doubao is a chatbot or an office agent. **Hard to monetize separately** — office tasks burn far more compute than ordinary conversation and need their own subscription tiers, team seats, and enterprise governance, which don't share a ledger with a consumer chat membership.

Splitting Doubao Work into its own brand is ByteDance telling the market: **this is a work tool — evaluate it with its own client, its own site, and its own pricing.**

### 2.2 Model Capability Reached the Point Where Product Splitting Was Inevitable

Seed's official release notes for the 2.1 line stress that high-value work tasks require the model to take part in data analysis, solution design, content planning, and results organization, and to keep improving along the Computer-Use Agent direction across environments and tools. TRAE Work, the "work tasks" mode inside Doubao, and later Doubao Work are the same capability line landing in product forms that can **deliver verifiable outcomes**.

When a model evolves from "writes well" to "finishes the job," the product organization has to evolve too — from "one app does everything" to "chat entry + office entry + coding entry." Doubao Work is the flag carrier for the office lane.

### 2.3 Feishu Enterprise Scenarios Need Their Own Product Boundary

The user agreement splits Doubao into personal and enterprise editions. The enterprise edition includes the Doubao Work client and in-Feishu Doubao features, requires a Feishu account, and lets organizations manage member identities and permissions.

The Team edition's positioning: deep Feishu integration that unifies team knowledge so you **don't have to re-explain background on every task**; access limited by Feishu's enterprise permissions to content members are actually allowed to see; and deliverables written straight back into Feishu collaboration instead of exported and re-imported.

A consumer chat product's interaction and compliance model can't carry all of that. A separate brand with team/enterprise subscriptions lets IT buy by **seat, audit trail, and training-data opt-out** — rather than having employees subscribe to a chat membership and "incidentally" operate company files.

### 2.4 TRAE and Coze Needed a Unified Office Exit

Seed's notes also tie the Doubao office-task mode to model access from TRAE Work and the TRAE IDE. If the office agent, the coding agent, and the Coze skill platform each fight their own war, enterprise customers end up with three accounts, three permission systems, and three bills.

As **ByteDance's unified brand for AI office**, Doubao Work pulls "work tasks" out of the Doubao app and gathers Feishu's component capabilities, the TRAE coding line, and Coze's skill ecosystem into one narrative. From the user's side the map is simple: chat with Doubao, work with Doubao Work, code with TRAE, and publish skills into Doubao Work's team library.

### 2.5 Competition Forced the Issue: Office Agents Are Already Their Own Category

By 2026, Tencent WorkBuddy and Alibaba Qwen Work had both launched or opened public testing as **standalone desktop workstations with their own websites**. If ByteDance kept its strongest office agent two levels deep inside the Doubao app's menu, it would start the "AI office entry point" race at a structural disadvantage.

**A standalone product is also a standalone claim on a search intent and a desktop install slot** — competing on the same table as WorkBuddy and Qwen Work, rather than borrowing a tab inside a super app to compare.

---

## 3. What Doubao Work Is

### 3.1 A One-Sentence Definition

> **Doubao Work is an AI office agent built on Doubao's foundation models: you state the goal, and the system breaks it into tasks itself, picks the tools (local computer, cloud PC, browser, office suite, skills, and connectors), and keeps executing until it hands back finished documents, spreadsheets, decks, or web pages.**

Explaining it to a colleague: **like an intern who knows how to use a computer — you say what you need done, it opens the software, finds the files, fills in the table, and you do the final review.**

### 3.2 Four Core Characteristics

**(1) Delivery-oriented.** Output is an editable file or a Feishu cloud document — not a paragraph that says "here's how you might structure your deck."

**(2) Two run modes: local and cloud.** Local software and private files stay on a **local virtual desktop**; long-running or scheduled jobs go to a **cloud PC**. The mobile app can **dispatch tasks remotely** to a machine you've authorized.

**(3) Skills and connectors.** Built-in skills cover earnings-call analysis, contract drafting, deck creation, and more; connectors reach Feishu, DingTalk, WeCom, and Tencent Meeting. The Team edition can additionally call Feishu messages, calendar, docs, spreadsheets, and the knowledge base.

**(4) Organizational context (Team edition).** After signing in with a Feishu enterprise account, it reads org structure, group chats, documents, and tasks **within permission boundaries**, and writes results back into the collaboration flow.

### 3.3 "Doubao Office" vs. "Doubao Work"

In everyday speech, "Doubao Office" usually means the "work tasks / office tasks" mode inside the Doubao app. **"Doubao Work" is the official standalone brand released in August 2026**, with its own site (doubao.com/work) and a separate desktop client. Same product line, two stages of naming.

### 3.4 How to Install It and Where to Enter

- **Website** doubao.com/work: download the Windows / macOS desktop app.
- **Doubao app**: the work-tasks mode still exists and is gradually aligning with the standalone client.
- **Inside Feishu**: enterprise users get an embedded experience; Feishu sign-in unlocks the Team capabilities.
- **Mobile**: dispatch tasks remotely to an authorized computer — not full desktop control from the phone.

### 3.5 What It Is Not

- Not a renamed chat Doubao.
- Not overseas Dola.
- Not hands-off full automation — authorization and high-risk steps still need human sign-off.
- Not an open platform for arbitrary models — the personal edition primarily uses ByteDance's own models, with paid tiers offering access to Doubao 2.1 Pro and similar (check the client for details).
- Not a calendar agent that runs pre-meeting prep by default — only when you start a task or configure a scheduled one.

---

## 4. How the Capabilities Actually Land

### 4.1 Local Virtual Desktop (Windows-First)

On Windows, Doubao Work opens a dedicated virtual desktop where the agent sees the screen, moves the mouse, clicks, and types: organizing files, converting WPS documents to PDF, moving data between apps.

The hard part is exception handling — expired logins, CAPTCHAs, version differences between applications. The official guidance is to rehearse on non-sensitive files first and learn the authorization boundaries before touching important data. Local mode can **reuse your browser's login state**, which suits intranet OA and other scenarios a pure API can't cover.

### 4.2 Cloud PC and Remote Dispatch

Use the cloud PC for scheduled collection, batch processing, and workflows that need to finish after your machine is off. **Private data and local software stay local; long-running and compute-heavy jobs go to the cloud.** Subscription tiers and quotas are as shown on the official pricing page and in the client.

### 4.3 Skills, Connectors, and Work Teammates

The Team edition highlights four blocks: **rich work delivery** (from documents to system applications), **unified team knowledge** (connecting Feishu data sources), **native Feishu integration**, and **clear permissions** (only content you're allowed to see; results written back to Feishu). Teams can also save a validated workflow as a **Skill** and share it across the organization.

### 4.4 Multimodal Delivery

Backed by Seedream and Seedance, Doubao Work can produce Word, Excel, PPT, images, video, and data-rich web pages within one task. When signed in through Feishu, deliverables can land directly as Feishu cloud documents.

---

## 5. Competitive Landscape: Doubao Work vs. WorkBuddy vs. Qwen Work vs. Floatboat

In 2026 the AI office-agent market runs along at least two main lines: **Chinese big tech grows the agent into its IM/document ecosystem** (Doubao Work, WorkBuddy, Qwen Work), and **Calendar-Driven AI grows the agent into the calendar runtime** (led by [Floatboat](https://floatboat.ai/)). All of them share the shape "natural-language goal → multi-step execution → verifiable delivery." They differ on **trigger, collaboration substrate, and whose context is inherited by default**.

### 5.1 Four-Way Positioning

| Dimension | Doubao Work | Tencent WorkBuddy | Alibaba Qwen Work | [Floatboat](https://floatboat.ai/) |
|------|----------|----------------|--------------|-------------------------------------|
| **Official positioning** | A new teammate for team work; deeply integrated with Feishu | All-scenario AI office workstation | One-stop AI office for individuals and enterprises | Calendar-as-runtime Proactive Agent OS |
| **Collaboration / context** | Feishu (native in the Team edition) | Tencent Docs, WeCom, QQ, WeChat | DingTalk (in-DingTalk + deep integration) | Google/Outlook/Lark calendars and ICS; event-level workspaces |
| **Trigger** | User initiates tasks; Team edition reads Feishu context | User initiates; remote dispatch via IM | User initiates; scheduled tasks in the cloud | **Calendar events trigger automatically** (pre-meeting prep, deadlines, post-meeting follow-up) |
| **Desktop agent** | Local virtual desktop + cloud PC | Local file reads/writes in authorized directories | Desktop computer control + cloud agent | Mac/Windows desktop; Combo Skills run on events/schedules |
| **Typical users** | Feishu teams; mainland content/office teams | Tencent-ecosystem IM/docs teams | DingTalk organizations; e-commerce/multi-device scenarios | Independent founders, consultants, cross-timezone calendar users |
| **Signature difference** | Feishu permissions + ByteDance multimodal stack | Broad IM reach; large expert/Skill library | Native DingTalk + web publishing | **Proactive execution, cross-calendar, not tied to one IM** |

The table is compiled from each company's official site and product documentation. For the Floatboat column, see our definitions of [Agentic Calendar](/blog/what-is-agentic-calendar) and [Calendar-Driven AI vs. Chat AI](/blog/calendar-driven-ai-vs-chat-ai).

### 5.2 Tencent WorkBuddy: A "Desktop Colleague" Inside the Tencent Ecosystem

Tencent Cloud officially defines WorkBuddy as an **all-scenario AI office workstation**: you describe a need in everyday language, and it thinks on its own, breaks the task down, plans steps, and **delivers a directly verifiable work result** — as opposed to "traditional AI that only chats and gives advice."

Official capabilities include:

- **Natural-language understanding**, with no special command syntax required.
- **Autonomous planning and execution** — complex tasks split into multiple steps, calling tools and self-checking along the way.
- **Multimodal processing** — documents, spreadsheets, PPTs, data analysis, and more.
- **Local file operations** — reading, writing, and batch processing within authorized directories.
- **100+ built-in domain experts** and **70,000+ Skills**, covering recruiting, investment research, legal, marketing, and more.
- **Continuous cloud execution** — long-running tasks keep going after you close the client.
- **IM reach** — dispatch tasks remotely through WeChat, WeCom, QQ, and other channels (enterprise capabilities per official docs).

WorkBuddy Enterprise is Tencent Cloud's one-stop agent platform for enterprises, sitting alongside CodeBuddy (intelligent coding) in a "coding + office + agent hosting" matrix, with support for Hunyuan and multiple models.

**Doubao Work vs. WorkBuddy:** WorkBuddy's strengths are **full coverage of the Tencent IM and document ecosystem, the expert/Skill library scale, and multi-model plus enterprise private deployment**; Doubao Work's strengths are **native Feishu data and permissions, the Seed multimodal pipeline, and the Windows virtual desktop**. Teams already deep in WeCom docs and Tencent Meeting face less migration friction with WorkBuddy; organizations whose knowledge lives in Feishu get a more "out-of-the-box" fit with the Doubao Work Team edition.

### 5.3 Alibaba Qwen Work: An "AI Workstation" Inside the DingTalk Ecosystem

Qwen Work's site (qwenwork.cn) positions it as a **one-stop AI office platform for individuals and enterprises**, with a web client plus macOS, Windows, and HarmonyOS apps covering content creation, data analysis, professional research, file processing, and web delivery.

The official docs highlight three agent forms:

- **Web / cloud agent** — runs in the browser or as scheduled cloud tasks that keep working after you close the browser.
- **Desktop agent** — natural-language task initiation combined with files, skills, connectors, **computer control**, IM, and Hooks.
- **Enterprise collaboration agent** — an in-DingTalk entry, admin console, credits, and SSO (supporting Feishu, DingTalk, WeCom, Microsoft Entra ID, and others).

The desktop documentation explicitly offers **computer control** (screen awareness, keyboard/mouse control, cross-app flows), **IM channels** (connecting common chat tools), **expert suites**, and a **skills** system; "My Web" includes built-in site hosting for publishing static or dynamic pages.

**Doubao Work vs. Qwen Work:** Qwen Work's strengths are **collaboration inside DingTalk organizations, web publishing and HarmonyOS coverage, and SSO across multiple IdPs**; Doubao Work is not natively bound to DingTalk at the same level. Teams whose center of gravity is DingTalk — and who want a consistent "in-DingTalk + desktop + cloud" experience across all three ends — should evaluate Qwen Work first; Feishu teams don't need to take the detour.

### 5.4 Floatboat: The Calendar-Driven Option for Overseas and Independent Users

[Floatboat](https://floatboat.ai/) is not "another chat agent inside Feishu or DingTalk." It is a **Calendar-Driven Agent OS**: the calendar is the agent's runtime, and meetings, deadlines, and recurring tasks automatically trigger preparation and execution — pre-meeting briefs, drafts before deadlines, post-meeting follow-up — without a fresh prompt every time. The category definition is in our "What Is an Agentic Calendar" explainer.

Compared with the Doubao Work model of "you issue a task, the agent goes and does it," Floatboat differs on:

- **Trigger model**: Floatboat is **system push** — when the calendar event arrives, it runs. Doubao Work is primarily **user pull**, with the Team edition layering Feishu IM/document context on top.
- **Context source**: Floatboat builds a persistent workspace around **calendar events**, connecting Google Calendar, Outlook, Notion Calendar, Lark/Feishu calendar via ICS and more, without defaulting to one IM suite. Doubao Work's Team edition draws its core context from **Feishu organizational data**.
- **Typical scenario**: pre-meeting preparation and post-meeting follow-up for independent founders, consultants, and cross-timezone teams — see [AI Meeting Preparation](/blog/ai-meeting-preparation); Doubao Work skews toward **document/PPT/video delivery inside Feishu plus local GUI control**.
- **Collaboration shape**: Floatboat + [FloatIM](https://floatboat.ai/floatim) run an agent-native group-chat network; Doubao Work runs deep Feishu integration.
- **Market**: Floatboat targets global solopreneurs and small teams; Doubao Work targets mainland China and serves Feishu enterprises deeply.

**Doubao Work vs. Floatboat:** Floatboat's strengths are **calendar-driven proactive execution, cross-calendar/cross-timezone, and no dependence on a Feishu or DingTalk stack**; Doubao Work's strengths are **organizational context inside Feishu permissions, the Windows virtual desktop, Seed's multimodal stack, and the domestic office ecosystem**. If your collaboration center is Feishu group chats and cloud documents, Doubao Work fits better; if your collaboration center is **meetings and deadlines on a calendar** and you want the agent to run pipelines around events automatically, evaluate [Floatboat](https://floatboat.ai/).

### 5.5 Why ByteDance Is Betting on This Now

All three share one backdrop: **once conversational model quality converges, the competition shifts to who owns the office entry point.** ByteDance's advantage is Doubao's consumer scale in China and Seed's sustained investment in agents, computer use, and multimodality; its constraint is that enterprise collaboration has to ride on Feishu — it can't self-produce a full IM suite the way Tencent can.

Making Doubao Work a standalone brand bundles ByteDance's strongest pieces — **agent execution + Feishu organizational context + multimodal delivery** — against WorkBuddy's "Tencent desktop + full IM reach," Qwen Work's "DingTalk + cloud workstation," and Floatboat's "calendar runtime + proactive pipeline." **Wherever your default work context lives, that's the agent line to pick.**

### 5.6 A Pragmatic Way to Choose

**Choose Doubao Work if:** your team is deeply on Feishu; you need a Windows local virtual desktop fused with Feishu permissions; your content work depends heavily on integrated document/PPT/video delivery; or you already pay for Doubao and want a single entry point.

**Choose WorkBuddy if:** your collaboration runs mainly on WeCom/WeChat/QQ and Tencent Docs; you value the expert marketplace and multi-model/private deployment; or you want the widest IM remote-dispatch coverage.

**Choose Qwen Work if:** your organization is already on DingTalk; you need in-DingTalk native plus desktop computer control plus cloud scheduled tasks; or you have HarmonyOS or web-publishing needs and enterprise SSO across several IdPs.

**Choose [Floatboat](https://floatboat.ai/) if:** you're an independent founder or consultant and **the calendar is the hub of your work**; you need automatic pre-meeting prep, deadline delivery, and follow-up via calendar-driven pipelines; you mix Google/Outlook/Feishu-calendar (ICS) sources and **don't want to be locked into one IM ecosystem**; or your team is overseas or cross-border.

**There is no universal answer.** Take a real task due next week and run it through the products you're weighing — **your software stack and trigger habits are more reliable than any comparison table.**

---

## 6. Pricing and the Team Edition (Overview)

The personal edition offers a free tier and several paid subscriptions; they differ in work-task quotas, cloud PC, and model tier. **Check doubao.com/work/price and the client for specifics.**

The Team edition (doubao.com/work/group) emphasizes Feishu integration, enterprise permissions, and Skill sharing. Public pricing-page information: the team subscription starts at 1 seat (roughly ¥166 per seat per month billed annually, per the official site); the enterprise subscription starts at 100 seats, with seats and usage billed separately and stronger audit and leak-prevention capabilities.

Before purchasing, have IT and legal review the user agreement and privacy policy clauses covering automation and data.

---

## 7. Conclusion

Doubao Work's logic fits into two sentences: **give people who already use Doubao a desktop built for work, and give companies on Feishu an agent colleague that inherits their permissions.**

It became its own product not because the features were impossible to build, but because **chat, office work, enterprise governance, and competitive positioning** can no longer fit inside one entry point. Seed pushes model capability toward "cross-tool delivery"; Feishu turns organizational context into the agent's moat; WorkBuddy and Qwen Work own IM ecosystems at home; and [Floatboat](https://floatboat.ai/) holds the **calendar-driven** position overseas and with independent users. ByteDance needed a standalone brand to own the Feishu office lane.

What decides the outcome is not whether a deck can be generated — plenty of products can — but **whether it can deliver reliably inside real permissions without causing trouble**. If you care more about "who runs the pre- and post-meeting work on my calendar," the agentic calendar explainer above is where that category is defined; if you care more about "an agent colleague inside Feishu," the Doubao Work Team edition is the product to compare against.

---

## FAQ

### Are Doubao Office and Doubao Work the same product?

Yes. In everyday speech, "Doubao Office" usually means the "work tasks / office tasks" mode inside the app; **Doubao Work is the official brand**, at doubao.com/work, with its own desktop client.

### Why did ByteDance make Doubao Work a standalone product?

The core reasons: office agents and chat products have different user expectations, compute costs, and enterprise-governance requirements; model capability now supports cross-tool delivery and needs a dedicated entry; Feishu team scenarios need their own permissions and subscription system; TRAE and Coze capabilities need a unified office exit; and WorkBuddy and Qwen Work both compete as standalone brands, so Doubao Work needed a comparable presence.

### Is there an international version of Doubao Work?

No. The overseas product is Dola (dola.com), a general AI assistant without Doubao Work-grade local agents or Feishu enterprise integration.

### Can I use it without Feishu?

Yes. The personal edition's core capabilities don't depend on Feishu. Only a Feishu sign-in or connectors unlock organizational context and team collaboration.

### How do I choose between Doubao Work, WorkBuddy, Qwen Work, and Floatboat?

Already on **Feishu** → prefer Doubao Work. Already on **DingTalk** → prefer Qwen Work. Primarily on **Tencent IM/docs** → prefer WorkBuddy. **Calendar-driven, pre/post-meeting automation, don't want to be tied to one IM** → look at [Floatboat](https://floatboat.ai/) and the Calendar-Driven AI vs Chat AI explainer. Test with a real task before committing to a subscription.

### What's the difference between Doubao Work and Floatboat?

Both "get things done," but the **default context and trigger are different**. Doubao Work: you start the task, the Team edition reads Feishu organizational data, and its strengths are delivery inside Feishu and domestic desktop GUI control. Floatboat: calendar events trigger the agent to prepare and execute automatically (pre-meeting, deadlines, follow-up), with strengths in [Proactive Agent OS](https://floatboat.ai/) and cross-calendar integration. Feishu teams should pick Doubao Work; independent founders and cross-timezone calendar users should compare [Floatboat](https://floatboat.ai/).

### Can Doubao Work replace Feishu?

No. It is an agent execution layer *on top of* Feishu (Team edition), or a personal office agent independent of Feishu (personal edition). Feishu remains the collaboration foundation.
