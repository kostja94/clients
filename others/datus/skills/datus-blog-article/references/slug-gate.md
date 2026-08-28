# Datus Glossary — Slug Gate

> Phase 2 加载。Gate B：6 问全 Pass + 12 反模式零触发。

---

## 1. Slug 硬规则

| 规则 | 说明 |
|------|------|
| 格式 | kebab-case ASCII |
| 长度 | 5–8 词；≤60 字符 |
| 常青 | **slug 不含年份**（`2026` 仅可进 title/filename） |
| Intent-first | 用户搜索词优先，非内部架构词 |
| 前缀 | GlossaryTerm → `what-is-*`；GlossaryComparison → `*-vs-*` |

---

## 2. Gate B — 6 问 Slug 审查

每候选 slug 逐问；任一 No → 淘汰该候选。

| # | 问题 | Pass 标准 |
|---|------|----------|
| 1 | 是否匹配 search intent？ | 用户搜此词期望定义/对比文 |
| 2 | 是否常青？ | 无年份、无版本号 |
| 3 | 是否与已有 slug 冲突？ | 对照 content-graph.md |
| 4 | 是否 intent-first？ | 非内部项目代号 |
| 5 | 是否可读？ | 朗读可理解；无连续 4+ 停用词 |
| 6 | 是否与 filename 一致？ | `NN-{slug}.md` 中段 = frontmatter slug |

---

## 3. 12 反模式（任一触发 → Fail）

| # | 反模式 | 示例 | 替代 |
|---|--------|------|------|
| 1 | 年份入 slug | `what-is-lakehouse-2026` | `what-is-lakehouse` |
| 2 | 内部架构词 | `de-glossary-framework` | `what-is-{term}` |
| 3 | 泛化 guide | `complete-guide-to-lakehouse` | `what-is-lakehouse` |
| 4 | 策略/诊断词 | `lakehouse-strategy` | intent 词 |
| 5 | 过长 | `what-is-a-lakehouse-architecture-explained` | 缩短至 5–8 词 |
| 6 | 重复 canonical | 第二篇 `what-is-semantic-layer-v2` | MERGE |
| 7 | 品牌词开头 | `datus-lakehouse` | `what-is-lakehouse` |
| 8 | 无动词对比 | `lakehouse-warehouse` | `lakehouse-vs-data-warehouse` |
| 9 | 双 vs | `etl-vs-elt-vs-elt` | 两概念对比 |
| 10 | 缩写不明 | `scd-explained`（可接受若 SERP 强） | `what-is-slowly-changing-dimensions` |
| 11 | 与 DE Agent 簇抢词 | `best-data-engineering-agents` | ArticleType → ToolsList，非 GlossaryTerm |
| 12 | forbidden slug | `data-engineering-agent-vs-claude-code` | 待稿发布后再用 |

---

## 4. 推荐 Slug 模式

| 类型 | 模式 | 示例 |
|------|------|------|
| GlossaryTerm | `what-is-{term}` | `what-is-lakehouse`, `what-is-data-contract` |
| GlossaryTerm (缩写) | `what-is-{expanded}` | `what-is-change-data-capture` |
| GlossaryComparison | `{a}-vs-{b}` | `etl-vs-elt`, `data-fabric-vs-data-mesh` |
| GlossaryComparison | `{a}-vs-{b}-architecture` | `lambda-vs-kappa-architecture` |
| GlossaryComparison | `olap-vs-oltp` | 行业惯用可省略 what-is |

---

## 5. Title 与 Slug 分工

| 字段 | 可含 2026 | 可含 em dash 副标题 | 示例 |
|------|-----------|-------------------|------|
| title | ✅ | ✅ | What Is a Lakehouse? Definition, Architecture & Open Table Formats |
| slug | ❌ | ❌ | `what-is-lakehouse` |
| filename | ✅（可选后缀） | ❌ | `30-what-is-lakehouse.md` |
