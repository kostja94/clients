---
name: thetawave-meta-title-description
description: Write or optimize meta title and meta description for ANY thetawave.ai page. HARD RULE every title and description must strongly match that page's target keywords and theme (not generic copy). Self-contained; covers /feature, /use-case, /study, /blog, /knowledge-hub, /comparison, all locales.
metadata:
  version: 2.2.1
  project: thetawave.ai
  self-contained: true
---

# ThetaWave Meta Title & Description

为 **https://thetawave.ai** 编写或优化 `<title>` 与 `<meta name="description">`。**硬性要求：每条 title 和 description 必须与该 URL 对应页面的目标关键词和页面主题强相关**——不可用泛化 SaaS 话术、不可套模板而不改主题词、不可写与页面 H1/正文无关的 metadata。

**本文件自包含**：Agent 只需读取本 skill，无需访问仓库内其他文档。

---

## 如何使用（分发给他人）

1. 将本文件复制到 Agent 的 skills 目录，例如：
   - Cursor: `.cursor/skills/thetawave-meta-title-description/SKILL.md`
   - Claude Code: `.claude/skills/thetawave-meta-title-description/SKILL.md`
2. 对 Agent 说：「按 thetawave-meta-title-description skill，为 [URL 或页面类型] 写 title 和 description」
3. 批量任务示例：「按 skill 为 `/study/education-notes` 和 `/ko/blog/...` 写 title + description」

**Agent 执行时**：直接输出 metadata 方案；首次可用 1 句说明范围，后续跳过前言。若 URL 不在清单中，走 §任意页面 Fallback。

---

## 页面类型路由（任意 URL 第一步）

给定 URL 后，**先去掉 locale 前缀**，再按 path 匹配：

| 路径匹配 | 类型 | 跳转章节 |
|----------|------|----------|
| `/` | 首页 | §首页 |
| `/feature/{slug}` | 功能页 | §功能页 |
| `/use-case/{slug}` | Use Case | §Use Cases |
| `/study` | Study 聚合 | §Study |
| `/study/{slug}-notes` | Study 学科页 | §Study |
| `/study/{slug}`（非 `-notes`） | Study 主题/工作流页 | §Study |
| `/comparison/thetawave-vs-{x}` | 对比页 | §对比页 |
| `/comparison` | 对比聚合 | §首页、聚合 |
| `/blog/{slug}` | 博客文章 | §博客 |
| `/blog` | 博客聚合 | §首页、聚合 |
| `/knowledge-hub/{slug}?id=` | Knowledge Hub 单条 | §Knowledge Hub |
| `/knowledge-hub` | Knowledge Hub 聚合 | §Knowledge Hub |
| `/pricing`, `/download`, `/explore`, `/chrome-extension`, `/changelog` | 营销页 | §首页、聚合 |
| `/legal/{slug}` | 法务页 | §法务页 |
| `/use-cases`, `/feature` | 聚合 hub | §首页、聚合 |
| `/{locale}/...` | 多语（任意上述类型） | §多语言 + 对应类型章节 |
| 其他可索引 path | 未知页 | §任意页面 Fallback |

**Locale 前缀**（匹配后剥离）：`de` `es` `fr` `it` `ja` `ko` `pt` `zh` `zh-tw`

**示例**：
- `https://thetawave.ai/ko/study/education-notes` → Study 学科页 + 韩语本地化
- `https://thetawave.ai/study/exam-review` → Study 主题/工作流页（en）
- `https://thetawave.ai/zh/blog/youtube-summary-ai-for-students` → 博客 + 简体中文

---

## Scope

| 元素 | 职责 |
|------|------|
| **Title tag** | **页面主题 + P1 关键词** 前置；功能页用冒号 + 动作句；每页唯一；品牌置尾 |
| **Meta description** | **页面主题下的 P2** + 该页独有场景/材料 + CTA；不与 title 重复同一句 |
| **不覆盖** | 正文、H2 结构、Schema、og:*、hreflang、robots |

---

## 核心原则：页面主题与关键词强相关（最高优先级）

**每条 metadata 都是「这一页」的 SERP 承诺，不是全站通用广告语。**

| 规则 | 说明 | 反例 |
|------|------|------|
| **一页一词一组** | title/description 的 P1、P2 必须来自 **该 URL 所在章节清单** 或 **该页 H1/首屏主题** | 所有功能页都写 `Best AI Note Taker` |
| **主题词入 title** | 页面核心主题（学科/输入格式/persona/书名/文章题）必须在 title 冒号前或 editorial 标题中 **显性出现** | `/study/education-notes` 写 `Study Notes: Turn Any Material...`（缺 Education） |
| **description 展开主题** | description 写 **该页独有的材料、考试、工作流、输出**，不是换说法重复 title | education 页只写 generic `notes, flashcards, quizzes` 而不提 Praxis/edTPA |
| **禁止套娃** | 不可把 A 页推荐 title 改几个词用于 B 页；批量任务时 **逐 URL 核对 P1/P2 表** | flashcard-maker 与 quiz-maker 用同一句 description |
| **与 H1 同主题** | 用户点进 SERP 后，H1 与 title 应感觉在讲 **同一件事**；可更短，不可更偏 | title 讲 YouTube，H1 却是 PDF |
| **多语 = 同主题** | 本地化时 **主题不变、检索词变**；`/zh/study/education-notes` 必须含「教育学/education」语义，不是泛化「学习笔记」 | 中文页写成泛化「AI 笔记工具」 |

