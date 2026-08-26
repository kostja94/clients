# Alignify 文章页面内链情况（快照）

> 生成日期：2026-08-27
> 数据源：`alignify-by-kostja/content/**/*.md`（共 400 篇文章）
> 方法：提取每篇正文与 frontmatter 中的站内链接（Markdown `[text](/path)` 与 `<a href="/path">`），
> 归一化目标为 `route/slug`（忽略 `/zh` 前缀）；外链、锚点、图片与静态资源不计。
> 完整数据见 `scripts/reports/md-internal-links-status-YYYY-MM-DD.json`。

> **口径说明**：`≥5 distinct` 为 SSOT 中 **Tools 长文**的硬性 R1 底线（`internal-links.md §3.1.5`）；
> SEO 频道遵循「少而准」与学习页节制原则（§4.1.6），**不适用** R1 硬标准；
> 因此「≥5 distinct」对其他类目仅为**观察性指标**，不构成违规判断。

## 概览

| 类目 | 文章数 | 内链总量 | 平均内链/篇 | ≥5 distinct 篇数 | ≥5 distinct 占比 |
|------|-------:|--------:|------------:|-----------------:|-----------------:|
| tools ⭐R1 | 216 | 1019 | 4.7 | 97 | 45% |
| seo | 76 | 214 | 2.8 | 14 | 18% |
| blog | 52 | 224 | 4.3 | 20 | 38% |
| marketing | 34 | 138 | 4.1 | 6 | 18% |
| insights | 14 | 104 | 7.4 | 6 | 43% |
| events | 8 | 4 | 0.5 | 0 | 0% |
| **合计** | **400** | **1703** | **4.3** | **143** | **36%** |

- ⭐R1：SSOT 硬性底线仅适用于 tools 类目（正文 4–9 条 distinct 内链，底线 ≥5）。

## 需要关注的问题

- **Tools R1 未达标**（distinct 站内目标 < 5，SSOT 硬规则）：**119** 篇 / 216 篇
- **其他类目低内链**（< 5 distinct，观察性，非违规）：**138** 篇
- **存在重复目标**（同一 `route/slug` 出现 >1 次）：**58** 篇
- **零内链**：**63** 篇

### Tools R1 未达标清单（硬规则）

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `3d` | en | 4 | 4 | `blog/cad`、`tools/3d-model-generator`、`tools/3d-scanner`、`tools/animation-generator` |
| `3d-model-generator` | en | 3 | 3 | `tools/3d-modelling`、`tools/3d-scanner`、`tools/world-model` |
| `3d-modelling` | en | 4 | 4 | `blog/cad`、`tools/3d`、`tools/3d-model-generator`、`tools/3d-scanner` |
| `3d-scanner` | en | 3 | 3 | `tools/3d-model-generator`、`tools/3d-modelling`、`tools/world-model` |
| `accent-conversion` | en | 3 | 3 | `tools/speech-to-text`、`tools/text-to-speech`、`tools/voice-changer` |
| `affiliate-marketing` | en | 4 | 4 | `blog/agentic-commerce`、`marketing/affiliate`、`tools/lead-generation`、`tools/referral-program` |
| `ai-homework-helper` | en | 2 | 2 | `tools/education`、`tools/essay-writer` |
| `ai-scheduling` | en | 3 | 3 | `tools/family-assistant`、`tools/lead-generation`、`tools/note-taker` |
| `animation-library` | en | 4 | 4 | `tools/design`、`tools/image-generator`、`tools/video-generator`、`tools/website-builder` |
| `app-builder` | en | 3 | 3 | `tools/coding`、`tools/vibe-coding`、`tools/website-builder` |
| `audio-translator` | en | 3 | 3 | `tools/accent-conversion`、`tools/video-translator`、`tools/voice` |
| `b2b` | en | 3 | 3 | `tools/lead-generation`、`tools/linkedin`、`tools/web-scraping` |
| `browser` | en | 3 | 3 | `tools/coding`、`tools/search-engine`、`tools/workflow` |
| `chatbot` | en | 3 | 3 | `tools/coding`、`tools/knowledge-base`、`tools/text` |
| `cli` | en | 2 | 2 | `tools/coding`、`tools/ide` |
| `code-completion` | en | 3 | 3 | `tools/code-review`、`tools/coding`、`tools/ide` |
| `code-review` | en | 4 | 4 | `tools/code-completion`、`tools/coding`、`tools/directory`、`tools/text-generator` |
| `coding` | en | 3 | 3 | `tools/code-completion`、`tools/documentation`、`tools/ide` |
| `community` | en | 3 | 3 | `tools/directory`、`tools/knowledge-base`、`tools/llm` |
| `dating` | en | 2 | 2 | `tools/ai-scheduling`、`tools/character-chat` |
| `design` | en | 4 | 4 | `blog/interior-design`、`tools/image-generator`、`tools/poster-generator`、`tools/website-builder` |
| `directory` | en | 2 | 2 | `tools/evaluation`、`tools/search-engine` |
| `education` | en | 2 | 2 | `tools/essay-writer`、`tools/web-search-api` |
| `essay-writer` | en | 2 | 2 | `tools/note-taker`、`tools/text-generator` |
| `evaluation` | en | 3 | 3 | `tools/agent-skills`、`tools/api`、`tools/coding` |
| `family-assistant` | en | 4 | 4 | `tools/ai-scheduling`、`tools/note-taker`、`tools/productivity`、`tools/voice-cloning` |
| `fashion` | en | 2 | 2 | `tools/background-changer`、`tools/image-generator` |
| `fundraising` | en | 2 | 2 | `tools/b2b`、`tools/lead-generation` |
| `headless-browser` | en | 3 | 3 | `tools/api`、`tools/geo`、`tools/ide` |
| `healthcare` | en | 4 | 4 | `blog/medical-scribe`、`tools/knowledge-base`、`tools/legal`、`tools/note-taker` |
| `ide` | en | 3 | 3 | `tools/cli`、`tools/code-completion`、`tools/coding` |
| `image` | en | 4 | 4 | `tools/community`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-relighting` |
| `image-editor` | en | 2 | 2 | `tools/background-changer`、`tools/image-enhancer` |
| `image-enhancer` | en | 2 | 2 | `tools/image-editor`、`tools/image-generator` |
| `image-generator` | en | 4 | 4 | `tools/background-changer`、`tools/headshot-generator`、`tools/tattoo-generator`、`tools/virtual-staging` |
| `image-relighting` | en | 2 | 2 | `tools/image-editor`、`tools/image-enhancer` |
| `influencer-marketing` | en | 1 | 1 | `tools/affiliate-marketing` |
| `interview-assistant` | en | 2 | 2 | `tools/lead-generation`、`tools/recruiting` |
| `knowledge-base` | en | 3 | 3 | `blog/agent-memory`、`tools/note-taker`、`tools/search-engine` |
| `lead-generation` | en | 3 | 3 | `tools/b2b`、`tools/knowledge-base`、`tools/recruiting` |
| `legal` | en | 3 | 3 | `tools/notes-generator`、`tools/productivity`、`tools/text-generator` |
| `linkedin` | en | 4 | 4 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting`、`tools/text-generator` |
| `lip-sync` | en | 3 | 3 | `tools/avatar`、`tools/video-to-video`、`tools/video-translator` |
| `memory` | en | 4 | 4 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `music-generator` | en | 2 | 2 | `tools/video-editor`、`tools/voice-changer` |
| `note-taker` | en | 4 | 4 | `blog/medical-scribe`、`tools/knowledge-base`、`tools/notes-generator`、`tools/speech-to-text` |
| `notes-generator` | en | 3 | 3 | `tools/ai-scheduling`、`tools/note-taker`、`tools/voice-cloning` |
| `ocr` | en | 3 | 3 | `tools/image-enhancer`、`tools/knowledge-base`、`tools/note-taker` |
| `poster-generator` | en | 3 | 3 | `tools/design`、`tools/fashion`、`tools/image-generator` |
| `presentation-maker` | en | 3 | 3 | `tools/design`、`tools/essay-writer`、`tools/image-generator` |
| `productivity` | en | 2 | 2 | `tools/hr-assistant`、`tools/note-taker` |
| `recruiting` | en | 3 | 3 | `tools/hr-assistant`、`tools/interview-assistant`、`tools/note-taker` |
| `referral-program` | en | 4 | 4 | `marketing/referral-program`、`tools/affiliate-marketing`、`tools/b2b`、`tools/lead-generation` |
| `religion` | en | 3 | 3 | `tools/essay-writer`、`tools/knowledge-base`、`tools/presentation-maker` |
| `search-indexing` | en | 3 | 3 | `tools/llm`、`tools/memory`、`tools/search-engine` |
| `short-drama` | en | 3 | 3 | `tools/animation-generator`、`tools/video-generator`、`tools/workflow` |
| `spreadsheet` | en | 3 | 3 | `tools/app-builder`、`tools/presentation-maker`、`tools/web-scraping` |
| `story-generator` | en | 2 | 2 | `tools/essay-writer`、`tools/text-generator` |
| `tattoo-generator` | en | 3 | 3 | `tools/avatar`、`tools/image`、`tools/image-generator` |
| `text` | en | 3 | 3 | `tools/essay-writer`、`tools/text-generator`、`tools/text-translator` |
| `text-to-speech` | en | 2 | 2 | `tools/voice-changer`、`tools/voice-cloning` |
| `user-research` | en | 2 | 2 | `tools/ai-scheduling`、`tools/productivity` |
| `vibe-coding` | en | 2 | 2 | `tools/app-builder`、`tools/coding` |
| `video-clipping` | en | 4 | 4 | `tools/text-to-video`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `video-translator` | en | 4 | 4 | `tools/audio-translator`、`tools/lip-sync`、`tools/video`、`tools/video-clipping` |
| `virtual-staging` | en | 1 | 1 | `tools/headshot-generator` |
| `voice` | en | 4 | 4 | `tools/accent-conversion`、`tools/notes-generator`、`tools/text-to-speech`、`tools/voice-cloning` |
| `voice-changer` | en | 1 | 1 | `tools/text-to-speech` |
| `voice-cloning` | en | 2 | 2 | `tools/text-to-speech`、`tools/voice-changer` |
| `web-scraping` | en | 2 | 2 | `tools/geo`、`tools/web-search-api` |
| `website-builder` | en | 3 | 3 | `tools/coding`、`tools/design`、`tools/image-generator` |
| `3d-model-generator` | zh | 3 | 4 | `tools/3d-modelling`、`tools/3d-scanner`、`tools/world-model` |
| `3d-modelling` | zh | 4 | 4 | `blog/cad`、`tools/3d`、`tools/3d-model-generator`、`tools/3d-scanner` |
| `3d-scanner` | zh | 3 | 5 | `tools/3d-model-generator`、`tools/3d-modelling`、`tools/world-model` |
| `accent-conversion` | zh | 4 | 5 | `tools/education`、`tools/text-to-speech`、`tools/voice-changer`、`tools/voice-cloning` |
| `affiliate-marketing` | zh | 4 | 4 | `blog/agentic-commerce`、`marketing/affiliate`、`tools/influencer-marketing`、`tools/referral-program` |
| `ai-homework-helper` | zh | 2 | 2 | `tools/education`、`tools/essay-writer` |
| `app-builder` | zh | 3 | 3 | `tools/coding`、`tools/vibe-coding`、`tools/website-builder` |
| `b2b` | zh | 4 | 4 | `tools/knowledge-base`、`tools/lead-generation`、`tools/linkedin`、`tools/web-scraping` |
| `chatbot` | zh | 4 | 4 | `tools/b2b`、`tools/coding`、`tools/llm`、`tools/productivity` |
| `cli` | zh | 2 | 2 | `tools/coding`、`tools/vibe-coding` |
| `code-completion` | zh | 4 | 4 | `tools/code-review`、`tools/coding`、`tools/ide`、`tools/llm-for-coding` |
| `community` | zh | 2 | 2 | `tools/directory`、`tools/knowledge-base` |
| `dating` | zh | 2 | 3 | `tools/ai-scheduling`、`tools/character-chat` |
| `education` | zh | 2 | 3 | `tools/essay-writer`、`tools/web-search-api` |
| `essay-writer` | zh | 3 | 3 | `tools/text`、`tools/text-generator`、`tools/web-search-api` |
| `evaluation` | zh | 3 | 3 | `tools/api`、`tools/llm`、`tools/llm-for-coding` |
| `fundraising` | zh | 3 | 3 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting` |
| `headless-browser` | zh | 3 | 3 | `tools/geo`、`tools/llm`、`tools/web-scraping` |
| `headshot-generator` | zh | 4 | 4 | `tools/image-generator`、`tools/image-relighting`、`tools/presentation-maker`、`tools/website-builder` |
| `hr-assistant` | zh | 4 | 4 | `tools/chatbot`、`tools/note-taker`、`tools/productivity`、`tools/recruiting` |
| `ide` | zh | 2 | 2 | `tools/code-completion`、`tools/code-review` |
| `image-enhancer` | zh | 2 | 2 | `tools/image-editor`、`tools/ocr` |
| `image-relighting` | zh | 2 | 2 | `tools/background-changer`、`tools/image-enhancer` |
| `interview-assistant` | zh | 3 | 3 | `tools/documentation`、`tools/lead-generation`、`tools/text-generator` |
| `knowledge-base` | zh | 4 | 4 | `blog/agent-memory`、`tools/search-engine`、`tools/text-generator`、`tools/web-search-api` |
| `lead-generation` | zh | 4 | 4 | `tools/b2b`、`tools/productivity`、`tools/recruiting`、`tools/referral-program` |
| `legal` | zh | 4 | 4 | `tools/notes-generator`、`tools/productivity`、`tools/religion`、`tools/text-generator` |
| `linkedin` | zh | 4 | 4 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting`、`tools/text-generator` |
| `memory` | zh | 4 | 4 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `music-generator` | zh | 3 | 3 | `tools/music-video-generator`、`tools/video-editor`、`tools/voice` |
| `note-taker` | zh | 3 | 3 | `blog/medical-scribe`、`tools/speech-to-text`、`tools/text-generator` |
| `notes-generator` | zh | 3 | 3 | `tools/note-taker`、`tools/text-generator`、`tools/voice-cloning` |
| `ocr` | zh | 3 | 3 | `tools/image-enhancer`、`tools/knowledge-base`、`tools/text-to-speech` |
| `openclaw-alternatives` | zh | 4 | 4 | `tools/agent-for-desktop`、`tools/api`、`tools/documentation`、`tools/knowledge-base` |
| `presentation-maker` | zh | 2 | 2 | `tools/logo-generator`、`tools/text-generator` |
| `productivity` | zh | 3 | 3 | `tools/ai-scheduling`、`tools/text-generator`、`tools/workflow` |
| `religion` | zh | 3 | 3 | `tools/community`、`tools/knowledge-base`、`tools/text-translator` |
| `short-drama` | zh | 3 | 3 | `tools/animation-generator`、`tools/video-generator`、`tools/workflow` |
| `spreadsheet` | zh | 3 | 3 | `tools/app-builder`、`tools/productivity`、`tools/web-scraping` |
| `story-generator` | zh | 2 | 2 | `tools/text-generator`、`tools/text-to-video` |
| `tattoo-generator` | zh | 3 | 3 | `tools/image`、`tools/image-editor`、`tools/image-generator` |
| `text` | zh | 4 | 4 | `tools/essay-writer`、`tools/story-generator`、`tools/text-generator`、`tools/text-to-speech` |
| `text-to-speech` | zh | 2 | 2 | `tools/voice-changer`、`tools/voice-cloning` |
| `user-research` | zh | 2 | 2 | `tools/ai-scheduling`、`tools/productivity` |
| `vibe-coding` | zh | 3 | 3 | `tools/app-builder`、`tools/code-completion`、`tools/coding` |
| `voice` | zh | 4 | 4 | `tools/notes-generator`、`tools/speech-to-text`、`tools/text-to-speech`、`tools/voice-cloning` |
| `voice-changer` | zh | 2 | 2 | `tools/text-to-speech`、`tools/voice-cloning` |
| `voice-cloning` | zh | 4 | 4 | `tools/audio-translator`、`tools/lip-sync`、`tools/text-to-speech`、`tools/voice-changer` |

