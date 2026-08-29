# ThetaWave Use Cases — By Exam（考试分类）

> **维度定义**：按「为哪个考试而学」分类——覆盖标准化考试和高 stakes 证书的专项备考需求。与 By Subject（学什么专业）和 By Stage/Exam Prep（通用考试方法论）互补，聚焦具体考试的题型、时间压力和评分逻辑。
> **关联**：[by-subject.md](./by-subject.md) | [by-identity.md](./by-identity.md) | [by-stage.md](./by-stage.md) | [../thetawave-use-cases.md](../thetawave-use-cases.md) | [../thetawave-features.md](../thetawave-features.md) | [../keywords/thetawave-keywords.md](../keywords/thetawave-keywords.md)
> **URL 模式**：`https://thetawave.ai/use-case/{exam}-prep`
> **更新**：2026-05-12 — 首版：6 个考试节点完整化（痛点+能力+Proof+竞品+关键词+内链）+ vs ChatGPT/NotebookLM + 内容缺口分析 + 内容营销建议 + 实施优先级矩阵

---

## 一、By Exam 页面全览

| 优先级 | 页面 | URL | 状态 | 关联学科页 |
|--------|------|-----|------|-----------|
| **P0** | MCAT Prep | /use-case/mcat-prep | ❌ 待建 | /use-case/for-pre-med-students |
| **P0** | NCLEX Prep | /use-case/nclex-prep | ❌ 待建 | /use-case/for-nursing-students |
| **P1** | LSAT Prep | /use-case/lsat-prep | ❌ 待建 | /use-case/for-law-students |
| **P1** | USMLE Prep | /use-case/usmle-prep | ❌ 待建 | /use-case/for-pre-med-students |
| **P2** | Bar Exam Prep | /use-case/bar-exam-prep | ❌ 待建 | /use-case/for-law-students |
| **P2** | GRE Prep | /use-case/gre-prep | ❌ 待建 | /use-case/for-graduate-students |

> **维度边界**：By Exam ≠ By Subject。Pre-Med 学生（身份）同时应对课程考试和 MCAT，两类需求不同——课程考试聚焦该学科的知识结构，MCAT 聚焦跨学科整合+考试策略。By Exam ≠ Exam Prep（By Stage）。Exam Prep 是通用考试方法论（闪卡/间隔重复/模拟测试），By Exam 是具体考试的专项策略（NCLEX 全选题 vs LSAT 逻辑推理 vs MCAT 阅读理解）。

---

## 二、各考试页详情

### 2.1 MCAT Prep — P0

**URL**: /use-case/mcat-prep

**痛点**：MCAT 覆盖 4 大板块（Bio/Biochem、Chem/Physics、Psych/Soc、CARS）跨学科整合难度极高；阅读理解（CARS）需要特殊策略——非知识型考查，而是推理+速度；每道题约 95 秒，时间压力巨大；备考周期通常 3-6 个月，需要跨月度的知识积累和进度追踪。

**ThetaWave 能力**：
- 4 板块知识库统一归档：MCAT 覆盖的生物/化学/物理/心理/社会学科材料→统一笔记，按 AAMC 大纲自动分类
- CARS 专项：上传阅读材料→自动提取论点/论据/作者语气/推理链条，生成 CARS 风格练习题
- Formula & Pathway 闪卡：有机化学反应、代谢路径、物理公式→自动生成间隔重复闪卡
- 全真模拟：Quiz Maker 生成 MCAT 风格 passage-based 选择题，含计时模式
- Podcast Generator：通勤/健身时听板块复习播客
- 进度仪表盘：按 AAMC 内容类别追踪掌握度

