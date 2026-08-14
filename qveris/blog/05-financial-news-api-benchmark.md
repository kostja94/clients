---
slug: financial-news-api-benchmark
metaTitle: "Financial News APIs 2026: 7 Providers Live Benchmark | QVeris"
description: "A dated, reproducible live benchmark of 7 financial news APIs — Brave, Caidazi, EODHD, Finlight, Gildata, Linkup, NewsAPI — across company discovery, ticker lookup, language coverage and relevance."
author: "QVeris Team"
publishedAt: "2026-07-28"
updatedAt: "2026-07-28"
readTime: "15 min read"
---

# Financial News APIs for AI Agents: 7 Providers Live-Tested

*We ran a controlled live benchmark of seven financial news providers on August 3, 2026: 316 completed observations across 158 tool-case cells, every cell run twice, plus a 44-observation strict ticker comparison across nine markets. Finlight was the strongest structured ticker-news option (24/24 processable responses, relevant in both rounds for all nine listing markets). Linkup produced the broadest requested-language retrieval. Gildata and Caidazi led Chinese specialist workflows. This is a dated observation, not a permanent ranking.*

## TL;DR

- **Fast answer** — There is no honest universal winner. In this dated comparison, Finlight was the strongest structured ticker-news option with 24/24 processable responses and relevant results in both rounds for all nine listing markets. Linkup produced the broadest observed requested-language retrieval, but it is a Web retrieval product rather than a strict financial news feed.
- **Important boundary** — A processable response, the expected empty/non-empty shape, and relevant news are separate metrics. Combining them would reward irrelevant fallback content and punish honest empty results.
- **Keep product shapes separate** — Global discovery, strict ticker filtering, multilingual retrieval, sentiment fields, and regional specialist feeds are different buying decisions. Pick by the agent workflow, not a universal score.

## What we tested

We ran a controlled, reproducible product-selection benchmark of seven financial news suppliers on August 3, 2026. The broad comparison contains 316 completed live observations across 158 tool-case cells, with every cell run twice. Cases cover companies, macro, crypto, forex, invalid input, and specialist feeds across nine market regions and seven requested languages. The strict ticker comparison contains 44 completed observations across 22 product-case cells: nine listing markets, one invalid ticker control, and provider-specific ticker-dialect controls. A market passed only when both rounds returned news relevant to the target company.

The fixed public shortlist is Brave, Caidazi, EODHD, Finlight, Gildata, Linkup, and NewsAPI. A supplier remains visible even when a later retest falls below the gate, preserving comparability between editions.

The scoring unit is one observation: one product, one applicable case, and one live round. A cell is one product-case pair; an API invocation is one physical request. N/A means the inspected contract cannot express the request. Not qualified means applicable tests completed but the best supplier tool did not clear the scenario gate. The two-round design is deliberate: a single round can be lucky, but a result that repeats across two independent rounds is a repeatable signal inside the test window. The published calculation rules also make the whole exercise auditable — anyone with a test credential can reproduce a cell and check whether the score moves for product reasons or methodology reasons.

## How the metrics are calculated

Each metric answers a distinct question, and the calculation rules are published so a retest can reproduce them.

| Metric | Public calculation and pass rule |
| --- | --- |
| Processable response rate | Completed observations that returned a structurally usable response divided by all completed observations. Transport-and-shape measure, not proof the returned news is relevant. |
| Expected-response rate | Positive cases pass when at least one article is returned. The invalid-input control passes only when no article is returned. |
| Relevant-result round rate | Applicable live rounds returning at least one relevant top-five row divided by completed applicable rounds. |
| Top-5 relevance | Relevant rows among the first five results. A row is relevant when the requested entity or topic alias appears in its title, summary, or structured entity fields. |
| Fresh-record rate | Returned rows with a usable publication time inside the case's seven-day window divided by all returned rows; a missing time does not receive freshness credit. |
| Core-field completeness | Present values for title, URL, publication time, source, and summary divided by the expected core-field values in returned rows. |
| Observable source diversity | Distinct normalized source values per non-empty observation. Zero means no usable normalized source field, not zero upstream publishers. |
| Duplicate rate | Repeated normalized URLs or title-and-date identities divided by returned rows. |
| Sentiment coverage | Relevant rows with an exposed sentiment value divided by relevant rows. Measures availability, not sentiment accuracy. |
| Requested-language rate | Rows matching the requested language divided by rows whose language is explicit or detectable. The observation denominator is always shown. |
| Requested-country rate | Rows matching the requested country divided by rows with observable country metadata in cases requesting a concrete country. |
| Median latency | Median end-to-end elapsed time across completed live observations. An observation from this run, not an SLA. |
| Strict ticker-market pass | A real market passes only when both rounds return news relevant to the target company through the provider's dedicated ticker or symbol input. |
| Negative-control pass | The invalid query or ticker returns no article. An irrelevant fallback is a failure, not a successful result. |

