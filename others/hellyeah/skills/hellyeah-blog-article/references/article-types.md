## §2 文章类型路由

收到任务后**先匹配类型**，再跳转对应 H2 模板。

### 2.1 路由表

| 类型 | 典型 intent | 词数 | 产品提及上限 | 参考 slug |
|------|------------|------|-------------|-----------|
| **Pillar** | 品类全景 / 方法论地图 | 3500–5000 | ≤20% | `programmatic-geo-vs-seo` |
| **Framework** | 可复用框架（非清单） | 2500–3200 | ≤25% | `continuous-growth-experiments` |
| **CommercialEducational** | AI ads / 品类教育 | 2800–3800 | ≤30% | `what-is-ai-ads-manager` |
| **PlatformExplainer** | 四平台/OS 分层 | 2200–3000 | ≤35% | `aima-vs-forge-vs-mutation` |
| **Alternative** | 对比 / 替代 | 2500–3500 | ≤30% | `hellyeah-vs-agency` |
| **UseCase** | 垂直场景 | 2200–3000 | ≤30% | `growth-for-mobile-apps` |
| **Diagnosis** | 瓶颈排查 | 2500–3200 | ≤25% | `why-roas-is-declining` |
| **Compliance** | 采购 / 信任 | 2000–2800 | ≤20% | `enterprise-marketing-platform-security` |

**路由规则**：
- `programmatic GEO` / `generative engine optimization` / `LLM SEO` → **Pillar**（P5 链 seo-geo）
- `continuous experiment` / `A/B throughput` → **Framework** 或 **PlatformExplainer**
- `event-driven` / `real-time signal` → **PlatformExplainer**（Mutation）
- `AI ads manager` / `ad optimization` / `unified dashboard` → **CommercialEducational**
- `vs agency` / `alternative` / `best AI growth platform` → **Alternative**
- `/for/{vertical}` 延伸 → **UseCase**
- `ROAS drop` / `visibility in ChatGPT` / `experiment backlog` → **Diagnosis**
- `SOC 2` / `GDPR marketing` / `enterprise security` → **Compliance**

### 2.2 全类型通用模块

| 模块 | 要求 |
|------|------|
| **Lead** | frontmatter 后第一段（第一个 `##` 前）；≤250 words；主题 + 对谁有用 + 独有角度 |
| **H2** | 英文描述性标题；**不编号** |
| **Conclusion** | `## Conclusion`（FAQ 之上） |
| **FAQ** | `## Frequently asked questions`；≥3 题；`### 问题` + 段落 |
| **内链** | ≥2 站内（capability/platform/customer/blog） |
| **外链** | 权威 2–8；竞品 nofollow |
| **CTA** | `/demo` 或 `/aima`；全文 ≤2 次 |
| **无 TL;DR** | 用 Lead 承担摘要 |

---

### 2.3 Pillar — H2 模板

**叙事弧线**：行业变化 → 分工地图（表格）→ 按 persona/org 分节 → 常见错误 → 工具注记（克制）→ 结论。

```
{Lead — 为何 2026 不同于旧指南}

## What's actually changed since {year}
## The {year} landscape map          ← 对比表：lane / owner / metric / hardest part
## How to divide labor — by team size
   ### If you are a Series A startup
   ### If you are mid-market with a growth pod
   ### If you are enterprise with procurement gates
## {N} mistakes that quietly kill {outcome}
## A note on platforms and command layers   ← Hellyeah 可出现；tool-agnostic 为主
## Conclusion
## Frequently asked questions
```

**Pillar 专属**：GEO Pillar 须链 `/capabilities/seo-geo`（P5）；须链 planned Spoke。

---

### 2.4 Framework — H2 模板

**禁止**写成 "50 checkpoints you can copy"。

```
{Lead — 清单文为何不是策略}
## Why {topic} lists are not a strategy
## The {N} principles that govern {outcome}
   ### Principle 1: …
   ### Principle 2: …
   ### Principle 3: …
## Matching principles to org maturity   ← 表格
## How to operationalize without adding headcount
## Conclusion
## Frequently asked questions
```

