# Agent 时代 Git 托管 / Code Forge · 知识块（非线性笔记）

**材料范围**：公开网络检索（Cursor / GitLab / GitHub / Zed / xAI 官方文档与工程博客；Reuters、VentureBeat、TechCrunch、The Verge、SiliconANGLE、Pragmatic Engineer；GitHub Status 与 availability 报告）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。产品阶段、定价与合规条款以各官网为准。网摘整理日期 **2026-08-21**。

**站内对照**：`/blog/git-hosting` · `/zh/blog/git-hosting`（Best Ranking · 2026-08-21）· slug **`git-hosting`**

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../../product/alignify-keywords-tools.md)（锚点 `#git-hosting-tools`）· `keywordEn`: **Agent-native Git hosting / Code forge** · `keywordZh`: **AI 原生 Git 托管 / 代码托管平台**

**站内相邻**：[coding.md](coding.md)（Coding Agent） · [ide.md](ide.md)（AI IDE） · [code-review.md](code-review.md)（PR 审查层） · [cli.md](cli.md)（终端 Agent） · [vibe-coding.md](vibe-coding.md)（氛围编程） · [agent-sandbox.md](../agent/agent-sandbox.md)（Agent 执行沙箱） · [multi-agent.md](../agent/multi-agent.md)（多 Agent 编排）

## 与相邻 slug 分流

| 维度 | **git-hosting（本文）** | **code-review** | **ide** | **coding** | **agent-sandbox** |
|------|-------------------------|-----------------|---------|------------|-------------------|
| 核心问题 | 源码**存哪、怎么 push/PR/merge** | PR **怎么审** | **在哪写/改**代码 | Agent **怎么执行任务** | Agent **在哪跑**不可信代码 |
| 典型读者 | 平台工程、CTO、DevOps | 工程效能、安全 | 应用开发者 | Agent 产品/全栈 | Agent 基础设施 |
| 交付形态 | Git forge、mirror、CI 集成 | GitHub App、审查机器人 | 编辑器 + Agent | 异步/终端 Agent | 隔离 VM/容器 |
| 验收核心 | 可用性、权限、导出、数据条款 | 噪声率、上下文深度 | 多文件编辑、模型 | PR 质量、CI 通过 | 隔离、TTL、审计 |

| 你的问题 | 看哪个 slug |
|----------|-------------|
| 「GitHub 之外有没有为 Agent 设计的托管？」 | **`git-hosting`（本页）** |
| 「AI 怎么自动 review 我的 PR？」 | [`code-review`](code-review.md) |
| 「Cursor / Copilot 在哪个编辑器里用？」 | [`ide`](ide.md) |
| 「谁帮我修 bug、开 PR？」 | [`coding`](coding.md) |
| 「Agent 跑代码的隔离环境？」 | [`agent-sandbox`](../agent/agent-sandbox.md) |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 共享事实速查（截至 2026-08-21）

| 事实 | 统一表述 |
|------|----------|
| Cursor **Origin** | Early Beta（2026-08-17 起向 Pro/Teams/Enterprise rollout）；**非**「Grok Origin」独立 SKU |
| Origin 存储 | **Continuity**（WAL + S3，Git 协议兼容）——见 Cursor 工程博客 |
| GitHub 负载 | 官方称 2025-12 起 **agentic 工作流**驱动流量急增；2026-02 目标从 10× 调至 **30×** 容量设计 |
| GitHub **Agent HQ** | Universe 2025-10 宣布；**不换** git substrate，做多厂商 Agent **编排** |
| GitLab 对策 | **下一代 SCM** private beta（免 clone API）；**Orbit** public beta；**Duo Agent Platform** GA |
| Zed **DeltaDB** | 2026-08 private beta；**Git 伴侣**，记录 commit 之间 edit + 对话 |
| OpenAI 内部 forge | Reuters 2026-03 报道；**早期**，可能不商用 |

---

## 词汇锚点

- **Git hosting / Code hosting / Code forge**：基于 **Git** 的远程仓库托管与协作层——分支、push/pull、PR/MR、权限、CI 钩子；GitHub / GitLab / Bitbucket 为 incumbent。**Forge** 强调 forge 层（PR、review、merge、权限）而不仅是裸 `git` 协议。
- **Agent-native Git hosting / Agent-scale forge**：假设主要写入者包含 **AI Agent**（高频小 commit、并行分支、大量 ephemeral 仓库）而不仅是人类低频 push；在 **review/merge 吞吐、存储副本策略、API 免 clone** 上重新设计或重建后端。
- **与 AI IDE 的区分**：IDE 解决「在哪编辑」；git hosting 解决「源码系统记录与协作边界在哪」。Cursor Origin 将二者 **同一产品面**（Codebase 标签），但品类上仍属托管层。
- **与 code-review 的区分**：审查工具（CodeRabbit、Graphite on GitHub）**叠加**在既有 forge 上；Origin 类产品是 **forge 本身** + 可选 mirror GitHub。Graphite 被 Cursor 收购后，**Graphite.com 仍可作为 GitHub 上的 stacked PR 产品**独立存在。
- **Mirror / wedge 策略**：从 GitHub **同步**到第二 forge，GitHub 可保持 **source of truth**；降低迁移风险。Origin 支持 Detach 后变为 Origin 独占托管。
- **Continuity（Cursor）**：Origin 后端存储；WAL 持久化至 S3、线性一致 push、副本数可按仓库规模弹性伸缩（相对 GitHub **Spokes** 固定 quorum 模型）。
- **Agent HQ（GitHub）**：Mission Control 统一调度 Copilot、Claude、Codex、xAI 等 Agent；**substrate 仍是 GitHub**。

