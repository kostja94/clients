# MeDo SelfCheck — H0–H4 + 12 维（自包含）

> Phase 5 使用。**本文件随 skill 分发**，不依赖 skill 文件夹外任何路径。
> 加载时机：先跑 `tools/` → Hard Gates → 12 维 → Gate C。
> 终审 → `references/portable/final-audit.md`（publish-ready ≥70 且 P0 Pass）。SelfCheck Pass = **audit-ready**，≠ publish-ready。

---

## 执行顺序

```
tools/ 三脚本 → H0 → H1 → H2 → H3 → H4 → 12 维 → Gate C
```

---

## Hard Gates H0–H4（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填（或 Degraded 已标注且无未验证 P0 claim） |
| **H1** | P0 Gate G1–G7 + A1–A4 | 零触发（见 `project-config.md` §2–§3） |
| **H2** | Slug Gate B | Design-Time 六问全 Pass（见 `slug-gate.md` §5） |
| **H3** | 字数硬门槛 | 叙事词数达类型词数下限（`article-types.md` §1） |
| **H4** | MeDo-Specific | 产品提及比例合规；Native vs PWA 叙事一致；secondary_category 一致；无工具页抢词（A4） |

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**（可进入终审，≠ publish-ready）。任一 Fail → 按 SKILL.md §3.G 回溯表回退修复。

---

## 12 维 Pass/Fail

| # | 维度 | Pass 标准（摘要） |
|---|------|------------------|
| 1 | **Publishability** | H0–H4 全 Pass |
| 2 | **Fact / E-E-A-T** | P0 数字有来源；政策有 as-of + 官方链 |
| 3 | **Differentiation** | ≥1 项 SERP 独有增量；正文**兑现** Synthesis |
| 4 | **Depth** | 词数达类型阈值（`article-types.md` §1）；FAQ 独立于正文 |
| 5 | **Presentation & Rhythm** | 长段落 ≥3；列表比例合规；衔接率 ≥70%；伪列表 0 |
| 6 | **Writing / Voice** | 非开发者友好；禁 hype（revolutionary/game-changing） |
| 7 | **Objectivity** | 对比文：≥1 竞品优势 + ≥1 非 MeDo 场景（A3） |
| 8 | **Structure / Links** | ≥2 blog 内链；Spoke 链回 Pillar；模块顺序正确 |
| 9 | **SEO / SERP** | title 45–65；description 120–160；关键词自然分布；BLUF 三处 Pass |
| 10 | **Conversion** | CTA ≤2；主 CTA → `/ai-mobile-app-builder` |
| 11 | **Slug Design** | Gate B 6 问 + 12 反模式零触发 |
| 12 | **MeDo-Specific** | Native vs PWA 叙事一致；secondary_category 一致；无工具页抢词（A4） |

**判定写作 vs 结构**：Fail 项落在维度 4–6、10 → 优先 Phase 4；维度 8–9、11 → 优先 Phase 2–3；维度 2 → Phase 4 + 事实核查。详见 SKILL.md §3.G。

---

## Perfect-Ready 附加清单（flagship 专用）

- [ ] Moat Asset 已在正文兑现（对照 Brief `MoatAssetPlanned`）
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 类型已标注
- [ ] Post-publish Metric Spec 已写入 Brief
- [ ] Extractability checklist Pass（见 `portable/extractability-checklist.md`）

---

## 工具预检（Phase 5 先跑，从 medo/ 项目根目录运行）

```bash
python skills/medo-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary kw}"
python skills/medo-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {pillartutorial|glossaryguide|comparison|publishguide|alternative|decisionguide|usecase|diagnosis|announcement}
python skills/medo-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/vs,/templates
```

任一 FAIL → 修复后重跑，再进人工自检。

---

## SelfCheck 输出格式

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| H0 Research / Gate 0R | Pass | |
| H1 P0 G1–G7 + A1–A4 | Pass | |
| H2 Slug Gate B | Pass | |
| H3 字数 | Pass | |
| H4 MeDo-Specific | Pass | |

### 12 维
| # | Dimension | Pass/Fail | Notes |
|---|-----------|-----------|-------|
| 1 | Publishability | Pass | |
| … | … | … | |

### Moat / Excellence
- Moat delivered: Yes / No
- Excellence: Yes — {类型} / No

**Overall**: PASS → audit-ready | FAIL → {fixes + §3.G 回退目标}
```

---

## 高频 Fail 速查

| # | 触发条件 | 修复 |
|---|---------|------|
| 1 | slug 含年份 / 内部架构词 | 重选 slug（`slug-gate.md` §2 反模式） |
| 2 | P0 数字无来源（17k+ apps、竞品定价） | 加 URL / as-of / 标 Unverified（`citations.md`） |
| 3 | 政策 claim 无 as-of | 加 `as of {month} {year}` + 官方链（A2） |
| 4 | Comparison 无「何时不选 MeDo」 | 补 A3 段（`product-competitors.md` §2） |
| 5 | FAQ <6 题 / 通用模板题 | 补足 6 题、全部内容相关（`presentation.md` §7） |
| 6 | 连续 3+ 短段 / 伪列表 | 合并段落重写（`presentation.md` §3C/§5） |
| 7 | 未跑 tools/ 即标 Pass | 先跑三脚本 |

---

*medo selfcheck · v2.1 · 2026-09-09 · 自 SKILL.md §3.5 外移（12 维 + Perfect-Ready + 输出格式）*
