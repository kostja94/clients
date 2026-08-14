# "Data Engineering Agent" 关键词簇内容策略

> **目标**：围绕核心词 `data engineering agent` 构建完整的关键词簇，通过 hub-spoke 模型建立品类搜索权威。
> **引用**：[datus-keywords.md](../datus-keywords.md) | [datus-competitors.md](../datus-competitors.md) | [datus-positioning.md](../datus-positioning.md)
> **日期**：2026-06-03

---

## 一、核心逻辑：Hub-and-Spoke 关键词簇模型

```
                         ┌─────────────────────────────┐
                         │  What Is a Data Engineering  │
                         │       Agent? (PILLAR)         │
                         │          ✅ 已完成             │
                         └──────────────┬──────────────┘
                                        │
         ┌──────────────┬───────────────┼───────────────┬──────────────┐
         │              │               │               │              │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │概念定义  │    │对比选择  │    │操作指南  │    │场景应用  │    │技术深潜  │
    │Cluster 1│    │Cluster 2│    │Cluster 3│    │Cluster 4│    │Cluster 5│
    └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**设计原则**：
- Pillar 页覆盖最宽泛的定义型搜索（"what is a data engineering agent"）
- 每个 Cluster 覆盖一类搜索意图的子关键词——通过内链回 Pillar，形成权重闭环
- 文章之间互相引用（不重复定义），让 Google 理解这是一组有组织的专题内容

---

## 二、五类搜索意图 × 关键词簇

### Cluster 1：概念定义（Informational — "What is" 型搜索）

**用户画像**：第一次听说品类，想理解「数据工程 Agent 到底是什么」的人。可能是被 Hacker News/Reddit 引过来的工程师，也可能是搜 "AI data engineering agent" 的产品经理。

| 目标关键词 | 搜索意图 | 已有覆盖 | 缺口 |
|-----------|---------|:---:|------|
| `what is a data engineering agent` | 品类定义 | ✅ Article #1 | — |
| `data engineering agent definition` | 简洁定义 | ✅ Article #1（FAQ 区） | — |
| `AI data engineering agent` | 品类确认（是不是 AI 的？） | ⚠️ 部分（Article #1 有提到但非核心） | 需要一篇更聚焦「AI 原生」的文章 |
| `contextual data engineering` | Datus 自创概念——搜索量目前为零，但品类叙事需要 | ❌ | 急需——已在 plan 中 |
| `evolvable context for data` | 同上，v0.3 核心概念词 | ❌ | 可合并到 contextual data engineering |
| `what is a data agent` | 更泛的关键词（不做数据也能用） | ❌ | 低优先——可以放 glossary |

**待写文章（本 Cluster）**：

| # | 标题 | Target Keyword | 优先级 | 说明 |
|---|------|---------------|:---:|------|
| C1-1 | **Contextual Data Engineering: Why Your Agent Needs Evolvable Context** | `contextual data engineering` | 🔴 高 | Datus 品类定义文章。定义这个自创概念 → 让搜索从零变成有。同时覆盖 `evolvable context for data`、`context engineering data`。**这是 Datus 在搜索引擎里的品类出生证明。** |

*注：Article #1 已经覆盖了 "what is a data engineering agent" 和 "data engineering agent definition"，本 Cluster 不再重复。*

---

### Cluster 2：对比选择（Commercial Investigation — "vs" / "best" / "alternative" 型搜索）

**用户画像**：已经知道什么是 data engineering agent，正在评估选哪个。搜索 "best data engineering agent"、"data engineering agent comparison" 或 "X vs Y"。这是**转化率最高的搜索意图**——搜这些词的人离做决策很近。

| 目标关键词 | 搜索意图 | 已有覆盖 | 缺口 |
|-----------|---------|:---:|------|
| `best data engineering agents` | 品类横向对比 | ❌ | 急需——这是品类关键词簇里最高价值的词之一 |
| `data engineering agent comparison` | 对比评测 | ❌ | 同上，可合并到 "best" 文章 |
| `open source data engineering agent` | 找开源方案 | ❌ | Datus 核心定位词——必须有独立文章 |
| `data engineering agent vs Claude Code` | 通用 vs 专用 Agent | ❌ | 已在 plan 中（#7） |
| `data engineering agent vs SQL copilot` | 品类型对比 | ❌ | 区分 "agent" vs "copilot"——品类叙事需要 |
| `data engineering agent vs text-to-SQL` | 同上，更泛 | ⚠️ Article #1 FAQ 有提 | 可独立成篇 |
| `Datus alternative` | 品牌流失拦截 | ❌ | 低优先——先有使用者再说 |
| `data engineering agent for Snowflake` | 平台特定搜索 | ❌ | 中等——承接 Snowflake 用户搜索 |

**待写文章（本 Cluster）**：

| # | 标题 | Target Keyword | 优先级 | 说明 |
|---|------|---------------|:---:|------|
| C2-1 | **Best Data Engineering Agents in 2026: An Honest Comparison** | `best data engineering agents` / `data engineering agent comparison` | 🔴 高 | 横向对比 BigQuery DEA / Adobe DEA / Claude Code subagent / Datus / Wren AI / Altimate——**最高转化意图的文章**。别写成软文，写成像 Wirecutter 一样的 honest comparison——承认每个产品的长处，然后说明 Datus 适合什么样的团队。Google 的 product review update 奖励这种写法。 |
| C2-2 | **Open Source Data Engineering Agents: Why They Exist, When to Use One, and What Your Options Are** | `open source data engineering agent` | 🔴 高 | Datus 核心定位词。讲清楚为什么数据工程 Agent 需要开源（可审计、可自托管、不被平台绑定），对比 Datus / Wren AI / Altimate / Vanna（已归档），说明开源 vs 平台嵌入 vs SaaS 的 tradeoff。 |
| C2-3 | **Data Engineering Agent vs. Claude Code: When to Use Which** | `data engineering agent vs Claude Code` / `Claude Code for data engineering` | 🟡 中高 | 已在 plan 中（#7）。叙事：不是对抗，是补位——Claude Code 很强，但 data engineering 需要持久上下文。 |
| C2-4 | **Data Engineering Agent vs. SQL Copilot: What's the Real Difference?** | `data engineering agent vs SQL copilot` / `data engineering agent vs text-to-SQL` | 🟡 中 | 品类区分文章。定义在 Article #1 FAQ 中已有雏形——展开成独立文章：copilot 回答问题，agent 积累知识。 |

*注：具体竞品对比页（/vs/wren-ai、/vs/altimate 等）是独立 URL 的对比页，不计入 blog 文章簇。它们通过内链从 blog 文章引流。*

---

### Cluster 3：操作指南（Transactional — "how to" 型搜索）

**用户画像**：已经决定试试 data engineering agent，想知道怎么开始。搜索 "how to build a data engineering agent"、"data engineering agent tutorial"、"data engineering agent setup"。这是从「了解」到「动手」的最后一步——也是注册/安装转化率最高的内容。

| 目标关键词 | 搜索意图 | 已有覆盖 | 缺口 |
|-----------|---------|:---:|------|
| `how to build a data engineering agent` | 实操入门 | ❌ | 高价值——搜索量可能低但转化率极高 |
| `data engineering agent tutorial` | 教程 | ❌ | 同上 |
| `data engineering agent quickstart` | 快速开始 | ❌ | 同上 |
| `data engineering agent setup` | 安装配置 | ❌ | 同上 |
| `build your first data engineering agent` | 动手实验 | ❌ | 同上——更有号召力 |
| `data engineering agent CLI` | CLI 使用 | ❌ | CLI First 定位需要一篇文章承接 |
| `pip install data engineering agent` | 安装指令搜索 | ❌ | 极长尾但 100% 转化 |

**待写文章（本 Cluster）**：

| # | 标题 | Target Keyword | 优先级 | 说明 |
|---|------|---------------|:---:|------|
| C3-1 | **How to Build Your First Data Engineering Agent in 15 Minutes** | `how to build a data engineering agent` / `build your first data engineering agent` | 🔴 高 | 动手教程。Quickstart 式的 step-by-step——从 pip install 到第一条 SQL 查询。内置 California Schools 数据集演示。结尾 CTA → Cloud Personal 免费版或 GitHub Star。 |
| C3-2 | ~~A Data Engineer's Guide to Running the Modern Data Stack from a CLI~~ | `data engineering agent CLI` / `CLI data engineering` | 🔀 已合并 | **已合并入 C3-1 §What your daily workflow looks like**（2026-06-03）。9:00-9:35 时间线叙事 + 命令表 + CLI vs GUI 分工均保留。#06 现在覆盖 tutorial + daily workflow 两个搜索意图。 |

*注：具体数据库的 setup guide（Snowflake/PostgreSQL 等）放在 docs.datus.ai 而非 blog。Blog 只做概念层级的 how-to。*

---

### Cluster 4：场景应用（Commercial Investigation — 按 Persona / Use Case 搜索）

**用户画像**：想知道「这东西对我的团队有什么用」的人。搜索 "data engineering agent for data engineers"、"one person data team agent"、"enterprise data engineering agent"。

| 目标关键词 | 搜索意图 | 已有覆盖 | 缺口 |
|-----------|---------|:---:|------|
| `one person data team agent` | 个人提效场景 | ❌ | v0.3 核心场景，Artikel #1 提到但未展开 |
| `full stack data engineer agent` | 同上 | ❌ | 已在 keywords 文档中规划 |
| `data engineering agent for data engineers` | 工程师场景 | ❌ | — |
| `enterprise data engineering agent` | 企业场景 | ❌ | 对应 Enterprise 版 |
| `data engineering agent use cases` | 场景总览 | ❌ | 可放到 use case 落地页 |

**待写文章（本 Cluster）**：

| # | 标题 | Target Keyword | 优先级 | 说明 |
|---|------|---------------|:---:|------|
| C4-1 | **One-Person Data Team: How a Data Engineering Agent Multiplies Your Output** | `one person data team agent` / `one person data team` | 🟡 中高 | 对应 v0.3 "From one-man data teams..." 叙事。讲一个人怎么用 Datus 管整个 modern data stack——不是替代团队，是把重复性工作封装成 agent。 |
| C4-2 | **What an Enterprise Data Engineering Agent Actually Needs** | `enterprise data engineering agent` | 🟢 中 | 面向 Decision Maker。不讲功能清单，讲需求：Context versioning / RBAC / Audit log / Long-running agents / Shared context。用云器案例的量化数据（15%→60%）做 proof point。结尾 CTA → Contact Us for Enterprise。 |

---

### Cluster 5：技术深潜（Informational — 专家型阅读）

**用户画像**：已经用了 Datus（或在深度评估），想理解背后的技术设计理念。搜索 "context engine data engineering"、"subagent data engineering"、"MCP data engineering"。

| 目标关键词 | 搜索意图 | 已有覆盖 | 缺口 |
|-----------|---------|:---:|------|
| `context engine data engineering` | 技术架构 | ❌ | Datus 核心技术概念 |
| `subagent data engineering` | 同上 | ❌ | Datus 独有概念 |
| `MCP data engineering` | MCP 在数据工程中的应用 | ❌ | MCP 搜索在上升——早占位 |
| `AI agent data pipeline` | 更泛的 AI pipeline agent | ❌ | 中等——偏泛 |
| `data engineering agent accuracy` | Agent 准确率问题 | ❌ | 痛点词 |

**待写文章（本 Cluster）**：

| # | 标题 | Target Keyword | 优先级 | 说明 |
|---|------|---------------|:---:|------|
| C5-1 | **How a Context Engine Makes Data Engineering Agents More Accurate** | `context engine data engineering` / `data engineering agent context` | 🟡 中高 | 从 Article #1 第 6 节 "Context is what separates..." 展开。讲清楚：Context Engine 如何提升 text-to-SQL 准确率（Schema Linking + Semantic Model + Reference SQL + Feedback Loop）。别写成产品页——写成工程问题。 |
| C5-2 | **Subagents: How to Ship Domain-Specific Data Agents Without Training a Model** | `subagent data engineering` | 🟢 中 | Scoped Context → Chatbot → API 的完整链条。一个概念的科普 + 一个 Datus 的实现演示。 |
| C5-3 | **MCP and Data Engineering: The Protocol That Connects Your Entire Stack** | `MCP data engineering` / `MCP protocol data engineering` | 🟡 中高 | MCP 在数据工程中的实际应用——作为 MCP Client 接 Airflow/soda-core，作为 MCP Server 暴露给 Claude Code。MCP 在 2026 年快速上涨——此文是品类占位。 |

---

## 三、文章优先级矩阵

按「搜索量 × 转化价值 × Datus 战略重要性」排序：

| 优先级 | # | 标题 | Cluster | 为什么 |
|:---:|---|------|:---:|------|
| 🔴 P0 | C2-1 | Best Data Engineering Agents in 2026 | 对比选择 | 最高转化意图；品类词簇里价值最高的搜索词 |
| 🔴 P0 | C1-1 | Contextual Data Engineering: Why Your Agent Needs Evolvable Context | 概念定义 | Datus 品类出生证明——定义这个概念等于定义这个品类 |
| 🔴 P0 | C2-2 | Open Source Data Engineering Agents | 对比选择 | 核心定位词；区分 Datus 与平台绑定 Agent |
| 🔴 P0 | C3-1 | How to Build Your First Data Engineering Agent in 15 Minutes | 操作指南 | 最高转化率——从阅读到安装的最后一步 |
| 🟡 P1 | C2-3 | Data Engineering Agent vs. Claude Code | 对比选择 | 高频对比搜索；补位叙事（不是对抗） |
| 🟡 P1 | C2-4 | Data Engineering Agent vs. SQL Copilot | 对比选择 | 品类区分——让搜 "SQL copilot" 的人理解 agent 的价值 |
| 🟡 P1 | C4-1 | One-Person Data Team | 场景应用 | v0.3 核心叙事；承接个人提效场景搜索 |
| 🟡 P1 | C5-1 | How a Context Engine Makes Agents More Accurate | 技术深潜 | Datus 核心技术壁垒的内容化 |
| 🟡 P1 | C5-3 | MCP and Data Engineering | 技术深潜 | MCP 搜索上升期；品类占位 |
| 🟢 P2 | ~~C3-2~~ | Guide to Running Modern Data Stack from CLI | 🔀 已合并入 C3-1 | 2026-06-03 合并 |
| 🟢 P2 | C4-2 | What an Enterprise Data Engineering Agent Needs | 场景应用 | 企业决策者内容；POC→Enterprise 转化辅助 |
| 🟢 P2 | C5-2 | Subagents: Domain-Specific Data Agents | 技术深潜 | Datus 独有概念；专家型内容建立技术权威 |

---

## 四、与现有内容的关系

```
                    Article #1（Pillar）
                    "What Is a DE Agent?"
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    Article #2      本方案 12 篇      Glossary
    "What Is a        blog 文章        /glossary
    Semantic Layer"   （上表）
         │
    └─── 互补角色 ───┘
    Article #2 定义 semantic layer
    → C5-1 解释 Context Engine 如何操作化语义层
    → C2-4 区分 agent vs copilot（semantic layer 是 copilot 的短板）