### 其他类目低内链清单（观察性）

| 文章 | 语言 | distinct | 总量 |
|------|------|---------:|-----:|
| `blog/en/agent-sandbox` | en | 4 | 4 |
| `blog/en/ai-components` | en | 2 | 2 |
| `blog/en/ai-flashcards` | en | 3 | 3 |
| `blog/en/ai-language-learning` | en | 2 | 2 |
| `blog/en/ai-traffic-and-citation-sources` | en | 2 | 3 |
| `blog/en/ai-visibility` | en | 3 | 3 |
| `blog/en/cad` | en | 4 | 4 |
| `blog/en/data-engineering-agent` | en | 3 | 3 |
| `blog/en/git-hosting` | en | 4 | 7 |
| `blog/en/github-for-marketing` | en | 2 | 2 |
| `blog/en/how-to-name-ai-products` | en | 1 | 1 |
| `blog/en/how-to-write-github-readme` | en | 2 | 2 |
| `blog/en/inference-infrastructure` | en | 2 | 2 |
| `blog/en/interior-design` | en | 4 | 4 |
| `blog/en/medical-scribe` | en | 4 | 4 |
| `blog/en/rate-limit-reset` | en | 4 | 6 |
| `blog/en/wrapped-marketing` | en | 4 | 5 |
| `blog/zh/ai-components` | zh | 2 | 2 |
| `blog/zh/ai-flashcards` | zh | 3 | 3 |
| `blog/zh/ai-language-learning` | zh | 2 | 2 |
| `blog/zh/ai-traffic-and-citation-sources` | zh | 2 | 3 |
| `blog/zh/ai-visibility` | zh | 4 | 4 |
| `blog/zh/cad` | zh | 4 | 4 |
| `blog/zh/data-engineering-agent` | zh | 3 | 3 |
| `blog/zh/git-hosting` | zh | 4 | 7 |
| `blog/zh/github-for-marketing` | zh | 2 | 2 |
| `blog/zh/how-to-name-ai-products` | zh | 1 | 1 |
| `blog/zh/how-to-write-github-readme` | zh | 2 | 2 |
| `blog/zh/inference-infrastructure` | zh | 3 | 3 |
| `blog/zh/interior-design` | zh | 4 | 4 |
| `blog/zh/rate-limit-reset` | zh | 4 | 6 |
| `blog/zh/wrapped-marketing` | zh | 4 | 5 |
| `events/en/founder-park-2024-11-06` | en | 0 | 0 |
| `events/en/linkloud-2025-02-23` | en | 1 | 1 |
| `events/en/linkloud-2026-01-24` | en | 0 | 0 |
| `events/en/praxis-2025-09-27` | en | 1 | 1 |
| `events/zh/founder-park-2024-11-06` | zh | 0 | 0 |
| `events/zh/linkloud-2025-02-23` | zh | 1 | 1 |
| `events/zh/linkloud-2026-01-24` | zh | 0 | 0 |
| `events/zh/praxis-2025-09-27` | zh | 1 | 1 |
| `insights/en/ai-logo-design` | en | 3 | 4 |
| `insights/en/generative-ai-landscape` | en | 1 | 1 |
| `insights/en/google` | en | 0 | 0 |
| `insights/en/openai` | en | 0 | 0 |
| `insights/zh/ai-logo-design` | zh | 3 | 4 |
| `insights/zh/generative-ai-landscape` | zh | 1 | 1 |
| `insights/zh/google` | zh | 0 | 0 |
| `insights/zh/openai` | zh | 0 | 0 |
| `marketing/en/affiliate` | en | 1 | 2 |
| `marketing/en/competitive-analysis` | en | 2 | 3 |
| `marketing/en/creator-challenge-program` | en | 1 | 1 |
| `marketing/en/creator-program` | en | 1 | 1 |
| `marketing/en/email-marketing` | en | 2 | 3 |
| `marketing/en/growth-case-studies` | en | 0 | 0 |
| `marketing/en/influencer` | en | 2 | 3 |
| `marketing/en/keyword-research` | en | 1 | 1 |
| `marketing/en/localization-strategy` | en | 1 | 1 |
| `marketing/en/marketing-types` | en | 0 | 0 |
| `marketing/en/pricing-strategy` | en | 2 | 3 |
| `marketing/en/reddit` | en | 0 | 0 |
| `marketing/en/referral-program` | en | 1 | 2 |
| `marketing/en/x-formerly-twitter` | en | 2 | 2 |
| `marketing/zh/affiliate` | zh | 3 | 4 |
| `marketing/zh/competitive-analysis` | zh | 2 | 3 |
| `marketing/zh/creator-challenge-program` | zh | 1 | 2 |
| `marketing/zh/creator-program` | zh | 1 | 1 |
| `marketing/zh/email-marketing` | zh | 2 | 3 |
| `marketing/zh/growth-case-studies` | zh | 0 | 0 |
| `marketing/zh/influencer` | zh | 3 | 4 |
| `marketing/zh/keyword-research` | zh | 1 | 1 |
| `marketing/zh/localization-strategy` | zh | 1 | 1 |
| `marketing/zh/marketing-types` | zh | 0 | 0 |
| `marketing/zh/pricing-strategy` | zh | 2 | 3 |
| `marketing/zh/reddit` | zh | 2 | 2 |
| `marketing/zh/referral-program` | zh | 2 | 3 |
| `marketing/zh/x-formerly-twitter` | zh | 3 | 3 |
| `seo/en/best-tools` | en | 0 | 0 |
| `seo/en/branded-queries-filter-google-search-console` | en | 0 | 0 |
| `seo/en/breadcrumbs` | en | 4 | 5 |
| `seo/en/crawler` | en | 0 | 0 |
| `seo/en/create-blog` | en | 0 | 0 |
| `seo/en/dark-traffic` | en | 0 | 0 |
| `seo/en/domain` | en | 4 | 6 |
| `seo/en/example-article` | en | 0 | 0 |
| `seo/en/external-links` | en | 0 | 0 |
| `seo/en/glossary` | en | 0 | 0 |
| `seo/en/google-tag-manager` | en | 0 | 0 |
| `seo/en/how-search-engine-works` | en | 0 | 0 |
| `seo/en/html-a-tag` | en | 0 | 0 |
| `seo/en/internal-links` | en | 0 | 0 |
| `seo/en/landing-page` | en | 0 | 0 |
| `seo/en/learn-seo` | en | 3 | 3 |
| `seo/en/link-building` | en | 0 | 0 |
| `seo/en/local-search-engines` | en | 0 | 0 |
| `seo/en/meta-tag` | en | 0 | 0 |
| `seo/en/navigation-menu` | en | 3 | 3 |
| `seo/en/new-domains-tld` | en | 0 | 0 |
| `seo/en/redirect-chain` | en | 0 | 0 |
| `seo/en/robots-txt` | en | 0 | 0 |
| `seo/en/serp` | en | 0 | 0 |
| `seo/en/sitemap` | en | 0 | 0 |
| `seo/en/subdomain-vs-subfolder` | en | 0 | 0 |
| `seo/en/submit-website` | en | 0 | 0 |
| `seo/en/website-indexing` | en | 0 | 0 |
| `seo/en/website-rendering` | en | 0 | 0 |
| `seo/en/website-structure` | en | 2 | 4 |
| `seo/en/website-traffic` | en | 4 | 14 |
| `seo/zh/best-tools` | zh | 0 | 0 |
| `seo/zh/branded-queries-filter-google-search-console` | zh | 0 | 0 |
| `seo/zh/crawler` | zh | 0 | 0 |
| `seo/zh/create-blog` | zh | 0 | 0 |
| `seo/zh/dark-traffic` | zh | 0 | 0 |
| `seo/zh/domain` | zh | 4 | 5 |
| `seo/zh/example-article` | zh | 0 | 0 |
| `seo/zh/external-links` | zh | 0 | 0 |
| `seo/zh/glossary` | zh | 0 | 0 |
| `seo/zh/google-tag-manager` | zh | 0 | 0 |
| `seo/zh/how-search-engine-works` | zh | 0 | 0 |
| `seo/zh/html-a-tag` | zh | 0 | 0 |
| `seo/zh/html-tag` | zh | 4 | 6 |
| `seo/zh/internal-links` | zh | 0 | 0 |
| `seo/zh/landing-page` | zh | 0 | 0 |
| `seo/zh/learn-seo` | zh | 3 | 3 |
| `seo/zh/link-building` | zh | 0 | 0 |
| `seo/zh/local-search-engines` | zh | 0 | 0 |
| `seo/zh/meta-tag` | zh | 0 | 0 |
| `seo/zh/navigation-menu` | zh | 3 | 3 |
| `seo/zh/new-domains-tld` | zh | 0 | 0 |
| `seo/zh/redirect-chain` | zh | 0 | 0 |
| `seo/zh/robots-txt` | zh | 0 | 0 |
| `seo/zh/serp` | zh | 0 | 0 |
| `seo/zh/sitemap` | zh | 2 | 3 |
| `seo/zh/subdomain-vs-subfolder` | zh | 0 | 0 |
| `seo/zh/submit-website` | zh | 0 | 0 |
| `seo/zh/website-indexing` | zh | 0 | 0 |
| `seo/zh/website-rendering` | zh | 0 | 0 |
| `seo/zh/website-structure` | zh | 0 | 0 |
| `seo/zh/website-traffic` | zh | 4 | 14 |

