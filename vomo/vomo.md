# VOMO

## 文档导航

| 文档 | 职责 | 引用 |
|------|------|------|
| [主文档](./vomo.md)（本页） | 概览、ICP、文档索引 | — |
| [vomo-keywords.md](./vomo-keywords.md) | 关键词映射、目标页 | [features](./vomo-features.md) |
| [vomo-features.md](./vomo-features.md) | 功能页：能力、URL | [use-cases](./vomo-use-cases.md) |
| [vomo-competitors.md](./vomo-competitors.md) | 竞品分析、差异化 | [features](./vomo-features.md) |
| [vomo-site-structure.md](./vomo-site-structure.md) | URL 层级、IA、技术栈 | 主文档 |
| [vomo-others.md](./vomo-others.md) | Sitemap 全量明细 | [site-structure](./vomo-site-structure.md) |
| [vomo-use-cases.md](./vomo-use-cases.md) | 场景、Persona | [features](./vomo-features.md) |
| [vomo-growth-strategy.md](./vomo-growth-strategy.md) | 增长渠道、内容计划 | [keywords](./vomo-keywords.md) |
| [podcast transcription/](./podcast%20transcription/podcast-platforms.md) | 播客平台全景、转录楔子（枢纽+8 平台页） | [use-cases](./vomo-use-cases.md) · [page-playbook](./podcast%20transcription/page-playbook.md) |
| [youtube transcription/](./youtube%20transcription/youtube-categories.md) | YouTube 分类全景、子页生产 | [growth-strategy](./vomo-growth-strategy.md) |


---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C/B2B SaaS — AI 会议笔记与音频转录 |
| 网站 | https://vomo.ai/ |
| 当前阶段 | 增长期（400K+ 用户，2023 年成立） |
| 核心产品 | AI 驱动的会议笔记与音频转录工具：录音 → 转录 → AI摘要 → 行动项 |
| 产品形态 | Web + iOS（无安卓，⚠️ 待验证） |
| 关键差异化 | Bot-free 录音（不加入会议）、多模型 ASR（Whisper+Nova-2）、Ask AI（GPT-4o对话式查询）、CLI 对接 Agent 工作流 |
| 目标用户 | 需要将会议/访谈/语音备忘录转化为结构化笔记的知识工作者、远程团队、创作者、学生 |
| 目标市场 | 全球（主英语市场），包括美国、印度等 |
| 更新日期 | 2026-07-21 |

---

## 1. 产品定位

