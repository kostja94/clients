# Final Round AI blog drafts

English Markdown articles for **Final Round AI** live in this folder (`*.md` with YAML frontmatter), aligned with the public URL pattern **`/blog/{slug}`**.

**本文档是文章登记 SSOT**（发布后在此表增行）。其余规范归属：
- **frontmatter 字段 / slug 规则** → [finalround-blog-article skill → article-types.md](../skills/finalround-blog-article/references/article-types.md) §4–§5
- **Blog 创作全流程（7 类路由、Gate、SelfCheck、F 红线）** → [finalround-blog-article skill](../skills/finalround-blog-article/SKILL.md)
- **Review 程序化生成** → skill `references/review-programmatic.md`
- **Blog 簇内链地图**（互链矩阵、`related` 对账、新文入簇）→ [blog-interlinks.md](./blog-interlinks.md)（互链 SSOT）
- **全站内链规则 + 外链 + 审计表** → [internal-external-links-checklist.md](../technical/internal-external-links-checklist.md)
- **Blog 内容策略（SEMrush、选题、日历）** → [finalround-blog.md](./finalround-blog.md)

---

## When adding a new post

1. 新建 `NN-{slug-kebab}-2026.md`（NN 见 [skill content-graph](../skills/finalround-blog-article/references/content-graph.md)；frontmatter 字段与 slug 规则见 [skill article-types.md](../skills/finalround-blog-article/references/article-types.md)）。
2. Ensure **`slug`** matches the path segment: `/blog/{slug}`（常青 slug 一般**不含**年份，与本目录已发布成稿一致）。
3. 按 [internal-external-links-checklist.md](../technical/internal-external-links-checklist.md) 做内链/外链；每改 Blog 互链或 `related` 后，更新 [blog-interlinks.md](./blog-interlinks.md) 的日期与对账。
4. Register the topic in [finalround-blog.md](./finalround-blog.md) 文章清单（如适用）；发布后核对 sitemap 与产品页互链。

---

## Published drafts in this folder

| File | slug | `date` (publish) |
|------|------|------------------|
| [01-verve-ai-review-2026.md](./01-verve-ai-review-2026.md) | `verve-ai-review` | 2026-03-16 |
| [02-parakeet-ai-review-2026.md](./02-parakeet-ai-review-2026.md) | `parakeet-ai-review` | 2026-03-16 |
| [03-tech-layoffs-ai.md](./03-tech-layoffs-ai.md) | `tech-layoffs-ai` | 2026-04-17 |
| [04-types-of-job-interviews-2026.md](./04-types-of-job-interviews-2026.md) | `types-of-job-interviews` | 2026-04-23 |
| [05-how-to-dress-for-a-job-interview-2026.md](./05-how-to-dress-for-a-job-interview-2026.md) | `how-to-dress-for-a-job-interview` | 2026-04-24 |
| [06-questions-to-ask-the-interviewer-2026.md](./06-questions-to-ask-the-interviewer-2026.md) | `questions-to-ask-the-interviewer` | 2026-04-25 |
| [07-how-to-answer-tell-me-about-yourself-2026.md](./07-how-to-answer-tell-me-about-yourself-2026.md) | `how-to-answer-tell-me-about-yourself` | 2026-04-26 |
| [08-what-is-interview-copilot-2026.md](./08-what-is-interview-copilot-2026.md) | `what-is-interview-copilot` | 2026-04-27 |
| [09-ai-mock-interview-guide-2026.md](./09-ai-mock-interview-guide-2026.md) | `ai-mock-interview-guide` | 2026-04-28 |
| [10-best-ai-interview-tools.md](./10-best-ai-interview-tools.md) | `best-ai-interview-tools` | 2026-04-29 |
| [11-whats-new-interview-copilot-2026.md](./11-whats-new-interview-copilot-2026.md) | `whats-new-interview-copilot` | 2026-08-11 |

---

*新稿发布后在本表增行；内链与 `related` 维护见 [blog-interlinks.md](./blog-interlinks.md)。*
