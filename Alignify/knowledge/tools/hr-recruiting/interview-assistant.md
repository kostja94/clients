# AI 面试助手 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI interview assistant / 面试助手**——用 LLM / speech / CV+JD 结构化输入，帮助**候选人**演练或帮助**招聘方**筛选、出题、摘要、排程；核心分界是 **prep-only（备考）** vs **live session copilot（实时场边提示）**。本页为 **面试助手 SSOT**（完整 URL 表仅此一处）；雇主侧招聘 → [recruiting.md](recruiting.md)；通用会议记录 → [note-taker.md](../productivity/note-taker.md)。

**材料范围**：公开网络检索（厂商官网、第三方评测、行业对比文、Reddit/Blind 社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 2026-05-10。

**站内对照**：[alignify.co/tools/interview-assistant](https://alignify.co/tools/interview-assistant) · `content/tools/en|zh/interview-assistant.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#interview-assistant-tools`](../../keywords/alignify-keywords-tools.md#interview-assistant-tools)）

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI interview assistant（本文件所指）**：泛指用 **LLM** / **speech** / **CV + JD（job description）** 结构化输入，帮助**候选人**演练或帮助**招聘方**筛选、出题、摘要、排程的一类工具；边界取决于「**prep-only（备考）**」还是「**live session copilot（实时场边提示）**」。
- **Mock interview**：模拟问答、计时、多轮追问；可纯 **AI**，也可「真人工程师 + 匿名」**peer** 模式。
- **Live copilot / real-time assist**：面试进行中由 AI 实时听写、生成回答建议、浮窗提示——是品类中争议最大、伦理风险最高的子类。核心叙事围绕「**undetectable / stealth / invisible**」——包括屏幕共享不可见、任务管理器不可见、无 dock 图标、全局热键（`⌘+B` / `Ctrl+B`）、击键事件屏蔽、click-through overlay、透明浮动窗口等。
- **Behavioral / STAR**：情境 **Situation**、任务 **Task**、行动 **Action**、结果 **Result**；常见与领导力原则类问题绑在一起练故事库。
- **Technical screen**：算法、**system design**、岗位栈深挖、**take-home** 复盘等；常与 **IDE**、**whiteboard**、**OJ（online judge）** 生态相邻。coding copilot 子类是 live copilot 中检索量最高的细分——Interview Coder 专注此场景，宣称 97,000+ 用户。
- **Follow-up question handling**：live copilot 的进阶能力——AI 不仅回答第一问，还能在面试官追问时保持上下文、处理 trade-off 分析和边界情况。
- **Credits-based pricing**：区别于月订阅的一次性信用点模式——ParakeetAI（$29.50/3 小时，永不过期）、LockedIn AI（credits vs unlimited 双轨）采用此模式，降低低频用户的付费门槛。
- **Adverse impact / disparate impact**：自动化筛选对受保护群体选取率显著偏低等风险；雇主侧选型常对照监管指引做 **audit**（非法律意见，见延伸阅读）。

---

## 专题对照 / 扩展定义

**Prep vs Live Copilot vs Post-Interview**——术语定义见 §词汇锚点；下表只列**买家问题、伦理风险、定价特征**。

| 维度 | Mock / Prep 型 | Live Copilot 型 | Post-Interview 分析型 |
|------|---------------|-----------------|----------------------|
| **典型买家问题** | 「我想练 STAR 故事但找不到人 mock」 | 「面试官问的题我不会，想有个东西提示我」 | 「面完了不知道自己哪里表现不好」 |
| **交付形态** | Web/App 端题库 + AI 评分 + 录音回放 | 桌面端 stealth overlay + 实时 ASR + LLM 推理 | 录音 → 转写 → 逐题打分 → 改写建议 |
| **伦理风险** | 低（等同于买本面试书） | 极高（多数公司明文禁止，可能构成作弊） | 低（事后复盘，不介入面试过程） |
| **代表产品** | Final Round AI Mock、LockedIn AI Mock | Interview Coder、LinkJob、ParakeetAI、Final Round AI Copilot | LockedIn AI Post-Interview Reports |
| **定价特征** | 免费增值或低价月付 | $30–$150/月 或 lifetime $500–$800 | 通常与 copilot 捆绑 |

**与相邻品类分界**：**AI note taker**（[note-taker.md](../productivity/note-taker.md)）与 post-interview 分析型有功能重叠——但 note taker 面向通用会议，interview assistant 面向面试场景优化（STAR 结构评分、JD 对齐检查）。**AI recruiting**（[recruiting.md](recruiting.md)）买家是雇主，interview assistant 买家是候选人——是招聘炉子的两端。

---

## 问题域（为何会出现这类产品）

- **面试反馈黑洞**：绝大多数公司在拒信后不提供任何反馈——AI mock 工具填补了这个信息真空。
- **真人 mock 成本高、协调难**：peer mock 平台虽然存在，但匹配耗时且质量方差大。AI mock 7×24 可用、几乎零边际成本。
- **技术面平台碎片化**：HackerRank、CodeSignal、CoderPad、LeetCode、公司自建 OJ——每种平台的题型风格、时间压力、IDE 体验不同。coding copilot 工具的「屏幕捕获 + 多平台兼容」正是对这一碎片化的回应。
- **「开口说」的练习壁垒**：很多候选人（尤其是非母语者）的面试障碍不在于「不知道答案」，而在于「无法在压力下用自然口语流畅表达」。
- **信息不对称**：**JD** 与实际考察点漂移；AI 常被用来「对齐 JD ↔ 题库 ↔ 简历亮点」做 **RAG** 式检索增强。

---

## 能力栈（概念拆分，非厂商功能表）

- **JD + 简历 → 定制问题库**：生成追问链、缺口提示；本质是提示工程 + 私有资料 **RAG**（若允许上传公司材料则涉密）。
- **语音 / 视频表现分析**：**filler words**、语速、结构分块、眼神/停顿（若启用摄像头则敏感）。
- **实时 ASR + 上下文推理**：live copilot 的核心技术链——面试官语音 → ASR 转写 → LLM 理解问题意图 → 结合简历/JD 上下文 → 生成结构化回答。延迟是关键指标（ParakeetAI 宣称 2-5 秒，见 §外链索引）。
- **Stealth / 隐蔽性技术栈**：OS 级窗口属性操作、全局热键注册、键盘事件拦截与伪装、click-through overlay、进程隐藏、dock/taskbar 无图标——术语见 §词汇锚点 **Live copilot**；各产品投入差异见 §外链索引「对比与测评」。
- **编码与系统设计**：沙盒跑用例、提示 **trade-offs**、对照标准答案 rubric；coding copilot 子类专做屏幕截图→代码分析→解题方案。
- **面试后复盘**：转写、逐题打分、改写「第二版回答」草稿——与 **AI note taker** 相邻。
- **多模态输入**：live copilot 产品通常同时处理音频（ASR）和屏幕（截图/OCR），coding 场景还需识别 IDE 中的代码上下文。
- **个性化上下文注入**：简历上传 + JD 粘贴 → 模型在生成答案时锚定候选人的真实经历和岗位要求。
- **招聘流程自动化**：聊天机器人初筛、自动约面、**ATS** 插件式评分——与「个人备考 **coach**」不是同一产品族，但常被同一检索词扫到。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 候选人 · 练习型：mock、STAR 打磨、technical 题库 | AI mock interview | Final Round AI Mock、LockedIn AI Mock、HackerRank |
| **B** | 候选人 · 实时 copilot：stealth overlay + 实时 ASR | Interview copilot / live assist | Interview Coder、LinkJob、ParakeetAI、Final Round AI Copilot |
| **C** | 候选人 · 求职全栈平台：以 copilot/mock 为入口扩展简历/投递 | Career job search platform | LockedIn AI、Final Round AI Job Hunter |
| **D** | 招聘方 · 评估型：结构化问卷、视频分析、代码评测 | Recruiter / TA automation | HackerEarth 等 B2B 向工具 |
| **E** | 真人 peer / 专家网络：非 LLM 主体，与「面试练习」检索意图重叠 | Peer mock / expert network | interviewing.io 等 |

**Type B 子类**：通用 copilot（Final Round AI、LockedIn AI、LinkJob、ParakeetAI）vs coding 专项 copilot（Interview Coder）。

---

## 风险 · 合规 · 诚信（外部框架可对照，非法律意见）

- **诚信边界与检测军备竞赛**：行业文章常区分「考前 **prep**」与「**live** 场边代答」；后者在多数公司与考场规则下可能构成作弊或合同违约。Interview Coder 明确标注在 Amazon Chime 上可被检测。
- **美国语境**：**EEOC** 对招聘中算法与 **AI** 的不当影响、**ADA** 与测评工具等有公开指引（见延伸阅读）；雇主仍可能对供应商工具的歧视性后果承担责任。
- **数据最小化**：简历、录音、摄像、屏幕录像的留存、训练用途、跨境传输、删除导出——应单独同意与 **DPA** 视角审视。ParakeetAI 宣传「不记录 interview session、转录后自动删除」，可作为隐私差异化的选型维度。
- **偏见与可解释性**：评分是否可审计、是否披露 **AI** 参与决策；候选人是否有救济渠道。
- **live copilot 的法律灰色地带**：目前多数法域没有专门针对「面试中使用 AI 辅助」的立法——但雇主 offer letter 中常含诚信条款。

---

## 落地碎片（无先后）

- 先定义场景：**校招海投** vs **社招精准岗** vs **转码** vs **高管行为面**——再选「练表达」还是「补硬技能」。
- 若用 **live** 辅助：先读目标公司 **Code of conduct** / 面试条款；技术面注意平台差异——Interview Coder 在 Zoom/Teams/Discord 可用但在 Amazon Chime 上可被检测。
- **反馈闭环**：同一故事用不同 **prompt** 追问 3 次，比刷 30 道浅题更有用；录音回听比只看文字稿更接近真实压力。
- 选 copilot 工具时优先关注隐蔽性维度而非功能列表——如果屏幕共享不 invisible、任务管理器可见、dock 有图标，再好的 AI 模型也没意义。
- 对于低频面试者（每年 1-3 次），credits-based 定价比月订阅更划算；高频面试者可考虑 lifetime license（Interview Coder $799、LinkJob $699，见 §外链索引）。
- mock 和 copilot 可以组合使用：mock 阶段练表达和思维框架，copilot 仅在真实面试中用作安全网。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| **Final Round AI** | B/C | 面试 Copilot（实时提示 + stealth）+ Mock 练习 + AI Job Hunter 全栈；定价 Free–$500/年 | [finalroundai.com](https://www.finalroundai.com/) |
| **LinkJob AI** | B | 桌面端实时 copilot，专注科技与金融面试；100+ 模型可选，6 种隐蔽机制 | [linkjob.ai](https://www.linkjob.ai/) |
| **LockedIn AI** | B/C | 求职全栈平台：Copilot（42+ 语言）+ Mock + 简历/LinkedIn 优化 + Job Tracker；credits/unlimited 双轨 | [lockedinai.com](https://www.lockedinai.com/) |
| **Interview Coder** | B | Coding 面试专项 copilot；97K+ 用户，20+ 隐蔽操作，LeetCode Hard 秒解；lifetime $799 | [interviewcoder.co](https://www.interviewcoder.co/) |
| **ParakeetAI** | B | 轻量实时 copilot；转写准确度（59+ 语言）和低延迟（2-5s）；credits 制 $29.50 起，永不过期 | [parakeet-ai.com](https://www.parakeet-ai.com/) |
| **HackerRank** | A | 技术向 **AI-powered mock interviews** 等练习入口 | [hackerrank.com/mock-interviews](https://www.hackerrank.com/mock-interviews) |
| **HackerEarth** | D | 招聘侧 **AI interview assistants** 类工具盘点 | [hackerearth.com/blog/best-ai-interview-assistants](https://www.hackerearth.com/blog/best-ai-interview-assistants) |

### 对比与测评（第三方；观点非官方）

招聘社区与职业向博客里的共识大致分三路：**模拟面试 / STAR 打磨**、**实时 Copilot / 浮窗**（争议最大）、**求职全栈平台**。

**Mock / Prep 路线**：多被描述为「省掉找 peer mock 的协调成本」，差评集中在模板化、与本公司题库风格不符。Final Round AI 的 audio-first 模式（强制开口录音而非打字）在社区评价中优于纯文本 mock。

**Live Copilot 路线**：Reddit/Blind 类讨论里常被警告——测评平台、银行与科技厂的**诚信条款**是否允许屏幕外提示，优先级往往高于「模型准不准」。五款产品在隐蔽性上形成了明确的竞争梯度：Interview Coder 以 20+ 隐蔽操作领先；LinkJob 以 6 种独立隐蔽机制紧随；ParakeetAI 主打轻量和转写准确度而非隐蔽性竞赛。

**Coding 专项**：技术岗对比文常把 Interview Coder 与 LeetCode、HackerRank、interviewing.io 真人模拟放在一张表：AI 胜在 7×24 可用、便宜，真人/专家反馈胜在追问像真面试官。

定价与隐私方面，第三方横评常见提醒是：简历与录音是否**默认**用于模型改进、是否可一键删除会话——与雇主 **NDA** 冲突的案例在论坛里偶被提起。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- **EEOC · AI 与算法公平倡议**：[eeoc.gov/newsroom/eeoc-launches-initiative-artificial-intelligence-and-algorithmic-fairness](https://www.eeoc.gov/newsroom/eeoc-launches-initiative-artificial-intelligence-and-algorithmic-fairness)
- **EEOC · 面向工人的歧视与 AI（PDF）**：[Employment Discrimination and AI for Workers (PDF)](https://www.eeoc.gov/sites/default/files/2024-04/20240429_Employment%20Discrimination%20and%20AI%20for%20Workers.pdf)
- **EEOC · ADA 与测评中的软件/AI**：[Artificial Intelligence and the ADA](https://www.eeoc.gov/eeoc-disability-related-resources/artificial-intelligence-and-ada)
- **社区诚信讨论**：[Interview Coder 2.0 争议与检测风险分析](https://leetcopilot.dev/blog/interview-coder-controversy-risks-ethical-alternatives)