**Proof**：年 85,000+ MCAT 考生；AAMC 官方数据：备考时间中位数 300 小时；TheataWave Pre-Med 用户已覆盖 Harvard/Stanford/Johns Hopkins

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无 MCAT-specific 题型生成；无法按 AAMC 大纲组织内容；无进度追踪
- vs NotebookLM：免费但无 CARS 专项训练；无考试计时模拟；无跨板块知识整合

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| King of the Curve | 5,000+ MCAT 题+AI 导师+预测评分 | 偏题目练习；ThetaWave 有讲座→笔记→闪卡→测验全链路 |
| Lecturio | MCAT 专项定价（$24.99–$34.99/mo）；8,050+ 视频 | 偏视频课程；ThetaWave 锚定自有课程材料（实时讲座捕获） |
| StudyFetch | 考试专项（MCAT passage-based 题）+Spark.E AI 导师 | 功能重叠但 ThetaWave 有中文版+双语输出 |
| Achievable | MCAT 课程一次性购买 ~$129 | 偏课程内容交付；ThetaWave 是工具平台 |
| Educato | 全考试选择器，AI 每日学习计划 | 泛考试工具；ThetaWave 有学科深度 |

**关键词**: MCAT prep AI, MCAT study notes AI, MCAT CARS practice AI, MCAT flashcards generator, MCAT podcast review, AAMC study guide AI

**长尾机会**: "MCAT biology notes generator", "MCAT psych-soc flashcards AI", "CARS passage to notes", "MCAT formula sheet generator", "MCAT 3-month study plan AI"

**内链** → /use-case/for-pre-med-students、/flashcard-maker、/quiz-maker、/podcast-generator、/notes-generator、/mind-map-maker

---

### 2.2 NCLEX Prep — P0

**URL**: /use-case/nclex-prep

**痛点**：NCLEX 使用 CAT（计算机自适应测试）——题目难度随答题表现动态调整，75-145 题不等；题型复杂：多选题（SATA/全选题）、排序题、图表题、计算题、音频题——远超传统的 ABCD 选择题；药理计算和药物相互作用是高频失分点；护理学生同时应对课程考试（知识型）和 NCLEX（应用/分析型），两种考试逻辑完全不同；Next Gen NCLEX（2023 改革后）增加了案例研究和临床判断题型。

**ThetaWave 能力**：
- NCLEX 专项题型生成：Quiz Maker 支持 SATA（全选题）、优先级排序、授权决策、药理计算——完全对齐 NCLEX 题型
- Drug Cards 自动生成：从药理/药物治疗学讲座→自动提取药名/分类/机制/副作用/护理要点/患者教育→导出为 NCLEX 复习闪卡
- Clinical Judgment 笔记：案例研究材料→结构化笔记，按 NCSBN Clinical Judgment Measurement Model（识别线索→分析线索→优先级假设→生成解决方案→采取行动→评估结果）
- 跨学科知识库：Med-Surg / Pediatrics / Maternity / Psych / Pharmacology 统一归档，按 NCLEX 客户需求类别（Client Needs Categories）索引
- Podcast Generator：临床实习通勤时听 NCLEX 重点复习

**Proof**：年 175,000+ NCLEX 考生；NCSBN 数据：首次通过率 ~80%（RN）、~82%（PN）；ThetaWave 护理学生已覆盖 Johns Hopkins/Duke/UPenn；每学期平均生成 150+ 药物闪卡

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无 NCLEX 特定题型（SATA/排序/图表）；无法模拟 CAT 逻辑
- vs NotebookLM：免费但无护理专项题型；无 Drug Cards 自动生成

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Nursify | Notes/Calendar/Clinical/Tutor + NCLEX 题 | 护理专用，功能重叠；ThetaWave 有跨学科统一知识库 |
| Repeatica | 讲座转录+闪卡+NCLEX 题 | 功能较基础；ThetaWave 有 Drug Cards+Next Gen NCLEX 题型 |
| Feynman Nurse | Feynman 模式/NCLEX/150+ 药卡 | 偏学习方法；ThetaWave 有实时讲座捕获 |
| Lecturio | Nursing Plan $19.99–$24.99/mo + NCLEX Qbank | 偏视频课程；ThetaWave 锚定自有课程材料 |
| UWorld NCLEX | 2,000+ NCLEX 题+详细解析（行业黄金标准） | 题目库之王但无 AI 笔记/闪卡生成；ThetaWave 定位为补充而非替代 |

**关键词**: NCLEX prep AI, NCLEX study notes AI, NCLEX drug cards generator, Next Gen NCLEX AI, NCLEX SATA practice AI, nursing board exam AI

