# AI 可见度（AI Visibility）· 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网产品页、独立评测博客、第三方品类盘点、行业媒体与社区讨论）；并归纳站内 GEO 知识块 [geo.md](./geo.md) 中「可见度监测」子域的**概念分层**（**未**逐字迁入）。**未**引用 Alignify 站内正文 JSON 作为事实来源。**市场规模类数字**以定性趋势为主——因品类尚在早期，数据源口径差异大，**不**做硬承诺。网摘整理日期 **2026-06-28**。

**站内对照**：待上线正式页时对齐（新文优先 `/blog/ai-visibility`；历史 Tools 模式 `/tools/ai-visibility`）· `content/blog/en|zh/ai-visibility.json` 或 `content/tools/en|zh/ai-visibility.json`

**Tools 关键词与 slug 映射**：待 `tools-pages-config.ts` 收录后补链

**与相邻 slug 分流**：

| slug | 典型买家问题 | 交付形态 | 验收核心 |
|------|-------------|---------|---------|
| **`ai-visibility`（本页）** | "ChatGPT/Perplexity 里有人提到我品牌吗？" | 监测仪表盘、自动化快照、多引擎轮询 | 提及率、引用率、声量份额走势 |
| [`geo`](./geo.md) | "怎么让 AI 多引用我的品牌？" | 监测 + 内容优化 + 技术审计全栈 | 可见度分数提升 + 内容改版闭环 |
| [`search-engine`](./search-engine.md) | "有哪些 AI 搜索引擎？他们怎么工作？" | AI 搜索产品索引与对比 | 品类认知、引擎覆盖列表 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 可见度（AI Visibility）**：品牌 / 产品在 AI 生成答案中被**提及、引用、推荐**的频率与质量。核心指标含：**提及率**（% 的抽样 prompt 中出现品牌名）、**引用率**（是否带 URL）、**声量份额**（vs 竞品）、**情感倾向**（正面 / 中立 / 负面）。不同于传统 SEO 的「排名—流量」逻辑——AI 答案里被提到未必能带来点击，但缺席意味着在零点击场景里**不可见**。
- **AI 可见度监测工具（AI Visibility Tool / AI Visibility Tracker）**：通过自动轮询多 AI 引擎、对预设提示词集反复抽样，生成品牌可见度报告的 SaaS 或 API。替代手工逐一查询 ChatGPT / Perplexity / Gemini 等。
- **AI Visibility Score**：多数监测产品的**合成指标**（0–100 或类似刻度），综合出现频次、位置、情感与竞品比例；各厂商算法不互通，**不可**横向对比分数。
- **AI 声量份额（Share of Voice in AI / AI SOV）**：在指定话题 / 提示词集内，品牌提及占比与竞品比较。**采样规模与 prompt 选择**强烈影响数值。
- **AI 引用（AI Citation）**：AI 答案中显式带 URL 的来源标注；区别于**口头提及（unlinked mention）**——引用更可操作（改页面能见效），提及更依赖整体权威。
- **提示词库（Prompt Library / Prompt Set）**：监测的输入——非传统关键词，而是用户实际可能问 AI 的**完整问题**（如「适合小团队的无代码建站工具有哪些？」）。质量由**代表真实买家意图**决定。
- **AI 引擎覆盖（Engine Coverage）**：监测工具实际轮询的平台（ChatGPT、Perplexity、Gemini、Claude、Google AI Overviews、Copilot 等）。单一引擎覆盖通常**漏掉 40-60% 品牌提及**。
- **LLM 提及（LLM Mentions）**：DataForSEO 等 API 商使用的术语，指 AI 回答中出现品牌 / 域名的记录；**聚合而非实时**，通常有 2–7 天延迟。
- **答案快照（Answer Snapshot）**：监测工具保存的 AI 完整响应存档；用于事后比对、合规审计、竞品语境分析。
- **AI 爬虫（Bot / Crawler）**：GPTBot、ClaudeBot、PerplexityBot 等——与 AI 可见度**间接相关**：爬取行为保证内容进入检索池，但**不等于**被引用。页面被爬 ≠ 被提。