**自检问句（输出前必答）**：

1. 若去掉品牌名，title 能否让人猜出 **这是哪一页**？（不能 → 重写）
2. description 是否至少包含 **1 个该页专属主题词**（非全站共用词）？（没有 → 重写）
3. 该页清单中的 P1 是否在 title 中出现？P2 是否在 description 中出现？（缺 → 补）

---

## 产品上下文（内嵌，勿外查）

**ThetaWave** 是面向大学生的 AI 笔记与学习平台（B2C SaaS，Freemium）。

| 项 | 内容 |
|----|------|
| **一句话** | 实时捕获讲座，将 audio / text / files / YouTube 转为 formatted notes、mind maps、quizzes、flashcards、podcasts |
| **ICP** | 大学生（本科、研究生）；次要：高中生、自学者 |
| **定位** | 比通用 ChatGPT 更专于 **学习笔记 + 结构化输出**；比 Otter 更专于 **复习材料生成** |
| **定价** | 免费试用；Pro 约 $118.80/年；学生首年折扣；7 天退款（以官网为准） |
| **站点** | https://thetawave.ai |
| **多语言路径** | `/de/` `/es/` `/fr/` `/it/` `/ja/` `/ko/` `/pt/` `/zh/` `/zh-tw/` + 英文无前缀 |
| **Voice** | 年轻、高效、学生友好；用 students, learn, capture, transform, effortlessly |
| **Avoid** | 企业 jargon、未验证 claim |

**可引用的 Proof points**（description 可选用，勿夸大）：

- 300,000+ registered students
- Free to try
- 10+ languages（**勿写** 50+）
- 4.2★ App Store rating
- Learn 10x faster（slogan，非可量化数据）

**禁止写入 metadata**（除非用户明确提供已核实数据）：

- SOC 2 认证、端到端加密
- Anki 导出（未证实）
- 「比 ChatGPT 准确率高 30%」等对比数字
- 月付价格（官网仅年付）

---

## 双核心词策略（全站 SEO 基石）

| 意图 | 核心词 | 主承接 URL |
|------|--------|------------|
| **记录** | AI note taker, lecture note taker, real-time note taking | `/`、`/feature/lecture-to-notes` |
| **生成** | AI notes generator, notes generator, generate study notes | `/feature/notes-generator` |

**规则**：两意图不可混为一谈。首页 / lecture 页不打「notes generator」为主词；notes-generator 页不打「real-time capture」为主词。

---

## 长度（按语言）

Google 按像素截断；下表为字符近似值。

| Script | Title | Meta description |
|--------|-------|------------------|
| Latin (en, de, es, fr, it, pt) | 50–60 | 150–160 |
| CJK (zh-Hans, zh-Hant, ja, ko) | 25–35 | 70–100 |

多语言：**本地化** P1/P2，勿英译后直接截断。简繁不可混用。

---

## Title 结构原则

### 功能页 / Use Case / Study / 对比页（默认：冒号 + 动作句）

面向 **Transactional 意图**——用户知道要做什么，title 应 **镜像搜索 query**，不是贴品类标签。

```
{P1 Keyword}: {Verb} {Input} into {Output} with AI | Thetawave
```

**示例（标准）**：

```
YouTube to Notes: Convert YouTube Video into Notes with AI | Thetawave
```

| 原则 | 说明 | 反例 |
|------|------|------|
| 冒号结构 | P1 在前，动作句在后 | `YouTube to Notes — AI Video Note Taker` |
| 动作动词 | Convert, Generate, Turn, Transcribe, Summarize, Create | 仅写 Note Taker / Generator |
| 自然语言 | 像用户搜索句 | 泛类目词 |
| 品牌 | 功能页用 `\| Thetawave` 省字符 | 固定 `\| ThetaWave AI` 挤占动作句 |
| Title ≠ Description | Title = P1 + 动作 | Description = P2，不重复 title |

### 首页（em dash + slogan）

```
{Primary Keyword} — {Value Prop} | ThetaWave AI
```

示例：`AI Note Taker for Students — Learn 10x Faster | ThetaWave AI`

### 博客 / Knowledge Hub 条目（editorial 或资源名 + 收益）

```
{Topic or Resource Title}: {What reader gets}   或   {Topic Title} ({Year} Guide)
```

slug **不含年份**（博客）；Knowledge Hub URL 可含 `?id=` 查询参数，title 用 **资源/书名**，非 id。

---

## Title vs Description 分工

| 元素 | 写什么 | 不写什么 |
|------|--------|----------|
| **Title** | **该页 P1 + 该页主题词** + 动词 + with AI | 其他页面的 P1/P2；泛类目标签 |
| **Description** | **该页 P2 + 该页场景/材料/考试/工作流** + CTA | 与 title 同句；其他页主题词 |

两者都必须 **强相关于同一页面主题**——title 锁定「搜什么进来」，description 锁定「这一页具体解决什么」。

### Title / Description 关键词变体分工（推荐）

**Title 与 description 不重复同一句，但应覆盖同一关键词簇的变体**——title 偏 **名词/工具名**，description 偏 **动词短语 / 动名词**，扩大 SERP 语义匹配。

