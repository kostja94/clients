# Lucius AI — SelfCheck（12 维 + Hard Gates H0–H4）

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
- [ ] R3 官方页 ≥1 + SERP Top3 已 Fetch（或 Degraded 已标注且无未验证 P0 claim）

### H1 — P0 Gate G1–G7

| ID | 检查项 | Pass 标准 |
|----|--------|----------|
| G1 | 事实错误 | 产品/竞品/数据与官方一致 |
| G2 | 死链 | 无 404 内链；外链不全挂 |
| G3 | 无来源数字 | 所有量化 claim 有 attribution |
| G4 | 竞品状态 | GA/Preview/Archived 标注正确 |
| G5 | 产品夸大 | 不超出 GA 能力 |
| G6 | 未上线内链 | 无禁止路径 |
| G7 | 品牌风险 | 无贬低性措辞 |

### H2 — Slug Gate B

- [ ] Design-Time 六问全 Pass（细则见 `references/slug-gate.md`）

### H3 — 字数硬门槛

词数达 §2 类型词数下限；可用 `tools/word_count_narrative.py` 预检。

| 类型 | 创作目标 | 硬阻断下限 | `--intent` |
|------|---------|-----------|------------|
| Research/Glossary | 2000–3000 | **<2000 → Fail** | `research` |
| Comparison | 2500–3500 | **<2500 → Fail** | `comparison` |
| Product/Scenario | 2000–2800 | **<2000 → Fail** | `product` |
| Alternative | 2000–2800 | **<2000 → Fail** | `alternative` |
| Announcement | 1200–1800 | **<1200 → Fail** | `announcement` |

### H4 — Lucius-Specific

- [ ] 产品提及比例合规（≤ §2 类型上限）
- [ ] 三步工作流（Connect → Detect → Handoff）描述准确
- [ ] 四大能力（Auto-Answer / Spam Filter / Onboarding / Self-Updating Knowledge）引用正确
- [ ] 关键指标（70%+/65%/2min）引用正确 + 有来源标注
- [ ] 支持平台列表完整
- [ ] Product Mention 1–2 次合规
- [ ] 产品名大小写统一（Lucius、Lucius AI Teammate）

---

## 12 维 Pass/Fail

### 1. Publishability

- [ ] **H0–H4 全部 Pass**

### 2. Fact / E-E-A-T

- [ ] 竞品描述有官方来源；每竞品 ≥1 优势
- [ ] 产品状态有时效标注（as of {month} {year}）
- [ ] P0 级数字有 `[Source: URL]`；P1 级有链接或限定词
- [ ] 内部数据有标注（"based on internal observation"）
- [ ] Source Map 已填（Claim × Paragraph × Source × Confidence，≥3 行）
- [ ] ≥1 场景推荐非 Lucius 方案

### 3. Differentiation

- [ ] 正文**兑现** Phase 0R Synthesis；IG 三问在成稿仍成立
- [ ] 与 content-graph.md 任一文章句子级重复 <30%
- [ ] 有本篇独有框架/表格/场景
- [ ] 未完整重定义 Canonical 概念
- [ ] 核心论点/框架在 SERP 前 3 竞品中找不到等效替代

### 4. Depth / Density

- [ ] 词数达 §2 类型下限（H3 Pass）
- [ ] 每 ~500 词 ≥1 具体例子
- [ ] 无 table+one-sentence 空壳 ≥3 处
- [ ] FAQ ≥3 题且独立于正文（非复制）
- [ ] ≥3 个分析性段落达 4–8 句（80–200 词）

### 5. Presentation / Rhythm

- [ ] **伪列表检测**：全文无 ≥3 处「`**Bold label.**` + 单句」连续簇
- [ ] 长段（≥4 句）≥3
- [ ] 连续短段（≤2 句）最长串 ≤2
- [ ] 列表占比 ≤ 类型上限
- [ ] 每个列表有前导句；列表后有 ≥2 句分析
- [ ] 无连续 2 个 H2 section 各含列表而中间无分析段落
- [ ] 抽样连续 10 段，≥7 对有衔接手段（衔接率 ≥70%）
- [ ] H2 后首段是引导段落，非直接列表
- [ ] Claim 原子性 Pass（段首 claim · 指代可解析 · chunk 可独立理解）

### 6. Writing / Voice

