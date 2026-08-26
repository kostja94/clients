# TL;DR（核心要点）章节最佳实践

本文档定义 TL;DR 章节的规范，**替代原「文章简介」**，适用于 Tools、SEO、Marketing 等所有文章页面。专为 **GEO（生成式引擎优化）** 设计，提升 AI Overview、ChatGPT、Perplexity 等 AI 引擎的引用与抽取效果。

**线上 SSOT（2026-08）**：`tldr-data.json` + `ArticleFromJson` → `Tldr.tsx`；md 内 `block:tldr` 被 parser 跳过。**Brief 采用 → Step 08 注册 JSON**（键 = `pageUrl` 路径）。

**勿新写**：md `#article-intro` section（写了也不渲染）；`<!-- block:tldr -->` 空壳占位。

**参考**：[templates/best-ranking.md](../templates/best-ranking.md)

---

## 〇、名称选择（Summary / Overview / Key Takeaways）

| 术语 | 用途 | 适用场景 |
|------|------|----------|
| **Summary** | 最通用，概括全文要点 | 50–100 词客观概述，回答「发生了什么」 |
| **Overview** | 高层概览，类似 synopsis | 常见于 literal 场景，偏「鸟瞰式」 |
| **Key Takeaways** | 聚焦可操作要点 | 回答「所以呢」，bullet 形式，便于快速决策 |

