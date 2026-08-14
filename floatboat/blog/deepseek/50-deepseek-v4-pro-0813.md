---
title: "DeepSeek V4 Pro 0813 — The Quiet GA and What It Actually Changes"
description: "DeepSeek V4 Pro 0813 went GA with no announcement. Specs, claimed agent benchmarks, the pricing window before the hike, and how it stacks against Grok 4.6."
slug: "deepseek-v4-pro-0813"
date: 2026-08-16
author: "Kostja"
category: "DeepSeek"
secondaryCategory: "Research"
---

## TL;DR

- DeepSeek V4 Pro 0813 is the production (GA) build of DeepSeek's flagship model, quietly swapped into the `deepseek-v4-pro` endpoint on August 12–13, 2026 — no blog post, no changelog, no press release, just a version-string change on the pricing page.
- The architecture is unchanged (1.6T-parameter MoE, 49B active, 1M-token context, 384K max output). What changed is post-training: DeepSeek claims agentic coding gains that are large on paper — DeepSWE from 12.8 to 62.7, Terminal-Bench 2.1 to 87.9.
- Every one of those scores is vendor-reported, produced through a benchmark harness DeepSeek has not released. Independent trackers have recorded zero third-party results for 0813 so far.
- Pricing holds at $0.435 input / $0.87 output per 1M tokens for now, but a peak/off-peak schedule kicks in August 16 (UTC) that can multiply output costs by up to ~4.5x at peak.
- For agentic workloads on a budget, 0813 is the cheapest credible option among frontier-adjacent models this week — and it shipped the same week as xAI's Grok 4.6, giving buyers a rare same-week head-to-head.

---

## 1. Why a Silent GA Is Still a Big Deal

DeepSeek has a habit of shipping without ceremony, but the V4 Pro 0813 rollout took that to an extreme. On August 12, 2026, the company's API pricing page quietly listed `DeepSeek-V4-Pro-0813` as the model behind the existing `deepseek-v4-pro` endpoint. There was no announcement page, no release notes entry, and — as of the week of publication — no blog post. The model had been running as a preview since April 24, and the switch flipped it to a production checkpoint with a single cell in a pricing table.

The low ceremony is partly a symptom of how DeepSeek operates and partly a deliberate choice. The company had already committed to the pattern with V4 Flash, which went GA on July 31 with a changelog note that the Pro official release would "follow soon." When that follow-through arrived, it landed the same week xAI shipped Grok 4.6 — a crowded 48 hours for anyone tracking frontier model releases. In that context, a silent version bump is not a lack of ambition; it is DeepSeek telling developers that the production version is simply the endpoint, and the endpoint is already what you use.

What makes the release consequential despite the quiet is timing. V4 Pro 0813 arrives as DeepSeek's strongest statement yet that its models are built for agentic work — tool use, multi-step coding, long-running tasks — rather than chat. That positioning matches what the company has been signalling since April, and it matters for solopreneurs because the cost structure of V4 makes agent loops affordable in a way they are not on premium closed models. The GA makes that affordability production-grade: teams no longer have to wonder whether they are benchmarking a preview that might change under them.

---

## 2. V4 Pro 0813 by the Numbers

The spec sheet for the GA build is unchanged from the preview, which is itself a useful fact: this is a post-training release, not a new architecture. The numbers below are drawn from DeepSeek's official model documentation and the [DeepSeek API docs pricing page](https://api-docs.deepseek.com/quick_start/pricing).

| Spec | Value |
|------|-------|
| Architecture | Mixture-of-Experts, 1.6T total / 49B active params |
| Attention | Hybrid: Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) |
| Context window | 1,000,000 tokens |
| Max output | 384,000 tokens |
| Input modality | Text only (no vision, audio, or video in this build) |
| Reasoning modes | Non-think, Think High, Think Max (`reasoning_effort` expanded to low / high / max) |
| API compatibility | OpenAI Responses API, Chat Completions, Anthropic-compatible format |
| Tool calling | JSON output, tool calls, beta prefix continuation, FIM (non-thinking only) |
| Concurrency | 500 (V4 Flash allows 2,500) |
| Weights | MIT-licensed; Hugging Face still hosts the April preview build, not 0813 |

