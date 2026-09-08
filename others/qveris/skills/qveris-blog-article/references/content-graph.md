# §4 已有内容图谱

## 4.1 本地 blog 文件表与下一序号

| NN | 文件 | slug | 类型 | 状态 |
|----|------|------|------|------|
| 01 | [01-stock-api-free-comparison.md](../../blog/01-stock-api-free-comparison.md) | `stock-api-free-comparison` | Comparison | ✅ 成稿（发布于 2026-07-24） |
| 02 | [02-real-time-stock-price-api.md](../../blog/02-real-time-stock-price-api.md) | `real-time-stock-price-api` | Comparison | ✅ 成稿（2026-07-25，重建自官网 guides） |
| 03 | [03-alpha-vantage-pricing.md](../../blog/03-alpha-vantage-pricing.md) | `alpha-vantage-pricing` | Comparison | ✅ 成稿（2026-07-26，重建自官网 guides） |
| 04 | [04-litellm-alternatives.md](../../blog/04-litellm-alternatives.md) | `litellm-alternatives` | Comparison | ✅ 成稿（2026-07-27，重建自官网 guides） |
| 05 | [05-financial-news-api-benchmark.md](../../blog/05-financial-news-api-benchmark.md) | `financial-news-api-benchmark` | Field Test & Audit | ✅ 成稿（2026-07-28，重建自官网 guides） |

**下一序号：06**（文件 NN 不重排）

## 4.2 官网已发博客索引（120 篇，主题避免重叠）

> 来源：qveris.ai sitemap.xml（2026-08-05）。以下为高频主题分组——新稿前先查本表，与官网已有 slug 主题重叠 >50% → MERGE 或改角度。完整 120 slug 见 sitemap.xml（快照存于 `qveris-others.md` §1.7）。

| 主题簇 | 代表 slug |
|--------|----------|
| **Agent 工具链 / MCP** | `mcp-qveris`、`qveris-in-cursor`、`qveris-cli`、`qveris-hosted-mcp-coding-agent-guide`、`qveris-skill-for-openclaw`、`codex-qveris-a-share-mainline`、`prompt-layering-for-tool-calling`、`agent-tool-use-quality` |
| **计费 / 成本审计** | `ai-finance-agent-cost-audit`、`agent-execution-ledger`、`qveris-oauth-agent-api-key`、`financial-agent-failure-recovery` |
| **金融数据接入** | `qveris-fmp-60`、`qveris-fmp-finance`、`qveris-twelve-data`、`openclaw-a-shares-data`、`financial-data-point-review-agent` |
| **市场 / 事件点评** | `a-share-realtime-quotes-agent`、`a-share-weekly-rebound-confidence-qveris`、`ai-tech-stock-selloff`、`oil-price-a-share-transmission`、`typhoon-bavi-stock-market-qveris`、`film-box-office-stock-qveris` |
| **Agent 架构 / 研究** | `anthropic-finance-agent-third-layer`、`trillion-agents-software-industry`、`why-not-another-langchain`、`agents-become-species`、`enterprise-trustworthy-agent-evidence` |
| **产品 / 生态** | `qveris-ai-options-assistant`、`qveris-ai-stock-research-assistant`、`ai-infrastructure-earnings-copilot`、`capability-explorer`、`qveris-financial-capability-network`、`qveris-playground-new-models` |
| **Agent 平台对比** | `openclaw-vs-hermes`、`codex-openclaw-qveris-bot`、`5-hermes-qveris-cli-prompt` |
| **中文博客（拼音 slug）** | `cong-yi-ci-xing-prompt-dao-lian-xu-gong-7933db`、`gei-coding-agent-jie-shang-10-000-zhong-fb0bca` |

## 4.3 Canonical Concept Registry（官网 guides 已覆盖概念）

> 引用这些概念时只 1–2 句 + link，**不重写完整定义**（G6/Cannibalization）。

| 概念 | Canonical 页 | 引用方式 |
|------|-------------|---------|
| 能力路由网络 | `/guides/capability-routing-network/` | 1–2 句 + link |
| MCP 与工具调用 | `/guides/mcp-server/`、`/guides/what-is-mcp/` | 1–2 句 + link |
| 金融数据 API 选型 | `/guides/financial-data-api-for-ai-agents/`、`/guides/best-financial-data-api-developers-2026/` | 引用已发稿 01 或 guides |
| 成本审计方法 | `/guides/ai-finance-agent-cost-audit/` | 1–2 句 + link |
| FMP 迁移 | `/guides/fmp-vs-alpha-vantage/` 等 fmp-* 系列 | 对比维度互链 |

## 4.4 跨篇边界声明模板

**Blog 互链锚文本**（轮换，勿每篇同一句）：
- `our comparison of free stock data APIs` → `/blog/stock-api-free-comparison`
- `how a QVeris-based audit breaks down API costs` → 相关成本审计文（待建）

**Guides 互链**：
> For the full protocol reference, see the [QVeris docs](/docs) and the [capability routing guide](/guides/capability-routing-network/).

## 4.5 内链原则

| 原则 | 说明 |
|------|------|
| **自然优先** | 只在读者需要下一步阅读时出现；语境不通则不加 |
| **不强求双向** | 入链为 0 的 spoke 仅在确有相关段落时补 1 条 |
| **禁 G6 路径** | 不链 `/auth/*` `/admin/*` `/dashboard/*` `/use-cases/*` `/scenarios/*` `/alternative/*` 及未上线页 |
| **同 slug 上限** | 同篇链同一目标 slug 通常 ≤2 次 |
| **禁链区域** | 正文 `## TL;DR` 区块与 FAQ 内不加内链 |
| **guides 斜杠** | `/guides/{slug}/` 带尾部斜杠 |

## 4.6 文件命名与 README 同步

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{working-slug}.md` |
| NN | 两位递增；当前下一号为 **02** |
| frontmatter `slug` | 裸 slug，与线上 `/blog/{slug}` 对应 |

**成稿后**：Agent 提示人类更新 `blog/README.md` 文件表。**Skill 不自动改 README**。
