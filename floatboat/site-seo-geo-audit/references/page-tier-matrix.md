# Floatboat Page Tier Matrix

> Defines audit depth, URL patterns, pass thresholds, and sample sizes per page type.
> **Last updated**: 2026-08-20

---

## Tier Overview

| Tier | Label | URL patterns | Audit depth | Sample |
|:----:|-------|--------------|-------------|--------|
| **T0** | Critical conversion | `/`, `/pricing`, `/download`, `/about`, `/combostore`, `/marketplace` | Full meta + schema + SSR + FAQ + GEO | 100% |
| **T1** | High-intent landing | `/alternatives/*`, `/use-cases/*`, `/floatim`, `/integrations`, `/models`, `/showcases`, `/ai-agent-workspace`, `/app` | Full meta + schema + SSR + FAQ | 100% |
| **T2** | Priority blog cluster | See § Blog clusters below | Full + extractability | 100% of cluster list |
| **T3** | General blog | `/blog/*` (not in T2) | Meta + H1 + canonical + thin check | 15% random (min 10) |
| **T4** | Combo Store detail | `/combostore/{name}-{shortId}` | Meta + H1 + body volume + duplicate | 30 random |
| **T5** | Utility / legal | `/privacy`, `/terms`, `/wishlist`, `/user-protection-program-terms`, `/selfware.md` | robots + meta + indexability | 100% |

---

## Minimum HTML Body Thresholds

Used by `tools/crawl_probe.py` and manual curl checks. Values are **heuristic** — SPA shells typically < 8 KB.

| Tier | Min raw HTML size | Fail signal |
|------|------------------:|-------------|
| T0 marketing | 25 KB | Likely SPA empty shell |
| T1 landing | 15 KB | Thin or JS-only |
| T2 blog post | 20 KB | Missing SSR body |
| T4 combo detail | 8 KB | Template-only shell |
| T5 legal | 5 KB | Acceptable if text present |

Additional pass rule: raw HTML must contain visible H1 text and ≥ 200 words of body (strip tags estimate).

---

## T0 Pages — Checklist Subset

| Path | Primary keyword intent | Required blocks |
|------|------------------------|-----------------|
| `/` | Proactive Agent OS, Calendar-Driven AI | Hero H1, FAQ (≥6), Organization schema, SoftwareApplication schema |
| `/pricing` | Floatboat pricing, AI agent pricing | FAQ (≥5), pricing table, AggregateOffer or offers in schema |
| `/download` | Floatboat download Mac Windows | Platform CTAs, SoftwareApplication |
| `/about` | Floatboat company, AOE Tech Labs | Founder, legal entity, sameAs candidates |
| `/combostore` | Agent Skills Store, Skills Marketplace | Indexable intro; mentions Combo + Workflow stores |
| `/marketplace` | Agent marketplace acquisition surface | Indexable intro copy |

---

## T1 Pages — Checklist Subset

### Alternatives (`/alternatives/*`)

| Requirement | Pass standard |
|-------------|---------------|
| Objective comparison | Table or bullets; includes competitor strengths |
| FAQ | ≥3 questions, first sentence answers directly |
| Title | Contains `{Competitor} alternative` pattern |
| Internal links | Links to `/download`, relevant blog, `/combostore` where natural |
| Canonical | Self-referencing `https://floatboat.ai/alternatives/...` |

Live alternatives (12 verticals + hub):
- airtable, asana, chatgpt, clickup, cursor, github-copilot, lovable, monday, n8n, notion, todoist, zapier

### Use Cases (`/use-cases/*`)

| Path | Audience keyword |
|------|------------------|
| `/use-cases` | hub |
| `/use-cases/for-solopreneur` | solopreneur |
| `/use-cases/for-creators` | creators |
| `/use-cases/for-small-business` | small business |
| `/use-cases/for-studio` | studio |

Pass: EN pages use **solopreneur** not "one-person company" in title/H1.

### Product landings (often live but missing from sitemap — P0 gap)

| Path | Purpose | Live (2026-08-20) |
|------|---------|-------------------|
| `/integrations` | 3,500+ integrations narrative | 200 |
| `/models` | All frontier models built in | 200 |
| `/floatim` | FloatIM product bridge to im.floatboat.ai | 200 |
| `/showcases` | Case/showcase library | 200, in sitemap |
| `/marketplace` | Combo + Workflow marketplace hub | 200, in sitemap |

**Removed / broken — do not audit as live:**
| Path | Status |
|------|--------|
| `/floatcup-2026` | 404 (campaign ended) |
| `/workflowstore` | 404 but listed in sitemap — **P0 sitemap bug** |
| `/combo-store` | 404 — use `/combostore` |

---

## T2 Blog Clusters — Full Audit List

Audit **every URL below** for meta + extractability (see `references/extractability-site-audit.md`).

### Cluster A — Calendar-Driven (core moat)