**长尾机会**: "NCLEX pharmacology study guide AI", "Next Gen NCLEX case study notes", "NCLEX clinical judgment model AI", "NCLEX 75 questions study plan", "NCLEX lab values flashcards AI"

**内链** → /use-case/for-nursing-students、/flashcard-maker、/quiz-maker、/podcast-generator、/notes-generator、/mind-map-maker

---

### 2.3 LSAT Prep — P1

**URL**: /use-case/lsat-prep

**痛点**：LSAT 不考知识——考逻辑推理和分析能力，传统「记笔记→复习」模式不适用；Logical Reasoning（LR）占 50% 分值，需要识别论证结构（前提/结论/假设/加强/削弱）；Reading Comprehension（RC）类似 MCAT CARS，但文体偏法律/人文/社科；Logic Games（LG/AR）将在 2024 年后逐步取消，考试结构正在变化；高分（170+）竞争极度激烈——Top 14 法学院中位数 170+。

**ThetaWave 能力**：
- LR 题型分类笔记：讲座/练习材料→自动按题型归类（Must Be True / Strengthen / Weaken / Flaw / Assumption / Parallel Reasoning）
- 论证结构提取：上传 LSAT 文章→自动标注 Premise / Conclusion / Assumption / Counterargument
- RC Passage → 结构化摘要：自动提取论点链、作者态度、段落功能
- Flashcard Maker：LR 题型识别卡（看到 "depends on which assumption" → Assumption 题）
- Quiz Maker：LR/RC 专项练习题，含计时和难度递进
- Podcast Generator：听 LR 题型策略和常见逻辑谬误讲解

**Proof**：年 120,000+ LSAT 考生；LSAC 数据：170+ 为 97.5 百分位；ThetaWave 法学学生已覆盖 T14 法学院

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无 LSAT 专项题型；无法生成 LR 题型分类训练
- vs NotebookLM：免费但无 LSAT 题型识别；无逻辑论证结构提取

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| AdeptLR | LSAT 专项 AI 自适应训练（LawHub 集成） | 偏题目练习；ThetaWave 有讲座→笔记→闪卡全链路 |
| 7Sage | LSAT 课程+视频解析+论坛 | 偏课程+社区；ThetaWave 偏工具 |
| LSAT Demon | AI 推荐题目+每日训练 | 偏题目；ThetaWave 有自有材料整理能力 |
| StudyFetch | LSAT 考试专项（logical reasoning 题型） | 功能部分重叠但 ThetaWave 有 LR 题型分类+论证结构提取 |

**关键词**: LSAT prep AI, LSAT logical reasoning AI, LSAT study notes AI, LSAT RC passage notes, LSAT argument analysis AI, LSAT flashcard generator

**长尾机会**: "LSAT logical reasoning question type notes", "LSAT reading comprehension passage to notes", "LSAT argument structure AI", "LSAT 170 study plan AI", "LSAT flaw question practice AI"

**内链** → /use-case/for-law-students、/quiz-maker、/flashcard-maker、/notes-generator、/podcast-generator

---

### 2.4 USMLE Prep — P1

**URL**: /use-case/usmle-prep

**痛点**：USMLE Step 1（基础科学）和 Step 2 CK（临床知识）覆盖海量内容；First Aid / UWorld / Pathoma / Sketchy / Anki 多资源并行，笔记极度分散；Step 1 改为 Pass/Fail 后，Step 2 CK 分数权重上升；临床 vignette 题型需要快速识别关键线索和多步骤推理。

**ThetaWave 能力**：
- 多资源统一笔记：First Aid PDF + 讲座录音 + UWorld 错题截图→统一知识库，按系统（Cardio/Neuro/Renal 等）和学科（Path/Pharm/Micro 等）双维度组织
- Clinical Vignette 生成：Quiz Maker 生成 Step 2 CK 风格的临床场景题（患者主诉→体检→实验室→诊断→治疗）
- 快速回顾闪卡：First Aid 知识点→自动提取为间隔重复闪卡（Bug/Drug 卡片、Pathology 卡片）
- Mind Map Maker：疾病-机制-表现-诊断-治疗五维可视化
- Podcast Generator：通勤/值班间隙听系统复习播客

