# §6 产品、竞品与合规事实

## 6.1 产品事实表（P0 级，写作唯一依据）

| 事实 | 值 | 来源日期 |
|------|-----|---------|
| 品类定位 | Capability routing network for AI agents | 官网（2026-08-05） |
| 核心协议 | Discover → Inspect → Probe → Call | 官网 /docs（2026-08-05） |
| 能力总量 | 10,000+ real-world verified capabilities | 官网首页（2026-08-05） |
| 能力分类 | 15+ categories，六大金融能力域 | 官网首页（2026-08-05） |
| 六大金融域 | Quant Trading / Macro & Fixed Income / Risk & Compliance / Investment Research / Crypto & Digital Assets / Alternative Signals | 官网首页（2026-08-05） |
| Agent 平台 | 14+（Claude Code/Cursor/OpenCode/Trae/VS Code/OpenClaw/Hermes） | 官网（2026-08-05） |
| 上线率 / 延迟 | 99.99% uptime / <500ms P95 | 官网声明（2026-08-05） |
| 计费 | Discover/Inspect 免费；Call 1–100 credits/次；credits 永不过期 | /pricing（2026-08-05） |
| 免费层 | 1,000 注册 credits + 100 每日登录 credits（次日重置） | /pricing（2026-08-05） |
| Pro | $19/月：10,000 credits、100 req/min、$0.002/credit 超额 | /pricing（2026-08-05） |
| Scale | $1+：$100→52,500(+5%)、$500→275,000(+10%)、$1,000→575,000(+15%) | /pricing（2026-08-05） |
| CLI 版本 | @qverisai/cli v0.10.0 | /cli、/for-agents（2026-08-05） |
| MCP 版本 | @qverisai/mcp v0.13.0（六工具：discover/inspect/probe/call/usage_history/credits_ledger） | /ecosystem（2026-08-05） |
| Python SDK | qveris v0.6.0（async/typed/streaming） | /ecosystem（2026-08-05） |
| TS SDK | @qverisai/sdk v0.7.0（零依赖，Node 18+） | /ecosystem（2026-08-05） |
| REST API | `POST /search`、`POST /tools/by-ids`、`POST /tools/execute`；Bearer 认证 | /docs/rest-api（2026-08-05） |
| Hosted MCP | 官方托管 MCP（2026-07-15 上线） | /whats-new（2026-08-05） |
| Probe API | 零成本参数预验证 + 报价（2026-07-21 上线） | /whats-new（2026-08-05） |
| Application Center | `/apps`：Earnings Copilot / Options Assistant（BETA） | /whats-new（2026-08-05） |
| QVeris Lab | 无代码 AI 代理工作区（beta，QVerisBot 并入） | /qverisbot（2026-08-05） |
| Skill Registry | 5 官方 skills（qveris-official / stock-copilot-pro / chairman-daily-report / exchange-rate / x-founder-operations） | /skills（2026-08-05） |
| 机器可读文档 | `/setup.md`、`/llms.txt`、`/llms-full.txt`、`/guidelines.md` | /for-agents（2026-08-05） |
| 计费审计 | usage_history / credits_ledger（按 API key 归因） | /whats-new（2026-08-05） |

## 6.2 竞品公平摘要（写作时每竞品 ≥1 优势）

| 竞品 | 定位 | 核心差异点（相对 QVeris） | 优势（写作可承认） |
|------|------|--------------------------|-------------------|
| **Composio** | Agent 工具集成平台（SaaS 操作连接） | 专注用户授权 SaaS 操作（Gmail/Slack），非能力路由 | 预置工具包最大、托管 OAuth 完善、SOC 2 |
| **Toolhouse** | 无代码 Agent 托管平台（BaaS） | 托管执行 + 无代码优先，缺金融纵深 | 上手最快、Cron/RAG 内置 |
| **OpenRouter** | LLM 统一路由网关 | 路由对象是 LLM 模型，非外部数据能力 | 模型路由领域事实标准、计费透明 |
| **Nango** | 代码优先 API 集成基础设施 | 代码优先、需自建工具层 | 灵活性最高、可自托管、审计日志 |
| **FMP** | 金融数据 API | 单一数据源，无 Agent 协议层 | 金融数据品类头部、文档清晰、价低 |
| **Alpha Vantage** | 金融数据 API | 单一数据源，免费层限流 | 免费层起步、品牌知名度高 |
| **Polygon/Massive** | 金融数据 API | 单一数据源 | Stocks Basic 免费档、文档规范 |
| **Databento** | 机构级历史数据 | 订阅 + 交易所许可 | $125 评估 credits、机构级 schema |

**公平对比写法**：
- ✅ 承认竞品优势：`Marketstack's free plan runs at 100 requests per month … one of the few plans you can leave running indefinitely without a billing relationship.`
- ✅ 差异描述：`QVeris runs on credits — no call, no cost. Switching cost drops from "two backend engineers for one week" to zero.`
- ❌ 贬低：`X is terrible / nobody should use Y`

## 6.3 合规红线（写作禁入）

| 红线 | 说明 |
|------|------|
| 投资建议 | 禁止买入/卖出/持仓建议；只陈述数据与事实 |
| 数据时效 | 行情/价格/费率带 `as of {date}` + 来源 |
| 实测方法 | 内部实测标注 n/时间窗/数据源；单次结果加限定语 |
| API 价格 | 竞品价格估算注明来源与"以官方为准" |
| 品牌名 | 统一 QVeris；不写 QVerisBot 代指 Lab 全量 |
| 版本号 | 以 §6.1 产品事实表为准，不用旧版本号 |
| 官网下线栏目 | 不链接 /use-cases/ /scenarios/ /alternative/ |

## 6.4 可引用的官方数据源（外链）

| 类型 | URL |
|------|-----|
| 官网 | https://qveris.ai/ |
| 定价 | https://qveris.ai/pricing |
| 文档 | https://qveris.ai/docs |
| CLI | https://qveris.ai/cli |
| 插件/安装 | https://qveris.ai/plugins |
| 能力图 | https://qveris.ai/capabilities/explore |
| 更新日志 | https://qveris.ai/whats-new |
| 生态 | https://qveris.ai/ecosystem |
| 竞品官网 | 各竞品官网（写 `rel="nofollow noopener"`） |