| 位置 | 推荐句式 | 示例 |
|------|----------|------|
| **Title** | `{Topic} Notes Generator`、`AI {Topic} Notes Generator`、`{Input} to Notes` | `AI Notes Generator: …`、`Education Notes Generator: …`（若主题需要） |
| **Description** | `generate notes from {source}`、`notes generation from {source}`、`generate {output} from your notes` | `Generate notes from pedagogy lectures and readings…` |

**规则**：

1. **Title 用 Generator / Note Taker 等名词标签**（类目 + 主题词），冒号后可跟动作句。
2. **Description 用 generate notes from / notes generation / turn … into notes** 等动词或动名词变体，**不要**再写一遍 title 里的 `{X} Notes Generator` 整句。
3. **变体须对应该页主题**：education 页 → `generate notes from pedagogy lectures`；YouTube 页 → `generate notes from YouTube videos`；不可全站共用同一句 `generate notes from any source`（除非 notes-generator 页）。
4. **与 P1/P2 一致**：title 承载 P1（如 `AI notes generator`）；description 用 P1 变体 + P2 场景词。

**成对示例**：

| 页面 | Title（含 Generator / 工具名） | Description（含 generate / generation 变体） |
|------|--------------------------------|-----------------------------------------------|
| /feature/notes-generator | `AI Notes Generator: Generate Study Notes from Any Source with AI \| Thetawave` | `Notes generation from lectures, PDFs, YouTube, and audio—structured outlines, flashcards, and quizzes. Free to try.` |
| /study/education-notes | `Education Notes: Turn Pedagogy Lectures into Structured Study Notes with AI \| Thetawave` | `Generate notes from education lectures, observation reflections, and textbook chapters—ready for Praxis and edTPA review. Free to try.` |
| /feature/youtube-to-notes | `YouTube to Notes: Convert YouTube Video into Notes with AI \| Thetawave` | `Generate notes from YouTube videos with chapter timestamps, playlists, and tutorial channels. Free to try.` |
| /feature/flashcard-maker | `AI Flashcard Generator: Turn Notes into Flashcards with AI \| Thetawave` | `Generate flashcards from your notes and PDFs with spaced repetition and cloze cards. Free to try.` |

**其他常见变体对照**（title → description）：

| Title 侧 | Description 侧 |
|----------|----------------|
| `{X} Notes Generator` | generate notes from … / notes generation from … |
| `AI Note Taker` | capture notes from … / note taking from … |
| `AI Flashcard Generator` | generate flashcards from … / flashcard generation from … |
| `AI Quiz Generator` | generate quizzes from … / quiz generation from … |
| `{Subject} Notes`（Study 页） | generate {subject} notes from … / notes generation for {exam} prep |

**禁止**：title 与 description **整句重复**；或 description 完全不用该页关键词变体（只写 `Free to try`）。

Description 公式（功能页 / Study 页，更新）：

```
{P1 variant: generate notes from … / notes generation from …}. {P2 differentiator}. Free to try.
```

---

## 全站 URL 模式

| 类型 | 模式 | 规模（en 基准 path） |
|------|------|----------------------|
| 首页 | `/` | 1 |
| 功能页 | `/feature/{slug}` | 16 |
| Use Case | `/use-case/{slug}` | 19 |
| **Study** | `/study`, `/study/{slug}-notes`, `/study/{topic}` | 14+（动态扩展） |
| 对比页 | `/comparison/thetawave-vs-{competitor}` | 12 |
| 博客 | `/blog/{slug}` | 9+（动态扩展） |
| **Knowledge Hub** | `/knowledge-hub/{slug}?id={id}` | 200+（动态） |
| 聚合 hub | `/use-cases`, `/blog`, `/feature`, `/comparison`, `/study`, `/knowledge-hub` | 若干 |
| 营销页 | `/pricing`, `/download`, `/explore`, `/chrome-extension`, `/changelog` | 若干 |
| 法务 | `/legal/privacy-policy`, `/legal/terms` | 2 |
| 多语 | `/{locale}/...`（上述任一路径 × 10 语种） | ~3000 URL |

**× 10 语种**：除 noindex 页外，**绝大多数索引页都有** `/{locale}/` 版本；metadata **按语种独立撰写**，结构遵循对应页面类型。

**勿为以下路径写 SEO metadata**（noindex / robots 屏蔽）：`/auth/*`, `/app/*`, `/signup`, `/login`, `/onboarding/*`, `/mobile`, `/team/*`, `/test/*`, `/go/*`

---

## 功能页完整清单（16 页）

URL 基准：`https://thetawave.ai/feature/{slug}`