| 维度 | 内容 |
|------|------|
| 品类 | AI 会议笔记与音频转录工具——属于 AI 生产力工具细分赛道 |
| 价值主张 | 让用户专注于对话本身，而非记笔记——AI 自动完成转录、摘要、行动项提取（用户评价："saves me hours of post-meeting documentation"） |
| 竞争替代 | 用户从手动记笔记、传统录音笔、或以 Otter.ai/Fireflies.ai 为代表的 Bot 加入型会议工具转向 VOMO——核心理由是 **Bot-free（不加入会议）、更灵活的输入方式（不限会议平台）、更便宜的定价** |
| 差异化锚点 | ① Bot-free 录音（不加入会议，隐私优先）→ 与 Otter/Fireflies 的 Bot 策略差异；② 双引擎 ASR 实现 99% 准确率；③ Ask AI 对话式查询转录内容；④ VOMO CLI 对接 AI Agent 工作流 |
| 市场位置 | 性价比领先者——Pro $1.92/周（≈$8.32/月），远低于 Otter Pro ($16.99/月) 和 Fireflies ($10/月起），但集成生态薄弱，定位为「轻量级个人转录工具」而非「企业会议智能平台」 |

### 1.1 定位简述

VOMO 占据 AI 转录工具市场中「轻量、灵活、个人友好」的位置。与 Otter.ai（强在实时字幕和会议平台集成）和 Fireflies.ai（强在 CRM 集成和销售分析）不同，VOMO 以 Bot-free 方式切入——用户只需录制设备音频，无需让 AI 机器人加入 Zoom/Teams 会议。这一设计契合了隐私敏感场景（客户会议、医疗、法律）和个人效率场景（语音备忘录、访谈、播客）。

核心用户是**需要快速将对话转为结构化文字的知识工作者**：远程团队成员记录会议、销售人员复盘客户通话、学生整理讲座、内容创作者转化 YouTube 视频为文章。VOMO 以远低于竞品的价格（$1.92/周 vs 竞品 $10–$17/月）提供高质量的转录+摘要+问答一体体验，形成了明显的价格优势。

VOMO 存在的原因是：大多数人不希望有一个 AI Bot 加入他们的私密谈话，但他们仍然需要从对话中提取关键信息——VOMO 以"隐形助手"的形态填补了这一空白。同时，通过 CLI 工具对接 Claude Code 等 AI Agent 工作流，VOMO 开辟了「会议记忆 → 自动化工作流」的新方向，这在竞品中尚属首创。

---

## 2. 产品信息

VOMO 提供 Web 端和 iOS App 两个入口。核心产品线：

- **AI 转录引擎**：Whisper + Nova-2 双模型，50+/90+ 语言，95–99% 准确率，自动说话人识别
- **Smart Notes**：自动生成会议摘要、行动项（含负责人）、章节、关键决策
- **Ask AI**：GPT-4o 驱动的对话式问答，可对任意转录内容进行自然语言查询
- **输入方式**：实时录音、文件上传（支持 MP3/WAV/M4A/MP4 等，最多 10 个同时）、粘贴 YouTube 链接
- **VOMO CLI**：将转录和笔记拉取到 AI Agent 工作流（Claude Code, Codex, OpenCode）
- **转换工具集**：覆盖 20+ 种音视频格式转换

定价为 **Freemium 模式**：Free 30 分钟/周，Pro **$1.92/周**（≈$8.32/月），是同类产品中定价最低的之一。

> 完整功能清单与定价对比见 [vomo-features.md](./vomo-features.md)

---

## 3. 关键词摘要

核心关键词围绕 "AI transcription"、"meeting notes"、"speech to text"、"YouTube transcript" 等高搜索量品类词，辅以格式转换长尾词（"MP3 to text"、"MP4 to text" 等）和竞品对比词（"Otter alternative"、"Fireflies alternative"）。

品牌词为 "VOMO" 和 "VOMO AI"。博客内容以对比评测（"X vs Y"、"Best X alternatives"）为主要 SEO 策略。

> 完整关键词策略见 [vomo-keywords.md](./vomo-keywords.md)

---

## 4. 竞品摘要

主要直接竞品：**Otter.ai**（实时字幕+会议集成）、**Fireflies.ai**（CRM 集成+销售智能）、**Descript**（音视频编辑+转录）、**Granola**、**Tactiq** 等。

VOMO 的核心差异：① Bot-free（不加入会议）、② 多模型 ASR（准确率领先）、③ 极低定价（$1.92/周）、④ CLI 的 Agent 工作流集成。主要劣势：缺乏第三方集成生态（无 CRM、日历、Slack 等集成）。

> 完整竞品分析见 [vomo-competitors.md](./vomo-competitors.md)

---

## 5. 站点结构摘要

VOMO.ai 为大规模多页面站点：首页 / 定价 / 关于 / 合规页；博客（`/guide`，**38** 篇 + 3 分类）；解决方案（`/use-case/*` **12**）；工具集主导航约 **20** 项，英文 sitemap 中 `/tools/*` 共 **240**（另有大量语种与场景 SEO 页）。Sitemap 索引含 **16** 语言子 sitemap（en ≈ 297 URL，其他语言各 ≈ 278）。

技术栈：疑似 Next.js，GPT-4o + Whisper + Nova-2 为 AI 核心。`/notes` 为产品区（robots Disallow）。

> 完整站点结构见 [vomo-site-structure.md](./vomo-site-structure.md)；URL 全量明细见 [vomo-others.md](./vomo-others.md)

---

## 6. 使用场景摘要

主要 Persona：① 远程团队成员（会议记录、跨时区协作）、② 销售与客户成功（客户通话复盘）、③ 内容创作者（YouTube→文章、播客转录）、④ 学生与研究者（讲座笔记、访谈转录）、⑤ 医疗/法律专业人士（合规记录）。

核心 JTBD：快速将对话转为结构化笔记、会后无需重新听录音即可找到关键决策、将转录内容对接下游工作流。

> 完整场景分析见 [vomo-use-cases.md](./vomo-use-cases.md)

---

## 7. 增长策略摘要

核心渠道：① SEO 内容营销（博客对比评测 + 工具类落地页）、② App Store 优化（4.4★ / 347 评分）、③ Product Hunt 等社区发布、④ 口碑传播。

当前博客以「竞品替代品」类型文章为主（占 80%+），内容策略清晰但有过度集中的风险。建议增加原始研究、客户案例和行业场景深度内容。

> 完整增长策略见 [vomo-growth-strategy.md](./vomo-growth-strategy.md)

---

## 8. 优化建议

1. **补齐 sitemap 与导航不一致的页面** — `/login`、`/contact-us`、`/tools/ai-dictation-tool` 及部分合规页可访问但未进英文 sitemap；若需索引应补录。

2. **创建结构化对比页** — 竞品对比目前主要在博客（如 `/guide/vomo-vs-otter-ai`、`/guide/vomo-vs-fireflies`），建议增加独立对比 IA（如 `/compare/vomo-vs-otter`），商业意图转化通常高于博文。

3. **多语言 SEO 质检** — 站点已有 16 语言 sitemap，下一步应核验 hreflang、翻译完整度，以及印地语等高潜市场是否仍有缺口；并理顺 240 条 Tools 页的内链层级，避免扁平互链稀释权重。

---

*遵循 [客户文档规范](../demo/client-template.md)*
*关联：[keywords](./vomo-keywords.md) | [features](./vomo-features.md) | [competitors](./vomo-competitors.md) | [site-structure](./vomo-site-structure.md) | [use-cases](./vomo-use-cases.md) | [growth-strategy](./vomo-growth-strategy.md) | [podcast-transcription](./podcast%20transcription/podcast-platforms.md) | [youtube-transcription](./youtube%20transcription/youtube-categories.md) | [others](./vomo-others.md)*
*Last updated: 2026-08-23*
*创建日期: 2026-07-16*
