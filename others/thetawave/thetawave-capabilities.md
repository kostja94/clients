# ThetaWave Capabilities — 能力库

> 从各产品详情页 Why Choose 区块抽取、去重后的**能力清单**。按能力本体组织，不绑定具体页面；生成文案时按主题挑选相关条目，可将「文案钩子」改写为页面标题。  
> **关联**：[thetawave-features.md](./thetawave-features.md)  
> **数据来源**：2026-07-28 · `thetawave.lovable.app` 功能详情页 Why Choose  
> **用法**：优先用「能力名」理解与组合；「文案钩子」仅供标题灵感；可变数字与合规主张见文末「可核验主张」。

**Last updated**: 2026-07-28

---

## 字段说明

| 列 | 含义 |
|----|------|
| ID | 稳定引用键，文案/配置中引用此 ID |
| 能力名 | 中性动词短语：系统**能做什么** |
| 说明 | 能力边界与行为，不含营销口号 |
| 文案钩子 | 可选标题灵感；可改写，勿与能力名混用 |

近义条目勿在同一 Why Choose 区块同时选用，见附录「忌同屏近义」。

---

## A · 输入与摄取

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-input-unified | 多源统一入口 | 教材、讲座录音、YouTube、幻灯片、语音备忘录等进入同一入口，产出结构一致。 | One Inbox for Every Source |
| cap-input-live-or-upload | 实时录制或事后上传 | 课上实时录音，或事后上传常见音视频格式；两种路径产出同类结构化结果。 | Record Live or Upload Later |
| cap-input-messy-audio | 嘈杂课堂音频适配 | 应对重叠人声、背景噪音、口音与长课时录音，不要求录音环境完美。 | Built for Messy Classroom Audio |
| cap-input-longform | 超长内容完整处理 | 支持多小时课程、长播客等，不截断；保留章节结构与时间戳。 | Built for Full-Length Content |
| cap-input-pdf-normalize | 杂乱 PDF 结构化 | 教材章节、论文、扫描讲义、幻灯片等整理为可导航大纲/笔记，无需手动复制粘贴。 | From PDF Chaos to a Clean Outline |

---

## B · 理解与结构化

含笔记理解、STEM 格式、多源合成。

### B1 · 笔记结构

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-note-academic-structure | 学术体例结构化 | 按标题层级、要点论证、定义标注、公式与对比表组织，而非无结构段落堆砌。 | Structure a Professor Would Recognize |
| cap-note-outline-not-transcript | 大纲式改写 | 将源内容改写为标题、核心概念与章节摘要，而非带时间戳的转录墙。 | Outline, Not Transcript |
| cap-note-extract-arguments | 抽取可考论点 | 识别定义、定理、方法、发现与结论等考查重点，而非逐字摘抄。 | Extracts Arguments, Not Just Text |
| cap-note-source-aware | 基于源材料生成 | 层级、案例与数据来自实际上传材料，非套用通用模板库。 | Source-Aware, Not Template-Filled |

### B2 · STEM 与学术格式

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-stem-latex | 口说/文本转规范 LaTeX | 积分、矩阵、化学方程式等转为可用的 LaTeX，便于 STEM 复习与导出。 | LaTeX-Perfect Math and Chemistry |
| cap-stem-formulas-intact | 公式与表格保真 | LaTeX 公式、化学结构式、数据表保留排版，不被压成普通段落。 | Formulas and Tables Stay Intact |

### B3 · 多源合成

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-synth-multi-source | 多源合成统一产物 | 同一主题下多个 PDF/讲座等合成一份跨文献笔记，或统一概念图，用于综述与论文规划。 | Merge Dozens of PDFs Into One Note |
| cap-synth-cross-chapter | 跨章节概念关联 | 识别不同章节概念并连线，形成网状关联而非仅树状目录，便于综合论述。 | Cross-Chapter Links, Not Just Trees |

---

## C · 学习产出

按产出形态分列；「任意来源 → 某产出」由 A 节输入能力覆盖，此处不再重复。

### C1 · 闪卡（主动回忆）

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-flashcard-auto-format | 按概念选型制卡 | 术语/定义、问答、填空、cloze 等，按概念类型自动选择卡片样式。 | Right Card Format for Each Concept |
| cap-flashcard-spaced-rep | 间隔重复调度 | 内置间隔重复（如 SM-2）；可导出至 Anki 等，保留格式与标签（以产品实际支持为准）。 | Spaced Repetition, Built In |
| cap-flashcard-editable | 生成后可编辑 | 可改文案、加图片/提示/记忆法，或调整顺序。 | Cards You Can Actually Edit |
| cap-flashcard-bulk-speed | 批量快速制卡 | 从讲座/笔记等批量生成复习卡，显著缩短手工制卡时间。 | 50 Cards a Minute, Not an Afternoon |