### 重复目标清单

| 文章 | 重复目标 |
|------|---------|
| `blog/en/ai-traffic-and-citation-sources` | `tools/geo` |
| `blog/en/coding-plan` | `blog/rate-limit-reset` |
| `blog/en/git-hosting` | `tools/cli`、`tools/code-review` |
| `blog/en/rate-limit-reset` | `marketing/pricing-strategy` |
| `blog/en/wrapped-marketing` | `blog/ugc-marketing` |
| `blog/zh/ai-traffic-and-citation-sources` | `tools/geo` |
| `blog/zh/coding-plan` | `blog/rate-limit-reset` |
| `blog/zh/git-hosting` | `tools/cli`、`tools/code-review` |
| `blog/zh/rate-limit-reset` | `marketing/pricing-strategy` |
| `blog/zh/wrapped-marketing` | `blog/ugc-marketing` |
| `insights/en/ai-logo-design` | `tools/logo-generator` |
| `insights/en/indie-hackers` | `insights/directory-submission-sites`、`insights/reasons-you-need-seo`、`marketing/email-marketing`、`marketing/geo`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/localization-strategy`、`marketing/pricing-strategy`、`marketing/reddit`、`marketing/x-formerly-twitter`、`tools` |
| `insights/zh/ai-logo-design` | `tools/logo-generator` |
| `insights/zh/indie-hackers` | `insights/directory-submission-sites`、`insights/reasons-you-need-seo`、`marketing/email-marketing`、`marketing/geo`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/localization-strategy`、`marketing/pricing-strategy`、`marketing/reddit`、`marketing/x-formerly-twitter`、`tools` |
| `marketing/en/affiliate` | `tools/affiliate-marketing` |
| `marketing/en/competitive-analysis` | `marketing/keyword-research` |
| `marketing/en/email-marketing` | `marketing/keyword-research` |
| `marketing/en/geo` | `blog/ai-traffic-and-citation-sources`、`blog/ai-visibility`、`marketing/affiliate`、`marketing/influencer`、`seo/how-search-engine-works`、`tools/geo` |
| `marketing/en/influencer` | `marketing/affiliate` |
| `marketing/en/lifetime-deal` | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/pricing-strategy` |
| `marketing/en/pricing-strategy` | `marketing/competitive-analysis` |
| `marketing/en/referral-program` | `tools/referral-program` |
| `marketing/en/ugc-marketing` | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/creator-program`、`marketing/lifetime-deal` |
| `marketing/zh/affiliate` | `tools/affiliate-marketing` |
| `marketing/zh/competitive-analysis` | `marketing/keyword-research` |
| `marketing/zh/creator-challenge-program` | `marketing/creator-program` |
| `marketing/zh/email-marketing` | `marketing/keyword-research` |
| `marketing/zh/geo` | `blog/ai-traffic-and-citation-sources`、`blog/ai-visibility`、`marketing/affiliate`、`marketing/creator-program`、`marketing/influencer`、`tools/geo` |
| `marketing/zh/influencer` | `marketing/affiliate` |
| `marketing/zh/lifetime-deal` | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/pricing-strategy` |
| `marketing/zh/pricing-strategy` | `marketing/competitive-analysis` |
| `marketing/zh/referral-program` | `tools/referral-program` |
| `marketing/zh/ugc-marketing` | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/creator-program`、`marketing/lifetime-deal` |
| `seo/en/breadcrumbs` | `seo/schema` |
| `seo/en/category-pages` | `seo/breadcrumbs` |
| `seo/en/domain` | `seo/redirect-chain`、`seo/robots-txt` |
| `seo/en/html-tag` | `seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag` |
| `seo/en/schema` | `seo/meta-tag` |
| `seo/en/url-optimization` | `seo/breadcrumbs`、`seo/sitemap` |
| `seo/en/website-structure` | `seo/internal-links` |
| `seo/en/website-traffic` | `seo/dark-traffic`、`seo/internal-links`、`seo/link-building`、`seo/website-structure` |
| `seo/zh/breadcrumbs` | `seo/schema` |
| `seo/zh/domain` | `seo/redirect-chain` |
| `seo/zh/html-tag` | `seo/internal-links`、`seo/meta-tag` |
| `seo/zh/schema` | `marketing/geo`、`seo/meta-tag` |
| `seo/zh/sitemap` | `seo/website-indexing` |
| `seo/zh/url-optimization` | `seo/breadcrumbs`、`seo/sitemap` |
| `seo/zh/website-traffic` | `seo/dark-traffic`、`seo/internal-links`、`seo/link-building`、`seo/website-structure` |
| `tools/zh/3d-model-generator` | `tools/3d-modelling` |
| `tools/zh/3d-scanner` | `tools/3d-modelling` |
| `tools/zh/accent-conversion` | `tools/voice-changer` |
| `tools/zh/audio-translator` | `tools/accent-conversion`、`tools/video-translator` |
| `tools/zh/background-changer` | `tools/image-editor` |
| `tools/zh/canvas-video` | `tools/workflow` |
| `tools/zh/dating` | `tools/character-chat` |
| `tools/zh/education` | `tools/web-search-api` |
| `tools/zh/geo` | `blog/ai-traffic-and-citation-sources` |
| `tools/zh/video-generator` | `tools/video-editor` |

### 零内链清单

- `events/en/founder-park-2024-11-06`
- `events/en/linkloud-2026-01-24`
- `events/zh/founder-park-2024-11-06`
- `events/zh/linkloud-2026-01-24`
- `insights/en/google`
- `insights/en/openai`
- `insights/zh/google`
- `insights/zh/openai`
- `marketing/en/growth-case-studies`
- `marketing/en/marketing-types`
- `marketing/en/reddit`
- `marketing/zh/growth-case-studies`
- `marketing/zh/marketing-types`
- `seo/en/best-tools`
- `seo/en/branded-queries-filter-google-search-console`
- `seo/en/crawler`
- `seo/en/create-blog`
- `seo/en/dark-traffic`
- `seo/en/example-article`
- `seo/en/external-links`
- `seo/en/glossary`
- `seo/en/google-tag-manager`
- `seo/en/how-search-engine-works`
- `seo/en/html-a-tag`
- `seo/en/internal-links`
- `seo/en/landing-page`
- `seo/en/link-building`
- `seo/en/local-search-engines`
- `seo/en/meta-tag`
- `seo/en/new-domains-tld`
- `seo/en/redirect-chain`
- `seo/en/robots-txt`
- `seo/en/serp`
- `seo/en/sitemap`
- `seo/en/subdomain-vs-subfolder`
- `seo/en/submit-website`
- `seo/en/website-indexing`
- `seo/en/website-rendering`
- `seo/zh/best-tools`
- `seo/zh/branded-queries-filter-google-search-console`
- `seo/zh/crawler`
- `seo/zh/create-blog`
- `seo/zh/dark-traffic`
- `seo/zh/example-article`
- `seo/zh/external-links`
- `seo/zh/glossary`
- `seo/zh/google-tag-manager`
- `seo/zh/how-search-engine-works`
- `seo/zh/html-a-tag`
- `seo/zh/internal-links`
- `seo/zh/landing-page`
- `seo/zh/link-building`
- `seo/zh/local-search-engines`
- `seo/zh/meta-tag`
- `seo/zh/new-domains-tld`
- `seo/zh/redirect-chain`
- `seo/zh/robots-txt`
- `seo/zh/serp`
- `seo/zh/subdomain-vs-subfolder`
- `seo/zh/submit-website`
- `seo/zh/website-indexing`
- `seo/zh/website-rendering`
- `seo/zh/website-structure`

## 按类目明细

