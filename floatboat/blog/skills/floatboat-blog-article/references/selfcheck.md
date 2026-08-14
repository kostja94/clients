# Floatboat SelfCheck — Hard Gates H0–H4 + 12 维 Pass/Fail

> 加载时机：**Phase 5**（Gate C 对照）
> 主文件：SKILL.md §3.5 指针

---

## Gate C — 全部 Pass 方可 audit-ready

> **Gate C（Phase 5）**：**H0–H4** 全部 Pass + **12 维** SelfCheck 全部 Pass → **audit-ready**（≠ publish-ready）。任一 Fail → 标注修复动作，按 SKILL §3.G 回溯表回退修复。

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
| G3 | 无来源数字 | 所有量化 claim 有 attribution（P0 级 link + P1 级限定词） |
| G4 | 竞品状态 | GA/Preview/Archived 标注正确 |
| G5 | 产品夸大 | 不超出 GA 能力 |
| G6 | 未上线内链 | 无禁止路径（对照 project-config.md 白名单） |
| G7 | 品牌风险 | 无贬低性措辞、法律风险 |

### H2 — Slug Gate B

- [ ] Design-Time 六问全 Pass（细则见 `references/gates.md` §5）

### H3 — 字数硬门槛

词数在 `article-types.md` §1 目标区间内；低于硬阻断下限 → Fail。可用 `tools/word_count_narrative.py` 预检。

| 类型 | 创作目标 | 硬阻断下限 | `--intent` |
|------|---------|-----------|------------|
| Research/Glossary | 2400–3500 | **<2000 → Fail** | `research` / `deep_glossary` |
| Comparison | 2800–3500 | **<1500 → Fail** | `comparison` |
| Alternative | 2200–3000 | **<1500 → Fail** | `comparison` |
| Product / Scenario | 2000–2700 | **<1500 → Fail** | `product_tutorial` |
| Announcement | 1500–2000 | **<1200 → Fail** | `simple_glossary` |

### H4 — Floatboat-Specific

- [ ] 产品提及比例合规（对照 article-types.md §1）
- [ ] Calendar-Driven 四步机制在正文中正确呈现
- [ ] Combo Skills / FloatIM 引用正确（按 Topic Scope 分开叙事）
- [ ] Pillar Hub（`what-is-agentic-calendar`）被 ≥2 篇 spoke 自然互链（spoke 文适用）
- [ ] Canonical Concept Registry（content-graph.md）对照通过
- [ ] 产品名大小写统一（Floatboat、FloatIM、Combo Skills、Tacit Engine、Selfware）
- [ ] 品类官方表述一致

---

## 12 维 Pass/Fail

### 1. Publishability

- [ ] **H0–H4 全部 Pass**

### 2. Fact / E-E-A-T

- [ ] 竞品描述有官方来源占位；每竞品 ≥1 优势
- [ ] 产品状态有时效标注（as of {month} {year}）
- [ ] P0 级数字有 `[Source: URL]`；P1 级有链接或限定词
- [ ] 内部数据有 n= 标注（"based on internal analysis, n=X"）
- [ ] **Research/Glossary**：≥2 个一手来源（官方 docs / 公告 / 标准文档）
- [ ] **Comparison/Alternative**：每个主要竞品 ≥1 官方来源占位（docs / pricing / changelog）
- [ ] Source Map 已填（Claim × Paragraph × Source × Confidence，≥3 行）

### 3. Differentiation

- [ ] 正文**兑现** Phase 0R Synthesis；IG 三问在成稿仍成立
- [ ] 与 content-graph.md 任一文章句子级重复 <30%
- [ ] 有本篇独有框架/表格/场景
- [ ] 未完整重定义 Canonical 概念
- [ ] 核心论点/框架在 SERP 前 3 竞品中找不到等效替代
- [ ] **冗余度检测**：逐段标记"读者可在竞品中找到等效内容吗？" — 冗余段占比 >40% → Fail

### 4. Depth / Density

- [ ] 词数达 §2 类型下限（H3 Pass）
- [ ] 每 ~500 词 ≥1 具体例子
- [ ] 无 table+one-sentence 空壳 ≥3 处
- [ ] FAQ 有独立内容（非正文复制）
- [ ] ≥3 个分析性段落达 4–8 句（80–200 词）

### 5. Presentation / Rhythm

- [ ] **伪列表检测**：全文无 ≥3 处「`**Bold label.**` + 单句（≤2 句）」连续簇；有则 Fail → 合并为分析段
- [ ] **机械计数**（不可目测 Pass）：逐段数句数，记录长段（≥4 句，主干论证）≥3；中段（2–4 句，过渡关节）占主体；短段（1–2 句，节奏锚点）占比 15–25%；连续短段最长串 ≤2；**段落长度标准差 ≥1.5**
- [ ] 列表占比 ≤ 类型上限
- [ ] 每个列表有完整前导句；列表后有 ≥2 句分析段落
- [ ] 无连续 2 个 H2 section 各含列表而中间无分析段落（列表轰炸）
- [ ] 表格前后各有 ≥2 句分析段落
- [ ] 抽样连续 10 段，≥7 对有衔接手段（衔接率 ≥70%）
- [ ] H2 后首段是引导段落，非直接列表或表格
- [ ] Claim 原子性 Pass（段首 claim · 指代可解析 · chunk 可独立理解）