**Proof**：年 50,000+ USMLE 考生；ThetaWave Pre-Med 学生进入医学院后持续使用；Leiden University 2025 实验：AI 辅助考试准备获 8.5/10

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无 USMLE 专项 vignette 生成；无法多资源统一整理
- vs NotebookLM：免费但无临床 vignette 题型；无 USMLE 系统分类

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Lecturio | USMLE 专项定价+8,050+ 视频+Qbank | 偏视频课程；ThetaWave 有自有材料统一整理 |
| UWorld | 3,600+ USMLE Qbank（行业黄金标准） | 题目库之王；ThetaWave 定位为笔记/闪卡补充工具 |
| Amboss | 医学知识库+Qbank 联动 | 偏知识库；ThetaWave 有讲座捕获+多输出链 |
| StudyFetch | USMLE Step 1/2/3 考试专项 | 功能重叠但 ThetaWave 有系统/学科双维度笔记 |

**关键词**: USMLE prep AI, USMLE study notes AI, USMLE Step 2 CK prep AI, USMLE clinical vignette AI, USMLE pharmacology notes, USMLE flashcard generator

**长尾机会**: "USMLE First Aid to flashcards AI", "USMLE Step 2 CK notes generator", "USMLE UWorld review notes AI", "USMLE dedicated period study plan AI", "USMLE bug-drug chart generator"

**内链** → /use-case/for-pre-med-students、/flashcard-maker、/quiz-maker、/mind-map-maker、/podcast-generator、/notes-generator

---

### 2.5 Bar Exam Prep — P2

**URL**: /use-case/bar-exam-prep

**痛点**：Bar Exam 覆盖 12+ 法律科目（MBE 7 科 + MEE 科目），2 个月内高强度复习；MBE 200 道题在 6 小时内完成，速度+耐力双重挑战；MEE（论文）和 MPT（实务任务）需要写作能力而非选择题技巧；Barbri/Themis/Kaplan 课程昂贵（$2,000-$4,000），学生寻求 AI 工具作为补充。

**ThetaWave 能力**：
- MBE 科目笔记统一归档：Con Law / Contracts / Criminal Law / Evidence / Torts / Property / Civil Procedure →按 MBE 大纲和 IRAC 框架自动整理
- MEE 写作助手：历年真题→提取考点模式→生成结构化答题模板
- MPT 任务分析：从任务材料中提取关键事实+法律依据+任务要求
- Flashcard Maker：MBE 高频考点（Con Law tests / Evidence rules / Property rules against perpetuities）
- Quiz Maker：MBE 风格单选题，含计时+难度递进

**Proof**：年 65,000+ Bar Exam 考生；NCBE 数据：首次通过率 ~78%（全国平均）；ThetaWave 法学学生已覆盖 T14 法学院

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无 IRAC 结构输出；无 MBE 科目分类
- vs NotebookLM：免费但无 Bar Exam 题型；无 MPT 任务分析

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Barbri/Kaplan/Themis | 综合备考课程（$2,000-$4,000） | 偏课程；ThetaWave 为 AI 辅助工具补充 |
| StudyFetch | Bar Exam（MBE/MEE/MPT）考试专项 | 功能部分重叠但 ThetaWave 有 IRAC 结构化笔记 |

**关键词**: bar exam prep AI, MBE study notes AI, MEE writing AI, bar exam flashcard generator, MPRE prep AI, UBE study tool AI

**长尾机会**: "MBE constitutional law notes AI", "MEE essay template generator", "bar exam 8-week study plan AI", "UBE MBE practice question generator", "MPT task memo AI"

**内链** → /use-case/for-law-students、/flashcard-maker、/quiz-maker、/notes-generator

---

### 2.6 GRE Prep — P2

**URL**: /use-case/gre-prep

**痛点**：GRE 词汇量要求高（3,000-5,000 学术词汇），传统单词书效率低；Verbal Reasoning 需要复杂文本的快速理解+推理；Quantitative Reasoning 覆盖高中至大学低年级数学，但对于非 STEM 背景学生仍需系统复习；Analytical Writing（Issue + Argument）需要写作模板和论证结构。

