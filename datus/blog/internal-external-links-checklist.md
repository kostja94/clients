# Internal & External Links 规范（Datus Blog）

> **依据**：Nori / Dynal blog 链接规范同一思路；站内 URL 权威以 [datus-site-structure.md](../datus-site-structure.md) 为准。
> **站点**：生产以 **datus.ai** 为准；正文为 **英文**，本规范为 **中文**，供写作与校对使用。
> **更新**：2026-07-17——移除 Related 列（已不使用）；补充全部 31 篇文章实际链接计数；移除 frontmatter `keywords`/`related` 相关引用。

---

## 内链范围约束

**Blog 文章仅链向两类站内目标：**
1. **Blog 互链**（`/blog/{slug}`）——系列稿、相邻主题
2. **Glossary**（`/glossary`）——术语定义

**不链向**：产品页（`/agent`、`/features/*`）、场景页（`/use-cases/*`）、对比页（`/vs/*`）、案例页（`/case-studies/*`）。原因：这些页面尚未上线——blog 内容不应依赖未上线的 URL。产品页上线后可补链。

---

## 链接分层（Datus）

| 类型 | URL 模式 | 用途 | 当前状态 |
|------|----------|------|:---:|
| **Blog 互链** | `/blog/{slug}` | 系列稿、相邻主题；锚文本用主题词 | ✅ 可用 |
| **Glossary** | `/glossary` | 术语定义——唯一非 blog 站内链接目标 | ✅ 可用 |
| **外部** | GitHub、Docs、Studio | 开源与试用转化 | ✅ 可用 |

*以下类型暂不链入 blog——页面未上线但 URL 已规划，上线后补链：*

| 类型 | URL 模式 | 用途 |
|------|----------|------|
| 品类 / 产品页 | `/agent`、`/features/*` | 产品叙事、功能说明 |
| 场景页 | `/use-cases/*` | Persona 补充 |
| 对比页 | `/vs/*`、`/alternatives/*` | 竞品拦截 |
| 案例 | `/case-studies/*` | ROI 证明 |

---

## Internal Links 正文分布

| 区域 | Blog 互链 | Glossary | 外链 |
|------|-----------|:---:|------|
| **开篇（第一个 `##` 之前）** | ≤ 1–2 条 | ≤ 1 条（术语首次出现时） | — |
| **正文各 `##` 小节** | 语义相关，每节通常 ≤ 2 条 | 术语首次出现，全篇 ≤ 3 条 | 竞品文档 ≤ 5 条 |
| **Conclusion / FAQ** | 收束链 | ≤ 1 条 | CTA → Studio / GitHub |

**锚文本**：描述性短语；避免 "click here"、"learn more"。

**Glossary 内链原则**：
- 每个术语在正文中**首次出现**时链向 `/glossary`
- 同一术语在单篇文章内只链一次（避免重复）
- 全篇 glossary 内链总数 ≤ 3 条（防止过度优化）

---

## External Links 规范

| 要求 | 说明 |
|------|------|
| **总量** | 每篇 2–5 条 |
| **用途** | 竞品官方文档、平台产品页、行业报告 |
| **格式** | `<a href="URL" rel="nofollow noopener">锚文本</a>` |
| **E-E-A-T** | Google Cloud docs、Adobe、GitHub 社区 repo 等权威来源 |

---

## 文章链接状态

**计数规则**：内链 Blog = 正文 `/blog/{slug}` 互链数；内链 Glossary = 正文 `/glossary` 引用数；外链 = 正文 `<a href="..." rel="nofollow noopener">` 数。

**状态阈值**：✅ blog ≥2 且 ext ≥2；⚠️ 不满足双条件但非全零；❌ blog =0 或 ext =0；— 文稿缺失。

| # | 文章 | 内链 Blog | 内链 Glossary | 外链 | 状态 |
|---|------|:---:|:---:|:---:|------|
| 01 | What Is a Data Engineering Agent | 2 | 0 | 5 | ✅ |
| 02 | What Is a Semantic Layer | 2 | 0 | 4 | ✅ |
| 03 | Contextual Data Engineering | 2 | 3 | 5 | ✅ |
| 04 | Best Data Engineering Agents 2026 | 3 | 0 | 1 | ⚠️ ext=1 |
| 05 | Open Source Data Engineering Agents | 3 | 2 | 3 | ✅ |
| 06 | Build Your First DE Agent + CLI Workflow | 8 | 2 | 3 | ✅ |
| 07 | DE Agent vs. Claude Code | 4 | 0 | 2 | ❌ 文稿缺失 |
| 08 | DE Agent vs. SQL Copilot | 4 | 1 | 2 | ✅ |
| 09 | One-Person Data Team | 4 | 1 | 2 | ✅ |
| 10 | Context Engine Accuracy | 5 | 2 | 3 | ✅ |
| 11 | MCP and Data Engineering | 4 | 1 | 2 | ✅ |
| 12 | —（空号，保留） | — | — | — | — |
| 13 | Enterprise DE Agent Needs | 5 | 0 | 1 | ⚠️ ext=1 |
| 14 | Subagents Deep Dive | 4 | 1 | 2 | ✅ |
| 15 | What Is Text-to-SQL | 6 | 0 | 3 | ✅ |
| 16 | What Is Schema Linking | 4 | 0 | 2 | ✅ |
| 17 | RAG for Data Engineering | 6 | 0 | 1 | ⚠️ ext=1 |
| 18 | What Is a Data Catalog | 6 | 0 | 3 | ✅ |
| 19 | What Is Data Mesh | 2 | 0 | 1 | ⚠️ ext=1 |
| 20 | What Is a Metric Layer | 1 | 0 | 6 | ⚠️ blog=1 |
| 21 | What Is a Semantic Model | 3 | 0 | 0 | ❌ ext=0 |
| 22 | Semantic Layer vs. Ontology | 2 | 0 | 0 | ❌ ext=0 |
| 23 | What Is a Data Agent | 1 | 0 | 0 | ❌ ext=0 |
| 24 | Open Semantic Interchange / OSI | 1 | 0 | 2 | ⚠️ blog=1 |
| 25 | dbt Semantic Layer & MetricFlow | 1 | 0 | 0 | ❌ ext=0 |
| 26 | Cube.dev Agentic Analytics | 3 | 0 | 0 | ❌ ext=0 |
| 27 | GoodData.AI AI-Native Analytics | 1 | 0 | 0 | ❌ ext=0 |
| 28 | AI-Native Data Platforms | 3 | 0 | 0 | ❌ ext=0 |
| 29 | Platform-Native DE Agents Compared | 0 | 0 | 0 | ❌ blog=0 ext=0 |
| 30 | What Is a Lakehouse | 8 | 0 | 3 | ✅ |
| 31 | Semantic Layer Tools List & OSI Support | 8 | 0 | 2 | ✅ |

**统计**：✅ 达标 19 篇 · ⚠️ 警告 4 篇 · ❌ 不达标 7 篇 · 空号/缺失 1 篇

**维护说明**：
- 共 **31** 篇（#07 文稿缺失，#12 保留空号）；其中 Glossary 类 **11** 篇 + DE Agent 类 **17** 篇 + Semantic Layer（ToolsList）**1** 篇；#31 category 已从 Glossary 改为 `Semantic Layer`
- **禁止**链向 slug `data-engineering-agent-vs-claude-code`，直至 `07-data-engineering-agent-vs-claude-code.md` 发布
- 每发布一篇新稿或修改链接，需更新上表
- 链接策略：正文内链（blog 互链 + glossary）+ 外链替代原 frontmatter `related` 和 `keywords` 字段
