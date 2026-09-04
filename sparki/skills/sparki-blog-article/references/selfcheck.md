# Sparki — SelfCheck（12 维 + Hard Gates H0–H4）

> 加载时机：**Phase 5**（Gate C 对照）
> 主文件：SKILL.md §3 Phase 5 指针

---

## Gate C — 全部 Pass 方可 audit-ready

**执行顺序**：先跑 `tools/` 脚本 → 过 Hard Gates H0–H4 → 再过 12 维 Pass/Fail。

---

## Hard Gates（一票否决，先于 12 维）

### H0 — Research 三角 / Gate 0R

- [ ] Research Log 完整（R1–R3 + Synthesis）
- [ ] SERP Fit 已填
- [ ] R3 官方页 + SERP Top3 已 Fetch（CreatorClone：红人公开素材 ≥2）
- [ ] Degraded 已标注且无未验证 P0 claim

### H1 — P0 Gate G1–G7

| ID | 检查项 | Pass 标准 |
|----|--------|----------|
| G1 | 事实错误 | 产品/竞品/数据与官方一致 |
| G2 | 死链 | 无 404 内链；外链不全挂 |
| G3 | 无来源数字 | 量化 claim 有 attribution 或官方来源标注 |
| G4 | 竞品状态 | 定价/定位/AI 原生与否标注正确 |
| G5 | 产品夸大 | 不超出 sparki.io 已上线功能 |
| G6 | 未上线/失效内链 | 主站页=绝对 URL、blog=/blog/{slug}、无相对失效路径 |
| G7 | 品牌/合规风险 | 无贬低；CreatorClone 无代言暗示、无臆测 |

### H2 — Slug Gate B

- [ ] 文件名 = slug；无 NN 前缀；6 问全 Pass（`references/slug-gate.md`）

### H3 — 字数硬门槛

用 `tools/word_count_narrative.py` 预检（叙事词数，排除 frontmatter/表格/FAQ）：

| 类型 | 创作目标 | 硬阻断下限 | `--intent` |
|------|---------|-----------|:---:|
| CreatorClone | 2200–3200 | **<2200 → Fail** | `creator` |
| WorkflowHowTo | 2000–2800 | **<2000 → Fail** | `workflow` |
| FeatureGuide | 1800–2600 | **<1800 → Fail** | `feature` |
| Comparison | 2500–3500 | **<2500 → Fail** | `comparison` |
| AlternativeRoundup | 2000–3000 | **<2000 → Fail** | `alternative` |
| CategoryPOV | 2000–3000 | **<2000 → Fail** | `pov` |
| Announcement | 1200–1800 | **<1200 → Fail** | `announcement` |

### H4 — Sparki-Specific

- [ ] 产品提及比例合规（≤ §2 类型上限）
- [ ] 功能事实（Copy Style/Long to Short/Caption/Commentary/Resizer）引用准确，不超上线能力
- [ ] 定价/credits 有 "as of" + 官网来源
- [ ] 主站链接全部绝对 URL；blog 互链 `/blog/{slug}` 相对
- [ ] Category 取值在枚举内；author = `Sparki Team`
- [ ] CreatorClone：素材级断言有出处；无代言/合作暗示
- [ ] description 在 80–320（validate 硬性）且 120–160 最佳

---

## 12 维 Pass/Fail

### 1. Publishability
- [ ] **H0–H4 全部 Pass**

### 2. Fact / E-E-A-T
- [ ] 竞品描述有官方来源；每竞品 ≥1 优势
- [ ] 产品状态/定价有时效标注（as of {month} {year}）
- [ ] P0 数字有来源或官网声明标注；内部观察有说明
- [ ] CreatorClone 素材证据可回查（正文标红人 + 位置）
- [ ] Source Map 已填（≥3 行）
- [ ] ≥1 场景推荐非 Sparki 方案（对比/替代/指南文）

### 3. Differentiation
- [ ] 正文**兑现** Phase 0R Synthesis；IG 三问成立
- [ ] 与 content-graph 任一文章句子级重复 <30%
- [ ] 有本篇独有框架/表格/素材观察
- [ ] 未完整重定义 Canonical 概念
- [ ] 核心论点在 SERP Top3 找不到等效替代

### 4. Depth / Density
- [ ] 词数达类型下限（H3）
- [ ] 每 ~500 词 ≥1 具体例子
- [ ] 无 "表格 + 一句注释" 空壳 ≥3 处
- [ ] FAQ ≥3 题且独立于正文
- [ ] ≥3 个分析性段落 4–8 句