**ThetaWave 能力**：
- 词汇闪卡自动生成：学术词汇列表→自动生成 GRE 词汇闪卡（定义+例句+同反义词+词根）
- RC Passage → 结构化摘要：自动提取论点链+作者态度+推理线索
- 数学公式卡：Quant 公式自动生成（几何/代数/数据分析/概率）
- AWA 模板：Issue Essay 和 Argument Essay 从大纲→模板→范文
- Mind Map Maker：按主题分类词汇（政策/科学/艺术/哲学/历史）
- Podcast Generator：听词汇复习+RC 策略讲解

**Proof**：年 500,000+ GRE 考生；ETS 数据：Verbal 中位数 ~151，Quant 中位数 ~155

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Magoosh | GRE 课程+词汇 App+题库 | 偏课程；ThetaWave 有自有材料→闪卡/播客生成 |
| Greg Mat | GRE 课程+社区（月付 $5-10） | 性价比之王；ThetaWave 偏工具 |
| Achievable | GRE 课程一次性购买 ~$129 | 偏课程；ThetaWave 偏工具 |

**关键词**: GRE prep AI, GRE vocabulary flashcards AI, GRE verbal reasoning AI, GRE quant notes generator, GRE AWA essay AI, GRE study notes AI

**长尾机会**: "GRE vocabulary builder AI", "GRE math formula to flashcards", "GRE reading comprehension notes AI", "GRE 3-month study plan AI", "GRE argument essay template generator"

**内链** → /use-case/for-graduate-students、/flashcard-maker、/quiz-maker、/notes-generator、/podcast-generator、/mind-map-maker

---

## 三、内链关系图（增强版）

```
/use-case/mcat-prep
  → /use-case/for-pre-med-students（学科身份锚点）
  → /flashcard-maker（跨学科闪卡）
  → /quiz-maker（MCAT 风格 passage-based 题）
  → /podcast-generator（板块复习播客）
  → /notes-generator（AAMC 大纲→结构化笔记）
  → /mind-map-maker（代谢路径/公式网络）

/use-case/nclex-prep
  → /use-case/for-nursing-students（学科身份锚点）
  → /flashcard-maker（Drug Cards + 护理诊断卡）
  → /quiz-maker（NCLEX 全选题/排序/计算/图表）
  → /podcast-generator（临床通勤复习播客）
  → /notes-generator（NCSBN CJMM 框架笔记）
  → /mind-map-maker（疾病-护理-药理关系图）

/use-case/lsat-prep
  → /use-case/for-law-students（学科身份锚点）
  → /quiz-maker（LR/RC 题型分类练习）
  → /flashcard-maker（LR 题型识别卡）
  → /notes-generator（论证结构提取）
  → /podcast-generator（LR 策略音频）

/use-case/usmle-prep
  → /use-case/for-pre-med-students（学科身份锚点）
  → /flashcard-maker（Bug/Drug/Pathology 卡片）
  → /quiz-maker（Clinical Vignette 生成）
  → /mind-map-maker（疾病五维图）
  → /podcast-generator（系统复习播客）
  → /notes-generator（多资源统一笔记）

/use-case/bar-exam-prep
  → /use-case/for-law-students（学科身份锚点）
  → /flashcard-maker（MBE 高频考点）
  → /quiz-maker（MBE 风格单选题）
  → /notes-generator（IRAC 结构化笔记）

/use-case/gre-prep
  → /use-case/for-graduate-students（学科身份锚点）
  → /flashcard-maker（词汇/公式卡）
  → /quiz-maker（Verbal/Quant 练习题）
  → /notes-generator（RC Passage 摘要）
  → /podcast-generator（词汇复习播客）
  → /mind-map-maker（词汇主题分类）
```

---

## 四、By Exam vs 相邻维度边界对照

