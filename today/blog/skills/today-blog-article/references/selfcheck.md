# 通用 12 维 SelfCheck（Pass/Fail）

> Phase 5 使用。项目 skill 可追加专属维度（如 MeDo A1–A4、FinalRound F1–F6），但不得删减 G1–G7 与下列 12 维。

## Hard Gates H0–H4（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填（Degraded 已标注且无未验证 P0 claim） |
| **H1** | P0 Gate G1–G7 + 项目专属 Gate | 零触发（见 project-config） |
| **H2** | Slug Gate B | Design-Time 六问全 Pass（见项目 slug-gate） |
| **H3** | 字数硬门槛 | 叙事词数 ≥ 项目 article-types 该类型下限 |
| **H4** | Today-Specific (T1–T4) | T1 Healthcare 合规 · T2 Beta 状态 · T3 产品线叙事 · T4 健康 claim；产品占比合规；禁抢词 |

## 12 维 Pass/Fail

| # | 维度 | Pass 标准（摘要） |
|---|------|------------------|
| 1 | **Publishability** | H0–H4 全 Pass |
| 2 | **Fact / E-E-A-T** | P0 数字有来源；政策/定价有 as-of + 官方链 |
| 3 | **Differentiation** | ≥1 项 SERP 独有增量；正文兑现 Synthesis |
| 4 | **Depth** | 词数达类型阈值；FAQ 独立于正文（非复制粘贴） |
| 5 | **Presentation & Rhythm** | 长段落 ≥3（4–8 句）；列表比例合规；衔接率 ≥70%；伪列表 0 |
| 6 | **Writing / Voice** | 符合项目 Voice；禁 hype 套话（revolutionary/game-changing/seamless） |
| 7 | **Objectivity** | 对比文：≥1 竞品优势 + ≥1 非自有产品更合适场景 |
| 8 | **Structure / Links** | ≥2 blog 内链；Spoke 链回 Hub；模块顺序正确 |
| 9 | **SEO / SERP** | title 45–65；description 120–160；BLUF 三处 Pass |
| 10 | **Conversion** | CTA ≤2；主 CTA 指向项目声明的转化路径 |
| 11 | **Slug Design** | Gate B 6 问 + 反模式零触发 |
| 12 | **Today-Specific** | T1–T4 零触发；Memory/Proactive/Execution 叙事一致；secondary_category 与 cluster 一致；HealthcareGuide 含 lifestyle 免责 |

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**（≠ publish-ready）。任一 Fail → 按 SKILL.md §3.G 回溯修复。

## Perfect-Ready 附加（flagship Mode）

- [ ] Moat Asset 已在正文兑现
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 类型已标注
- [ ] Post-publish Metric Spec 已写入 Brief

## 工具预检（Phase 5 前）

```bash
python tools/frontmatter_validator.py {draft-path} --keyword "{primary kw}"
python tools/word_count_narrative.py {draft-path} --intent {type} --min {threshold}
python tools/link_checker.py {draft-path} --forbidden /pricing,/compare,article.today.ai
```

**Today forbidden 前缀**：`/pricing`, `/compare`, `article.today.ai`

阈值以 `article-types.md` / `project-config.md` 为准。从 `today/` 项目根运行：

```bash
python blog/skills/today-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary kw}"
python blog/skills/today-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {type}
python blog/skills/today-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/compare,article.today.ai
```

*selfcheck · v1.0 · 2026-08-23 · generic 12-dim*