### C2 · 自测与考试

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-quiz-auto-format | 按知识点选题型 | 选择、简答、判断、填空等，按知识点选择题型，而非一律选择题。 | Four Question Formats, Auto-Picked |
| cap-quiz-bloom-level | 认知层次难度可调 | 难度可从记忆到应用、分析等调节，对齐期中/执照等考查层次。 | Bloom-Aligned Difficulty Control |
| cap-quiz-explanations | 逐题解析并溯源 | 说明正误原因，并引用源材料对应段落。 | Explanations for Every Answer |
| cap-quiz-exam-simulation | 仿真考试模式 | 限时、锁定导航、分节等，模拟真实考试压力。 | Real Exam Simulation Mode |
| cap-quiz-weak-topics | 薄弱点诊断 | 作答映射到概念，指向应回顾的章节或闪卡组。 | Weak-Topic Diagnostics |

### C3 · 思维导图

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-mindmap-auto-hierarchy | 自动构建层级导图 | 识别中心主题、主/子分支，无需空白画布手工拖框。 | Auto-Built Central Hierarchy |
| cap-mindmap-drill-down | 交互下钻 | 缩放、展开/折叠；可下钻至原笔记句子等粒度。 | Zoom, Expand and Collapse |

### C4 · 播客 / 音频

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-podcast-dialogue | 双主持人对话脚本 | 对话式脚本含过渡与呼应，非单调 TTS 朗读。 | Two-Host Conversation, Not TTS |
| cap-podcast-length | 篇幅可选 | 按可用时间选择短速览或较长深度版。 | Pick Your Episode Length |
| cap-podcast-offline | 离线可听 | 下载常见音频格式，无网环境可听。 | Offline-Ready on Any Device |

### C5 · 信息图

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-infographic-auto-layout | 按内容选视觉结构 | 时间线、流程、对比、数据摘要等，按内容选型而非单一模板。 | Right Layout for the Content |
| cap-infographic-numbers | 数字可视化 | 统计、百分比、趋势转为图表、标注与并排对比。 | Numbers Become Visuals |
| cap-infographic-one-pager | 单页复习摘要 | 整章压缩为单页可扫视视觉摘要，便于打印或贴墙。 | One-Page Revision Poster |

---

## D · 横切能力

语言、一源多格式、导出、隐私与溯源。

| ID | 能力名 | 说明 | 文案钩子 |
|----|--------|------|----------|
| cap-pipeline-one-to-many | 一源多学习格式 | 同一来源一次生成笔记、闪卡、测验、导图、音频摘要等，无需工具间复制粘贴。 | One Source, Multiple Study Formats |
| cap-lang-cross-lingual | 跨语言学习产出 | 源语言与产出语言可不同；生成另一语言的笔记或音频，术语需保持准确。 | Study in a Language the Source Isn't In |
| cap-lang-native-narration | 母语音频讲解 | 在跨语言场景下，将笔记内容生成学习者母语播客/讲解音频。 | Native-Language Audio |
| cap-export-no-lockin | 开放格式导出 | 导出 Markdown、可打印 PDF，或同步至常见笔记工具；数据不锁死在 App。 | Yours to Keep, Anywhere You Write |
| cap-export-visual-share | 视觉产物导出分享 | 导图、信息图等导出高分辨率图或可打印 PDF，便于分享或插入幻灯片。 | PNG or PDF, Ready to Share |
| cap-trust-privacy | 隐私与安全基建 | 企业级安全实践（如 SOC 2）、传输/存储加密等，保护用户学习材料。 | Private by Design |
| cap-trust-source-citation | 产出可溯源至原文 | 笔记、解析等可指向源材料具体位置，便于核对与复习。 | Exam-Grade Accurate, Source-Cited |
| cap-learn-dual-channel | 读写+听力双通道复习 | 同一内容可同时以文字与音频形态复习，支持多通道巩固。 | Multi-Modal Memory Boost |

---

## 附录 A · 选能力示例

展示「按页面主题从库中挑选」；其他页面不必照搬。

### 示例 1 · Lecture to Notes

