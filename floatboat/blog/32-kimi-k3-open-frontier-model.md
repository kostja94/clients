---
title: "Kimi K3 — What a 2.8T Open Model Changes for Agentic Coding"
description: "Kimi K3 lands as the largest open-source model at 2.8T params, with 1M context and KDA hybrid attention. How it changes long-horizon agentic workflow economics."
slug: "kimi-k3-open-frontier-model"
date: 2026-07-18
author: "Tan Shaoqing"
category: "Research"
---

## TL;DR

- Kimi K3, released on July 16, 2026, is Moonshot AI's new flagship model with 2.8 trillion parameters — the largest open-source model ever released, with a 1-million-token context window, native visual understanding, and always-on thinking mode. Full model weights are scheduled for release by July 27.
- Two architectural innovations drive its performance: **Kimi Delta Attention** (KDA), a hybrid linear attention mechanism that cuts KV cache usage by 75% and enables up to 6.3x decoding speedup at 1M context, and **Attention Residuals** (AttnRes), which improves training efficiency by approximately 25% at less than 2% additional cost.
- On the Artificial Analysis Intelligence Index, K3 scores 57 — third globally behind Claude Fable 5 and GPT-5.6 Sol. On Arena.AI's Frontend Code Arena, it ranks first with 1,679 points, overtaking both Fable 5 and GPT-5.6 Sol.
- K3 demonstrated 48-hour autonomous chip design, two-hour astrophysics research pipeline replication, and ranked first in four out of eight real-world task automation benchmarks — capabilities that matter more for long-horizon agentic workflows than single-turn benchmark scores.
- Priced at $3 per million input tokens and $15 per million output tokens, K3 is the most expensive model from a Chinese lab. Floatboat has integrated Kimi K3 as a built-in model — no API key, no configuration, available alongside DeepSeek, Claude, Gemini, and the rest of the model roster.

---

## 1. Why K3 Matters — Beyond the Parameter Count

Moonshot AI's trajectory over the past 18 months tells a story about what happens when a market leader loses its footing and has to rebuild. In early 2025, the Beijing-based startup founded by Tsinghua graduate Yang Zhilin was riding high — Kimi ranked third in monthly active users in China, the company had raised roughly $1.5 billion across multiple rounds, and its long-text analysis and AI search features had drawn a loyal user base. Then DeepSeek released R1, and the landscape shifted. By mid-2025, Kimi had slid to seventh in monthly active users, and the company that had been one of China's six "AI Tigers" looked more like a cautionary tale about how fast a market darling can lose relevance.

The open-source pivot that followed was not a marketing strategy. It was a survival move. Kimi K2 arrived in July 2025 — a 1-trillion-parameter MoE model with 384 experts and 32 billion active parameters, focused on coding and general agentic tasks. K2.5 followed in January 2026, pushing the company back into competitive territory. K2.6 in April 2026 added native multimodal capabilities, powerful agent swarm functionality, and 300 specialized agents. K2.7 Code in June 2026 trimmed thinking tokens by roughly 30% while improving coding benchmarks — an efficiency play that signaled the company was thinking about production costs, not just leaderboard scores.

K3 is the culmination of that arc. At 2.8 trillion parameters, it is roughly 75% larger than DeepSeek V4 Pro, and Moonshot claims it is the world's largest open-source model. More importantly, it introduces architectural innovations — hybrid linear attention and attention residuals — that were previously published as open research on GitHub but had not appeared in a production model at this scale. The model ships with 1-million-token context, native visual understanding, and an always-on reasoning mode. Full weights are promised within two weeks of the announcement, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems).

The shift matters for agentic workflows in a way that extends beyond the benchmark tables. Before K3, the largest open-weight model available was DeepSeek V4 Pro at approximately 1.6 trillion parameters. The gap between open-source and proprietary models was closing, but nothing open could claim to compete with Claude Fable 5 and GPT-5.6 Sol at the top of the leaderboard. K3 changes that calculation — and the full model weights on July 27 will let the community verify whether the published benchmarks hold up under independent evaluation.

