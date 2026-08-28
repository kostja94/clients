# Datus — FAQ 规范

> **归档说明**：本文档已于 2026-08-28 移入 `_archive/`，不再维护。活跃文档见 [_archive/README.md](./README.md)。

> **本文档职责**：全站 FAQ 组件架构、页内 FAQ 内容规则、FAQPage schema；供实现者与 Agent 生成/审核 FAQ。  
> **引用**：[datus-site-structure.md](../datus-site-structure.md) | [datus-features.md](../datus-features.md) | [blog/README.md](../blog/README.md)  
> **外部规则**：FAQ Page Skill（内容长度、schema parity、去重）

**最近更新**：2026-06-21

---

## 一、架构

### 1.1 一个组件，多页内容

| 层 | 职责 |
|----|------|
| **`<FAQ />` UI 组件** | 全站复用：accordion / 手风琴、语义 HTML（`h3` 问题 + 答案段） |
| **页级内容** | 每页注入 **独立** Q&A 列表；不与它页重复同一问法 |

**内容注入方式**（择一，实现统一即可）：

| 来源 | 适用 |
|------|------|
| CMS 字段 `faq: [{ question, answer }]` | 营销页（products、pricing、integrations） |
| Blog frontmatter `faq:` 数组 | `/blog/{slug}/` Markdown |
| 静态 JSON `content/faq/{page-id}.json` | SSG 构建 |
| 页面 MDX 内 `## Frequently asked questions` | 与现有 Blog 稿一致；构建时解析为组件 props + schema |

**原则**：组件负责样式、折叠、a11y、JSON-LD 渲染；**内容不在组件内硬编码**。

### 1.2 页内 FAQ 规格

| 维度 | 要求 |
|------|------|
| **题量** | **3–8**（最佳 5–6） |
| **位置** | 主内容之后、Footer 之前 |
| **用途** | 转化异议、页专属长尾、PAA 占位 |
| **Schema** | 该页一个 `FAQPage` |

**决策**：

- 问题 **只** 与当前 URL 主题相关 → 页内 FAQ。
- 题量 > 8 且都属本页 → 保留页内 5–6 条最关键的，其余扩展为正文 H2 小节。

---

## 二、内容规则（对齐 FAQ Skill）

### 2.1 篇幅与结构

| 元素 | 要求 |
|------|------|
| **答案** | **40–80 英文词**；Featured Snippet 目标可压到 40–60 |
| **首句** | **Answer-first**：第一句即直接回答 |
| **句数** | 2–4 句；可独立被 AI 引用 |
| **问题** | 真实用户口吻（how / what / why / can I）；H2/H3 作问题标题 |
| **Blog** | 区块标题：`## Frequently asked questions`（无编号，见 [blog/README.md](../blog/README.md)） |

### 2.2 质量与 SEO

- **Schema parity**：`FAQPage` 中 `Question`/`Answer` **必须与可见 DOM 逐字一致**（允许 HTML 标签差异仅限 schema 允许的 `<p><ul><li><strong><a>`）。
- **无跨页重复**：同一问题 **只在一个 canonical URL** 上作为 FAQ；选最权威页（定价问价 → `/pricing/`；术语定义 → 术语文 `/blog/{slug}/`）。
- **页内相关**：FAQ 只答 **本页** 意图；不在 CLI 页写 Enterprise SLA 全套。
- **禁止**：编造无搜索/无支持依据的「营销问」；答案从正文整段复制（相似度宜 <30%）；hidden schema。
- **Accordion**：内容须在首屏 HTML/DOM 中（非点击后 AJAX）；Google 可索引折叠内容。
- **更新**：季度从 GSC PAA、支持工单、销售异议补充新问。

### 2.3 内容来源（Datus）

| 来源 | 用途 |
|------|------|
| 支持 / GitHub Issues / Discussions | 安装、连接、错误类 |
| 销售 POC 异议 | Enterprise、安全、部署 |
| [datus-features.md](../datus-features.md) | 产品能力边界 |
| [datus-competitors.md](../datus-competitors.md) | 对比类 FAQ（放在对比文，非泛化 FAQ） |
| Glossary / PAA | 术语文、DE Agent 文的长尾问 |
| 定价表 | `/pricing/` 专属 |

---

## 三、FAQPage JSON-LD 模板

