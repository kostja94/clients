# VOMO — Project Configuration

> 加载时机：Phase 0R（R1）· Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §1 速查指针

---

## 1. 品牌与产品

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | VOMO（VOMO AI） |
| **主域名** | vomo.ai |
| **博客路径前缀** | `/guide/`（非 `/blog/`） |
| **产品定位** | AI 会议笔记与音频转录 — Bot-free（不加入会议） |
| **品类 one-liner** | Record → Transcribe → Smart Notes → Ask AI；Bot-free 录音、双引擎 ASR |
| **核心能力** | AI 转录（Whisper+Nova-2 双引擎）、Smart Notes、Ask AI（GPT-4o）、说话人识别、多格式导出、VOMO CLI |
| **输入方式** | 实时录音、文件上传（MP3/WAV/M4A/MP4 等，最多 10 个）、粘贴 YouTube 链接 |
| **三步工作流** | Record → Transcribe → Extract（Ask AI / Smart Notes） |
| **目标用户** | 知识工作者、远程团队、销售/客户成功、内容创作者、学生/研究者、专业服务人士 |
| **关键指标** | 400K+ 用户、转录 1,000,000+ 小时、95–99% 准确率、90+ 语言、App Store 4.4★（347 评分）、Product Hunt #2 Product of the Day |
| **定价** | Free 30 分钟/周；Pro $1.92/周（≈$8.32/月，年付省 75%） |
| **Hero 叙事** | "No credit card required · Free daily credits" |
| **CTA 主链** | https://vomo.ai/ |
| **署名** | `VOMO Team` |
| **语言** | 英文正文；中文仅用于沟通 |
| **禁止内链** | 未上线产品页、`/notes`（产品区，robots Disallow） |

---

## 2. 可链接 URL 白名单（内链优先）

| 类型 | 路径 |
|------|------|
| 首页 | `/` |
| 定价 | `/pricing` |
| 博客 | `/guide`、`/guide/{slug}`、`/guide/category/{ai-transcription\|ai-insights\|use-cases}` |
| 工具页（主导航 P0） | `/tools/youtube-transcript`、`/tools/audio-to-text`、`/tools/speech-to-text`、`/tools/video-to-text`、`/tools/mp3-to-text`、`/tools/mp4-to-text`、`/tools/ai-voice-memos` |
| 工具页（扩展，白名单按需扩展） | `/tools/{format}-to-{text\|pdf\|html}`、`/tools/transcribe-{lang}-audio-to-text` |
| 解决方案页 | `/use-case/{meeting-notes\|consulting\|customer-support\|marketing\|education\|sales\|podcast\|media\|legal\|healthcare\|finance\|hr-recruitment}` |

**G6 规则**：只链白名单内路径；forthcoming ≤1 且仅正文脚注。**每篇必须链 ≥1 个主 Tools/楔子页**（growth-strategy §5.5）。

---

## 3. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、数据（400K+/1M+ hours/95–99%）与官网矛盾 | 逐 claim 对照 §1 产品事实 |
| **G2** | 死链 | 站内或站外链接 404 | 逐个检查内链可达性；外链可有 1–2 失效但非全挂 |
| **G3** | 无来源数字 | 量化 claim 无 attribution | P0 级数字须 `[Source: URL]`；内部数据须标注 "internal observation, n=X" |
| **G4** | 竞品状态错误 | 竞品状态与官网矛盾 | 打开竞品官网/docs 验证 |
| **G5** | 产品能力夸大 | 定位语言 ≠ 已实现功能（如"编辑音视频"非 VOMO 能力） | 不超出 GA 版本；定位语言与功能描述区分 |
| **G6** | 内链指向未上线页面 | 只链白名单内路径 | 对照 §2 白名单；`/notes` 禁用 |
| **G7** | 品牌风险 | 贬低性措辞（"just a bot"、"merely"） | 竞品描述必须公平；每竞品 ≥1 优势 |

---

## 4. 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **节奏** | 博客目标约 10 篇/周（growth-strategy §5） |
| **publishDate 创建后慎重更改** | 首次发布日设定后尽量不改；仅在未上线阶段可调整 |
| **错开方向** | 从锚点日（通常为目标上线日）**往前**排，越重要的文章排越近 |
| **避让已占用日** | 已有文章的日期不重复使用 |

Agent 在 Phase 2 应读取 `references/content-graph.md` 中已发布文章的日期，避免冲突。

---

## 5. 品牌 Voice 速查

| 维度 | 要求 |
|------|------|
| Clear | 知识工作者能复述核心观点 |
| Creator/practitioner friendly | 像同行交流，非企业采购文 |
| Evidence-led | 量化数字有来源；框架有观察基础 |
| Category-building | 产品首次出现前已提供独立价值 |
| Fair comparison | 每竞品 ≥1 优势 |

### 禁止

- revolutionary · game-changing · unlock · seamless · magic
- 虚构场景开头（"Imagine you're a product manager…"）
- 空泛句：In today's world · Let's dive in · Without further ado
- 声称 VOMO 可编辑音视频（Descript 的领域，G5）

---

*project-config · v1.0.0 · 2026-08-03*
