# AI Tools for Lawyers（律师用 AI 工具）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Legal AI / AI for lawyers**——判例检索、合同审阅、诉讼材料与律所工作流中的 **GenAI 垂直套件**；验收以 **引用可验证性、保密/零训练、DMS 集成** 为主。本页为 **法律 AI 产品 SSOT**（完整 URL 表仅此一处）；通用文档格式/编辑器 → [ai-documents.md](ai-documents.md)；OCR/扫描件提取 → [ocr.md](ocr.md)。**本知识块不构成任何法域下的法律意见。**

**材料范围**：公开网络检索（各国律师协会伦理指引、两大法律数据库厂商公开产品页、Legaltech 媒体综述、垂直社区讨论摘要）；**未**把 Alignify 站内 Tools 正文 JSON 当作「事实来源」复述为独立论据。网摘整理日期 **2026-04-19**。

**站内对照**：[alignify.co/tools/legal](https://alignify.co/tools/legal) · `/zh/tools/legal` · `content/tools/en/legal.md`、`content/tools/zh/legal.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#legal-tools`](../../keywords/alignify-keywords-tools.md#legal-tools)）

**站内相邻**：[ai-documents.md](ai-documents.md) · [ocr.md](ocr.md) · [knowledge-base.md](knowledge-base.md)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`legal`（本页）** | **`ai-documents`** | **`ocr`** | **`knowledge-base`** |
|------|---------------------|-------------------|-----------|---------------------|
| **典型买家问题** | 判例引用是否可验证？客户材料能否进模型？ | 文档格式/编辑器如何 AI 原生？ | 扫描合同如何提文字？ | 律所知识库如何 RAG 检索？ |
| **验收核心** | 引用链、保密、伦理监督 | 格式治理、编辑器 Agent | CER、表格、部署形态 | 权限感知检索、引用粒度 |

---

## 词汇锚点

- **Legal AI / AI for lawyers**：泛指面向**律师、法务、司法机关配套业务**的大模型应用与垂直套件；英文检索常与 **legaltech**、**GenAI legal**、**contract AI**、**AI legal research** 混排。
- **Citation-grounded research**：回答需绑定**判例、成文法或二次文献库**检索结果与引用；与「开放式聊天」在未接入权威库时的 **hallucinated citation（虚构判例引用）** 相对——后者在公开发表的律师惩戒与诉讼新闻中屡次被讨论。
- **Contract intelligence / CLM adjacent**：侧重**尽职调查清单、并购合同抽取、条款比对、 playbook**；常与 **contract lifecycle management（CLM）**、电子签名栈相邻。
- **Litigation support / ediscovery**：海量披露材料中的**相关性排序、线程化、机密打码（privilege review）**；与传统 **e-discovery** 平台在数据规模与工作流程上咬合。
- **Domain-specific deployment**：是否使用**法律语料微调**、是否限制在**租户知识库（Vault/DMS）**内 **RAG**、是否禁止客户文件进入通用模型训练——企业采购尽职调查高频条款。
- **Unauthorized practice / 跨法域**：工具宣传「可替代律师意见」在各司法辖区可能触碰**无照执业**红线。

---

## 专题对照 / 扩展定义

Citation-grounded research、CLM、ediscovery 等定义见 §词汇锚点；下表只列**买家体验差**。

| 维度 | **检索 + 先例验证型** | **合同审阅 / 抽取型** |
|------|------------------------|-------------------------|
| **典型意图** | memo、动议结构、判例脉络 | 尽调清单、条款偏离市场基准 |
| **失败形态** | 引用不实、忽略不利先例 | 漏掉关键例外条款、歧义项 |
| **常与谁集成** | 判例库、citator | **Word**、**DMS**、数据室 |

| 维度 | **律所一体化 Copilot** | **垂直领域套件（如人身损害材料分析）** |
|------|------------------------|----------------------------------------|
| **买家** | 全局 IT、知识管理 | 业务组（诉讼类型） |
| **验收** | 权限、审计、多辖区 | 专用文档类型上的抽取准确率 |

出版商原生 AI（Westlaw/Lexis 类）vs 独立法律 AI 平台 vs Word 插件——架构路线见 §形态谱系；产品规格见 §外链索引。

---

## 问题域（为何会出现这类产品）

- **小时计费压力**：研究、初稿、重复性披露审查占用大量可计费时间，事务所需证明「效率提升」且**不降低监督标准**。
- **知识分布碎片化**：先例、内部先例、客户模板、监管更新分散在 **DMS**、邮件与聊天中；**RAG** 叙事承诺「可问即得」。
- **大型出版商防御**：传统判例与二次文献订阅需把 **GenAI** 嵌入既有工作流以免被通用聊天机器人替代。
- **企业法务 KPI**：合同周转天数、平均谈判轮次、统一条款库——与 **CLM** KPI 对齐。
- **法律服务可及性的「供给缺口」**：「先筛后审」（AI 初筛 → 律师复核）降低最低消费门槛。

---

## 能力栈（概念拆分，非厂商功能表）

- **检索 → 摘要 → 草稿**：从自然语言问题到**带引注结构**；中间是否强制**逐段链接至源段落**决定可信度。
- **文档比对与偏离表**：长合同版本差分、与「市场模板」或「客户 playbook」 redline。
- **多文档时间线 / 事实表**：卷宗极厚场景下的实体与日期抽取（准确率与人工抽检协议绑定）。
- **工作流 / Agent**：按 matter 类型触发清单（**playbook**）、跨工具推送——「自动化」与**监管对「监督义务」**的张力在此集中。
- **安全与隔离**：**SOC 2**、区域驻留、**BYOK**、**零训练**声明、**客户机密**与**对手方材料**隔离策略；各产品条款见 §外链索引。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 判例库/实务指南同账号 **assistant**，强调与订阅内容同源引用 | Publisher-native legal AI | Westlaw/Lexis 系 GenAI（购买路径以合同为准） |
| **B** | 跨任务一体化门户，企业合约与 Am Law 叙事 | Independent legal AI platform | Harvey、Legora |
| **C** | 单一案类超高页数卷宗与医疗记录类实体 | Practice-area litigation AI | Supio、EvenUp |
| **D** | **Word**/浏览器插件，在编辑环境完成条款建议 | Legal drafting Copilot | 各插件型 + 通用 Copilot 竞争同一编辑框 |
| **E** | 专利/IP 垂直：撰写、侵权、claim chart | Patent intelligence / IP AI | Patlytics |
| **F** | 无独立产品，通用 LLM + 自建提示 | DIY GenAI legal | 小型所常见；伦理依赖个人规范 |

**Type A vs B**：A 的引用与 citator 绑定订阅；B 跨 matter 工作流但引用验证仍须人工——社区共识 **先分清库是否自带权威引用** 再谈流畅度。

---

## 风险 · 合规 · 法律职业伦理（外部框架可对照，非法律意见）

- **美国律师协会**：约 **2024-07** 发布 **Formal Opinion 512**（胜任、保密、与客户沟通、对法庭坦诚、监督助理与费用等）——各州规则可能进一步细化。
- **虚构引用与重大诉讼**：公开报道中已有律师因提交含**不存在判例**的文书而引发纪律后果——须保留「**人工核对引用**」环节。
- **保密与跨境传输**：客户事实与策略是否进入**第三方模型**、存储区域、分包处理；**欧盟**、**英国**与**美国州**规则不一。
- **监管技术本身**：部分法域讨论**AI 辅助裁判**或**律师广告**中对 AI 的披露——与「工具辅助研究」不同层面。

---

## 落地碎片（无先后）

- 先区分 matter：**能否使用开源网页聊天处理本案材料**——多数合规手册默认**禁止或限缩**。
- 固定「**引用必点回源段落**」流程；对对手方 AI 生成文本保持**真实性**与**证据规则**视角。
- 为**初稿**加水印或版本命名（**AI 草稿**），避免误当最终版本对外提交。
- **采购 RFP** 中单列：训练数据政策、日志保留、**次级处理者**名单、**退出权**。

---

## 工具与产品类型（「AI legal」「legal AI software」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **AI legal research assistant** | 判例检索、Memo 结构、引用链 | 与 **citator**、KeyCite/Shepard's 强绑定 |
| **Contract AI / contract intelligence** | 条款标注、风险清单、比对市场基准 | 常与 M&A、采购尽调同屏 |
| **Legal drafting Copilot** | 诉状、合同首稿、文书模板 | 须适配本地诉讼规则 |
| **E-discovery + GenAI** | 相关性排序、摘要、机密筛查辅助 | 数据量与**特权**边界更敏感 |
| **Practice-area specialists** | 特定卷宗类型结构化 | 验收按案类定制 |
| **Patent / IP intelligence** | 申请辅助、侵权分析、claim chart | 与通用 legal research 检索混排 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

与站内 Tools 页 **Best Tools** 五款一致，并增补 **Patlytics**（专利/IP 垂直）。

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| **Supio** | C | 人身损害等卷宗与材料分析 AI，海量文档理解与合规安全叙事 | [supio.com](https://supio.com/) |
| **Harvey** | B | 大型律所与企业法务一体化法律 AI（助理、知识库、工作流） | [harvey.ai](https://www.harvey.ai/) |
| **EvenUp** | C | 人身损害案件效率与流程自动化 | [evenuplaw.com](https://www.evenuplaw.com/) |
| **Casetext** | A/B | 判例检索与法律研究向 AI 助手（所属集团与产品线以官网为准） | [casetext.com](https://casetext.com/) |
| **Legora** | B | 律师团队协作文档与工作区类 AI | [legora.com](https://legora.com/) |
| **Patlytics** | E | 专利情报/IP 垂直：撰写、侵权、claim chart；官网自述 SOC 2 Type II | [patlytics.ai](https://www.patlytics.ai/) |

### 对比与测评（第三方；观点非官方）

英文科技媒体与 **Legaltech** 博客在 **2025–2026** 年间大量刊登「Top AI tools for lawyers」类榜单：共识通常是——**先分清研究库是否自带权威引用与验证**，再谈回答流畅度；**合同类**工具要比拼与 **Word / 数据室** 的集成深度与**条款库**是否可审计。**Reddit** 等社区吐槽集中在「**瞎编引用**」「**客户机密能否进模型**」「**大型所 IT 一刀切禁用某些网页端**」三类，而非单一品牌的绝对排序。两大文献集团各自把 **GenAI** 捆进订阅的做法，使「独立 Casetext 式」对比在历史上成立、**现今购买路径需以合同与登录后界面为准**。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **ABA · Formal Opinion 512 背景解读**：[ABA Business Law Today · ethics overview](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-october/aba-ethics-opinion-generative-ai-offers-useful-framework/)
- **OECD · AI Principles**：[OECD Artificial Intelligence](https://www.oecd.org/en/topics/sub-issues/ai-principles.html)
- **行业媒体（观点非官方）**：LawNext、Artificial Lawyer 等对并购与产品路线跟踪——适合观察出版商整合对工具可用性的长期影响。

**站内**

- [ai-documents.md](ai-documents.md) · [ocr.md](ocr.md) · [knowledge-base.md](knowledge-base.md)