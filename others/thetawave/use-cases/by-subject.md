# ThetaWave Use Cases — By Subject（学科分类）

> **维度定义**：按「学什么」分类——覆盖 STEM、医学、商科、法学、人文社科等学科/专业的专属痛点与 ThetaWave 能力匹配。
> **关联**：[by-identity.md](./by-identity.md) | [by-stage.md](./by-stage.md) | [../thetawave-use-cases.md](../thetawave-use-cases.md) | [../thetawave-features.md](../thetawave-features.md) | [../keywords/thetawave-keywords.md](../keywords/thetawave-keywords.md) | [../thetawave-competitors.md](../thetawave-competitors.md)
> **URL 模式**：`https://thetawave.ai/use-case/{slug}`（注意 `/use-case/` 为单数）
> **更新**：2026-05-12 — 多轮迭代：(1) Web 验证并修正 CS/心理/经济/商学/预科/生物描述；(2) 6 个学科从表行提升为完整详情段（痛点+能力+竞品+关键词+内链）；(3) 关键词表扩展为 3-5 核心 + 3-5 长尾；(4) 新增 §六 内容缺口分析（工程学/药学/建筑学/艺术）；(5) 新增 §七 按学科内容营销建议；(6) 新增 §八 实施优先级矩阵

---

## 一、学科 Use Case 页面全览

| 优先级 | 学科 | 页面 | URL | 状态 |
|--------|------|------|-----|------|
| **S** | 法学 | For Law Students | /use-case/for-law-students | ✅ 已上线（含 /zh 中文版） |
| **S** | 护理 | For Nursing Students | /use-case/for-nursing-students | ✅ 已上线（含 /study/nursing-notes） |
| **S** | 医学预科 | For Pre-Med Students | /use-case/for-pre-med-students | ✅ 已上线 |
| **A** | STEM | For STEM Students | /use-case/for-stem-students | ✅ 已上线 |
| **A** | 计算机科学 | For CS Students | /use-case/for-cs-students | ✅ 已上线 |
| **A** | 生物 | For Biology Students | /use-case/for-biology-students | ✅ 已上线 |
| **A** | 商学 | For Business Students | /use-case/for-business-students | ✅ 已上线 |
| **B** | 经济 | For Economics Students | /use-case/for-economics-students | ✅ 已上线 |
| **B** | 心理 | For Psychology Students | /use-case/for-psychology-students | ✅ 已上线 |
| **B** | 教育 | For Education Students | /use-case/for-education-students | ✅ 已上线 |
| **C** | 人文社科 | For Humanities Students | /use-case/for-humanities-students | ❌ 待建 |

---

## 二、各学科详情

### 2.1 法学（For Law Students）— P1

**URL**: /use-case/for-law-students（含 /zh/use-case/for-law-students 中文版）

**痛点**: 高密度信息课程；判例摘要、法规条文、阅读材料分散；期末无统一复习版本。

**ThetaWave 能力**：
- 上传讲座录音 + PDF + 判例阅读 + 视频 → AI 统一整理概念/术语/判例/法学理论为结构化复习笔记
- Flashcard Maker：定义、概念、高频考点
- Quiz Maker：自测
- **差异化**：实时讲座捕获 + 播客生成（通勤听复习）

**热门笔记示例**：Criminal Law Intro、Federal Rules of Evidence、Civil Procedure: Pleading & Defense、Trusts Law

**vs ChatGPT**：强调将真实课程材料（讲座/PDF/判例）保留在同一工作流中，输出锚定自有源材料。

**竞品参考**：

| 竞品 | URL | 模式 |
|------|-----|------|
| LegesGPT | legesgpt.com/law-student | 判例检索/引用/模拟题 |
| Mindgrasp | mindgrasp.ai/law-students | 五件套 + FAQ + 社会证明 |
| Lawfton | lawfton.ai | Outline→闪卡/测验/播客 |
| Lexplug | lexplug.com | Gunnerbot/ELI5/case podcast |

**关键词**: AI note taker for law students, law school notes AI, case brief generator

**内链** → /use-case/exam-prep、/pdf-to-notes、/lecture-to-notes

