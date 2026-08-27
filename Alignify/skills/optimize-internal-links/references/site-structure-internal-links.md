# Alignify 全站文章结构与内链

> **用途**：全站唯一的**结构与内链优化**参考（人类 + 站点维护）。回答：**① ~400 篇文章如何按频道组织；② 当前正文内链快照；③ 后续优化优先级**
>
> **Skill 对齐**：规则 SSOT [`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) · 存量优化 [`../SKILL.md`](../SKILL.md) · Marketing Part 4.5（M1–M11）
>
> **最后更新**：2026-08-27（自动扫描部署仓 `content/**/*.md`，共 **412** 篇）
>
> **机器可读数据**：[`../../../scripts/reports/md-internal-links-status-2026-08-27.json`](../../../scripts/reports/md-internal-links-status-2026-08-27.json)

---

## 一、站点文章结构

```
alignify.co
├── /tools/{slug}          ← 216 篇
├── /seo/{slug}            ← 76 篇
├── /blog/{slug}           ← 66 篇
├── /marketing/{slug}      ← 32 篇
├── /insights/{slug}       ← 14 篇
└── /events/{slug}         ← 8 篇
```

**正文 SSOT**：`E:\自有部署项目\alignify production\content/{channel}/{locale}/{slug}.md`

| 频道 | EN+ZH 篇数 | 内链存储 | 优化原则 |
|------|-----------|---------|----------|
| `tools` | 216 | 正文 Markdown / HTML | 点击意图；无硬性条数 |
| `seo` | 76 | 正文 Markdown / HTML | 点击意图；无硬性条数 |
| `blog` | 66 | 正文 Markdown / HTML | 点击意图；无硬性条数 |
| `marketing` | 32 | 正文 Markdown / HTML | 点击意图；无硬性条数 |
| `insights` | 14 | 正文 Markdown / HTML | 点击意图；无硬性条数 |
| `events` | 8 | 正文 Markdown / HTML | 点击意图；无硬性条数 |
| **合计** | **412** | — | — |

**跨频道桥接**（常见）：`tools/*` ↔ `blog/*`（产品深度文）、`tools/*` ↔ `marketing/*`（GTM）、`seo/*` ↔ `blog/*`（搜索/GEO）。

---

## 二、内链规则（不在此重复）

> **SSOT**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 1–2（点击意图、每段 ≤1 链、同 URL 1 次；FAQ 答案内链计入正文）
> **Marketing M1–M11**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md#part-45-marketing-频道内链)
> **结论内链**：[`../../create-article/rules/sections.md`](../../create-article/rules/sections.md) Part 4.4（0–2 条，非清单式）

审计脚本可能仍输出 distinct 计数，**仅作观察**，不作为发布阻断条件。

---

## 三、当前快照概览

| 类目 | 文章数 | 出链总量 | 均出链/篇 | distinct≥5（观察） | 占比 |
|------|-------:|--------:|----------:|------------:|-----:|
| tools ⭐ | 216 | 1008 | 4.7 | 95 | 44% |
| seo | 76 | 214 | 2.8 | 14 | 18% |
| blog | 66 | 363 | 5.5 | 34 | 52% |
| marketing | 32 | 158 | 4.9 | 12 | 38% |
| insights | 14 | 104 | 7.4 | 6 | 43% |
| events | 8 | 4 | 0.5 | 0 | 0% |
| **合计** | **412** | **1851** | **4.5** | **161** | **39%** |

### 需要关注的问题

- **Tools distinct<5（观察）**：**121** / 216 篇
- **零出链**：**60** 篇
- **零入链（EN 基准）**：**13** 篇
- **同篇重复目标（须修）**：**61** 篇

---

## 四、高入链 Hub（全站 Top 30 · 按入链次数）

| 排名 | pageKey | 入链次数 | 说明 |
|-----:|---------|--------:|------|
| 1 | `tools/text-generator` | 37 | tools hub |
| 2 | `tools/llm` | 35 | tools hub |
| 3 | `tools/image-generator` | 34 | tools hub |
| 4 | `tools/api` | 33 | tools hub |
| 5 | `tools/productivity` | 32 | tools hub |
| 6 | `tools/video-generator` | 32 | tools hub |
| 7 | `tools/knowledge-base` | 31 | tools hub |
| 8 | `tools/web-search-api` | 31 | tools hub |
| 9 | `marketing/pricing-strategy` | 30 | marketing |
| 10 | `tools/workflow` | 29 | tools hub |
| 11 | `marketing/geo` | 28 | marketing |
| 12 | `tools/coding` | 26 | tools hub |
| 13 | `tools/geo` | 26 | tools hub |
| 14 | `seo/internal-links` | 26 | seo |
| 15 | `tools/video-editor` | 25 | tools hub |
| 16 | `marketing/affiliate` | 25 | marketing |
| 17 | `seo/website-structure` | 24 | seo |
| 18 | `blog/embedded-virality` | 23 | blog |
| 19 | `tools/note-taker` | 22 | tools hub |
| 20 | `marketing/keyword-research` | 22 | marketing |
| 21 | `marketing/creator-challenge-program` | 22 | marketing |
| 22 | `tools/browser` | 21 | tools hub |
| 23 | `tools/search-engine` | 21 | tools hub |
| 24 | `seo/sitemap` | 21 | seo |
| 25 | `tools/directory` | 20 | tools hub |
| 26 | `blog/rate-limit-reset` | 20 | blog |
| 27 | `marketing/creator-program` | 19 | marketing |
| 28 | `tools/text-to-speech` | 18 | tools hub |
| 29 | `marketing/competitive-analysis` | 18 | marketing |
| 30 | `blog/ugc-marketing` | 18 | blog |

---

## 五、优化优先级队列

### P0 — 结构性违规（R4 重复 / 机械指路链）

优先修复同篇重复 URL（含 FAQ 与正文重复）、组合拳段堆链。Tools 低 distinct 仅作观察，不为凑数加链。

**Tools distinct<5（观察）**：121 篇

### P1 — 零入链 EN 页（Hub 曝光不足）

- `blog/ai-components` — AI Components: Injecting Differentiated UI into Vi
- `blog/how-to-name-ai-products` — AI Product Naming: Strategies, Case Studies, and a
- `insights/ai-logo-design` — AI Product Logo Design: A Founder's Guide from Pos
- `insights/generative-ai-landscape` — Generative AI Landscape & Reports
- `insights/google` — Google AI Products: Complete Ecosystem from Search
- `insights/openai` — OpenAI Products: Complete Ecosystem from ChatGPT t
- `seo/best-tools` — Best SEO Tools: Free Essentials, Stacks & Platform
- `seo/branded-queries-filter-google-search-console` — Branded Queries Filter: Google Search Console
- `seo/example-article` — MDX Usage: Markdown+React in Next.js Tutorial
- `seo/glossary` — Glossary-Driven Growth: Build Content Moat
- `seo/new-domains-tld` — .New Domains: Google to AI Programming Innovation
- `tools/fundraising` — Fundraising Tools: AI-Powered Investor Discovery
- `tools/healthcare` — AI Healthcare Tools: Digital Transformation in Hea

### P2 — 零出链

- `events/en/founder-park-2024-11-06`
- `events/zh/founder-park-2024-11-06`
- `events/en/linkloud-2026-01-24`
- `events/zh/linkloud-2026-01-24`
- `insights/en/google`
- `insights/zh/google`
- `insights/en/openai`
- `insights/zh/openai`
- `marketing/en/growth-case-studies`
- `marketing/en/reddit`
- `seo/en/best-tools`
- `seo/zh/best-tools`
- `seo/en/branded-queries-filter-google-search-console`
- `seo/zh/branded-queries-filter-google-search-console`
- `seo/en/crawler`
- `seo/zh/crawler`
- `seo/en/create-blog`
- `seo/zh/create-blog`
- `seo/en/dark-traffic`
- `seo/zh/dark-traffic`
- `seo/en/example-article`
- `seo/zh/example-article`
- `seo/en/external-links`
- `seo/zh/external-links`
- `seo/en/glossary`
- `seo/zh/glossary`
- `seo/en/google-tag-manager`
- `seo/zh/google-tag-manager`
- `seo/en/how-search-engine-works`
- `seo/zh/how-search-engine-works`
- … 另有 **30** 篇

### P3 — 同篇重复目标

共 **61** 篇；见 JSON `duplicates` 字段或运行 `python scripts/audit/audit-md-internal-links.py` 刷新快照。

---

## 六、按频道明细

> 列：**出链 distinct** · **入链** · **出链目标**（`route/slug`）· ⚠重复 = 同篇同目标 >1 次

### tools

| 文章 | 语言 | 出链 | 入链 | 出链目标 |
|------|------|-----:|-----:|---------|
| `3d` | en | 4 📊 | 8 | `blog/cad`、`tools/3d-model-generator`、`tools/3d-scanner`、`tools/animation-generator` |
| `3d-model-generator` | en | 3 📊 | 8 | `tools/3d-modelling`、`tools/3d-scanner`、`tools/world-model` |
| `3d-modelling` | en | 4 📊 | 8 | `blog/cad`、`tools/3d`、`tools/3d-model-generator`、`tools/3d-scanner` |
| `3d-scanner` | en | 3 📊 | 6 | `tools/3d-model-generator`、`tools/3d-modelling`、`tools/world-model` |
| `accent-conversion` | en | 3 📊 | 6 | `tools/speech-to-text`、`tools/text-to-speech`、`tools/voice-changer` |
| `affiliate-marketing` | en | 3 📊 | 7 | `blog/agentic-commerce`、`tools/lead-generation`、`tools/referral-program` |
| `agent-for-desktop` | en | 9 | 8 | `blog/multi-agent`、`tools/api`、`tools/authentication`、`tools/browser`、`tools/directory`、`tools/headless-browser`、`tools/ide`、`tools/knowledge-base`、`tools/productivity` |
| `agent-skills` | en | 16 | 16 | `tools/agent-for-desktop`、`tools/api`、`tools/app-builder`、`tools/browser`、`tools/chatbot`、`tools/code-completion`、`tools/code-review`、`tools/coding`、`tools/directory`、`tools/evaluation`、`tools/family-assistant`、`tools/knowledge-base`、`tools/llm`、`tools/openclaw-alternatives`、`tools/productivity`、`tools/vibe-coding` |
| `ai-homework-helper` | en | 2 📊 | 4 | `tools/education`、`tools/essay-writer` |
| `ai-scheduling` | en | 3 📊 | 8 | `tools/family-assistant`、`tools/lead-generation`、`tools/note-taker` |
| `animation-generator` | en | 5 | 9 | `tools/animation-library`、`tools/filmmaking`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video` |
| `animation-library` | en | 4 📊 | 5 | `tools/design`、`tools/image-generator`、`tools/video-generator`、`tools/website-builder` |
| `api` | en | 5 | 33 | `tools/coding`、`tools/image-generator`、`tools/llm`、`tools/video-generator`、`tools/workflow` |
| `app-builder` | en | 3 📊 | 16 | `tools/coding`、`tools/vibe-coding`、`tools/website-builder` |
| `audio-translator` | en | 3 📊 | 4 | `tools/accent-conversion`、`tools/video-translator`、`tools/voice` |
| `authentication` | en | 7 | 4 | `tools/api`、`tools/app-builder`、`tools/browser`、`tools/notes-generator`、`tools/productivity`、`tools/user-research`、`tools/web-search-api` |
| `avatar` | en | 11 | 7 | `tools/api`、`tools/background-changer`、`tools/headshot-generator`、`tools/image-editor`、`tools/image-generator`、`tools/lip-sync`、`tools/music-generator`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-generator`、`tools/web-search-api` |
| `b2b` | en | 3 📊 | 8 | `tools/lead-generation`、`tools/linkedin`、`tools/web-scraping` |
| `background-changer` | en | 6 | 13 | `tools/avatar`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator`、`tools/poster-generator`、`tools/text-generator` |
| `browser` | en | 3 📊 | 21 | `tools/coding`、`tools/search-engine`、`tools/workflow` |
| `canvas-video` | en | 5 | 5 | `tools/image-to-video`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/workflow` |
| `character-chat` | en | 7 | 5 | `tools/api`、`tools/chatbot`、`tools/dating`、`tools/directory`、`tools/headshot-generator`、`tools/story-generator`、`tools/web-search-api` |
| `chatbot` | en | 3 📊 | 17 | `tools/coding`、`tools/knowledge-base`、`tools/text` |
| `cli` | en | 2 📊 | 9 | `tools/coding`、`tools/ide` |
| `code-completion` | en | 3 📊 | 11 | `tools/code-review`、`tools/coding`、`tools/ide` |
| `code-review` | en | 4 📊 | 16 | `tools/code-completion`、`tools/coding`、`tools/directory`、`tools/text-generator` |
| `coding` | en | 3 📊 | 26 | `tools/code-completion`、`tools/documentation`、`tools/ide` |
| `community` | en | 3 📊 | 6 | `tools/directory`、`tools/knowledge-base`、`tools/llm` |
| `dating` | en | 2 📊 | 1 | `tools/ai-scheduling`、`tools/character-chat` |
| `design` | en | 4 📊 | 13 | `blog/interior-design`、`tools/image-generator`、`tools/poster-generator`、`tools/website-builder` |
| `directory` | en | 2 📊 | 20 | `tools/evaluation`、`tools/search-engine` |
| `documentation` | en | 19 | 16 | `tools/api`、`tools/app-builder`、`tools/browser`、`tools/chatbot`、`tools/cli`、`tools/code-completion`、`tools/code-review`、`tools/coding`、`tools/directory`、`tools/geo`、`tools/ide`、`tools/llm`、`tools/productivity`、`tools/text-generator`、`tools/user-research`、`tools/vibe-coding`、`tools/web-search-api`、`tools/website-builder`、`tools/workflow` |
| `education` | en | 2 📊 | 3 | `tools/essay-writer`、`tools/web-search-api` |
| `essay-writer` | en | 2 📊 | 13 | `tools/note-taker`、`tools/text-generator` |
| `evaluation` | en | 3 📊 | 17 | `tools/agent-skills`、`tools/api`、`tools/coding` |
| `family-assistant` | en | 4 📊 | 4 | `tools/ai-scheduling`、`tools/note-taker`、`tools/productivity`、`tools/voice-cloning` |
| `fashion` | en | 2 📊 | 2 | `tools/background-changer`、`tools/image-generator` |
| `filmmaking` | en | 6 | 6 | `tools/animation-library`、`tools/lip-sync`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video`、`tools/video-translator` |
| `fundraising` | en | 2 📊 | 0 | `tools/b2b`、`tools/lead-generation` |
| `geo` | en | 9 | 26 | `blog/ai-traffic-and-citation-sources`、`tools/api`、`tools/browser`、`tools/notes-generator`、`tools/productivity`、`tools/search-engine`、`tools/search-indexing`、`tools/user-research`、`tools/web-search-api` |
| `headless-browser` | en | 3 📊 | 6 | `tools/api`、`tools/geo`、`tools/ide` |
| `headshot-generator` | en | 6 | 6 | `tools/image`、`tools/image-enhancer`、`tools/image-generator`、`tools/poster-generator`、`tools/presentation-maker`、`tools/web-search-api` |
| `healthcare` | en | 4 📊 | 0 | `blog/medical-scribe`、`tools/knowledge-base`、`tools/legal`、`tools/note-taker` |
| `hr-assistant` | en | 5 | 5 | `tools/chatbot`、`tools/interview-assistant`、`tools/note-taker`、`tools/productivity`、`tools/recruiting` |
| `ide` | en | 3 📊 | 12 | `tools/cli`、`tools/code-completion`、`tools/coding` |
| `image` | en | 4 📊 | 6 | `tools/community`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-relighting` |
| `image-editor` | en | 2 📊 | 16 | `tools/background-changer`、`tools/image-enhancer` |
| `image-enhancer` | en | 2 📊 | 16 | `tools/image-editor`、`tools/image-generator` |
| `image-generator` | en | 4 📊 | 34 | `tools/background-changer`、`tools/headshot-generator`、`tools/tattoo-generator`、`tools/virtual-staging` |
| `image-relighting` | en | 2 📊 | 3 | `tools/image-editor`、`tools/image-enhancer` |
| `image-to-video` | en | 5 | 9 | `tools/animation-generator`、`tools/filmmaking`、`tools/image-generator`、`tools/video-editor`、`tools/video-generator` |
| `influencer-marketing` | en | 1 📊 | 2 | `tools/affiliate-marketing` |
| `interview-assistant` | en | 2 📊 | 2 | `tools/lead-generation`、`tools/recruiting` |
| `knowledge-base` | en | 3 📊 | 31 | `blog/agent-memory`、`tools/note-taker`、`tools/search-engine` |
| `lead-generation` | en | 3 📊 | 14 | `tools/b2b`、`tools/knowledge-base`、`tools/recruiting` |
| `legal` | en | 3 📊 | 2 | `tools/notes-generator`、`tools/productivity`、`tools/text-generator` |
| `linkedin` | en | 4 📊 | 3 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting`、`tools/text-generator` |
| `lip-sync` | en | 3 📊 | 9 | `tools/avatar`、`tools/video-to-video`、`tools/video-translator` |
| `llm` | en | 10 | 35 | `tools/api`、`tools/chatbot`、`tools/documentation`、`tools/geo`、`tools/knowledge-base`、`tools/llm-for-coding`、`tools/llm-for-reasoning`、`tools/search-engine`、`tools/text-generator`、`tools/workflow` |
| `llm-for-coding` | en | 10 | 7 | `tools/code-completion`、`tools/code-review`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/knowledge-base`、`tools/llm`、`tools/llm-for-math`、`tools/search-engine`、`tools/vibe-coding` |
| `llm-for-math` | en | 8 | 3 | `tools/api`、`tools/browser`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/llm`、`tools/llm-for-coding`、`tools/text-generator` |
| `llm-for-reasoning` | en | 6 | 2 | `tools/api`、`tools/directory`、`tools/llm`、`tools/multimodal-llm`、`tools/search-engine`、`tools/text-generator` |
| `logo-generator` | en | 5 | 10 | `media-kit`、`tools/background-changer`、`tools/design`、`tools/image-generator`、`tools/poster-generator` |
| `memory` | en | 4 📊 | 3 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `multimodal-llm` | en | 8 | 2 | `tools/api`、`tools/browser`、`tools/directory`、`tools/documentation`、`tools/image-generator`、`tools/llm`、`tools/ocr`、`tools/web-search-api` |
| `music-generator` | en | 2 📊 | 3 | `tools/video-editor`、`tools/voice-changer` |
| `music-video-generator` | en | 5 | 4 | `tools/lip-sync`、`tools/music-generator`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-generator` |
| `note-taker` | en | 4 📊 | 22 | `blog/medical-scribe`、`tools/knowledge-base`、`tools/notes-generator`、`tools/speech-to-text` |
| `notes-generator` | en | 3 📊 | 12 | `tools/ai-scheduling`、`tools/note-taker`、`tools/voice-cloning` |
| `ocr` | en | 3 📊 | 3 | `tools/image-enhancer`、`tools/knowledge-base`、`tools/note-taker` |
| `openclaw-alternatives` | en | 7 | 6 | `tools/agent-for-desktop`、`tools/api`、`tools/chatbot`、`tools/directory`、`tools/documentation`、`tools/knowledge-base`、`tools/productivity` |
| `poster-generator` | en | 3 📊 | 6 | `tools/design`、`tools/fashion`、`tools/image-generator` |
| `presentation-maker` | en | 3 📊 | 5 | `tools/design`、`tools/essay-writer`、`tools/image-generator` |
| `productivity` | en | 2 📊 | 32 | `tools/hr-assistant`、`tools/note-taker` |
| `recruiting` | en | 3 📊 | 8 | `tools/hr-assistant`、`tools/interview-assistant`、`tools/note-taker` |
| `referral-program` | en | 3 📊 | 6 | `tools/affiliate-marketing`、`tools/b2b`、`tools/lead-generation` |
| `religion` | en | 3 📊 | 1 | `tools/essay-writer`、`tools/knowledge-base`、`tools/presentation-maker` |
| `search-engine` | en | 5 | 21 | `tools/browser`、`tools/evaluation`、`tools/geo`、`tools/knowledge-base`、`tools/search-indexing` |
| `search-indexing` | en | 3 📊 | 7 | `tools/llm`、`tools/memory`、`tools/search-engine` |
| `short-drama` | en | 3 📊 | 5 | `tools/animation-generator`、`tools/video-generator`、`tools/workflow` |
| `social-cards-generator` | en | 5 | 4 | `tools/api`、`tools/geo`、`tools/image-generator`、`tools/logo-generator`、`tools/web-scraping` |
| `speech-to-text` | en | 5 | 8 | `blog/medical-scribe`、`tools/accent-conversion`、`tools/note-taker`、`tools/text-to-speech`、`tools/voice-changer` |
| `spreadsheet` | en | 3 📊 | 1 | `tools/app-builder`、`tools/presentation-maker`、`tools/web-scraping` |
| `story-generator` | en | 2 📊 | 4 | `tools/essay-writer`、`tools/text-generator` |
| `tattoo-generator` | en | 3 📊 | 3 | `tools/avatar`、`tools/image`、`tools/image-generator` |
| `text` | en | 3 📊 | 2 | `tools/essay-writer`、`tools/text-generator`、`tools/text-translator` |
| `text-generator` | en | 6 | 37 | `tools/documentation`、`tools/essay-writer`、`tools/evaluation`、`tools/llm`、`tools/presentation-maker`、`tools/story-generator` |
| `text-to-speech` | en | 2 📊 | 18 | `tools/voice-changer`、`tools/voice-cloning` |
| `text-to-video` | en | 5 | 12 | `tools/image-to-video`、`tools/video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator` |
| `text-translator` | en | 5 | 2 | `tools/audio-translator`、`tools/essay-writer`、`tools/llm`、`tools/text-generator`、`tools/video-translator` |
| `user-research` | en | 2 📊 | 5 | `tools/ai-scheduling`、`tools/productivity` |
| `vibe-coding` | en | 3 📊 | 16 | `blog/how-to-build-a-blog-without-a-cms-using-ai`、`tools/app-builder`、`tools/coding` |
| `video` | en | 6 | 6 | `tools/canvas-video`、`tools/filmmaking`、`tools/image-to-video`、`tools/music-video-generator`、`tools/text-to-video`、`tools/video-generator` |
| `video-clipping` | en | 4 📊 | 12 | `tools/text-to-video`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `video-editor` | en | 5 | 25 | `tools/video`、`tools/video-clipping`、`tools/video-effects`、`tools/video-generator`、`tools/video-to-video` |
| `video-effects` | en | 5 | 8 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator`、`tools/video-to-video` |
| `video-generator` | en | 5 | 32 | `tools/canvas-video`、`tools/image-to-video`、`tools/text-to-video`、`tools/video-clipping`、`tools/video-editor` |
| `video-to-video` | en | 5 | 12 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-effects`、`tools/video-generator`、`tools/video-translator` |
| `video-translator` | en | 4 📊 | 13 | `tools/audio-translator`、`tools/lip-sync`、`tools/video`、`tools/video-clipping` |
| `virtual-staging` | en | 1 📊 | 4 | `tools/headshot-generator` |
| `voice` | en | 4 📊 | 2 | `tools/accent-conversion`、`tools/notes-generator`、`tools/text-to-speech`、`tools/voice-cloning` |
| `voice-changer` | en | 1 📊 | 11 | `tools/text-to-speech` |
| `voice-cloning` | en | 2 📊 | 10 | `tools/text-to-speech`、`tools/voice-changer` |
| `web-scraping` | en | 2 📊 | 11 | `tools/geo`、`tools/web-search-api` |
| `web-search-api` | en | 5 | 31 | `tools/knowledge-base`、`tools/llm`、`tools/search-indexing`、`tools/text-generator`、`tools/workflow` |
| `website-builder` | en | 3 📊 | 9 | `tools/coding`、`tools/design`、`tools/image-generator` |
| `workflow` | en | 6 | 29 | `blog/agent-to-agent`、`tools/agent-skills`、`tools/browser`、`tools/canvas-video`、`tools/coding`、`tools/productivity` |
| `world-model` | en | 8 | 6 | `tools/3d`、`tools/directory`、`tools/image-generator`、`tools/llm`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/web-search-api` |
| `3d` | zh | 6 | 8 | `blog/cad`、`tools/3d-model-generator`、`tools/3d-modelling`、`tools/3d-scanner`、`tools/design`、`tools/image-generator` |
| `3d-model-generator` | zh | 3 📊 | 8 | `tools/3d-modelling`、`tools/3d-scanner`、`tools/world-model` ⚠重复 |
| `3d-modelling` | zh | 4 📊 | 8 | `blog/cad`、`tools/3d`、`tools/3d-model-generator`、`tools/3d-scanner` |
| `3d-scanner` | zh | 3 📊 | 6 | `tools/3d-model-generator`、`tools/3d-modelling`、`tools/world-model` ⚠重复 |
| `accent-conversion` | zh | 4 📊 | 6 | `tools/education`、`tools/text-to-speech`、`tools/voice-changer`、`tools/voice-cloning` ⚠重复 |
| `affiliate-marketing` | zh | 3 📊 | 7 | `blog/agentic-commerce`、`tools/influencer-marketing`、`tools/referral-program` |
| `agent-for-desktop` | zh | 13 | 8 | `blog/multi-agent`、`tools/api`、`tools/authentication`、`tools/browser`、`tools/cli`、`tools/directory`、`tools/evaluation`、`tools/geo`、`tools/ide`、`tools/knowledge-base`、`tools/llm`、`tools/productivity`、`tools/workflow` |
| `agent-skills` | zh | 10 | 16 | `blog/agent-memory`、`tools/api`、`tools/browser`、`tools/cli`、`tools/code-review`、`tools/directory`、`tools/evaluation`、`tools/knowledge-base`、`tools/productivity`、`tools/vibe-coding` |
| `ai-homework-helper` | zh | 2 📊 | 4 | `tools/education`、`tools/essay-writer` |
| `ai-scheduling` | zh | 5 | 8 | `tools/family-assistant`、`tools/lead-generation`、`tools/note-taker`、`tools/productivity`、`tools/workflow` |
| `animation-generator` | zh | 5 | 9 | `tools/animation-library`、`tools/filmmaking`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video` |
| `animation-library` | zh | 5 | 5 | `tools/design`、`tools/vibe-coding`、`tools/video-effects`、`tools/video-generator`、`tools/website-builder` |
| `api` | zh | 7 | 33 | `tools/agent-skills`、`tools/coding`、`tools/documentation`、`tools/image-generator`、`tools/llm`、`tools/video-generator`、`tools/workflow` |
| `app-builder` | zh | 3 📊 | 16 | `tools/coding`、`tools/vibe-coding`、`tools/website-builder` |
| `audio-translator` | zh | 5 | 4 | `tools/accent-conversion`、`tools/speech-to-text`、`tools/text-to-speech`、`tools/video-translator`、`tools/voice-changer` ⚠重复 |
| `authentication` | zh | 7 | 4 | `blog/agentic-commerce`、`tools/browser`、`tools/chatbot`、`tools/llm`、`tools/notes-generator`、`tools/productivity`、`tools/user-research` |
| `avatar` | zh | 10 | 7 | `tools/api`、`tools/background-changer`、`tools/image`、`tools/image-editor`、`tools/lip-sync`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-translator`、`tools/web-search-api`、`tools/workflow` |
| `b2b` | zh | 4 📊 | 8 | `tools/knowledge-base`、`tools/lead-generation`、`tools/linkedin`、`tools/web-scraping` |
| `background-changer` | zh | 6 | 13 | `tools/avatar`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator`、`tools/logo-generator`、`tools/text-generator` ⚠重复 |
| `browser` | zh | 5 | 21 | `tools/agent-for-desktop`、`tools/coding`、`tools/headless-browser`、`tools/search-engine`、`tools/workflow` |
| `canvas-video` | zh | 5 | 5 | `tools/image-to-video`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/workflow` ⚠重复 |
| `character-chat` | zh | 8 | 5 | `tools/api`、`tools/evaluation`、`tools/geo`、`tools/notes-generator`、`tools/productivity`、`tools/text-generator`、`tools/text-to-speech`、`tools/web-search-api` |
| `chatbot` | zh | 4 📊 | 17 | `tools/b2b`、`tools/coding`、`tools/llm`、`tools/productivity` |
| `cli` | zh | 2 📊 | 9 | `tools/coding`、`tools/vibe-coding` |
| `code-completion` | zh | 4 📊 | 11 | `tools/code-review`、`tools/coding`、`tools/ide`、`tools/llm-for-coding` |
| `code-review` | zh | 7 | 16 | `tools/code-completion`、`tools/coding`、`tools/directory`、`tools/llm`、`tools/productivity`、`tools/text-generator`、`tools/workflow` |
| `coding` | zh | 5 | 26 | `tools/agent-skills`、`tools/code-completion`、`tools/code-review`、`tools/ide`、`tools/vibe-coding` |
| `community` | zh | 2 📊 | 6 | `tools/directory`、`tools/knowledge-base` |
| `dating` | zh | 2 📊 | 1 | `tools/ai-scheduling`、`tools/character-chat` ⚠重复 |
| `design` | zh | 7 | 13 | `blog/interior-design`、`tools/animation-library`、`tools/image-editor`、`tools/image-generator`、`tools/logo-generator`、`tools/poster-generator`、`tools/tattoo-generator` |
| `directory` | zh | 5 | 20 | `tools/community`、`tools/evaluation`、`tools/search-engine`、`tools/search-indexing`、`tools/web-search-api` |
| `documentation` | zh | 17 | 16 | `tools/api`、`tools/app-builder`、`tools/browser`、`tools/cli`、`tools/code-completion`、`tools/code-review`、`tools/coding`、`tools/directory`、`tools/geo`、`tools/ide`、`tools/ocr`、`tools/productivity`、`tools/text-generator`、`tools/vibe-coding`、`tools/web-search-api`、`tools/website-builder`、`tools/workflow` |
| `education` | zh | 2 📊 | 3 | `tools/essay-writer`、`tools/web-search-api` ⚠重复 |
| `essay-writer` | zh | 3 📊 | 13 | `tools/text`、`tools/text-generator`、`tools/web-search-api` |
| `evaluation` | zh | 3 📊 | 17 | `tools/api`、`tools/llm`、`tools/llm-for-coding` |
| `family-assistant` | zh | 5 | 4 | `tools/ai-scheduling`、`tools/chatbot`、`tools/note-taker`、`tools/productivity`、`tools/voice-cloning` |
| `fashion` | zh | 5 | 2 | `tools/3d`、`tools/image`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator` |
| `filmmaking` | zh | 6 | 6 | `tools/animation-library`、`tools/lip-sync`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video`、`tools/video-translator` |
| `fundraising` | zh | 3 📊 | 0 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting` |
| `geo` | zh | 11 | 26 | `blog/ai-traffic-and-citation-sources`、`blog/ai-visibility`、`tools/browser`、`tools/chatbot`、`tools/notes-generator`、`tools/productivity`、`tools/search-engine`、`tools/spreadsheet`、`tools/text-generator`、`tools/user-research`、`tools/web-search-api` ⚠重复 |
| `headless-browser` | zh | 3 📊 | 6 | `tools/geo`、`tools/llm`、`tools/web-scraping` |
| `headshot-generator` | zh | 4 📊 | 6 | `tools/image-generator`、`tools/image-relighting`、`tools/presentation-maker`、`tools/website-builder` |
| `healthcare` | zh | 5 | 0 | `blog/medical-scribe`、`tools/family-assistant`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `hr-assistant` | zh | 4 📊 | 5 | `tools/chatbot`、`tools/note-taker`、`tools/productivity`、`tools/recruiting` |
| `ide` | zh | 2 📊 | 12 | `tools/code-completion`、`tools/code-review` |
| `image` | zh | 6 | 6 | `tools/community`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-relighting`、`tools/tattoo-generator`、`tools/virtual-staging` |
| `image-editor` | zh | 6 | 16 | `tools/avatar`、`tools/background-changer`、`tools/image`、`tools/image-enhancer`、`tools/image-generator`、`tools/virtual-staging` |
| `image-enhancer` | zh | 2 📊 | 16 | `tools/image-editor`、`tools/ocr` |
| `image-generator` | zh | 5 | 34 | `tools/background-changer`、`tools/headshot-generator`、`tools/image-editor`、`tools/image-enhancer`、`tools/virtual-staging` |
| `image-relighting` | zh | 2 📊 | 3 | `tools/background-changer`、`tools/image-enhancer` |
| `image-to-video` | zh | 5 | 9 | `tools/animation-generator`、`tools/filmmaking`、`tools/image-generator`、`tools/video-editor`、`tools/video-generator` |
| `influencer-marketing` | zh | 4 📊 | 2 | `tools/affiliate-marketing`、`tools/lead-generation`、`tools/referral-program`、`tools/social-cards-generator` |
| `interview-assistant` | zh | 3 📊 | 2 | `tools/documentation`、`tools/lead-generation`、`tools/text-generator` |
| `knowledge-base` | zh | 4 📊 | 31 | `blog/agent-memory`、`tools/search-engine`、`tools/text-generator`、`tools/web-search-api` |
| `lead-generation` | zh | 4 📊 | 14 | `tools/b2b`、`tools/productivity`、`tools/recruiting`、`tools/referral-program` |
| `legal` | zh | 4 📊 | 2 | `tools/notes-generator`、`tools/productivity`、`tools/religion`、`tools/text-generator` |
| `linkedin` | zh | 4 📊 | 3 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting`、`tools/text-generator` |
| `lip-sync` | zh | 5 | 9 | `tools/avatar`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-to-video`、`tools/video-translator` |
| `llm` | zh | 9 | 35 | `tools/api`、`tools/browser`、`tools/documentation`、`tools/evaluation`、`tools/geo`、`tools/knowledge-base`、`tools/llm-for-coding`、`tools/text-generator`、`tools/workflow` |
| `llm-for-coding` | zh | 11 | 7 | `tools/api`、`tools/code-review`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/knowledge-base`、`tools/llm`、`tools/llm-for-math`、`tools/search-engine`、`tools/vibe-coding`、`tools/workflow` |
| `llm-for-math` | zh | 9 | 3 | `tools/api`、`tools/browser`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/llm`、`tools/llm-for-coding`、`tools/text-generator`、`tools/web-search-api` |
| `llm-for-reasoning` | zh | 10 | 2 | `tools/api`、`tools/browser`、`tools/directory`、`tools/geo`、`tools/llm`、`tools/llm-for-coding`、`tools/multimodal-llm`、`tools/search-engine`、`tools/text-generator`、`tools/web-search-api` |
| `logo-generator` | zh | 5 | 10 | `media-kit`、`tools/background-changer`、`tools/design`、`tools/image-generator`、`tools/poster-generator` |
| `memory` | zh | 4 📊 | 3 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `multimodal-llm` | zh | 9 | 2 | `tools/api`、`tools/documentation`、`tools/evaluation`、`tools/image-generator`、`tools/llm`、`tools/llm-for-math`、`tools/llm-for-reasoning`、`tools/web-search-api`、`tools/workflow` |
| `music-generator` | zh | 3 📊 | 3 | `tools/music-video-generator`、`tools/video-editor`、`tools/voice` |
| `music-video-generator` | zh | 5 | 4 | `tools/lip-sync`、`tools/music-generator`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-generator` |
| `note-taker` | zh | 3 📊 | 22 | `blog/medical-scribe`、`tools/speech-to-text`、`tools/text-generator` |
| `notes-generator` | zh | 3 📊 | 12 | `tools/note-taker`、`tools/text-generator`、`tools/voice-cloning` |
| `ocr` | zh | 3 📊 | 3 | `tools/image-enhancer`、`tools/knowledge-base`、`tools/text-to-speech` |
| `openclaw-alternatives` | zh | 4 📊 | 6 | `tools/agent-for-desktop`、`tools/api`、`tools/documentation`、`tools/knowledge-base` |
| `poster-generator` | zh | 5 | 6 | `tools/fashion`、`tools/image-editor`、`tools/image-generator`、`tools/logo-generator`、`tools/social-cards-generator` |
| `presentation-maker` | zh | 2 📊 | 5 | `tools/logo-generator`、`tools/text-generator` |
| `productivity` | zh | 3 📊 | 32 | `tools/ai-scheduling`、`tools/text-generator`、`tools/workflow` |
| `recruiting` | zh | 5 | 8 | `tools/documentation`、`tools/hr-assistant`、`tools/lead-generation`、`tools/note-taker`、`tools/productivity` |
| `referral-program` | zh | 4 📊 | 6 | `tools/affiliate-marketing`、`tools/influencer-marketing`、`tools/linkedin`、`tools/productivity` |
| `religion` | zh | 3 📊 | 1 | `tools/community`、`tools/knowledge-base`、`tools/text-translator` |
| `search-engine` | zh | 6 | 21 | `tools/browser`、`tools/evaluation`、`tools/geo`、`tools/knowledge-base`、`tools/text-generator`、`tools/web-search-api` |
| `search-indexing` | zh | 5 | 7 | `seo/internal-links`、`seo/website-structure`、`tools/search-engine`、`tools/web-search-api`、`tools/website-builder` |
| `short-drama` | zh | 3 📊 | 5 | `tools/animation-generator`、`tools/video-generator`、`tools/workflow` |
| `social-cards-generator` | zh | 5 | 4 | `tools/api`、`tools/geo`、`tools/image-generator`、`tools/logo-generator`、`tools/web-scraping` |
| `speech-to-text` | zh | 5 | 8 | `blog/medical-scribe`、`tools/accent-conversion`、`tools/note-taker`、`tools/video-translator`、`tools/voice-changer` |
| `spreadsheet` | zh | 3 📊 | 1 | `tools/app-builder`、`tools/productivity`、`tools/web-scraping` |
| `story-generator` | zh | 2 📊 | 4 | `tools/text-generator`、`tools/text-to-video` |
| `tattoo-generator` | zh | 3 📊 | 3 | `tools/image`、`tools/image-editor`、`tools/image-generator` |
| `text` | zh | 4 📊 | 2 | `tools/essay-writer`、`tools/story-generator`、`tools/text-generator`、`tools/text-to-speech` |
| `text-generator` | zh | 5 | 37 | `tools/chatbot`、`tools/coding`、`tools/essay-writer`、`tools/llm`、`tools/story-generator` |
| `text-to-speech` | zh | 2 📊 | 18 | `tools/voice-changer`、`tools/voice-cloning` |
| `text-to-video` | zh | 5 | 12 | `tools/image-to-video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `text-translator` | zh | 5 | 2 | `tools/audio-translator`、`tools/essay-writer`、`tools/llm`、`tools/text-generator`、`tools/video-translator` |
| `user-research` | zh | 2 📊 | 5 | `tools/ai-scheduling`、`tools/productivity` |
| `vibe-coding` | zh | 4 📊 | 16 | `blog/how-to-build-a-blog-without-a-cms-using-ai`、`tools/app-builder`、`tools/code-completion`、`tools/coding` |
| `video` | zh | 7 | 6 | `tools/canvas-video`、`tools/filmmaking`、`tools/image-to-video`、`tools/music-video-generator`、`tools/short-drama`、`tools/text-to-video`、`tools/video-generator` |
| `video-clipping` | zh | 5 | 12 | `tools/text-to-video`、`tools/video`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `video-editor` | zh | 6 | 25 | `tools/text-to-video`、`tools/video`、`tools/video-clipping`、`tools/video-effects`、`tools/video-generator`、`tools/video-to-video` |
| `video-effects` | zh | 5 | 8 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator`、`tools/video-to-video` |
| `video-generator` | zh | 7 | 32 | `tools/avatar`、`tools/image-to-video`、`tools/music-video-generator`、`tools/text-to-video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-to-video` ⚠重复 |
| `video-to-video` | zh | 6 | 12 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator`、`tools/video-translator` |
| `video-translator` | zh | 6 | 13 | `tools/lip-sync`、`tools/speech-to-text`、`tools/video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator` |
| `virtual-staging` | zh | 6 | 4 | `tools/3d`、`tools/background-changer`、`tools/headshot-generator`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator` |
| `voice` | zh | 4 📊 | 2 | `tools/notes-generator`、`tools/speech-to-text`、`tools/text-to-speech`、`tools/voice-cloning` |
| `voice-changer` | zh | 2 📊 | 11 | `tools/text-to-speech`、`tools/voice-cloning` |
| `voice-cloning` | zh | 4 📊 | 10 | `tools/audio-translator`、`tools/lip-sync`、`tools/text-to-speech`、`tools/voice-changer` |
| `web-scraping` | zh | 5 | 11 | `blog/web-fetch`、`tools/geo`、`tools/llm`、`tools/web-search-api`、`tools/workflow` |
| `web-search-api` | zh | 7 | 31 | `blog/web-fetch`、`tools/api`、`tools/geo`、`tools/llm`、`tools/search-indexing`、`tools/text-generator`、`tools/workflow` |
| `website-builder` | zh | 5 | 9 | `tools/coding`、`tools/design`、`tools/documentation`、`tools/image-generator`、`tools/vibe-coding` |
| `workflow` | zh | 7 | 29 | `blog/agent-to-agent`、`tools/agent-skills`、`tools/browser`、`tools/canvas-video`、`tools/coding`、`tools/productivity`、`tools/text-generator` |
| `world-model` | zh | 7 | 6 | `tools/3d`、`tools/image-to-video`、`tools/llm`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/video-to-video` |

### seo

| 文章 | 语言 | 出链 | 入链 | 出链目标 |
|------|------|-----:|-----:|---------|
| `best-tools` | en | 0 | 0 | — |
| `branded-queries-filter-google-search-console` | en | 0 | 0 | — |
| `breadcrumbs` | en | 4 | 12 | `marketing/geo`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap` ⚠重复 |
| `category-pages` | en | 5 | 4 | `seo/breadcrumbs`、`seo/internal-links`、`seo/navigation-menu`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `checklist` | en | 27 | 4 | `marketing/geo`、`seo/category-pages`、`seo/crawler`、`seo/create-blog`、`seo/external-links`、`seo/google-tag-manager`、`seo/how-search-engine-works`、`seo/html-tag`、`seo/internal-links`、`seo/landing-page`、`seo/learn-seo`、`seo/link-building`、`seo/meta-tag`、`seo/programmatic-seo`、`seo/redirect-chain`、`seo/robots-txt`、`seo/schema`、`seo/serp`、`seo/sitemap`、`seo/subdomain-vs-subfolder`、`seo/submit-website`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-rendering`、`seo/website-structure`、`seo/website-traffic`、`tools/geo` |
| `crawler` | en | 0 | 2 | — |
| `create-blog` | en | 0 | 2 | — |
| `dark-traffic` | en | 0 | 8 | — |
| `domain` | en | 4 | 2 | `seo/redirect-chain`、`seo/robots-txt`、`seo/submit-website`、`seo/website-structure` ⚠重复 |
| `example-article` | en | 0 | 0 | — |
| `external-links` | en | 0 | 3 | — |
| `glossary` | en | 0 | 0 | — |
| `google-tag-manager` | en | 0 | 2 | — |
| `how-search-engine-works` | en | 0 | 13 | — |
| `html-a-tag` | en | 0 | 1 | — |
| `html-tag` | en | 5 | 2 | `seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `internal-links` | en | 0 | 26 | — |
| `landing-page` | en | 0 | 4 | — |
| `learn-seo` | en | 3 | 6 | `glossary`、`seo/how-search-engine-works`、`seo/website-indexing` |
| `link-building` | en | 0 | 10 | — |
| `local-search-engines` | en | 0 | 2 | — |
| `meta-tag` | en | 0 | 13 | — |
| `navigation-menu` | en | 3 | 8 | `seo/html-a-tag`、`seo/internal-links`、`seo/website-structure` |
| `new-domains-tld` | en | 0 | 0 | — |
| `programmatic-seo` | en | 7 | 2 | `home`、`seo/category-pages`、`seo/internal-links`、`seo/sitemap`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-structure` |
| `redirect-chain` | en | 0 | 6 | — |
| `robots-txt` | en | 0 | 6 | — |
| `schema` | en | 5 | 10 | `marketing/geo`、`seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag`、`seo/sitemap` ⚠重复 |
| `search-engine` | en | 10 | 4 | `marketing/geo`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/local-search-engines`、`seo/schema`、`seo/website-traffic`、`tools/browser`、`tools/search-engine`、`tools/web-search-api` |
| `serp` | en | 0 | 5 | — |
| `sitemap` | en | 0 | 21 | — |
| `subdomain-vs-subfolder` | en | 0 | 8 | — |
| `submit-website` | en | 0 | 7 | — |
| `url-optimization` | en | 6 | 4 | `seo/breadcrumbs`、`seo/meta-tag`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `website-indexing` | en | 0 | 8 | — |
| `website-rendering` | en | 0 | 2 | — |
| `website-structure` | en | 2 | 24 | `seo/external-links`、`seo/internal-links` ⚠重复 |
| `website-traffic` | en | 4 | 6 | `seo/dark-traffic`、`seo/internal-links`、`seo/link-building`、`seo/website-structure` ⚠重复 |
| `best-tools` | zh | 0 | 0 | — |
| `branded-queries-filter-google-search-console` | zh | 0 | 0 | — |
| `breadcrumbs` | zh | 5 | 12 | `marketing/geo`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap`、`seo/submit-website` ⚠重复 |
| `category-pages` | zh | 5 | 4 | `seo/breadcrumbs`、`seo/internal-links`、`seo/navigation-menu`、`seo/sitemap`、`seo/website-structure` |
| `checklist` | zh | 28 | 4 | `marketing/geo`、`marketing/keyword-research`、`seo/category-pages`、`seo/crawler`、`seo/create-blog`、`seo/external-links`、`seo/google-tag-manager`、`seo/how-search-engine-works`、`seo/html-tag`、`seo/internal-links`、`seo/landing-page`、`seo/learn-seo`、`seo/link-building`、`seo/meta-tag`、`seo/programmatic-seo`、`seo/redirect-chain`、`seo/robots-txt`、`seo/schema`、`seo/serp`、`seo/sitemap`、`seo/subdomain-vs-subfolder`、`seo/submit-website`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-rendering`、`seo/website-structure`、`seo/website-traffic`、`tools/geo` |
| `crawler` | zh | 0 | 2 | — |
| `create-blog` | zh | 0 | 2 | — |
| `dark-traffic` | zh | 0 | 8 | — |
| `domain` | zh | 4 | 2 | `seo/redirect-chain`、`seo/robots-txt`、`seo/submit-website`、`seo/website-structure` ⚠重复 |
| `example-article` | zh | 0 | 0 | — |
| `external-links` | zh | 0 | 3 | — |
| `glossary` | zh | 0 | 0 | — |
| `google-tag-manager` | zh | 0 | 2 | — |
| `how-search-engine-works` | zh | 0 | 13 | — |
| `html-a-tag` | zh | 0 | 1 | — |
| `html-tag` | zh | 4 | 2 | `seo/internal-links`、`seo/meta-tag`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `internal-links` | zh | 0 | 26 | — |
| `landing-page` | zh | 0 | 4 | — |
| `learn-seo` | zh | 3 | 6 | `glossary`、`seo/how-search-engine-works`、`seo/website-indexing` |
| `link-building` | zh | 0 | 10 | — |
| `local-search-engines` | zh | 0 | 2 | — |
| `meta-tag` | zh | 0 | 13 | — |
| `navigation-menu` | zh | 3 | 8 | `seo`、`seo/robots-txt`、`seo/sitemap` |
| `new-domains-tld` | zh | 0 | 0 | — |
| `programmatic-seo` | zh | 7 | 2 | `seo/category-pages`、`seo/internal-links`、`seo/sitemap`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-structure`、`zh` |
| `redirect-chain` | zh | 0 | 6 | — |
| `robots-txt` | zh | 0 | 6 | — |
| `schema` | zh | 6 | 10 | `marketing/geo`、`seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag`、`seo/serp`、`seo/sitemap` ⚠重复 |
| `search-engine` | zh | 10 | 4 | `marketing/geo`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/local-search-engines`、`seo/schema`、`seo/website-traffic`、`tools/browser`、`tools/search-engine`、`tools/web-search-api` |
| `serp` | zh | 0 | 5 | — |
| `sitemap` | zh | 2 | 21 | `seo/internal-links`、`seo/website-indexing` ⚠重复 |
| `subdomain-vs-subfolder` | zh | 0 | 8 | — |
| `submit-website` | zh | 0 | 7 | — |
| `url-optimization` | zh | 6 | 4 | `seo/breadcrumbs`、`seo/meta-tag`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `website-indexing` | zh | 0 | 8 | — |
| `website-rendering` | zh | 0 | 2 | — |
| `website-structure` | zh | 0 | 24 | — |
| `website-traffic` | zh | 4 | 6 | `seo/dark-traffic`、`seo/internal-links`、`seo/link-building`、`seo/website-structure` ⚠重复 |

### blog

| 文章 | 语言 | 出链 | 入链 | 出链目标 |
|------|------|-----:|-----:|---------|
| `agent-memory` | en | 5 | 3 | `blog/agent-sandbox`、`blog/ai-training-data`、`tools/agent-skills`、`tools/knowledge-base`、`tools/openclaw-alternatives` |
| `agent-sandbox` | en | 4 | 10 | `blog/inference-infrastructure`、`tools/agent-for-desktop`、`tools/authentication`、`tools/headless-browser` |
| `agent-to-agent` | en | 5 | 4 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/character-chat`、`tools/community`、`tools/workflow` |
| `agentic-commerce` | en | 5 | 5 | `tools/affiliate-marketing`、`tools/chatbot`、`tools/geo`、`tools/memory`、`tools/search-engine` |
| `agentic-payments` | en | 5 | 3 | `blog/agentic-commerce`、`tools/agent-skills`、`tools/api`、`tools/openclaw-alternatives`、`tools/web-search-api` |
| `ai-components` | en | 2 | 0 | `tools/app-builder`、`tools/design` |
| `ai-flashcards` | en | 3 | 2 | `blog/ai-language-learning`、`tools/ai-homework-helper`、`tools/notes-generator` |
| `ai-language-learning` | en | 2 | 2 | `blog/ai-flashcards`、`tools/ai-homework-helper` |
| `ai-traffic-and-citation-sources` | en | 2 | 7 | `blog/ai-visibility`、`tools/geo` ⚠重复 |
| `ai-training-data` | en | 5 | 4 | `blog/inference-infrastructure`、`tools/evaluation`、`tools/llm`、`tools/web-scraping`、`tools/world-model` |
| `ai-visibility` | en | 3 | 3 | `blog/ai-traffic-and-citation-sources`、`tools/geo`、`tools/search-engine` |
| `cad` | en | 4 | 6 | `blog/interior-design`、`tools/3d`、`tools/3d-model-generator`、`tools/workflow` |
| `coding-plan` | en | 6 | 17 | `blog/rate-limit-reset`、`marketing/competitive-analysis`、`marketing/geo`、`marketing/pricing-strategy`、`marketing/referral-program`、`marketing/x-formerly-twitter` ⚠重复 |
| `data-engineering-agent` | en | 3 | 3 | `blog/inference-infrastructure`、`tools/agent-skills`、`tools/api` |
| `embedded-virality` | en | 11 | 23 | `blog/coding-plan`、`blog/git-commit-attribution`、`blog/how-to-add-payments-to-vibe-coded-app`、`blog/platform-subdomain-gating`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`blog/watermark-growth`、`marketing/creator-challenge-program`、`marketing/lifetime-deal`、`marketing/pricing-strategy`、`tools/social-cards-generator` ⚠重复 |
| `git-commit-attribution` | en | 5 | 8 | `blog/coding-plan`、`blog/embedded-virality`、`blog/rate-limit-reset`、`marketing/competitive-analysis`、`marketing/pricing-strategy` |
| `git-hosting` | en | 4 | 2 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/cli`、`tools/code-review` ⚠重复 |
| `github-for-marketing` | en | 2 | 4 | `blog/how-to-build-a-blog-without-a-cms-using-ai`、`blog/how-to-write-github-readme` |
| `how-to-add-payments-to-vibe-coded-app` | en | 5 | 4 | `blog/agentic-payments`、`blog/ai-traffic-and-citation-sources`、`insights/indie-hackers`、`tools/app-builder`、`tools/vibe-coding` |
| `how-to-build-a-blog-without-a-cms-using-ai` | en | 11 | 12 | `blog/git-hosting`、`blog/github-for-marketing`、`blog/subdirectory-hosting`、`glossary/seo`、`seo/sitemap`、`seo/subdomain-vs-subfolder`、`skills`、`tools/agent-skills`、`tools/app-builder`、`tools/ide`、`tools/vibe-coding` ⚠重复 |
| `how-to-name-ai-products` | en | 1 | 0 | `seo/domain` |
| `how-to-write-github-readme` | en | 1 | 2 | `blog/github-for-marketing` |
| `inference-infrastructure` | en | 2 | 6 | `blog/agent-sandbox`、`blog/ai-training-data` |
| `interior-design` | en | 4 | 4 | `blog/cad`、`tools/background-changer`、`tools/image-enhancer`、`tools/image-generator` |
| `medical-scribe` | en | 4 | 6 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/speech-to-text` |
| `multi-agent` | en | 5 | 6 | `blog/agent-sandbox`、`tools/agent-for-desktop`、`tools/hr-assistant`、`tools/llm`、`tools/workflow` |
| `platform-subdomain-gating` | en | 10 | 5 | `blog/coding-plan`、`blog/embedded-virality`、`blog/git-commit-attribution`、`blog/how-to-add-payments-to-vibe-coded-app`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`blog/watermark-growth`、`marketing/lifetime-deal`、`marketing/pricing-strategy`、`seo/subdomain-vs-subfolder` ⚠重复 |
| `rate-limit-reset` | en | 5 | 20 | `blog/coding-plan`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/pricing-strategy`、`marketing/x-formerly-twitter` ⚠重复 |
| `subdirectory-hosting` | en | 4 | 4 | `audit-website-by-lovable`、`blog/how-to-build-a-blog-without-a-cms-using-ai`、`seo/sitemap`、`seo/subdomain-vs-subfolder` ⚠重复 |
| `ugc-marketing` | en | 7 | 18 | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/influencer`、`marketing/marketing-types`、`seo/landing-page` ⚠重复 |
| `watermark-growth` | en | 7 | 14 | `blog/embedded-virality`、`blog/platform-subdomain-gating`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`marketing/creator-challenge-program`、`marketing/lifetime-deal`、`marketing/pricing-strategy` ⚠重复 |
| `web-fetch` | en | 6 | 2 | `blog/data-engineering-agent`、`tools/headless-browser`、`tools/llm`、`tools/search-indexing`、`tools/web-scraping`、`tools/web-search-api` |
| `wrapped-marketing` | en | 4 | 2 | `blog/rate-limit-reset`、`blog/ugc-marketing`、`marketing/creator-challenge-program`、`marketing/pricing-strategy` |
| `agent-memory` | zh | 5 | 3 | `blog/agent-sandbox`、`blog/ai-training-data`、`tools/agent-skills`、`tools/knowledge-base`、`tools/openclaw-alternatives` |
| `agent-sandbox` | zh | 5 | 10 | `blog/agent-to-agent`、`blog/inference-infrastructure`、`tools/agent-for-desktop`、`tools/authentication`、`tools/headless-browser` |
| `agent-to-agent` | zh | 6 | 4 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/agent-skills`、`tools/character-chat`、`tools/community`、`tools/workflow` |
| `agentic-commerce` | zh | 6 | 5 | `blog/agentic-payments`、`tools/affiliate-marketing`、`tools/chatbot`、`tools/geo`、`tools/memory`、`tools/search-engine` |
| `agentic-payments` | zh | 5 | 3 | `blog/agentic-commerce`、`tools/agent-skills`、`tools/api`、`tools/openclaw-alternatives`、`tools/web-search-api` |
| `ai-components` | zh | 2 | 0 | `tools/app-builder`、`tools/design` |
| `ai-flashcards` | zh | 3 | 2 | `blog/ai-language-learning`、`tools/ai-homework-helper`、`tools/notes-generator` |
| `ai-language-learning` | zh | 2 | 2 | `blog/ai-flashcards`、`tools/ai-homework-helper` |
| `ai-traffic-and-citation-sources` | zh | 2 | 7 | `blog/ai-visibility`、`tools/geo` ⚠重复 |
| `ai-training-data` | zh | 6 | 4 | `blog/data-engineering-agent`、`blog/inference-infrastructure`、`tools/evaluation`、`tools/llm`、`tools/web-scraping`、`tools/world-model` |
| `ai-visibility` | zh | 4 | 3 | `blog/ai-traffic-and-citation-sources`、`tools/geo`、`tools/search-engine`、`tools/text-generator` |
| `cad` | zh | 4 | 6 | `blog/interior-design`、`tools/3d`、`tools/3d-model-generator`、`tools/workflow` |
| `coding-plan` | zh | 6 | 17 | `blog/rate-limit-reset`、`marketing/competitive-analysis`、`marketing/geo`、`marketing/pricing-strategy`、`marketing/referral-program`、`marketing/x-formerly-twitter` ⚠重复 |
| `data-engineering-agent` | zh | 3 | 3 | `blog/inference-infrastructure`、`tools/agent-skills`、`tools/api` |
| `embedded-virality` | zh | 11 | 23 | `blog/coding-plan`、`blog/git-commit-attribution`、`blog/how-to-add-payments-to-vibe-coded-app`、`blog/platform-subdomain-gating`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`blog/watermark-growth`、`marketing/creator-challenge-program`、`marketing/lifetime-deal`、`marketing/pricing-strategy`、`tools/social-cards-generator` ⚠重复 |
| `git-commit-attribution` | zh | 5 | 8 | `blog/coding-plan`、`blog/embedded-virality`、`blog/rate-limit-reset`、`marketing/competitive-analysis`、`marketing/pricing-strategy` |
| `git-hosting` | zh | 4 | 2 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/cli`、`tools/code-review` ⚠重复 |
| `github-for-marketing` | zh | 2 | 4 | `blog/how-to-build-a-blog-without-a-cms-using-ai`、`blog/how-to-write-github-readme` |
| `how-to-add-payments-to-vibe-coded-app` | zh | 5 | 4 | `blog/agentic-payments`、`blog/ai-traffic-and-citation-sources`、`insights/indie-hackers`、`tools/app-builder`、`tools/vibe-coding` |
| `how-to-build-a-blog-without-a-cms-using-ai` | zh | 11 | 12 | `blog/git-hosting`、`blog/github-for-marketing`、`blog/subdirectory-hosting`、`glossary/seo`、`seo/sitemap`、`seo/subdomain-vs-subfolder`、`skills`、`tools/agent-skills`、`tools/app-builder`、`tools/ide`、`tools/vibe-coding` ⚠重复 |
| `how-to-name-ai-products` | zh | 1 | 0 | `seo/domain` |
| `how-to-write-github-readme` | zh | 1 | 2 | `blog/github-for-marketing` |
| `inference-infrastructure` | zh | 3 | 6 | `blog/agent-sandbox`、`blog/ai-training-data`、`tools/agent-skills` |
| `interior-design` | zh | 4 | 4 | `blog/cad`、`tools/background-changer`、`tools/image-enhancer`、`tools/image-generator` |
| `medical-scribe` | zh | 5 | 6 | `tools/chatbot`、`tools/knowledge-base`、`tools/legal`、`tools/note-taker`、`tools/speech-to-text` |
| `multi-agent` | zh | 8 | 6 | `blog/agent-sandbox`、`blog/agent-to-agent`、`tools/agent-for-desktop`、`tools/agent-skills`、`tools/hr-assistant`、`tools/llm`、`tools/openclaw-alternatives`、`tools/workflow` |
| `platform-subdomain-gating` | zh | 10 | 5 | `blog/coding-plan`、`blog/embedded-virality`、`blog/git-commit-attribution`、`blog/how-to-add-payments-to-vibe-coded-app`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`blog/watermark-growth`、`marketing/lifetime-deal`、`marketing/pricing-strategy`、`seo/subdomain-vs-subfolder` ⚠重复 |
| `rate-limit-reset` | zh | 5 | 20 | `blog/coding-plan`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/pricing-strategy`、`marketing/x-formerly-twitter` ⚠重复 |
| `subdirectory-hosting` | zh | 4 | 4 | `audit-website-by-lovable`、`blog/how-to-build-a-blog-without-a-cms-using-ai`、`seo/sitemap`、`seo/subdomain-vs-subfolder` ⚠重复 |
| `ugc-marketing` | zh | 6 | 18 | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/influencer`、`marketing/marketing-types` ⚠重复 |
| `watermark-growth` | zh | 7 | 14 | `blog/embedded-virality`、`blog/platform-subdomain-gating`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`marketing/creator-challenge-program`、`marketing/lifetime-deal`、`marketing/pricing-strategy` ⚠重复 |
| `web-fetch` | zh | 6 | 2 | `blog/data-engineering-agent`、`tools/headless-browser`、`tools/llm`、`tools/search-indexing`、`tools/web-scraping`、`tools/web-search-api` |
| `wrapped-marketing` | zh | 4 | 2 | `blog/rate-limit-reset`、`blog/ugc-marketing`、`marketing/creator-challenge-program`、`marketing/pricing-strategy` |

### marketing

| 文章 | 语言 | 出链 | 入链 | 出链目标 |
|------|------|-----:|-----:|---------|
| `affiliate` | en | 3 | 25 | `marketing/creator-challenge-program`、`marketing/creator-program`、`tools/affiliate-marketing` ⚠重复 |
| `competitive-analysis` | en | 2 | 18 | `marketing/email-marketing`、`marketing/keyword-research` ⚠重复 |
| `creator-challenge-program` | en | 6 | 22 | `blog/embedded-virality`、`blog/ugc-marketing`、`blog/watermark-growth`、`marketing/affiliate`、`marketing/creator-program`、`marketing/marketing-types` |
| `creator-program` | en | 4 | 19 | `marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/influencer`、`marketing/marketing-types` ⚠重复 |
| `email-marketing` | en | 1 | 6 | `marketing/keyword-research` ⚠重复 |
| `geo` | en | 6 | 28 | `marketing/affiliate`、`marketing/creator-program`、`marketing/influencer`、`marketing/marketing-types`、`seo/how-search-engine-works`、`seo/search-engine` ⚠重复 |
| `growth-case-studies` | en | 0 | 2 | — |
| `influencer` | en | 4 | 10 | `blog/ugc-marketing`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program` ⚠重复 |
| `keyword-research` | en | 2 | 22 | `marketing/geo`、`marketing/marketing-types` |
| `lifetime-deal` | en | 7 | 15 | `blog/coding-plan`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/creator-program`、`marketing/pricing-strategy`、`marketing/referral-program`、`seo/landing-page` |
| `localization-strategy` | en | 1 | 4 | `seo/navigation-menu` |
| `marketing-types` | en | 14 | 12 | `blog/coding-plan`、`blog/embedded-virality`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`blog/watermark-growth`、`blog/wrapped-marketing`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/geo`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/pricing-strategy`、`marketing/referral-program` |
| `pricing-strategy` | en | 4 | 30 | `blog/coding-plan`、`marketing/competitive-analysis`、`marketing/lifetime-deal`、`marketing/marketing-types` ⚠重复 |
| `reddit` | en | 0 | 5 | — |
| `referral-program` | en | 2 | 9 | `blog/coding-plan`、`tools/referral-program` |
| `x-formerly-twitter` | en | 2 | 9 | `insights/indie-hackers`、`marketing/influencer` |
| `affiliate` | zh | 7 | 25 | `blog/ugc-marketing`、`marketing/competitive-analysis`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/influencer`、`marketing/pricing-strategy`、`marketing/referral-program` ⚠重复 |
| `competitive-analysis` | zh | 6 | 18 | `blog/coding-plan`、`marketing/email-marketing`、`marketing/geo`、`marketing/influencer`、`marketing/keyword-research`、`marketing/pricing-strategy` ⚠重复 |
| `creator-challenge-program` | zh | 6 | 22 | `blog/embedded-virality`、`blog/ugc-marketing`、`blog/watermark-growth`、`marketing/affiliate`、`marketing/creator-program`、`marketing/marketing-types` |
| `creator-program` | zh | 5 | 19 | `blog/ugc-marketing`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/influencer`、`marketing/marketing-types` ⚠重复 |
| `email-marketing` | zh | 1 | 6 | `marketing/keyword-research` |
| `geo` | zh | 7 | 28 | `marketing/affiliate`、`marketing/creator-program`、`marketing/influencer`、`marketing/keyword-research`、`marketing/marketing-types`、`seo/how-search-engine-works`、`seo/search-engine` |
| `growth-case-studies` | zh | 3 | 2 | `marketing/affiliate`、`marketing/keyword-research`、`marketing/referral-program` |
| `influencer` | zh | 4 | 10 | `blog/ugc-marketing`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program` ⚠重复 |
| `keyword-research` | zh | 3 | 22 | `marketing/competitive-analysis`、`marketing/geo`、`marketing/marketing-types` |
| `lifetime-deal` | zh | 6 | 15 | `blog/coding-plan`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/creator-program`、`marketing/pricing-strategy`、`marketing/referral-program` |
| `localization-strategy` | zh | 2 | 4 | `marketing/keyword-research`、`seo/navigation-menu` |
| `marketing-types` | zh | 14 | 12 | `blog/coding-plan`、`blog/embedded-virality`、`blog/rate-limit-reset`、`blog/ugc-marketing`、`blog/watermark-growth`、`blog/wrapped-marketing`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/geo`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/pricing-strategy`、`marketing/referral-program` |
| `pricing-strategy` | zh | 7 | 30 | `blog/coding-plan`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/geo`、`marketing/lifetime-deal`、`marketing/marketing-types`、`marketing/referral-program` ⚠重复 |
| `reddit` | zh | 2 | 5 | `marketing/geo`、`marketing/x-formerly-twitter` |
| `referral-program` | zh | 4 | 9 | `blog/coding-plan`、`marketing/affiliate`、`marketing/pricing-strategy`、`tools/referral-program` |
| `x-formerly-twitter` | zh | 4 | 9 | `insights/indie-hackers`、`marketing/influencer`、`marketing/reddit`、`seo/meta-tag` |

### insights

| 文章 | 语言 | 出链 | 入链 | 出链目标 |
|------|------|-----:|-----:|---------|
| `ai-logo-design` | en | 3 | 0 | `marketing/competitive-analysis`、`tools`、`tools/logo-generator` ⚠重复 |
| `directory-submission-sites` | en | 9 | 6 | `insights/reasons-you-need-seo`、`marketing`、`marketing/geo`、`marketing/keyword-research`、`seo/how-search-engine-works`、`seo/internal-links`、`seo/link-building`、`seo/submit-website`、`seo/website-structure` |
| `generative-ai-landscape` | en | 1 | 0 | `marketing/pricing-strategy` |
| `google` | en | 0 | 0 | — |
| `indie-hackers` | en | 15 | 6 | `insights/directory-submission-sites`、`insights/reasons-you-need-seo`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/email-marketing`、`marketing/geo`、`marketing/growth-case-studies`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/localization-strategy`、`marketing/pricing-strategy`、`marketing/reddit`、`marketing/x-formerly-twitter`、`tools`、`tools/app-builder` ⚠重复 |
| `openai` | en | 0 | 0 | — |
| `reasons-you-need-seo` | en | 8 | 7 | `insights/indie-hackers`、`marketing/geo`、`marketing/keyword-research`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/serp`、`seo/website-traffic` |
| `ai-logo-design` | zh | 3 | 0 | `marketing/competitive-analysis`、`tools`、`tools/logo-generator` ⚠重复 |
| `directory-submission-sites` | zh | 9 | 6 | `insights/reasons-you-need-seo`、`marketing`、`marketing/geo`、`marketing/keyword-research`、`seo/how-search-engine-works`、`seo/internal-links`、`seo/link-building`、`seo/submit-website`、`seo/website-structure` |
| `generative-ai-landscape` | zh | 1 | 0 | `marketing/pricing-strategy` |
| `google` | zh | 0 | 0 | — |
| `indie-hackers` | zh | 15 | 6 | `insights/directory-submission-sites`、`insights/reasons-you-need-seo`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/email-marketing`、`marketing/geo`、`marketing/growth-case-studies`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/localization-strategy`、`marketing/pricing-strategy`、`marketing/reddit`、`marketing/x-formerly-twitter`、`tools`、`tools/app-builder` ⚠重复 |
| `openai` | zh | 0 | 0 | — |
| `reasons-you-need-seo` | zh | 8 | 7 | `insights/indie-hackers`、`marketing/geo`、`marketing/keyword-research`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/serp`、`seo/website-traffic` |

### events

| 文章 | 语言 | 出链 | 入链 | 出链目标 |
|------|------|-----:|-----:|---------|
| `founder-park-2024-11-06` | en | 0 | 0 | — |
| `linkloud-2025-02-23` | en | 1 | 0 | `tools/design` |
| `linkloud-2026-01-24` | en | 0 | 0 | — |
| `praxis-2025-09-27` | en | 1 | 0 | `seo/search-engine` |
| `founder-park-2024-11-06` | zh | 0 | 0 | — |
| `linkloud-2025-02-23` | zh | 1 | 0 | `tools/design` |
| `linkloud-2026-01-24` | zh | 0 | 0 | — |
| `praxis-2025-09-27` | zh | 1 | 0 | `seo/search-engine` |

## 七、Marketing / GTM 内链专项

> **规则**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 4.5（M1–M11）
> **Cluster 矩阵与逐页指令**：[`marketing-internal-links-backlog.md`](marketing-internal-links-backlog.md)（人工维护；本节 §7.2–7.3 为脚本快照）

### 7.1 范围

- **`/marketing/*`**：16 slug × 2 语言 = **32** 篇
- **`/blog/*` 增长策略**：8 slug × 2 语言 = **16** 篇（`ugc-marketing` 等已迁 `/blog/`，勿按 `/marketing/` 查）

### 7.2 快照摘要

| 分区 | 语言 | 篇数 | 零出链 | 堆链/重复 | 零入链 |
|------|------|-----:|-------:|----------:|-------:|
| marketing | en | 16 | 2 | 9 | 0 |
| marketing | zh | 16 | 0 | 7 | 0 |
| blog GTM | en | 8 | 0 | 6 | 0 |
| blog GTM | zh | 8 | 0 | 6 | 0 |

**典型待办**：EN `/marketing/*` 零出链孤岛 · `geo` / `lifetime-deal` 堆链 · `blog/wrapped-marketing` 零入链 · blog GTM 8 篇互链（Batch 5）。

### 7.3 逐页现状（自动）

#### `/marketing/*`

| slug | en 出 | zh 出 | en 入 | zh 入 | 标记 |
|------|------:|------:|------:|------:|------|
| `affiliate` | 3 | 7 | 25 | 25 | 堆链 · EN/ZH不对称 |
| `competitive-analysis` | 2 | 6 | 18 | 18 | 堆链 · EN/ZH不对称 |
| `creator-challenge-program` | 6 | 6 | 22 | 22 | ✓ |
| `creator-program` | 4 | 5 | 19 | 19 | 堆链 |
| `email-marketing` | 1 | 1 | 6 | 6 | 堆链 |
| `geo` | 6 | 7 | 28 | 28 | 堆链 |
| `growth-case-studies` | 0 | 3 | 2 | 2 | 零出 · EN/ZH不对称 |
| `influencer` | 4 | 4 | 10 | 10 | 堆链 |
| `keyword-research` | 2 | 3 | 22 | 22 | ✓ |
| `lifetime-deal` | 7 | 6 | 15 | 15 | 堆链 |
| `localization-strategy` | 1 | 2 | 4 | 4 | ✓ |
| `marketing-types` | 14 | 14 | 12 | 12 | 堆链 |
| `pricing-strategy` | 4 | 7 | 30 | 30 | 堆链 · EN/ZH不对称 |
| `reddit` | 0 | 2 | 5 | 5 | 零出 |
| `referral-program` | 2 | 4 | 9 | 9 | ✓ |
| `x-formerly-twitter` | 2 | 4 | 9 | 9 | ✓ |

#### `/blog/*` 增长策略

| slug | en 出 | zh 出 | en 入 | zh 入 | 标记 |
|------|------:|------:|------:|------:|------|
| `coding-plan` | 6 | 6 | 17 | 17 | 堆链 |
| `embedded-virality` | 11 | 11 | 23 | 23 | 堆链 |
| `git-commit-attribution` | 5 | 5 | 8 | 8 | ✓ |
| `platform-subdomain-gating` | 10 | 10 | 5 | 5 | 堆链 |
| `rate-limit-reset` | 5 | 5 | 20 | 20 | 堆链 |
| `ugc-marketing` | 7 | 6 | 18 | 18 | 堆链 |
| `watermark-growth` | 7 | 7 | 14 | 14 | 堆链 |
| `wrapped-marketing` | 4 | 4 | 2 | 2 | ✓ |

### 7.4 Cluster 矩阵 · 逐页指令 · 执行批次

> **快照与逐页出/入链**：见 [`site-structure-internal-links.md`](./site-structure-internal-links.md) **§7.3**（脚本自动生成，勿在此重复写「现状」数字）  
> **规则 SSOT**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 4.5（M1–M11）

---

## 一、Cluster 互链矩阵（应链向 · 应被链自）

> **现状列**：以 §7.3 自动快照为准（✓ 2+ 出链且无堆链标记 · △ 薄链/EN-ZH 不对称 · ✗ 零出链或零入链 · ⚠ 出链过多或同篇重复）

### 1.1 `/marketing/*` — Research 基础

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **keyword-research** | A | competitive-analysis, seo/learn-seo | competitive-analysis, geo, indie-hackers, reasons-you-need-seo |
| **competitive-analysis** | A | keyword-research, email-marketing | pricing, geo, lifetime-deal, keyword-research, blog/coding-plan |

### 1.2 `/marketing/*` — GTM 定价

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **pricing-strategy** | A | competitive-analysis, lifetime-deal, blog/coding-plan | geo, lifetime-deal, indie-hackers, blog/coding-plan |
| **lifetime-deal** | C | pricing-strategy, blog/rate-limit-reset, affiliate | pricing, blog/ugc-marketing, indie-hackers |
| **growth-case-studies** | C | competitive-analysis, geo | indie-hackers |

### 1.3 `/marketing/*` — Creator 生态

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **creator-program** | C | creator-challenge-program, affiliate, blog/ugc-marketing | geo, influencer, lifetime-deal, blog/ugc-marketing |
| **creator-challenge-program** | C | creator-program, blog/ugc-marketing, blog/watermark-growth, blog/embedded-virality, affiliate | blog/ugc-marketing, wrapped-marketing |
| **influencer** | C | creator-program, affiliate, blog/ugc-marketing | geo, blog/ugc-marketing, reddit |
| **affiliate** | C | referral-program, creator-program | geo, influencer, blog/ugc-marketing, lifetime-deal |
| **referral-program** | C | affiliate, tools/referral-program, blog/coding-plan | blog/ugc-marketing, lifetime-deal |

### 1.4 `/marketing/*` — Channel 战术

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **geo** | B | blog/ai-visibility, blog/ai-traffic-and-citation-sources, tools/geo, seo/search-engine | 全站高频 |
| **x-formerly-twitter** | B | blog/rate-limit-reset, influencer, indie-hackers | blog/coding-plan, blog/rate-limit-reset |
| **reddit** | B | influencer, x-formerly-twitter | indie-hackers |
| **email-marketing** | B | competitive-analysis, keyword-research | competitive-analysis |
| **localization-strategy** | B | seo/navigation-menu, seo/submit-website | indie-hackers |

### 1.5 `/marketing/*` — Hub

| slug | 类型 | 应链向（出） | 应被链自 |
|------|------|-------------|----------|
| **marketing-types** | Hub | pricing-strategy, geo, creator-program, keyword-research（各 1） | 全站 Hub 页 |

### 1.6 `/blog/*` — 增长策略（GTM · category=marketing）

| slug | 应链向 | 组合拳节 |
|------|--------|----------|
| **coding-plan** | rate-limit-reset(×1), pricing, competitive-analysis, referral, x, geo | 各 H2 分散，gtm-combo **0 链** |
| **rate-limit-reset** | pricing(×1), coding-plan, affiliate, competitive-analysis, x | 组合拳 1–2 链，勿堆 |
| **ugc-marketing** | creator-program, affiliate, influencer, rate-limit-reset, lifetime-deal, creator-challenge | 表无链；结论 ≤2 链 |
| **wrapped-marketing** | rate-limit-reset, creator-challenge-program, pricing-strategy, blog/ugc-marketing | Q4 仪式对照 |
| **embedded-virality** | git-commit-attribution, watermark-growth, platform-subdomain-gating, pricing-strategy | badge 族互链 |
| **watermark-growth** | embedded-virality, pricing-strategy, platform-subdomain-gating | 导出 watermark 轴 |
| **platform-subdomain-gating** | embedded-virality, watermark-growth, seo/subdomain-vs-subfolder | URL 门控轴 |
| **git-commit-attribution** | embedded-virality, blog/coding-plan, blog/github-for-marketing | 开发者向 embedded |

---

## 二、逐页优化指令（EN/ZH 同步）

> 每页目标：**4–5 distinct 出链**，**每段 ≤1 链**，**同 slug 不重复**。下列「删/移/加」以 **ZH 段落逻辑**为准，EN 镜像。

### P0 — 堆链 / 重复 / 零入链

#### `geo`

| 动作 | 说明 |
|------|------|
| **删** | §什么是 段 1：affiliate + influencer + creator-program **只留 1 条**（建议 creator-program） |
| **移** | affiliate / influencer 移到对应战术节各 1 链 |
| **保留** | blog/ai-traffic, blog/ai-visibility, tools/geo, seo/search-engine 各 1，分处不同 H2 |

#### `lifetime-deal`

| 动作 | 说明 |
|------|------|
| **删** | 结论段 pricing-strategy 链（§什么是 已有） |
| **移** | rate-limit-reset 仅 §专题对照 1 次 |
| **保留** | pricing, rate-limit-reset, referral, competitive-analysis, creator-program, affiliate — **6** 个 H2 分散 |
| **加** | §风险 链 **blog/coding-plan**（订阅 vs LTD，1 句） |

#### `blog/ugc-marketing`

| 动作 | 说明 |
|------|------|
| **删** | 对比表内链 → 表无链，§什么是 用 1 链区分 creator-program |
| **移** | affiliate+referral 合并段内 **1 链** |
| **全局** | influencer、creator-program 至少 1 处链入 |

#### `marketing-types`（Hub）

| 动作 | 说明 |
|------|------|
| **加** | pricing-strategy, geo, creator-program, keyword-research — 分类介绍各 1 链 |

### P1 — EN 零出链孤岛

| slug | 什么是 | 主体 1 | 主体 2 | 结论/案例 |
|------|--------|--------|--------|-----------|
| **affiliate** | vs referral-program | creator-program | competitive-analysis | tools/affiliate-marketing |
| **creator-program** | vs ugc-marketing | creator-challenge-program | affiliate | influencer |
| **creator-challenge-program** | vs creator-program | ugc-marketing | watermark-growth / embedded-virality | affiliate |
| **influencer** | vs creator-program | affiliate | ugc-marketing | tools/influencer-marketing |
| **reddit** | vs x-formerly-twitter | influencer | geo | — |
| **x-formerly-twitter** | vs reddit | blog/rate-limit-reset | influencer | — |
| **localization-strategy** | seo/navigation-menu | seo/submit-website | competitive-analysis | — |
| **growth-case-studies** | competitive-analysis | geo | blog/coding-plan 或 rate-limit-reset | — |
| **referral-program** | coding-plan | affiliate | tools/referral-program | — |
| **keyword-research**（EN） | competitive-analysis | seo/learn-seo | — | — |

### P2 — 微调

| slug | 动作 |
|------|------|
| **competitive-analysis** | 加 blog/coding-plan 于框架节 1 链 |
| **email-marketing** | 保持 2–3 链；keyword / competitive 不同段 |
| **pricing-strategy** | 已有 coding-plan + competitive + lifetime-deal；结论 **0 链** |

---

## 三、Blog × Marketing 组合拳（coding-plan / rate-limit-reset）

| 页 | reset | pricing | referral | competitive | geo | x |
|----|-------|---------|----------|-------------|-----|---|
| coding-plan | §什么是 ×1 | §架构 | §方舟 | §百炼 | §风险 | §vs OpenAI |
| rate-limit-reset | — | §什么是 ×1 | §banked | §benchmark | — | §X 节奏 |
| gtm-combo | **0** | **0** | **0** | **0** | **0** | **0** |

---

## 四、执行批次

| 批次 | 页面 | 验收 |
|------|------|------|
| **Batch 1** | geo, lifetime-deal, blog/ugc-marketing | 无段 ≥2 链；ugc 入链 ≥3 |
| **Batch 2** | affiliate, creator-program, influencer, creator-challenge（**EN 优先**） | 每页 4 distinct |
| **Batch 3** | reddit, x, localization, growth-case-studies, marketing-types | 零 EN 孤岛消除 |
| **Batch 4** | keyword-research, competitive-analysis, email, pricing, referral | 微调 + 去重 |
| **Batch 5** | blog 增长策略 8 篇互链 | embedded ↔ watermark ↔ platform-subdomain 三角 |

**Done 定义**：4–6 distinct 出链 · 段 ≤1 链 · 同 URL 1 次 · EN/ZH 同构 · 跑 `build-site-internal-links-doc.py` 刷新 §7

---

*维护：改版 Marketing / blog GTM 正文后更新矩阵「应链向」；快照数字只信 §7.3，勿写死在本文件。*

---

## 八、维护说明

1. **刷新本文**：`python scripts/audit/build-site-internal-links-doc.py`
2. **Marketing backlog**：改 [`marketing-internal-links-backlog.md`](marketing-internal-links-backlog.md) 后重跑上一条（§7.4 自动嵌入）
3. **单频道快照**：`python scripts/audit/audit-md-internal-links.py`
4. **改内链**：只改部署仓 `content/**/*.md` 正文；改后重跑本脚本更新快照
5. **邻居选题**：SSOT 附录 B · [`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md)

*自动生成 · 2026-08-27 · Alignify 上下文仓 · `skills/optimize-internal-links/references/`*