### 5. Presentation / Rhythm
- [ ] 无 ≥3 处「`**Bold label.**` + 单句」伪列表簇
- [ ] 长段 ≥3；连续短段最长串 ≤2
- [ ] 列表占比 ≤ 类型上限；列表有前导句 + 后随 ≥2 句分析
- [ ] 抽样连续 10 段衔接率 ≥70%
- [ ] H2 后首段是引导段落，非直接列表
- [ ] Claim 原子性 Pass

### 6. Writing / Voice
- [ ] 正向 Voice 5 项（Clear / Practitioner-first / Evidence-led / Category-building / Fair）
- [ ] 禁词（revolutionary / game-changing / unlock / seamless / magic / cutting-edge）0 命中
- [ ] 空泛句 ≤2；无虚构开场
- [ ] 每 300–500 词出现 1 个具体对象
- [ ] Judgment J1–J2 Pass

### 7. Objectivity
- [ ] 产品占比合规；≥1 非自有方案更适合场景
- [ ] 漏斗结构符合 §3 writing-constraints
- [ ] 竞品无贬低措辞

### 8. Structure / Links
- [ ] 模块顺序：YAML → TL;DR → H2 → Conclusion → FAQ
- [ ] TL;DR 3–5 bullets；bullet 1 是 snippet 定义句
- [ ] blog 互链 ≥2；锚文本描述性
- [ ] 主站链接绝对 URL 且存活；外链 2–6；竞品 nofollow
- [ ] Forthcoming ≤1（脚注）

### 9. SEO / SERP
- [ ] title 含 primary keyword；title <60c / desc 120–160c
- [ ] H2 覆盖关键词簇；Research/CategoryPOV 有 snippet 定义句
- [ ] SERP Fit 已填；**BLUF 三处** Pass

### 10. Conversion
- [ ] CTA ≤2；匹配读者阶段（CTA 目标：Try Free / 功能页）
- [ ] CTA 前已给足价值；无虚假承诺

### 11. Slug Design
- [ ] 文件名 = slug、kebab-case、无年份/禁词/NN
- [ ] ≤60 字符；"大声读"通过；12 反模式零触发

### 12. Cross-Article
- [ ] 同 cluster 无矛盾/重复（单篇 N/A）
- [ ] hub-spoke 链接完整；spoke 回链 hub
- [ ] 跨篇产品描述一致性；Cannibalization 通过
- [ ] Intro/Conclusion 不模板化（vs 61 篇同簇文）

---

## SelfCheck 输出格式

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| H0 Research / Gate 0R | Pass | |
| H1 P0 G1–G7 | Pass | |
| H2 Slug Gate B | Pass | |
| H3 字数 | Pass | |
| H4 Sparki-Specific | Pass | |

### 12 维
| Dimension | Pass/Fail | Notes |
|-----------|-----------|-------|
| 1 Publishability | Pass | H0–H4 全 Pass |
| … | … | … |

**Overall**: PASS → audit-ready | FAIL → {fixes}
```

---

## Perfect-Ready 附加清单（flagship 专用）

- [ ] Moat Asset 已在正文兑现（素材级拆解/原创框架）
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 已标注；Post-publish Metric Spec 已写入 Brief

---

## 高频 Fail 速查

| # | 触发条件 | 修复 |
|---|---------|------|
| 1 | CategoryPOV/CreatorClone 前 30% 出现产品 pitch | 产品移至论证后、FAQ 前 |
| 2 | Comparison 写"Sparki 唯一推荐" | 与同类并列；加 ≥1 非 Sparki 更适合场景 |
| 3 | 相对路径链到主站页面 | 改绝对 URL `https://sparki.io/...` |
| 4 | 无 Source Map 且含 ≥3 个 P0 claim | Phase 5/6 补 Claim×Source 表 |
| 5 | Hub 概念在 spoke 文完整重定义 | 改 1–2 句 + canonical link |
| 6 | 伪列表 | 合并为 ≥4 句分析段 |
| 7 | CreatorClone 无素材证据写断言 | 回 Phase 0R 抓素材或删断言 |
| 8 | 文件名 ≠ slug 或带 NN | 改名重过 Gate B |

---

*selfcheck · sparki v1.0.0 · 2026-09-04*
