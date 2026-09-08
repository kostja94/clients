# QVeris — 增长策略

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[主文档](./qveris.md) | [keywords](./qveris-keywords.md) | [competitors](./qveris-competitors.md) | [use-cases](./qveris-use-cases.md)

**Last updated**: 2026-08-05（已同步 2026-08-05 官网快照）

> **结构说明**：官网 8 月改版移除了 `/use-cases/*`、`/scenarios/*`、`/alternative/*` 栏目并统一了 `/guides/` 尾部斜杠；本版战役节奏据此调整，技术 SEO 清理项已标记完成。

## 1. 增长渠道规划

| 渠道方向 | 目标 Persona | 内容类型 | 优先级 | 预期效果 |
|----------|-------------|---------|--------|---------|
| **竞品截流 SEO**（vs 页 + alternatives 页矩阵，位于 /guides/ 下） | 代理工程师、量化工程师 | 对比页、评测、迁移指南 | P0 | 截获 "composio/openrouter/litellm alternatives" 高意图流量 |
| **金融数据 API 长尾 SEO**（free-*-api 系列） | 量化工程师、投资研究分析师 | 指南、API 对比、教程 | P0 | 承接 "free stock api / best financial data api" 搜索需求 |
| **Agent 生态分销**（Claude Code/Cursor/OpenClaw/Hermes 安装入口 + OpenClaw 插件 + npm + ClawHub Skill） | 代理工程师 | 安装文档、插件、skill、开源仓库 | P0 | 低摩擦获客，生态内口碑传播（14+ 平台、13 安装入口） |
| **内容营销双中心**（/guides 452 篇 + /blog 121 篇） | 全 Persona | 教程、技术博客、市场分析、中文博客 | P1 | 品类教育 + 品牌权威 + 长尾收录 |
| **开发者社区**（GitHub/npm/ClawHub/Reddit/HN） | 代理工程师 | 开源客户端、Release Notes、Show HN、QVerisFlow | P1 | 技术圈口碑、早期采用者 |
| **金融应用层触达**（Application Center） | 投资研究分析师、量化工程师 | 应用演示、工作流教程 | P1 | 承接"ai earnings research / options analysis"意图 |
| **无代码用户触达**（QVeris Lab 场景） | 投资决策者、内容创作者 | 工作流教程、日报模板、社媒分发 | P2 | 扩展非技术用户层 |

## 2. 内容主题与栏目

