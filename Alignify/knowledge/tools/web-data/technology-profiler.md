# 网站技术检测与画像工具 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**website technology profiler / 网站技术栈检测**——自动识别站点在用的 CMS、框架、分析工具、CDN 等**技术标签**；核心输出是「用什么」而非「有什么内容」。与 web-scraping、headless-browser、web-fetch 分流见 §与相邻 slug 分流。本页为 **产品 URL 表 SSOT**（完整链接表仅此一处）。

**材料范围**：公开网络检索（BuiltWith/Wappalyzer/SimilarTech/WhatRuns 等厂商官网与博客、行业对比测评、社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 2026-05-18。

**站内对照**：待上线 Tools 页时对齐（`slug: technology-profiler`）。

**Tools 关键词映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（`slug: technology-profiler`，待收录）

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`technology-profiler`（本页）** | **`web-scraping`** | **`web-search-api`** |
|------|-----------------------------------|---------------------|----------------------|
| **典型买家问题** | 这个网站用什么搭的？哪些公司在用 Shopify？ | 批量提取网页里的结构化数据 | 我的 Agent/RAG 要接哪条 HTTP API 搜网页？ |
| **交付形态** | 浏览器插件、网站查询框、API + 技术标签数据库 | 脚本/SDK、托管爬虫 API | 开发者 API、JSON 搜索结果 |
| **验收核心** | 检测覆盖率与准确率、分类粒度、历史变更追踪 | 数据完整性、绕过封禁、结构化解析 | 延迟、索引新鲜度、snippet 质量 |
| **与网页内容的关系** | **不看内容**——只看技术 | **取内容** | **索引内容** |

以下条目可任意顺序阅读；**不是**文章体例，无叙事线。

---

## 词汇锚点

- **Technology profiler / 技术检测器**：通过 HTTP 头、HTML meta、JS 全局变量、CSS 类名、Cookie、DNS 等信号识别技术栈——自动化指纹匹配，非人工看源码。
- **Technographic data / 技术画像数据**：检测结果汇总为公司技术栈档案，用于销售线索（「找全美用 Shopify + Stripe + Klaviyo 的 DTC 品牌」）——与 web scraping 产出的内容数据不同。
- **Detection fingerprint / 检测指纹**：每种技术的识别特征——如 WordPress 的 `wp-content`、Shopify 的 `cdn.shopify.com`、GA 的 `gtag`。
- **Coverage vs Accuracy tradeoff**：爬取型覆盖宽但可能滞后；众包实时型更新快但覆盖依赖用户访问分布。
- **Technology churn / 技术流失**：站点更换技术栈的行为——部分工具追踪，用于销售触发。
- **Read vs Write detection**：多数工具只做「读」；写检测（主动触发交互判断技术）极少，是评测盲区。

---

## 专题对照 / 扩展定义

**检测范式**（术语见 §词汇锚点；下表只列机制与场景差）：

| 维度 | **爬取型（crawl-based）** | **众包型（crowdsourced）** |
|------|---------------------------|---------------------------|
| **代表** | BuiltWith、SimilarTech | Wappalyzer、WhatRuns |
| **机制** | 自建爬虫周期扫描全网上亿站点 | 浏览器插件访问时实时上报 |
| **覆盖 vs 新鲜度** | 广度大、变更滞后 | 更实时、受用户分布约束 |
| **适用** | 大规模线索列表、市场趋势 | 竞品实时调研、个人快查 |

| 维度 | **免费插件/查询** | **付费 technographic 平台** |
|------|------------------|------------------------------|
| **典型用户** | 开发者、PM、好奇浏览者 | 销售、市场分析师、投资尽调 |
| **核心需求** | 一次性「这站用什么」 | 批量导出「用 X+Y+Z 的公司 list」 |
| **支付意愿** | 0 | $149–$995/月 |

---

## 问题域

- **网页技术不透明**：多数站点不主动声明技术栈——profiler 填补信息缺口。
- **销售拓客需要技术信号**：按技术栈筛选潜在客户是最强购买意图信号之一。
- **竞品情报规模化**：「行业 top 100 用什么 CMS」从体力活变为可查询数据。
- **技术趋势追踪**：投资者需跨数百万站点的渗透率数据（React vs Vue、无头 CMS 等）。
- **安全与合规审计**：识别过时/有漏洞版本、未声明第三方脚本——安全扫描前置步骤。
- **广告与营销归因**：部分 profiler 数据被集成到广告/归因系统。

---

## 能力栈

以下维度解耦于任何单一厂商功能表：

- **检测通道**：HTTP 头、meta、JS 对象、CSS 类名、Cookie、DNS/SSL、robots 目录等——通道越多遗漏越少。
- **指纹库规模**：500 种到 10 万+ 条目——数量大不等于覆盖好（同技术多版本号会膨胀计数）。
- **分类粒度**：CMS → 具体 CMS → 版本；分析工具 → SDK 版本——越细对销售线索越有价值。
- **历史追踪**：能否查域名过去技术栈、何时从 A 换到 B。
- **批量查询**：单 URL → 列表上传 → API 批量 → CRM 集成——定价与能力存在巨大断层。
- **准确率与误报**：cdn 缓存混淆、部分页面不同技术、指纹过宽——工具间差异显著（SimilarTech 被指误报 Shopify、Snowplow）。
- **反检测对抗**：站点隐藏 meta、混淆 JS——工具能否用替代信号绕开。
- **技术支出估算**：BuiltWith、NerdyData 等附加月支出估算——**不宜作精确财务数据**。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态特征 | 典型用户 | 代表（规格见 §外链索引） |
|------|----------|----------|--------------------------|
| **1** | 浏览器插件型 | 开发者、PM | Wappalyzer、WhatRuns |
| **2** | 网页即时查询型 | 快速调研 | CRFT Lookup |
| **3** | API / 开发者型 | 集成自有工具链 | Wappalyzer API、BuiltWith API、Apify |
| **4** | Sales Intelligence 平台型 | 销售与市场 | BuiltWith Pro、Bloomberry |
| **5** | 源码搜索引擎型 | 安全研究、营销分析 | NerdyData、PublicWWW |

