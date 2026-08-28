# Web 抓取工具谱系（HTTP / 浏览器 / 编排 / 托管 API）· 知识块（非线性笔记）

**材料范围**：从 [`seo/crawler.md`](../seo/crawler.md) 迁出的 **Crawl / Scrape 辨析、无头自动化栈、SEO 工具爬虫** 等段落；并补充 **工具分层**、**代表产品速览（偏商业/托管）**；**AI · Agent** 与 **Web Search API**、**托管抓取**、**训练爬虫** 的分工；IETF **RFC 9309**（robots）、**OWASP OAT-011 Scraping**；官方文档与第三方对比文（ByteTunnels、Scrapfly、DEV Community、Firecrawl 等）。**未**将 Alignify 站内 Tools 正文 JSON 当作事实来源复述。网摘整理 **2026-04-21**。

**与专册分工**：[`seo/crawler.md`](../seo/crawler.md) 侧重 **谁以何种身份访问站点**（搜索引擎 / AI / Agent / 第三方 / 恶意）、UA、robots、验真与观测；**本文**侧重 **数据采集侧** 常见技术栈与产品形态（合规边界仍以站点条款与法域为准）。若目标是**「把单个/批量 URL 变成 LLM 能直接读的 Markdown」**（轻量、API-first、面向 AI 开发者），先看 [web-fetch.md](web-fetch.md)——那是不同于「批量数据管道」的另一采购路径。若需要多步交互（登录、点击、填表），再看 [headless-browser.md](headless-browser.md)。