A scenario ranking requires at least 50% processable responses, relevant results in at least 50% of applicable rounds, and contract coverage for at least 50% of fixed cases. The multi-market ticker ranking separately requires at least 50% processable responses and repeatable relevant results in five or more of nine markets. This is a controlled benchmark, not an academic study or a long-term SLA certification — two rounds show repeatability during the test window, not monthly reliability.

### Why negative controls are part of the gate

The invalid-input control is deliberately strict: an irrelevant fallback is a failure, not a successful result. Several suppliers returned fallback content for a deliberately nonexistent query during this run, which is the behavior most likely to corrupt an agent's output because it arrives wrapped in a valid response envelope. An agent that trusts the envelope will surface a wrong entity as if it were relevant news. In practice, this means a production pipeline should run its own relevance guard after any news capability — check that the requested entity or topic alias actually appears in the returned title, summary, or structured fields — regardless of which supplier is behind the call.

### What "not qualified" means

A supplier marked "not qualified" for a scenario completed the applicable tests but its best tool did not clear the scenario gate — for example, NewsAPI's global company discovery returned relevant results in 38% of applicable rounds, below the 50% threshold. It does not mean the product is broken; it means that, within the fixed case set and test window, the tool did not repeatably produce relevant results for that workflow. A supplier remains visible in the results table even after falling below the gate, so scores between editions stay comparable.

## The headline results

| Supplier | Global company discovery | China/HK company news | China specialist news | Macro/cross-asset | Multi-market ticker |
| --- | --- | --- | --- | --- | --- |
| Brave | Not qualified — 75% (4) | N/A | N/A | Qualified — 83% (6) | N/A |
| Caidazi | Qualified — 67% (18) | Qualified — 100% (4) | Qualified — 100% (6) | Qualified — 50% (12) | N/A |
| EODHD | Qualified — 78% (18) | Qualified — 100% (4) | N/A | N/A | Qualified — 7/9 markets |
| Finlight | Not qualified — 50% (4) | N/A | N/A | Qualified — 67% (6) | Qualified — 9/9 markets |
| Gildata | Qualified — 78% (18) | Qualified — 100% (4) | Qualified — 100% (6) | Qualified — 83% (12) | N/A |
| Linkup | Qualified — 100% (18) | Qualified — 100% (4) | N/A | Qualified — 100% (12) | N/A |
| NewsAPI | Not qualified — 38% (16) | Not qualified — 0% (4) | N/A | Qualified — 80% (10) | N/A |

## Best observed fits by agent workflow

Use the workflow-specific result, not a universal score. The observed patterns fall into four groups. For strict multi-market ticker news, Finlight led with 24/24 processable responses, relevant results in both rounds across all nine listing markets, and clean negative-control behavior. For global company discovery and macro/cross-asset retrieval, Linkup was the repeatability leader — 18/18 and 12/12 relevant observations respectively — while NewsAPI followed at 8/10 in macro discovery. For China/HK company workflows, Gildata Stock News, EODHD, and Linkup each returned relevant results in all applicable observations, with Caidazi WeChat Search offering the freshest records. For Chinese specialist news, Caidazi Hybrid Search V2 and Gildata Public Opinion both hit 100% top-5 relevance across six observations, with Caidazi materially faster and more structurally complete.

## Scenario-level trade-offs

### China/HK company news

EODHD and Gildata Stock News were highly relevant in the fixed company cases. Caidazi exposed richer observable source and core-field data. A zero source count means the normalized response exposed no usable source value — it does not mean the supplier ingested zero publishers.

