# 大模型训练数据平台 · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网与产品文档、融资新闻、TechCrunch/The Information 等行业报道、Research and Markets / IDC 类市场摘要、Anthropic/OpenAI 公开 RLHF 说明、arXiv 预印本）；归纳 **AI 训练数据平台 / AI training data infrastructure**——为 LLM 与多模态模型采购、生产、质检与交付可训练语料的全栈系统，覆盖数据标注 Lab、标注 MLOps 平台、授权语料市场、合成数据管线。**未**引用 Alignify 站内文章或站内 JSON 内容稿。具体定价、合同条款与数据许可以各官网为准。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/ai-training-data](https://alignify.co/blog/ai-training-data) · [alignify.co/zh/blog/ai-training-data](https://alignify.co/zh/blog/ai-training-data) · 正文 md 已同步至部署仓 `alignify-by-kostja/content/blog/{en|zh}/ai-training-data.md` · slug **`ai-training-data`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#ai-training-data-tools`](../../product/alignify-keywords-tools.md#ai-training-data-tools)）· `keywordEn`: **AI Training Data Platform** · `keywordZh`: **大模型训练数据平台（底层：AI训练数据基础设施）

## 与相邻 slug 分流

| 维度 | **ai-training-data（本文）** | **web-scraping** | **evaluation** | **inference-infrastructure** |
|------|------------------------------|------------------|----------------|-------------------------------|
| 核心问题 | 怎么**采购/生产/交付**可训数据 | 怎么**抓取**网页/API 原始数据 | 怎么**评测**已训模型/应用 | 怎么**部署运行**模型 |
| 典型读者 | AI Lab、MLOps、数据平台负责人 | 数据工程师、Agent 开发者 | AI 工程师、QA | 平台架构师 |
| 交付形态 | 标注集、RLHF 偏好对、授权语料包、多模态数据 API | 原始 HTML/JSON、托管 scrape API | 评分报告、在线监控 | 推理端点、GPU 集群 |
| 验收核心 | 质量 rubric、版权链、规模、模态覆盖 | 抽取准确率、合规 | 基准通过率、幻觉率 | tok/s、$/1M tokens |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 训练数据 / AI Training Data**：用于预训练、微调（SFT）、对齐（RLHF/DPO）或专用任务适配的标注或授权语料——与「推理日志」「评测基准集」不同：训练数据进入模型权重，评测数据不进入权重。与 web-scraping 的区别：后者交付 raw 抓取结果，训练数据平台交付 **已质检、有许可、可版本化** 的数据产品。
- **数据标注 / Data Labeling**：人工或半自动地为原始样本打标签——分类、边界框、转写、偏好排序（A/B 更好）等。中文检索「数据标注」流量最大；与「AI训练数据」在 B2B 采购语境下常同指，但训练数据平台还包含 **合成、授权采购、交付 API** 等超出纯标注的能力。
- **RLHF 数据 / RLHF Training Data**：人类反馈强化学习所需的 **偏好对**（chosen/rejected）、排序或 rubric 评分数据——供奖励模型（RM）或 DPO 类对齐训练使用。高端 Lab（Scale AI、Surge AI）的核心溢价在于 **专家标注员 + 复杂 rubric + 保密流程**。
- **Human-in-the-Loop（HITL）**：人在环路的质检与迭代——模型辅助预标注，人工修正与 adjudication。训练数据平台的经济性取决于 HITL 比例：全人工贵但质量稳，全合成便宜但分布漂移风险高。
- **Licensed Training Data / 授权训练数据**：权利已 cleared 的语料——创作者授权、出版社许可或企业自有数据合同化交付。Wirestock、Luel、Origin Lab 等代表 **版权可审计** 的采购路径，与未授权爬取形成对立叙事。
- **Multimodal Training Data / 多模态训练数据**：跨文本、图像、视频、音频、3D、机器人轨迹的统一或分模态数据包——视频生成与世界模型（World Model）推动该子赛道 2024–2026 快速分化。
- **Synthetic Training Data / 合成训练数据**：由模型或规则引擎生成的训练样本——Snorkel 等以 **programmatic labeling** 降低人工成本。风险：合成数据可能放大母模型偏见，需与真实数据混合与分布监控。
- **Training Data Marketplace / 训练数据市场**：连接数据供给方（创作者、专家、机构）与模型方的双边平台——Wirestock 等以 **marketplace + 许可层** 差异化，而非单纯外包劳动力。
- **Data Provenance / 数据血缘**：样本来源、标注员、版本、许可条款的可追溯链——EU AI Act 与企业 AI 治理推动 provenance 从「合规附件」变为 **采购硬门槛**。