### tools

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `3d` | en | 4 | 4 | `blog/cad`、`tools/3d-model-generator`、`tools/3d-scanner`、`tools/animation-generator` |
| `3d-model-generator` | en | 3 | 3 | `tools/3d-modelling`、`tools/3d-scanner`、`tools/world-model` |
| `3d-modelling` | en | 4 | 4 | `blog/cad`、`tools/3d`、`tools/3d-model-generator`、`tools/3d-scanner` |
| `3d-scanner` | en | 3 | 3 | `tools/3d-model-generator`、`tools/3d-modelling`、`tools/world-model` |
| `accent-conversion` | en | 3 | 3 | `tools/speech-to-text`、`tools/text-to-speech`、`tools/voice-changer` |
| `affiliate-marketing` | en | 4 | 4 | `blog/agentic-commerce`、`marketing/affiliate`、`tools/lead-generation`、`tools/referral-program` |
| `agent-for-desktop` | en | 9 | 9 | `blog/multi-agent`、`tools/api`、`tools/authentication`、`tools/browser`、`tools/directory`、`tools/headless-browser`、`tools/ide`、`tools/knowledge-base`、`tools/productivity` |
| `agent-skills` | en | 17 | 17 | `skills`、`tools/agent-for-desktop`、`tools/api`、`tools/app-builder`、`tools/browser`、`tools/chatbot`、`tools/code-completion`、`tools/code-review`、`tools/coding`、`tools/directory`、`tools/evaluation`、`tools/family-assistant`、`tools/knowledge-base`、`tools/llm`、`tools/openclaw-alternatives`、`tools/productivity`、`tools/vibe-coding` |
| `ai-homework-helper` | en | 2 | 2 | `tools/education`、`tools/essay-writer` |
| `ai-scheduling` | en | 3 | 3 | `tools/family-assistant`、`tools/lead-generation`、`tools/note-taker` |
| `animation-generator` | en | 5 | 5 | `tools/animation-library`、`tools/filmmaking`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video` |
| `animation-library` | en | 4 | 4 | `tools/design`、`tools/image-generator`、`tools/video-generator`、`tools/website-builder` |
| `api` | en | 5 | 5 | `tools/coding`、`tools/image-generator`、`tools/llm`、`tools/video-generator`、`tools/workflow` |
| `app-builder` | en | 3 | 3 | `tools/coding`、`tools/vibe-coding`、`tools/website-builder` |
| `audio-translator` | en | 3 | 3 | `tools/accent-conversion`、`tools/video-translator`、`tools/voice` |
| `authentication` | en | 8 | 8 | `tools/api`、`tools/app-builder`、`tools/browser`、`tools/documentation`、`tools/notes-generator`、`tools/productivity`、`tools/user-research`、`tools/web-search-api` |
| `avatar` | en | 11 | 11 | `tools/api`、`tools/background-changer`、`tools/headshot-generator`、`tools/image-editor`、`tools/image-generator`、`tools/lip-sync`、`tools/music-generator`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-generator`、`tools/web-search-api` |
| `b2b` | en | 3 | 3 | `tools/lead-generation`、`tools/linkedin`、`tools/web-scraping` |
| `background-changer` | en | 6 | 6 | `tools/avatar`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator`、`tools/poster-generator`、`tools/text-generator` |
| `browser` | en | 3 | 3 | `tools/coding`、`tools/search-engine`、`tools/workflow` |
| `canvas-video` | en | 5 | 5 | `tools/image-to-video`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/workflow` |
| `character-chat` | en | 7 | 7 | `tools/api`、`tools/chatbot`、`tools/dating`、`tools/directory`、`tools/headshot-generator`、`tools/story-generator`、`tools/web-search-api` |
| `chatbot` | en | 3 | 3 | `tools/coding`、`tools/knowledge-base`、`tools/text` |
| `cli` | en | 2 | 2 | `tools/coding`、`tools/ide` |
| `code-completion` | en | 3 | 3 | `tools/code-review`、`tools/coding`、`tools/ide` |
| `code-review` | en | 4 | 4 | `tools/code-completion`、`tools/coding`、`tools/directory`、`tools/text-generator` |
| `coding` | en | 3 | 3 | `tools/code-completion`、`tools/documentation`、`tools/ide` |
| `community` | en | 3 | 3 | `tools/directory`、`tools/knowledge-base`、`tools/llm` |
| `dating` | en | 2 | 2 | `tools/ai-scheduling`、`tools/character-chat` |
| `design` | en | 4 | 4 | `blog/interior-design`、`tools/image-generator`、`tools/poster-generator`、`tools/website-builder` |
| `directory` | en | 2 | 2 | `tools/evaluation`、`tools/search-engine` |
| `documentation` | en | 19 | 19 | `tools/api`、`tools/app-builder`、`tools/browser`、`tools/chatbot`、`tools/cli`、`tools/code-completion`、`tools/code-review`、`tools/coding`、`tools/directory`、`tools/geo`、`tools/ide`、`tools/llm`、`tools/productivity`、`tools/text-generator`、`tools/user-research`、`tools/vibe-coding`、`tools/web-search-api`、`tools/website-builder`、`tools/workflow` |
| `education` | en | 2 | 2 | `tools/essay-writer`、`tools/web-search-api` |
| `essay-writer` | en | 2 | 2 | `tools/note-taker`、`tools/text-generator` |
| `evaluation` | en | 3 | 3 | `tools/agent-skills`、`tools/api`、`tools/coding` |
| `family-assistant` | en | 4 | 4 | `tools/ai-scheduling`、`tools/note-taker`、`tools/productivity`、`tools/voice-cloning` |
| `fashion` | en | 2 | 2 | `tools/background-changer`、`tools/image-generator` |
| `filmmaking` | en | 6 | 6 | `tools/animation-library`、`tools/lip-sync`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video`、`tools/video-translator` |
| `fundraising` | en | 2 | 2 | `tools/b2b`、`tools/lead-generation` |
| `geo` | en | 10 | 10 | `blog/ai-traffic-and-citation-sources`、`marketing/geo`、`tools/api`、`tools/browser`、`tools/notes-generator`、`tools/productivity`、`tools/search-engine`、`tools/search-indexing`、`tools/user-research`、`tools/web-search-api` |
| `headless-browser` | en | 3 | 3 | `tools/api`、`tools/geo`、`tools/ide` |
| `headshot-generator` | en | 6 | 6 | `tools/image`、`tools/image-enhancer`、`tools/image-generator`、`tools/poster-generator`、`tools/presentation-maker`、`tools/web-search-api` |
| `healthcare` | en | 4 | 4 | `blog/medical-scribe`、`tools/knowledge-base`、`tools/legal`、`tools/note-taker` |
| `hr-assistant` | en | 5 | 5 | `tools/chatbot`、`tools/interview-assistant`、`tools/note-taker`、`tools/productivity`、`tools/recruiting` |
| `ide` | en | 3 | 3 | `tools/cli`、`tools/code-completion`、`tools/coding` |
| `image` | en | 4 | 4 | `tools/community`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-relighting` |
| `image-editor` | en | 2 | 2 | `tools/background-changer`、`tools/image-enhancer` |
| `image-enhancer` | en | 2 | 2 | `tools/image-editor`、`tools/image-generator` |
| `image-generator` | en | 4 | 4 | `tools/background-changer`、`tools/headshot-generator`、`tools/tattoo-generator`、`tools/virtual-staging` |
| `image-relighting` | en | 2 | 2 | `tools/image-editor`、`tools/image-enhancer` |
| `image-to-video` | en | 5 | 5 | `tools/animation-generator`、`tools/filmmaking`、`tools/image-generator`、`tools/video-editor`、`tools/video-generator` |
| `influencer-marketing` | en | 1 | 1 | `tools/affiliate-marketing` |
| `interview-assistant` | en | 2 | 2 | `tools/lead-generation`、`tools/recruiting` |
| `knowledge-base` | en | 3 | 3 | `blog/agent-memory`、`tools/note-taker`、`tools/search-engine` |
| `lead-generation` | en | 3 | 3 | `tools/b2b`、`tools/knowledge-base`、`tools/recruiting` |
| `legal` | en | 3 | 3 | `tools/notes-generator`、`tools/productivity`、`tools/text-generator` |
| `linkedin` | en | 4 | 4 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting`、`tools/text-generator` |
| `lip-sync` | en | 3 | 3 | `tools/avatar`、`tools/video-to-video`、`tools/video-translator` |
| `llm` | en | 10 | 10 | `tools/api`、`tools/chatbot`、`tools/documentation`、`tools/geo`、`tools/knowledge-base`、`tools/llm-for-coding`、`tools/llm-for-reasoning`、`tools/search-engine`、`tools/text-generator`、`tools/workflow` |
| `llm-for-coding` | en | 10 | 10 | `tools/code-completion`、`tools/code-review`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/knowledge-base`、`tools/llm`、`tools/llm-for-math`、`tools/search-engine`、`tools/vibe-coding` |
| `llm-for-math` | en | 8 | 8 | `tools/api`、`tools/browser`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/llm`、`tools/llm-for-coding`、`tools/text-generator` |
| `llm-for-reasoning` | en | 6 | 6 | `tools/api`、`tools/directory`、`tools/llm`、`tools/multimodal-llm`、`tools/search-engine`、`tools/text-generator` |
| `logo-generator` | en | 6 | 6 | `insights/ai-logo-design`、`media-kit`、`tools/background-changer`、`tools/design`、`tools/image-generator`、`tools/poster-generator` |
| `memory` | en | 4 | 4 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `multimodal-llm` | en | 8 | 8 | `tools/api`、`tools/browser`、`tools/directory`、`tools/documentation`、`tools/image-generator`、`tools/llm`、`tools/ocr`、`tools/web-search-api` |
| `music-generator` | en | 2 | 2 | `tools/video-editor`、`tools/voice-changer` |
| `music-video-generator` | en | 5 | 5 | `tools/lip-sync`、`tools/music-generator`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-generator` |
| `note-taker` | en | 4 | 4 | `blog/medical-scribe`、`tools/knowledge-base`、`tools/notes-generator`、`tools/speech-to-text` |
| `notes-generator` | en | 3 | 3 | `tools/ai-scheduling`、`tools/note-taker`、`tools/voice-cloning` |
| `ocr` | en | 3 | 3 | `tools/image-enhancer`、`tools/knowledge-base`、`tools/note-taker` |
| `openclaw-alternatives` | en | 7 | 7 | `tools/agent-for-desktop`、`tools/api`、`tools/chatbot`、`tools/directory`、`tools/documentation`、`tools/knowledge-base`、`tools/productivity` |
| `poster-generator` | en | 3 | 3 | `tools/design`、`tools/fashion`、`tools/image-generator` |
| `presentation-maker` | en | 3 | 3 | `tools/design`、`tools/essay-writer`、`tools/image-generator` |
| `productivity` | en | 2 | 2 | `tools/hr-assistant`、`tools/note-taker` |
| `recruiting` | en | 3 | 3 | `tools/hr-assistant`、`tools/interview-assistant`、`tools/note-taker` |
| `referral-program` | en | 4 | 4 | `marketing/referral-program`、`tools/affiliate-marketing`、`tools/b2b`、`tools/lead-generation` |
| `religion` | en | 3 | 3 | `tools/essay-writer`、`tools/knowledge-base`、`tools/presentation-maker` |
| `search-engine` | en | 5 | 5 | `tools/browser`、`tools/evaluation`、`tools/geo`、`tools/knowledge-base`、`tools/search-indexing` |
| `search-indexing` | en | 3 | 3 | `tools/llm`、`tools/memory`、`tools/search-engine` |
| `short-drama` | en | 3 | 3 | `tools/animation-generator`、`tools/video-generator`、`tools/workflow` |
| `social-cards-generator` | en | 5 | 5 | `tools/api`、`tools/geo`、`tools/image-generator`、`tools/logo-generator`、`tools/web-scraping` |
| `speech-to-text` | en | 5 | 5 | `blog/medical-scribe`、`tools/accent-conversion`、`tools/note-taker`、`tools/text-to-speech`、`tools/voice-changer` |
| `spreadsheet` | en | 3 | 3 | `tools/app-builder`、`tools/presentation-maker`、`tools/web-scraping` |
| `story-generator` | en | 2 | 2 | `tools/essay-writer`、`tools/text-generator` |
| `tattoo-generator` | en | 3 | 3 | `tools/avatar`、`tools/image`、`tools/image-generator` |
| `text` | en | 3 | 3 | `tools/essay-writer`、`tools/text-generator`、`tools/text-translator` |
| `text-generator` | en | 6 | 6 | `tools/documentation`、`tools/essay-writer`、`tools/evaluation`、`tools/llm`、`tools/presentation-maker`、`tools/story-generator` |
| `text-to-speech` | en | 2 | 2 | `tools/voice-changer`、`tools/voice-cloning` |
| `text-to-video` | en | 5 | 5 | `tools/image-to-video`、`tools/video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator` |
| `text-translator` | en | 5 | 5 | `tools/audio-translator`、`tools/essay-writer`、`tools/llm`、`tools/text-generator`、`tools/video-translator` |
| `user-research` | en | 2 | 2 | `tools/ai-scheduling`、`tools/productivity` |
| `vibe-coding` | en | 2 | 2 | `tools/app-builder`、`tools/coding` |
| `video` | en | 6 | 6 | `tools/canvas-video`、`tools/filmmaking`、`tools/image-to-video`、`tools/music-video-generator`、`tools/text-to-video`、`tools/video-generator` |
| `video-clipping` | en | 4 | 4 | `tools/text-to-video`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `video-editor` | en | 5 | 5 | `tools/video`、`tools/video-clipping`、`tools/video-effects`、`tools/video-generator`、`tools/video-to-video` |
| `video-effects` | en | 5 | 5 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator`、`tools/video-to-video` |
| `video-generator` | en | 5 | 5 | `tools/canvas-video`、`tools/image-to-video`、`tools/text-to-video`、`tools/video-clipping`、`tools/video-editor` |
| `video-to-video` | en | 5 | 5 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-effects`、`tools/video-generator`、`tools/video-translator` |
| `video-translator` | en | 4 | 4 | `tools/audio-translator`、`tools/lip-sync`、`tools/video`、`tools/video-clipping` |
| `virtual-staging` | en | 1 | 1 | `tools/headshot-generator` |
| `voice` | en | 4 | 4 | `tools/accent-conversion`、`tools/notes-generator`、`tools/text-to-speech`、`tools/voice-cloning` |
| `voice-changer` | en | 1 | 1 | `tools/text-to-speech` |
| `voice-cloning` | en | 2 | 2 | `tools/text-to-speech`、`tools/voice-changer` |
| `web-scraping` | en | 2 | 2 | `tools/geo`、`tools/web-search-api` |
| `web-search-api` | en | 5 | 5 | `tools/knowledge-base`、`tools/llm`、`tools/search-indexing`、`tools/text-generator`、`tools/workflow` |
| `website-builder` | en | 3 | 3 | `tools/coding`、`tools/design`、`tools/image-generator` |
| `workflow` | en | 6 | 6 | `blog/agent-to-agent`、`tools/agent-skills`、`tools/browser`、`tools/canvas-video`、`tools/coding`、`tools/productivity` |
| `world-model` | en | 8 | 8 | `tools/3d`、`tools/directory`、`tools/image-generator`、`tools/llm`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/web-search-api` |
| `3d` | zh | 6 | 6 | `blog/cad`、`tools/3d-model-generator`、`tools/3d-modelling`、`tools/3d-scanner`、`tools/design`、`tools/image-generator` |
| `3d-model-generator` | zh | 3 | 4 | `tools/3d-modelling`、`tools/3d-scanner`、`tools/world-model` ⚠重复 |
| `3d-modelling` | zh | 4 | 4 | `blog/cad`、`tools/3d`、`tools/3d-model-generator`、`tools/3d-scanner` |
| `3d-scanner` | zh | 3 | 5 | `tools/3d-model-generator`、`tools/3d-modelling`、`tools/world-model` ⚠重复 |
| `accent-conversion` | zh | 4 | 5 | `tools/education`、`tools/text-to-speech`、`tools/voice-changer`、`tools/voice-cloning` ⚠重复 |
| `affiliate-marketing` | zh | 4 | 4 | `blog/agentic-commerce`、`marketing/affiliate`、`tools/influencer-marketing`、`tools/referral-program` |
| `agent-for-desktop` | zh | 13 | 13 | `blog/multi-agent`、`tools/api`、`tools/authentication`、`tools/browser`、`tools/cli`、`tools/directory`、`tools/evaluation`、`tools/geo`、`tools/ide`、`tools/knowledge-base`、`tools/llm`、`tools/productivity`、`tools/workflow` |
| `agent-skills` | zh | 11 | 11 | `blog/agent-memory`、`skills`、`tools/api`、`tools/browser`、`tools/cli`、`tools/code-review`、`tools/directory`、`tools/evaluation`、`tools/knowledge-base`、`tools/productivity`、`tools/vibe-coding` |
| `ai-homework-helper` | zh | 2 | 2 | `tools/education`、`tools/essay-writer` |
| `ai-scheduling` | zh | 5 | 5 | `tools/family-assistant`、`tools/lead-generation`、`tools/note-taker`、`tools/productivity`、`tools/workflow` |
| `animation-generator` | zh | 5 | 5 | `tools/animation-library`、`tools/filmmaking`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video` |
| `animation-library` | zh | 5 | 5 | `tools/design`、`tools/vibe-coding`、`tools/video-effects`、`tools/video-generator`、`tools/website-builder` |
| `api` | zh | 7 | 7 | `tools/agent-skills`、`tools/coding`、`tools/documentation`、`tools/image-generator`、`tools/llm`、`tools/video-generator`、`tools/workflow` |
| `app-builder` | zh | 3 | 3 | `tools/coding`、`tools/vibe-coding`、`tools/website-builder` |
| `audio-translator` | zh | 5 | 7 | `tools/accent-conversion`、`tools/speech-to-text`、`tools/text-to-speech`、`tools/video-translator`、`tools/voice-changer` ⚠重复 |
| `authentication` | zh | 8 | 8 | `blog/agentic-commerce`、`tools/browser`、`tools/chatbot`、`tools/documentation`、`tools/llm`、`tools/notes-generator`、`tools/productivity`、`tools/user-research` |
| `avatar` | zh | 10 | 10 | `tools/api`、`tools/background-changer`、`tools/image`、`tools/image-editor`、`tools/lip-sync`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-translator`、`tools/web-search-api`、`tools/workflow` |
| `b2b` | zh | 4 | 4 | `tools/knowledge-base`、`tools/lead-generation`、`tools/linkedin`、`tools/web-scraping` |
| `background-changer` | zh | 6 | 7 | `tools/avatar`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator`、`tools/logo-generator`、`tools/text-generator` ⚠重复 |
| `browser` | zh | 5 | 5 | `tools/agent-for-desktop`、`tools/coding`、`tools/headless-browser`、`tools/search-engine`、`tools/workflow` |
| `canvas-video` | zh | 5 | 6 | `tools/image-to-video`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/workflow` ⚠重复 |
| `character-chat` | zh | 8 | 8 | `tools/api`、`tools/evaluation`、`tools/geo`、`tools/notes-generator`、`tools/productivity`、`tools/text-generator`、`tools/text-to-speech`、`tools/web-search-api` |
| `chatbot` | zh | 4 | 4 | `tools/b2b`、`tools/coding`、`tools/llm`、`tools/productivity` |
| `cli` | zh | 2 | 2 | `tools/coding`、`tools/vibe-coding` |
| `code-completion` | zh | 4 | 4 | `tools/code-review`、`tools/coding`、`tools/ide`、`tools/llm-for-coding` |
| `code-review` | zh | 7 | 7 | `tools/code-completion`、`tools/coding`、`tools/directory`、`tools/llm`、`tools/productivity`、`tools/text-generator`、`tools/workflow` |
| `coding` | zh | 5 | 5 | `tools/agent-skills`、`tools/code-completion`、`tools/code-review`、`tools/ide`、`tools/vibe-coding` |
| `community` | zh | 2 | 2 | `tools/directory`、`tools/knowledge-base` |
| `dating` | zh | 2 | 3 | `tools/ai-scheduling`、`tools/character-chat` ⚠重复 |
| `design` | zh | 7 | 7 | `blog/interior-design`、`tools/animation-library`、`tools/image-editor`、`tools/image-generator`、`tools/logo-generator`、`tools/poster-generator`、`tools/tattoo-generator` |
| `directory` | zh | 5 | 5 | `tools/community`、`tools/evaluation`、`tools/search-engine`、`tools/search-indexing`、`tools/web-search-api` |
| `documentation` | zh | 17 | 17 | `tools/api`、`tools/app-builder`、`tools/browser`、`tools/cli`、`tools/code-completion`、`tools/code-review`、`tools/coding`、`tools/directory`、`tools/geo`、`tools/ide`、`tools/ocr`、`tools/productivity`、`tools/text-generator`、`tools/vibe-coding`、`tools/web-search-api`、`tools/website-builder`、`tools/workflow` |
| `education` | zh | 2 | 3 | `tools/essay-writer`、`tools/web-search-api` ⚠重复 |
| `essay-writer` | zh | 3 | 3 | `tools/text`、`tools/text-generator`、`tools/web-search-api` |
| `evaluation` | zh | 3 | 3 | `tools/api`、`tools/llm`、`tools/llm-for-coding` |
| `family-assistant` | zh | 5 | 5 | `tools/ai-scheduling`、`tools/chatbot`、`tools/note-taker`、`tools/productivity`、`tools/voice-cloning` |
| `fashion` | zh | 5 | 5 | `tools/3d`、`tools/image`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator` |
| `filmmaking` | zh | 6 | 6 | `tools/animation-library`、`tools/lip-sync`、`tools/short-drama`、`tools/video-generator`、`tools/video-to-video`、`tools/video-translator` |
| `fundraising` | zh | 3 | 3 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting` |
| `geo` | zh | 12 | 13 | `blog/ai-traffic-and-citation-sources`、`blog/ai-visibility`、`marketing/geo`、`tools/browser`、`tools/chatbot`、`tools/notes-generator`、`tools/productivity`、`tools/search-engine`、`tools/spreadsheet`、`tools/text-generator`、`tools/user-research`、`tools/web-search-api` ⚠重复 |
| `headless-browser` | zh | 3 | 3 | `tools/geo`、`tools/llm`、`tools/web-scraping` |
| `headshot-generator` | zh | 4 | 4 | `tools/image-generator`、`tools/image-relighting`、`tools/presentation-maker`、`tools/website-builder` |
| `healthcare` | zh | 5 | 5 | `blog/medical-scribe`、`tools/family-assistant`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `hr-assistant` | zh | 4 | 4 | `tools/chatbot`、`tools/note-taker`、`tools/productivity`、`tools/recruiting` |
| `ide` | zh | 2 | 2 | `tools/code-completion`、`tools/code-review` |
| `image` | zh | 6 | 6 | `tools/community`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-relighting`、`tools/tattoo-generator`、`tools/virtual-staging` |
| `image-editor` | zh | 6 | 6 | `tools/avatar`、`tools/background-changer`、`tools/image`、`tools/image-enhancer`、`tools/image-generator`、`tools/virtual-staging` |
| `image-enhancer` | zh | 2 | 2 | `tools/image-editor`、`tools/ocr` |
| `image-generator` | zh | 5 | 5 | `tools/background-changer`、`tools/headshot-generator`、`tools/image-editor`、`tools/image-enhancer`、`tools/virtual-staging` |
| `image-relighting` | zh | 2 | 2 | `tools/background-changer`、`tools/image-enhancer` |
| `image-to-video` | zh | 5 | 5 | `tools/animation-generator`、`tools/filmmaking`、`tools/image-generator`、`tools/video-editor`、`tools/video-generator` |
| `influencer-marketing` | zh | 5 | 5 | `marketing/influencer`、`tools/affiliate-marketing`、`tools/lead-generation`、`tools/referral-program`、`tools/social-cards-generator` |
| `interview-assistant` | zh | 3 | 3 | `tools/documentation`、`tools/lead-generation`、`tools/text-generator` |
| `knowledge-base` | zh | 4 | 4 | `blog/agent-memory`、`tools/search-engine`、`tools/text-generator`、`tools/web-search-api` |
| `lead-generation` | zh | 4 | 4 | `tools/b2b`、`tools/productivity`、`tools/recruiting`、`tools/referral-program` |
| `legal` | zh | 4 | 4 | `tools/notes-generator`、`tools/productivity`、`tools/religion`、`tools/text-generator` |
| `linkedin` | zh | 4 | 4 | `tools/b2b`、`tools/lead-generation`、`tools/recruiting`、`tools/text-generator` |
| `lip-sync` | zh | 5 | 5 | `tools/avatar`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-to-video`、`tools/video-translator` |
| `llm` | zh | 9 | 9 | `tools/api`、`tools/browser`、`tools/documentation`、`tools/evaluation`、`tools/geo`、`tools/knowledge-base`、`tools/llm-for-coding`、`tools/text-generator`、`tools/workflow` |
| `llm-for-coding` | zh | 11 | 11 | `tools/api`、`tools/code-review`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/knowledge-base`、`tools/llm`、`tools/llm-for-math`、`tools/search-engine`、`tools/vibe-coding`、`tools/workflow` |
| `llm-for-math` | zh | 9 | 9 | `tools/api`、`tools/browser`、`tools/directory`、`tools/documentation`、`tools/evaluation`、`tools/llm`、`tools/llm-for-coding`、`tools/text-generator`、`tools/web-search-api` |
| `llm-for-reasoning` | zh | 10 | 10 | `tools/api`、`tools/browser`、`tools/directory`、`tools/geo`、`tools/llm`、`tools/llm-for-coding`、`tools/multimodal-llm`、`tools/search-engine`、`tools/text-generator`、`tools/web-search-api` |
| `logo-generator` | zh | 6 | 6 | `insights/ai-logo-design`、`media-kit`、`tools/background-changer`、`tools/design`、`tools/image-generator`、`tools/poster-generator` |
| `memory` | zh | 4 | 4 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/productivity` |
| `multimodal-llm` | zh | 9 | 9 | `tools/api`、`tools/documentation`、`tools/evaluation`、`tools/image-generator`、`tools/llm`、`tools/llm-for-math`、`tools/llm-for-reasoning`、`tools/web-search-api`、`tools/workflow` |
| `music-generator` | zh | 3 | 3 | `tools/music-video-generator`、`tools/video-editor`、`tools/voice` |
| `music-video-generator` | zh | 5 | 5 | `tools/lip-sync`、`tools/music-generator`、`tools/text-to-speech`、`tools/video-editor`、`tools/video-generator` |
| `note-taker` | zh | 3 | 3 | `blog/medical-scribe`、`tools/speech-to-text`、`tools/text-generator` |
| `notes-generator` | zh | 3 | 3 | `tools/note-taker`、`tools/text-generator`、`tools/voice-cloning` |
| `ocr` | zh | 3 | 3 | `tools/image-enhancer`、`tools/knowledge-base`、`tools/text-to-speech` |
| `openclaw-alternatives` | zh | 4 | 4 | `tools/agent-for-desktop`、`tools/api`、`tools/documentation`、`tools/knowledge-base` |
| `poster-generator` | zh | 5 | 5 | `tools/fashion`、`tools/image-editor`、`tools/image-generator`、`tools/logo-generator`、`tools/social-cards-generator` |
| `presentation-maker` | zh | 2 | 2 | `tools/logo-generator`、`tools/text-generator` |
| `productivity` | zh | 3 | 3 | `tools/ai-scheduling`、`tools/text-generator`、`tools/workflow` |
| `recruiting` | zh | 5 | 5 | `tools/documentation`、`tools/hr-assistant`、`tools/lead-generation`、`tools/note-taker`、`tools/productivity` |
| `referral-program` | zh | 5 | 5 | `marketing/referral-program`、`tools/affiliate-marketing`、`tools/influencer-marketing`、`tools/linkedin`、`tools/productivity` |
| `religion` | zh | 3 | 3 | `tools/community`、`tools/knowledge-base`、`tools/text-translator` |
| `search-engine` | zh | 6 | 6 | `tools/browser`、`tools/evaluation`、`tools/geo`、`tools/knowledge-base`、`tools/text-generator`、`tools/web-search-api` |
| `search-indexing` | zh | 5 | 5 | `seo/internal-links`、`seo/website-structure`、`tools/search-engine`、`tools/web-search-api`、`tools/website-builder` |
| `short-drama` | zh | 3 | 3 | `tools/animation-generator`、`tools/video-generator`、`tools/workflow` |
| `social-cards-generator` | zh | 5 | 5 | `tools/api`、`tools/geo`、`tools/image-generator`、`tools/logo-generator`、`tools/web-scraping` |
| `speech-to-text` | zh | 5 | 5 | `blog/medical-scribe`、`tools/accent-conversion`、`tools/note-taker`、`tools/video-translator`、`tools/voice-changer` |
| `spreadsheet` | zh | 3 | 3 | `tools/app-builder`、`tools/productivity`、`tools/web-scraping` |
| `story-generator` | zh | 2 | 2 | `tools/text-generator`、`tools/text-to-video` |
| `tattoo-generator` | zh | 3 | 3 | `tools/image`、`tools/image-editor`、`tools/image-generator` |
| `text` | zh | 4 | 4 | `tools/essay-writer`、`tools/story-generator`、`tools/text-generator`、`tools/text-to-speech` |
| `text-generator` | zh | 5 | 5 | `tools/chatbot`、`tools/coding`、`tools/essay-writer`、`tools/llm`、`tools/story-generator` |
| `text-to-speech` | zh | 2 | 2 | `tools/voice-changer`、`tools/voice-cloning` |
| `text-to-video` | zh | 5 | 5 | `tools/image-to-video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `text-translator` | zh | 5 | 5 | `tools/audio-translator`、`tools/essay-writer`、`tools/llm`、`tools/text-generator`、`tools/video-translator` |
| `user-research` | zh | 2 | 2 | `tools/ai-scheduling`、`tools/productivity` |
| `vibe-coding` | zh | 3 | 3 | `tools/app-builder`、`tools/code-completion`、`tools/coding` |
| `video` | zh | 7 | 7 | `tools/canvas-video`、`tools/filmmaking`、`tools/image-to-video`、`tools/music-video-generator`、`tools/short-drama`、`tools/text-to-video`、`tools/video-generator` |
| `video-clipping` | zh | 5 | 5 | `tools/text-to-video`、`tools/video`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator` |
| `video-editor` | zh | 6 | 6 | `tools/text-to-video`、`tools/video`、`tools/video-clipping`、`tools/video-effects`、`tools/video-generator`、`tools/video-to-video` |
| `video-effects` | zh | 5 | 5 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator`、`tools/video-to-video` |
| `video-generator` | zh | 7 | 9 | `tools/avatar`、`tools/image-to-video`、`tools/music-video-generator`、`tools/text-to-video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-to-video` ⚠重复 |
| `video-to-video` | zh | 6 | 6 | `tools/animation-generator`、`tools/video-clipping`、`tools/video-editor`、`tools/video-effects`、`tools/video-generator`、`tools/video-translator` |
| `video-translator` | zh | 6 | 6 | `tools/lip-sync`、`tools/speech-to-text`、`tools/video`、`tools/video-clipping`、`tools/video-editor`、`tools/video-generator` |
| `virtual-staging` | zh | 6 | 6 | `tools/3d`、`tools/background-changer`、`tools/headshot-generator`、`tools/image-editor`、`tools/image-enhancer`、`tools/image-generator` |
| `voice` | zh | 4 | 4 | `tools/notes-generator`、`tools/speech-to-text`、`tools/text-to-speech`、`tools/voice-cloning` |
| `voice-changer` | zh | 2 | 2 | `tools/text-to-speech`、`tools/voice-cloning` |
| `voice-cloning` | zh | 4 | 4 | `tools/audio-translator`、`tools/lip-sync`、`tools/text-to-speech`、`tools/voice-changer` |
| `web-scraping` | zh | 5 | 5 | `blog/web-fetch`、`tools/geo`、`tools/llm`、`tools/web-search-api`、`tools/workflow` |
| `web-search-api` | zh | 7 | 7 | `blog/web-fetch`、`tools/api`、`tools/geo`、`tools/llm`、`tools/search-indexing`、`tools/text-generator`、`tools/workflow` |
| `website-builder` | zh | 5 | 5 | `tools/coding`、`tools/design`、`tools/documentation`、`tools/image-generator`、`tools/vibe-coding` |
| `workflow` | zh | 7 | 7 | `blog/agent-to-agent`、`tools/agent-skills`、`tools/browser`、`tools/canvas-video`、`tools/coding`、`tools/productivity`、`tools/text-generator` |
| `world-model` | zh | 7 | 7 | `tools/3d`、`tools/image-to-video`、`tools/llm`、`tools/text-to-video`、`tools/video-editor`、`tools/video-generator`、`tools/video-to-video` |

