
# VOMO — 功能分析

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./vomo.md) | [site-structure](./vomo-site-structure.md) | [keywords](./vomo-keywords.md) | [competitors](./vomo-competitors.md) | [use-cases](./vomo-use-cases.md) | [growth-strategy](./vomo-growth-strategy.md)

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **AI 转录** | 95%+ 准确率，90+ 语言，自动标注说话人和时间戳，支持混合语言会议 | ★ | `/`, `/tools/speech-to-text`, `/tools/audio-to-text` | AI transcription, speech to text, audio to text |
| **Multi-model ASR** | 同时使用 OpenAI Whisper + Nova-2 双引擎，嘈杂环境下保持高准确率 | ★ | `/` | AI speech recognition, ASR engine |
| **Smart Notes** | 自动生成结构化会议笔记：摘要、关键要点、行动项、章节、决策，忠实于对话内容，不编造细节 | ★ | `/` | AI meeting notes, meeting summary AI |
| **Ask AI** | 基于 GPT-4o 的对话式问答，针对转录内容提问（"行动项是什么？""谁提到了预算？"），无限使用 | ★ | `/` | AI chat transcript, ask transcript questions |
| **多输入方式** | 实时录音、上传音频/视频文件（最多 10 个同时）、粘贴 YouTube 链接 | — | `/`, `/tools/youtube-transcript` | youtube transcript, upload audio transcribe |
| **说话人识别** | 自动区分不同说话人，在转录和笔记中标注 | ★ | `/` | speaker diarization, speaker labels |
| **多格式导出** | TXT, DOCX, PDF, SRT, HTML，支持复制某一段落或全文 | — | `/` | export transcript PDF, transcript to text |
| **公开分享链接** | 生成公开链接，团队成员无需注册即可查看、搜索转录和笔记 | — | `/` | share meeting notes, share transcript link |
| **会议模板** | 内置模板：团队会议、站立会、销售电话、面试评估、播客，支持自定义模板，Markdown 友好 | ★ | `/` | meeting notes template, AI note template |
| **VOMO CLI** | 命令行工具，将转录和 Smart Notes 拉取到 Claude Code、Codex、OpenCode 等 Agent 工作流 | ★★ | `/`（底部 Agent Workflows 区域） | VOMO CLI, AI agent transcription |
| **YouTube 转录** | 粘贴链接即可获取带字幕的 YouTube 视频转录 + AI 摘要，无需注册 | — | `/tools/youtube-transcript` | YouTube transcript generator, YouTube to text |
| **工具转换集** | MP3/WAV/M4A/FLAC/MP4→文字、视频→PDF/图片/HTML 等多格式转换 | — | `/tools/*` | MP3 to text, MP4 to text, video to PDF |
| **笔记编辑** | 转录后支持手动编辑摘要、修正文字、调整结构，不锁定输出 | ★ | `/` | edit transcript, edit meeting notes |
| **文件组织** | 按项目/客户文件夹管理录音，云同步 | — | `/` | organize recordings, meeting library |

---

## 2. 用户流程

### 核心操作路径

```
① 输入 → ② 转录 → ③ AI 处理 → ④ 交互 → ⑤ 分享/导出

① 输入（三选一）
   ├─ 实时录音（App / Web）
   ├─ 上传文件（MP3, WAV, M4A, MP4 等，最多 10 个同时）
   └─ 粘贴 YouTube 链接

② 智能转录
   └─ Whisper + Nova-2 双引擎 → 说话人标注 → 时间戳 → 段落格式化
   └─ 处理速度：1 小时录音 ≈ 15 分钟

③ AI 生成 Smart Note
   └─ 摘要 + 关键要点 + 行动项（含负责人）+ 章节 + 决策

④ 交互与编辑
   ├─ Ask AI：对话式查询转录内容
   ├─ 手动编辑：修正摘要/文字
   └─ 保存 AI 回答到笔记

⑤ 分享与导出
   ├─ 生成公开链接
   ├─ 导出 TXT/DOCX/PDF/SRT/HTML
   └─ 导出原始音频
```

### Free vs Pro 限制路径

- **Free**：30 分钟/周 → 达到上限后无法继续转录 → 引导升级 Pro
- **Pro**：$1.92/周 → 无限制转录 → 3 小时/文件上限 → 批量导入

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 转录准确率 | 95–99%（清晰音频）/ 混合语言支持 | 官网 + 第三方评测 |
| 支持语言数 | 90+ | 官网 |
| ASR 引擎 | OpenAI Whisper + Nova-2（Deepgram） | 第三方技术评测 |
| AI 问答模型 | GPT-4o | 官网声明 |
| 处理速度 | ~15 分钟处理 1 小时音频 | 用户评测 |
| 最长录音 | 3+ 小时（连续录制） | 官网 |
| Free 额度 | 30 分钟/周 | 定价页 |
| Pro 单价 | $1.92/周（≈$8.32/月） | 定价页 |
| App Store 评分 | 4.4★ / 347 评分 | App Store (2026-07) |
| 用户量 | 400,000+ | PR Newswire (2026-07) |
| 转录总时长 | 1,000,000+ 小时 | 官网 |
| Product Hunt | #2 Product of the Day | 官网 |

---

## 4. 定价

| 维度 | Free | Pro |
|------|------|-----|
| 价格 | $0 | $1.92/周（年付省 75%） |
| 转录额度 | 30 分钟/周 | 无限制 |
| 文件上传限制 | 30 分钟/文件 | 3 小时/文件 |
| 准确率 | 99% + 说话人识别 | 同 Free |
| Smart Notes | ✓ | ✓ |
| Ask AI (GPT-4o) | ✓ | ✓ |
| 自定义模板 | — | ✓ |
| 批量导入 | — | ✓ |
| YouTube 转录 | ✓ | ✓ |
| 多语言混合会议 | ✓ | ✓ |
| Web Beta | ✓ | ✓ |

> Pro 定价策略独特：按周计费（$1.92/周），实际月费约 $8.32，远低于 Otter.ai Pro ($16.99/月) 和 Fireflies ($10/月起)。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| AI 转录 + Smart Notes | 会议记录、客户通话 | 远程团队成员、销售、管理者 |
| Ask AI | 会后复盘、快速查找信息 | 所有 Persona |
| YouTube 转录 | 内容创作、学习研究 | 内容创作者、学生/研究者 |
| 会议模板 | 不同会议类型的结构化输出 | 项目经理、招聘官、销售 |
| 工具转换集 | 媒体文件格式转换 | 内容创作者、媒体从业者 |
| VOMO CLI | Agent 工作流集成 | 开发者、技术团队 |
| 公开分享 | 团队协作、信息同步 | 远程团队、管理者 |

> 完整 Persona 定义见 [use-cases](./vomo-use-cases.md)

---

*Last updated: 2026-07-16*
*来源：官网内容分析、定价页、App Store、第三方评测*
