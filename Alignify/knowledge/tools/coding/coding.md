# AI Coding · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Coding Agent / 编程智能体**——在**已有代码库**上自主规划、执行、验证多步工程任务，验收以**可合并 PR、CI 通过、沙盒隔离**为主。本页为 **Coding Agent 产品 SSOT**（完整 URL 表仅此一处）；被动补全 → [code-completion.md](code-completion.md)；编辑器内 Agent → [ide.md](ide.md)；终端形态 → [cli.md](cli.md)；从零搭应用 → [app-builder.md](app-builder.md)；PR 审查层 → [code-review.md](code-review.md)。

**材料范围**：公开网络检索（厂商产品页、技术文档、开发者社区评测、行业对比文与社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-08**；补充更新 **2026-05-13**。

**站内对照**：[alignify.co/tools/coding](https://alignify.co/tools/coding) · `/tools/coding` · [alignify.co/zh/tools/coding](https://alignify.co/zh/tools/coding) · `/zh/tools/coding` · `content/tools/zh/coding.md`、`content/tools/en/coding.md` · slug **`coding`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#coding-tools`](../../keywords/alignify-keywords-tools.md#coding-tools)

**站内相邻**：[ide.md](ide.md) · [cli.md](cli.md) · [code-completion.md](code-completion.md) · [code-review.md](code-review.md) · [git-hosting.md](git-hosting.md) · [app-builder.md](app-builder.md) · [vibe-coding.md](vibe-coding.md) · [website-builder/website-builder.md](../website-builder/website-builder.md)

---

## 与相邻 slug 分流（编程工具链 Buyer 决策树）

| 你的问题 | 看哪个 slug | 区分 |
|----------|-------------|------|
| 「已有代码库，怎么让 AI 帮我写代码/修 bug？」 | **`coding`（本页）** | Coding Agent 自主规划多步任务，代理执行+审查 |
| 「用什么编辑器？IDE 的 AI 能力哪个强？」 | [`ide`](ide.md) | 编辑器+内嵌 AI 代码补全/重构/测试 |
| 「怎么让 AI 从零搭一个完整的应用？」 | [`app-builder`](app-builder.md) | 自然语言→全栈应用+部署 |
| 「怎么在终端里用 AI 帮我操作/写脚本？」 | [`cli`](cli.md) | Shell 命令、系统操作、脚本编写 |
| 「AI 能自动审查我的 PR 吗？」 | [`code-review`](code-review.md) | CI 集成、安全扫描、代码质量 |
| 「源码要不要从 GitHub 迁到 Agent 向 forge？」 | [`git-hosting`](git-hosting.md) | Origin / GitLab SCM / Agent HQ 路线分流 |
| 「AI 自动帮我补全下一行/下一个函数」 | [`code-completion`](code-completion.md) | 被动补全，非 Agent 自主执行 |
| 「我不懂代码，想凭感觉让 AI 生成应用」 | [`vibe-coding`](vibe-coding.md) | 非传统编程范式，描述→生成 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 共享事实速查（编程工具链统一口径）

| 事实 | 统一表述（截至 2026-06） |
|------|------------------------|
| Claude Code SWE-bench | **80.9%**（当前最高；终端交互 Agent） |
| Devin 估值 | **$10.2B**（Cognition；异步全自主型代表） |
| Google Jules→Jitro | **2025-08 GA → 2026-04 waitlist 升级**（prompt→目标驱动） |
| SWE-bench Pro | **contamination-reduced** 版本优先参考 |
| Coding Agent vs Copilot | **主动执行 vs 被动补全**——编程工具光谱两端 |
| MCP 协议角色 | 使 Agent 可跨 Jira/Slack/数据库等系统协调，降低跨工具摩擦 |

---

## 词汇锚点

- **AI Coding Agent（AI 编程智能体）**：能在已有代码库上**自主规划、执行、验证**多步骤软件工程任务的 AI 系统；典型工作模式是「接收 issue/spec → 理解代码库 → 拆解任务 → 编码 → 运行测试 → 提交 PR」。
- **与 AI IDE 的区分**：Coding Agent 可在无 IDE 环境异步运行（后台、沙盒 VM、CI）；AI IDE 需开发者在编辑器内交互——偏「委托—审查」vs「协作—实时反馈」。
- **与 Copilot / Code Completion 的区分**：Copilot **被动补全**下一行；Coding Agent **主动执行**完整任务——光谱两端（详见 [code-completion.md](code-completion.md)）。
- **Agentic Coding / Agentic Engineering**：Andrej Karpathy 2026 年概念——编排 agent 而非逐行手写；从「AI 帮你写」进化为「AI 帮你管」。
- **异步 Coding Agent**：分配任务后 Agent 在云端沙盒独立工作，完成后返回 PR——与终端交互型相对（形态见 §形态谱系）。

---

## 专题对照 / 扩展定义

*Coding Agent vs Copilot vs Vibe Coding*：范式定义见 §词汇锚点；下表只列**买家体验差**，不重复术语。

| 维度 | **Coding Agent** | **Copilot / 补全** | **Vibe Coding** |
|------|-----------------|-------------------|----------------|
| **自主程度** | 高（自主规划、执行、验证） | 零（被动提示下一行） | 中（对话迭代，每步需人触发） |
| **适用代码库** | 已有仓库（多文件） | 已有文件（单文件） | 从零生成新项目 |
| **典型用户** | 专业工程师、工程团队 | 所有开发者 | 非技术创始人、独立创业者 |
| **典型任务** | 修 bug、重构、实现 feature | 补全下一行/函数 | 生成完整应用 |
| **验收标准** | 可合并 PR、通过 CI | Tab 接受率 | 能跑、能演示 |
| **代表产品** | 见 §外链索引 | 见 [code-completion.md](code-completion.md) | 见 [vibe-coding.md](vibe-coding.md) |

架构路线（异步 / 终端 / IDE 内嵌 / CI）→ **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- 工程 backlog 积压「重要但不紧急」任务（技术债、依赖升级、测试补充）——Coding Agent 可异步消化。
- 大型代码库多文件改动需仓库级规划——单文件补全与 chat 不够。
- 开发者时间稀缺——将可委托任务交给 agent，人专注架构、审查与安全。
- 工具链碎片化——MCP 使 Agent 跨 Jira/Slack/数据库协调，降低「人去操作工具」摩擦。
- 非技术角色验证想法——与 [vibe-coding.md](vibe-coding.md) 重叠但本页主轴是**已有仓库的专业交付**。

---

## 能力栈（概念拆分，非厂商功能表）

- **仓库级理解**：AST 级索引、模块依赖、调用链——非 grep 级文本搜索。
- **任务拆解与规划**：高层目标→可执行步骤，按中间结果动态调整。
- **多文件编辑**：跨模块协调改动。
- **自主测试与修复**：运行测试→分析失败→修改→重测循环。
- **PR 生成**：标题、描述、commit 拆分、关联 issue，符合团队规范。
- **沙盒执行**：隔离 VM/容器，不污染本地环境。
- **MCP 集成**：接入 Linear、Jira、Slack、数据库等外部系统。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 交互模式 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 异步全自主——Fire-and-forget，云端沙盒 | autonomous dev agent, async coding agent | Devin、Google Jules/Jitro |
| **B** | 终端交互——实时观察、随时介入 | CLI agent, terminal agent | Claude Code、Codex CLI、Gemini CLI、Aider |
| **C** | IDE 内嵌——与编辑器上下文联动 | AI IDE agent mode | Cursor Agent、Windsurf Cascade |
| **D** | CI 集成——PR 审查、lint、changelog | automated PR review | CodeRabbit、What The Diff → [code-review.md](code-review.md) |

Type B 深度见 [cli.md](cli.md)；Type C 见 [ide.md](ide.md)。

---

## 工具与产品类型（检索词常混品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|-------------|------|
| **Coding Agent · 异步全自主** | Type A 产品 | 见 §外链索引 |
| **Coding Agent · 终端交互** | Type B 产品 | 见 [cli.md](cli.md) |
| **AI IDE · 编辑器内嵌** | Type C 产品 | 见 [ide.md](ide.md) |
| **Copilot · 代码补全** | 被动 inline 补全 | 见 [code-completion.md](code-completion.md) |
| **Vibe Coding 平台** | 从零生成应用 | 见 [vibe-coding.md](vibe-coding.md) |
| **CI 集成型代码审查** | Type D 产品 | 见 [code-review.md](code-review.md) |

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **代码安全**：Agent 产出须与人类代码同等级别审查——不因「AI 写的」降标准。
- **代码库读写权限**：须确认沙盒、代码留存、模型训练退避条款。
- **许可证与版权**：训练数据可能含 copyleft——评估各 provider indemnity 差异。
- **供应商依赖**：关键路径保留至少两个 provider 切换能力。
- **基准作弊**：优先 SWE-bench Pro 等 contamination-reduced 版本。

---

## 落地碎片（无先后）

- POC 从**一个真实 backlog 任务**开始——非 demo 项目。
- 将 Agent 产出当作**外部贡献者 PR** 审查。
- 异步 agent 适合「今天分配、明天审查」；终端 agent 适合需实时协作的复杂任务。
- 企业须确认沙盒、留存、训练退避——权限边界高于 Copilot。
- CI/CD 集成时限制**自动合并**——推荐「生成 PR → 人工审查 → 合并」。

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Devin**（Cognition） | 自主 Coding Agent——沙盒 VM 异步全流程（Fire-and-forget、$20/mo + ACU、估值 $10.2B） | [devin.ai](https://devin.ai/) |
| **Google Jules**（→ Jitro） | Google 异步 Coding Agent——GitHub 集成，正升级为目标驱动 | [jules.google](https://jules.google/) |
| **Claude Code**（Anthropic） | Agentic CLI——终端多步 agent 循环 + MCP（SWE-bench 80.9%、200K 上下文） | [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code) |
| **Codex CLI**（OpenAI） | 开源 agentic CLI——本地执行、多模型后端（Terminal-Bench 77.3%） | [github.com/openai/codex](https://github.com/openai/codex) |
| **Gemini CLI**（Google） | 开源 AI CLI——Gemini 驱动、高免费配额（Apache 2.0） | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **Aider** | 开源 AI pair programming CLI——多模型后端、Git 原生 | [aider.chat](https://aider.chat/) |
| **SWE-bench Verified** | Coding Agent 评测基准——真实 GitHub issue 端到端修复 | [swebench.com](https://www.swebench.com/) |
| **CodeSOTA** | 跨模型编程能力宽表对比 | [codesota.com](https://codesota.com/) |

### 对比与测评（第三方；观点非官方）

2026 年社区讨论集中于三轴：(1) **SWE-bench Verified/Pro**——Claude Code 与 Devin 竞争激烈，分数变动频繁须回源；(2) **终端 vs 异步**——可见性/可控性 vs 释放开发者时间，共识为长期共存；(3) **多文件复杂任务**——Aider 开源生态在特定工作流有忠实用户。Google Jules→Jitro（prompt→目标驱动）被部分媒体称为「Coding Agent 2.0」信号，产品仍在 waitlist。*本小节为网摘综合，非 Alignify 实测；产品事实见 §外链索引与 §共享事实速查。*

---

## 行业注记 · 2026 年 Coding Agent 格局

- **Google 编程工具碎片化**：Gemini Code Assist / CLI / AI Studio / Firebase Studio / Jules / Antigravity 六产品线并存——Koray Kavukcuoglu 推动 Antigravity 整合；前负责人 Kathy Korevec 2026-04 离职 OpenAI 并公开批评碎片化。
- **Jitro 叙事**：Jules 从 prompt 驱动转向 KPI/目标驱动——预计 Google I/O 2026 展示；细节以官方为准。
- **MCP 标准化**：Agent 从「只能改代码」扩展为跨 SaaS 协调——见 §共享事实速查。

---

## 延伸阅读 · 站内外

**站外**

- **Grand View Research · AI Code Assistants 市场报告（2026）**：[grandviewresearch.com](https://www.grandviewresearch.com/industry-analysis/ai-code-assistants-market-report)

**站内**

- 终端 Agent：[cli.md](cli.md) · IDE 内嵌：[ide.md](ide.md) · 补全：[code-completion.md](code-completion.md) · 审查：[code-review.md](code-review.md) · Forge：[git-hosting.md](git-hosting.md)