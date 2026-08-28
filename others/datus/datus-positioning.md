# Datus — 定位

> **本文档职责**：品类定义、One Story、Messaging Framework、竞争叙事、品牌策略。
> **引用**：[datus.md](./datus.md) 概览 | [datus-competitors.md](./datus-competitors.md) 竞品分析 | [datus-features.md](./datus-features.md) 功能 | [datus-use-cases.md](./datus-use-cases.md) 场景 | [datus-keywords.md](./datus-keywords.md) 关键词

**最近更新**：2026-05-24（根据 Datus 官方 Positioning & Message 0.3 重写）

---

## 0. 战略背景（创始人思考）

> 以下为 Datus 创始人赵恒在 v0.3 阶段的核心战略判断，作为定位的背景上下文。

**商业化路径调整**：

| 旧路径 | 新路径 |
|--------|--------|
| 开源推大互联网公司 → 中型公司（100K+ ARR） | 开源推个人提效 → 中型公司（100K+ ARR）或 小型公司（10K ARR） |

**关键决策**：
- **个人效率提升的部分全部开放出去**——因为个人提效难以量化是 AI 模型的价值还是 Datus 的价值，且 Claude Code 本身就具备这个能力
- **在开源基础上持续优化企业团队能力**——做企业版雏型，找 Expedia 这类客户验证
- **企业价值锚点不变**：Data Context Engine（org-level versioning）& Governance & Long Running Agents
- **北美机会**：为小 B 公司完成 Snowflake → Lakehouse 的迁移 + 部署管理运维（v0.3 尚达不到）

**风险认知**：
- 开源产品越来越难（商业化模式全部变了）
- 个人开发者需要教育——很多人会说"不一定 AI 有效"
- 关键行动：开源 Onboarding & SaaS Tutorial 要好好搞

---

## 一、One Story（统一品牌故事）

> 不分开源和企业版独立内容，都在一个主页上展现。

### 一句话定位

**Datus is the open-source data engineering agent that builds evolvable context for your data systems.**

### 两句话版本

> Datus is the open-source data engineering agent that builds evolvable context for your data systems.
>
> From one-man data teams to enterprise agent teams, Datus turns data work into reliable, reusable agent systems.

### 中文版

> Datus 是一个开源的数据工程 Agent，为你的数据系统构建可演进的上下文。
>
> 从一人数据团队到企业 Agent 团队——Datus 把数据工作变成可靠、可复用的 Agent 系统。

### 两条价值路径

| 路径 | 对个人 | 对企业 |
|------|--------|--------|
| **Slogan** | End-to-end data engineering productivity | Shared context, governance, and long-running data agents |
| **翻译** | 用 Datus 帮助你变成一个 one-man data team | 用 Datus 把分散的人和知识，变成一个稳定、可审计、可协作、可自动运行的 agent system |

---

## 二、Positioning 核心逻辑

### Who（目标受众）

> For engineers who want to run the modern data stack like a one-man data team,
> and for enterprises that want reliable, auditable, collaborative agent teams.

### What（产品定义）

> Datus is the open-source data engineering agent that builds evolvable context for your data systems. It turns data work into reusable context, and context into reliable agents, workflows, and team-scale automation.

### Why Now（为何是现在）

> Because one engineer can now do far more with LLMs and agents — but only if the data system is structured with reusable context. And enterprises can only trust agent teams when that context is stable, auditable, and collaborative.

### Why Different（差异化）

| 维度 | 对个人 | 对企业 |
|------|--------|--------|
| 不是 | 一个只会写 SQL 的 copilot | 一个孤立的 chatbot or ChatBI |
| 而是 | 一个能帮你把整个 modern data stack 管起来的 data engineering agent | 一个能让 agent 团队长期稳定运行的 context + audit + orchestration system |

---

## 三、Messaging Framework（3-Pillar）

### Pillar 1: One engineer can run the modern data stack with 10x productivity

