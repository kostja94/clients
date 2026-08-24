# Site-Level Content Extractability Audit

> BLUF and chunk rules for T2 blog samples and T0/T1 FAQ blocks during site audit.
> **Last updated**: 2026-08-20

---

## Purpose

Generative engines extract **passages**, not whole pages. Site audit samples must pass the same extractability bar expected of new blog content.

Apply this reference to:
- T2 blog cluster URLs (full list in page-tier-matrix.md)
- T0 FAQ sections (/, /pricing)
- T1 alternatives FAQ blocks

---

## BLUF Three Locations

| ID | Location | Pass standard |
|----|----------|---------------|
| B1 | TL;DR or intro summary | 40–60 words directly answering primary page intent |
| B2 | Each major H2 first paragraph | Answer first — no "In today's fast-paced world..." delay |
| B3 | Each FAQ answer | First sentence is the complete short answer; <30% overlap with body copy |

---

## Claim Atomicity

| Check | Pass |
|-------|------|
| Paragraph lead | First 1–2 sentences state the paragraph's single claim |
| Chunk independence | Random 3 paragraphs each answer one sub-question alone |
| Pronoun resolution | "It/this" resolvable within same paragraph |
| One claim per paragraph | No 3+ unrelated conclusions in one block |

---

## FAQ Extractability (T0/T1)

| Page | Min questions | Pass |
|------|:-------------:|------|
| `/` | 6 | Each answer 40–80 words; first sentence = direct answer |
| `/pricing` | 5 | Credit counts and prices with "as of {Month} {Year}" |
| `/alternatives/*` | 3 | Includes at least one question acknowledging competitor strength |

**Schema alignment**: FAQ JSON-LD text must match visible FAQ verbatim.

---

## Time Context (GEO freshness signal)

| Content type | Requirement |
|--------------|-------------|
| Pricing claims | "As of August 2026" or equivalent |
| Model list | Name current models; remove deprecated |
| Competitor comparisons | Date the comparison; note product changes |
| Statistics | Attribute source or "per Floatboat internal data" |

---

## Judgment & Objectivity (Alternatives pages)

| Pass | Fail |
|------|------|
| "For solopreneurs who live in calendar rhythm, Floatboat…" | "Floatboat is the best" without qualification |
| Acknowledges competitor strength in specific dimension | One-sided trashing |
| Comparison table with ≥3 dimensions | Marketing fluff only |

---

## Blog T2 Sample Scoring

For each T2 URL, score extractability:

| Dimension | Weight | Score 0–2 |
|-----------|:------:|:---------:|
| B1 TL;DR present | 20% | 0=missing, 1=weak, 2=pass |
| B2 H2 leads | 30% | avg of H2 samples |
| B3 FAQ if present | 20% | |
| Time context on claims | 15% | |
| Chunk independence | 15% | |

**Pass threshold**: weighted score ≥ 1.5 / 2.0

---

## Quick Manual Test

1. Open page → copy first paragraph under main H2
2. Ask: "Does this alone answer the H2 question?"
3. If no → flag `EXTRACT-B2-FAIL` in audit report

---

## Relationship to Blog Creation

When blog posts fail site audit extractability, note slug for content team refresh — do not rewrite in audit skill unless user requests fix pass.