---

## 专题对照 / 扩展定义

| 维度 | **SEO 排名追踪** | **AI 可见度监测** |
|------|-----------------|-------------------|
| **测量对象** | 关键词在搜索结果页（SERP）的排序位置 | 品牌在 AI 合成答案中的出现、位置与语境 |
| **输入** | 关键词（2–4 词，搜索量有数据） | 提示词（多句、对话式；无公开搜索量） |
| **可复现性** | 确定性高；同一查询同日两次结果基本一致 | **概率性**；同一 prompt 同引擎两次可能不同 |
| **商业指标** | 排名、点击、转化 | 提及率、声量份额、引用率、情感；**未必带点击** |
| **抽样频率** | 日 / 周级 rank tracking 是标准 | 周级至月级；太频繁可能放大噪声 |
| **数据来源** | 搜索引擎公开 + 抓取 | **平台不公开**；全靠工具自行轮询/估算 |

| 维度 | **AI Visibility Tools** | **GEO 全栈平台** |
|------|------------------------|------------------|
| **核心功能** | 监测 + 报表 | 监测 + 内容生成 + 技术审计 + 归因 |
| **典型购买者** | 想知道「现状」的营销团队 | 想要「改现状」的内容/增长团队 |
| **典型入口价格** | $29–$99/月 | $99–$499/月 |
| **是否含内容功能** | 否或极弱 | 含简报、大纲、AI 撰稿 |
| **本知识块范围** | **是** | 不在此覆盖；见 [geo.md](./geo.md) |

---

## 问题域（为何会出现这类产品）

- **零点击搜索爆发**：56%→69%（2024→2025），用户直接在 AI 对话中获取答案。品牌不在 AI 答案里 = 对此类用户**不可见**。
- **传统排名工具完全盲区**：Ahrefs、Semrush、SE Ranking 的经典 rank tracker **只看 Google/Bing 蓝色链接**，无法探测 ChatGPT、Perplexity、Claude 等独立助手内的品牌出现情况。2025-2026 间所有 SEO 套件**都在紧急加装 AI 可见度模块**。
- **引用结构脆弱**：同一问题在不同引擎下的引用源**重叠度低**（第三方实测常<30%）。手工抽查不可规模化——一个品牌可能需要追踪 50–200 个 prompt × 5+ 引擎 = **250–1,000+ 个答案快照 / 周**。
- **品牌声誉在 AI 中不可控**：错误事实、过时信息、负面语境在 AI 回答中**更难发现**——不像搜索结果页可以被人工浏览。监测工具提供**预警机制**。
- **合规与治理需求**：医疗、金融、法律品牌需有**可审计记录**证明 AI 对品牌表述的准确性——催生 enterprise-grade 监测需求。
- **监测市场快速膨胀**：2025 夏季到 2026 春季内前十家 AI visibility 公司**公开融资超 $3.9 亿**，品类从 0 到 60+ 产品仅 18 个月。
- **本地/区域引擎盲区**：海外域名 tracker **不能**覆盖各地区本地 AI 助手（如本地大模型对话产品）——催生本地方案等本土监测产品。

---

## 能力栈（概念拆分，非厂商功能表）

- **多引擎轮询**：按预设提示词库，向 ChatGPT / Perplexity / Gemini / Claude / Google AI Overviews / Copilot 等周期性发送查询并存档答案快照。
- **提及检测**：在答案文本中识别品牌名称（精确匹配 + 变体 + 别名），区分**带链接引用**与**纯口头提及**。
- **声量与竞品对标**：在同一组提示词下并排展示品牌 vs 竞品的提及率、位置分布、趋势变化。
- **情感与语境分类**：将答案中与品牌相关的片段标记为正面 / 中立 / 负面；部分工具提供**幻觉检测**（品牌被错误归因）。
- **引用溯源**：分析 AI 答案中 URL 的域名归属——官网、新闻、UGC、百科——指导 PR 与内容策略。
- **爬虫日志对照**（高端产品）：服务器端识别 GPTBot 等访问，与「答案中是否出现」做**互补验证**——被爬不代表被提，但未爬**大概率**不会被提。
- **报告与告警**：周/月度趋势报表 + 出现重大变化（如竞品突然被频繁推荐）时的实时告警。
- **API / 数据导出**：供企业 BI 管道消费——Looker、BigQuery、Google Sheets。

