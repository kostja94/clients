---
title: "DeepSeek V4.1 Flash — The Two-Day Beta That Tests Whether Flash Can Replace Pro"
description: "DeepSeek opened a two-day beta of V4.1 Flash on Sept 8, 2026 — a new architecture with native multimodal input and community-measured speeds above 300 tokens/s. Its feedback form asks whether the model can replace V4 Pro. Here is what the beta reveals before it expires on September 10."
slug: "deepseek-v4-1-flash"
date: 2026-09-09
author: "Judy"
category: "Research"
---

**TL;DR**
  * DeepSeek V4.1 Flash is an intermediate beta model that went live in the DeepSeek API on September 8, 2026, under the self-expiring model ID `deepseek-v4.1-flash-expires-on-0910` — no blog post, no technical report, and a hard shutdown scheduled for September 10.

  * It is the first architecture-level revision of the V4 family since April 2026: DeepSeek describes a new model structure with native multimodal input (text, image, and audio handled in one pass), replacing the bolt-on vision approach used by V4-Flash-Vision-Exp in August.

  * Developer measurements are the only performance data so far, and they cluster tightly: sustained output generally above 300 tokens/s with peaks reported at 507 tokens/s, roughly 5.7x the sustained throughput of V4 Pro and 3.9–6x faster than V4-Flash-Vision-Exp on identical end-to-end tasks — all community-measured, none vendor-certified.

  * The beta's real purpose is strategic: the feedback questionnaire that shipped with it asks users whether V4.1 Flash could "fully replace" the production V4 Pro, a direct test of whether DeepSeek can sell Flash-level prices with Pro-level capability.

  * A flash-series price cut announced September 9 takes effect at the same moment the beta expires — 12:00 Beijing time on September 10 — which makes the two-day window a preview of how DeepSeek plans to reposition its cheapest tier.

## 1\. Why a 48-Hour Model Drop Is the Week's Biggest Signal

DeepSeek shipped V4.1 Flash the way it shipped most of its V4 line: without ceremony. On the afternoon of September 8, 2026, the company's team posted a short notice in its official community groups that an "intermediate version" of a new model — `deepseek-v4.1-flash-expires-on-0910` — was open for limited testing, accessible to anyone with an existing API key by swapping the model name. There was no landing page, no changelog entry, no model card, and no post on X, a silence that independent trackers flagged within hours ([Sahil Panhotra noted on X that the model was live "but weirdly... DeepSeek hasn't even announced it on X yet"](https://www.kocpc.com.tw/archives/668214)).

That silence is exactly why the beta matters. DeepSeek's pattern since V4 launched in April has been to expose an intermediate build in the live API environment, measure real-traffic behavior for a tightly bounded window, then ship the formal version. V3.2-Speciale followed the same playbook in late 2025 with an expiry date baked into its endpoint. The V4.1 Flash ID carries that logic one step further: the expiry is in the name itself, and the clock started at roughly 15:00 Beijing time on September 8, giving testers under 48 hours of uptime before the identifier stops resolving.

