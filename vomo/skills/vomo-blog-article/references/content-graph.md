# VOMO Blog — Content Graph

> 加载时机：Phase 0（选题前检查冲突）· Phase 2（日期避让）· Phase 5（Cross-Article）
> 主文件：SKILL.md §4 指针

---

## 文件表

> 编号体系：**线上存量**（已发布在 vomo.ai `/guide/`）NN 为 `—`，不占本地序号；**本地新建稿**（skill 产出的 `vomo/blog/NN-{slug}.md`）从 **01** 开始独立递增。
> 线上存量来源：vomo-site-structure.md §1.2（2026-07-21 核对）。日期字段以线上 `/guide/{slug}` 为准，创作新文时避免与存量日期冲突（见「日期占用」说明）。

### 线上存量（38 篇，NN = —）

| NN | slug（部署路径 `/guide/{slug}`） | 类型（归纳） | 主关键词簇 |
|----|------|-------------|-----------|
| — | `vomo-vs-otter-ai` | Alternative | VOMO vs Otter |
| — | `vomo-vs-fireflies` | Alternative | VOMO vs Fireflies |
| — | `proactor-ai-vs-chatgpt` | Comparison | Proactor vs ChatGPT |
| — | `granola-ai-alternatives` | Alternative | Granola alternative |
| — | `plaud-note-alternatives` | Alternative | Plaud alternative |
| — | `fathom-ai-alternatives` | Alternative | Fathom alternative |
| — | `proactor-ai-alternatives` | Alternative | Proactor alternative |
| — | `elevenlabs-transcription-alternatives` | Alternative | ElevenLabs transcription alternative |
| — | `savesubs-alternatives-in-2025-top-tools-for-downloading-and-using-video-subtitles` | Alternative | Savesubs alternative |
| — | `best-ai-meeting-note-taker-without-bot` | Comparison | best AI meeting note taker |
| — | `best-bot-free-ai-meeting-notes-app` | Comparison | best bot-free meeting notes app |
| — | `best-ai-recorder-app-for-meetings` | Comparison | best AI recorder app |
| — | `best-ai-audio-note-takers` | Comparison | best AI audio note takers |
| — | `best-voice-recorder-with-transcription` | Comparison | best voice recorder with transcription |
| — | `best-audio-to-text-apps` | Comparison | best audio to text apps |
| — | `best-audio-to-text-apps-for-iphone` | Comparison | best audio to text apps iPhone |
| — | `best-audio-to-text-apps-for-android` | Comparison | best audio to text apps Android |
| — | `best-focus-group-transcription-software` | Comparison | best focus group transcription |
| — | `best-interview-evaluation-tools` | Comparison | best interview evaluation tools |
| — | `3-best-online-tools-to-practice-transcription-ive-tested-2025` | Comparison | transcription practice tools |
| — | `how-to-convert-audio-to-text` | HowTo | how to convert audio to text |
| — | `how-to-transcribe-a-video-on-iphone` | HowTo | transcribe video on iPhone |
| — | `how-to-copy-a-zoom-transcript` | HowTo | copy Zoom transcript |
| — | `how-to-record-a-teams-meeting-if-youre-not-the-host` | HowTo | record Teams meeting |
| — | `how-to-upload-video-to-chatgpt` | HowTo | upload video to ChatGPT |
| — | `how-to-download-videos-from-youtube` | HowTo | download YouTube videos |
| — | `how-to-download-youtube-videos-on-iphone` | HowTo | download YouTube videos iPhone |
| — | `how-to-download-youtube-videos-as-mp3-step-by-step-guide` | HowTo | YouTube to MP3 |
| — | `how-to-extract-audio-from-a-youtube-video` | HowTo | extract audio from YouTube |
| — | `top-tools-for-youtube-audio-download-quick-and-easy-solutions` | Comparison | YouTube audio download tools |
| — | `can-chatgpt-analyze-audio` | HowTo | ChatGPT audio analysis |
| — | `can-chatgpt-analyze-videos` | HowTo | ChatGPT video analysis |
| — | `can-chatgpt-summarize-a-video` | HowTo | ChatGPT video summarize |
| — | `can-you-upload-audio-files-to-chatgpt` | HowTo | upload audio to ChatGPT |
| — | `can-claude-ai-transcribe-audio` | HowTo | Claude transcribe audio |
| — | `can-claude-analyze-video` | HowTo | Claude analyze video |
| — | `automated-transcript-claude-ai-for-recording-simplify-your-workflows` | WorkflowUseCase | Claude transcript workflow |
| — | `best-free-typing-jobs-from-home-where-to-apply` | HowTo | typing jobs from home |

### 本地新建稿（NN 从 01 起）

