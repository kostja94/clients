# ThetaWave Notes Generator — 核心策略文档

> **主题**：Notes Generator 承载 ThetaWave 双核心词之「生成」意图（核心 B），与 AI Note Taker（核心 A / 记录意图）构成双引擎。本文档集中收录 Notes Generator 产品、关键词、竞品、实施优先级等核心信息，细节见文末关联文档。
>
> 遵循[通用文档规范](../../通用知识库/元文档-通用文档规范.md)：主题一致、去重引用、内容聚焦、相关文档互链。
>
> **输入扩展 2026-05-21**：竞品调研确认 6 条新增输入维度有真实需求。

**Last updated**: 2026-05-21

---

## 一、定位

**一句话定位**：从任意素材（PDF、YouTube、任意网页 URL、文本、音频、图片/板书/手写、课件/幻灯片、在线课程、学术论文、Notion/Obsidian 笔记）一键生成结构化学习笔记，并进一步产出闪卡、测验、思维导图、播客、信息图等格式。

**核心区分**：Notes Generator 聚焦「事后生成/产出」意图（上传素材→获得笔记），与 AI Note Taker 的「实时捕获/记录」意图互补。详见 [thetawave-features.md §〇](./thetawave-features.md#〇核心关键词区分ai-note-taker-vs-notes-generator)。

**品牌关键词**：ThetaWave notes generator, ThetaWave AI notes

---

## 二、落地页

| 项目 | 内容 |
|------|------|
| **URL** | `/feature/notes-generator` |
| **H1** | AI Notes Generator |
| **Title** | AI Notes Generator — Generate Study Notes Instantly \| ThetaWave AI |
| **Meta Description** | Turn lectures, PDFs, YouTube videos, images, and audio into structured study notes, flashcards, and quizzes. 300,000+ students. Free to try. |
| **核心卖点** | Any Source One Tool、Structured & Beautiful、Flashcards & Quizzes、10 语言、Export Anywhere、Privacy First |
| **Proof** | 300K+ 注册学生；4.2★ App Store（~26 评）；10 语言 |

**当前 SEO 状态**：未在 `thetawave.ai` 主域独立审计。需确认 canonical、hreflang、OG tags、Schema（SoftwareApplication + FAQPage）是否到位。

---

## 三、输入维度

Notes Generator 是「多源→笔记」枢纽。各输入方式的独占长尾（如有独立功能页）归各输入页，Notes Generator 作聚合入口。

| # | 输入类型 | 支持状态 | 独占长尾归属 | 竞品参考 |
|---|----------|---------|-------------|---------|
| 1 | 音频/讲座 | ✅ 已上线 | /feature/lecture-to-notes | — |
| 2 | 视频/YouTube | ✅ 已上线（有独立页） | /feature/youtube-to-notes | NoteGPT、Supamind |
| 3 | **网页/文章 URL** | ✅ Chrome Ext 已支持<br>❌ 无独立落地页 | **建议：/feature/url-to-notes** | NotebookLM、Note Hoard |
| 4 | **在线课程（Coursera/Udemy/edX）** | ⚠️ youtube-to-notes 部分覆盖<br>❌ 无平台专属页 | **建议：/feature/online-course-to-notes** | Snipo（40K 用户）、HoverNotes |
| 5 | 文件/PDF | ✅ 已上线 | /feature/pdf-to-notes | — |
| 6 | **课件/幻灯片** | ✅ PDF 导入可处理<br>❌ 无独立落地页 | **建议：/feature/slides-to-notes** | Turbo AI（5M 用户）、SlideNotes |
| 7 | **学术论文/Google Scholar** | ⚠️ pdf-to-notes 部分覆盖<br>❌ 无独立落地页 | **建议：/feature/research-paper-to-notes** | SciSpace、ChatPDF、Scholarcy |
| 8 | **图片/板书/手写** | ⚠️ 有一定 OCR 能力<br>❌ 未作为独立功能宣传 | **建议：/feature/image-to-notes** | Cramberry、Pen to Print |
| 9 | 文本粘贴 | ✅ 已上线 | 归属 Notes Generator 自身 | — |
| 10 | **Notion/Obsidian 笔记集成** | ❌ 未开发 | **建议：/feature/notion-obsidian-integration** | Notes2Flash（1.2K+★）、Klarrity |

---

## 四、调研关键发现

### 4.1 图片/板书/手写→笔记

- **Cramberry**：以图片上传为核心入口，手写照片→闪卡/测验/播客/笔记，功能与 ThetaWave 高度重叠
- **Pen to Print**：专注手写 OCR（拉丁字母），4.6★（24K+ 评），$4.99/月
- **Google Gemini**：免费，手写→学习指南/模拟考/闪卡+Audio Overviews
- 竞品趋势：手写识别已成 2026 年 AI 学习工具标配

### 4.2 URL/网页文章→笔记

- **NotebookLM**（Google）：任意 URL→学习指南+播客；**18 个月从 0 增长到 1.8 亿月访问**
- **Note Hoard / MindWeave / NoteGPT**：任意网页一键→AI 摘要笔记+知识库
- **关键发现**：ThetaWave Quick Notes **已支持**任意网页一键抓取，但仅通过 Chrome Extension 页面宣传，无 `/feature/` 独立落地页承接搜索流量

### 4.3 课件/幻灯片→笔记

- **Turbo AI**：**5M 用户、20K 日新增、8 位数 ARR**；创始人自述学生「主要上传幻灯片/PDF，而非录制讲座」
- **SlideNotes**：专注幻灯片→笔记，~15K 月访问，38% 自然搜索
- **关键发现**：学生搜索的是「slides to notes」而非「PDF to notes」，需要一个独立页面承接这个搜索意图

### 4.4 在线课程平台→笔记

- **Snipo**：Chrome 扩展，Coursera/Udemy/edX 视频→Notion 笔记+时间戳+AI 闪卡；**~40K 用户**，活跃开发中，付费 $4/月
- **HoverNotes / Beastnotes**：同类工具，支持多平台
- **关键发现**：ThetaWave 已通过 `/use-case/for-online-learners` 和 youtube-to-notes 服务在线学习者，但缺少「Coursera to notes」等平台特定搜索的承接

### 4.5 学术论文→笔记

- **市场**：AI 文献阅读工具市场 **$689M（2025）→ $818M（2026）→ $2.85B（2032），CAGR 22.44%**
- **主要玩家**：SciSpace、ChatPDF、Scholarcy、Elicit、NotebookLM
- **关键发现**：ThetaWave 的 pdf-to-notes 可处理论文 PDF，但与学术读者的意图有差距——需引用管理、文献综述、关键发现提取等论文专属功能

### 4.6 Notion/Obsidian 笔记集成

- **Notes2Flash**（Anki 插件）：Notion/Obsidian/Google Docs→AI 生成 Anki 闪卡；1.2K+ GitHub ★
- **Klarrity**：网页高亮→AI 闪卡→导出到 Notion/Obsidian/Anki/Quizlet；**$50/年**
- **Flashcard-inator**：Obsidian→Anki，完全本地离线
- **关键发现**：学生已积累大量笔记在 Notion/Obsidian 中，需要一个「学习引擎」将其转化为闪卡/测验/播客。双方向：导入（已有笔记→学习材料）和导出（学习材料→同步回知识库）
- **生态趋势**：Notion 3.0 和 Obsidian 1.12+ 均向 AI Agent 原生集成演进；MCP 服务器使 AI 工具读写笔记成为标准化能力

---

## 五、实施规划

### 5.1 优先级矩阵

> 评估维度：**市场需求**（竞品规模/用户量）、**现有能力**（是否已有后端）、**SEO 潜力**（搜索意图强度）、**战略价值**（对 ThetaWave 差异化的贡献）。

| 优先级 | 建议功能页 | 市场需求 | 现有能力 | SEO 潜力 | 战略价值 | 后端依赖 |
|--------|-----------|---------|---------|---------|---------|---------|
| **P0** | `/feature/url-to-notes` | ★★★★（NotebookLM 验证） | ★★★★（Chrome Ext 已有） | ★★★★★ | ★★★★ | 低—复用现有 |
| **P0** | `/feature/image-to-notes` | ★★★★（Cramberry/Pen to Print） | ★★★（有 OCR 需强化） | ★★★★★ | ★★★★ | 中—OCR 增强 |
| **P1** | `/feature/slides-to-notes` | ★★★★★（Turbo AI 5M 用户） | ★★★（依赖 pdf-to-notes） | ★★★★ | ★★★★ | 低—复用 pdf-to-notes |
| **P1** | `/feature/online-course-to-notes` | ★★★★（Snipo 40K 用户） | ★★★（依赖 youtube-to-notes） | ★★★ | ★★★ | 低—页面差异化为主 |
| **P2** | `/feature/research-paper-to-notes` | ★★★★（$689M 市场） | ★★（需新功能） | ★★★ | ★★★ | 高—需论文专属能力 |
| **P2** | `/feature/notion-obsidian-integration` | ★★★（Notes2Flash 1.2K★） | ★（需新开发） | ★★ | ★★★★★ | 高—需 API 开发 |
| **P2 (blog)** | exam-paper-to-notes | ★★（搜索量不明） | ★★★（quiz-maker 已有） | ★★ | ★★ | 无—仅内容 |

### 5.2 实施阶段

| 阶段 | 内容 | 目标 |
|------|------|------|
| **Phase 1（立即）** | url-to-notes + image-to-notes | 低投入、高 SEO 回报；利用现有能力快速上线 |
| **Phase 2（近期）** | slides-to-notes + online-course-to-notes | 页面差异化定位，共享后端，中等投入 |
| **Phase 3（中期）** | research-paper-to-notes + notion-obsidian-integration + exam-paper-to-notes blog | 需要新功能开发；先写 blog 测试论文和试卷方向 |

### 5.3 各功能页与 Notes Generator 聚合枢纽的关系

所有建议新增功能页本质上是 **NG（Notes Generator）聚合枢纽的 SEO 入口**——它们在搜索中承接不同的意图关键词，但在后端可以复用 Notes Generator/各功能页的现有能力，不需要为每个页面独立开发一套处理管线。

| 新增页面 | 复用哪个后端能力 |
|----------|----------------|
| url-to-notes | Chrome Extension 抓取 + NG 结构化 |
| image-to-notes | 现有 OCR + NG 结构化 |
| slides-to-notes | pdf-to-notes（PPT→PDF） |
| online-course-to-notes | youtube-to-notes |
| research-paper-to-notes | pdf-to-notes（需增强引用/摘要） |
| notion-obsidian-integration | 需新建 API 连接器 |

### 5.4 转化策略

所有 Notes Generator 相关的功能页遵循统一的转化路径：

```
搜索流量 → 功能落地页（免费试用） → 笔记生成体验 → Pro 升级（解锁高级功能 + 更大用量）
```

- **免费层钩子**：结构化笔记生成（所有输入方向均提供免费试用）
- **Pro 转化点**：更丰富的笔记格式、更多输出类型、更大处理量。输出格式详情见 [thetawave-features.md](./thetawave-features.md)
- **定价参考**：$118.80/年，学生首年 $83.16（30% off），无月付。详见 [thetawave.md §5](./thetawave.md#5-existing-website)

---

## 六、内容营销管道

以下方向有需求但规模不确定，通过博客内容先测试搜索反应。

| 方向 | 验证 | 建议动作 | 目标关键词 |
|------|------|---------|-----------|
| 试卷/真题→笔记 | QuickPass AI、NotebookLM、Thea 支持 | 博客：「How to Turn Past Exam Papers into Study Notes」；内链至 quiz-maker 和 notes-generator | past paper to notes, exam paper to study guide |

---

## 七、关键词（核心）

> 完整关键词策略见 [thetawave-keywords.md §2.1](./keywords/thetawave-keywords.md#21-notes-generator核心-b)。10 语种本地化检索词见 [feature-pages-keywords-localization.md §2](./keywords/feature-pages-keywords-localization.md#2-notes-generator)。

### 7.1 输入侧——Notes Generator 自身 + 各输入功能页

| 类型 | 关键词 | 目标页 |
|------|--------|--------|
| **核心** | **AI notes generator, notes generator, generate study notes** | /feature/notes-generator |
| **扩展** | generate notes from PDF/YouTube/lecture | /feature/notes-generator |
| **扩展（图片）** | image to notes, photo to notes, handwritten notes to digital | /feature/image-to-notes |
| **扩展（URL）** | url to notes, webpage to notes, article to notes | /feature/url-to-notes |
| **扩展（课件）** | slides to notes, lecture slides to notes, powerpoint to notes | /feature/slides-to-notes |
| **扩展（在线课程）** | coursera to notes, udemy to notes, online course notes | /feature/online-course-to-notes |
| **扩展（学术论文）** | research paper to notes, academic paper summarizer, google scholar to notes | /feature/research-paper-to-notes |
| **扩展（集成）** | notion to notes, obsidian to notes, notion flashcard generator | /feature/notion-obsidian-integration |
| **长尾** | best AI notes generator, AI notes generator for students | /feature/notes-generator、博客 |

### 7.2 竞品对比关键词

| 关键词 | 目标页 | 说明 |
|--------|--------|------|
| ThetaWave vs ChatGPT, ChatGPT alternative for notes | /thetawave-vs-chatgpt | 已规划详见 [thetawave-vs-chatgpt.md](./thetawave-vs-chatgpt.md) |
| TurboLearn alternative, Snipo alternative | /feature/notes-generator | 选型对比类，博客或对比页 |

---

## 八、站内位置

```
首页 (/)  ← AI Note Taker（实时捕获/记录）
  └── /feature/notes-generator  ← ★ Notes Generator 聚合枢纽（生成/产出）
        ├── /feature/lecture-to-notes（音频→笔记）✅
        ├── /feature/youtube-to-notes（视频 URL→笔记）✅
        ├── /feature/url-to-notes（任意网页 URL→笔记）← P0 新增
        ├── /feature/online-course-to-notes（Coursera/Udemy/edX→笔记）← P1 新增
        ├── /feature/pdf-to-notes（文件→笔记）✅
        ├── /feature/slides-to-notes（课件/幻灯片→笔记）← P1 新增
        ├── /feature/image-to-notes（图片/板书/手写→笔记）← P0 新增
        ├── /feature/research-paper-to-notes（学术论文→笔记）← P2 新增
        ├── /feature/notion-obsidian-integration（从已有笔记库→学习材料）← P2 新增

    Chrome Extension（Quick Notes）— 任意网页/YouTube 一键抓取
    注：博客文章在提及「notes generator」场景时内链至 /feature/notes-generator
```

---

## 关联文档

> **规则**：关联文档置于文末，正文优先。关联文档不是目录，仅在有跳转需要时查阅。

| 文档 | 用途 |
|------|------|
| [thetawave.md](./thetawave.md) | 产品营销上下文（定价、ARR、URL 清单、公司信息） |
| [thetawave-features.md](./thetawave-features.md) | 10 功能页概览（§〇 核心关键词区分、§三.0 Notes Generator 详情） |
| [keywords/thetawave-keywords.md](./keywords/thetawave-keywords.md) | 全站关键词映射（§1 主关键词表、§2.1 Notes Generator 专项） |
| [keywords/feature-pages-keywords-localization.md](./keywords/feature-pages-keywords-localization.md) | 10 语种 P1/P2/P3 检索词（§2 Notes Generator） |
| [thetawave-competitors.md](./thetawave-competitors.md) | 竞品分析 |
| [thetawave-use-cases.md](./thetawave-use-cases.md) | Use Cases 三分支枢纽 |
| [thetawave-data-attribution.md](./thetawave-data-attribution.md) | GA4 + BigQuery 归因方案 |
| [thetawave-project-tasks.md](./thetawave-project-tasks.md) | SEO 待办 13 项 |
