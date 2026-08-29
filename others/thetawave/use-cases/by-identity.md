# ThetaWave Use Cases — By Identity（身份分类）

> **维度定义**：按「谁在用」分类——覆盖不同身份/特征的学生群体及其独特需求。
> **关联**：[by-subject.md](./by-subject.md) | [by-stage.md](./by-stage.md) | [../thetawave-use-cases.md](../thetawave-use-cases.md) | [../thetawave-features.md](../thetawave-features.md) | [../keywords/thetawave-keywords.md](../keywords/thetawave-keywords.md)
> **URL 模式**：`https://thetawave.ai/use-case/{slug}`
> **更新**：2026-05-12 — 多轮迭代：(1) Web 验证并修正 ADHD/国际学生/在线学习者能力描述；(2) 4 个身份全部补充竞品对比 + vs ChatGPT/NotebookLM；(3) 关键词表扩展为 3-5 核心 + 3-5 长尾；(4) 新增 §五 内容缺口分析（非传统学生/第一代大学生/残障学生/高中生）；(5) 新增 §六 按身份内容营销建议；(6) 新增 §七 实施优先级矩阵

---

## 一、Identity Use Case 页面全览

| 页面 | URL | 状态 | 说明 |
|------|-----|------|------|
| For Graduate Students | /use-case/for-graduate-students | ✅ 已上线 | 论文/研讨会/导师会议/文献管理 |
| For International Students | /use-case/for-international-students | ✅ 已上线 | 双语对照笔记；学术词汇包；写作模板；10 语言支持 |
| For Online Learners | /use-case/for-online-learners | ✅ 已上线 | Coursera/edX/YouTube 异步学习；模块摘要；跨平台整合 |
| For Students with ADHD | /use-case/for-adhd-students | ✅ 已上线 | 分块摘要；视觉主题图；音频复习脚本；精简闪卡 |

> **原文档错误**：2026-05-06 版标注 /for-international-students、/for-online-learners、/for-adhd-students 为「❌ 缺失」，实际已全部上线。

---

## 二、各身份页详情

### 2.1 Graduate Students（研究生）— P1

**URL**: /use-case/for-graduate-students

**痛点**：同时管理研讨会、TA 职责、导师会议和论文截止日期；反馈和论点容易丢失；跨学期/跨年度的知识连续性差；文献综述综合耗时巨大（单一综述耗时 20-50 小时）。

**ThetaWave 能力**：
- 录制导师 Check-in → 反馈按论文章节整理，附修改要求和行动项
- 研讨会笔记按发言人论点和引用文献自动整理
- **跨学期论文知识库**：可搜索的知识存档，支持按章节/主题/时间线检索
- Infographic Generator：可视化论文结构（Introduction → Literature → Methods → Results → Discussion）
- 文献综述综合：多 PDF 上传 → 统一笔记，标注方法、样本量、主要发现、理论框架
- Podcast Generator：将文献笔记转为播客，通勤/实验间隙听复习

**Proof**：文献综述速度 3× 提升；PhD 候选人在 200+ 大学使用；平均每周节省 5 小时（会议笔记 + 研讨会准备）；Leiden University 2025 实验：AI 辅助论文获 8.5/10

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无实时讲座捕获；无结构化论文知识库；无法跨学期积累
- vs NotebookLM：免费但无闪卡/测验/思维导图输出；无法按导师反馈整理章节

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| NotebookLM | Google 背书，文档分析+Audio Overviews，免费 | 无结构化学习输出链（闪卡/测验/导图）；无实时讲座捕获 |
| Obsidian + AI 插件 | 本地知识图谱，Bidirectional Linking | 学习曲线陡；无 AI 讲座转录；需自行配置 |
| Elicit / ResearchRabbit | 文献发现+系统综述 | 非笔记工具；无讲座/会议捕获 |
| RemNote | 间隔重复+笔记 | 偏闪卡学习，非论文写作全流程 |

**关键词**: AI note taker for graduate students, thesis research tool, PhD note taking, dissertation notes AI, literature review AI, academic research notes, graduate seminar notes AI

