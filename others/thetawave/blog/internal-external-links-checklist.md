# Internal & External Links 最佳实践 Checklist（ThetaWave Blog）

> **依据**：与 [Nori blog](../../nori/blog/INTERNAL-EXTERNAL-LINKS-CHECKLIST.md)、[Lessie blog](../../others/lessie/blog/INTERNAL-EXTERNAL-LINKS-CHECKLIST.md) 同一思路；站点以 **thetawave.ai** 为准；正文为 **英文**，本规范为 **中文**。  
> **产品语境**：[thetawave.md](../thetawave.md) · **功能 URL**：[thetawave-features.md](../thetawave-features.md)  
> **组件与内链策略（v1.0）**：[thetawave-blog-components-spec.md](../thetawave-blog-components-spec.md) — **废弃文末 Related Reading**；内链改为正文上下文分布。

---

## 链接分层（ThetaWave）

| 类型 | 路径 / URL | 用途 |
|------|------------|------|
| **Blog 互链** | `/blog/{slug}` | 相关主题文章；**不要**用裸域名拼文章 URL |
| **核心转化** | `https://thetawave.ai/auth/signup` | 注册 / 试用 CTA |
| **Notes Generator（意图 B）** | `https://thetawave.ai/feature/notes-generator` | 「从素材生成笔记」主落地 |
| **AI Note Taker（意图 A）** | `https://thetawave.ai/` | 实时记录 / 讲座捕获（首页承载） |
| **输入向功能页** | `/feature/lecture-to-notes`、`/feature/youtube-to-notes`、`/feature/pdf-to-notes` | 与稿内主题强相关时再链 |
| **输出向功能页** | `/feature/flashcard-maker`、`/feature/quiz-maker`、`/feature/mind-map-maker`、`/feature/podcast-generator`、`/feature/infographics-generator` | 复习 / 输出格式向稿件 |
| **对比与信任** | `/thetawave-vs-chatgpt`（若已上线） | ChatGPT 替代、学生向选型 |
| **Use Cases** | `/for-stem-students`、`/for-graduate-students`、`/exam-prep` 等 | 见 [thetawave-use-cases.md](../thetawave-use-cases.md)，**有对应页再链** |
| **Chrome 扩展** | [Chrome Web Store — Thetawave Quick Notes](https://chromewebstore.google.com/detail/thetawave-quick-notes/eihlofmfpienfpoldbfbdjbilfccgcjg) | 网页 / YouTube 一键笔记；按需 nofollow 策略与法务一致即可 |
| **作者页** | `/blog/author/kostja`、`/blog/author/thetawave-team` | Blog byline 可点击；Person schema |

---

## Internal Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **Introduction 首段** | ≥1 条 | 相关 **`/blog/{slug}`** 或核心功能页 |
| **Body Blog 互链** | 每篇 **1–4 条** | 仅链至 **`/blog/{slug}`**；分布在正文 H2 内（**非**文末 Related 列表） |
| **Body Feature / Use Case** | 0–2 条 | 与主题强相关的 `/feature/*` 或 `/use-case/*` |
| **FAQ 答案内链** | 0–2 条 | 可选；描述性锚文本 |
| **Final CTA** | 可选 | 站点级组件；**不再**使用 frontmatter `final_cta`（见 [blog-article SKILL](../skills/blog-article/SKILL.md) §2.9） |
| **产品 / 转化内链** | 按节分布 | signup、feature 分散在不同 **H2**，各 **至多 1 次**；避免堆砌 |
| ~~**文末 Related**~~ | — | **已废弃**（2026-06-22） |
| ~~**frontmatter `related`**~~ | — | **已废弃** |
| **锚文本** | 描述性 | 避免 "click here"、"learn more" |

---

## External Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **权威 / 行业** | **2–8 条**（视篇幅） | 教育统计、认知科学、可核对数据：大学官网、政府教育统计、知名期刊/媒体 |
| **竞品 / 对比对象** | 对比稿必备 | HTML：`<a href="https://…" rel="nofollow noopener">Name</a>`；锚文本用**公司名或产品定位** |
| **E-E-A-T** | 可核对来源 | 数据注明出处；避免不可验证的夸张宣称 |

**竞品与素材索引**：[thetawave-competitors.md](../thetawave-competitors.md)

---

## 文章链接状态（占位）

新稿入库后在 [`readme.md`](./readme.md) 登记表补充一行，并在下表记录内链 / 外链优化状态。

| # | 文章（slug 或标题） | 内链 Introduction | 内链 Body | Feature 内链 | 外链 | 已优化 |
|---|---------------------|:------------:|:---------:|:------------:|------|--------|
| 01 | best-ai-note-takers | 1 | 2 blog | 2 feature | 8 | ✅ 2026-05-12 |
| 02 | quizlet-alternatives | 1 | 1 blog | 2 feature | 6 | ✅ 2026-05-12 |
| 03 | chatgpt-alternatives | 1 | 2 blog | 1 feature | 6 | ✅ 2026-05-12 |
| 04 | cornell-note-taking-method | 1 | 2 blog | 1 feature | 3 | ✅ 2026-05-18 |
| 05 | how-to-take-notes-in-college | 1 | 2 blog | 2 feature | 2 | ✅ 2026-05-18 |
| 06 | how-to-study-for-finals | 1 | 2 blog | 4 feature | 2 | ✅ 2026-05-18 |
| 07 | study-methods-compared | 1 | 4 blog | 0 | 1 | ✅ 2026-05-18 |
| 08 | mind-mapping-method | 1 | 3 blog | 1 feature | 1 | ✅ 2026-05-18 |
| 09 | zettelkasten-method | 1 | 3 blog | 1 feature | 1 | ✅ 2026-05-18 |
| 10 | feynman-technique | 1 | 3 blog | 2 feature | 0 | ✅ 2026-05-18 |
| 11 | sq3r-method | 1 | 3 blog | 1 feature | 1 | ✅ 2026-05-18 |
| 12 | leitner-system | 1 | 3 blog | 1 feature | 2 | ✅ 2026-05-18 |
| 13 | turn-notes-into-podcast | 1 | 2 blog | 8 feature | 2 | ✅ 2026-06-22 |

---

## 规范总结

- **内链**：Introduction 首段 ≥1 + Body blog 1–4 + Feature 0–2；**上下文分布**，无文末 Related。
- **外链**：权威来源 + 竞品 **nofollow**；锚文本描述性。
- **FAQ**：正文 `## Frequently Asked Questions` 必填（≥3 题）；**不要**写入 YAML frontmatter。
- **双核心词**：**AI note taker** 与 **notes generator** 分稿或分节覆盖时，对应链到首页与 `/feature/notes-generator`。