---

## 专题对照 / 扩展定义

| 二分维度 | A 方向 | B 方向 |
|------|------|------|
| **供给模式** | **Enterprise Lab**（Scale AI、Surge AI）：全托管项目制，Lab 出 rubric + 人力 | **Self-serve Platform**（Labelbox、Encord）：客户自建项目，平台提供工具与工作流 |
| **数据来源** | **Human-labeled**（偏好、边界框、转写） | **Synthetic / Programmatic**（Snorkel、规则+弱监督） |
| **权利模型** | **Licensed / Rights-cleared**（Luel、Origin Lab、Wirestock） | **Scraped / Public**（常与 web-scraping 重叠，**非**本文主路径） |
| **模态** | **Text / RLHF**（Surge、Scale） | **Video / 3D / Robotics**（Encord、Origin Lab） |
| **买家阶段** | **Pre-training / SFT**（大规模通用语料） | **Post-training / Alignment**（高难偏好与红队数据） |

---

## 问题域（为何会出现这类产品）

- **闭源高质量语料枯竭叙事**：头部模型厂商公开表述训练数据已高度筛选，新能力竞争转向 **专有数据、对齐数据、多模态稀缺资产**——催生独立训练数据采购与生产市场。
- **RLHF 与对齐成本刚性**：对齐阶段单位 token 的人工成本远高于预训练 crawl——Surge AI、Scale AI 等 Lab 模式将 **专家劳动力 + 流程保密** 产品化。
- **多模态与世界模型数据缺口**：文本标注成熟，**视频时序、3D 资产、机器人轨迹、游戏交互日志** 仍缺标准化供应链——Origin Lab、Encord 等向垂直模态延伸。
- **版权与诉讼压力**：未授权爬取面临集体诉讼与许可谈判——**rights-cleared** 采购（Luel、Human Native、Wirestock）成为 Lab 与媒体公司的合规选项。
- **自建标注团队的隐性成本**：招募、培训、质检、流失、多语言覆盖——中大型企业发现 **外包 Lab + 平台工具** 的 TCO 低于纯自建，除非数据为最高核心机密。
- **合成数据的工程拐点**：弱监督与 LLM 辅助标注使 **10× 样本效率** 在部分任务可达，但生产环境仍需 golden set 与人工 adjudication——Snorkel 类平台填补「规模化 programmatic labeling」。
- **Agent 与物理 AI 的新需求**：工具调用轨迹、环境交互、failure recovery 日志——训练数据从「静态 QA 对」扩展到 **过程级（process-level）** 数据。

---

## 能力栈（概念拆分，非厂商功能表）

- **采集与入库**：原始媒体上传、API 拉取、与 object storage 对接 → 版本化 dataset snapshot。
- **标注工作流**：任务分配、预标注（model-assisted）、双人复核、adjudication、inter-annotator agreement（IAA）统计。
- **RLHF / 偏好管线**：prompt 库管理、side-by-side 比较、rubric 培训、专家 tier 分级、anti-gaming 检测。
- **质检与验收**：gold 题目插入、速度/一致性异常检测、按 locale 与 domain 分层验收。
- **合成与增强**：规则程序、弱监督、LLM 生成补充样本；需与真实分布对照监控。
- **许可与合规**：合同模板、opt-in 证明、PII 脱敏、区域数据驻留、审计导出。
- **交付与集成**：SDK/API 导出至训练框架（PyTorch、Hugging Face、自定义）；与 **evaluation** 闭环——同一 rubric 可用于训前验收与训后回归。