---

### 2.2 护理（For Nursing Students）— P1

**URL**: /use-case/for-nursing-students（额外页 /study/nursing-notes）

**痛点**: 药理学讲座 50 分钟讲 15+ 药物；药名/机制/禁忌症/护理要点易遗漏；NCLEX 题型与课本学习不同；临床和课堂知识脱节。

**ThetaWave 能力**：
- 录制临床/药理讲座 → 自动生成 **Drug Cards**（药名/分类/机制/副作用/护理要点）
- **NCLEX 风格练习题**（全选、优先级、授权题型）
- 统一知识库：病理生理 ↔ 临床轮转

**Proof**: 每学期平均生成 150+ 药物闪卡；Johns Hopkins/Duke/UPenn 护理学生使用

**额外页面 /study/nursing-notes**: 覆盖 Pharmacology、Pathophysiology、Medical-Surgical Nursing、Pediatric Nursing、Mental Health Nursing、Fundamentals of Nursing；支持 NCLEX-RN/NCLEX-PN/HESI Exit Exam/ATI Comprehensive

**竞品参考**：

| 竞品 | URL | 模式 |
|------|-----|------|
| Nursify | nursifyai.com | Notes/Calendar/Clinical/Tutor；NCLEX |
| Repeatica | repeatica.com/for/nursing-students | 讲座转录/闪卡/NCLEX 题 |
| Feynman Nurse | feynmannurse.app | Feynman 模式/NCLEX/150+ 药卡 |
| Lily | studywithlily.com | Coursework/NCLEX 双模式 |

**关键词**: nursing school lecture notes AI, NCLEX study notes, nursing drug cards AI

**内链** → /use-case/exam-prep、/flashcard-maker、/podcast-generator

---

### 2.3 医学预科（For Pre-Med Students）— P1

**URL**: /use-case/for-pre-med-students

**痛点**: MCAT 备考覆盖生物/化学/物理/心理多学科；有机化学方程式和生物路径难以手写记录。

**ThetaWave 能力**: STEM 共用公式图表引擎；LaTeX 渲染有机化学方程式；PDF/实验报告输入；多源笔记合成

**Proof**: Harvard、Stanford、Johns Hopkins 预科学生使用

**竞品参考**：

| 竞品 | URL | 模式 |
|------|-----|------|
| Savant | savantapp.com | FSRS/闪卡/语义搜索 |
| MedLect | medlect.ai | USMLE/MCAT/NCLEX/临床 rationale |
| RemNote | remnote.io/mcat_landing_page | MCAT 独立落地页 |

**关键词**: MCAT notes AI, pre-med study notes, organic chemistry notes AI

---

### 2.4 STEM（For STEM Students）— P1

**URL**: /use-case/for-stem-students

**痛点**: 跟不上快节奏的数学推导、公式和图表；LaTeX 手写太慢。

**ThetaWave 能力**: 实时讲座录制 → 自动 LaTeX 渲染（积分/矩阵/希腊字母）；公式专用闪卡；多源笔记合成（讲座+教科书 PDF+幻灯片）

**Proof**: 93% STEM 用户认为笔记比手写更完整；Stanford/MIT/UCLA/UC Berkeley 使用；4.8/5 评分

---

### 2.5 计算机科学（For CS Students）— P1

**URL**: /use-case/for-cs-students

**痛点**：讲座中代码片段难以手写记录；算法推导与板书不同步——抄完代码已丢失讲解上下文；数据结构/设计模式/系统设计等概念分散在多个课程和文档中；项目代码和课堂笔记分离。

**ThetaWave 能力**：
- 实时讲座捕获保留代码走读（Code Walkthroughs）+ 关键注释，不错过讲师解释
- 算法模式卡（Algorithm Pattern Cards）：Big-O 复杂度、数据结构选择、设计模式场景——自动归类
- 理论-实现联动：教科书定义 ↔ 实际代码示例 ↔ 项目应用，三向链接
- Flashcard Maker：时间复杂度速记；Quiz Maker：系统设计选择题

