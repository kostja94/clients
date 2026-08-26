# 爬虫谱系与流量形态（全网摘 · 搜索引擎 / AI / Agent / 第三方 / 恶意）· 知识块（非线性笔记）

**材料范围**：Google / Bing / Yandex / Baidu / Apple / OpenAI / Anthropic 等公开文档中对 **User-Agent、robots、爬虫用途、验真方法** 的说明；IETF **RFC 9421**（HTTP Message Signatures）、**RFC 9309**（Robots Exclusion Protocol）等标准页；OpenAI Help（**ChatGPT agent** 验签与 CDN 放行）；Cloudflare、F5 Labs、Imperva 等对 **自动化流量、坏机器人、抓取类威胁** 的公开材料；独立开发者博客与 SEO 行业对 **AI 爬虫、robots.txt、流量识别** 的讨论。**未**将 Alignify 站内页面 JSON 当作事实来源复述。网摘整理 **2026-04-21**；**2026-04-21** 起做「全网摘」扩写，仍**非**穷尽清单——新 UA/新产品会持续出现，以各运营方最新文档为准。

**规范对照**：[section-seo.md](../../skills/create-article/rules/meta.md) · [technical/README.md](../../skills/ops/README.md) · 本分册说明：[seo/README.md](./README.md) · 经典三阶段流水线：[how-search-engine-works.md](./how-search-engine-works.md)

**与 `/seo/crawler`、Tools 页的分工**：用户向的 **站长指南** 正文在 **`/seo/crawler`**（及中文）；本知识块为**网摘笔记**（UA 表、外链、碎片），**不**与 `content/seo/*/crawler.md` 逐段同步。若读者站在**数据采集方**（代理、Playwright、托管 API），请参阅 Tools **`/tools/web-scraping`** 与知识块 **[`web-scraping.md`](../tools/web-scraping.md)**；本文件**不**展开厂商选型八条。

以下条目可任意顺序阅读；**不是**文章体例。文中「爬虫 / 机器人 / bot / 抓取器」在 HTTP 语境下常互通；**Crawl（爬取）** 与 **Scrape（抓取/刮取）** 的辨析见 **词汇锚点**。**合规与可识别性**以各运营方文档为准。**User-Agent 可被伪造**，安全与运维侧需结合 **反向 DNS、IP 段、ASN、TLS/JA3、行为与会话、HTTP 签名** 等综合判断。

---

**词汇锚点**

### 协议、爬取与索引

