# Lucius AI Blog — Content Graph

> 加载时机：Phase 0（选题前检查冲突）· Phase 2（日期避让）· Phase 5（Cross-Article）
> 主文件：SKILL.md §4 指针

---

## 文件表

| NN | 文件 | slug | 类型 | 日期 | 主关键词 |
|----|------|------|------|------|---------|
| 01 | 01-what-is-call-deflection.md | what-is-call-deflection | Research | 2026-07-02 | call deflection, AI customer support |
| 02 | 02-automate-customer-support-in-community.md | automate-customer-support-in-community | Product | 2026-07-03 | automate customer support in community |
| 03 | 03-what-is-claude-tag.md | what-is-claude-tag | Research | 2026-07-27 | Claude Tag, what is Claude Tag |
| 04 | 04-best-claude-tag-alternatives.md | best-claude-tag-alternatives | Comparison | 2026-07-28 | Claude Tag alternatives, best Claude Tag alternatives |
| 05 | 05-what-is-grok-bot.md | what-is-grok-bot | Research | 2026-08-14 | Grok Bot, what is Grok Bot |

**下一序号：06**

---

## 日期占用表（Phase 2 避让）

| 日期 | 已占用 slug |
|------|-----------|
| 2026-07-02 | what-is-call-deflection |
| 2026-07-03 | automate-customer-support-in-community |
| 2026-07-27 | what-is-claude-tag |
| 2026-07-28 | best-claude-tag-alternatives |
| 2026-08-14 | what-is-grok-bot |

---

## 主题簇结构

```
Research / Glossary（品类教育）
    └── 01 what-is-call-deflection ←→ 02 automate-customer-support-in-community（双向互链）

Product / Scenario（实操指南）
    └── 02 automate-customer-support-in-community → 01 what-is-call-deflection（上游概念引用）

Claude Tag / AI Teammate（2026-07）
    └── 03 what-is-claude-tag（hub） ←→ 04 best-claude-tag-alternatives（spoke）
        └── 03/04 → 01 call-deflection、02 community support automation（引用）

Grok Bot / Agentic Outsourcing（2026-08）
    └── 05 what-is-grok-bot（单篇·品类对照）
        └── 05 → 01 call-deflection、02 community support automation、03 claude-tag（backend/frontend 分工）

Comparison / Alternative（截流获客·规划中）
    ├── intercom-fin-alternative
    ├── mee6-alternative
    ├── botpress-alternative
    └── best-ai-community-bots
```

---

## Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| Call Deflection | what-is-call-deflection | 1–2 句 + link；#1 完整定义，#2 引用 |
| Community Support Automation | automate-customer-support-in-community | 1–2 句 + link；#2 完整展开，#1 FAQ 引用 |
| Claude Tag | what-is-claude-tag | #3 完整定义；#4 只 1–2 句 + link |

**规则**：每个核心概念只在一篇文章中完整定义（canonical），其他文章引用 1–2 句 + internal link。Hub 文章承载品类定义；Spoke 引用 canonical 定义，不重新展开。

---

## 关键词冲突快查

| slug | 主关键词 | 边界 |
|------|---------|------|
| what-is-call-deflection | call deflection, what is call deflection | 术语定义与原理；不覆盖实操 setup |
| automate-customer-support-in-community | automate customer support in community, community support automation | 实操 setup 三步法；引用 #1 概念但不重复定义 |
| what-is-claude-tag | Claude Tag, what is Claude Tag | Claude Tag 定义与机制；不写完整选型表 |
| best-claude-tag-alternatives | Claude Tag alternatives, best Claude Tag alternatives | 多产品选型；Claude Tag 只 1–2 句 + 回链 #3 |

---

## 集群 → 分类映射

Agent 判断新文章归属集群后，按以下映射推荐 category：

| 集群 | 默认 category | 说明 |
|------|:---:|------|
| Community AI / Research | Research | 品类定义与教育内容 |
| Community AI / Setup | Product | 实操指南与工作流 |
| Comparison / Alternative | Comparison | 横向对比与选型 |
| Product Announcement | Product | 产品发布与功能介绍 |

---

## 维护规则

每发布一篇新文章后，人类应：
1. bump 本文件 §2 的「下一文件序号」
2. 更新本文件已发布文章登记表（新增行）
3. 更新日期占用表
4. 更新 Canonical Concept Registry（如有新的 canonical 概念）
5. bump `SKILL.md` frontmatter `version` patch

---

*content-graph · v2.0.0 · 2026-07-06*