| 栏目/主题 | 对标关键词（P0/P1） | 内容形式 | 发布节奏 | 承接页 |
|-----------|-------------------|---------|---------|--------|
| X vs QVeris 对比矩阵（补 Pipedream/Glama/Bifrost/Kong/Cloudflare AI Gateway 等） | composio vs qveris（P0） | 对比页 | 2 篇/月 | /guides/{comp}-vs-qveris/ |
| 免费/最佳金融数据 API 系列 | free stock api、best financial data api（P0） | 榜单 + 对比 | 4 篇/月 | /guides/free-*-api/ |
| MCP 教程系列（含 Hosted MCP、Probe） | mcp server、hosted mcp（P0） | 教程 | 2 篇/月 | /guides/mcp-*/ |
| 金融分析主题库（earnings/SEC/估值） | sec filing api、ai investment research（P1） | 指南 | 2 篇/月 | /guides/*-agent/ |
| Application Center 应用页 | ai earnings research、options analysis（P1） | 应用 Landing 页 | 1 篇/季 | /apps → 独立 Landing |
| Agent 机器可读文档 | llms.txt、ai agent protocol（P1） | 协议文档 | 持续 | /for-agents + /llms.txt |
| 中文内容本地化 | 实时股票 api 中文（P2） | 中文指南/博客 | 1–2 篇/月 | /blog 中文 slug |

## 3. 战役节奏

### 短期（0–3 个月）
1. **补齐竞品 vs 页矩阵**：优先 Pipedream、Glama、Kong、Cloudflare AI Gateway 四页（对标 P0 截流词），复用已有对比模板 15 维度结构。
2. **上线"best ai agent tool platforms 2026"品类榜单页**：填补 content gap，抢占品类认知位（官网已有 best-llm-gateways、best-earnings-apis 等单点榜单，可整合为品类总榜）。
3. **迭代 `*-vs-qveris` 页内部互链**：每个 vs 页链接到相邻竞品对比页与本品 /docs，形成截流网络，提升爬取效率。

### 中期（3–6 个月）
4. **Application Center SEO 落地**：为 Earnings Copilot / Options Assistant 各建独立 Landing 页并补入 sitemap（当前 /apps 未入 sitemap），承接金融应用层搜索意图。
5. **重启场景页栏目**：以 guides 高流量主题为基础，重建 `/use-cases/{slug}` 栏目（earnings research / market monitor / price alert 等），或改为应用工作流页形态。
6. **中文内容中心规模化**：将 Top 10 P0 指南本地化为中文，配合中文站 URL 结构，承接中文市场长尾。
7. **企业与合规方向**：公开 SOC 2 状态、增加企业案例页，配合 Scale/企业销售。

### 长期（6–12 个月）
8. **刷新停滞工具页**：`/tools/*` 11 页 lastmod 均停滞于 2025-12-26，按新能力目录扩充或 301 归并（消除陈旧信号）。
9. **生态联盟**：与 Claude Code/Cursor/OpenClaw 官方教程联动，成为其生态推荐工具（已有 /ecosystem 开源页与 QVerisFlow 框架背书）；参与 Agent 工具层行业报告与榜单。

## 4. 竞品差异化方向

基于 [competitors](./qveris-competitors.md#4-差异与机会swot) 的差距分析，本品可攻克的机会：

1. **"调用前质量信号"心智**：Inspect/Probe（成功率/延迟/成本 + 零成本预验证）是竞品空白，可强化"负责任工具调用"叙事，切入企业代理团队。
2. **"金融数据 + Agent 协议"组合定位**：单一金融 API（FMP/Alpha Vantage）缺协议层、工具平台（Composio/Toolhouse）缺金融数据——QVeris 是唯一两者兼备；Application Center 把这一组合从 API 层上探到应用层（Earnings Copilot / Options Assistant），重点打击"从 FMP 迁移到 Agent 原生"的搜索需求（已有 fmp-vs-* 系列承接）。
3. **"零 Token 调用"成本叙事**：相对 MCP schema 注入，CLI 子进程方案直接量化 Token 节省（官方声明最高 80%），攻击高成本痛点。
4. **"托管 MCP"零运维叙事**：2026-07-15 上线 Hosted MCP，与"无需本地进程"的开发者体验差异化，可作为 MCP 教程内容的招牌。

## 5. 度量指标

| KPI | 建议跟踪工具 | 说明 |
|-----|------------|------|
| vs/alternatives 页品牌词引流 | Google Search Console | 竞品词到本品搜索的转化 |
| guides/blog 收录与排名 | Ahrefs/Semrush | P0 词排名变化（composio vs qveris 等） |
| 注册转化率（1000 credits 领取） | 站内 Analytics | 内容→注册漏斗 |
| Free→Pro/Scale 转化率 | Dashboard 计费数据 | 免费 credits 耗尽后的付费转化 |
| 日活调用 / credits 消耗 | usage_history | 留存与用量健康度 |
| MCP/CLI 安装量 | npm download stats + OpenClaw 插件数据 | 生态触达指标 |
| /apps 应用使用量 | 站内 Analytics | Application Center 工作流活跃度 |
| 机器可读文档被 Agent 调用次数 | 日志（/setup.md、/llms.txt 抓取） | Agent 生态自助 onboarding 效果 |

---

*Last updated 2026-08-05 · 渠道与内容主题对齐 [keywords](./qveris-keywords.md) P0/P1 与 [use-cases](./qveris-use-cases.md) Persona*
