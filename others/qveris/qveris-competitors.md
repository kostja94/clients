# QVeris — 竞品分析

> 遵循 [客户文档规范](../../skills for clients/client-template.md)
> 关联：[主文档](./qveris.md) | [features](./qveris-features.md) | [keywords](./qveris-keywords.md)

**Last updated**: 2026-08-11（竞品范围收敛：按"主要对标 + 知名"标准移除 OpenRouter/Toolhouse/LiteLLM/Portkey，依据 2026-08-11 流量与融资核实；保留 Composio/Nango/FMP/Alpha Vantage 并回填市场份额数据；同日回填 Composio 情报核实——工具规模 / MCP 架构 / 融资 / 营收 / 开源 / 安全事件六项修正 + 定价精确化 + Semrush 数据，见 §5；同日核查用户清单 15 个候选竞品（Composio/Nango 原已收录），新增 13 个：Fiscal / Benzinga / Quiver Quantitative / AlphaSense / BridgeWise / Financial Datasets / Zapier MCP / Pipedream / LlamaIndex / Merge / OpenBB / Paragon / Arcade.dev，全部保留，分为直接竞品（入 §1~§3）与相邻观察名单（入 §6））

> **结构说明**：QVeris 的 "X vs QVeris / X alternatives" 页面 2026-08 改版后统一归属 `/guides/{slug}/` 栏目（如 `/guides/composio-vs-qveris/`、`/guides/openbb-vs-qveris/`），原 `/alternative/*` 栏目已移除。

## 1. 竞品总览

> 分两档：**核心对标**（§2 详拆，写入对比页）与**相邻/观察**（§6 跟踪名单，一般只用于内部情报）。

### 1.1 核心对标

| 竞品 | 定位 | 目标用户 | 核心功能 | 价格区间 | 与本品差异 |
|------|------|---------|---------|---------|-----------|
| **Composio** | Agent 工具集成平台（SaaS 操作连接，正向跨类别能力扩展） | 构建生产力 Agent 的开发者 | 1,000+ 工具包 / 500+ 应用 / 20,000+ tools、托管 OAuth、Sessions 用户隔离、Tool Router 单一网关（GA） | Free → $29 → $229 + 企业定制（Pro tools 按 ~3x 计价） | 专注用户授权 SaaS 操作（Gmail/Slack/Salesforce），正用 Pro tools 与 toolkit 文档页扩展数据/API 侧能力，非能力路由 |
| **Nango** | 代码优先 API 集成基础设施 | 生产级集成团队 | 900+ API、OAuth 托管、数据同步、webhooks、自托管 | 开源 + 云订阅 | 代码优先、需自建工具层，非开箱即用的能力目录 |
| **Fiscal** | 机构级金融数据平台（AI Agent 原生） | 金融数据 Agent / 量化团队 | 基本面/KPI/比率/报表审计可溯源、API + MCP、2026-06 成为 OpenAI Codex/ChatGPT 官方 app | Free + API $990/年起 | 单一金融数据源，无能力路由、无多 Provider 冗余 |
| **Financial Datasets** | 面向 AI Agent 的金融数据 API | AI 金融 Agent / 量化工程师 | 27,000+ tickers、财报/SEC filings/insider/持仓/earnings、hosted MCP | $20 一次性 → $200/月起 | YC 支持，单域金融数据，无跨类别能力、无路由/审计账本 |
| **OpenBB（ODP）** | 开源金融数据平台（数据归一化层） | 量化工程师 / 投资研究团队 | ODP 归一化 100+ provider、Python/CLI/MCP/REST 多出口、Workspace 企业版 | 开源（AGPLv3）+ 企业版 | 开源生态强、自托管，但需自建能力目录，无调用级质量信号 |
| **FMP（Financial Modeling Prep）** | 金融数据 API | 开发者/量化团队 | 财务报表、实时行情、SEC 文件、可选 API | $20+/月起 | 单一金融数据源，无 Agent 协议层、无多 Provider 路由 |
| **Alpha Vantage** | 金融数据 API | 开发者 | 股票/外汇/加密/经济指标 API | 免费层 + $50/月起 | 单一数据源，免费层延迟高，无 Agent 原生协议 |

### 1.2 相邻 / 观察名单（详见 §6）

Zapier MCP、Pipedream（已被 Workday 收购）、Merge（Agent Handler）、Arcade.dev、Paragon、LlamaIndex（LlamaParse）、Benzinga、Quiver Quantitative、AlphaSense、BridgeWise

## 2. 直接竞品详细拆解