```

**内链范围约束**：
- Blog 文章**仅做 blog 互链 + glossary 引用**，不链向产品页（/agent、/features/*、/use-cases/*、/vs/*、/case-studies/*）
- Glossary（/glossary）为唯一站内非 blog 链接目标——术语定义型搜索通过 glossary 承接
- CTA 仅使用外部链接（GitHub、Datus Studio、docs.datus.ai）
- 后续产品页上线时再补链——blog 内容本身不应依赖未上线的页面

---

## 五、发布节奏建议

按照「先占品类、再做转化、最后建壁垒」的节奏：

**第 1 批（当月，4 篇）——品类定义 + 最高转化**：
1. C1-1: Contextual Data Engineering（品类出生证明）
2. C2-1: Best Data Engineering Agents 2026（最高转化意图）
3. C2-2: Open Source Data Engineering Agents（核心定位词）
4. C3-1: Build Your First Agent in 15 Minutes（最高转化率）

**第 2 批（次月，4 篇）——对比 + 场景**：
5. C2-3: DE Agent vs. Claude Code
6. C2-4: DE Agent vs. SQL Copilot
7. C4-1: One-Person Data Team
8. C5-3: MCP and Data Engineering

**第 3 批（第 3 月，4 篇）——技术深潜 + 企业**：
9. C5-1: How a Context Engine Makes Agents More Accurate
10. C4-2: What an Enterprise DE Agent Needs
11. ~~C3-2: Running Modern Data Stack from CLI~~ → merged into C3-1 (#06)
12. C5-2: Subagents: Domain-Specific Data Agents

---

## 六、每篇文章的内容框架（3 篇 P0 重点展开）

### C2-1: Best Data Engineering Agents in 2026

**结构**：
- 开头：2026 年，"data engineering agent" 是一个新品类，但各家做的根本不是同一件事（呼应 Article #1）
- 评测维度：环境（平台绑定 vs 跨栈）× 上下文（持久 Context vs 无状态）× 交付形态（CLI/Chat/API）× 开源 vs 闭源 × 适用团队规模
- 逐产品评（各 200-300 字）：BigQuery DEA / Adobe DEA / Claude Code subagent / Datus / Wren AI / Altimate / TextQL
- 决策框架：按团队类型推荐（全在 BigQuery → Google；想开源自托管 → Datus；dbt 重度 → Altimate）
- 结尾：没有 best for everyone——但你得先想清楚 agent 的 context 住在哪里

**关键词**：`best data engineering agents`, `data engineering agent comparison`, `top data engineering agents 2026`

### C1-1: Contextual Data Engineering

**结构**：
- 开头：数据工程的最大浪费不是写 SQL——是对同一张表、同一个指标、同一条业务规则反复重新理解（呼应 Bitter Lessons）
- 定义：Contextual Data Engineering = 把数据上下文（schema、指标、reference SQL、业务规则、反馈）作为**一等公民**管理，让它持续进化，而不是一次性建模
- 对比传统模式：传统：建模→交付→遗忘；Contextual：Agent 运行→反馈→上下文进化→下次更准
- 三层上下文：Schema Metadata（物理层）→ Business Semantics（语义层）→ Institutional Memory（反馈层——这是 Copilot 做不到的）
- 结尾：Contextual data engineering 不是一个 feature——它是 data engineering agent 的 operating system。没有它，agent 只是聪明一点的 SQL writer。

**关键词**：`contextual data engineering`, `evolvable context for data`, `context engineering data`, `data context system`

### C3-1: Build Your First Data Engineering Agent in 15 Minutes

**结构**：
- 开头：你不需要一个团队、一个审批流程、一个云预算——只需要 `pip install` 和 15 分钟
- Step 1: Install（`pip install datus-agent`）
- Step 2: Connect（连接内置 California Schools 数据集）
- Step 3: Ask（第一条 NL 查询："Show me schools with above-average math scores"）
- Step 4: Explore Context（看看 Context Engine 自动构建了什么——`@catalog` 浏览表结构）
- Step 5: Generate Semantic Model（`/gen_semantic_model`——自动理解哪些列是 measure、哪些是 dimension）
- Step 6: Create Subagent（`.subagent add`——把刚才的上下文封装成一个专用 Chatbot）
- Step 7: Share（给同事发 Subagent 链接）
- 结尾：这不是 demo——这就是 Datus 的日常工作流。接下来你可以连 Snowflake、导 MCP、接 Airflow。但第一步只需要 15 分钟。

**关键词**：`how to build a data engineering agent`, `build your first data engineering agent`, `data engineering agent tutorial`, `data engineering agent quickstart`

---

## 七、内链策略

**范围约束**：Blog 文章仅链向 blog 互链 + glossary，不链向产品页。

每篇文章的链接结构：

```
文章正文
  ├── 开篇 → Article #1（Pillar："如我们在《What Is a DE Agent》中定义的..."）
  ├── 概念出现时 → Glossary（/glossary 对应术语）——唯一非 blog 站内链接
  ├── 竞品提及时 → 竞品官方文档（外链 rel="nofollow noopener"）
  ├── 同类主题 → 其他 blog 文章互链（/blog/{slug}）
  ├── CTA → GitHub / Datus Studio / docs.datus.ai（外链）
  └── 文末 Related → 2-3 篇相关 blog 文章（双向互链 + frontmatter `related` 数组同步）
