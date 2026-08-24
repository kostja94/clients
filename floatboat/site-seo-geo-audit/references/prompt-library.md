# Floatboat GEO Prompt Library

> 35 core prompts for manual AI visibility sampling. Run monthly across engines.
> Record: mention / citation-with-link / absent / wrong-info
> **Last updated**: 2026-08-20

---

## How to Use

1. Run each prompt on: **ChatGPT (Search on)**, **Perplexity**, **Google AI Mode / AI Overviews**, **Gemini**, **Copilot** (optional)
2. Log result in spreadsheet: date, engine, prompt_id, brand_mention, link_to_floatboat.ai, cited_url, competitor_present
3. Distinguish **mention** vs **citation with link** vs **referral traffic** (GA4 separate)
4. Sample 3 runs per engine per month — do not conclude from single run

---

## Category A — Brand (5)

| ID | Prompt | Expected cite URL |
|----|--------|-------------------|
| B01 | What is Floatboat? | `/` or `/about` |
| B02 | What is Floatboat.ai? | `/` |
| B03 | Who makes Floatboat? | `/about` |
| B04 | Floatboat pricing | `/pricing` |
| B05 | How to download Floatboat | `/download` |

---

## Category B — Category definition (6)

| ID | Prompt | Expected cite URL |
|----|--------|-------------------|
| C01 | What is calendar-driven AI? | `/blog/calendar-driven-ai-vs-chat-ai` |
| C02 | What is an agentic calendar? | `/` or calendar cluster blog |
| C03 | What is a proactive AI agent? | `/` or `/ai-agent-workspace` |
| C04 | What is a proactive agent OS? | `/` |
| C05 | AI agent that runs on your calendar | `/` or scheduling cluster |
| C06 | Calendar vs chat AI for work | `/blog/calendar-driven-ai-vs-chat-ai` |

---

## Category C — Solopreneur intent (5)

| ID | Prompt | Expected cite URL |
|----|--------|-------------------|
| S01 | Best AI agent for solopreneurs 2026 | `/use-cases/for-solopreneur` or blog |
| S02 | AI tools for solo founders | blog cluster |
| S03 | Should a solo operator use an AI agent? | `/blog/ai-agent-solo-operators` |
| S04 | AI workspace for one person business | `/ai-agent-workspace` |
| S05 | How to automate meeting prep as a solopreneur | `/blog/ai-meeting-preparation` |

---

## Category D — Competitor intercept (8)

| ID | Prompt | Expected cite URL |
|----|--------|-------------------|
| D01 | Best Claude Cowork alternative | `/alternatives/*` or blog |
| D02 | Claude Cowork alternative for Mac | `/alternatives/chatgpt-alternative` or dedicated vs page |
| D03 | ChatGPT alternative for work automation | `/alternatives/chatgpt-alternative` |
| D04 | Best AI scheduling assistant | `/blog/best-ai-scheduling-assistants` |
| D05 | Motion app alternative for solopreneurs | `/alternatives/*` |
| D06 | Manus AI alternative | blog alternatives posts |
| D07 | Notion AI alternative for solopreneurs | `/alternatives/notion-alternative` |
| D08 | Cursor alternative for non-developers | `/alternatives/cursor-alternative` |

---

## Category E — Feature / product (6)

| ID | Prompt | Expected cite URL |
|----|--------|-------------------|
| F01 | AI agent with all models built in no API key | `/models` or `/` |
| F02 | What are Combo Skills in Floatboat? | `/combostore` |
| F03 | Best agent skills store | `/combostore` |
| F04 | AI meeting preparation tool | `/blog/ai-meeting-preparation` |
| F05 | AI follow-up email automation after meetings | `/blog/ai-follow-up-automation` |
| F06 | FloatIM agent native messaging | `/floatim` or `/blog/introducing-floatim` |

---

## Category F — Chinese ecosystem (5)

| ID | Prompt | Engine | Expected |
|----|--------|--------|----------|
| Z01 | Floatboat 是什么 | 豆包 / Kimi / 秘塔 | 品牌准确描述 |
| Z02 | 一人公司 AI 工具推荐 | 豆包 / Kimi | `/zh/` 或中文内容 |
| Z03 | 日历驱动 AI 是什么 | Kimi / 元宝 | 品类定义 |
| Z04 | Claude Cowork 替代品 | 豆包 | 客观对比 |
| Z05 | Floatboat 定价 | 秘塔 | 与官网一致 |

---

## Competitor Co-occurrence Watchlist

When running D-prompts, note if these appear while Floatboat is absent:

| Competitor | Relevance |
|------------|-----------|
| Claude Cowork | Primary intercept |
| Motion, Reclaim | Calendar-adjacent |
| Manus, Eigent, Accomplish | Desktop agent |
| ChatGPT desktop, Gemini | Chat-based baseline |
| Slock, Kollab | Team agent IM |
| skills.sh | Skills directory |

---

## GA4 AI Referrer Regex

Configure exploration filter (Session source matches regex):

```
chatgpt\.com|openai\.com|perplexity\.ai|copilot\.microsoft\.com|gemini\.google|bard\.google\.com|claude\.ai|anthropic\.com|edgeservices\.bing\.com|poe\.com|chat\.deepseek\.com
```

Track separately from prompt sampling — measures click-through, not citation rate.

---

## Baseline Snapshot Template

```markdown
## GEO Baseline — YYYY-MM-DD

| Prompt ID | ChatGPT | Perplexity | Gemini | AIO | Notes |
|-----------|:-------:|:----------:|:------:|:---:|-------|
| C01 | cite / mention / — | | | | |
| D01 | | | | | |
...

**Share of voice (D-category)**: Floatboat cited in __/8 competitor prompts
**Brand accuracy issues**: (list wrong pricing, wrong category, etc.)
```