| 搜索意图 | By Subject 承接 | By Exam 承接 |
|---------|----------------|-------------|
| "pre-med notes AI" | ✅ /use-case/for-pre-med-students | — |
| "MCAT prep AI" | — | ✅ /use-case/mcat-prep |
| "nursing school notes AI" | ✅ /use-case/for-nursing-students | — |
| "NCLEX study notes AI" | — | ✅ /use-case/nclex-prep |
| "law school outline AI" | ✅ /use-case/for-law-students | — |
| "LSAT logical reasoning AI" | — | ✅ /use-case/lsat-prep |

| 搜索意图 | By Stage（Exam Prep）承接 | By Exam 承接 |
|---------|--------------------------|-------------|
| "how to study for exams AI" | ✅ /use-case/exam-prep（通用方法论） | — |
| "MCAT CARS strategy notes" | — | ✅ /use-case/mcat-prep（考试专项策略） |
| "best flashcard app for exams" | ✅ /use-case/exam-prep | — |
| "NCLEX SATA question practice" | — | ✅ /use-case/nclex-prep |

---

## 五、SEO 关键词

| 考试 | 核心关键词（3-5） | 长尾关键词（3-5） | 竞品 vs 机会 |
|------|------------------|-------------------|-------------|
| MCAT | MCAT prep AI, MCAT study notes AI, MCAT CARS practice AI, MCAT flashcards generator, AAMC study guide AI | "MCAT biology notes generator", "MCAT psych-soc flashcards AI", "CARS passage to notes", "MCAT formula sheet generator", "MCAT 3-month study plan AI" | StudyFetch/King of the Curve 已有，但 ThetaWave 有中文版+双语输出 |
| NCLEX | NCLEX prep AI, NCLEX study notes AI, NCLEX drug cards generator, Next Gen NCLEX AI, NCLEX SATA practice AI | "NCLEX pharmacology study guide AI", "Next Gen NCLEX case study notes", "NCLEX clinical judgment model AI", "NCLEX 75 questions study plan", "NCLEX lab values flashcards AI" | UWorld 主导题目侧；ThetaWave 可占据「笔记/闪卡生成」侧 |
| LSAT | LSAT prep AI, LSAT logical reasoning AI, LSAT study notes AI, LSAT argument analysis AI, LSAT flashcard generator | "LSAT LR question type notes", "LSAT RC passage to notes", "LSAT argument structure AI", "LSAT 170 study plan AI", "LSAT flaw question practice AI" | AdeptLR 主导 AI 自适应训练；ThetaWave 差异化在笔记/论证提取 |
| USMLE | USMLE prep AI, USMLE study notes AI, USMLE Step 2 CK prep AI, USMLE clinical vignette AI, USMLE flashcard generator | "USMLE First Aid to flashcards AI", "USMLE Step 2 CK notes generator", "USMLE dedicated period study plan AI", "USMLE bug-drug chart generator" | UWorld/Amboss 主导；ThetaWave 差异化在多资源统一笔记 |
| Bar Exam | bar exam prep AI, MBE study notes AI, MEE writing AI, bar exam flashcard generator, UBE study tool AI | "MBE constitutional law notes AI", "MEE essay template generator", "bar exam 8-week study plan AI", "MPT task memo AI" | Barbri/Kaplan 主导课程侧；AI 笔记工具空白 |
| GRE | GRE prep AI, GRE vocabulary flashcards AI, GRE verbal reasoning AI, GRE quant notes generator, GRE AWA essay AI | "GRE vocabulary builder AI", "GRE math formula to flashcards", "GRE reading comprehension notes AI", "GRE 3-month study plan AI", "GRE argument essay template generator" | Magoosh/Greg Mat 主导课程侧；AI 笔记工具空白 |

---

## 六、内容缺口与未覆盖考试

### 6.1 当前覆盖度

