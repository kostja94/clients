# QVeris Blog

Markdown 文章目录（英文），对应线上 `https://qveris.ai/blog/{slug}`。

**写作流程**：用 skill [`../skills/qveris-blog-article/SKILL.md`](../skills/qveris-blog-article/SKILL.md)；frontmatter Schema 见 skill 内 `references/frontmatter-schema.md`。

## 文件结构

- `NN-{slug}.md`：单篇文章，NN 为两位数序号；frontmatter `slug` 为裸 slug（不含 `/blog/` 与 NN 前缀）
- 必填 frontmatter：`slug` `metaTitle` `description` `author`（`QVeris Team`）`publishedAt` `updatedAt`（`readTime` 推荐）；`title` 在正文 `# H1`、`excerpt` 在正文 H1 后首段、`TL;DR` 在正文 excerpt 后 `## TL;DR` 区块（详见 skill）
- 发布节奏：一天一篇；`publishedAt` 全库唯一；新稿 = 最晚日期 +1 天

## 文章列表

| # | 文件 | slug | 类型 | 发布 date | 状态 |
|---|------|------|------|-----------|------|
| 01 | [01-stock-api-free-comparison.md](./01-stock-api-free-comparison.md) | `stock-api-free-comparison` | Comparison | 2026-07-24 | ✅ 成稿 |
| 02 | [02-real-time-stock-price-api.md](./02-real-time-stock-price-api.md) | `real-time-stock-price-api` | Comparison | 2026-07-25 | ✅ 成稿 |
| 03 | [03-alpha-vantage-pricing.md](./03-alpha-vantage-pricing.md) | `alpha-vantage-pricing` | Comparison | 2026-07-26 | ✅ 成稿 |
| 04 | [04-litellm-alternatives.md](./04-litellm-alternatives.md) | `litellm-alternatives` | Comparison | 2026-07-27 | ✅ 成稿 |
| 05 | [05-financial-news-api-benchmark.md](./05-financial-news-api-benchmark.md) | `financial-news-api-benchmark` | Field Test | 2026-07-28 | ✅ 成稿 |

> 02–05 为按 `qveris-blog-article` skill 从官网 guides 重建的英文文章（2026-08-06），均已通过 tools 三脚本回归。

**下一序号**：06

> 成稿后由人类更新本表；Skill 不自动改 README。
