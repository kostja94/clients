# Custom H2 Section Inventory & Standardization Analysis

Analysis date: 2026-05-18. Source: all 105 `content/tools/en/*.md` files.

> **Note**: The block types proposed in this document (`risksBlock`, `toolTypes`, `llmBenchmarks`, `practicalTips`, `executionModels`, `technicalParadigms`) are aspirational — none are defined in `article-doc.ts`, dispatched in `ArticleFromJson.tsx`, or have corresponding React components. They represent standardization candidates for future implementation.

---

## Overview

> **历史说明（2026-08 前）**：旧 JSON 体系曾用 8 种 block type（`howItWorks`、`bestTools`、`howToChoose` 等）。**现均为 Markdown `section` / 集中 JSON。**

### The 3 shared sections

| Section ID | Pages | Notes |
|------------|-------|-------|
| `conclusion` | 103/105 | Universal; missing only on agent-for-desktop and openclaw-alternatives (which have custom variants) |
| `risk-compliance` | 2 | api, character-chat |
| `other-products` | 2 | character-chat, chatbot |

Everything else (171 IDs) appears on exactly one page.

---

## Part 1: Candidate Block Types (High Confidence)

These patterns are followed by multiple existing pages and could be formalized as shared block types with minimal content restructuring.

### 1.1 `risksBlock` — Risk / Compliance / Governance

**Current usage:** 9 pages have risk sections, 5 of which follow the identical structure.

**Structure:**

```
introHtml (string, optional)
items: [
  { title: string, descriptionHtml: string }
]
```

**Pages that already fit this template:**

| Slug | Section ID | Items |
|------|-----------|-------|
| cli | `risks-and-security` | 4 risks (via inline subSections) |
| knowledge-base | `risks-security-governance` | 7 risks (via inline bold labels) |
| voice-changer | `risks-compliance-and-ethical-use` | 4 risks (via inline bold labels) |
| workflow | `risks-and-considerations` | 5 risks (via inline bold labels) |
| api | `risk-compliance` | 4 risks (via inline bold labels) |

**Pages with risk sections that should remain custom:**

| Slug | Reason |
|------|--------|
| code-completion | Data journalism format — cites specific CVEs, vendor names, and research studies unique to AI code security |
| linkedin | Platform-specific — tethered to LinkedIn ToS, platform behavior rules, and hiring discrimination law |
| user-research | Domain methodology — cites ACM CHI studies, MeasuringU research, user-research-specific ethics |
| character-chat | Legal/minor-safety — uniquely focused on child safety regulations and age-gating; structurally brief |

**Recommendation:** Create `risksBlock` as a standard block type. The 5 templatable pages use different markup (some via `subSections`, others via inline `<strong>` tags in paragraphs) but all follow the same conceptual structure. Migration would require consistent formatting.

---

### 1.2 `toolTypes` — Category / Type Taxonomy

**Current usage:** 8 pages have categorization sections, 5 of which follow the identical "N types" pattern.

**Structure:**

```
introHtml (string, optional)
types: [
  {
    name: string,
    descriptionHtml: string,
    useCaseHtml: string (optional),
    exampleTools: string[] (optional)
  }
]
```

**Pages that already fit this template:**

| Slug | Section ID | Types |
|------|-----------|-------|
| 3d-modelling | `3d-modelling-types` | 4 modeling types (via subSections) |
| canvas-video | `canvas-video-types` | 7 types (via separate paragraphs) |
| video-effects | `video-effects-types-5-categories` | 5 categories (via subSections) |
| voice-changer | `types-of-ai-voice-changers` | 3 form factors (via inline bold) |

**Pages with type sections that should remain custom:**

| Slug | Reason |
|------|--------|
| ai-homework-helper | Binary comparison narrative (Answer-First vs. Socratic), not enumeration |
| avatar | Disambiguation (word meaning), not tool categorization |
| image-generator | 39-word stub — not substantive enough to justify a template |
| spreadsheet | Binary comparison narrative (AI-native vs. Excel-enhanced), not enumeration |

**Recommendation:** Create `toolTypes` block type. Two implementation variants exist: pages using formal `subSections` (3d-modelling, video-effects) and pages using standalone paragraphs with bold inline labels (canvas-video, voice-changer). Standardize on the `subSections` approach for consistency.

---

### 1.3 `llmBenchmarks` — LLM Benchmark Explanations

**Current usage:** All 5 LLM-series pages (llm, llm-for-coding, llm-for-math, llm-for-reasoning, multimodal-llm) follow the identical pattern.

**Structure:**

```
categoryName: string,
benchmarks: [
  { name: string, descriptionHtml: string }
],
warningPhrase: string,
crossReferences: ("evaluation" | "search-engine" | "geo")[]
```

**All 5 pages:**