**Proof**：4.8/5 评分；Stanford/MIT/CMU CS 学生使用

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Knowt（UGC 闪卡） | 社区上传的 CS 闪卡集（AP CS、A-Level CS） | Knowt 内容为手动创建；ThetaWave 实时讲座→自动代码笔记+闪卡 |
| Stempad | 科学笔记，LaTeX/图表/代码块 | 偏写作工具，非实时讲座捕获 |
| Notiva | 单上传→六输出（闪卡/歌曲/视频/信息图） | 早期项目，未规模验证 |

**关键词**: AI notes for CS students, coding lecture notes AI, algorithm study tool, CS study notes AI, data structures flashcard AI

**长尾机会**: "convert coding lecture to notes", "Big-O cheat sheet AI", "system design interview notes generator"

**内链** → /use-case/for-stem-students、/lecture-to-notes、/flashcard-maker、/quiz-maker

---

### 2.6 生物（For Biology Students）— P2

**URL**: /use-case/for-biology-students

**痛点**：代谢路径（Krebs cycle、Calvin cycle、glycolysis 等）纯文本难以理解；分类学（taxonomy）层级/特征需要反复记忆；实验报告笔记与课堂理论脱节；解剖学/组织学需要图文联动。

**ThetaWave 能力**：
- 讲座转录→自动标注代谢路径关键步骤/酶/产物；可导出为路径图笔记
- 概念分类卡（Concept Classification Cards）：界-门-纲-目-科-属-种 层级闪卡
- 实验报告 + 课堂理论统一知识库
- Mind Map Maker：代谢网络可视化

**Proof**：与 pre-med track 联动（同一学习路径上的前期课程）；Johns Hopkins/Duke 生物系学生使用

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| RemNote | 间隔重复闪卡，支持生物学术语 | 无实时讲座捕获；ThetaWave 有代谢路径可视化 |
| StudyX /subjects/social-science/ | 通用生物 Q&A | 非学习笔记专用；ThetaWave 有一站式输出链 |

**关键词**: biology study notes AI, pre-med biology notes, metabolic pathway flashcards AI, taxonomy study tool

**长尾机会**: "Krebs cycle notes generator", "biology lab report to notes", "AP Biology AI study guide"

**内链** → /use-case/for-pre-med-students、/mind-map-maker、/flashcard-maker、/lecture-to-notes

---

### 2.7 商学（For Business Students）— P1

**URL**: /use-case/for-business-students

**痛点**：案例分析（case study）阅读量大（HBS 案例通常 20-40 页）；SWOT/五力/价值链等框架需手动套用；多人 case prep 笔记格式不统一；财务/会计/战略/营销/组织行为多学科并行。

**ThetaWave 能力**：
- 上传案例 PDF → 自动提取关键事实、决策点、利益相关方、财务数据→结构化案例摘要笔记
- 框架模板自动套用：SWOT、Porter's Five Forces、Value Chain、PESTEL
- 每案例节省 90 分钟阅读+整理时间
- Flashcard Maker：财务公式、管理理论；Quiz Maker：case-based 情景题

**Proof**：Wharton、HBS、Kellogg MBA 学生使用；热门笔记：Strategic Management、Financial Accounting、Principles of Marketing、Organizational Behavior

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Mindgrasp | Canvas/Blackboard 集成，适合有 LMS 的商学院 | 不瞄准 business-specific 痛点；ThetaWave 有案例框架模板 |
| NotebookLM | 文档分析强，适合案例阅读 | 无框架化输出；无闪卡/测验 |
| ChatGPT | 通用案例摘要 | 无结构化框架；需手动粘贴 |

**关键词**: MBA notes AI, business case study notes, case prep AI, business school note taker, SWOT analysis AI, strategic management notes

**长尾机会**: "HBS case study to notes", "consulting case interview prep AI", "financial accounting notes generator"

**内链** → /pdf-to-notes、/flashcard-maker、/quiz-maker、/mind-map-maker

---

### 2.8 经济（For Economics Students）— P2

**URL**: /use-case/for-economics-students

**痛点**：供需曲线/IS-LM/AD-AS 等图表推导难以在笔记中重现；宏观微观模型切换频繁，概念混淆风险高；计量经济学软件输出（Stata/R）需要与理论笔记整合。