| slug | P1（en，title 冒号前） | P2（en，仅 description） | 推荐 Title |
|------|------------------------|---------------------------|------------|
| notes-generator | AI notes generator, notes generator | multi-source ingest, outline levels, rubric-aligned study guide | `AI Notes Generator: Generate Study Notes from Any Source with AI \| Thetawave` |
| lecture-to-notes | lecture to notes, transcribe lecture | in-person classroom, professor long-form audio, LaTeX/formulas | `Lecture to Notes: Transcribe Lectures into Structured Notes with AI \| Thetawave` |
| youtube-to-notes | YouTube to notes, video to notes | chapter timestamps, playlist batch, tutorial channels | `YouTube to Notes: Convert YouTube Video into Notes with AI \| Thetawave` |
| pdf-to-notes | PDF to notes, summarize PDF | textbook chapters, page-level cites, scanned OCR | `PDF to Notes: Summarize PDF into Study Notes with AI \| Thetawave` |
| flashcard-maker | AI flashcard generator | spaced repetition, cloze deletion, deck export | `AI Flashcard Generator: Turn Notes into Flashcards with AI \| Thetawave` |
| quiz-maker | AI quiz generator | mock exam pacing, distractor quality, answer explanations | `AI Quiz Generator: Create Practice Quizzes from Notes with AI \| Thetawave` |
| podcast-generator | AI podcast generator, notes to podcast | commute listening, multi-voice TTS, offline playback | `AI Podcast Generator: Turn Notes into Audio for Studying with AI \| Thetawave` |
| mind-map-maker | AI mind map generator | parent-child branches, concept clustering, exam scope canvas | `AI Mind Map Generator: Turn Text into Mind Maps with AI \| Thetawave` |
| infographic-generator | AI infographic generator | one-page poster, share card, icon-stat blocks | `AI Infographic Generator: Turn Notes into Visual Study Guides with AI \| Thetawave` |
| exam-generator | AI exam generator | full mock tests, weak-topic retest, adaptive difficulty | `AI Exam Generator: Create Practice Exams from Notes with AI \| Thetawave` |
| ai-study-assistant | AI study assistant | note-based Q&A, concept explanations from your materials | `AI Study Assistant: Ask Questions About Your Notes with AI \| Thetawave` |
| image-to-notes | image to notes | photo of whiteboard, handwritten notes OCR | `Image to Notes: Convert Photos into Study Notes with AI \| Thetawave` |
| url-to-notes | web page to notes, URL to notes | any webpage, Chrome extension one-click | `URL to Notes: Turn Web Pages into Notes with AI \| Thetawave` |
| slides-to-notes | slides to notes | lecture slides, deck to structured notes | `Slides to Notes: Convert Slides into Study Notes with AI \| Thetawave` |
| online-course-to-notes | online course to notes | Coursera/edX/Khan, course video series | `Online Course to Notes: Turn Course Videos into Notes with AI \| Thetawave` |
| research-paper-to-notes | research paper to notes | literature synthesis, page-level quotes | `Research Paper to Notes: Summarize Papers into Notes with AI \| Thetawave` |

**动作动词选用**（每页一个，避免全站重复）：

| 输入形态 | 优先动词 |
|----------|----------|
| 视频 / YouTube / 课程 | Convert, Turn |
| PDF / 论文 / 长文 | Summarize, Extract |
| 讲座 / 音频 | Transcribe, Record |
| 笔记 → 输出格式 | Turn, Generate, Create |

**YouTube 页 description 示例**（title 已写 convert，description 只写 P2）：

> Get structured notes with chapter timestamps, playlist batching, and key concepts from tutorial channels. Free to try.

---

## Use Cases 完整清单（19 页）

URL 基准：`https://thetawave.ai/use-case/{slug}`（**use-case 单数**）

**Title 模式**：

```
AI Note Taker for {Persona}: Turn {Material} into {Output} with AI | Thetawave
```

或阶段类：`{Stage}: Turn {Material} into {Output} with AI | Thetawave`

| slug | 分支 | P1（en） | 痛点/场景（description 用） |
|------|------|----------|----------------------------|
| for-law-students | Subject | AI note taker for law students | case briefs, dense readings, exam prep |
| for-nursing-students | Subject | AI study tool for nursing students | drug cards, NCLEX-style practice, clinical lectures |
| for-pre-med-students | Subject | AI note taker for pre-med | organic chem lectures, MCAT prep materials |
| for-stem-students | Subject | AI note taker for STEM students | formulas, tables, lab lectures |
| for-cs-students | Subject | AI note taker for CS students | code lectures, algorithm notes |
| for-biology-students | Subject | AI notes for biology majors | diagrams, terminology-heavy lectures |
| for-business-students | Subject | AI note taker for business students | case studies, MBA lectures |
| for-economics-students | Subject | AI note taker for economics | models, graphs, problem sets |
| for-psychology-students | Subject | AI note taker for psychology | theories, research papers, stats |
| for-education-students | Subject | AI note taker for education majors | pedagogy courses, field notes |
| for-graduate-students | Identity | AI note taker for grad school | research-heavy workload, thesis sources |
| for-international-students | Identity | multi-language study notes | ESL lectures, translate + structure |
| for-online-learners | Identity | AI note taker for online courses | async video, no live capture |
| for-adhd-students | Identity | ADHD study app, focus notes | distraction-free capture, multimodal outputs |
| exam-prep | Stage | exam prep AI, notes to flashcards | cramming, mock tests, weak topics |
| research-thesis | Stage | research note taking, thesis notes | lit review, long PDFs, citation-ready notes |
| daily-study | Stage | daily study sessions AI | routine review, multi-course organization |
| group-study | Stage | collaborative study notes | shared materials, group exam prep |
| korean-history-exam-prep | Stage (KR) | Korean history exam prep | timeline, source questions（韩文市场本地化） |
| toeic-prep | Stage (KR) | TOEIC prep AI | LC expressions, wrong-answer notes |

**Use Case Title 示例**：

- `AI Note Taker for Law Students: Turn Lectures into Case Briefs with AI | Thetawave`
- `Exam Prep with AI: Turn Notes into Flashcards and Quizzes with AI | Thetawave`

**Use Case Description 公式**：

```
{Persona pain in one clause}. Capture {sources} and get notes, flashcards, and quizzes built for {context}. Free to try.
```