### seo

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `best-tools` | en | 0 | 0 | — |
| `branded-queries-filter-google-search-console` | en | 0 | 0 | — |
| `breadcrumbs` | en | 4 | 5 | `marketing/geo`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap` ⚠重复 |
| `category-pages` | en | 5 | 7 | `seo/breadcrumbs`、`seo/internal-links`、`seo/navigation-menu`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `checklist` | en | 27 | 27 | `marketing/geo`、`seo/category-pages`、`seo/crawler`、`seo/create-blog`、`seo/external-links`、`seo/google-tag-manager`、`seo/how-search-engine-works`、`seo/html-tag`、`seo/internal-links`、`seo/landing-page`、`seo/learn-seo`、`seo/link-building`、`seo/meta-tag`、`seo/programmatic-seo`、`seo/redirect-chain`、`seo/robots-txt`、`seo/schema`、`seo/serp`、`seo/sitemap`、`seo/subdomain-vs-subfolder`、`seo/submit-website`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-rendering`、`seo/website-structure`、`seo/website-traffic`、`tools/geo` |
| `crawler` | en | 0 | 0 | — |
| `create-blog` | en | 0 | 0 | — |
| `dark-traffic` | en | 0 | 0 | — |
| `domain` | en | 4 | 6 | `seo/redirect-chain`、`seo/robots-txt`、`seo/submit-website`、`seo/website-structure` ⚠重复 |
| `example-article` | en | 0 | 0 | — |
| `external-links` | en | 0 | 0 | — |
| `glossary` | en | 0 | 0 | — |
| `google-tag-manager` | en | 0 | 0 | — |
| `how-search-engine-works` | en | 0 | 0 | — |
| `html-a-tag` | en | 0 | 0 | — |
| `html-tag` | en | 5 | 8 | `seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `internal-links` | en | 0 | 0 | — |
| `landing-page` | en | 0 | 0 | — |
| `learn-seo` | en | 3 | 3 | `glossary`、`seo/how-search-engine-works`、`seo/website-indexing` |
| `link-building` | en | 0 | 0 | — |
| `local-search-engines` | en | 0 | 0 | — |
| `meta-tag` | en | 0 | 0 | — |
| `navigation-menu` | en | 3 | 3 | `seo/html-a-tag`、`seo/internal-links`、`seo/website-structure` |
| `new-domains-tld` | en | 0 | 0 | — |
| `programmatic-seo` | en | 7 | 7 | `home`、`seo/category-pages`、`seo/internal-links`、`seo/sitemap`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-structure` |
| `redirect-chain` | en | 0 | 0 | — |
| `robots-txt` | en | 0 | 0 | — |
| `schema` | en | 5 | 6 | `marketing/geo`、`seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag`、`seo/sitemap` ⚠重复 |
| `search-engine` | en | 10 | 10 | `marketing/geo`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/local-search-engines`、`seo/schema`、`seo/website-traffic`、`tools/browser`、`tools/search-engine`、`tools/web-search-api` |
| `serp` | en | 0 | 0 | — |
| `sitemap` | en | 0 | 0 | — |
| `subdomain-vs-subfolder` | en | 0 | 0 | — |
| `submit-website` | en | 0 | 0 | — |
| `url-optimization` | en | 6 | 8 | `seo/breadcrumbs`、`seo/meta-tag`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `website-indexing` | en | 0 | 0 | — |
| `website-rendering` | en | 0 | 0 | — |
| `website-structure` | en | 2 | 4 | `seo/external-links`、`seo/internal-links` ⚠重复 |
| `website-traffic` | en | 4 | 14 | `seo/dark-traffic`、`seo/internal-links`、`seo/link-building`、`seo/website-structure` ⚠重复 |
| `best-tools` | zh | 0 | 0 | — |
| `branded-queries-filter-google-search-console` | zh | 0 | 0 | — |
| `breadcrumbs` | zh | 5 | 6 | `marketing/geo`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap`、`seo/submit-website` ⚠重复 |
| `category-pages` | zh | 5 | 5 | `seo/breadcrumbs`、`seo/internal-links`、`seo/navigation-menu`、`seo/sitemap`、`seo/website-structure` |
| `checklist` | zh | 28 | 28 | `marketing/geo`、`marketing/keyword-research`、`seo/category-pages`、`seo/crawler`、`seo/create-blog`、`seo/external-links`、`seo/google-tag-manager`、`seo/how-search-engine-works`、`seo/html-tag`、`seo/internal-links`、`seo/landing-page`、`seo/learn-seo`、`seo/link-building`、`seo/meta-tag`、`seo/programmatic-seo`、`seo/redirect-chain`、`seo/robots-txt`、`seo/schema`、`seo/serp`、`seo/sitemap`、`seo/subdomain-vs-subfolder`、`seo/submit-website`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-rendering`、`seo/website-structure`、`seo/website-traffic`、`tools/geo` |
| `crawler` | zh | 0 | 0 | — |
| `create-blog` | zh | 0 | 0 | — |
| `dark-traffic` | zh | 0 | 0 | — |
| `domain` | zh | 4 | 5 | `seo/redirect-chain`、`seo/robots-txt`、`seo/submit-website`、`seo/website-structure` ⚠重复 |
| `example-article` | zh | 0 | 0 | — |
| `external-links` | zh | 0 | 0 | — |
| `glossary` | zh | 0 | 0 | — |
| `google-tag-manager` | zh | 0 | 0 | — |
| `how-search-engine-works` | zh | 0 | 0 | — |
| `html-a-tag` | zh | 0 | 0 | — |
| `html-tag` | zh | 4 | 6 | `seo/internal-links`、`seo/meta-tag`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `internal-links` | zh | 0 | 0 | — |
| `landing-page` | zh | 0 | 0 | — |
| `learn-seo` | zh | 3 | 3 | `glossary`、`seo/how-search-engine-works`、`seo/website-indexing` |
| `link-building` | zh | 0 | 0 | — |
| `local-search-engines` | zh | 0 | 0 | — |
| `meta-tag` | zh | 0 | 0 | — |
| `navigation-menu` | zh | 3 | 3 | `seo`、`seo/robots-txt`、`seo/sitemap` |
| `new-domains-tld` | zh | 0 | 0 | — |
| `programmatic-seo` | zh | 7 | 7 | `home`、`seo/category-pages`、`seo/internal-links`、`seo/sitemap`、`seo/url-optimization`、`seo/website-indexing`、`seo/website-structure` |
| `redirect-chain` | zh | 0 | 0 | — |
| `robots-txt` | zh | 0 | 0 | — |
| `schema` | zh | 6 | 8 | `marketing/geo`、`seo/breadcrumbs`、`seo/internal-links`、`seo/meta-tag`、`seo/serp`、`seo/sitemap` ⚠重复 |
| `search-engine` | zh | 10 | 10 | `marketing/geo`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/local-search-engines`、`seo/schema`、`seo/website-traffic`、`tools/browser`、`tools/search-engine`、`tools/web-search-api` |
| `serp` | zh | 0 | 0 | — |
| `sitemap` | zh | 2 | 3 | `seo/internal-links`、`seo/website-indexing` ⚠重复 |
| `subdomain-vs-subfolder` | zh | 0 | 0 | — |
| `submit-website` | zh | 0 | 0 | — |
| `url-optimization` | zh | 6 | 8 | `seo/breadcrumbs`、`seo/meta-tag`、`seo/navigation-menu`、`seo/schema`、`seo/sitemap`、`seo/website-structure` ⚠重复 |
| `website-indexing` | zh | 0 | 0 | — |
| `website-rendering` | zh | 0 | 0 | — |
| `website-structure` | zh | 0 | 0 | — |
| `website-traffic` | zh | 4 | 14 | `seo/dark-traffic`、`seo/internal-links`、`seo/link-building`、`seo/website-structure` ⚠重复 |