The practical takeaway for this scenario is that relevance and structure trade off against each other. EODHD returned 100% top-5 relevance but exposed no usable source field and zero fresh records inside the seven-day window — a strong answer for a static research agent, a weaker one for a news-monitoring agent that needs recency. Caidazi WeChat Search returned fresh records with a richer source count, which suits a workflow that emphasizes timeliness over exact-match depth. Gildata Stock News was the slowest in the group at a 17.6-second median, which matters for interactive agents but less for scheduled batch jobs.

### Chinese specialist news

Caidazi Hybrid Search V2 and Gildata Public Opinion both returned relevant results in all six observations and reached 100% top-five relevance. Caidazi was faster and more structurally complete in this run.

The decision between the two is mostly latency and field completeness versus raw volume. Caidazi completed every observation at roughly a 2.5-second median with 100% core-field completeness, while Gildata Public Opinion matched relevance but took 25 seconds and exposed fewer structured fields. For a Chinese fund, industry, or organization research workflow, the faster and more structured option is easier to wire into an interactive agent; the slower one may still be justified when its specific index coverage is what the product needs.

### Macro and cross-asset news

Linkup had the strongest relevant-result repeatability. An invalid-control failure means the endpoint returned fallback content for the deliberately nonexistent query — agents should add their own relevance guard.

Macro and cross-asset discovery is where the product-shape boundary shows up most clearly. Linkup returned relevant results in every applicable observation across both rounds, but exposed only 40% core-field completeness — it is a Web retrieval product, not a structured feed, so an agent consuming it should expect to parse and re-verify the source and timestamp itself. Finlight's financial news endpoint was faster and fully structured but relevant in four of six rounds and failed its invalid control by returning fallback content. NewsAPI Everything sat in between: familiar keyword semantics, 80% relevant rounds, but weak negative-control behavior. Agents monitoring macro themes are best served by treating the retrieval layer as a candidate generator and applying their own relevance and freshness gate before the model reasons over the results.

### Scenario highlights at a glance

The compact table below keeps only the decision-critical columns across the three scenario groups. Full per-product detail is retained in the analysis above each group.

| Scenario | Product | Relevant rounds | Top-5 relevance | Median latency | Invalid control |
| --- | --- | --- | --- | --- | --- |
| China/HK | Caidazi WeChat Search | 4/4 | 60% | 2,388 ms | 0/2 |
| China/HK | EODHD Financial News | 4/4 | 100% | 2,585 ms | 0/2 |
| China/HK | Gildata Stock News | 4/4 | 95% | 17,621 ms | 2/2 |
| China/HK | Linkup Search | 4/4 | 60% | 4,177 ms | 0/2 |
| Chinese specialist | Caidazi Hybrid Search V2 | 6/6 | 100% | 2,547 ms | — |
| Chinese specialist | Gildata Public Opinion | 6/6 | 100% | 25,013 ms | — |
| Macro/cross-asset | Brave News Search | 5/6 | 96% | 2,443 ms | 0/2 |
| Macro/cross-asset | Caidazi Hybrid Search | 6/12 | 43% | 3,938 ms | 0/2 |
| Macro/cross-asset | Finlight Financial News | 4/6 | 90% | 2,091 ms | 2/2 |
| Macro/cross-asset | Gildata Public Opinion | 10/12 | 90% | 14,603 ms | 2/2 |
| Macro/cross-asset | Linkup Search | 12/12 | 100% | 4,560 ms | 0/2 |
| Macro/cross-asset | NewsAPI Everything | 8/10 | 70% | 1,922 ms | 2/2 |

Reading the compact view, the cleanest signals are the two specialist wins — Caidazi and Gildata at 6/6 with 100% top-5 relevance — and Linkup's repeatability in macro discovery. The latency column also separates interactive candidates (Caidazi, Brave, Finlight, NewsAPI at roughly 2–4 seconds) from batch-only options (both Gildata tools at 15–25 seconds).

## Strict ticker lookup by market

Ticker support is not keyword recall. A product may find an article containing "Toyota" yet fail a strict `7203.T` lookup. Normalize each user symbol to the provider's native dialect before calling the endpoint.