每页 **至多一个** `FAQPage`。`mainEntity` 顺序与页面 FAQ 展示顺序一致。

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://datus.ai/PAGE-PATH/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION TEXT EXACTLY AS ON PAGE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<p>Answer-first paragraph, 40-80 words, matches visible content.</p>"
      }
    }
  ]
}
```

**校验**：Rich Results Test、Schema.org Validator；`mainEntity.length >= 2`（页内 FAQ 至少 2 题，推荐 ≥3）。

---

## 四、页面类型 → FAQ 主题 → 建议题量

| 页面类型 | 路径示例 | FAQ 主题（只选与本页相关的） | 建议题量 |
|----------|----------|------------------------------|:--------:|
| 首页 | `/` | 可选 3–4：品类是什么、是否开源、如何开始 | 0–4 |
| 产品 | `/products/cli/` | 安装、模型、Subagent、vs Studio、开源范围 | 5–6 |
| 产品 | `/products/studio/` | 云端、注册、与 CLI 关系、免费层 | 5–6 |
| 产品 | `/products/enterprise/` | SSO、审计、SLA、部署、POC | 5–7 |
| 定价 | `/pricing/` | 免费层、Enterprise 询价、开源许可、BYOK、取消 | 6–8 |
| 集成 | `/integrations/` | 支持的数据库、MCP、Semantic 工具、适配器贡献 | 5–6 |
| Glossary 索引 | `/glossary/` | 术语表如何用、与 Blog 关系、贡献术语 | 3–5 |
| Glossary 术语文 | `/blog/what-is-*` | 定义辨析、vs 相近概念、何时需要、与 Datus 关系 | 4–6 |
| DE Agent 文 | `/blog/contextual-data-engineering` | 品类、Context Engine、实施、限制 | 4–6 |
| 对比 / 列表文 | `/blog/best-data-engineering-agents` | 选型标准、开源 vs 商业、评估维度 | 5–6 |
| Hub | `/blog/data-engineering-agent/` | 簇导航、从何读起、与 docs 区别 | 3–5 |

---

## 五、完整示例（英文 Q&A，40–80 词）

以下为例题 **内容**；上线时须与产品事实同步。

### 5.1 `/products/cli/`

**Q: What do I need to install Datus CLI?**  
A: You need Python 3.12 or newer and pip. Install with `pip install datus-agent`, then run `datus-agent` to start the interactive CLI. Configure your LLM API key and database connection in `agent.yml`. Datus CLI works on macOS and Linux today; Windows is supported via Python but not officially certified. Full setup steps are in docs.datus.ai Quickstart.

**Q: Does Datus CLI work with my existing warehouse?**  
A: Yes. Datus ships native adapters for Snowflake, PostgreSQL, MySQL, ClickZetta, and others, plus MCP-based connectors for DuckDB, StarRocks, Hive, Spark, ClickHouse, and Trino. You point the CLI at your catalog or JDBC connection—no need to migrate data. Custom DB adapters can be added via the plugin architecture described in the GitHub repo.

**Q: How is Datus CLI different from Datus Studio?**  
A: Datus CLI is the full open-source agent for engineers: context building, Subagent creation, MCP tools, and local control. Datus Studio is the hosted web experience for faster trial and chat-style exploration. Both share the same Context Engine concepts; many teams prototype in Studio and run production workflows in CLI or Enterprise.

**Q: Can I use my own LLM API keys with the CLI?**  
A: Yes. Datus CLI is bring-your-own-key. You configure OpenAI, Claude, Qwen, DeepSeek, Kimi, Gemini, or others in `agent.yml`, including per-Subagent model overrides. Usage and cost stay on your provider account. Cloud Personal may offer managed keys; the open-source CLI never requires a Datus-hosted model.

**Q: What can I build with Subagents in the CLI?**  
A: A Subagent is a scoped chatbot backed by roughly ten tables, twenty metrics, and thirty reference SQL patterns for one business domain. You create them with `.subagent add`, refine context through feedback loops, and export mature Subagents as HTTP APIs or MCP servers for other agents to call.

### 5.2 `/pricing/`

**Q: Is Datus really free to use?**  
A: The core Datus agent is free and open source under Apache 2.0, including CLI, Context Engine, Subagents, and multi-model support. Cloud Personal is also free for hosted exploration. You still pay your own LLM and warehouse costs. Enterprise adds team governance, SSO, audit logs, and SLA-backed support through a custom quote.

**Q: What is included in Cloud Personal versus Enterprise?**  
A: Cloud Personal lets you try Datus in the browser without installing the CLI—ideal for demos and light exploration. Enterprise adds shared context stores, access control, audit trails, dedicated support, and deployment options for regulated teams. LinkedIn, Expedia, and Coinbase-class requirements map to Enterprise, not the free tiers.

**Q: How do I get Enterprise pricing?**  
A: Enterprise pricing is not listed publicly. Contact the Datus team through the site form or sales email with your team size, warehouses, and compliance needs. Typical buyers need SSO, audit logs, shared context across engineers, and an SLA. POC engagements often start on open source before upgrading.

**Q: Do I need to pay for LLM usage separately?**  
A: Yes, for CLI and most self-hosted setups. Datus does not bundle model tokens; you connect your OpenAI, Anthropic, or other provider keys. That keeps inference costs transparent and lets you choose models per Subagent. Cloud Personal may include limited managed usage—check the current pricing page for quotas.

**Q: Can I cancel or downgrade at any time?**  
A: Open-source CLI has no subscription—you simply stop using it. Cloud Personal can be abandoned without a contract. Enterprise terms depend on your agreement; standard POCs convert to annual contracts with negotiated exit clauses. There is no lock-in on your data context exports from the CLI.

**Q: Does the open-source license allow commercial use?**  
A: Yes. Apache 2.0 permits commercial use, modification, and distribution with attribution. You can run Datus internally or embed derived Subagent APIs in your products, subject to Apache terms. Enterprise is optional unless you need vendor support, SSO, or a managed context store.

### 5.3 `/blog/what-is-semantic-layer/`（Glossary）

**Q: What is a semantic layer in one sentence?**  
A: A semantic layer is a governed mapping from physical database tables to stable business concepts—metrics, dimensions, and entities—so people and software query data using business language instead of raw schema names and join paths.

**Q: What is the difference between a semantic layer and a data catalog?**  
A: A data catalog documents what data exists: tables, columns, owners, tags, and lineage for discovery. A semantic layer defines how to compute and slice business metrics correctly. Catalogs help you find data; semantic layers help you use it consistently in BI, APIs, and agents.

**Q: Do I need a semantic layer before deploying AI text-to-SQL?**  
A: You need governed business terms somewhere, not necessarily a standalone product. Text-to-SQL fails when agents see raw schema only. A semantic layer—or an equivalent evolvable context system—supplies metric definitions, join rules, and validated SQL patterns so generated queries match how the business actually counts revenue or churn.

**Q: How does a semantic layer relate to tools like MetricFlow or Cube?**  
A: MetricFlow and Cube are implementations of semantic or metric layers with YAML models and APIs. They excel at headless metrics and BI consumption. Datus can ingest those definitions and extend them with feedback-driven context, but the semantic layer concept is broader than any single vendor.

### 5.4 `/blog/contextual-data-engineering/`（DE Agent）

**Q: What is contextual data engineering?**  
A: Contextual data engineering is the practice of building and continuously evolving data context—schemas, metrics, reference SQL, and feedback—not just running one-off pipelines. Datus coined the term to describe agents that treat context as a first-class, versioned asset rather than disposable prompt stuffing.

**Q: How is contextual data engineering different from traditional data engineering?**  
A: Traditional work optimizes pipelines and tables for each ticket. Contextual data engineering optimizes reusable context so the next query, agent, or analyst inherits prior validation. Success is measured by context coverage and reuse, not only job runtime. Agents automate exploration; engineers curate what gets promoted into shared context.

**Q: Does Datus replace dbt or my orchestrator?**  
A: No. Datus complements orchestration and transformation tools by managing the semantic and operational context agents need at query time. You still model in dbt or Spark; Datus ingests metadata and SQL history, then exposes Subagents and APIs. It replaces the ad hoc spreadsheet of “which table is the real revenue table,” not your scheduler.

**Q: How long until contextual data engineering shows ROI?**  
A: Teams often see faster ad hoc answers within the first week after connecting a warehouse and bootstrapping reference SQL. Durable ROI—higher self-serve rates and fewer repeated Slack questions—typically appears after one or two Subagents cover a core domain with feedback loops. Yunqi Lakehouse reported self-serve rising from 15% to 60% after integration.

### 5.5 `/integrations/`

**Q: Which databases does Datus support out of the box?**  
A: Native adapters include ClickZetta, Snowflake, PostgreSQL, and MySQL. MCP-based connectors cover DuckDB, StarRocks, Hive, Spark, ClickHouse, and Trino as of v0.2.6. The adapter layer is plugin-based, so new warehouses can be added without forking core code. See the GitHub repo for the current adapter matrix.

**Q: Can Datus connect to dbt, MetricFlow, or Cube semantic models?**  
A: Yes. Datus ingests MetricFlow-compatible YAML and can reinforce semantic definitions from existing models rather than forcing re-modeling. Cube and other semantic layers can feed the Context Engine while Datus adds scoped Subagents, reference SQL, and feedback loops on top for agent consumption.

**Q: How does MCP fit into Datus integrations?**  
A: Datus acts as both MCP client and server. As a client, it calls external MCP tools—for example Airflow or quality checkers—via `.mcp add`. As a server, it exposes database and context search tools to Claude Desktop, Claude Code, or other agents. MCP is an extension layer; core SQL and context paths use native tools.

**Q: Can I contribute a custom database adapter?**  
A: Yes. v0.2.3 introduced a plugin architecture for DB adapters. Contributors implement the adapter interface, publish via GitHub PR, and document connection parameters. Enterprise customers sometimes maintain private adapters; the open-source repo documents patterns for JDBC-like and warehouse-specific auth.

**Q: Does Datus integrate with BI tools like Looker or Tableau?**  
A: Datus does not replace BI dashboards. It integrates at the semantics and query layer: ingesting models, capturing validated SQL from BI usage, and powering chat or API interfaces that respect the same metrics. Dashboard Copilot can bootstrap Subagents from BI metadata where supported.

---

## 六、Agent 规则

### 6.1 按页面类型生成

```
INPUT: page_type, page_url, page_topic, existing_faq_registry (optional)

