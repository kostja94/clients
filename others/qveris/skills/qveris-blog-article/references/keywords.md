# §5 关键词速查

> 派生自 `clients/qveris/qveris-keywords.md`（2026-08-05 同步版）。搜索量/难度 ⚠️ 待验证（需 Semrush/Ahrefs 回填），禁止凭推断填入。

## 5.1 P0 / P1 / P2

| 关键词 | 优先级 | 意图 | 建议类型 | 关联官方内容 |
|--------|:---:|------|---------|-------------|
| capability routing | P0 | 信息 | TechnicalDeepDive | `/guides/capability-routing-network/` |
| ai agent tools | P0 | 信息 | TechnicalDeepDive | `/guides/ai-agent-tool-routing/` |
| financial data api for ai agents | P0 | 商业 | Comparison | `/guides/financial-data-api-for-ai-agents/` |
| free stock api | P0 | 商业 | Comparison | `/blog/stock-api-free-comparison`（已发） |
| best financial data api | P0 | 商业 | Comparison | `/guides/best-financial-data-api-developers-2026/` |
| mcp server | P0 | 信息 | WorkflowGuide | `/docs/mcp-server` |
| ai finance agent cost | P0 | 商业 | FieldTest | `/guides/ai-finance-agent-cost-audit/` |
| hosted mcp | P1 | 信息 | WorkflowGuide | `/docs/mcp-server` |
| ai agent no code | P1 | 商业 | ProductStory | `/qverisbot` |
| earnings copilot | P1 | 商业 | ProductStory | `/apps` |
| options analysis ai | P1 | 商业 | ProductStory | `/apps` |
| sec filing api for ai agents | P1 | 商业 | Comparison | guides sec/filing 主题 |
| ai earnings research | P1 | 商业 | WorkflowGuide | `/apps` |
| ai stock research assistant | P1 | 商业 | WorkflowGuide | 官网 blog 已有 |
| ai api cost calculator | P1 | 商业 | FieldTest | `/guides/api-cost-calculator/` |

## 5.2 话题簇（选题来源）

| 簇 | 关键词示例 | 类型 |
|----|-----------|------|
| **A. 能力路由 / Agent 工具层** | capability routing、tool routing、ai agent tool discovery、unified api for ai tools、agent orchestration | TechnicalDeepDive |
| **B. 金融数据 API** | free stock api、best financial data api、earnings api、sec filing api、real-time stock price api、financial data mcp server | Comparison |
| **C. 计费与审计** | ai api cost、credits pricing、usage ledger、ai finance agent cost audit | FieldTest |
| **D. MCP / 集成** | mcp server setup、hosted mcp、mcp vs function calling、cursor mcp tools、claude code mcp | WorkflowGuide |
| **E. 竞品截流** | composio alternatives、toolhouse alternatives、openbb vs qveris、fmp vs alpha vantage、openrouter alternatives | Comparison |
| **F. 金融分析主题** | earnings call analysis、stock research agent、yield curve、sector rotation、a-share market | MarketAnalysis / FieldTest |
| **G. 产品与生态** | qveris earnings copilot、options assistant、qveris openclaw、qveris cli、agent payments | ProductStory |

## 5.3 意图分类与承接映射

| 意图 | 关键词 | 建议类型 | 承接 |
|------|--------|---------|------|
| 导航 | qveris / qveris pricing / qveris cli | —（非博客任务） | 首页 / pricing / cli |
| 信息 | what is mcp、capability routing | TechnicalDeepDive | 博客 + guides 互链 |
| 商业 | best financial data api、composio alternatives | Comparison / FieldTest | 博客承接 |
| 交易 | install qveris cli、openclaw plugin | WorkflowGuide | 博客 → /plugins /cli 转化 |

## 5.4 内容缺口（选题机会）

| 缺口关键词 | 说明 | 优先级 |
|-----------|------|:---:|
| ai earnings research / earnings copilot 独立词 | `/apps` 无独立 Landing，博客可先承接 | P0 |
| options analysis ai | Options Assistant 无独立 SEO 落地 | P1 |
| hosted mcp 深度教程 | 官网仅 /docs 提及，缺独立教程文 | P1 |
| free-*-api 系列（free forex api 等） | 已发 01 开启，可系列化 | P1 |
| 计费审计系列（credits ledger 实务） | 官网有单篇 audit，可扩为系列 | P2 |
