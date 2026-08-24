# UTM & Nofollow Rules

Business rules for outbound link handling in `src/lib/utils.ts` (`addUtmToExternalLink` and `getExternalLinkRel`).

## UTM Injection (`addUtmToExternalLink`)

### Default behavior
All external (non-alignify.co) outbound links automatically get `?utm_source=kostja&utm_medium=blog` appended.

### Exceptions — UTM NOT added

| Condition | Rule | Example |
|---|---|---|
| URL already has query params | Skip generic UTM (don't interfere with existing tracking) | `?vsource=cutout_share-1370384` |
| Partner invite links | Return URL as-is (no Alignify UTM) | `lovable.dev/invite/*`, `manus.im/invitation/*` |

### Internal links
Links to `alignify.co`, `www.alignify.co`, or `*.alignify.co` subdomains never get UTM params.

---

## Nofollow Rules (`getExternalLinkRel`)

### Default behavior
All external links get `rel="noopener noreferrer nofollow"`.

### Exceptions — dofollow (no `nofollow`)

| Domain | Reason |
|---|---|
| `voispark.com` / `*.voispark.com` | VoiSpark (partner) |
| `novascientia.com.br` / `*.novascientia.com.br` | Nova Scientia (Kostja's localization test site) |
| `google.com` / `google.cn` / `g.cn` / `blog.google.com` / `developers.google.com` / `search.google.com` / `support.google.com` / `*.google.com` / `*.blog.google.com` / `*.developers.google.com` / `*.search.google.com` / `*.support.google.com` | Google (search engine, dofollow) |

### Invalid URLs
If the URL cannot be parsed, default to `nofollow` for safety.

---

## Related code
- `src/lib/utils.ts` — function definitions
- `src/components/BestTools.tsx` — tool card external links
- `src/components/CustomerCaseCard.tsx` — customer case website links
- `src/components/Footer.tsx` — social icons + Nova Scientia link
- `src/components/GlossaryViewer.tsx` — glossary reference links
- `src/components/PartnershipPageContent.tsx` — IRIS project link
- `src/components/References.tsx` — citation links
- `src/components/YouTubeThumbnail.tsx` — video link
- `src/components/YouTubeThumbnailImage.tsx` — thumbnail link
- `src/marketing/GrowthCaseStudiesIndex.tsx` — growth case study cards