| Sub-message | 说明 |
|------------|------|
| **Operate the full data system, not just one tool** | Connect and operate services across the modern data stack |
| **Manage the full data engineering lifecycle** | Turn workflows into reusable skills and manage them end to end |
| **Improve agent stability with validation loops** | Make data agents more reliable through testing, feedback, and iterative refinement |

### Pillar 2: Build evolvable context, for better accuracy

| Sub-message | 说明 |
|------------|------|
| **Turn semantics into usable context** | Capture metrics, semantic models, business rules, and reference logic in a reusable context layer |
| **Build chatbots that learn and evolve** | Let chatbots improve through feedback, usage, and changing business needs |
| **Embedded data skills that improve through usage and feedback** | Build skills that adapt to your specifications, environment, and real workflows over time |

### Pillar 3: Scale from personal productivity to enterprise agent teams

| Sub-message | 说明 |
|------------|------|
| **Run agents autonomously and continuously** | Use harness engineering to support long-running, reliable agent execution |
| **Add control, safety, and versioning** | Govern agents with access control, sandboxing, approvals, and versioned changes |
| **Build a shared enterprise context knowledge graph** | Create a collaborative context graph / knowledge layer for teams and agent systems |

---

## 四、产品形态定位

| 层级 | 形态 | 入口 | 定位 |
|------|------|------|------|
| **Open Source** | 开源核心能力 | GitHub | Core capabilities for builders |
| **Cloud Personal** | 云端个人版（免费） | Datus Cloud | The easiest way to start and explore |
| **Enterprise** | 企业版 | 邮件联系 / 填信息 | Team-scale collaboration, enterprise-level access control and context store |

*注：定价详情见 [datus-features.md](./datus-features.md) §五。*

---

## 五、分受众 Messaging

| 受众 | 定位句 |
|------|--------|
| **Data Engineer** | Run the modern data stack like a one-man data team |
| **Data Team Lead** | Turn your team's data work into reusable systems, not repeated manual effort |
| **Decision Maker** | Scale data output without scaling data headcount |
| **Open Source Community** | Build the open context layer for AI-native data engineering |

---

## 六、Competitive Framing（竞争叙事）

> 总论述框架：
> **We do not compete as a generic coding assistant, a warehouse-native copilot, a chatbot, or a semantic layer. We are the open-source system that builds and evolves the data context those tools need to become reliable.**

### 6.1 vs Claude Code

| 维度 | 内容 |
|------|------|
| **一句话** | Claude Code is great at coding. Datus is purpose-built for data engineering. |
| **锋利版** | Claude Code helps you work on code. Datus helps you work on data systems. |
| **推荐话术** | Claude Code is the best general coding assistant. Datus is the specialized context system for data engineering — and that context can be exposed back to Claude Code through MCP. |
| **核心主张** | 我们不是反 Claude Code。我们是 **Claude Code for data engineering 的 missing layer**——或者更准确：**the data context layer for Claude Code**。 |

**不要说的**：
- ❌ "我们比 Claude Code 更强"
- ✅ "Claude Code 很强，但数据工程需要额外的数据上下文系统"

**关键支撑论据**：
- 数据工程不是普通 coding task——真正难的是 data context（metrics、semantic models、reference SQL、table semantics、validation loops、service integrations）
- 这些 context 不该只待在 Datus 里，可以通过 MCP 暴露给 Claude Code

### 6.2 vs Cortex Code / Genie Code（First-party AI for a single data platform）

| 维度 | 内容 |
|------|------|
| **一句话** | They are strong inside their own platforms. Datus is built for the open data stack. |
| **推荐话术** | Cortex Code and Genie Code are powerful first-party copilots for Snowflake and Databricks. Datus is for teams that want an open, cross-stack data engineering agent — not one bound to a single warehouse or control plane. |
| **核心主张** | 不否认它们的价值——但很多团队实际是 heterogeneous stack（catalog、warehouse、semantic layer、BI、scheduler 都是混搭的）。Datus 赢在 **开放、跨栈、可迁移、可组合**。 |

