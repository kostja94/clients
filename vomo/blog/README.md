# VOMO Blog — 文章表

> 本目录存放 vomo.ai `/guide/` 博客的本地稿件（`NN-{slug}.md`）。由 `vomo-blog-article` skill 产出。
> 发布路径：`https://vomo.ai/guide/{slug}`

## 发布规则

| 规则 | 说明 |
|------|------|
| 文件命名 | `NN-{slug}.md`，NN 为**本地新建稿序号**（从 01 起，两位递增） |
| 下一篇序号 | **02** |
| 一天一篇 | 每自然日 ≤1 篇 |
| 节奏 | 约 10 篇/周（growth-strategy §5） |
| 分类 | `ai-transcription` / `ai-insights` / `use-cases` |

---

## 存量已发布文章（38 篇，`/guide/{slug}`）

| Slug | 类型 | 分类 |
|------|------|------|
| `vomo-vs-otter-ai` | Alternative | ai-insights |
| `vomo-vs-fireflies` | Alternative | ai-insights |
| `proactor-ai-vs-chatgpt` | Comparison | ai-insights |
| `granola-ai-alternatives` | Alternative | ai-insights |
| `plaud-note-alternatives` | Alternative | ai-insights |
| `fathom-ai-alternatives` | Alternative | ai-insights |
| `proactor-ai-alternatives` | Alternative | ai-insights |
| `elevenlabs-transcription-alternatives` | Alternative | ai-insights |
| `savesubs-alternatives-in-2025-top-tools-for-downloading-and-using-video-subtitles` | Alternative | ai-insights |
| `best-ai-meeting-note-taker-without-bot` | Comparison | ai-transcription |
| `best-bot-free-ai-meeting-notes-app` | Comparison | ai-transcription |
| `best-ai-recorder-app-for-meetings` | Comparison | ai-transcription |
| `best-ai-audio-note-takers` | Comparison | ai-transcription |
| `best-voice-recorder-with-transcription` | Comparison | ai-transcription |
| `best-audio-to-text-apps` | Comparison | ai-transcription |
| `best-audio-to-text-apps-for-iphone` | Comparison | ai-transcription |
| `best-audio-to-text-apps-for-android` | Comparison | ai-transcription |
| `best-focus-group-transcription-software` | Comparison | ai-transcription |
| `best-interview-evaluation-tools` | Comparison | ai-transcription |
| `3-best-online-tools-to-practice-transcription-ive-tested-2025` | Comparison | ai-transcription |
| `how-to-convert-audio-to-text` | HowTo | ai-transcription |
| `how-to-transcribe-a-video-on-iphone` | HowTo | ai-transcription |
| `how-to-copy-a-zoom-transcript` | HowTo | ai-transcription |
| `how-to-record-a-teams-meeting-if-youre-not-the-host` | HowTo | ai-transcription |
| `how-to-upload-video-to-chatgpt` | HowTo | ai-transcription |
| `how-to-download-videos-from-youtube` | HowTo | ai-transcription |
| `how-to-download-youtube-videos-on-iphone` | HowTo | ai-transcription |
| `how-to-download-youtube-videos-as-mp3-step-by-step-guide` | HowTo | ai-transcription |
| `how-to-extract-audio-from-a-youtube-video` | HowTo | ai-transcription |
| `top-tools-for-youtube-audio-download-quick-and-easy-solutions` | Comparison | ai-transcription |
| `can-chatgpt-analyze-audio` | HowTo | ai-transcription |
| `can-chatgpt-analyze-videos` | HowTo | ai-transcription |
| `can-chatgpt-summarize-a-video` | HowTo | ai-transcription |
| `can-you-upload-audio-files-to-chatgpt` | HowTo | ai-transcription |
| `can-claude-ai-transcribe-audio` | HowTo | ai-transcription |
| `can-claude-analyze-video` | HowTo | ai-transcription |
| `automated-transcript-claude-ai-for-recording-simplify-your-workflows` | WorkflowUseCase | use-cases |
| `best-free-typing-jobs-from-home-where-to-apply` | HowTo | ai-insights |

---

## 本地新建稿（skill 产出，NN 从 01 起）

| NN | 本地文件 | 类型 | 分类 |
|----|---------|------|------|
| 01 | `01-how-to-convert-podcast-to-blog-post.md` | HowTo | use-cases |

---

## 排障记录

- [发布排障记录 — Preview API 创建草稿失败](./PUBLISH-TROUBLESHOOTING.md)（2026-08-07）
- [发布流程 Runbook — 完整命令与格式规范](./PUBLISH-RUNBOOK.md)（2026-08-11）

---

## 新稿登记模板

发布新稿后，将行复制到「本地新建稿」表格并填入 slug，同时更新：

1. 本文件「本地新建稿」表格（新增行）
2. `../skills/vomo-blog-article/references/content-graph.md`（本地序号 + 登记表 + 日期）
3. `../skills/vomo-blog-article/SKILL.md` frontmatter `version` patch

```markdown
| {NN} | `{NN}-{slug}.md` | {Type} | {category} |
```

---

*关联：[SKILL.md](../skills/vomo-blog-article/SKILL.md) · [content-graph](../skills/vomo-blog-article/references/content-graph.md)*
*Last updated: 2026-08-03*
