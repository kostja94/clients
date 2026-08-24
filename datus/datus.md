# Datus

**最近更新**：2026-08-04（文档导航增加 i18n 规范）

---

## 文档导航

| 文档 | 职责 | 引用 |
|------|------|------|
| [datus.md](./datus.md)（本文） | 产品概览、ICP、文档索引 | — |
| [datus-positioning.md](./datus-positioning.md) | One Story、Messaging Framework、竞争叙事、产品形态定位 | [datus.md](./datus.md)、[datus-competitors.md](./datus-competitors.md) |
| [datus-site-structure.md](./datus-site-structure.md) | 站点结构：URL 层级、IA、技术栈 | [datus.md](./datus.md) |
| [datus-i18n-spec.md](./datus-i18n-spec.md) | 主站 `/zh` i18n：范围规则、路由、术语、机翻→精调、SEO | [datus-site-structure.md](./datus-site-structure.md)、[datus-positioning.md](./datus-positioning.md) |
| [datus-growth-strategy.md](./datus-growth-strategy.md) | 增长策略：渠道、实验、内容计划 | [datus-keywords.md](./datus-keywords.md)、[datus-site-structure.md](./datus-site-structure.md) |
| [datus-features.md](./datus-features.md) | 功能页：CLI、Subagent、Context Engine、多模型 | [datus-use-cases.md](./datus-use-cases.md) |
| [datus-use-cases.md](./datus-use-cases.md) | 应用场景：Persona、Scenario、用户旅程 | [datus-features.md](./datus-features.md) |
| [datus-competitors.md](./datus-competitors.md) | 竞品分析、差异化 | [datus-features.md](./datus-features.md) |
| [datus-keywords.md](./datus-keywords.md) | 关键词映射、目标页、待办 | [datus-features.md](./datus-features.md)、[datus-use-cases.md](./datus-use-cases.md) |
| [datus-glossary.md](./datus-glossary.md) | Glossary 策略设计：关键词簇、术语选择逻辑、内容网络位置（7 类 42 词） | [datus-keywords.md](./datus-keywords.md)、[datus-positioning.md](./datus-positioning.md)、[datus-competitors.md](./datus-competitors.md) |
| [datus-breadcrumb-spec.md](./datus-breadcrumb-spec.md) | 面包屑 UI + BreadcrumbList JSON-LD（除首页外全站） | [datus-site-structure.md](./datus-site-structure.md) |
| [datus-faq-spec.md](./datus-faq-spec.md) | 全站 FAQ 组件 + 页内 FAQ 内容规则与示例 | [datus-site-structure.md](./datus-site-structure.md)、[blog/README.md](./blog/README.md) |
| [datus-dosi.md](./datus-dosi.md) | **Dosi** 新产品调研、关键词与候选文章（调研阶段） | [datus-keywords.md](./datus-keywords.md)、[blog/24-open-semantic-interchange-osi-2026.md](./blog/24-open-semantic-interchange-osi-2026.md) |
| [blog/](./blog/) | Blog 文章目录（Markdown + YAML frontmatter） | [datus-growth-strategy.md](./datus-growth-strategy.md) |

