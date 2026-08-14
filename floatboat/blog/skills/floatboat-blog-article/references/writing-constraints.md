# Floatboat Writing Constraints — Voice, Citations, Funnel, Fragmentation

> 加载时机：Phase 4（Outline 阶段参考）· Phase 5（Draft 全程对照）
> 主文件：SKILL.md §3 Phase 5 指针

---

## 1. Voice

### 正向

| 维度 | 要求 |
|------|------|
| Clear | 非专业读者能复述核心观点 |
| Evidence-led | 强判断有依据或限定（likely / emerging / as of June 2026） |
| Practitioner-grade | 有具体对象：meeting brief、ICS feed、client call、deadline |
| Calm but opinionated | ≥1 处承认非自有方案更适合的场景 |
| Category-building | 产品首次出现前已提供独立价值 |

### 禁止腔调

| 禁止 | 触发词 |
|------|--------|
| AI hype | revolutionary, transforming everything |
| Vendor puffery | only solution, best-in-class |
| Generic SaaS | unlock, seamless, game-changing, magic |
| Fake neutrality | 每段都推 Floatboat |
| Academic fog | 连续抽象定义无具体对象 |

---

## 2. 引用分级（P0/P1/P2）

| 级别 | 触发条件 | 要求 | 示例 |
|------|---------|------|------|
| **P0 — 必须引用链接** | 任何可在外部数据源验证的量化声明 | 链接到原始来源（官方报告、官方文档、一手数据页）。同一数字跨篇出现时每篇都要链。 | 竞品定价、"3500+ integrations"、benchmark 分数 |
| **P1 — 应当引用** | 行业趋势、产品能力描述、竞品状态 | 链接到官方 docs / GitHub / Changelog。如无法链接则加限定词（"based on"、"typically"、"as of June 2026"）。 | "Calendar-Driven AI is an emerging paradigm as of mid-2026" |
| **P2 — 可不引用** | 作者自己测试/观察得出的 benchmark、原创框架、从已引用数据衍生的分析 | 注明方法论基础或标注 "internal observation, n=X"。框架性结论（如"四代演进框架"）是原创分析。 | "Based on internal testing across 20+ calendar workflows in Q2 2026" |

**内部数据声明标准格式**：`Based on internal analysis of [N] [data type] across [time period], [finding].`

---

## 3. 漏斗透明度自检

**检测方法**：提取文章叙事弧——开头（教育/问题陈述）→ 中部（中立概述）→ 转折点（"but" / "however"）→ Floatboat 作为答案。

| 文章类型 | 漏斗透明度接受标准 |
|---------|-------------------|
| **Research / Glossary** | 漏斗应不可见。产品仅在定义之后、FAQ 之前出现，≤3 段。读者在全文前 70% 不应识别这是 vendor blog。 |
| **Comparison** | 可接受透明漏斗——读者知道这是产品对比文。 |
| **Alternative** | 可接受透明漏斗——读者知道这是替代品对比。 |
| **Product / Scenario** | 漏斗可明显——读者意图就是了解 workflow。 |
| **Product Announcement** | 漏斗可透明——读者知道是品牌/产品发布内容。 |

**自检问题**：如果读者在全文前 30% 就能识别这是 vendor blog → 漏斗过于明显。

---

## 4. 碎片化防护规则

### 段落优先起草协议（Phase 5 强制执行）

**问题背景**：规则若只写在 Phase 6 SelfCheck，Agent 会按 Outline 的 H2/步骤结构直接产出短句簇，再在自检时「标记 Pass」——08 稿即此模式。

**起草顺序**（不可颠倒）：

```
1. 每个 H2 下先写 1 个 ≥4 句引导段（说明本节论证目标）
2. 展开 1–2 个 ≥4 句分析段（证据、对比、含义）
3. 必要时才加表格 / 正式列表 / 编号步骤
4. 表格或列表后必须跟 ≥2 句分析段
```

**伪列表（Pseudo-list）— 红线，等同列表轰炸 Fail**

用加粗标签 + 单句重复 ≥3 次，视觉上像列表、节奏上全是短段：

```markdown
❌ 禁止（08-claude-cowork-alternative §3.3 反例）：
**Meeting prep without panic.** Floatboat's pipeline runs before Zoom.
**Follow-up that survives.** Calendar-triggered follow-up targets drop-off.
**Multi-model subtasks.** Product docs include Claude without API keys.

✅ 正确：合并为 1 个 ≥4 句分析段，段内用过渡词串联各论点；若需扫读，再用正式 bullet（带前导句 + 段后分析）
```

同类禁止模式：