**长尾机会**: "dissertation chapter organizer AI", "literature review matrix AI", "advisor meeting notes to action items", "PhD comprehensive exam prep notes", "academic conference notes AI"

**内链** → /use-case/research-thesis、/pdf-to-notes、/notes-generator、/mind-map-maker、/podcast-generator、/infographics-generator

---

### 2.2 International Students（国际学生）— P1

**URL**: /use-case/for-international-students

**痛点**：英语非母语环境下跟不上讲座速度（平均语速 150 wpm，非母语理解需 100-120 wpm）；多语言笔记需求；文化背景知识缺失导致课堂案例/讨论难以跟进；学术写作中英文表达不地道。

**ThetaWave 能力**：
- **Bilingual Class Notes**：原文 + 母语对照笔记，不遗漏课堂要点；支持 10 语言双向对照
- **Academic Vocabulary Packs**：课程学术词汇双语对照（含学科专属术语），同步提升学术英语
- **Case & Context Notes**：文化背景案例补充（如美国宪法案例背景、西方哲学语境），帮助理解课堂讨论
- **Academic Writing Expression Templates**：论文常用句式模板（文献综述/方法论/讨论/结论），对标 APA/MLA
- 播客生成：语言沉浸式复习，可调语速

**Proof**：10 语言支持；热门笔记涵盖 Principles of Economics、Macroeconomics、Political Economy（双语对照）

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：翻译质量好但无学科专属术语对照；无原文-译文对照笔记模式
- vs NotebookLM：支持 50 语言但无双语对照笔记；无学术词汇包；无写作模板

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| LazyAI | 100+ 语言转录+闪卡+测验 | 面向通用场景，非学生专属；无学术词汇/写作模板 |
| SumiNote | 实时转录+多语言，"International Student Advantage" | 功能偏基础；无写作模板/文化背景补充 |
| Zoc | 多语言翻译+Bloom 测验 | 付费制；无双语对照笔记模式 |
| Zoho Notebook | 80+ 语言，.edu 免费 | 通用笔记本；无学科专属学术功能 |

**关键词**: AI note taker for international students, multilingual study notes, ESL student notes AI, bilingual class notes, academic English AI, study abroad note taking, lecture translation AI

**长尾机会**: "English lecture to Chinese notes AI", "IELTS academic vocabulary study", "bilingual Cornell notes generator", "academic writing for non-native speakers AI", "TOEFL lecture note practice AI"

**内链** → /notes-generator（多语言输出）、/podcast-generator（语言沉浸）、/youtube-to-notes、/pdf-to-notes（文献对照阅读）

---

### 2.3 Online Learners（在线学习者）— P1

**URL**: /use-case/for-online-learners

**痛点**：Coursera/edX/YouTube 课程无结构化笔记；异步学习节奏难掌握，缺少外部约束；视频内容难以转化为复习材料；多平台课程（Coursera + YouTube + 独立课程）笔记分散。

**ThetaWave 能力**：
- **Module Study Summaries**：课程模块自动整理为结构化复习笔记（Week 1 → Week 8 递进式归档）
- **Live Session Review Notes**：直播课/录播课自动捕获，含关键概念和时间戳（支持 Zoom/Teams/Meet 录播导入）
- **Cross-Platform Integrated Notes**：Coursera/edX/YouTube/独立课程统一归档，按课程+模块双维度组织
- **Progress Check Notes**：学习进度自测笔记，与 Quiz Maker 联动；每周自动生成进度报告
- Chrome Extension：任意网页/YouTube 一键生成笔记
- 播客生成：通勤/运动时听课程复习

**Proof**：YouTube 输入 + Chrome Extension 一键笔记；4.8/5 App Store 评分