*产品入口*：Web [datus.ai](https://datus.ai/) | GitHub [Datus-ai/Datus-agent](https://github.com/Datus-ai/Datus-agent) | Docs [docs.datus.ai](https://docs.datus.ai)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2B SaaS · **开源 AI 数据工程 Agent**（Open Source Data Engineering Agent） |
| 网站 | https://datus.ai/ |
| 当前阶段 | 早期增长（v0.2.6，~1.2K GitHub stars，LinkedIn/Expedia/Coinbase POC 中） |
| 核心产品 | **Datus-agent**：开源数据工程 Agent——为数据系统构建可演进的上下文（evolvable context）；CLI + Chat + API + MCP Server 四形态 |
| 公司 | 创始人赵恒（Dshadowzh），前阿里分布式数据库工程师 / StarRocks TSC 成员；2025 年创立 |
| 产品形态 | Open Source（GitHub）+ Cloud Personal（免费）+ Enterprise（企业版） |
| 关键差异化 | **Context Engineering 为核心**——将数据上下文作为一等公民管理、持续演进，而非一次性建模；从一人数据团队到企业 Agent 团队的开源底座 |
| 使命/愿景 | The open-source data engineering agent that builds evolvable context for your data systems |
| 目标用户 | 数据工程师（个人提效 & 团队协作）→ 数据团队 Leader / CDO（规模化 Agent 交付） |
| 目标市场 | 全球（英文为主）+ 中文（微信公众号 / 国内社区），当前 LinkedIn/Expedia/Coinbase POC 中 |
| 商业模式 | 开源核心（Apache 2.0）+ Cloud Personal（免费引流）+ Enterprise（SLA / SSO / 审计日志 / 专属支持） |
| 数据规模 | ~1,236 GitHub stars / 148 forks / 185 PRs（30 天内）；云器 Lakehouse 案例：数据分析自助率 15%→60%，查询时间 30min→3min |

---

## 1. 产品摘要

Datus 是一个开源 AI 原生的数据工程 Agent，核心理念是将数据工作从一次性任务转变为可演进的数据上下文（evolvable context）。它的产品形态覆盖 CLI、Web Chat、API 与 MCP Server，让数据工程师构建和持续强化数据上下文，并把它变成 Agent、Workflow 和团队协作的基础。

其核心技术架构围绕 **Context Engine** 展开，从两个维度组织信息：物理维度（Catalog → Database → Schema → Table，贴附 Semantic Model）和语义维度（业务域 → 一级主题 → 二级主题，承载指标、Reference SQL 与外部知识）。通过 `/gen_semantic_model`、`/gen_metrics`、`/gen_sql_summary` 等命令自动生成上下文，配合 `datus-agent bootstrap-kb` 从历史 SQL 文件和 Success Story 批量冷启动知识库。

Subagent 是交付单元——它将 Scoped Context（约 10 张表、20 个指标、30 条 Reference SQL）封装为特定场景的 Chatbot，通过反馈闭环（Ad-hoc 探索 → 生成指标与 SQL → 配置 Subagent → 用户反馈回流 → 优化上下文）持续提升准确率与覆盖率，直至可以导出为 API 供其他 Agent 或微服务调用。

创始人赵恒于 2025 年裸辞创业，2025 年 10 月正式开源（Apache 2.0），源于对 DBT 的反思和对「数据工程 Agent」赛道的判断。目前 LinkedIn、Expedia、Coinbase 正在进行 POC，云器 Lakehouse 已成功集成。

*完整功能线见 [datus-features.md](./datus-features.md)。*

---

## 2. 定位要点

| 维度 | 说明 |
|------|------|
| **品类标签** | *data engineering agent*（首选）、*contextual data engineering*（自创概念）、*NL2SQL agent*（市场认知）、*open-source evolvable context system*（差异化标签） |
| **One Story** | *Datus is the open-source data engineering agent that builds evolvable context for your data systems. From one-man data teams to enterprise agent teams, Datus turns data work into reliable, reusable agent systems.* |
| **差异锚点** | **Context Engineering 范式**——将上下文作为一等公民管理、持续进化（vs 竞品一次性建模）；**两条价值路径**——个人端 one-man data team × 企业端 shared context + governance + long-running agents；**开放跨栈**——不绑定单一 warehouse 或 control plane |
| **竞品定位** | 不把自己定义为通用 coding assistant、平台绑定 copilot、聊天机器人或单一 semantic layer。Datus 是一个开源系统，用来构建和持续演进这些工具真正可靠所需要的数据上下文。详见 [datus-competitors.md](./datus-competitors.md) |
| **地缘策略** | 英文主站（datus.ai）覆盖全球 → GitHub 开源社区（中英文）→ 微信公众号「数据杂货铺」覆盖国内 → 云器/ClickZetta 生态合作 |
| **信任信号** | Apache 2.0 开源、LinkedIn/Expedia/Coinbase POC、云器 Lakehouse 生产案例（自助率 15%→60%）、创始人 StarRocks 背景、Agentic AI Summit 演讲 |

*展开见 [datus-positioning.md](./datus-positioning.md)（品类定义、品牌叙事、竞争生态）与 [datus-competitors.md](./datus-competitors.md)（完整竞品矩阵）。*

## 3. ICP（简版）

- **数据工程师（10 人+团队）**：需要管理大量表、指标、SQL 口径；痛点不是写 SQL 而是理解不熟悉的表结构、沟通需求、数据验证流程繁琐；核心诉求是上下文沉淀与持续复用。
- **数据分析师**：需要自助查询但缺乏 SQL 能力或表结构知识；痛点是与工程侧反复沟通口径；核心诉求是通过 Chatbot 自助取数并具备多轮对话校正能力。
- **数据团队 Leader / CDO**：需要推动团队 AI 化转型；痛点是如何将散落在人脑中的「潜规则、指标黑话、SQL 标准」系统化；核心诉求是可度量的 ROI（自助率提升、查询时间缩短）。
- **企业级客户（POC 阶段）**：LinkedIn、Expedia、Coinbase 类大型企业数据团队；痛点：多数据源、复杂血缘、跨团队协作；核心诉求：安全、稳定、可审计的 Agent 交付。
- **开源社区用户**：个人开发者、小型团队、学生；被「builds evolvable context for your data systems」的概念吸引；通过 GitHub/Docs 自行尝试。

*展开见 [datus-use-cases.md](./datus-use-cases.md)。*

---

## 4. 关键词与竞品（入口）

- [datus-keywords.md](./datus-keywords.md)
- [datus-competitors.md](./datus-competitors.md)

## 5. 站点结构与增长策略（入口）

- [datus-site-structure.md](./datus-site-structure.md)
- [datus-growth-strategy.md](./datus-growth-strategy.md)

---

## 6. 网络检索补充（非官网原文，供策略参考）

| 补充项 | 说明 |
|--------|------|
| **2025 开源节奏** | 2025 年 10 月正式开源（Apache 2.0），5 个月内迭代至 v0.2.6（11 个次版本），发版密度极高——利于内容营销制造话题；LinkedIn、Expedia、Coinbase 等海外头部企业 POC 中 |
| **竞品格局** | 活跃严格竞品 5 个：Wren AI（~9.8K）、Altimate.ai（agentic dbt harness）、TextQL/Ana（enterprise AI data scientist）、Cube.dev（~20K·语义层+Agent）、Defog.ai（SQLCoder）。已退出独立竞争：Dataherald（🔴 关停）、Numbers Station（🟡 被 Alation 收购）、Secoda（🟡 被收购）、Vanna.ai（⚠️ 开源归档）。大公司平台产品：Databricks Genie Code、Snowflake Cortex Code CLI、Google BigQuery DE Agent。详见 [datus-competitors.md](./datus-competitors.md) |
| **Gartner 2025 Hype Cycle** | AI Agents 和 AI-Ready Data 处于 Peak of Inflated Expectations——品类正处于舆论高峰期，利于品牌叙事与 SEO 占位 |
| **中文社区** | 创始人微信公众号「数据杂货铺」+ 中文技术社区（CSDN、知乎）有讨论，但品牌区分度低（类「Datu AI Analyst」同名项目存在）——SEO 与品牌防御为关键课题 |
| **MCP 生态** | Datus 支持 MCP Server 导出 + MCP Client 接入，是早期采用者；MCP 协议在 2025 年已近「table stakes」——差异化需来自工具设计深度而非协议支持本身 |

---

*Demo 文档包 · Datus · https://datus.ai/*