- **Robots Exclusion Protocol / robots.txt**：站点根目录的纯文本声明，告知爬虫**哪些路径不宜抓取**；**自愿遵守**，不是强制 ACL（见 [RFC 9309](https://datatracker.ietf.org/doc/html/rfc9309) 与 [Google 对 robots 的说明](https://developers.google.com/search/docs/crawling-indexing/robots/intro)）。
- **Crawling / 爬取**：下载 URL 资源；**不等于**收录。口语里常强调 **顺着链接大量发现页面**、持续访问（如搜索引擎蜘蛛）。
- **Scraping / Web scraping（抓取、刮取）**：用程序 **自动从页面或 API 抽取数据**；与 **Crawl** 的辨析、**HTTP/浏览器/编排工具栈**、SEO 审计爬虫与 **自研抓取管线** 的分工见专册 **[`tools/web-scraping.md`](../tools/web-scraping.md)**（本站知识块；**非**穷尽工具清单）。
- **Indexing / 索引**：处理内容并可能纳入索引库；被 robots **禁止抓取**的页面仍可能以「仅 URL」等形式出现在搜索结果中（Google 文档对限制的说明）。
- **Serving / 呈现**：查询时组装 SERP；与爬取、索引是不同环节（见 [how-search-engine-works.md](./how-search-engine-works.md)）。
- **User-agent token（robots 内）**：`User-agent:` 行使用的**令牌**（如 `Googlebot`），与 HTTP 请求头里的完整 **User-Agent 字符串**不是同一概念；部分产品（如 **Google-Extended**）在 Google 文档中说明为 **robots 专用令牌**，**HTTP 层可能仍使用既有 Google UA**。
- **Allow / Disallow**：路径前缀规则；具体匹配语义依爬虫实现（Google 有专门说明页）。
- **Crawl-delay**：非标准扩展；部分厂商（如 Anthropic 文档）提及会参考；**Googlebot 不保证按 Crawl-delay 行为**（以 Google 文档为准）。
- **Sitemap**：URL 发现辅助；不替代内链与质量信号。
- **meta robots / `X-Robots-Tag`**：控制**索引/跟随**等（如 `noindex`）；**想禁止收录时**不能仅靠 `Disallow` 而不让爬虫读到 `noindex`（常见坑见 Google robots 文档与 [indexing](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) 类说明）。
- **Canonical**：重复 URL 聚合信号；与 robots 分工不同。

### 身份、观测与流量口径

- **Crawler / Bot / Spider / Robot**：自动拉取 HTTP 资源的程序；口语常混用。
- **Fetcher**：偏「单次代取」或用户触发的抓取；Google 文档区分 **user-triggered fetchers**。
- **User-Agent（HTTP 头）**：客户端自报身份；**可伪造**。
- **Verified Bot / 已验证机器人**：CDN/WAF 厂商维护的**高置信度**分类（依赖厂商实现）；用于**放行或策略分层**，不等于法律上「授权」。
- **爬虫流量 / 自动化流量 / Bot traffic**：日志或边缘网络上识别为**非真人浏览器会话**的请求集合；与 **GSC 中「抓取」**、与 **GA 中「自然搜索会话」** 口径**不一致**，不可直接加减对齐。
- **Good bot / Bad bot**：安全行业标签；**坏 bot** 含撞库、薅羊毛、恶意抓取、漏洞扫描等。**好/坏**不等于「是否遵守你站的商业条款」——**合法爬虫**也可能被你站策略禁止。

### 搜索引擎与商业产品线（概念）

- **Googlebot**：Google 搜索主爬取；含移动/桌面等；**移动优先索引**下多数请求来自移动 UA（见 [What is Googlebot](https://support.google.com/webmasters/answer/182072)）。
- **Google-Extended**：**robots 令牌**，用于控制内容是否用于 **Gemini 等模型相关用途**；Google 文档说明 **不影响 Google 搜索收录本身**（见 [Google common crawlers — Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)）。
- **Special-case crawlers / AdsBot**：对 `User-agent: *` 等规则可能有**例外**（与广告/发布商约定相关）；见 [Overview of Google crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers)。
- **bingbot / AdIdxBot / Preview 类**：微软搜索、广告、快照/预览等；见 [Which crawlers does Bing use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)。
- **Applebot**：苹果搜索等；**iTMS** 等为独立 UA，**未必**按通用 Applebot robots 规则（见 [About Applebot](https://support.apple.com/en-us/119829)）。
- **YandexBot** 等：Yandex 有多款机器人；验真强调 **反向 DNS**（见 [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)）。
- **Baiduspider** 及变体：百度多产品线 UA；验真 **host 反查**（见 [百度搜索资源平台 / Baiduspider 介绍](https://ziyuan.baidu.com/college/articleinfo?id=34) 等）。

### AI、训练与检索

- **AI 爬虫**：为 **模型训练**、**搜索/答案检索**、**预览或安全校验** 等目的访问站点的自动化客户端；UA 与 **robots 令牌** 需对照厂商文档。
- **训练爬虫 vs 检索/搜索爬虫**：例如 OpenAI **GPTBot** vs **OAI-SearchBot**；Anthropic **ClaudeBot** vs **Claude-SearchBot**（见各厂商文档）。
- **用户触发拉取**：如 **ChatGPT-User**；OpenAI 说明 **robots 对自动爬取的规则可能不适用**，且与「是否出现在 Search」管理入口不同（见 [Overview of OpenAI crawlers](https://platform.openai.com/docs/gptbot)）。
- **Common Crawl / CCBot**：开放网络存档项目；站点可通过 robots 对 **CCBot** 等声明（见 [Common Crawl](https://commoncrawl.org/) 与项目说明）。
- **第三方聚合的「AI 爬虫名单」**：社区/工具站维护的 UA 列表便于**起步配置**，**不等价于**官方完备列表，需定期复核。

### Agent 与浏览器自动化

- **Agent 爬虫 / 浏览器型 AI Agent**：多步任务、表单、会话；可能使用**类真机 Chrome** 的 UA；OpenAI **ChatGPT agent** 官方说明用 **RFC 9421** 签名 + **`Signature-Agent: "https://chatgpt.com"`**（见 [ChatGPT agent allowlisting](https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting)）。
- **无头浏览器 / 通用网页抓取栈**（Puppeteer、Playwright、Selenium、Scrapy 等）用于**数据采集与测试**时的工具谱系、分层选型，见 **[`tools/web-scraping.md`](../tools/web-scraping.md)**；本文保留 **UA 可被仿冒**、**与 ChatGPT agent 验签机制不同** 的站位结论。

### 第三方与站内生态

- **SEO 工具爬虫 / 桌面审计爬虫**：链接图、排名监控、站点审计（Ahrefs、Semrush、Majestic、Lighthouse、Screaming Frog 等）的**工具谱系与抓取技术栈辨析**见 **[`tools/web-scraping.md`](../tools/web-scraping.md)**；在本文中的结论不变——**模拟的是「可观测的抓取」**，不等于搜索引擎内部渲染与索引状态。
- **预览/社交爬虫**：为生成链接预览抓取 OG 信息（如 **facebookexternalhit**、**Slackbot**、**Discord**、**Twitterbot**、**LinkedInBot** 等）；频率与缓存策略各异。
- **RSS/聚合阅读器**：按 Feed 拉取；部分仍 HEAD/GET 页面。
- **监控与可用性**：Uptime、Synthetic monitoring；可能从全球 PoP 出流量。
- **学术与档案**：Internet Archive、引文索引、数据集构建；遵守程度与项目使命相关。

### 安全与滥用

- **恶意 / 灰色爬虫**：撞库、凭证填充、库存锁单、虚假互动、高频爬取致 **DoS**、**绕过付费墙/鉴权** 等。
- **OAT-011 Scraping（OWASP 自动化威胁分类）**：以自动化手段**批量提取数据**的一类威胁；常与业务风控、账户安全并列讨论。
- **Scraping 的中性与负面语境**：**中性**时指合规场景下的公开数据抓取、有约定的速率与用途（监控、研究、聚合等）。**负面**时多指违反服务条款、绕过鉴权、大规模盗用内容、撞库等——与「正规爬虫是否被站点欢迎」不是同一维度。
- **Scraper**：常指 **执行 scraping 的程序或脚本**；与 **Crawler** 在命名上可能重叠（一个 bot 既爬又刮）。**技术栈与产品分类**（HTTP 库、框架、浏览器自动化等）见 **[`tools/web-scraping.md`](../tools/web-scraping.md)**。

### 性能与站点侧

- **Crawl budget / 爬取预算**：搜索引擎侧资源分配概念；**低价值 URL 爆炸** 会浪费发现机会（见 crawlability skill）。
- **渲染与 JS**：搜索引擎爬虫可能执行 JS；**其他爬虫未必**——「自己能跑 Lighthouse」不等于「所有 bot 都看到同一 DOM」。
- **国际化**：`hreflang`、地区爬虫（各引擎）、**合规**（数据出境、个人信息）属独立大题，本文仅点题。

---

**专题对照 / 扩展定义**

| **术语（口语辨析）** | **侧重点** |
|---------------------|------------|
| **Crawl / 爬取** | 发现 URL、沿链访问、批量下载资源（常与「索引型爬虫」联想） |
| **Scrape / 抓取（刮取）** | 从页面或 API **解析并抽取**结构化数据；可与 crawl 同属一个自动化流程 |

| **环节** | **典型目标** | **常用抓手（概念层）** |
|----------|--------------|------------------------|
| **可发现** | URL 被蜘蛛知道 | 内链、列表页、sitemap、GSC/Bing Webmaster |
| **可爬取** | 不被 robots/服务器错误误伤 | robots 语法、5xx/429、带宽与限流 |
| **可索引** | 控制是否入库与展现 | `noindex`、`X-Robots-Tag`、canonical、软 404 排查 |
| **可呈现** | SERP/摘要与意图一致 | 标题/描述、结构化数据、体验信号 |

| **声明/机制** | **主要作用** | **常见误区（口语）** |
|---------------|--------------|----------------------|
| **robots.txt `Disallow`** | 限制**抓取路径** | **不是**可靠的「保密」；**不等于**禁止 URL 出现在任何搜索结果形态 |
| **`noindex` / `X-Robots-Tag`** | 倾向控制**索引/展现** | 若页面被 robots 彻底挡到**读不到**标签，反而可能卡住预期 |
| **`Google-Extended`（robots 令牌）** | 与 **Google 搜索收录**解耦的 **AI 用途**控制（见 Google 文档） | 与 HTTP 里看到的 **User-Agent 字符串**不一一对应 |

| **大类** | **典型目的** | **与站长的关系（概念上）** |
|----------|--------------|------------------------|
| **搜索引擎爬虫** | 建索引、呈现自然结果 | 内容 + 技术可爬性 + 规范对照 GSC |
| **AI 相关爬虫** | 训练、检索、预览/安全 | **分令牌/分 UA** 管理；与 GEO 相关：[tools/geo.md](../tools/geo.md) |
| **Agent / 浏览器自动化（厂商）** | 代用户多步操作 | **签名/验真**、边缘 Bot 策略；区别于批量索引爬虫 |
| **第三方合规/半合规爬虫** | SEO、监控、存档、科研 | robots 与速率；过量仍占 **成本** |
| **恶意 / 灰色爬虫** | 盗刷、撞库、薅羊毛、攻击辅助 | WAF、风控、身份与速率；UA **冒充** |

| **令牌 / 代表性 UA（robots 或 HTTP；以厂商最新文档为准）** | **运营方（示意）** | **备注** |
|----------------------------------------------------------|-------------------|----------|
| `Googlebot` | Google | 搜索主爬取 |
| `Google-Extended` | Google | **robots 令牌**；HTTP UA 见 [Google 文档](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) |
| `bingbot` | Microsoft | 与 Edge 渲染版本号演进相关 |
| `Applebot` | Apple | 搜索；另有 **Applebot-Extended** 等叙述见第三方与 Apple 更新 |
| `YandexBot` | Yandex | 多子类机器人 |
| `Baiduspider`（及 image/video/news…） | Baidu | 分产品线 UA |
| `GPTBot` / `OAI-SearchBot` / `ChatGPT-User` / `OAI-AdsBot` | OpenAI | 用途各异；见 [OpenAI crawlers](https://platform.openai.com/docs/gptbot) |
| `ClaudeBot` / `Claude-User` / `Claude-SearchBot` | Anthropic | 见 [Anthropic 帮助中心](https://support.anthropic.com/en/articles/8896518) |
| `Googlebot` + **ChatGPT agent 签名头** | OpenAI | 非单一传统 UA 可概括；见 Help **allowlisting** |
| `PerplexityBot` 等 | 各 AI 搜索产品 | 以厂商说明为准 |
| `CCBot` | Common Crawl | 开放爬虫生态 |
| `Amazonbot` | Amazon | 与 Alexa 等能力相关公开说明见 AWS/Amazon 文档 |

*上表**不是**完整名单；新品牌、新令牌会迭代。*

| **流量视角** | **含义** |
|--------------|----------|
| **服务端爬虫请求占比** | 日志或边缘识别为自动化/特定 UA 的请求比例 |
| **安全报告 bot 占比** | 厂商样本中的自动化 vs 人类；**不可**直接当本站占比 |
| **GSC 抓取统计** | Googlebot 对本站抓取与响应码分布 |

---

**问题域（为何会出现这类产品）**

- **同一 URL 被多类机器人重复请求**：搜索索引、AI 训练/检索、监控、预览、恶意抓取叠加，**成本与排障难度**上升。
- **意图冲突**：要搜索可见度、要 AI 引用、要保护版权与付费内容——需 **分令牌、分路径、分鉴权**，很少能仅凭单一 `Disallow: /` 表达全部意图。
- **识别困难**：UA 伪造、代理、**类真人浏览器** Agent；需 **验签、DNS、IP 列表、行为**。
- **报表混用**：CDN bot 报表、GSC、GA、服务器日志 **四种口径**混谈会产生错误决策。
- **产品迭代快**：新 UA、新「检索 vs 训练」拆分、**验签机制**（RFC 9421）出现——文档需**持续对照官方**。

---

**能力栈（概念拆分，非厂商功能表）**

- **taxonomy**：先分 **搜索引擎 / AI 训练 / AI 检索 / Agent / 第三方工具 / 预览社交 / 恶意**。
- **声明层**：robots、sitemap、meta/`X-Robots-Tag`、（可选）**付费墙与登录**作为真正访问控制。
- **验证层**：搜索引擎官方验真方法；AI 厂商 **IP JSON**；**RFC 9421** 公钥与签名链；CDN **Verified Bot**。
- **观测层**：日志字段（UA、referer、ASN、路径、响应码、延迟）、GSC、Bing/Yandex Webmaster、安全仪表板。
- **治理层**：速率限制、挑战、按路径的 WAF、**业务风控**（登录、支付、库存）。
- **成本与架构**：缓存、源站保护、分离静态与动态；**无限滚动/筛选参数** 导致的 URL 爆炸（见 crawlability）。

---

**形态谱系（与具体品牌解耦）**

- **搜索索引类**：主索引爬虫、图片/新闻/视频垂直爬虫、广告与预览类爬虫。
- **AI 管线类**：训练、搜索索引（AI 搜索）、用户触发拉取、广告落地页校验。
- **Agent 管线类**：多步浏览、会话、脚本执行；验签与 WAF 白名单策略与「传统爬虫」不同。
- **工具与监控类**：SEO 外链与站点审计、排名监控、价格监控、变更检测（工具层细节见 [`tools/web-scraping.md`](../tools/web-scraping.md)）。
- **预览与社交类**：链接 unfurl、消息应用预览。
- **Feed 与聚合类**：RSS/Atom、内容聚合器。
- **档案与科研类**：Web Archive、引文与大规模语料。
- **无头自动化类**：测试脚本、灰产采集、**自研 Agent**（合规性因场景而异；与「站长侧观测到的 bot」的统计口径仍可能不一致）。
- **恶意与对抗类**：OAT-011 类抓取、撞库、刷票、CC、应用层 DDoS。

---

**风险 · 合规 · 工程治理（外部框架可对照，非法律意见）**

- **robots 与法律效力**：行业惯例；违反可导致**合同/侵权/竞争法**争议——视法域与行为。**不是**单独的技术「锁」。
- **版权与数据库权**：训练数据、**实质性摘录**、竞争法下的抓取，需专业法律意见。
- **个人信息与跨境**：日志中的 IP、Cookie、**可识别身份**字段受隐私法约束；**不是**「爬虫主题」能覆盖。
- **误伤**：封 ASN、封「像 bot 的真人」出口 IP、误杀预览爬虫导致**分享体验**下降。
- **第三方 SEO 爬虫 vs 恶意**：多数可沟通、可限频；后者走**安全运营**。

---

**落地碎片（无先后）**

- **Google**：`Google-Extended` 在 robots 中单独声明；与 **Googlebot** 搜索收录关系见 [common crawlers 文档](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)。**AdsBot** 等规则例外见总览页。
- **OpenAI**：**GPTBot** vs **OAI-SearchBot**；**ChatGPT-User** 与 Search 管理入口关系见 [OpenAI crawlers](https://platform.openai.com/docs/gptbot)；**ChatGPT agent** 见 [allowlisting](https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting)。
- **Anthropic**：**ClaudeBot / Claude-User / Claude-SearchBot**；Anthropic 文档提及 **Crawl-delay** 与 robots 合规，**以最新 Help 为准**（[Anthropic 爬取说明](https://support.anthropic.com/en/articles/8896518)）。
- **Apple**：**Applebot** vs **iTMS** 等；后者**不一定**遵循通用搜索爬虫 robots 规则（见 [Applebot](https://support.apple.com/en-us/119829)）。
- **Yandex / Baidu**：强调 **反向 DNS / host 验真**；子机器人列表见各自站长文档（[Yandex 验真](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)、[Baidu 学堂](https://ziyuan.baidu.com/college/articleinfo?id=34)）。
- **Crawl vs Scrape**：日志分析时「爬虫多」未必等于「有人在做 scraping 盗库」——可能是搜索引擎索引、预览、或合规监控；需结合路径、鉴权、响应与业务判断（见上文词汇锚点）。
- **Googlebot 体积**：支持文件类型有 **抓取字节上限**（如 HTML 与 PDF 差异）；异常大页面需工程侧自查（见 [What is Googlebot](https://support.google.com/webmasters/answer/182072)）。
- **「屏蔽 AI」新兴约定**：社区出现 **llms.txt** 等倡议性文件——**不具备** robots 的广泛互操作性前，**视为补充信号而非硬标准**。
- **JS 站点**：若仅服务端渲染给某一类 bot，可能制造**内容与用户不一致**风险（搜索引擎质量政策方向与用户体验）。
- **国际化站点**：`hreflang`、分地区爬虫、**各地法律**分治。

---

**工具与产品类型（数据采集 / 网页抓取栈）**

- **网页抓取**相关的 HTTP 库、浏览器自动化、爬虫框架、托管 API、SEO 审计工具等 **分层与示例**，已迁至 **[`tools/web-scraping.md`](../tools/web-scraping.md)**，避免与本文「访客机器人身份与治理」重复。
- **仍留在本文的相邻品类**：**站长与调试**（**Rich Results Test**、**URL Inspection**（GSC））、**搜索引擎站长工具**（GSC、Bing、Yandex、百度站长等）、**CDN / WAF / Bot Management**、**日志与 SIEM**、**威胁情报**、**第三方 UA 目录**（非官方，需复核）。

---

**外链索引（检索整理；非广告、无排序优先级）**

### 官方与权威参考（协议与搜索引擎）

- [RFC 9309 — Robots Exclusion Protocol](https://datatracker.ietf.org/doc/html/rfc9309)
- [Introduction to robots.txt（Google Search Central）](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [How Google Search works](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Overview of Google crawlers and fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers)
- [Google's common crawlers（含 Google-Extended 说明）](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [What is Googlebot](https://support.google.com/webmasters/answer/182072)
- [Which crawlers does Bing use?](https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0)
- [Using robots.txt（Yandex Webmaster）](https://yandex.com/support/webmaster/en/controlling-robot/robots-txt.html)
- [How to check that a robot belongs to Yandex](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots)
- [About Applebot](https://support.apple.com/en-us/119829)
- [百度 spider 介绍（搜索学堂）](https://ziyuan.baidu.com/college/articleinfo?id=34)
- [Baiduspider / robots 英文帮助页](https://www.baidu.com/search/robots_english.html)

### AI、Agent 与验签

- [Overview of OpenAI crawlers](https://platform.openai.com/docs/gptbot)
- [ChatGPT agent allowlisting（OpenAI Help）](https://help.openai.com/en/articles/11845367-chatgpt-agent-allowlisting)
- [RFC 9421 — HTTP Message Signatures](https://datatracker.ietf.org/doc/html/rfc9421)
- [Anthropic — 爬取与 ClaudeBot 等说明](https://support.anthropic.com/en/articles/8896518)
- [Common Crawl](https://commoncrawl.org/)
- [Regain control of AI crawlers（Cloudflare theNET）](https://www.cloudflare.com/the-net/building-cyber-resilience/regain-control-ai-crawlers/)

### 安全与自动化威胁

- [2025 Imperva Bad Bot Report（博客摘要）](https://www.imperva.com/blog/2025-imperva-bad-bot-report-how-ai-is-supercharging-the-bot-threat/)
- [2025 F5 Scraper bots deep-dive](https://www.f5.com/labs/articles/threat-intelligence/2025-advanced-persistent-bot-report-scraper-bots-deep-dive)
- [OWASP Automated Threats — OAT-011 Scraping](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping.html)

### 行业报告与趋势（第三方）

- [User agent strings to HTTP signatures（Arcjet）](https://blog.arcjet.com/user-agent-strings-to-http-signatures-methods-for-ai-agent-identification/)
- [ChatGPT agent’s user-agent（Simon Willison）](https://simonwillison.net/2025/Aug/4/chatgpt-agents-user-agent/)
- [ChatGPT vs Googlebot 请求量（Search Engine Journal / 第三方数据）](https://www.searchenginejournal.com/chatgpt-googlebot-crawl-data-alliai-spa/570885/) — **方法与时效见原文**

### 对比与测评（第三方；观点非官方）

英文 SEO 与开发者社区对 **AI 爬虫** 的立场常分裂为 **「显式允许检索类 UA 以换引用」** 与 **「禁止训练类、限制版权风险」**；实操上 **wildcard Disallow**、安全插件默认规则、CMS 模板**可能误伤** OAI-SearchBot 等——需逐项对照 robots。**Agent** 议题则更多讨论 **「HTTPS 签名 + 边缘放行」** 而非再增加一条易拦截的 UA。**第三方爬虫排行榜**与 **单站日志** 往往数量级不一致，宜作趋势参考。*网摘综合、非本站实测。*

### 站内索引（Alignify 仓库）

- **站长向用户页**：`/seo/crawler`、`/zh/seo/crawler`（正文见 `content/seo/*/crawler.md`；与本笔记 **主题重叠但信息密度分工**，见 [knowledgehub README](../README.md)「Crawler / 网页抓取：内容边界」）
- **采集向工具页**：`/tools/web-scraping`、`/zh/tools/web-scraping`（`content/tools/*/web-scraping.md`）
- **流水线**：[how-search-engine-works.md](./how-search-engine-works.md)
- **清单**：[checklist.md](./checklist.md)
- **GEO**：[tools/geo.md](../tools/geo.md)
- **Web 抓取工具谱系（HTTP/浏览器/编排/托管 API）**：[tools/web-scraping.md](../tools/web-scraping.md)
- **Agent Skills（产品技能生态，非 HTTP 爬虫）**：[agent-skills.md](../tools/agent-skills.md)

---

**延伸阅读与参考材料**

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google Search Console 抓取/索引相关文档入口](https://support.google.com/webmasters/search?q=crawl)（站内搜索入口；具体页面以官方更新为准）
- [OpenAI GPTBot 公开页](https://openai.com/gptbot)
- [OWASP Automated Threats 总览](https://owasp.org/www-project-automated-threats-to-web-applications/) — 自动化威胁分类框架（含 Scraping）
