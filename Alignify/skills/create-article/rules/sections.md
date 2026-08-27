# Alignify 章节规范（唯一真相源）

> **位置**：`skills/create-article/rules/sections.md`  
> **格式**：`content/{channel}/{locale}/{slug}.md` + JSON 侧车（TL;DR / FAQ / References）  
> **Last updated**：2026-08-27  
> **说明**：所有章节写法、选节决策、JSON 侧车、**结论**、**Final CTA** 规则**仅在本文件维护**。结构映射见 [`anatomy.md`](./anatomy.md)；内链见 [`internal-links.md`](./internal-links.md)。

---

## 目录

1. [Part 0 · 内容优先：如何选节](#part-0-内容优先如何选节)
2. [Part 1 · 全局写法（Markdown / H1–H6）](#part-1-全局写法markdown--h1h6)
3. [Part 2 · JSON 侧车三件套](#part-2-json-侧车三件套)
   - [2.1 TL;DR / 核心要点](#part-21-tldr--核心要点)
   - [2.2 FAQ / 常见问题](#part-22-faq--常见问题)
   - [2.3 References / 参考文献](#part-23-references--参考文献)
4. [Part 3 · 正文节型库（按需选用）](#part-3-正文节型库按需选用)
   - [3.1 什么是 XXX](#part-31-什么是-xxx)
   - [3.2 通用主体节（分析 / 场景 / 技术）](#part-32-通用主体节分析--场景--技术)
   - [3.3 Best 产品 H3（best-ranking）](#part-33-best-产品-h3best-ranking)
   - [3.4 对比表格](#part-34-对比表格)
   - [3.5 How To / 如何选择（可选）](#part-35-how-to--如何选择可选)
5. [Part 4 · 结论](#part-4-结论)
6. [Part 5 · Final CTA（页底 SecondaryCta）](#part-5-final-cta页底-secondarycta)
7. [附录 A · 节型 × articleType 速查](#附录-a-节型--articletype-速查)
8. [附录 B · A/B/C 底线汇总](#附录-b-abc-底线汇总)
9. [附录 C · 相关文档索引](#附录-c-相关文档索引)

---

<a id="part-0-内容优先如何选节"></a>

# Part 0 · 内容优先：如何选节

> **原则**：文章架构由**内容**决定；下文与 [`templates.md`](./templates.md) Part 0 均为**参考菜单**，不是必填清单。详见 [`anatomy.md`](./anatomy.md) §〇。

## 选节三问（Step 01 / Brief）

1. 读者离开页面前**必须带走什么**？（定义 / 对比 / 决策路径 / 判断）
2. 哪一节能**单独删掉**而不伤主旨？→ 删
3. 两节是否在**说同一件事**？→ 合并

## 节型菜单（C 层建议）

| 读者需求 | 考虑采用的节 | 常见 articleType | 可省略条件 |
|----------|-------------|------------------|------------|
| 快速判断值不值 | TL;DR | 全部 | Brief 写理由 |
| 建立共同语言 | 什么是 | 几乎全部 | 极短快讯可并入首段 |
| 看产品差异 | Best H3 + 对比表 | best-ranking | 非榜单文 |
| 主体论证 / 场景 | 分析节 / 应用场景 H3 | marketing / insights | 由大纲决定 |
| 知道怎么选 | How To | tools / seo 操作文 | marketing / insights **默认不用** |
| 收束行动 | 结论 | 几乎全部 | — |
| 页底转化 | Final CTA | 几乎全部 | Hub 页走 `exact` |
| 扫尾疑问 | FAQ | 常用 | Brief 省略 |
| 权威背书 | References | 有外部引用时 | 策略文仅 A/B 类源 |

## Brief Section Plan（推荐）

```markdown
| 节 | 采用 | 理由 |
|----|------|------|
| TL;DR | ✅ / ❌ | … |
| 什么是 | ✅ | … |
| How To | ❌ | 策略判断文，用分析节表达落地 |
| FAQ | ✅ | … |
```

## A 层硬底线（与采用哪些节无关）

- md 正文以 **`## 结论 {#conclusion}`** 收束；FAQ 由页底 `FAQ.tsx` 全局渲染（**不在 md 流内**）
- Brief **采用** FAQ → `faq-data.json` 中英文各 **7 问**；内链若存在须 R4 全文 1 次
- Brief **省略** TL;DR/FAQ/Refs → 三 JSON **不得**留对应 pathname 键
- **禁止** frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44）
- **禁止** md 写 `#article-intro` / `#faq` / `#references` 指望渲染
- ZH/EN **对齐实际采用的节**与 anchor id，不对齐「是否凑满 10 节」

---


<a id="part-1-全局写法markdown--h1h6"></a>

# Part 1 · 全局写法（Markdown / H1–H6）

> 新文（2026-08+）：`content/blog/` 或 `content/tools/` 的 md + `<!-- block:section -->` + Markdown `##` / `###` + `{#anchor}`。详见 [`anatomy.md`](./anatomy.md) §四·一。

## 1.1 基本结构

```markdown
<!-- block:section -->
## 章节标题 {#kebab-case-id}

首段 BLUF ≥3 句（策略/marketing 文）。

第二段展开…

### 子节标题 {#sub-id}

…
```

- 列表 / 表格 → `childrenHtml`（`content-html` + 语义 class，E35）
- 段落 → 裸 Markdown，**禁止** inline Tailwind（E35）

## 1.2 H1 / H2 / excerpt

| 元素 | 来源 | 规范 |
|------|------|------|
| H1 | frontmatter `title` | [`meta.md`](./meta.md) §三 |
| excerpt | frontmatter `description` | [`meta.md`](./meta.md) §四 |
| H2/H3 | 正文 `##` / `###` | kebab-case `{#id}`；ZH/EN 同 slug 用相同 id |

## 1.3 H1–H6 层级

- **H1**：`[主题]：[价值]`；不写年份
- **H2 间距**：容器 `space-y-12`；正文 H2 之间**不加** divider（E36）
- 完整可访问性与字数见 [`meta.md`](./meta.md)、[`consistency.md`](./consistency.md)

---

<a id="part-2-json-侧车三件套"></a>

# Part 2 · JSON 侧车三件套

> **共性**：Brief 决定采用/省略 → **Step 08 注册 JSON**（键 = `pageUrl` 路径）。线上组件读 JSON；md 内对应 block 被 parser 跳过。

---


<a id="part-21-tldr--核心要点"></a>

## 2.1 TL;DR / 核心要点

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

**Step 08 注册**：同步写入 `tldr-data.json`（键 = `pageUrl` 路径，如 `/zh/blog/{slug}` 或 `/tools/{slug}`）。见 [`anatomy.md`](./anatomy.md) §二·一。

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

---


<a id="part-22-faq--常见问题"></a>

## 2.2 FAQ / 常见问题

## 一、定位与作用

**FAQ** 是文章末尾的问答章节，核心作用是：

- **解答剩余疑问**：回应读者在正文中可能产生的常见问题
- **提升 SEO**：FAQ Schema 可增加搜索结果曝光（Rich Results）
- **支持 AI 引用**：结构化 FAQ 有助于 AI 系统理解和引用内容
- **延长停留时间**：解答疑虑可减少跳出率

---

## 二、通用规范

### 2.1 数量要求

| 页面类型 | 条数（中/英各） | 默认建议 |
|----------|-----------------|----------|
| **转化 hub**（首页、services、customer-stories、about、author、partnership） | **6–8** | **6** |
| **内容 hub**（tools / seo / marketing / insights / glossary / events / explore） | **6–8** | **6–7** |
| **文章页**（Tools / SEO / Marketing / Insights / Blog） | **7** | **7**（线上标准） |

**注意**：**文章页** FAQ 统一为 **7 问**（md inline，7 问）。Hub 页可为 6–8。中英同 slug 条数必须一致。

### 2.2 字数控制（搜索与 Featured Snippet 最佳实践）

全文篇幅层级见 [consistency.md §〇、§二](./consistency.md#〇字数层级硬底线-vs-建议必读)；下表为 **FAQ 答案**的常用目标，**非**刚性上限。

| 语言 | 问题长度 | 答案长度 | 统一性 | 依据 |
|------|----------|----------|--------|------|
| **中文** | 12-22 字 | 约 **60–120 字**（常用 70–100） | 同页答案不宜悬殊 | 见下方「研究依据」 |
| **英文** | 6-12 词 | 约 **40–80 词**（常用 40–60） | 同页答案不宜悬殊 | 英文按词计数 |

**研究依据（SEO/Google 最佳实践）**：

- **40-50 词（英文）为 Featured Snippet 最优长度**：Portent 研究（7,854 个段落摘要）显示，段落摘要多数为 40-55 词，超过 55 词后明显减少；**极少超过 320 字符**（Portent, 2021；Ghergich & Co./SEMrush）
- **2-3 句为宜**：段落摘要通常为 2-3 句，4 句以上极少（Portent）
- **过短**：难以满足搜索意图，易被判定为低质量
- **过长**：超出展示空间被截断，影响 CTR；Google 更偏好简洁直接的回答

**搜索优化要点**：

- **答案 40-60 词（英文）/ 70-100 字（中文）**：符合 Google 常见提取长度，利于 Position Zero
- **首句直接回答**：FAQ 答案首句应直接回应问题，便于 AI 与搜索引擎摘要
- **避免重复**：同一问答不可在多页重复标记，否则违反 Google 指南
- **Google 限制**：单条搜索结果最多展示 2 个 FAQ；权威站点更易获得展示（2023 年 8 月后 FAQ 富结果主要限于政府/健康类权威站点）

### 2.3 内容要求

- **真实问题**：基于用户实际常见问题，而非虚构
- **简洁回答**：直接回答，不冗长
- **覆盖核心主题**：覆盖页面主题相关的关键疑问
- **避免重复**：问题与正文内容不重复

### 2.4 呈现与标题阶梯

FAQ 由 `FAQ` 组件渲染，**不要**在内容里再手工加一层「区块标题」的 H2。组件内部的字号层级：

| 部分 | 样式 | 说明 |
|------|------|------|
| 区块标题（如「常见问题」） | `text-4xl md:text-5xl lg:text-6xl leading-[1.08]` | 大号 H2，与 Section 章节 H2 同级 |
| 每条问题 | `text-lg md:text-xl font-serif font-normal` | `<summary>` 内三行折叠式 |
| 答案正文 | `text-base md:text-lg text-muted-foreground leading-relaxed` | 与文章段落一致 |

**编写注意**：`answer` 仍为 HTML 字符串；请勿在答案根部包 `text-sm` / `text-xs` 等缩小整段正文；如需强调单句，使用 `<strong>` 即可。

---

## 三、Inline Markdown 格式

```markdown
<!-- block:section -->
## 常见问题 {#faq}

### 问题 1 {#faq-1}
答案正文…

### 问题 2 {#faq-2}
…
```

**文章页默认 7 问**（中英文同 slug 条数一致）。

**答案格式**：首句直接回答；**允许**站内 `<a href>`（计入正文；同 URL 全文 1 次，见 [`internal-links.md` §1.5](./internal-links.md#15-faq-内链规则)）。

---

## 四、Markdown 写法（创作 SSOT）

```markdown
<!-- block:section -->
## 常见问题 {#faq}

### 问题 1 {#faq-1}
首句直接回答。70–100 字（中文）或 40–60 词（英文）。**允许**站内链（R4 全文 1 次）。

### 问题 2 {#faq-2}
…
（共 7 问，中英文条数一致）
```

**Step 08 注册**：同步写入 `faq-data.json`（键 = `pageUrl` 路径，如 `/zh/blog/{slug}`），否则线上 FAQ 组件不渲染。见 [`anatomy.md`](./anatomy.md) §二·一。

**禁止**：在 `## 常见问题 {#faq}` 前再写一层 H2；FAQ 答案中同一 URL 出现超过 1 次（R4）。

### 4.1 Schema

FAQ 组件从 `faq-data.json` 生成 FAQPage JSON-LD；Brief 采用时 Step 08 注册 JSON。

---

## 五、FAQ Schema 最佳实践（Google）

- **真实问题**：使用用户实际会问的问题，避免虚构
- **完整回答**：答案应能真正解决问题
- **可见内容**：Schema 内容必须与页面可见内容一致
- **避免重复**：不同页面间避免 FAQ 重复
- **格式正确**：使用 JSON-LD，符合 Google 规范

---

## 六、问题来源建议

- 客服和用户反馈
- 搜索词和长尾关键词
- 正文中未覆盖的疑问
- 竞品和行业常见问题

---

## 七、常见错误

- ❌ FAQ 答案重复链同一 URL（违反 R4）
- ❌ 问题或答案过长（超出推荐范围影响 Featured Snippet 提取）
- ❌ 同一页面内答案字数差异过大（±10 字/词）
- ❌ 答案过短（无法满足搜索意图）
- ✅ Step 08 注册 `faq-data.json`，首句直接回答；内链若存在须 R4 全文 1 次
- ❌ 跨页复用「这些工具是否免费？」等模板问句（须绑定本页实体）

---

## 八、类型区分（Tools / SEO / Marketing / Insights）

### 8.1 Tools

- **问题侧重**：工具选择、功能对比、适用场景、使用门槛、定价模式
- **答案风格**：客观、可操作，突出「如何选」「适合谁」「与竞品区别」
- **数量**：中英文各 **7 问**

### 8.2 SEO

- **问题侧重**：概念定义、技术实现、与排名/索引的关系、实操步骤
- **答案风格**：专业、准确，可引用 Google 官方表述（纯文本）
- **数量**：中英文各 **7 问**

### 8.3 Marketing

- **问题侧重**：策略价值、ROI、执行门槛、与竞品策略对比
- **答案风格**：务实、可落地，侧重「是否值得做」「如何起步」
- **数量**：中英文各 **7 问**

### 8.4 Insights

- **问题侧重**：行业趋势、产品/公司解读、生态格局、实践建议
- **答案风格**：洞察型、归纳型，可适当概括正文观点
- **数量**：中英文各 **7 问**

---

## 九、研究参考（长度依据）

| 来源 | 结论 |
|------|------|
| Portent（2021） | 段落摘要 40-55 词常见；极少超过 320 字符；2-3 句为主 |
| Ghergich & Co./SEMrush | 段落摘要最优长度约 40-50 词或约 300 字符 |
| Flyrank | 40-50 词符合 Featured Snippet 常见提取长度 |
| Google | 答案应简洁、直接、基于事实；符合自然语言 |

---


<a id="part-23-references--参考文献"></a>

## 2.3 References / 参考文献

## 一、定位与作用

**参考文献**是列举文中引用来源的章节，核心作用是：

- **权威性**：引用外部文章、研究报告、权威来源，增强内容可信度
- **可追溯**：提供可点击的原文链接，方便读者深入阅读
- **Schema**：md `#references` section自动生成 Article Schema 的 citation 属性

---

## 二、通用规范

### 2.1 Markdown 列表写法

```markdown
<!-- block:section -->
## 参考文献 {#references}

- [文章标题](https://example.com/article) — 出版方，2026年。一句说明本条参考价值。
```

**Step 08 注册**：同步写入 `references-data.json`（`items[]` 字段：`title`, `url`, `source?`, `date?`, `description?`）。见 [`anatomy.md`](./anatomy.md) §二·一。

### 2.2 引用添加规则（正文中）

- **必须添加原文链接**：引用外部文章、研究报告时必须提供可点击链接
- **链接位置**：优先在被引用机构/公司名称上
- **链接样式**：`text-primary hover:underline`
- **链接属性**：`target="_blank"`、`rel="noopener noreferrer"`（正文引用不设 nofollow，便于读者溯源）
- **UTM**：正文中的引用链接使用 `addUtmToExternalLink()`，参见链接规范文档

**说明**：md `#references` section（底部列表）使用 `getExternalLinkRel()`；正文中**手动**添加的引用链接使用 `rel="noopener noreferrer"` 即可。

**链接格式示例**：

```tsx
import { addUtmToExternalLink } from "@/lib/utils";

{/* 正确：href 用 addUtmToExternalLink，rel 用 noopener noreferrer */}
<p>根据<a href={addUtmToExternalLink("https://exa.ai/blog/...")} target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">Exa</a>的分析...</p>
```

**质量检查清单**：

- [ ] 所有引用都有可点击的原文链接
- [ ] 链接使用 `addUtmToExternalLink()` 添加 UTM
- [ ] 链接样式统一（`text-primary hover:underline`）
- [ ] 链接在新标签页打开（`target="_blank"`）
- [ ] 包含 `rel="noopener noreferrer"`
- [ ] 引用内容准确、不歪曲原文意思
- [ ] 链接 URL 正确且可访问

### 2.3 references-data.json 字段

| 字段 | 约定 |
|------|------|
| `title` | 原文标题或与页面一致的译名 |
| `url` | 稳定可访问的原文链接 |
| `source` | 出版方/站点名（可选） |
| `date` | 出版或改版日期（可选） |
| `description` | 一句客观说明（可选，20–60 字） |

### 2.4 列表展示规则（中英一致）

1. **主链**：`title` 链至 `url`（经 `addUtmToExternalLink`）。
2. **来源行**：`source` / `date` 用括号展示（中文全角括号 + `，`；英文半角 + ` · `）。
3. **描述**：有 `description` 时用 ` — ` 连接。
4. **Schema**：JSON 条目映射为 Article `citation`。

### 2.5 字段填写细则

| 字段 | 约定 |
|------|------|
| `title` | 原文标题或与页面一致的译名；勿把 URL 或域名当作标题。 |
| `url` | 稳定可访问的原文链接。 |
| `source` | 机构、媒体或产品站点的常用英文名/中文名（如 Moz、Search Engine Journal），不加多余后缀。 |
| `date` | 出版或最近大改版年份/日期；动态页面可用 `持续更新`（中文）或 `Updated regularly`（英文）；仅年份可用 `2026` / `2026年`。 |
| `description` | **一句**客观说明（推荐 20–60 字）：说明数据范围、文章侧重点或为何引用，避免口号式文案；中英文各自统一是否句末加句号即可。 |

---

## 三、引用选择标准

### 3.1 总则

- **权威来源**：行业领先企业、知名研究机构、专业媒体
- **时效性**：优先 6 个月内内容
- **数据支持**：优先包含数据分析、研究结果、基准测试

### 3.2 引用分型（2026-08 起 · Marketing / Blog 策略文强制）

底部 **References / 参考文献** 只收录**事件相关**来源；**禁止**收录与本文同题、同体裁的第三方「类似文章」。

| 类型 | 是否进 References | 说明 |
|------|:-----------------:|------|
| **A — 事件 / 政策一手** | ✅ | 带明确日期的产品公告、限额调整、事故与补偿、官方 Help / Changelog / 定价页中**针对该事件或政策**的说明 |
| **B — 事件媒体报道** | ✅ | Tier 1 媒体对**具体事件**的报道（须可写清日期 + 事件，如「2026-06 Codex quota 异常与 warroom 修复」） |
| **C — 通用对照文档** | ❌ | 竞品 pricing/docs、行业对照表用的静态说明页——**正文内链即可**，不进 References |
| **D — 同题第三方文** | ❌ | 增长策略指南、Freemium 方法论、Substack/博客「Credits 增长技巧」、与本文类似的 GTM / 营销 playbook、泛化案例 roundup |

**数量**：策略 / 营销文 References **通常 3–6 条**（事件 + 必要的一手政策页）；**宁缺毋滥**，无合格事件源时可省略整个 References 节。

**正文 vs 底部列表**：

- 对比表、Benchmark、P0 数字所需的官方 docs → 正文 `addUtmToExternalLink()` 内链 + Source Map
- References 仅汇总读者「按时间线追溯事件」需要的条目

**description 写法**：须点明**哪起事件**或**哪条政策**，勿写「用于行业对照」「策略家族变体」等泛化理由（那是类型 C 的信号）。

### 3.3 按文章类型

| 类型 | References 侧重 |
|------|----------------|
| **marketing-strategy / insights** | 仅 A + B；**默认禁止** D |
| **seo-guide** | 官方指南（Google、Schema.org）+ 有日期的算法/政策更新 |
| **best-ranking / tools** | 产品官方 docs、评测、**该产品的**发布/变更；禁止跨品类市场报告套娃（见 §八） |

---

---

## 五、批量规范化（仓库脚本）

对 `content/**` 下文章 md `#references` section 条目，可运行：

```bash
node scripts/ops/normalize-references-in-json.mjs
```

作用：trim 字段、按文件语言目录（`zh`/`en`）统一 `date` 年份写法、解码引用字段中的常见 HTML 实体、校正块级 `locale`；对个别长文（如 `generative-ai-landscape`）脚本内嵌了按 `url` 匹配的 `description` 补全表。新增大批量引用时可扩展脚本中的 `EXTRA_DESCRIPTIONS_BY_REL_PATH`，或直接在 JSON 中写好 `description` 后无需改脚本。

---

## 六、适用范围

- **SEO**：技术说明、指南类页面常见
- **Marketing / Blog 策略文**：**仅事件相关引用**（§3.2）；勿用 References 堆砌同题增长文或对照用官方 docs
- **Tools**：`references-data.json` 注册 + Article Schema `citation`

---

## 七、常见错误

- ❌ 正文引用未添加可点击链接
- ❌ 链接缺少 `target="_blank"` 或 `rel`
- ❌ 引用内容歪曲原文意思
- ❌ References 收录与本文类似的第三方策略文 / 方法论（类型 D）
- ❌ References 用竞品静态 docs 充数（类型 C → 正文内链）
- ❌ `description` 只写「行业对照」「策略变体」而无具体事件/政策
- ✅ 正文引用含链接；References 仅 A + B（策略文）或对口权威源（Tools/SEO）


---

## 八、引用质量现状（2026-05-19 审计）

### 8.1 审计范围

对 105 个 EN tools pages 的全部 references block（395 条引用）进行了逐页审计，检查每条引用与页面主题的实际关联度。

### 8.2 核心发现

| 分类 | 页面数 | 占比 | 说明 |
|------|--------|------|------|
| 引用 100% 为通用模板报告（与页面主题无关） | 16 | 15% | 致命——零条对口引用 |
| 引用以通用模板为主（≥50%），仅 1-2 条对口 | 26 | 25% | 高优——对口引用被淹没 |
| 引用大部分对口但信息密度低 | 63 | 60% | 中优——以付费报告目录页为主 |
| 含有 arxiv/GitHub 等技术权威来源 | 仅 15 | 14% | 整体技术深度不足 |

### 8.3 三类错配模式

**模式 1 — 跨品类套娃（最严重）**：以下 3 条报告作为一个固定组合出现在 16 个完全不相关的页面中（从 `religion` AI 宗教工具到 `tattoo-generator` AI 纹身生成器）：

1. Grand View Research. "Conversational AI Market" (giiresearch.com) — 19 页
2. Grand View Research. "Large Language Models Market" (grandviewresearch.com) — 27 页
3. Grand View Research. "Generative AI Market" (grandviewresearch.com) — 9 页

**受影响页面**：ai-scheduling, community, directory, essay-writer, fashion, fundraising, llm, memory, note-taker, notes-generator, openclaw-alternatives, poster-generator, presentation-maker, religion, tattoo-generator, user-research

**模式 2 — 品类级摊大饼（中度）**：品类级市场报告被不加区分地复制到同品类所有页面。例如 "AI Coding Assistant Market" 被用在 agent-skills（Agent Skills 目录页）上——弱关联但不算全错。共影响 26 页。

**模式 3 — 信息密度低（轻度）**：即便引用对口，395 条中绝大多数（~90%）是 researchandmarkets / grandviewresearch 的付费报告目录页，用户点击后看到的是价格和摘要而非实质内容。仅 4.3% 引用指向 arxiv 论文，2.8% 指向 GitHub 仓库。

### 8.4 根源

引用生成逻辑疑似按大品类（audio / video / image / marketing / coding / general）分配模板引用。对于没有明确品类归属的页面（religion, tattoo-generator, fashion 等），直接用最通用的 3 条报告填充——引用作用是凑数而非提供参考价值。

---

## 九、引用质量标准（强化版）

本章替换并扩展第三节「引用选择标准」。**所有 tools pages 的 references 必须满足以下标准**。

### 9.1 第一原则：主题对口（硬底线）

**每条引用必须与页面主题直接相关。** 以下为绝对禁止：

- ❌ LLM / Conversational AI / Generative AI 等泛 AI 市场报告出现在非 LLM 品类的页面上（如 religion, tattoo-generator, fashion, memory, authentication 等）
- ❌ 跨品类报告复用（如 Affiliate Marketing Platform 报告出现在 fundraising 页面）
- ❌ 引用付费报告的目录页作为主要引用——这些是 sales pages，不是内容来源

### 9.2 来源质量层级

引用来源按权威性从高到低排列。每个 tools page 的 references 应**至少覆盖 2 个层级**：

| 层级 | 来源类型 | 适用场景 | 示例 |
|------|---------|---------|------|
| **L1 学术/技术** | arxiv, ACM, IEEE, 顶会论文 | 引用底层技术原理 | Stable Diffusion 论文、DDSP-SVC 论文 |
| **L2 官方/开源** | GitHub 仓库、官方文档、SDK 文档 | 引用产品功能、API、开源实现 | ElevenLabs API docs、DDSP-SVC GitHub |
| **L3 科技媒体** | TechCrunch, The Verge, Ars Technica, MIT Tech Review | 引用行业动态、收购、趋势 | TechCrunch 产品发布报道 |
| **L4 权威市场报告** | Gartner, IDC, CB Insights, Research and Markets（**对口品类**） | 引用市场规模、预测数据 | AI Voice Cloning Market Report（仅用于 voice-cloning 页面） |
| **L5 厂商官方** | 厂商博客、白皮书、产品发布页 | 引用产品功能、路线图 | 标注"据厂商公开资料" |

### 9.3 每页引用数量与结构

| 页面类型 | 最少引用条数 | 建议结构 |
|---------|------------|---------|
| Tools 页面（技术品类） | 3 条 | L1/L2 技术来源 ×1 + L3 媒体 ×1 + L4 市场报告 ×1（对口品类） |
| Tools 页面（营销/商业品类） | 3 条 | L3 媒体 ×1 + L4 市场报告 ×1 + L5 厂商 ×1 |
| SEO / Marketing 页面 | 按需 | 至少 1 条 L2 或 L3 来源 |

### 9.4 引用可获取性原则

- **优先免费可访问的完整内容**（arxiv 论文、GitHub README、官方文档、科技媒体文章）
- **谨慎使用付费报告目录页**（researchandmarkets.com / giiresearch.com）——这些页面仅提供摘要和价格，不是实质内容来源。仅在引用**确切对口**的市场报告时允许，且不应超过引用总数的 1/3
- **每个 URL 必须可访问**——失效链接需及时替换或移除

### 9.5 引用时效性

- 技术论文：不受时效限制（经典论文可长期引用）
- 市场报告：优先 18 个月内
- 科技媒体报道：优先 12 个月内
- 官方文档/GitHub：以当前版本为准

---

## 十、分品类引用指南

### 10.1 技术品类（image, video, audio, coding, 3d 等）

首选引用组合：
1. **1 条该品类的核心开源项目 GitHub 仓库或 arxiv 论文**（如 image-generator → Stable Diffusion 论文；voice-changer → DDSP-SVC GitHub）
2. **1 条对口市场报告**（如 voice-cloning → AI Voice Cloning Market Report）
3. **1 条科技媒体深度报道或官方技术文档**

**禁止**：用「LLM 市场报告」或「Conversational AI 市场报告」替代品类对口来源。

### 10.2 营销/商业品类（seo, marketing, affiliate, social-media 等）

首选引用组合：
1. **1 条对口市场报告**（如 affiliate-marketing → Affiliate Marketing Platform Market Report）
2. **1 条行业媒体/研究机构分析**（如 Search Engine Journal, Moz, HubSpot Research）
3. **1 条平台官方文档或案例研究**

### 10.3 泛 AI / 交叉品类（religion, fashion, fundraising 等非典型 AI 品类）

这些品类没有现成的「AI + X」市场报告。首选引用组合：
1. **1 条该品类底层 AI 技术的论文或 GitHub 仓库**（如 fashion → 虚拟试穿论文；fundraising → 投资者匹配算法研究）
2. **1 条该传统行业的数字化/科技化报告**（如 fashion → CB Insights Fashion Tech Report）
3. **1 条科技媒体关于 AI + 该领域交叉的报道**

**禁止**：用泛 AI 市场报告（LLM / Conversational AI / GenAI）填充——这些报告覆盖的是完全不同的产品市场。

### 10.4 LLM 评测品类（llm, llm-for-coding, llm-for-math, llm-for-reasoning, multimodal-llm）

这些页面天然适合引用 arxiv 论文和 GitHub 仓库。首选：
1. **1-2 条评测基准论文**（如 HELM, LMSYS Chatbot Arena, HumanEval）
2. **1 条模型技术报告**（如 GPT-4 Technical Report, Claude Model Card）
3. **1 条开源模型 GitHub 仓库**（如 Llama, Mistral）

---

## 十一、修复方案

### 11.1 修复优先级

| 优先级 | 页面数 | 说明 | 方式 | 状态 |
|--------|--------|------|------|------|
| **P0** | 16 | 引用 100% 与主题无关 | 逐页 web search 验证 → 手动替换全部引用 | ✅ 已完成（2026-05-19） |
| **P1** | 26 | 引用以通用模板为主，仅 1-2 条对口 | 删除非对口引用 → 补充 2-3 条对口引用 | ✅ 已完成（2026-05-19） |
| **P2** | 63 | 引用对口但信息密度低 | 为每页补充 1-2 条 L1/L2 技术来源 | ⏳ 待实施 |

### 11.2 P0 16 个页面逐页替换计划

| 页面 slug | 当前引用问题 | 建议引用方向 |
|-----------|------------|------------|
| religion | ConvAI + LLM + GenAI 报告 | AI 与灵性/宗教交叉研究论文、宗教科技平台报道 |
| tattoo-generator | 同上 | AI 图像生成论文（Stable Diffusion）、纹身设计趋势报道 |
| fashion | 同上 | AI 时尚市场报告（CB Insights）、虚拟试穿论文（VITON 系列） |
| memory | 同上 | 长期记忆/向量数据库论文（MemGPT, RAPTOR）、RAG 架构参考 |
| fundraising | AI Marketing + Affiliate Marketing 报告 | VC/募资科技报告、投资者匹配算法论文 |
| community | ConvAI + LLM 报告 | 社区平台市场报告（CMX/Peak Community）、Discourse CHAOSS 指标 |
| directory | 同上 | AI 工具目录 curation 研究、Product Hunt 年度报告 |
| essay-writer | ConvAI + LLM + GenAI 报告 | AI 写作辅助市场报告、学术写作 AI 伦理论文 |
| ai-scheduling | 同上 | 智能日程安排市场（Smart Scheduling Market）、时间管理 AI 研究 |
| note-taker | 同上 | AI 笔记工具市场、语音转文字技术论文（Whisper） |
| notes-generator | 同上 | AI 内容生成工具市场、知识管理/AI 写作研究 |
| poster-generator | 同上 | AI 设计工具市场报告、生成式视觉设计论文 |
| presentation-maker | 同上 | AI 演示工具市场（Pitch/Gamma 竞品分析）、信息设计研究 |
| openclaw-alternatives | 同上 | OpenClaw 官方仓库、替代品对比社区讨论 |
| user-research | 同上 | UX 研究工具市场、用户研究方法论论文 |
| llm | ConvAI + LLM + GenAI 报告 | LLM 评测标准论文（HELM, LMSYS）、开源 LLM 技术文档 |

### 11.3 P1 26 个页面替换完成记录（2026-05-19）

共修复 26 个 EN + 26 个 ZH 页面。全部从 2 条通用模板引用（ConvAI + LLM）+ 1 条弱对口引用 → 替换为 4 条主题对口引用。EN 总引用数：105 页 440 条。

**A 组：2 条通用 ConvAI/LLM 替换（9 页）**
chatbot, education, healthcare, legal, evaluation, world-model, search-indexing, web-search-api, authentication

- chatbot：新增 Rasa 对话式 AI 报告、企业对话式 GenAI 市场、AI Chatbot 市场报告，保留 Chatbot Market 预测
- education：新增 LLMs in Education 市场、AI 高等教育市场、教育大模型市场，保留 AI 教育总体市场
- healthcare：新增 AI 医疗诊断市场、可解释 AI 诊断市场、AI 医疗全局市场报告
- legal：新增 LLM 法律市场、LegalOn AI 合同审查采用报告，保留 AI 法律市场 + Technavio 法律科技
- evaluation：全部替换 → Implicator AI Top 40、Chatbot Arena、HELM（Stanford CRFM）、SWE-bench（Princeton NLP）
- world-model：保留 MIT Tech Review，新增 Google Genie、NVIDIA Cosmos、腾讯 HY-World 2.0
- search-indexing：新增 AI 搜索统计数据、Google 搜索中心文档、IndexNow 协议
- web-search-api：新增 Google Custom Search API、Brave Search API，保留 AI 搜索引擎市场
- authentication：全部替换 → Gartner IAM AI Agent 报告、IAM 市场数据、HID Global 无密码认证预测、FIDO Alliance Passkey

**B 组：完全错误品类引用替换（5 页）**
geo, animation-library, web-scraping, browser, headless-browser

- geo：全部替换 → 地理空间分析 AI 市场、多模态地理空间 AI、NASA-IBM Prithvi 基础模型、位置分析市场
- animation-library：全部替换 → AI 动画软件工具市场、AI 动画工具战略报告、Lottie（Airbnb）、Motion（Framer Motion）
- web-scraping：全部替换 → Zyte 自主数据管道、自主 AI Agent 市场、browser-use（GitHub）、Scrapy
- browser：新增 HUMAN Security Agent 流量报告、AI 浏览器代理生态，保留 AI 生产力 + 无代码 AI 市场
- headless-browser：新增 HUMAN Security 报告、browser-use、Puppeteer、Playwright

**C 组：AI Marketing + Affiliate Marketing 模板替换（8 页）**
b2b, influencer-marketing, lead-generation, linkedin, recruiting, referral-program, interview-assistant, affiliate-marketing

- b2b：新增 Forrester B2B 2026 预测、EMARKETER AI 营销投资优先、G2 需求生成报告，保留 B2B Lead Scoring
- influencer-marketing：新增 Forrester B2B 预测、Fractional Teams B2B 营销、Abstrakt B2B 趋势，保留 Creator Economy
- lead-generation：新增 DW Media 线索生成趋势 + Q2 需求生成趋势、G2 需求生成，保留 AI SDR 市场
- linkedin：新增 RelevanceAI LinkedIn Agent Top 10、Snov.io LinkedIn 工具评测、Taboola B2B 趋势，保留人才招聘市场
- recruiting：新增 Gartner 人才招聘趋势、HireVue AI 招聘报告、iCIMS AI 采用报告，保留 AI 人才招聘市场
- referral-program：全部替换 → SkyQuest 推荐营销市场、Proofmap 客户倡导技术、ReferralCandy 趋势、EMARKETER FAQ
- interview-assistant：新增 AI Career Coach 市场、QY Research AI 面试代理市场、头豹中国 AI 面试洞察、HireVue AI 招聘
- affiliate-marketing：新增 Grand View Research 联盟营销平台、TBRC AI 营销、Research and Markets 全球战略报告，保留 EMARKETER FAQ

**D 组：已有对口引用但增强 L1/L2 来源（4 页）**
story-generator, text, text-generator, productivity

- story-generator：新增 2 篇 arxiv 论文（Echoes in AI / PNAS、Creative Story Generation / ICCC 2025），保留 2 条市场报告
- text：新增 Scaling Laws for Economic Productivity（arxiv），保留 3 条市场报告
- text-generator：新增 Small LMs Outperform Humans in Creative Writing（COLING 2025），保留 3 条市场报告
- productivity：新增 Generative AI at Work（QJE, Brynjolfsson et al.）+ Scaling Laws（arxiv），保留 2 条市场报告

### 11.5 修复流程（逐页执行）

每页按以下步骤操作：

1. **读取页面 JSON** → 确认当前 references 条目
2. **Web search** → 验证候选引用来源的真实性和对口度
3. **选择 3-5 条** → 按 §9.2 来源质量层级搭配（至少覆盖 2 个层级）
4. **更新 JSON** → 用 Python 脚本替换 references items（遵循 CLAUDE.md 安全规则）
5. **检查可访问性** → 确认每个 URL 可打开

### 11.6 批量工具

对 `content/**` 下文章 md `#references` section 条目格式化，可运行：

```bash
node scripts/ops/normalize-references-in-json.mjs
```

此脚本处理格式化（trim、日期写法统一、HTML 实体解码、locale 校正），**不处理引用内容质量**。引用内容的对口度需按本规范手动逐页审核。

---

## 十二、与 TEMPLATE.md 的对齐

本文档与 `knowledge/tools/_TEMPLATE.md` §14a「参考来源质量标准」保持一致：

- 可用来源类型优先级：学术论文 > 权威市场报告 > 官方文档/GitHub > 知名科技媒体 > 厂商官方
- 明确拒绝的来源：个人论坛、中文技术社区（CSDN/掘金等）、个人博客/Medium、营销落地页、社交媒体帖子
- 同一份知识块中外链索引与延伸阅读可交叉引用，但避免同一 URL 在不同条目中重复

知识块的外链索引服务于**研究笔记**，文章的 references 服务于**读者溯源**——两者质量标准一致，但格式和粒度不同。

---


<a id="part-3-正文节型库按需选用"></a>

# Part 3 · 正文节型库（按需选用）

> 按 Brief Section Plan **只写需要的节**；勿为凑模板加空章。

---


<a id="part-31-什么是-xxx"></a>

## 3.1 什么是 XXX

## 〇、字数层级：硬底线 vs 建议（必读）

| 层级 | 项目 | 中文 | 英文 | 说明 |
|------|------|------|------|------|
| **A 硬底线** | 段落数 | ≥ 2 段 | ≥ 2 段 | 单段落为错误；段数服从厘清主题 |
| **C 软建议** | 内链 | 有自然落点时 **0–1** 个强相关内链 | 同上 | 见 §三；**无硬性条数**（Marketing M7：什么是 0–1） |
| **A 硬底线** | 绝对上限 | ≤ 450 字 | ≤ 350 词 | 防止篇幅失衡；超出须有合规/对比等理由 |
| **A 硬底线** | 绝对下限 | ≥ 150 字 | ≥ 100 词 | 防止信息空洞 |
| **C 软建议** | 篇幅 | 180–380 字 | 150–280 词 | 以说清意图为先，勿为贴数字删补 |
| **C 软建议** | 常见结构 | 2–4 段 | 2–4 段 | 多数页面 2 段即可；复杂主题可 3–4 段 |

**EN 下限 150 词的理由**：130 词仅够「一句话定义 + 一句内链」，无法完成「定义 → 价值 → 人群 → 能力 → 工作流关系」的完整信息覆盖。150 词约为中文 180 字的信息对等换算。

**内链计数排除**：`<a href>` 标签及其内容不计入篇幅统计；统计规则见 §2.4。

---

## 一、定位与作用

**什么是 XXX**是页面的**主题介绍章节**，在 TL;DR 之后、详细内容之前。其核心作用是：

- **定义概念**：清楚说明主题是什么
- **说明核心价值**：介绍工具类别、核心价值、应用领域
- **建立上下文**：说明为什么重要、适用场景、适用人群
- **引导内链**：在合适位置自然融入与主题强相关的内链

**与 TL;DR 的区别**：「什么是 XXX」是主题介绍，建立读者对领域的理解；TL;DR 是开篇价值摘要（直答 + 要点列表），侧重 actionable insight。两者侧重点不同，不应互相复制内容。参见 [Part 2.1 TL;DR](#part-21-tldr--核心要点)。

---

## 二、通用规范

### 2.1 标题格式

| 页面类型 | 中文标题 | 英文标题 |
|----------|----------|----------|
| **Tools** | 什么是[工具类型]？ | What Are [Tool Type]? |
| **SEO** | 什么是[主题]？ | What is [Topic]? |
| **Marketing** | 什么是[策略名称]？ | What is [Strategy Name]? |

### 2.2 结构模板

根据主题复杂度选择对应模板。多数 Tools 页面使用标准型；技术门槛高或概念边界模糊的类目使用扩展型。

#### 标准型（2 段）— 80% 页面适用

| 段落 | 内容 | 占比 |
|------|------|------|
| **P0 定义段** | 1) 一句话定义 → 2) 核心价值与能力 → 3) 适用人群与场景 | 55–70% |
| **P1 内链段** | 工作流/生态关系 + 内链（1–2 个），自然融入功能互补或场景关联 | 30–45% |

```tsx
// 示例：AI 变声器
<P>AI 变声器是利用人工智能实时改变声音特征的工具，能将输入语音转换为不同的音色、性别或风格。其核心价值在于降低声音处理门槛，让内容创作者无需专业录音设备即可实现声音变换。适用于直播、播客、游戏配音和社交媒体创作等场景。</P>
<P>在音频处理工具生态中，<Link href="/zh/tools/text-to-speech"><strong>AI 文字转语音工具</strong></Link>负责将文本转换为语音，<Link href="/zh/tools/voice-cloning"><strong>AI 声音克隆工具</strong></Link>负责克隆特定人物声音。与它们相比，变声器更专注于实时改变声音风格，三者可按创作需求组合使用。</P>
```

#### 扩展型（3–4 段）— 高门槛 / 边界模糊类目

| 段落 | 内容 | 适用场景 |
|------|------|----------|
| **P0 定义段** | 定义 + 核心价值 + 适用人群 | 所有页面 |
| **P1 边界段** | 与相邻品类的区分、常见误解澄清 | 概念易混淆（如 web-scraping vs crawling、agent vs chatbot） |
| **P2 误区/上下文段** | 技术选型陷阱、行业背景（可选） | 技术门槛高的类目（如 authentication、headless-browser） |
| **P3 内链段** | 工作流 + 内链 | 所有页面 |

```tsx
// 示例：网页抓取工具（边界模糊，需 3-4 段）
<P><strong>网页抓取工具</strong>泛指帮助团队自动获取网页或可下载资源并结构化的软件与服务，包含爬虫框架、无头浏览器、托管抓取 API 等。适用于需要规模化采集竞品数据、训练语料或市场情报的团队。</P>
<P>与 <strong>Web Search API</strong> 的分工：检索 API 面向托管搜索索引，返回链接与摘要；抓取工具面向指定 URL，获取完整 HTML/JSON 乃至渲染后的 DOM。二者可串联：先搜索再深读。</P>
<P>体量较大的采集任务常同时遇到反爬与 IP 封禁：速率限制、验证码、TLS 指纹都会抬高工程成本。商业产品线通常捆绑代理与自动重试；自研团队需在队列、限速与法务之间平衡。</P>
<P>与只读站内的技术 SEO 爬虫相比，通用抓取涉及跨域、鉴权与增量更新。选型时先把业务问题写成「输入 URL → 输出 schema」再挑工具。<Link href="/zh/tools/web-search-api"><strong>Web Search API 工具</strong></Link>适合搜索发现场景，二者可配合使用。</P>
```

#### 小众/新兴型（2–3 段）— 新兴概念

| 段落 | 内容 |
|------|------|
| **P0 概念段** | 概念界定 + 为什么现在重要 + 解决了什么此前未解决的问题 |
| **P1 定位段** | 与主流方案的定位差异（非功能对比，而是范式差异） |
| **P2 内链段** | 相关工具链 + 内链 |

### 2.3 段落级篇幅

同一「什么是」章节内各段落不宜出现 **3 倍以上** 长短差。标准双段结构中，定义段通常长于内链段是正常的，但避免定义段 200 字而内链段仅 15 字的极端情况。内链段应展开工作流场景描述而非仅贴链接。

### 2.4 计数规范

统计前须 `stripHtmlTags()` 去除所有 HTML 标签、`**加粗**` 标记和 `[链接](url)` 的方括号部分；合并多余空格和换行。中文按非空白字符数，英文按空格分词。

### 2.5 内容要求

- **首段**：工具/主题类别、核心价值（降低门槛/提升效率等用户收益）、适用人群、主要能力
- **后续段**：边界区分、常见误区、工作流/生态关系 + 内链（见 §三）
- **英文信息深度对等**：英文版应与中文版信息覆盖项数一致（定义、价值、人群、场景、工作流关系），而非仅字数对齐。反例：中文提了 4 个应用场景，英文只写 "suited for creators and teams" 即为信息丢失

### 2.6 英文内容原则

- 与中文**信息深度**相当，意译优先；内链句保留工作流/场景关联描述
- 避免仅为贴链的极简句（如 "For X, pair with Y"）
- 不逐字翻译中文；但信息覆盖项数应与中文一致

---

## 三、内链规范

**Tools 类目**：除本节通用规则外，已约定的相邻 Tools 速查见 [alignify-internal-links.md 附录 B](./internal-links.md#附录-b相邻-tools-速查邻居矩阵)；完整意图表见 `alignify-keywords-tools.md`。

### 3.1 位置

- 内链放在首段**之后**的独立段落中，自然融入工作流或场景叙述
- 多段结构中也可出现在第三段等位置，以阅读流畅为准

### 3.2 格式

```tsx
<Link href="/zh/tools/xxx"><strong>锚文本</strong></Link>
```

### 3.3 锚文本要求

- 使用关键词（如「AI 图片工具」），不含「Guide」「完整指南」「详细指南」等后缀

### 3.4 内链相关性原则

内链目标必须与当前主题有**强功能关联或场景关联**，避免为凑数而强行链接。

| 关联类型 | 说明 | 示例 |
|----------|------|------|
| **功能互补** | 同一工作流中上下游工具 | 音乐生成 → 视频编辑（配乐）、MV 生成（音乐+视频） |
| **同质替代** | 解决同类问题的不同工具 | 变声器 ↔ 文字转语音 ↔ 声音克隆（均为人声/语音处理） |
| **场景延伸** | 同一使用场景下的不同需求 | 视频制作：视频编辑 + 音乐生成 + 字幕生成 |

**反例（应避免）**：仅因同属「音频」大类而链接。如音乐生成 ↔ 文字转语音、声音克隆——音乐是旋律创作、后两者是人声处理，功能边界不同。

### 3.5 与「如何工作」章节的分工

「什么是」聚焦定义、价值、适用人群；「如何工作」聚焦技术原理与架构差异。

| 属于「什么是」 | 属于「如何工作」 |
|----------------|------------------|
| 工具是什么、解决什么问题 | 采用什么技术、如何实现 |
| 适用人群、应用场景 | 不同架构类型的技术差异 |
| 与相关工具的关系（内链） | 核心技术优势 |

**避免**：在「什么是」中展开技术细节；在「如何工作」中重复功能价值描述。

### 3.6 内链融入方式

**功能关联式**：说明工具间的功能关系和互补性

```tsx
<p>
  在音频处理工具生态中，<Link href="/zh/tools/text-to-speech"><strong>AI 文字转语音工具</strong></Link>负责将文本转换为语音，<Link href="/zh/tools/voice-cloning"><strong>AI 声音克隆工具</strong></Link>负责克隆特定人物的声音特征，而变声器工具则专注于实时改变声音的风格和效果。
</p>
```

**对比式**：通过对比不同工具的功能差异融入

```tsx
<p>
  与传统的<Link href="/zh/tools/video-editor"><strong>视频编辑工具</strong></Link>相比，AI 对口型工具专门针对口型同步优化。对于需要生成数字人视频的用户，可以查看<Link href="/zh/tools/avatar"><strong>AI 数字人生成工具</strong></Link>。
</p>
```

**工作流关联式**：同一创作流程中上下游工具

```tsx
<p>
  在视频与音乐创作流程中，AI 音乐生成可为<Link href="/zh/tools/video-editor"><strong>AI 视频编辑工具</strong></Link>提供背景音乐，也可与<Link href="/zh/tools/music-video-generator"><strong>AI MV 生成工具</strong></Link>配合，从音乐到视觉一体化制作。无论是视频配乐、播客片头还是商业广告，AI 音乐生成都是内容创作环节中的重要一环。
</p>
```

---

## 四、反模式（应避免）

| 反模式 | 说明 | 正确做法 |
|--------|------|----------|
| **信息空洞** | 英文仅 40–80 词，两个短句收工 | 展开至 150 词以上，覆盖定义 + 价值 + 人群 + 场景 |
| **堆砌产品名** | 在「什么是」中列举具体工具名称 | 产品推荐属于正文 H3 产品块，非「什么是」节 |
| **技术原理溢出** | 展开技术架构、算法细节、训练管线 | 属于「如何工作」区块 |
| **与 TL;DR 重复** | 将 TL;DR intro 改写凑数 | 「什么是」建立上下文和领域理解，TL;DR 直答价值 |
| **弱相关内链** | 仅因同属某大类而链接（音乐 → TTS） | 必须功能互补/同质替代/场景延伸 |
| **极简内链句** | 英文仅 "For X, pair with Y" | 保留完整工作流/场景描述，内链自然融入 |
| **单段结构** | 只有 1 段 | 必须 ≥ 2 段；首段定义 + 后续段边界/工作流（有自然落点时可内链） |
| **段落悬殊** | 定义段 200 字、内链段 15 字 | 同章内各段不宜 3 倍以上长短差；内链段展开场景描述 |
| **信息丢失** | 中文 4 个场景 → 英文 "suited for creators" | 英文版信息覆盖项数与中文一致 |

---

## 五、页面类型差异

| 类型 | 第一段重点 | 内链目标 |
|------|------------|----------|
| **Tools** | 工具类别、核心价值、应用领域、适用人群 | `/tools/` 相关页面 |
| **SEO** | 概念定义、SEO 价值、工作原理 | `/seo/` 相关页面 |
| **Marketing** | 策略定义、核心价值、适用场景 | 新文 `/blog/` 相关页；存量 `/marketing/` |

---

## 六、检查清单（创建/优化时）

- [ ] 段落数 ≥ 2（硬底线）
- [ ] 有自然落点时含强相关内链，内链段落完整描述工作流关系（**无硬性条数**）
- [ ] 篇幅在硬底线范围内（中文 150–450 字，英文 100–350 词）
- [ ] 首段覆盖：定义 + 核心价值 + 适用人群 + 主要能力
- [ ] 选择正确的结构模板（标准型/扩展型/新兴型）
- [ ] 无技术原理溢出（不抢「如何工作」的内容）
- [ ] 无产品名堆砌（不抢产品 H3 块的内容）
- [ ] 与 TL;DR 内容无明显重复
- [ ] 英文版信息覆盖项数与中文版一致
- [ ] 同章内各段无 3 倍以上长短差
- [ ] 内链符合相关性原则（功能互补/同质替代/场景延伸）

---

## 七、文档修订

| 日期 | 说明 |
|------|------|
| 2026-05-10 | 引入 §〇 硬底线/软建议分层；新增 §2.2 三种结构模板；新增 §2.3 段落级篇幅；新增 §2.4 计数规范；新增 §2.5 英文信息深度对等；新增 §四 反模式表；EN 建议下限从 130 词上调至 150 词；统一硬底线与软建议术语 |
| 2026-04-20 | 初版 |

---


<a id="part-32-通用主体节分析--场景--技术"></a>

## 3.2 通用主体节（分析 / 场景 / 技术）

> Markdown 壳与 H1–H6 见 [Part 1](#part-1-全局写法markdown--h1h6)。本节描述**非专用节型**的正文 H2/H3（Marketing 分析节、Insights 论证、SEO 实施要点、Tools 应用场景等）。

### 适用场景

- 主体论证、框架拆解、案例叙述、风险边界
- 应用场景（`###` 按场景分子块）
- 技术概述 / 如何工作（与 [3.1](#part-31-什么是-xxx) 分工：这里是原理，不是定义）

### 写法要点

| 项目 | 建议 |
|------|------|
| **首段 BLUF** | Marketing / Insights 文 H2 下首段 ≥3 句，直答本节要解决的问题 |
| **H3 粒度** | 一个 H3 = 一个可独立扫读的小论点或场景 |
| **内链** | 任务句内嵌；每段 ≤1 链（见 [`internal-links.md`](./internal-links.md)） |
| **How To 替代** | 策略/观点文用分析节表达落地，**不**套 step-1~N（见 [3.5](#part-35-how-to--如何选择可选) 适用范围） |

### 字数参考

见 [`consistency.md`](./consistency.md) §二；以说清为准，勿为凑节加空 H2。

---


<a id="part-33-best-产品-h3best-ranking"></a>

## 3.3 Best 产品 H3（best-ranking）

> **客户露出（Tier 1/2）**：[`partner-products.md`](./partner-products.md) — 商业保留/突出规则，非节写法 SSOT。

## 〇、规则层级（必读）

| 层级 | 适用 | 说明 |
|------|------|------|
| **A 硬底线** | 组件使用、产品数量、比例、字数绝对上下限 | 不可逾越，违规必须修复 |
| **B 强建议** | shortDescription 最佳区间、描述最佳区间、风格统一 | 尽量达标，偏离需有理由 |
| **C 软建议** | 差异化表达、条件推荐语气、信息密度 | 内容质量导向，持续优化 |

---

## 一、定位与作用

**产品展示**是列举具体工具/产品的章节，核心作用是：

- **产品介绍**：每个产品包含名称、图片/视频、描述、CTA 按钮
- **垂直大图布局**：图片在上、文字在下，统一卡片样式
- **差异化定位**：每款产品的描述需回答「**最适合谁**」和「**与同页其他产品的关键差异**」
- **SEO 与转化**：产品描述含关键词，CTA 引导试用

---

## 二、通用规范

### 2.1 正文 section 写法（替代 md Best 榜单 section）

**A 层硬底线**：Tools 页面的产品展示 **必须** 使用 Markdown section（H3 产品标题 + 段落 + 可选图片），禁止依赖已删除的 `BestTools.tsx`。

```markdown
<!-- block:section -->
## 2026 年最好的 {分类} {#best-{slug}-2026}

### 产品名 {#product-slug}

![产品截图](/tools/{slug}/product.jpg)

段落描述（ZH ≥100 字 / EN ≥280 字符）…
```

**图片**：`public/` 下路径；`loading="lazy"` 由组件层处理；YouTube 缩略图可用外链 URL。

### 2.2 产品数量

**A 层硬底线**：每个产品 H3 区块至少包含 **2 个产品**。单产品无法构成「排名/推荐」。

### 2.3 篇幅

#### 硬底线（A 层）

| 项目 | 中文 | 英文 | 说明 |
|------|------|------|------|
| **shortDescription 上限** | ≤ 25 字 | ≤ 50 字符 | 防止撑破卡片布局 |
| **shortDescription 下限** | ≥ 4 字 | ≥ 10 字符 | 防止无信息量（如单字"好"） |
| **产品 description 上限** | ≤ 400 字 | ≤ 800 字符 | 防止堆砌 |
| **产品 description 下限** | ≥ 100 字 | ≥ 280 字符 | 防止信息空洞，至少说清定位+功能+适用场景 |
| **同页 max/min 比例** | < 3x | < 3x | 避免极端篇幅悬殊 |

**shortDescription 额外硬底线**：不得与产品 name 重复或高度重叠。例如 name 为 "Style3D AI"，shortDescription 写 "Style3D AI Tool" 视为违规（重复产品名）。

#### 强建议（B 层）

| 项目 | 中文（建议） | 英文（建议） |
|------|-------------|-------------|
| **shortDescription** | 6–18 字 | 15–35 字符 |
| **产品 description** | 180–260 字 | 350–650 字符 |
| **风格统一** | 同页各 shortDescription 句式统一 | 同上 |

#### 软建议（C 层）

纯内容质量导向，不限字数，旨在提升读者决策效率：

| 原则 | 说明 |
|------|------|
| **差异化原则** | 每款描述必须包含：① 核心定位 ② 最适合谁（Ideal for / Perfect for）③ 与同页其他产品的关键差异点 |
| **条件推荐语气** | 使用 "Ideal for / Perfect for / Best suited for / 最适合" 等条件推荐语，而非泛泛的 "Great tool / 优秀工具" |
| **避免冗余** | 跨产品描述不重复相同的功能点表述；同页产品避免同一句式套壳（如全部以 "XXX is a powerful platform that..." 开头） |
| **通用句禁止** | 禁止 "dramatically improving efficiency" "revolutionizing the industry" "显著提升效率" "彻底改变行业" 等无信息量的空洞结尾 |
| **信息密度** | 每个词承载信息，避免 "Comprehensive Solution" "Professional Platform" "全面解决方案" 等无辨识度标签 |

详见 [§四 内容质量要求](#四内容质量要求)。

### 2.4 标题格式

- **H2 格式**：`[年份] 年最好的 [工具分类]`（中文）/ `Best [Tool Category] [Year]` 或 `[Year] Best [Tool Category]`（英文）
  - 示例：`2026 年最好的 AI 时尚工具` / `2026 Best AI Fashion Tools: Design & Styling Innovation`
  - 允许加冒号副标题提供额外语境
- **H3 格式**：`[序号]. [产品名称]：[shortDescription]`
  - shortDescription 渲染为冒号后的文本，与产品名自然衔接
  - 示例：`1. Style3D AI：3D Garment Design & Virtual Try-On`

### 2.5 布局要求

- **卡片样式**：`border-2 border-border rounded-lg p-6 bg-muted/40 shadow-md my-8`
- **图片**：居中，`w-full rounded-lg shadow-lg`，支持 `loading="lazy"`；Alt 与文件名规范参见图片 SEO 规范
- **按钮**：居中，`btn-external-link`，文案 `试试 [产品名称]`（中文）或 `Try [产品名称]`（英文）；外链自动使用 `addUtmToExternalLink` 和 `getExternalLinkRel`
- **描述容器**：`product-description` 类

---

## 三、shortDescription 格式指南

shortDescription 渲染为 `[序号]. [产品名]：[shortDescription]` 中冒号后的部分，本质是**品类标签 / 角色识别词**。

### 3.1 三种推荐格式

| 类型 | 格式 | EN 示例 | ZH 示例 |
|------|------|---------|---------|
| **功能定位型** | `[核心功能] [品类名词]` | "Real-Time Voice Changer"、"3D Garment Simulator" | "实时变声工具"、"3D 服装模拟器" |
| **差异化定位型** | `[核心优势] [品类]` | "Enterprise-Grade Code Review"、"Open-Source 3D Engine" | "企业级代码审查"、"开源 3D 引擎" |
| **场景定位型** | `[场景/人群] [功能]` | "E-Commerce Model Generation"、"Social Media Video Clipping" | "电商模特生成"、"社媒视频剪辑" |

### 3.2 禁止格式

| 反模式 | 问题 | 示例 |
|--------|------|------|
| 纯形容词堆砌 | 无信息量 | ❌ "Powerful Professional Platform" |
| 重复产品名 | 废话 | ❌ name="Style3D AI" + shortDescription="Style3D AI Tool" |
| 过度通用标签 | 无法区隔产品 | ❌ "Comprehensive Solution"、"AI Tool" |
| 功能罗列 | 短描述不应是功能清单 | ❌ "Design, Try-On, Model Generation, Analytics" |

### 3.3 同页一致性

同一页面内各产品的 shortDescription 应保持**句式结构统一**。如果第一个产品用「功能定位型」，其他产品也应用同一类型，避免混用。

---

## 四、内容质量要求

### 4.1 产品描述的必备要素

每款产品描述应在一段内包含以下三个要素（C 层软建议）：

| 要素 | 位置建议 | EN 示例 |
|------|----------|---------|
| **核心定位** | 首 1-2 句 | "Style3D AI is the most comprehensive 3D fashion design platform..." |
| **关键功能/差异化** | 中段 | "Unlike basic try-on tools, it provides full 3D garment simulation, pattern generation, and intelligent stitching..." |
| **最佳适用场景/人群** | 尾 1-2 句 | "Ideal for fashion brands and design teams requiring end-to-end 3D workflows." |

### 4.2 差异化写作原则

同页产品描述应让读者能快速区分**每款产品最适合什么场景**：

- ✅ **好**：每款以不同定位词开头，尾句给出不同的 "Ideal for"
- ❌ **差**：三款产品都以 "XXX is a powerful platform that..." 开头，尾句都是 "suitable for various needs"

### 4.3 禁止的冗余表达

| 类别 | 禁止表达 | 替代方案 |
|------|----------|----------|
| 空洞副词 | "dramatically"、"revolutionarily"、"incredibly" | 删除或用具体数据替代 |
| 万能结尾 | "This tool will significantly improve your workflow and efficiency." | 写具体的 "Ideal for..." 收尾 |
| 废话定语 | "comprehensive solution"、"powerful platform"、"innovative technology" | 写具体的功能或优势 |
| 功能堆砌 | "Supports A, B, C, D, E, F, G, and H." | 选 2-3 个最核心的差异化功能 |

### 4.4 条件推荐语气

使用 "Best for / Ideal for / Perfect for / Particularly suitable for" 等条件推荐语收尾，而非泛泛的结论。这既帮助读者决策，也符合 Google 对「有帮助的内容」的评价标准。

---

## 五、产品图片优先级

### 5.1 优先级顺序

1. **产品代表页面截图**（最高，Firecrawl 抓取）：默认使用 JSON 中的 `linkUrl`；当首页无法展示核心 UI（营销页、登录墙、功能在子路径）时，在 `scripts/data/tools-screenshot-registry.json` 中指定 `screenshotUrl`。使用本地路径 `/tools/{page-slug}/{product-slug}.jpg`（或历史 `/seo/` 路径），通过 `scripts/ops/screenshot-tools-products.py` 批量抓取。截图配置 `fullPage: false`（仅首屏，非全页）。
2. **官方演示视频**：仅当产品无独立官网可截图，或产品本身是视频型工具（如 Nano Banana）时使用。此时 `imageSrc` 使用 YouTube 缩略图 URL，同时保留 `youtubeUrl` 字段供点击跳转。
3. **已有本地截图**：从现有截图库复用。
4. **通用图片**：以上均不可用时的最后手段。

### 5.2 YouTube 缩略图规则

- **YouTube 缩略图 URL**：`https://img.youtube.com/vi/[VIDEO_ID]/maxresdefault.jpg`
- **不应滥用 YouTube 缩略图**：如果产品有真实官网，优先使用 Firecrawl 首页截图，而非 YouTube 视频缩略图。YouTube 缩略图仅在以下情况使用：
  - 产品官网就是 YouTube 视频（无独立网站）
  - 产品是纯视频/演示类工具
  - 产品官网无法正常抓取（如需要登录、反爬严格）
- **现有 YouTube 缩略图存量**：109 个产品当前使用 YouTube 缩略图作为主图（详见 `knowledge/tools/screenshot-audit-youtube-2026-05.md`），分阶段迁移为 Firecrawl 首页截图。

### 5.3 Firecrawl 截图规范

| 参数 | 值 | 说明 |
|------|-----|------|
| `fullPage` | `false` | 仅截首屏（viewport），非全页截图 |
| `quality` | `90` | JPEG 质量（推荐 90；最低 85） |
| 输出格式 | `.jpg` | 统一使用 JPEG |
| 命名规则 | `{product-slug}.jpg` | 小写、连字符分隔、无 vendor 前缀 |
| 存放路径 | `public/tools/{page-slug}/{product-slug}.jpg` | 按页面分组 |

**独立使用视频预览**（非 BestTools）：参见 [product-screenshots.md](./product-screenshots.md)

---

## 六、Markdown 产品块示例

```markdown
<!-- block:section -->
## 2026 年最好的 [工具类型] {#best-tools}

### 1. [产品名]：[核心优势] {#product-slug}

[100–400 字中文 / 280–800 字符英文描述。核心定位 + 关键差异 + 最佳场景。]

![alt 文本](/tools/{page-slug}/{product-slug}.jpg)
```

---

## 七、迁移检查清单

- [ ] md Best 榜单 section已正确导入
- [ ] 所有产品数据完整（id, name, shortDescription, imageSrc, linkUrl, description）
- [ ] shortDescription 符合 A 层硬底线（10-50 字符 EN / 4-25 字 ZH；不重复产品名）
- [ ] 产品描述符合 A 层硬底线（280-800 字符 EN / 100-400 字 ZH）
- [ ] 同页 max/min 描述比例 < 3x
- [ ] 每款描述包含：核心定位 + 关键差异 + 最佳适用场景
- [ ] 图片路径正确且文件存在于 `/public/tools/[page-name]/`
- [ ] YouTube 视频 ID 正确（如适用）
- [ ] 产品描述中无 `<Link>` 组件
- [ ] 同页 shortDescription 风格统一

---

## 八、常见错误

- ❌ 图片文件不存在
- ❌ 产品描述仍含内链
- ❌ 按钮文案使用「访问官网」而非「试试 XXX」
- ❌ H3 标题在卡片外
- ❌ **图片不显示**：检查 `public/tools/{page-slug}/` 路径与 `imageSrc` 文件名
- ❌ 使用原始 HTML 替代 md Best 榜单 section
- ❌ shortDescription 与产品名重复
- ❌ shortDescription 为纯形容词堆砌（"Powerful Professional Platform"）
- ❌ 多款产品描述套用同一模板仅替换关键词
- ❌ 产品描述以 "dramatically improving efficiency" 等空洞句结尾
- ✅ 使用 md Best 榜单 section，垂直大图布局，shortDescription 信息密集，描述区隔清晰

---

## 九、图片字段（md 产品块）

正文产品块使用 Markdown 图片语法 `![alt](/tools/{page-slug}/{product}.jpg)`；YouTube 预览见 [product-screenshots.md](./product-screenshots.md)。

---

## 十、文档修订

| 日期 | 说明 |
|------|------|
| 2026-02-11 | 初版 |
| 2026-05-10 | 全面重写：引入 A/B/C 三级规则分层；shortDescription 上限从 15 字符放宽至 50 字符（硬）/ 35 字符（软），增加下限和格式指南；描述增加 280 下限和 800 上限（硬），保留 350-650 为软建议；新增 §三 shortDescription 格式指南、§四 内容质量要求（差异化原则、条件推荐、反模式） |

---


<a id="part-34-对比表格"></a>

## 3.4 对比表格

## 〇、两种 JSON block type

Table 组件通过 ArticleFromJson 以两种 JSON block type 调度：

### 1. `comparisonSection`（推荐，最常用）

```json
{
  "type": "comparisonSection",
  "h2Id": "best-tools-comparison",
  "h2Text": "{工具类型}对比",
  "introHtml": "以下是主流{工具类型}工具的对比...",
  "table": {
    "toolType": "AI图片工具",
    "toolTypeEn": "AI Image Tools",
    "columns": ["功能类型", "核心特点", "主要应用场景", "定价模式"],
    "items": [
      {
        "toolName": "产品名",
        "coreFeatures": "关键词1、关键词2、关键词3",
        "bestFor": "最适合场景",
        "pricing": "定价",
        "integrations": "扩展信息"
      }
    ]
  }
}
```

**字段说明**：
- `h2Id` / `h2Text`：H2 标题（优先使用 `h2Text`，fallback `title`）
- `introHtml`：引导段落（优先使用 `introHtml`，fallback `introduction`）
- `table.items`：**嵌套在 `table` 下，不是顶层字段**

### 2. `table`（可选 H2 + intro）

```json
{
  "type": "table",
  "id": "optional-anchor",
  "title": "可选 H2 标题",
  "introduction": "可选引导段",
  "table": {
    "items": [...]
  }
}
```

**区别**：`title` 和 `introduction` 均可选，无则直接渲染表格。

### 3. `html` 块中手写 Table 组件

在 `html` block 中直接使用 React `<Table>` 组件的三种模式（见 §二）。适用于无法用 JSON 结构化的场景。

---

## 一、字数与规范层级：硬底线 vs 建议（必读）

| 层级 | 适用 | 说明 |
|------|------|------|
| **A 硬底线** | bestFor/pricing/toolName 不得为空、coreFeatures 每条 2–4 个关键词、items ≥ 2 条、无空 intro、列结构统一 | 不因「样式化」放宽 |
| **B 强建议** | H2 标题含「对比」/ `Comparison`、intro 段落存在、列标题含语义、5 列扩展语义明确 | 跨页格式一致 |
| **C 软建议** | 每表 4–8 条 items、ZH/EN 页面对齐、同类型工具扩展列语义统一 | 以信息密度与可读性为先 |

**一致性重新定义**：跨页优先对齐 **列数、列标题语义、H2 格式、intro 段落存在性**；条目数量与 coreFeatures 个数值允许在建议区间内随工具品类复杂度浮动。

---

## 二、定位与作用

**对比表格**是展示多款工具/产品核心差异的章节，核心作用是：

- **快速对比**：一屏内对比工具名称、核心特点、应用场景、定价
- **移动端友好**：外层 `overflow-x-auto`，小屏横向滚动查看全表
- **SEO 与可访问性**：表格含 caption、scope 等属性

---

## 三、Table 组件三种数据传入模式

`Table` 组件本身支持三种 Props 模式（通过 `renderTable()` 在 ArticleFromJson 中自动调用）：

**用法 A：items 格式**（兼容原 ComparisonTable）
- `items`：`{ toolName, coreFeatures, bestFor, pricing?, integrations? }[]`
- `toolType`、`toolTypeEn`：工具类型名称（用于 caption）
- `columnHeaders`：可选，自定义列标题

**用法 B：columns + data**（通用数据驱动）
- `columns`：`{ key, header, align?, className?, render? }[]`
- `data`：`Record<string, any>[]`
- `caption`：表格描述（SEO）

**用法 C：children**（自定义内容）
- 包裹原生 `<table>`，适用于完全自定义结构

**导入**：`import Table from "@/components/Table";`

---

## 四、表格列结构（统一规范）

**同类型 Tools 页面必须保持列数、列标题、内容格式一致**。

### 3.1 标准 4 列（必选）

| 列 key | 中文标题 | 英文标题 | 内容规范 |
|--------|----------|----------|----------|
| toolName | 工具名称 | Tool Name | 产品名称，用 `<strong>` 标注 |
| coreFeatures | 核心特点 | Core Features | 2–4 个关键词，中文顿号（、）分隔 |
| bestFor | 主要应用场景 | Best For | 2–4 个场景，**必填**，不空 |
| pricing | 定价模式 | Pricing | 订阅制/按量付费/免费/待定，**必填**，无则填「待定」 |

### 3.2 可选第 5 列（扩展列）

仅当工具类型有明确、统一的附加维度时使用，且须在 `columnHeaders` 中明确命名：

| 列 key | 中文标题示例 | 适用场景 |
|--------|--------------|----------|
| integrations | 处理方式 | 变声器（实时/非实时） |
| integrations | 单张成本 \| 处理速度 | 虚拟家居陈设等按张计费工具 |
| integrations | 生成速度 | 头像生成等强调处理时间的工具 |

**要求**：同类型页面使用相同扩展列语义；若无法统一，则采用标准 4 列。

### 3.3 内容规范

| 字段 | 规范 | 层级 |
|------|------|------|
| toolName | 产品名称，**不得为空** | **A** |
| coreFeatures | 2–4 个关键词，中文顿号（、）分隔，英文逗号分隔；**不得为空** | **A** |
| bestFor | 2–4 个应用场景，**不得为空**；无明确场景时填「多种场景」 | **A** |
| pricing | **不得为空**；无数据时填「待定」或「免费」；可简写如「订阅制」「按量付费」 | **A** |
| items | 每表 **≥ 2 条** | **A** |

### 3.4 文案规范

| 项目 | 中文 | 英文 | 层级 |
|------|------|------|------|
| H2 标题 | [工具类型]工具对比（须含「对比」） | [Tool Type] Tools Comparison（须含 `Comparison`） | **B** |
| H2 可选后缀 | 选择最适合你的 | Choose the Best for You | C |
| intro 段落 | 以下是主流[工具类型]工具的对比，帮助您快速了解各工具的特点、应用场景和适用性： | Below is a comparison of top [tool type] tools to help you quickly understand each tool's features, use cases, and suitability: | **B** |
| intro 必须存在 | 不得为空 | 同左 | **B** |

### 3.5 条目数量（建议）

| 项目 | 建议 | 层级 |
|------|------|------|
| 每表 items | 4–8 条 | C |
| 同页 bestFor 个数 | 各条目宜 2–4 个场景，不宜出现 1 个 vs 6 个悬殊 | C |

---

## 五、样式要求

- **容器**：`min-w-full border-collapse border border-border`
- **表头**：`bg-muted`
- **单元格**：`border border-border p-4 text-left font-semibold`
- **响应式**：组件自动处理移动端折叠

---

## 六、Table 实现示例

```tsx
<Table
  toolType="AI图片工具"
  toolTypeEn="AI Image Tools"
  items={[
    {
      toolName: "AI图片生成",
      coreFeatures: "根据文本描述或参考图像自动生成新图像",
      bestFor: "概念设计、艺术创作、营销素材",
      pricing: "订阅制/按量付费",
      integrations: "Midjourney, Flux, Stable Diffusion"
    },
    // ...
  ]}
  columnHeaders={{
    toolName: "功能类型",
    integrations: "代表工具"
  }}
/>
```

---

## 七、Table + children 实现示例（自定义内容）

```tsx
<Table caption="自定义表格">
  <table className="min-w-full border-collapse border border-border">
    <thead>
      <tr className="bg-muted">
        <th className="border border-border p-4 text-left font-semibold">工具名称</th>
        <th className="border border-border p-4 text-left font-semibold">核心特点</th>
        <th className="border border-border p-4 text-left font-semibold">主要应用场景</th>
        <th className="border border-border p-4 text-left font-semibold">定价模式</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td className="border border-border p-4"><strong>工具A</strong></td>
        <td className="border border-border p-4">...</td>
        <td className="border border-border p-4">...</td>
        <td className="border border-border p-4">...</td>
      </tr>
    </tbody>
  </table>
</Table>
```

---

## 八、适用范围

- **Tools**：工具对比表格 → Table
- **SEO**：HTML 标签参考、数据表 → Table
- **SEO/Marketing**：纯文字或列表为主时，一般不使用表格

---

## 九、检查清单（创建/优化时）

- [ ] **A 层**：所有 items 的 toolName、bestFor、pricing 非空；coreFeatures 每条 2–4 个关键词（中文顿号、英文逗号分隔）；每表 ≥ 2 条 items
- [ ] **A 层**：introHtml 非空
- [ ] **A 层**：所有 items 字段名统一（仅 toolName/coreFeatures/bestFor/pricing，可选 integrations）
- [ ] **B 层**：H2 标题含「对比」/ `Comparison`
- [ ] **B 层**：列标题语义与数据一致（扩展列须在 columnHeaders 中命名）
- [ ] **C 层**：每表 items 在 4–8 条建议区间或能说明理由
- [ ] **C 层**：ZH/EN 两版页面均有 comparisonSection
- [ ] **C 层**：同类型工具页面的扩展列语义一致
- [ ] 表头列数与数据列数一致
- [ ] pricing 格式统一（无「免费试用」与「Freemium」混用等情况）

## 十、常见错误

- ❌ 未导入 Table
- ❌ 表格内容与产品详情重复
- ❌ 列标题与内容不一致
- ❌ bestFor 或 pricing 为空（应填「待定」或「多种场景」）
- ❌ coreFeatures 为 0-1 个关键词或为空
- ❌ 同类型页面列数、列标题不一致
- ❌ intro 段落缺失
- ✅ 使用 Table，列结构统一，内容格式一致

---


<a id="part-35-how-to--如何选择可选"></a>

## 3.5 How To / 如何选择（可选）

## 适用范围（先读）

**How To / 如何选择不是全站默认章节。** 只有「选型/操作类」内容才需要：

| 类型 | 是否适用 | 说明 |
|------|---------|------|
| Tools 选型文（best-ranking） | 适用 | 从分叉点开始选、核验、落地 |
| SEO 操作文 | 视题材 | 偏实施步骤（怎么配置、怎么验证） |
| Marketing / Blog 策略文 | **不适用** | 策略文用分析 + 判断表达落地（如「我的判断」「组合拳」），**不套 step-1~N 步骤** |
| Insights 分析文 | **不适用** | 分析结论 + 风险边界即可 |

**判据**：问自己「读者读完前面章节，是否还需要一条从 A 到 B 的决策路径」——没有明确分叉就删除 How To，不要为凑章节数量而加。2026-08 rate-limit-reset 实践：策略文硬套 4 步 how-to 被判定为模板残留并移除。

---

## 目录

1. [Part 1 · 定位与分工（与 TLDR 的关系）](#part-1--定位与分工与-tldr-的关系)
2. [Part 2 · 结构规范（位置 / 标题 / 步骤数量）](#part-2--结构规范位置--标题--步骤数量)
3. [Part 3 · 写作规则（去模板 / 决策分叉 / 内容优先）](#part-3--写作规则去模板--决策分叉--内容优先)
4. [Part 4 · 正文渲染结构（H2 + intro + H3 步骤，无 Schema）](#part-4--正文渲染结构h2--intro--h3-步骤无-schema)
5. [Part 5 · 页面类型差异](#part-5--页面类型差异)
6. [Part 6 · 验收与审计](#part-6--验收与审计)
7. [Part 7 · 常见错误速查](#part-7--常见错误速查)

---

<a id="part-1--定位与分工与-tldr-的关系"></a>

# Part 1 · 定位与分工（与 TLDR 的关系）

> **Last updated**: 2026-08-08
> **实践来源**：2026-08 tools 全站 TLDR 去模板化 + howTo 试点（`chatbot`、`directory`、`video-clipping`）

## 一、定位

**How To（如何选择）是页面结尾的「决策路由」章节**：把「从哪几个分叉点开始选、每一步要核验什么」拆成可执行步骤。它位于正文末尾（Conclusion 之前），给读者一条从「产品认知」到「做出选择」的路径。

## 二、与 TLDR 的分工（不重复）

| | TLDR（开篇） | How To（结尾） |
|---|-------------|---------------|
| **回答** | 「这个工具是做什么、该选谁」的**结论摘要** | 「具体怎么选」的**步骤路径** |
| **形式** | intro 直答 + 4–5 条要点（可独立抽取） | intro 给分叉 + 3–5 步递进动作 |
| **决策锚点** | 与 HowTo **共享同一分叉**（真相源 / 技术路线 / 交付物…） | 与 TLDR **共享同一分叉** |
| **表述** | 结论式短句（`Intercom fits product inboxes…`） | 判断式步骤（`Locate the truth source` → 核验条件） |
| **重复** | 不复制 HowTo 的步骤文字 | 不复制 TLDR 的要点文字 |

**一句话分工**：TLDR 给答案，How To 给路径；两者锚定同一个分叉，但一个讲「该选谁」，一个讲「怎么确认」。

## 三、与正文的关系

- 不与「什么是 / What are」（主题介绍）重复——How To 是决策，不是概念。
- 不与 BestTools 产品卡重复——How To 的步骤里可点名工具，但不重述产品卡描述。
- 不与结论重复——How To 是「怎么选」，结论是「选型后的落地要点」。

---

<a id="part-2--结构规范位置--标题--步骤数量"></a>

# Part 2 · 结构规范（位置 / 标题 / 步骤数量）

> **Last updated**: 2026-08-08

## 一、位置

正文末尾，**结论之前**（Tools 页面常见顺序见 [`templates.md`](./templates.md#part-2-tools--best-ranking) §2.4）：

```
… 应用场景 → 如何选择 → 结论 → FAQ
```

## 二、H2 标题与 id

| 项目 | 中文 | 英文 |
|------|------|------|
| **H2 标题** | `如何选择 [AI] [工具类型]` | `How to Choose [AI] [Tool Type]` |
| **示例** | 如何选择 AI 变声器 | How to Choose AI Voice Changer |
| **block id** | `how-to-choose-{slug}` | `how-to-choose-{slug}` |

**id 规则**：必须 `how-to-choose-{slug}`（如 `how-to-choose-chatbot`），**禁止**全站统一 `"id": "how-to-choose"`（防锚点冲突）。

## 三、步骤数量：3–5 步，不硬性 5

步骤数量**按主题复杂度决定**，不强制 5 步：

| 主题复杂度 | 步数 | 说明 |
|-----------|------|------|
| 单一品类、单一分叉 | 3–4 步 | 分叉 → 核验 → 落地即可 |
| 多子域、多分叉（代理+API+合规+管线等） | 5 步 | 覆盖完整决策链 |

**硬底线**：≥3 步；「步骤少于 5 个」不再视为错误，但少于 3 个视为 stub。

## 四、introduction（引导段）

- **第一句给决策分叉**：点明读者要做的第一个关键取舍（`The fork is where truth lives — a product inbox, a ticket queue, or a marketing landing page`）。
- **第二句说明步骤职责**：`These steps route that decision first, then check…`。
- 禁止模板开头（见 Part 3 黑名单）。
- 篇幅：**内容优先**，参考 40–90 字 / 40–90 词，说清分叉即可，不硬凑。

---

<a id="part-3--写作规则去模板--决策分叉--内容优先"></a>

# Part 3 · 写作规则（去模板 / 决策分叉 / 内容优先）

> **Last updated**: 2026-08-08
> **实践来源**：tools 全站 TLDR 去模板化标准迁移 + howTo 试点反馈（用户明确「内容优先，不要为字数牺牲信息」）

## 一、步骤标题：动词开头 + 分叉短语，禁止泛化祈使

标题 = **动词开头的决策分叉短语**，让读者一眼看到这一步在判断什么：

| 优秀（动词 + 分叉） | 劣质（泛化祈使，禁止） |
|--------------------|----------------------|
| `Locate the truth source` / `定位真相源` | `Evaluate Technical Requirements` / `评估技术要求` |
| `Route by source type` / `按素材类型路由` | `Consider Budget and Pricing` / `考虑预算和定价` |
| `Pick the curation model` / `选策展模型` | `Determine Your Purpose` / `确定使用目的` |
| `Lock the handoff` / `锁死移交` | `Assess Usability` / `评估易用性` |

**禁用的泛化祈使**（无分叉信息，跨页复用 = 模板）：`Evaluate` / `Consider` / `Assess` / `Determine` / `Check`（单独成步且无具体对象时）。

## 二、步骤描述：四条要素，内容优先

每步描述为**单一段落**，至少包含以下要素（不要求每步全有，但整节覆盖）：

1. **决策分叉**：这一步在 A 与 B 之间怎么取舍（`Product inbox → Intercom; SLA queue → Zendesk AI`）。
2. **判断信号**：读者怎么知道自己属于哪一档（`if your renewals bill in Stripe…`）。
3. **约束条件**：选了之后要满足什么才成立（`verify 9:16 export presets, batch limits…`）。
4. **可测指标 / 成本 / 误区**：一个能验收的数字或常见坑（`containment rate and time-to-first-response`；`orphaned chats burn trust faster than a slow queue`）。

**要点**：
- 可点名 ≥2 个真实产品/机制锚点（Intercom、Zendesk AI、OpusClip、Toolify…），但不重述产品卡。
- 段落式，**禁止 `<ul>` 列表**（见原规范 3.1 保留）。
- **内容优先**：篇幅以讲透为准，不为凑字数增删信息（EN 参考 35–90 词 / ZH 参考 60–140 字，作为质检参考而非硬底线）。
- 与 TLDR 同一分叉、不同表述：TLDR 写结论，How To 写判断过程。

## 三、去模板黑名单（must be 0）

| 信号 | 示例 | 替代 |
|------|------|------|
| description 泛模板 | `Select the right X based on A, B, C` / `选择合适的 X 需要综合考虑 A、B、C` | 第一句给分叉 |
| description 数步数 | `Follow these 5 steps…` / `以下五步…` | 第二句给步骤职责 |
| 标题泛祈使 | `Evaluate…` / `Consider…` / `Assess…` / `确定使用目的` | 动词 + 分叉短语 |
| 步骤标题跨页复用 | `Consider budget and pricing`（同标题多页） | 每页分叉不同 |
| 步骤描述一句箭头 | `A→B` / `A → B；C → D` 无展开 | 补判断信号与约束 |
| 与 TLDR 复制 | 步骤文字 = TLDR 要点文字 | 换判断式表述 |

## 四、与 TLDR 的分叉一致性

每篇 howTo 的**首个分叉应与 TLDR 的选型槽锚点一致**（真相源 / 技术路线 / 交付物 / 交互模式…），但表述为「步骤判断」而非「要点结论」。审计时核对两者锚点是否同一分叉。

---

<a id="part-4--正文渲染结构h2--intro--h3-步骤无-schema"></a>

# Part 4 · 正文渲染结构（H2 + intro + H3 步骤，无 Schema）

> **Last updated**: 2026-08-08
> **变更**：2026-08-08 移除 HowTo JSON-LD Schema（Google 已停用 HowTo rich results）。`howto-schema.ts`、`markdown-doc.ts` 的 schema 注入逻辑、`HowToChoose` 组件引用均已删除；`HowToChoose.tsx` 组件在部署仓不存在。How To 章节由 Markdown 正文直接渲染。

## 一、Markdown 结构（唯一真相源）

```md
<!-- block:section -->
## How to Choose [AI] [Tool Type] {#how-to-choose-{slug}}

[intro 段：分叉句 + 步骤职责]

### [Step1 标题] {#step-1-id}

[步骤 1 段落：分叉 / 判断信号 / 约束 / 可测指标]

### [Step2 标题] {#step-2-id}

[步骤 2 段落]
…
```

- **H2**：`如何选择 [AI] [工具类型]` / `How to Choose [AI] [Tool Type]`，id 用 `how-to-choose-{slug}`（禁止全站统一 `how-to-choose`）
- **intro 段**：H2 下第一个段落，按 Part 3（分叉 + 步骤职责）
- **步骤**：每步一个 `###` + 单一段落；`markdown-doc.ts` 会把 `###` 解析为 subSection 渲染
- **无 script / childrenHtml**：不再插入 `application/ld+json` HowTo 脚本

## 二、frontmatter 不再需要 howTo 字段

- **Markdown 版**：如何选择内容全部在正文（H2 + intro + H3 步骤），**frontmatter 禁止 `howTo:`**（E44）。历史遗留须清理；跑 `audit-frontmatter.py` Fail。
- **JSON 版（已废弃）**：`howToChoose` block 与 `HowToChoose.tsx` 组件仅存在于旧 JSON 体系；Markdown 内容不使用。

## 三、步骤标题格式

见 Part 3（动词开头 + 分叉短语），`###` 标题与 TLDR 分叉一致。

---

<a id="part-5--页面类型差异"></a>

# Part 5 · 页面类型差异

> **Last updated**: 2026-08-08

| 页面类型 | 特有规则 |
|----------|---------|
| **Tools** | 可点名具体工具与选择建议（Intercom、OpusClip、Toolify…）；步骤覆盖选型分叉、核验与落地 |
| **SEO** | 偏实施步骤（怎么配置、怎么验证），可含 HowTo 但不重述技术正文；纯文字 |
| **Marketing** | **仅方法驱动型设置**（keyword-research、localization-strategy 等）；策略判断/观点文（rate-limit-reset 类）**不设**，落地用分析节表达。设置时禁止链接、产品名、工具名，用通用表述——见 [`templates.md`](./templates.md#part-3-marketing) §3.2 |

页面类型的 section 顺序与内链分布细则见 [`templates.md`](./templates.md) Part 2–3 与 [internal-links.md §3.1.5](./internal-links.md#135-tools-内链均衡分布阅读体验优先--锚文本规范--跨板块预留)。

---

<a id="part-6--验收与审计"></a>

# Part 6 · 验收与审计

> **Last updated**: 2026-08-08

## 一、必跑命令（部署仓）

```bash
npm run verify:content-json    # 校验 frontmatter 与 block 标记
npm run build
```

> **HowTo Schema 已移除（2026-08-08）**：Google 已停用 HowTo rich results 展示，且 Markdown 版内容由正文 H2 + H3 步骤直接渲染。不再生成 `application/ld+json` HowTo 脚本，`howto-schema.ts` 已删除，`audit:howto-choose`（JSON 版）不再适用 Markdown 内容。

## 二、howTo 专用审计（部署仓）

`scripts/permanent/audit-howto-tools.mjs` 检查：

| 维度 | 标准 |
|------|------|
| description 模板信号 | `select-right` / `based-on-list` / `follow-n-steps` / `choosing-right` / 副词模板 = 0 |
| 步骤标题泛化 | `evaluate` / `consider` / `assess` / `identify` / `determine` 等泛化祈使出现率尽量低 |
| 步骤标题跨页复用 | 同标题 ≥4 页 = 模板信号，须整改 |
| 步骤数量 | ≥3 步 |
| 步骤 stub | 每步 description 有实质内容（非 `A→B` 箭头式） |
| 与 TLDR 分叉一致 | howTo 首个分叉与 TLDR 选型槽锚点一致 |

**批次流程**（对齐 TLDR 实践）：读正文提取分叉 → 写 EN+ZH（分叉一致、表述不同）→ 审计 → 合入 → `verify:content-json`。

---

<a id="part-7--常见错误速查"></a>

# Part 7 · 常见错误速查

> **Last updated**: 2026-08-08

| 编号 | 症状 | 修复 |
|------|------|------|
| H1 | frontmatter 仍保留 `howTo:` 块 | E44 禁止；须删除并跑 `audit-frontmatter.py`；正文（H2+intro+H3 步骤）是唯一真相源 |
| H2 | 步骤过短（stub） | 每步段落有实质判断信号；勿写 `A→B` 一句箭头式 |
| H3 | H2 id 泛化 | 用 `how-to-choose-{slug}`，勿全站 `how-to-choose` |
| H4 | intro 泛模板 | `Select the right X based on…` / `Follow these N steps` → 首句给分叉 |
| H5 | 标题泛化祈使 | `Evaluate…` / `Consider…` / `Assess…` / `确定使用目的` → 动词 + 分叉短语 |
| H6 | 与 TLDR 复制 | 步骤文字 ≠ TLDR 要点文字；同一分叉、判断式表述 |
| H7 | 步骤少于 3 个 | ≥3 步；按主题复杂度 3–5 步 |
| H8 | body 残留 HowTo JSON-LD script | 已废弃；删除 `<!-- childrenHtml -->` 中 `"@type": "HowTo"` 的 script 块 |

---

## 与其他文档的关系

- **[templates.md Part 2](./templates.md#part-2-tools--best-ranking)**：Tools 特有规则仅保留「可含工具名 + 标题示例」，其余指向本文件。
- **[templates.md Part 3 §3.2](./templates.md#part-3-marketing)**：Marketing 特有规则（禁产品名/链接）见上文 [Part 5 · 页面类型差异](#part-5--页面类型差异)。
- **[rules/README.md](./README.md)**：组件索引表指向本文件。
- **common-errors.md**：howTo 相关条目指向本文件，长期以本文为准。

---



---

<a id="part-4-结论"></a>

# Part 4 · 结论

> **渲染**：md 正文 `## 结论 {#conclusion}`；FAQ 在其后由页底 `FAQ.tsx` 全局渲染。  
> **内链专规**：本节 §4.4；全站规则见 [`internal-links.md`](./internal-links.md)。  
> **篇幅数字索引**：[`word-counts.md`](./word-counts.md) · [`consistency.md`](./consistency.md)

<a id="part-41-定位与作用"></a>

## 4.1 定位与作用



**Conclusion** 是正文的收尾章节，核心作用是：

- **重申核心论点**：简明回顾文章主要观点和价值
- **归纳支撑要点**：总结正文中的关键工具、策略或解决方案
- **回答「所以呢？」**：说明内容对读者的意义
- **回答「下一步？」**：提供 CTA 或行动建议（可选）

**SEO 价值**：结论是读者离开前的最后接触点，约 70% 读者根据结论决定是否分享或互动；精心设计的结论可提升页面停留时间 20-30%、转化率 15-25%。

**第一原则（高于一切数字）**：结论是**有论证的归纳**，不是工具名罗列，也不是凑字数的段落填充。删掉任何支撑性论据（数据、价格、权衡逻辑）只留断言，是失真的精简，违反本规范。

---

<a id="part-42-通用规范"></a>

## 4.2 通用规范



## 4.2.1 位置与顺序

**结论与 FAQ 的相对顺序（A 层）**：若页面**同时**包含结论与 FAQ → 结论必须在 FAQ **之前**（How To → Conclusion → FAQ → References 为常见顺序，中间节可增减）。

- 在 md `<!-- block:section -->` 数组中，结论 section 必须是 **FAQ 之前最后 / 倒数第 2 个非 References section**
- 违反即 P0 级错误，一票否决

## 4.2.2 标题格式

| 语言 | 标题 | 锚点 id |
|------|------|---------|
| 中文 | 结论 或 总结 | `conclusion` |
| 英文 | Conclusion | `conclusion` |

**锚点规范**：`id` 固定为 `"conclusion"`（勿使用 `article-conclusion`、`conclusion-section` 等变体）。历史页面如用 `{#section-9}` 等非标准锚点，优化时统一改为 `{#conclusion}`。

## 4.2.3 篇幅（软约束 · 内容优先）

> **定位说明**：篇幅区间是 **C 层软建议**（见 [section-consistency §〇](./consistency.md)），**不是硬性红线**。审校与生成时**优先看内容**：论证完整、信息对等、无注水 > 字数达标。**切勿为贴数字删补句式**；跨页优先对齐语气与结构，正文字数允许随主题难度浮动，不强制逐字相等。

| 语言 | 参考区间 | 结构 |
|------|---------|------|
| **中文** | 约 **180–320 字** | **常见 2–4 段**；单段宜 2–5 句 |
| **英文** | 约 **120–220 词** | 同上 |

**约束边界（何时才需要处理字数）**：

- **仅在「很离谱」时调整**：中文 ≥500 字或 ≤120 字、英文 ≥300 词或 ≤80 词（视频 spoke 过短例外见 §2.3.3），且确认是**注水冗余**或**信息缺失**时才动手
- 落在参考区间外但**论证完整、信息对等、无注水**的结论，**视为合格**，不需要为凑字数增删
- 工具密集页（工具数 ≥6）直接按 §2.3.1 例外区间判断，无需回到 320 字常规区间
- **计数口径**：中文字数按**可见全字符**（含标点、英文工具名、数字）统计，与扫描脚本口径一致；纯汉字数仅为辅助参考。中文与英文的**信息对等**用 §2.3.2 的换算判断，不机械要求数字相等

### 4.2.3.1 高信息密度页例外（已定稿）

`image-generator` 这类 hub / 专页，因需保留工具清单、企业生态权衡、退役日期等**支撑论证**，严格执行 320 字会导致论证失真。

**定稿规则**：

> 普通页参考 180–320；信息密度高的 hub/专页（判断标准：工具数 ≥6、需保留价格/退役日期/生态权衡等论据）可放宽至 **180–400 字 / 120–260 词**，前提是**信息零损失、无注水**。

**规则优先级**：本例外仅在「删论据即失真」时启用，不可作为堆字数的借口。若超 400 字但每句都有不可删的论证（如 433 字对应的中英对等合理），按 §2.3 的「内容优先」原则判定合格，不必机械裁剪。

**判定辅助**：工具数 ≥6、或结论中出现具体价格/日期/权衡逻辑的页面，适用本例外；其余页面按 §2.3 常规区间。

### 4.2.3.2 中英对等（新增，必读）

**同一页面中英文结论必须信息对等、结构对齐**：

- **信息点**：工具清单、价格、日期、权衡逻辑、趋势洞察在中英文中一一对应，不得中文有而英文无（或反之）
- **段落结构**：中英文段落数一致（通常 2–4 段，各段承担相同功能——选型 / 用法边界 / 人机或趋势）
- **篇幅换算**：中文 1 字 ≈ 英文 0.45–0.55 词（中文信息密度更高）。中文 400 字 ≈ 英文 ~200 词属合理对等，不应机械要求词数相等
- **禁止**：中英一处有具体论据（如 `$0.035/图`）、另一处只有模糊概括（如 "commodity API pricing"）

**示例（image-generator，已对齐）**：中英均 3 段、信息点逐一对应；中文 421 字 / 英文 198 词（≈ 换算一致）。

### 4.2.3.3 视频 spoke 短结论

路由型 spoke（`video`、`filmmaking`、`animation-generator` 等）职责是**路由而非总结**，允许短于 180 字下限，但不得低于 **100 字 / 80 词**，且必须包含「选型分流 + 相邻环节」两个实质点。

## 4.2.4 时效核对句（策略 / 事件文）

涉及厂商政策、限额、Attribution 默认、定价的案例文，**可以**提醒读者核对官方源，但须遵守 [`presentation.md`](./presentation.md) **E42**：

- **禁止**在 `#conclusion` **之后**或结论 section **内单独成段**写「政策随产品更新；请核对 FAQ / Changelog / Usage 页」
- **须**并入结论**最后一段**末句，与 actionable 收束同段

**中文示例（并入末句）**：「…比硬凑一个空 wrap 更安全；政策与案例随产品更新，launch 前请核对各官方 FAQ 与 Changelog。」

**英文示例**：「…rather than forcing an empty wrap—policies and case details change by vendor, so verify official FAQ and changelogs before you ship.」

**禁止**结论只有套话核对句、无论证收束。

## 4.2.4 内容要求

- **总结核心观点**：不引入新信息，只归纳正文要点
- **回顾主要工具/策略**：简要列出核心工具或解决方案
- **提供选择建议**：给出行动指引或下一步建议
- **与引言呼应**：可与开头章节形成呼应，形成完整闭环
- **保留论证**：关键结论附支撑（数据、价格、权衡逻辑），不写成裸断言

## 4.2.5 段落结构

- **常见 2–4 段**；单段宜 2–5 句
- 段间比例：仅检查同一 section 内并列段落，不跨 section 比较
- 避免整页「一段占满屏」、避免并列段落数量级长短差（约 3 倍以上）
- **写作节奏参考**：
  - 段 1（品类格局 / 代表工具）：重申主题、归纳正文要点
  - 段 2（选型决策点）：提供选择建议 / 行动指引
  - 段 3（人机分工 / CTA，可选）：边界与下一步

---

<a id="part-43-页面类型差异"></a>

## 4.3 页面类型差异



## 4.3.1 Tools（工具推荐页）

- **可包含**：内链到相关工具页面（如适用）
- **重点**：总结各工具的核心优势和适用场景
- 篇幅：见 §2.3

## 4.3.2 Marketing（营销策略页）

- **可包含**：内链（见 §4.1，**0–2** 条；承接上文未覆盖的相邻 GTM 任务，非清单式）
- **禁止**：外链；结论段堆产品名清单或「延伸阅读 A、B、C」
- **可保留**：策略类型名称（红人营销、联盟营销、创作者计划等）为纯文本或链至对应策略页
- **重点**：归纳方法论和策略价值
- 篇幅：见 §2.3

## 4.3.3 SEO（SEO 指南页）

- **可包含**：内链到相关 SEO 页面（如适用）
- **重点**：总结优化要点和最佳实践
- 篇幅：见 §2.3

## 4.3.4 Insights（洞察页）

- **主体走 `type: "html"` 长文块**；Conclusion 用独立 `section` 块总结洞察
- 可包含内链
- **Insights 页面历史上「总结」写在 HTML 内**，改版时优先迁回独立 `section`，便于检索与维护

## 4.3.5 Glossary（术语表）

- **无 Conclusion**：术语表为词条列表，非指南文章

---

<a id="part-44-内链规则"></a>

## 4.4 内链规则



## 4.4.1 数量与密度

| 位置 | 规则 |
|------|------|
| **结论** | **0–2** 个内链；承接上文未覆盖的相邻环节，**不做「延伸阅读清单」** |

- 密度自检：结论内链若连续堆叠、或做成「感兴趣」清单式，均违规
- 推荐节奏：结论 → 0–1（落地动作，如「导出到建站 / 监测 GEO」）

## 4.4.2 禁止的反模式

- ❌ 「如果你在探索 X，可能也会对 A、B、C 感兴趣」→ 改为 1 个具体下游场景 + 1 链
- ❌ 「相邻品类：[A]、[B]」清单 → 删标签；在正文一句说明边界，最多 1 链
- ❌ 「选型时常与 X 一并评估」→ 删除；或改为单句流程描述
- ❌ 结论末尾的 Explore / 相关工具领域包括…

## 4.4.3 与全文唯一性

- 同一内链 URL 全文只出现一次；已在正文链过的 slug，结论里改纯文本
- 可保留 1 条 `/tools` 目录链
- 跨频道链接（SEO 指南、论文工具等）堆在结论：**最多 1 个**且与结论强相关

## 4.4.4 R-LINK-ONLY 内容保全

存量内链修复**只允许改 `<a>` 标签**（增/删 `href`、保留锚文本为纯文本）。**禁止**整段替换结论、用短句覆盖长段以满足内链规则。验收：改链前后结论/FAQ 字段去 HTML 后长度不得异常缩水（人工 spot-check）。

---

<a id="part-45-实现方式"></a>

## 4.5 实现方式



## 4.5.1 JSON `section` 块（BlogLayout，主流）

```json
{
  "type": "section",
  "title": "结论",
  "paragraphs": ["段落1", "段落2", "段落3"]
}
```

- **`id` 固定为 `"conclusion"`**
- 标题英文为 **Conclusion**，中文为 **结论** 或 **总结**
- 该块必须出现在 **`type: "faq"` 之前**

## 4.5.2 MDX `Section` 组件

```tsx
<Section
  id="conclusion"
  level={2}
  title="总结"
  paragraphs={[
    `第一段（50-80字）：重申主题与核心价值，归纳正文要点。`,
    `第二段（50-80字）：成功的关键在于...，以 CTA 或下一步建议收尾。`,
    `第三段（50-80字）：可与相关策略相互补充（纯文本，不含链接）。`
  ]}
  showDivider={true}
/>
```

## 4.5.3 div（历史 / 备用）

```tsx
<div className="space-y-6 pt-8 border-t border-border" id="conclusion">
  <h2 className="text-2xl md:text-3xl font-bold tracking-tight">总结</h2>
  <p className="text-base md:text-lg leading-relaxed">...</p>
</div>
```

## 4.5.4 childrenHtml（Insights 长文）

Insights 页面结论若在 `childrenHtml` 内，需保留 `id="conclusion"`；改版时优先迁回独立 `section`。

---

<a id="part-46-质量检查"></a>

## 4.6 质量检查



## 4.6.1 P0 级一票否决（创建 / 新增）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P0-1 | Conclusion 收束 md 正文 | md 以 `## 结论 {#conclusion}` 结尾；FAQ 由页底 `FAQ.tsx` 全局渲染（不在 md 流内） |
| P0-2 | 锚点 id | 固定为 `conclusion`，无变体 |
| P0-3 | 段落数 | ≥2 段，否则仓促（spoke 例外见 §2.3.3） |

## 4.6.2 内容质量（优化时）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| Q1 | 篇幅 | 落在 §2.3 建议区间附近，或能说明「因高密度/合规而略长」等理由 |
| Q2 | 论证保留 | 关键结论附支撑（数据/价格/权衡），非裸断言 |
| Q3 | 无套话 | 无「革命性/前所未有/协作伙伴」等模板腔；无「Choose the right tool based on…」机械句 |
| Q4 | 内链 | 0–2 条；不与正文重复；非清单式 |
| Q5 | 人机分工 | Tools/SEO 类收尾含人机边界或 CTA（可选） |

## 4.6.3 验收命令

```bash
npm run verify:content-json   # 实际 = verify-content-md.py（md 结构；不验 JSON）
npm run build                 # 部署仓：全量构建
```

---

<a id="part-47-相关文档与迁移说明"></a>

## 4.7 交叉引用

- 结论内链全站规则：[`internal-links.md`](./internal-links.md) · 本节 Part 4.4
- 篇幅数字索引：[`word-counts.md`](./word-counts.md) · [`consistency.md`](./consistency.md)
- 交叉引用：[`internal-links.md`](./internal-links.md) · [`word-counts.md`](./word-counts.md) · [`consistency.md`](./consistency.md)

---

<a id="part-48-常见错误"></a>

## 4.8 常见错误



- ❌ 结论放在 FAQ 之后
- ❌ 结论缺失
- ❌ 字数过少，缺乏总结价值（视频 spoke 例外见 §2.3.3）
- ❌ 字数过多且无论证（高密度页例外见 §2.3.1）
- ❌ 中英信息不对等：一处有具体论据、另一处只有模糊概括（见 §2.3.2）
- ❌ Marketing 结论内链堆叠成「延伸阅读」清单，或链与正文重复同一 URL
- ❌ 裸断言：删掉支撑论据只剩结论（$0.035/图 → 「中文优先 Qwen」）
- ❌ 模板腔：革命性 / 前所未有 / 协作伙伴 / Choose the right tool based on…
- ❌ 结论内链堆叠成「感兴趣」清单
- ✅ 结论紧跟 How To 或应用场景，位于 FAQ 之前

---

<a id="part-49-修订记录"></a>

## 4.9 修订记录



| 日期 | 说明 |
|------|------|
| 2026-08-08 | 从 `section-conclusion.md` 等 16 处文件收敛为唯一真相源；新增「高密度页例外（讨论中）」与「视频 spoke 短结论」条款；新增「论证保留」第一原则 |
| 2026-08-08 | 定稿 §2.3.1 高密度页例外（180–400 字）；新增 §2.3.2 中英对等条款（信息点/段落结构/篇幅换算）；spoke 顺延为 §2.3.3；`image-generator` 按新规则对齐为 3 段、中英信息对等 |

---

<a id="part-5-final-cta页底-secondarycta"></a>

# Part 5 · Final CTA（页底 SecondaryCta）

> **渲染**：部署仓 `src/components/SecondaryCta.tsx`  
> **数据源 SSOT**：`src/data/cta-config.json` → `slugs.{slug}.{zh|en}`  
> **缺条目时**：回退 `fallback` 通用文案（「你的产品，值得被发现。」）——**禁止**新文上线时落入 fallback。  
> **与 Part 4 关系**：CTA title/description 从结论 / Author POV 提炼，**不复读** Meta description。

## 5.1 何时写入

| 时机 | 动作 |
|------|------|
| **Step 08** Meta + Config | 与 `*-meta.ts` 注册**同批**写入 `cta-config.json` |
| **Step 09 后** | EN 版 title/description 定稿后，**补齐** `slugs.{slug}.en` |
| **改版 slug** | 若结论/主叙事大变，同步更新 CTA；小改可不动 |

## 5.2 JSON 结构

```json
"{slug}": {
  "zh": {
    "title": "一句 punchline，≤28 字为宜",
    "description": "1–2 句，承接结论或 Author POV，≤60 字为宜",
    "cta": "开始合作"
  },
  "en": {
    "title": "One punchline sentence.",
    "description": "1–2 sentences tied to conclusion or thesis.",
    "cta": "Work with us"
  }
}
```

- **href 不写**：组件固定链 `/services`（中文自动加 `/zh` 前缀）
- **cta 按钮文案**：中文常用 `开始合作` · `获取帮助` · `看看我们怎么做`；英文常用 `Work with us` · `Get started` · `Get help`
- **slug 键**：与 md 文件名一致（如 `git-commit-attribution`），**非** URL path

## 5.3 写法原则

1. **承接正文，不复读 Meta description** — 用结论句、Author POV 或「我会把这篇文章收成…」的提炼  
2. **title = 可独立传播的 punchline** — 读者没读全文也能 get 核心判断  
3. **description = 下一步行动的理由** — 为什么找 Alignify / 为什么现在动  
4. **双语独立撰写** — EN 不是 ZH 直译；语气对齐 [`presentation.md`](./presentation.md)  
5. **Hub 页走 `exact`** — 仅 `/tools`、`/marketing` 等频道首页；**文章详情页一律 `slugs`**

## 5.4 Brief 必填字段（Step 02 定稿）

```markdown
**Final CTA**（Step 08 写入 cta-config.json）:
- ZH title: …
- ZH description: …
- EN title: …
- EN description: …
- cta 按钮: zh「开始合作」/ en「Work with us」（或见 §5.2）
```

Step 05 动笔前 Brief 里 ZH title/description **至少要有草案**；Step 09 EN 完稿后 EN 字段定稿。

## 5.5 验收

```powershell
node E:\clients\Alignify\scripts\ops\merge-cta-slugs.mjs --check
```

- 输出 `Missing: 0` → Pass  
- 任一 slug 缺失 → Gate C **BLOCK**

## 5.6 常见错误

| 错误 | 正确 |
|------|------|
| 新文上线无 `slugs.{slug}` | Step 08 与 meta 同批注册 |
| 用 fallback 通用「好产品输的从来不是质量」 | 每篇定制 punchline |
| title 复制 Meta title | 从结论/POV 提炼 |
| EN 逐句翻译 ZH CTA | 独立重写 |
| slug 键写错（如 `git-commit`） | 与 `{slug}.md` 文件名一致 |

见 [`common-errors.md`](./common-errors.md) **E43**。

---

<a id="附录-a-节型--articletype-速查"></a>

# 附录 A · 节型 × articleType 速查

| articleType | 几乎总是 | 常用 | 视题材 | 默认省略 |
|-------------|---------|------|--------|---------|
| best-ranking | 什么是 · 主体(Best H3) · 结论 | TL;DR · 对比表 · 应用场景 · How To · FAQ | References | — |
| seo-guide | 什么是 · 主体 · 结论 | TL;DR · How To · FAQ | References | How To（纯概念文） |
| marketing-strategy | 什么是 · 主体分析节 · 结论 | TL;DR · FAQ | References（A/B 源） | **How To**（观点/事件文） |
| insights-analysis | 主体 · 结论 | 什么是 · TL;DR · FAQ | References | How To · Best H3 |

**中英 parity**：对齐**实际采用的节**与 anchor id，不机械复制节数。

---

<a id="附录-b-abc-底线汇总"></a>

# 附录 B · A/B/C 底线汇总

| 层级 | 含义 | 章节相关示例 |
|------|------|-------------|
| **A** | 违反即 Fail | 结论收束 md；FAQ 7 问（若采用）；无 frontmatter `howTo:`；产品 H3 ≥2 款（best-ranking）；对比表 bestFor/pricing 非空 |
| **B** | 强建议 | TL;DR intro 30–100 字；什么是 180–380 字；How To 3–5 步（若采用） |
| **C** | 软建议 | 节型菜单顺序；GEO items 模板；References 条数区间 |

质检：A 层必 Pass；B/C 偏离须在 Brief 或 SelfCheck 说明理由。

---

<a id="附录-c-相关文档索引"></a>

# 附录 C · 相关文档索引

| 主题 | 文档 | 说明 |
|------|------|------|
| 各节字数表 | [`word-counts.md`](./word-counts.md) | TL;DR / 什么是 / 结论 / FAQ 数字索引 |
| Best H3 客户露出 | [`partner-products.md`](./partner-products.md) | Tier 1/2 商业规则；写法见 Part 3.3 |
| Best 产品截图 | [`product-screenshots.md`](./product-screenshots.md) | Step 04 操作；非节写法 |
| 跨页一致性 | [`consistency.md`](./consistency.md) | C 层软建议定位 |
| BLUF / Author voice | [`presentation.md`](./presentation.md) | 全节通用 |

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 初版：合并 sections 九文件为单 SSOT；新增 Part 0 内容优先选节 |
| 2026-08-27 | 合并结论 → Part 4 · Final CTA → Part 5；附录 C 索引；删除 `sections/` 子目录 |

*sections.md · v1.1 · 2026-08-27*
