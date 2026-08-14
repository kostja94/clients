# FinalRound Content Graph（Skill reference）

> **Skill 创作速查**：NN 序号 + 文章类型 + 日期占用 + Canonical Registry。
> **SSOT**：文章登记（File/slug/date）→ `blog/README.md`；互链矩阵 → `blog/blog-interlinks.md`。**本文件不再重复维护 File/slug/date**——slug 由文件名 `NN-{slug}.md` 推导，日期查 README。

---

## 1. NN → slug → 类型 → category 映射

> slug = 文件名去掉 `NN-` 前缀与 `-2026` 年份后缀；发布日查 `blog/README.md` 登记表。`category` 三选一（Product | Comparison | Research），写入 frontmatter。

| NN | slug | 类型 | category |
|----|------|------|----------|
| 01 | verve-ai-review | Review | Comparison |
| 02 | parakeet-ai-review | Review | Comparison |
| 03 | tech-layoffs-ai | Industry | Research |
| 04 | types-of-job-interviews | ResearchDefinition | Research |
| 05 | how-to-dress-for-a-job-interview | InterviewPrep | Product |
| 06 | questions-to-ask-the-interviewer | InterviewPrep | Product |
| 07 | how-to-answer-tell-me-about-yourself | InterviewPrep | Product |
| 08 | what-is-interview-copilot | ResearchDefinition | Research |
| 09 | ai-mock-interview-guide | InterviewPrep | Product |
| 10 | best-ai-interview-tools | CommercialRoundup | Comparison |
| 11 | whats-new-interview-copilot | Announcement | Product |

**下一篇 NN：12**

---

## 2. 主题簇

| 子簇 | slugs | 关系 |
|------|--------|------|
| 评测 | verve-ai-review, parakeet-ai-review | 对读；与选购、行业稿交叉 |
| 宏观/季节 | tech-layoffs-ai | 为「为何 loop 更短、更算法化」提供语境 |
| Prep 四支柱 | types-of-job-interviews, how-to-dress-for-a-job-interview, questions-to-ask-the-interviewer, how-to-answer-tell-me-about-yourself | 形式 → 形象 → 开场 / 收束 提问的漏斗 |
| 产品三篇 | what-is-interview-copilot, ai-mock-interview-guide, best-ai-interview-tools | 释义 (live) → 练习 (mock) → 选购 (grid) |
| 产品更新 | whats-new-interview-copilot | 2026-08 桌面应用更新公告 |

---

## 3. Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| Interview Copilot 是什么 | what-is-interview-copilot | 1–2 句 + link；不重复完整定义 |
| 面试准备练习循环 | ai-mock-interview-guide | 同上 |
| 面试类型全景 | types-of-job-interviews | 同上 |
| AI 面试工具选型 | best-ai-interview-tools | Commercial 入口 |
| 桌面应用更新 | whats-new-interview-copilot | 产品形态变化引用入口 |
| Tell me about yourself | how-to-answer-tell-me-about-yourself | 开场题 canonical |
| 面试提问 | questions-to-ask-the-interviewer | 收束题 canonical |
| 面试着装 | how-to-dress-for-a-job-interview | 形象 canonical |
| 裁员与 AI | tech-layoffs-ai | 宏观 canonical |

---

## 4. 日期占用表（创作分配日期用）

| 日期 | slug |
|------|------|
| 2026-03-16 | verve-ai-review, parakeet-ai-review |
| 2026-04-17 | tech-layoffs-ai |
| 2026-04-23 | types-of-job-interviews |
| 2026-04-24 | how-to-dress-for-a-job-interview |
| 2026-04-25 | questions-to-ask-the-interviewer |
| 2026-04-26 | how-to-answer-tell-me-about-yourself |
| 2026-04-27 | what-is-interview-copilot |
| 2026-04-28 | ai-mock-interview-guide |
| 2026-04-29 | best-ai-interview-tools |
| 2026-08-11 | whats-new-interview-copilot |

**新稿日期**：一天一篇，从锚点日往前排；避开上表已占用日。

---

## 5. 互链现状摘要

- 旧 10 篇在 blog slug 上全连通（每篇对另外 9 个 slug 至少 1 条正文出链）
- 11 `whats-new-interview-copilot`：正文连 `types-of-job-interviews`、`what-is-interview-copilot`、`ai-mock-interview-guide`、`best-ai-interview-tools` 四篇（2026-08-11 起 frontmatter 不再含 `related`，互链以正文为准）
- 新文入簇后需更新 `blog/blog-interlinks.md` §4/§5 + `blog/README.md` 登记表

---

*content-graph · FinalRound · v1.0.1 · 文章登记 SSOT = blog/README.md；互链 SSOT = blog/blog-interlinks.md*
