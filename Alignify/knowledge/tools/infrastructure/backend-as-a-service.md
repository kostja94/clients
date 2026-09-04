# Backend as a Service（BaaS）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Backend as a Service / BaaS**（**非** Banking as a Service）——托管 **Auth + Database + Storage + Functions + Realtime**，前端经 SDK 直连，常见场景**无独立自写 server app**；验收以 **数据模型（SQL vs NoSQL vs reactive query）、实时一致性、可迁移性与计费可预测性** 为主。本页为 **BaaS 产品 SSOT**（完整 URL 表仅此一处）。人类登录框深写 → [authentication.md](authentication.md)；统一调模型 → [api.md](api.md)；Agent **怎么跑完** → [agent-runtime.md](../agent/agent-runtime.md)；确定性长任务 → [workflow.md](../agent/workflow.md)；Vibe 全栈绑定 → [vibe-coding.md](../coding/vibe-coding.md)。

**材料范围**：公开网络检索（Supabase / Firebase / Convex / Appwrite / PocketBase / Nhost / Amplify 官方文档与公告；Cloudflare Learning · BaaS 定义；InfoQ Local-First / Sync Engine 讨论；HN Convex 技术讨论；InstantDB OpenAI 收购公告）。调研底稿 `clients/temp/stateful-backend-convex-web-search-2026-09-03.md`。**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-09-03**。簇边界见 [`skills/knowledge-block/references/backend-as-a-service-cluster.md`](../../skills/knowledge-block/references/backend-as-a-service-cluster.md)。

**站内对照**：slug **`backend-as-a-service`** · KB only（发文走 `/blog/backend-as-a-service`）

**Tools 关键词与 slug 映射**：`keywordEn`: **Backend as a Service (BaaS)** · `keywordZh`: **后端即服务** · Secondary：`best BaaS` · `Supabase vs Firebase` · `Convex vs Supabase` · `reactive backend`（正文 Type A，**不**作 slug）

**站内相邻**：[authentication.md](authentication.md) · [api.md](api.md) · [agent-runtime.md](../agent/agent-runtime.md) · [workflow.md](../agent/workflow.md) · [vibe-coding.md](../coding/vibe-coding.md) · [app-builder.md](../coding/app-builder.md)

---

## 与相邻 slug 分流

| 维度 | **`backend-as-a-service`（本页）** | **`authentication`** | **`api`** | **`agent-runtime`** | **`workflow`** |
|------|----------------------------------|----------------------|-----------|---------------------|----------------|
| **典型买家问题** | 「App 后端（库+鉴权+文件+实时）托管在哪？」 | 「用户怎么登录我的 App？」 | 「怎么统一调用多模型？」 | 「Agent 任务怎么可靠跑完？」 | 「多步业务/Agent 长任务怎么编排？」 |
| **优化单位** | **应用共享状态 + 后端积木** | **人类身份 / 出站 OAuth** | **模型调用路由** | **Agent loop / durability** | **IF/THEN 或 step 持久化** |
| **验收核心** | 数据模型、realtime、锁定、定价 | AuthN/AuthZ、SSO、合规 | TTFT、$/token | checkpoint、HITL、trace | 流程成功率、重试 |
| **代表产品** | Supabase、Firebase、Convex | Auth0、Clerk | OpenRouter、LiteLLM | LangGraph、Temporal | Inngest、Trigger.dev、n8n |

