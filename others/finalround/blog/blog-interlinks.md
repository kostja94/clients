# Final Round Blog 簇内链地图（11 篇）

**最后更新**：2026-08-11（新增 `whats-new-interview-copilot`；slug 去年份；与 `blog/*.md` 正文对账）

**与全站规范的关系**：内链**分层、首段/Body 条数、锚文本、`related` 写法** 以 [`../internal-external-links-checklist.md`](../technical/internal-external-links-checklist.md) 为准。本文件是 **本簇** 的：意图说明、**互链全矩阵**、逐篇对账、维护习惯。

**统计口径**：仅统计**正文**（frontmatter 之后）中，锚为 `](/blog/{slug})` 的 **blog 文内链**；`image: "/blog/images/...` 等不计入。不统计 `/{product}` 落地页，除非在「`related` 对照」中说明。

---

## 1. 为什么做互链，以及不滥链

- **发现与权重**：同主题簇以 `/blog/{slug}` 显式成网，帮助爬虫与读者理解**访谈准备 → 工具/评测 → 宏观行业** 的阅读路径。  
- **体验**：在「你接下来该读什么」处给**可预测**的下一篇，减少孤立页。  
- **原则**（与 [`internal-external-links-checklist.md`](../technical/internal-external-links-checklist.md) 一致，仅限 Final Round 站）：

  1. **只链相关意图**：不为一味凑满 10 篇而强塞；**若一句里说不通，不链**。  
  2. **避免相邻段重复**同一 `URL`；同一 URL 在全文宜按 **H2** 分散。  
  3. **`related` 与正文**应覆盖同簇核心 slug 或产品路径，避免侧栏挂名、正文无解释地链。

旧十篇在 **blog 文互链** 上已达成：**每一篇对另外 9 个 slug 均至少 1 条正文出链**（全连通），无需再为「连上」而加无关节。2026-08 新增第 11 篇 `whats-new-interview-copilot` 为更新公告，出链聚焦相关意图（见 §4 矩阵 `N` 列）。

---

## 2. 主题簇（阅读顺序的抽象）

| 子簇 | slugs | 关系 |
|------|--------|------|
| 评测 | `verve-ai-review`, `parakeet-ai-review` | 对读；与选购、行业稿交叉 |
| 宏观/季节 | `tech-layoffs-ai` | 为「为何 loop 更短、更算法化」提供语境 |
| Prep 四支柱 | `types-of-job-interviews`, `how-to-dress-for-a-job-interview`, `questions-to-ask-the-interviewer`, `how-to-answer-tell-me-about-yourself` | 形式 → 形象 → 开场 / 收束 提问的漏斗 |
| 产品三篇 | `what-is-interview-copilot`, `ai-mock-interview-guide`, `best-ai-interview-tools` | 释义 (live) → 练习 (mock) → 选购 (grid) |
| 产品更新 | `whats-new-interview-copilot` | 2026-08 桌面应用更新公告；承接新产品形态 |

`types` 的 Next steps 与多篇首段/Quick Verdict 把 **行业 + 两评测 + 四 prep 支柱 + 三产品** 接在一起；长评测稿的 Verdict/尾段会指向 **三产品 + 行业 + pillar**。`whats-new` 作为更新公告，`related` 覆盖产品三篇；上游 `types`、`what-is-interview-copilot`、`ai-mock-interview-guide` 三篇已补入链，其余旧稿按「只链相关意图」原则暂不强连。

---

## 3. 文章索引

> **文章登记 SSOT：见 [README.md](./README.md)「Published drafts」表**（File / slug / date）。本文不再重复维护；新稿发布后在 README 登记，并将本簇互链矩阵更新到 §4。

---

## 4. 出站全矩阵：from（行）→ to（列）

行 = 文内**来源**，列 = 目标 slug。`✓` 表示正文中**至少存在** one 条 `](/blog/列名)`；`✗` 表示**未连**（可按需补，非强求）；`—` = 自身。

列序：`verve` | `parakeet` | `layoffs` | `types` | `dress` | `questions` | `tell-me` | `copilot` | `mockGuide` | `bestTools` | `whatsNew`  

| from \\ to | v | p | L | t | d | q | m | 8 | 9 | 10 | N |
|------------|---|---|---|---|---|---|---|---|---|---|---|
| 01 verve | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 02 parakeet | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 03 layoffs | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 04 types | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 05 dress | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 06 questions | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✗ |
| 07 tell-me | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✗ |
| 08 copilot | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| 09 mock guide | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| 10 best tools | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✗ |
| 11 whats-new | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | — |

> **读法**：旧 10 篇在 blog slug 上仍全连通（K₁₀）；`N` 列为 2026-08 新增 `whats-new-interview-copilot`，上游 `04/08/09` 已补入链，其余旧稿按「只链相关意图」暂不强连；新文正文连 `types`、`copilot`、`mockGuide`、`bestTools` 四篇，其余保留在 `related`。

**缩写**：`L` = `tech-layoffs-ai`，`m` = `how-to-answer-tell-me-about-yourself`，`8/9/10` = 产品三篇 slug，`N` = `whats-new-interview-copilot`。

---

## 5. 正文互链与 `related` 说明（2026-08-11 起）

**约定变更**：2026-08-11 起，frontmatter **不再包含 `related`**（与 `image`、`keywords` 一并从全部成稿移除）。互链以**正文出链**为准；`related` 如需展示由 CMS 侧配置。

- 旧稿（01–10）曾用 `related` 数组承载互链集合；迁移后该字段已删除，正文出链不受影响。
- 11 `whats-new-interview-copilot`（2026-08-11 入库）：正文连 `types-of-job-interviews`、`what-is-interview-copilot`、`ai-mock-interview-guide`、`best-ai-interview-tools` 四篇；产品出链以 `/interview-copilot`、`/ai-mock-interview`、`/download`、`/coding-copilot`、`/phone-interview`、`/getting-started`、`/subscription` 为主，blog 互链按 H2 分散。

大改互链时：**先改正文**，最后更新**本文件 §4 与日期**。

---

## 6. 新文入簇检查清单

1. 在 [README.md](./README.md)「Published drafts」登记新稿。  
2. 从「上游」2–3 篇（`types`、评测、产品三篇）**自然段** 加 1 条入链（若成稿后仍主题相关）。  
3. 新文正文：按规范首段/Body/文末做互链（frontmatter 不含 `related`）。  
4. 更新 §4 矩阵新行/列（若超过 10 篇则扩展表或拆表）。

> **11 `whats-new-interview-copilot` 状态**：✅ 完成——README 登记表已增行；正文互链已完成；上游 `what-is-interview-copilot`、`ai-mock-interview-guide`、`types-of-job-interviews` 三篇各补 1 条自然入链；§4 矩阵已扩展为 11×11（`N` 列）。

---

*维护：每次批量调整 `/blog/` 内链或 `related` 后，更新**最后更新**日期，并视情况在 [`../internal-external-links-checklist.md`](../technical/internal-external-links-checklist.md)「Blog 内链现状」中写一句总述。*