| 选用 ID | 能力名 |
|---------|--------|
| cap-input-live-or-upload | 实时录制或事后上传 |
| cap-input-messy-audio | 嘈杂课堂音频适配 |
| cap-stem-latex | 口说/文本转规范 LaTeX |
| cap-note-outline-not-transcript | 大纲式改写 |
| cap-pipeline-one-to-many | 一源多学习格式 |

### 示例 2 · PDF to Notes

| 选用 ID | 能力名 |
|---------|--------|
| cap-input-pdf-normalize | 杂乱 PDF 结构化 |
| cap-note-extract-arguments | 抽取可考论点 |
| cap-note-source-aware | 基于源材料生成 |
| cap-synth-multi-source | 多源合成统一产物 |
| cap-export-no-lockin | 开放格式导出 |

### 示例 3 · Quiz / Exam

| 选用 ID | 能力名 |
|---------|--------|
| cap-quiz-auto-format | 按知识点选题型 |
| cap-quiz-bloom-level | 认知层次难度可调 |
| cap-quiz-explanations | 逐题解析并溯源 |
| cap-quiz-exam-simulation | 仿真考试模式 |
| cap-quiz-weak-topics | 薄弱点诊断 |

### 示例 4 · Podcast Generator

| 选用 ID | 能力名 |
|---------|--------|
| cap-podcast-dialogue | 双主持人对话脚本 |
| cap-podcast-length | 篇幅可选 |
| cap-podcast-offline | 离线可听 |
| cap-lang-cross-lingual | 跨语言学习产出 |
| cap-learn-dual-channel | 读写+听力双通道复习 |

---

## 附录 B · 忌同屏近义

同一 Why Choose（或同类卖点区）避免同时选用下列组合，择一即可。

| 组 | 近义 ID | 建议 |
|----|---------|------|
| 笔记改写重心 | `cap-note-outline-not-transcript` ↔ `cap-note-extract-arguments` | 强调「非转录墙」用前者；强调「考点抽取」用后者 |
| 学术体例 vs 大纲 | `cap-note-academic-structure` ↔ `cap-note-outline-not-transcript` | 体例/格式感用前者；「不是逐字稿」用后者 |
| 跨语言 | `cap-lang-cross-lingual` ↔ `cap-lang-native-narration` | 通用跨语言用前者；仅播客母语讲解用后者（可与前者同页仅当页面主打音频） |
| 一源多格式 | `cap-pipeline-one-to-many` 已覆盖「笔记→闪卡/测验」叙事 | 勿再单开已删除的「笔记变回忆练习」类重复条目 |
| 隐私 vs 溯源 | `cap-trust-privacy` ↔ `cap-trust-source-citation` | 可同页，但分两条写清；勿再合成一条模糊「又私密又准」 |
| 双通道记忆 | `cap-learn-dual-channel` | 属学习方式主张；播客页可用，勿写成医疗/ADHD 疗效承诺 |

---

## 附录 C · 可核验主张（易变，写文案前请核对产品）

以下数字与合规表述**不写入能力正文**；对外使用前以官网/合规文档为准。

| 主题 | 历史文案中出现过的主张 | 备注 |
|------|------------------------|------|
| 转录质量 | 准确率 95%+ | 易变；注明条件或改为定性「嘈杂环境可用」 |
| 语言数 | 50+ 语言 | 与 features 文档曾记录的「10」等存在漂移风险，务必现核 |
| 制卡速度 | 约 60 分钟讲座 → 数分钟内 50–100 张卡 | 作量级示例，勿写成 SLA |
| 安全合规 | SOC 2、端到端加密 | 以实际认证范围与实现为准 |
| Anki 导出 | 曾出现「导出至 Anki」 | features 侧曾有「Anki 导出移除」记录；写前确认是否仍支持 |
| 学习者群体效果 | ADHD 等特定人群 retention 更高 | 能力库不保留疗效式表述；对外需有依据再写 |

---

## 附录 D · ID 变更对照（相对旧版）

| 旧 ID | 处理 |
|-------|------|
| `cap-note-professor-grade` | → `cap-note-academic-structure` |
| `cap-pipeline-recall-drills` | 并入 `cap-pipeline-one-to-many`（删除） |
| `cap-flashcard-any-source` | 由 A 节输入能力覆盖（删除） |
| `cap-synth-multi-pdf` / `cap-synth-multi-source-map` | → `cap-synth-multi-source` |
| `cap-trust-private-accurate` | 拆为 `cap-trust-privacy` + `cap-trust-source-citation` |
| `cap-podcast-dual-coding` | → `cap-learn-dual-channel`（去掉疗效式措辞） |