Two pieces of context make the timing more than a routine checkpoint. First, this beta arrives roughly 40 days after V4-Flash reached public beta on July 31 and barely three weeks after V4 Pro went GA as build 0813 on August 13 — we covered what that quiet GA actually changed in our [DeepSeek V4 Pro 0813 breakdown](/blog/deepseek-v4-pro-0813), and DeepSeek's own API changelog documents both rollouts ([DeepSeek's API changelog](https://api-docs.deepseek.com/updates/)). An architecture-level revision on that cadence is unusual for any frontier lab, and it signals that DeepSeek is treating the V4 generation as a fast-moving platform rather than a finished product line. Second, the same week brought a flash-series price cut, effective September 10 at 12:00 Beijing time, and reports that DeepSeek has engaged CITIC Securities to prepare a STAR Market IPO ([IT Home, citing Reuters](https://www.ithome.com/1/000/188.htm)). A cheap, fast, multimodal model is the product story DeepSeek wants to tell investors and developers simultaneously.

This article is a field report on that two-day window: what V4.1 Flash actually is, what the architecture change implies, what the community measured before the deadline, and — most importantly — what the questionnaire buried inside the beta says about where DeepSeek's model line is heading.

## 2\. What DeepSeek V4.1 Flash Actually Is

The practical definition first: **DeepSeek V4.1 Flash is a limited, intermediate test build of DeepSeek's next Flash-tier model, served through the standard DeepSeek API under a model ID that expires on September 10, 2026.** It is not a production model, not a general release, and not a rename of an existing checkpoint. DeepSeek's own framing — relayed through its community-group notice and repeated consistently by Chinese tech media — is that this is an "intermediate version" (中间版本) opened for user testing ahead of a final release ([Phoenix Tech](https://tech.ifeng.com/c/8wFovW2dxl1), [36Kr/APPSO](https://eu.36kr.com/en/p/3974571498057985)).

Access is deliberately frictionless. You keep your existing `base_url` and API key, and change only the `model` parameter. No waitlist, no separate endpoint, no new console, no beta qualification. Billing during the test matches `deepseek-v4-flash` exactly — there is no premium for early access. The one hard constraint is concurrency: each account is capped at 20 simultaneous requests, compared with the 2,500 concurrency limit DeepSeek publishes for the production flash model ([DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/)).

| What we know | What we don't |
|---|---|
| Model ID `deepseek-v4.1-flash-expires-on-0910`, same `base_url` | Total / active parameter count |
| Billing identical to `deepseek-v4-flash` | Context-window length (V4 family standard is 1M) |
| 20 concurrent requests per account | Official benchmark scores |
| Auto-expires September 10, 2026 | Training approach or data mix |
| Native multimodal input (text/image/audio unified) | Whether the architecture reaches the Pro tier |
| New, redesigned model structure (per DeepSeek) | Formal release date or pricing |

The concurrency cap is the tell. Twenty concurrent requests is not a number anyone uses for production traffic; it is a number designed for functional validation and load sampling. Combined with a model name that encodes its own death date, the setup forces every caller to treat the beta as an evaluation harness rather than a dependency. That is the same read several outlets reached independently — Cocoloop described the 48-hour window as "a stress test rather than a release" ([Cocoloop](https://news.cocoloop.cn/2026/09/deepseek-v41-flash-multimodal/)), and OrcaRouter's field note called it "a build dropped into the real API environment for a limited test... It is not a launch" ([OrcaRouter](https://www.orcarouter.ai/blog/deepseek-v4-1-flash-leak)).

For anyone evaluating the model, the missing information is as important as what DeepSeek did disclose. As of September 9, the official Models & Pricing page still lists only `deepseek-v4-flash`, `deepseek-v4-pro`, and `deepseek-v4-flash-vision-exp`, and the changelog has no V4.1 entry. Parameter counts, context length, and evaluation data have not been published, which means every capability claim below rests on community measurement and developer reports rather than a vendor spec sheet.

## 3\. A New Architecture — and What "Native Multimodal" Actually Changes

DeepSeek's description of V4.1 Flash is three adjectives long: stronger capability, faster generation, lower cost — delivered, the company says, by "a new model structure" with native multimodal support. The architecture point is the one worth unpacking, because it marks a real departure from how DeepSeek has handled vision so far.

The V4 family's existing multimodal path is an add-on, not a redesign. DeepSeek-V4-Flash-Vision-Exp, released August 21, 2026, bolts a vision encoder and an alignment layer onto the text-only V4-Flash-0731 base, letting the model accept images as an extension of its text pipeline ([DeepSeek changelog](https://api-docs.deepseek.com/updates/)). V4.1 Flash, by contrast, is described as integrating text, image, and audio processing into the model architecture itself — input modalities handled in a unified pass rather than routed through an external vision pack. Chinese coverage of the release consistently highlights the distinction: this is an architectural iteration, not parameter tuning, with multimodal capability "built in from the factory" rather than attached ([36Kr / Zimu AI](https://eu.36kr.com/zh/p/3974719807231617)).

Why that distinction matters is a question of cost and reliability, not just engineering aesthetics. A bolt-on vision pipeline adds latency and complexity at the API boundary — the text model runs, the vision encoder runs, an aligner reconciles the two. A natively multimodal model trains and serves those paths together, which is the only credible way DeepSeek's simultaneous claims of "stronger, faster, and cheaper" can hold: the cost reduction has to come from somewhere structural, and fusing modalities into one architecture is the most plausible source given that no other major cost lever has been disclosed.

Two independent signals support the idea that this is more than a marketing gloss. First, the same community bloggers who benchmarked the beta report qualitatively better multimodal behavior than the Vision-Exp model — one tester fed V4.1 Flash a photo of a person in a suit and found it correctly identified the pinstripes, a detail the earlier bolt-on model had hallucinated ([36Kr / Zimu AI](https://eu.36kr.com/zh/p/3974719807231617)). Second, China's Yicai (First Financial) reported that developers suspect the model was substantially pre-trained rather than merely post-trained on the V4 base — a "rebuild," not a polish — which is consistent with an architecture-level revision arriving so soon after Flash's public beta ([Yicai via Sina Finance](https://finance.sina.com.cn/roll/2026-09-08/doc-inircmeq9212156.shtml)). Neither is proof; both are directionally consistent with DeepSeek's own description.

## 4\. Community-Measured Speed: The Numbers Before the Deadline

Because DeepSeek published no benchmark table, the performance picture for V4.1 Flash comes entirely from developers who pointed their own keys at the endpoint during the two-day window. The measurements cluster remarkably tightly across independent testers, which is itself a useful signal, but they remain community data — conditions vary, and the most spectacular figures have not been reproduced under controlled conditions.

The most detailed single test came from X user @riba2534, whose numbers circulated widely through Chinese tech media ([King of Computer Media](https://www.kocpc.com.tw/archives/668214)):

- Time to first token: 178 ms, stabilizing around 160 ms on short exchanges
- Sustained output: stable at ~355 tokens/s, peaking above 365 tokens/s
- Long-form code generation: a complete 1,500-token doubly linked-list LRU implementation in 4.40 seconds
- Thinking phase: built-in reasoning completes in roughly 1.1 seconds before switching to the answer

Other reporters and testers produced figures in the same band. A developer quoted by Wall Street CN measured an output peak of 507 tokens/s and 328 tokens/s on a live SVG-animation generation task, with averages "generally above 300 tokens/s" ([Wall Street CN](https://wallstreetcn.com/articles/3781316)). Zimu AI's own testing logged a "hello" exchange with 0.3 seconds of thinking time, an instantaneous rate of 159.3 tokens/s, and an 0.8-second end-to-end round trip, while a heavier long-context reasoning run hit 420 tokens/s with end-to-end throughput of 409.5 tokens/s ([36Kr / Zimu AI](https://eu.36kr.com/zh/p/3974719807231617)). Threads on V2EX and LINUX DO reported sustained rates between 350 and 530 tokens/s across the first evening.

The more decision-relevant comparison is against the rest of DeepSeek's own line, because that is the choice a developer is actually making. On the same end-to-end tasks, the beta was measured at roughly 5.2x the speed of V4-Flash-Vision-Exp on 49k-token long-context retrieval, 6.0x on SVG code generation, 4.6x on a Manacher palindrome-algorithm problem, 5.0x on large SQL generation, and 3.9x on an asyncio refactor — per community benchmarks relayed by Zimu AI and corroborated in Yicai's reporting. Against V4 Pro, the same testers measured 5.7x sustained throughput (355 vs. 63 tokens/s) and 77% lower first-token latency (178 ms vs. 766 ms), cutting the time to generate 1,500 tokens from 24.7 seconds to 4.4 seconds ([King of Computer Media](https://www.kocpc.com.tw/archives/668214)).

What these numbers mean for a working developer is worth stating plainly: at 300–400 tokens/s with sub-200 ms first-token latency, V4.1 Flash-class throughput moves the practical bottleneck of agent work away from model latency and toward your own loop design. Iterative coding, batch code generation, and sub-agent fan-out — the workloads where a slow model makes each retry expensive in wall-clock time — are precisely where this speed changes the economics. This is also why several beta testers on V2EX immediately framed the model as sub-agent material: "run this fast, intelligence doesn't need to be top-tier — it just needs to execute instructions accurately" is the rough consensus of one thread ([V2EX discussion](https://www.v2ex.com/t/1240438)). If you are evaluating DeepSeek models inside a broader agent stack, our guide to [what a DeepSeek Agent is](/blog/what-is-deepseek-agent) frames where Flash-tier throughput fits among the four archetypes.

The caveat deserves equal weight. Every one of these figures is community-measured on an intermediate build served at reduced concurrency; some testers speculated the highest readings came from a separately deployed version that may not reflect the final serving stack ([King of Computer Media](https://www.kocpc.com.tw/archives/668214)). Treat the direction as credible and the specific peaks as unverified until DeepSeek publishes its own numbers with the formal release.

## 5\. The Questionnaire That Reveals the Strategy: "Can It Replace V4 Pro?"

The most revealing artifact of the entire beta is not a benchmark — it is a survey. Alongside the model, DeepSeek distributed a feedback questionnaire for the "V4.1 Flash intermediate version" whose centerpiece question asks users to choose among "Yes," "No," "Uncertain," and "Other" in response to the prompt: **"Do you think this model can fully replace the DeepSeek V4 Pro now in production?"** ([36Kr / Zimu AI](https://eu.36kr.com/zh/p/3974719807231617), [King of Computer Media](https://www.kocpc.com.tw/archives/668214)).

Read that question literally and it is odd: why would a lab ask the public whether its cheap tier can replace its expensive one? Read it strategically and it is the clearest statement DeepSeek has made about the V4.1 generation's purpose. The company is not trying to build a slightly better Flash. It is testing whether a Flash-priced, Flash-speed model can absorb workloads that currently justify V4 Pro's price premium — and it wants the market's answer before it commits to the positioning. Zimu AI's write-up framed the same point in marketing terms ("Flash's model, Pro's ambition"), and OrcaRouter described the underlying question as whether "DeepSeek's cheapest tier just started aiming at its most expensive one" ([OrcaRouter](https://www.orcarouter.ai/blog/deepseek-v4-1-flash-leak)).

The strategic logic is easy to miss if you think of DeepSeek's tiers as fixed. Since the V4 family launched, the official line has been that Flash delivers reasoning close to Pro on simple agent tasks while Pro owns the complex end. V4.1 Flash's architecture revision compresses that gap from the cheap side: if the new structure genuinely delivers Pro-adjacent capability at Flash pricing, then the product line stops being a capability ladder and becomes a single capability with a speed-and-price dial. For developers, that would collapse today's binary choice — fast-but-cheap vs. strong-but-expensive — into one question: is Flash enough for this task?

The economics behind that repositioning are stark, and they are visible in the official price list. At current rates, V4 Pro's output costs roughly three times V4 Flash's per million tokens at off-peak rates ($1.98 vs. $0.66 output per 1M tokens), a gap that makes Pro a poor default for high-volume agent traffic even when its quality edge is real ([DeepSeek Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/)). If V4.1 Flash — at Flash prices — handles a large fraction of what teams currently send to Pro, DeepSeek's revenue per token falls while its addressable workload expands dramatically. That is a volume-over-margin bet, and the questionnaire is DeepSeek's way of stress-testing it with the people who would have to migrate.

## 6\. The Price Cut That Lands at the Same Moment

The beta's expiry is not the only September 10 deadline. On September 9, DeepSeek's open platform announced a flash-series price adjustment effective 12:00 Beijing time on September 10 — the same minute the V4.1 Flash beta identifier stops resolving. The two announcements are almost certainly coordinated parts of one rollout ([TMTPost](https://www.tmtpost.com/nictation/8133581.html), [MyDrivers](https://news.mydrivers.com/1/1149/1149680.htm)).

Under the new schedule, the flash series (currently `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp`) drops to RMB 0.02 per million input tokens on cache hits, RMB 1 per million on cache misses, and RMB 4 per million output tokens during off-peak hours, with peak-hour prices at exactly double ([DeepSeek's announcement, as relayed by TMTPost](https://www.tmtpost.com/nictation/8133581.html)). Against the previous rates, that is a 60% cut on cache-hit input, 33.3% on cache-miss input, and 11.1% on output. Peak hours are defined as Monday–Friday 09:00–12:00 and 14:00–18:00 Beijing time; weekends run entirely at off-peak rates.

Three things are worth noticing about this price move. First, it partially reverses the August hike that raised peak-hour prices when the peak/off-peak system launched on August 16 — a pricing whipsaw that Chinese developer communities have been openly cynical about, with the founder's nickname oscillating between "saint" and "cheapskate" depending on the week's price direction ([V2EX discussion](https://www.v2ex.com/t/1240438), [36Kr / Zimu AI](https://eu.36kr.com/zh/p/3974719807231617)). Second, the cut applies to the flash series — the tier V4.1 Flash belongs to — which suggests the price change is clearing the path for the formal V4.1 Flash release rather than reacting to the beta. Third, even after the cut, off-peak output remains at RMB 4 per million tokens, roughly double the pre-August promotional price, so the "discount" is relative to a raised baseline rather than a return to the old list. Timing also matters for anyone reading the beta's own billing as a price signal: during the test, V4.1 Flash bills at the same rate as `deepseek-v4-flash`, so when that baseline itself drops on September 10, the beta's measured cost-per-task will slightly understate what the formal model costs — though by little, since output (the dominant cost in agent workloads) falls only 11%.

## 7\. What to Do Before September 10 — and What Happens After

The beta's remaining life is measured in hours, so the practical window is narrow. If you have a DeepSeek API key and any interest in where model economics are heading, the highest-value use of the next day is a focused evaluation rather than a production migration — the model ID dies on September 10 and requests using it will fail afterward, so nothing built on the beta survives the deadline without a fallback path.

A useful evaluation protocol fits inside the 20-concurrency limit and the time available. Benchmark one or two of your actual workloads — not generic prompts — against `deepseek-v4.1-flash-expires-on-0910`, capturing three numbers: end-to-end time per task, tokens consumed per task, and output quality relative to your current model. The speed gain is only valuable if it does not arrive with a quality regression, and the two-day window is long enough to find out on real tasks even if it is too short for a full harness. Record your own cost-per-task at flash rates so you can compare against the post-September-10 price list rather than the pre-cut baseline. And build the fallback logic now: any integration pointed at the expiring ID must be ready to switch back to `deepseek-v4-flash` or wait for the formal release, because the expiry is enforced by the model name itself.

After September 10, the questions shift from the beta to the roadmap. DeepSeek has given no date for the formal V4.1 Flash release, no indication of whether the new architecture will also appear in the Pro tier, and no commitment on pricing beyond the flash-series cut ([Cocoloop](https://news.cocoloop.cn/2026/09/deepseek-v41-flash-multimodal/)). The credible expectation, based on DeepSeek's rollout history — V4-Flash preview to public beta, then V4-Pro GA, each within weeks — is a formal release in the near term rather than a long gap. What remains genuinely open is whether the final model keeps the beta's speed profile at full production concurrency, whether the weights are released under the MIT license that the rest of the V4 family carries, and whether DeepSeek follows the questionnaire's logic and positions V4.1 Flash as a genuine Pro replacement for the workloads that can afford to move.

For solo operators and agent builders specifically, the strategic read is simpler than the benchmark coverage suggests. DeepSeek is using a two-day beta to test the market's appetite for a model that collapses its own price tiers. The beta's community measurements — whatever their caveats — suggest the architecture is real enough that the question is no longer whether the capability gap can close, but how fast DeepSeek chooses to close it and at what price. Your job before the deadline is to know, on your own workloads, whether Flash-tier speed and price are enough; if they are, the September 10 announcements will tell you exactly what that capability will cost.

## 8\. Conclusion

A two-day beta is an unusual launch, but it is a very DeepSeek way to run a strategy experiment. The company shipped an intermediate build under an expiring name, capped concurrency at a level that rules out production use, published no benchmarks, and let the community generate the only performance data that exists. In that data, the architecture-level revision looks genuine: speeds in the 300–500 tokens/s band, multimodal input handled natively rather than bolted on, and cost structure that stays on the flash price list. And in the questionnaire, DeepSeek asked the question that matters more than any single number — whether this cheap, fast model can replace the expensive one. The price cut landing at the exact moment the beta expires suggests DeepSeek already has its answer in mind; September 10 will tell us whether the market agrees.

## FAQ

### What is DeepSeek V4.1 Flash?

DeepSeek V4.1 Flash is an intermediate test version of DeepSeek's next Flash-tier model, opened for limited API beta on September 8, 2026, and scheduled to auto-expire on September 10. It uses a new model architecture with native multimodal input and bills at the same rate as `deepseek-v4-flash`. It is not a formal release and has no official technical report or benchmark table yet.

### How do I access DeepSeek V4.1 Flash during the beta?

Keep your existing API `base_url` and key, and change only the `model` parameter to `deepseek-v4.1-flash-expires-on-0910`. No separate endpoint or beta qualification is needed. Each account is capped at 20 concurrent requests, and the model ID stops working after September 10, 2026.

### Is V4.1 Flash faster than V4 Pro?

Community measurements during the beta recorded roughly 5.7x the sustained throughput of V4 Pro (around 355 tokens/s vs. 63 tokens/s) with about 77% lower first-token latency. These are developer measurements on an intermediate build, not official figures; DeepSeek has not published its own benchmarks.

### Is V4.1 Flash cheaper than V4 Pro?

During the beta it bills exactly like `deepseek-v4-flash`, which is roughly one-third of V4 Pro's output price. A flash-series price cut effective September 10 lowers cache-hit input prices by 60% while output drops about 11%, so the formal model is expected to remain far below Pro pricing if it keeps the flash price list.

### Can DeepSeek V4.1 Flash replace V4 Pro?

That is precisely the question DeepSeek's own beta feedback questionnaire asks users to answer. The model is positioned to test whether Flash-tier speed and price can absorb Pro-level workloads; whether it fully replaces Pro depends on the formal release's quality at production concurrency, which has not been published.

### Is DeepSeek V4.1 Flash open source?

No weights have been released for V4.1 Flash. The rest of the V4 family (V4 Pro and V4 Flash) is MIT-licensed on Hugging Face, but DeepSeek has made no statement about open-sourcing the new architecture. Expect confirmation — or silence — with the formal release.
