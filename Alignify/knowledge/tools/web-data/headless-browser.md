# 无头浏览器与云浏览器基础设施（Headless / BaaS / Agent 向）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Headless browser / 云浏览器基础设施**——服务端或 Agent 驱动的 **无头/远程 Chromium 会话**、CDP 连接与 REST 原子任务；验收以 **冷启动、会话持久化、steering/交互稳定性** 为主。本页为 **托管浏览器 + Agent SDK 产品 URL 表 SSOT**（完整规格表仅此一处）；批量抓取管道 → [web-scraping.md](web-scraping.md)；人类向 AI 浏览器 → [`browser.md`](../agent/browser.md)；无交互 URL→Markdown → [web-fetch.md](web-fetch.md)。

**材料范围**：厂商公开站与文档（Browserless、Steel、Browserbase、Stagehand、Browser Use 等）、GitHub [browserbase/stagehand](https://github.com/browserbase/stagehand)、社区与第三方对比文；**未**将 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-04-22**（含 Stagehand 增补）。

**站内对照**：[alignify.co/tools/headless-browser](https://alignify.co/tools/headless-browser) · `/zh/tools/headless-browser` · `content/tools/en/headless-browser.md`、`content/tools/zh/headless-browser.md` · **`slug`：`headless-browser`**

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（[`#headless-browser-tools`](../../keywords/alignify-keywords-tools.md#headless-browser-tools)）

**站内相邻**：[web-scraping.md](web-scraping.md) · [web-fetch.md](web-fetch.md) · [`browser.md`](../agent/browser.md)

以下条目可任意顺序阅读；**不是**文章体例，无叙事主线。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **无头浏览器基础设施**（本页） | **网页抓取全谱**（见 web-scraping） | **AI 浏览器（人类入口）**（见 browser） |
|------|-----------------------------------|-------------------------------------|----------------------------------------|
| 典型读者 | 后端、数据、Agent 工程师 | 采集、SEO、数据产品 | 知识工作者、一般网民 |
| 核心抽象 | 会话、CDP、连接串、REST 原子任务 | fetch → render → parse → orchestrate | 标签页、对话、摘要、半自动操作 |
| 代表关键词 | headless browser, cloud browser, BaaS, puppeteer connect | web scraping, crawlers, proxies | AI browser, agentic browsing |

---

## 词汇锚点

- **Headless browser / 无头浏览器**：无可见 UI（或最小 UI）的浏览器实例，用于自动化测试、渲染后取 DOM、PDF/截图；常见内核为 Chromium / Chrome。
- **CDP（Chrome DevTools Protocol）**：调试与自动化底层协议；**puppeteer.connect / playwright.connect** 连接云端或局域网已启动浏览器——BaaS 典型集成方式。
- **Browsers as a Service（BaaS）**：托管方维护浏览器池，客户端改连接串即可跑现有脚本。
- **Headless browser API / 浏览器会话 API**：HTTP 创建会话、WebSocket 驱动、或单次 REST（截图、PDF、scrape）。
- **Agent browser / browser for agents**：LLM 或 Agent 运行时把「打开 URL、点击、填表」当作 tool；与 [`browser.md`](../agent/browser.md) 的「人类 AI 浏览器」相邻但买家与合规语境不同。
- **Stagehand**：Browserbase 主推的开源（MIT）浏览器 Agent SDK——四类原语 **`act()` / `extract()` / `observe()` / `agent()`**；TS + Python；本地 Chromium 或接 Browserbase 云浏览器（规格见 §外链索引）。
- **Browser Use（browser-use）**：开源 Python Agent 库，常用 Playwright；与 Steel、Browserbase 等常出现在同一篇教程。
- **自然语言动作 vs 选择器脚本**：Stagehand 类方案在 DOM 改版时可能比纯选择器少断流，但每步依赖 LLM 推理——带来延迟、单价与可复现性新约束。
- **轻量级非 Chromium 引擎（Lightpanda）**：Zig + V8、CDP 兼容、移除图形管线换速度/内存；**不做截图/PDF**、部分 SPA 兼容性不如完整 Chromium（基准与许可见 §外链索引 **Lightpanda**）。

---

## 专题对照 / 扩展定义

**层级分工**（术语见 §词汇锚点；下表只列职责差，不重复定义）：

| 层级 | **典型职责** | **常见接口形态** |
|------|--------------|------------------|
| **库（本地）** | 启动或连接浏览器、写自动化脚本 | Playwright、Puppeteer、Selenium |
| **托管 BaaS** | 浏览器池、区域、重连、部分反爬 | `wss://...` 连接、控制台配额 |
| **REST 原子 API** | 单次截图、PDF、结构化 scrape | POST `/screenshot`、`/scrape` 等 |
| **Agent 平台** | Search/Fetch/会话与模型编排同一账单 | 统一 API key、Functions 等 |
| **浏览器 Agent SDK** | 自然语言原语 + 仍可用底层 page/CDP | Stagehand 等；叠在 Playwright 与 BaaS 之上 |
| **开源自托管** | Docker 跑 Steel Browser 等 | 私有部署、与云混合 |
| **轻量替代引擎** | 非 Chromium、CDP 兼容 | Lightpanda——高量抓取/Agent 管道；规格见 §外链索引 |

---

## 问题域（为何会出现这类产品）

- **运维 Chromium 痛苦**：内存、版本、补丁、并发隔离；团队愿买托管换稳定取数或稳定 E2E。
- **弹性与冷启动**：促销、批处理、Agent 突发调用需要秒级起会话与清晰限额。
- **反爬现实**：仅换 User-Agent 不够；托管层叠代理、挑战处理的叙事常见（效果因站而异）。
- **AI 产品要「真网页」**：Search API 只有摘要时，管线需渲染后正文或多步 UI；推动 Agent + 浏览器组合。
- **合规与数据驻留**：金融、医疗等客户筛选区域、VPC、自托管与日志留存策略。

---

## 能力栈（概念拆分，非厂商功能表）

- **连接模式**：`launch` 本地 vs `connect` 远程；CI 与云函数与长会话选型不同。
- **有头 vs 无头**：调试时常 headed；生产 headless；部分流将无头用于截图仍遇字体/时区差异。
- **会话生命周期**：创建、复用、`release`、超时；泄漏会话等于烧钱与占配额。
- **与编排集成**：队列、重试、死信；Agent tool 层限流，避免模型循环放大请求。
- **可观测性**：录屏、HAR、实时查看；生产排障依赖供应商仪表盘或自建日志。
- **与抓取栈衔接**：远程浏览器解决 JS 渲染；结构化字段传统上依赖选择器维护（见 [web-scraping.md](web-scraping.md)）。**Stagehand `extract()`** 等路径把部分「找字段」交给模型，但验收、稽核与成本仍要工程化。
- **LLM 原语的可观测性**：Browserbase Session Inspector 可查看 Stagehand 相关决策（以当前控制台为准）；生产需约定日志、重放与失败样本留存。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 纯自管：自建 VM/K8s 跑 Chrome | self-hosted headless | — |
| **B** | 托管 BaaS + 现有脚本改 `connect` | cloud browser, BaaS | Browserless、Steel |
| **C** | REST 优先、无状态短任务 | headless browser API | Steel REST、Browserless REST |
| **D** | Agent 向全栈：会话 + fetch/search + 云函数 | browser for agents | Browserbase、Hyperbrowser |
| **E** | Stagehand 式「脚本 + 提示」原语层 | browser agent SDK | Stagehand、Browser Use |
| **F** | 非 Chromium 轻量 CDP 引擎 | lightweight headless engine | Lightpanda |
| **G** | 开源核心 + 商业云 | open-source browser API | Steel、Lightpanda（AGPL 需注意商用） |

**B vs D**：体验均可「远程浏览器」，B 偏现有 Playwright/Puppeteer 脚本最小改动；D 偏 Agent 编排与统一账单——媒体对照见 §外链索引「对比与测评」。

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **目标站 ToS**：自动化、批量访问可能违约；**技术可行 ≠ 权利许可**。
- **个人信息与日志**：页面含 PII 时，留存与跨境需对齐 DPA；会话录像敏感。
- **供应链**：浏览器大版本升级可导致选择器静默失效；引入 LLM 解析 DOM 后还需监控模型升级、提示漂移。
- **成本失控**：按分钟/按请求计费 + 高并发 Agent 易超预算；需硬上限与告警。
- **供应商锁定**：连接协议虽基于 CDP，增值能力（unblock、区域）切换有迁移成本。

---

## 落地碎片（无先后）

- 先证明必须 JS 渲染再上云浏览器；能用 HTTP+API JSON 则不必上全浏览器。
- POC 用最难的 5 个 URL，再看成功率与单价，避免 demo 站代表生产。
- Agent 场景为 `fetch_url` / `browse` 配 allowlist、每域 QPS、总步数上限。
- 关键词策略：**slug 用 `headless-browser`**；正文覆盖 cloud browser、BaaS、agent browser 等同意图短语。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **托管 BaaS** | WebSocket 连 Chromium、会话管理 | 与 Puppeteer/Playwright 脚本最小改动 |
| **REST 浏览器 API** | 单次 scrape、截图、PDF | 复杂多步仍落回长会话或 `/function` |
| **Agent 向浏览器平台** | 会话 + fetch/search + 云函数 | 与 LLM 产品捆绑叙事强 |
| **浏览器 Agent SDK** | `act` / `extract` / `observe` / `agent` | 编排层；产品见 §外链索引 |
| **轻量级替代引擎** | 非 Chromium、CDP 兼容 | Lightpanda；混合架构「轻量优先 + Chrome 兜底」 |
| **本地 Agent 库** | browser-use 等 | **库 ≠ 浏览器**；需自备或购买远程浏览器 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Browserless** | 托管浏览器、BaaS、REST API、BrowserQL 等 | [browserless.io](https://www.browserless.io/) |
| **Steel** | 开源浏览器 API + 云；Sessions、Puppeteer/Playwright 连接 | [steel.dev](https://www.steel.dev/) |
| **Browserbase** | Agent 向平台：云浏览器、Fetch/Search、Functions、Stagehand 集成 | [browserbase.com](https://www.browserbase.com/) · [Stagehand 落地页](https://www.browserbase.com/stagehand) |
| **Stagehand** | 开源（MIT）浏览器 Agent SDK：`act` / `extract` / `observe` / `agent` | [stagehand.dev](https://www.stagehand.dev/) · [docs](https://docs.stagehand.dev/) · [GitHub](https://github.com/browserbase/stagehand) |
| **Browser Use** | 开源 Python Agent 库（Playwright）；可选云 | [browser-use.com](https://browser-use.com/) · [GitHub](https://github.com/browser-use/browser-use) |
| **Hyperbrowser** | AI-first 云端浏览器；HyperAgent、MCP、Ultra Stealth | [hyperbrowser.ai](https://hyperbrowser.ai/) |
| **Browserbeam** | LLM 优化浏览器 API——Markdown + 交互引用；声明式提取 | [browserbeam.com](https://browserbeam.com/) |
| **Kernel** | 云端浏览器，速度优化针对 AI workload | [kernel.dev](https://kernel.dev/) |
| **Rusty Browser** | Rust 分布式 browser agent 集群；WebDriver BiDi | [github.com/dashn9/rusty-browser](https://github.com/dashn9/rusty-browser) |
| **Lightpanda** | 开源（AGPL-3.0）轻量无头浏览器：Zig + V8、CDP 兼容；无图形渲染 | [lightpanda.io](https://lightpanda.io/) · [GitHub](https://github.com/lightpanda-io/browser) |
| **Bright Data Agent Browser** | 基于代理网络的云端浏览器；MCP/n8n/LangChain 集成 | [brightdata.com](https://brightdata.com/) |
| **Playwright** | 微软主导的多浏览器自动化框架 | [playwright.dev](https://playwright.dev/) |
| **Puppeteer** | Chrome/CDP 生态常用库 | [pptr.dev](https://pptr.dev/) |
| **Cloudflare Browser Run** | 边缘 CDP 会话，面向 Agent（2026-04） | [blog.cloudflare.com/browser-run-for-ai-agents](https://blog.cloudflare.com/browser-run-for-ai-agents/) |

### 对比与测评（第三方；观点非官方）

英文社区常把 **Browserless、Steel、Browserbase** 放在「不想自己养 Chrome」的同一决策里——比较冷启动、会话时长上限、`connect` 改造成本、REST 是否够用、Agent 范例是否丰富。**browser-use** 与 **Stagehand** 常被归为编排层：底层仍是 Playwright/Chromium 或托管会话；Stagehand 更强调逐步原语与纯黑盒 agent 的折中。DEV 上 Browserbase + Stagehand + Cloudflare Workers 复盘暴露运行时兼容问题——集成风险而非产品官宣。

**Cloudflare Browser Run** 等云厂商入局后叙事偏向「给 Agent 的浏览器」与 MCP/CDP。**不宜**把「无头浏览器 API」与「网页抓取托管 API（偏 HTTP/提取）」混为同一验收标准——前者重交互与渲染会话，后者重字段 schema 与提取 SLA。

2026 新变量：**非 Chromium 轻量引擎**（Lightpanda）——基准称比 Chrome 快 9–11×、内存少 9–16×，支持 `puppeteer.connect` / `playwright.connectOverCDP` 零改动接入；代价是无截图/PDF、部分 SPA 兼容性、AGPL 商用授权。高量抽取与 Agent 工具调用场景下 **Lightpanda 优先 + Chrome 兜底** 的混合架构正在出现。

*本小节为网摘与行业观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **Browserless · BaaS 文档**：WebSocket 连接、BaaS vs REST vs BrowserQL — [docs.browserless.io/baas/start](https://docs.browserless.io/baas/start)
- **Browserbase · Stagehand Quickstart** — [docs.browserbase.com/welcome/quickstarts/stagehand](https://docs.browserbase.com/welcome/quickstarts/stagehand)
- **DEV Community（第三方复盘）**：Browserbase + Stagehand + Cloudflare Workers — [dev.to/...](https://dev.to/whateverneveranywhere/how-i-built-an-ai-that-applies-to-jobs-with-browserbase-stagehand-and-cloudflare-workers-1h0f)

**站内**

- 抓取全谱：[web-scraping.md](web-scraping.md) · 正式页 <https://alignify.co/tools/web-scraping>
- 无交互取内容：[web-fetch.md](web-fetch.md)
- 人类向 AI 浏览器：[`browser.md`](../agent/browser.md)