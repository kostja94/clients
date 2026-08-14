# QVeris — 杂项归档

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[site-structure](./qveris-site-structure.md) | [主文档](./qveris.md)

**Last updated**: 2026-08-05（Sitemap 明细已按 2026-08-05 快照重写）

## 1. Sitemap 明细

> 完整 sitemap.xml 共 **615 条 URL**（单文件，无子 sitemap，robots.txt 声明）。按类别归档如下（访问日期 2026-08-05）。
> **对比 2026-08-03 旧快照（~1,294 条）**：`/use-cases/*`（4）、`/scenarios/*`（6）、`/alternative/*`（7）、部分 `/tools/*`（16→11）已移除；guides 尾部斜杠统一；总量精简约 52%。

### 1.1 单页（14 条）

| URL | lastmod | priority |
|-----|---------|----------|
| https://qveris.ai/ | 2025-12-26 | 1.00 |
| https://qveris.ai/playground | 2026-07-10 | 0.80 |
| https://qveris.ai/help | 2026-07-10 | 0.51 |
| https://qveris.ai/privacy | 2026-07-10 | 0.41 |
| https://qveris.ai/terms | 2026-07-10 | 0.41 |
| https://qveris.ai/docs | 2025-12-26 | 0.80 |
| https://qveris.ai/providers | 2025-12-26 | 0.80 |
| https://qveris.ai/pricing | 2025-12-26 | 0.51 |
| https://qveris.ai/blog | 2026-07-10 | 0.64 |
| https://qveris.ai/capabilities/explore | 2026-07-10 | 0.64 |
| https://qveris.ai/cli | 2026-07-10 | 0.64 |
| https://qveris.ai/ecosystem | 2026-07-10 | 0.64 |
| https://qveris.ai/for-agents | 2026-07-10 | 0.64 |
| https://qveris.ai/plugins | 2026-07-10 | 0.64 |
| https://qveris.ai/qverisbot | 2026-07-10 | 0.64 |
| https://qveris.ai/security | 2026-07-10 | 0.64 |
| https://qveris.ai/skills | 2026-07-10 | 0.64 |
| https://qveris.ai/whats-new | 2026-07-10 | 0.64 |

### 1.2 工具页 `/tools/{slug}`（11 条）

binance / coingecko / google-maps / openweather / unsplash / stripe / twilio / sendgrid / deepl / mapbox / amap（lastmod 全部 2025-12-26，⚠️ 长期未更新）

> 旧快照中的 crypto-dashboard / fear-greed-index / mcp-tester / stock-app / currency-converter 已移除。

### 1.3 文档页 `/docs/{slug}`（8 条）

claude-code-setup / cookbook / ide-cli-setup / mcp-server / openclaw-setup / opencode-setup / python-sdk / rest-api（lastmod 2026-07-10）

### 1.4 Skills 页 `/skills/{slug}`（5 条）

chairman-daily-report / exchange-rate / qveris-official / stock-copilot-pro / x-founder-operations（lastmod 2026-07-10）

> 旧快照中的 qveris-earnings-call-brief / qveris-equity-research-report 已移除；对应能力并入 stock-copilot-pro（金融研究）与 guides 中的 earnings/equity 主题文章。

### 1.5 Provider 页 `/providers/{slug}`（1 条）

morningstar（lastmod 2025-12-26）

### 1.6 指南页 `/guides/`（452 条）

- 目录：`/guides/`（lastmod 2026-08-04，已核实 200）
- 文章：`/guides/{slug}/` 共 **451 条**，**全部为尾部斜杠形态（452/452 无混用）**，规范问题已解决
- lastmod 覆盖 2026-07-03 ~ 2026-08-04，更新频繁
- 主题覆盖：MCP/工具协议（what-is-mcp、mcp-vs-function-calling、mcp-registry）、能力路由（capability-routing-network、ai-agent-tool-routing）、金融数据（best-financial-data-api-developers-2026、free-stock-api、financial-statements-api-fmp、fmp-vs-*）、Agent 构建（build-ai-investment-research-agent、ai-earnings-analysis-agent）、竞品截流（composio-vs-qveris、toolhouse-vs-qveris、openbb-vs-qveris、nango-alternatives、openrouter-alternatives、best-llm-gateways）等