---

### 2.5 CommercialEducational — H2 模板

```
{Lead — 定义品类，非推销}
## What an AI ads manager actually does (and does not)
## How it differs from dashboards, MMPs, and agencies
## Evaluation criteria for {persona}
## Common failure modes when buying
## Where a command layer fits   ← 克制 Hellyeah；链 /aima
## Conclusion
## Frequently asked questions
```

---

### 2.6 PlatformExplainer — H2 模板

```
{Lead — OS 视角，非功能清单}
## Why growth stacks split into layers
## AIMA: orchestration and conversation
## Forge: execution systems
## Mutation: intelligence from external signals
## Déjà Vu: experimentation (private alpha)
## How the layers compose in RCLL
## Conclusion
## Frequently asked questions
```

**P3**：Déjà Vu 必须标注 private alpha。

---

### 2.7 Alternative — H2 模板

```
{Lead — 公平对比框架}
## When {alternative A} is the right fit
## When a productized growth stack wins
## Side-by-side comparison   ← 表格；≥1 竞品优势
## Migration and TTV considerations
## Conclusion
## Frequently asked questions
```

---

### 2.8 UseCase — H2 模板

```
{Lead — vertical challenge}
## What breaks in {vertical} growth loops
## Signal → action patterns that work
## Capability stack for {vertical}   ← 链 /for/{arena} + capabilities
## Proof from comparable deployments   ← 链 /customers/{slug}
## Conclusion
## Frequently asked questions
```

---

### 2.9 Diagnosis — H2 模板

```
{Lead}
## Stop treating every failure as the same failure
## Bottleneck 1: …（metric + fix）
## Bottleneck 2: …
…
## Bottleneck 5: …
## The diagnostic decision tree
## Conclusion
## Frequently asked questions
```

---

### 2.10 Compliance — H2 模板

```
{Lead — 采购视角，非营销口号}
## What enterprise buyers actually ask
## Data handling and residency
## Certifications: what is live vs in flight
## Audit, SSO, and access controls
## How to run a security review   ← 链 /security
## Conclusion
## Frequently asked questions
```

**P2**：SOC 2 in flight only。

---

### 2.11 Article Brief 模板

```markdown
## Article Brief
**Working title**:
**Primary keyword**:
**Search intent**: [ ] Informational  [ ] Commercial  [ ] Transactional
**Article type**: {from §2.1}
**Platform/capability lane**: AIMA | Forge | Mutation | Déjà Vu | Capability | Demo
**Reader persona**: Founder | Growth engineer | Performance marketer | CMO | Agency | RevOps
**Publish goal**: SEO | Brand | Demo | AIMA Free
**Word count target**:
**Cluster role**: Pillar | Spoke | Standalone
**Pillar link**: /blog/programmatic-geo-vs-seo（如适用）
**Differentiation angle** (vs SERP top 3):
**Information Gain Statement** (from Phase 0):
**Canonical concepts to reference** (link only):
**Primary CTA**: /demo | /aima | /capabilities/...
**KEEP/MERGE**: KEEP | MERGE → {target slug}
**Compliance notes**: P2/P3/P4/P5 相关
```

---

### 2.12 Frontmatter Schema

```yaml
---
title: "Editorial Title — Subtitle After Em Dash (if needed)"
description: "140–160 chars, benefit + main intent keyword"
slug: "/blog/kebab-case-slug"
date: "June 15, 2026"
isoDate: "2026-06-15"
updated: "2026-06-15"
author: "Kostja"
status: draft
category: Pillar
---
```

> **2026-08-11 起废弃**：`image` / `imageAlt` / `keywords` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords 仅用于 SEO 规划）。

---

## §8 Voice 与合规

### 8.1 正向 Voice（五必满足）