**规则**：功能页 title 不写 `for law students`；Use Case title 不写 `YouTube summarizer`（那是 feature 页 P1）。

---

## Study 页（`/study/*`）

**定位**：Study = **学科学习资源 hub / 主题工作流落地页**（教材、topic map、考试路径、视频笔记工作流）。与 Use Case 区别：

| 维度 | `/use-case/*` | `/study/*` |
|------|---------------|------------|
| 回答 | 谁在用、什么情境 | 学什么科目 / 什么复习工作流 |
| 内容 |  persona + 痛点 + 产品能力 | 学科笔记、topic map、推荐路径、FAQ |
| Title 侧重 | `AI Note Taker for {Persona}` | `{Subject} Notes` 或 `{Topic} Video Notes` |

URL 基准：`https://thetawave.ai/study/{slug}`；多语：`/{locale}/study/{slug}`

### A. Study 聚合 `/study`

- **Title**: `Study Notes & Subject Guides — AI Notes for Every Course | Thetawave`
- **Description**: `Browse subject study guides for law, nursing, STEM, education, and more. Turn lectures and readings into notes, flashcards, and quizzes. Free to try.`

### B. 学科页 `/study/{subject}-notes`（13 页，sitemap 已收录）

**Title 模式**：

```
{Subject} Notes: Turn {Subject Material} into Study Notes with AI | Thetawave
```

| slug | P1（en） | P2（description 专用） | 推荐 Title |
|------|----------|------------------------|------------|
| biology-notes | biology notes, biology study notes | diagrams, lab terms, MCAT bio review | `Biology Notes: Turn Lectures and Textbooks into Study Notes with AI \| Thetawave` |
| business-notes | business school notes, MBA notes | case studies, frameworks, exam finals | `Business Notes: Turn Case Studies and Lectures into Study Notes with AI \| Thetawave` |
| calculus-notes | calculus notes, calculus study guide | problem sets, exam review, step-by-step | `Calculus Notes: Turn Lectures and Problem Sets into Study Notes with AI \| Thetawave` |
| chemistry-notes | chemistry notes, chem study notes | formulas, reactions, exam cram | `Chemistry Notes: Turn Lectures and Labs into Study Notes with AI \| Thetawave` |
| cs-notes | computer science notes, CS lecture notes | code lectures, algorithms, project docs | `CS Notes: Turn Code Lectures and Slides into Study Notes with AI \| Thetawave` |
| economics-notes | economics notes | models, graphs, problem sets | `Economics Notes: Turn Lectures and Readings into Study Notes with AI \| Thetawave` |
| education-notes | education notes, pedagogy notes | Praxis/edTPA prep, observation notes, lesson planning | `Education Notes: Turn Pedagogy Lectures into Structured Study Notes with AI \| Thetawave` |
| law-notes | law school notes, law notes | case briefs, dense readings, exam prep | `Law Notes: Turn Lectures and Case Readings into Study Notes with AI \| Thetawave` |
| nursing-notes | nursing school notes, NCLEX notes | drug cards, clinical lectures, NCLEX-style review | `Nursing Notes: Turn Clinical Lectures into Drug Cards and Study Notes with AI \| Thetawave` |
| physics-notes | physics notes | formulas, problem-solving, exam review | `Physics Notes: Turn Lectures and Problem Sets into Study Notes with AI \| Thetawave` |
| pre-med-notes | pre-med notes, MCAT notes | organic chem, biochem pathways, MCAT review | `Pre-Med Notes: Turn Lectures and MCAT Materials into Study Notes with AI \| Thetawave` |
| psychology-notes | psychology notes | theories, research, stats-heavy courses | `Psychology Notes: Turn Lectures and Readings into Study Notes with AI \| Thetawave` |
| stem-notes | STEM notes | formulas, tables, multi-course STEM workload | `STEM Notes: Turn Science and Math Lectures into Study Notes with AI \| Thetawave` |

**Education Notes description 示例**（title 已写 pedagogy → notes，description 写 P2 + 考试）：

> Organize pedagogy frameworks, observation notes, and certification topics into flashcards and practice questions for Praxis and edTPA prep. Free to try.

### C. 主题 / 工作流页 `/study/{topic}`（动态，如 exam-review）

**适用**：复习视频合集、跨学科工作流、非 `{subject}-notes` 命名的 study 落地页。

**Title 模式**：

```
{Topic Title}: {Verb} {Source} into {Study Output} with AI | Thetawave
```

| slug | 页面主题 | 推荐 Title | Description P2 |
|------|----------|------------|----------------|
| exam-review | Exam review video notes（化学、微积分、MCAT、AP 等复习视频） | `Exam Review Video Notes: Convert Review Videos into Quiz-Ready Notes with AI \| Thetawave` | chemistry/calc/biology/MCAT/AP review playlists; flashcards, mind maps, podcasts |

**exam-review description 示例**：

> Turn high-yield exam review videos into structured notes, quizzes, flashcards, and mind maps for last-pass review. Use YouTube-to-notes, then listen as a podcast. Free to try.

**新 Study 主题页**：从 H1 + 首屏文案提取 topic；套用 `{Topic}: {Verb} {Input} into {Output} with AI | Thetawave`；P2 写该页独有的材料类型或工作流步骤。

