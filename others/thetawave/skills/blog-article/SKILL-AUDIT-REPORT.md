# ThetaWave Blog Article SKILL.md — 严苛审核报告

**审核日期**: 2026-06-15  
**文件**: `D:\项目文档\clients\thetawave\skills\blog-article\SKILL.md`  
**版本**: v1.0.0 (metadata declared)  
**总行数**: 757  
**审核者**: Claude (claude-sonnet-4-6)  

---

## 总评

**Overall: FAIL** — 1 个阻断级缺陷 (G1–G7 未定义)、2 个高危缺陷 (search intent 概念混淆、`templates` 全文拼写错误)、4 个中危缺陷、6 个低危建议。阻断缺陷必须先修复才能进入生产使用。

---

## 阻断级缺陷 (Blocker) — 1 个

### 🔴 B1. Publishability G1–G7 未定义 (Line 420, Line 107)

Phase 6 SelfCheck 第一个维度引用 "Publishability G1–G7"，Line 107 引用 "G6 规则"，但**全文从未定义 G1–G7 各自是什么**。这是 §2.2 全类型通用模块、Phase 6 自检、以及 templates 审核链的共同前提，缺失导致 Agent 无法执行该维度的 self-check。

**Line 420**:
> Publishability G1–G7 | 事实、死链、来源、竞品状态、产品夸大、未上线内链、品牌风险

括号内给了 7 个关键词，但没有编号到 G1–G7 的映射，也没有每条的判断标准。Line 107 单独提到 "G6 规则：不链未上线页"，这暗示 G1–G7 应该是一组明确编号的规则。

**修复建议**: 在 §1 或 §6 之后新增一个小节，明确枚举 G1–G7:
- G1: 事实核查
- G2: 死链
- G3: 来源标注
- G4: 竞品状态准确性
- G5: 产品夸大
- G6: 未上线内链
- G7: 品牌风险

每条附 1–2 句判断标准。

---

## 高危缺陷 (Critical) — 2 个

### 🟠 C1. `templates` 全文拼写错误 (7 处)

标准英文单词为 `templates`，但全文使用 `templates`。涉及行: 9, 14, 51, 453, 454, 702, 756。这是一个系统性的拼写错误，且该词出现在 frontmatter `complements` 字段、Phase 7 交付指令模板（复制即用的 prompts）中——如果 templates/ 文件夹实际命名为 `templates`，会导致路径不匹配。

**验证需求**: 确认实际文件夹名称是 `templates` 还是 `templates`，然后全文替换。

### 🟠 C2. Search Intent 与 Article Type 概念混淆 (Line 327, Phase 2 Brief)

Phase 2 Article Brief 模板中:

```markdown
**Search intent**: Commercial / Alternative / StudyMethodHub / StudyMethodSpoke / HowTo
```

这里的枚举值实际上是 §2.1 的**文章类型 (article type)**，而非 SEO 领域的 search intent（informational / commercial / transactional / navigational）。同时 Phase 3 "SERP Fit mini-audit" (Line 350) 又单独列出了 `Search intent:` 字段——两处的 "search intent" 含义不一致。

**修复建议**: Phase 2 Brief 中改为 `**Article type**` 或 `**Content type**`，与 §2.1 路由表对齐。Phase 3 SERP Fit 中保留 `Search intent` 但使用标准 SEO 四分类 (informational / commercial / transactional / navigational)。

---

## 中危缺陷 (Major) — 4 个

### 🟡 M1. Phase 1 关键词冲突快查表不完整 (Line 306–313)

快查表仅覆盖 5 个 slug（best-ai-note-takers, quizlet-alternatives, chatgpt-alternatives, study-methods-compared, cornell-note-taking-method），但 §4.1 列出 12 篇已有文章。其余 7 篇（how-to-take-notes-in-college, how-to-study-for-finals, mind-mapping-method, zettelkasten-method, feynman-technique, sq3r-method, leitner-system）的关键词边界未在表中。

这意味着 Agent 为新文章做 KEEP/MERGE 决策时，缺少对 7/12 已有内容的边界参考。

**修复建议**: 补全 12 篇的快查表，或改为引用 §4.1 完整表 + 对每篇文章追加 "边界" 列。

### 🟡 M2. 交叉引用 "内联 meta §博客规则" 悬空 (Line 237)

§2.8 标题为:

> Slug、Title、Description（内联 meta §博客规则）

但全文不存在 "§博客规则" 这个 section。§9 提到 `thetawave-meta-title-description` 是一个独立 skill，不是本文内的小节。

**修复建议**: 改为指向 §2.8 自身，或改为 "(内联规则，详见下方)"。如果 meta skill 确有独立的博客规则，改为引用 meta skill 名称。

### 🟡 M3. "标注 verify on site" 语义模糊 (Line 391)

Phase 5 事实与合规:

> 定价 | $118.80/年；标注 verify on site

Agent 无法确定 "标注" 在草稿中应如何呈现：是写 `[verify on site]` 标记、是加 HTML 注释、还是输出到 SelfCheck 而非草稿？对于其他量化 claim 有明确的 `[Source: URL]` 格式，但定价这里的格式缺失。

**修复建议**: 明确标注格式，例如: `[$118.80/年 — verify on thetawave.ai/pricing]`。

### 🟡 M4. SelfCheck 示例不完整 (Line 436–442)

SelfCheck 模板只展示了一行:

```markdown
| Dimension | Pass/Fail | Notes |
|-----------|-----------|-------|
| ... | Pass | |
```

12 个维度的完整示例缺失。Agent 在面对实际 SelfCheck 时没有参照基准，可能对某些维度（如 "Differentiation <30%"、"Study hub-spoke"）的判断标准产生歧义。

