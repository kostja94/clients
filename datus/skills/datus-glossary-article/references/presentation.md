## ⚠️ 拆分说明（v2.0.0）

> **本文件仍为 Voice / 链接规范的 canonical 来源。**
> 表现节奏检查（段落、列表、碎片化、衔接率）已迁移至 `references/presentation-rhythm.md`。
> —— 2026-06-15

---

# Datus Glossary — Voice 与链接规范

> Phase 3 加载（Voice + 链接规范）。Phase 4/5 表现节奏检查用 `presentation-rhythm.md`。

---

## 1. Voice

| 维度 | 规则 |
|------|------|
| **Primary ICP** | Data Engineer / Analytics Engineer |
| **Tone** | Wirecutter 式客观 + 工程实践深度 |
| **Person** | 第二人称 sparingly；多用「teams」「organizations」 |
| **禁词** | revolutionary, game-changing, 10x（无数据）, guaranteed, only solution |
| **竞品** | 中立描述；禁 "just a chatbot"、"merely" |
| **数字** | 须有来源或 `as of {month} {year}` |

### 1.2 空泛句检测（10 项）⭐v2.0.0

出现以下模式 → 标记。超过 **3 处 → Writing & Voice 维度 ≤5/10**：

- "In today's data-driven world..."
- "In today's fast-paced..."
- "This is why...（无前文因果）"
- "Consider the following..."
- "It is important to note that..."
- "As we all know..."
- "The reality is that..."
- "Here's the thing..."
- "But that's not all..."
- "Let's dive in..."

### 1.3 Excerpt 模式（H1 下方 1–2 句）

**模式 A — 场景失败**（推荐用于 agent/AI 相关术语）：

> An analyst asks "{question}." The SQL runs. The numbers look plausible — and wrong, because {context failure}. This glossary entry explains how {term} works, where it fails, and what production-ready systems need.

**模式 B — 定义先行**（推荐用于架构/存储术语）：

> **{Term}** is {one-sentence definition}. This glossary entry explains how it works, how it compares to {related concepts}, and why it matters for {AI/data engineering}.

**模式 C — 对比方向**（GlossaryComparison 专用）：

> **{A}** and **{B}** solve different problems but are often confused. This article defines each, compares them across key dimensions, and explains why the distinction matters for {data engineering / AI agents}.

**模式 D — 产品/工具速览**（推荐用于竞品分析/工具列表类）：

> {Product} {brief origin/positioning sentence}. {What this article covers in one clause}.

---

## 2. Snippet-ready 定义句

在 §1 canonical 节内提供 **150–200 词**可独立提取的定义块，格式：

```markdown
A useful working definition:

> **{Term}** is {precise definition with scope boundaries}.
```

要求：

- 含 primary keyword
- 说明 what it is **and** what it is not
- 可单独作为 Google featured snippet 候选

TL;DR 第 1 条为压缩版（≤40 词）。

---

## 3. 内链规范

### 3.1 允许目标

| 类型 | 格式 | 限制 |
|------|------|------|
| Blog | `[anchor](/blog/{slug})` 或 Markdown link | ≥2 条 |
| Glossary | `[term](https://datus.ai/glossary)` 或 `/glossary` | ≤3 条；术语首次出现；同术语只链一次 |

### 3.2 禁止目标

- `/agent`、`/features/*`、`/use-cases/*`、`/vs/*`、`/case-studies/*`
- slug `data-engineering-agent-vs-claude-code`（文稿缺失）

### 3.3 分布

| 区域 | Blog | Glossary |
|------|------|----------|
| 开篇（第一个 `##` 前） | ≤1–2 | ≤1 |
| 正文各 `##` | 每节通常 ≤2 | 全篇 ≤3 |
| Conclusion / FAQ | 收束链 | ≤1 |

**锚文本**：描述性短语；禁 "click here"、"learn more"。

---

## 4. 外链规范

| 要求 | 说明 |
|------|------|
| **总量** | 2–5 条 |
| **格式** | `<a href="URL" rel="nofollow noopener">锚文本</a>` |
| **来源** | 竞品官方 docs、云厂商 docs、GitHub、行业标准 |
| **E-E-A-T** | dbt docs、Databricks、Snowflake、Google Cloud、Cube.dev 等 |

---

## 5. Datus 产品提及（≤15%）

**允许出现的内容**（见 product-facts.md）：

- Context Engine、Subagent、Feedback Loop（作为实现示例，非 glossary 词条）
- `/gen_semantic_model`、`/gen_metrics`、`@table`、`@metrics` 等命令
- 与术语的自然关联（如 text-to-SQL + context retrieval）

**出现位置**：

- FAQ 前「How tools implement this」或类似中立段
- 不超过 3 段
- 不写成 sole answer / 推销漏斗

**禁止**：

- 开篇即推 Datus
- "Datus is the only…"
- 将 Datus 专有术语（Context Engine）作为 glossary 词条标题

---

## 6. CTA

- **主 CTA**：GitHub repo 或 docs.datus.ai（Conclusion/FAQ 自然出现）
- **不用**未上线产品页 CTA

---

## 7. 结构与可读性

- 每 ~500 词 ≥1 具体例子（表名、metric 名、失败场景）
- 对比表：≥3 行 × ≥3 列
- FAQ 须有独立内容（非正文复制粘贴）
- 列表比例 ≤25% 全文
