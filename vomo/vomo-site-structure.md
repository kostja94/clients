# VOMO — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./vomo.md) | [features](./vomo-features.md) | [keywords](./vomo-keywords.md) | [competitors](./vomo-competitors.md) | [use-cases](./vomo-use-cases.md) | [growth-strategy](./vomo-growth-strategy.md) | [others / Sitemap 明细](./vomo-others.md)

---

## 1. 核心路径表

> 本节为**主导航 / 页脚可见**的核心路径。英文 sitemap 另有约 220+ 条 SEO 工具页未进导航，统计与全量清单见 §4 与 [vomo-others.md](./vomo-others.md)。

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页 | AI meeting notes, audio transcription software | P0 |
| `/pricing` | 定价页 | VOMO pricing, AI transcription pricing | P0 |
| `/about` | 关于页 | about VOMO, AI meeting notes company | P1 |
| `/guide` | 博客首页 | AI transcription guide, meeting notes tips | P0 |
| `/guide/{slug}` | 单篇博文 | 长尾关键词（如 "best AI recorder apps"） | P0 |
| `/tools/youtube-transcript` | 工具着陆页 | YouTube transcript generator, YouTube to text | P0 |
| `/tools/ai-voice-memos` | 工具页 | AI voice memos, voice memo transcription | P1 |
| `/tools/ai-scribe` | 工具页 | AI scribe, AI dictation | P2 |
| `/tools/ai-dictation-tool` | 工具页 | AI dictation tool, speech to text dictation | P1 |
| `/tools/audio-to-text` | 工具页 | audio to text converter | P0 |
| `/tools/mp3-to-text` | 工具页 | MP3 to text, convert MP3 to text | P0 |
| `/tools/speech-to-text` | 工具页 | speech to text, speech recognition | P0 |
| `/tools/m4a-to-text` | 工具页 | M4A to text | P1 |
| `/tools/flac-to-text` | 工具页 | FLAC to text | P2 |
| `/tools/wav-to-text` | 工具页 | WAV to text | P2 |
| `/tools/video-to-text` | 工具页 | video to text | P0 |
| `/tools/mp4-to-text` | 工具页 | MP4 to text | P0 |
| `/tools/mpeg-to-text` | 工具页 | MPEG to text | P2 |
| `/tools/video-to-pdf` | 工具页 | video to PDF | P1 |
| `/tools/video-to-image` | 工具页 | video to image | P2 |
| `/tools/mp4-to-image` | 工具页 | MP4 to image | P2 |
| `/tools/audio-to-image` | 工具页 | audio to image | P2 |
| `/tools/mp4-to-html` | 工具页 | MP4 to HTML | P2 |
| `/tools/mp3-to-html` | 工具页 | MP3 to HTML | P2 |
| `/tools/mp3-to-pdf` | 工具页 | MP3 to PDF | P2 |
| `/use-case/meeting-notes` | 解决方案页 | AI meeting notes, meeting transcription | P0 |
| `/use-case/consulting` | 解决方案页 | consulting transcription | P1 |
| `/use-case/customer-support` | 解决方案页 | customer support transcription | P1 |
| `/use-case/marketing` | 解决方案页 | marketing transcription | P1 |
| `/use-case/education` | 解决方案页 | education transcription, lecture notes | P1 |
| `/use-case/sales` | 解决方案页 | sales call transcription | P0 |
| `/use-case/podcast` | 解决方案页 | podcast transcription | P1 |
| `/use-case/media` | 解决方案页 | media transcription | P2 |
| `/use-case/legal` | 解决方案页 | legal transcription | P1 |
| `/use-case/healthcare` | 解决方案页 | healthcare transcription, medical notes | P1 |
| `/use-case/finance` | 解决方案页 | finance transcription | P2 |
| `/use-case/hr-recruitment` | 解决方案页 | HR recruitment transcription | P2 |
| `/login` | 登录页 | VOMO login | P2 |
| `/contact-us` | 联系页 | contact VOMO | P2 |
| `/privacy-policy` | 合规页 | VOMO privacy policy | P2 |
| `/cookie-notice` | 合规页 | VOMO cookie notice | P2 |
| `/tos` | 合规页 | VOMO terms of use | P2 |
| `/guide/category/ai-transcription` | 分类归档 | AI transcription blog | P2 |
| `/guide/category/ai-insights` | 分类归档 | AI insights blog | P2 |
| `/guide/category/use-cases` | 分类归档 | use cases blog | P2 |