| Slug | Section ID | Benchmarks covered | Words |
|------|-----------|-------------------|-------|
| llm | `llm-benchmarks-landscape` | MMLU-Pro, HumanEval, Arena Elo, SWE-bench | 277 |
| llm-for-coding | `coding-benchmarks-harness` | SWE-bench, LiveCodeBench | 200 |
| llm-for-math | `math-benchmarks-saturation` | MATH, GSM8K, AIME, FrontierMath | 123 |
| llm-for-reasoning | `reasoning-benchmarks-protocols` | GPQA, Humanity's Last Exam, ARC-AGI-2 | 121 |
| multimodal-llm | `multimodal-benchmarks-judges` | MMMU, MMMU-Pro, MM-Vet | 146 |

**Common structural elements across all 5:**
1. Opening: lists relevant benchmarks with category-specific caveats about interpretation
2. Closing: cross-reference to `/tools/evaluation` and/or `/tools/geo` or `/tools/search-engine`
3. Dense advisory prose — no subSections, no bullet lists

**Recommendation:** Create `llmBenchmarks` as an LLM-series-specific block type. This is the strongest standardization candidate — the 5 pages already follow the identical formula.

---

## Part 2: Candidate Block Types (Lower Confidence)

These patterns exist on 1-2 pages each but the concept is general enough to apply to other tool categories.

### 2.1 `practicalTips` — Implementation Tips

**Current usage:** Only `api.json` (`practical-tips`).

**Structure:**
```
tips: [
  { tipHtml: string }
]
```

The api page has 4 tips, each a self-contained paragraph with actionable advice. This pattern is generic — any tool category could benefit from a "tips for getting started" or "best practices" section.

**Recommendation:** Create `practicalTips` block type. Low risk — simple structure, broadly applicable. Other pages (3d-model-generator, image-generator, video-generator) could adopt this without content duplication.

---

### 2.2 `executionModels` — Binary Approach Comparison

**Current usage:** Only `cli.json` (`agentic-vs-copilot-cli`).

**Structure:**
```
approachA: { name: string, descriptionHtml: string },
approachB: { name: string, descriptionHtml: string },
guidanceHtml: string
```

The cli page contrasts "Agentic CLI" vs. "Copilot CLI" with a "how to choose" section at the end.

**Recommendation:** Consider creating if 2+ other pages adopt the pattern. The binary comparison structure applies to several tool categories (e.g., cloud vs. local, real-time vs. batch, code-first vs. no-code).

---

### 2.3 `technicalParadigms` — Technical Trade-off Analysis

**Current usage:** Only `3d-model-generator.json` (`generation-paradigms`). 811 words across 4 subSections.

**Structure:**
```
introHtml: string,
paradigms: [
  { name: string, descriptionHtml: string, tradeOffHtml: string }
]
```

The 3d-model-generator page explores 3 axes (optimization vs. feed-forward, mesh vs. neural, text vs. image input) in depth. This pattern could serve any page that explains "how the AI works under the hood" with multiple technical approaches.

**Recommendation:** Consider creating if adopted by other technically-deep pages (video-generator, music-generator, world-model). The content density makes this a niche but powerful template.

---

## Part 3: Truly Page-Specific Sections

These sections cannot be standardized — their content is irreducibly tied to a specific tool category, platform, or time-bound event.

### 3.1 Data journalism / research-heavy

| Slug | Section ID | Why page-specific |
|------|-----------|-------------------|
| code-completion | `security-reality-check` | Cites Veracode study (45% OWASP failure rate), CVE-2025-8217, specific slopsquatting rates, Amazon Q Developer |
| user-research | `risks-and-ethics` | Cites MeasuringU study, ACM CHI, domain-specific synthetic user methodology |
| accent-conversion | `ethical-considerations` | Explores "softening vs. erasure" debate citing Sanas, Unifor union, TELUS |

### 3.2 Platform / policy-specific

| Slug | Section ID | Why page-specific |
|------|-----------|-------------------|
| linkedin | `risks-compliance-content-integrity` | Tethered to LinkedIn ToS, platform automation rules, hiring discrimination law |
| character-chat | `risk-compliance` | Child safety regulations, platform age-gating — legal/safety, not technical risk |
| legal | `ethics-citations-vendor-due-diligence` | References ABA Formal Opinion 512, hallucinated case citations — legal-profession specific |
| character-chat | `boundary-byok` | Platform-specific content filter implementation details |
| character-chat | `character-cards-local` | Platform-specific local frontend architecture |

### 3.3 Time-bound news / announcements

| Slug | Section ID | Why page-specific |
|------|-----------|-------------------|
| image-generator | `industry-trends-and-evaluation` | Dated vendor announcements: ChatGPT Images 2.0 (April 2026), Microsoft MAI-Image-2 (April 2026), Qwen-Image-2.0 (February 2026), Canva AI 2.0 (April 2026) |

### 3.4 Binary comparison narratives (not enumeration)

| Slug | Section ID | Why page-specific |
|------|-----------|-------------------|
| ai-homework-helper | `two-types-of-ai-homework-helpers` | Narrative comparing two philosophies, not enumerating N types |
| spreadsheet | `types-of-ai-spreadsheet-tools` | Narrative comparing two approaches, not enumerating N types |

### 3.5 Stubs / navigation / marketing

