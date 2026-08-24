# Step 2 — Research（Gate 0R）

> **定位**：写作前的素材梳理与竞争分析。确保所有论断有来源、数据可追溯、信息增量可论证。未通过 Research Gate 不进入写作阶段。
> **产出**：Research Log + Synthesis Statement + Candidate Examples + SERP Fit 确认
> **引用**：clients `blog-create/06-research.md` 的 Research 三角方法论

---

## Gate 0R：Research 通过条件

- [ ] R1 素材梳理完成（知识块全部内容已审阅）
- [ ] R2 SERP 搜索完成（至少分析了 Top 3-5 ranking pages）
- [ ] R3 至少 3 个 URL 原文 Fetch 完成
- [ ] Synthesis Statement 已产出（80-150 字洞察合成）
- [ ] Candidate Examples ≥5 个（含数据来源）
- [ ] SERP Fit 确认与现有内容的差异化空间

---

## R1：知识块 SSOT 素材梳理

### 操作

1. **完整阅读知识块**：逐节审阅，标记所有事实性论断、数据、引用
2. **提取素材清单**：

```markdown
| # | 素材类型 | 内容摘要 | 需验证 | 来源 |
|---|---------|---------|--------|------|
| 1 | 数据     | ...     | Yes    | 知识块外链 #3 |
| 2 | 案例     | ...     | Yes    | 知识块深度分析章节 |
| 3 | 概念定义 | ...     | No     | — |
```

3. **标记缺口**：哪些论断在知识块中有但没有引用来源？哪些需要 R3 Fetch 补充？

---

## R2：SERP 搜索

### 搜索策略

对以下目标 prompt 在 Google / ChatGPT / Perplexity 中搜索：

- `[核心关键词] 2026`
- `[核心关键词] guide / 指南`
- `[核心关键词] best tools / 最佳工具`
- `[核心关键词] comparison / 对比`

### SERP 分析表

```markdown
| 排名 | URL / 来源 | 类型 | 覆盖角度 | 我们的差异化空间 | 可参考的结构/数据 |
|------|-----------|------|---------|---------------|-----------------|
| 1 | ...        | 榜单 | ...     | →             | → |
| 2 | ...        | 教程 | ...     | →             | → |
| 3 | ...        | 产品页 | ...   | →             | → |
```

### 差异化确认

至少写出 **1 个** 我们文章独有的信息增量（Moat Asset）：

- 「SERP 上目前无人覆盖 ________」
- 「我们有一手数据/案例 ________ 可作为独有差异化」
- 「我们可以补充 ________（角度/对比维度/分析框架）」

---

## R3：URL 原文 Fetch

### 操作

对 R1 和 R2 中标记需要验证的来源 URL，使用浏览器的 `WebFetch` 或 MCP browse 工具获取原文。

### Research Log 模板

```markdown
## Research Log — {slug}

### R1 — SSOT 素材

| # | 来源 | 关键发现 | Confidence |
|---|------|---------|-----------|
| 1 | knowledge/tools/xxx.md | ... | High |
| 2 | ... | ... | Medium |

### R2 — SERP 分析

| # | Query | Top Result | 差异化空间 |
|---|-------|-----------|-----------|
| 1 | ... | ... | → |

### R3 — URL Fetch

| # | URL | 关键数据 | 文章中使用位置 | Confidence |
|---|-----|---------|-------------|-----------|
| 1 | ... | ... | Section 2 | High |
| 2 | ... | ... | bestTools product #3 | Medium |

### Synthesis Statement

[80-150 字：本文的核心差异化是什么？读者读完能获得什么独特价值？]

### Candidate Examples

| # | 示例/案例 | 用于哪个 section | 数据要点 |
|---|----------|---------------|---------|
| 1 | ... | useCases #1 | ... |
| 2 | ... | bestTools description | ... |
```

---

## SERP Fit 检查表（精简版）

- [ ] 文章主题在 SERP 上有明确的搜索需求（非零搜索量 niche）
- [ ] Top 3-5 ranking pages 的最佳实践的共性已理解
- [ ] 本文的信息增量已可清晰表述
- [ ] 不会与 Alignify 已有的其他文章产生 cannibalization
- [ ] Slug 符合 SEO 最佳实践（不与搜索词完全重复、不含年份、不含数量）

---

## 输出清单

- [ ] Research Log 完整填写
- [ ] Synthesis Statement 已产出
- [ ] Candidate Examples ≥5 个
- [ ] SERP Fit 通过
- [ ] 所有 R1 标记「需验证」的论断都已完成 R3 Fetch

---

*02-research.md · v1.0 · 2026-07-16*
