# AI Homework Helper · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI homework helper / 拍照解题**——拍照或文本输入→**答案+分步过程**的 answer-first 工具；验收以 OCR/公式识别、多步推导一致性、学科覆盖为主。本页为 **作业助手产品 SSOT**（完整 URL 表仅此一处）；苏格拉底式引导不给答案 → [ai-tutor.md](ai-tutor.md)；闪卡备考 → [ai-flashcards.md](ai-flashcards.md)；Hub → [education.md](education.md)。

**材料范围**：公开网络检索（厂商官网、App Store/Google Play、行业报告、社区评测）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-05-10**。

**站内对照**：待上线 Tools 页；候选 slug **`ai-homework-helper`**。

**Tools 关键词与意图**：待 `tools-pages-config.ts` 收录后补充锚点。

**站内相邻**：[ai-tutor.md](ai-tutor.md) · [ai-flashcards.md](ai-flashcards.md) · [education.md](education.md)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流（避免混买混评）

| slug | 典型买家问题 | AI 哲学 | 代表见 |
|------|-------------|--------|--------|
| **ai-homework-helper**（本页） | 这道题不会做，要答案 | Answer-first | §外链索引 |
| **ai-tutor** | 像家教一样引导学会 | Socratic | §外链索引 **Khanmigo** |
| **ai-flashcards** | 笔记变闪卡备考 | Retrieval practice | §外链索引 **Quizlet** |

---

## 词汇锚点

- **AI homework helper / AI 作业助手**：拍照或文本→**答案 + 分步解题**；与 AI tutor（苏格拉底）、flashcard（记忆）不同品类。
- **Photo math solver / 拍照解题**：OCR + AI 识别后生成解答——核心入口交互。
- **Step-by-step explanation / 分步解答**：合规防线——社区争议：多数学生只看最终答案。
- **Multi-subject coverage**：从 math solver 向全科演化。
- **Human tutor backup**：AI 置信度低时转真人——Gauth、Upstudy 提供。
- **Answer-first vs Socratic tutor**：本页 6 产品均属 answer-first。
- **Cognitive offloading（认知卸载）**：RAND 2025——AI 替学生完成思考 vs augmentation。

---

## 专题对照 / 扩展定义

Cognitive offloading、Answer-first 等定义见 §词汇锚点；下表只列**买家体验差**。

| 维度 | AI Homework Helper（本页） | AI Tutor | AI Flashcards | General Chatbot |
|------|--------------------------|----------|---------------|-----------------|
| **核心交互** | 拍照→答案+步骤 | 对话引导→自得出答案 | 笔记→闪卡/测验 | 手动描述问题 |
| **学术争议** | 最高 | 较低 | 低 | 取决于用法 |
| **代表见** | §外链索引 | §外链索引 | §外链索引 | ChatGPT 等 |

---

## 问题域（为何会出现这类产品）

- **家庭作业不平等**：$0–16/月 vs $100–150/小时真人辅导。
- **数学焦虑普遍**：拍照降低「完全不会」的羞耻感。
- **家长辅导能力断崖**：高中 STEM 超出多数家长。
- **中国双减溢出**：作业帮、字节将拍照搜题瞄准海外——Gauth、Question AI。
- **多模态 LLM 突破**：手写公式、几何、化学方程式可靠识别。
- **「只对答案」心态**：RAND 2025 仅 45% 认为获取直接答案是作弊。

---

## 能力栈（概念拆分，非厂商功能表）

- **题目识别（OCR + 多模态）**：手写、几何、化学式、图表轴——第一道坎。
- **解题引擎**：简单题通用 LLM；多步推导需领域微调；自测准确率差异见 §对比与测评（缺独立第三方）。
- **分步解答生成**：步骤质量参差不齐、跳步常见。
- **多模态输入**：拍照、PDF（Mathos）、手写板。
- **图形与可视化**：Desmos 级交互 vs 静态图。
- **真人导师兜底**：连接速度、水平、语言。
- **学科广度 vs 深度**：每增一科学科是新挑战。
- **抄袭检测规避**：Cluely 等极端品类法律/伦理雷区——主流产品营销回避。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 拍照为核心，OCR→答案+步骤 | Camera-first math solver | Upstudy、Gauth、Question AI |
| **B** | 对话+PDF/长文上传 | Chat+upload homework helper | Mathos、Solvely |
| **C** | 底层 GPT/Gemini API + 学科 UI | Wrapper around GPT | Answer AI、Question AI（部分） |
| **D** | 自研/微调 STEM 模型叙事 | Proprietary math model | Gauth、Solvely |
| **E** | LMS 集成（Canvas 等） | School-integrated homework AI | Solvely |
| **F** | 屏幕叠加/Canvas Agent/考试提示（极端） | Undetectable AI agent | Cluely、Einstein AI（对照，非本页主品类） |

