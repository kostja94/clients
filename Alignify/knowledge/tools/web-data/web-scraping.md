# Web 抓取工具谱系（HTTP / 浏览器 / 编排 / 托管 API）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Web scraping / 网页抓取**——程序自动从页面或 API **抽取**结构化数据；与 web-fetch（单 URL→LLM Markdown）、headless-browser（远程可编程浏览器）、web-search-api（程序化找 URL）分属不同采购路径。本页为 **代表产品 + 标准文档 URL 表 SSOT**（完整链接表仅此一处）。

**材料范围**：自 [`seo/crawler.md`](../seo/crawler.md) 迁出的 Crawl/Scrape 辨析、无头栈、SEO 工具爬虫等；IETF RFC 9309、OWASP OAT-011；官方文档与第三方对比文。**未**将 Alignify Tools JSON 当作事实来源。网摘整理 **2026-04-21**。

**与专册分工**：[`seo/crawler.md`](../seo/crawler.md) 侧重**谁以何种身份访问站点**（UA、robots、验真）；**本文**侧重**数据采集侧**技术栈与产品形态。轻量 URL→Markdown → [web-fetch.md](web-fetch.md)；多步交互 → [headless-browser.md](headless-browser.md)。

**站内对照**：[alignify.co/tools/web-scraping](https://alignify.co/tools/web-scraping) · slug **`web-scraping`**

以下条目可任意顺序阅读；**不是**文章体例。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`web-scraping`（本页）** | **`web-fetch`** | **`headless-browser`** | **`/seo/crawler`** |
|------|---------------------------|-----------------|------------------------|---------------------|
| **典型买家问题** | 怎么批量爬取建数据库/监控？ | 怎么把单个 URL 变成 LLM 能读的 Markdown？ | 怎么让 Agent 登录、点击、填表单？ | 日志里是谁在爬我、怎么配 robots？ |
| **交付形态** | SDK、框架、托管 API、代理池 | REST/MCP、一次调用返回 Markdown | CDP 会话、REST 原子操作 | 站长治理、UA/robots 策略 |
| **验收核心** | 吞吐量、成功率、反爬对抗 | Token 节省、Markdown 质量 | 会话持久化、交互稳定性 | 入站治理、验真蜘蛛 |

---

## 词汇锚点

- **Web scraping / 网页抓取**：程序自动抽取正文、价格、表格、JSON 等；口语常与 crawling 混用，技术讨论里 scraping 更强调**解析与抽取**。
- **Crawling / 爬取**：偏发现与遍历 URL、批量下载；搜索引擎蜘蛛是典型 crawl-heavy 场景。
- **Crawl vs Scrape**：Crawl 强调链路与规模发现；Scrape 强调从已获取表示中抠数据——同一流水线可两者兼备。
- **HTTP 层抓取**：requests、httpx、aiohttp 等——**不执行 JS**（除非另接渲染）。
- **TLS / HTTP 指纹**：JA3、HTTP/2 指纹等区分自动化客户端——社区方案如 `curl_cffi`（**非**合规担保）。
- **浏览器自动化**：Puppeteer（CDP）、Playwright、Selenium——用于 SPA、登录流、需执行 JS 的抽取。
- **爬虫框架 / 编排**：Scrapy 等——队列、并发、重试、管道；可与 scrapy-playwright 组合。
- **解析器**：Beautiful Soup、lxml、Cheerio——**不负责**发请求或调度全网爬取。
- **托管抓取 API / 代理层**：取数端点、住宅/数据中心代理、反爬规避——与自管 Scrapy **不是**同一抽象层。
- **AI 辅助抽取**：自然语言定字段、自适应结构变化——Firecrawl、Crawl4AI 等；维护成本与幻觉风险需单独评估。
- **Agent 工具型抓取**：编排层把 `scrape_url` / `crawl` / `browser` 暴露为 function calling——底层仍落 HTTP 或浏览器（见 §AI · Agent 与网页抓取）。
- **SEO 站点审计爬虫**：Ahrefs、Semrush、Screaming Frog 等——**不等于**搜索引擎内部渲染口径。
- **与搜索蜘蛛区分**：Googlebot 等有独立 robots 与验真——见 [`crawler.md`](../seo/crawler.md)。

---

## 专题对照 / 扩展定义

**管道分层**（术语见 §词汇锚点；下表只列职责）：

| **分层** | **典型职责** | **代表形态（示意）** |
|----------|--------------|----------------------|
| **取回（Fetch）** | HTTP(S) 请求、会话与重试 | 语言 HTTP 库、托管 API |
| **渲染（Render）** | 执行 JS、接近用户 DOM | Headless Chromium、Playwright |
| **解析（Parse）** | CSS/XPath/正则、结构化字段 | Beautiful Soup、lxml |
| **编排（Orchestrate）** | 去重、限速、管道、分布式 | Scrapy、自研队列 |
| **对抗与出口** | 代理、验证码、挑战页 | 商业代理网（合规自理） |

**需求信号 → 选型方向（概念层）**

| **需求信号** | **常讨论的选型方向** |
|--------------|----------------------|
| 静态 HTML、无强反爬 | HTTP 库 + 解析器 |
| 强 JS、前端路由 | 浏览器自动化或托管渲染 |
| 十万级以上同站路径 | 框架级调度 + 限速与去重 |
| 多站点、反爬波动大 | 托管 API 或代理 + 重试策略 |
| Agent 要证据链+正文 | Web Search API 取 URL → 抓取/清洗；或 search+extract 一体供应商 |

---

## 问题域（为何会出现这类产品）

- **SPAs 与前端框架普及**：仅抓 HTML 源站常缺字段，倒逼无头浏览器或边缘渲染。
- **反爬与指纹升级**：速率限制、验证码、TLS 指纹使「几行 requests」在生产常不够。
- **规模与运维成本**：自建 Playwright 集群 vs 云浏览器 API——并发、冷启动、资金权衡。
- **合规与条款**：抓取公开页 ≠ 有权用于训练、转售或规避付费墙；robots 与合同/著作权是不同维度。
- **观测混淆**：SEO 桌面爬虫「可抓取」与真实搜索爬虫或用户所见 DOM 仍可不一致。

---

## 能力栈（概念拆分，非厂商功能表）

- **判定页面类型**：是否依赖 JS、是否有登录壳、多版本（移动/桌面）。
- **最小可行路径**：能 HTTP 则 HTTP；必须 JS 再上浏览器；避免全站无差别无头。
- **限速与礼貌**：域名级并发、`Retry-After`、robots（若承诺遵守）。
- **数据契约**：字段 schema、变更告警、稽核抽样。
- **与站点治理协同**：允许自家站被抓取用于收录/引用的策略在 robots/CDN——见 [`crawler.md`](../seo/crawler.md)；对外抓取他站走合规审查。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | 标准库/脚本级 | curl + 管道 |
| **B** | HTTP 客户端生态 | requests、httpx、curl_cffi |
| **C** | 解析与抽取 | Beautiful Soup、lxml |
| **D** | 大型爬虫框架 | Scrapy |
| **E** | 浏览器驱动栈 | Playwright、Puppeteer、Selenium |
| **F** | 云端浏览器 / 抓取 SaaS | Apify、Browserbase（相邻） |
| **G** | 低代码与可视化 | Octoparse |
| **H** | AI / LLM 增强 | Firecrawl、Crawl4AI |
| **I** | SEO / 竞品工具 | Ahrefs、Semrush、Screaming Frog |

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **ToS 与 robots**：违反平台 ToS 可能封禁；[RFC 9309](https://datatracker.ietf.org/doc/html/rfc9309) robots 为自愿约定，**不等于**单独赋予抓取权。
- **版权与数据库权**：批量转载、实质性替代原站服务——法域差异大。
- **个人信息**：PII、UGC 在抓取与存储链路需对齐 GDPR/CCPA/PIPL。
- **滥用分类**：[OWASP OAT-011 Scraping](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping.html)——安全运营语境。
- **资源与道德**：过高并发可构成 DoS 压力——限速与退避。

---

## 落地碎片（无先后）

- 决策树：「是否需要 JS 渲染？」→ 否则 HTTP+解析；是则 Playwright/Puppeteer；超大规模同站 → 框架编排。
- Scrapy + 浏览器中间件：仅部分 URL 需 JS 时按需拉起浏览器。
- 「浏览器 ≠ 过反爬」：常需代理、会话质量、缩频组合拳。
- SEO 站点侧：Screaming Frog 等问题应回 GSC、样本 URL 与实际 Googlebot 日志对照——报表不可混用。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **HTTP + 解析** | HTTP 客户端 + HTML/XML 解析器 | 静态页、SSR |
| **爬虫框架** | 异步调度、管道、去重 | 常配代理 |
| **浏览器自动化** | CDP / WebDriver | SPA、登录 |
| **托管抓取 API / Residential proxy** | 代取 HTML、出口 IP | 按次或按 GB |
| **低代码 / 云爬虫** | 可视化规则、定时导出 | 非研发监控 |
| **AI / LLM 管线** | URL→Markdown→chunk | 可与 Web Search API 串行或同厂 |
| **SEO 站点审计** | 站内爬模、链接、元数据 | 目标 SEO 可观测性 |

---

## AI · Agent 与网页抓取（典型接法；非实现教程）

- **与 Web Search API 分工**：多数 Agent 优先用 [web-search-api.md](web-search-api.md) 拿已索引 URL、标题、摘要，再决定是否深入抓正文——**不是**所有「联网」都等于整站爬取。
- **深读 / 取证链**：Search → 选 URL → scrape/crawl → 清洗分块 → RAG。供应商常把 search+extract+crawl 打成一个 SKU（Tavily、Exa、Parallel、Firecrawl 等，见 §外链索引）。轻量「给定 URL→Markdown」优先 [web-fetch.md](web-fetch.md)；需代理池、ETL、数仓再回到本文批量栈。
- **工具调用层**：`browse`、`scrape_website`、MCP 等语义上可能触发真实 HTTP 或浏览器会话——计费、超时、ToS 需单列评估。
- **训练爬虫 vs 在线 Agent**：GPTBot、Common Crawl 等走独立 UA/robots 叙事（[`crawler.md`](../seo/crawler.md)）；用户会话内点开链接属不同合规语境——**勿与自写 scraping 脚本混谈**。
- **何时不必 scraping**：仅要 snippet 可缩少抓取面；强反爬/付费墙应优先官方 API、数据授权、人工导出。
- **与 [`agent-skills.md`](../agent/agent-skills.md) 边界**：MCP 描述何时调用何种工具；scrape 底层仍落本文 HTTP 或浏览器栈。

---

## 外链索引（产品 + 标准 SSOT；非广告、无排序优先级）

### 代表产品（商业/托管为主；开源栈见下节官方文档）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Bright Data** | 住宅/数据中心代理与商业数据采集 | [brightdata.com](https://brightdata.com/) |
| **Oxylabs** | 企业代理与网页抓取 API | [oxylabs.io](https://oxylabs.io/) |
| **Zyte** | 原 Scrapinghub；企业采集与合规叙事 | [zyte.com](https://www.zyte.com/) |
| **Apify** | 云平台 + Actor 市场 | [apify.com](https://apify.com/) |
| **Octoparse** | 低代码/可视化抓取 | [octoparse.com](https://www.octoparse.com/) |
| **Firecrawl** | URL→Markdown/结构化；LLM·Agent 集成叙事 | [firecrawl.dev](https://www.firecrawl.dev/) |
| **Ahrefs / Semrush** | 主流 SEO SaaS；含站内爬审计 | [ahrefs.com](https://ahrefs.com/) · [semrush.com](https://www.semrush.com/) |
| **Screaming Frog SEO Spider** | 桌面站内爬模代名词级工具 | [screamingfrog.co.uk](https://www.screamingfrog.co.uk/seo-spider/) |
| **Browserbase** | 云浏览器；常与 AI Agent 编排并列 | [browserbase.com](https://www.browserbase.com/) |

### 标准、威胁模型与官方文档

- [RFC 9309 — Robots Exclusion Protocol](https://datatracker.ietf.org/doc/html/rfc9309)
- [OWASP — OAT-011 Scraping](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping.html)
- [Playwright](https://playwright.dev/) · [Puppeteer](https://developer.chrome.com/docs/puppeteer) · [Selenium](https://www.selenium.dev/documentation/) · [Scrapy](https://docs.scrapy.org/)
- [Google · Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Firecrawl 官方文档](https://docs.firecrawl.dev/) · [Crawl4AI](https://github.com/unclecode/crawl4ai)

### 横向对比（第三方）

- [Playwright vs Puppeteer vs Selenium vs Scrapy 2026（ByteTunnels）](https://bytetunnels.com/posts/playwright-vs-puppeteer-vs-selenium-vs-scrapy-2026-mega-comparison/)
- [Web Scraping Tools Comparison 2026（DEV）](https://dev.to/vhub_systems_ed5641f65d59/web-scraping-tools-comparison-2026-requests-vs-curlcffi-vs-playwright-vs-scrapy-2fad)
- [Best Web Scraping Tools 2026 — pipeline stages（Scrapfly）](https://scrapfly.io/blog/posts/best-web-scraping-tools-in-2026)
- [Best Open-Source Libraries 2026（Firecrawl Blog）](https://www.firecrawl.dev/blog/best-open-source-web-scraping-libraries)——含厂商推广，阅读时区分

### 对比与测评（第三方；观点非官方）

英文社区共识：**不做跨层对比**（如 Beautiful Soup vs 云抓取 API），而按「取回→（可选）渲染→解析→编排」分段选型。Playwright 常为现代多浏览器自动化默认提及；Scrapy 仍是大规模 Python 编排代表；curl_cffi 多与边缘反爬同帖出现——量产环境仍需法务与条款评估。托管 vs 自建：云浏览器会话与按 GB 代理的**边际成本**常被低估。

2026 宏观（不重复 §问题域细节）：Agent 将抓取标准化为 tool calling；Firecrawl/Crawl4AI 的 LLM 增强叙事；robots 合规与版权诉讼推动讨论升级；代理与反爬军备竞赛；hiQ v. LinkedIn 与 GDPR/PIPL 使跨境合规成本上升。

*网摘综合、非本站实测。*

---

## 延伸阅读 · 站内外

**站内**

- 站长向：[`/zh/seo/crawler`](https://alignify.co/zh/seo/crawler) · [crawler.md](../seo/crawler.md)
- Tools 正文 SSOT：[`/zh/tools/web-scraping`](https://alignify.co/zh/tools/web-scraping)
- [how-search-engine-works.md](../seo/how-search-engine-works.md) · [geo.md](../search-geo/geo.md)
- [web-search-api.md](web-search-api.md) · [web-fetch.md](web-fetch.md) · [headless-browser.md](headless-browser.md)

**站外**

- [Google Search Central — Crawling / indexing](https://support.google.com/webmasters/search?q=crawl)
- [Common Crawl](https://commoncrawl.org/)
- [Scrapfly Blog · Pipeline 模型](https://scrapfly.io/blog/)