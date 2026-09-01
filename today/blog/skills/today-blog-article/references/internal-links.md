# Today AI Blog — Internal Links Specification

> Phase 3 / 3.5 / 5 加载。内链规则 + 集群矩阵（文章未写前为规划态）。

---

## 一、硬性规则（R1–R7）

| 规则 | 要求 | 严重度 |
|------|------|:---:|
| **R1** | 每篇正文至少 **2** 条不同 `/blog/` slug 内链 | high |
| **R2** | 每篇被其他 blog 文章 backlink ≥1（发布后验证） | high |
| **R3** | 锚文本描述性；禁 `click here`、`learn more`、`this article` | high |
| **R4** | 同一目标 slug 单篇仅 **1 次** `<a>` | high |
| **R5** | TL;DR 内链 ≤1；正文分散在不同 H2 | medium |
| **R6** | Hub-Spoke 双向互链 | high |
| **R7** | 同集群优先；跨集群仅在自然延伸时 | medium |

---

## 二、产品页内链规则

| 路径 | 使用场景 | 限制 |
|------|---------|------|
| `/waitlist` | 主 CTA | ≤2 次/篇 |
| `/downloads` | 次 CTA、UseCase | ≤2 次/篇 |
| `/landing#proactive` | Proactive 相关 | 上下文自然 |
| `/landing#memories` | Memory 相关 | 上下文自然 |
| `/healthcare/*` | Healthcare 簇 | 链对应 spoke |
| `/privacy` | 健康数据、AI Provider | 合规引用 |

**禁止**：`/pricing`、`/compare/*`、`article.today.ai/*`

---

## 三、集群内链矩阵（规划）

### 3.1 Core Pillar 簇（AI personal agent）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| what-is-ai-personal-agent | Hub | 01, 02, 04, 05, /landing, /waitlist | 01, 02, 04, 05 |
| ai-personal-assistant-vs-ai-personal-agent | Spoke | 03, 05, 01, /waitlist | 03, 05 |
| ai-personal-agent-vs-work-agent | Spoke | 03, 04, 01, /waitlist | 03, 04 |

### 3.2 Brand 簇

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| what-is-today | Hub | 02, 03, /landing, /waitlist, /downloads | 02, 03 |
| meet-today | Spoke (vision) | 01, 03, /landing, /waitlist | 01, 03 |

### 3.3 Proactive 簇（规划）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| what-is-proactive-ai-assistant | Spoke | 03, 01, 09, /landing#proactive | 01, 02, 09 |

### 3.4 Memory 簇

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| living-memory-ai-assistant | Hub | 01, 03, /landing#memories | 01, 03, 04 |

### 3.5 Comparison 簇

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| best-ai-personal-assistant | Hub | 04, 05, 03 | 04, 05 |
| today-vs-chatgpt | Spoke | 03, 06, 02 | 04, 05, 06 |
| today-vs-apple-intelligence | Spoke | 03, 06, 05 | 05, 06 |

### 3.6 Proactive 簇

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| ai-morning-brief | Hub | 01, 08, /landing#proactive | 07, 08 |
| proactive-vs-reactive-ai-assistant | Spoke | 01, 07 | 07, 08 |

### 3.7 Healthcare 簇

| slug | 角色 | 应链向 | 应被链自 |
|------|------|-------|---------|
| ai-health-assistant-lifestyle | Hub | 16, 17, /healthcare, /waitlist | 16, 17, 18 |
| ai-meal-planner-guide | Spoke | 15, /healthcare/meal-planner | 15, 16 |

---

## 四、锚文本变体库（示例）

| 目标 slug | 允许锚文本 |
|-----------|-----------|
| what-is-ai-personal-agent | AI personal agent、what a personal agent means |
| ai-personal-assistant-vs-ai-personal-agent | AI personal assistant vs agent、assistant vs personal agent |
| ai-personal-agent-vs-work-agent | personal agent vs work agent、Cowork vs personal agent |
| what-is-proactive-ai-assistant | proactive AI assistant、what proactive means、acts before you ask |
| living-memory-ai-assistant | living memory、AI that remembers your context |
| today-vs-chatgpt | Today vs ChatGPT、how Today differs from ChatGPT |
| best-ai-personal-assistant | best AI personal assistant、top personal AI assistants |

---

*internal-links · v1.0 · 2026-09-01*
