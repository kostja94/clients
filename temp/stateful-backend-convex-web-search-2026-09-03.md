# 深度搜索报告 — Stateful Backend（含 Convex）

> **检索基准日**：2026-09-03  
> **时间范围**：近 24 个月为主；Convex 融资与产品定位截至 2026-08  
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档  
> **Loop 轮次**：6 轮  
> **来源统计**：Tier 0 12 · Tier 1 4 · Tier 2 6  
> **置信度摘要**：Convex 官方定义与文档高度一致；品类 taxonomy 由官方 + InfoQ + 多家 Tier 1 对比稿互证；InstantDB 云托管关停为官方已确认事实

---

## 1. 执行摘要

**Stateful Backend（有状态后端）** 在 2025–2026 语境下，主要指：**把「应用共享状态 + 实时同步 + 业务逻辑」从传统「无状态 API + 客户端缓存」里抽出来，由平台统一管理会话、订阅、事务与一致性** 的后端形态。用户提到的 **Convex**（非 "convenx"）是该品类最常被引用的代表：官方自称 **Stateful Sync Platform / reactive backend platform**，用 TypeScript query/mutation 函数替代 SQL + REST + 手动 WebSocket/缓存失效。

同赛道还有 **Postgres 之上的 Sync Engine**（Zero、PowerSync、Electric）、**客户端关系型 Sync DB**（InstantDB，云托管 2027 关停、团队已加入 OpenAI）、**事件溯源 Local-First**（LiveStore）等。**Inngest / Trigger.dev / Temporal** 解决的是 **长运行工作流与步骤级持久状态**，与 Convex 的「在线协作态同步」重叠但不同层——常被组合使用而非直接替代。

社区对 Convex 的评价两极：**支持者**强调 reactive query、ACID、端到端 TypeScript 对 AI Agent 写码友好；**质疑者**关注 vendor lock-in、非 SQL、离线能力弱、write path 性能争议。2026-08 Convex 完成 **$57M Series B**（Insight Partners 领投），官方称数百万生产实例、近万付费团队，并明确将 **Agent + 人类共写代码** 作为核心叙事。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `Convex stateful sync platform site:convex.dev` | 官方「Stateful Sync Platform」定义；reactive DB + WebSocket push |
| R1 | `stateful backend AI agents Convex Inngest Trigger.dev` | Convex vs 工作流引擎分层；Agent 组件与 Workflow 组件 |
| R2 | `sync engines ElectricSQL Convex Zero 2025` | Zero/Electric/PowerSync 三分法；query-driven sync |
| R2 | `site:news.convex.dev Series B 57M` | 2026-08 Series B；Agent 叙事与 Components 隔离 |
| R3 | `site:news.ycombinator.com Convex reactive database` | 联合创始人技术解释：read-set 订阅、自定义事务层 |
| R4 | `InstantDB sync engine OpenAI team joins` | InstantDB 团队加入 OpenAI；云托管 2027-08-31 关停 |
| R5 | `PowerSync Postgres SQLite sync engine` | PowerSync 双向 sync + 自有 backend API 写路径 |
| R6 | `site:stack.convex.dev how convex works` | 开源 backend；sync worker + function runner + DB 三件套 |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线 Q1：Stateful Backend 是什么 | `stateful sync platform`, `reactive backend` | 已覆盖 |
| 概念基线 Q2：有哪些类型 | `sync engine taxonomy`, `local-first vs reactive BaaS` | 已覆盖 |
| 概念基线 Q3：知名产品 | `Convex Zero InstantDB PowerSync` | 已覆盖（无 Gartner MQ；用官方 + 对比稿 + npm/社区线索） |
| Convex 具体能力 | `site:docs.convex.dev overview` | 已覆盖 |
| 与 Firebase/Supabase 差异 | `Convex vs Firebase Supabase real-time` | 已覆盖 |
| AI Agent 语境 | `site:stack.convex.dev AI agents` | 已覆盖 |
| 社区反响 | `site:news.ycombinator.com Convex` | 已覆盖 |
| 中文语境 | `Convex 实时数据库 中文` | 权威源未覆盖（未见 36氪/量子位深度稿） |