### 2.1 Composio
- **定位与核心能力**：Agent 集成平台，核心是 Sessions 架构——按用户隔离身份、连接账户、允许的工具集与执行状态。托管 OAuth（存储/刷新/轮换/吊销），SOC 2 Type II，Enterprise 可 VPC/on-prem 部署。工具规模官方口径已统一为 **1,000+ 工具包 / 500+ 应用 / 20,000+ tools**（约 982 toolkits）。MCP 架构已换代：**Tool Router 已 GA**，`mcp.composio.dev` 完全弃用，Rube 并入主 SDK——现在是"单一网关端点"而非"一堆 MCP server"。另有 real-time event triggers / webhooks（RightAIChoice 等第三方评测确认），集成深度已不止于 tool call。
- **入选依据**：Agent 工具集成品类最知名之一。主体 **Sampark Inc（YC W24）**；融资合计 $29M：Lightspeed 领投 Series A $25M + Together Fund $4M 种子；约 65 名员工（2026-05，1 月为 57）；2025 年中约 $2M 收入、200+ 付费客户、10 万+ 开发者。
- **优势**：预置工具包最大；托管认证完善（用户级凭证）；Sessions 用户隔离是护城河；SOC 2 Type II + VPC/on-prem 可部署；SDK 开源（ComposioHQ/composio，MIT，约 29.5k stars / 4.5k forks）——建议表述为"SDK 开源、托管层闭源"。
- **劣势**：托管运行时与工具实现闭源（主仓库开源的是 SDK，不是工具实现）；曾有过安全事件记录——但 2026-07 已做 SSRF-safe URL 上传、遥测脱敏等加固，写安全对比须注明"已修复"。
- **定价**：见下方案格。注意 **Pro tools 概念**：搜索 API（Composio Search / Perplexity / Exa / SerpAPI）、代码沙箱（E2B）、ML 推理、OCR/文档解析、爬虫——按约 3 倍计价，说明其已向"数据/API 侧能力"扩展，不再只是 SaaS 操作。
- **市场份额**：月访问约 100–170 万（Semrush 1.36M / SimilarWeb 0.99–1.7M，2026-06）、同类竞品中最大；2025 年中约 $2M 收入、200+ 付费客户（来源：Composio 官方 / Press release 2025-07）。
- **SEO/GEO 表现**：Composio 官网有大量 alternatives 内容，流量最高的不是产品页而是对比型技术长文（`/content/` 栏目：claude-code-vs-openai-codex、claude-code-vs-open-code、claude-agents-sdk-vs-openai-agents-sdk-vs-google-adk 等）；`docs.composio.dev/toolkits/polygon_io` 已把 "polygon.io"（3,600/mo）品牌词排到第 4 位——正用 toolkit 文档页截流金融数据 API 品牌词，与 QVeris `fmp-vs-polygon-io` 等页面直接对撞（详见 §5.3）。QVeris 的 `composio-vs-qveris` 页正在截流其品牌词（来源：qveris sitemap 2026-08-05）。

**Composio 定价明细**（2026-08-11 核实，以官方为准）

| 方案 | 价格 | 标准调用/月 | Pro 调用/月 | 超额单价 |
|------|------|-----------|------------|---------|
| Hobby / Totally Free | $0 | 20K | 1K | — |
| Growth / Ridiculously Cheap | $29/月 | 200K | 5K | $0.299 / 1K（Pro $0.897） |
| Scale / Serious Business | $229/月 | 2M | 50K | $0.249 / 1K（Pro $0.747） |
| Enterprise | 定制 | 弹性 | 弹性 | VPC/on-prem、SOC 2、SLA |

> Pro tools 的 ~3x 计价对场景表 2 很关键：Composio 已向"跨类别能力"扩，不再只是 SaaS 操作；"金融数据纵深"仍是壁垒，但"数据/API 能力 vs SaaS 操作"二分法正在被侵蚀（对应 Threats 中"Composio 增加能力发现"，已有实证）。

### 2.2 Nango
- **定位与核心能力**：代码优先 API 集成平台。工程师用 TS 函数在仓库里写集成，云端运行；900+ API、OAuth、同步（RAG）、webhooks、MCP server、OpenTelemetry。开源、可自托管。
- **入选依据**：YC W23、GitHub 10K+ stars；融资 $7.5M seed（2026-04，Gradient 领投）、月访问约 5–18 万（SimilarWeb/Semrush 2026-06）。
- **优势**：灵活性最高、企业合规友好（审计日志）、自托管第一天可用。
- **劣势**：代码优先=工作量更大；无预置工具 schema、无 Agent 感知错误处理；需要自己搭工具层。
- **市场份额**：月访问约 5–18 万；10,000+ 团队、月处理数十亿 API 请求、融资前已现金流为正（来源：Nango 博客 2026-04；SimilarWeb/Semrush 2026-06）。
- **SEO/GEO 表现**：QVeris 有 `nango-alternatives` 页截流（来源：qveris sitemap 2026-08-05）。