### 1.1 SEO 工具页 URL 模式（导航外，sitemap 收录）

| 模式 | 量级（en sitemap） | 示例 | 说明 |
|------|-------------------|------|------|
| `/tools/{format}-to-{output}` | ~42（扩展格式，不含导航 19 项） | `/tools/mov-to-text`、`/tools/audio-to-docx` | AVI/FLV/MKV/MOV + docx/markdown 等 |
| `/tools/{场景/功能 slug}` | ~63 | `/tools/ai-meeting-summarizer`、`/tools/zoom-meeting-summarizer` | 会议/录音/平台/垂类着陆页 |
| `/tools/transcribe-{lang}-audio-to-text` | ~54 语种 | `/tools/transcribe-japanese-audio-to-text` | 语种 × 音频 |
| `/tools/transcribe-{lang}-video-to-text` | ~55 语种 | `/tools/transcribe-spanish-video-to-text` | 语种 × 视频 |
| 短路径语种页 | 少量 | `/tools/armenian-to-text`、`/tools/transcribe-zulu` | 与主模式并存 |

> 全量路径见 [vomo-others.md §1](./vomo-others.md#1-sitemap-明细英文)。Tools 合计（en sitemap）**240**；主导航仅展示约 **20** 项。

### 1.2 已上线博文（`/guide/{slug}`，38 篇）

| Slug | 类型（归纳） |
|------|-------------|
| `vomo-vs-otter-ai`、`vomo-vs-fireflies`、`proactor-ai-vs-chatgpt` | 竞品对比 |
| `granola-ai-alternatives`、`plaud-note-alternatives`、`fathom-ai-alternatives`、`proactor-ai-alternatives`、`elevenlabs-transcription-alternatives`、`savesubs-alternatives-in-2025-top-tools-for-downloading-and-using-video-subtitles` | Alternatives |
| `best-ai-meeting-note-taker-without-bot`、`best-bot-free-ai-meeting-notes-app`、`best-ai-recorder-app-for-meetings`、`best-ai-audio-note-takers`、`best-voice-recorder-with-transcription`、`best-audio-to-text-apps`、`best-audio-to-text-apps-for-iphone`、`best-audio-to-text-apps-for-android`、`best-focus-group-transcription-software`、`best-interview-evaluation-tools`、`3-best-online-tools-to-practice-transcription-ive-tested-2025` | Best-of 榜单 |
| `how-to-convert-audio-to-text`、`how-to-transcribe-a-video-on-iphone`、`how-to-copy-a-zoom-transcript`、`how-to-record-a-teams-meeting-if-youre-not-the-host`、`how-to-upload-video-to-chatgpt`、`how-to-download-videos-from-youtube`、`how-to-download-youtube-videos-on-iphone`、`how-to-download-youtube-videos-as-mp3-step-by-step-guide`、`how-to-extract-audio-from-a-youtube-video`、`top-tools-for-youtube-audio-download-quick-and-easy-solutions` | How-to / 教程 |
| `can-chatgpt-analyze-audio`、`can-chatgpt-analyze-videos`、`can-chatgpt-summarize-a-video`、`can-you-upload-audio-files-to-chatgpt`、`can-claude-ai-transcribe-audio`、`can-claude-analyze-video`、`automated-transcript-claude-ai-for-recording-simplify-your-workflows` | ChatGPT/Claude 相关 |
| `best-free-typing-jobs-from-home-where-to-apply` | 其他 |

---

## 2. URL 层级

```
/                              # 首页
├── /pricing                   # 定价
├── /about                     # 关于
├── /login                     # 登录（导航有；未进 en sitemap）
├── /contact-us                # 联系我们（页脚；未进 en sitemap）
├── /privacy-policy            # 隐私政策（页脚）
├── /cookie-notice             # Cookie 声明（页脚）
├── /tos                       # 服务条款（页脚）
├── /tools/                    # 工具集（无独立索引页；导航约 20 项 + sitemap ~220 SEO 页）
│   ├── [主导航] youtube-transcript, ai-voice-memos, ai-scribe, ai-dictation-tool, …
│   ├── [扩展格式] *-to-{text|pdf|html|docx|markdown|image}
│   ├── [场景 SEO] ai-*-summarizer, *-transcription, transcribe-zoom-*, …
│   └── [语种] transcribe-{lang}-{audio|video}-to-text
├── /use-case/                 # 解决方案（12，与导航一致）
│   ├── /meeting-notes
│   ├── /consulting
│   ├── /customer-support
│   ├── /marketing
│   ├── /education
│   ├── /sales
│   ├── /podcast
│   ├── /media
│   ├── /legal
│   ├── /healthcare
│   ├── /finance
│   └── /hr-recruitment
└── /guide/                    # 博客 / 指南
    ├── /category/
    │   ├── /ai-transcription
    │   ├── /ai-insights
    │   └── /use-cases
    └── /{slug}                # 单篇博文（38 篇，见 §1.2）
```

### 2.1 主导航与页脚（内链实测）

| 区域 | 链接目标 |
|------|---------|
| 顶栏 | Pricing → `/pricing`；Tools 下拉（约 20 工具）→ 各 `/tools/*`；Blog → `/guide` + 3 分类；Solution → 12 个 `/use-case/*`；Login → `/login` |
| Tools 下拉结构 | YouTube Transcript / AI Voice Memos / AI Scribe / AI Dictation Tool；Audio to Text 簇；Video to Text 簇；Video to PDF / Image / HTML；MP3 to HTML/PDF 等 |
| 页脚 Tools | 精简子集（YouTube / Audio-Video to Text / Speech / Voice Memos / Scribe / 若干转换） |
| 页脚 Solution | 与顶栏 12 个 use-case 一致 |
| 页脚 Company | Contact Us、Privacy Policy、Cookie Notice、Terms of Use |

---

## 3. 技术架构

| 维度 | 内容 | 识别方式 |
|------|------|---------|
| 前端框架 | 疑似 Next.js（基于路由结构和 `/notes` 路径特征） | 推测 |
| AI 模型 | GPT-4o（Ask AI）、OpenAI Whisper + Nova-2（ASR） | 官网声明 + 第三方评测 |
| 托管 | 未确认 | ⚠️ 待验证 |
| CMS | 无传统 CMS，疑似 SSG/MDX 博客 | 推测 |
| 移动端 | iOS App（App Store 4.4★） | App Store / 官网 CTA |
| 安卓 | ⚠️ 待验证 | App Store 未提安卓版本 |
| CDN | 未确认 | ⚠️ 待验证 |
| 应用区 | `/notes`（robots Disallow，登录后产品区） | robots.txt |

---

## 4. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 量级 | lastmod |
|------|----------|------|---------|
| Sitemap Index | `https://vomo.ai/sitemap.xml` | 16 个子 sitemap（按语言） | 2026-07-20 |
| 英文 | `sitemap/en/sitemap-0.xml` | **297** URL | 子项多为 2026-05 ~ 2026-07 |
| 其他语言各一份 | `sitemap/{locale}/sitemap-0.xml` | 各约 **278** URL | 2026-07-20 |
| 首页导航 Tools | `/tools/*`（导航可见） | ~20 | — |
| Sitemap Tools 合计 | `/tools/*` | **240** | — |
| Use-case | `/use-case/*` | **12** | — |
| Guide | `/guide` + 分类 + 博文 | **1 + 3 + 38** | — |
| 核心营销页（en sitemap） | `/`、`/pricing`、`/about` | 3 | — |

> 完整英文 URL 清单 → [vomo-others.md](./vomo-others.md)。  
> 核对日期：2026-07-21。此前文档称 sitemap 500；现已恢复可用。

### 4.1 覆盖缺口摘要（文档 vs 线上）

| 维度 | 说明 |
|------|------|
| 导航核心页 | 路径表已覆盖；与首页 withAllLinks 一致 |
| Sitemap SEO Tools | 约 221 条未进主导航，已用模式表 + others 明细归档 |
| 博文 | 由「~12」更正为 **38** 篇（§1.2） |
| 合规页 | 已补入路径表；`/privacy` 301 → `/privacy-policy` |
| 未进 en sitemap 但可访问 | `/login`、`/contact-us`、`/tools/ai-dictation-tool` 等，见 others §2 |

---

## 5. robots.txt 要点

抓取日期：2026-07-21（`https://vomo.ai/robots.txt`）

- **Allow**: `/`
- **Disallow**: `/notes`
- **Sitemap**: `https://vomo.ai/sitemap.xml`
- **AI Crawler 策略**：未特别声明（无 GPTBot/CCBot 等规则）

> 旧版文档中的查询参数 Disallow（`pid=`、`af_channel=` 等）当前 robots.txt **已不存在**。

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 | CTA、功能锚点、用户评价、FAQ；页脚 Tools/Solution/Company | 注册转化、功能认知 |
| 主导航 | Pricing / Tools / Blog / Solution / Login | 漏斗分流 |
| 页脚 | Tools 子集、Solution 全量、Company（Contact/Privacy/Cookie/Terms） | 次级导航、合规 |
| Pricing 页 | Free vs Pro 对比表、CTA | 付费转化 |
| Blog 首页 `/guide` | 分类 Tab（All / Use Cases / AI Transcription / AI Insights）+ 分页文章卡片 | 内容发现 |
| 工具页底部 | 「More AI Transcription Tools」相关工具互链 | SEO 内链扩散 |
| Use-case 页 | 与 Solution 导航互相强化 | 场景转化 |

---

## 7. 多语言

| 维度 | 内容 |
|------|------|
| 主语言 | 英语（默认根路径 `/`，无 `/en` 前缀） |
| 已上线语言（sitemap） | `en`, `ar`, `da`, `de`, `es`, `fi`, `fr`, `id`, `it`, `ja`, `ko`, `nl`, `pt`, `sv`, `zh`, `zh-tw`（共 **16**） |
| URL 结构 | 非默认语言为子目录前缀：`/{locale}/…`（如 `/ja/pricing`、`/zh/tos`） |
| 语言选择器 | 页脚可见（实测含 English 等） |
| 量级 | en ≈ 297 URL；其余语言各 ≈ 278 URL |
| hreflang | ⚠️ 待验证（HTML 头是否输出） |
| 本地化深度 | ⚠️ 待抽样验证（营销页 vs 工具页是否同等翻译） |

> 旧文档「仅 en-US / 无系统化多语言」已过时。

---

## 8. URL 分阶段规划

| 阶段 | 建议新增 / 优化 | 对标关键词优先级 |
|------|----------------|----------------|
| 短期 | 将 `/login`、`/contact-us`、合规页、关键 Tools 补入 sitemap（若希望被索引） | P1 |
| 短期 | 独立对比着陆页 `/compare/vomo-vs-otter` 等（现有博文 `/guide/vomo-vs-*`，缺独立对比 IA） | P0 |
| 短期 | Tools 聚合索引页（现状无 `/tools` 列表页，仅靠下拉 + SEO 散页） | P1 |
| 中期 | `/integrations` 集成页（若后续有集成） | P1 |
| 中期 | `/enterprise`、`/case-studies` | P1 |
| 长期 | 语种页与格式页的内链分层（避免 240 tools 扁平互指） | P2 |

---

*Last updated: 2026-07-21*
*来源：robots.txt、sitemap 索引与 en/各语言子 sitemap、首页 withAllLinks、/guide 聚合页、合规页核验*
