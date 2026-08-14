# VOMO — Internal Links Rules

> 加载时机：Phase 3（Outline 内链规划）· Phase 4（Draft 内链执行）· Phase 5（SelfCheck 内链复核）
> 主文件：SKILL.md §3 各 Phase 指针

---

## R1 — 内链数量

| 规则 | 标准 |
|------|------|
| **blog 互链** | ≥2（全文上下文分布） |
| **Tools / 楔子主链** | **≥1**（每篇必须有明确主承接 URL，growth-strategy §5.5） |
| **product page** | 1–2（自然嵌入正文，非每段推） |
| **外链** | 2–6（**只链权威来源**：研究机构/官方统计/权威媒体；竞品与工具**纯文本提及不链接**） |

---

## R2 — 锚文本标准

| 规则 | 标准 |
|------|------|
| 描述性 | "our guide to converting audio to text"、"how to download videos from YouTube" |
| 禁止 | "click here"、"learn more"、"read more" |
| 竞品 | **纯文本提及，不链接**（产品官网/评测站不作外链） |
| 权威外链 | Markdown `[描述性锚文本](https://authoritative-source)` |
| 内链 | Markdown `[描述性锚文本](/guide/{slug})` |

---

## R3 — Canonical Concept 引用

每个核心概念只在一篇文章中完整定义（canonical），其他文章引用 1–2 句 + link：

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| Bot-free 会议笔记 | best-bot-free-ai-meeting-notes-app | 1–2 句 + link；canonical 完整定义 |
| VOMO vs Otter | vomo-vs-otter-ai | 1–2 句 + link；他文引用 |
| 如何转换音频为文字 | how-to-convert-audio-to-text | 1–2 句 + link；他文引用 |

---

## R4 — Hub-Spoke 双向互链

- **Hub** → 链接所有 spoke（或主要 spoke）
- **Spoke** → 必须回链 hub
- **Spoke ↔ Spoke**：语义相关时互链

---

## R5 — 禁止链接

- 未上线产品页（G6）
- `/notes`（产品区，robots Disallow）
- Forthcoming 页面（正文核心流程 ≥0；脚注 ≤1）
- **竞品/工具官网与评测站**（不链接，纯文本提及）
- **非权威第三方**（内容农场、SEO 博客）
- 首页 `/` 作为唯一主链（每篇必须有 Tools/楔子主链）

---

## Tools 主链候选（按主题）

| 文章主题 | 建议主 Tools/楔子页 |
|---------|-------------------|
| 音频转文字 | `/tools/audio-to-text` |
| 语音转文字 | `/tools/speech-to-text` |
| YouTube 转录 | `/tools/youtube-transcript` |
| 视频转文字 | `/tools/video-to-text` |
| MP3 转文字 | `/tools/mp3-to-text` |
| MP4 转文字 | `/tools/mp4-to-text` |
| 会议笔记 | `/use-case/meeting-notes` |
| 播客转录 | `/use-case/podcast`（或规划中的 `/tools/podcast-transcription`） |
| 销售通话 | `/use-case/sales` |
| 讲座/教育 | `/use-case/education` |
| 语音备忘录 | `/tools/ai-voice-memos` |

---

## 内链验证清单（Phase 5 对照）

- [ ] ≥2 blog 互链（全文上下文分布，非集中末尾）
- [ ] ≥1 Tools/楔子主链（G6 白名单内）
- [ ] Spoke 回链 hub（如适用）
- [ ] 锚文本描述性（无 "click here"）
- [ ] 竞品/工具纯文本提及，无官网链接；外链只链权威来源
- [ ] 无未上线页面链接、无 `/notes`
- [ ] Forthcoming ≤1（仅脚注）
- [ ] Canonical 概念 1–2 句 + link（非重定义）

---

*internal-links · v1.0.0 · 2026-08-03*