**与 `/seo/crawler` 的分工**：[`/seo/crawler`](https://alignify.co/zh/seo/crawler) 面向 **站长与入站治理**（日志里是谁、如何配 robots/WAF）；**不**在本知识块复述 GPTBot 全表或「如何验真蜘蛛」教程——需要时请读 crawler 正文或 SEO 知识块 [`crawler.md`](../seo/crawler.md)。**边界总表**见 [knowledgehub README](../README.md) 章节「**Crawler / 网页抓取：内容边界**」。

**站内对照**：[alignify.co/tools/web-scraping](https://alignify.co/tools/web-scraping) · `/zh/tools/web-scraping` · `content/tools/en/web-scraping.md`、`content/tools/zh/web-scraping.md` · **`slug`: `web-scraping`

**知识块文件名**：`web-scraping.md` 与站内 Tools **`slug`：`web-scraping`**、`content/tools/*/web-scraping.md` 对齐（本文为网摘专册，正文 SSOT 以 Tools Markdown 为准）。

以下条目可任意顺序阅读；**不是**文章体例，无叙事主线。

---

## 词汇锚点

- **Web scraping / 网页抓取（刮取）**：用程序 **自动从页面或 API 抽取** 正文、价格、表格、JSON 等；口语常与 **crawling** 混用，技术讨论里 **scraping** 更强调 **解析与抽取**。
- **Crawling / 爬取**：偏 **发现与遍历 URL**、批量下载资源；搜索引擎蜘蛛是典型 crawl-heavy 场景。
- **Crawl 与 Scrape（辨析）**：**Crawl** 强调链路与规模发现；**Scrape** 强调从已获取表示中 **抠数据**；同一流水线可两者兼备。
- **HTTP 层抓取**：`curl`、`wget`、`requests`、`httpx`、`aiohttp` 等；**不执行站点 JavaScript**（除非另接渲染步骤）。
- **TLS / HTTP 指纹**：部分站点用 **JA3、HTTP/2 指纹** 等在边缘区分自动化客户端；社区方案如 **`curl_cffi`** 等常在与反爬相关的第三方文中出现（**非**合规担保）。
- **浏览器自动化**：**Puppeteer**（Chrome DevTools Protocol）、**Playwright**（多引擎、统一 API）、**Selenium**（WebDriver 生态、语言覆盖面广）；用于 **SPA、登录流、需执行 JS** 的抽取。
- **爬虫框架 / 编排**：**Scrapy** 等——管队列、并发、重试、管道；多在 **服务端批量** 场景；可与 **`scrapy-playwright`** 等中间件组合以接入浏览器。
- **解析器（HTML/XML）**：**Beautiful Soup**、**lxml**、**Cheerio**（Node）等，**不负责**发请求或调度全网爬取。
- **托管抓取 API / 代理层**：厂商提供 **取数端点、住宅/数据中心代理、反爬规避**；与「自管 Scrapy」**不是**同一抽象层；第三方博客常以 **「抓取管道分阶段」** 比喻（取回 → 解析 → 编排；见 Scrapfly 类文章）。
- **无代码 / 可视化爬虫**：云端任务、定时、模板字段映射；工程边界与成本模型与脚本不同。
- **AI 辅助抽取**：自然语言描述字段、**自适应页面结构变化**、与 LLM 结合的管线（如 **Firecrawl**、**Crawl4AI** 等）；**维护成本**与**幻觉风险**需在工程上单独评估。
- **Agent 工具型抓取**：编排层（LangChain、LlamaIndex、厂商 Agent SDK）把 **`scrape_url` / `crawl` / `browser`** 暴露为 **function calling**；底层仍落回 HTTP 或浏览器，见下文 **「AI · Agent 与网页抓取」**。
- **SEO 站点审计爬虫**：**Ahrefs、Semrush、Majestic、Screaming Frog SEO Spider、Sitebulb** 等——抓链接、状态码、标题元数据等，**模拟的是可观测抓取**，**不等于**搜索引擎内部渲染与索引口径。
- **与「搜索蜘蛛」区分**：自研或第三方 **scraping** 栈用于商业/运维目的；**Googlebot** 等有其独立 **robots 令牌与验真**（见 [`crawler.md`](../seo/crawler.md)）。

---

## 专题对照 / 扩展定义

| **分层** | **典型职责** | **代表形态（示意）** |
|----------|--------------|----------------------|
| **取回（Fetch）** | HTTP(S) 请求、会话与重试 | 语言 HTTP 库、托管 API |
| **渲染（Render）** | 执行 JS、拿到与用户接近的 DOM | Headless Chromium、Playwright |
| **解析（Parse）** | CSS/XPath/正则、结构化字段 | Beautiful Soup、lxml、服务端解析 |
| **编排（Orchestrate）** | 去重、限速、管道、分布式 | Scrapy、自研队列 |
| **对抗与出口** | 代理、验证码、挑战页 | 商业代理网、打码服务（合规自理） |

| **需求信号** | **常讨论的选型方向（概念层）** |
|--------------|--------------------------------|
| 静态 HTML、无强反爬 | HTTP 库 + 解析器（轻量） |
| 强 JS、前端路由 | 浏览器自动化或托管渲染 |
| 十万级以上同站路径 | 框架级调度 + 限速与去重 |
| 多站点、反爬波动大 | 托管 API 或代理 + 成熟重试策略（成本敏感） |
| Agent 要「证据链 + 正文」 | 先 **Web Search API** 取 URL，再 **抓取/清洗** 管线；或一体化 **search + extract** 供应商（见 [`web-search-api.md`](web-search-api.md)） |

---

## 问题域（为何会出现这类产品）

- **SPAs 与前端框架普及**：仅抓 HTML 源站常缺字段，倒逼 **无头浏览器** 或 **边缘渲染** 方案。
- **反爬与指纹升级**：速率限制、验证码、TLS/HTTP 指纹使「几行 requests」在生产环境常不够；**分层组合**工具成为常见叙述（见第三方「pipeline」模型）。
- **规模与运维成本**：自建 Playwright 集群 vs **云浏览器 API**，常在**并发、冷启动、资金**之间权衡。
- **合规与条款**：抓取公开页未必等于有权用于训练、转售或规避付费墙；**robots 自愿遵守**与 **合同/著作权** 是不同维度。
- **观测混淆**：**SEO 桌面爬虫**报告的「可抓取」与 **真实搜索爬虫**或 **用户所见 DOM** 仍可不一致。

---

## 能力栈（概念拆分，非厂商功能表）

- **判定页面类型**：首屏是否依赖 JS、是否有登录壳、是否有多版本（移动/桌面）。
- **最小可行路径**：能 HTTP 则 HTTP；必须 JS 再上浏览器；避免全站无差别无头（成本与特征）。
- **限速与礼貌**：域名级并发、`Retry-After`、robots（若承诺遵守）；降低对源站的压力与封禁概率。
- **数据契约**：抽取字段 schema、变更告警（站点改版）、稽核抽样。
- **与站点治理协同**：若要 **允许** 自家营销站被抓取用于收录或引用，策略在 **robots / 登录 / CDN 规则** 上配合（见 [`crawler.md`](../seo/crawler.md)）；**自家**对外抓取他站则走合规审查。

---

## 形态谱系（与具体品牌解耦）

- **标准库/脚本级**：单 URL 试验、`curl` + 管道。
- **HTTP 客户端生态**：同步/异步、HTTP/2、连接池；适合高并发 **静态** 或 API JSON。
- **解析与抽取**：HTML/XML 解析、表结构提取、PDF/表格专项工具（与 Web 页抓取相邻但不等同）。
- **大型爬虫框架**：异步引擎、中间件、Item 管道、分布式扩展。
- **浏览器驱动栈**：headed/headless、定位器等待、截图、HAR；常与 **代理池** 组合叙述。
- **云端浏览器 / 抓取 SaaS**：按需浏览器会话、托管 IP、部分集成反爬；与 **自营脚本** 的成本曲线不同。
- **低代码与可视化**：规则配置、定时任务、导出表格；适合非研发主导的监控类需求。
- **AI / LLM 增强**：自然语言到选择器、页面摘要转结构化字段；**需校验**字段级准确率。
- **SEO / 竞品工具**：关键词、外链、站点审核；**产品目标**是营销与技术 SEO，不是通用抓取框架。

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **服务条款与机器人协议**：违反平台 ToS 可能触发封禁或纠纷；**robots.txt** 为自愿约定（[RFC 9309](https://datatracker.ietf.org/doc/html/rfc9309)），**不等于**单独赋予抓取权。
- **版权与数据库权**：批量转载、实质性替代原站点服务的用法，法域差异大。
- **个人信息**：页面中的 PII、用户生成内容，在抓取与存储链路需对齐 GDPR/CCPA/PIPL 等框架。
- **滥用与安全分类**：[OWASP OAT-011 Scraping](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping.html) 将 **自动化批量提取** 列为自动化威胁之一；与撞库、刷票等并列时，属于**安全运营**语境。
- **资源与道德**：过高并发可构成事实上的 **DoS 压力**；工程上应 **限速与退避**。

---

## 落地碎片（无先后）

- **决策树（社区常见归纳）**：「是否需要 JS 渲染？」→ 否则优先 HTTP + 解析；是则 **Playwright / Puppeteer** 等；超大规模同站可考虑 **框架级编排**（第三方文章常给出类似分支，**非**唯一答案）。
- **Scrapy + 浏览器中间件**：仅部分 URL 需 JS 时，用中间件 **按需** 拉起浏览器，避免全站无头开销（概念见 scrapy-playwright 类方案）。
- **「浏览器 ≠ 过反爬」**：多篇第三方文强调 Playwright 等 **控制浏览器**，但 **不是**万能绕过 CDN 挑战；常需 **代理、会话质量、缩频** 组合拳。
- **与 SEO 站点侧**：运营人员用 **Screaming Frog** 等看到的问题，应回到 **GSC、独立样本 URL** 与 **实际Googlebot** 日志对照 [`crawler.md`](../seo/crawler.md) 中的 **报表不可混用** 条目。

---

## 工具与产品类型（「scraper」「crawl」「无头浏览器」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **HTTP + 解析** | 语言 HTTP 客户端 + HTML/XML 解析器 | 静态页、服务端渲染内容 |
| **爬虫框架** | 异步调度、管道、去重、分布式 | 同站大规模；常配代理 |
| **浏览器自动化** | CDP / WebDriver 驱动真浏览器 | SPA、登录、执行 JS |
| **托管抓取 API / Residential proxy** | 代取 HTML、解密挑战、出口 IP | 按次或按 GB；合规与地域选型关键 |
| **低代码 / 云爬虫** | 可视化规则、定时、表格导出 | 非研发场景监控 |
| **AI / LLM 管线** | URL → 清洗 Markdown → chunk；或自然语言定字段 | 与 **Web Search API** 可串行或同厂打包 |
| **SEO 站点审计** | 站内爬模、链接、元数据、Core 指标 | 目标为 **SEO 可观测性**，非通用数据采集 |

---

## 代表产品速览（商业 / 托管为主；各线仅列最知名项；非穷尽）

以下条目为 **谱系锚点**，**不等于**选型推荐；定价与条款以官网为准。**开源栈**（Playwright、Scrapy、Puppeteer、Selenium 等）的官方入口见下文 **「外链索引 → 标准、威胁模型与官方文档」**，本表不重列。

| 名称 | 一句话（据公开材料归纳） | URL |
|------|--------------------------|-----|
| **Bright Data** | 住宅/数据中心代理与 **面向商业的数据采集** 产品线 | [brightdata.com](https://brightdata.com/) |
| **Oxylabs** | 企业代理与 **网页抓取 API** 组合 | [oxylabs.io](https://oxylabs.io/) |
| **Zyte** | 原 **Scrapinghub**；企业采集与合规向叙事 | [zyte.com](https://www.zyte.com/) |
| **Apify** | **云平台** + Actor 市场；托管运行自动化任务 | [apify.com](https://apify.com/) |
| **Octoparse** | **低代码 / 可视化** 抓取（桌面与云） | [octoparse.com](https://www.octoparse.com/) |
| **Firecrawl** | **URL → Markdown/结构化**；云产品与 **LLM·Agent** 集成叙事常见 | [firecrawl.dev](https://www.firecrawl.dev/) |
| **Ahrefs / Semrush** | 两套主流 **SEO SaaS**；均含 **站内爬审计** 类能力 | [ahrefs.com](https://ahrefs.com/) · [semrush.com](https://www.semrush.com/) |

- **补充（仍偏「产品」心智）**：**Screaming Frog SEO Spider** 为桌面 **站内爬模** 代名词级工具（[screamingfrog.co.uk](https://www.screamingfrog.co.uk/seo-spider/)）；**Browserbase**（[browserbase.com](https://www.browserbase.com/)）等 **云浏览器** 常与 **AI Agent** 编排并列。*仅作相邻品类提示，不扩表。*

---

## AI · Agent 与网页抓取（典型接法；非实现教程）

- **与「托管网页检索 API」分工**：多数对话式 / 任务型 Agent 优先用 **Web Search API**（[web-search-api.md](web-search-api.md)）拿到 **已索引的 URL、标题、摘要**，再决定是否 **深入抓正文**——**不是**所有「联网」都等于整站爬取。
- **深读 / 取证链**：当答案需 **整页 Markdown、表格、站内多跳** 时，常见管线是 **Search → 选 URL → `scrape`/`crawl` 工具 → 清洗分块 → RAG**。供应商侧常把 **search + extract + crawl** 打成一个 SKU（如 **Tavily、Exa、Parallel、Firecrawl** 等在公开材料中的叙事，见 [web-search-api.md](web-search-api.md) 供应商表与上文 **Firecrawl** 等一行）；自建则多用 **Playwright** + 自管队列（Playwright 见下文 **外链索引**）。轻量级「给定 URL→返回 Markdown」需求优先评估 [web-fetch.md](web-fetch.md) 中列出的 AI-native fetch 工具；需要代理池、ETL 管道、数据仓库时再回到本文的批量采集栈。
- **工具调用层**：Agent 框架中的 **`browse`**、**`scrape_website`**、**`firecrawl_*`/`crawl`**、**MCP（Playwright、浏览器自动化、第三方抓取 MCP）** 等，语义上都可能触发 **真实 HTTP 或浏览器会话**；计费、超时、并发与 **ToS** 在集成时需单列评估。
- **训练爬虫 vs 在线 Agent**：**GPTBot、Common Crawl、厂商批量爬取** 面向 **语料与索引**，走独立 **User-Agent / robots** 叙事（[crawler.md](../seo/crawler.md)）；**用户会话内点开链接**、**代用户操作浏览器** 常属 **用户触发拉取** 或 **浏览器型 Agent**，验签与 CDN 放行策略不同（如 OpenAI **ChatGPT agent** 与 **RFC 9421**，见 Help），**勿与「自写 scraping 脚本」混谈合规**。
- **何时不一定要 scraping**：仅要 **可引用短摘录** 时，**仅 Web Search API 的 snippet** 即可缩少抓取面；**强反爬或付费墙** 场景强行 headless 往往触及条款与风控，应优先 **官方 API、数据授权、人工导出**。
- **与 [`agent-skills.md`](../agent/agent-skills.md) 的边界**：Agent Skills / MCP 描述的是 **「何时调用何种工具」**；**scrape** 能力若暴露为 MCP 工具，底层仍落回本文所述 HTTP 或浏览器 —— **协议层不与抓取伦理混为一谈**。

---

## 外链索引（检索整理；非广告、无排序优先级）

### 标准、威胁模型与官方文档

- [RFC 9309 — Robots Exclusion Protocol](https://datatracker.ietf.org/doc/html/rfc9309)
- [OWASP — OAT-011 Scraping](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping.html)
- [Playwright 文档](https://playwright.dev/)
- [Puppeteer（Chrome for Developers）](https://developer.chrome.com/docs/puppeteer)
- [Selenium 文档](https://www.selenium.dev/documentation/)
- [Scrapy 文档](https://docs.scrapy.org/)

### 横向对比与架构讨论（第三方）

- [Playwright vs Puppeteer vs Selenium vs Scrapy: The 2026 Mega-Comparison（ByteTunnels）](https://bytetunnels.com/posts/playwright-vs-puppeteer-vs-selenium-vs-scrapy-2026-mega-comparison/)
- [Web Scraping Tools Comparison 2026: requests vs curl_cffi vs Playwright vs Scrapy（DEV Community）](https://dev.to/vhub_systems_ed5641f65d59/web-scraping-tools-comparison-2026-requests-vs-curlcffi-vs-playwright-vs-scrapy-2fad)
- [Best Web Scraping Tools in 2026 — stages of a scraping pipeline（Scrapfly Blog）](https://scrapfly.io/blog/posts/best-web-scraping-tools-in-2026)
- [Best Open-Source Web Scraping Libraries in 2026（Firecrawl Blog）](https://www.firecrawl.dev/blog/best-open-source-web-scraping-libraries) — **含厂商自身产品，阅读时区分陈述与推广**

### 站点与流量治理（与本主题相邻）

- [Introduction to robots.txt（Google Search Central）](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

### 站内索引（Alignify 仓库）

- **站长向 SEO 长文**（谁在访问、UA/robots）：[`/zh/seo/crawler`](https://alignify.co/zh/seo/crawler)、[`/seo/crawler`](https://alignify.co/seo/crawler)；知识块 deeper 笔记：[crawler.md](../seo/crawler.md)
- **采集向 Tools 正文**（与本文 **信息密度 SSOT**）：[`/zh/tools/web-scraping`](https://alignify.co/zh/tools/web-scraping)、[`/tools/web-scraping`](https://alignify.co/tools/web-scraping)
- **搜索引擎流水线**：[how-search-engine-works.md](../seo/how-search-engine-works.md)
- **GEO（AI 答案可见度）**：[geo.md](../search-geo/geo.md)
- **Web Search API 与检索即服务**：[web-search-api.md](web-search-api.md)
- **Web Fetch / URL→Markdown（AI 开发者向）**：[web-fetch.md](web-fetch.md)——与本文批量采集管道的采购路径不同

### 对比与测评（第三方；观点非官方）

英文开发者社区与厂商技术博客里，常见结论是 **不做跨层对比**（例如直接把「Beautiful Soup」与「云抓取 API」比速度），而采用 **「取回 →（可选）渲染 → 解析 → 编排」** 分段选型。横向文章里，**Playwright** 常被选为 **现代多浏览器自动化** 的默认提及对象；**Scrapy** 仍是大规模 **Python 编排** 的代表；**Selenium** 在 **多语言遗留栈与 Grid** 场景持续出现。Python 路线上，**curl_cffi** 等贴近 TLS 客户端指纹的讨论多与 **边缘反爬** 同帖出现，**量产环境**仍需结合法务与平台条款评估。托管与自建之间，第三方文常提醒 **云浏览器会话与按 GB 代理** 的 **边际成本**。*网摘综合、非本站实测。*

---

## 行业注记 · 2026 年网页抓取格局

- **AI Agent 将抓取标准化为 tool calling**：LangChain、OpenAI Agents SDK、MCP 将网页抓取封装为标准工具调用——抓取不再是独立脚本，而是 Agent 推理链中的一环。与传统「写 Scrapy spider + 配代理池」形成代际差异。
- **Firecrawl 和 Crawl4AI 的 LLM 增强**：自然语言描述抓取字段、自适应页面结构变化成为 LLM 增强抓取的标准叙事——维护成本和幻觉风险是尚未解决的工程挑战。
- **robots.txt 合规讨论升级**：RFC 9309 仍为自愿约定，但 AI 训练数据采集引发的版权诉讼（如 NYT v. OpenAI）正在推动「robots.txt 应成为机器可读数据许可协议」的行业讨论。
- **代理层与反爬的军备竞赛**：TLS/HTTP 指纹、验证码挑战持续升级——Bright Data 和 Oxylabs 等商业代理网络与自建 Playwright 集群的成本曲线分化加剧。
- **法律边界持续演变**：hiQ Labs v. LinkedIn 确立美国法下公共数据爬取的有限合法性，但 GDPR/PIPL 的个人数据保护条款使跨境爬取合规成本持续上升。

---

## 延伸阅读与参考材料

- [Google Search Central — Crawling / indexing 文档检索](https://support.google.com/webmasters/search?q=crawl)（站长侧；与「自研抓取」目的不同）
- [Common Crawl](https://commoncrawl.org/)（开放网络语料项目；遵守 robots 的自愿性同属 [`crawler.md`](../seo/crawler.md) 论域）
- [Firecrawl 官方文档](https://docs.firecrawl.dev/)（LLM 增强抓取管道——URL→Markdown/结构化）
- [Crawl4AI 开源项目](https://github.com/unclecode/crawl4ai)（开源 AI 抓取框架，LLM 驱动的自适应字段抽取）
- [Scrapfly Blog · Web Scraping Pipeline 模型](https://scrapfly.io/blog/)（分层抓取管道的行业视角）
- [RFC 9309 — Robots Exclusion Protocol](https://datatracker.ietf.org/doc/html/rfc9309)