| Slug | Primary intent |
|------|----------------|
| `calendar-driven-ai-vs-chat-ai` | Category definition |
| `ai-scheduling-agent` | Hub definition |
| `ai-meeting-preparation` | Meeting prep |
| `ai-follow-up-automation` | Follow-up |
| `best-ai-scheduling-assistants` | Ranking |
| `best-ai-scheduling-assistant` | Ranking variant |
| `best-calendar-app-solo-operators` | Calendar + solopreneur |
| `google-calendar-vs-outlook` | Calendar comparison |
| `google-calendar-vs-apple-calendar` | Calendar comparison |

### Cluster B — Solopreneur / workspace

| Slug | Primary intent |
|------|----------------|
| `ai-agent-solo-operators` | Should solo operator use AI agent |
| `ai-workflow-for-solo-founders` | Workflow |
| `how-one-person-businesses-work-like-a-team-with-ai` | Team narrative |
| `workspace-agents-for-solo-operators` | Workspace agents |
| `workspace-agents-vs-chat-assistants` | vs chat |

### Cluster C — Claude / Cowork intercept

| Slug | Primary intent |
|------|----------------|
| `claude-code-non-developers-solo-operators` | Cowork adjacent |
| `what-are-claude-managed-agents` | Managed agents |

### Cluster D — FloatIM

| Slug | Primary intent |
|------|----------------|
| `introducing-floatim` | Product announcement |

### Cluster E — High GSC exposure (monitor in audit)

| Slug | Note |
|------|------|
| `genspark-ai-pricing` | High impressions — check CTR/thin |
| `genspark-vs-manus` | Comparison traffic |
| `manus-ai-alternatives-2026` | Alternatives intercept |

---

## T4 Combo Store — Sampling & Rules

**URL pattern**: `/combostore/{name}-{shortId}` where `shortId` = 6-char Base62.

| Check | Rule | Fail action |
|-------|------|-------------|
| Unique title | No duplicate titles in sample | P1 — template fix |
| Unique meta description | No duplicate descriptions in sample | P1 |
| H1 present | Skill name visible in HTML | P0 if mass fail |
| Body volume | ≥ 8 KB OR ≥ 150 words visible | P1 thin content |
| Index strategy | If >400 pages with near-duplicate meta → recommend noindex or enrich | P0 strategic |

See `references/combo-store-rules.md` for full policy.

---

## Title / Meta Standards (all tiers)

| Field | Standard |
|-------|----------|
| `<title>` | Unique; 50–60 characters; primary keyword in first half; brand `Floatboat` at end with `\|` or `—` |
| `<meta name="description">` | Unique; 120–160 characters; value prop + audience |
| `<h1>` | Exactly one; matches page intent; not identical to title |
| `canonical` | Absolute `https://floatboat.ai/...`; self-referencing unless hreflang pair |
| `robots` | Indexable pages: absent or `index,follow`; utility pages: explicit policy documented |

### Title templates (reference)

| Page type | Template |
|-----------|----------|
| Home | `Floatboat — Proactive Agent OS for Calendar-Driven Work` |
| Alternative | `Best {Competitor} Alternative for Solopreneurs \| Floatboat` |
| Blog hub | `Floatboat Blog — Calendar-Driven AI & Solopreneur Guides` |
| Combo Store hub | `Agent Skills Store — Browse AI Skills for Desktop \| Floatboat` |
| FloatIM | `FloatIM — Agent-Native IM for Humans and AI Agents \| Floatboat` |

---

## Indexability Matrix

| Page type | Default index | Sitemap | Notes |
|-----------|:-------------:|:-------:|-------|
| T0–T2 | yes | yes | |
| T3 blog | yes | yes | |
| T4 combo detail | yes* | yes | *Revisit if duplicate meta epidemic |
| `/app` | case-by-case | no | Often login — prefer noindex if thin |
| `/wishlist` | yes | if valuable | |
| Legal | yes | optional | low priority |

---

## Sitemap Expectations (2026-08-20 live)

Current sitemap has **31 URLs** — not ~620. Typical structure:

| In sitemap | Often missing from sitemap (still live) |
|------------|----------------------------------------|
| `/`, `/about`, `/pricing`, `/download`, `/blog` (hub) | `/blog/{slug}` posts |
| `/combostore` (hub) | `/combostore/{name}-{id}` details |
| `/alternatives/*` (13) | `/use-cases/*`, `/integrations`, `/models`, `/floatim` |
| `/marketplace`, `/showcases` | `/zh/*` localized pages |
| `/workflowstore` (**404 — remove**) | |

**Audit rule**: Low sitemap count is not automatically wrong — but if blog/combo **posts** get traffic in GSC, missing URLs are **P0**.

---

## Audit Sample Seed

For reproducible T3/T4 sampling, use slug hash modulo:

```python
# In combo_store_sample.py — seed=20260820 for Aug 2026 audit
import random
random.seed(20260820)
```

Document actual sample URLs in audit report appendix.
