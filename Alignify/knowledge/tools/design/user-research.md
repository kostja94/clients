# AI User Research · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI User Research**——AI 主持访谈、合成用户、主题分析等**定性研究**加速；验收以 **洞察深度、可行动性、合规** 为主。本页为 **工具 URL 表 SSOT**。设计稿生成 → [design/](design.md) 各子 slug；问卷/分析/录屏等 adjacent 见 §与相邻 slug 分流。

**材料范围**：公开网络检索；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 2026-05-13。

**站内对照**：[alignify.co/tools/user-research](https://alignify.co/tools/user-research) · slug **`user-research`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（[`#user-research-tools`](../../keywords/alignify-keywords-tools.md#user-research-tools)）

---

## 与相邻 slug 分流

| 维度 | user-research（本页） | survey | analytics | session-recording |
|------|--------------------------|--------|-----------|-------------------|
| 典型买家问题 | 用户为什么流失？怎么理解功能？ | NPS/满意度几分？ | 哪页跳出率最高？ | 用户点了哪里？ |
| 交付形态 | AI 主持访谈、合成用户、定性报告 | 在线问卷+统计 | 事件追踪+漏斗 | 录屏+热图 |
| 验收核心 | 洞察深度与可行动性 | 样本量与显著性 | 数据准确性 | 回放完整性与隐私 |
| AI 介入点 | AI 代替访谈员、合成受访者、主题提取 | AI 生成问卷 | AI 异常检测 | AI 会话摘要 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **AI-moderated interview**：LLM 驱动对话代理代替人类研究员主持访谈——进行中即语义理解，非仅录播回看。
- **Synthetic users / AI personas**：LLM/multi-agent 模拟目标用户——**可对话**；285 项硅样本对比仅约 25% 与人类相似，65% 显著分歧——适合早期假设，非替代战略决策真人数据。
- **AI thematic analysis**：开放题/访谈文本自动聚类、情感标注、代表性引用——可能放大「流利但空洞」偏差。
- **Multi-agent research system**：Composer→Interview→Research→Reviewer 等分工——ListenLabs 四代理流水线。
- **Continuous discovery**：从项目制转为始终在线——AI 主持使操作上可行。
- **AI-native vs AI-added**：Outset/ListenLabs/Conveo/Trooly 从零构建 vs UserTesting/Maze/Qualertics 叠加 AI——架构与定价逻辑本质不同。
- **Laddering**：逐层追问「为什么」——User Intuition 自称 5–7 级。
- **Synthetic panel**：持久 AI 人设样本组——Qualtrics 2026 X4 合成消费者 Panel（2 亿+ 受访者数据训练）。

---

## 专题对照 / 扩展定义

**三类 AI 研究能力**（术语见 §词汇锚点；下表只列价值与风险差）

| 维度 | AI 主持访谈 | 合成用户 | AI 辅助分析 |
|------|-----------|---------|------------|
| 数据来源 | 真人 | AI 模拟 | 已有素材 |
| 核心价值 | 真人在说什么，10–100× 加速 | 低成本探索「若问 1000 人」 | 消化已有数据 ~80% 提速 |
| 最大风险 | 误读情绪/微妙信号 | 与真人系统性偏离 | 流利度偏差/幻觉引用 |
| 适合决策 | 战术到战略 | 早期探索、脚本压测 | 辅助分析，判断在人 |
| 代表 | Outset, ListenLabs, Conveo, Trooly | Aaru, Atypica, Synthetic Users | Dovetail, Condens, Looppanel |

---

## 问题域（为何会出现这类产品）

- **定性研究规模化瓶颈**：传统深度访谈 8–20 人、3–6 周、$500–$5,000/次——产品迭代速度远超交付。
- **「为什么」被「是什么」压制**：问卷/analytics 给行为，不给动机——AI 将定性成本 ~$487 拉低至 ~$22/次。
- **非研究人员民主化**：66% 团队研究需求增长，PM/市场 increasingly 主导——需低门槛 AI 工具。
- **研究员角色转型**：从操作者到战略家——AI 接管转录、编码、模式识别。
- **合成用户填补难招募人群**：高净值、罕见病、竞品用户、敏感话题——合规前提下补充路径。
- **持续发现从理想到可行**：人工招募+主持+分析成本使「每周对话」不现实——AI 主持首次使节奏可行。

---

## 能力栈（概念拆分，非厂商功能表）

- **访谈主持深度**：浅/中/深（3/5/8 分钟）；freeform vs structured。
- **多模态采集**：文本/语音/视频；副语言信号；屏幕共享（可用性）。
- **语言与文化覆盖**：40–100+ 语言；文化适配>语言翻译。
- **合成用户构建源**：社交数据 vs 深度访谈 vs 人口统计 vs 第三方研究（Qualtrics 2 亿+）。
- **分析粒度**：高亮→聚类→跨会话模式→报告→可交互 Research Hub。
- **质量控制**：低效回答标记、合成校准、幻觉检测、欺诈检测。
- **招募与 Panel**：ListenLabs 3000 万+、User Interviews/Prolific、BYOP。
- **交付物自动化**：转录→摘要→高亮→PPT/视频→可搜索仓库。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | AI 主持访谈平台 | Outset、ListenLabs、Conveo、Trooly |
| **B** | 合成用户 / AI Persona | Aaru、Atypica、Synthetic Users、Bulker |
| **C** | AI 辅助分析 / 研究仓库 | Dovetail、Condens、Looppanel |
| **D** | AI-Enhanced 传统平台 | UserTesting、Qualtrics、SurveyMonkey |
| **E** | 垂直行业定制 | 医疗患者、金融客户等 |

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **合成用户与真实决策**：285 项元分析仅 25% 一致——Forrester 预测 2026 至少两起丑闻。不用于高风险最终决策。
- **AI 访谈过度披露 PII**：ACM CHI 2026——纯手动编辑 PII 减少仅 2.6%，AI 后编辑 41.2%。
- **LLM 推断敏感属性**：从无害回复推断收入/病史——误用风险真实。
- **流利度偏差**：LLM 偏好清晰表达——可能遗漏不善言辞的真知。
- **训练数据隔离**：逐项核对零训练、SOC 2/ISO 范围。
- **全球监管碎片化**：欧盟 AI 法案、中国算法备案、美国州法。
- **知情同意在 AI 场景不足**：须额外理解谁在问、数据如何处理、可否要求人类复核。

---

## 落地碎片（无先后）

- 从最混乱项目验证，非厂商 demo；并行试点 AI vs 传统。
- 三类边界：AI 主持=真人说什么；合成=快速扫射；AI 分析=消化已有数据。
- 合成用户：不用于最终决策；用于脚本压测、极端人群。
- 工具栈 2–3 个 specialist，非单一平台。
- 检查模型训练政策与企业零训练合同。
- 为非研究员写内部研究手册——何时用 AI、如何写目标、如何解读、常见陷阱。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **AI-moderated interview platform** | AI 主持+追问+分析 | ≠ 录播后人工分析 |
| **Synthetic user platform** | AI 模拟受访者 | ≠ 静态 persona 文档 |
| **AI research repository** | 上传→转录编码 | 人类仍是访谈者 |
| **Traditional + AI layer** | 问卷/测试+AI | 适合已有合同团队 |
| **Continuous discovery platform** | 始终在线流水线 | 依赖 AI 主持 |
| **Multi-agent research system** | 多 agent 分工 | ≠ 单一模型包办 |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Outset** | YC S23；AI 主持视频/语音/文字；$17M A；Microsoft/Nestlé/Uber | [outset.ai](https://outset.ai/) |
| **ListenLabs** | 多代理；$100M/$500M 估值；100 万+ AI 访谈 | [listenlabs.ai](https://listenlabs.ai/) |
| **Conveo** | YC S24；50+ 语言；$5.3M Seed | [conveo.ai](https://conveo.ai/) |
| **Dialogue AI** | $6M Seed；实时对话式访谈 | [dialogueai.com](https://www.dialogueai.com/) |
| **Trooly** | 45 分钟深度定性；共情引擎；1.8 亿受访者覆盖 | [trooly.ai](https://www.trooly.ai/) |
| **Maze** | AI-first 产品发现；Figma 集成 | [maze.co](https://maze.co/) |
| **UserTesting** | 老牌+AI 转录/情感；2026 收购 User Interviews | [usertesting.com](https://www.usertesting.com/) |
| **User Intuition** | 400 万+样本；5–7 层 laddering；$20/次 | [userintuition.ai](https://www.userintuition.ai/) |
| **Perspective AI** | 深度追问「为什么背后的为什么」 | [getperspective.ai](https://getperspective.ai/) |
| **Stratify** | YC；即时招募+动态访谈 | [stratify.ai](https://stratify.ai/) |
| **Aaru** | 合成用户；$1B 估值；选举预测案例 | [aaru.com](https://aaru.com/) |
| **Atypica** | 30 万+ AI 虚拟消费者；特赞旗下 | [atypica.ai](https://atypica.ai/) |
| **Synthetic Users Inc.** | 多代理角色访谈 | [syntheticusers.com](https://www.syntheticusers.com/) |
| **Bulker** | 20 角色<60 秒；免费层 | [bulker.ai](https://www.bulker.ai/) |
| **Dovetail** | 研究仓库+AI 转录/主题/语义搜索 | [dovetail.com](https://dovetail.com/) |
| **Condens** | 定性仓库+AI 分析 | [condens.io](https://condens.io/) |
| **Looppanel** | AI 笔记与摘要 | [looppanel.com](https://www.looppanel.com/) |
| **Great Question** | 招募+运营+AI 合成 | [greatquestion.co](https://greatquestion.co/) |
| **Qualtrics** | XM 巨头；2026 合成 Panel+Research Hub | [qualtrics.com](https://www.qualtrics.com/) |
| **SurveyMonkey** | 问卷+AI 生成/情感分析 | [surveymonkey.com](https://www.surveymonkey.com/) |
| **Discuss** | Forrester Wave 2026 领导者 | [discuss.io](https://www.discuss.io/) |
| **Sprig** | 产品内微问卷+AI 分析 | [sprig.com](https://sprig.com/) |
| **Hotjar** | 热图+录屏+AI 摘要 | [hotjar.com](https://hotjar.com/) |

### 对比与测评（第三方；观点非官方）

2026 结构性分裂：**AI-Native**（Outset/ListenLabs/Conveo/Trooly）卖速度×深度 vs **AI-Added**（Qualtrics/UserTesting）卖合规与集成。正面：参与者对 AI 更坦诚（Conveo 83%）；负面：情绪细微度仍是人类护城河。合成用户争议最大——Aaru 选举预测 vs 消费品类可复现性存疑；行业共识=探索加速器非决策替代品。定价：User Intuition ~$200/研究 vs ListenLabs ~$50K–$200K+/年。

*非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- Maze · Future of User Research Report 2026
- Forrester Wave™ Experience Research Platforms Q1 2026
- Insights Association Q4 2025：AI 主持量首超人类
- ACM CHI 2026 · Disclose with Care（AI 访谈 PII）
- MeasuringU · Review of Experiments with Synthetic Users
- User Intuition · AI-Native vs AI-Added (2026)