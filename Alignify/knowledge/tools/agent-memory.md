# AI Agent 记忆层 · 知识块（非线性笔记）

**材料范围**：公开网络检索（Mem0、Zep/Graphiti、Letta/MemGPT、Supermemory、Cognee、LangMem、MemU、MemOS、claude-mem、agentmemory 等厂商文档与 GitHub；LongMemEval/LoCoMo/BEAM 基准与 arXiv 论文摘要；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/blog/agent-memory](https://alignify.co/blog/agent-memory) · [alignify.co/zh/blog/agent-memory](https://alignify.co/zh/blog/agent-memory) · slug **`agent-memory`** · 正文 JSON `alignify-by-kostja/content/blog/{en|zh}/agent-memory.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 [`#agent-memory-tools`](../../product/alignify-keywords-tools.md#agent-memory-tools)）· `keywordEn`: **AI Agent Memory** · `keywordZh`: **AI Agent 记忆

## 与相邻 slug 分流

| 维度 | **agent-memory（本文）** | **memory** | **knowledge-base** | **context**（待建 KB） | **openclaw-alternatives** |
|------|--------------------------|------------|--------------------|-------------------------|---------------------------|
| **买家问题** | 给 Agent **跨会话持久化**事实/偏好/程序性知识 | 个人/团队 **第二大脑**与笔记组织 | 企业 **文档库 RAG** 问答 | Agent **此刻**该看到什么上下文 | **个人助理**网关与本地 Harness |
| **时间尺度** | 跨会话、跨任务 **长期** | 长期个人知识资产 | 企业知识库版本迭代 | **单次任务/当前窗口** 即时 | 会话 + 本地 Markdown 记忆 |
| **典型产品** | Mem0、Zep、Letta、MemOS | Mem.ai、Notion AI、Limitless | Glean、Notion Enterprise | Rewind、AirJelly（意图采集） | OpenClaw MEMORY.md |
| **集成面** | SDK、MCP、LangGraph | App、MCP App 层 | SSO、RAG pipeline | OS/屏幕采集 | IM 渠道 + 本地文件 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agent Memory Layer / Agent 记忆层**：嵌入 Agent 运行时与应用的 **持久化记忆中间件**——从对话/工具输出中提取事实，写入外部存储，在后续 turn 按语义/图谱/时间检索注入上下文。与「把整段 chat history 塞进 prompt」不同；与 RAG over 静态文档库也不同——记忆来自 **交互过程**，且常带 user/session/agent 作用域。
- **Persistent Memory vs Context Window**：上下文窗口是 **单次推理的工作集**；持久记忆是 **跨会话的外部存储+检索**。2026 年共识：100 万 token 窗口 **不能替代** 记忆层——会 context rot、成本线性膨胀、且无法在会话间结构化更新（OpenAI/Anthropic 内置 Memory 仍是该问题的产品化封装，第三方 layer 提供可移植与可治理）。
- **Episodic / Semantic / Procedural Memory**：情景记忆（发生了什么）、语义记忆（稳定事实与偏好）、程序性记忆（怎么做某类任务）——Agent 记忆框架常按此分层（Letta core/archival/recall 即 OS 式分层）。选型时问：你的 Agent 更需要「记住用户喜欢什么」还是「记住上次怎么修这个 bug」。
- **Vector-first vs Graph / Temporal Graph**：向量检索擅长「像什么」；知识图谱擅长「谁与谁、何时为真」；**时序图谱**（Zep/Graphiti）追踪事实有效期——「去年相信 X，现在相信 Y」。LongMemEval 的 temporal 子项是 2026 年选型关键分水岭。
- **Memory as File System（MemU）**：将记忆暴露为 **可见、可组织的文件结构**而非纯向量黑箱——便于调试、导出与 Theory of Mind 层扩展；常见于情感陪伴与 proactive agent。
- **Memory OS（MemOS）**：把记忆当作 **可调度系统资源**（MemCube：内容+溯源+版本+治理）——plaintext / activation / parameter 多形态统一；面向企业可审计、可迁移、可跨平台共享。
- **Coding Agent Memory**：IDE 插件/CLI 侧记忆（claude-mem、agentmemory、memento）——记录会话、决策、文件变更；与 Mem0 等 **通用 memory API** 交叉但买家是开发者工作流。

---

## 专题对照

### Memory Layer vs RAG vs Platform Memory

| 维度 | **Agent Memory Layer** | **Enterprise RAG / Knowledge Base** | **ChatGPT / Claude Memory** |
|------|------------------------|-------------------------------------|----------------------------|
| **数据来源** | 对话、工具输出、Agent 行为 | 上传文档、Wiki、Ticket | 平台内对话推断 |
| **买家** | Agent 平台工程师 | 知识管理、Support | 终端用户 |
| **可移植性** | 高（自建/换模型） | 中（绑企业 CMS） | 低（绑平台） |
| **治理** | 自管 retention、scope、audit | DLP、权限、版本 | 平台策略 |
| **代表** | Mem0、Zep、Letta | Glean、knowledge-base 页产品 | ChatGPT Memory、Claude Projects |

### 架构选型四问

| 问题 | 偏 A | 偏 B |
|------|------|------|
| 查询类型 | 「找相似表述」→ 向量 / Mem0 免费层 | 「谁导致了什么、何时变真」→ Zep/Graphiti |
| 部署 | 托管 API（Mem0 Cloud、Supermemory） | 自托管（Letta、Cognee、AutoMem） |
| Agent 形态 | 薄 memory layer 接现有框架 | 有状态 Agent 运行时（Letta） |
| 场景 | 个性化助手 | 编码 Agent MCP 插件（claude-mem） |

---

## 问题域

- **无状态 Agent 是死路**：57% 组织已部署 Agent（2026 行业调查口径），但质量与延迟瓶颈常追溯到 **记不住** 或 **记错了**——多步任务中 context drift 被指为企业失败主因之一。
- **全量 context 不可扩展**：把全部历史塞进窗口——p95 延迟与 token 成本随 turn 线性恶化；Mem0 等 benchmark 叙事： selective memory 相对 full-context 可 **~90% 降 token、~91% 降延迟**，准确率 trade-off 需按场景测。
- **品类混称**：Mem0、Letta、Supermemory App、Mem.ai、claude-mem **不可互换**——框架 vs 笔记 vs IDE 插件；采购前必须先定 **memory layer 还是 end-user 产品**（见 [memory.md](./memory.md) 与 [/tools/memory](https://alignify.co/tools/memory) 分流）。
- **Stars ≠ 真实采用**：GitHub star 可异常堆积；选型应看 LongMemEval/LoCoMo、生产 case、MCP 部署面，而非单看 star。
- **中国与全球双轨**：MemU、MemOS、ClawBrain、kiwi-mem 等面向中文陪伴/ proactive / 本地部署；Mem0/Zep 面向全球 Agent infra——监管与数据 residency 影响选型。

---

## 能力栈

- **Extract → Consolidate → Retrieve**：写入管线（LLM 提取事实、去重、冲突消解）+ 检索管线（向量+关键词+图谱+重排）——Mem0、Supermemory 等核心卖点。
- **Scoped memory**：user / session / agent / team 作用域——多租户 SaaS 必备。
- **Selective forgetting**：矛盾事实更新、过期淘汰、用户删除——GDPR 与「有害记忆」问题。
- **MCP / SDK 集成**：Firecrawl、Supermemory、TinyFish 等通过 MCP 暴露 `memory_*` 工具——与 [agent-skills.md](./agent-skills.md) 生态衔接。
- **Hybrid retrieval**：向量 + BM25（FTS5）+ 实体链接——2026 年 coding agent 记忆标配（agentmemory 等）。
- **Tiered / OS-style memory**：热上下文 vs 归档 vs 召回（Letta MemGPT）——长运行 Agent 适用。
- **Temporal validity**：事实带时间戳与有效期——合规、金融、医疗场景倾向 Zep 类方案。

---

## 形态谱系

- **Type I — Managed Memory API**：Mem0 Platform、Zep Cloud、Supermemory Cloud——最少 ops，按量计费。
- **Type II — Open-source memory layer**：Mem0 OSS、Graphiti、LangMem、Cognee、AutoMem——可自托管，接 LangChain/LangGraph/任意框架。
- **Type III — Stateful agent framework**：Letta（MemGPT）——记忆是 Agent 运行时一等公民，非外挂。
- **Type IV — IDE / coding harness memory**：claude-mem、agentmemory、memento——绑定 Claude Code/Cursor 等工作流。
- **Type V — Memory OS / proactive**：MemOS、MemU——文件系统式或 24/7 proactive agent 记忆引擎。
- **Type VI — Minimal file memory**：OpenClaw `MEMORY.md`、CLAUDE.md——无向量库，Markdown 即记忆；成本最低，可扩展性有限。

---

## 风险 · 合规 · 隐私

- **Memory poisoning**：恶意输入污染长期记忆——生产需校验写入、隔离 scope、审计读取（Mem0 2026 安全博文议题）。
- **PII 与 HIPAA**：Mem0 等宣称 SOC2/HIPAA——自建仍需加密、BYOK、保留策略。
- **删除是否彻底**：向量嵌入「删除」的技术可行性仍受质疑——企业需 retention API 与导出能力。
- **跨工具记忆孤岛**：ChatGPT Memory 不导出到 Cursor——第三方 layer 的价值在于 **可移植**，但增加集成成本。

---

## 落地碎片

- **先定 benchmark 场景**：用 LongMemEval 子集或自有 golden query set 测 hit@k——勿只看 vendor 自报分数。
- **Hybrid 优于纯向量**：错误码、版本号、文件路径靠 BM25；语义靠向量——只上向量会在生产翻车。
- **Memory 与 Context 分工**：即时任务上下文（读哪些文件、哪些 tool result）归 **context engineering**；跨会话用户偏好归 **agent memory**——一文写两题易混（Context KB 待建）。
- **OpenClaw 用户**：Markdown 记忆足够起步；规模化再评估 Mem0/Supermemory MCP。

---


## 产品候选与定价对照（2026-06）

> **主榜分组**：Universal memory layer（Mem0、Zep、Letta、Supermemory API、Cognee）与 Coding agent memory（claude-mem、agentmemory）见部署仓 `/blog/agent-memory`。MemOS/MemU **仅**出现在该文对比表/FAQ（中国生态），**不**入主榜 EN BestTools。

| 产品 | 类型 | 公开定价（2026-06） | 部署 | 最佳买家 |
|------|------|---------------------|------|----------|
| **Mem0** | Universal layer | 免费层 + **$19/月** Pro + Enterprise | 托管 + OSS | 框架无关 Agent 平台 |
| **Zep / Graphiti** | 时序图谱记忆 | 免费开发者层 + **$25/月** 起 Team | Cloud + OSS Graphiti | 需 temporal validity 的企业 Agent |
| **Letta** | Stateful Agent + 记忆 | OSS 免费 + **Letta Cloud** 按量 | 自托管 / Cloud | MemGPT 式长运行 Agent |
| **Supermemory API** | Universal layer + MCP | 免费 credits + 按 memory op 计费 | Cloud + 自托管选项 | MCP 优先的 Agent 栈 |
| **Cognee** | 图原生 control plane | OSS 免费 + 企业许可 | 自托管为主 | 图+向量统一检索 |
| **claude-mem** | Coding harness | 开源免费 | 本地 Claude Code | IDE 会话/决策记忆 |
| **agentmemory** | Coding harness | 开源免费 | 本地 MCP | Cursor 工作流混合检索 |
| **MemOS**（对比/FAQ） | Memory OS | 开源 + 企业定制 | 自托管 | 中国企业可审计记忆治理 |
| **MemU**（对比/FAQ） | Memory as FS | API 按量 + 开源组件 | Cloud / 本地 | 中文陪伴/proactive Agent |

**架构选型定价轴**：

| 选型问题 | 低成本起步 | 生产扩展 |
|----------|------------|----------|
| 最少 ops | Mem0 Cloud、Supermemory Cloud | Enterprise 合同 + BYOK |
| 自托管 | Mem0 OSS、Graphiti、Cognee、Letta | 自建向量库 + 运维 |
| Coding Agent | claude-mem、agentmemory | + Mem0 MCP 统一跨 IDE |
| 中国数据 residency | MemOS、MemU（对比表） | 私有化部署 + 审计 API |

## 工具与产品类型

| 类型 | 代表 | 备注 |
|------|------|------|
| **Universal memory layer** | Mem0, Zep, Supermemory API | 框架无关，GitHub 社区最大（Mem0 ~59k stars，2026-06） |
| **Temporal KG memory** | Zep / Graphiti | LongMemEval temporal 强项 |
| **Stateful agent + memory** | Letta | 学术 MemGPT 血统 |
| **Graph-native control plane** | Cognee | 图+向量+关系统一 |
| **LangGraph-native** | LangMem | 已在 LangChain 栈则优先评估 |
| **Coding agent memory** | claude-mem, agentmemory, memento | IDE/MCP 集成 |
| **CN: Memory OS / proactive** | MemOS, MemU, ClawBrain | 企业治理 / 陪伴 / API 网关叙事 |
| **Minimal harness** | OpenClaw MEMORY.md | 见 [openclaw-alternatives.md](./openclaw-alternatives.md) |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| Mem0 | Agent 记忆层；托管 + OSS；Apache-2.0 | https://mem0.ai/ |
| Zep / Graphiti | 时序知识图谱记忆；Graphiti OSS | https://www.getzep.com/ |
| Letta | MemGPT 有状态 Agent 框架 | https://www.letta.com/ |
| Supermemory | 记忆 API + MCP；LongMemEval 自报领先 | https://supermemory.ai/ |
| MemOS | 记忆操作系统；MemCube；arxiv:2507.03724 | https://github.com/MemTensor/MemOS |
| MemU | Memory as File System；proactive 24/7 agent | https://memu.pro/ |
| claude-mem | Claude Code 会话记忆插件 | https://github.com/thedotmack/claude-mem |

### 对比与测评（第三方）

- **Atlan / AgentMarketCap 2026**：Mem0 vs Zep vs Letta vs Supermemory head-to-head；强调架构赌注不同，无 universal winner。
- **Preuve.ai AI Memory Stats 2026**：60+ 数字；ChatGPT Memory 7 亿 WAU 级部署 vs 开源框架 star 与 benchmark 对照。
- **Mem0 vs Zep（Vectorize 2026）**：向量+可选图 vs 时序图；自托管路径与定价 tier 差异。

---

## 延伸阅读与参考材料

- arXiv:2504.19413 — Mem0 ECAI 2025（latency/token vs full-context）
- arXiv:2501.13956 — Zep temporal knowledge graph
- Wu et al., ICLR 2025 — LongMemEval benchmark
- Maharana et al., ACL 2024 — LoCoMo
- AWS 中国区博客 — Context Engineering 与 AgentCore Gateway（context 与 memory 分工）
