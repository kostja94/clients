# AI Tutor（AI 家教与智能辅导）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI tutor / AI 家教**——LLM **苏格拉底式引导**（不直接给答案，追问/提示/纠偏）；验收以 next-item 正确率提升、是否可关闭直接答案、FERPA/COPPA 与 proactive 触发 engagement 为主。本页为 **AI 家教产品 SSOT**（完整 URL 表仅此一处）；拍照直接解题 → [ai-homework-helper.md](ai-homework-helper.md)；语言学习专页 → [ai-language-learning.md](ai-language-learning.md)；Hub → [education.md](education.md)。

**材料范围**：公开网络检索（厂商产品页、行业报告、EdTech 媒体、学术研究）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/ai-tutor](https://alignify.co/tools/ai-tutor) · slug **`ai-tutor`**（已收录 `tools-pages-config`）

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#ai-tutor-tools`](../../keywords/alignify-keywords-tools.md#ai-tutor-tools)

**站内相邻**：[ai-homework-helper.md](ai-homework-helper.md) · [ai-flashcards.md](ai-flashcards.md) · [ai-language-learning.md](ai-language-learning.md) · [education.md](education.md)

## 与相邻 slug 分流（避免混买混评）

| slug | 买家核心问题 | AI 哲学 | 边界 |
|------|-------------|--------|------|
| **`ai-tutor`**（本页） | AI 像家教引导学会？ | Socratic | — |
| **ai-homework-helper** | 不会做，要答案步骤 | Answer-first | 不给答案 vs 直接解题 |
| **ai-flashcards** | 笔记变闪卡记住 | Retrieval practice | 对话教学 vs 记忆工具 |
| **ai-language-learning** | 学一门语言 | 口语+课程 | 语言是子集但生态独立 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI Tutor / AI 家教**：苏格拉底式引导——反问「第一步该怎么做？」而非直接给答案；与 homework helper 品类级对立。
- **Socratic tutoring**：限制直接给答案后 next-item 正确率 +6.1%（Khanmigo 2025–2026 实验叙事）。
- **Proactive tutoring**：从被动 chat 到解题过程中主动出现——Khanmigo 2026 夏季改版；旧版仅 15% 有权限学生使用。
- **Adaptive learning path**：按掌握度、薄弱点、先修缺口动态调整。
- **Cognitive augmentation vs offloading**：RAND 2025 框架——家教设计目标应是 augmentation。
- **MTSS**：美国 K-12 分层支持——AI 家教定位 Tier 1–2 效率工具。

---

## 问题域（为何会出现这类产品）

- **人类家教不可规模化**：$40–80/小时、地域不均——AI 以 App 成本送达数十亿学习者。
- **作业助手伦理驱动替代需求**：拍照→答案引发 offloading 恐慌——Socratic 家教是「负责任 AI 教育」回应。
- **Bloom 2 sigma 问题**：一对一可提升两个标准差——AI 是最接近规模化的方案。
- **教师负担**：54 小时/周仅 49% 直接教学——Khanmigo 试点省 30–60 分钟/天。
- **推理成本暴跌**：2024–2026 ~10× 下降使多轮 Socratic 对话经济上可行。

---

## 能力栈（概念拆分，非厂商功能表）

- **教学法层**：Socratic 策略、scaffolding、错误诊断（概念性 vs 粗心）、先修检测。
- **内容层**：结构化课程库、LLM 内置知识、联网检索、教师上传。
- **交互层**：文本 chat、主动弹窗、语音（CK-12 Flexi）、Avatar（Genius Group）、手写识别。
- **学生建模层**：掌握度、遗忘曲线、情感状态、学习风格——有历史数据时 next-item +6.1% vs 仅对话 ~+2%（Khan 2026 实验结论，见 §对比与测评）。
- **Guardrails**：数学验证器、内容过滤、FERPA/COPPA——Math Agent 只验证不给答案使「直接给答案」降 50%。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **1** | 已有学习平台 + AI 辅导层 | Platform-embedded AI tutor | Khanmigo、Duolingo Video Call |
| **2** | 独立 App，AI 对话为核心 | Standalone AI tutor app | CK-12 Flexi、GoSkills AI Tutor、Genius Group |
| **3** | 完整闭环：诊断→教→练→评→调路径 | Adaptive learning system | Carnegie Learning、Century Tech、Squirrel AI |
| **4** | 标准化考试备考，题库驱动 | Test prep AI tutor | Riiid、Cognii |
| **5** | 面向教师的教学辅助（相邻） | AI teaching assistant | MagicSchool、Formative AI |

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **幻觉与错误教学**：1500 万+ 线程实验仍无法完全消除——限制「只验证已完成工作」降直接给答案 50%。
- **数据隐私**：对话/行为/情感数据比传统 EdTech 更深——FERPA/COPPA/GDPR。
- **情感依赖**：AI Avatar 加剧过度信任——MIT 2025 部分学生过度信任 AI。
- **付费层级模型差异**：免费轻量 vs 付费强模型——可能放大教育不平等。
- **EU AI Act**：教育场景 AI 高风险，2026 分阶段实施。
- **教师去技能化**：长期依赖 AI 辅导可能削弱人类诊断技能。

---

## 落地碎片（实践建议）

- 采购第一条：**能否关闭直接答案**——无此选项更接近 homework helper。
- K-12：FERPA/COPPA DPA；对话数据不进训练。
- 定位 **AI 辅导 + 教师监督**，非替代。
- 考试备考：优先有**题库溯源**的产品（Riiid）。
- 关注 **proactive vs passive**——2026 后仍纯被动 chat 可能 engagement 落后。

---

## 工具与产品类型（「AI tutor」「AI tutoring bot」检索里常混；非穷举）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| **Platform-Embedded AI Tutor** | 学习平台 + AI 层 | 内容/题库已有 |
| **Standalone AI Tutor App** | 独立对话产品 | 冷启动难、体验原生 |
| **Adaptive Learning System** | 诊断→路径闭环 | 重学习科学 |
| **Test Prep AI Tutor** | SAT/ACT/GRE/TOEFL | 提分 KPI |
| **AI Teaching Assistant** | 面向教师 | 用户是教师 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| **Khanmigo** | 1 | Khan Academy Socratic 辅导；2026 主动触发；108M+ 交互 | [khanmigo.ai](https://www.khanmigo.ai/) |
| **Carnegie Learning** | 3 | K-12 数学自适应，30+ 年学习科学 | [carnegielearning.com](https://www.carnegielearning.com/) |
| **Century Tech** | 3 | 自适应路径+干预，英国市场 | [century.tech](https://www.century.tech/) |
| **Squirrel AI** | 3 | 中国 K-12 自适应，5200 万学生叙事 | [squirrelai.com](https://www.squirrelai.com/) |
| **Riiid** | 4 | 韩国考试备考，Santa/R.test | [riiid.co](https://www.riiid.co/) |
| **Cognii** | 4 | 对话式教学评估 | [cognii.com](https://www.cognii.com/) |
| **CK-12 Flexi** | 2 | WhatsApp 内免费 K-12 家教 | [ck12.org](https://www.ck12.org/) |
| **GoSkills AI Tutor** | 2 | 企业技能培训（2025-04） | [goskills.com](https://www.goskills.com/) |
| **Genius Group** | 2 | 25 AI Avatar 导师 | [geniusgroup.net](https://www.geniusgroup.net/) |
| **Duolingo Video Call** | 1 | Max 内 Lily 角色语音对话 | [duolingo.com](https://www.duolingo.com/) |

### 对比与测评（第三方；观点非官方）

- **2026 核心分化 Socratic vs Answer-first**——Khanmigo/Carnegie/Cognii 坚持不给答案；CK-12/GoSkills 更灵活。
- **学生建模 > 对话界面**：有掌握度/先修数据 next-item +6.1%；仅对话 ~+2%——数据基础设施更重要。
- **Engagement 实验**：仅 15% 有权限学生用 Khanmigo（被动 chat）——2026 主动触发是品类关键 UX 实验。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **TBRC · AI Personal Tutors / Tutoring Bots Market 2026**（市场规模 CAGR 叙事）
- **Khan Academy · Building a Better AI Tutor**：[blog.khanacademy.org](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/)
- **RAND · Cognitive Offloading**：[rand.org](https://www.rand.org/)
- **Bloom (1984) · 2 Sigma Problem** · **EU AI Act 教育分类** · **中国教育部 AI 赋能教育行动方案 2025**
- **EdWeek Market Brief 2026 · 教师对 AI 家教态度**

**站内**

- [ai-homework-helper.md](ai-homework-helper.md) · [education.md](education.md) · [ai-language-learning.md](ai-language-learning.md)