**禁写注记**：LangGraph / Temporal / AgentCore → **`agent-runtime`**；Inngest / Trigger.dev 主叙事 → **`workflow`**（可与本页 Type A **组合**）；OpenRouter → **`api`**；Mem0 → **`agent-memory`**。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Backend as a Service（BaaS）/ 后端即服务**：云厂商提供预建后端能力（认证、数据库、文件存储、推送/实时、无服务器函数等），开发者主要写前端，通过 **SDK / 自动生成 API** 消费后端。**勿与** Banking as a Service（金融开户/支付基础设施）混淆——标题与 SEO 须写全称。
- **PaaS vs BaaS**：PaaS（Heroku、Railway）给你**跑自写 server app 的平台**；BaaS 常让你**少写甚至不写**独立 server，直接消费 Auth/DB/Storage。
- **FaaS / Serverless Functions**：按事件执行的函数（Cloud Functions、Edge Functions）；现代 BaaS 几乎都内嵌 FaaS，但 **FaaS ≠ 完整 BaaS**。
- **Reactive / Stateful Sync Backend**：BaaS 子形态——**query 函数自动跟踪依赖并推送结果**（Convex 自称 Stateful Sync Platform）；与「文档/行监听」Realtime **机制不同**。
- **Postgres BaaS**：以 **专用 Postgres 实例** 为真相源，自动生成 REST/GraphQL，权限常落在 **RLS**（Supabase、Nhost）。
- **Document Realtime BaaS**：以 NoSQL 文档库 + 客户端 listener 为主（Firebase Firestore）。
- **Sync Engine**：把服务端 DB（常是 Postgres）同步到客户端本地存储（SQLite/IndexedDB）的中间层（Zero、Electric、PowerSync）——**常需自写写路径**，本页 Type D 注记；完整产品地图以本页 Buyer 分流为准，深度可日后拆 `sync-engine`。
- **RLS（Row Level Security）**：在数据库层按行策略授权；Postgres BaaS 的默认安全叙事。
- **Vendor lock-in**：数据模型与 API 专有化导致迁出成本高——Firestore 通常高于专有 NoSQL / 专有 reactive API。

---

## Buyer 决策树

```
你要建的是 Agent 本身，还是 Agent/人写的 App 后端？
├─ Agent 本身（loop / 部署 / 观测）     → agent-runtime
├─ 只调 LLM API                        → api
├─ 只要登录框 / SSO                    → authentication
└─ App 的 DB + Auth + Storage + 实时   → 本页 BaaS
    ├─ 要 SQL / Postgres / 可迁移      → Type B（Supabase 等）
    ├─ 要函数级 reactive、少 glue、TS  → Type A（Convex）
    ├─ 移动离线 + 文档模型优先         → Type C（Firebase）
    ├─ 已有 Postgres，只加实时读/离线  → Type D（Zero / Electric / PowerSync）
    └─ Agent 长任务 / 重试             → 本页 + workflow（组合，非替代）
```

---

## 专题对照

### Type A–D（本页主分类 · 按数据与 sync 机制）

| Type | 机制 | 写路径 | 离线 | 典型场景 | 代表（见 §外链索引） |
|------|------|--------|------|----------|----------------------|
| **A · Reactive / Stateful** | 函数级 query 订阅；mutation 事务 | 平台 mutation | 弱 | 协作 SaaS、Agent 写 TS 全栈 | Convex |
| **B · Postgres BaaS** | Postgres + 自动 API + RLS + CDC Realtime | SDK / PostgREST / Edge Fn | 有限 | Web SaaS、向量/RAG、可迁移 | Supabase、Nhost |
| **C · Document Realtime** | NoSQL 文档 listener | Client SDK + Rules | **强** | 移动优先、离线同步 | Firebase |
| **D · Sync Engine（叠加）** | 行级/查询驱动 sync 到本地 | 常 BYO API | **强** | 已有后端加 local-first | Zero、Electric、PowerSync |

### 与云模型对照

| 模型 | 你管什么 | 本页关系 |
|------|----------|----------|
| IaaS | OS + 应用 | 非本页 |
| PaaS | 应用代码 | 相邻；可叠 BaaS 部分能力 |
| **BaaS** | 前端 + 少量函数 | **本页** |
| FaaS | 函数代码 | BaaS 的组件，非独立品类页 |

### AI / Agent 友好度（2026）

| 维度 | Type A（Convex） | Type B（Supabase） | Type C（Firebase） |
|------|------------------|--------------------|--------------------|
| Agent 写码 | TS end-to-end、少 glue | SQL + RLS，Agent 易写错策略 | Rules 语言与 NoSQL 查询限制 |
| 向量 / RAG | 内置 vector search | pgvector 成熟 | 扩展 / 外接 |
| 叙事 | 「developers and agents」 | 「Postgres + AI」 | Google 生态 Genkit 等 |

---

## 问题域（为何会出现这类产品）