---

## 形态谱系（与具体品牌解耦）

- **独立 AI 可见度监测 SaaS**：单一品类心智——只做品牌在 AI 答案中出现 / 不出现的监测。典型起点 $29–$99/月。代表路径：Searchable、Trakkr、Otterly.AI、Peec AI、LLM Pulse、ZipTie、Rankscale、Presenc AI。
- **企业级 AI 品牌治理平台**：多品牌、多区域、多团队权限；含 SOC2 / HIPAA 合规。典型起点 $300–$2,400/月。代表路径：Profound、Scrunch AI、Evertune、Bluefish、AthenaHQ。
- **SEO 套件附加 AI 模块**：传统 SEO 平台内的附加功能——与已有 rank tracking、keyword research 数据同一订阅。代表路径：Semrush AI Visibility Toolkit、Ahrefs Brand Radar、SE Ranking AI Visibility、Surfer AI Tracker、Conductor。
- **GEO 全栈平台内的监测层**：监测不是独立产品，而是「发现缺口→改内容→复测」闭环中的第一环。代表路径：Promptwatch、Frase、Writesonic GEO、Goodie AI、KIME。
- **免费 AI 可见度检查器**：一次性快照，无需注册——用作付费品的获客漏斗。代表路径：Ahrefs AI Visibility Checker、HubSpot AEO Grader。
- **API 数据层**：提供结构化 LLM 提及数据供企业自建仪表盘，而非直接向终端用户售卖 UI。代表路径：DataForSEO LLM Mentions API。
- **本地 GEO 监测**：侧重各地区本地 AI 助手与对话平台；常以「品牌可见度」「GEO 评分」为叙事。代表路径：各市场本地品牌可见度追踪方案。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **监测数据的非确定性**：AI 答案本身是概率生成，同类 prompt 两次结果可能不同。工具的「可见度分数」若无足够样本支撑（如每月仅 50 次送检），**趋势噪音大**——不可据此做重大预算决策。
- **采样偏差**：多数海外工具**默认 Web 端英文用户视角**，App 内、本地语言版、登录态下的答案可能完全不同。**API 调用 ≠ 真实用户体验**——Surfer 测试显示 API 结果比网页结果平均短 46%，25% 的 API 请求甚至不返回引用源。
- **「AI 搜索量」指标的不可靠性**：没有平台公开提示词数据。所有「AI prompt volume」都是估算或面板外推，**精度远低于 Google Keyword Planner**。禁止以此作为硬承诺依据。
- **跨法域数据采集**：在不同司法管辖区域向 AI 平台自动发请求可能涉及爬虫条款与隐私合规；本地/区域引擎监测需独立方案。
- **监测 ≠ 行动**：购买仪表盘但未建立「发现问题→改页面→复测」的**闭环流程**时，AI 可见度分数会波动但业务无感——这是此品类最常见的采购失效模式。

---

## 落地碎片（无先后）

- **先定义核心提示词集**：不是「行业大词」，而是**买家实际会问 AI 的问题**——从销售对话、售后工单、客服聊天记录里提取。
- **覆盖 ≥5 个引擎**：仅监测单一引擎（如 ChatGPT）会漏掉 **40–60% 品牌提及**。
- **把监测节奏与内容发布节奏对齐**：周级 / 双周级；过频采样放大噪声，过疏错过趋势。
- **区分「被提」与「被引」**：口头提及靠长期品牌建设，带链接引用靠**页面结构 + 可爬取性**——这是可操作杠杆。
- **爬虫日志作互补数据**：如果 GPTBot 从没来过你的站，大概率也不会被引用。
- **先免后付**：用 Ahrefs 免费 checker 或 OtterlyAI $29/月起步做基线，确认有数据价值后再升级到 enterprise 级。
- **本地/区域场景单独设计**：海外工具覆盖不了各地区本地 AI 助手——需要本土监测方案或手工抽检。