### 2.3 FMP（Financial Modeling Prep）
- **定位与核心能力**：金融数据 API——实时行情、财务报表、SEC 文件、公司概况、分析师共识等，涵盖 50+ 端点。
- **入选依据**：金融数据 API 品类公认头部之一；月访问约 45 万（2026-06 流量估算）。
- **优势**：金融数据品类头部独立 API；文档清晰；价格相对亲民。
- **劣势**：单一数据源、无 Provider 冗余；无 Agent 协议层（需自己包装 MCP）；无跨类别能力（不覆盖文档/视觉/媒体）。
- **市场份额**：月访问约 45 万（来源：流量估算工具 2026-06）；2016 年成立、无公开融资、靠付费订阅运营。
- **SEO/GEO 表现**：QVeris 已建 `fmp-vs-alpha-vantage`、`fmp-vs-finnhub`、`fmp-vs-polygon-io`、`fmp-mcp-server-for-claude`、`financial-statements-api-fmp` 等一批 FMP 关键词页（来源：qveris sitemap 2026-08-05）。

### 2.4 Alpha Vantage
- **定位与核心能力**：老牌免费金融数据 API（股票/外汇/加密/经济指标），免费层 + 付费层。
- **入选依据**：金融数据 API 品类老牌头部、品牌知名度高；月访问约 40 万（2026-06）。
- **优势**：免费层起步、品牌知名度高。
- **劣势**：免费层限流严重（5 req/min 级别）、数据深度与更新时效受限；无 Agent 协议。
- **市场份额**：月访问约 40 万（来源：流量估算工具 2026-06）；YC 出身、团队约 7–10 人、营收 $1M–$10M 量级、无公开融资。
- **SEO/GEO 表现**：QVeris 有 `alpha-vantage-mcp-alternative`、`alpha-vantage-pricing-alternative` 截流页。

### 2.5 Fiscal
- **定位与核心能力**：机构级公共股权数据平台，**为 AI Agent 原生设计**——基本面、KPI、比率、分部数据、报表（20+ 年历史），每个数字可链接回源文件（human analyst verification，审计可溯源）；提供 REST API + 官方 MCP server + Terminal 三种交付。盈利后数分钟内发布数据。
- **入选依据**：与 QVeris 同为"金融数据 + Agent 原生"直接对位；2023 年由 Stratosphere.io 衍生（前身 FinChat），2025 年中 rebrand 为 Fiscal.ai 并完成 Series A；2026-06-02 OpenAI 开放 ChatGPT/Codex 给外部业务应用，Fiscal.ai 是首批官方 app 之一（投资场景插件）。
- **优势**：数据可溯源到 SEC 源文件（合规审计友好）；MCP 官方托管；机构客户背书（Morgan Stanley、Raymond James、Salesforce 等）。
- **劣势**：单一数据源、无多 Provider 冗余；个体 API 订阅 $990/年起、无免费 API 层；分部/KPI 覆盖约全球 2,300 家最大公司，小盘稀疏；盘中数据 15 分钟延迟。
- **市场份额**：无公开融资规模；付费 API 客户含多家大型机构（来源：matchmybroker 2026 评测、docs.fiscal.ai 2026-08-11）。
- **SEO/GEO 表现**：尚无 QVeris 截流页，建议规划 `fiscal-vs-qveris` / `finchat-alternatives` 类页面承接。

### 2.6 Financial Datasets
- **定位与核心能力**：面向 AI Agent 的机构级金融数据 API——标准化 + 原始口径财务报表、SEC filings（支持按 section 抽取，如 Item 1A/Item 7）、earnings、insider trades、机构持仓、股价；27,000+ US tickers（含退市）、30+ 年历史；JSON 结构化、machine-first；提供 hosted MCP（mcp.financialdatasets.ai）、OpenAPI spec、llms.txt。数据以"秒级"发布并对照 EDGAR 人工抽样校验。
- **入选依据**：YC 支持（官网"Backed by Y Combinator"，批次待查）；与 QVeris 同为"金融数据 API for AI agents"直接对位；价格低（$20 起）对独立开发者有吸引力。
- **优势**：Agent 原生（MCP/OpenAPI/llms.txt 齐全）；数据源头直采 SEC；价格友好。
- **劣势**：单域（仅金融、仅 US 股票）无跨类别能力；无能力路由/质量信号/审计账本；无用户授权 SaaS 操作。
- **市场份额**：无公开融资/流量数据（来源：官网 financialdatasets.ai 2026-08-11）。
- **SEO/GEO 表现**：品牌词 "financial datasets" 竞争弱，QVeris 建议用 `financial-datasets-api-alternative` 类页截流。

