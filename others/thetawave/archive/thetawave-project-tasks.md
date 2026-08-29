# ThetaWave 项目任务

> 关联：[thetawave.md](./thetawave.md) | [thetawave-use-cases.md](./thetawave-use-cases.md) | [use-cases/discipline-use-cases.md](./use-cases/discipline-use-cases.md) | [thetawave-features.md](./thetawave-features.md) | [thetawave-keywords.md](./keywords/thetawave-keywords.md) | [thetawave-competitors.md](./thetawave-competitors.md) | [thetawave-vs-chatgpt.md](./thetawave-vs-chatgpt.md)

**Last updated**: 2026-03-31 — 新增 Task 13（认证页 noindex / robots）；更新后请同步修改日期。

---

## 任务进度

| 状态 | 数量 | 占比 |
|------|------|------|
| **未完成**（Pending / In Progress） | 13 | 100% |
| **已完成**（Done） | 0 | 0% |
| **总计** | 13 | — |

**进度**：0 / 13 已完成

---

## Legend

| Status | Meaning |
|--------|---------|
| **Pending** | Not started; needs work |
| **In Progress** | Currently working on it |
| **Done** | Completed |

| Priority | Meaning |
|----------|---------|
| **P0** | Blocker — fix first |
| **P1** | High — do soon |
| **P2** | Medium — important but not urgent |

---

## 未完成（Pending / In Progress）