**ThetaWave 能力**：
- 讲座转录自动保留公式推导步骤（LaTeX 渲染）
- 图表描述→结构化笔记（"供给曲线右移→均衡价格下降，数量上升"）
- 10 语言双语输出：非英语母语学生可用母语对照学习
- Flashcards：公式/定义/理论对比；Quiz：政策情景分析题

**Proof**：热门笔记覆盖 Principles of Economics、Macroeconomics、Political Economy、Money & Banking

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| StudyX（Q&A 为主） | 经济学定义/概念问答 | 纯 Q&A；ThetaWave 实时讲座+多格式输出 |
| NotebookLM | PDF 分析，适合论文阅读 | 无公式渲染专项 |
| Stempad | LaTeX 渲染 | 偏写作工具；ThetaWave 一站式学习链 |

**关键词**: economics notes AI, econometrics study tool, microeconomics study notes, macroeconomics notes generator, economics formula flashcards

**长尾机会**: "supply and demand notes AI", "IS-LM model study notes", "econometrics Stata output to notes"

**内链** → /use-case/for-business-students、/notes-generator、/flashcard-maker、/mind-map-maker

---

### 2.9 心理（For Psychology Students）— P2

**URL**: /use-case/for-psychology-students

**痛点**：研究方法论笔记维度多（假设/方法/样本/发现/局限/理论映射——每项都需记录）；经典研究众多（Bandura, Milgram, Zimbardo, Asch, Loftus 等），实验-理论对应关系易混淆；APA 格式写作要求严格；每门课 40+ 篇研究论文需要消化。

**ThetaWave 能力**：
- 讲座转录→自动提取研究方法论要素（假设/方法/样本量/主要发现/理论框架）
- 研究者-理论联动索引：自动关联经典实验↔理论↔后续研究
- APA 格式期刊文章提取：Abstract/Introduction/Method/Results/Discussion 结构化摘要
- Mind Map：理论流派可视化（行为主义↔认知↔人本↔生物↔社会文化）

**Proof**：Yale、UCLA、UChicago 心理学系学生使用；每门课可处理 40+ 篇研究论文

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| StudyX | 心理学基础概念 Q&A | 非研究导向；ThetaWave 有方法论+APA 提取 |
| Nabi X | 学术 AI，哲学家对话（HKU） | 偏人文/哲学；ThetaWave 覆盖实证研究方法论 |

**关键词**: psychology study notes AI, psychology research notes generator, APA citation notes AI, psychology experiment study guide, psych lecture notes

**长尾机会**: "cognitive psychology notes AI", "social psychology experiment summaries", "DSM study guide AI", "psychology research methods notes"

**内链** → /use-case/for-stem-students（统计/方法论重叠）、/pdf-to-notes、/flashcard-maker、/mind-map-maker

---

### 2.10 教育（For Education Students）— P2

**URL**: /use-case/for-education-students

**痛点**：教育理论（Piaget/Vygotsky/Bloom/Dewey/Montessori）庞大且分散；教案设计需要从理论到实践的转化；课堂观察笔记与教育理论难以实时对照；教师资格考试（PRAXIS/教师编制）需要系统复习。

**ThetaWave 能力**：
- 讲座转录→自动关联教育理论家+概念（如 "scaffolding → Vygotsky → ZPD"）
- 教案模板自动生成：基于上传的课程大纲+教学目标+学生画像
- 课堂观察笔记→理论对照索引
- Flashcard Maker：教育理论对比卡（Constructivism vs Behaviorism vs Cognitivism）
- Quiz Maker：PRAXIS/教师资格考试风格题

**Proof**：Teachers College/Stanford GSE/Vanderbilt Peabody 学生使用

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| StudyX | 教育基础概念 Q&A | 偏作业帮助；ThetaWave 有教案生成+理论联动 |
| NotebookLM | 文档分析 | 无教案模板；无结构化学习输出 |

**关键词**: education student notes AI, lesson plan AI generator, teacher certification prep AI, educational theory flashcards, PRAXIS study notes AI