**关于成本**：
> "1/3–1/10 成本" 很有吸引力，但有 benchmark 之前不要当主句。更稳的讲法：Use open systems to build a modern data stack with far more flexibility — and often at materially lower cost.

### 6.3 vs ChatBI

| 维度 | 内容 |
|------|------|
| **一句话** | ChatBI is the interface. Datus builds the system behind the interface. |
| **推荐话术** | Most ChatBI products optimize the chat experience. Datus helps engineers continuously build and evolve the context, metrics, skills, and workflows that make ChatBI reliable over time. |
| **简短版** | We do not just ship chatbots. We help engineers build evolvable ChatBI systems. |
| **核心主张** | Chatbot 只是交付层，Datus 的重点是**可演进的后端 context system**。不是一次性 chatbot，而是 **evolvable ChatBI infrastructure**。 |

### 6.4 vs Semantic Layer

| 维度 | 内容 |
|------|------|
| **一句话** | A semantic layer defines business logic. Datus helps build it, strengthen it, and put it to work in agents and workflows. |
| **推荐话术** | Semantic layers are essential, but they are not the whole system. Datus supports existing semantic layers, helps create one when it is missing, and turns semantic definitions into reusable context for agents, workflows, and chat experiences. |
| **锋利版** | Semantic layers define metrics. Datus operationalizes them. |
| **核心主张** | **Datus sits above and around the semantic layer**。不反 semantic layer，而是它的放大器、连接器、执行层、学习层。 |

**兼容性策略**：
- 已有 semantic layer → Datus 强化它
- 没有 semantic layer → Datus 帮你构建它
- 不同 semantic layer → Datus 做统一编排和上下文利用
- 内置 MetricFlow → 自己也能跑起来

---

## 七、竞争生态总览

| 竞争类型 | 代表 | Datus 定位 |
|---------|------|-----------|
| **通用 Coding Agent** | Claude Code | The data context layer — 专业垂直 + MCP 反向暴露 |
| **平台绑定 Copilot** | Cortex / Genie Code | Open, cross-stack — 不绑定单一 warehouse |
| **ChatBI** | 各类 ChatBI 产品 | The system behind the interface — 可演进后端 |
| **Semantic Layer** | MetricFlow / dbt Semantic Layer | The amplifier — 坐在 semantic layer 之上和周围 |

*完整竞品矩阵与分析见 [datus-competitors.md](./datus-competitors.md)。*

---

## 八、信任证据（Social Proof）

| 层级 | 证据 | 状态 |
|------|------|------|
| **开源证明** | Apache 2.0，~1.2K GitHub stars | ✅ |
| **企业 POC** | LinkedIn、Expedia、Coinbase | ✅ 进行中 |
| **生产案例** | 云器 Lakehouse：自助率 15%→60%，查询 30min→3min | ✅ 已发布 |
| **创始人信誉** | 赵恒，前阿里 + StarRocks TSC，裸辞创业 | ✅ |
| **行业演讲** | Agentic AI Summit 2026 北京站 | ✅ |
| **报道** | 多篇微信技术文章 + 云器官方博客 | ✅ |
| **Cloud Personal** | 免费云端版，降低体验门槛 | 🟡 待上线 |
| **定价透明度** | Enterprise contact 入口 | 🟡 待完善 |

---

## 九、推荐策略要点

1. **One Story 统一叙事**：不开源和企业版各自表述，所有页面围绕「builds evolvable context for your data systems」展开
2. **Onboarding 即获客**：开源 Onboarding & SaaS Tutorial 是当前最高优先级转化动作
3. **Competitive Framing 即内容**：vs Claude Code、vs ChatBI 等 framing 话术直接转化为 blog / 对比页内容（见 [datus-competitors.md](./datus-competitors.md) §五）
4. **个人端 → 企业端 漏斗**：开放个人效率工具引流 → 企业版 Context Engine + Governance 变现
5. **不反竞品，而是补位**：Claude Code 很强，Datus 是它的 data context layer；ChatBI 是界面，Datus 是界面背后的系统

---

*定位文档 v0.3-aligned · Datus · https://datus.ai/*