| # | Task | Skill | Status | Priority | Action / Notes | Updated |
|---|------|-------|--------|----------|-----------------|---------|
| 1 | **Canonical URLs** — 所有页面缺少 canonical | canonical-tag | Pending | P1 | 每页添加 `<link rel="canonical" href="https://thetawave.ai/当前页URL" />`；Next.js 用 `metadata.alternates.canonical` | |
| 2 | **Heading 结构** — H 标签混乱（多 H1、层级跳跃、通用标题） | heading-structure | Pending | P1 | 每页仅 1 个 H1；H1→H2→H3 不跳级；H2/H3 含关键词、描述性强 | |
| 3 | **Open Graph** — 社交分享预览缺失 | open-graph | Pending | P1 | 每页添加 og:title、og:description、og:image、og:url；图片 1200×630px、绝对 URL | |
| 4 | **Twitter Cards** — X 分享预览缺失 | twitter-cards | Pending | P2 | 添加 twitter:card、twitter:title、twitter:description、twitter:image；可复用 OG | |
| 5 | **Hreflang** — 多语言/区域未配置 | page-metadata | Pending | P2 | 添加 hreflang；每页自引用；所有版本互链；x-default 指向 en | |
| 6 | **Schema 结构化数据** — 全站缺失 | schema-markup | Pending | P1 | Organization、WebSite；Article、FAQPage、BreadcrumbList、SoftwareApplication；JSON-LD | |
| 7 | **首页多语言 Metadata** — title/description 仍为英语 | title-tag, meta-description | Pending | P1 | 见下方「首页 Metadata 多语言」 | |
| 8 | **功能页关键词本地化** — 10 个落地页各市场检索词（见 `keywords/`） | keyword-research, localization-strategy | Pending | P1 | [feature-pages-keywords-localization.md](./keywords/feature-pages-keywords-localization.md) | |
| 9 | **PageSpeed 分数过低** — 性能优化 | google-search-console | Pending | P1 | 优化 LCP、INP、CLS；图片懒加载、字体优化、资源压缩；见 GSC Core Web Vitals 报告 | |
| 10 | **Social Proof 嵌入** — YouTube/Instagram/TikTok 内容墙 | testimonials, trust-badges | Pending | P2 | 嵌入用户评价/视频作为 social proof；参考 [Solvely GMAT](https://gmat.solvely.ai/#section-comments) 文案型 testimonial（姓名+学校+分数+引用）；TikTok/YouTube/Instagram 嵌入见下方 Task Details | |
| 11 | **ThetaWave vs ChatGPT 落地页** — 竞品对比独立页 | alternatives, competitor-research | Pending | P1 | 详见 [thetawave-vs-chatgpt.md](./thetawave-vs-chatgpt.md) | |
| 12 | **学科/专业 Use Case 落地页** — 参考 LegesGPT、Mindgrasp 等程序化页 | website-structure, use-cases | Pending | P1 | 优先 **/for-law-students**；文案与内链见 [thetawave-use-cases.md](./thetawave-use-cases.md)、[use-cases/discipline-use-cases.md](./use-cases/discipline-use-cases.md)；关键词 [thetawave-keywords.md](./keywords/thetawave-keywords.md) §4.1 | 2026-03-20 |
| 13 | **认证页收录控制** — `/auth/login`、`/auth/signup` 不应用 robots.txt Disallow | robots-txt, indexing, page-metadata | Pending | P2 | 页面级 `noindex`（勿在 robots 中 Disallow 同路径，否则爬虫可能读不到 noindex）；Login：`noindex,nofollow`；Signup：`noindex,follow`；勿将此类页列入 sitemap。详见下方「认证页 Metadata / robots」 | 2026-03-31 |

---

## 已完成（Done）

| # | Task | Skill | Completed | Notes |
|---|------|-------|-----------|------|
| — | *暂无* | — | — | 完成时将任务从上方移入此处 |

---

## 首页 Metadata 多语言（Task 7 详情）

**问题**：首页 en/zh/ja 内容已本地化，但 meta title 和 description 仍为英语。

**关键词映射**（Note Taker for College Students 等效）：
- en：AI note taker for college students
- zh：大学生 AI 笔记
- ja：AI ノートテイカー 大学生

**各语言 Title / Description**：

| Locale | Title | Meta description |
|--------|-------|------------------|
| en | AI Note Taker for College Students — Learn 10x Faster \| ThetaWave | Turn lectures into notes, mindmaps, quizzes & flashcards in real-time. Trusted by 100,000+ students worldwide. Free to try. |
| zh | 大学生 AI 笔记 — 10 倍学习效率 \| ThetaWave | 实时将讲座、音频、视频转为结构化笔记、思维导图、测验、闪卡。全球 10 万+ 大学生信赖，免费试用。 |
| ja | 大学生向け AI ノートテイカー — 10倍速で学ぶ \| ThetaWave | 講義・音声・動画をリアルタイムでノート、マインドマップ、クイズ、フラッシュカードに変換。スタンフォード・MIT など世界中の学生が利用。無料でお試し。 |

**实现**：`generateMetadata()` 按 locale 返回 title/description；同步配置 hreflang、og:locale。

---

## Task Details (from Skills)

### Canonical
绝对 URL；与当前页或首选版本一致；Next.js `metadata.alternates.canonical`

### Heading
H1 含主关键词；H2–H6 不跳级；每标题一主题

### Open Graph
og:title、og:description、og:image、og:url；1200×630px；og:locale 多语言

### Hreflang
自引用；对称；x-default；与 canonical 一致

### Schema
Organization、WebSite；Article、FAQPage、BreadcrumbList、SoftwareApplication；JSON-LD

### 认证页 Metadata / robots（Task 13）

**范围**：[https://thetawave.ai/auth/login](https://thetawave.ai/auth/login)、[https://thetawave.ai/auth/signup](https://thetawave.ai/auth/signup)

| 做法 | 说明 |
|------|------|
| **推荐** | 页面级 **noindex**（Next.js：`metadata.robots` 或 `<meta name="robots" ...>` / `X-Robots-Tag`） |
| **勿用 robots.txt Disallow 替代** | `Disallow` 只限制抓取，**不保证**不收录；若外链指向该 URL，仍可能出现在 SERP（常无摘要） |
| **勿 Disallow 与 noindex 同路径** | 爬虫需能抓取页面才能读取 **noindex**；在 robots 中屏蔽会削弱该指令 |
| **Login** | `noindex, nofollow` — 无搜索价值，减少误收录 |
| **Signup** | `noindex, follow` — 若页内链向 Privacy/Terms，保留 follow |
| **Sitemap** | 不要将 login/signup 提交进 sitemap |

**robots.txt 更适合**：`/admin/`、`/api/`、`/staging/` 等整段路径；认证落地页用 **noindex**，而非路径级 Disallow。

### Social Proof 嵌入（Task 10）
- **TikTok**：官方 tiktok.com/embed 支持 Profile、Hashtag、Sound 墙
- **YouTube**：单条视频或播放列表 iframe；无官方频道墙
- **Instagram**：单条帖子 [...] → Embed；无官方 feed 墙，需第三方
- **多平台聚合**：Tagembed、EmbedSocial、Curator.io 等

**参考竞品**：[Solvely GMAT](https://gmat.solvely.ai/#section-comments) — 「What Our Users Say」区块：姓名 + 目标学校（Applying: Stanford GSB、MIT Sloan 等）+ 引用 + 分数提升（From 585 → 705 in 2 months）+ 头像；锚点 `#section-comments`；教育类产品可借鉴此文案型 testimonial 结构。

---

## Page Scope (ThetaWave)

> **完整清单见 [thetawave.md §5](./thetawave.md#5-existing-website)、[thetawave-features.md](./thetawave-features.md)、[thetawave-use-cases.md](./thetawave-use-cases.md)**。以下为任务相关路径摘要。

- **功能页**（10 个）：/note-taker、/notes-generator、/lecture-to-notes、/youtube-to-notes、/pdf-to-notes、/flashcard-maker、/quiz-maker、/podcast-generator、/mind-map-maker、/infographics-generator — 详见 [thetawave-features.md](./thetawave-features.md)
- **Use Cases**（18 个，三分支）：By Subject（10 页）/ By Identity（4 页）/ By Stage（4 页）— 详见 [thetawave-use-cases.md](./thetawave-use-cases.md)
- **竞品对比**：/thetawave-vs-chatgpt（详见 [thetawave-vs-chatgpt.md](./thetawave-vs-chatgpt.md)）
- **认证**（Task 13）：/auth/login、/auth/signup — 页面 noindex，不写入 sitemap，robots.txt 勿 Disallow
- **其他**：/app、/blog