Three things in that table deserve attention. First, the expanded `reasoning_effort` ladder — low / high / max — gives developers a cost dial that maps directly to task complexity, which is the same control DeepSeek added to V4 Flash at its GA. Second, the Anthropic-compatible endpoint means anyone already pointing Claude Code at `api.deepseek.com` gets the production checkpoint with no code change. Third, the input modality is text-only: 0813 does not add native image reasoning, despite some coverage suggesting otherwise — the Artificial Analysis model card and DeepSeek's own docs both list text input only.

The architecture itself is worth understanding at a level deeper than the parameter count, because it explains the model's economics. V4 uses a hybrid attention design — Compressed Sparse Attention (CSA) combined with Heavily Compressed Attention (HCA) — that compresses long-context memory so aggressively that the model runs at roughly 27% of the single-token inference FLOPs of DeepSeek's V3.2 at the same 1M-token context, and keeps KV cache usage around a tenth. That is why a 1M-token context window is affordable at all: the sparse attention keeps the incremental cost of long inputs small, which is exactly the property an agentic workload — where context accumulates over many steps — rewards. It is also why the model uses FP4 precision for MoE experts with FP8 elsewhere; the reduced footprint directly lowers serving cost, and DeepSeek's own release materials note the format aligns with domestic accelerator support, hinting at further inference-cost reductions as that hardware scales through 2026.

---

## 3. Agent Benchmarks: The Good, the Claimed, and the Unverified

DeepSeek's official changelog for the GA release publishes a benchmark table that reads like a step change. The headline numbers: Terminal-Bench 2.1 at 87.9 (up from 72.1 on the preview), DeepSWE at 62.7 (up from 12.8, roughly a 4.9x jump), Cybergym at 83.3 (up from 52.7), NL2Repo at 61.5 (up from 38.5), and Toolathlon-Verified at 74.1. On two of the table's agent benchmarks, DeepSeek claims scores that edge past Anthropic's Claude Fable 5 — Cybergym at 83.3 vs 83.1, and AutomationBench (Public) at 31.8 vs 29.1 — while Terminal-Bench 2.1 trails Fable 5 by a tenth of a point (87.9 vs 88.0).

Those numbers need context that the changelog does not provide. The agent benchmarks were run through "DeepSeek Harness minimal mode," a benchmark framework the company has not released, which means the harness's strengths and weaknesses are baked into every score. The stakes of that opacity are higher than usual because of the preview's track record: on an independently run DeepSWE evaluation using a verifier with a 0.3% false-positive rate, the preview build scored roughly 8% pass@1 — versus 80.6% on DeepSeek's own SWE-bench Verified under a harness with a far higher false-positive rate. If the 0813 post-training genuinely produced 62.7 on the tighter DeepSWE benchmark, that is a real capability advance; if it is the product of a permissive harness, it is noise. Independent trackers have not yet arbitrated either way — benchable.ai listed zero third-party results for 0813 at the time of writing, and the vendor's evaluation harness remains unpublished.

What an honest reading supports is this: the agentic direction of the improvement is credible, the magnitude is unverified, and anyone choosing a model on these numbers alone is choosing on faith. For a deeper framework on how DeepSeek agents are categorized and how the four archetypes differ, see [what is a DeepSeek Agent](/blog/what-is-deepseek-agent). The practical stance — and the one that survives independent verification either way — is to treat 0813 as a strong, cheap candidate for agentic coding and to validate it on your own workload before committing.

---

## 4. What Actually Changed vs the Preview

For teams that have been running the preview, the question is whether to move, and the honest answer is: the switch already happened for you. Because the GA is a checkpoint swap on the same endpoint, every API call to `deepseek-v4-pro` now returns the 0813 build. There is no migration step, no new model string, and no configuration change. If you want to confirm you are getting the new build, the version fingerprint on responses changed along with the pricing-page listing.