**长尾机会**: "Piaget vs Vygotsky study guide", "classroom observation notes AI", "edTPA notes organizer", "Bloom's taxonomy lesson plan generator"

**内链** → /use-case/for-psychology-students（教育心理交叉）、/notes-generator、/flashcard-maker、/quiz-maker

---

## 2.11 人文社科（For Humanities Students）— P2 待建

**URL**: /use-case/for-humanities-students（❌ 待建）

**痛点**：长文本阅读量大（每门课每周 100-300 页）；论点/论据/反论结构难以从长篇阅读中提取；跨文本主题连接是核心技能但无工具支撑；论文写作需要引用管理和论证结构。

**ThetaWave 能力（规划）**：
- 上传 PDF/书籍章节→自动提取核心论点、支持论据、方法论、结论
- 跨文本主题索引：自动关联多篇阅读中的共同主题/对立观点
- 论文论证结构助手：从阅读笔记→论点大纲→引用映射
- 时间线/历史事件→因果链可视化

**竞品参考**：

| 竞品 | 模式 | 说明 |
|------|------|------|
| Nabi / Nabi X | 学术 AI，历史/哲学专用（HKU/HKBU） | 研究级 RAG，学生共建知识库；非商业产品 |
| Jargon | 开源 Zettelkasten + AI | 自动链接概念，适合跨领域研究 |
| NotebookLM | Google 背书，文档分析+Audio Overviews | 免费，目前是人文学科学生首选的 AI 工具 |
| Obsidian + AI 插件 | 本地笔记+知识图谱 | 学习曲线陡峭 |

**ThetaWave 差异化机会**：当前市场上没有专为人文社科学生设计的商业 AI 笔记工具——NotebookLM 是唯一实用选项但无结构化学习输出（闪卡/测验/思维导图）。ThetaWave 可填补「长文本→结构化笔记→复习材料」全链路空白。

**关键词**: AI notes for history students, humanities study tool AI, long reading notes AI, thesis research notes, philosophy study notes AI, literature review AI, primary source analysis notes

**内链规划** → /pdf-to-notes、/notes-generator、/mind-map-maker、/use-case/research-thesis

---

## 三、SEO 关键词分工（防 cannibalization · 扩展版）

