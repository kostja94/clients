# FinalRound Gates（Skill reference）

> **Gate A/B/0R/C + KEEP/MERGE + 冲突快查。** Phase 0 / 1 / 2 / 5 加载。

---

## 1. Gate 总览

| Gate | 位置 | 内容 | 阻断条件 |
|------|------|------|---------|
| **A** | Phase 0 | Investment Score + KEEP/MERGE/STOP | MERGE / STOP / Investment <3.0 / 必问缺失 |
| **0R** | Phase 0R | Research 三角完整 + Synthesis | R2 未搜 / R3 未 Fetch / 无 Synthesis / P0 claim 不可验证 |
| **B** | Phase 2 | Slug 6 问全 Pass | 任一问 Fail |
| **C** | Phase 5 | H0–H4 + 12 维全 Pass | 任一 Fail → 回溯 |

---

## 2. Gate A — Intake

### 2.1 Investment Score（五因子算术平均，各 1–5）

| 因子 | 1 分 | 5 分 |
|------|------|------|
| 搜索需求 | 几乎无搜索量 | 稳定或上升 |
| 商业相关性 | 与 ICP/产品路径无关 | 靠近购买或使用路径 |
| 差异化能力 | 只能复述 SERP | 有 Moat / Proof 可引用 |
| 证据可得性 | 无法验证强 claim | R3 可支撑 |
| 内容生命周期 | <3 月过时 | 2+ 年常青 |

| 均分 | 动作 |
|------|------|
| **≥4.0** | KEEP，按声明 Mode 执行 |
| **3.0–3.9** | KEEP 但**降级 Mode** 或改角度 |
| **<3.0** | MERGE / STOP / 降级为 FAQ·短帖 |

### 2.2 KEEP / MERGE（3 条件满足 ≥2 → KEEP）

| 条件 | 判断 |
|------|------|
| 搜索意图独立 | 与已有文章 primary keyword 搜索池重叠 <50% |
| 读者阶段不同 | Awareness / Consideration / Evaluation / Activation 不重叠 |
| 内容深度不可压缩 | 核心论证 >800 词，无法压入他文 ≤3 段 |

### 2.3 信息增量 Gate（KEEP 后强制）

相对 SERP Top 3，本篇须至少提供 **2 项** 以下之一，否则 **STOP**：

- 独有分析框架（如面试类型分类、工具选型决策树）
- 可执行决策表（场景 × 工具 × 成本/适用区间）
- 带方法论的内部实测（n + 时间窗 + 限定语）
- 跨篇 canonical 引用 + 新边界声明

---

## 3. Gate 0R — Research

### 3.1 Research 三角

```
R1 — 读 allow-extra-reads 项目文档（finalround.md + product-competitors + content-graph）
R2 — Web 搜索 primary keyword → SERP Top 5 + PAA
R3 — Fetch finalroundai.com 相关页 + SERP Top 3–5（竞品/官方文档）
Synthesis + Candidate Examples
→ Research Log + SERP Fit → Gate 0R
```

### 3.2 Mode 差异

| R 步骤 | lite | standard | flagship |
|--------|------|----------|----------|
| R2 Top5 | 可选 | ✅ | ✅ |
| R3 Top3–5 | 可选 | Top3 | Top5 + 官方页 |
| Synthesis | 简版（1–2 句） | 完整 | 完整 + Moat 验证 |
| Candidate Examples | 0–1 | ≥1 | ≥2 |

### 3.3 Degraded 模式

R2/R3 缺失时标注 `Research mode: Degraded — {reason}`；Degraded 下正文**不得**写 P0 级未验证 claim。

---

## 4. Gate B — Slug

### 4.1 Slug 6 问

| # | 问题 |
|---|------|
| 1 | 是否含 primary keyword 完整核心词？ |
| 2 | 是否常青（无年份/无数量/无内部架构词）？ |
| 3 | 是否 kebab-case、全小写、≤60 字符？ |
| 4 | 是否有语义余量（30% 内容变化后仍合适）？ |
| 5 | "大声读"测试通过（去掉连字符通顺）？ |
| 6 | 与既有文章/官网无冲突？ |

### 4.2 Slug 12 反模式

| # | 反模式 |
|---|--------|
| 1 | 含年份 |
| 2 | 含数量/序数（top-5 / 7-ways） |
| 3 | 连续重复词（app-app / ai-ai） |
| 4 | 内部架构词（framework / strategy / diagnosis / guide / complete） |
| 5 | 下划线/大写/空格 |
| 6 | 分类前缀沉积（多篇同前缀） |
| 7 | 与既有 slug 重复 |
| 8 | >60 字符 |
| 9 | 不含主关键词 |
| 10 | 人不可读（连读不通顺） |
| 11 | 缩写模糊（无词义） |
| 12 | 非 kebab-case |

---

## 5. Gate C — SelfCheck

### 5.1 Hard Gates

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填 |
| **H1** | P0 Gate G1–G7 | 零触发 |
| **H1B** | FinalRound Gate F1–F6 | 零触发 |
| **H2** | Slug Gate B | 6 问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | FinalRound-Specific | 产品形态（桌面应用核心）、定价（无免费试用）、旧词规避、Stealth 措辞准确 |

### 5.2 12 维 Pass/Fail

见 `references/selfcheck.md` 完整判据。

**Gate C**：H0–H4 + 12 维全 Pass → **audit-ready**（可进入加权终审）；任一 Fail → 标注修复动作 → 按回溯表回退修复。

---

## 6. Gate 失败回溯表

| Gate / 结果 | 回退至 | 典型原因 | 修复后 |
|-------------|--------|---------|--------|
| **Gate A → STOP** | 流程结束 | 增量不足、MERGE 建议、必问未确认 | 改选题或合并后重新 Phase 0 |
| **Gate A → MERGE** | 流程结束 | 搜索意图重叠、深度不可独立 | 执行合并清单，不写新稿 |
| **Gate 0R ❌** | **Phase 0R** | SERP 未搜、Top3 未 Fetch、无 Synthesis | 补 R2/R3 → 更新 Log → 重过 Gate 0R |
| **Gate 0R ❌ — 事实不可验证** | **STOP 或 Phase 0** | 官方页无法 Fetch 且需写 P0 claim | Degraded 模式不写 P0 claim，或改选题 |
| **Gate 3.5 ❌** | **Phase 3** | 同批 Outline H2/叙事/Synthesis 重叠 | 改角度或 MERGE → 重过 3.5 |
| **Gate B ❌** | **Phase 2** | Slug 反模式、关键词不对齐 | 新 slug → 重过 Gate B → 更新 Brief |
| **Gate C ❌ — 写作/事实类** | **Phase 4** | EEAT、Voice、Presentation、产品事实、F1–F6 | 改稿 → 重跑 Phase 5 SelfCheck |
| **Gate C ❌ — 结构类** | **Phase 3** | 缺模块、H2 骨架不符 | 改 Outline → Phase 4 重写或局部改稿 |
| **Gate C ❌ — Slug/Meta** | **Phase 2** | title/description 不合规 | 改 frontmatter → Phase 4 同步正文首段 |
| **Gate C ❌ — 混合** | **Phase 3 或 4**（以多数为准） | 多项 Fail | 先修结构再修 prose |

**判定写作 vs 结构**：Fail 项落在维度 4–6、10 → 优先 Phase 4；维度 8–9、11 → 优先 Phase 2–3；维度 2 → Phase 4 + 事实核查。

---

*gates · FinalRound · v1.0.0*