- **前端主导交付**：移动与 SPA 时代，团队不愿先搭服务器、连接池、会话与文件管道。
- **积木重复**：Auth、CRUD API、文件、推送在每个项目重复建设 → 平台化打包。
- **实时成为默认 UX**：聊天、协作、库存、仪表盘要求订阅而非轮询。
- **Vibe / Agent 编码**：生成式全栈工具默认绑定 BaaS（Lovable↔Supabase、Firebase Studio 等）；买家需要「选哪家 BaaS」而非再写 Express。
- **锁定与迁出焦虑**：Firestore 开源 + 可自托管 vs 专有 API 的长期权衡推动品类对比文（Supabase vs Firebase、Convex vs Supabase）。

---

## 能力栈（概念拆分，非厂商功能表）

- **数据层**：关系表 / 文档 / document-relational；索引、事务、备份、分支。
- **访问层**：自动 REST/GraphQL、客户端 SDK、服务端 Admin API。
- **身份**：内置 Auth（可与 [authentication.md](authentication.md) 专精 CIAM 叠加或替换）。
- **授权**：RLS / Security Rules / 服务端 mutation 权限。
- **Realtime / Sync**：CDC、文档监听、或 reactive query invalidation。
- **Functions**：Edge / Cloud Functions 跑副作用（邮件、Webhook、调 LLM）。
- **Storage**：对象存储与权限绑定用户/行。
- **可选**：向量搜索、调度/cron、Presence、分支环境、EU 驻留。

---

## 形态谱系

| 形态 | 特征 | 适合 |
|------|------|------|
| **托管全栈 BaaS** | 一键项目、控制台、用量计费 | 多数 Web/移动 MVP |
| **开源自托管 BaaS** | Docker / K8s；数据在自有机房 | 合规、成本可控 |
| **单二进制 / 轻量** | SQLite + 一体二进制 | 一人 SaaS、内网工具 |
| **Reactive 专有运行时** | TS 函数即 API；强一致订阅 | 实时协作、Agent 全栈 |
| **Best-of-breed 拼装** | Neon/PlanetScale + Clerk + Inngest… | 已知瓶颈、拒绝全家桶 |

---

## 风险 · 合规 · 治理

- **Vendor lock-in**：专有 query 模型或 NoSQL 迁出成本高；Postgres 路径迁出相对容易但仍有 Auth/Storage 绑定。
- **计费惊喜**：按读次数（部分 NoSQL）或连接数失控；优先看定价模型是否可预测。
- **RLS / Rules 配错**：权限写在库层时，错误策略 = 数据裸奔；需策略测试与审计。
- **Realtime 扩展边界**：CDC/监听在高并发写下的延迟与成本；reactive 写路径的 subscription 匹配开销（社区争议点）。
- **托管关停风险**：InstantDB 云计划 2027 关停（团队加入 OpenAI）提醒：**开源可自托管 ≠ 托管永远在线**。
- **合规**：SOC2 / HIPAA / 区域驻留看各家 Enterprise；自托管把运维责任转回买家。
- **与 Agent 组合时的边界**：BaaS 管应用态；长任务 durability 仍常需 workflow/runtime，勿指望单一 BaaS 替代 Temporal 级编排。

---

## 落地碎片

1. **先定数据模型**：关系型 → Type B；强实时协作 + TS → Type A；移动离线文档 → Type C。
2. **Vibe 产物默认栈**：Lovable 等常绑 Type B——生产前确认 RLS、备份与迁出路径。
3. **Agent 全栈**：优先 Type A 或 Type B + 严格 schema；Components/沙箱边界利于 Agent 改局部。
4. **已有 Postgres**：不必换全家桶 → Type D sync 或仅加 Realtime。
5. **长任务**：邮件序列、多步 Agent → 叠 [workflow.md](../agent/workflow.md)，状态仍可落 BaaS。
6. **自托管门槛**：评估运维带宽；「开源」不等于零成本。
7. **对比文 SEO**：`Supabase vs Firebase`、`Convex vs Supabase` 用本页 Type 表，勿另开 slug。

---

## 工具与产品类型