**Study vs Use Case cannibalization**：
- `/use-case/for-education-students` → persona「education majors 怎么用 ThetaWave」
- `/study/education-notes` → 资源 hub「education 笔记怎么组织、考什么证」
- 两页 title **不可互换**；Study 用 `{Subject} Notes`，Use Case 用 `AI Note Taker for {Persona}`

---

## 对比页（12 页）

URL：`https://thetawave.ai/comparison/thetawave-vs-{competitor}`

| slug | Primary keyword |
|------|-----------------|
| thetawave-vs-chatgpt | ChatGPT alternative, ThetaWave vs ChatGPT |
| thetawave-vs-otter | Otter alternative for students |
| thetawave-vs-quizlet | Quizlet alternative |
| thetawave-vs-knowt | Knowt alternative |
| thetawave-vs-remnote | RemNote alternative |
| thetawave-vs-notebooklm | NotebookLM alternative |
| thetawave-vs-anki | Anki alternative |
| thetawave-vs-asksia | AskSia alternative |
| thetawave-vs-clova-note | Clova Note alternative |
| thetawave-vs-daglo | Daglo alternative |
| thetawave-vs-lilys-ai | Lilys AI alternative |
| thetawave-vs-univ-ai | Univ AI alternative |

**Title 模式**：

```
ThetaWave vs {Competitor}: {Differentiator for Students} | Thetawave
```

**示例**：

- Title: `ThetaWave vs ChatGPT: AI Note Taker Built for Students | Thetawave`
- Description: `Comparing ChatGPT and Thetawave for study notes? Thetawave captures lectures live and outputs notes, flashcards, quizzes, and podcasts—built for students. Free to try.`

勿写未核实准确率数字。对比结论放 description 前半句。

---

## 首页、聚合、其他营销页

### 首页 `/`

- **P1**: AI note taker, AI note taking app, best AI note taker for students
- **Title**: `AI Note Taker for Students — Learn 10x Faster | ThetaWave AI`
- **Description**: `Capture lectures in real time and turn audio, PDFs, and YouTube into notes, flashcards, quizzes, and podcasts. Trusted by 300,000+ students. Free to try.`

### 聚合页

| URL | Title 示例 |
|-----|------------|
| /use-cases | `AI Note Taker Use Cases for Students \| ThetaWave AI` |
| /blog | `ThetaWave Blog — AI Notes & Study Tips for Students` |
| /feature | `AI Study Tools — Notes, Flashcards, Quizzes & More \| ThetaWave AI` |
| /comparison | `ThetaWave Comparisons — Best AI Note Taker Alternatives` |
| /pricing | `ThetaWave Pricing — AI Note Taker Plans for Students \| Thetawave` |
| /chrome-extension | `Chrome Extension: Save Web Pages & YouTube as Notes \| Thetawave` |
| /study | `Study Notes & Subject Guides — AI Notes for Every Course \| Thetawave` |
| /knowledge-hub | `Knowledge Hub — Free Open Textbooks & Study Resources \| Thetawave` |
| /download | `Download ThetaWave — AI Note Taker for iOS, Android & Web \| Thetawave` |
| /explore | `Explore ThetaWave — AI Study Tools for Students \| Thetawave` |

### 法务页 `/legal/*`

| URL | Title | Description |
|-----|-------|-------------|
| /legal/privacy-policy | `Privacy Policy \| Thetawave` | 简短说明数据收集与 TLS 传输；无营销 CTA |
| /legal/terms | `Terms of Service \| Thetawave` | 简短说明使用条款；无营销 CTA |

法务页 **不用** 冒号动作句；description 一句概括即可，50–120 chars。

---

## 博客 `/blog/{slug}`

**线上已收录 slug（en）**——新文章按同规则扩展：

| slug | 建议 title 角度 | 主关键词 |
|------|-----------------|----------|
| how-to-turn-past-exam-papers-into-study-notes | How-to | past exam papers to study notes |
| infographic-study-guide | Guide | infographic study guide |
| mind-map-study-guide | Guide | mind map study method |
| research-paper-summary-ai | Tool/method | research paper summary AI |
| youtube-summary-ai-for-students | Tool roundup | YouTube summary AI for students |
| korean-history-exam-timeline | Exam prep (KR) | Korean history exam timeline |
| korean-history-source-questions | Exam prep (KR) | Korean history source questions |
| toeic-lc-expression-review | Exam prep (KR) | TOEIC LC expressions |
| toeic-wrong-answer-notes | Exam prep (KR) | TOEIC wrong answer notes |

Frontmatter 即 SERP metadata：

```yaml
---
title: "How to Turn Past Exam Papers Into Study Notes (2026)"
description: "Turn old exams into flashcards, summaries, and practice quizzes—not just reread them. Step-by-step workflow for college students."
slug: "how-to-turn-past-exam-papers-into-study-notes"   # 不含年份
date: 2026-04-16
---
```

| 项 | 规则 |
|----|------|
| title | editorial；how-to / guide / roundup；通常 **不加** `\| Thetawave` |
| description | 读者将得到什么 + 主关键词；轻 CTA 可用「Free tools included」 |
| slug | 常青 URL，**不含年份** |
| 韩文博客 | 路径可为 `/ko/blog/{slug}`；title/description **韩语撰写**，非英译 |
| ThetaWave 提及 | 主题相关时在 description 轻提；避免硬广 |

**新博客文章 Fallback**：从文章 H1 提炼 title；description 写「读完能做什么」+ 1 个主关键词。

---

## Knowledge Hub `/knowledge-hub/{slug}?id={id}`

