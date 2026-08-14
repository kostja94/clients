# Clink — SelfCheck（12 维 + Hard Gates H0–H4 + C1–C4）

> 加载时机：**Phase 5**（Gate C）
> 主文件：SKILL.md §3 Phase 5 指针

---

## 执行顺序

1. 跑 `tools/` 脚本
2. Hard Gates H0–H4 + C1–C4
3. 12 维 Pass/Fail

全部 Pass → **audit-ready**。

---

## Hard Gates

### H0 — Research 三角 / Gate 0R

- [ ] Research Log 完整（R1–R3 + Synthesis）
- [ ] SERP Fit 已填
- [ ] R3 官方页 ≥1 + SERP Top3（或 Degraded 已标注）

### H1 — G1–G7

| ID | Pass 标准 |
|----|----------|
| G1 | 产品/竞品与官方一致 |
| G2 | 无 placeholder / forbidden 死链 |
| G3 | 量化 claim 有 attribution |
| G4 | 竞品角色（PSP/MoR/billing/orch）正确 |
| G5 | 无无证据 superlative |
| G6 | 无 `/vs/*` `/pricing` `/for/*` `/learn/*` `/customers/*` |
| G7 | 竞品无贬低；≥1 优势 |

### H2 — Slug Gate B

- [ ] 六问全 Pass（`slug-gate.md`）

### H3 — 字数硬门槛

叙事词数排除 FAQ 问答块与表格（与 `tools/word_count_narrative.py` 一致）。创作目标仍见 `article-types.md`；下表为硬阻断下限（已按 01–04 基线校准）：

| 类型 | 硬阻断下限 | 创作目标（含 FAQ） | `--intent` |
|------|-----------|-------------------|------------|
| BrandIntroduction | **2500** | 2500–3500 | `brand` |
| Comparison | **1600** | 2500–3500 | `comparison` |
| Product | **1800** | 2200–3200 | `product` |
| Opinion | **1800** | 2000–2800 | `opinion` |
| EvaluationComparison | **2500** | 2500–3500 | `evaluation` |
| GlossaryTerm | **1800** | 2200–3200 | `glossary` |

### H4 — Clink-Specific（含 C1–C4）

| ID | Pass 标准 |
|----|----------|
| C1 | 无具体 Clink 费率数字（Contact Sales） |
| C2 | MoR/tax 有限定语或 as-of |
| C3 | 证言 as-of；无夸大 GMV |
| C4 | Agentic Payments → Early Access（若提及） |
| — | 产品占比 ≤ 类型上限 |
| — | 品牌名统一 **Clink**；域名 clinkbill.com |
| — | frontmatter **无** keywords / related / disclosure |
| — | **倒数第二节 `## Conclusion`，最后一节 `## FAQ`** |

---

## 12 维 Pass/Fail

| # | 维度 | Pass 条件摘要 |
|---|------|-------------|
| 1 | Publishability | H0–H4 + C1–C4 全 Pass |
| 2 | Fact / E-E-A-T | Source Map ≥3；竞品 ≥1 优势；≥1 非 Clink 更合适场景 |
| 3 | Differentiation | Synthesis 兑现；句级重复 <30%；未重写 canon |
| 4 | Depth / Density | 词数达标；FAQ ≥3 独立；每 ~500 词 ≥1 例子 |
| 5 | Presentation / Rhythm | 长段 ≥3；伪列表 0；衔接率 ≥70%；H2 不编号 |
| 6 | Writing / Voice | 禁词 0；空泛句 ≤2；Professional + Evidence-led |
| 7 | Objectivity | 产品占比合规；无贬低 |
| 8 | Structure / Links | TL;DR；Conclusion→FAQ；blog 正文互链 ≥2 |
| 9 | SEO / SERP | title 含 keyword；SERP Fit；BLUF 三处 |
| 10 | Conversion | CTA ≤2（Conclusion 或更早）；Contact Sales / docs |
| 11 | Slug Design | Gate B + 反模式 0 |
| 12 | Cross-Article | 同 cluster 无矛盾（单篇 N/A） |

---

## SelfCheck 输出格式

```markdown
## SelfCheck — {slug}
### Tools
| Script | Result |
### Hard Gates
| Gate | Pass/Fail | Notes |
### Weighted / 12-Dim
| # | Dimension | Pass/Fail | Notes |
### Source Map
| Claim | § | Source | Confidence |
**Status**: audit-ready | needs-fix
```

---

## Perfect-Ready（flagship）

- [ ] Moat Asset 正文兑现
- [ ] Answer Blocks 3–5 可独立成 40–60 词段
- [ ] Excellence 已标注
- [ ] Post-publish Metric Spec 已写入 Brief

---

*selfcheck · v1.0.0 · 2026-07-21*
