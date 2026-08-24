# AI 文档（AI Documents）· 知识块（非线性笔记）

**材料范围**：公开产品介绍（Factify、DocLang、Notion、Coda、Guse、Watto AI、Humata 等）、行业评测与报道（Gartner Magic Quadrant for Document Management 2026-04、Everest Group IDP PEAK Matrix 2026、IDC MarketScape IDP 2025–2026）、社区讨论与竞品拆解；归纳「文档格式替代」「AI 原生编辑器」「IDP 企业文档处理」「文档问答/智能分析」四个子层的边界与交叉。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-05-13**。

**站内对照**：**待**上线 Tools 页时与 `slug` **`ai-documents`**、`content/tools/*/*ai-documents.json` 对齐；当前仅知识块占位。

**Tools 关键词与 slug 映射**（待 tools-pages-config 收录 slug **`ai-documents`** 后生效）：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#ai-documents-tools`](../../keywords/alignify-keywords-tools.md#ai-documents-tools)）

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流

| 维度 | **ai-documents（本文）** | **documentation** | **notes-generator** | **legal** | **spreadsheet** |
|------|--------------------------|-------------------|---------------------|-----------|-----------------|
| **核心问题** | 文档格式能否是智能的？编辑器能否内置 AI？ | 开发者如何写/托管 API 文档？ | 如何用 AI 把学习材料变成笔记？ | AI 如何辅助法律合同/合规？ | AI 如何增强表格分析？ |
| **典型产品** | Factify, Notion AI, Coda, Guse | Mintlify, ReadMe, GitBook | ThetaWave, NotebookLM | Ironclad, Casetext, Chamelio | Claude in Excel, Equals |
| **买家** | 知识工作者、团队、企业文档负责人 | 开发者、DevRel 团队 | 学生、自学者 | 法务、律师、合规官 | 分析师、财务、运营 |
| **交付形态** | 编辑器 / 文档平台 / 格式标准 | 文档站点生成器 | 笔记应用 / 学习平台 | 合同管理 / 法律研究 | 电子表格 / 数据分析 |

---

## 词汇锚点

- **AI 文档（AI Documents）**：在本文中指两个方向的交汇——① **格式层**：文档本身从静态文件（PDF/DOCX）变成自带身份、权限、审计日志的智能实体；② **编辑器层**：AI 不再侧边栏聊天，而是住在文档内部、参与创作与编排。与「AI 文档处理」（IDP，企业在现有格式上做 OCR/提取）**不同**——IDP 操作的是旧格式，AI 文档重构的是格式本身。
- **Intelligent Document / 智能文档**：Factify 和 DocLang 的核心叙事——文档不是死文件，而是活的 API。自带唯一身份标识（谁是权威版本？）、权限控制（谁可以看哪段？）、审计轨迹（谁在何时做了什么？）、内建工作流（审批/签名/修订不依赖外部工具）。
- **AI-Native Editor / AI 原生编辑器**：与「旧编辑器 + AI 插件」不同——AI 从地基开始嵌入编辑体验。Notion AI Agent 可自主运行 20 分钟完成多步任务，Guse 的 AI copilot 内嵌在每一行而非侧边栏，Coda 将 AI 融入公式与数据库层。判断标准：关掉 AI 功能后编辑器是否仍完整？如果只是「加了个聊天框」，不算原生。
- **Document-as-Infrastructure / 文档即基础设施**：Factify CEO Matan Gavish 提出的概念——文档不应是孤立的文件，而应像 API 一样可寻址、可查询、可治理。全文检索搜不到「这份 NDA 谁签过」的答案，但 Factified 文档自带这个能力。
- **IDP（Intelligent Document Processing / 智能文档处理）**：企业后台自动化赛道——用 AI 从现有 PDF/扫描件中提取字段、分类、验证。代表：ABBYY、Hyperscience、Rossum、Google Document AI。与「AI 文档」的**根本区别**：IDP 在旧格式之上工作，AI 文档在替代旧格式。两者共享买家预算池但走不同技术路线。
- **Document Q&A / 文档问答**：不改变文档格式也不修改文档内容——AI 在已有文档之上提供自然语言问答层。用户上传 PDF/DOCX/PPT，用自然语言提问（「第三章的实验方法是什么？」「这份合同的终止条款在哪？」），AI 返回带引用的答案（精确到段落/页码）。代表：Humata、ChatPDF。与 IDP 的区别：IDP 是「从 100 万份文档中提取结构化数据」，文档问答是「理解少量文档的语义内容并回答自由形式问题」——前者面向后台批量处理，后者面向知识工作者阅读/研究。
- **Post-PDF / 后 PDF**：Factify 和 DocLang 共用的叙事框架——PDF 诞生于 1991 年，为打印 fidelity 设计，不为 AI 设计。全球约 3 万亿份 PDF 在流通，但没有一份自带身份、版本或权限。「后 PDF」不是消灭 PDF，而是让新的文档基础设施成为默认——就像 PDF 当年替代纸质传真。