**本规范选用「Key Takeaways / 核心要点」**：本组件为「直答 + 要点列表」，侧重 actionable insight 而非纯概括；Key Takeaways 更贴合「每条可独立抽取、便于 AI 引用」的 GEO 目标。Google 等平台在博客模板中亦采用 Key Takeaways 区块（[YouTube 示例](https://www.youtube.com/watch?v=ZOj9wOStA1w)）。

---

## 一、定位与作用

**TL;DR / 核心要点** 是页面的**价值摘要章节**，位于正文最开头，核心作用是：

- **直接回答**：在前 40–70 词内用直白语言回答页面核心问题
- **便于 AI 抽取**：结构化列表（bullet points）便于 AI 引擎解析与引用
- **提升可见性**：开篇含实体信号的内容在 AI Overview 中引用率更高

**GEO 作用与引用来源**：

| 来源 | 发现 | 链接 |
|------|------|------|
| **WordStream / Authoritas** | 开篇含实体信号可提升 AI Overview 引用率约 **38%** | [Why Your First 200 Words Are Crucial for AI Search](https://www.wordstream.com/blog/ai-search-optimization-for-intros) |
| **WordStream** | AI Overview 引用最多来源在开篇 **150 词**内含清晰范围与专业标记 | 同上 |
| **GEO 学术论文 (KDD 2024)** | 内容优化可提升生成式引擎响应可见性最多 **40%** | [GEO: Generative Engine Optimization (arXiv)](https://arxiv.org/abs/2311.09735) |
| **Geneo** | 直答式开篇 40–90 词、Q&A 标题、bullet 列表和表格便于 AI 抽取 | [GEO Ultimate Guide 2025](https://geneo.app/blog/generative-engine-optimization-ultimate-guide-2025/)、[Optimize for AI Overview](https://geneo.app/blog/optimize-google-ai-overview-2025-best-practices/) |
| **Search Engine Land** | 描述性 H2 与清晰结构使内容被 AI 引用概率提升约 **40%**；开篇直答段落 **67%** 更易被引用 | [How to optimize content for AI search engines](https://searchengineland.com/how-to-optimize-content-for-ai-search-engines-a-step-by-step-guide-467272) |
| **Google** | 无特殊 markup，遵循标准 Search 最佳实践，使回答易于提取 | [Succeeding in AI Search (2025)](https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search)、[AI features in Search](https://developers.google.com/search/docs/appearance/ai-features) |

---

## 二、通用规范

### 2.1 位置与标题

| 项目 | 中文 | 英文 |
|------|------|------|
| **位置** | 页面最开头，所有其他章节之前 | 同左 |
| **H2 标题** | 核心要点 | Key Takeaways |
| **id** | `article-intro` | `article-intro` |

**说明**：保留 `id="article-intro"` 以维持旧锚点兼容；页面内若有引用 `#article-intro` 的链接仍可跳转。

### 2.2 字数控制

| 项目 | 中文 | 英文 | 依据 |
|------|------|------|------|
| **introduction** | 30–100 字 | 25–70 词 | Geneo 直答开篇 40–90 词；下限对精准短 intro 留弹性（如 llm-for-coding 的 20 词仍可接受）；上限覆盖复杂主题需定义范围 |
| **items** | 4–5 条（推荐） | 4–5 条（推荐） | 演示/执行摘要最佳实践：3–5 条匹配工作记忆，4–5 条信息覆盖更充分 |
| **items 范围** | 3–6 条 | 3–6 条 | 简单工具（单一品类对比）3–4 条；复杂主题（覆盖多个子域，如代理+API+浏览器+合规+生产管线）可用 5–6 条 |
| **单条 item** | 25–60 字（目标） | 18–35 词（目标） | 需容纳产品名（2–5 个）、技术术语和内链；下限保证信息密度，上限控制移动端约两行 |
| **单条上限** | ≤80 字 | ≤40 词 | 超过则拆分为两条或精简修饰；核心信息优先 |

**计数字数时先 `stripHtmlTags` 去除 HTML 标签和 Markdown 标记**（`**bold**`、`[text](url)` 不计入字数），仅统计纯文本内容。审计脚本必须使用 `stripHtmlTags()` 预处理后再计数。

### 2.2.1 items 长度一致性

**依据**：Nielsen Norman Group 研究表明，列表项长度相近时更易扫读、视觉更平衡；长度差异过大会降低可读性。

| 原则 | 要求 | 说明 |
|------|------|------|
| **目标长度** | 中文 25–60 字，英文 18–35 词 | 每条落在该区间内；审计时先 `stripHtmlTags` 再计字数 |
| **长度差异** | 同组内最长条不超过最短条的 2 倍 | 避免一条明显偏长或偏短；≤2.0 即可，items 功能不同（定义 vs. 对比 vs. 行动）天然有别 |
| **语气一致** | 各条保持统一的语气和信息密度 | 同为陈述句/祈使句/定义句均可，但整组不应混杂叙事风格（如三条客观陈述 + 一条口语化评论）。不要求所有条目以相同词性开头——功能不同的条目自然需要不同的起始模式 |

**检查方法**：统计同组 items 字数（stripHtmlTags 后），最长条 ÷ 最短条 ≤ 2.0 即可；若超过则压缩长者或扩展短者。语气一致性人工判断。

**内容与字数最佳实践**（含引用来源）：

| 来源 | 建议 | 说明 |
|------|------|------|
| **Geneo** | 每段前 40–90 词直答 | [Answer-Ready Formatting](https://geneo.app/blog/generative-engine-optimization-ultimate-guide-2025/) |
| **Single Grain** | 可抽取块 134–167 词；H2 下开篇 45–75 词 | [Google AI Overviews Guide 2025](https://www.singlegrain.com/search-everywhere-optimization/google-ai-overviews-the-ultimate-guide-to-ranking-in-2025/) |
| **Single Grain** | 理想段落 <52 词；主答案在前 150 词 | 同上 |
| **WordStream** | 前 200 词关键；前 150 词含专业标记 | [AI Search Optimization for Intros](https://www.wordstream.com/blog/ai-search-optimization-for-intros) |
| **Eric Buckley (Medium)** | 列表、表格、清晰 H2/H3 | [TL;DR for AI Overviews](https://medium.com/@eric_82001/tl-dr-to-rank-in-google-ai-overviews-and-gemini-content-must-be-structured-for-ai-extraction-8708e54b2f30) |

**标题最佳实践**：描述性 H2 使内容被 AI 引用概率提升约 40%（[Search Engine Land](https://searchengineland.com/how-to-optimize-content-for-ai-search-engines-a-step-by-step-guide-467272)）。

### 2.3 内容要求

- **introduction**：直答式，含核心关键词、主题实体、受众/价值；不得模糊或堆砌
- **长说明外置**：「Related / 相关阅读」「Scope / 分工」「编辑部笔记」、仓库路径、GA4/GSC 口径免责声明等**不得**塞进 introduction 拉长 TL;DR（易触发 GEO 与扫读目标冲突）。应放在 **Tldr 正下方** 的独立 `html` 块（建议 `text-sm text-muted-foreground`）或并入首个正文 Section，并保持 **introduction 仍满足 §2.2 字数**
- **items**：每条为独立事实或价值点，可被 AI 单独抽取；避免冗长描述
- **首句含核心关键词**：页面主关键词应在 introduction 首句或前 50 字内（[Yoast](https://yoast.com/focus-keyphrase-in-introduction)）
- **实体与范围明确**：明确主题、受众、内容范围，便于 AI 分类与引用

### 2.3.1 items 中 HTML / Markdown 使用规范

items 内允许 `**粗体**` 与 `[锚文本](/path)`（每 item 最多 1–2 内链）。计字数前 strip HTML/Markdown 标记。

### 2.4 Markdown 写法与 items 内链

`introduction` + `- ` 列表 items；items 内允许 `**粗体**` 与 `[锚文本](/path)`（每 item 最多 1–2 内链）。计字数前 strip HTML/Markdown 标记。

**Step 08 注册**：同步写入 `tldr-data.json`（键 = `pageUrl` 路径，如 `/zh/blog/{slug}` 或 `/tools/{slug}`）。见 [`anatomy.md`](../anatomy.md) §二·一。

```markdown
<!-- block:section -->
## 核心要点 {#article-intro}

开篇直答 30–100 字（中文）或 25–70 词（英文）。

- 要点 1：独立可抽取的句子。
- 要点 2：…
- 要点 3–5 条（推荐 4–5 条）
```

---

## 三、按页面类型的 introduction / items 模式

### 3.1 Tools 页面（30–100 字，含实体+范围+受众三信号；以下为参考变体，非强制套用）：

| 语言 | 变体 A（标准） | 变体 B（技术导向） | 变体 C（对比/替代品导向） |
|------|---------------|---------------------|---------------------------|
| 中文 | 本文介绍 [年份] 年最佳 [工具类型]，帮助 [受众] 根据需求选择合适方案。 | [工具类型] 的实用选型笔记：[核心维度1]、[核心维度2] 与部署模式，面向 [受众]。 | 检索 [工具名] 替代品的人通常面对 [分类1]、[分类2] 与 [分类3]——本文按定位与代码血缘拆解。 |
| 英文 | This guide explores the best [tool type] for [year], helping [audience] choose the right solution. | A practical map of [tool type]：benchmarks, deployment patterns, and [key dimension] for [audience]. | Searchers asking for the best [tool name] alternatives usually land in [bucket1], [bucket2], or [bucket3]——here's how to navigate them. |

**introduction 三信号检查**（每条 intro 至少含两类）：
- **实体信号**：核心关键词（工具名、品类名）在首 50 字/词内
- **范围信号**：页面涵盖内容（「对比」「选型」「排名」「工作流」等）
- **受众信号**：目标读者（「设计师」「开发者」「呼叫中心」「AI/SaaS 团队」等）

**items 模板**（4–5 条推荐，每条 25–60 字 / 18–35 词，stripHtmlTags 后计数；同组最长 ≤ 最短的 2 倍；符合 Island Test）：

| 序号 | 内容方向 | 中文示例 | 最佳实践 |
|------|----------|----------|----------|
| 1 | 核心功能 + 适用场景 | [工具类型] 支持 [功能1]、[功能2]，适用于 [场景1]、[场景2]。 | 首句含工具类型 |
| 2 | 产品对比 | 比较 [产品1]、[产品2] 等主流工具的功能、定价与适用场景。 | 2–3 个代表产品名 |
| 3 | 选择标准 | 掌握选择标准：[维度1]、[维度2]、[维度3]。 | 与如何选择 section 维度一致 |
| 4 | 技术/工作流（可选） | 了解技术原理与实时处理能力，可搭配 [关联工具] 等工作流。 | 有强关联工具时加入 |
| 5 | 应用场景/延伸（可选） | 涵盖 [场景A]、[场景B] 等应用，支持选择指南与常见问题。 | 补充页面范围 |

**完整示例**（AI 口音消除）见 §2.4 Markdown 块；introduction + 4 条 bullet 对应上表 items 方向。

---

### 3.2 Marketing 页面

**页面特征**：营销策略指南、方法论；含什么是、核心方法论、如何实施 section、References

**introduction 模板**（40–80 字）：

| 语言 | 模板 | 占位符说明 |
|------|------|------------|
| 中文 | 本文介绍 [策略名称] 的核心价值、[方法关键词] 与工具支持，帮助 [受众] 建立有效的 [策略简称] 策略。 | [策略名称]：红人营销、联盟营销、关键词调研；[方法关键词]：实施方法、红人筛选方法；[受众]：AI/SaaS 产品、独立开发者 |
| 英文 | This guide covers [strategy] core value, methodology, and tools, helping [audience] build effective [strategy] strategies. | 同上 |

**items 模板**（4–5 条推荐，每条 25–60 字 / 18–35 词，stripHtmlTags 后计数；同组最长 ≤ 最短的 2 倍；Island Test）：

| 类型 | 内容方向 | 中文示例 |
|------|----------|----------|
| 有量化数据 | 核心价值 + 数据背书 | 红人营销通过 KOL 合作提升品牌信任，转化率比传统广告高 2–3 倍，获客成本低 40%–60%。 |
| 方法论类 | 完整流程 | 掌握 [步骤1]、[步骤2]、[步骤3] 的完整方法论。 |
| 有工具 | 工具推荐 | 推荐 [工具1]、[工具2] 等工具，配合 [案例] 等成功案例。 |
| 方法论类 | 定义 + 价值 | 关键词调研是系统性发现用户搜索词汇的过程，是内容营销和 SEO 的基础。 |
| 适用受众 | 受众与输出 | 适用于 SEO、内容营销和独立开发者，帮助搭建优质 Topical Map。 |

---

### 3.3 SEO 页面

**页面特征**：SEO 技术指南、概念说明；含什么是、如何工作、实施要点、References；可选如何选择 section

**introduction 模板**（40–80 字）：

| 语言 | 模板 | 占位符说明 |
|------|------|------------|
| 中文 | 本文介绍 [主题] 的概念、[核心要点] 与最佳实践，帮助读者理解并应用 [主题] 提升 [目标]。 | [主题]：站点地图、Schema、robots.txt；[核心要点]：配置方法、创建提交；[目标]：网站索引效率、SEO 表现 |
| 英文 | This guide covers [topic] concepts, implementation, and best practices for [goal]. | 同上 |

**items 模板**（4–5 条推荐，每条 25–60 字 / 18–35 词，stripHtmlTags 后计数；同组最长 ≤ 最短的 2 倍；Island Test）：

| 类型 | 内容方向 | 中文示例 |
|------|----------|----------|
| 技术配置类 | 核心概念 + 作用 | 站点地图是向搜索引擎提供网站页面与元数据的文件，加速发现与抓取。 |
| 技术配置类 | 类型/格式 | 掌握 XML、HTML 站点地图及站点地图索引的创建、提交与验证方法。 |
| 技术配置类 | 扩展类型 | 涵盖图片、视频、新闻等扩展类型，配合 Search Console 提交与验证。 |
| 实施要点 | 最佳实践与排错 | 提供创建与提交指南、最佳实践与常见错误解决方案。 |

---

### 3.4 占位符速查表

| 页面类型 | introduction 关键占位符 | items 常见方向 |
|----------|-------------------------|----------------|
| **Tools** | [工具类型]、[受众] | 功能+场景、产品对比、选择标准、技术/工作流（可选） |
| **Marketing** | [策略名称]、[方法关键词]、[受众] | 核心价值+数据、方法论、工具+案例、适用受众 |
| **SEO** | [主题]、[核心要点]、[目标] | 概念+作用、类型/格式、扩展类型、实施要点 |

---

## 五、SEO 与 GEO 最佳实践

### 5.1 实体信号（Entity Signals）

AI 引擎从开篇提取三类信息：

| 信号类型 | 说明 | 示例 |
|----------|------|------|
| **主题实体** | 文章核心话题 | 「AI 口音消除工具」「红人营销」 |
| **内容范围** | 文章涵盖的内容 | 「功能对比」「选择指南」「常见问题」 |
| **受众/价值** | 目标读者与收益 | 「帮助读者选择合适方案」 |

### 5.2 AI 可读开篇三要素

| 要素 | 要求 | 示例 |
|------|------|------|
| **意图信号** | 前两句话说明页面目的 | 「本文介绍…」「This guide explores…」 |
| **专业信号** | 明确主题与范围 | 核心关键词、工具类型、年份 |
| **上下文信号** | 明确实体与受众 | 「帮助读者选择合适方案」「for creators and designers」 |

### 5.3 Schema 支持

Step 08 注册 `tldr-data.json` 后，线上 `Tldr.tsx` 输出 ItemList Schema。

### 5.4 语义完整性（Island Test）

每条 item 应为**自包含信息单元**，脱离上下文仍可理解、可被 AI 单独抽取。避免依赖前后文才能解读的表述（[Single Grain](https://www.singlegrain.com/search-everywhere-optimization/google-ai-overviews-the-ultimate-guide-to-ranking-in-2025/)）。

---

## 六、参考文献（GEO 与 AI 搜索）

| 类型 | 来源 | URL |
|------|------|-----|
| 学术 | GEO: Generative Engine Optimization (Aggarwal et al., KDD 2024) | https://arxiv.org/abs/2311.09735 |
| 官方 | Google: Succeeding in AI Search (2025) | https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search |
| 官方 | Google: AI features in Search | https://developers.google.com/search/docs/appearance/ai-features |
| 行业 | WordStream: AI Search Optimization for Intros | https://www.wordstream.com/blog/ai-search-optimization-for-intros |
| 行业 | Geneo: GEO Ultimate Guide 2025 | https://geneo.app/blog/generative-engine-optimization-ultimate-guide-2025/ |
| 行业 | Geneo: Optimize for Google AI Overview | https://geneo.app/blog/optimize-google-ai-overview-2025-best-practices/ |
| 行业 | Search Engine Land: Optimize for AI Search | https://searchengineland.com/how-to-optimize-content-for-ai-search-engines-a-step-by-step-guide-467272 |
| 行业 | Single Grain: Google AI Overviews Guide 2025 | https://www.singlegrain.com/search-everywhere-optimization/google-ai-overviews-the-ultimate-guide-to-ranking-in-2025/ |

---

## 七、适用范围

- **Tools**：工具介绍、产品对比、排名列举类页面
- **SEO**：SEO 指南、技术说明类页面
- **Marketing**：营销策略指南类页面
- **Insights**：可按需使用

---

## 八、与文章简介的关系

**TL;DR 替代「文章简介」**：原「文章简介」为结构导航（「文章首先介绍 X，然后 Y」），TL;DR 改为**价值摘要**（直答 + 要点列表），更符合 GEO 最佳实践。文章简介规范已废弃，本规范为唯一标准。