### 2.7 OpenBB（Open Data Platform）
- **定位与核心能力**：开源金融数据平台。ODP 作为"connect once, consume everywhere"数据归一化层，统一 100+ 数据 provider（Fred/Polygon/Benzinga 等）为单一 API；Python 包（`pip install openbb`）、CLI、MCP servers for AI agents、REST 多出口；Workspace 为面向分析师的 AI 工作台（on-prem/VPC、SOC 2、访问控制、审计追踪）。
- **入选依据**：开源金融数据品类公认头部（GitHub 71k+ stars / 7k+ forks，AGPLv3）；131k 注册用户；融资约 $9M（2022-03 seed $8.5M，OSS Capital 领投，Ram Shriram 等参与）；QVeris 已有 `openbb-vs-qveris` 页面承接。
- **优势**：开源社区生态最大、数据 provider 可插拔、可自托管/私有化部署（企业合规友好）。
- **劣势**：数据质量与时效依赖所连 provider；无开箱即用的能力目录与调用级质量信号；无按次计费/审计账本；能力需自行编排。
- **市场份额**：月访问约 20–50 万（流量估算 2026-06，需复核）；开源下载量大（来源：GitHub 2026-08-11）。
- **SEO/GEO 表现**：QVeris `openbb-vs-qveris` 已上线承接（来源：qveris sitemap 2026-08-05）。

## 3. 场景级对比表

### 场景表 1：实时金融数据获取（Agent 内调用）

| 维度 | QVeris | FMP | Alpha Vantage |
|------|--------|-----|---------------|
| 接入方式 | CLI/MCP/Hosted MCP/SDK/REST，14+ Agent 平台 | REST 为主 | REST 为主 |
| 数据广度 | 10,000+ 能力跨 15 类，金融六域纵深 | 金融数据深度强，单域 | 金融基础数据，单域 |
| Provider 冗余 | ✅ 多 Provider 自动 failover | ❌ 单一来源 | ❌ 单一来源 |
| 调用前质量信号 | ✅ 成功率/延迟/成本可查 + Probe 零成本预验证 | ❌ | ❌ |
| Agent 原生协议 | ✅ Discover→Inspect→Probe→Call | ❌ 需自行封装 | ❌ 需自行封装 |
| 计费 | 按次 1–100 credits，免费层 1,000 | 订阅制 $20+/月 | 免费层 + $50/月起 |
| 本品优势 | 一站式 Agent 集成 + 冗余 + 审计 | 数据结构化程度高 | 免费起步 |

### 场景表 2：Agent 外部工具集成（生产力/自动化）

| 维度 | QVeris | Composio | Nango |
|------|--------|----------|-------|
| 核心主张 | 能力路由网络 | SaaS 操作连接（正向跨类别扩展） | 代码优先集成基建 |
| 工具规模 | 10,000+ 能力 | 1,000+ 工具包 / 500+ 应用 / 20,000+ tools（约 982 toolkits） | 900+ API（自建） |
| 用户授权操作（Gmail/Slack） | ❌ 侧重数据/API 能力 | ✅ 强项（Sessions + 托管 OAuth 护城河，SOC 2 Type II） | ✅ 托管 OAuth |
| 调用前 Inspect | ✅ 成本/延迟/成功率 | ❌ | ❌ |
| 定时任务 / RAG | ❌（聚焦调用层） | ✅ 部分（triggers/webhooks 已内建） | ✅ 同步内建 |
| 自托管 | ❌（核心引擎托管） | ✅（Enterprise VPC/on-prem） | ✅ |
| 金融数据纵深 | ✅ 六域 | ⚠️ 扩展中（Pro tools 含搜索/爬虫/OCR；toolkit 文档页已截流 polygon.io 等金融品牌词） | ❌ |
| 本品优势 | 调用层协议最完整、数据广 | — | — |

> **修订说明（2026-08-11）**：Composio 已具 real-time triggers/webhooks，"集成深度到 tool call 为止"的说法不成立，不得写入对比页；Enterprise 提供 VPC/on-prem，自托管差距仅存在于非企业场景。"金融数据纵深"仍是 QVeris 壁垒，但"数据 vs SaaS 操作"二分法已松动（§5 有实证）。