---

## 工具与产品类型（品类划分）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **AI visibility tool / tracker** | 多引擎轮询、提示词库、品牌提及率、声量份额 | 品类核心命名；独立 SaaS 多在此 |
| **AI brand visibility platform** | 企业级多品牌治理、多区域、合规审计 | 偏 enterprise；定价 >$300/月 |
| **GEO monitoring / AEO platform** | 监测 + 内容优化 + 技术审计 | 全栈产品内的监测层，非独立 |
| **LLM mentions API** | 结构化数据供自建仪表盘 | 开发者向；不向终端用户销售 UI |
| **Free AI visibility checker** | 一次性免费快照，获客漏斗 | 如 Ahrefs、HubSpot；非持续监测 |
| **本地 GEO 监测平台** | 各地区本地 AI 助手覆盖 | 独立品类；常含语料库与优化建议 |

---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

与站内 GEO 页面的 `bestTools` 互补——GEO 页覆盖**全栈方案**，本表专注**独立监测工具**。各一句话据 **2026-06** 对**所给官网 URL** 抓取归纳，**定价与功能边界以厂商最新页及合同为准**。

| 名称 | 一句话（据官网公开表述归纳） | URL |
|------|------------------------------|-----|
| **Otterly.AI** | $29/月起的最低入门门槛，覆盖 ChatGPT / Perplexity / Google AI Overviews / Gemini / Copilot，适合小团队试水 | [otterly.ai](https://otterly.ai/) |
| **Peec AI** | €85/月起，115+ 语言，每日刷新；纯监测向——给数据但不给内容生成 | [peeck.ai](https://peec.ai/) |
| **Trakkr** | 8 模型覆盖、提示词级粒度、品牌感知追踪、AI 爬虫分析；$49/月起 | [trakkr.ai](https://trakkr.ai/) |
| **Searchable** | $50/月起，监测 + 内容 Studio 闭环，覆盖 ChatGPT / Claude / Perplexity / Google AI Overviews / Copilot；偏 DTC/电商 | [searchable.com](https://www.searchable.com/) |
| **Profound** | 品类首家独角兽（$9600 万 C 轮），10+ 引擎、SOC2/HIPAA、400M+ 对话；$99/月起步 | [tryprofound.com](https://www.tryprofound.com/) |
| **Evertune** | 百万级 prompt 抽样 / 品牌 / 月，CMO 级企业报表；仅企业定价 | [evertune.ai](https://evertune.ai/) |
| **Scrunch AI** | Agent Experience Platform（AXP）——技术 GEO 基础设施，非纯监测仪表盘；SOC2 | [scrunch.ai](https://scrunch.ai/) |
| **AthenaHQ** | Shopify + GA4 归因原生对接——引文数据直接映射到订单 | [athenahq.com](https://athenahq.com/) |
| **Promptwatch** | 10 引擎监测 + Answer Gap Analysis + AI 撰稿 + AI Crawler Logs；闭环平台 | [promptwatch.ai](https://promptwatch.ai/) |
| **LLM Pulse** | €49/月，品牌情感追踪、14 天免费、不限席位；bootstrapped | [llmpulse.ai](https://llmpulse.ai/) |
| **ZipTie** | $29/月起，轻量 AI Overviews + ChatGPT + Perplexity 追踪 | [ziptie.dev](https://ziptie.dev/) |
| **Presenc AI** | 独立评测综合得分 94/100（Presenc AI Research, 2026），6 平台覆盖，$79/月 | [presenc.ai](https://presenc.ai/) |
| **Rankscale AI** | 最宽模型覆盖 + 不限席位的最低价格定位 | [rankscale.ai](https://rankscale.ai/) |
| **KIME** | €149/月，10 模型、Action Centre 优化引擎；已服务 Saxo/Gymshark 等品牌 | [kime.ai](https://kime.ai/) |
| **Semrush AI Visibility Toolkit** | 289M+ 提示词数据库，与经典 SEO 同一订阅；适合已有 Semrush 的团队 | [semrush.com · AI Visibility](https://www.semrush.com/ai-seo/overview/) |
| **Ahrefs Brand Radar** | 253M+ 月提示词、AI 声量份额、可免费入门快照；适合已有 Ahrefs 的团队 | [ahrefs.com/ai-visibility-checker](https://ahrefs.com/ai-visibility-checker) |
| **DataForSEO LLM Mentions API** | 2 亿条聚合 AI 响应的结构化数据；$100 月最低消费 + 按行付费 | [dataforseo.com](https://dataforseo.com/apis/ai-optimization-api) |
| **本地监测方案** | 本地 AI 可见度平台——覆盖各地区多个本地 AI 助手与对话平台 | [geo.aibase.com](https://geo.aibase.com/) |

### 对比与测评（第三方；观点非官方）

**2025–2026** 第三方盘点（TechnologyAdvice、Presenc AI Research、Surferstack、Trakkr、Frase、Evertune 等）的核心共识：

1. **"独立监测工具"与"SEO 套件附加"差距明显**——独立品类评分平均高出 31 分（Presenc AI Research 8 工具打分对比）。传统 SEO 套件的 AI 模块（如 Ahrefs Brand Radar、Semrush AI Visibility）覆盖率较低、更新节奏慢，但优势在于**捆绑订阅 + 与现有 rank tracking 同一界面**。
2. **引擎覆盖数是最重要的区分器**：仅跟踪 1–2 个引擎的工具可能漏掉 40–60% 的品牌提及。**≥5 引擎覆盖**是 2026 年的及格线。
3. **定价两极分化**：$29–$99/月（OtterlyAI、Searchable、ZipTie、LLM Pulse）vs $300–$2,400/月（Profound、Scrunch、Evertune）。中腰部 $79–$199/月（Trakkr、Presenc AI、Peec AI）是性价比最优区间。
4. **"监测 vs 行动"是核心分歧**：一类观点认为 AI 可见度工具只需做好监测（数据→BI→人工决策）；另一类主张监测必须与内容生成、技术审计闭环。两种路线都在市场上存在且有利基。
5. **本地/区域引擎监测**是海外工具**普遍盲区**——各地区本地 AI 助手拥有大量活跃用户，但海外 tool 几乎全都不覆盖这些本地平台。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各 SaaS 营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **学界**：[Princeton · GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735)（KDD 2024；citations 优化方法论基础）
- **厂商公开**：[OpenAI · Bots](https://platform.openai.com/docs/bots)（GPTBot 爬取行为与 robots.txt 规则）
- **市场数据**：[Rankability · AI Search Statistics 2026](https://www.rankability.com/reports/state-of-ai-search/)（48 个月搜索需求全景）
- **品类盘点**：[TechnologyAdvice · Best AI Search Monitoring Tools 2026](https://technologyadvice.com/blog/information-technology/ai-software/best-ai-search-monitoring-tools/)
- **品类盘点**：[Trakkr · AI Visibility Tools Category Map](https://trakkr.ai/ai-visibility-tools)（12 工具对比 + 品类地图）
- **品类盘点**：[Ibrahim Furkan Ozcelik · 60+ AI Search Visibility Tools Compared](https://ibrahimfurkanozcelik.com/writing/complete-guide-ai-search-visibility-tools-2026)
- **实证研究**：[Presenc AI · Best AI Visibility Tools 2026](https://presenc.ai/research/best-ai-visibility-tools-2026)（8 工具加权评分）
- **行业叙事**：[Neil Patel · AI Brand Visibility Tracking](https://neilpatel.com/blog/ai-brand-visibility-tracking/)（批判「把 prompt 当关键词」的思维陷阱）
- **本地生态**：[IT之家 · GEO 赛道白皮书 2025-2026](https://www.ithome.com/0/945/559.htm)（区域 GEO 服务商生态图谱）