---

## 专题对照 / 扩展定义

| 维度 | **格式替代层**（Factify, DocLang） | **AI 原生编辑器层**（Notion AI, Coda, Guse） | **企业 IDP 层**（ABBYY, Google Doc AI, Rossum） |
|------|-------------------------------------|-----------------------------------------------|--------------------------------------------------|
| **改的是什么** | 文档的底层格式 | 文档的创作体验 | 文档的处理效率 |
| **核心动作** | 创造新格式 | 在编辑器里建 AI | 在旧格式上提取/分类 |
| **技术路径** | 新文档标准 + 嵌入式治理 | LLM + Agent 编排 + 编辑器架构 | OCR + 视觉模型 + 分类器 |
| **买家** | 企业合规/法务/IT 架构 | 知识工作者/团队/创作者 | 后台运营/共享服务中心 |
| **代表叙事** | "PDF is digital stone" | "AI lives inside the doc" | "Touchless processing" |
| **成熟度** | 极早期（2026 才浮出水面） | 快速增长（Notion 3.0, Coda AI） | 成熟市场（30+ 年 OCR 遗产） |

---

## 问题域（为何会出现这类产品）

- **PDF 是 AI 时代的瓶颈**：PDF 为 1991 年的打印机设计，不为 2026 年的 AI Agent 设计。AI 要读一份 PDF——需要 OCR、布局分析、表格还原——每一步都有误差。3 万亿份 PDF 是 AI 自动化最大的非结构化数据障碍。
- **编辑器里 AI 和文档是分离的**：2024–2025 的典型体验——左边 Google Docs，右边 ChatGPT 窗口，手动复制粘贴。用户在两个界面间来回跳，AI 看不到文档全貌，文档不知道 AI 干了什么。AI 原生编辑器的核心命题是把这两个世界合并。
- **文档治理靠外部工具拼凑**：一份合同的典型生命周期——Google Docs 起草 → Word 排版 → PDF 定稿 → DocuSign 签名 → 邮件分发 → 网盘归档。每一跳丢失元数据、权限、版本。「文档即基础设施」用一份活的文档替代这整条链。
- **组织需要「权威版本」**：当一份 PDF 被邮件转发了 5 次、存在 3 个网盘里、被 12 个人各自批注过——哪一份是真的？Factify 的「每份文档自带唯一身份」直接回答这个问题。
- **「AI 文档」搜索意图碎片化但总量巨大**：用户搜「AI文档」可能想要 AI 写作、AI 摘要、AI PDF 编辑器、AI 文档管理——没有一个统一品类名，但有统一需求：「让 AI 帮我和我的文档一起工作」。

---

## 能力栈（概念拆分，非厂商功能表）

