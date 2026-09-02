# AI 文档（AI Documents）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Documents / 智能文档**——① **格式层**：文档从静态 PDF/DOCX 变为自带身份、权限、审计的智能实体；② **编辑器层**：AI 住在文档内部参与创作与编排。验收以格式治理、编辑器 Agent 深度、与旧格式/IDP 边界为主。本页为 **AI 文档产品 SSOT**（完整 URL 表仅此一处）；企业 OCR/字段提取（旧格式上处理）→ [ocr.md](ocr.md) + IDP 对照 §专题对照；开发者 API 文档 → [documentation.md](documentation.md)；学习向笔记 → [notes-generator.md](../education/notes-generator.md)。

**材料范围**：公开产品介绍、行业评测与报道（Gartner Document Management 2026-04、Everest IDP PEAK Matrix 2026、IDC MarketScape IDP 2025–2026）、社区讨论；**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-05-13**。

**站内对照**：**待**上线 Tools 页时与 slug **`ai-documents`**、`content/tools/*/*ai-documents.json` 对齐；当前仅知识块占位。

**Tools 关键词与 slug 映射**（待 tools-pages-config 收录后生效）：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#ai-documents-tools`](../../keywords/alignify-keywords-tools.md#ai-documents-tools)）

**站内相邻**：[documentation.md](documentation.md) · [ocr.md](ocr.md) · [legal.md](legal.md) · [spreadsheet.md](spreadsheet.md) · [knowledge-base.md](knowledge-base.md) · [notes-generator.md](../education/notes-generator.md)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **ai-documents（本页）** | **documentation** | **notes-generator** | **legal** | **spreadsheet** |
|------|--------------------------|-------------------|---------------------|-----------|-----------------|
| **核心问题** | 文档格式能否智能？编辑器能否 AI 原生？ | 开发者如何写/托管 API 文档？ | 如何把学习材料变成笔记？ | AI 如何辅助法律合同？ | AI 如何增强表格？ |
| **典型买家** | 知识工作者、企业文档负责人 | 开发者、DevRel | 学生、自学者 | 法务、律师 | 分析师、财务 |
| **交付形态** | 编辑器/文档平台/格式标准 | 文档站点生成器 | 笔记/学习平台 | 合同管理/法律研究 | 电子表格 |
| **代表见** | §外链索引 | §外链索引 **Mintlify** 等 | §外链索引 **ThetaWave** 等 | §外链索引 **Harvey** 等 | §外链索引 **Rows** 等 |

---

## 词汇锚点

- **AI 文档（AI Documents）**：两个方向交汇——① **格式层**：文档从静态文件变成自带身份、权限、审计的智能实体；② **编辑器层**：AI 参与创作与编排。与「AI 文档处理」（IDP，在现有格式上做 OCR/提取）**不同**——IDP 操作旧格式，AI 文档重构格式本身。
- **Intelligent Document / 智能文档**：文档不是死文件，而是活的 API——唯一身份、权限、审计轨迹、内建工作流（审批/签名/修订）。
- **AI-Native Editor / AI 原生编辑器**：AI 从地基嵌入编辑体验——关掉 AI 后编辑器仍完整；「侧边栏聊天框」不算原生。
- **Document-as-Infrastructure / 文档即基础设施**：文档像 API 一样可寻址、可查询、可治理——全文检索搜不到「这份 NDA 谁签过」，但 Factified 文档自带此能力。
- **IDP（Intelligent Document Processing）**：企业后台自动化——从 PDF/扫描件提取字段、分类、验证。与 AI 文档的**根本区别**：IDP 在旧格式之上，AI 文档替代旧格式。
- **Document Q&A / 文档问答**：不改变格式——在已有 PDF/DOCX/PPT 上提供自然语言问答层，答案带引用；与 IDP 批量结构化提取不同。
- **Post-PDF / 后 PDF**：PDF 为打印 fidelity 设计不为 AI 设计——「后 PDF」让新文档基础设施成为默认，而非消灭 PDF。

---

## 专题对照 / 扩展定义

Post-PDF、IDP、Document Q&A 定义见 §词汇锚点；下表只列**买家体验差**（不重复术语）。

