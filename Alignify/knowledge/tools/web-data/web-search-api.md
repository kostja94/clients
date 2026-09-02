# Web Search API · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Web Search API**——程序化 **公网网页**检索接口；**Search Engine API** 仅作同义与营销侧别称（见 §词汇锚点），不另起并行技术谱系。终端 AI 搜索产品 → **`slug: search-engine`**。本页为 **供应商速览 + 术语文档 URL 表 SSOT**。

**材料范围**：公开网络检索；术语关系综合 [Firecrawl · Web Search API vs API search engine](https://www.firecrawl.dev/glossary/web-search-apis/web-search-api-vs-api-search-engine)、[Brave · What is a search engine API?](https://brave.com/search/api/guides/what-is-search-engine-api)。**未**把 Alignify 站内 Tools JSON 当作独立事实来源。网摘整理日期 **2026-04-20**。

**站内对照**：[alignify.co/tools/web-search-api](https://alignify.co/tools/web-search-api) · [search-engine](https://alignify.co/tools/search-engine)

**Tools 关键词与 slug 映射**：`slug: web-search-api`（**Web Search API** / **Web搜索API**）；并列 `slug: search-engine` 见 [tools-pages-config.ts](../../../src/data/tools-pages-config.ts)

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Web Search API（主线术语）**：HTTP + JSON/XML 查询托管**网页索引**，返回 URL、标题、snippet、可选元数据——面向 LLM/Agent/RAG grounding。评估以索引范围、延迟、snippet/正文档位、配额、ToS 为准，不以字面是否含 Web 为依据。
- **Search Engine API（辅助 · 常为同义）**：强调「搜索引擎以 API 交付」——与 Web Search API 大量互换；语感偏「买了一套搜索引擎能力」。
- **API search engine**：营销前置定语，语义常回落「可编程网页检索」——归并到 Web Search API 理解即可。
- **Search API（泛称 · 须防歧义）**：可能是公网检索，也可能是站内/向量库——必须核对索引对象。
- **SERP API**：偏重 SERP 结构字段——常与 SEO/情报相邻；与「极简十条链 Agent 馈送」可能分包计价。
- **相对人肉搜索**：Headless 模拟点击是另一类路线（合规与 ToS 另议）。

---

## 专题对照 / 扩展定义

**术语角色**（定义见 §词汇锚点；下表只列与主线的关系）：

| 角色 | 术语 | 与主线（公网托管索引 Web Search API） |
|------|------|--------------------------------------|
| **主线** | Web Search API | **本页默认所指** |
| **辅助 · 同义** | Search Engine API | **同类** |
| **辅助 · 别名** | Programmatic search API | **同类** |
| **泛称 · 慎用** | Search API | **不一定同类** |
| **收窄索引** | Google Programmable Search JSON API | 程序化搜索；索引未必整网 |

---

## 问题域（为何会出现这类产品）

- **助手与代理不能绑架浏览器**：服务端需带 URL 的证据链。
- **相对野蛮抓取**：合作型 API 在配额、滥用检测、缓存上更可预期（以条款为准）。
- **结构化喂给模型**：下游要 JSON 字段、可选 chunk，非整页 HTML。
- **多供应商混合**：索引新鲜度、地域、垂直偏好不同——产线常并行接入多家。
- **Agent 编排标准化（2025–2026）**：Search 成为可编排 tool call——推动「统一接口兼容多后端」需求。

---

## 能力栈（概念拆分，非厂商功能表）

- **查询接入**：关键词/自然语言、分页、时间/语言/站点过滤。
- **结果载荷**：标题、摘要、链接；进阶套餐叠加正文/Markdown/高亮摘录。
- **配额与 SLA**：按次、QPS、企业席；超额降级策略。
- **索引与新鲜度**：新闻与长尾覆盖是核心采购指标。
- **滥用与合规**：高频自动化常伴反滥用；禁止用途需单审。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 备注 |
|------|------|------|
| **A** | 通用网页检索 API | 传统全网搜索的可编程版 |
| **B** | 检索 + 抽取 / 研究管线 | Search 之上叠加正文、分块 |
| **C** | 垂直或区域索引 API | 特定语言、合规市场 |
| **D** | 可编程站内 / 混合索引 | **非**整网 Web Search API 采购需求 |
| **E** | 传统品牌多条产品线 | SERP 情报 vs 给应用的 web search 可能同名不同接口 |

---

## 风险 · 合规 · ToS 与滥用（外部框架可对照，非法律意见）

- **服务条款**：禁止大规模缓存再分发、规避限速等在各 ToS 中常见。
- **版权与摘录**：snippet 与缓存可否二次发布影响媒体/聚合商用例。
- **操纵与垃圾**：批量操纵可见度可能触犯平台政策或多法域规则。
- **日志与隐私**：查询是否用于模型改进或广告——企业对齐 DPA。
- **试用额与生产配额**：免费层与商用 QPS 常分离。

---

## 落地碎片（无先后）

- 对外文档、PRD、RFP：**默认主词 Web Search API**，必要时括号「亦称 Search Engine API」。
- 先弄清要**公网页证**还是**站内库**。
- 横向评测固定同一查询集（含新闻与长尾）。
- RAG：分清仅 SERP 元数据 vs 带正文档位——后者涉及版权与加价。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Web Search API** | 托管网页索引查询 | Search Engine API 常为同义 |
| **SERP API** | 结构化 SERP 字段 | 偏 SEO/情报 |
| **Search + extract / crawl** | 检索后拉正文 | 常与「仅十条链」分层计价 |
| **Enterprise / site search API** | 私域索引 | **非**整网 Web Search API |
| **Cloud AI bundle web search** | 与云账号绑定 | 索引边界以文档为准 |

---

## 外链索引（产品 + 术语 SSOT；非广告、无排序优先级）

### 常见供应商（AI / Agent 叙事；非穷尽）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Tavily** | AI Agent 向 search · extract · crawl 单一 API | [tavily.com](https://www.tavily.com/) |
| **Exa** | Web Search API / AI search，语义检索 + 结构化输出 | [exa.ai](https://exa.ai/) |
| **Parallel** | Search API 面向 Agent，多档延迟/摘录，MCP 叙事 | [parallel.ai](https://parallel.ai/) |
| **Brave Search API** | 独立索引，隐私检索 | [brave.com/search/api](https://brave.com/search/api/) |
| **Nimble** | Web Search Agents、SDK、结构化数据入仓 | [nimbleway.com](https://www.nimbleway.com/) |
| **博查 Bocha** | 国内 AI 应用 Search API | [bochaai.com](https://bochaai.com/) |
| **Serper** | 轻量 Google SERP API；$1/千次；仅元数据 | [serper.dev](https://serper.dev/) |
| **You.com Search API** | 2025 转型企业搜索 API 平台（$100M Series C @ $1.5B）；Web Search / Contents / Research / Finance 四条线；月 10 亿+ 调用 | [you.com](https://you.com/) · [docs](https://you.com/docs) · [pricing](https://you.com/pricing) |
| **Perplexity Sonar API** | 返回合成答案+引用（非原始十条链）——验收维度与纯 Web Search API 不同 | [perplexity.ai](https://www.perplexity.ai/) |

### 术语与官方文档

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Firecrawl · Web Search API vs API search engine** | 可互换表述与别名 | [firecrawl.dev/glossary/.../web-search-api-vs-api-search-engine](https://www.firecrawl.dev/glossary/web-search-apis/web-search-api-vs-api-search-engine) |
| **Microsoft · Bing Web Search API** | 官方产品名含 Web Search | [learn.microsoft.com/.../bing-web-search/overview](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview) |
| **Google · Programmable Search JSON API** | 自定义索引范围示例 | [developers.google.com/custom-search/v1/overview](https://developers.google.com/custom-search/v1/overview) |
| **Brave · What is a search engine API?** | Search Engine API 话术释义 | [brave.com/search/api/guides/what-is-search-engine-api](https://brave.com/search/api/guides/what-is-search-engine-api) |
| **SerpAPI** | 第三方 SERP 结构化访问 | [serpapi.com](https://serpapi.com/) |

### 对比与测评（第三方；观点非官方）

盘点「best web search API for LLM / agents」（2025–2026）通常比较延迟、价格、索引覆盖、是否内置正文清洗；争议多在**索引对象误配**（站内 vs 公网），而非 Web 与 Engine 字面优劣。**Brave Search Engine API** 与 **Bing Web Search API** 命名并存——第三方共识仍是**能力表优先**。

2026 格局要点（宏观，不重复 §问题域）：统一 API 网关化（多后端路由）；搜索+抽取一体化（Firecrawl、Jina Reader 等）；索引新鲜度竞争加剧；欧盟 DMA 影响默认搜索引擎结构；中国市场百度/360 等与 Google/Bing 不可互换。

*本小节为网摘综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站内**

- [web-fetch.md](web-fetch.md)——Search 找 URL 之后 Fetch 取正文
- [search-engine.md](../search-geo/search-engine.md) · [geo.md](../search-geo/geo.md)

**站外**

- RAG 中开放网页检索与引用校验（grounding, web-augmented LLM）
- Tavily / Exa / Brave Search API 官方文档