- **格式层：身份与治理**：文档唯一 ID、访问控制规则、不可篡改审计日志、版本权威性——这些能力嵌入文档本身而非依赖外围系统（Factify 的核心壁垒）。
- **格式层：AI 可读性**：文档结构化到 AI 能直接消费的程度（JSON/Markdown 语义输出），不再需要 OCR 猜测。DocLang 的「语义+几何双层编码」和 IBM Docling 的「文档→结构化转换」解决同一问题。
- **编辑器层：Agent 编排**：AI 在文档内执行多步任务——Notion AI Agent 可自主搜索、整理、生成长达 20 分钟；Coda 的 AI 融入公式层进行数据驱动决策。
- **编辑器层：上下文窗口**：AI 能看到的是「整个文档/整个工作区」还是「当前段落」？Notion 的 Agent 可跨页面操作，Guse 的 AI 可搜索网络并带回文档——上下文粒度决定 AI 能做什么。
- **编辑器层：多人 + AI 协作**：Guse 的「首个完全多人 AI 画布」——多个用户和一个 AI 同时在同一文档上操作，AI 不锁定文档。
- **生成层：模板→定制**：从 Watto AI 的「按角色生成 PRD/GTM 策略」到 Gixo 的「结构化商业文档全流程」，AI 文档生成的进化方向是从填空模板走向理解业务上下文。

---

## 形态谱系（与具体品牌解耦）

- **新文档格式标准（专有）**：创建全新的文档格式——不是文件，是自带计算与治理能力的实体。代表：Factify（Factified 格式）。买家是受监管行业（银行、保险、法律），卖点是「合规长在文档里」。
- **新文档格式标准（开源）**：社区驱动的 AI 文档格式规范，编码语义+布局+权限。代表：DocLang（ABBYY+IBM+Red Hat，LF AI & Data 基金会）。买家是需要供应商中立性的企业和 ISV。
- **通用 AI 原生编辑器**：以大用户基数为前提，将 AI Agent 嵌入已有的文档/笔记/工作区。代表：Notion AI（1 亿+ 用户基础）。卖点是「你已经在用 Notion，AI 现在住进去了」——零迁移成本。
- **下一代 AI-First 编辑器**：从零开始以 AI 为设计原点的文档工具。代表：Guse（AI 画布）、Remalt（视觉 OS）、Gixo（商业文档全流程）。卖点是「不修补旧编辑器，直接重建 AI 时代的文档体验」——更激进，但存量用户迁移成本是致命短板。
- **垂直文档生成器**：针对特定角色/场景的 AI 文档生成。代表：Watto AI（PM 文档）、Gixo（法律/提案/简报）。卖点是「不管文档怎么写，只管文档写什么」——模板深度 × 领域知识 = 竞争力。
- **文档问答/智能分析型**：不创建新格式也不修改编辑器——在用户已有的 PDF/DOCX/PPT 之上提供自然语言问答层。核心能力是引用溯源（答案精确到段落/页码）和多文档跨文件对比。代表：Humata（ChatGPT for your files，SOC 2 Type II）。买家是研究人员、学生、法务、分析师——需要快速理解和提取文档内容而非创作或编辑文档。
- **IDP 平台（对照，非本文主品类）**：企业级文档提取与分类——不碰格式，不碰编辑器，专注「从 100 万份 PDF 里自动提取发票字段」。代表：ABBYY、Hyperscience、Google Document AI。与本文品类不同但共享「AI+文档」搜索流量。

---

## 风险 · 合规 · 数据治理（外部框架可对照，非法律意见）

- **格式锁定与供应商依赖**：Factify 的专有格式一旦被采用，组织在事实上面临「Factify 或破产」的单点依赖。DocLang 的开源路线降低了这一风险，但开源标准的分叉和碎片化是另一重风险。
- **AI 生成内容的可审核性**：当 AI Agent 在文档内自主操作（Notion AI Agent 运行 20 分钟），生成的修改记录是否可追溯？决策依据是否可解释？Guse 的「每行 AI 修改可追踪」是正面案例——但多数产品未做到同等粒度。
- **权限边界与越权**：AI Agent 连接到 Google Suite、Slack、CRM 等 20+ 外部系统时（Watto AI），权限最小化原则是关键——AI 对每个集成是只读还是可写？能否以用户身份跨系统操作？
- **「权威版本」的法律地位**：Factify 声称文档自带「权威版本」标识——但在现行法律框架下，法院和监管机构是否承认这个标识？美国版权局 2026 年 3 月明确拒绝纯 AI 作品版权登记——AI 文档的法律地位同样待定。
- **数据驻留与云端推理**：Notion、Coda、Guse 均为云端产品——文档内容是否经 AI 厂商的推理端点？日志保留多久？GDPR/Schrems II 下欧盟企业客户的合规路径以各厂商 DPA 为准。