---

## 专题对照：五条技术路线（2026）

| 路线 | 代表 | 是否新 forge | Git 协议 | Agent 差异化 |
|------|------|:------------:|:--------:|-------------|
| **A. 新建 Agent-scale forge** | Cursor **Origin** | 是（Beta） | 兼容 | Continuity + IDE 内 PR/Agent；Graphite 技术线 |
| **B. 改造 incumbent SCM 后端** | **GitLab** 下一代 SCM | 否（同 GitLab） | 兼容 | 免 clone API、Orbit 上下文图、临时仓库 epic |
| **C. 守 substrate + 编排** | **GitHub Agent HQ** | 否 | 原生 | 多 Agent 并行、AGENTS.md；不换 host |
| **D. commit 之间的版本层** | **Zed Delta / DeltaDB** | 否 | **伴侣** | CRDT 记录 edit + 对话；Git 仍负责对外交换 |
| **E. 早期 / 传闻** | OpenAI 内部 forge、Oak、Gitdot | 部分 | 各异 | 单源或社区早期 |

---

## 问题域

- **Agent 负载击穿 human-scale forge**：GitHub 官方博客（2026）称 repository 创建、PR、API、大仓库工作负载自 2025-12 起因 **agentic 开发**急增；PR 触达 Git/Actions/Search/权限等 **全链路耦合**，小 inefficiency 在规模下放大为 outage。
- **Review/Merge 成为新瓶颈**：Coding Agent 提高 **产出速度**，人类与自动化 review 带宽未同比扩展；stacked PR、merge queue、Agent 自动 merge 状态成为竞争焦点。
- **Spokes 模型的结构性限制**：行业标配 **3PC + NVMe packfile 副本**对 **超大 monorepo**（副本 quorum 延迟）与 **海量 Agent 小仓库**（每库最低副本地板过高）两端都不理想——Cursor Continuity 博客从工程角度阐述此动机。
- **垂直整合压力**：Editor（Cursor）+ Model（Grok）+ Host（Origin）+ Agent（Grok Bot/Build）同厂——降低集成摩擦，引入 **数据治理与锁定** 采购问题。
- **GitHub 可靠性疲劳**：2025–2026 多次 major incident（含 2026-08-17 **7h47m** 全球降级，[GitHub Status](https://www.githubstatus.com/)）——催生 **第二 forge 试验**（OpenAI 内部项目、Origin mirror 叙事），不等同于 mass migration。
- **Ephemeral / 临时仓库需求**：Agent fan-out 需要 **cheap create/destroy** 仓库与 **commit-without-clone**（GitLab epic #21716 方向）。

---

## 能力栈（概念维度，非厂商功能表）

- **存储与一致性模型**：packfile-on-NVMe + quorum（Spokes 系）vs WAL-on-object-store + 线性化 push（Continuity 系）vs 关系库 + blob（Azure DevOps 类）。
- **Agent 访问模式**：传统 **git clone/fetch** vs **结构化 API**（列目录、读文件、提交 diff 无 clone）——GitLab 下一代 SCM 主打后者。
- **PR / Review 吞吐**：人类 bounded chunks vs Agent **小步高频 PR**；stacked PR、自动 conflict resolution、Agent 可读「谁写的这段」元数据。
- **Mirror 与迁移**：单向/双向 sync、Detach、namespace 策略、导出与 **Detach from GitHub** 语义。
- **CI 集成**：跑现有 **GitHub Actions workflow**（Origin 通过 Buildkite/Depot）vs 原生 pipeline vs 仅 webhook。
- **Agent 同界面**：仓库浏览、PR diff、Cloud Agent 改同一 PR——Origin 与 IDE 一体化。
- **身份与合规**：Enterprise SSO、audit log、数据保留/训练使用条款、subprocessor 列表——Beta 产品常 **条款滞后**。

---

## 形态谱系

- **Type I — Incumbent + Agent 编排**：GitHub **Agent HQ**；保留 GitHub，加 Mission Control、多厂商 Agent、AGENTS.md。适合 **零迁移**、已深度绑定 Actions/Apps 的团队。
- **Type II — Incumbent + SCM 引擎升级**：GitLab **下一代 SCM + Orbit + Duo Agent Platform**；企业留在 GitLab，后端为 Agent 并发优化。适合 **已有 GitLab** 与合规自建需求。
- **Type III — Editor 系新建 Forge**：Cursor **Origin**；mirror wedge + Continuity；与 Cursor/Grok 生态绑定。适合 **Cursor 重度用户**、愿试验第二托管面。
- **Type IV — Git 伴侣 / 会话版本层**：Zed **DeltaDB**；不替换 remote，捕获 **commit 之间** 的 edit 与 Agent 对话。适合 **审查溯源**、多人/多 Agent 实时协作。
- **Type V — 替代 VCS / 早期 forge**：Oak（virtual mount VCS）、Gitdot（Rust forge 早期）、OpenAI 内部 forge（传闻）——成熟度与 **企业就绪** 差异大。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **源码 custody 集中**：Editor + Host + Model 同母公司（如 SpaceXAI 收购 Cursor 后）——CISO 需单独审查 **数据保留、训练使用、subprocessor、导出**；Origin 原生托管 **独立条款** 截至 2026-08 仍不完整（据 VentureBeat 等 Tier 1 与官方文档缺口综合）。
- **Enterprise 默认开启**：Origin Beta 对 Enterprise **默认启用**、管理员 **opt-out**（据 Cursor Changelog）——未主动决策的组织可能 unaware。
- **Mirror ≠ 无风险**：GitHub 仍为 source of truth 时，Origin 侧重 **工作界面**；Detach 后 Origin 独占，需重新评估备份与合规。
- **Namespace 不可变**：Origin Beta 内 codebase namespace **不可更改**——抢注与组织命名冲突风险。
- **可用性记录**：新 forge **uptime 历史短**；不可用「GitHub 宕机」 alone 证明替代品更可靠。
- **供应链安全**：IDE/Agent 与仓库同栈时，**仓库投毒**（如恶意 `git.exe` 类 RCE 讨论）影响面扩大——需与 [`code-review`](code-review.md)、[`agent-sandbox`](../agent/agent-sandbox.md) 联合治理。
- **锁定与导出**：试验 mirror 阶段应验证 **git clone 导出、Detach 流程、CI 可迁移性**；AGENTS.md / Origin API 绑定加深后迁移成本上升。

---

## 落地碎片

- **先 mirror，后 Detach**：用 GitHub 作 source of truth，在 Origin 试 Agent 工作流；稳定后再评估 Detach。
- **平台工程 checklist**：数据条款、audit log、branch protection、Agent 默认权限、Enterprise opt-out 状态、subprocessor 列表。
- **与审查栈对齐**：forge 换不换，[`code-review`](code-review.md) 工具是否支持新 host（Graphite 仍可在 GitHub；Origin 内置审查在 Beta 仍 evolving）。
- **区分「编排」与「托管」**：Agent HQ 不解决 GitHub 存储层负载；若问题是 **clone/push 限流**，需看 GitLab 下一代 SCM 或 Origin 类 forge。
- **Incumbent 可靠性**：关注 GitHub **availability 报告**与 status；DR 计划不应假设单一 forge 100% 可用。
- **术语澄清**：对外沟通写 **Cursor Origin**，避免与 xAI **Grok** 产品线混称为「Grok Origin」——官方无此 SKU。

---

## 工具与产品类型

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| **Incumbent Git hosting** | GitHub, GitLab, Bitbucket, Gitee | Agent HQ / Duo 等 **编排**叠加上去 |
| **Agent-native forge（Beta）** | Cursor Origin | Git 兼容 + mirror wedge |
| **SCM 引擎升级（enterprise）** | GitLab next-gen SCM, Orbit | private/public beta 分阶段 |
| **Stacked PR on GitHub** | Graphite | 可被 Cursor 收购 narrative 关联，**产品仍服务 GitHub** |
| **Git companion VCS** | Zed DeltaDB | 非 remote replacement |
| **Early OSS forge** | Gitdot, Forgejo/Codeberg | 联邦/开源路线；与 Agent-scale 成熟度不一 |
| **Internal / rumoured forge** | OpenAI（The Information/Reuters） | 可能永不商用 |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Cursor Origin** | Early Beta git forge；GitHub mirror、PR、Origin API、Vercel/Depot/Buildkite | [cursor.com/docs/origin](https://cursor.com/docs/origin) |
| **Origin Changelog** | 2026-08-17 Beta rollout；Enterprise opt-out 说明 | [cursor.com/changelog/origin-code-hosting](https://cursor.com/changelog/origin-code-hosting) |
| **Continuity 工程博客** | WAL+S3 存储；Agent-scale 动机 vs Spokes | [cursor.com/blog/git-at-any-scale](https://cursor.com/blog/git-at-any-scale) |
| **GitHub Agent HQ** | 多厂商 Agent Mission Control；**不换** git host | [github.blog Agent HQ](https://github.blog/news-insights/company-news/welcome-home-agents/) |
| **GitHub availability 更新** | Agent 负载；10×→30× 容量目标 | [github.blog availability](https://github.blog/news-insights/company-news/an-update-on-github-availability/) |
| **GitLab Transcend** | 下一代 SCM private beta；Orbit public beta | [about.gitlab.com/blog/gitlab-transcend-announcements/](https://about.gitlab.com/blog/gitlab-transcend-announcements/) |
| **GitLab Duo Agent Platform** | Agent Platform GA（2026-01） | [about.gitlab.com/blog/gitlab-duo-agent-platform-is-generally-available/](https://about.gitlab.com/blog/gitlab-duo-agent-platform-is-generally-available/) |
| **Zed Delta / DeltaDB** | commit 之间版本层；Git 伴侣 | [zed.dev/blog/introducing-delta](https://zed.dev/blog/introducing-delta) |
| **Graphite** | GitHub 上 stacked PR + review（独立产品） | [graphite.com](https://graphite.com/) |
| **GitHub Status** | 官方 incident 记录（如 2026-08-17） | [githubstatus.com](https://www.githubstatus.com/) |

### 对比与测评（第三方；观点非官方）

- **VentureBeat**（2026-08-17）：Origin 为 **wedge**——mirror GitHub、双向 PR sync；强调 Agent 时代 **procurement + governance** 新问题；SpaceX 收购后 **editor+host+model** 垂直整合的 CISO 难题。
- **Reuters / The Verge**（2026-03）：OpenAI **内部** GitHub 替代因 outage 动机；**可能不商用**；Microsoft 持股冲突叙事。
- **Pragmatic Engineer**（2026）：GitHub 可靠性下降与 **Agent 负载**；CTO 引述 PR 全链路耦合；第三方可用性追踪与官方 narrative 对照。
- **SiliconANGLE**（2026-08-17）：Origin 为收购后首个 major product update；集成 Vercel/Depot/Buildkite。
- **社区观点（HN 等，非事实源）**：对 Origin **SpaceX 信任**、vendor lock-in、skeptical 与 **Graphite/Tomas 信誉** 认可并存；多人呼吁 **Forgejo/Fediverse** 互操作——写入「行业情绪」，不作产品能力断言。

---

## 行业注记 · Cursor Origin Beta（2026-08）

> 快变事实块；与主框架解耦，复审时以 Tier 0 为准。

| 日期 | 事件 | 来源层级 |
|------|------|----------|
| 2025-12-19 | Cursor 收购 Graphite | Tier 1 媒体 |
| 2026-06-16 | Compile：Origin 演示 + SpaceX 收购协议 | Tier 1 |
| 2026-08-14 | Cursor 加入 SpaceX / SpaceXAI | Tier 0 [blog](https://cursor.com/blog/joining-spacex) |
| 2026-08-17 | Origin **Early Beta**；GitHub **7h47m** outage 同日 | Tier 0 Changelog + GitHub Status |
| 2026-08-21 | 仍为 Early Beta；**Agent-native features ship soon**（Changelog 原文） | Tier 0 |

**已验证增量（相对官方通稿）**：
- Enterprise **默认开启**、admin **opt-out**（Changelog + Tier 1 一致）。
- **独立数据治理条款** 对 Origin 原生托管尚未完整发布（Tier 1 多源 + 文档缺口）。

**未纳入主框架的传闻（验证失败或单源）**：
- 「Grok Origin」产品名；**Grok Build ↔ Origin 深度集成**（仅媒体推测）；**35% Agent PR**（非白名单二手源）。

---

## 延伸阅读与参考材料

- **Git 托管架构**：Cursor「Git at any scale」——Spokes 与 WAL 设计权衡（Tier 0 工程文）。
- **DORA / 2025 报告**：AI  adoption 与 delivery throughput / stability 关系——Agent 放大产出亦放大 breakage（VentureBeat 等引用；以 Google/DORA 原文为准）。
- **GitLab Agent-native epic**：Standalone repository API、commit-without-clone（[gitlab.com epic #21716](https://gitlab.com/groups/gitlab-org/-/work_items/21716)）。
- **站内相邻**：[code-review.md](code-review.md)（Graphite/CodeRabbit 等）、[coding.md](coding.md)（Agent 开 PR）、[llm-for-coding.md](../llm/llm-for-coding.md)（代码模型评测）。

---

*Agent 时代 Git 托管 · 知识块 · slug `git-hosting` · 2026-08-21*
