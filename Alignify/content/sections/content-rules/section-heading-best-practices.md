# HTML H 标签最佳实践（H1-H6）

本文档统一 HTML Heading 标签（H1-H6）的 SEO、可访问性、可读性与文案构建最佳实践，全站通用。

> **注意**：Meta title 和 Meta description 的文案规则已迁移至 [section-meta-copy](./section-meta-copy.md)（全站唯一规范来源）。本文档 §九「Meta Title 与 H1 关系」保留概述，详细字数、模板、页面类型差异以 section-meta-copy 为准。

**参考来源**：[Moz](https://moz.com/learn/seo/h1-tags)、[SEMrush](https://www.semrush.com/blog/header-tag/)、[Google Developers](https://developers.google.com/search/docs/appearance/publication-dates)、[WAI/WCAG](https://www.w3.org/WAI/GL/WCAG21/quickref/?headings)、[Search Engine Land](https://searchengineland.com/seo-page-titles-meta-descriptions-clicks-448381)、[Ahrefs](https://ahrefs.com/blog/how-to-add-keywords-to-headings-for-on-page-seo-success)、[WebAIM](https://webaim.org/techniques/headings)、[Yoast](https://yoast.com/how-to-use-headings-on-your-site/)  
**职责**：本文档专注于 H1-H6 层级结构、可访问性、文案构建。Meta title/description 文案规范见 [section-meta-copy](./section-meta-copy.md)。

---

## 〇、项目特定规则（仅本网站）

### 页面构建形式（技术统一）

| 要求 | 说明 |
|------|------|
| **根组件** | Tools、Marketing、SEO 页面一律使用 `BlogLayout` 作为根组件 |
| **必填 props** | `title`（H1）、`excerpt`（Hero 摘要）、`heroContent`、`publishDate`、`modifiedDate`、`readTime`、`pageUrl` |
| **正文章节** | 使用 `<!-- block:section -->` / `Section.tsx`；FAQ 在 `faq-data.json` |
| **导入方式** | `title`、`excerpt` 使用硬编码字面量，避免引用变量导致构建失败 |

**详见**：各 template（[template-tools](../templates/template-tools.md)、[template-marketing](../templates/template-marketing.md)、[template-seo](../templates/template-seo.md)）的 BlogLayout 配置。

### 层级结构原则

| 规则 | 说明 |
|------|------|
| **H1 唯一** | 每页仅一个 H1；BlogLayout 用 `title` prop 生成，heroContent 禁止 H1 |
| **不跨级** | 层级顺序 H1 → H2 → H3，不得跳过 |
| **组件驱动** | 正文章节使用 `<!-- block:section -->` / `Section.tsx`；FAQ 在 `faq-data.json`
| **FAQ 例外** | FAQ 组件自动渲染 H2，禁止在组件前手动添加 H2 |

### 字号类名（实现约定，与 brand-visual 一致）

正文内标题与段落须符合 **H1 > H2 > H3 > 正文**。Tailwind 摘要如下（完整表见 [brand-visual §2.2](../alignify-project-context/brand-visual.md)）：

| 阶梯 | 典型用法 | Tailwind（摘要） |
|------|----------|------------------|
| **L1** | 页内唯一 H1（BlogLayout） | `text-3xl md:text-4xl lg:text-5xl font-bold` |
| **L2** | 章节 H2、FAQ 区块标题、列表索引分区标题 | `text-2xl md:text-3xl font-bold tracking-tight` |
| **L3** | 子节 H3、FAQ 问题行（组件样式） | `text-lg font-semibold` |
| **L4** | 段落、列表、FAQ 答案、HowTo 步骤正文 | `text-base md:text-lg leading-relaxed` |

**禁止**：为增大 H3 使用 `text-lg md:text-xl` / `lg:text-2xl` 等破坏与 L2 的层级差。

---

## 一、标题层级结构原则（全网最佳实践）

### 1.1 基础规则

| 规则 | 说明 |
|------|------|
| **每个页面仅一个 H1** | H1 代表页面主题，多个 H1 会混淆搜索引擎与用户 |
| **保持层级顺序** | H1 → H2 → H3，不得跳跃（如 H1 后直接 H3） |
| **不跳过层级** | 可在收尾时跳过层级（如 H3 → H2），但不得在展开时跳过 |
| **语义化使用** | 使用 `<h1>`-`<h6>` 标签，而非仅样式加粗 |
| **H1 对应主题** | H1 内容应与页面主关键词、URL、meta title 一致 |

### 1.2 可访问性（WCAG 合规）

- 屏幕阅读器用户依赖标题导航：约 70% 的屏幕阅读器用户将标题作为主要导航方式
- 屏幕阅读器可跳过重复内容（如导航、菜单），直接跳到 H1-H6
- 标题层级帮助认知障碍用户理解内容组织
- WCAG Level AA 要求语义化使用标题，Level AAA 要求有组织的标题结构

### 1.3 SEO 收益

| 收益 | 说明 |
|------|------|
| **搜索引擎理解** | 标题帮助搜索引擎理解页面主题与子话题 |
| **Passage Indexing** | H1-H6 支持 Passage Indexing，特定段落可排名 |
| **Featured Snippets** | 结构化标题有助于 Google 选择内容为摘要 |
| **关键词加权** | H1 权重最大，H2-H6 递减 |
| **URL 结构** | 清晰的标题层级对应清晰的 URL 结构 |

---

## 二、H1 标签

### 2.1 字数与格式

| 语言 | 字数/字符 | 说明 |
|------|------------|------|
| 中文 | 14-22 字 | 约 20-70 字符 |
| 英文 | 40-60 字符 | 建议范围，无技术限制 |

**依据**：Google 建议标题长度约 20-70 字符，避免过短（描述性不足）或过长（截断）。SiteLint 建议至少 20 字符。

### 2.2 SEO 规则

| 规则 | 说明 |
|------|------|
| **关键词前置** | 主要关键词放在 H1 开头，权重最高 |
| **与 meta title 区别** | H1 侧重用户可读性，meta title 侧重 SEO |
| **与 URL 一致** | H1 应反映页面核心内容，与 URL 路径匹配 |
| **自然融入** | 关键词自然融入，避免关键词堆砌 |
| **避免重复** | 与 meta title、URL 避免完全相同，但主题应一致 |

### 2.3 文案构建形式（跨类型统一）

#### 2.3.1 基础公式

```
[类型/策略/主题]：[核心价值/卖点]
```

**示例**：
- Tools：`AI 变声器：改变声音，创造无限可能`
- Marketing：`关键词调研：找到好话题与长尾词`
- SEO：`网站结构：层级清晰利于抓取`

#### 2.3.2 禁用

- 含「Guide」「指南」
- 年份（如 2026）
- 疑问句开头（如「如何选择 X」），需转换为陈述式 `[主题]：[价值]`）

#### 2.3.3 英文翻译原则

- Tools：`[Type]: [Value Proposition]`（冒号分隔）
- Marketing/SEO：`[Noun Phrase] + Value`（如 `Keyword Research: Find Topics & Long-Tail Keywords`）
- 避免「How to...」开头，用陈述式（`Topic: Value`）

---

## 三、Excerpt（Hero 摘要）

### 3.1 字数

| 语言 | 字数/字符 | 说明 |
|------|------------|------|
| 中文 | 100-150 字 | 约 200-300 字符 |
| 英文 | 200-250 字符 | 约 400-600 字符 |

### 3.2 规则

| 规则 | 说明 |
|------|------|
| **内容聚焦** | 聚焦页面价值、适用场景、用户收益 |
| **避免通用结尾** | 禁止「这将显著提升你的创作效率和专业表现」等通用句 |
| **独立字段** | 必须使用 `excerpt` prop，不使用 `metadata.description` |
| **与 H1 一致** | 摘要应与 H1 主题相关，但不重复 |

### 3.3 文案构建形式（三段式）

#### 中文结构

| 首句（价值主张） | 中段（能力/方法/适用场景） | 收尾（具体场景或目标用户） |
|---------------------|---------------------------|---------------------------|
| 核心价值/行动号召（如「让…」「释放…」「通过…」「将…」） | 工具能力/方法论/适用场景、用户收益 | 具体场景或目标用户（**禁止**通用句） |

**示例**：

```
让音乐创作变得人人可及。AI 音乐生成工具能根据文字描述或风格偏好自动创作旋律，从背景音乐到主题曲，让每个人都能成为音乐创作者。无论是音乐爱好者、视频创作者还是播客制作人，都能快速生成高质量背景音乐，大幅提升创作效率。
```

#### 英文结构

| 首句（Value Proposition） | 中段（Capabilities/Use Cases） | 收尾（Target Users/Ideal For） |
|--------------------------|------------------------------|------------------------------|
| Transform/Discover/Unlock/Make/Explore… | 工具能力/功能点/适用场景 | Ideal for [目标用户] / 具体场景描述 |

**示例**：

```
Unlock infinite potential in voices and create unique audio experiences. AI voice changer tools provide real-time voice transformation, effect layering, and personalization, suitable for entertainment, education, and professional recording.
```

---

## 四、H2 标题

### 4.1 字数与格式

| 语言 | 建议 | 说明 |
|------|------|------|
| 中文 | 8-20 字 | 符合对应 template「标准 H2 标题格式」 |
| 英文 | 50-80 字符 | 描述性短语（What Are...、How...、Best...）；避免直译 |

### 4.2 标准格式（按页面类型）

详见各 template 的「标准 H2 标题格式」表：

| 页面类型 | 格式模式 | 详见 |
|----------|----------|------|
| **Tools** | 什么是 [工具类型]、[工具类型] 是如何工作的、如何选择 [工具类型] | [template-tools](../templates/template-tools.md) § 七 |
| **Marketing** | 什么是 [策略名称]、如何实施 [策略名称] | [template-marketing](../templates/template-marketing.md) § 七 |
| **SEO** | 什么是 [主题]、[主题] 如何工作 | [template-seo](../templates/template-seo.md)、[section-consistency](../section/section-consistency.md) § 4.1 |

### 4.3 技术实现与禁用

| 项目 | 规则 |
|------|------|
| **实现** | 通过 Section 组件 `level={2}`、`title="..."` 生成，禁止裸 `<h2>` |
| **分割线** | 中文 H2 之间可用 `showDivider`；Marketing 正文章节默认由 `space-y-12` 控制，不使用分割线；英文仅 `pt-8`，无分割线 |
| **禁止** | FAQ 组件前手动添加 H2（会导致重复） |

---

## 五、H3 标题

### 5.1 字数与格式

| 场景 | 格式 | 示例 |
|------|------|------|
| Tools 产品 | `[序号]. [产品名]：[核心优势]` | `1. Dubbing AI：游戏直播声音转换` |
| Tools 应用场景 | `[序号]. [场景名称]` | `1. 直播实时变声` |
| Marketing/SEO 子章节 | 按主题分，每节聚焦一子问题 | 按主题命名 |
| 分类列举 | 不使用 H3 | 分类章节用列表，无 H3 |

### 5.2 规则

| 规则 | 说明 |
|------|------|
| **实现** | 通过 Section 组件 `level={3}` 或 `subSections` 生成 |
| **一致性** | 同一 H2 下各 H3/subSection 字数相近（±15%） |
| **英文 Tools**：H3 使用 generator/editor/enhancer 等专业术语，避免 "XXX Tools" |

---

## 六、标题文案写作最佳实践

### 6.1 H1 文案原则

| 规则 | 说明 |
|------|------|
| **以价值开头** | 避免「欢迎来到我们的网站」，直接陈述收益或解决方案 |
| **问题 + 方案 + 受众公式** | 包含：解决什么问题、如何解决、为谁解决 |
| **具体明确** | 避免通用描述，提供具体收益 |
| **独立可读** | H1 常独立出现在搜索结果中，必须完整传达主题 |
| **清晰真实** | 避免 cute idioms、hype，使用熟悉的行业术语 |
| **匹配搜索意图** | 与用户搜索期望一致，降低跳出率 |

### 6.2 H2/H3 文案原则

| 规则 | 说明 |
|------|------|
| **简洁描述** | 理想 65 字符或更少，含相关关键词 |
| **使用名词短语** | 概念性内容使用名词短语 |
| **避免 "-ing" 动词** | 过度动词影响可读性 |
| **避免过多标点** | 简洁、专业 |
| **唯一描述性** | 便于用户导航和内容扫描 |

### 6.3 可读性与用户体验

| 规则 | 说明 |
|------|------|
| **用户仅读 20% 内容** | 标题是快速扫描的关键 |
| **用户在 54 秒内决定** | H1 是捕捉注意力的唯一机会 |
| **H1 是数字头条** | 相当于印刷媒体的头条 |
| **标题作为路标** | 帮助用户定位信息 |

---

## 七、标题关键词位置最佳实践

### 7.1 H1 标签（主要关键词）

| 项目 | 说明 |
|------|------|
| **包含主目标关键词** | 信号页面主题 |
| **自然融入** | 避免关键词堆砌 |
| **与 URL、首段一致** | 关键词出现在 H1、URL、首段和内容中 |
| **匹配搜索意图** | 降低跳出率，提升表现 |

### 7.2 H2-H6 标签（次要关键词）

| 项目 | 说明 |
|------|------|
| **使用关键词变体和同义词** | 扩大受众范围 |
| **在 H2 和更低级标题中放置次要和长尾关键词** | 支持主要主题 |
| **自然融入** | 改善可读性和搜索可见性 |

### 7.3 SEO 收益

| 收益 | 说明 |
|------|------|
| **Passage Indexing** | 优化标题允许 Google 排名内容特定段落 |
| **主题关系** | 搜索引擎通过标题理解主题和子话题关系 |
| **自然关键词融入** | 避免强制关键词堆砌，改善可读性 |
| **标题可视化层级** | 使内容更易扫描，同时支持可访问性 |

---

## 八、常见错误与反模式

### 8.1 标题层级错误

| 错误 | 后果 |
|------|------|
| **多个 H1** | 混淆搜索引擎关于页面焦点 |
| **跳过层级** | 破坏内容结构，影响可访问性 |
| **基于样式选择级别** | 选择 H1-H6 基于 desired styling 而非逻辑结构 |
| **使用多个 H1** | 混淆搜索引擎关于页面焦点 |
| **跳过第一级标题** | 缺少主要章节标题 |

### 8.2 文案错误

| 错误 | 后果 |
|------|------|
| **标题过长** | 应该不是整个段落 |
| **通用或含糊标题** | 不提供价值或差异化 |
| **缺少第一级标题** | 用户体验和 SEO 受损 |
| **空标题元素** | 无意义，影响可访问性 |

### 8.3 技术错误

| 错误 | 后果 |
|------|------|
| **非语义化标题** | 仅样式加粗，不是真正标题 |
| **标题仅用于视觉样式** | 影响可访问性和 SEO |

---

## 九、Meta Title 与 H1 关系

### 9.1 区别

| 项目 | H1 | Meta Title |
|-----|----|------------|
| **目的** | 用户可读性 | SEO、搜索结果点击 |
| **长度** | 14-22 字 / 40-60 字符 | 25-32 字 / 50-60 字符 |
| **格式** | `[类型]：[价值]` | `[N]款最佳[类型]（2026）：[简短描述] | 品牌` |
| **关键词** | 自然融入 | 前置、聚焦搜索意图 |

### 9.2 一致性原则

- H1 应与 meta title 主题一致
- H1 可与 meta title 不同（侧重可读性）
- H1 常独立出现在社交媒体分享（Open Graph）

---

## 十、检查清单

创建或优化页面时：

### 层级结构
- [ ] 每页仅一个 H1
- [ ] 层级顺序 H1 → H2 → H3
- [ ] 不跳过层级（展开时）
- [ ] 使用语义化 `<h1>`-`<h6>` 标签

### 项目特定
- [ ] 构建形式：BlogLayout 根组件；title、excerpt 硬编码；Section 等组件承载正文
- [ ] heroContent 禁止 H1

### H1
- [ ] 字数：14-22 字 / 40-60 字符
- [ ] 格式：`[类型]：[核心价值/卖点]`
- [ ] 禁用：Guide、年份、疑问句开头
- [ ] 关键词前置，与 URL、首段一致

### Excerpt
- [ ] 字数：100-150 字 / 200-250 字符
- [ ] 三段式：首句（价值主张）→ 中段（能力/场景）→ 收尾（目标用户）
- [ ] 禁止通用结尾
- [ ] 独立字段，不使用 metadata.description

### H2
- [ ] 字数：8-20 字 / 50-80 字符
- [ ] 格式符合对应 template 标准
- [ ] 通过 Section 组件 `level={2}` 生成
- [ ] FAQ 前不手动添加 H2

### H3
- [ ] 格式符合场景类型
- [ ] 同一 H2 下字数相近（±15%）
- [ ] 通过 Section 组件 `level={3}` 或 `subSections` 生成

### 文案质量
- [ ] H1 以价值开头，避免「欢迎」
- [ ] 具体明确，避免通用描述
- [ ] 匹配搜索意图
- [ ] H2/H3 简洁描述，使用名词短语
- [ ] 避免 "-ing" 动词和过多标点

### SEO
- [ ] H1 包含主目标关键词
- [ ] H2-H6 使用关键词变体和同义词
- [ ] 关键词自然融入，避免堆砌
- [ ] H1 与 URL、首段、meta title 一致