### 场景表 3：Agent 原生金融数据 API（2026-08-11 新增竞品核查）

| 维度 | QVeris | Fiscal | Financial Datasets | OpenBB ODP |
|------|--------|--------|--------------------|-----------|
| 品类 | 能力路由网络 | 机构级金融数据平台 | 金融数据 API for AI agents | 开源数据归一化层 |
| 金融数据广度 | 10,000+ 能力跨 15 类，六域纵深 | 基本面/KPI/比率/报表，2,300+ 大盘覆盖 | 27,000+ US tickers（含退市） | 100+ provider 聚合 |
| 数据可溯源 | ❌（聚合路由） | ✅ 每值链回 SEC 源文件 | ✅ 对照 EDGAR 校验 | ❌ 依赖 provider 来源 |
| 数据时效 | 实时（P95 <500ms） | 披露后分钟级；盘中 15 分钟延迟 | 发布后秒级 | 依赖 provider 时效 |
| Provider 冗余 | ✅ 多 Provider failover | ❌ 单一来源 | ❌ 单一来源 | ⚠️ 可插拔 provider（自建） |
| 调用前质量信号 | ✅ Inspect + Probe 零成本预验证 | ❌ | ❌ | ❌ |
| 计费 | 按次 1–100 credits，免费层 1,000 | API $990/年起 | $20 一次性 / $200/月 | 开源免费 + 企业版 |
| 审计账本 | ✅ usage_history/credits_ledger | ⚠️ 部分（溯源到源文件） | ❌ | ❌ |
| 本品优势 | 协议最完整 + 冗余 + 审计；跨类别 | 机构信任背书 + 溯源 | 最便宜起步 + 秒级时效 | 开源生态 + 私有化 |

> 结论：Fiscal / Financial Datasets 验证了"金融数据 + Agent 原生"品类的需求正在放大（前者打进 OpenAI 官方 app 生态，后者 YC 支持低价走量）；对 QVeris 而言，数据单点能力可被追平，**调用前质量信号 + 多 Provider 冗余 + 跨类别广度**仍是差异化（与 §5.4 叙事收窄一致）。

## 4. 差异与机会（SWOT）

### 优势 Strengths
- **能力路由 + 质量信号**：Inspect 提前暴露成功率/延迟/成本，竞品均不具备；Probe API（2026-07-21）更将"零成本预验证"公共化，是决策层差异化。
- **金融六域纵深**：Composio/Nango 均无垂直数据，FMP/Alpha Vantage 有数据但无 Agent 协议层——这是 QVeris 独特壁垒；Application Center（Earnings Copilot / Options Assistant）进一步把能力打包成金融工作流应用。
- **按次计费 + 审计账本**：Pay-as-you-go + usage_history/credits_ledger（支持按 API key 归因），契合 Agent 高频小额的调用经济。
- **CLI 零 Token**：相对 MCP schema 注入，子进程方案在长上下文场景可省最高 80% prompt token（官方声明）。
- **托管 MCP（2026-07-15）**：无需本地进程即可让 MCP 客户端接入，降低 onboarding 门槛。

### 劣势 Weaknesses
- **无用户授权 SaaS 操作**（Gmail/Slack/Salesforce 级连接）——Composio 独占该场景，其 Sessions + 托管 OAuth + SOC 2 Type II + VPC/on-prem 是护城河。
- 核心引擎闭源托管，自托管能力缺失（企业内网部署受限）——Composio Enterprise 可 VPC/on-prem，QVeris 无对等方案，企业单是实打实的落差。

### 机会 Opportunities
- **"Agent 工具层"品类教育窗口期**：Best-of 榜单页（best ai agent tool platforms 2026）可抢占品类认知位。
- **"金融数据 + Agent 原生"品类被竞品验证放大**：Fiscal（打进 OpenAI Codex/ChatGPT 官方 app 生态）、Financial Datasets（YC 支持）、OpenBB（开源 + MCP 出口）同向涌入，说明开发者对"金融数据直接接 Agent"的认知正在被教育——QVeris 的 `*-alternative` / vs 页矩阵（含 `openbb-vs-qveris`）正好承接这批高意图流量。
- **金融数据 API 迁移潮**：FMP/Alpha Vantage 用户向 Agent 原生方案迁移（已有 `*-alternative` 页承接）。
- **MCP 标准红利**：MCP 成为事实标准后，托管 MCP + 能力目录的定位放大。
- **金融应用层空白**：Application Center 刚起步（BETA 两应用），"ai earnings research / options analysis" 搜索意图尚未被大规模承接。

