# Step 3 — 关键词 & README 注册

> **前置**：Gate 0R Pass + Brief 已定稿  
> **SSOT**：Brief **`Primary keyword`** · [`rules/article-brief.md`](./rules/article-brief.md) · 意图重叠 [`rules/outline-cross-check.md`](./rules/outline-cross-check.md) §检查项  
> **产出**：关键词表条目 + Hub `README.md` 分流说明

---

## 从 Brief 复制（不得改意图）

| 字段 | 来源 |
|------|------|
| Primary keyword（ZH / EN） | Brief 定稿 |
| Search intent | Brief |
| One-line thesis / Moat 一行 | Brief（供 README 分流） |
| 目标 URL | [`article-types.md`](./rules/article-types.md) — 新文 `/blog/{slug}` |

Step 02 已填 SERP Fit；本 Step **只登记**关键词锚点，**不重做** Research。

---

## 关键词表（按 articleType）

在对应关键词总表追加或更新 slug 行（与 Hub README 交叉引用）：

| articleType | 关键词总表（上下文仓） | Hub README |
|-------------|------------------------|------------|
| `best-ranking` · `best-ranking-legacy` | `keywords/alignify-keywords-tools.md` | [`knowledge/tools/README.md`](../../../knowledge/tools/README.md) |
| `seo-guide` | `keywords/alignify-keywords-seo.md` | [`knowledge/seo/README.md`](../../../knowledge/seo/README.md) |
| `marketing-strategy` | `keywords/alignify-keywords.md`（Marketing 段） | [`knowledge/marketing/README.md`](../../../knowledge/marketing/README.md) |
| `insights-analysis` | `keywords/alignify-keywords.md`（Insights 段） | [`knowledge/insights/README.md`](../../../knowledge/insights/README.md) |

> 若 `keywords/` 目录尚未存在，先在 Hub README 文件清单区登记 slug；总表路径以 [`knowledge/README.md`](../../../knowledge/README.md) 为准。

---

## README 条目模板

### Tools（best-ranking）

```markdown
### {slug}

**意图**：[Brief Search intent + primary keyword 一句话]

**目标 URL**：`/zh/blog/{slug}`（新文）· 存量 `/zh/tools/{slug}`

**Moat**：[Brief 一行]

**分流**：[与相邻 slug 的差异 — 读者任务 / 关键词意图]

**数据源**：`knowledge/tools/{slug}.md` 或 `knowledge/tools/{cluster}/{slug}.md`
```

### 其他类型

目标 URL 与 [`article-types.md`](./rules/article-types.md) 一致；须含 **Moat 一行** + **分流**（与相邻 slug 为何不同篇）。

按 slug 字母序插入 Hub README；**禁止**与已有条目 primary keyword 意图重叠 **>50%**（否则回到 Step 01 MERGE 或改角）。

---

## 检查

- [ ] Primary keyword / Search intent **与 Brief 逐字一致**（未静默改词）
- [ ] 关键词总表或 Hub README 已登记（见上表路径）
- [ ] 相邻 slug 意图重叠 ≤50%（同批 ≥2 篇时另过 [`outline-cross-check.md`](./rules/outline-cross-check.md)）
- [ ] 目标 URL 符合新文 `/blog/` 政策

---

## 下一步

| articleType | 下一步 |
|-------------|--------|
| `best-ranking` · `best-ranking-legacy` | [04-screenshots.md](./04-screenshots.md) |
| 其余 | [`rules/content-locale.md`](./rules/content-locale.md) Part 2（Step 05）— **跳过 Step 04** |