The substantive changes are all in post-training behavior, and independent reviewers have started mapping them. Testing done through the Anthropic-compatible endpoint in a real agent environment (rather than a chat UI) found the GA build dramatically better at the creative-frontend tasks that used to expose the preview — the "AI front-end that looks obviously synthetic" pattern largely disappeared, and long-horizon engineering tasks completed with working test loops and self-repair instead of stalling. The same reviewers flagged persistent edge-case bugs, including a now-notorious image task that produced two crescent moons floating in the sky. In other words: meaningfully more capable, still not flawless, and — this is the recurring theme — the same model, more finished.

That matters for a specific group: anyone who benchmarked the preview in April–July and built assumptions on its behavior. The gap between preview scores and GA scores in the official table — DeepSWE 12.8 to 62.7 is the extreme example — means earlier evaluations are stale. If you decided in May that V4 Pro was "not good enough for agentic work," that decision was made against a different model. The GA is a re-evaluation point, not a continuation of the same verdict.

---

## 5. Pricing: The Window Before the Hike

The pricing story is where the silent release gets loud. As of the GA, the API rates are unchanged from the May discount that became permanent: $0.435 per 1M input tokens on a cache miss, $0.003625 on a cache hit, and $0.87 per 1M output tokens. At those prices, V4 Pro remains roughly an order of magnitude cheaper than premium closed models — Anthropic's Claude Fable 5 lists at $10 input / $50 output per 1M tokens, and GPT-5.6 Sol sits around $30 output.

That window closes on August 16, 2026 at 16:00 UTC. DeepSeek's announced peak/off-peak schedule sets peak hours at 01:00–04:00 and 06:00–10:00 UTC, with off-peak at half of peak pricing. For V4 Pro, the effective new rates are $1.32 input / $3.96 output at peak and $0.66 / $1.98 off-peak — a 4.5x jump on peak output versus the current flat rate. Headlines calling this "up to 1,100%" are technically correct only for specific token types and time bands; the more useful framing is that off-peak hours, which cover most of the day, roughly double today's prices, and peak hours roughly quadruple output costs.

For teams running long agent loops, the economic implication is specific and actionable. Agentic workloads are token-hungry, and their costs scale with output tokens — exactly the rate that multiplies most at peak. Scheduling heavy batch work into off-peak hours (most of a 24-hour day) preserves much of the old economics, while real-time interactive agent use at peak absorbs the full increase. Combined with the new `reasoning_effort` dial, the cost-management toolkit for V4 now has both a price-time dimension and a reasoning-depth dimension — neither of which existed at the preview's flat-rate launch.

---

## 6. How This Compares to Grok 4.6 (Same-Week)

The same week DeepSeek slipped V4 Pro 0813 into production, xAI held a formal release for Grok 4.6 — the most legible same-week frontier launch since the two labs started shipping on overlapping cadences. The two models are closer in positioning than their different rollout styles suggest. Both are post-training upgrades rather than new architectures. Both target long-running agentic work as their headline use case. Both are priced far below the closed premium tier, with Grok 4.6 at $2 / $6 per 1M input/output tokens and V4 Pro at $0.435 / $0.87.

