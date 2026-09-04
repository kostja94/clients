# Backend as a Service 簇 · 边界与产品独占

> **SSOT**：本文件 + Hub KB [`knowledge/tools/infrastructure/backend-as-a-service.md`](../../../knowledge/tools/infrastructure/backend-as-a-service.md)  
> **slug**：`backend-as-a-service`（**勿**用 `baas` 裸词作 slug——Banking as a Service 歧义；**勿**用 `stateful-backend` 作 slug——搜索量近零）  
> **keywordEn**：Backend as a Service (BaaS) · **keywordZh**：后端即服务  
> **更新**：2026-09-03

---

## 三分法（与 Agent 执行链）

| slug | 优化单位 | 典型问题 |
|------|----------|----------|
| **`backend-as-a-service`** | **App 共享状态 + 后端积木** | 「库/鉴权/文件/实时托管在哪？」 |
| **`agent-runtime`** | Agent **怎么跑完** | loop、checkpoint、HITL |
| **`workflow`** | **确定性 / 耐久步骤** | 长任务、重试、调度 |

Type A（Convex）可与 workflow **组合**，**不**互相吞并产品。

---

## Hub 内 Type（不拆 slug）

| Type | 机制 | Canonical 产品 |
|------|------|----------------|
| **A** Reactive / Stateful Sync | 函数级 query + mutation | **Convex** |
| **B** Postgres BaaS | Postgres + API + RLS + Realtime | **Supabase**、Nhost |
| **C** Document Realtime | NoSQL listener + 离线 | **Firebase** |
| **D** Sync Engine（注记） | 行/查询 sync → 本地 | Zero、Electric、PowerSync（日后可拆 `sync-engine`） |
| **E** 轻量/自托管 | Docker / 单二进制 | Appwrite、PocketBase |
| **F** 云厂商套件 | AWS/GCP 积木 | Amplify |

**正文可用、不作 slug**：`reactive backend`、`stateful sync`、`AI-native backend`。

---

## 产品独占（相对本簇）

| 产品 | Canonical |
|------|-----------|
| Convex、Supabase、Firebase、Nhost、Appwrite、PocketBase、Amplify | **`backend-as-a-service`** |
| Zero、Electric、PowerSync | 本页 Type D；深度文可另开 `sync-engine` |
| InstantDB | 对照/风险（云 sunset）；勿作推荐主榜 |
| LangGraph、Temporal、AgentCore | **`agent-runtime`** |
| Inngest、Trigger.dev、n8n、Zapier | **`workflow`** |
| OpenRouter、LiteLLM | **`api`** |
| Auth0、Clerk（专精 CIAM） | **`authentication`**（BaaS 内置 Auth 仅作能力栈提及） |
| Mem0、Zep | **`agent-memory`** |

---

## SEO

| 优先级 | 词 | 用途 |
|--------|-----|------|
| P0 | backend as a service · BaaS platforms · best BaaS | slug / H1 |
| P1 | Supabase vs Firebase · Convex vs Supabase | Hub 内 H2 |
| P2 | reactive backend · AI backend | Type A 段 |
| P3 | stateful backend | 仅解释 Convex 用语 |

发文路径：优先 **`/blog/backend-as-a-service`**。