| 维度 | **格式替代层** | **AI 原生编辑器层** | **企业 IDP 层** |
|------|---------------|---------------------|-----------------|
| **改的是什么** | 文档底层格式 | 创作体验 | 旧格式处理效率 |
| **核心动作** | 创造新格式 | 编辑器内建 AI | OCR+分类+抽取 |
| **买家** | 合规/法务/IT 架构 | 知识工作者/团队 | 后台运营/共享中心 |
| **成熟度** | 极早期（2026  surfaced） | 快速增长 | 成熟（30+ 年 OCR 遗产） |

三层是否收敛、Factify vs Notion 买家错位等社区框架 → §对比与测评；产品规格 → §外链索引。

---

## 问题域（为何会出现这类产品）

- **PDF 是 AI 时代的瓶颈**：OCR、布局分析、表格还原每一步有误差；约 3 万亿份 PDF 是 AI 自动化最大非结构化障碍。
- **编辑器里 AI 和文档分离**：2024–2025 典型体验——左边 Docs，右边 ChatGPT，手动复制粘贴。
- **文档治理靠外部工具拼凑**：起草→排版→PDF→签名→邮件→网盘，每一跳丢失元数据与权限。
- **组织需要「权威版本」**：多副本、多批注时哪一份是真的？
- **「AI 文档」搜索意图碎片化**：写作、摘要、PDF 编辑、管理——统一需求是「让 AI 和文档一起工作」。

---

## 能力栈（概念拆分，非厂商功能表）

- **格式层：身份与治理**：唯一 ID、访问控制、不可篡改审计、版本权威性——嵌入文档本身。
- **格式层：AI 可读性**：结构化到 AI 直接消费（JSON/Markdown），免 OCR 猜测。
- **编辑器层：Agent 编排**：文档内多步任务——搜索、整理、生成；运行时长与自主度见 §外链索引各产品。
- **编辑器层：上下文窗口**：整文档/整工作区 vs 当前段落——决定 Agent 能做什么。
- **编辑器层：多人 + AI 协作**：多用户与 AI 同时操作、文档不锁定。
- **生成层：模板→定制**：从角色模板到理解业务上下文的定制文档。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 专有智能文档格式，合规长在文档里 | New document standard (proprietary) | Factify |
| **B** | 开源 AI 文档格式，LF 基金会治理 | Open document standard | DocLang |
| **C** | 大用户基数工作区 + AI Agent 嵌入 | AI-native workspace editor | Notion AI |
| **D** | 从零 AI-First 编辑器/画布 | AI-first document editor | Guse、Remalt、Gixo |
| **E** | 按角色/场景垂直文档生成 | Vertical doc generator | Watto AI |
| **F** | 已有 PDF/DOCX 上问答层，不改格式 | Document Q&A / PDF chat | Humata |
| **G** | 旧格式 OCR/提取（对照，非本页主品类） | Intelligent document processing | ABBYY、Google Document AI |

**本页主轴 Type A–F**；Type G 与 [ocr.md](ocr.md) 共享流量但技术路线不同。

---

## 风险 · 合规 · 数据治理（外部框架可对照，非法律意见）

- **格式锁定与供应商依赖**：专有格式 vs 开源标准分叉风险。
- **AI 生成内容的可审核性**：Agent 自主操作 20 分钟时修改记录是否可追溯——见 §外链索引 **Guse**「每行可追踪」正面案例。
- **权限边界与越权**：Agent 连接 20+ 外部系统时的最小权限。
- **「权威版本」的法律地位**：Factify 标识在现行法下是否被法院/监管承认仍待定。
- **数据驻留与云端推理**：Notion、Coda、Guse 等 DPA 与 Schrems II 路径以各厂商为准。

---

## 落地碎片（无先后）