Finlight completed 24/24 strict-ticker calls and passed US, HK, CN, JP, DE, FR, BR, IN, and ES in both rounds. The negative controls — an invalid ticker, `600519.SS`, and secondary listing `PETR4` — returned empty in both rounds. EODHD passed seven of nine markets.

| Product | Markets passing both rounds | Edge-case behavior |
| --- | --- | --- |
| Finlight Financial News | US, HK, CN, JP, DE, FR, BR, IN, ES | Invalid ticker, 600519.SS, and secondary listing PETR4 returned empty in both rounds; primary tickers passed |
| EODHD Financial News | US, HK, CN, DE, FR, BR, ES | JP, IN, and invalid ticker returned provider errors |

The strict-ticker results have a direct consequence for agent design: the provider's native ticker dialect must be resolved before the call, not guessed by the model. A portfolio agent that tracks US and Hong Kong listings should maintain a symbol-normalization map per provider and surface a provider error as an explicit outcome rather than a silently empty result. This is the same evidence-contract discipline we describe in the [real-time stock price API guide](/blog/real-time-stock-price-api), where symbol identity, feed, and timestamp are validated before a quote reaches the model. For a deeper look at how free tiers across data providers differ, see the [free stock API comparison](/blog/stock-api-free-comparison).

## Which languages do the news APIs support?

Language coverage has three layers: what the vendor documents, what the current integration lets an agent request, and what the fixed live cases returned. Do not infer an undocumented inventory from one successful result.

Linkup returned relevant requested-language results in de, en, es, fr, ja, pt, and zh, but exposes no explicit language filter in the tested contract. NewsAPI exposed 14 language codes, while only English repeated in the fixed company cases. Finlight's native API documents one ISO 639-1 filter per request; the current QVeris connector does not expose it. A separate native correction suite repeated Chinese results for zh, zh-CN, and zh-Hans.

The distinction between a documented language and a repeatable observed language matters for an agent's expected behavior. A multilingual agent should not assume that declaring a language code guarantees relevant local-market results. In this run, NewsAPI advertised the broadest code set yet only English repeated in the fixed company cases, which suggests the declared inventory is not a coverage guarantee. Linkup delivered the broadest observed multilingual recall precisely because it is a general Web retrieval product with no strict news-feed contract — a trade-off teams must weigh before wiring it into a pipeline that needs structured provenance.

| Product | Documented or exposed language control | Repeatably observed requested languages |
| --- | --- | --- |
| Finlight Financial News | Native API accepts one ISO 639-1 language per request and normalizes aliases; current integration does not expose the parameter | Connector: en; native correction suite: zh, including zh-CN and zh-Hans aliases |
| Linkup Search | No explicit language filter in the tested contract | de, en, es, fr, ja, pt, zh |
| NewsAPI Everything | 14 exposed codes: ar, de, en, es, fr, he, it, nl, no, pt, ru, sv, ud, zh | en |
| Brave News Search | Current integration enumerates ar, bg, bn, ca, en, eu | en |

## Selection guidance

Choose Finlight when the agent starts from a ticker and needs structured entities, sentiment labels, categories, provenance, and clean negative-control behavior. Choose EODHD when broad exchange-coded ticker coverage matters and the agent can handle provider errors explicitly. Choose Linkup when multilingual recall and citations matter more than a strict news-feed contract. Choose Brave for English discovery within its tested scope. Choose NewsAPI for a familiar keyword API and explicit language selection, while recognizing that declared language options do not guarantee relevant local-market results. For China/HK company workflows, compare Gildata Stock News, EODHD, Linkup, and Caidazi WeChat Search against the response shape you actually need. For Chinese fund, industry, and organization workflows, compare Caidazi Hybrid Search V2 with Gildata Public Opinion.

Reading the guidance as a whole, the pattern is that the right supplier follows the data shape the agent consumes. An agent that answers "what did this ticker just release" needs strict ticker filtering and structured fields, which points to Finlight or EODHD. An agent that answers "what is the market watching today" needs broad multilingual recall, which points to Linkup. An agent that serves Chinese-speaking users on specialist workflows should shortlist the China-native suppliers. A workflow that combines several of these questions is exactly the case for a routing layer that can switch sources per request rather than wiring the agent to one vendor.