| 学科 | 核心关键词（3-5） | 长尾关键词（3-5） | ThetaWave 差异化 |
|------|------------------|-------------------|-----------------|
| 法学 | AI note taker for law students, law school case brief AI, legal study notes, case brief generator, law school outline AI | "IRAC case brief AI", "bar exam study notes", "1L note taking tips AI", "law school outline from lecture" | 实时讲座 + 播客生成；判例→结构化笔记 |
| 护理 | nursing school lecture notes AI, NCLEX prep AI, nursing drug cards AI, clinical notes AI, pharmacology study tool | "NCLEX-RN notes generator", "nursing dosage calculation flashcard", "clinical rotation notes AI", "ATI comprehensive study guide AI" | NCLEX 风格题 + Drug Cards + 播客复习 |
| 医学预科 | MCAT notes AI, pre-med study tool, organic chemistry notes AI, pre-med biology notes, MCAT prep AI | "MCAT CARS practice notes", "biochemistry pathway notes AI", "medical school prerequisites study AI", "AMCAS application study plan" | STEM 公式引擎 + YouTube 视频输入 |
| STEM | AI note taker for STEM, LaTeX lecture notes, math study notes AI, physics formula notes, engineering study tool | "calculus lecture to notes", "physics equation flashcard AI", "circuit diagram notes", "MATLAB notes generator" | 实时 LaTeX 渲染；公式闪卡 |
| CS | AI notes for CS students, coding lecture notes, algorithm study tool, data structures flashcard AI, CS study notes AI | "convert coding lecture to notes", "Big-O cheat sheet AI", "system design interview notes generator", "GitHub code to notes", "LeetCode pattern notes" | 代码走读；算法复杂度卡片；理论-实现联动 |
| 生物 | biology study notes AI, pre-med biology, metabolic pathway flashcards AI, taxonomy study tool, anatomy notes AI | "Krebs cycle notes generator", "biology lab report to notes", "AP Biology AI study guide", "dissection notes organizer", "phylogenetic tree study notes" | 代谢路径图；分类学概念卡 |
| 商学 | MBA notes AI, business case study notes, case prep AI, business school note taker, SWOT analysis AI | "HBS case study to notes", "consulting case interview prep AI", "financial accounting notes generator", "Porter five forces notes AI", "DCF model study notes" | 案例研究笔记；框架化分析；Wharton/HBS/Kellogg |
| 经济 | economics notes AI, econometrics study tool, microeconomics study notes, macroeconomics notes generator, economics formula flashcards | "supply and demand notes AI", "IS-LM model study notes", "econometrics Stata output to notes", "game theory study guide AI", "monetary policy notes" | 10 语言双语输出；宏观/微观模型 |
| 心理 | psychology study notes AI, psychology research notes generator, APA citation notes AI, psych lecture notes, psychology experiment study guide | "cognitive psychology notes AI", "social psychology experiment summaries", "psychology research methods notes", "DSM diagnostic criteria study AI", "developmental psychology stages notes" | 研究方法论；研究者-理论映射；APA 提取 |
| 教育 | education student notes AI, lesson plan AI generator, teacher certification prep AI, educational theory flashcards, PRAXIS study notes AI | "Piaget vs Vygotsky study guide", "classroom observation notes AI", "edTPA notes organizer", "Bloom's taxonomy lesson plan generator", "IEP notes organizer AI" | 教案模板；理论与课堂实践联动 |
| 人文社科（待建） | AI notes for history students, humanities study tool AI, long reading notes AI, thesis research notes, philosophy study notes AI | "primary source analysis notes AI", "literature review organizer AI", "dissertation chapter notes", "comparative literature study notes", "historical timeline notes AI" | NotebookLM 替代 + 长文本→结构化复习全链路 |

---

## 四、建站结构模板（可复用 · 增强版）

每个学科页均使用统一模块，**但痛点/能力/Proof 必须按学科定制**：

```
Headline（H1，含学科关键词）
  → 模板：AI Note Taker for [Discipline] Students — Learn [X]x Faster | ThetaWave

The Problem（3–5 条痛点，只写该学科独有）
  → ❌ 禁止复用：STEM 页的 "跟不上数学推导" 不能写入 Law 页
  → ✅ 学科痛词示例：IRAC/case brief（法学）、drug cards/dosage calc（护理）、code walkthrough（CS）

How ThetaWave Helps（对应痛点 3–5 条能力，每条对应 1 个 Feature）
  → 必须引用具体 Feature 页名称：Flashcard Maker / Quiz Maker / Mind Map Maker 等

Sample Notes（热门笔记示例，2–4 个）
  → 真实课程名或主题，体现学科特色

vs ChatGPT / vs NotebookLM / vs [竞品]（对比表）
  → 侧重该学科场景，而非通用对比

Social Proof（该学科相关）
  → 学校名（如 "Used at Yale, UCLA, UChicago"）、用户数、评分、节时数据
  → ❌ 避免空泛 "100,000+ students" 替代学科专属 proof

Related Features & Use Cases（5–8 个内链）
  → 优先链 Features（/flashcard-maker 等）+ 同维度其他学科页 + 相关 stage/identity 页

FAQ（5–6 个，结构化,含关键词）
  → 50% 通用问题（What formats / Is it free / How accurate / vs ChatGPT）
  → 50% 学科专属问题（e.g. "Can ThetaWave handle IRAC format for law?"）

CTA（注册/免费试用）
```

**原则**：
- 避免与主 STEM / Graduate 页复用同一段 Problem；学科页须体现该学科的独特痛词
- 每页至少 3 个真实课程名/热门笔记示例（增强 E-E-A-T）
- 学科专属 FAQ 是 Featured Snippet 获取的关键——需用 H2/H3 结构化

---

## 五、泛学科竞品索引

以下竞品覆盖多学科场景，在评估学科页 SEO 竞争时参考：