**定位**：开放教材 / 学习资源条目页（200+ 动态 URL）。URL 含 `?id=` 参数；**title 用资源/书名，不用 id**。

**Title 模式（二选一）**：

```
{Resource Title}: AI Study Notes and Summaries | Thetawave
{Resource Title}: Read and Turn into Flashcards with AI | Thetawave
```

| 页类型 | Description 要点 |
|--------|------------------|
| 教材 / 教科书 | 章节笔记、flashcards、quiz；open textbook |
| 学科导读 | 核心概念、复习路径 |
| 聚合 `/knowledge-hub` | free textbooks, study resources, AI notes |

**示例**（slug: `an-introduction-to-philosophy`）：

- Title: `An Introduction to Philosophy: AI Study Notes and Summaries | Thetawave`
- Description: `Turn this open textbook into structured notes, flashcards, and practice quizzes for faster review. Free to try.`

**规则**：
- Title 保留书名可读性（勿全小写 slug）
- 字符过长时缩短后半句，保留书名
- 不与 `/study/*` 或 `/feature/*` 抢同一 P1；KH 页 P1 = **书名 + study notes**

---

## 多语言 metadata（适用于任意页面类型）

**所有索引页类型**（feature / use-case / study / blog / comparison / knowledge-hub / 聚合 / 首页）均可能有 10 个 locale 版本。

### 执行步骤

1. **剥离 locale**：`/ko/study/education-notes` → 基准 path `/study/education-notes`，locale = `ko`
2. **识别页面类型**：用 §页面类型路由
3. **套用同类型 title 结构**（冒号 / em dash / editorial），**非英译英文 title**
4. **使用该 locale 的 P1 检索词**（下表 + 页面语境）
5. **按 CJK 长度表**控制字符；超长则缩短动作句，保留 P1

| locale | 代码 | 通用 P1 示例 |
|--------|------|--------------|
| 英文 | en（无前缀） | 本文各表默认 |
| 德语 | de | KI Notizen, Vorlesung transkribieren, Lernnotizen |
| 西语 | es | notas IA, resumir PDF, apuntes de universidad |
| 法语 | fr | notes IA, résumé PDF, prise de notes |
| 意大利语 | it | appunti IA, riassunto PDF |
| 葡萄牙语 | pt | notas IA, resumir PDF |
| 日语 | ja | AI ノート, 要約, 講義 文字起こし |
| 韩语 | ko | AI 노트, 요약, 강의 녹취 |
| 简体中文 | zh | AI 笔记, 总结, 讲座转笔记 |
| 繁体中文 | zh-tw | AI 筆記, 摘要, 講座轉筆記 |

**多语 title 示例**：

| 基准 URL | en | zh |
|----------|----|----|
| /feature/youtube-to-notes | `YouTube to Notes: Convert YouTube Video into Notes with AI \| Thetawave` | `YouTube 转笔记：AI 将 YouTube 视频转为学习笔记 \| Thetawave` |
| /study/education-notes | `Education Notes: Turn Pedagogy Lectures into Structured Study Notes with AI \| Thetawave` | `教育学笔记：AI 将教学法课程转为结构化学习笔记 \| Thetawave` |
| /study/exam-review | `Exam Review Video Notes: Convert Review Videos into Quiz-Ready Notes with AI \| Thetawave` | `考试复习视频笔记：AI 将复习视频转为可自测的结构化笔记 \| Thetawave` |
| /use-case/for-law-students | `AI Note Taker for Law Students: Turn Lectures into Case Briefs with AI \| Thetawave` | `法学生 AI 笔记：将法学讲座转为判例摘要 \| Thetawave` |

**禁止**：把 en title 直译后截断；简繁混用；同一 URL 各语种 description 完全复制粘贴仅换语言标签。

---

## Cannibalization（站内竞争）

| 层级 | 规则 |
|------|------|
| **P1** | 类目词可跨页出现，但每页 P1 **侧重不同输入/输出** |
| **P2/P3** | **每页唯一**——YouTube chapters → 仅 youtube-to-notes；spaced repetition → 仅 flashcard-maker；mock exam pacing → 仅 quiz-maker |
| **Features vs Use Cases vs Study** | Feature = 输入→输出能力；Use Case = persona；Study = 学科/主题学习 hub |
| **Study vs Use Case** | Study 用 `{Subject} Notes`；Use Case 用 `for {persona}`；同学科两页 P2 须不同 |
| **首页 vs notes-generator** | 首页 = capture / AI note taker；notes-generator = generate / AI notes generator |
| **lecture vs youtube vs pdf** | 各输入页独占各自动词与 P2，互不复制 |
| **Knowledge Hub vs Study** | KH = 单本书/资源名；Study = 学科聚合与 workflow |

---

## 任意页面 Fallback（URL 不在清单时）

1. **解析 URL**：剥离 locale → 得基准 path
2. **若可访问页面**：读 `<h1>`、首段文案、面包屑 — **先提炼页面主题与目标关键词，再写 metadata**
3. **推断类型**：用 §页面类型路由
4. **P1/P2 从页面来**：H1 → P1；首屏 bullet/section 标题 → P2；**不可先用泛化模板再硬套**
5. **选 title 结构**：产品页 → 冒号+动作（动作句须含该页材料/输出词）；内容页 → editorial
6. **Description** = 该页独有场景 + P2 + CTA
7. **Theme-keyword self-check** — §核心原则 三条自检
8. **Cannibalization**：与同站相近 path 不重复 P2

