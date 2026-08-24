# Moras SelfCheck — H0–H4 + I1–I5 + 12 维（自包含）

> Phase 5 使用。**本文件随 skill 分发**，不依赖 skill 文件夹外任何路径。
> 加载时机：先跑 `tools/` → Hard Gates → 12 维 → Gate C。
> 终审 → `references/portable/final-audit.md`（publish-ready ≥70 且 P0 Pass）。

---

## 执行顺序

```
tools/ 三脚本 → H0 Gate 0R → H1 G1–G7 → I1–I5 → H2 Slug → H3 字数 → H4 Moras → 12 维 → Gate C
```

---

## Hard Gates H0–H4 + I1–I5（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填（Degraded 已标注且无未验证 P0 claim） |
| **H1** | P0 Gate G1–G7 | 零触发（见 `project-config.md` §1.2） |
| **I1–I5** | Income Claim Gate | 零触发；Topic Scope 非 tiktok-shop-affiliate 时按 project-config 跳过规则 |
| **H2** | Slug Gate B | Design-Time 六问全 Pass（见 `slug-gate.md` §13） |
| **H3** | 字数硬门槛 | 叙事词数 ≥ 类型硬阻断下限（见下表） |
| **H4** | Moras-Specific | 见下文 H4 清单 |

### I1–I5 速查

| ID | 检查项 | Pass 标准 |
|----|--------|----------|
| **I1** | 收入承诺 | 无 guaranteed income；区间 + 条件 |
| **I2** | 证言滥用 | GMV 证言有 testimonial 标注 + "Results vary" |
| **I3** | 平台政策无时效 | TikTok Shop 政策有 "as of {date}" + 官方链 |
| **I4** | Who/How/Why 缺失 | Pillar/Framework/Research 含 Who/How/Why |
| **I5** | 复述 SERP | 无 "studies show" 泛引；非句级复制 Top3 |

### H3 — 字数硬门槛

| 类型 | 创作目标 | 硬阻断下限 | `--intent` |
|------|---------|-----------|------------|
| Pillar | 3500–5000 | **<3000 → Fail** | `pillar` |
| Setup | 2500–3500 | **<2200 → Fail** | `howto` |
| Production | 2800–3800 | **<2400 → Fail** | `product` |
| Research | 2800–3500 | **<2400 → Fail** | `research` |
| Framework | 2500–3200 | **<2200 → Fail** | `framework` |
| Strategy | 2500–3200 | **<2200 → Fail** | `howto` |
| Side Hustle | 2200–3000 | **<2000 → Fail** | `howto` |
| Diagnosis | 2500–3200 | **<2200 → Fail** | `diagnosis` |
| Platform Ops | 1800–2500 | **<1500 → Fail** | `announcement` |

### H4 — Moras-Specific

- [ ] 产品提及比例合规（`article-types.md` §2.1）
- [ ] Affiliate-first；seller 仅对比语境
- [ ] US-only（TikTok Shop 文）
- [ ] 品牌 **Moras**（非 Morris）；title 不加 `\| K2 Lab`
- [ ] Intent lane 与内链一致
- [ ] Cannibalization 对照 content-graph + TVG 白名单
- [ ] TL;DR：60–110 词长描述 + 3–6 bullets；TL;DR/FAQ 无内链
- [ ] FAQ ≥6 题 + ≥1 题正文未覆盖
- [ ] `isoDate` 不与 portfolio 重复

---

## 12 维 Pass/Fail

| # | 维度 | Pass 标准（摘要） |
|---|------|------------------|
| 1 | **Publishability** | H0–H4 + I1–I5 全 Pass |
| 2 | **Fact / E-E-A-T** | P0 数字有来源；TikTok 政策有 as-of + 官方链 |
| 3 | **Differentiation** | **≥2 项** SERP 独有增量；正文兑现 Synthesis |
| 4 | **Depth** | 词数达类型阈值；FAQ 独立于正文 |
| 5 | **Presentation & Rhythm** | 长段落 ≥3（4–8 句）；列表比例合规；衔接率 ≥70%；伪列表 0 |
| 6 | **Writing / Voice** | Moras Voice 五正向；禁词 0；≥1 具体 scenario |
| 7 | **Objectivity** | 产品≤类型上限；Who/How/Why 齐备；无贬低措辞 |
| 8 | **Structure / Links** | TL;DR+Conclusion+FAQ；blog 互链 ≥2；forthcoming ≤1 |
| 9 | **SEO / SERP** | title 45–60；description 140–160；BLUF 三处 Pass |
| 10 | **Conversion** | CTA ≤2；匹配读者阶段 |
| 11 | **Slug Design** | `/blog/{slug}` 格式；Gate B 6 问 + 反模式零触发 |
| 12 | **Moras Project-Specific** | Cannibalization 表已填；I Gates Pass；TVG 边界清晰 |

**Gate C**：全部 Pass → **audit-ready**（≠ publish-ready）。任一 Fail → 按 SKILL.md §3.G 回溯。

---

## Perfect-Ready 附加（flagship Mode）

- [ ] Moat Asset（独有框架/决策表）已在正文兑现
- [ ] Answer Blocks 3–5 个可独立成段
- [ ] Post-publish Metric Spec 已写入 Brief
- [ ] Extractability checklist Pass（见 `portable/extractability-checklist.md`）

---

## 工具预检（Phase 5 前）

```bash
python skills/blog-article/tools/frontmatter_validator.py blog/{NN-slug}.md --keyword "{kw}" --moras-slug
python skills/blog-article/tools/word_count_narrative.py blog/{NN-slug}.md --intent {intent} --min {threshold}
python skills/blog-article/tools/link_checker.py blog/{NN-slug}.md --forbidden "/use-cases/,/app/,/auth/,/admin/"
python skills/blog-article/tools/link_audit.py   # 全库 R1–R4；在 moras/blog/ 运行
```

---

## SelfCheck 输出格式

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| H0 Research / Gate 0R | Pass | |
| H1 P0 G1–G7 | Pass | |
| I1–I5 | Pass | (or: I3 skipped — moras-product scope) |
| H2 Slug Gate B | Pass | |
| H3 字数 | Pass | |
| H4 Moras-Specific | Pass | |

### 12 维
| Dimension | Pass/Fail | Notes |
|-----------|-----------|-------|
| 1 Publishability | Pass | |
| … | … | |
| 12 Moras Project-Specific | Pass | |

### Cannibalization Check
| vs | Boundary | Clear? |
|----|----------|:---:|
| /blog/{slug} | … | ✅ |
| /tiktok-video-generator | blog=教育, TVG=交易 | ✅ |

**Overall**: PASS → audit-ready | FAIL → {fixes}
```

---

## 高频 Fail 速查

| # | 触发条件 | 修复 |
|---|---------|------|
| 1 | slug 无 `/blog/` 前缀 | frontmatter 改为 `/blog/{slug}` |
| 2 | guaranteed $X/month | 改区间 + 条件（I1） |
| 3 | TikTok 佣金率无 as-of | 加日期 + 官方链（I3） |
| 4 | Framework 文 Moras >25% | 减产品段；漏斗后移 |
| 5 | 裸引 $15.8B GMV | 加 Reuters 等来源（G3） |
| 6 | 两篇共用 isoDate | 最晚 date +1 天 |
| 7 | 未跑 tools/ 即标 Pass | 先跑三脚本 |

*moras selfcheck · v2.1 · 2026-08-24 · self-contained*
