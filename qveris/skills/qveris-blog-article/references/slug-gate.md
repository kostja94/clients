# §13 Slug 设计审查

## 7 原则

1. **裸 slug**：frontmatter `slug` 不含 `/blog/` 前缀、不含 NN 序号（文件名才带）
2. **kebab-case**：小写字母 + 连字符（`stock-api-free-comparison`）
3. **常青**：不含年份、不含"2026"（标题可含展示年份，slug 不行）
4. **语义化**：从关键词提炼，读者看到 slug 即知主题
5. **短**：理想 ≤5 词；过长截断关键词，不加停用词
6. **无内部架构词**：不含 guide/how-to/analysis/strategy/diagnosis/framework 等内部类型词
7. **无品牌冗余**：不用 `qveris-` 前缀（官网博客已含大量 `qveris-*`，仅当品牌本身就是搜索词时可用）

## 12 反模式（命中任一 → 重选）

| # | 反模式 | 反例 | 正例 |
|---|--------|------|------|
| 1 | 含年份 | `best-stock-api-2026` | `stock-api-free-comparison` |
| 2 | 含 `/blog/` | `blog/stock-api` | `stock-api` |
| 3 | 含内部类型词 | `stock-api-comparison-guide` | `stock-api-comparison` |
| 4 | 连字符滥用 | `free--stock-api` | `free-stock-api` |
| 5 | 大小写混合 | `Stock-Api` | `stock-api` |
| 6 | 停用词冗余 | `the-best-of-stock-apis` | `best-stock-apis` |
| 7 | 与官网已发 slug 重复 | `mcp-qveris`（已存在） | 换角度 |
| 8 | 与本地已发 slug 重复 | `stock-api-free-comparison`（01 已用） | 换角度 |
| 9 | 歧义/多义 | `markets`（太泛） | `a-share-realtime-quotes-agent` |
| 10 | 动词 + 品牌冗余 | `qveris-qveris-setup` | `qveris-in-cursor` |
| 11 | 中文/非 ASCII | `股票-api` | `a-share-stock-api` |
| 12 | 超过 8 词 | `free-stock-market-data-apis-for-ai-agents-comparison` | `stock-api-free-comparison` |

## Design-Time 6 问（Gate B 硬性）

1. Slug 是否精确反映 primary keyword 的搜索意图？
2. Slug 是否与官网/本地已发 slug 重复或高度重叠？（对照 `content-graph.md`）
3. Slug 是否常青（3 年后仍成立）？
4. Slug 是否简短可读（无缩写歧义）？
5. 竞品 SERP Top 5 的 URL 结构是否与我们的不同且更优？（避免雷同）
6. 是否存在两个候选语义相近导致将来 cannibalization？

**Gate B**：6 问全 Pass + 0 反模式 → 定 slug。否则重选。**禁止 Flag 过关。**

## 竞品基准检查

搜 Google `{primary keyword}` → 打开前 5 结果 → 记录其 URL slug 结构 → 对比我们的候选：
- 若前 5 全部用长尾名词短语 → 我们也用名词短语
- 若前 5 存在强势 listicle（`N best …`）→ 评估是否值得竞争或换长尾