| Slug | Section ID | Words | Why page-specific |
|------|-----------|-------|-------------------|
| image-generator | `image-generation-types` | 39 | Too brief to justify a template |
| logo-generator | `general-image-generation-tools` | 27 | Cross-reference link, not content |
| logo-generator | `logos-as-brand-assets` | 99 | Brand marketing prose linking to media kit |
| avatar | `two-meanings-of-avatar` | 89 | Disambiguation, not categorization |

### 3.6 Composite / fused sections

| Slug | Section ID | Words | Why page-specific |
|------|-----------|-------|-------------------|
| 3d-model-generator | `lab-to-production` | 985 | Fuses 3 separate H2 concepts (product taxonomy + pipeline workflow + risk management) into one section |

### 3.7 Deployment / operations

| Slug | Section ID | Why page-specific |
|------|-----------|-------------------|
| api | `platform-type-spectrum` | Categorization of API platform types — structurally similar to Group 2 `toolTypes` but content is API-infrastructure-specific |
| llm-for-reasoning | `reasoning-deploy-human` | Operational best-practices for reasoning model deployment — latency routing, human review gates |

### 3.8 Cross-reference / interlinking

| Slug | Section ID | Why page-specific |
|------|-----------|-------------------|
| 3d-modelling | `things-to-watch-out-for` | Practical advice about 3D tool limitations |
| 3d-modelling | `why-3d-modelling-matters-2026` | Category-specific value proposition |
| accent-conversion | `proven-business-impact` | Category-specific ROI data |
| character-chat | `community-consensus` | Community sentiment aggregation |
| llm | `llm-grounding-and-surface` | Grounding, API deployments, human-in-the-loop discussion |
| llm-for-coding | `coding-rag-and-ship` | Repo grounding, glue code discussion |
| llm-for-math | `math-applied-and-classroom` | Tutoring UX to FP&A bridge discussion |
| multimodal-llm | `multimodal-worldmodel-ux` | World models, OCR SLAs discussion |
| web-search-api | `china-and-open-model-stacks` | Region-specific API examples |

---

## Part 4: The 118 Pseudo-Shared Sections

Two section patterns exist on nearly every page but use page-specific IDs that prevent sharing:

### 4.1 `what-are-*` (95 pages)

Every page has a "What Are X" introduction section. All follow the same conceptual structure but the section ID is page-specific (e.g., `what-are-ai-3d-generators`, `what-are-unified-api-platforms`).

**Recommendation:** Do not attempt to share these. The content is necessarily page-specific (defining each tool category). The ID convention `what-are-{slug-description}` is consistent and works as-is.

### 4.2 `other-*` (23 pages)

"Other Notable X Tools" sections. Same concept across pages but IDs vary (e.g., `other-notable-api-platforms`, `other-image-generators`).

**Recommendation:** Consider standardizing the ID convention to `other-notable-tools` with a `category` parameter if a shared block type is created. Currently 23 pages use this pattern; the other 82 pages lack an "other tools" section entirely — standardization could encourage broader adoption.

---

## Part 5: Standardization Roadmap

### Phase 1: Create 3 new block types (high confidence, multiple existing pages)

| Block Type | Existing Pages | Effort |
|------------|---------------|--------|
| `risksBlock` | cli, knowledge-base, voice-changer, workflow, api (5) | Medium — need to normalize markup across pages |
| `toolTypes` | 3d-modelling, canvas-video, video-effects, voice-changer (4) | Medium — two implementation variants to unify |
| `llmBenchmarks` | llm, llm-for-coding, llm-for-math, llm-for-reasoning, multimodal-llm (5) | Low — all 5 already follow identical structure |

### Phase 2: Create 1-2 experimental block types (lower confidence, 1-2 pages each)

| Block Type | Existing Pages | Risk |
|------------|---------------|------|
| `practicalTips` | api (1) | Low — simple structure, broadly applicable |
| `executionModels` | cli (1) | Medium — wait for 2+ pages to adopt pattern |

### Phase 3: Monitor and decide

| Block Type | Condition to Create |
|------------|---------------------|
| `technicalParadigms` | If 1+ more technically-deep page adopts the trade-off analysis format |
| `otherNotableTools` | If standardizing the 23 existing `other-*` sections into a shared block type |

### Phase 4: Leave as-is

The 35+ truly page-specific sections in Part 3 should remain custom. Their value comes from category-specific depth, not structural consistency.

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Total section-type blocks | 281 |
| Total unique section IDs | 174 |
| Shared across 2+ pages | 3 |
| Page-specific (all groups) | 171 |
| — Pseudo-shared (`what-are-*` + `other-*`) | 118 |
| — Truly unique custom sections | 53 |
| — — Could be standardized into new block types | 13 |
| — — Irreducibly page-specific | 40 |

**Bottom line:** Of the 174 unique section IDs, 16 could be eliminated by creating 3-5 new standardized block types. The remaining 158 are either necessarily page-specific `what-are-*` intros (95), `other-*` tool lists that could converge later (23), or genuinely category-specific content that benefits from custom prose (40).