**修复建议**: 参照 §10 Mini Example，为 cornell-note-taking-method 补充一个完整的 12 维 SelfCheck 示例表。

---

## 低危缺陷 (Minor) — 6 个

### 🔵 m1. "选问" 措辞简略 (Line 288)

> **选问**：是否链特定 Use Case；pricing 是否需在文中提及。

"选问" 是 "可选问题" 的缩写，但这是一份英文为主的 skill 文档，突然出现的缩写中文可能让中英文混用的 Agent 感到困惑。建议改为 **Optional** 或 **额外可选问题**。

### 🔵 m2. §5 关键词 Intent 分类与 §2.1 不一致 (Lines 536–576)

§2.1 路由表中 intent 列为 "best X / tool selection"、"X alternative(s)"、"compare N methods" 等，描述的是**文章类型意图**。但 §5 中 intent 列为 "capture"、"generate"、"人群+工具"、"选型" 等，描述的是**用户搜索意图**。两套体系混在同一个文档中。

**修复建议**: 统一分类体系，或在 §5 表头将 "intent" 改为 "user intent" 以区分。

### 🔵 m3. `internal-external-links-checklist 状态表` 未定义 (Line 659)

> 成稿后提示人类更新 `blog/readme.md` 与 internal-external-links-checklist 状态表。

这个文件在 skill 内部和 §9 的 templates 分工中均未被描述。Agent 不知道它的位置、格式、或应如何提示人类更新。

**修复建议**: 要么删除此引用，要么在 §7 中添加一行说明该文件的位置和作用。

### 🔵 m4. AI Connection 示例使用 HTML 内链 (Line 752)

> `<a href="https://thetawave.ai/feature/pdf-to-notes">AI PDF to Notes</a>`

§6.4 规定内链使用 markdown 格式，竞品外链才用 `rel="nofollow noopener"` 的 HTML。此示例将内部 feature 链接写成 HTML，可能误导 Agent 对内链也用 HTML 格式。而且 `rel="nofollow noopener"` 对内链是反模式。

**修复建议**: 改为 Markdown: `[AI PDF to Notes](https://thetawave.ai/feature/pdf-to-notes)`，移除 nofollow。

### 🔵 m5. Phase 3 缺少显式 "下一步" 指令 (Lines 340–357)

Phase 3 以 "SERP Fit mini-audit" 结束，但没有像其他 Phase 那样说明完成后进入 Phase 4。Agent 需要从 §0 执行顺序 (Line 54) 推导。

**修复建议**: Phase 3 末尾加一行: `→ 进入 Phase 4 — Outline`。

### 🔵 m6. Differentiation <30% 度量标准缺失 (Line 422)

> Differentiation | 与 §4 重复 <30%

"重复" 如何度量？是逐词 overlap、概念 overlap、还是 H2 结构相似度？Agent 无法客观执行此判断。

**修复建议**: 明确为: "H2 标题重叠 <30%（即 12 篇已有文章 ≈3.6 个 H2 以内）；核心论点不重复"。

---

## 语言/本地化一致性

| 问题 | 位置 | 严重度 |
|------|------|--------|
| 中文指令 + 英文内容规则混排 | 全文 | 设计决策，非缺陷 |
| "提示人类" vs 英文 `remind human` | Lines 51, 472, 659 | 低 — 可接受但风格不统一 |
| "选问" 缩写 | Line 288 | 低 |

---

## 硬编码值验证

| 值 | 位置 | 验证结果 |
|----|------|---------|
| $118.80/年; $9.90/月 | Line 79 | $118.80 ÷ 12 = $9.90 ✅ |
| 学生 30% off → $83.16 | Line 79 | $118.80 × 0.7 = $83.16 ✅ |
| 12 篇文章; 下一序号 13 | Lines 480–495 | 01–12 = 12 篇 ✅ |
| 十功能页 = 10 pages | Lines 595–605 | 1–10 = 10 ✅ |
| keywords ≥5; related 2–6 | Line 272 | 与 §6.4 (2–6 slug) 一致 ✅ |
| 竞品表 8 rows | Lines 637–646 | 8 竞品 ✅ |

---

## 缺失的边界情况

以下情况 skill 没有覆盖，Agent 会遇到不确定行为:

1. **用户提供的关键词匹配不到 5 种类型中的任何一种** → §2.1 路由表没有 "none of the above" 分支
2. **Phase 1 判定 MERGE 但目标 slug 尚不存在** → 只描述了 MERGE 到已有文章，未覆盖 "新建目标后再 merge" 或 "先建 target 再创作" 场景
3. **同一关键词已有文章但用户要求新角度** → Phase 1 只考虑关键词重叠，未考虑角度/时效性差异
4. **用户指定非英文 locale** → Line 17 明确 "仅英文 `blog/`"，但如果用户给了中文关键词或要求 KR 版本，Agent 应拒绝还是重定向？未说明

---

## 优先级修复清单

| 优先级 | ID | 描述 | 工作量 |
|--------|-----|------|--------|
| P0 | B1 | 定义 G1–G7 规则 | 中 |
| P0 | C1 | `templates` → `templates` 全文替换 | 小 |
| P1 | C2 | Brief 中 Search intent → Article type | 小 |
| P1 | M1 | 补全 Phase 1 快查表至 12 篇 | 中 |
| P1 | M2 | 修复悬空引用 "§博客规则" | 小 |
| P1 | M3 | 明确 "标注 verify on site" 格式 | 小 |
| P1 | M4 | 补充完整 SelfCheck 示例 | 中 |
| P2 | m1–m6 | 6 个低危修复 | 小–中 |
| P3 | 缺失边界 | 补充 4 个边界情况处理 | 中 |