1. Select row from §四 table → themes + target count N (3-8)
2. Source questions from:
   - PAA / AnswerThePublic for page primary keyword
   - datus-features / positioning for product facts
   - NOT from other pages' FAQ verbatim (check registry)
3. Write each answer: 40-80 English words, answer-first, 2-4 sentences
4. For Blog: append ## Frequently asked questions with ### per question
5. Emit FAQPage JSON-LD from same strings
6. If count > 8: keep top 5-6 by conversion/intent, move remainder to in-page H2 sections
```

### 6.2 验证清单

- [ ] 题量在页型建议范围内
- [ ] 每答 40–80 英文词（计词工具验收）
- [ ] 首句直接答题
- [ ] 无与其它 URL 重复的 Q（registry 或站点搜索）
- [ ] FAQ 主题与 **当前 URL** 一致
- [ ] 可见 HTML 与 `FAQPage` 问答文本一致
- [ ] Blog FAQ 非正文复制（<30% 相似）
- [ ] 至少 2 题（推荐 ≥3）
- [ ] 无「Why is Datus the best…」类纯推销问

### 6.3 禁止模式

| 禁止 | 原因 |
|------|------|
| 同一 Q 出现在 `/pricing/` 与 `/products/cli/` | 去重；保留更权威 URL |
| Schema 多于或少于可见 FAQ | parity 违规 |
| 答案 <40 或 >80 词（无拆分理由） | Skill 长度要求 |
| Glossary 术语 FAQ 写「如何安装 CLI」 | 离题 |
|  invented questions 无 PAA/支持依据 | 低质量 / 无搜索量 |
| 首页堆 15 条 FAQ | 超出建议题量；应精简至 0–4 |
| 用 FAQPage 标记 HowTo 步骤 | 应使用 HowTo schema |

### 6.4 机器可读摘要

```yaml
faq_architecture:
  component: shared FAQ UI
  content: per-page inject (CMS | frontmatter | JSON | MD section)
  in_page_count: 3-8
  answer_words: 40-80
  schema: FAQPage
  schema_parity: required
  duplicate_questions: forbidden across URLs
  blog_section_heading: "## Frequently asked questions"
  blog_question_heading: "### {question}"
  language:
    doc: zh
    on_site_qa: en
```

---

## 七、与 Blog 工作流衔接

- Glossary Skill 要求 FAQ ≥3、覆盖 PAA；本规范 **加严** 40–80 词与去重，与之兼容。
- 新建 Blog 稿：在 Conclusion 之后写 FAQ；构建管道解析为 `<FAQ items={...} />` + JSON-LD。
- 内链：FAQ 答案内链遵循 [internal-external-links-checklist.md](../blog/internal-external-links-checklist.md)（术语 → `/blog/{slug}`，CTA → GitHub / docs）。

---

*FAQ 规范 · Datus · https://datus.ai/*
