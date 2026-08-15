# Web Search API · 知识块（非线性笔记）

**叙述主词**：**Web Search API**（程序化 **公网网页**检索接口）。**Search Engine API** 仅作**同义与营销侧别称**（见下「辅助术语」），不另起一条并行的技术谱系。

**与 Tools 的对应（方案 A）**：**程序化网页检索**专页使用 `slug: web-search-api`，正文见 `content/tools/en|zh/web-search-api.json`，路由 **`/tools/web-search-api`**。终端 **AI 搜索产品**（Perplexity 向盘点）留在 **`slug: search-engine`** → **`/tools/search-engine`**。本文件与 **`slug: web-search-api` 同名**。

**材料范围**：公开网络检索（术语表、云厂商文档、搜索引擎 **API** 指南、英文 **programmatic web search** 用法）。术语关系综合 [Firecrawl · Web Search API vs API search engine](https://www.firecrawl.dev/glossary/web-search-apis/web-search-api-vs-api-search-engine)、[Brave · What is a search engine API?](https://brave.com/search/api/guides/what-is-search-engine-api)。**未**把 Alignify 站内 Tools 正文 JSON 当作独立事实来源复述。网摘整理日期 **2026-04-20**。

**站内对照**：[alignify.co/tools/web-search-api](https://alignify.co/tools/web-search-api) · `/zh/tools/web-search-api`（API 专页）；[alignify.co/tools/search-engine](https://alignify.co/tools/search-engine) · `/zh/tools/search-engine`（AI 搜索引擎产品）

**Tools 关键词与 slug 映射**：`slug: web-search-api`（`keywordEn`: **Web Search API**，`keywordZh`: **Web搜索API**）；并列类目 `slug: search-engine`（**AI 搜索引擎**）见 [tools-pages-config.ts](../../../src/data/tools-pages-config.ts)。

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Web Search API（主线术语）**：用代码（通常 **HTTP**，响应 **JSON/XML**）查询服务商托管的**网页索引**，返回排序结果及 **URL、标题、摘要 snippet、可选元数据**；面向 **LLM / Agent / RAG grounding**、自动化研究与需**可引用链**的产品文档时，英文检索与技术写作常以 **web search API** 为主词。**评估供应商时**，以索引范围、延迟、snippet 与正文档位、配额与 **ToS** 为准，不以字面是否含 **Web** 为依据。
- **Search Engine API（辅助术语 · 常为同义）**：强调「搜索引擎以 **API** 交付」，在**同一品类**上与 **Web Search API** **大量互换**（厂商白皮书、Brave 指南等常用此说法）。差别主要在**语感**：偏「买了一套搜索引擎能力」而非「接一条网页检索管线」。产品线若同时卖人机搜索站与开发者接口，文档里可出现 **Search Engine API** 小节——**仍为同一类产品族**，除非文档明确写的是**站内搜索**或**私域索引**。
- **API search engine**：英文营销里偶见的前置定语写法，语义常回落到「可编程的网页检索」，归并到对 **Web Search API** 的理解即可。
- **Search API（泛称 · 须防歧义）**：既可指 **Web Search API**，也可指**站内搜索**、应用内检索、向量库检索——读到 **Search API** 时必须核对**索引对象是公网页还是站内库**。
- **SERP API**：偏重「**搜索结果页结构**字段」（有机结果块、可选附加栏位等），常与 **SEO**、竞品情报相邻；可与纯 **Web Search API** 重叠，也可能面向**营销分析**而非 **token 友好摘录**，采购时与「极简十条链」封装区分报价。
- **相对「人肉开浏览器搜索」**：上述接口均为**程序化**访问；**Headless + 自动化点击**模拟搜索是另一类路线（合规与站点 **ToS** 另议）。

---

## 专题对照 / 扩展定义

| 角色 | 术语 | 常见含义 | 与主线（公网托管索引上的 **Web Search API**） |
|------|------|----------|------------------------------------------------|
| **主线** | **Web Search API** | 程序化查询网页索引；开发者文档与 AI 集成语境高频 | **本页默认所指** |
| **辅助 · 常为同义** | **Search Engine API** | 同上，话术偏「搜索引擎即服务」 | **同类**（选型看能力表，不比对字面） |
| **辅助 · 别名** | **Programmatic search API / Web search endpoint** | 与前两者同簇 | **同类** |
| **泛称 · 慎用** | **Search API** | 可能是公网检索，也可能是站内/私域 | **不一定同类**——读索引范围 |
| **示例 · 收窄索引** | **Google Programmable Search JSON API** 等 | 程序员配置的**站点集合**上检索 | **同属程序化搜索**；索引未必是「整网」 |

---

## 问题域（为何会出现这类产品）

- **助手与代理不能绑架浏览器**：需要在服务端拿到**带 URL 的证据链**，而非让用户复制搜索结果。
- **相对野蛮抓取**：面向合作的 **Web Search API** 往往在配额、滥用检测、缓存策略上更可预期（以各服务商条款为准）。
- **结构化喂给模型**：下游要 **JSON** 字段、可选 **chunk**，而非整页 **HTML**。
- **多供应商混合**：索引新鲜度、地域与垂直偏好不同，产线常并行接入多家 **Web Search API**。
- **Agent 编排层的「搜→取→读→答」管线标准化**：2025-2026 年 Agent 框架（LangChain、OpenAI Agents SDK、MCP）将 Web Search API 标准化为可编排的 tool call——搜索不再是独立产品而是 Agent 的能力原子，这推动了对「统一接口兼容多后端」API 的需求。

---

## 能力栈（概念拆分，非厂商功能表）

- **查询接入**：关键词或自然语言、分页、时间/语言/站点过滤（以服务商为准）。
- **结果载荷**：标题、摘要、链接、排序相关信号；进阶套餐叠加**正文抓取、Markdown、高亮摘录**（常与纯 **SERP** 元数据分拆计费）。
- **配额与 SLA**：按次、**QPS**、企业席；超额降级策略需预留。
- **索引与新鲜度**：新闻与长尾覆盖是核心采购指标，**优于**争论用 **Web** 还是 **Engine** 自称。
- **滥用与合规**：高频自动化查询常伴反滥用策略；合同中的禁止用途需单审。

---

## 形态谱系（与具体品牌解耦）

- **通用网页检索 API**：传统「全网」搜索体验的可编程版；云厂商与独立搜索供应商均有路线。
- **检索 + 抽取 / 研究管线**：在 **Web Search API** 之上叠加正文、分块、研究型端点，服务 **Agent** 一条龙。
- **垂直或区域索引 API**：面向特定语言、合规市场或行业语料。
- **可编程站内 / 混合索引**：检索语法类似，但**索引对象非开放公网**——文档仍可能写 **Search API**，与主线 **Web Search API** **不是**同一采购需求。
- **传统搜索品牌下的多条产品线**：**SERP 情报**与「给应用用的 **web search**」可能同名族不同接口，**勿凭名称等同能力**。

---

## 风险 · 合规 · ToS 与滥用（外部框架可对照，非法律意见）

- **服务条款**：禁止大规模缓存再分发、规避限速、垃圾用途等在各 **Web Search API** 提供商 **ToS** 中常见；跨境场景核对数据出境。
- **版权与摘录**：snippet 与缓存可否二次发布、保存时长，影响媒体与聚合商用例。
- **操纵与垃圾**：批量操纵可见度或生成误导内容可能触犯平台政策或多法域不正当竞争规则——**不得以本知识块替代专项合规**。
- **日志与隐私**：查询是否用于模型改进或广告；企业采购对齐 **DPA**。
- **试用额与生产配额**：控制台免费层与商用 **QPS** 经常分离。

---

## 落地碎片（无先后）

- 对外文档、**PRD**、采购 **RFP**：**默认主词写 Web Search API**，必要时括号注明「亦称 **Search Engine API**」可减少歧义。
- 先弄清要的是**公网页证**还是**站内库**；同名 **search API** 常被误接。
- 横向评测时固定**同一查询集**（含新闻与长尾），对比延迟、摘录质量、死链率。
- **RAG**：分清仅 **SERP** 元数据与「带正文/高亮」档位；后者常涉及版权与加价。

---

## 工具与产品类型（「Web Search API」「程序化检索」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Web Search API** | 托管网页索引上的查询；本文主线 | **Search Engine API** 常为同义自称 |
| **SERP API** | 结构化 **SERP** 字段 | 偏 **SEO**/情报工作流时可与「极简 Agent 馈送」分包 |
| **Search + extract / crawl** | 检索后拉正文、转 **Markdown** | 常与「仅十条链」分层计价 |
| **Enterprise / site search API** | 私域或客户站索引 | **非**整网 **Web Search API** 时应写明 |
| **Cloud AI bundle 中的 web search** | 与云账号绑定的网页检索能力 | 索引边界以文档为准 |

---

## 常见供应商速览（AI / Agent 叙事；外链；非穷尽、无排序）

以下产品在公开材料中常与 **LLM / Agent / RAG** 并列出现；**不等同**于「唯一正确选型」，仅作检索谱系锚点。定价与能力以官网为准。

| 名称 | 一句话（据官网/公开叙事归纳） | URL |
|------|------------------------------|-----|
| **Tavily** | 强调为 AI Agent 提供 **search · extract · crawl** 单一 API 入口与安全层 | [tavily.com](https://www.tavily.com/) |
| **Exa** | 自称 **Web Search API / AI search**，神经·语义检索 + 结构化输出 + 正文能力 | [exa.ai](https://exa.ai/) |
| **Parallel** | **Search API** 面向 Agent，多档延迟/摘录，文档与 **MCP** 集成叙事常见 | [parallel.ai](https://parallel.ai/) |
| **Brave Search API** | **Brave Search** 的开发者接口；隐私检索 + 第三方助手集成报道需对照官方 | [brave.com/search/api](https://brave.com/search/api/) |
| **Nimble** | **Web Search Agents**、SDK、结构化数据入仓（偏企业情报/电商管线） | [nimbleway.com](https://www.nimbleway.com/) |
| **博查 Bocha** | 国内 AI 应用侧 **Search API** 叙事（调用量等以厂商披露为准） | [bochaai.com](https://bochaai.com/) |
| **Serper** | 轻量 Google SERP API；$1/千次起，仅返回搜索元数据（无正文），常与 Fetch 工具串联 | [serper.dev](https://serper.dev/) |
| **You.com Search API** | 2025 年从消费级 AI 搜索转型为**企业搜索 API 平台**（$100M Series C @ $1.5B）。四条产品线：Web Search API（$5/千次）、Contents API（$1/千页）、Research API（4 档 $12–$450/千次，AAAI 2026 最佳论文）、Finance Research API。月 10 亿+ 调用，客户含 DuckDuckGo/Windsurf/Databricks。SOC 2、Zero Data Retention、MCP 免费端点（100 次/天）、Python/TS SDK | [you.com](https://you.com/) · [API docs](https://you.com/docs) · [pricing](https://you.com/pricing) |
| **Perplexity Sonar API** | 返回合成答案 + 引用（而非原始十条链）；Agent 无法独立核验合成结果，与纯 Web Search API 验收维度不同 | [perplexity.ai](https://www.perplexity.ai/) |

---

## 外链索引（术语与文档；外链；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Firecrawl · Web Search API vs API search engine** | 词条将 **Web Search API** 与 **API search engine** 列为可互换表述，并列举等价别名（含 **Search engine API**） | [firecrawl.dev/glossary/.../web-search-api-vs-api-search-engine](https://www.firecrawl.dev/glossary/web-search-apis/web-search-api-vs-api-search-engine) |
| **Microsoft · Bing Web Search API** | 官方产品名含 **Web Search**，可作「主线用语」与云文档对齐的示例 | [learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview](https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview) |
| **Google · Programmable Search JSON API** | 自定义索引范围的程序化搜索示例 | [developers.google.com/custom-search/v1/overview](https://developers.google.com/custom-search/v1/overview) |
| **Brave · What is a search engine API?（辅助术语释义）** | 用 **Search Engine API** 话术解释同类能力；可与主线对照阅读 | [brave.com/search/api/guides/what-is-search-engine-api](https://brave.com/search/api/guides/what-is-search-engine-api) |
| **SerpAPI** | 第三方 **SERP** 结构化访问的常见文档入口（计费与用途独立评估） | [serpapi.com](https://serpapi.com/) |

### 对比与测评（第三方；观点非官方）

盘点「**best web search API for LLM / agents**」的英文博客与论坛（**2025–2026**）通常以 **Web Search API** 或 **AI search API** 为题，比较延迟、价格、索引覆盖与是否内置正文清洗；评论区争议多在**索引对象误配**（站内 vs 公网），而非 **Web** 与 **Engine** 两个英文单词的优劣。**Brave** 等厂商文档采用 **Search Engine API** 自称，与 **Bing Web Search API** 这类「**Web**」命名并存——第三方共识仍是**能力表优先**。*本小节为网摘综合，非 Alignify 实测。*

---

## 行业注记 · 2026 年中格局

- **统一 API 网关化**：2025-2026 年，越来越多的 Agent 框架和 AI 应用通过统一 API 层同时接入 Brave、Bing、Google、SerpAPI 等多后端——这催生了「Web Search API 路由器」品类（如 Tavily、Exa、Parallel），将多供应商融合为单一端点，按查询特征智能路由。
- **搜索 + 抽取一体化**：单纯返回 10 条蓝色链接的 API 正在被「搜索 → 拉正文 → 清洗 Markdown → 分块」的一体化管线替代。Firecrawl、Jina Reader 等产品将搜索 API 从「信息定位」升级为「Agent 可消费的上下文块」。
- **索引新鲜度作为核心竞争维度**：传统 SERP 缓存延迟在 2026 年被 AI 应用放大——新闻类查询对分钟级更新的需求推动 Brave Search API 等独立索引提供商强调「无第三方索引依赖」。
- **合规与定价分化**：欧盟 DMA 对默认搜索引擎的约束（2024 生效）间接影响了 Web Search API 的市场结构——Google 的 Programmable Search 配额收紧与 Bing Web Search API 的价格竞争形成对照。采购时需区分「企业 SLA 合约」与「开发者免费层」的适用场景。
- **中国市场自有生态**：百度搜索 API、360 搜索 API 在国内 Agent 生态中为核心基础设施，但与 Google/Bing 的开放公网索引覆盖和 API 协议不可互换——中文 Agent 工具链需单独评估国内搜索引擎 API 的可用性与配额。

---

---

## 延伸阅读与参考材料

- **站内相邻**：[web-fetch.md](./web-fetch.md)——Search 找到 URL 之后，Fetch 负责取回正文；两者是标准 Agent「搜→取→读→答」管线的前两步。[search-engine.md](./search-engine.md)（面向人类的 AI 搜索产品） · [geo.md](./geo.md)（生成式引擎优化，如何被 AI 搜索引用）
- **行业综述**：面向 AI 应用的 Web Search API 年度盘点（核对作者是否与单一厂商有商业关系）
- **工程参考**：RAG 中开放网页检索与引用校验（grounding, web-augmented LLM）
- **Tavily Search API 文档**：[tavily.com](https://tavily.com/)——面向 AI Agent 的搜索 + 抽取一体化 API，含正文抓取与分块
- **Exa Search API**：[exa.ai](https://exa.ai/)——语义搜索 API，强调内容相似度而非关键词匹配
- **Brave Search API 文档**：[brave.com/search/api](https://brave.com/search/api/)——独立索引的 Web Search API，强调隐私与无第三方索引依赖
