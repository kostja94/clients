# §1 项目配置与 G1–G7 / F1–F4 阻断规则

## 1.1 项目配置

| 配置项 | QVeris 值 |
|--------|----------|
| **品牌/产品名** | QVeris |
| **公司名** | QVeris AI（仅公司语境） |
| **主域名** | qveris.ai |
| **博客路径** | `/blog/{slug}`（frontmatter `slug` 不含前缀，文件名才带 `NN-`） |
| **作者（默认）** | `QVeris Team`（统一署名；原 Maya Rodriguez 已弃用） |
| **品类 one-liner** | Capability routing network for AI agents — discover, inspect, and call real-world, verified capabilities through one unified protocol |
| **核心协议** | **Discover → Inspect → Probe → Call**（Probe = 零成本参数预验证，2026-07-21 公共 API） |
| **六大金融能力域** | Quant Trading · Macro & Fixed Income · Risk & Compliance · Investment Research · Crypto & Digital Assets · Alternative Signals |
| **关键指标** | 10,000+ capabilities / 15+ categories / 14+ agent platforms / 99.99% uptime / <500ms P95 |
| **定价** | Free $0（1,000 注册 credits + 100 每日登录 credits）；Pro $19/月（10,000 credits，超额 $0.002/credit）；Scale On-Demand $1+（$100→52,500 +5%、$500→275,000 +10%、$1,000→575,000 +15%） |
| **计费模型** | Discover/Inspect 永远免费；Call 1–100 credits/次；credits 永不过期；无订阅强制 |
| **集成方式** | CLI（@qverisai/cli v0.10.0）· MCP Server（@qverisai/mcp v0.13.0，6 工具）· Hosted MCP · Python SDK（qveris v0.6.0）· TypeScript SDK（@qverisai/sdk v0.7.0）· REST API（/api/v1）· OpenClaw 插件 |
| **子产品** | Application Center（Earnings Copilot / Options Assistant）· QVeris Lab / QVerisBot（beta）· QVerisFlow（开源多 Agent 引擎）· Skill Registry（5 官方 skills） |
| **CTA 主链** | `https://qveris.ai/` · `/pricing` · `/plugins`（一键安装）· `/cli` · `/docs` |
| **语言/市场** | 英文正文；全球市场（金融数据覆盖美股/A 股/加密等，无需强制 US-only） |
| **数据版本基准** | 所有产品/版本号/定价以官网 2026-08-05 抓取为准 |

## 1.2 G1–G7 一票否决阻断规则

以下 7 项为发布前硬性阻断——**任一项触发则文章不得发布**，修复后重新过 Gate。Phase 5 SelfCheck 首维即逐项对照此表。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、定价、版本、协议与 qveris.ai 官方矛盾 | 逐 claim 对照 §1.1 配置表 + `product-competitors.md` §6.1 产品事实表。功能不在当前版本 → 不能声称"已发布"。 |
| **G2** | 死链 | 站内或站外链接 404/域名拼写错误 | 逐个检查内链（对照 §1.4 白名单）。外链可有 1–2 失效，但不能全挂。 |
| **G3** | 无来源数字 | 量化 claim（10,000+ 能力、credits 成本、价格）无 attribution | P0 级必须 `[Source: URL]` 或脚注；无来源则删或改定性表述。 |
| **G4** | 竞品/平台状态错误 | 竞品 GA/Beta、数据源能力与官方矛盾 | 打开竞品官网/docs 验证；竞品状态过时可致误导。 |
| **G5** | 产品能力夸大 | 超出 GA 能力；禁「全球首个」「唯一支持」 | 定位语言（"designed to"）≠ 已实现功能。 |
| **G6** | 内链指向未上线页面 | 链到禁止内链列表或未发布路径 | 对照 §1.4 白名单；forthcoming ≤1 且仅 Conclusion 脚注。 |
| **G7** | 重大品牌/合规风险 | 品牌误拼、贬低竞品、投资建议暗示 | 对照 §1.5 合规红线 + 品牌名规则。 |

## 1.3 F1–F4 金融合规阻断（QVeris 特有）

QVeris 博客大量涉及行情、计费、投资研究数据——此类声明需最严格证据标准。**F1–F4 任一项 Fail = 不得发布。** 非金融类文章（纯技术/纯产品流程）自动 Pass。

| # | 阻断条件 | 严格标准 |
|---|---------|---------|
| **F1** | 投资建议 | 任何买入/卖出/持仓建议（"buy X"、"add to your portfolio"）。正确写法：只陈述数据与事实（价格、涨跌幅、订单簿、财务数据），明确"不构成投资建议"。 |
| **F2** | 数据时效缺失 | 行情/价格/费率数据须标注 `as of {date} {timezone}` + 数据来源。历史对比须给时间窗。 |
| **F3** | 实测标注缺失 | 内部实测（credits 消耗、调用延迟、空返回）须标注方法："based on internal analysis, n≈X" 或 "QVeris Data Test — 数据通过 QVeris 能力路由网络实时获取"。单次结果不得写成普适结论。 |
| **F4** | API 价格无来源 | 竞品 API 订阅价格估算须注明 "estimates based on public information" + "refer to each vendor's official site"；禁用无来源的精确报价。 |

## 1.4 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}` — 本地与官网已发（见 `content-graph.md`；slug 不含 NN 前缀） |
| 指南 | `/guides/{slug}/` — 官网 SEO 内容中心（452 篇，统一尾部斜杠） |
| 文档 | `/docs/{slug}` — mcp-server / rest-api / python-sdk / claude-code-setup / opencode-setup / ide-cli-setup / openclaw-setup / cookbook |
| 转化页 | `/pricing` · `/playground` · `/plugins` · `/cli` · `/for-agents` |
| 产品页 | `/apps`（Application Center）· `/capabilities/explore` · `/providers` · `/providers/{slug}` · `/qverisbot` · `/skills` · `/skills/{slug}` · `/ecosystem` · `/whats-new` |
| 信任页 | `/security` · `/privacy` · `/terms` · `/help` |
| 外链 | 数据源官方文档、交易所官网、权威行业报告（带 `rel="nofollow noopener"`） |

**G6 规则**：不链未上线页；forthcoming ≤1 且仅 Conclusion 脚注。**禁链**：`/auth/*` `/admin/*` `/dashboard/*` 及官网已下线栏目 `/use-cases/*` `/scenarios/*` `/alternative/*`。

**内链格式**：Markdown `[锚文本](/blog/{slug})`；guides 用 `/guides/{slug}/` 带尾部斜杠。

## 1.5 合规红线速查

| 红线 | 说明 |
|------|------|
| 品牌名 | 全文统一 **QVeris**；`QVeris AI` 仅公司语境；不写 `QVerisBot` 代指 Lab 全量能力 |
| 投资建议 | 只陈述事实数据（F1） |
| 竞品公平 | 每竞品 ≥1 优势；描述差异而非贬低（G7） |
| 版本事实 | MCP v0.13.0 / CLI v0.10.0 / PySDK v0.6.0 / TSSDK v0.7.0（2026-08-05 抓取） |
| 官网已下线栏目 | 不链接 `/use-cases/*` `/scenarios/*` `/alternative/*`（2026-08 改版移除） |
| 计量单位 | credits 计费（1–100/call）；不写"credits 可兑换美元"等未经证实的表述 |
