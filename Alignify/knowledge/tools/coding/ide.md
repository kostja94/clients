# AI IDE · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI IDE / Agentic IDE**——以图形化编辑器为主界面，集成 **AI agent** 做补全、重构、测试与多文件编辑；验收以**agent 编排深度、上下文索引与审查闭环**为主。本页为 **AI IDE 产品 SSOT**（完整 URL 表仅此一处）；从零搭应用 → [app-builder.md](app-builder.md)；自然语言写码心智 → [vibe-coding.md](vibe-coding.md)；终端 AI → [cli.md](cli.md)；PR 审查 → [code-review.md](code-review.md)。

**材料范围**：公开网络检索（厂商产品页、技术文档、开发者社区评测、行业对比文与社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-08**；补充更新 **2026-05-13**。

**站内对照**：[alignify.co/tools/ide](https://alignify.co/tools/ide) · `/tools/ide` · [alignify.co/zh/tools/ide](https://alignify.co/zh/tools/ide) · `/zh/tools/ide` · `content/tools/zh/ide.md`、`content/tools/en/ide.md` · slug **`ide`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#ide-tools`](../../keywords/alignify-keywords-tools.md#ide-tools)

**站内相邻**：[app-builder.md](app-builder.md) · [vibe-coding.md](vibe-coding.md) · [cli.md](cli.md) · [code-review.md](code-review.md)

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`ide`（本页）** | **`vibe-coding`** | **`app-builder`** | **`cli`** |
|------|---------------------|--------------------|--------------------|-----------|
| **典型买家问题** | 「什么 IDE 的 AI 能力最强？」 | 「怎么用自然语言让 AI 写代码？」 | 「怎么用 AI 搭一个完整应用？」 | 「怎么在终端里用 AI 帮我操作？」 |
| **核心能力** | 编辑器 + 内嵌 AI agent——代码补全、重构、测试、调试 | 自然语言→完整应用代码生成 | 零代码/低代码→全栈应用 | Shell 命令生成、脚本编写、系统操作 |
| **用户画像** | 专业软件工程师 | 产品经理/设计师/非传统开发者 | 创业者/非技术人员 | DevOps/系统管理员 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI IDE**：集成 AI agent 能力的集成开发环境；核心交互从「手动编写代码 + AI 补全」演进为「编排多个 AI agent 并行处理工程任务」——2026 年新兴子品类（agentic IDE）支持多 agent 同时工作（如分别修 bug、写测试、重构模块），开发者角色从代码编写者转向 **agent 调度者与交付物审查者**。
- **与 AI CLI 的区分**：AI IDE 以图形化编辑器为主界面（VS Code / JetBrains 风格），AI CLI 以终端为主界面；二者可以共存——用户可能在 IDE 里用内置终端调 AI CLI。区分在**主交互界面**而非底层能力。
- **与 Vibe Coding / App Builder 的区分**：AI IDE 用于**已有代码库**的维护与演进（打开仓库 → 改代码 → review diff → 合并）；App Builder 用于**从零创建**应用（描述 → 生成 → 部署）。IDE 用户是专业工程师，App Builder 用户可能是非技术人员。Copilot 与 Agentic 范式对照见 §专题对照。

---

## 专题对照 / 扩展定义

**Agentic vs Copilot vs 传统**：范式定义见 §词汇锚点；下表只列**买家体验差**，不重复术语。

| 维度 | **Type A（Agentic）** | **Type B（Copilot）** | **传统 IDE** |
|------|---------------------|----------------------|-------------|
| **AI 角色** | 主动执行任务、多 agent 并行 | 被动补全、单点建议 | 无 AI |
| **开发者角色** | 任务编排者、交付物审查者 | 代码编写者 + AI 辅助 | 完全手动编码 |
| **典型工作流** | 分配多 agent → 审查 artifacts → 合并 | 写代码 → Tab 接受补全 → 手动测试 | 编写 → 编译 → 调试 |
| **代表产品** | 见 §外链索引 **Type A** | 见 §外链索引 **Type B** | VS Code、IntelliJ IDEA |

架构路线（Agent-First / Copilot / Multi-Agent 编辑 / BYOM / 性能优先）→ **§形态谱系**；产品规格、定价与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- 专业开发者的编码时间被大量「非核心但必要」的任务占据（写测试、修 lint、重构命名、更新依赖）——agentic IDE 将这些任务委托给 AI，开发者聚焦架构决策与代码审查。
- 大型代码库的多文件改动需要跨模块理解——单文件补全不够，需要 agent 在仓库范围内自主规划与执行多步操作。
- 团队协作中，非核心开发者（初级工程师、跨职能贡献者）需要降低「正确改代码」的门槛。
- 传统 IDE 的功能更新周期（年）无法跟上 AI 模型迭代速度（月/周）——开发者需要能按日切换模型后端、调整 agent 策略的编辑器，静态 IDE 插件模型已不足以承载这种快速演进。
- **审查瓶颈**：AI 生成代码的速度远超人工审查带宽——agentic IDE 将开发者角色从「写代码」转为「审代码」，审查能力而非编码速度成为团队吞吐量的新约束（审查工具见 [code-review.md](code-review.md)）。

---

## 能力栈（概念拆分，非单一厂商功能表）

- **多 Agent 编排**：同时运行多个 AI agent，各自负责独立任务（如一个修 bug、一个写文档、一个跑测试），开发者通过仪表盘监控进度与审查产出。
- **上下文感知**：深度索引项目结构（AST 级理解模块依赖），持续跟踪会话上下文（记住 20+ 步前的尝试，避免重复错误）。
- **Artifacts 系统**：每个 agent 操作产出可审查的交付物（task list、implementation plan、diff、screenshot、browser recording）。
- **内置浏览器测试**：agent 可直接在 IDE 内启动浏览器实例，点击 UI、填写表单、截图验证——无需离开开发环境。
- **多模型后端**：支持按任务切换模型（Gemini / Claude / GPT），不锁定单一供应商。
- **项目记忆**：在仓库内持久化项目上下文（架构决策、技术栈版本、当前焦点），跨会话保持。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 核心交互是编排多 AI agent 并行；Mission Control 式仪表盘 | Agent-First IDE / agentic IDE / AI-first IDE | Antigravity |
| **B** | AI 作为补全与建议引擎深度嵌入；开发者仍为主要编码者 | AI Copilot IDE / copilot IDE / AI code editor | GitHub Copilot、Cursor |
| **C** | AI 跨多文件同时编辑；开发者审 diff 并合并 | Multi-Agent Editor / multi-agent IDE | Windsurf |
| **D** | 完全开源、支持任意模型后端；可自托管 | Open-Source BYOM / local LLM IDE | Cline / Kilo Code、Continue |
| **E** | 编辑器本身极致性能为核心，AI 为附加层 | Performance-First / fast code editor / Rust IDE | Zed |

**Type A vs B**（均含「AI 写码」，交互范式不同）：A 为任务编排；B 为编码加速——SWE-bench 与定价见 §外链索引及「对比与测评」。

---

## 风险 · 合规 · 安全与供应商依赖（外部框架可对照，非法律意见）

- **代码隐私与模型训练风险**：大多数 AI IDE 将代码上下文发送到云端 LLM 进行处理——企业代码库中的密钥、内部架构、业务逻辑可能暴露给第三方。GitHub Copilot Business/Enterprise 承诺不保留代码用于训练，但免费版和部分竞品的条款可能不同。Cline 的 BYOM 模式（代码不离开自有基础设施）是此风险的缓解方案。
- **供应商锁定与迁移成本**：一旦团队围绕特定 IDE 的 agent 系统建立了工作流（如 Cursor Rules、Antigravity Mission Control），迁移到另一工具意味着 workflow 重建。Agentic IDE 的锁定效应比传统 IDE 更深——不仅是编辑器偏好，而是工作方式的依赖。
- **AI 生成代码的许可证污染**：AI 代码补全可能从训练数据中复制受版权保护的代码片段（Copilot 被诉案件中原告主张 GPL 代码被逐字复现）。企业使用 AI IDE 产出的代码可能面临开源许可证合规风险。
- **安全漏洞的 AI 放大效应**：AI 生成的代码可能包含安全漏洞——当多个开发者接受相似 AI 建议时，同一类漏洞可能在代码库中批量出现，而非孤立事件。

---

## 落地碎片（无先后）

- **个人/小团队**：性价比与社区验证见 §外链索引 **Type B**；免费替代见 **Type D/E**（对比见「对比与测评」）。
- **企业合规**：**Type B** 企业档或 **Type D** 自托管路径——隐私条款见 §外链索引与 §风险。
- **Agentic 范式**：**Type A** 为品类定义者（公测稳定性 caveat 见索引）；**Type C** 提供更温和的 agentic 过渡。
- 任何 AI IDE 的代码输出在合并到主分支前都应经过人工 code review——将 AI agent 视为「可以写代码的初级工程师」而非「可以信任的资深工程师」。SWE-bench 分数见 §外链索引（最高 ~76%，仍有约四分之一任务需人工介入）。
- 启用代码库索引前，确认无硬编码密钥——agent 会读取全库上下文，可能无意在 prompt 中携带敏感数据。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Antigravity**（Google） | A | Agent-first IDE：2025-07 Google 以 **$2.4B** 从 Windsurf（Codeium）挖核心团队，**2025-11-18** 随 Gemini 3 公测。**Mission Control** 独立仪表盘 spawn/监控/编排并行 agent；**Chromium Agent** 内置 Chrome 自主测 UI（点击、填表、截图、录屏）；**Memory Bank**（`.agents/` 目录，Markdown：projectbrief / systemPatterns / techContext / activeContext）跨会话持久化。默认 **Gemini 3.1 Pro**，可切 **Claude Opus 4.6 / Sonnet 4.6 / GPT-OSS-120B**；Gemini 3 **2M+ token** 上下文。**SWE-bench 76.2%**（agentic 模式，2026 基准报道）。定价：公测免费，Pro **$20/月**（与 Google AI Pro 捆绑），Ultra **$249.99/月**。局限：公测无 GA 日期、UI 偶发 bug、资源占用大、Google 账户深度绑定引发隐私与锁定顾虑 | [官方文档](https://cloud.google.com/antigravity) |
| **Cursor** | B | AI-first 代码编辑器——多模型支持、子 agent 系统；**36 万**付费用户、**$1B+** 年化收入、估值 **~$30B**；社区评测常列 **$20/月 Pro** 为 2026 性价比首选 | [cursor.com](https://cursor.com/) |
| **Windsurf**（Codeium） | C | Agent 式多文件编辑——企业工程向（**5** 并行 agent、**$15/月**、多模型后端）；SWE-bench 约 **60–65%**（因多模型波动） | [windsurf.com](https://windsurf.com/) |
| **GitHub Copilot**（IDE 集成） | B | 微软生态 AI pair programmer——**$10/月**、多模型 GPT/Claude/Gemini、VS Code/JetBrains 深度集成；**Free** 档 **2000 次补全/月**；**Enterprise $39/人/月**（代码隐私、IP 赔偿、微软生态） | [github.com/features/copilot](https://github.com/features/copilot) |
| **Zed** | E | 高性能协作编辑器——Rust 原生、极速启动、实时协作；AI 内嵌；评测常列启动与编辑流畅度最优，AI 能力不及专用 AI IDE | [zed.dev](https://zed.dev/) |
| **Cline / Kilo Code** | D | 开源 VS Code 插件——BYOM **500+** 模型、完全开源、零供应商锁定；完全免费 | [github.com/cline/cline](https://github.com/cline/cline) |

### 对比与测评（第三方；观点非官方）

**SWE-bench（2026）**：Type A（agentic）路线 SWE-bench 分数居首；Type B/C 约 60–65%（多模型波动）——数值 SSOT 见 §外链索引。**SWE-bench 只测「能否修 bug/加功能」**，不测日常编码体验；Type E 启动与编辑流畅度评测最优但 AI 弱于专用 AI IDE。

**定价与社区共识**：Copilot Free 档与 Type D 开源插件对个人免费；Type B **$20/月** 档在多社区评测中被认为「物超所值」（子 agent + 多模型路由）。Type A Ultra 档锁定企业，公测稳定性让部分评测建议「再等 6 个月」——定价见 §外链索引。

**选型切片（Reddit r/programming、Hacker News）**：2026 年无单一「最佳 AI IDE」——愿意将 **30–50%** 编码任务委托 AI 的团队适合 **Type A/C**；希望 AI 辅助而非主力的适合 **Type B**；代码隐私硬性要求适合 **Type D** 自托管。形态定义见 §形态谱系。

*网摘综合，非本站实测。*

---

## 延伸阅读 · 站内外

- [Google Cloud Antigravity 文档 — Agentic IDE 概念](https://cloud.google.com/antigravity/docs)（产品门户见 §外链索引）
- SWE-bench 2026 社区横评与 Reddit/HN 选型讨论（观点非官方；具体产品规格见 §外链索引）