---

## 2. What K3 Is — Architecture, Scale, and the KDA Breakthrough

K3 is a mixture-of-experts model with 896 total experts, of which 16 are activated per token during inference. That sparsity — roughly 56:1 — means the model stores far more knowledge than it mobilizes for any single query, keeping inference costs bounded while the total parameter count continues scaling. Combined with training and data optimizations, Moonshot claims K3 achieves approximately 2.5x the overall scaling efficiency of K2, translating compute into capability at a significantly higher rate, as documented in [Kimi's API docs](https://platform.kimi.com/docs/guide/kimi-k3-quickstart).

The two architectural innovations that enable this efficiency are worth understanding separately, because they address different constraints in large-model design: one handles long-sequence attention cost, the other handles deep-network information flow.

### 2.1 Kimi Delta Attention — Hybrid Linear Attention

The attention mechanism in a standard Transformer scales quadratically with sequence length. When the context window extends to 1 million tokens, that quadratic curve becomes the dominant cost driver — both in compute and in KV cache memory, which stores the key-value pairs needed for autoregressive generation.

KDA addresses this by making attention hybrid rather than uniform. In K3, every 4 attention layers follow a 3:1 pattern: three layers use linear attention (where complexity scales linearly with sequence length), and one layer uses full attention (where complexity remains quadratic but the model retains precise retrieval capability at critical points). The linear attention layers handle the bulk of the sequence — the parts where approximate attention is sufficient — while the full attention layers handle the segments where exact token-level matching matters, as documented in [Kimi K3's documentation](https://platform.kimi.com/docs/guide/kimi-k3-quickstart).

The measured impact is substantial: KV cache usage drops by 75%, and at 1-million-token context length, decoding throughput increases by up to 6.3x. For agent builders who need to process long documents or maintain long-running conversation histories, this efficiency translates directly to lower latency and reduced memory pressure on inference infrastructure. The model also uses NoPE (no positional encoding), which stabilizes attention computation over extreme sequence lengths without the positional drift that can degrade output quality in very long contexts.

### 2.2 Attention Residuals — Making Deep Models Remember

Deep Transformer models face a structural problem: as information passes through more layers, earlier representations get diluted. The standard solution — residual connections that add each layer's output to its input — helps, but treats all layers uniformly regardless of what information they contribute.

Attention Residuals (AttnRes) changes this by making information flow across layers selective rather than uniform. Instead of summing the output of every layer into the cumulative representation, AttnRes lets the model retrieve information from earlier layers only when it needs it — effectively giving the model a controllable "memory" of what previous layers computed. Moonshot's research shows this mechanism adds less than 2% computational overhead while improving training efficiency by approximately 25%, as documented in [Kimi K3's documentation](https://platform.kimi.com/docs/guide/kimi-k3-quickstart).

The practical implication is straightforward: a 2.8-trillion-parameter model with dozens of layers would normally lose signal from its bottom layers by the time it reaches the output. AttnRes preserves that signal, which means the model can use information from early layers — where basic syntactic and semantic patterns are encoded — alongside information from later layers where complex reasoning happens. For tasks that require both surface-level detail and deep structural understanding — like reading a 50-page document and synthesizing its argument — this cross-layer coherence is what separates useful output from hallucinated summaries.

### 2.3 MoE at Scale — 896 Experts, 16 Active

The mixture-of-experts architecture in K3 uses 896 expert modules — subnetworks that each specialize in different types of knowledge or computation — but activates only 16 per token. Combined with the Stable LatentMoE framework, this high-sparsity design means the model's total knowledge capacity scales with the number of experts while the per-token compute cost scales with the number of active experts. Training also uses quantization-aware techniques — MXFP4 weight precision and MXFP8 activation precision — applied from the supervised fine-tuning stage onward, so the model is optimized for low-precision inference from the start rather than being quantized post-training, as documented in [Kimi's API docs](https://platform.kimi.com/docs/guide/kimi-k3-quickstart).

---

## 3. Where K3 Stands — The Benchmark Picture

### 3.1 Artificial Analysis Intelligence Index — Third Globally

The Artificial Analysis Intelligence Index evaluates models across reasoning, coding, and knowledge tasks — a composite that weights multiple benchmarks to estimate real-world capability rather than single-task performance. Kimi K3 scores 57 on this index, placing it third globally behind Claude Fable 5 and GPT-5.6 Sol. It leads Claude Opus 4.8, DeepSeek V4 Pro, and all other open-weight models by a margin that, while not enormous, is consistent across sub-scores, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems).

The composite matters because it reduces the risk of cherry-picking a single benchmark where a model happens to excel. A model that ranks third on a broad intelligence index while ranking first on specific sub-tasks tells you something useful: it is well-rounded enough to be a general-purpose agent, with specific strengths you can route toward.

### 3.2 Frontend Code Arena — First, Overtaking Fable 5

On Arena.AI's Frontend Code Arena, a blind human-preference ranking where users compare model outputs on frontend coding tasks, K3 scores 1,679 — the highest score on the leaderboard, ahead of Claude Fable 5 and GPT-5.6 Sol, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems). This result is significant because frontend coding — generating HTML, CSS, and JavaScript that renders correctly and looks good — requires a combination of code generation accuracy, visual reasoning, and an understanding of how users interact with interfaces. Most models are strong at one or two of these. K3 appears strong at all three, which aligns with its native visual understanding capability.

### 3.3 Knowledge Work and Agentic Benchmarks

K3's performance on long-horizon knowledge work tasks is where the 1-million-token context window becomes visible in the numbers. On AA-Briefcase, a private agentic benchmark from Artificial Analysis designed to test sustained knowledge work over extended time horizons, K3 scores 1,527 — second overall, ahead of GPT-5.6 Sol Max (1,495) and behind only Claude Fable 5 Max (1,587). This result was achieved in a single-agent setup with no context compression or external memory management — the model processed everything inside its native context window, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems).

On BrowseComp, a benchmark for long-horizon, high-difficulty information seeking, K3 scores 91.2 out of 100. On GDPval-AA v2, which measures real-world task performance across 44 occupations and 9 industries, K3 scores 1,687 — ahead of Claude Opus 4.8 Max (1,600). These scores, taken together, describe a model that is not just a strong coder or a strong reasoner — it is a strong autonomous worker, capable of sustaining coherent output across tasks that would exhaust the context window or attention span of smaller models.

---

## 4. What K3 Can Actually Do — Agentic Demonstrations Beyond Benchmarks

Benchmark scores are useful abstractions, but they compress a model's behavior into a single number and discard the qualitative texture of what it can do. Moonshot AI included several demonstrations in its technical materials that show K3 operating in ways no benchmark captures.

### 4.1 Forty-Eight-Hour Autonomous Chip Design

In a proof-of-concept documented in Moonshot AI's technical materials, K3 was tasked with designing a physical chip capable of running a nano-scale version of itself. Over 48 hours of continuous autonomous operation, the model used open-source electronic design automation tools and the Nangate 45nm process library to independently complete the full chip construction pipeline — architectural design, optimization, and verification. The resulting design: a 4 mm² chip integrating 1.46 million standard cells, achieving timing convergence at 100 MHz, with simulated decode throughput above 8,700 tokens per second, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems).

This is not a production chip. It is a demonstration of what Moonshot considers the next competitive frontier: long-range autonomous agent capability. The model sustained multi-step technical work — reading documentation, making design decisions, running verification loops, iterating on failures — for two full days without losing coherence. That is a qualitatively different capability than single-turn coding, where a model writes a function and the human evaluates it. Autonomous chip design requires the model to be its own evaluator, catching its own errors and correcting course without external supervision.

### 4.2 Two-Hour Astrophysics Research Pipeline

In a computational astrophysics case study, K3 reproduced the universal I-Love-Q relation — a complex calculation in neutron star physics that relates a star's moment of inertia, tidal Love number, and quadrupole moment. The work typically takes a senior researcher one to two weeks. K3 completed it in approximately two hours, reading and cross-validating more than 20 papers, evaluating over 300 equations of state, generating more than 3,000 lines of code, and producing a complete numerical pipeline from literature review through computation to validation, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems).

The point here is not that K3 is a physicist. It is that research pipelines — reading papers, implementing methods, validating results, iterating on failures — follow a pattern that is structurally similar to the agentic workflows many businesses run daily. Meeting preparation that requires reading three previous meeting notes, cross-referencing a CRM, and synthesizing a structured brief is a smaller-scale version of the same pattern: ingest multiple documents, connect information across them, produce a coherent output, and validate against known constraints. If K3 can do this at astrophysics-research scale, it can handle the business-scale version with room to spare.

### 4.3 Kernel Optimization Arena

Moonshot AI built an internal evaluation environment called the Kernel Optimization Arena, where models are placed in isolated GPU sandboxes and given up to 24 hours to analyze, rewrite, and verify GPU kernel code. The test covers H200 GPU kernels for attention residuals, KDA linear attention, and 512-head-dimension MLA kernels, plus KDA tasks on a domestic Chinese GPU. K3 at maximum thinking effort performed close to Claude Fable 5 in this environment, meaningfully ahead of Claude Opus 4.8 and GPT-5.6 Sol, as documented in [Moonshot AI's Kimi K3 tech blog](https://www.kimi.com/blog/kimi-k3).

Low-level kernel optimization is one of the hardest coding tasks for any model — it requires understanding hardware constraints, memory hierarchies, and instruction-level parallelism, areas where even experienced human engineers regularly make mistakes. K3's performance here suggests its reasoning depth extends to hardware-aware optimization, not just high-level application logic.

---

## 5. Pricing and the Open-Source Strategy

K3's API pricing — $3 per million input tokens and $15 per million output tokens — makes it the most expensive model ever released by a Chinese AI lab. For comparison, K2.6 costs $0.95 in and $4 out; K2.7 Code costs the same. K3 represents roughly a 3x price increase over the previous generation, putting it on par with Claude Sonnet-class pricing and roughly 60% of Claude Opus 4.8 ($5/$25), as reported by [Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3).

The pricing shift is telling. Chinese AI labs have historically competed on cost — DeepSeek's disruption of the market in early 2025 was a cost story as much as a capability story. K3's pricing at Sonnet-class levels signals that Moonshot AI believes the model's capability justifies premium positioning. Cached input tokens drop to $0.30 per million, and Moonshot AI's Mooncake disaggregated serving architecture — which won the Best Paper award at FAST 2025 — reports cache hit rates above 90% in certain high-reuse scenarios, as documented in the [Mooncake technical report](https://arxiv.org/html/2407.00079v1). At that hit rate, the effective input cost is roughly one-quarter of the standard input price.

The open-source dimension adds another layer. Full model weights are promised by July 27, 2026. If Moonshot AI delivers, K3 will be the first open-weight model at the 3-trillion-parameter scale. The company has framed this as a strategic choice — a bid to become the center of gravity for the global open-source AI developer community, following the path DeepSeek charted but at a significantly larger scale. For enterprise teams evaluating their model stack, an open-weight frontier model creates options that proprietary APIs do not: the ability to fine-tune, self-host on private infrastructure, and build derivative systems without being locked into a specific provider's API contract, as reported by [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems).

The caveat is that inference at 2.8 trillion parameters is not trivial. Even heavily quantized — the model was trained with quantization-aware techniques using MXFP4 weights and MXFP8 activations — running K3 requires substantial GPU infrastructure. The Mooncake serving architecture was designed specifically to make inference at this scale practical, but it remains a server-class model. Community quantization efforts will determine whether it can run on consumer hardware, and the early Reddit reactions suggest skepticism: as one r/LocalLLaMA commenter put it, "I own a RTX 6000 Pro 96 GB, but right now I feel like a guy with 4 GB VRAM."

---

## 6. Known Limitations and Honest Assessment

Moonshot AI's release documentation includes three limitations worth discussing directly, because they affect how the model behaves in agentic workflows.

The first is sensitivity to historical thinking content. K3 was post-trained with reasoning history retention enabled throughout — meaning the model expects its complete chain of thought from previous turns to be present in the context. If an agent framework does not pass back the full reasoning history between turns, or if a conversation switches from another model to K3 mid-session, the context mismatch can cause output quality to degrade. Moonshot recommends using agent frameworks that have been compatibility-validated with K3 and avoiding mid-session model switches. For builders integrating K3 into custom agent pipelines, this means the integration layer needs to preserve reasoning tokens across conversation turns — a requirement that not all agent frameworks handle by default.

The second is a tendency toward over-action. K3 was optimized for long-horizon, high-difficulty tasks, which means it can be too proactive when the task is simple or the user's intent is ambiguous. In practical terms, the model may make decisions the user did not expect — taking actions, choosing directions, or making assumptions — when a more restrained model would ask for clarification. Moonshot's recommendation is to impose explicit behavioral constraints through system prompts and AGENTS.md files, which mirrors the approach most agent builders already use for frontier models. The behavior is a side effect of optimizing for autonomy: a model trained to sustain multi-hour tasks without human check-ins will naturally lean toward action rather than hesitation.

The third is an honest acknowledgment that K3, while competitive, still trails Claude Fable 5 and GPT-5.6 Sol on overall user experience. Benchmark scores place K3 in the same tier as these models on specific tasks — and ahead on frontend coding — but the qualitative feel of interacting with the model, particularly on tasks where nuance, tone, and judgment matter, does not yet match the top two closed-source models. For the majority of agentic workflows where correctness and completeness dominate over stylistic polish, this gap may be negligible. For tasks where the output reads like a conversation rather than a work product, the gap is more noticeable.

Elon Musk commented "Impressive" on coverage of the K3 release — a one-word verdict that captures the general sentiment in the technical community. The model is impressive. It is not yet a Fable 5 replacement in every dimension.

---

## 7. What K3 Means for Agentic Workflows

The practical significance of K3 for anyone building or using agents is not the benchmark scores. It is the architecture.

A 1-million-token context window paired with always-on thinking mode means that long-horizon agent tasks — preparing for a complex client meeting by reading multiple previous meeting notes, cross-referencing a CRM, scanning recent emails, and generating a structured brief — can run in a single model call without context compression or multi-agent workarounds. The model simply reads everything relevant into its context window, reasons across it, and produces the output. The 6.3x decoding speedup from KDA at long context lengths means this does not take proportionally longer than a short-context call.

The visual understanding capability — which K3 uses natively, not through a separate vision encoder bolted on after text training — expands the range of agentic tasks beyond text. A calendar-driven AI agent preparing for a design review can look at the latest mockup screenshots alongside the meeting notes. An agent handling game development tasks can read code, run it, capture the output as a screenshot, compare it to the intended design, and iterate — a visual feedback loop that text-only models cannot execute. K3's Frontend Code Arena #1 ranking makes sense in this context: visual reasoning is not an add-on for K3, it is part of how the model was trained.

For solopreneurs running <a href="/blog/what-is-agentic-calendar">agentic calendar systems</a> where agent cost determines whether the tool is a daily driver or a demo, K3's pricing sits at an interesting inflection point. At $3/$15 per million tokens, running K3 on the hardest events — the ones that genuinely need frontier-level reasoning — costs roughly as much as running GPT-5.5 used to cost for everything. Coupled with K2.7 Code at $0.95/$4 for routine coding tasks and K2.6 for classification and routing, a tiered model strategy that matches model cost to task complexity is now possible within the Kimi model family.

Floatboat has integrated Kimi K3 as a built-in model — no API key, no configuration, no routing layer to build. The model appears in the agent workspace alongside DeepSeek, Claude, Gemini, MiniMax, GLM, and the rest of the built-in model roster. For a detailed walkthrough of which calendar events map to K3's specific capabilities and what different model combinations cost for a typical solopreneur, see <a href="/blog/kimi-k3-floatboat">Kimi K3 in Floatboat — setup and event mapping</a>.

---

## 8. Conclusion

Kimi K3 matters for two reasons that have little to do with the parameter count. The first is architectural: KDA hybrid linear attention and attention residuals are not incremental optimizations. They are structural changes to how large models handle long sequences and deep information flow, and they produce efficiency gains — 75% less KV cache, 6.3x decoding speedup, 2.5x overall scaling efficiency — that shift what is practical to run at scale. The second is strategic: an open-weight model at 2.8 trillion parameters that competes with the best closed-source systems changes the economics of the entire model market. OpenAI and Anthropic justify premium API pricing on the basis of capability. When open-weight models close the capability gap, the pricing justification moves from performance to ecosystem, developer experience, and enterprise features — a different conversation.

The model has real limitations. It is sensitive to context history, can be overly proactive, and does not yet match the qualitative feel of Fable 5 or GPT-5.6 Sol. But for the work that agents actually do — long-horizon coding, knowledge synthesis across documents, autonomous task execution over hours or days — K3 represents a meaningful step forward for anyone who can route complex work to the right model. The full weights arrive on July 27. The architecture is what ships now.

---

## FAQ

### Is Kimi K3 better than Claude Fable 5 or GPT-5.6 Sol?

On specific benchmarks, yes — K3 ranks first on Frontend Code Arena (1,679), ahead of both Fable 5 and GPT-5.6 Sol. On the broader Artificial Analysis Intelligence Index, it ranks third (57) behind Fable 5 and GPT-5.6 Sol. On long-horizon knowledge work (AA-Briefcase), it ranks second (1,527), ahead of GPT-5.6 Sol Max. The honest answer is that K3 is in the same tier as these models — trading blows rather than winning outright — with frontend coding as its clearest advantage.

### Can I run Kimi K3 locally?

K3 is a 2.8-trillion-parameter model. Even with quantization-aware training (MXFP4 weights), running it locally requires server-class GPU infrastructure. A 1.58-bit quantized version would need over 512 GB of RAM just to load. For most developers, the practical access points are the Kimi API or built-in integrations like Floatboat. The open weights release on July 27 will enable community quantization and optimization efforts, but local inference at usable speeds on consumer hardware is unlikely without significant advances in compression techniques.

### What is Kimi Delta Attention?

KDA (Kimi Delta Attention) is a hybrid linear attention mechanism that replaces standard quadratic attention in most layers of the Transformer. In K3, every 4 attention layers follow a 3:1 pattern — 3 KDA layers use linear attention, 1 layer uses full attention. The result is a 75% reduction in KV cache memory usage and up to 6.3x decoding speedup at 1-million-token context lengths, with no loss of retrieval precision at critical points where exact token-level attention is needed.

### Is Kimi K3 fully open source?

Moonshot AI has committed to releasing full model weights by July 27, 2026. The architecture — KDA and AttnRes — was previously published as open research on GitHub. The training code, dataset, and training methodology details are expected in the technical report that accompanies the weight release. At 2.8 trillion parameters, K3 is the largest model for which open weights have been promised. Whether "open weights" plus published architecture constitutes "fully open source" is a debate the AI community has been having for two years — K3 inherits that ambiguity.

### Is Kimi K3 available in Floatboat?

Yes. Kimi K3 is built into Floatboat with zero configuration — no API key, no routing setup, no external accounts. It appears in the agent workspace model selector alongside DeepSeek, Claude, Gemini, MiniMax, GLM, and the rest of the built-in model roster. For a complete guide on which calendar events match K3's capabilities, see the <a href="/blog/kimi-k3-floatboat">Kimi K3 in Floatboat walkthrough</a>.

### When was Kimi K3 released?

Kimi K3 was officially released on July 16, 2026, by Moonshot AI. It is available immediately through kimi.com, the Kimi mobile app, Kimi Work desktop client, Kimi Code CLI, and the Kimi API. Full model weights are scheduled for release by July 27, 2026.