**vs ChatGPT / NotebookLM**：
- vs ChatGPT：无课程进度管理；无跨平台统一归档；无法生成结构化学习路径
- vs NotebookLM：免费但无 Chrome Extension 一键捕获；无进度自测功能

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| NoteGPT | YouTube 摘要+时间戳+闪卡+幻灯片 | 偏视频摘要；无跨平台统一归档；无进度管理 |
| StudyFetch | AI 导师 Spark.E + 动画视频讲解 | 偏深度互动；ThetaWave 有进度追踪+跨平台统一 |
| Studocu AI | 50M+ 学生共享笔记库 | 依赖历史笔记库；无实时/异步课程捕获 |
| Genio (Glean) | 实时转录+同步幻灯片，大学授权 | 机构采购模式；非个人学生自助工具 |
| Ainee | 开源 NotebookLM 替代 | 免费但需自部署；无 Chrome Extension |

**关键词**: AI notes for online courses, Coursera note taker AI, edX notes AI, MOOC study notes, YouTube course notes AI, online learning study tool, async course note taking

**长尾机会**: "Coursera specialization notes organizer", "Udemy course to flashcards AI", "online bootcamp study notes", "self-paced course progress tracker AI", "LinkedIn Learning notes AI"

**内链** → /youtube-to-notes、/notes-generator、/podcast-generator、/flashcard-maker、Chrome Extension

---

### 2.4 Students with ADHD（ADHD 学生）— P1

**URL**: /use-case/for-adhd-students

**痛点**：认知负荷高（需同时听讲+记笔记+保持专注——三项并行超出工作记忆容量）；传统笔记方式导致注意力分散（手写跟不上→焦虑→放弃）；长文本阅读困难（持续注意力不足）；启动困难（面对堆积的未整理笔记无从下手）。

**ThetaWave 能力**：
- **Chunked Chapter Summaries**：长章节自动拆分为短段落（每段 150-250 词），降低单次认知负荷
- **Visual Topic Maps**：知识结构可视化，替代密集文字阅读；颜色编码区分主题
- **Audio Review Scripts**：播客模式替代视觉阅读，通勤/运动/散步时听复习——将被动时间转化为学习时间
- **Short-Form Review Flashcards**：精简闪卡，单卡信息量可控（每卡 1 个概念，非多概念堆叠）
- 实时讲座自动捕获→消除「听+写」双任务竞争
- 专注模式：简化界面，减少视觉干扰

**Proof**：Tiimo 获 Apple "App of the Year 2025" 证明 ADHD 工具市场需求强劲；Bloom AI Notebook 专注 ADHD/阅读障碍设计获好评

**竞品参考**：

| 竞品 | 模式 | ThetaWave 差异化 |
|------|------|------------------|
| Bloom AI Notebook | 录音→AI 输出笔记/闪卡/测验/导图 | 功能重叠；ThetaWave 有分块摘要+精简闪卡+播客 |
| Tiimo | AI 日程规划+专注计时器 | 偏时间管理；非笔记/学习工具 |
| Dopamind | AI OS for ADHD（任务分解+专注区+习惯追踪） | 偏生活管理；非学术场景 |
| AYOA | AI 思维导图+DSA 认证（UK） | 偏思维导图；ThetaWave 覆盖笔记→复习全链路 |
| MyndMap | ADHD 综合工作台（任务+日历+计时器+笔记） | 偏生产力；学习深度不如 ThetaWave |

**关键词**: AI note taker for ADHD students, ADHD study tools AI, focus-friendly note taking, neurodivergent study app, distraction-free study AI, ADHD college note taking, executive function study tool

**长尾机会**: "ADHD lecture capture AI", "executive dysfunction study helper", "neurodivergent-friendly flashcard app", "ADHD exam prep AI", "sensory-friendly study notes"

**内链** → /notes-generator（降低认知负荷）、/podcast-generator（听复习）、/mind-map-maker（视觉学习）、/flashcard-maker（精简闪卡）

---

## 三、内链关系图（增强版）