---

## 形态谱系（与具体品牌解耦）

- **Type I — Enterprise Labeling Lab（纯 Lab）**：买家购买「项目结果」而非软件席位。核心能力：复杂 rubric、专家网络、保密与驻场。代表定位：Scale AI、Surge AI、Appen（传统众包向 AI 升级）。
- **Type II — Labeling Platform + MLOps**：买家在平台上自建项目，可选托管劳动力。核心能力：工作流、自动化 QA、与训练 pipeline 集成。代表：Labelbox、Encord。
- **Type III — Licensed / Creator Marketplace**：从创作者或机构采购 **权利 cleared** 的内容包。核心：许可链、定价透明、双边网络。代表：Wirestock、Luel。
- **Type IV — Multimodal / Vertical Data Pack**：按行业或模态打包（视频、3D、游戏、医疗影像）。代表：Origin Lab、Encord（视频-heavy）。
- **Type V — Synthetic / Programmatic Data**：以程序与弱监督生成标签，降低人工比例。代表：Snorkel AI、Defined.ai。
- **Type VI — Robotics / Physical AI Data**：真实世界轨迹、teleop、sim-to-real 配对——与 world-model、具身智能需求交汇。

---

## 风险 · 合规 · 数据治理（外部框架可对照，非法律意见）

- **版权与训练权**：即使「公开网页」也不等于可自由用于训练——采购需 **书面许可** 与 jurisdiction 法律评估；marketplace 产品应索取 provenance 文档。
- **PII 与敏感内容**：标注员接触原始数据带来泄露面——需 VPC 标注、脱敏 pipeline、最小权限与 NDAs。
- **标注员劳动伦理**：低薪众包 vs 专家 Lab 的声誉风险——欧盟与美国对 AI 供应链尽职调查趋严。
- **数据偏见与代表性**：采样偏差会固化到模型——需 stratified sampling 与 demographic audit（尤其面向消费级模型）。
- **供应商锁定**：专有标注工具格式、难迁移的 rubric 历史——最低防护：导出开放格式（JSONL/Parquet）与版本快照。
- **合成数据幻觉循环**：多轮 synthetic-only 微调可能导致 **模型 collapse**——与真实数据混合并监控分布漂移。
- **跨境传输**：训练数据常含多国 PII——需确认 DPA、SCCs 与区域标注中心。

---

## 落地碎片（无先后）

- 先定义 **任务级 rubric**（什么算「更好回答」）再选供应商——无 rubric 的 RFP 只会比较单价。
- 建立 **50–200 条 gold 集** 用于供应商试标与 ongoing QA——与 evaluation 页的 golden dataset 概念同源。
- RLHF 项目采用 **tier 标注员**（普通 / 专家 / 红队）分层计价，避免单一费率导致质量倒挂。
- 版权敏感领域（媒体、出版、游戏资产）优先 **Licensed marketplace** 路径，scraping 仅作 research 而非生产默认。
- 多模态项目验收 **帧级 + 事件级** 双指标——仅框精度不足以支撑视频生成训练。
- 合同写入 **数据删除与模型卸载条款**（客户终止后标注缓存如何处理）。
- 训后与训前用 **同一 rubric 子集** 做回归——链向 evaluation 工具形成闭环。

---

## 工具与产品类型（「data labeling」「AI training data」「RLHF data」检索常混在一起的品类；非穷尽）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Enterprise RLHF Lab** | Scale AI、Surge AI | 项目制、高保密、专家偏好数据 |
| **Crowd + Enterprise 混合** | Appen | 传统数据标注巨头向 GenAI 延伸 |
| **标注平台 / MLOps** | Labelbox、Encord | 自建工作流 + 可选劳动力 |
| **Creator / Licensed Marketplace** | Wirestock、Luel | 授权内容、创作者网络 |
| **Multimodal Data Pack** | Origin Lab | 视频/3D/游戏向训练包 |
| **Synthetic / Programmatic** | Snorkel AI、Defined.ai | 弱监督与合成标签 |
| **Raw Scrape 管道** | Firecrawl、Bright Data 等 | 见 [web-scraping.md](../web-data/web-scraping.md)，**非**训练交付终点 |