1. **Command layer 叙事**：agents *operate* workflows — not "another dashboard"
2. **RCLL 或 OS 分层**：Research–Create–Launch–Learn 或 AIMA/Forge/Mutation/Déjà Vu
3. **人机边界**：spend caps, approvals, growth memory — 禁全自主
4. **具体 scenario**：≥1 段 named persona + metric（可 anonymized）
5. **B2B 克制**：不 consumer 口语；不 hype 无来源数字

### 8.2 通用 Editorial Voice 标准（五必满足）⭐v2.0.0

| 维度 | 要求 | 判断标准 |
|------|------|------|
| **Clear** | 技术概念解释清楚，不炫技 | 非专业读者能复述核心观点 |
| **Evidence-led** | 先给事实、场景、例子，再下结论 | 每个强判断都有依据或限定（"likely""emerging""in our deployment"） |
| **Practitioner-grade** | 像真正做过该行业的人写的 | 有本行业具体对象（广告平台名/marketing metric/客户案例名） |
| **Calm but opinionated** | 有判断，但不过度营销 | 至少 1 处承认非自有方案更适合的场景 |
| **Category-building** | 帮读者理解品类，不推单一产品 | 自有产品首次出现前，文章已提供独立价值 |

### 8.3 禁止风格（五类）⭐v2.0.0

| 禁止风格 | 触发词/模式 | 替代方式 |
|------|------|------|
| **AI hype** | "AI is transforming everything""revolutionary" | 写具体变化："the agent can reuse validated creative from prior runs" |
| **Vendor puffery** | "{品牌} is the only solution""best-in-class" | 写具体适用场景与边界，而非绝对化 |
| **Generic SaaS copy** | "unlock your potential""seamless""game-changing""magic" | 写可验证的具体收益或工作流变化 |
| **Fake neutrality** | 表面比较，每段都推自有产品 | 明确写出竞品/替代方案在什么场景更合适 |
| **Academic fog** | 连续抽象定义，无具体对象 | 每 300–500 词至少 1 次出现本行业具体对象 |

### 8.4 禁止措辞（Hellyeah 特定）

| 禁止 | 替代 |
|------|------|
| SOC 2 Type II certified | SOC 2 in flight |
| Déjà Vu available now | private alpha |
| Guaranteed ROAS/CAC | case study + results vary |
| Agents replace your team | agents operate with approvals |
| Just a dashboard (竞品) | fair capability comparison |
| $1,500/month AIMA | Free $0 tier |

### 8.5 空泛句检测（10 项）⭐v2.0.0

出现以下模式 → 标记并替换。超过 **3 处 → Voice 维度扣分**：

- "In today's data-driven world..."
- "In today's fast-paced digital landscape..."
- "This is why...（无前文因果）"
- "Consider the following..."
- "It is important to note that..."
- "As we all know..."
- "The reality is that..."
- "Here's the thing..."
- "But that's not all..."
- "Let's dive in..."

### 8.6 段落/句子质量标准 ⭐v2.0.0

| 检查项 | 标准 |
|------|------|
| 平均段落长度 | 60–90 words |
| 单段上限 | 130 words → ⚠️；连续两个长段 → ❌ |
| 平均句长 | 15–24 words |
| 从句层数 | 避免 3 层以上 |
| 语态 | 主动语态优先 |
| H2 下首段 | 必须说明本节要回答什么问题 |

### 8.7 Who / How / Why（Pillar / Framework 强制）

- **Who**：作者/Hellyeah 如何接触此类 growth 问题（1 段）
- **How**：研究方法或框架来源（非空泛 "we analyzed"）
- **Why**：帮读者做采购/组织决策 — 非推销 Hellyeah

### 8.8 产品名规范

- **Hellyeah**（产品/公司）
- **AIMA** · **Forge** · **Mutation** · **Déjà Vu**（平台；Déjà Vu 首次出现可注 accent）
- 域名 **hellyeahai.com** 小写