```
/use-case/for-graduate-students
  → /use-case/research-thesis（论文全流程）
  → /pdf-to-notes（论文综合+文献综述）
  → /mind-map-maker（论文结构+文献地图可视化）
  → /infographics-generator（论文架构图）
  → /podcast-generator（文献复习播客）
  → /notes-generator（文献→结构化笔记）

/use-case/for-international-students
  → /notes-generator（多语言输出+双语对照）
  → /podcast-generator（语言沉浸+听力提升）
  → /youtube-to-notes（英文讲座+双语笔记）
  → /pdf-to-notes（文献对照阅读）
  → /flashcard-maker（学术词汇闪卡）

/use-case/for-online-learners
  → /youtube-to-notes（视频课程笔记）
  → /notes-generator（跨平台统一归档）
  → /podcast-generator（异步学习复习）
  → /quiz-maker（进度自测）
  → /flashcard-maker（模块闪卡）
  → Chrome Extension（一键捕获）

/use-case/for-adhd-students
  → /notes-generator（降低认知负荷+自动化）
  → /podcast-generator（听复习→替代视觉阅读）
  → /mind-map-maker（视觉学习+结构化）
  → /flashcard-maker（精简闪卡+微复习）
```

---

## 四、SEO 关键词（扩展版）

| 身份 | 核心关键词（3-5） | 长尾关键词（3-5） | ThetaWave 差异化 |
|------|------------------|-------------------|-----------------|
| Graduate | AI note taker for graduate students, thesis research tool, PhD note taking, dissertation notes AI, literature review AI | "dissertation chapter organizer AI", "literature review matrix AI", "advisor meeting notes AI", "PhD comprehensive exam prep", "academic conference notes AI" | 跨学期论文知识库 + 导师反馈按章节整理 + 文献综述综合 |
| International | AI note taker for international students, multilingual study notes, ESL student notes AI, bilingual class notes, academic English AI | "English lecture to Chinese notes", "IELTS academic vocabulary AI", "bilingual Cornell notes generator", "lecture translation for students", "TOEFL lecture note practice AI" | 双语对照笔记 + 学术词汇包 + 写作模板 + 文化背景补充 |
| Online Learners | AI notes for online courses, Coursera note taker AI, edX notes AI, MOOC study notes, YouTube course notes AI | "Coursera specialization notes organizer", "online bootcamp study notes AI", "self-paced course progress tracker", "Udemy course to flashcards", "LinkedIn Learning notes AI" | 跨平台统一归档 + 进度追踪 + Chrome Extension + 异步复习播客 |
| ADHD | AI note taker for ADHD students, ADHD study tools AI, focus-friendly note taking, neurodivergent study app, distraction-free study AI | "ADHD lecture capture AI", "executive dysfunction study helper", "neurodivergent-friendly flashcard app", "ADHD exam prep AI", "sensory-friendly study notes" | 分块摘要 + 视觉主题图 + 音频复习脚本 + 精简闪卡 + 实时自动捕获 |

---

## 五、内容缺口与未覆盖身份（Content Gap Analysis）

### 5.1 当前覆盖度

| 状态 | 身份 | 竞争强度 | 搜索量潜力 | 建议 |
|------|------|----------|-----------|------|
| ✅ 已覆盖 | 研究生、国际学生、在线学习者、ADHD 学生 | — | — | 优化页面深度 + 补充竞品对比 |
| ❌ 未规划 | **非传统学生**（成人学习者/职业转换者/返校生） | 低（无专用工具） | 中（长期增长） | P2 评估 |
| ❌ 未规划 | **第一代大学生**（First-Gen） | 低 | 中-高（政策关注度高） | P2 评估 |
| ❌ 未规划 | **残障学生（广义）**：阅读障碍/听力障碍/视力障碍/行动障碍 | 低-中（细分工具存在） | 中 | P2 评估 |
| ❌ 未规划 | **高中生/大学预科**（AP/IB/A-Level） | 中（Knowt/Cognito 覆盖） | 高 | P2 评估 |

### 5.2 非传统学生（Non-Traditional Students）— 值得关注的赛道

**为什么值得做**：
- 美国 40%+ 本科生年龄超过 25 岁
- 痛点独特：工作-学习-家庭三重平衡；距上次正式学习多年，学习技能生疏；需要高效时间管理型笔记
- 竞品空白：无专用 AI 学习工具瞄准此人群

**关键搜索词**："adult learner study tools", "back to school note taking AI", "working student study app", "career changer study notes"

