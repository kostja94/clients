# Datus SelfCheck — H0–H4 + 类型 Gate + 12 维

> Phase 5 使用。**自包含**，不依赖 skill 外路径。
> 终审 → `references/portable/final-audit.md`（publish-ready：P0 Pass + 加权 ≥70）。

---

## 执行顺序

```
tools/ 三脚本 → H0 Gate 0R → H1 G1–G7 → 类型 Gate → H2 Slug → H3 字数 → 12 维 → Gate C
```

---

## Hard Gates

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research / Gate 0R | Research Log + Synthesis + SERP Fit（Degraded 已标注） |
| **H1** | G1–G7 | 零触发（`project-config.md` §2） |
| **H2** | Slug Gate B | `slug-gate.md` 六问全 Pass |
| **H3** | 字数 | ≥ `article-types.md` 该类型硬阻断下限 |
| **H4** | 类型 Gate | 见下表 |

### H4 — 按 ArticleType

| ArticleType | Gate |
|-------------|------|
| GlossaryTerm / GlossaryComparison | D1–D4 |
| ToolsList | T1–T4 |
| Product / Tutorial | P1–P3 |
| Research / Comparison / Pillar | R1–R2 |

---

## H3 — 字数硬阻断下限

| ArticleType | 目标 | 硬阻断 `<` |
|-------------|------|-----------|
| GlossaryTerm | 2200–3200 | 2000 |
| GlossaryComparison | 2400–3400 | 2200 |
| ToolsList | 2800–4000 | 2600 |
| Comparison | 2200–3200 | 2000 |
| Research | 2800–4500 | 2600 |
| Product | 1800–2800 | 1600 |
| Tutorial | 2500–3500 | 2300 |
| Pillar | 3200–4800 | 3000 |

`word_count_narrative.py --intent` 映射：Glossary→`glossary`；ToolsList→`toolslist`；Comparison→`comparison`；Research/Pillar→`research`；Product/Tutorial→`howto`。

---

## 12 维 Rubric（各 1–10，加权 100）

| # | 维度 | 权重 | 要点 |
|---|------|:---:|------|
| 1 | EEAT & Fact | 20% | Source Map；POC≠GA |
| 2 | Information Gain | 15% | ≥2 SERP 增量 |
| 3 | Presentation & Rhythm | 14% | `presentation-rhythm.md` |
| 4 | ArticleType Structure | 12% | 符合 `article-types.md` 模板 |
| 5 | Writing & Voice | 10% | `presentation.md` |
| 6 | SERP Fit | 8% | PAA / snippet |
| 7 | Objectivity | 8% | Datus 占比合规 |
| 8 | Internal Links | 7% | blog ≥2；G6=0 |
| 9 | Depth & Density | 6% | 例子 / case |
| 10 | Slug / Meta | 5% | title/desc/slug |
| 11 | FAQ Quality | Gate | 4–6 题独立 |
| 12 | Cluster / Path | Gate | NN + folder 与 content-graph 一致 |

**Gate C**：Hard Gates 全 Pass + 加权 ≥70 + 无维度 <3。

---

## tools/ 预检

```bash
python datus/skills/datus-blog-article/tools/frontmatter_validator.py {draft} --keyword "{kw}"
python datus/skills/datus-blog-article/tools/word_count_narrative.py {draft} --intent {type} --min {threshold}
python datus/skills/datus-blog-article/tools/link_checker.py {draft} --forbidden /agent,/features/,/use-cases/,/vs/,/alternatives/,/case-studies/
```

---

*selfcheck · v2.0.0 · 2026-08-28*
