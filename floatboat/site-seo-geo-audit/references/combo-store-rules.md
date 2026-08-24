# Floatboat Combo Store SEO Rules

> Audit policy for Combo Store (`/combostore`) and related marketplace surfaces.
> **Last updated**: 2026-08-20 (live-verified)

---

## Scale Context (live vs historical)

| Metric | Historical (2026-06) | Live (2026-08-20) |
|--------|--------------------:|------------------:|
| Hub URL | `/combostore` | `/combostore` ✅ |
| Detail pattern | `/combostore/{name}-{shortId}` | Still works (e.g. `bracket-boss-1nKR69` → 200) |
| Detail count (approx) | ~506 | **Unknown** — not in sitemap; sample via fallback |
| Sitemap | Hub + 506 details | **Hub only** — details omitted |
| Wrong path | — | `/combo-store` → **404** |

**Related surfaces (2026-08)**:
- `/marketplace` — live, in sitemap (Combo + Workflow narrative)
- `/workflowstore` — **404** but wrongly in sitemap
- Homepage mentions **Workflow Store** alongside Combo Store

---

## Strategic Options

| Strategy | When to use |
|----------|-------------|
| **A — Full index + enrich** | Each skill page unique; **restore detail URLs to sitemap** |
| **B — Hub + marketplace only** | Detail pages noindex; traffic via `/combostore` + `/marketplace` |
| **C — Current de-facto state** | Hubs in sitemap; details discoverable via internal links / search — **high indexing risk** |

Live state matches **C** — audit should flag if GSC shows blog/combo post traffic.

---

## Hub Page (`/combostore`) Requirements

| Field | Pass standard | P |
|-------|---------------|---|
| Indexable intro | ≥150 words; mentions Combo + Workflow value prop | P0 |
| Title | "Agent Skills Store" / "Skills Marketplace" / Combo Store | P0 |
| SSR | Not empty shell — live ~303KB HTML | P0 |
| Crawlable detail links | `<a href="/combostore/...">` in raw HTML for top items | P1 |

---

## Detail Page Template Requirements

Apply when sampling live URLs (sitemap or fallback list):

| Field | Pass standard | P |
|-------|---------------|---|
| Title unique | `{Skill Name} — … \| Floatboat` | P0 |
| Meta description unique | 120–160 chars | P0 |
| Body | ≥150 words or structured sections | P1 |
| Live check | HTTP 200 even if not in sitemap | P0 |

---

## Sampling Protocol

1. Run `python tools/combo_store_sample.py -n 30 --seed {YYYYMMDD}`
2. If sitemap has 0 detail URLs, tool uses **fallback samples** — note in report
3. Optionally expand sample from `/combostore` hub HTML links

---

## Pass/Fail Summary

| Metric | Pass | Warn | Fail |
|--------|------|------|------|
| Hub in sitemap | Yes | — | No |
| Hub SSR | Present | — | Empty |
| Detail pages live | Sample 200 | — | Mass 404 |
| Detail pages in sitemap | Team choice | Hub only (current) | N/A |
| `/combo-store` alias | 301→combostore or unused | — | 404 confusion |
