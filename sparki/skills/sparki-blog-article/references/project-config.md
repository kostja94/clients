# Sparki — Project Configuration

> 加载时机：Phase 0R（R1）· Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §1 速查指针

---

## 1. 品牌与产品

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | Sparki（sparki.io） |
| **产品定位** | the first AI editing agent |
| **主域名** | https://sparki.io |
| **博客路径** | `/blog/`（独立 OpenBlog 部署，Rewrite 只覆盖 `/blog/*`） |
| **品类 one-liner** | Chat-to-edit AI video editing — upload footage, describe the cut in plain language, and an AI agent plans and executes the edit in the cloud |
| **核心功能** | Copy Style、Long to Short、AI Caption、AI Commentary、Video Resizer（+ Highlight Reels 等 solutions） |
| **交互范式** | 对话式 Agent：沟通 → 计划 → 执行 → 多轮修订 |
| **ICP** | 短视频创作者（Commentary/Vlog/Montage/Talking-head）、Podcast/Webinar 长改短团队、品牌/MCN、本地商家 |
| **作者署名** | `Sparki Team`（Organization 级；`author` 必填） |
| **语言** | en-US 正文；中文仅沟通用 |
| **联系** | enterprise@sparki.io（企业）；support@sparksview.com（Contact footer，勿当作品牌名） |
| **Socials** | X `x.com/sparkilovesedit` · YouTube `@sparkiai_official/shorts` · Instagram `sparki_ai_official` · TikTok `sparkiai_official` · Discord `discord.gg/3cWs84Jza8` |

---

## 2. 可链接 URL 白名单（内链规则 SSOT）

### A. 站内主站页面 — 一律**绝对 URL** `https://sparki.io/...`（不是相对路径）

| 类型 | URL |
|------|-----|
| 首页 | `https://sparki.io/` |
| 定价 | `https://sparki.io/pricing` |
| 功能 Hub | `https://sparki.io/features` |
| Copy Style | `https://sparki.io/features/copy-style` |
| Long to Short | `https://sparki.io/features/long-to-short` |
| AI Caption | `https://sparki.io/features/ai-caption` |
| AI Commentary | `https://sparki.io/features/ai-commentary` |
| Video Resizer | `https://sparki.io/features/video-resizer` |
| Solutions | `https://sparki.io/solutions/highlight-reels` 等（highlight-reels / youtube-to-tiktok / edit-videogen-clip / daily-vlog / panoramic-camera） |
| Creators | `https://sparki.io/creators/{slug}`（线上 18 页 + hub `/creators`） |
| Industries | `https://sparki.io/industries/{slug}`（线上 21 页） |
| Video-editor 类型页 | `https://sparki.io/video-editor/{slug}`（product-video / product-ad / product-review / ecommerce 等 + gaming） |
| Use Cases | `https://sparki.io/use-cases` |
| API/Dev | `https://sparki.io/doc/api`、`https://sparki.io/doc/developer` |

### B. 博客站内互链 — 相对路径 `/blog/{slug}`

- 链接 **61 篇既有文章** 或新稿，一律 `/blog/{slug}`（不开新标签、不加域名）
- 部署仓 frontmatter `slug` 不含 `/blog/`；正文链接含 `/blog/` 前缀

### C. 外链

- 权威来源 2–6；竞品官网用 HTML `<a href="URL" rel="nofollow noopener">`

### D. 禁止

- 未上线/规划中页面（G6）——不确定时在 Phase 0 六必问确认
- Forthcoming 链接作正文核心流程（脚注 ≤1）
- 死链（G2）

---

## 3. Frontmatter Schema（与 `validate:posts` 强一致）

| 字段 | 必填 | 规则 |
|------|:---:|------|
| `title` | ✅ | ≥1 字符；H1/title 含 primary keyword；45–60 字符最佳 |
| `description` | ✅ | **80–320** 字符（validate 硬性）；建议 120–160，benefit + 主词 |
| `slug` | ✅ | kebab-case 小写；**必须 = 文件名（去 `.md`）**；不含 `/blog/` |
| `date` | ✅ | 发布日 UTC `YYYY-MM-DD`；永不变 |
| `updated` | 可选 | 最近实质性更新日；无则省略；页面只显示一个日期 |
| `author` | ✅ | `Sparki Team` |
| `category` | ✅ | 枚举见 SKILL.md §1（validate 在 categories off 下仍要求字段存在） |
| `tags` | 可选 | 字符串数组；3–6 个；含主词变体与长尾 |
| `draft` | 可选 | 默认 `false`；创作期 `true`，终审通过后 `false` |
| `cover` | 可选 | `/blog/images/{slug}/…` 或绝对 URL；无则页面取正文首图 |
| `tldr` | 可选 | 40–320 字符的 TL;DR 短块（OpenBlog 支持）；与正文 `## TL;DR` 二选一 |

```yaml
---
title: "Editorial Title — Subtitle After Em Dash"
description: "140–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"
date: 2026-09-XX
updated: 2026-09-XX
author: "Sparki Team"
category: "Video Editing Features"
tags: ["primary keyword", "related variant", "use case"]
cover: "/blog/images/{slug}/cover.png"
draft: false
---
```

---

## 4. 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章 |
| **date = 发布日** | UTC 日期；创建后不轻易更改 |
| **避让已占用日** | 对照 `content-graph.md` 日期占用表 |
| **updated 语义** | 仅实质性内容更新时加；页面只显示一个日期 |

---

## 5. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、定价、Free credits/GB 与官网矛盾 | 逐 claim 对照 product-competitors.md §1 |
| **G2** | 死链 | 站内或站外链接 404 | 逐个检查内链可达；外链不全挂 |
| **G3** | 无来源数字 | 量化 claim（95% 转写、50+ 音色、3 小时、10–20 clips 等）无 attribution | P0 数字须 `[Source: URL]`；官网能力标注 "per Sparki's feature page" |
| **G4** | 竞品状态错误 | 竞品是否 AI 原生、定价区间、定位与官方矛盾 | 打开竞品官网/docs 验证 |
| **G5** | 产品能力夸大 | 定位语言 ≠ sparki.io 已实现 | 只写 features 白名单内的功能；不写未上线能力 |
| **G6** | 内链指向未上线页面 | 只链 §2 白名单 | 对照 §2 A/B/C/D |
| **G7** | 品牌/合规风险 | 贬低竞品；CreatorClone 暗示代言/合作；误导标题 | 竞品每家有 ≥1 优势；CreatorClone 只描述公开素材可验证手法 |

---

## 6. Sparki Voice 速查

| 维度 | 要求 |
|------|------|
| Clear | 目标创作者能复述核心 workflow |
| Practitioner-first | 像做过剪辑的同行在讲，不是营销稿 |
| Evidence-led | 切点/转场/字幕观察来自真实素材；数字有来源 |
| Category-building | 先讲清"对话式剪辑/Agent 剪辑"价值，再出现产品 |
| Fair comparison | 每竞品 ≥1 优势；≥1 场景非 Sparki 更合适 |

### 禁止

- revolutionary · game-changing · unlock · seamless · magic · cutting-edge
- 虚构开场（"Imagine you're a creator who…"）
- 空泛句：In today's world · Let's dive in · Without further ado
- 红人文：把个人偏好当普适结论、编造 creator 未公开说过的意图

---

*project-config · sparki v1.0.0 · 2026-09-04*