### 6. Writing / Voice

- [ ] 五正向标准满足（Clear / Evidence-led / Practitioner-grade / Calm / Category-building）
- [ ] 五禁止腔调未触发
- [ ] 无 Imagine… 开头
- [ ] 空泛句 ≤2 处
- [ ] 每 300–500 词出现 1 个具体对象
- [ ] Judgment J1–J2 Pass（强判断 scoped + 同段/前段有依据）

### 7. Objectivity

- [ ] 产品占比合规（对照 article-types.md §1）
- [ ] ≥1 非自有方案更适合场景（Comparison/Alternative）
- [ ] 漏斗结构不过透明（对照 writing-constraints.md §3）；Disclosure 到位
- [ ] category 与内容一致
- [ ] 竞品描述无贬低性措辞

### 8. Structure / Links

- [ ] 模块顺序：YAML → TL;DR → H2 → Conclusion → FAQ
- [ ] TL;DR 为 3-5 bullet；bullet 1 是 snippet 定义句（40-60 词）
- [ ] TL;DR + H2 + Conclusion + FAQ 齐全
- [ ] FAQ 节用 `## FAQ`，问题用 `### ` 不带序号（如 `### What is an agentic calendar?`）
- [ ] blog 互链 ≥2；内链锚文本描述性（无 "click here"）
- [ ] canonical 概念 1–2 句 + link；外链 rel="nofollow noopener"
- [ ] Forthcoming ≤1

### 9. SEO / SERP

- [ ] H1/title 含 primary keyword；title <60c / desc <160c
- [ ] H2 覆盖关键词簇
- [ ] Research 有 snippet-ready 定义句
- [ ] SERP Fit 已填
- [ ] **BLUF 三处** Pass（B1 TL;DR / B2 每 major H2 首段 / B3 FAQ 首句即答）

### 9B. Date / Publishing

- [ ] publishDate 不与已有文章重叠（对照 content-graph.md 日期表）
- [ ] 每自然日 ≤1 篇新文章（§1B 日期策略）
- [ ] modifiedDate ≥ publishDate（上线后适用）

### 10. Conversion

- [ ] CTA ≤2；匹配读者阶段
- [ ] 无虚假承诺

### 11. Slug / Meta

- [ ] 常青、无禁词、intent-first（同 H2 Gate B）
- [ ] 5–8 词、≤60 字符
- [ ] 无年份/数量/序数；无连续重复词
- [ ] 通过"大声读"测试；通过 article-types.md §9 反模式表
- [ ] 30% 内容变化后 slug 仍然合适（语义余量原则）

### 12. Cross-Article

- [ ] 同 cluster 无矛盾/重复（单篇 N/A）
- [ ] Hub-spoke 链接完整性：spoke 回链 hub
- [ ] 跨篇产品描述一致性：四步机制表述统一、Calendar-Driven vs Chat-Based 对比口径一致
- [ ] Cannibalization 检查：新文关键词不与已有文章 SERP 意图重叠 >50%
- [ ] **Intro 功能序列检测**：3 句功能序列与同簇已有文相同 → Fail
- [ ] **Conclusion 互换测试**：Conclusion 首段替换到同簇另一篇仍通顺 → Fail
- [ ] Scheduling Agent 簇叙事弧线不与其他 4 篇雷同（同簇适用）

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
| H4 Floatboat-Specific | Pass | |

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
| 11 Slug/Meta | Pass | |
| 12 Cross-Article | Pass | N/A — single article |
| — Date/Publishing | Pass | publishDate 不与已有重叠 |

**Overall**: PASS → audit-ready，进入 Phase 6 Delivery | FAIL → {fixes}，按 §3.G 回溯
```

---

## 高频 Fail 速查（Gate C 前 30 秒对照）

| # | 触发条件 | 修复 |
|---|---------|------|
| 1 | 英文正文用 one-person company 作主词 | 改 solopreneur / solo founder |
| 2 | Research 文前 30% 出现产品 pitch | 产品移至定义后、FAQ 前 |
| 3 | Comparison/Alternative 写「Floatboat 唯一推荐」 | 与同类并列；加 ≥1 非自有更适合场景 |
| 4 | FloatIM 与 Floatboat 桌面工作区混为一谈 | 按 Topic Scope 分开叙事 |
| 5 | forthcoming 作正文核心流程链接 | 移除或降至 Related 脚注（≤1） |
| 6 | 无 Source Map 且含 ≥3 个 P0 量化 claim | Phase 5/6 补 Claim×Source 表 |
| 7 | Hub 概念在 spoke 文中完整重定义 | 改 1–2 句 + canonical link |
| 8 | Intro 3 句功能序列与同簇已有文相同 | 重写首段，加入本篇独有细节 |
| 9 | Comparison 遗漏 Claude Cowork / Manus 等 P0 竞品 | 补入表或说明排除理由 |
| 10 | 对比表 Yes/No 无脚注、误导读者 | 加 nuance 或表下简化说明 |
| 11 | 呈「加粗标签 + 单句」伪列表 | 合并为 ≥4 句分析段；参照 writing-constraints.md §4 |
| 12 | SelfCheck 未逐段计数即标 Pass | 重做机械计数后再过 Gate C |
| 13 | publishDate 与已有文章同一天 | 一天一篇规则：从锚点日往前错开至唯一日 |