### 威胁 Threats
- **Composio 横向扩张已有实证**：Pro tools（搜索 API / 代码沙箱 E2B / ML 推理 / OCR / 爬虫，按 ~3x 计价）正在侵蚀"数据/API 能力 vs SaaS 操作"二分法；`docs.composio.dev/toolkits/polygon_io` 已把 "polygon.io"（3,600/mo）截流到第 4 位，证明其 toolkit 文档页会直接抢金融数据品牌词——与 QVeris `fmp-vs-polygon-io` 等页面同战场；Tool Router GA 后其 MCP 架构收敛为单一网关，能力发现口径与 QVeris 对齐。
- **金融数据层单点对位（新增）**：Fiscal / Financial Datasets / OpenBB 均以"金融数据直连 Agent"为卖点且价格更便宜/开源免费，QVeris 在纯数据维度不再有数量优势（10,000+ 能力 vs 其单点深覆盖），必须靠质量信号 + 冗余 + 跨类别 + 审计差异化。
- **大厂生态收紧（新增）**：Pipedream 已被 Workday 收购（agent-to-SaaS 基建成为企业战略资产）；Arcade 绑定 Anthropic MCP 授权规范；Zapier MCP 用 9,000+ apps 无代码治理占位——工具层竞争从独立产品转向"平台内建"。
- **企业研究层 AI 化（新增）**：AlphaSense（SuperAnalyst agent、$600M+ ARR）、BridgeWise（pAI wealth agent、22 语言）、Fiscal 进 OpenAI 生态，说明"AI 金融研究"从数据 API 向应用/Agent 端上探，压缩中间层差异化空间。
- 大模型厂商内建工具生态（原生 MCP 支持）压缩中间层空间。
- 企业单中 Composio 的 VPC/on-prem + SOC 2 Type II 对 QVeris"核心引擎托管、无自托管"形成实打实的落差。

---

## 5. Composio 情报核实与修订记录（2026-08-11）

### 5.1 事实修正表（相对旧版表述）

| 项目 | 旧版表述 | 核实结果 |
|------|---------|---------|
| 工具规模 | 850–1,000+ 工具包 | 官方口径统一为 **1,000+ 工具包 / 500+ 应用 / 20,000+ tools**（约 982 toolkits） |
| MCP | 500+ 托管 MCP server | 架构换代：**Tool Router 已 GA**，`mcp.composio.dev` 完全弃用，Rube 并入主 SDK；现在是"单一网关端点"而非"一堆 MCP server" |
| 融资/公司 | $29M，Lightspeed 领投 A 轮 $25M | 正确。补充：Together Fund $4M 种子；主体 Sampark Inc（YC W24）；约 65 名员工（2026-05，1 月为 57） |
| 营收 | ARR 七位数 | 更具体：2025 年中约 $2M 收入、200+ 付费客户 |
| 开源 | 工具封闭源码 | 主仓库 ComposioHQ/composio 约 29.5k stars / 4.5k forks、MIT，SDK 开源；托管运行时/工具实现闭源——改述为"**SDK 开源、托管层闭源**" |
| 安全事件 | 曾有安全事件记录 | 仍成立但须注明已修复：2026-07 做了 SSRF-safe URL 上传、遥测脱敏等加固 |

### 5.2 Composio 定价（精确化，以官方为准）

| 方案 | 价格 | 标准调用/月 | Pro 调用/月 | 超额单价 |
|------|------|-----------|------------|---------|
| Hobby / Totally Free | $0 | 20K | 1K | — |
| Growth / Ridiculously Cheap | $29/月 | 200K | 5K | $0.299 / 1K（Pro $0.897） |
| Scale / Serious Business | $229/月 | 2M | 50K | $0.249 / 1K（Pro $0.747） |
| Enterprise | 定制 | 弹性 | 弹性 | VPC/on-prem、SOC 2、SLA |

> **Pro tools 概念**：搜索 API（Composio Search / Perplexity / Exa / SerpAPI）、代码沙箱（E2B）、ML 推理、OCR/文档解析、爬虫——约 3 倍计价。对场景表 2 关键：Composio 已向"跨类别能力"扩展，不再只是 SaaS 操作；"金融数据纵深"仍是壁垒，但"数据/API 能力 vs SaaS 操作"二分法正在被侵蚀（Threats 已有实证支撑）。

### 5.3 Semrush 数据（us 库，与 SimilarWeb 口径并列而非替换）