---

## 落地碎片（无先后）

- 选型第一步不是比功能，是判断你的组织在「格式替代」「编辑器升级」「IDP 自动化」三个层级中的**紧迫度排序**——解决不同问题，不可互相替代。
- 如果你的核心痛点是「找不到文档的权威版本」「NDA 发出后失控」——看格式替代层（Factify/DocLang）。如果是「编辑器体验割裂，AI 和文档在两个窗口」——看 AI 原生编辑器层（Notion AI/Guse/Coda）。如果是「10 万份扫描件需要提取数据」——那是 IDP 的活，不是本文范畴。
- Notion 用户：AI Agent（3.0+）是否满足需求决定了要不要迁移。如果 Notion AI 够用，别为了「更 AI 原生」迁移到 Guse/Remalt——迁移成本远高于功能增量。
- Factify 目前处于极早期（2026-01 才出 stealth），**采购决策应等待 GA 版本 + 独立安全审计**后再做。可作为「未来 12–18 个月文档基础设施方向」的关注对象。
- Guse、Remalt、Watto AI 均为早期产品，功能和定价不稳定——建议以免费试用验证核心工作流，不以官网营销页为采购依据。
- 与 [documentation.md](./documentation.md)（开发者文档工具）交叉：本文覆盖的是**通用文档**（合同、提案、笔记、知识库），不是 API 文档生成。

---

## 工具与产品类型（「AI documents」「AI document tools」「smart documents」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|--------------|------|
| **New Document Standard / Format** | Factify, DocLang | 创建全新文档格式；极早期赛道 |
| **AI-Native Document Editor** | Notion AI, Coda AI, Guse, Remalt | AI 嵌入编辑器体验，非侧边栏附加 |
| **Vertical Doc Generator** | Watto AI (PM docs), Gixo (business deliverables) | 按角色/场景生成特定类型文档 |
| **Open-Source Doc Conversion** | IBM Docling | 旧格式→AI 可读的转换桥梁 |
| **Document Q&A / PDF Chat** | Humata, ChatPDF | 上传文档→自然语言问答→带引用溯源 |
| **Intelligent Document Processing** | ABBYY, Hyperscience, Rossum, Google Document AI | 对照品类——在旧格式上做 AI 处理 |
| **AI Writing Assistant** | Jasper, Copy.ai, ChatGPT | 通用文本生成——不绑定文档格式/编辑器 |

---

