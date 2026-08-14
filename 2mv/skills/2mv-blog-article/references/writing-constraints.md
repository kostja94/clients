# 2mv — Writing Constraints

> 加载时机：Phase 4（Draft 阶段全程对照）
> 主文件：SKILL.md §3 Phase 4 指针

---

## 1. Voice

### 正向

| 维度 | 要求 |
|------|------|
| Clear | 增长/社媒团队能复述核心观点 |
| Evidence-led | 量化数字有来源；病毒模式有观察基础 |
| System-building | 强调「系统/复利」而非单篇爆款 |
| Category-building | 产品首次出现前已提供独立价值（品类教育） |
| Fair comparison | 每竞品 ≥1 优势；≥1 场景非 2mv 更合适 |

### 禁止腔调

| 禁止 | 触发词 |
|------|--------|
| AI hype | revolutionary、transforming everything |
| Vendor puffery | only solution、best-in-class |
| Generic SaaS | unlock、seamless、game-changing、magic |
| Fake neutrality | 每段都推 2mv |
| Fiction openings | "Imagine you're a founder…" |
| Viral promise | guarantees viral / guaranteed views（见 §7） |

---

## 2. 引用分级（P0/P1/P2）

| 级别 | 触发条件 | 要求 | 示例 |
|------|---------|------|------|
| **P0** | 任何可在外部验证的量化声明 | 链接到原始来源。同一数字跨篇出现时每篇都要链。 | 搜索量（Semrush 数据）→ 标注来源与日期；官网自报指标（100M+ views）→ 标注为官网声称而非验证事实 |
| **P1** | 行业趋势、产品能力描述、竞品状态 | 链接到官方 docs / 官方产品页。无法链接则加限定词。 | "based on public sources"、"typically"；Feature Status 须与 product-competitors.md §1 一致 |
| **P2** | 原创框架、衍生分析 | 注明方法论基础。框架性结论是原创分析。 | "based on internal observation across reaction creator workflows" |

### 2.1 外链来源规则（2026-08-14 定标）

**只允许权威来源**，其余一律不设外链（可内联为普通文本）：
- ✅ 官方产品页 / 官方文档：`2mv.ai`（/ 与 /research）、`blaze.ai`、`arcads.ai`、`superscale.ai`、`predis.ai`、竞品官方站等
- ✅ 官方数据源 / 权威行业机构：Semrush（数据）、官方调查报告、融资新闻（PR Newswire 等）
- ❌ **营销/SEO 文章**：任何工具站的 blog/评测页/affiliate 内容 —— 一律不链，改写为普通陈述
- ❌ 自媒体/软文/affiliate 内容

**链接形式**（与其他项目文章一致）：
- 竞品官方站：HTML `<a href="URL" rel="nofollow noopener">Company Name</a>`
- 权威来源内联：markdown `[描述性锚文本](URL)`，融入句子，**不使用** `[Source: ...]` 标注形式

**无来源数字处理**：若删除营销链接导致量化 claim 无权威来源 → 弱化表述（"roughly" / "widely reported" / 去掉精确比例），不得保留无来源数字（G3）。

**内部数据声明标准格式**：`Based on internal analysis of [N] niches across [time period], [finding].`

**2mv 特有**：官网自报指标（"100M+ organic views"、"170+ brands & creators"、"10x faster"、"first agentic growth agency"）为营销原文——引用时用 `as stated on 2mv's site` 框架，不得作为已验证数据。

---

## 3. 漏斗透明度自检

| 文章类型 | 漏斗透明度接受标准 |
|---------|-------------------|
| **Research / Glossary** | 漏斗应不可见。产品仅在定义之后、FAQ 之前出现。读者在前 70% 不应识别这是 vendor blog。 |
| **Comparison** | 可接受透明漏斗——读者知道这是产品对比文。 |
| **Alternative** | 可接受透明漏斗——读者知道这是替代品对比。 |
| **Product / Scenario** | 漏斗可明显——读者意图就是了解 workflow。 |
| **Announcement** | 漏斗可透明——读者知道是产品发布内容。 |

