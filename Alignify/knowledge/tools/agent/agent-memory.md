# AI Agent 记忆层 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Agent Memory Layer / Agent 记忆层**——嵌入 Agent 运行时的持久化记忆中间件，从对话/工具输出中提取事实并在后续 turn 检索注入；验收以 **跨会话 recall、temporal validity、与 RAG/平台 Memory 的可移植性** 为主。本页为 **Agent Memory 产品 SSOT**（完整 URL 表仅此一处）；个人第二大脑 → [memory.md](../enterprise-knowledge/memory.md)；企业 RAG → [knowledge-base.md](../enterprise-knowledge/knowledge-base.md)；OpenClaw 本地 Markdown 记忆 → [openclaw-alternatives.md](openclaw-alternatives.md)。

**材料范围**：公开网络检索（Mem0、Zep/Graphiti、Letta/MemGPT、Supermemory、Cognee、LangMem、MemU、MemOS、claude-mem、agentmemory 等厂商文档与 GitHub；LongMemEval/LoCoMo/BEAM 基准与 arXiv 论文摘要）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/agent-memory](https://alignify.co/blog/agent-memory) · slug **`agent-memory`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#agent-memory-tools`](../../product/alignify-keywords-tools.md#agent-memory-tools)）

---

## 与相邻 slug 分流

| 维度 | **agent-memory（本文）** | **memory** | **knowledge-base** | **openclaw-alternatives** |
|------|--------------------------|------------|--------------------|---------------------------|
| **买家问题** | 给 Agent **跨会话持久化**事实/偏好/程序性知识 | 个人/团队 **第二大脑**与笔记组织 | 企业 **文档库 RAG** 问答 | **个人助理**网关与本地 Harness |
| **时间尺度** | 跨会话、跨任务 **长期** | 长期个人知识资产 | 企业知识库版本迭代 | 会话 + 本地 Markdown 记忆 |
| **典型产品** | Mem0、Zep、Letta、MemOS | Mem.ai、Notion AI、Limitless | Glean、Notion Enterprise | OpenClaw MEMORY.md |
| **集成面** | SDK、MCP、LangGraph | App、MCP App 层 | SSO、RAG pipeline | IM 渠道 + 本地文件 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agent Memory Layer / Agent 记忆层**：嵌入 Agent 运行时与应用的 **持久化记忆中间件**——从对话/工具输出中提取事实，写入外部存储，在后续 turn 按语义/图谱/时间检索注入上下文。与「把整段 chat history 塞进 prompt」不同；与 RAG over 静态文档库也不同——记忆来自 **交互过程**，且常带 user/session/agent 作用域。
- **Persistent Memory vs Context Window**：上下文窗口是 **单次推理的工作集**；持久记忆是 **跨会话的外部存储+检索**。2026 年共识：100 万 token 窗口 **不能替代** 记忆层——会 context rot、成本线性膨胀、且无法在会话间结构化更新。
- **Episodic / Semantic / Procedural Memory**：情景记忆（发生了什么）、语义记忆（稳定事实与偏好）、程序性记忆（怎么做某类任务）——Letta core/archival/recall 即 OS 式分层。
- **Vector-first vs Graph / Temporal Graph**：向量检索擅长「像什么」；知识图谱擅长「谁与谁、何时为真」；**时序图谱**（Zep/Graphiti）追踪事实有效期——LongMemEval 的 temporal 子项是 2026 年选型关键分水岭。
- **Memory as File System（MemU）**：将记忆暴露为 **可见、可组织的文件结构**而非纯向量黑箱。
- **Memory OS（MemOS）**：把记忆当作 **可调度系统资源**（MemCube：内容+溯源+版本+治理）。
- **Coding Agent Memory**：IDE 插件/CLI 侧记忆（claude-mem、agentmemory、memento）——与 Mem0 等 **通用 memory API** 交叉但买家是开发者工作流。

---

## 专题对照 / 扩展定义

**Memory Layer vs RAG vs Platform Memory**（术语见 §词汇锚点；Type 见 §形态谱系）：

| 维度 | **Agent Memory Layer** | **Enterprise RAG / Knowledge Base** | **ChatGPT / Claude Memory** |
|------|------------------------|-------------------------------------|----------------------------|
| **数据来源** | 对话、工具输出、Agent 行为 | 上传文档、Wiki、Ticket | 平台内对话推断 |
| **买家** | Agent 平台工程师 | 知识管理、Support | 终端用户 |
| **可移植性** | 高（自建/换模型） | 中（绑企业 CMS） | 低（绑平台） |
| **代表** | Mem0、Zep、Letta | Glean、knowledge-base 页产品 | ChatGPT Memory、Claude Projects |

**架构选型四问**（产品规格与定价见 §外链索引）：

| 问题 | 偏 A | 偏 B |
|------|------|------|
| 查询类型 | 「找相似表述」→ 向量 / Mem0 免费层 | 「谁导致了什么、何时变真」→ Zep/Graphiti |
| 部署 | 托管 API（Mem0 Cloud、Supermemory） | 自托管（Letta、Cognee、AutoMem） |
| Agent 形态 | 薄 memory layer 接现有框架 | 有状态 Agent 运行时（Letta） |
| 场景 | 个性化助手 | 编码 Agent MCP 插件（claude-mem） |

---

## 问题域

- **无状态 Agent 是死路**：57% 组织已部署 Agent（2026 行业调查口径），但质量与延迟瓶颈常追溯到 **记不住** 或 **记错了**。
- **全量 context 不可扩展**：Mem0 等 benchmark 叙事： selective memory 相对 full-context 可 **~90% 降 token、~91% 降延迟**，准确率 trade-off 需按场景测。
- **品类混称**：Mem0、Letta、Supermemory App、Mem.ai、claude-mem **不可互换**——框架 vs 笔记 vs IDE 插件；采购前必须先定 **memory layer 还是 end-user 产品**（见 [memory.md](../enterprise-knowledge/memory.md)）。
- **Stars ≠ 真实采用**：选型应看 LongMemEval/LoCoMo、生产 case、MCP 部署面。
- **中国与全球双轨**：MemU、MemOS、ClawBrain、kiwi-mem 等面向中文陪伴/ proactive / 本地部署；Mem0/Zep 面向全球 Agent infra。

---

## 能力栈

- **Extract → Consolidate → Retrieve**：写入管线 + 检索管线（向量+关键词+图谱+重排）。
- **Scoped memory**：user / session / agent / team 作用域。
- **Selective forgetting**：矛盾事实更新、过期淘汰、用户删除。
- **MCP / SDK 集成**：与 [agent-skills.md](agent-skills.md) 生态衔接。
- **Hybrid retrieval**：向量 + BM25（FTS5）+ 实体链接——2026 年 coding agent 记忆标配。
- **Tiered / OS-style memory**：热上下文 vs 归档 vs 召回（Letta MemGPT）。
- **Temporal validity**：事实带时间戳与有效期——合规、金融、医疗场景倾向 Zep 类方案。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **I** | 托管 Memory API；最少 ops，按量计费 | Managed memory API | Mem0 Platform、Zep Cloud、Supermemory Cloud |
| **II** | 开源 memory layer；可自托管，接任意框架 | Open-source memory layer | Mem0 OSS、Graphiti、LangMem、Cognee、AutoMem |
| **III** | 有状态 agent framework；记忆是一等公民 | Stateful agent framework | Letta（MemGPT） |
| **IV** | IDE / coding harness memory | Coding agent memory | claude-mem、agentmemory、memento |
| **V** | Memory OS / proactive；文件系统式或 24/7 agent | Memory OS / proactive | MemOS、MemU |
| **VI** | Minimal file memory；无向量库，Markdown 即记忆 | File-based harness memory | OpenClaw `MEMORY.md` |

**Type I vs II vs III**：I 最少 ops；II 可移植+自托管；III 记忆内建于 Agent 运行时——选型四问见 §专题对照。

---

## 风险 · 合规 · 隐私

- **Memory poisoning**：恶意输入污染长期记忆——生产需校验写入、隔离 scope、审计读取。
- **PII 与 HIPAA**：Mem0 等宣称 SOC2/HIPAA——自建仍需加密、BYOK、保留策略。
- **删除是否彻底**：向量嵌入「删除」的技术可行性仍受质疑。
- **跨工具记忆孤岛**：ChatGPT Memory 不导出到 Cursor——第三方 layer 的价值在于 **可移植**。

---

## 落地碎片

- **先定 benchmark 场景**：用 LongMemEval 子集或自有 golden query set 测 hit@k。
- **Hybrid 优于纯向量**：错误码、版本号、文件路径靠 BM25；语义靠向量。
- **Memory 与 Context 分工**：即时任务上下文归 **context engineering**；跨会话用户偏好归 **agent memory**。
- **OpenClaw 用户**：Markdown 记忆足够起步（Type VI）；规模化再评估 Mem0/Supermemory MCP。

---

## 外链索引（产品 SSOT：URL + 规格 + 定价；非广告、无排序优先级）

| 名称 | Type | 公开定价（2026-06） | 部署 | 一句话 | URL |
|------|------|---------------------|------|--------|-----|
| **Mem0** | I/II | 免费层 + **$19/月** Pro + Enterprise | 托管 + OSS | Agent 记忆层；Apache-2.0；~59k stars | https://mem0.ai/ |
| **Zep / Graphiti** | I/II | 免费开发者层 + **$25/月** 起 Team | Cloud + OSS Graphiti | 时序知识图谱记忆；LongMemEval temporal 强项 | https://www.getzep.com/ |
| **Letta** | III | OSS 免费 + **Letta Cloud** 按量 | 自托管 / Cloud | MemGPT 有状态 Agent 框架 | https://www.letta.com/ |
| **Supermemory API** | I | 免费 credits + 按 memory op 计费 | Cloud + 自托管选项 | 记忆 API + MCP | https://supermemory.ai/ |
| **Cognee** | II | OSS 免费 + 企业许可 | 自托管为主 | 图+向量统一检索 | https://cognee.ai/ |
| **claude-mem** | IV | 开源免费 | 本地 Claude Code | IDE 会话/决策记忆 | https://github.com/thedotmack/claude-mem |
| **agentmemory** | IV | 开源免费 | 本地 MCP | Cursor 工作流混合检索 | https://github.com/agentmemory/agentmemory |
| **MemOS** | V | 开源 + 企业定制 | 自托管 | 记忆操作系统；MemCube；中国企业可审计 | https://github.com/MemTensor/MemOS |
| **MemU** | V | API 按量 + 开源组件 | Cloud / 本地 | Memory as File System；中文陪伴/proactive | https://memu.pro/ |

> **主榜分组**：Universal memory layer（Mem0、Zep、Letta、Supermemory API、Cognee）与 Coding agent memory（claude-mem、agentmemory）见部署仓 `/blog/agent-memory`。MemOS/MemU **仅**出现在对比表/FAQ（中国生态），**不**入主榜 EN BestTools。

### 对比与测评（第三方）

- **Atlan / AgentMarketCap 2026**：Mem0 vs Zep vs Letta vs Supermemory head-to-head；强调架构赌注不同，无 universal winner。
- **Preuve.ai AI Memory Stats 2026**：60+ 数字；ChatGPT Memory 7 亿 WAU 级部署 vs 开源框架 star 与 benchmark 对照。
- **Mem0 vs Zep（Vectorize 2026）**：向量+可选图 vs 时序图；自托管路径与定价 tier 差异。

---

## 延伸阅读 · 站内外

**站外**

- arXiv:2504.19413 — Mem0 ECAI 2025（latency/token vs full-context）
- arXiv:2501.13956 — Zep temporal knowledge graph
- Wu et al., ICLR 2025 — LongMemEval benchmark
- Maharana et al., ACL 2024 — LoCoMo
- AWS 中国区博客 — Context Engineering 与 AgentCore Gateway（context 与 memory 分工）
- [agent-runtime.md](agent-runtime.md) — Agent 生产执行层（loop、部署、durability）；Memory 为其组件

**站内**

- 个人记忆：[memory.md](../enterprise-knowledge/memory.md)
- OpenClaw 本地记忆：[openclaw-alternatives.md](openclaw-alternatives.md)