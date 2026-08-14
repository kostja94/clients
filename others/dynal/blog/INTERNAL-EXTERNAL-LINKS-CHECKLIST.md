# Internal & External Links 规范（Dynal Blog）

> **依据**：基于 blog 链接规范的同一思路；站内 URL 权威以 [dynal-site-structure.md](../dynal-site-structure.md) 为准。
> **站点**：生产以 **dynal.ai** 为准；正文为 **英文**，本规范为 **中文**，供写作与校对使用。

---

## 链接分层（Dynal）

| 类型 | URL 模式 | 用途 |
|------|----------|------|
| **Blog 互链** | `https://dynal.ai/blog/{slug}` | 系列稿、相邻主题；锚文本用主题词，避免 "click here"。**勿**用裸域拼错路径。 |
| **Solutions / Post Generator** | `/linkedin-post-generator`（**已上线 hub**）；`/solutions/linkedin-content-system`、`/solutions/linkedin-ai-writer`、`/solutions/linkedin-post-generator`（⚠️ 将被废弃） | 产品叙事、工作流说明；Post Generator 全链 `https://dynal.ai/linkedin-post-generator` |
| **对比与定价** | 对比页、**`/pricing`** | 商业决策、与通用聊天工具区分；见下条 **canonical** |
| **首页 / 功能总览** | `https://dynal.ai/`、[dynal-features](https://dynal.ai/) | 品牌与功能入口，节制使用 |
| **Use case** | `/use-case/{slug}` | 按 persona 补充时链，如 `for-founder-ceo` |

**对比页 canonical**：站点导航与 [dynal-site-structure §〇.3](../dynal-site-structure.md) 记为 **`/vs-chatgpt`**。**当前 Markdown 文稿**已统一为 **`https://dynal.ai/vs-chatgpt`**（与线上 `/vs-chatgpt` 一致）。

---

## Internal Links 正文分布（Dynal）

| 区域 | Blog 互链 | 产品与转化（Solutions / vs / pricing / 首页） |
|------|-----------|------------------------------------------------|
| **标题下第一段（读者可见开篇，出现在第一个 `##` 之前）** | **≤ 1–2 条**；自然引入主题，避免链接目录式罗列 | **同段合计 ≤ 1 条**；或本节不放，下移到首次出现产品语境的段落 |
| **正文各 `##` / 逻辑小节** | 需要时再链，**语义相关**，每节通常 **≤ 2 条 Blog** | 每大一节或大概念块 **≤ 1 条** 产品对比/定价，避免三节连刷屏 |
| **frontmatter `related`** | YAML 中为 **slug** 数组（无 `/blog/` 前缀），与正文重要互链 **一致** |
| **`## Conclusion` / FAQ** | 可保留收束链；FAQ 中与问题强相关的链优先保留 | 同上 |

**锚文本**：描述性短语或篇名短语；少用裸 "learn more""read more"（英文稿尤忌）。

---

## External Links 规范（Dynal）

| 要求 | 说明 |
|------|------|
| **权威出处** | LinkedIn Help、[Feed ranking](https://www.linkedin.com/help/linkedin/answer/a9554004)、Engineering 博客、developers.google.com 等，支撑机制与 E-E-A-T |
| **竞品 / 厂商** | 若稿件出现可对比的第三方产品站，HTML 侧建议 `rel="nofollow noopener"`（Markdown 交付时由 CMS 或构建层处理时再补） |

---

## 各篇链接状态维护表（blog `*-2026.md`）

改版后轮询更新；Blog 链条数以 **dynal.ai/blog/** 粗略计数为宜。

| # | File / slug | 开篇首段互链 | `related` 与正文互链对齐 | 备注 |
|---|-------------|-------------------|---------------------------|------|
| 01 | [01-types…](./01-types-of-linkedin-posts-2026.md) · `types-of-linkedin-posts` | ✅ 按清单 | ✅ | Taxonomy |
| 02 | [02-how…](./02-how-to-get-clients-on-linkedin-2026.md) · `how-to-get-clients-on-linkedin` | ✅ | ✅ | System/trust |
| 03 | [03-playbook…](./03-linkedin-client-acquisition-playbook-2026.md) · `linkedin-client-acquisition-playbook` | ✅ | ✅ | Weekly loop |
| 04 | [04-hooks…](./04-linkedin-hooks-without-clickbait-2026.md) · `linkedin-hooks-without-clickbait` | ✅ | ✅ | Hooks |
| 05 | [05-notes…](./05-linkedin-posts-from-notes-and-pdfs-2026.md) · `linkedin-posts-from-notes-and-pdfs` | ✅ | ✅ | Notes/PDF |
| 06 | [06-calendar…](./06-linkedin-content-calendar-template-solo-2026.md) · `linkedin-content-calendar-template-solo` | ✅ | ✅ | Solo calendar |
| 07 | [07-profile…](./07-linkedin-personal-profile-vs-company-page-2026.md) · `linkedin-personal-profile-vs-company-page` | ✅ | ✅ | Profile vs Page |
| 08 | [08-dms…](./08-linkedin-dms-b2b-without-spam-2026.md) · `linkedin-dms-b2b-without-spam` | ✅ | ✅ | DMs |
| 09 | [09-scheduling…](./09-scheduling-linkedin-posts-time-zones-2026.md) · `scheduling-linkedin-posts-time-zones` | ✅ | ✅ | TZ |
| 10 | [10-voice…](./10-linkedin-brand-voice-guidelines-ai-2026.md) · `linkedin-brand-voice-guidelines-ai` | ✅ | ✅ | Brand voice |
| 11 | [11-newsletter…](./11-linkedin-newsletter-vs-feed-posts-2026.md) · `linkedin-newsletter-vs-feed-posts` | ✅ | ✅ | Newsletter |
| 12 | [12-automate…](./12-ai-for-linkedin-what-to-automate-2026.md) · `ai-for-linkedin-what-to-automate` | ✅ | ✅ | Automation |
| 13 | [13-tools…](./13-best-linkedin-tools-2026.md) · `best-linkedin-tools` | ✅ | ✅ | Stack choice |
| 14 | [14-how…](./14-how-to-create-linkedin-carousel-posts-2026.md) · `how-to-create-linkedin-carousel-posts` | ✅ 按清单 | ✅ | Carousel posts |
| 15 | [15-carousel-ads…](./15-linkedin-carousel-ads-complete-guide-2026.md) · `linkedin-carousel-ads-complete-guide` | ✅ 按清单 | ✅ | Carousel ads |

**维护**：新稿加入本表与 [README.md](./README.md) 登记表；互链或 slug 变更时同步 `related` 与本表。

---

*与 [README.md](./README.md) 配合使用。*