### 1.7 博客 `/blog/{slug}`（121 条）

- 目录：`/blog` + 文章 120 条
- lastmod 覆盖 2026-03-13 ~ 2026-08-04
- 英文技术博客：qveris-in-cursor / mcp-qveris / ai-finance-agent-cost-audit / agent-action-long-term / ai-infrastructure-earnings-copilot / qveris-fmp-60 / qveris-backtesting-data-first 等
- 中文博客（拼音 slug）：`cong-yi-ci-xing-prompt-dao-lian-xu-gong-7933db` / `gei-coding-agent-jie-shang-10-000-zhong-fb0bca` / `a-share-weekly-rebound-confidence-qveris` 等
- 市场分析类：google-tesla-q2-a-share-semiconductor / oil-price-a-share-transmission / openclaw-a-shares-finance-assistant 等

### 1.8 未入 sitemap（已核实在线）

- `/apps`（Application Center，HTTP 200）—— ⚠️ 未入 sitemap，建议补录
- 机器可读文档：`/setup.md`、`/llms.txt`、`/llms-full.txt`、`/guidelines.md`（经 /for-agents 声明，未在 sitemap）

## 2. 数据引用

| 数据 | 数值 | 来源 + 日期 |
|------|------|-----------|
| 能力总量 | 10,000+ | qveris.ai 官网（2026-08-05） |
| 能力分类 | 15+，六大金融域 | qveris.ai 官网（2026-08-05） |
| 上线率 / P95 延迟 | 99.99% / <500ms | qveris.ai 官网声明（2026-08-05），⚠️ 未独立验证 |
| Agent 平台 | 14+ | qveris.ai 官网（2026-08-05） |
| MCP 版本 | @qverisai/mcp v0.13.0（六工具） | /ecosystem、/for-agents（2026-08-05） |
| CLI 版本 | @qverisai/cli v0.10.0 | /cli、/for-agents（2026-08-05） |
| Python SDK | qveris v0.6.0（PyPI） | /ecosystem（2026-08-05） |
| TS SDK | @qverisai/sdk v0.7.0（npm） | /ecosystem（2026-08-05） |
| 定价 | Free $0 / Pro $19 / Scale $1+ | /pricing（2026-08-05） |
| 示例调用成本 | 1–100 credits/次 | /pricing（2026-08-05） |
| Sitemap 总量 | 615 URL（guides 452 / blog 121 / 其余 42） | sitemap.xml（2026-08-05） |
| 官网流量 / 搜索量 / 市场份额 | — | ⚠️ 待验证（需 Semrush / Similarweb 补充） |

## 3. 合规（如适用）

- 官网含 `/privacy`、`/terms`、`/security` 页面（lastmod 2026-07-10 / 2025-12-26）
- QVeris 核心引擎为托管服务，客户端工具（MCP server、SDK、skills、plugins、CLI、QVerisFlow）开源；/ecosystem 页统一承载开源与社区入口
- 内容页含大量 "X vs QVeris" 竞品对比页（位于 /guides/ 下），属于标准的 SEO 竞品词策略，非合规风险

## 4. 归档

- 本文件各分区按需更新；某区超过 200 行时拆出独立文件
- Sitemap 明细随站点改版重抓 sitemap.xml 刷新本表（上次抓取 2026-08-05）
- 旧快照（2026-08-03）中的 use-cases / scenarios / alternative 明细已随栏目下线归档移除

---

*Last updated 2026-08-05 · 数据抓取：sitemap.xml 全量解析 + 核心页（2026-08-05）*