**自检问题**：如果读者在全文前 30% 就能识别这是 vendor blog → 漏斗过于明显。

---

## 4. 段落优先起草协议

### 起草顺序（Phase 4 强制执行）

```
1. 每个 H2 下先写 1 个 ≥4 句引导段（说明本节论证目标）
2. 展开 1–2 个 ≥4 句分析段（证据、对比、含义）
3. 必要时才加表格 / 正式列表 / 编号步骤
4. 表格或列表后必须跟 ≥2 句分析段
```

### 伪列表（Pseudo-list）—— 红线

用加粗标签 + 单句重复 ≥3 次，视觉上像列表、节奏上全是短段——**自动 Fail**。

```markdown
❌ 禁止：
**Monitors viral signals.** 2mv watches 12,000+ videos a day across 500+ niches.
**Decodes winning videos.** 2mv breaks down hooks, structure, and triggers frame by frame.
**Turns patterns into playbooks.** 2mv clusters winning patterns into an executable plan.

✅ 正确：合并为 1 个 ≥4 句分析段
```

### 段落节奏

| 检查项 | 健康标准 | 红线 |
|--------|---------|------|
| 长段落（≥4 句，80–200 词） | ≥3 个 | 0 个 |
| 连续短段落（≤2 句） | ≤2 个连续 | ≥4 个连续 |
| 段落长度标准差（句数） | 能目测长短交替 | 全文所有段落长度几乎相同 |

### 列表使用

| 检查项 | 标准 |
|--------|------|
| 每个列表前 | 必须有完整前导句说明列表目的 |
| 每个列表后 | ≥2 句分析（"这意味着什么？"） |
| 无单一项列表 | 1 个 bullet 是段落，不是列表 |
| 相邻 H2 section | 不连续出现 2 个 "H2 → 列表 → 无分析 → 下一 H2" 模式 |

### 段间衔接

- 相邻段落之间至少有 1 种衔接手段：过渡词 / 句子桥 / 关键词重复 / 指代词回指
- 目标：任意连续 10 段中 ≥7 对有衔接手段
- 避免 H2 后直接跟列表（H2 → 1–2 句过渡段 → 列表）

---

## 5. BLUF 三处（Bottom-Line Up Front）

| # | 位置 | Pass 标准 |
|---|------|----------|
| B1 | TL;DR 下 | 40–60 词直接回答 primary keyword |
| B2 | 每个 major H2 首段 | 先答后铺背景 |
| B3 | FAQ 每问 | 首句即答；与正文非复制（相似度 <30%） |

---

## 6. 模块顺序（正文）

```
YAML frontmatter
→ ## TL;DR（3-5 bullet；bullet 1 为 snippet 定义句 40-60 词）
→ 编号 H2 正文
→ ## N. Conclusion
→ ## FAQ（≥3 题；≥1 题覆盖边界/异议）
```

---

## 7. 夸大承诺写作约束（2mv 特有）

| 规则 | 执行 |
|------|------|
| 涉及病毒/增长话题 | 禁止病毒/播放量承诺（见 product-competitors.md §6 Claims 禁令） |
| 禁 G8 句式 | guarantees viral / guaranteed views / "post this and go viral" / "first agentic growth agency"（无证据时） |
| 手法描述 | 五引擎闭环、逐帧解码、模式聚类、playbook 输出可作机制描述教育，不承诺病毒结果 |
| 数据来源 | 引用官网 self-reported 指标时给 `as stated on 2mv's site` 标注 |

---

## 8. 竞品公平描述

| 规则 | 执行 |
|------|------|
| 每竞品 ≥1 明确优势 | 从 `product-competitors.md` 优势列取 |
| 禁贬低性措辞 | "just" / "merely" / "only does X" |
| Agency vs Tool / Organic vs Paid | 客观呈现两条路线，不做路线霸权 |
| ≥1 场景非 2mv 更合适 | 写在正文，非脚注（例：需要付费广告素材规模化的团队更适合 Arcads/Superscale） |
| 竞品外链 | HTML `rel="nofollow noopener"` |

---

*writing-constraints · v1.0.0 · 2026-08-14 · 2mv 定制*
