# Sparki — Writing Constraints

> 加载时机：Phase 4（Draft 阶段全程对照）
> 主文件：SKILL.md §3 Phase 4 指针

---

## 1. Voice

### 正向

| 维度 | 要求 |
|------|------|
| Clear | 目标创作者能复述核心 workflow / 结论 |
| Practitioner-first | 像真的做过这类剪辑的人在讲步骤与取舍 |
| Evidence-led | 素材级观察（CreatorClone）与量化数字有来源 |
| Category-building | 先讲清范式/工作流价值，产品出现前正文已自足 |
| Fair comparison | 每竞品 ≥1 优势；≥1 场景非 Sparki 更合适 |

### 禁止腔调

| 禁止 | 触发词/示例 |
|------|------------|
| AI hype | revolutionary、transforming everything、next-gen magic |
| Vendor puffery | only solution、best-in-class |
| Generic SaaS | unlock、seamless、game-changing、cutting-edge |
| Fake neutrality | 每段都推 Sparki |
| Fiction openings | "Imagine you're a creator who…" |
| 红人臆测 | "she clearly edits with X"（除非素材证实） |

---

## 2. 引用分级（P0/P1/P2）

| 级别 | 触发条件 | 要求 | 示例 |
|------|---------|------|------|
| **P0** | 任何可在外部验证的量化声明 | 链接原始来源或标注官网能力声明 | "95% transcription accuracy" → 标注 "per Sparki's AI Caption page" |
| **P1** | 行业趋势、产品能力描述、竞品状态 | 链接官方页 / Changelog；无法链接加限定词 | "as of September 2026"、"typically" |
| **P2** | 原创框架、素材级拆解观察 | 注明观察来源（哪个公开视频/时间点） | "Across the 5 most recent uploads, cuts land every 1.2s on average" |

**CreatorClone 素材声明标准格式**：`Based on {creator}'s recent uploads (linked above), the edit uses …`

---

## 3. 漏斗透明度自检

| 文章类型 | 漏斗透明度接受标准 |
|---------|-------------------|
| **CreatorClone** | 漏斗不可见：先纯手法拆解（前 60–70%），Sparki 仅在"如何复现"段落出现；产品 ≤20% |
| **CategoryPOV** | 漏斗不可见；产品在论点成立后、FAQ 前出现；≤25% |
| **Comparison / AlternativeRoundup** | 可接受透明——读者知道是选型文 |
| **WorkflowHowTo / FeatureGuide** | 可明显——读者意图即工作流 |
| **Announcement** | 透明——产品发布 |

**自检**：若读者在前 30% 就识别这是 vendor blog → 漏斗过于明显。

---

## 4. 段落优先起草协议

```
1. 每个 H2 下先写 1 个 ≥4 句引导段（本节论证目标）
2. 展开 1–2 个 ≥4 句分析段（证据、对比、含义）
3. 必要时才加表格 / 列表 / 编号步骤
4. 表格/列表后必须跟 ≥2 句分析段
```

**伪列表（红线）**：加粗标签 + 单句重复 ≥3 次 → 自动 Fail。

**段落节奏**：长段（≥4 句，80–200 词）≥3；连续短段 ≤2；长短交替。

**列表使用**：每个列表有前导句；列表后 ≥2 句分析；无单一项列表；相邻 H2 不连续 "H2 → 列表 → 无分析"。

**段间衔接**：任意连续 10 段 ≥7 对有衔接手段；H2 后不直接跟列表。

---

## 5. BLUF 三处

| # | 位置 | Pass 标准 |
|---|------|----------|
| B1 | TL;DR | 40–110 词长描述 + 3–5 bullets；bullet 1 为 snippet 定义句 |
| B2 | 每个 major H2 首段 | 先答后铺背景 |
| B3 | FAQ 每问 | 首句即答；与正文非复制 |

---

## 6. 模块顺序（正文）

```
YAML frontmatter
→ ## TL;DR（3–5 bullets + 长描述 40–110 词）
→ 编号 H2 正文
→ ## N. Conclusion
→ ## FAQ（3–6 题；≥1 题覆盖边界/异议）
```

无 `## Related articles` 模块（与既有 61 篇一致）。

---

## 7. 竞品公平描述

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势 | 从 `product-competitors.md` §2 优势列取 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" |
| ≥1 场景非 Sparki 更合适 | 写在正文，非脚注 |
| 竞品外链 | HTML `rel="nofollow noopener"` |

---

## 8. CreatorClone 专项约束

- 每个"手法断言"须对应公开素材证据（R3 已抓），正文标 creator 名 + 视频位置
- 产品出现节奏：先"如何徒手复现"→ 再"AI 如何提速"→ 最后 Sparki 一句定位
- 不写未证实的 creator 工具/动机；不暗示合作
- 结尾给可执行清单（不是"去模仿"的空话，而是切点/转场/字幕可抄项）

---

*writing-constraints · sparki v1.0.0 · 2026-09-04*
