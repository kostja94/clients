# Features 簇

产品能力与版本更新的 blog 分簇。公开 URL 仍是 `/blog/{slug}`，文件夹不进路径。

**Docs 源**：[`docs.datus.ai`](https://docs.datus.ai/)（当前对照 [0.3 Knowledge Base](https://docs.datus.ai/0.3/knowledge_base/introduction/)）· 本地摘录 [`../docs-crawl/`](../docs-crawl/)

---

## 为什么单独成簇

现有四簇（Data Agent / DEA / Semantic Layer / OSI）做**行业词与品类叙事**。Features 做 **Datus 自己的能力页**：Knowledge Base、Subagent 工具、OSI adapter、Skills、Workflow。

| 不要放进 Features | 放哪 |
|-------------------|------|
| `what is semantic layer / model / metric` | Semantic Layer / Glossary |
| `what is a data engineering agent` | DEA Hub |
| 准确率论证、contextual 操作模型 | 已有 `#03` `#10`（DEA Research） |
| 厂商标本（Genie / Timbr） | Data Agent / Semantic Layer |
| 发布说明 changelog | 线上已有 `datus-0-2-6-release-*`，不进本簇 |

**和 `#10` Context Engine 的分工**：`#10` 回答「为什么 context 决定准确率」。本簇 Hub 回答「Datus Knowledge 里实际存了什么、六个部件怎么协作」。互链，不重写。

---

## Frontmatter

```yaml
---
title: "Introducing Datus Knowledge: ..."
description: "120–160 chars"
slug: "introducing-datus-knowledge"  # 功能介绍文：introducing + 产品名；不要用泛词 what-is-knowledge-base
date: 2026-08-17
author: "Kostja"
category: "Features"
secondaryCategory: "Product"
---
```

- `category: Features`（主题簇）
- `secondaryCategory: Product`（体裁；与 `#06` `#32` 相同）
- 正文英文；docs 外链可用 follow（第一方）

**内链配额（Product）**：unique 3–4。Lede ≤1（可链 DEA Hub 或 contextual）；Conclusion 2–3 条 next-read。不要把六个部件各链一篇 glossary。

---

## 簇结构

```
Features
  46 Hub  Introducing Datus Knowledge  ← Datus Agent 能力入口（已发）
  47      Datus OSI Semantic Adapter   ← 已发
  48      Introducing Datus Subagents  ← 已发
          50 /init + /build-kb         （计划）
          51 Dashboard Copilot         （计划）
          —  Skills / Workflow         （更后）
```

**Dosi 产品叙事**在 [`../dosi/`](../dosi/) 簇（#49–#54）。簇规则见 [blog/README.md](../README.md#dosi6-篇--hub-49)。

已发布、**不要搬目录**的近邻：`#14` 领域交付、`#11` MCP、`#06` 教程、`#10` Context Engine。`#48` 链 `#14`，不重写 lifecycle。

---

## 选题漏斗（从 docs 来）

只发「改变 agent 怎么工作」的能力，不发配置手册。

| 优先级 | 选题 | slug 意向 | docs | 搜索意图 | 注意 |
|:---:|------|-----------|------|----------|------|
| **P0** | Knowledge Base | `introducing-datus-knowledge` | [KB intro 0.3](https://docs.datus.ai/0.3/knowledge_base/introduction/) | introducing Datus Knowledge / agent knowledge base for SQL | 首篇 Hub，成稿 [`46-introducing-datus-knowledge.md`](./46-introducing-datus-knowledge.md) |
| **P0** | OSI Semantic Adapter | `datus-osi-semantic-adapter` | [OSI adapter 0.3](https://docs.datus.ai/0.3/adapters/osi_semantic_adapter/) | OSI + Datus 产品连接 | 成稿 [`47-datus-osi-semantic-adapter.md`](./47-datus-osi-semantic-adapter.md)；链 OSI Hub，不重写定义 |
| **P0** | Task Subagents | `introducing-datus-subagents` | [Subagent intro](https://docs.datus.ai/0.3/subagent/introduction/) · [AskMetrics](https://docs.datus.ai/0.3/subagent/ask_metrics/) | Datus subagents / ask metrics | 成稿 [`48-introducing-datus-subagents.md`](./48-introducing-datus-subagents.md)；AskMetrics 做主 walkthrough；**不**重写 `#14` 领域交付 |
| P1 | `/init` + `/build-kb` | `datus-init-build-knowledge-base` | Skills → Init / Build KB | 如何灌知识 | 操作向，链 Hub；与 Skills marketplace **拆开** |
| P1 | Dashboard Copilot | `datus-dashboard-copilot` | Getting Started | BI 侧能力 | 消费者表面，链 Data Agent |
| P2 | Skills | `datus-skills` | Integration → Skills | agentskills / marketplace | 扩展层，勿与 `/init` 合成一篇 |
| P2 | Workflow | `datus-agent-workflow` | Workflow | agent 编排 | 别写成 API 文档 |
| P2 | Reference Template | `datus-reference-sql-templates` | KB → Reference Template | 参数化 SQL | 可做 Hub 的 spoke，勿抢 Hub |
| — | 领域 Subagent 交付 | — | — | — | **已有 `#14`**，不重开 |
| — | AskMetrics 独立篇 | — | — | — | **并入 `#48`**，不单开 |
| — | CLI 命令清单 | — | CLI | — | 归 docs，不上 blog |

版本小步（storage backend、新 adapter）优先 **更新 Hub** 的 `updated` 字段，而不是每发一版一篇。

---

## 写作规则

1. **教育句 → 产品句**。先说失败模式（schema dump、指标漂移、过期 SQL），再落到 KB 部件。
2. **禁止把 docs 六段复制成 H2**。部件用一张主表 + 2–3 个失败故事，不要六个配置小节。
3. **术语只链不定义**。semantic model / metric layer / RAG / catalog / schema linking 各最多 1 条 canonical。
4. **CLI 最多一个最小例子**（如 `bootstrap-kb`）。完整 flag 留给 docs。
5. **版本**：正文写 `as of August 2026`，对照 docs **0.3**。与 skill 里残留的 v0.2.6 冲突时，以 docs 0.3 为准。
6. **不要进 glossary**。Knowledge Base / Context Engine 是产品实现，策略词表已排除。

---

## 成稿后

1. Hub：[`46-introducing-datus-knowledge.md`](./46-introducing-datus-knowledge.md)
2. Spoke：[`47-datus-osi-semantic-adapter.md`](./47-datus-osi-semantic-adapter.md) · [`48-introducing-datus-subagents.md`](./48-introducing-datus-subagents.md)
3. 更新 [`../README.md`](../README.md) 文章表
4. 更新 [`../internal-external-links-checklist.md`](../internal-external-links-checklist.md) 互链
5. 入链：`#10` → Hub；`#24` → `#47`；`#14` → `#48`；Hub Conclusion → `#47` `#48`