- 自然关键词 7,612 个，模型化自然流量约 **11,000/月**（仅 Google 自然、美国库，是下限；SimilarWeb 的 100–170 万是全渠道全球访问量，两者不冲突）。
- 品牌词 `composio` 月搜 18,100、排名第 1。
- **内容策略值得关注**：流量最高的页面不是产品页，而是对比型技术长文——`claude-code-vs-openai-codex`（单页吃掉 "codex vs claude code" 8,100/mo + "claude code vs codex" 4,400/mo 的 Top3）、`claude-code-vs-open-code`、`claude-agents-sdk-vs-openai-agents-sdk-vs-google-adk`，全部位于 `/content/` 栏目。
- **对 QVeris 直接相关**：`docs.composio.dev/toolkits/polygon_io` 排到 "polygon.io"（3,600/mo）第 4 位——Composio 正用 toolkit 文档页截流金融数据 API 品牌词，这正是 QVeris `fmp-vs-polygon-io` 那批页面的战场。

### 5.4 三条修订建议及执行状态

1. **2.1 节"劣势：集成深度到 tool call 为止（无 syncs/webhooks）"已下调**——RightAIChoice 明确提到 Composio 有 real-time event triggers，triggers/webhooks 已是卖点。✅ 已从本文移除，后续对比页不得再写此条。
2. **场景表 2"用户授权操作 ✅ 强项"已配护城河注记**（Sessions + 托管 OAuth + SOC 2 Type II + VPC/on-prem）；自托管行改为 Enterprise VPC/on-prem。✅ 已更新。Weaknesses"自托管缺失"已标注为企业单落差。
3. **QVeris 差异化叙事收窄到三点**（其余易被追平）：
   - Inspect / Probe 的调用前质量信号（成功率/延迟/成本 + 零成本预验证）；
   - 多 Provider failover；
   - 金融六域纵深 + Application Center。
   - **工具数量不再打牌**：10,000+ 能力 vs 20,000+ tools 已不占优，对比页中避免纯数字对比。

---

## 6. 相邻竞品与观察名单（2026-08-11 核查，全部保留）

> 定位：一般不写入对比页正文（与 QVeris 直接对位度低于 §2 竞品），但纳入跟踪——尤其是品牌词截流与融资动态。各项事实已按 2026-08-11 检索核实。

### 6.1 Agent 工具/集成层（App 连接与授权）

| 竞品 | 定位 | 关键事实（2026-08-11 核实） | 与 QVeris 关系 |
|------|------|---------------------------|---------------|
| **Zapier MCP** | 无代码 AI Agent 连接层（9,000+ apps / 40,000+ actions） | SOC 2 Type II；动态工具发现；每次 tool call 消耗 2 tasks；无代码治理（账号级权限/审计） | 工具层"平台内建"代表——占位用户授权 SaaS 操作，与 QVeris 数据侧互补不冲突 |
| **Pipedream** | 开发者集成与工作流平台 | **已被 Workday 收购**（2025-11-19 宣布，2026-01-31 完成，条款未披露）；累计 $22.4M；5,000+ 客户；Conduit（AI connector gateway）+ Connect + MCP server（3,000+ apps / 10,000+ tools）；11.4k+ GitHub stars | 验证 agent-to-SaaS 基建是企业战略资产；归入 Workday 后中立性存疑，对独立开发者吸引力下降 |
| **Merge（Agent Handler）** | 统一 API + Agent 工具调用（MCP） | Agent Handler 2025-10 上线（与 Unified API 分开销售）；统一 API 250+ providers（HRIS/ATS/CRM/accounting 等）；累计约 $74.5M；定价 $650/月 10 linked accounts + $65/account | 偏企业 HRIS/CRM 场景工具调用，金融数据缺失；与 QVeris 交集有限 |
| **Arcade.dev** | Agent 安全动作层 / 授权运行时 | **累计 $72M**（$60M Series A 2026-06，SYN Ventures 领投 + Morgan Stanley/Wipro 战略；$12M seed 2025）；**编写 MCP authorization 规范并被 Anthropic 采纳**；8,000+ MCP tools；用户级 OAuth 委托；tool call 量 25x/6 个月；生产客户含美国头部银行、Prosus、LangChain | 占位"企业 Agent 授权/治理"心智，非数据竞品；但其 MCP 规范话语权会放大工具层"合规叙事"压力 |
| **Paragon** | 嵌入式集成平台（embedded iPaaS） | **$13M Series A**（2022-07，Inspired Capital 领投，累计当时 $16.5M）✅ 与用户清单一致；2024-10 $5.5M Series A-II，累计约 $21.15M；YC W20；130+ connectors；ActionKit/Managed Sync；SOC 2 + airgapped/自托管 | 面向 SaaS 产品内嵌集成的 B2B 场景，与 QVeris 无直接竞争；关注其 AI 用例部署（self-host/forward-deploy） |
| **LlamaIndex（含 LlamaParse）** | 开源 AI 数据框架（RAG / agentic document workflows） | 累计 $27.5M（2025-03 $19M Series A，Norwest 领投，估值约 $93M；Databricks/KPMG 战略投资）；40k+ GitHub stars、300 万+ 月下载；LlamaParse 主打 PDF/表格等非结构化文档解析（GA）；LlamaCloud | 与 QVeris 重叠仅在"文档解析"能力点（QVeris PDF 3–10 credits/页）；本质是 Agent 构建框架而非数据/能力平台，互补多于竞争 |