---

## 4. 核心发现（多源验证）

### 4.1 Stateful Backend 是什么

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| **Stateful Backend** 指后端持久维护并同步**应用共享状态**（非每次请求重建），客户端通过**长连接订阅**获得一致视图 | [Convex Sync 官方页](https://www.convex.dev/sync) T0 | [Convex Docs Overview](https://docs.convex.dev/understanding/overview) T0 | 已确认 |
| 核心机制：**query 函数跟踪 read-set → 数据变更自动重算 → WebSocket 推送**；mutation 在 **ACID 事务**中执行 | [Convex Docs](https://docs.convex.dev/understanding/overview) T0 | [How Convex Works](https://stack.convex.dev/how-convex-works) T0 | 已确认 |
| 与传统三层栈对比：省去独立 **REST/GraphQL 层 + Redis 缓存 + 手动 invalidation + WebSocket 网关** | [Convex vs SQL](https://www.convex.dev/compare/sql) T0 | [Convex vs Relational DBs](https://stack.convex.dev/convex-vs-relational-databases) T0 | 已确认 |
| **相邻但不同**：Inngest/Trigger.dev/Temporal = **durability workflow**（步骤状态、重试、调度）；Convex = **在线数据 reactive sync** | [Convex AI Agents 组件文](https://stack.convex.dev/ai-agents) T0 | [Inngest vs Trigger.dev](https://www.promptstoproduct.com/inngest-vs-trigger-dev) T1 | 已确认 |

**可操作定义**：Stateful Backend = **Database + Sync Engine +（通常）Server Functions** 一体化，让 UI/Agent 以「订阅 query 结果」而非「拉取 REST + 本地拼状态」的方式读写共享状态。

**与相邻概念边界**：

| 相邻概念 | 边界 |
|----------|------|
| **BaaS（Firebase/Supabase）** | 也提供 DB+Auth；Stateful 强调 **函数级 reactive query** 与 **跨 UI 同一逻辑时刻一致性** |
| **CDN/Edge KV** | 键值缓存，无事务级 query 依赖跟踪 |
| **Workflow Engine** | 编排长任务步骤，不替代前端实时列表/购物车等在线态 |
| **Local-First CRDT** | 客户端为真相源之一；Stateful Sync 多为 **服务端权威 + 推送** |

---

### 4.2 Stateful Backend / Sync Engine 有哪些类型

分类依据：**状态权威位置 + 与现有 DB 的关系**（综合 [InfoQ Podcast](https://www.infoq.com/podcasts/rethinking-data-client-event-sourcing/) T1、[Convex 官方](https://www.convex.dev/sync) T0、[Zero 官方](https://zero.rocicorp.dev/) T0）。

| 类型 | 特征 | 典型场景 | 代表 |
|------|------|----------|------|
| **A. 一体化 Reactive BaaS** | 专有 DB + TS 函数 + 内置 sync/auth/storage/scheduling；**无 SQL** | 协作 SaaS、Agent 全栈原型、实时 dashboard | **Convex** |
| **B. Postgres 上 Query-driven Sync Engine** | 保留 Postgres；客户端 **query 定义同步切片**；本地 SQLite 副本 | 需要 SQL 生态 + 极致响应的 greenfield | **Zero** (Rocicorp) |
| **C. Postgres Read-path Sync** | **只 sync 读路径**；写仍走自有 API；HTTP/CDN fan-out | 已有 Rails/Node 后端，加实时读 | **Electric** |
| **D. Postgres ↔ SQLite 双向 Sync** | 逻辑复制/WAL → 客户端 SQLite；写回自有 API | 离线优先、现场作业、移动端 | **PowerSync** |
| **E. 客户端关系型 Sync DB** | 浏览器 triple store + InstaQL；默认 multiplayer/offline | Firebase 替代、前端主导 | **InstantDB**（云托管关停中） |
| **F. 事件溯源 Local-First** | 变更日志 → 客户端 materialized view | 需 undo/time-travel/确定性 merge | **LiveStore** |
| **G. Durable Workflow（非在线 sync 主叙事）** | Event/step 持久化、重试、人机回路 | Agent 长任务、ETL、邮件序列 | **Inngest**, **Trigger.dev**, **Temporal** |

**易混淆**：

- **Convex ≠ Postgres BaaS**：Convex Cloud 底层用 PlanetScale/MySQL 持久化，但开发者 API 是 **document-relational + TS 函数**，不是 SQL（[Docs](https://docs.convex.dev/understanding/overview)）。
- **Sync Engine ≠ 完整 Backend**：Zero/Electric/PowerSync 通常仍需 **自写写路径 API**；Convex 写路径内置在 mutation 中。
- **Real-time presence**（光标、在线人数）与 **data sync** 常被拆层（[johnny.sh 2026 选型文](https://johnny.sh/blog/choosing-a-sync-engine-in-2026/) T2 单源经验）。

---

### 4.3 知名产品 / 代表方案

| 场景或类型 | 代表产品 | 备注 | 来源 |
|-----------|----------|------|------|
| **一体化 Reactive BaaS** | **Convex** | 2026-08 Series B $57M；开源 backend [get-convex/convex-backend](https://github.com/get-convex/convex-backend)；云托管为主 | [Series B 公告](https://news.convex.dev/convex-raises-57m/) T0 |
| **Query-driven + Postgres** | **Zero** | Rocicorp（Replicache 后继）；`zero-cache` 有状态服务；开源可自托管 | [zero.rocicorp.dev](https://zero.rocicorp.dev/) T0 |
| **Read-path Postgres sync** | **Electric** | Elixir sync service；Shapes + HTTP；与 TanStack DB 组合 | [electric.ax](https://electric.ax/sync/postgres-sync) T0 |
| **Offline-first 双向 sync** | **PowerSync** | Postgres/Mongo/MySQL/SQL Server → 客户端 SQLite；写回 BYO API | [powersync.com](https://powersync.com/) T0 |
| **客户端关系型 sync** | **InstantDB** | 400 万 app / 25 亿事务（官方自述）；**团队 2026 加入 OpenAI**；云 **2027-08-31 关停**，转自托管 | [Instant 公告](https://www.instantdb.com/essays/instant_team_joins_openai) T0 |
| **Event-sourced local-first** | **LiveStore** | SQLite + event log；InfoQ 嘉宾自研，社区早期 | [InfoQ Podcast](https://www.infoq.com/podcasts/rethinking-data-client-event-sourcing/) T1 |
| **Legacy 实时 NoSQL** | **Firebase Firestore** | 文档监听；Convex 常作对比对象 | [HN Convex vs Firebase](https://news.ycombinator.com/item?id=31831623) T2 |
| **Postgres BaaS + Realtime** | **Supabase** | Postgres + Realtime CDC；非函数级 reactive | [Convex stack 对比文](https://stack.convex.dev/convex-vs-relational-databases) T0 |
| **Agent 工作流持久化** | **Inngest**, **Trigger.dev** | 与 Convex **组合**：Convex 存 thread/message，Trigger 跑长任务 | [Convex AI Agents](https://stack.convex.dev/ai-agents) T0 |

**市场份额**：该品类 **无 W3Techs/Gartner 统一份额**；Convex 官方 2026-08 称「millions of instances」「~10,000 paying teams」「1.2M+ weekly npm downloads」（[Series B](https://news.convex.dev/convex-raises-57m/) T0，**单源官方**）。

---

### 4.4 Convex 深度（用户所问「convenx」= Convex）

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 产品定位：**reactive backend platform** — Database + Functions + Workflow + Sync + Search + File Storage，全 TypeScript | [convex.dev 首页](https://www.convex.dev/) T0 | [Series B](https://news.convex.dev/convex-raises-57m/) T0 | 已确认 |
| 编程模型：`query`（只读）/ `mutation`（事务写）/ `action`（可调外部 API） | [Docs Overview](https://docs.convex.dev/understanding/overview) T0 | [How Convex Works](https://stack.convex.dev/how-convex-works) T0 | 已确认 |
| 客户端：`useQuery` 订阅；mutation 排队；**所有订阅对齐同一 DB 逻辑时刻** | [Docs](https://docs.convex.dev/understanding/overview) T0 | [HN cofounder 回复](https://news.ycombinator.com/item?id=40605530) T2 | 已确认 |
| 持久层：Cloud 版 **PlanetScale/MySQL**；开源版支持 SQLite/Postgres/MySQL | [Docs](https://docs.convex.dev/understanding/overview) T0 | [GitHub convex-backend](https://github.com/get-convex/convex-backend) T0 | 已确认 |
| **无完整离线 sync**；探索中；有客户用 Replicache 等 | [convex.dev/sync FAQ](https://www.convex.dev/sync) T0 | — | 已确认 |
| **Agent 友好**：Components 沙箱隔离；Agent 组件存 threads/messages/stream deltas | [Series B](https://news.convex.dev/convex-raises-57m/) T0 | [AI Agents 组件](https://stack.convex.dev/ai-agents) T0 | 已确认 |
| 合规：SOC 2 Type II、HIPAA；EU hosting 已上线 | [convex.dev](https://www.convex.dev/) T0 | [Series B](https://news.convex.dev/convex-raises-57m/) T0 | 已确认 |

**架构三件套**（[How Convex Works](https://stack.convex.dev/how-convex-works)）：**Sync Worker**（WebSocket 会话）+ **Function Runner**（跑 `convex/` TS）+ **Database**（自定义事务 + reactive invalidation）。

---

## 5. 时间线

| 日期 | 事件 | 来源（Tier） |
|------|------|-------------|
| 2021 | Convex 创立（Dropbox 背景联创） | [Series A](https://news.convex.dev/series-a/) T0 |
| 2022 | Series A $26M（a16z） | T0 |
| 2023-11 | 开源 single-machine backend | [HN cofounder](https://news.ycombinator.com/item?id=40020516) T2 |
| 2025-11 | $24M 成长轮（a16z + Spark） | [news.convex.dev](https://news.convex.dev/convex-raises-24m/) T0 |
| 2026-08-04 | **Series B $57M**（Insight Partners） | [Series B](https://news.convex.dev/convex-raises-57m/) T0 |
| 2026 | Instant 团队加入 OpenAI；Instant Cloud 计划 **2027-08-31** 关停 | [Instant 公告](https://www.instantdb.com/essays/instant_team_joins_openai) T0 |

---

## 6. 实体关系

```
┌─────────────────────────────────────────────────────────┐
│              Stateful Backend 品类光谱                    │
├─────────────────────────────────────────────────────────┤
│  一体化 BaaS          │  Convex, (InstantDB 云 sunset)   │
│  Postgres Sync Engine │  Zero, Electric, PowerSync        │
│  Local-First 框架     │  LiveStore, (Automerge 等)      │
│  Workflow 持久化      │  Inngest, Trigger.dev, Temporal   │
└─────────────────────────────────────────────────────────┘

Convex 典型栈：
  React/Next ──WebSocket──► Convex (query/mutation/action)
                              │
                              ▼
                         Reactive DB ◄──► MySQL (Cloud)

组合用法（Agent）：
  Convex (thread/state) + Trigger.dev/Inngest (长任务编排)
```

---

## 7. 增量信息

### 7.0 增量对照表（多源 diff）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源 | 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|---------|---------|---------|--------|
| Agent 时代「Postgres  objection」减弱 | Series B 文称 18 个月前客户执着 Postgres，现 Agent 委托实现选型 | [Series B](https://news.convex.dev/convex-raises-57m/) T0 | [Why AI agents love Convex](https://stack.convex.dev/why-ai-agents-love-convex) T0 | 已确认 | 已确认 |
| Components = Agent 的 context-window 单元 | 官方战略解读，非早期文档重点 | [Series B](https://news.convex.dev/convex-raises-57m/) T0 | — | 单源官方 | 很可能 |
| InstantDB 云托管关停 | 2027-08-31；新注册关闭 | [Instant 公告](https://www.instantdb.com/essays/instant_team_joins_openai) T0 | [instantdb.com/docs](https://www.instantdb.com/docs) T0 | 已确认 | 已确认 |
| HN 对 write-path read-set 交集的性能质疑 | 写路径需查 subscription 表，可能影响吞吐 | [SurrealDB 1.0 讨论串](https://news.ycombinator.com/item?id=38059276) T2 | [Convex cofounder 技术解释](https://news.ycombinator.com/item?id=38062228) T2 | 技术争议 | 待核实（设计权衡，非 bug） |
| BuildPilot 称 Convex ~50ms vs Supabase ~200-500ms | 非独立 benchmark | [BuildPilot 2026](https://trybuildpilot.com/644-convex-vs-firebase-vs-supabase-real-time-2026) 非白名单 | — | 验证失败 | — |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| Convex 2026-08 融资 $57M，累计约 $110M+ | [Series B](https://news.convex.dev/convex-raises-57m/) T0 | 已确认 | 官方 |
| 客户包括 OpenAI、Tripadvisor、Solana、Zapier、Reducto（官方列举） | Series B T0 | 很可能 | 单源官方 |
| Instant 开源可自托管；云迁移指南已发布 | Instant T0 | 已确认 | |
| Convex Workflow 组件语法 **Inngest-inspired** | [AI Agents 文](https://stack.convex.dev/ai-agents) T0 | 已确认 | 官方 stack 文 |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源 | 拒绝原因 |
|----------|------|---------|
| Convex 延迟全面优于所有竞品 ~50ms | BuildPilot/StarterPick 等对比博客 | §2.3 排除的 SEO/对比农场；无独立 benchmark |
| Electric「应完全避免」 | johnny.sh 个人博客 T2 | 单源 Tier 2 观点，非事实 |

### 7.3 权威媒体解读

- **VentureCapitalTracker / LinkedIn 转述**：Convex 将 DB、函数、实时 sync 打包，瞄准「AI agent 写码需要单一连贯 substrate」——与官方 Series B 叙事一致（T1 转述官方，**非独立 Tier 1 深稿**）。
- **InfoQ Podcast（Local-First 嘉宾）**：行业正从三层 Web 栈转向 **client-side event sourcing** 或 **query-driven sync engine** 两路 — 为 Convex/Zero/Electric 提供品类语境（T1）。

### 7.4 社区与舆论反响

**HN 观点分布**（Tier 2，非唯一事实源）：

- **支持**：reactive UI 消除「改用户名要刷新 N 处」；mutation 确定性 + 客户端重试；端到端 TS；对 Firebase security rules 的替代。
- **质疑**：vendor lock-in；非 SQL；write subscription 交集算法在复杂 join 下的 scalability（[38059276 讨论](https://news.ycombinator.com/item?id=38059276)）；full-stack framework 是否过度封装（[40605530](https://news.ycombinator.com/item?id=40605530)）。
- **中立技术讨论**：联合创始人解释 read-set range 订阅机制（[38062228](https://news.ycombinator.com/item?id=38062228)）。

### 7.5 争议与风险

| 风险 | 说明 |
|------|------|
| **Vendor lock-in** | 专有 query/mutation 模型；迁移需重写 backend 逻辑 |
| **无 SQL / 无 JOIN 生态** | 复杂分析型查询需 export 或外接 warehouse |
| **离线能力弱** | 官方承认无 full offline sync（[sync FAQ](https://www.convex.dev/sync)） |
| **云托管为主** | 自托管开源版存在，但 enterprise 特性与云路径分化（[2025 融资文](https://news.convex.dev/convex-raises-24m/) 提 scale-up self-hosted） |
| **竞品动态** | InstantDB 云 sunset → 品类向 Convex 集中，亦提示 **托管 sync 初创风险** |

### 7.6 竞品与行业对照

| 维度 | Convex | Supabase | Firebase | Zero |
|------|--------|----------|----------|------|
| DB | Document-relational 专有 API | Postgres | Firestore NoSQL | Postgres + 本地 SQLite |
| Reactive 粒度 | **函数级 query** | 表/行 CDC | 文档 listener | **ZQL query** |
| 写路径 | mutation 内置 | RLS + API/Edge Fn | Client SDK + rules | Server API |
| 离线 | 有限 | 有限 | **强** | **强** |
| AI Agent 叙事 | **核心**（2026） | 一般 | 一般 | 一般 |

### 7.7 中文语境

检索范围内 **未见** 36氪/量子位/少数派对 Stateful Backend 或 Convex 的 Tier 1 深度稿。中文开发者讨论多分散于翻译社区与对比博客，**权威源未覆盖**。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| Convex 是否「开源可自托管」 | GitHub 有 convex-backend | 官方主推 Cloud；enterprise self-host「coming soon」 | 原型可自托管；生产 enterprise 需对照官方 enterprise 条款 |
| InstantDB 状态 | 开源活跃 | 云 2027 关停 | 新项目勿依赖 Instant Cloud；评估 Convex 或自托管 Instant |
| 「Stateful Backend」是否为行业标准术语 | Convex 营销用语 **Stateful Sync Platform** | 社区亦说 sync engine / reactive BaaS | 对外沟通可用，但选型文档应写清技术机制 |

---

## 9. 对用户问题的直接回答

### 9.1 Stateful Backend 是什么？

**Stateful Backend** 指后端**持续持有并同步应用共享状态**，而非无状态 API 每次从客户端拼装。典型能力包括：

1. **持久化数据库**（用户、会话、业务对象）  
2. **Sync Engine**：客户端 **订阅 query**，服务端数据变更 **自动推送**  
3. **事务一致性**：并发写不破坏跨 UI 的一致性（如库存 + 购物车数字）  
4. **（通常）Server Functions**：权限与业务逻辑与 DB 同平台  

**Convex** 把上述打包为 **Stateful Sync Platform**：你用 TypeScript 写 `query`/`mutation`，React 用 `useQuery` 订阅，WebSocket 由平台管理。

### 9.2 有哪些类型？

见 §4.2，简表：

1. **一体化 Reactive BaaS** — Convex  
2. **Postgres Query Sync** — Zero  
3. **Postgres Read Sync** — Electric  
4. **Postgres ↔ SQLite 双向** — PowerSync  
5. **客户端 Sync DB** — InstantDB（云 sunset）  
6. **Event-sourced Local-First** — LiveStore  
7. **Workflow 状态机**（Adjacent）— Inngest / Trigger.dev / Temporal  

### 9.3 有哪些知名产品？

**首选了解 Convex**（你提到的产品）：

- 官网：https://www.convex.dev/  
- 文档：https://docs.convex.dev/understanding/overview  
- 品类自述：https://www.convex.dev/sync  

**同赛道**：Zero、Electric、PowerSync、Supabase Realtime、Firebase、LiveStore；**Agent 长任务**常叠加 Inngest/Trigger.dev。

**选型速查**：

| 你的优先级 | 倾向 |
|-----------|------|
| 最快全栈 + Agent 写 TS + 实时协作 | **Convex** |
| 必须 Postgres + SQL | **Zero** 或 **Supabase** + Electric |
| 离线优先 / 现场无网 | **PowerSync** 或 **Zero** |
| 已有后端，只加实时读 | **Electric** |
| 长运行 Agent 工作流 | **Inngest/Trigger.dev** + 任选 DB |

---

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方

- https://www.convex.dev/
- https://www.convex.dev/sync
- https://docs.convex.dev/understanding/overview
- https://stack.convex.dev/how-convex-works
- https://stack.convex.dev/ai-agents
- https://stack.convex.dev/why-ai-agents-love-convex
- https://news.convex.dev/convex-raises-57m/
- https://github.com/get-convex/convex-backend
- https://zero.rocicorp.dev/
- https://electric.ax/sync/postgres-sync
- https://powersync.com/
- https://www.instantdb.com/essays/instant_team_joins_openai
- https://github.com/instantdb/instant/

### Tier 1 权威媒体

- https://www.infoq.com/podcasts/rethinking-data-client-event-sourcing/
- https://www.promptstoproduct.com/inngest-vs-trigger-dev

### Tier 2 补充（反响/社区）

- https://news.ycombinator.com/item?id=40020516
- https://news.ycombinator.com/item?id=40605530
- https://news.ycombinator.com/item?id=31831623
- https://news.ycombinator.com/item?id=38059276
- https://johnny.sh/blog/choosing-a-sync-engine-in-2026/

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-09-03，共 6 轮 loop。*