---

## 外链索引（工具与平台；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Scale AI** | 头部 AI 训练数据 Lab，服务 RLHF、自动驾驶、政府与 enterprise；Meta 等大客户公开合作报道频繁 | [scale.com](https://scale.com) |
| **Surge AI** | 高质量 RLHF 与 expert labeling，定位 premium alignment data | [surgehq.ai](https://www.surgehq.ai) |
| **Labelbox** | 训练数据平台 + 标注工作流 + 模型辅助标注，面向企业自建数据迭代 | [labelbox.com](https://labelbox.com) |
| **Encord** | 视频与多模态标注平台，医疗与计算机视觉场景强 | [encord.com](https://encord.com) |
| **Wirestock** | 创作者向 AI 训练数据 marketplace，许可与分成模式 | [wirestock.io](https://wirestock.io) |
| **Luel** | Rights-cleared 训练语料采购，强调版权可审计 | [luel.ai](https://www.luel.ai) |
| **Origin Lab** | 多模态训练数据（视频/3D/游戏等）打包交付 | [originlab.ai](https://www.originlab.ai) |
| **Snorkel AI** | Programmatic labeling 与数据-centric AI 平台 | [snorkel.ai](https://snorkel.ai) |
| **Appen** | 全球性数据标注与 AI 数据服务 | [appen.com](https://www.appen.com) |
| **Defined.ai** | AI 训练数据 marketplace（含 speech 等） | [defined.ai](https://defined.ai) |

### 对比与测评（第三方；观点非官方）

2024–2026 年 **AI training data** 从「Scale 一家独大」演变为 **四条 Lane 并行**：Lab（Scale/Surge）、Platform（Labelbox/Encord）、Licensed marketplace（Wirestock/Luel/Origin Lab）、Synthetic（Snorkel）。TechCrunch 等对 Surge AI、Scale AI 融资报道将品类与 **foundation model 对齐成本** 绑定——对齐数据单价远高于普通分类标注。

**买家分层明显**：Frontier lab 采购 Surge/Scale 做复杂 RLHF；中型 AI 公司在 Labelbox/Encord 上自建迭代；媒体与出版倾向 Luel/Wirestock 解决 **版权 cleared**；研究型团队用 Snorkel 做 programmatic 实验。**Wirestock** 等 marketplace 仍处早期——品牌搜索量低，品类词（AI training data platform、licensed training data）才是 SEO 主战场。

**与 web-scraping 的边界**是常见误购：抓取 API 解决「拿到 HTML」，不解决「偏好对 + 许可链 + IAA 报告」。**与 evaluation 的边界**：评测工具消费模型输出；训练数据平台生产进入权重的样本——二者应 rubric 对齐但产品不同。

*本小节为网摘与行业观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **What is RLHF?**（AWS 文档）：RLHF 流程与 human feedback 角色说明。  
  - <https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/>
- **Training Data for AI Models — market reports**（Research and Markets / 同类机构摘要）：AI 训练数据市场规模与 CAGR 预测（引用时以报告原文为准）。
- **Alignify · Web 抓取**（知识块）：[`web-scraping.md`](../web-data/web-scraping.md)——raw 采集侧；本文是 curated 训练交付。
- **Alignify · AI 评测**：[`evaluation.md`](../llm/evaluation.md)——训后质量；本文是训前数据。
- **Alignify · AI 推理基础设施**：[`inference-infrastructure.md`](inference-infrastructure.md)——模型部署；与训练数据为上下游。
- **Alignify · 世界模型**：[`world-model.md`](../world-model.md)——多模态/视频训练需求场景。