## How to build a financial news benchmark of your own

The reproducible discipline matters more than the specific results. Freeze the case list — companies, macro, crypto, forex, invalid inputs, and specialist feeds across the markets and languages you serve. Run every cell twice to separate a one-off from a repeatable result. Record the exact endpoint, schema, and parameter dialect used, because a score change between editions should reflect the product, not a rewritten benchmark. Keep negative controls: an invalid ticker that returns irrelevant fallback content is a failure, not a successful result. Report processable rate, expected-shape rate, and relevance as separate numbers so honest empty results are not punished.

The most common mistake in home-grown benchmarks is collapsing three questions into one score. A supplier can return a structurally valid response, an empty result that is correctly empty, and irrelevant fallback content in the same day — and a single "accuracy" number would hide all three behaviors. Publishing the calculation rules (as in the metrics table above) is what lets a retest distinguish a product change from a methodology change. It is also what makes a benchmark honest about latency: median end-to-end time in this run is an observation from a specific region, feed, and client, not an SLA claim.

A second common mistake is treating one successful result as coverage. The language section of this benchmark exists precisely because a supplier that returned one relevant German article is not evidence of German coverage. The discipline applies to tickers too: a keyword hit on "Toyota" does not make the endpoint a strict `7203.T` lookup. Design the case list to force these distinctions instead of discovering them after the agent is in production.

A multi-provider agent should apply the same relevance guard regardless of supplier. When the agent needs to discover, inspect, and call news capabilities across several vendors, QVeris surfaces capability coverage, provider choice, per-call cost, and output contract before a call executes — the tested tools (Finlight Financial News, Linkup Search, Gildata Stock News, Caidazi Hybrid Search, EODHD Financial News, and NewsAPI Everything) are inspectable through the provider hub.

## Limitations and retest checklist

This is a dated live observation, not a permanent claim about a provider's full inventory. Results vary with the news cycle, plan, licensing, indexing delay, and integration schema. Empty results show what the fixed query returned in the test window; they do not prove contractual non-support. Rerun quarterly and after any material endpoint, source, plan, schema, language, or ticker-routing change, keeping cases stable so score changes reflect the product rather than a rewritten benchmark.

The retest checklist: exact endpoint and stable schema; supported ticker formats and exchanges; language codes and whether filtering is article-level or source-level; country-field semantics; source, licensing, and freshness constraints; invalid-input and empty-result behavior.

## Conclusion

In this dated live benchmark, Finlight led structured multi-market ticker news, Linkup led global discovery and multilingual retrieval, and Gildata and Caidazi led Chinese specialist workflows. No provider is a universal winner, and the correct choice is defined by the agent workflow: the data shape, the ticker dialect, the language coverage, and the licensing you actually need. For agents that must compare or combine several of these sources, the disciplined benchmark — reproducible cases, separate metrics, negative controls, quarterly retest — is the same discipline a multi-provider routing layer applies before any call executes.

## Frequently asked questions

### Can I search financial news by stock ticker?

Yes. Several tested integrations exposed dedicated ticker or symbol inputs, but only Finlight and EODHD met the published multi-market ranking gate. Normalize the user's symbol to each provider's dialect.

### Which API had the broadest observed language coverage?

Linkup repeated relevant results in all seven requested languages, but it is a Web retrieval product rather than a strict structured financial news feed. Among explicit news APIs in the tested integrations, English was the only language repeated in the fixed company cases.

### How often should the benchmark be rerun?

Quarterly, and after any material endpoint, source, plan, schema, language, or ticker-routing change. Keep the cases stable.

### What makes a news result "relevant" in this benchmark?

A row is relevant when the requested entity or topic alias appears in its title, summary, or structured entity fields, within the top five results. Top-5 relevance is reported separately from processable rate and freshness so the three questions are not collapsed into one number.

### How should an agent handle a supplier that returns fallback content for an invalid query?

Treat it as a negative-control failure and add your own relevance guard. An irrelevant fallback is not a successful result, and an agent that trusts it will surface wrong context as if it were news.