### 6.2 金融数据/研究层（数据源与内容平台）

| 竞品 | 定位 | 关键事实（2026-08-11 核实） | 与 QVeris 关系 |
|------|------|---------------------------|---------------|
| **Benzinga** | 财经媒体 + 专业行情平台（to B + to C） | 双产品：Benzinga Pro（$37–$197/月，交易者终端，含 Benzinga AI）+ Benzinga APIs（News/Market/Company Data，sales-gated 报价，News API 有免费 Basic 层）；实时低延迟 news 为差异化卖点 | 在"金融数据/新闻 API"维度与 QVeris 部分重叠；品牌流量高，属数据源型竞品，无 Agent 协议层 |
| **Quiver Quantitative** | 另类数据与零售投资研究平台 | 2020 成立（Kardatzke 兄弟）；累计约 $2.5–2.63M（2022-03 $2M Series A，Allos Ventures 领投）；Quiver API $25/月 + **Quiver MCP**；另类数据集：国会交易/内幕/政府合同/WSB 情绪等；2026-07 与 New Constructs 合作上线评级数据（$199/月） | 与 QVeris"Alternative Signals"金融域直接重叠，且已提供 MCP——是六域纵深中最可能正面撞上的单点竞品 |
| **AlphaSense** | 企业级市场情报平台 | 2026-06 G 轮 **$350M，估值 $75 亿**（较 $4B 近翻倍），累计 $1B+；**ARR $600M+**（Q1 2026）；5 亿+ 文档内容库（研报/财报电话会/专家访谈/filings）；7,500 客户（90% S&P 100）；SuperAnalyst 常驻 agent | 企业级研究平台（订阅制、非 API/按次），价格与客群完全不同；但"AI 研究 + Agent 执行"叙事（SuperAnalyst）与 QVeris Application Center 上层重合，值得跟踪 |
| **BridgeWise** | AI 金融研究平台（B2B2C，面向券商/交易所/财富机构） | 2019 成立（Tel Aviv）；累计约 $41.5M（2024-04 $21M，SIX Group 领投，累计当时 $35M）；90% 全球上市证券覆盖、22 语言、5 万+ 股票 ML 评分；Bridget™ LLM chat、pAI wealth agent、SignalWise；客户含 Rakuten Securities、SIX 系 | 研究内容/财富端产品，非数据 API；与 QVeris 无直接竞争，但"AI 生成个股分析"叙事与 Application Center 有概念重叠 |

---

*Last updated 2026-08-11 · 数据来源：QVeris vs 竞品对比页（qveris.ai 2026-08-05）、dreaming.press / alatirok / respan / RightAIChoice 等第三方评测（2026-06~08，含 Composio triggers/webhooks 确认）、Nango 博客（2026-04）；流量数据为 Semrush/SimilarWeb 估算（2026-06）与 Semrush us 库（2026-08-11，自然流量下限口径，与全渠道全球访问量并列），融资与营收数据来自官方公告 / Press release（2025-07~2026-04）及 Composio 官网定价页（2026-08-11）；候选竞品核查（2026-08-11）：fiscal.ai 官方与 docs、financialdatasets.ai 官方与定价、openbb.co 与 GitHub、zapier.com/mcp、pipedream.com 与 PitchBook/Workday 公告、merge.dev、arcade.dev（$72M Series A）、useparagon.com 与 CB Insights/Forbes、llamaindex.ai（$27.5M，$19M Series A）、benzinga.com/pro、quiverquant.com（$2.63M）与 Neudata、alpha-sense.com Press（$350M @ $7.5B，$600M ARR）、bridgewise.com 与 PRNewswire（$41.5M）*