### blog

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `agent-memory` | en | 5 | 5 | `blog/agent-sandbox`、`blog/ai-training-data`、`tools/agent-skills`、`tools/knowledge-base`、`tools/openclaw-alternatives` |
| `agent-sandbox` | en | 4 | 4 | `blog/inference-infrastructure`、`tools/agent-for-desktop`、`tools/authentication`、`tools/headless-browser` |
| `agent-to-agent` | en | 5 | 5 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/character-chat`、`tools/community`、`tools/workflow` |
| `agentic-commerce` | en | 5 | 5 | `tools/affiliate-marketing`、`tools/chatbot`、`tools/geo`、`tools/memory`、`tools/search-engine` |
| `agentic-payments` | en | 5 | 5 | `blog/agentic-commerce`、`tools/agent-skills`、`tools/api`、`tools/openclaw-alternatives`、`tools/web-search-api` |
| `ai-components` | en | 2 | 2 | `tools/app-builder`、`tools/design` |
| `ai-flashcards` | en | 3 | 3 | `blog/ai-language-learning`、`tools/ai-homework-helper`、`tools/notes-generator` |
| `ai-language-learning` | en | 2 | 2 | `blog/ai-flashcards`、`tools/ai-homework-helper` |
| `ai-traffic-and-citation-sources` | en | 2 | 3 | `blog/ai-visibility`、`tools/geo` ⚠重复 |
| `ai-training-data` | en | 5 | 5 | `blog/inference-infrastructure`、`tools/evaluation`、`tools/llm`、`tools/web-scraping`、`tools/world-model` |
| `ai-visibility` | en | 3 | 3 | `blog/ai-traffic-and-citation-sources`、`tools/geo`、`tools/search-engine` |
| `cad` | en | 4 | 4 | `blog/interior-design`、`tools/3d`、`tools/3d-model-generator`、`tools/workflow` |
| `coding-plan` | en | 5 | 9 | `blog/rate-limit-reset`、`marketing/competitive-analysis`、`marketing/pricing-strategy`、`marketing/referral-program`、`marketing/x-formerly-twitter` ⚠重复 |
| `data-engineering-agent` | en | 3 | 3 | `blog/inference-infrastructure`、`tools/agent-skills`、`tools/api` |
| `git-hosting` | en | 4 | 7 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/cli`、`tools/code-review` ⚠重复 |
| `github-for-marketing` | en | 2 | 2 | `blog/how-to-write-github-readme`、`services` |
| `how-to-add-payments-to-vibe-coded-app` | en | 5 | 5 | `blog/agentic-payments`、`blog/ai-traffic-and-citation-sources`、`insights/indie-hackers`、`tools/app-builder`、`tools/vibe-coding` |
| `how-to-name-ai-products` | en | 1 | 1 | `seo/domain` |
| `how-to-write-github-readme` | en | 2 | 2 | `blog/github-for-marketing`、`services` |
| `inference-infrastructure` | en | 2 | 2 | `blog/agent-sandbox`、`blog/ai-training-data` |
| `interior-design` | en | 4 | 4 | `blog/cad`、`tools/background-changer`、`tools/image-enhancer`、`tools/image-generator` |
| `medical-scribe` | en | 4 | 4 | `tools/chatbot`、`tools/knowledge-base`、`tools/note-taker`、`tools/speech-to-text` |
| `multi-agent` | en | 5 | 5 | `blog/agent-sandbox`、`tools/agent-for-desktop`、`tools/hr-assistant`、`tools/llm`、`tools/workflow` |
| `rate-limit-reset` | en | 4 | 6 | `marketing/affiliate`、`marketing/competitive-analysis`、`marketing/pricing-strategy`、`marketing/x-formerly-twitter` ⚠重复 |
| `web-fetch` | en | 6 | 6 | `blog/data-engineering-agent`、`tools/headless-browser`、`tools/llm`、`tools/search-indexing`、`tools/web-scraping`、`tools/web-search-api` |
| `wrapped-marketing` | en | 4 | 5 | `blog/rate-limit-reset`、`blog/ugc-marketing`、`marketing/creator-challenge-program`、`marketing/pricing-strategy` ⚠重复 |
| `agent-memory` | zh | 5 | 5 | `blog/agent-sandbox`、`blog/ai-training-data`、`tools/agent-skills`、`tools/knowledge-base`、`tools/openclaw-alternatives` |
| `agent-sandbox` | zh | 5 | 5 | `blog/agent-to-agent`、`blog/inference-infrastructure`、`tools/agent-for-desktop`、`tools/authentication`、`tools/headless-browser` |
| `agent-to-agent` | zh | 6 | 6 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/agent-skills`、`tools/character-chat`、`tools/community`、`tools/workflow` |
| `agentic-commerce` | zh | 6 | 6 | `blog/agentic-payments`、`tools/affiliate-marketing`、`tools/chatbot`、`tools/geo`、`tools/memory`、`tools/search-engine` |
| `agentic-payments` | zh | 5 | 5 | `blog/agentic-commerce`、`tools/agent-skills`、`tools/api`、`tools/openclaw-alternatives`、`tools/web-search-api` |
| `ai-components` | zh | 2 | 2 | `tools/app-builder`、`tools/design` |
| `ai-flashcards` | zh | 3 | 3 | `blog/ai-language-learning`、`tools/ai-homework-helper`、`tools/notes-generator` |
| `ai-language-learning` | zh | 2 | 2 | `blog/ai-flashcards`、`tools/ai-homework-helper` |
| `ai-traffic-and-citation-sources` | zh | 2 | 3 | `blog/ai-visibility`、`tools/geo` ⚠重复 |
| `ai-training-data` | zh | 6 | 6 | `blog/data-engineering-agent`、`blog/inference-infrastructure`、`tools/evaluation`、`tools/llm`、`tools/web-scraping`、`tools/world-model` |
| `ai-visibility` | zh | 4 | 4 | `blog/ai-traffic-and-citation-sources`、`tools/geo`、`tools/search-engine`、`tools/text-generator` |
| `cad` | zh | 4 | 4 | `blog/interior-design`、`tools/3d`、`tools/3d-model-generator`、`tools/workflow` |
| `coding-plan` | zh | 5 | 9 | `blog/rate-limit-reset`、`marketing/competitive-analysis`、`marketing/pricing-strategy`、`marketing/referral-program`、`marketing/x-formerly-twitter` ⚠重复 |
| `data-engineering-agent` | zh | 3 | 3 | `blog/inference-infrastructure`、`tools/agent-skills`、`tools/api` |
| `git-hosting` | zh | 4 | 7 | `blog/agent-sandbox`、`blog/multi-agent`、`tools/cli`、`tools/code-review` ⚠重复 |
| `github-for-marketing` | zh | 2 | 2 | `blog/how-to-write-github-readme`、`services` |
| `how-to-add-payments-to-vibe-coded-app` | zh | 5 | 5 | `blog/agentic-payments`、`blog/ai-traffic-and-citation-sources`、`insights/indie-hackers`、`tools/app-builder`、`tools/vibe-coding` |
| `how-to-name-ai-products` | zh | 1 | 1 | `seo/domain` |
| `how-to-write-github-readme` | zh | 2 | 2 | `blog/github-for-marketing`、`services` |
| `inference-infrastructure` | zh | 3 | 3 | `blog/agent-sandbox`、`blog/ai-training-data`、`tools/agent-skills` |
| `interior-design` | zh | 4 | 4 | `blog/cad`、`tools/background-changer`、`tools/image-enhancer`、`tools/image-generator` |
| `medical-scribe` | zh | 5 | 5 | `tools/chatbot`、`tools/knowledge-base`、`tools/legal`、`tools/note-taker`、`tools/speech-to-text` |
| `multi-agent` | zh | 8 | 8 | `blog/agent-sandbox`、`blog/agent-to-agent`、`tools/agent-for-desktop`、`tools/agent-skills`、`tools/hr-assistant`、`tools/llm`、`tools/openclaw-alternatives`、`tools/workflow` |
| `rate-limit-reset` | zh | 4 | 6 | `marketing/affiliate`、`marketing/competitive-analysis`、`marketing/pricing-strategy`、`marketing/x-formerly-twitter` ⚠重复 |
| `web-fetch` | zh | 6 | 6 | `blog/data-engineering-agent`、`tools/headless-browser`、`tools/llm`、`tools/search-indexing`、`tools/web-scraping`、`tools/web-search-api` |
| `wrapped-marketing` | zh | 4 | 5 | `blog/rate-limit-reset`、`blog/ugc-marketing`、`marketing/creator-challenge-program`、`marketing/pricing-strategy` ⚠重复 |

### marketing

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `affiliate` | en | 1 | 2 | `tools/affiliate-marketing` ⚠重复 |
| `competitive-analysis` | en | 2 | 3 | `marketing/email-marketing`、`marketing/keyword-research` ⚠重复 |
| `creator-challenge-program` | en | 1 | 1 | `marketing/creator-program` |
| `creator-program` | en | 1 | 1 | `marketing/affiliate` |
| `email-marketing` | en | 2 | 3 | `marketing/competitive-analysis`、`marketing/keyword-research` ⚠重复 |
| `geo` | en | 8 | 15 | `blog/ai-traffic-and-citation-sources`、`blog/ai-visibility`、`marketing/affiliate`、`marketing/creator-program`、`marketing/influencer`、`seo/how-search-engine-works`、`seo/search-engine`、`tools/geo` ⚠重复 |
| `growth-case-studies` | en | 0 | 0 | — |
| `influencer` | en | 2 | 3 | `marketing/affiliate`、`marketing/creator-program` ⚠重复 |
| `keyword-research` | en | 1 | 1 | `marketing/competitive-analysis` |
| `lifetime-deal` | en | 7 | 11 | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/creator-program`、`marketing/pricing-strategy`、`marketing/referral-program`、`seo/landing-page` ⚠重复 |
| `localization-strategy` | en | 1 | 1 | `seo/navigation-menu` |
| `marketing-types` | en | 0 | 0 | — |
| `pricing-strategy` | en | 2 | 3 | `marketing/competitive-analysis`、`marketing/lifetime-deal` ⚠重复 |
| `reddit` | en | 0 | 0 | — |
| `referral-program` | en | 1 | 2 | `tools/referral-program` ⚠重复 |
| `ugc-marketing` | en | 8 | 14 | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/influencer`、`marketing/lifetime-deal`、`marketing/referral-program`、`seo/landing-page` ⚠重复 |
| `x-formerly-twitter` | en | 2 | 2 | `insights/indie-hackers`、`marketing/influencer` |
| `affiliate` | zh | 3 | 4 | `marketing/creator-challenge-program`、`marketing/creator-program`、`tools/affiliate-marketing` ⚠重复 |
| `competitive-analysis` | zh | 2 | 3 | `marketing/email-marketing`、`marketing/keyword-research` ⚠重复 |
| `creator-challenge-program` | zh | 1 | 2 | `marketing/creator-program` ⚠重复 |
| `creator-program` | zh | 1 | 1 | `marketing/affiliate` |
| `email-marketing` | zh | 2 | 3 | `marketing/competitive-analysis`、`marketing/keyword-research` ⚠重复 |
| `geo` | zh | 8 | 21 | `blog/ai-traffic-and-citation-sources`、`blog/ai-visibility`、`marketing/affiliate`、`marketing/creator-program`、`marketing/influencer`、`seo/how-search-engine-works`、`seo/search-engine`、`tools/geo` ⚠重复 |
| `growth-case-studies` | zh | 0 | 0 | — |
| `influencer` | zh | 3 | 4 | `marketing/affiliate`、`marketing/creator-program`、`tools/influencer-marketing` ⚠重复 |
| `keyword-research` | zh | 1 | 1 | `marketing/competitive-analysis` |
| `lifetime-deal` | zh | 7 | 11 | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/creator-program`、`marketing/pricing-strategy`、`marketing/referral-program`、`seo/landing-page` ⚠重复 |
| `localization-strategy` | zh | 1 | 1 | `seo/navigation-menu` |
| `marketing-types` | zh | 0 | 0 | — |
| `pricing-strategy` | zh | 2 | 3 | `marketing/competitive-analysis`、`marketing/lifetime-deal` ⚠重复 |
| `reddit` | zh | 2 | 2 | `marketing/influencer`、`marketing/x-formerly-twitter` |
| `referral-program` | zh | 2 | 3 | `marketing/affiliate`、`tools/referral-program` ⚠重复 |
| `ugc-marketing` | zh | 8 | 14 | `blog/rate-limit-reset`、`marketing/affiliate`、`marketing/creator-challenge-program`、`marketing/creator-program`、`marketing/influencer`、`marketing/lifetime-deal`、`marketing/referral-program`、`seo/landing-page` ⚠重复 |
| `x-formerly-twitter` | zh | 3 | 3 | `insights/indie-hackers`、`marketing/influencer`、`seo/meta-tag` |

