# Floatboat Internal Links Policy

> Hub-and-spoke architecture rules for sitewide SEO and GEO citation paths.
> **Last updated**: 2026-08-20

---

## Architecture Diagram

```
                    ┌─────────────┐
                    │  / (Home)   │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐
    │ /use-cases │  │/alternatives│  │ /combostore│
    └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
          │               │               │
    ┌─────▼─────┐   ┌─────▼─────┐   ┌─────▼──────┐
    │ for-*     │   │ *-alt     │   │ skill slug │
    │ verticals │   │ pages     │   │ detail     │
    └───────────┘   └───────────┘   └────────────┘

    ┌────────────┐  ┌────────────┐  ┌────────────┐
    │/integrations│  │  /models   │  │  /floatim  │
    └────────────┘  └────────────┘  └────────────┘

    ┌────────────┐  ┌────────────┐
    │/marketplace│  │ /showcases │
    └────────────┘  └────────────┘

                  ┌──────────────┐
                  │  /blog/*     │──── cross-links to all hubs
                  └──────────────┘

Note: `/floatcup-2026` removed (404). `/workflowstore` in sitemap but 404.
```

---

## Hub Responsibilities

| Hub | Must link to | Must receive links from |
|-----|--------------|------------------------|
| `/` (Home) | use-cases, alternatives, combostore, marketplace, floatim, integrations, models, download, pricing, blog | All major sections |
| `/use-cases` | 4 vertical pages, download | Home, blog (solopreneur cluster) |
| `/alternatives` | 12 competitor pages | Home, blog (vs/alternative posts) |
| `/combostore` | Top skills; link to `/marketplace` | Home, blog, marketplace |
| `/marketplace` | combostore; workflow when route live | Home |
| `/showcases` | cases, download | Home |
| `/blog` | Pillar posts in calendar + solopreneur clusters | Home header |
| `/floatim` | im.floatboat.ai, vs-floatboat (if live) | Home, blog introducing-floatim |
| `/pricing` | download, FAQ | Home, alternatives, blog |
| `/download` | pricing, platform requirements | Home, all CTAs |

---

## Anchor Text Rules

| Do | Don't |
|----|-------|
| Descriptive anchors: "AI scheduling agent guide" | "click here", "read more" only |
| Natural product mentions: "Calendar-Driven AI" | Competitor trademarks as primary anchor in titles |
| Link to canonical URL format (pick trailing slash policy) | Mix `/blog` and `/blog/` without redirect |

---

## Blog Cross-Link Requirements

### Calendar-Driven cluster posts must link to:
- `/blog/ai-scheduling-agent` (hub)
- `/blog/calendar-driven-ai-vs-chat-ai` (definition)
- `/download` or `/pricing` (conversion)
- At least one `/use-cases/for-solopreneur`

### Alternative/intercept posts must link to:
- Relevant `/alternatives/{competitor}-alternative`
- `/blog/calendar-driven-ai-vs-chat-ai` when comparing chat vs calendar

### Skills-related posts must link to:
- `/combostore` hub
- Specific skill detail if discussing named skill

---

## Orphan Page Detection

**Orphan** = in sitemap but zero internal links from other indexable pages (excluding sitemap-only discovery).

| Audit step | Method |
|------------|--------|
| 1 | Export sitemap URLs |
| 2 | Crawl internal `<a href>` from Home + Blog hub + Alternatives hub (depth 3) |
| 3 | Flag sitemap URLs not reached | 
| 4 | Priority: T0/T1 orphans = P0; T4 combo = P2 unless strategic |

Known risk: Combo detail pages may be **orphans** if hub loads links via client JS only — verify `<a href>` in raw HTML.

---

## Click Depth Rule

| Tier | Max clicks from `/` |
|------|:-------------------:|
| T0, T1 | 2 |
| T2 blog pillars | 3 |
| T3 blog general | 3 (via blog hub) |
| T4 combo detail | 3 (via combostore hub) |

---

## Footer / Header Minimum

**Header** (confirmed live):
- Logo → `/`
- Combo Store → `/combostore`
- Blog → `/blog`
- Pricing → `/pricing`
- Download → `/download`

**Footer**:
- About, Blog, Pricing
- Privacy, Terms

Audit: Header/Footer identical on all T0–T2 templates.

---

## Audit Checklist

| # | Check | P |
|---|-------|---|
| L1 | Home links to pillars: use-cases, integrations, models, combostore, **marketplace**, floatim, download | P0 |
| L2 | Alternatives hub links all 12 verticals | P1 |
| L3 | Calendar blog cluster interlinked | P1 |
| L4 | No important T1 page is orphan | P0 |
| L5 | `/floatim` links to im.floatboat.ai with clear rel | P1 |
| L6 | Canonical URL format consistent in internal links | P1 |
| L7 | Combo store detail pages link back to hub | P2 |