---

## 风险 · 合规 · 数据治理（外部框架可对照，非法律意见）

- **被检测方隐私**：分析公开可访问资源；WHOIS 等在某些法域受 GDPR 约束。
- **准确率误导决策**：关键决策前交叉验证 2+ 工具。
- **数据时效性**：爬取型滞后可能导致联系「已换平台」的商家。
- **技术支出估算误导**：投资/收购场景须标注「据第三方估算」。
- **反爬与检测对抗法律边界**：欺诈性 UA 或违反 robots 可能触及 CFAA 等——商业用户应了解供应商合规策略。

---

## 落地碎片

- 选型：免费插件（Wappalyzer/WhatRuns）→ 需批量/筛选再评估付费平台。
- 关键判断交叉验证：Wappalyzer + BuiltWith 等不同范式。
- 销售场景配合 firmographic 数据（规模/行业/地域）。
- 勿高估 Write detection——后端技术需结合招聘、工程博客等其他来源。
- 关注技术流失告警——刚换 CMS/电商平台的公司是周边服务商优质时机。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| `technology profiler` / `tech stack detector` | BuiltWith、Wappalyzer 等 | 本页核心品类 |
| `source code search engine` | NerdyData、PublicWWW | 底层源码搜索 |
| `CMS detector` | WhatCMS、CMS Detect | 仅 CMS |
| `ecommerce platform detector` | StoreLeads | Shopify 专检 |
| `technology lookup API` | Wappalyzer/BuiltWith API、Apify | 开发者 API |
| `technographic sales intelligence` | BuiltWith Pro、Bloomberry、UpLead | 销售线索平台 |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| BuiltWith | 规模最大的技术检测数据库（11.3 万+ 技术），爬取型，历史可追溯到 1980s | https://builtwith.com |
| Wappalyzer | 用户量最大的浏览器插件（330 万+），众包实时，API 与 lead gen | https://wappalyzer.com |
| WhatRuns | 完全免费轻量插件，技术变更 Follow | https://whatruns.com |
| SimilarTech | SimilarWeb 旗下企业销售型，爬取 3 亿+ 站点 | https://similartech.com |
| NerdyData | 源码搜索引擎——跨数百万站点搜 HTML/JS 字符串 | https://nerdydata.com |
| PublicWWW | 网页源码搜索，数字营销/联盟营销研究 | https://publicwww.com |
| W3Techs | 侧重服务端技术调研（CMS、语言、托管分布） | https://w3techs.com |
| WhatCMS | 专注 CMS，800+ 平台 | https://whatcms.org |
| StoreLeads | Shopify 店铺发现与筛选 | https://storeleads.app |
| Bloomberry | 企业级检测与 lead gen，可检测非 Web 技术（CRM、ERP） | https://bloomberry.com |
| CRFT Lookup | 免费不限次查询 + Lighthouse、meta、sitemap 预览 | https://crft.studio |
| Apify Tech Stack Detector | 按次付费批量检测 API | https://apify.com |
| BuiltWith MCP Server | BuiltWith MCP，供 AI 助手调用 | https://www.npmjs.com/package/@builtwith/mcp-server |

### 对比与测评（第三方；观点非官方）

- BuiltWith 覆盖最广，但新鲜度不及 Wappalyzer 等实时插件。
- Wappalyzer 整体准确率与 UX 被普遍认为最佳（月搜 ~6000）。
- WhatRuns 完全免费但漏检率较高（如 Amplitude、Navattic）。
- SimilarTech 准确率问题被独立测评反复提及——不宜作唯一来源。
- NerdyData/PublicWWW 走源码搜索路线，与预设分类工具不同赛道。
- 2025 年末社区讨论开源指纹库自建免费替代——覆盖与维护可持续性远不及商业产品。

*本小节为网摘综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- [BuiltWith Blog: The New BuiltWith (2025.09)](https://blog.builtwith.com/2025/09/10/the-new-builtwith/)
- [BuiltWith · AI MCP 遇见网络技术发现 (2025.05)](https://blog.builtwith.com/zh/2025/05/27/ai-mcp-%e9%81%87%e8%a7%81%e7%bd%91%e7%bb%9c%e6%8a%80%e6%9c%af%e5%8f%91%e7%8e%b0/)
- [CRFT Studio: CRFT Lookup vs BuiltWith vs Wappalyzer (2025)](https://www.crft.studio/blog/crft-lookup-vs-builtwith-vs-wappalyzer)
- [Bloomberry: 5 BuiltWith Alternatives (2025)](https://bloomberry.com/blog/5-builtwith-alternatives-for-technology-intelligence/)
- [MarketBetter: Best Free Website Technology Checker Tools (2026)](https://www.marketbetter.ai/blog/best-free-website-technology-checker-tools-2026/)