```

**关键原则**：
- 每篇文章的内链出口 ≥ 3 个（blog 互链 ≥ 2 + glossary ≥ 1）
- Pillar 文章（Article #1）被所有 cluster 文章引用——建立权重中心
- 每篇 Related 里的互链必须是**双向**的——发布新文章时同步更新旧文章的 Related frontmatter
- Glossary 是 blog → 站内非 blog 页面的唯一内链出口——术语定义型搜索通过 glossary 承接后续转化

---

## 八、成功指标

| 指标 | 3 个月目标 | 6 个月目标 |
|------|-----------|-----------|
| Blog 文章数 | 6 篇（含已有 2 篇 + 新增 4 篇 P0） | 14 篇（全部） |
| "data engineering agent" 搜索结果 | 前 10 | 前 3 |
| "contextual data engineering" 搜索结果 | #1（Datus 定义了这个词） | #1 |
| "best data engineering agents" 搜索结果 | 前 20 | 前 5 |
| "open source data engineering agent" 搜索结果 | 前 5 | 前 3 |
| Blog 月活 | 建立基线 | 2K+ |
| Blog → 产品页 CTR | 建立基线 | 15%+ |
| Blog → GitHub Star 转化 | 建立基线 | 可追踪 |

---

*关键词簇策略 v1.0 · Datus Blog · 2026-06-03*
