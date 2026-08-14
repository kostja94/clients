# VOMO — Slug Design Gate B

> 加载时机：Phase 2
> 主文件：SKILL.md §3 Phase 2 指针

---

## 6 问检查

| # | 检查项 | 标准 | Fail 动作 |
|---|--------|------|----------|
| 1 | **含 primary keyword？** | slug 核心词与 target keyword 一致 | 改 slug 让关键词居前 |
| 2 | **通过"大声读"测试？** | 去掉连字符大声读 → 通顺 → Pass | 不通顺或含重复词 → 重选 |
| 3 | **不含禁词？** | framework / strategy / guide / diagnosis / complete / ultimate | 移除禁词 |
| 4 | **≤60 字符？** | 计数不含 `/guide/` | 缩短 |
| 5 | **常青无年份？** | 不含 2026 等年份数字 | 去年份 |
| 6 | **语义余量？** | 30% 内容变化后 slug 仍合适 | 改得更通用 |

---

## 12 反模式（创作阶段必检）

| # | 反模式 | 错误示例 | 正确示例 |
|---|--------|---------|---------|
| 1 | 含年份 | `best-transcription-software-2026` | `best-transcription-software` |
| 2 | 含数量 | `top-5-podcast-tools` | `best-podcast-transcription-tools` |
| 3 | 连续重复词 | `transcription-transcription-tools` | `best-transcription-tools` |
| 4 | 内部架构词泄漏 | `podcast-transcription-framework` | `how-to-transcribe-a-podcast` |
| 5 | 分类前缀沉积 | `vomo-podcast-transcription` | `podcast-transcription` |
| 6 | 过多词 | `how-to-transcribe-a-podcast-to-show-notes-and-newsletter`（>8 词 / >60 字符） | `how-to-transcribe-a-podcast-to-show-notes`（≤8 词） |
| 7 | 空洞词 | `complete-guide` / `ultimate` | 用描述性词替代 |
| 8 | 品牌名前置 | `vomo-vs-otter-ai`（例外：Alternatives 可用 vs-X 格式） | `otter-ai-alternatives`（对比文例外） |
| 9 | 含特殊字符 | `call_transcription` / `CallTranscription` | `call-transcription` |
| 10 | 过于具体 | `transcribe-youtube-video-on-iphone-2026` | `transcribe-video-on-iphone` |
| 11 | misleading | `free-ai-transcription-tool` | `ai-transcription-tool`（若非所有计划免费） |
| 12 | 与已有 slug 混淆 | 太接近已有 slug（如重复 `how-to-convert-audio-to-text`） | 用更区分的关键词 |

---

## Slug 命名规范

| 规则 | 说明 |
|------|------|
| 格式 | kebab-case；全小写 + 连字符 |
| 长度 | 5–8 词；≤60 字符（HowTo 类可到 7–8 词，保留完整关键词） |
| 关键词 | **含 primary keyword 完整核心词**（HowTo 类用 `how-to-{action}` 前缀，如 `how-to-convert-podcast-to-blog-post`） |
| 可读 | 大声读通顺；避免过度缩写或丢关键词 |
| 常青 | 不含年份、版本号 |
| 品牌名 | 不前置（除非 Alternative 类 vs-X / X-alternative 格式） |

**HowTo / PlatformFeature / WorkflowUseCase 类 slug 公式**：
- HowTo：`how-to-{action}-{object}`（如 `how-to-convert-audio-to-text`、`how-to-convert-podcast-to-blog-post`）
- PlatformFeature：`{platform}-podcast-transcript` / `how-to-{transcribe}-{platform}-content`
- WorkflowUseCase：`{source}-to-{output}-workflow`（或 HowTo 前缀 `how-to-convert-{source}-to-{output}`，关键词完整优先）

> 权衡原则：**关键词完整优先，可读性其次**。宁可 slug 到 7–8 词，也不为缩短而丢掉用户实际搜索的词（如把 `how-to-convert-podcast-to-blog-post` 缩成 `podcast-to-blog`）。

---

## Title 公式

- ResearchGlossary：`What Is {Term}? — {Why It Matters for X}`
- HowTo：`How to {Action} — {Benefit / Workflow}`
- Comparison：`Best {Category} — {Differentiator Frame}`
- Alternative：`{Competitor} Alternative — {Why Teams Switch}`
- PlatformFeature：`How to {Transcribe} {Platform} Content — {Benefit}`
- WorkflowUseCase：`{Scenario} Workflow — {Benefit}`
- Diagnosis：`{Problem}? Here's Why and How to Fix It`
- Announcement：`Introducing {Feature} — {Value Proposition}`

Meta description：120–160 chars · benefit + main intent keyword + 差异化一句。

---

*slug-gate · v1.0.0 · 2026-08-03*