- [ ] 正向 Voice 5 项（Clear / Community-friendly / Evidence-led / Category-building / Fair）
- [ ] 禁词（revolutionary / game-changing / unlock / seamless / magic）0 次命中
- [ ] 空泛句 ≤2 处
- [ ] 无虚构 community manager 场景开头
- [ ] 每 300–500 词出现 1 个具体对象
- [ ] Judgment J1–J2 Pass

### 7. Objectivity

- [ ] 产品占比合规（≤ §2 类型上限）
- [ ] ≥1 非自有方案更适合场景
- [ ] 漏斗结构不过透明
- [ ] 竞品描述无贬低性措辞

### 8. Structure / Links

- [ ] 模块顺序：YAML → TL;DR → H2 → Conclusion → FAQ
- [ ] TL;DR 为 3–5 bullet；bullet 1 是 snippet 定义句
- [ ] blog 互链 ≥2；内链锚文本描述性
- [ ] canonical 概念 1–2 句 + link
- [ ] 外链 2–6；竞品 `rel="nofollow noopener"`
- [ ] Forthcoming ≤1（脚注）

### 9. SEO / SERP

- [ ] H1/title 含 primary keyword；title <60c / desc <160c
- [ ] H2 覆盖关键词簇
- [ ] Research 有 snippet-ready 定义句（40–60 词）
- [ ] SERP Fit 已填
- [ ] **BLUF 三处** Pass（B1 TL;DR / B2 每 major H2 首段 / B3 FAQ 首句即答）

### 10. Conversion

- [ ] CTA ≤2；匹配读者阶段
- [ ] CTA 前已给足价值
- [ ] 无虚假承诺

### 11. Slug Design

- [ ] 常青 kebab-case；无年份/数量/禁词
- [ ] 5–8 词、≤60 字符
- [ ] 通过"大声读"测试
- [ ] 通过 `slug-gate.md` 12 反模式表
- [ ] 语义余量原则通过

### 12. Cross-Article

- [ ] 同 cluster 无矛盾/重复（单篇 N/A）
- [ ] Hub-spoke 链接完整性：spoke 回链 hub
- [ ] 跨篇产品描述一致性
- [ ] Cannibalization 检查通过
- [ ] Intro/Conclusion 不与其他篇模板化相同

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
| H4 Lucius-Specific | Pass | |

### 12 维
| Dimension | Pass/Fail | Notes |
|-----------|-----------|-------|
| 1 Publishability | Pass | H0–H4 全 Pass |
| 2 Fact/E-E-A-T | Pass | |
| 3 Differentiation | Pass | |
| 4 Depth/Density | Pass | |
| 5 Presentation/Rhythm | Pass | |
| 6 Writing/Voice | Pass | |
| 7 Objectivity | Pass | |
| 8 Structure/Links | Pass | |
| 9 SEO/SERP | Pass | |
| 10 Conversion | Pass | |
| 11 Slug Design | Pass | |
| 12 Cross-Article | Pass | N/A — single article |

**Overall**: PASS → audit-ready | FAIL → {fixes}
```

---

## Perfect-Ready 附加清单（flagship 专用）

- [ ] Moat Asset 已在正文兑现
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 类型已标注（框架/数据/checklist/案例/洞见）
- [ ] Post-publish Metric Spec 已写入 Brief
- [ ] Distribution Snippets 已产出

---

## 高频 Fail 速查

| # | 触发条件 | 修复 |
|---|---------|------|
| 1 | Research 文前 30% 出现产品 pitch | 产品移至定义后、FAQ 前 |
| 2 | Comparison 写「Lucius 唯一推荐」 | 与同类并列；加 ≥1 非自有更适合场景 |
| 3 | forthcoming 作正文核心流程链接 | 移除或降至脚注（≤1） |
| 4 | 无 Source Map 且含 ≥3 个 P0 量化 claim | Phase 5/6 补 Claim×Source 表 |
| 5 | Hub 概念在 spoke 文中完整重定义 | 改 1–2 句 + canonical link |
| 6 | 呈「加粗标签 + 单句」伪列表 | 合并为 ≥4 句分析段 |
| 7 | SelfCheck 未逐段计数即标 Pass | 重做机械计数后再过 Gate C |

---

*selfcheck · v2.0.0 · 2026-07-06*