## 外链索引（工具与产品；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Factify** | 专有「后 PDF」智能文档标准——每份文档自带身份标识、访问权限、不可篡改审计日志、内建审批/签名/修订工作流；CEO Matan Gavish（斯坦福 PhD / 希伯来大学教授）；$73M 种子轮（Valley Capital Partners 领投，2026-01）；目标银行/保险/法律/HR 等受监管行业；Pittsburgh 为美国运营中心 | [factify.com](https://www.factify.com/) |
| **DocLang** | ABBYY + IBM + Red Hat 联合发起的开源 AI 文档格式标准（LF AI & Data 基金会治理）；编码语义含义+几何布局，嵌入隐私/提取/训练权限等治理控制；2026 年 ABBYY Ascend 大会发布，ABBYY FineReader beta 已演示 | [LF AI & Data](https://lfaidata.foundation/) |
| **Notion AI** | 1 亿+ 用户的通用 AI 工作空间——Notion 3.0（2025-09）内置 AI Agent，可自主运行长达 20 分钟的搜索/整理/生成任务；3.3（2026-02）推出 Custom Agent 支持定时触发；$10–20/座/月 | [notion.so/product/ai](https://www.notion.so/product/ai) |
| **Coda AI** | 文档即应用——AI 融入公式层与数据库层；2025-10 被 Grammarly 收购后 Coda Brain 整合入 Superhuman Go；Doc Maker 计费模式（$10/创建者/月，编辑者免费）；适合定制工作流和表格级数据场景 | [coda.io](https://coda.io/) |
| **Guse** | 「首个完全多人 AI 画布」——AI copilot 内嵌在每一行（非侧边栏），支持自主网页搜索与一键导出幻灯片；2026-02 上线；编辑器从零以 AI 为设计原点，非旧编辑器+插件 | [guse.io](https://guse.io/) |
| **Watto AI** | YC 项目——AI 文档生成 for 产品经理；20+ 集成（Google Suite、Notion 等）；自动生成 PRD、GTM 策略、发布沟通文档；代表「按角色生成文档」的垂直方向 | [watto.ai](https://www.watto.ai/) |
| **Humata** | 「ChatGPT for your files」——上传 PDF/DOCX/PPT 后自然语言问答，每句答案精确引用到源文档段落和页码；支持多文档跨文件对比、OCR、笔记导出；SOC 2 Type II，AES-256 加密；免费 60 页/月，Expert .99/月 | [humata.ai](https://www.humata.ai/) |

### 对比与测评（第三方；观点非官方）

社区与行业分析中较常见的对比框架：**「格式替代 vs 编辑器升级 vs IDP」三层是否最终会收敛？**一种观点认为 Factify 和 Notion 最终会进入同一市场——文档的格式和编辑体验本就是一体两面。另一种观点认为两者走不同路径：Factify 的买家是合规/法务（关心不可篡改的权威记录），Notion 的买家是知识工作者（关心创作流畅度），两者的产品哲学、购买决策者、替换周期完全错位。

关于 AI 原生编辑器的讨论集中在**迁移成本 vs 体验增量**：Notion 的存量用户基础是巨大的护城河——Guse 和 Remalt 即使 AI 体验更好，也需要等用户「愿意为 AI 原生体验放弃已有工作区」。关于 DocLang 的讨论集中在**开源标准能否追上专有格式的迭代速度**——历史案例（HTML vs Flash、ODF vs OOXML）提示开源标准的胜率取决于是否有足够多的重量级实现者（IBM + Red Hat 是关键变量）。

针对 Factify 的批评主要来自**实用性**：「我需要一个更好的 PDF 编辑器，不是一个新的文档格式。」这是典型的新品类教育成本——用户还不知道问题的根本在于格式本身，而非编辑器。*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **Factify 官方**：[factify.com](https://www.factify.com/)；VentureBeat 深度报道 [Factify wants to move past PDFs and .docx](https://venturebeat.com/infrastructure/factify-wants-to-move-past-pdfs-and-docx-by-giving-digital-documents-their)
- **DocLang 发布**：ABBYY Ascend 2026 发布报道 [ABBYY, IBM & Red Hat announce DocLang](https://www.computerweekly.com/blog/Open-Source-Insider/ABBYY-IBM-Red-Hat-announce-DocLang-open-source-universal-document-format)
- **IBM Docling**：GitHub [docling](https://github.com/DS4SD/docling)（Apache 2.0，37K+ stars）；Thoughtworks Technology Radar 2025-11 收录
- **Gartner Magic Quadrant for Document Management**（2026-04）：15 家核心厂商评估
- **Everest Group IDP PEAK Matrix 2026**：32 家厂商评估，10 家 Leader
- **IDC MarketScape IDP 2025–2026**：18 家厂商评估，8 家 Leader
- **能力相邻知识块**：[documentation.md](./documentation.md)（开发者文档工具）、[notes-generator.md](./notes-generator.md)（AI 笔记生成）、[legal.md](./legal.md)（AI 法律工具）、[spreadsheet.md](./spreadsheet.md)（AI 表格工具）、[knowledge-base.md](./knowledge-base.md)（AI 知识库）