### insights

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `ai-logo-design` | en | 3 | 4 | `marketing/competitive-analysis`、`tools`、`tools/logo-generator` ⚠重复 |
| `directory-submission-sites` | en | 9 | 9 | `insights/reasons-you-need-seo`、`marketing`、`marketing/geo`、`marketing/keyword-research`、`seo/how-search-engine-works`、`seo/internal-links`、`seo/link-building`、`seo/submit-website`、`seo/website-structure` |
| `generative-ai-landscape` | en | 1 | 1 | `marketing/pricing-strategy` |
| `google` | en | 0 | 0 | — |
| `indie-hackers` | en | 15 | 28 | `insights/directory-submission-sites`、`insights/reasons-you-need-seo`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/email-marketing`、`marketing/geo`、`marketing/growth-case-studies`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/localization-strategy`、`marketing/pricing-strategy`、`marketing/reddit`、`marketing/x-formerly-twitter`、`tools`、`tools/app-builder` ⚠重复 |
| `openai` | en | 0 | 0 | — |
| `reasons-you-need-seo` | en | 8 | 8 | `insights/indie-hackers`、`marketing/geo`、`marketing/keyword-research`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/serp`、`seo/website-traffic` |
| `ai-logo-design` | zh | 3 | 4 | `marketing/competitive-analysis`、`tools`、`tools/logo-generator` ⚠重复 |
| `directory-submission-sites` | zh | 9 | 9 | `insights/reasons-you-need-seo`、`marketing`、`marketing/geo`、`marketing/keyword-research`、`seo/how-search-engine-works`、`seo/internal-links`、`seo/link-building`、`seo/submit-website`、`seo/website-structure` |
| `generative-ai-landscape` | zh | 1 | 1 | `marketing/pricing-strategy` |
| `google` | zh | 0 | 0 | — |
| `indie-hackers` | zh | 15 | 32 | `insights/directory-submission-sites`、`insights/reasons-you-need-seo`、`marketing/affiliate`、`marketing/competitive-analysis`、`marketing/email-marketing`、`marketing/geo`、`marketing/growth-case-studies`、`marketing/keyword-research`、`marketing/lifetime-deal`、`marketing/localization-strategy`、`marketing/pricing-strategy`、`marketing/reddit`、`marketing/x-formerly-twitter`、`tools`、`tools/app-builder` ⚠重复 |
| `openai` | zh | 0 | 0 | — |
| `reasons-you-need-seo` | zh | 8 | 8 | `insights/indie-hackers`、`marketing/geo`、`marketing/keyword-research`、`seo/checklist`、`seo/how-search-engine-works`、`seo/learn-seo`、`seo/serp`、`seo/website-traffic` |

### events

| 文章 | 语言 | distinct | 总量 | 内链目标 |
|------|------|---------:|-----:|---------|
| `founder-park-2024-11-06` | en | 0 | 0 | — |
| `linkloud-2025-02-23` | en | 1 | 1 | `tools/design` |
| `linkloud-2026-01-24` | en | 0 | 0 | — |
| `praxis-2025-09-27` | en | 1 | 1 | `seo/search-engine` |
| `founder-park-2024-11-06` | zh | 0 | 0 | — |
| `linkloud-2025-02-23` | zh | 1 | 1 | `tools/design` |
| `linkloud-2026-01-24` | zh | 0 | 0 | — |
| `praxis-2025-09-27` | zh | 1 | 1 | `seo/search-engine` |