---

## 风险 · 合规 · 学术诚信（外部框架可对照，非法律意见）

- **学术诚信**：Einstein AI 下架、Cluely a16z $15M、RAND 62% 学生用 AI 做作业仅 1/3 学校有政策。
- **AI 检测不可靠**：非英语母语误判 61.3%——检测路径根本缺陷。
- **答案正确、方法错误**：学生无法判断时内化错误方法。
- **未成年人数据**：COPPA/GDPR——拍照可能含 PII。
- **滑坡至全流程代学 Agent**：拍照→答案与 Canvas Agent 技术距离不远。
- **中国出海数据治理**：Gauth、Question AI 跨境传输在欧美学校场景的合规摩擦。

---

## 落地碎片（无先后）

- 明确需求：救急看步骤 → 本页；真正学懂 → [ai-tutor.md](ai-tutor.md)。
- 测试真实作业题：手写识别、多步推导、文字题理解。
- 有真人导师则测连接速度与水平。
- 学生/家长：先自己做→卡住再用 AI→关掉重做一遍（productive struggle）。
- 教师： redesign 评估——课堂闭卷、口头答辩；作业当练习。
- 学区采购：SDPA、SSO、数据是否进训练、COPPA/FERPA。

---

## 工具与产品类型（「AI homework helper」「math solver app」检索里常混；非穷举）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Photo math solver** | 拍照→AI 解题+分步 | vs 2010 年代题库匹配 App |
| **Multi-subject AI homework helper** | 全科覆盖 | Upstudy 改名信号 |
| **AI writing assistant for students** | 作文生成/改写 | 与解题用户心智不同 |
| **AI study companion** | 笔记+闪卡+计划 | Solvely 品牌偏此 |
| **Undetectable AI desktop agent** | 屏幕叠加、LMS 自动操作 | 超出作业帮助边界 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| **Upstudy** | A | 前身 CameraMath；拍照多学科+24/7 真人导师 | [upstudy.ai](https://upstudy.ai/) |
| **Gauth** | A/D | 字节跳动；拍照 STEM+真人+写作；App Store 1.67 亿+ 评价 | [gauthmath.com](https://www.gauthmath.com/) |
| **Answer AI** | C | 600 万+ 用户；多学科+SAT/ACT；$9.99/月 Pro | [answerai.pro](https://answerai.pro/) |
| **Question AI** | A/C | 作业帮出品；美国免费教育 Top 3 | [questionai.com](https://www.questionai.com/) |
| **Solvely** | B/E | 1000 万+ 学生；LMS 集成；$12–15.99/月 | [solvely.ai](https://solvely.ai/) |
| **Mathos** | B | YC W24；PDF 整本上传+Desmos 图形 | [mathgptpro.com](https://www.mathgptpro.com/) |

### 对比与测评（第三方；观点非官方）

**Answer-first vs 引导思考**是根本分裂——市场需求大（~200K+ 月搜）但教育界批评 cognitive offloading；Khanmigo 代表 Socratic 端但使用量远低于 answer-first。

**中国 EdTech 出海**：双减后 Gauth、Question AI 快速崛起——美国本土产品更强调 SAT/LMS。

**准确率黑箱**：Gauth 自测 96% vs ChatGPT 94% 差 2pp 且自选测试集；社区反馈简单题可接受、微积分/统计/文字题显著下降。

**免费→付费漏斗**：广告、限次数、隐藏步骤——Reddit/App Store 主要投诉。

**灰色地带**：Google Chrome Homework Help 按钮争议、Cluely「cheat on everything」—— legitimate 助手面临品牌毒性。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **RAND · Student AI Use Survey (Dec 2025)**：[rand.org](https://www.rand.org/)
- **Pew · Teens & AI (2025)**：[pewresearch.org](https://www.pewresearch.org/)
- **36氪 · 中国 AI 教育出海**：[36kr.com/p/2826118377507328](https://36kr.com/p/2826118377507328)
- **Nature · Einstein AI (Feb 2026)**：[nature.com](https://www.nature.com/articles/d41586-026-00764-w)
- **TechCrunch · Cluely (Jun 2025)** · **Futurism · Cluely CEO**
- **Stanford · AI Detector Bias** · **THE Journal · Chrome Homework Help (Sep 2025)**
- **HN**：`site:news.ycombinator.com AI homework`

**站内**

- [ai-tutor.md](ai-tutor.md) · [education.md](education.md) · [ai-flashcards.md](ai-flashcards.md)