| NN | 本地文件 `vomo/blog/NN-{slug}.md` | 类型 | 主关键词 |
|----|-----------------------------------|------|---------|
| 01 | `01-how-to-convert-podcast-to-blog-post.md` | HowTo / WorkflowUseCase | how to convert podcast to blog post |

**下一本地序号：02**（新文件名 `02-{slug}.md`）

---

## 日期占用说明

线上存量 38 篇具体发布日以线上 `/guide/{slug}` 为准（skill 不复制，避免过期）。本地新建稿（01 起）Phase 2 排期时：
1. 从**目标上线日**为锚点日，**往前**逐日分配
2. 每自然日 ≤1 篇（§1 日期策略）
3. 存量文章已有日期若已知（如 2025 系列），避让不重复

---

## 主题簇结构

```
Alternatives / 竞品截流（占博客 80%+，核心栏目）
    ├── vomo-vs-otter-ai ←→ vomo-vs-fireflies
    ├── granola-ai-alternatives / fathom-ai-alternatives / proactor-ai-alternatives
    ├── elevenlabs-transcription-alternatives / plaud-note-alternatives / savesubs-…
    └── 内容缺口：vomo-vs-descript（P1）、best-transcription-software（P0）

Best-of 榜单（Comparison）
    ├── meeting: best-bot-free-ai-meeting-notes-app / best-ai-meeting-note-taker-without-bot
    ├── audio: best-audio-to-text-apps（+iPhone/Android）
    ├── recorder: best-ai-recorder-app-for-meetings / best-voice-recorder-with-transcription
    └── vertical: best-focus-group-transcription-software / best-interview-evaluation-tools

How-to / 教程
    ├── audio: how-to-convert-audio-to-text
    ├── iPhone: how-to-transcribe-a-video-on-iphone
    ├── meeting: how-to-copy-a-zoom-transcript / how-to-record-a-teams-meeting-…
    └── YouTube: how-to-download-* / how-to-extract-audio-*（4 篇）

AI 平台能力问答（ChatGPT/Claude）
    ├── can-chatgpt-*（4 篇）/ can-you-upload-audio-files-to-chatgpt
    ├── can-claude-*（2 篇）/ automated-transcript-claude-ai-…
    └── 引流词：user 搜"ChatGPT 能否分析音频" → 导向 VOMO 转录

Podcast 楔子（growth-strategy §3）
    ├── podcast-transcription（枢纽，待建）
    ├── spotify-podcast-transcription / apple-podcast-transcription（L3，待建）
    └── how-to-convert-podcast-to-blog-post（本地 #01，HowTo · category use-cases）
```

---

## Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| Bot-free 会议笔记 | best-bot-free-ai-meeting-notes-app | 完整定义在此；他文 1–2 句 + link |
| VOMO vs Otter | vomo-vs-otter-ai | Otter 对比 canonical；他文引用不重复 |
| 如何转换音频为文字 | how-to-convert-audio-to-text | HowTo canonical；他文引用 |
| YouTube 下载/提取 | how-to-download-videos-from-youtube | YouTube 操作 canonical |

**规则**：每个核心概念只在一篇文章中完整定义（canonical），其他文章引用 1–2 句 + internal link。Hub 文章承载品类定义；Spoke 引用 canonical 定义，不重新展开。

---

## 关键词冲突快查

| slug | 主关键词 | 边界 |
|------|---------|------|
| vomo-vs-otter-ai | VOMO vs Otter, Otter alternative | 横向对比；Otter 功能不全面展开 |
| best-audio-to-text-apps | best audio to text apps | 榜单评测；每工具 ≥1 优势 |
| how-to-convert-audio-to-text | how to convert audio to text | 教程实操；不覆盖竞品选型 |
| how-to-convert-podcast-to-blog-post（本地 #01） | how to convert podcast to blog post | 场景工作流；关键词完整前缀（HowTo）；不覆盖竞品选型 |

---

## 集群 → 分类映射

| 集群 | 默认 category | 说明 |
|------|:---:|------|
| Alternatives / 竞品对比 | ai-insights | 横向对比与选型 |
| Best-of 榜单 | ai-transcription | 工具评测与榜单 |
| How-to 教程 | ai-transcription | 实操指南与工作流 |
| AI 平台能力问答 | ai-transcription | ChatGPT/Claude 分析能力 |
| 场景工作流 | use-cases | 行业场景与 workflow |
| 产品发布 | ai-insights | 产品更新与功能介绍 |

---

## 维护规则

每发布一篇本地新建稿后，人类应：
1. bump 本文件 §1「本地新建稿」表的「下一本地序号」
2. 更新本文件「本地新建稿」登记表（新增行）
3. 更新日期占用说明
4. 更新 Canonical Concept Registry（如有新的 canonical 概念）
5. bump `SKILL.md` frontmatter `version` patch
6. 更新 `vomo/blog/README.md` 文章表

---

*content-graph · v1.0.0 · 2026-08-03*