**建议**：P2 → 若现有 4 个 identity 页表现好，可建 `/use-case/for-non-traditional-students`

### 5.3 第一代大学生（First-Generation Students）

**为什么值得做**：
- 美国约 1/3 本科生为第一代大学生
- 痛点：缺乏家庭学习指导；不了解大学学术规范；笔记和学习策略需从头建立
- 与「国际学生」痛点在「学术适应」上有重叠但人群不同

**建议**：P2 → 可与 University Access 类非营利组织合作内容

### 5.4 残障学生（广义 Accessibility）— 与 ADHD 页的关系

当前 ADHD 页覆盖了神经多样性中的一个子集。更广义的 accessibility 需要覆盖：

| 障碍类型 | 专门需求 | 是否被现有功能覆盖 |
|----------|---------|-------------------|
| 阅读障碍（Dyslexia） | 文字→音频优先；字体/间距可调 | 部分（播客生成可覆盖） |
| 听力障碍（Deaf/HoH） | 讲座转录准确率至关重要；字幕同步 | ✅ 实时转录可覆盖 |
| 视力障碍（Visual Impairment） | 屏幕阅读器兼容；音频优先 | 待验证：需 WCAG 合规 |
| 行动障碍（Mobility） | 免手操作；语音指令 | 待验证 |
| 自闭谱系（ASD） | 可预测的界面；感官友好设计 | 部分（专注模式可覆盖） |

**建议**：P2 → 可建 `/use-case/for-students-with-disabilities`，但需要先确保产品 WCAG 合规。

### 5.5 高中生/大学预科 — 扩展考虑

AP/IB/A-Level 学生与大学生在使用场景上有 80% 重叠，但痛点差异在于：
- 更依赖教科书（非讲座）作为主要输入
- 标准化考试导向（AP Exam / IB Exam / A-Level）与大学课程考试不同
- 家长参与购买决策

**建议**：P2 → 可建 `/use-case/for-high-school-students`，目前关键词表仅有草稿条目。

---

## 六、按身份的内容营销建议

| 身份 | 博客/资源页主题（建议） |
|------|------------------------|
| **研究生** | "How AI Cuts Literature Review Time by 3×" / "PhD Student's AI Stack: Notes, Citations, Drafting" / "Advisor Meeting Notes: From Scribbles to Action Items with AI" |
| **国际学生** | "Bilingual Note Taking: AI as Your Classroom Translator" / "Academic English: AI Vocabulary Builder for ESL Students" / "Culture Shock in the Classroom: How AI Context Notes Help" |
| **在线学习者** | "Coursera + AI: Your Complete Study Workflow" / "Self-Paced Learning: How AI Keeps You on Track" / "From YouTube Playlist to Study Guide: AI Workflow" |
| **ADHD 学生** | "ADHD Study Hacks: AI Tools That Actually Work" / "Executive Dysfunction and AI: A Practical Guide" / "The ADHD Student's AI Toolkit: Notes, Focus, and Review" |

---

## 七、实施优先级矩阵

| 优先级 | 动作 | 类型 | 预期影响 |
|--------|------|------|----------|
| **P0** | 补充已上线 4 页的竞品对比块 + vs ChatGPT/NotebookLM | 页面优化 | ✅ 已完成（见上方 §2.1–§2.4） |
| **P0** | 扩展关键词表（§四）：每身份 3-5 核心 + 3-5 长尾 | SEO 策略 | ✅ 已完成 |
| **P0** | 补充已上线 4 页的 FAQ 结构化（50% 身份专属） | 页面优化 | Featured Snippet 获取 |
| **P1** | 补充已上线 4 页的 Proof 数据（搜索结果中找到的第三方数据） | 页面优化 | E-E-A-T 增强 |
| **P2** | 评估 4 个新身份页面可行性（非传统/第一代/残障/高中） | 市场调研 | 长尾覆盖 |
| **P2** | 为每个身份创建 2-4 篇博客（§六） | 内容营销 | 长尾流量 + 领域权威 |
| **P3** | 产品 WCAG 合规评估 → 支撑残障学生页面 | 产品需求 | 条件性触发 |