- 选型先判断紧迫度排序：**格式替代 / 编辑器升级 / IDP 自动化**——不可互相替代。
- 痛点是权威版本失控 → Type A/B；编辑器割裂 → Type C/D；10 万份扫描提取 → IDP/ocr，非本文。
- Notion 用户：Agent 是否够用决定要不要迁移 Guse/Remalt——迁移成本常高于功能增量。
- Factify 极早期（2026-01 stealth）——采购宜等 GA + 独立安全审计。
- 与 [documentation.md](documentation.md) 交叉：本文是**通用文档**，非 API 文档。

---

## 工具与产品类型（「AI documents」「smart documents」检索里常混；非穷举）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|--------------|------|
| **New Document Standard / Format** | 全新文档格式+嵌入式治理 | 极早期赛道 |
| **AI-Native Document Editor** | AI 嵌入编辑器，非侧边栏附加 | 与 Notion-like 检索重叠 |
| **Vertical Doc Generator** | 按角色生成 PRD/提案/法律文档 | 模板深度 × 领域知识 |
| **Open-Source Doc Conversion** | 旧格式→AI 可读结构 | IBM Docling 等桥梁 |
| **Document Q&A / PDF Chat** | 上传→问答→引用溯源 | 与 ChatPDF 类混排 |
| **Intelligent Document Processing** | 旧格式 OCR/抽取 | **对照品类**——见 [ocr.md](ocr.md) |
| **AI Writing Assistant** | 通用文本生成 | 不绑定格式/编辑器 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Factify** | A | 专有「后 PDF」标准——身份、权限、审计、内建审批/签名；$73M 种子轮（2026-01）；受监管行业 | [factify.com](https://www.factify.com/) |
| **DocLang** | B | ABBYY+IBM+Red Hat 开源格式（LF AI & Data）；语义+几何双层编码 | [lfaidata.foundation](https://lfaidata.foundation/) |
| **Notion AI** | C | 1 亿+ 用户工作空间；3.0 Agent 自主多步任务；Custom Agent 定时触发；$10–20/座/月 | [notion.so/product/ai](https://www.notion.so/product/ai) |
| **Coda AI** | C | 文档即应用，AI 融入公式/数据库；2025-10 Grammarly 收购；Doc Maker $10/创建者/月 | [coda.io](https://coda.io/) |
| **Guse** | D | 多人 AI 画布，copilot 内嵌每行；2026-02 上线 | [guse.io](https://guse.io/) |
| **Watto AI** | E | YC，PM 文档生成，20+ 集成 | [watto.ai](https://www.watto.ai/) |
| **Humata** | F | PDF/DOCX/PPT 问答，段落级引用；SOC 2；免费 60 页/月 | [humata.ai](https://www.humata.ai/) |

### 对比与测评（第三方；观点非官方）

社区框架：**格式替代 vs 编辑器升级 vs IDP 是否收敛？** 一种观点认为 Factify 与 Notion 终将同市场；另一种认为买家（合规 vs 知识工作者）、决策者、替换周期错位。

AI 原生编辑器讨论集中在**迁移成本 vs 体验增量**——Notion 存量是护城河；DocLang 讨论集中在**开源标准能否追上专有迭代**（HTML vs Flash 历史类比）。

Factify 批评：**「要更好的 PDF 编辑器，不是新格式」**——新品类教育成本。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **VentureBeat · Factify 深度**：[move past PDFs and .docx](https://venturebeat.com/infrastructure/factify-wants-to-move-past-pdfs-and-docx-by-giving-digital-documents-their)
- **Computer Weekly · DocLang 发布**：[ABBYY IBM Red Hat DocLang](https://www.computerweekly.com/blog/Open-Source-Insider/ABBYY-IBM-Red-Hat-announce-DocLang-open-source-universal-document-format)
- **IBM Docling**：[GitHub docling](https://github.com/DS4SD/docling)（Apache 2.0；Thoughtworks Radar 2025-11）
- **Gartner MQ Document Management 2026-04** · **Everest IDP PEAK 2026** · **IDC MarketScape IDP 2025–2026**（行业格局，非单品排名）

**站内**

- [documentation.md](documentation.md) · [notes-generator.md](../education/notes-generator.md) · [legal.md](legal.md) · [spreadsheet.md](spreadsheet.md) · [knowledge-base.md](knowledge-base.md) · [ocr.md](ocr.md)