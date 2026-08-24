# Priority Rubric — P0 / P1 / P2

> How audit findings get severity assignments.
> **Last updated**: 2026-08-20

---

## Definitions

| Priority | Timeline | Impact |
|:--------:|----------|--------|
| **P0** | Fix this month | Blocks crawling, indexing, AI citation, or conversion on critical paths |
| **P1** | Fix this quarter | Materially hurts SEO/GEO but site still functions |
| **P2** | Backlog / continuous | Optimization, optional enhancements, strategic debt |

---

## P0 Triggers (any one qualifies)

| Category | Example |
|----------|---------|
| Crawl block | AI search bots get 403 on `/` or `/pricing` |
| Index block | T0 page has accidental noindex |
| SSR failure | `/pricing` returns SPA shell < 8KB with no body |
| Schema mismatch | Pricing FAQ schema ≠ visible prices |
| Sitemap gap | Live T1 page (e.g. `/floatim`) missing from sitemap |
| Wrong robots | OAI-SearchBot or PerplexityBot Disallow |
| Entity error | Pricing on site contradicts schema and FAQ |
| Security | Staging indexed with production content duplicate |

---

## P1 Triggers

| Category | Example |
|----------|---------|
| Missing llms.txt | No agent discovery file |
| Google-Extended Disallow | Limits Gemini-side (team wants Allow) |
| Duplicate meta | 10+ combo store pages share description |
| Missing Organization legalName | Schema incomplete |
| Orphan T1 page | `/integrations` no internal links |
| Extractability | Calendar hub blog fails B2 on 50%+ H2s |
| hreflang error | Broken mutual links EN↔ZH |
| Thin alternatives FAQ | <3 questions |

---

## P2 Triggers

| Category | Example |
|----------|---------|
| Link response header | No rel=sitemap Link header |
| Markdown negotiation | No Accept: text/markdown |
| lastmod batch date | All sitemap lastmod same day without updates |
| Blog T3 sample | Minor title length 62 chars |
| Leaderboard not live | Planned Gap — document only |
| Baidu webmaster | Not verified |

---

## Planned Gap vs Fail

| Type | Mark in report | Counts against pass rate? |
|------|----------------|:---------------------------:|
| **Fail** | ❌ | Yes |
| **Warn** | ⚠️ | Partial |
| **Pass** | ✅ | Yes |
| **Planned Gap** | 📋 | No — listed separately |
| **Unknown** | ❓ | Needs manual/GSC access |

---

## Escalation Rules

| Condition | Action |
|-----------|--------|
| ≥3 P0 in same Part | Part marked RED in scorecard |
| Combo store >30% duplicate meta in sample | Elevate to P0 index strategy decision |
| Brand prompt wrong pricing in 2+ engines | P0 entity fix + off-site correction |
| Same P0 unfixed from previous audit | Flag REGRESSION in executive summary |

---

## Owner Assignment

| Finding type | Default owner |
|--------------|---------------|
| robots, sitemap, SSR, schema injection | Engineering |
| Meta, H1, FAQ copy, extractability | Content |
| GSC, IndexNow, GA4 regex | SEO / Analytics |
| llms.txt content | Content + Engineering deploy |
| Prompt snapshot / directory listings | SEO / Marketing |

---

## Scorecard Color

| Pass rate | Color |
|:---------:|:-----:|
| ≥90% | Green |
| 70–89% | Yellow |
| <70% | Red |

Pass rate = (Pass + 0.5×Warn) / (Pass + Warn + Fail) — exclude Planned Gap and Unknown from denominator unless Unknown >20%.