| 类型 | 买家问题 | 见 |
|------|----------|-----|
| Type A Reactive | 「订阅 query、少写 glue」 | §外链索引 A |
| Type B Postgres | 「要 SQL 与可迁移」 | §外链索引 B |
| Type C Document | 「移动离线优先」 | §外链索引 C |
| Type D Sync Engine | 「已有 DB，加本地/实时」 | §外链索引 D |
| 轻量 / 自托管全家桶 | 「一人运维、Docker」 | §外链索引 E |
| 云厂商套件 | 「已在 AWS/GCP」 | §外链索引 F |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

### A · Reactive / Stateful Sync

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Convex** | TypeScript reactive backend：query/mutation/action + 自动 sync；2026-08 Series B | [convex.dev](https://www.convex.dev/) · [docs](https://docs.convex.dev/understanding/overview) · [sync](https://www.convex.dev/sync) |

### B · Postgres BaaS

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Supabase** | 开源 Postgres 开发平台：Auth、Storage、Realtime、Edge Functions、pgvector | [supabase.com](https://supabase.com/) |
| **Nhost** | Hasura GraphQL + Postgres + Auth/Storage 的 BaaS | [nhost.io](https://nhost.io/) |

### C · Document Realtime

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Firebase** | Google 系 Auth、Firestore、Functions、Hosting；移动与离线成熟 | [firebase.google.com](https://firebase.google.com/) |

### D · Sync Engine（叠加层 · 非完整 BaaS 替代）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Zero** | Rocicorp query-driven sync：Postgres + 客户端 SQLite | [zero.rocicorp.dev](https://zero.rocicorp.dev/) |
| **Electric** | Postgres read-path sync（Shapes） | [electric.ax](https://electric.ax/sync/postgres-sync) |
| **PowerSync** | Postgres/Mongo 等 ↔ 客户端 SQLite 双向 sync | [powersync.com](https://powersync.com/) |

### E · 轻量 / 开源自托管全家桶

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Appwrite** | 开源自托管 BaaS（Auth、DB、Storage、Functions） | [appwrite.io](https://appwrite.io/) |
| **PocketBase** | 单二进制 + SQLite 的轻量后端 | [pocketbase.io](https://pocketbase.io/) |

### F · 云厂商套件

| 名称 | 一句话 | URL |
|------|--------|-----|
| **AWS Amplify** | Cognito + AppSync/DynamoDB + S3 等组合式 BaaS | [aws.amazon.com/amplify](https://aws.amazon.com/amplify/) |

### 对照与风险（非主榜）

| 名称 | 注记 | URL |
|------|------|-----|
| **InstantDB** | 曾为 client-side sync BaaS；团队加入 OpenAI，**云托管计划 2027-08-31 关停**，转自托管 | [instantdb.com](https://www.instantdb.com/) |

### 对比与测评（观点-only）

- Cloudflare Learning：[What is BaaS?](https://www.cloudflare.com/learning/serverless/glossary/backend-as-a-service-baas/) — PaaS vs BaaS 边界
- Convex stack：[How Convex Works](https://stack.convex.dev/how-convex-works) · [Why AI agents love Convex](https://stack.convex.dev/why-ai-agents-love-convex)
- InfoQ：[Local-First / client event sourcing](https://www.infoq.com/podcasts/rethinking-data-client-event-sourcing/) — sync 边界语境
- HN：[How Convex Works 讨论](https://news.ycombinator.com/item?id=40020516)（技术细节，非产品背书）

---

## 延伸阅读 · 站内外

**站内**

- 人类身份 / 出站 OAuth：[authentication.md](authentication.md)
- 统一模型 API：[api.md](api.md)
- Agent 执行层：[agent-runtime.md](../agent/agent-runtime.md)
- 长任务编排：[workflow.md](../agent/workflow.md)
- Vibe 全栈常绑 BaaS：[vibe-coding.md](../coding/vibe-coding.md) · [app-builder.md](../coding/app-builder.md)
- 簇边界（skills）：[`backend-as-a-service-cluster.md`](../../skills/knowledge-block/references/backend-as-a-service-cluster.md)

**站外**

- [Convex Series B](https://news.convex.dev/convex-raises-57m/)（2026-08）
- [Instant team joins OpenAI](https://www.instantdb.com/essays/instant_team_joins_openai)
