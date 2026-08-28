# Datus Glossary — Mini Example（黄金样例）

> Phase 1 / Phase 3 参照。基于已发布 `#15 what-is-text-to-sql`。

---

## Article Brief（样例）

```markdown
## Article Brief

**Working title**: What Is Text-to-SQL? Definition, How It Works & Why Context Matters
**Primary keyword**: text-to-SQL
**Article type**: GlossaryTerm
**Datus category**: Glossary
**Search intent**: Informational (definition)
**Reader stage**: Awareness → Understanding production requirements
**Publish goal**: SEO — capture definition + NL2SQL cluster
**Target audience**: Data engineers evaluating text-to-SQL vs copilot vs agent
**Word count target**: 2400–2800
**Glossary category**: F — AI & Agents
**Cluster role**: Spoke (AI stack)
**Hub link**: /blog/what-is-data-engineering-agent
**Differentiation angle**: Four-stage pipeline failure taxonomy + grain-error case walkthrough
**Information increment** (vs SERP top 3):
  1. Stage-by-stage failure table (intent / linking / synthesis / validation)
  2. Full MAU grain case walkthrough (wrong COUNT vs DISTINCT)
  3. Explicit "when text-to-SQL is enough vs when you need an agent" decision frame
**Planned internal links**:
  - /blog/what-is-schema-linking (§1 pipeline)
  - /blog/what-is-semantic-layer (§3 context)
  - /blog/what-is-data-engineering-agent (§2 vs copilot)
**KEEP/MERGE**: KEEP
**Canonical references** (link only, no redefine): schema linking, semantic layer, RAG
```

---

## Outline（样例）

```markdown
## Outline — what-is-text-to-SQL

| § | H2 | Target words | Links / Notes |
|---|-----|-------------|---------------|
| Excerpt | 1–2 sentence summary | 30–50 | explain what the article covers |
| TL;DR | 5 bullets | 120 | bullet 1 = definition |
| 1 | Text-to-SQL: a working definition | 450 | blockquote definition; 4-stage table; link schema-linking |
| 2 | Text-to-SQL vs NL2SQL vs SQL copilot | 350 | comparison table; link data-engineering-agent, vs-sql-copilot |
| 3 | What context text-to-SQL systems need | 400 | semantic layer, reference SQL, feedback |
| 4 | Accuracy limits and failure modes | 350 | — |
| 5 | How agents improve on copilots | 300 | Datus ≤2 段 |
| 6 | Architecture patterns in production | 300 | — |
| 7 | Case walkthrough: MAU grain error | 450 | snippet-ready depth |
| 8 | When text-to-SQL is enough — and when not | 300 | decision list |
| — | Conclusion | 120 | — |
| FAQ | 5 questions | 450 | production-ready test; ChatGPT vs text-to-SQL |

**Estimated total**: ~2600 words
```

---

## Frontmatter（样例）

```yaml
---
title: "What Is Text-to-SQL? Definition, How It Works & Why Context Matters"
description: "Text-to-SQL definition, NL2SQL pipeline stages, accuracy limits, and how data engineering agents improve with persistent context."
slug: "what-is-text-to-sql"
date: 2026-06-05
author: "Kostja"
category: "Glossary"
---
```

---

## GlossaryComparison Brief 片段（semantic-layer-vs-ontology）

```markdown
**Article type**: GlossaryComparison

---

## Phase 5 SelfCheck（v2.0.0 格式，预期）

```markdown
## SelfCheck — what-is-text-to-sql

### Hard Gates
| Gate | Pass/Fail |
|------|-----------|
| G1–G7 | ✅ Pass |
| D1–D4 | ✅ Pass |
| Slug | ✅ Pass |

### Weighted Scoring (10 dimensions)
| # | Dimension | Weight | Score | Weighted |
|---|-----------|:---:|:---:|:---:|
| 1 | EEAT & Fact | 22% | 8 | 1.76 |
| 2 | Information Gain | 16% | 9 | 1.44 |
| 3 | Presentation & Rhythm | 14% | 8 | 1.12 |
| 4 | Writing & Voice | 11% | 8 | 0.88 |
| 5 | SERP Fit | 8% | 7 | 0.56 |
| 6 | Structure & Scannability | 8% | 9 | 0.72 |
| 7 | Objectivity | 7% | 9 | 0.63 |
| 8 | Internal Links | 5% | 9 | 0.45 |
| 9 | Depth & Density | 5% | 8 | 0.40 |
| 10 | Slug / H1 | 4% | 9 | 0.36 |
| **Total** | | **100%** | | **8.32 / 10 Grade A** |
```

**Primary keyword**: semantic layer vs ontology
**Information increment**:
  1. Opening agent failure story (correct metric, wrong relationships)
  2. 6-dimension comparison table
  3. Agent task matrix (what semantic layer vs ontology each provides)
**Planned internal links**: what-is-semantic-layer (recap only), what-is-semantic-model, what-is-data-engineering-agent
**Cannibalization**: Term A recap ≤150 words + link to canonical semantic layer article
```

---

## SelfCheck 片段（Pass 示例）

| ID | Result | Notes |
|----|--------|-------|
| G1 | Pass | Pipeline stages align with industry usage |
| D1 | Pass | Links to canonical schema-linking; no full redefine |
| D2 | Pass | 3 blog links; 0 glossary; 4 external |
| D3 | Pass | Datus ~12%; disclosure ×2 |
| Health score | 5/5 | Ready for delivery |