The trade-offs split by workload rather than by "better model." Grok 4.6 leads on agentic knowledge work — its GDPval-AA v2 Elo of 1753 sits just behind Claude Opus 5 — and on certain coding benchmarks like CursorBench. DeepSeek counters on price (roughly a quarter of Grok's input rate and a seventh of its output rate) and on raw context economics for very long inputs. On the composite Artificial Analysis Intelligence Index, Grok 4.6's 61 matches GPT-5.6 Sol, while V4 Pro 0813's independent score sat at 53 when last measured — a gap that reflects Grok's stronger knowledge-reasoning baseline rather than a verdict on agentic coding, where the two are far closer. We break down that same-week head-to-head in [our Grok 4.6 analysis](/blog/grok-4-6).

---

## 7. What It Means for Solopreneurs

For a solo operator, the GA changes the math in three ways. First, production stability: the model you benchmark today is the model that will serve your calls, with the version pinned on the pricing page rather than floating under a preview label. Second, cost structure: even after the August 16 increase, V4 Pro off-peak pricing keeps long agent loops — the kind that run hundreds of tool calls per task — viable at a fraction of premium-model cost, provided you can shift heavy work into off-peak hours. Third, the ecosystem cue: DeepSeek's own benchmark notes were produced through its in-house execution framework, DeepSeek Harness, which shipped as an open-source developer preview alongside the GA. A first-party harness changes the "model plus tooling" equation — instead of routing V4 through Claude Code or OpenCode and living inside someone else's product, you can run the model through the vendor's own agent loop. Our [DeepSeek Harness explainer](/blog/what-is-deepseek-harness) covers what that framework does and where it fits.

The honest caveats are the ones this article has kept returning to. The benchmark gains are unverified by third parties, so build a validation task before you commit. The model is text-only, so image workloads still need a different tool. And the pricing window is real but narrow — the economics you lock in today are not the economics of September. For agentic coding on a budget in August 2026, V4 Pro 0813 is the cheapest credible option in its class; whether it is the best for your specific workload is a question only a hands-on test can answer.

---

## Conclusion

DeepSeek V4 Pro 0813 is a strange kind of milestone: a flagship GA delivered with no announcement, no changelog, and no press release — just a version string on a pricing page. That low ceremony fits the company's operating style, and it does not change what the release is: the production build of a model that had spent 111 days in preview, with agentic post-training improvements that are dramatic on paper and still awaiting independent verification.

The decision framework this leaves a buyer with is straightforward. If you already use `deepseek-v4-pro`, you are on the new build — re-benchmark anything you measured in the preview era. If you are comparing models for agentic work, treat the official benchmark table as directional and validate on your own tasks. If you are cost-sensitive, understand the August 16 price change and route heavy work into off-peak hours. And if you are choosing between this week's two frontier-adjacent releases, the Grok 4.6 comparison is the right next read — because the real competition in agentic AI is no longer about who has the best scorecard, but about whose economics make long-running agents actually affordable.

---

## FAQ

### Is DeepSeek V4 Pro 0813 a new model or an update?

It is the production build of V4 Pro, the same architecture as the April preview (1.6T-parameter MoE, 49B active, 1M context) with updated post-training. DeepSeek swapped the `deepseek-v4-pro` endpoint to this checkpoint on August 12–13, 2026; no integration change is required.

### How do I access DeepSeek V4 Pro 0813?

Use the existing `deepseek-v4-pro` model name on the DeepSeek API. It is OpenAI- and Anthropic-format compatible, so existing integrations, including Claude Code pointed at `api.deepseek.com`, work without modification.

### Are the 0813 benchmark scores independently verified?

Not yet. All agent benchmark scores (DeepSWE 62.7, Terminal-Bench 2.1 87.9, Cybergym 83.3, and others) are vendor-reported and were produced through DeepSeek's unreleased Harness minimal mode. Independent trackers had recorded no third-party 0813 results at the time of writing.

### When does the DeepSeek price increase take effect?

August 16, 2026 at 16:00 UTC. Peak/off-peak billing starts then, with peak hours at 01:00–04:00 and 06:00–10:00 UTC and off-peak priced at half of peak. Peak V4 Pro output rises to $3.96 per 1M tokens, up from the current $0.87 flat rate.

### Does DeepSeek V4 Pro 0813 support images?

No. This build is text-only. It accepts text input and produces text output; it does not natively support image, audio, or video input, despite some coverage suggesting otherwise.

### Is DeepSeek V4 Pro 0813 open-source?

The V4 series weights are MIT-licensed, but the 0813 build's weights had not been published at the time of writing — Hugging Face still hosted the April preview build. The API is the guaranteed way to access 0813.