| 竞品 | URL | 规模 | 核心功能 |
|------|-----|------|----------|
| **Knowt** | knowt.com | 1.5M–3M 用户 | AI 讲座笔记/闪卡/YouTube；**全部免费** |
| **Coconote**（Quizlet 嫡系）| coconote.app | App Store 4.8★（16K+） | 100+ 语言；讲座→笔记/测验/闪卡 |
| **StudyX** | studiox.ai | 16M+ 学生 | 免费；PDF/视频/讲座→笔记+闪卡+测验 |
| **Wave** | wave.co | App Store 4.9★（11K+） | 日本 #1；后台离线录音；76 语言 |
| **Glasp** | glasp.ai | 1M+ 用户 | 网页高亮+AI 摘要；Notion/Obsidian 导出 |
| Lemora AI | lemora.ai | — | PDF/视频/讲座→笔记/闪卡/测验/播客 |
| StudyFetch | studyfetch.com | — | subject-specific AI aids |
| Mindgrasp | mindgrasp.ai | 10K+ 学生 | AI 五件套；pSEO 学科模板页（`/[field]-students`） |
| **NotebookLM** | Google | 免费 | 文档分析+Audio Overviews；人文社科学生首选免费工具 |

---

## 六、内容缺口与未覆盖学科（Content Gap Analysis）

### 6.1 学科覆盖度评估

| 状态 | 学科 | 竞争强度 | 搜索量潜力 | 建议 |
|------|------|----------|-----------|------|
| ✅ 已覆盖 | 法学（S）、护理（S）、预科（S）、STEM（A）、CS（A）、生物（A）、商学（A）、经济（B）、心理（B）、教育（B） | — | — | 优化页面深度 + 内链 |
| ❌ 待建 | 人文社科 | 低（仅 NotebookLM/开源工具） | 中高（长尾聚集） | P1 建站 |
| ❌ 未规划 | **工程学**（独立于 STEM） | 中（Stempad/Notiva） | 高（细分赛道） | P2 评估 |
| ❌ 未规划 | **药学**（Pharmacy） | 低（无专用 AI 笔记工具） | 中（NAPLEX/MPJE 考试） | P2 评估 |
| ❌ 未规划 | **建筑学**（Architecture） | **极低**（完全未被服务） | 低-中（利基但高意图） | P3 探索 |
| ❌ 未规划 | **艺术/设计**（Art & Design） | **极低**（完全未被服务） | 低（非文本主导） | P3 暂缓 |

### 6.2 工程学（Engineering）— 独立于 STEM 的理由

STEM 页覆盖所有理工科，但工程学的痛点和 ThetaWave 的工程化卖点无法容纳：

**痛点独特性**：
- 电路图/CAD/控制系统框图无法用 LaTeX 表达
- 需要 MATLAB/Simulink/AutoCAD 多软件环境的笔记整合
- Capstone/毕业设计需要跨学期项目管理型笔记
- FE/PE 工程师资格考试有独立备考需求

**搜索验证**："AI note taker for engineering students"、"circuit diagram notes AI" "FE exam prep AI" 均在 Google 有搜索量但无专用落地页承接。

**建议**：P2 评估 → 如果 STEM 页的工程相关流量增长，可拆分独立 `/use-case/for-engineering-students`。

### 6.3 药学（Pharmacy）— 被忽视的高价值赛道

**为什么值得做**：
- 美国 140+ 药学院，每年 15,000+ PharmD 新生
- NAPLEX/MPJE 考试有明确备考工具需求
- 药理学/药物治疗学/药物化学知识密集，与护理有重叠但更深入
- 竞品空白：搜索未发现专用 AI 笔记工具（Dentascribe 类似模式但针对牙医）
- ChatGPT-4o 在药学治疗学问题准确率达 97.5%（2025 研究），证明 AI+药学是可行组合

**关键搜索词**："NAPLEX study notes AI", "pharmacology drug cards generator", "pharmacy school notes AI", "pharmacokinetics notes generator"

**建议**：P2 → 若护理页（同属 healthcare education）表现好，可复用 Drug Cards + NCLEX 题型模式，适配 NAPLEX。

### 6.4 建筑学与艺术设计 — 远期机会