**slug 人话化示例**：`exam-review` → 主题 `Exam review videos`，P1 `exam review video notes`，P2 `chemistry/calc/MCAT/AP playlists`

---

## Best Practices

| Item | Guideline |
|------|-----------|
| **Theme-keyword fit** | **最高优先级**：title/description 与该 URL 的 P1/P2 及页面主题强相关；见 §核心原则 |
| Front-load | 该页 P1 + 主题词在 title 最前 |
| Query mirror | 功能页冒号后 = 该页用户搜索动作句（含该页输入/输出词） |
| Unique | 全站无 duplicate title/description |
| H1 alignment | Title 与 H1 **同主题**；H1 可更短 |
| Title ≠ Description | 不整句重复；**title 用 Generator 等名词，description 用 generate notes from / notes generation 等变体** |
| CTA | Description 末尾：`Free to try.` |
| Keyword variants | 同一页 title/description 覆盖同一关键词簇的 **名词 + 动词/动名词** 变体；见 §Title/Description 关键词变体分工 |
| Keyword stuffing | 该页主词及变体各约 1 次；不堆无关同义词 |
| YouTube | 品牌写法 `YouTube` |
| 字符超限 | 优先缩短品牌或动作句；**不可删掉主题词** |

---

## Workflow（Agent 逐步执行）

1. **Parse URL** — 剥离 `/{locale}/`，得基准 path + locale
2. **Route page type** — §页面类型路由
3. **Identify page theme** — 从清单取 P1/P2；或读该页 H1/首屏/面包屑确定 **主题词**（Fallback 页必做）
4. **Lookup P1/P2** — 查对应章节清单；**禁止**用其他页的 P1/P2 顶替
5. **Pick title pattern** — 功能/Study/Use Case/对比 = 冒号+动作；首页 = em dash；博客/KH = editorial
6. **Draft title** — **必须含该页 P1 + 主题词**；计字符
7. **Draft description** — **必须含该页 P2 + 专属场景**；不与 title 重复
8. **Theme-keyword self-check** — 回答 §核心原则 三条自检问句；不通过则重写
9. **Locale check** — 非 en 则同主题、当地检索词独立撰写
10. **Cannibalization + Claims check**
11. **Output** — §Output Format（含 Page theme 字段）

---

## Output Format

```markdown
### {Page name} — `{URL}`

**Page theme**: {one-line page topic, e.g. "Education majors — pedagogy notes & certification prep"}

**Primary keyword (P1)**: {this page only}

**Secondary keyword (P2)**: {this page only — for description}

**Recommended title** ({n} chars)
> {title text}

**Recommended meta description** ({n} chars)
> {description text}

**Theme-keyword fit**: {1 sentence — why title/desc match this page's topic}

**Alternatives**（可选）
- Title B: …
- Description B: …

**H1 alignment**: {suggested H1}
**Notes**: {cannibalization / locale / 特殊说明}
```

**批量任务**：输出 Markdown 表格，列：URL | Title | Description | Chars

---

## Templates（复制即用）

### Feature page

```
Title: {P1 / {Topic} Notes Generator}: {Verb} {Input} into {Output} with AI | Thetawave
Description: {Generate notes from … / Notes generation from … — P1 variant}. {P2}. Free to try.
```

### Use case

```
Title: AI Note Taker for {Persona}: Turn {Material} into {Output} with AI | Thetawave
Description: {Pain clause}. Notes, flashcards, and quizzes for {context}. Free to try.
```

### Comparison

```
Title: ThetaWave vs {Competitor}: {Differentiator} for Students | Thetawave
Description: {One-line verdict}. Live lecture capture, multi-format outputs, built for students. Free to try.
```

### Study subject page

```
Title: {Subject} Notes: Turn {Material} into Study Notes with AI | Thetawave
Description: Generate notes from {material sources — P1 variant}. {Cert/exam or topic map P2}. Free to try.
```

### Study topic / workflow page

```
Title: {Topic Title}: {Verb} {Source} into {Output} with AI | Thetawave
Description: {Workflow P2—video types, outputs, linked features}. Free to try.
```

### Knowledge Hub entry

```
Title: {Book Title}: AI Study Notes and Summaries | Thetawave
Description: Turn this open resource into notes, flashcards, and quizzes. Free to try.
```

### Blog

```
title: "Best {Topic} in {Year}: {Angle}"
description: "{What reader learns}. Compare tools, pricing, and common mistakes."
```

---

## GSC 优化（可选）

1. Google Search Console → 高展示、低 CTR 页面
2. 优先改 title/description（通常改 title）
3. 改后 2–4 周再看 CTR；避免频繁改动

---

## 版本与维护

| 字段 | 值 |
|------|-----|
| version | 2.2.1 |
| last-updated | 2026-06-15 |
| site | thetawave.ai |
| covers | homepage, feature×16, use-case×19, study×14+, comparison×12, blog×9+, knowledge-hub×200+, legal×2, all locales |
| core-rule | **Every title & description must strongly match that page's keywords and theme** |

更新 proof points、新增 slug 或竞品对比页时，同步修改本文 §产品上下文 与对应清单表。

**外部参考（可选，非必读）**：

- [Google: Build a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [title-tag skill](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/on-page/title/SKILL.md)
- [meta-description skill](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/on-page/description/SKILL.md)
