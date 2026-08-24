# Floatboat JSON-LD Schema Specification

> Site-side structured data requirements for SEO rich results and GEO entity extraction.
> Agent validates **live HTML output** only — not local blog repo drafts.
> **Last updated**: 2026-08-20

---

## Global Rules

| Rule | Standard |
|------|----------|
| Format | JSON-LD in `<script type="application/ld+json">` |
| Domain in `@id` | Always `https://floatboat.ai/...` — never im.floatboat.ai for main product |
| Language | `inLanguage`: `en-US` (EN pages); `zh-CN` for `/zh/` pages |
| Consistency | Schema text must match visible DOM word-for-word (FAQ especially) |
| Validation | Google Rich Results Test — zero errors on T0/T1 |
| Single graph | Prefer `@graph` array; no conflicting duplicate types |

---

## Appendix A — Organization (Homepage + About)

**Required on**: `/`, `/about`

```json
{
  "@type": "Organization",
  "@id": "https://floatboat.ai/#organization",
  "name": "Floatboat",
  "legalName": "AOE Tech Labs Limited",
  "url": "https://floatboat.ai",
  "logo": {
    "@type": "ImageObject",
    "url": "https://floatboat.ai/..."
  },
  "foundingDate": "2025-11",
  "founder": {
    "@type": "Person",
    "name": "Tan Shaoqing"
  },
  "sameAs": [
    "https://www.youtube.com/watch?v=SWMIbUBfhJY",
    "https://www.reddit.com/r/alphaandbetausers/comments/1snnwl1/i_built_a_desktop_workspace_where_the_ai_learns"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "email": "...",
    "availableLanguage": ["English", "Chinese"]
  }
}
```

| Field | Priority | Audit |
|-------|:--------:|-------|
| name, url, logo | P0 | Must exist |
| legalName | P0 | Must match footer © AOE Tech Labs Limited |
| sameAs | P1 | ≥2 authoritative profiles (YouTube, Reddit, PH, LinkedIn, GitHub) |
| contactPoint | P2 | Email from footer or support page |
| founder | P1 | Person node with name |

---

## Appendix B — WebSite (Homepage)

```json
{
  "@type": "WebSite",
  "@id": "https://floatboat.ai/#website",
  "url": "https://floatboat.ai",
  "name": "Floatboat",
  "alternateName": ["Floatboat AI", "Floatboat.ai"],
  "publisher": { "@id": "https://floatboat.ai/#organization" },
  "inLanguage": "en-US"
}
```

Optional: `SearchAction` for sitelinks search box if site search exists.

---

## Appendix C — SoftwareApplication (Home, Pricing, Download)

**Live note (2026-08-20)**: `/` has SoftwareApplication + FAQPage ✅. `/pricing` currently lacks SoftwareApplication and FAQPage in JSON-LD — flag as P0 if still true at audit.

Use **SoftwareApplication** (not generic Product) for desktop agent OS positioning.

```json
{
  "@type": "SoftwareApplication",
  "@id": "https://floatboat.ai/#software",
  "name": "Floatboat",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "macOS, Windows",
  "description": "Calendar-driven proactive agent OS for solopreneurs. Agents prep before meetings, execute on deadlines, and follow up after — automatically.",
  "url": "https://floatboat.ai",
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "USD",
    "lowPrice": "...",
    "highPrice": "...",
    "offerCount": "..."
  }
}
```

| Audit check | Pass |
|-------------|------|
| `operatingSystem` | Contains macOS and Windows |
| `description` | Matches hero copy — Calendar-Driven, not "chat box" |
| `offers` | Numbers match visible `/pricing` page |
| `aggregateRating` | Only if real reviews exist — never fabricate |

---

## Appendix D — FAQPage

**Required on**: `/`, `/pricing`, each `/alternatives/*` page, product landings with FAQ block.

```json
{
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Floatboat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "..."
      }
    }
  ]
}
```

| Rule | Standard |
|------|----------|
| Question count | Homepage ≥6; Pricing ≥5; Alternatives ≥3 |
| Answer length | 40–80 words ideal for AI extraction |
| DOM match | `name` and `text` identical to visible FAQ accordion |
| First sentence | Direct answer — no "Great question..." preambles |
| Pricing FAQ | Credit counts and prices match live pricing as-of audit date |

---

## Appendix E — BlogPosting (Blog articles)

**Live note (2026-08-20)**: Pillar post `/blog/calendar-driven-ai-vs-chat-ai` had Organization/WebSite only — **BlogPosting missing**. Flag any T2 cluster post without BlogPosting as P0.

```json
{
  "@type": "BlogPosting",
  "@id": "https://floatboat.ai/blog/{slug}#article",
  "headline": "...",
  "description": "...",
  "datePublished": "2026-03-15T08:00:00+00:00",
  "dateModified": "2026-03-20T10:00:00+00:00",
  "author": {
    "@type": "Person",
    "name": "...",
    "url": "..."
  },
  "publisher": { "@id": "https://floatboat.ai/#organization" },
  "image": "https://floatboat.ai/blog/images/...",
  "mainEntityOfPage": "https://floatboat.ai/blog/{slug}",
  "inLanguage": "en-US"
}
```

| Field | Rule |
|-------|------|
| headline | ≤110 characters |
| datePublished | ISO 8601 with timezone |
| dateModified | Only if substantive update occurred |
| author | Person preferred over Organization for E-E-A-T |
| image | ≥1200px wide recommended |

---

## Appendix F — BreadcrumbList

**Required on**: all T1 pages, blog posts, combo store detail (if breadcrumbs visible).

```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://floatboat.ai/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://floatboat.ai/blog" },
    { "@type": "ListItem", "position": 3, "name": "Article Title" }
  ]
}
```

Positions must match visible breadcrumb order.

---

## Appendix G — ItemList (Hub pages)

**Optional on**: `/alternatives`, `/combostore`, `/blog`

Use when page lists linked items (competitor cards, skill cards, recent posts).

---

## Appendix H — FloatIM ( `/floatim` only)

Separate product narrative — may use additional `SoftwareApplication` or `WebApplication` node:

- `name`: FloatIM
- `url`: reference `https://im.floatboat.ai` in description or `sameAs`
- Do not merge FloatIM and Floatboat into one SoftwareApplication without clear `isPartOf` / branding

See `references/floatim-cross-domain.md`.

---

## Validation Checklist (per audit)

| # | Page | Schema types expected | Tool |
|---|------|----------------------|------|
| 1 | `/` | Organization, WebSite, SoftwareApplication, FAQPage | schema_extract.py |
| 2 | `/pricing` | SoftwareApplication, FAQPage, BreadcrumbList | schema_extract.py |
| 3 | `/alternatives/chatgpt-alternative` | FAQPage, BreadcrumbList | schema_extract.py |
| 4 | `/blog/calendar-driven-ai-vs-chat-ai` | BlogPosting, FAQPage?, BreadcrumbList | schema_extract.py |
| 5 | `/combostore` (hub) | ItemList? WebPage | schema_extract.py |

Record Rich Results Test URL in audit appendix.

---

## Common Failures

| Failure | Fix priority |
|---------|:------------:|
| FAQ schema text ≠ DOM | P0 |
| Missing legalName on Organization | P1 |
| Pricing offers stale vs page | P0 |
| dateModified updated without content change | P1 (GEO trust signal) |
| BlogPosting without author Person | P1 |
| Multiple conflicting SoftwareApplication nodes | P1 |