这两个领域以视觉/空间思维为主，当前 AI 笔记工具全部以文本为核心范式。除非 ThetaWave 推出「图片优先 Canvas + Sketch-to-Diagram」功能，否则不适宜建学科页——建了页面也缺乏产品能力承接。

**触发条件**（何时评估）**：** ThetaWave 推出可视化笔记 / Canvas 模式 / 图片优先输入。

---

## 七、按学科的内容营销建议

每个学科应配套 2-4 篇博客/资源页，形成 topic cluster：

| 学科 | 博客/资源页主题（建议） |
|------|------------------------|
| **法学** | "How to Brief a Case with AI" / "1L Survival Guide: AI Note Taking" / "IRAC Method + AI: Faster Case Analysis" |
| **护理** | "NCLEX Prep: AI Drug Cards vs Manual" / "Clinical Rotation Notes: How AI Helps" / "Pharmacology Study Hacks for Nursing Students" |
| **医学预科** | "MCAT Study Plan with AI Notes" / "Organic Chemistry: From Lecture to Flashcards" / "Pre-Med Prerequisites: AI Study Workflow" |
| **STEM** | "LaTeX Notes Without Typing: AI Does It" / "Math Lecture to Formula Flashcards" / "Physics Problem Sets: AI-Assisted Review" |
| **CS** | "Code Walkthroughs: AI Note Taking for CS Lectures" / "Big-O Cheat Sheet: Auto-Generated from Your Notes" / "System Design Interview Prep with AI" |
| **商学** | "Case Study Prep: 90 Minutes Saved with AI" / "SWOT to Notes: Framework Automation" / "MBA First Year: AI Study Stack" |
| **经济** | "Supply & Demand Diagrams to Structured Notes" / "Econometrics + AI: Stata Output to Study Guide" / "Macro vs Micro: AI Concept Mapping" |
| **心理** | "APA Formatting: AI Extracts Your Research Notes" / "Classic Psychology Experiments: AI Study Guide" / "Research Methods Notes: From Lecture to Flashcards" |
| **教育** | "Lesson Plan Generator: AI for Student Teachers" / "PRAXIS Prep: Education Theory Flashcards" / "Classroom Observation Notes: AI vs Manual" |
| **人文社科（待建）** | "NotebookLM Alternative for History Students" / "Long Reading to Structured Notes: AI Workflow" / "Thesis Research: AI Literature Review Organizer" |

---

## 八、实施优先级矩阵

| 优先级 | 动作 | 类型 | 预期影响 |
|--------|------|------|----------|
| **P0** | 将 §2.5–§2.10 的 6 个学科表行提升为完整详情段（CS、生物、商学、经济、心理、教育） | 文档优化 | ✅ 已完成（见上方 §2.5–§2.10） |
| **P0** | 扩展关键词表（§三）：每学科 3-5 核心 + 3-5 长尾 | SEO 策略 | ✅ 已完成（见上方 §三） |
| **P1** | **建站** /use-case/for-humanities-students（人文社科） | 新页面 | 填补 NotebookLM 替代词空白；覆盖 10+ 人文社科专业 |
| **P1** | 补充已上线学科页的 FAQ 结构化（50% 学科专属） | 页面优化 | Featured Snippet 获取 |
| **P1** | 补充已上线学科页的 Sample Notes / Proof 数据 | 页面优化 | E-E-A-T 增强 |
| **P2** | 评估 /use-case/for-engineering-students 建站可行性 | 市场调研 | 覆盖工程细分赛道 |
| **P2** | 评估 /use-case/for-pharmacy-students 建站可行性 | 市场调研 | 覆盖药学空白赛道 |
| **P2** | 为每个学科创建 2-4 篇博客，形成 topic cluster（§七） | 内容营销 | 长尾流量 + 领域权威 |
| **P3** | 监控建筑学/艺术设计 AI 笔记工具发展 | 市场监控 | 远期机会识别 |

---

*文档创建日期：2026-05-11 | 更新：2026-05-12 — Web 验证 + 6 学科完整化 + 关键词扩展 + 内容缺口分析 + 内容营销建议*