| 模式 | 示例 | 修复 |
|------|------|------|
| 逐步骤单句 | `**Step 1 — Audit.**` + 1 句 × 4 | 1 个 ≥4 句段落叙述迁移逻辑；步骤仅作段内枚举 |
| 场景标签簇 | `**You run open-source.**` + 1 句 × N | 1–2 个分析段，场景作段内从句 |
| H3 下全短段 | §1.1 连续 6 个 1–2 句段 | 合并为 2 个 ≥4 句段 |

**参考成稿**：`06-ai-meeting-preparation.md`、`05-best-ai-scheduling-assistants.md`（长段优先）；**反面教材**：`08-claude-cowork-alternative.md` §1.1、§3.3、§4、§5。

### 段落节奏

| 检查项 | 健康标准 | 红线 |
|--------|---------|------|
| 长段落（≥4 句，80–200 词） | ≥3 个 | 0 个 |
| 连续短段落（≤2 句） | ≤2 个连续 | ≥4 个连续 |
| 段落长度标准差（句数） | 能目测长短交替 | 全文所有段落长度几乎相同 |
| 每节叙事重量 | 每 H2 section 至少 1 个 ≥3 句段落 | 3+ 节全是短段落 |

### 列表使用

| 检查项 | 标准 |
|--------|------|
| 每个列表前 | 必须有完整前导句说明列表目的 |
| 每个列表后 | ≥2 句分析（"这意味着什么？"） |
| 无单一项列表 | 1 个 bullet 是段落，不是列表 |
| 相邻 H2 section | 不连续出现 2 个 "H2 → 列表 → 无分析 → 下一 H2" 模式 |
| 列表项不超过 7 条 | 超过则考虑拆分为子标题 + 段落 |

### 段间衔接

- 相邻段落之间至少有 1 种衔接手段：过渡词（"however"/"specifically"）/ 句子桥 / 关键词重复 / 指代词回指
- 目标：任意连续 10 段中 ≥7 对有衔接手段
- 避免 H2 后直接跟列表（H2 → 1–2 句过渡段 → 列表）

---

## 5. 事实与合规速查

| 规则 | 执行 |
|------|------|
| 量化 claim | 必须 `[Source: URL]` 或脚注；无来源则删或改定性表述 |
| 竞品能力 | 基于官网/docs；每竞品 ≥1 优势 |
| 竞品措辞 | 禁 just a / merely / only does X |
| 产品能力 | 不超出 GA 或已文档化能力；「以现网 docs 为准」 |
| 品牌风险 | 禁「全球首个」；禁称竞品 dead/failed |
| 商标 | Slack/Discord/微信仅旁白类比，不作 title 主体或 SEO 锚文本 |
| AI 视觉 | 若提及 AI 生成图，需标注 |

### 选择性遗漏（Comparison / Alternative 必检）

品类全景或对比表不得遗漏目标读者可能知道的关键玩家。只列部分竞品时，正文须说明选择标准。

| 文章类型 | 最低覆盖 |
|---------|---------|
| Comparison（Scheduling 簇） | Calendly/Motion 等 Gen 1–2 代表 + 至少 1 个 Chat-Based（ChatGPT/Claude）+ Floatboat 同代竞品 |
| Alternative | 目标竞品完整描述 + ≥1 个「仍选竞品」场景 |

遗漏 P0 竞品（如 Claude Cowork alternative 文未覆盖 Cowork）→ Gate C Fail。

### 对比表二元化（Comparison / Alternative 必检）

禁止把复杂能力压成误导性 Yes/No。需要人工审核、半自动或场景依赖的能力，cell 须写清边界，或表下加脚注说明简化范围。

---

## 6. 内链规则

- 正文 `/blog/{slug}` ≥2
- canonical 概念：1–2 句 + link，不在此篇完整重定义
- 锚文本描述性（非 click here）
- 站外 2–5，`rel="nofollow noopener"`
- Alternative 类必须链 Pillar Hub

---

## 7. 模块顺序（正文）

```
YAML frontmatter
→ ## TL;DR（3-5 bullet，第一个 bullet 为 snippet 定义句）
→ 编号 H2 正文
→ ## Conclusion
→ ## FAQ
```

---

## 8. 日期发布约束

> 来源：§1B 日期发布策略

| 约束 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章，不准集中在同一天 |
| **publishDate** | 首次发布日设定后慎重更改；仅在未上线阶段可调整 |
| **错开方向** | 成批文章从锚点日往前逐日分配，重要文章靠前 |
| **避让** | 已有文章的 publishDate 不重复使用 |