| 状态 | 考试 | 竞争强度 | 搜索量潜力 | 建议 |
|------|------|----------|-----------|------|
| ❌ 待建 | MCAT（P0）、NCLEX（P0）、LSAT（P1）、USMLE（P1）、Bar（P2）、GRE（P2） | — | — | 按优先级逐步建站 |
| ❌ 未规划 | **AP Exams**（30+ 科目） | 中（StudyFetch 已覆盖） | 中（高中生群体） | P3 评估——高中生非当前核心用户群 |
| ❌ 未规划 | **GMAT** | 中 | 中（年 40,000+ 考生但 GRE 更主流） | P3 评估——优先 GRE 后再考虑 |
| ❌ 未规划 | **DAT / OAT / PCAT**（牙医/验光/药学） | 低（无 AI 工具覆盖） | 低-中（利基） | P3 远期——需先建对应学科页 |
| ❌ 未规划 | **Professional Certifications**（AWS/Google/PMP/CFA） | 中（通用工具可服务） | 中-高（但搜索模式不同） | P3——非学术考试，用户画像可能与大学生不同 |

### 6.2 考试页触发的条件逻辑

与学科页（只要有该专业的用户就可建）不同，考试页建站需要三重验证：

1. **搜索量**：该考试是否有足够的独立搜索需求（不与学科词重叠）
2. **报考规模**：年考生数是否足够支撑 ROI（通常需 >30,000）
3. **题型特殊性**：该考试是否有独特题型/策略需要专用页面（而非通用 Exam Prep 页可覆盖）

---

## 七、按考试的内容营销建议

| 考试 | 博客/资源页主题（建议） |
|------|------------------------|
| **MCAT** | "MCAT CARS: From Passage to Practice Questions with AI" / "MCAT Study Plan: How AI Cuts 300 Hours to 200" / "MCAT Psych-Soc: AI Flashcards for the 65-Minute Section" |
| **NCLEX** | "Next Gen NCLEX: AI for Clinical Judgment Case Studies" / "NCLEX Drug Cards: AI vs Manual — Speed Comparison" / "NCLEX SATA Questions: How AI Generates Unlimited Practice" |
| **LSAT** | "LSAT Logical Reasoning: AI Argument Structure Extraction" / "LSAT Without Logic Games: New Era Study Strategy" / "LSAT 170+: AI-Assisted Study Plan" |
| **USMLE** | "USMLE Step 2 CK: AI Clinical Vignette Generator" / "From First Aid to Flashcards: AI Speed Run" / "USMLE Dedicated Period: AI Study Stack" |
| **Bar Exam** | "Bar Exam MBE: AI Subject-by-Subject Breakdown" / "MEE Essay Writing: AI Template Generator" / "Bar Exam 8-Week Plan: AI as Your Study Partner" |
| **GRE** | "GRE Vocabulary: AI Flashcard Method vs Traditional Word Lists" / "GRE AWA: AI Essay Template and Argument Analysis" / "GRE Quant: AI Formula Sheet for Non-STEM Students" |

---

## 八、实施优先级矩阵

| 优先级 | 动作 | 类型 | 预期影响 |
|--------|------|------|----------|
| **P0** | 建站 /use-case/mcat-prep | 新页面 | MCAT 高意图搜索捕获；85,000+ 年考生 |
| **P0** | 建站 /use-case/nclex-prep | 新页面 | NCLEX 高意图搜索捕获；175,000+ 年考生 |
| **P0** | 在 /for-pre-med-students 和 /for-nursing-students 增加考试页内链 | 内链优化 | 流量闭环 |
| **P1** | 建站 /use-case/lsat-prep | 新页面 | LSAT 高意图搜索捕获 |
| **P1** | 建站 /use-case/usmle-prep | 新页面 | USMLE 搜索捕获 |
| **P1** | 为每个考试页创建 2-3 篇博客（§七） | 内容营销 | Topic cluster 建设 |
| **P2** | 建站 /use-case/bar-exam-prep 和 /use-case/gre-prep | 新页面 | 扩展考试覆盖 |
| **P2** | 在 /for-law-students 和 /for-graduate-students 增加考试页内链 | 内链优化 | 流量闭环 |
| **P3** | 评估 AP/GMAT/DAT/Professional Certs 建站可行性 | 市场调研 | 识别下一个考试赛道 |

---

*文档创建日期：2026-05-12 | 基于 category-expansion-analysis.md 的 By Exam 维度推荐，6 个考试节点完整化（痛点+能力+Proof+竞品+关键词+内链+内容营销+实施优先级）*
