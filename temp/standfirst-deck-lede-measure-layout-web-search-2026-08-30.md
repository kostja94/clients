# 深度搜索报告 — 标题较窄、描述更宽的编辑布局（standfirst / deck / lede 与 measure）

> **检索基准日**：2026-08-30
> **时间范围**：概念/品类调研，不限单一发布事件；优先现行官方文档与可核验定义
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档
> **Loop 轮次**：6 轮
> **来源统计**：Tier 0 9 · Tier 1 8 · Tier 2 7
> **置信度摘要**：术语定义与 measure 数值区间已由词典、报业官方材料与政府设计系统交叉确认；「上窄下宽」作为**布局命名**无单一权威术语，属描述性说法；Web 落地存在与之相反的常见做法，须并列说明。

---

## 1. 执行摘要

在排版与编辑设计里，**标题下方、正文之前、字号介于标题与正文之间的那段说明文字**，英式报业最贴切的专名是 **standfirst**；美式新闻室对应 **deck / dek**。**lede（导语）**在专业用法中通常指**正文第一段**，不是标题家具（furniture）本身——把 standfirst 直接叫 lede 是常见混用，Wikipedia 也有这种混写。

「标题较窄、下面描述明显更宽」**没有单一权威布局名**。最接近的说法是描述性短语：*centered hero with a wider standfirst / deck*，或 *constrained heading + wide lede*。原理是给不同层级设不同的 **measure（行宽 / 行长）**：大号 display 标题用较短 measure，standfirst / lead 可用更宽 measure，形成视觉上的「上窄下宽」。

美国政府设计系统 USWDS 明确写了「**大号文字可以、也常常应该用更短的 measure**」，同时默认把 **lead（导语段）设为最宽的 measure token 6（88ex）**，正文默认 measure 4（68ex）——这是官方代码里最接近「标题收、导语放」的实现。与此同时，大量 SaaS hero 模板走的是**相反方向**（标题 `max-w-3xl`、描述 `max-w-2xl`）。社区对 45–75 字符行长讨论很多，但对「上窄下宽」这一具体构图**几乎没有统一命名讨论**。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `standfirst newspaper typography definition`; `lede vs standfirst vs dek`; `site:en.wikipedia.org standfirst` | 立住英式 standfirst、美式 deck/dek、lede 三词骨架；Guardian 2009 术语表将 standfirst 定义为独立于 body 的块 |
| R2 | `Butterick line length`; `USWDS large text shorter measure`; `"standfirst" CSS max-width heading` | 行长权威区间 45–90 cpl；USWDS 明文「大号文字可用更短 measure」 |
| R3 | `kicker vs standfirst vs deck`; `GOV.UK lead paragraph`; `Bringhurst measure site:webtypography.net` | kicker 至少四种含义；GOV.UK 有正式 Lead paragraph；deck 在术语表里还有「标题行数」义 |
| R1b | `导语 副题 肩题 standfirst` | 中文对应：副题/子题 ≈ deck；导语 ≈ lede；肩题/引题 ≈ kicker/overline |
| R4 | `USWDS $theme-lead-measure`; Tailwind/Shadcn hero `max-w-2xl` vs `max-w-3xl` | USWDS 默认 lead 比正文更宽；SaaS hero 常把描述收得比标题更窄 |
| R5 | `site:news.ycombinator.com line length measure`; `site:thetype.com 行长`; W3C clreq | HN 热议正文 measure，不讨论本布局专名；中文权威谈行长，不谈 standfirst 构图 |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线三问：Q1 这套术语/布局是什么 | `standfirst definition`; `what is dek journalism`; `measure line length typography` | 已覆盖 |
| 概念基线三问：Q2 有哪些类型 | `kicker vs deck vs lede`; 中文肩题/副题/导语；hero 宽窄两种惯例 | 已覆盖 |
| 概念基线三问：Q3 知名产品/代表方案 | USWDS / GOV.UK / Guardian / Tailwind 容器刻度 | 已覆盖（无「市场份额」维度，改为实现地图） |
| 布局命名是否存在权威专名 | `"centered hero" wider standfirst`; `"constrained heading" wide lede` | 权威源未覆盖单一专名 |
| 排版原理（measure） | Bringhurst §2.1.2；Butterick；USWDS measure tokens | 已覆盖 |
| 术语冲突 | Wikipedia 将 standfirst 写入 lead 条；kicker 多义 | 已覆盖（见 §8） |
| 社区反响 | HN line length；设计模板实践 | 已覆盖：有 measure 讨论，无本布局命名热议 |
| 中文语境 | 副题/导语/行长；W3C clreq；The Type 孔雀计划 | 已覆盖 |

---

## 4. 核心发现（多源验证）

### 4.1 这是什么：standfirst / deck / lede，以及「上窄下宽」

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| **Standfirst**（英式新闻用语）是标题下方、用于引入/概括稿件的文字块，风格通常有别于标题与正文 | [Guardian《Typographical terms》PDF](http://image.guardian.co.uk/sys-files/Guardian/documents/2009/02/16/Typographicalterms.pdf) T0（2009-02-16） | [Wiktionary: standfirst](https://en.wiktionary.org/wiki/standfirst) T2 作索引；与 Guardian 读者编辑用法互证 | 已确认 |
| Guardian 内部把 standfirst 视为与 headline、caption 并列的 **furniture（标题家具）**，用来补全标题无法说清的细节 | [Guardian 读者编辑 Chris Elliott, 2012-09-16](https://www.theguardian.com/commentisfree/2012/sep/16/headlines-more-easily-misunderstood-online) T0 | [Charlotte Naughton on subeditors, 2012-07-26](https://www.theguardian.com/commentisfree/2012/jul/26/subeditor-role-changed) T0 | 已确认 |
| **Deck / dek** 是标题下方的副标题/摘要句，字号小于 hed、大于正文；hed+dek 合称 furniture | [Wikipedia: Glossary of journalism — deck](https://en.wikipedia.org/wiki/Glossary_of_journalism) T2 索引 | [Language Log, 2007](https://itre.cis.upenn.edu/~myl/languagelog/archives/004380.html) T2；与 Wikipedia News style 互证 | 很可能 |
| **Lede / lead** 在词典与新闻手册中是**新闻稿开篇段落**，用来勾住读者 | [Merriam-Webster: lede](https://www.merriam-webster.com/dictionary/lede) T1 | [Wikipedia: Lead paragraph](https://en.wikipedia.org/wiki/Lead_paragraph) T2（须回链词典） | 已确认 |
| 专业区分：standfirst/deck 在标题区、与正文**排版分离**；lede 是正文第一段 | Guardian 术语表把 Standfirst 与 Body text 分列 T0 | [David Agnew on deks](https://www.davidagnew.com/2022/05/03/how-to-write-better-deks/) T2（从业者稿，单源细节） | 很可能 |
| **Measure** = 一行文字的水平长度，通常以**每行字符数（cpl）**衡量，而非英寸 | [Butterick, Line length](https://practicaltypography.com/line-length.html) T0（实务权威手册） | [Bringhurst via webtypography.net §2.1.2](https://webtypography.net/2.1.2) T1 | 已确认 |
| 「上窄下宽」**不是**已登记的单一布局品类名，而是对「标题与描述使用不同 max-width / measure」的描述 | 多轮检索无 Tier 0/1 专名 | — | 已确认（否定性结论） |

**叙述：三个词分别管什么**

1. **Headline / hed**：最大号，抓住注意。Guardian 定义为「概括文章要点的短语，用大字号与不同风格吸引读者」。
2. **Standfirst（UK）/ deck·dek（US）**：标题与正文之间的桥。Guardian 原文："*block of text that introduces the story, normally in a style different to the body text and headline.*" Wiktionary 强调「小于标题、仍大于正文」。David Agnew 补充：hed 常 Title Case，dek 常 sentence case；报纸 dek 补细节，杂志 dek 往往承担「这篇到底讲什么」。
3. **Lede / lead / 导语**：正文开篇。Merriam-Webster："*the introductory section of a news story that is intended to entice the reader to read the full story*"。拼写 *lede* 是新闻室故意错拼，以免和金属铅条 leading、或「lead」的其他义项混淆（OED 最早书证 1951；手册普及约 1980s）。

**「上窄下宽」在原理上是什么**

不是新组件，而是 **macrotypography（宏观排版）**：同一英雄区里，标题与描述不共享同一个 measure。

- 大号标题若与描述同宽，一行只有很少几个词，或反过来拉成一条过长的巨型字带，都会难看。
- USWDS 官方句："*Large text can have a shorter measure. Since larger text takes up more screen real estate, it may make sense to assign it a relatively small measure.*"
- 描述/standfirst 字号更接近正文、句子更长，需要更接近 45–75（或 Butterick 的 45–90）cpl 的阅读宽度，因此 **max-width 可以、也常常应该比标题更大**。

Web 上的常见落地（描述性，非官方配方）：

| 层级 | 典型约束 | Tailwind 刻度（官方容器尺，约值） |
|------|----------|----------------------------------|
| 居中 hero 标题 | 较短 measure，强迫 2–4 行换行 | `max-w-2xl` ≈ 42rem / 672px |
| Standfirst / 描述 | 明显更宽 | `max-w-4xl` ≈ 56rem / 896px 或 `max-w-5xl` ≈ 64rem / 1024px |
| 长文正文 | 回到阅读舒适区 | `max-w-prose` / `65ch` / USWDS measure 2–5 |

这就是会话里说的 *Centered hero with a wider standfirst / deck* 或 *constrained heading + wide lede*。后一个短语里的 lede，在落地时多半其实是 **standfirst / lead paragraph 组件**，不是新闻学严格意义上的正文第一段。

### 4.2 有哪些类型（分类依据：功能位置 + 地域术语 + 宽度关系）

**分类依据 A：在版面上的位置与功能（报业 / 杂志）**

| 类型 | 位置 | 特征 | 典型场景 | 来源 |
|------|------|------|----------|------|
| **Kicker / overline / eyebrow / 肩题·引题** | **标题上方** | 短（常 2–4 词），标栏目或给语境 | 报纸复合标题、Web 文章 eyebrow | [Wikipedia: News style — Kicker](https://en.wikipedia.org/wiki/News_style)；中文新闻培训「引题/肩题」 |
| **Headline / 主题** | 主视觉 | 最大字号 | 全品类 | Guardian 术语表 |
| **Standfirst / deck / 副题·子题** | **标题下方、正文前** | 一句至一小段，补事实或「卖」文章 | 英媒 standfirst；美刊 dek；中文副题 | Guardian；Wikipedia glossary deck② |
| **Lede / lead / 导语** | **正文第一段** | 5W 或 hook，属 copy 而非 furniture | 消息体、GOV.UK lead | MW；GOV.UK Paragraphs |
| **Nut graf** | 特稿中 lede 之后 | 用一段话点题 | 杂志特稿 | 业内常用，Tier 2 手册 |

**分类依据 B：deck 一词的两种报业义（易混淆）**

| 义项 | 含义 | 来源 |
|------|------|------|
| Deck = **标题的一行** | “three-deck headline” = 三行标题 | [Wikipedia Glossary — deck ①](https://en.wikipedia.org/wiki/Glossary_of_journalism) |
| Deck = **主标题下的副题** | 总结故事关键部分的 sub-headline | 同条 ②；Language Log |

**分类依据 C：Web 英雄区标题 vs 描述的宽度关系（实践分类，非学院 taxonomy）**

| 类型 | 特征 | 适用 | 来源 |
|------|------|------|------|
| **上窄下宽（本主题）** | 标题 `max-w` < 描述 `max-w` | 大号 display 标题 + 较长 standfirst；编辑感 hero | USWDS「大号更短 measure」+ 默认 lead 更宽；[Shadcn Simple Centred](https://www.shadcn-ui-blocks.com/blocks/marketing/hero-sections/simple-centred) 示例为 `max-w-2xl` 标题 + `max-w-3xl` 描述 |
| **同宽** | 二者包在同一 `max-w-*` | GOV.UK 两栏 2/3 网格同时约束标题与 lead | [GOV.UK Layout](https://design-system.service.gov.uk/styles/layout/) |
| **上宽下窄（SaaS 常见）** | 标题更宽、描述收进 `max-w-2xl` | 短标题要气势、描述当正文读 | 大量 Tailwind 模板；Lovable 类 hero 片段把 h1 放在 `max-w-3xl`、p 用 `max-w-2xl`（Tier 2 模板，非官方教条） |

**易混淆点**

- **Standfirst ≠ lede**（严格用法）。Wikipedia *Lead paragraph* 有一句把英国 standfirst 写成新闻第一段的别名，与 Guardian 自己的「standfirst 是独立块、与 body 分开」冲突——见 §8。
- **Kicker ≠ standfirst**。不少美式口语把 kicker 当 deck 用；ThoughtCo 称「纯粹派认为这是误用」，kicker 更常指标题**上方**的 overline，或稿件**结尾**的 punchline。
- **中文「导语」更接近 lede，不是 standfirst。** 副题才更接近 deck。把 Web hero 描述叫「导语」在中文产品圈能懂，但和新闻学导语不是同一物件。

### 4.3 知名产品 / 代表方案

本主题无 CMS 式「市场份额」。Q3 改为 **权威实现与代表出版物**。

| 场景或类型 | 代表产品 / 方案 | 备注（定位） | 来源 |
|-----------|-----------------|--------------|------|
| 英式新闻 furniture | **The Guardian** | 内部术语表与读者编辑均使用 standfirst；强调网上标题必须能脱离 standfirst 独立成立 | [术语 PDF](http://image.guardian.co.uk/sys-files/Guardian/documents/2009/02/16/Typographicalterms.pdf)；[Elliott 2012](https://www.theguardian.com/commentisfree/2012/sep/16/headlines-more-easily-misunderstood-online) |
| 美刊 hed + dek | The New Yorker / The Atlantic / Wired 等 | Agnew 文中引用的 dek 范例（写作规范，非官方设计 token） | [How to Write Better Deks](https://www.davidagnew.com/2022/05/03/how-to-write-better-deks/) |
| 政府站点：标题/导语/正文分 token | **USWDS** | measure 1–6 = 44–88ex；`$theme-text-measure` 默认 **4**；`$theme-lead-measure` 默认 **6**；`.usa-intro` 为 lead | [Typography](https://designsystem.digital.gov/components/typography/)；[Measure tokens](https://designsystem.digital.gov/design-tokens/typesetting/measure/)；[Settings](https://designsystem.digital.gov/documentation/settings/) |
| 政府站点：网格控行长 | **GOV.UK Design System** | 推荐 two-thirds 栏，桌面约 **≤75 字符/行**；**Lead paragraph**（`govuk-body-l`）桌面 24px，每页至多一次 | [Paragraphs](https://design-system.service.gov.uk/styles/paragraphs/)；[Layout](https://design-system.service.gov.uk/styles/layout/)；[Design in government, 2015-09-16](https://designnotes.blog.gov.uk/2015/09/16/tips-for-creating-good-typography/) |
| 西文行长经典 | **Bringhurst *Elements*** → Rutter 网站化 | 单栏 45–75，理想 **66**；多栏 40–50；建议用 em/`ch` 保 measure | [webtypography.net 2.1.2](https://webtypography.net/2.1.2) |
| 屏幕实务手册 | **Butterick *Practical Typography*** | 45–90 字符或 2–3 个小写字母表 | [Line length](https://practicaltypography.com/line-length.html) |
| Web 工具层 | **Tailwind `max-w-*` / `max-w-prose`** | 用容器尺近似 measure，不是新闻术语 | [Tailwind max-width 文档](https://tailwindcss.com/docs/max-width) |
| 上窄下宽示例（组件市场） | Shadcn「Simple Centred」hero | 标题容器 `max-w-2xl`，描述 `max-w-3xl` | [shadcn-ui-blocks](https://www.shadcn-ui-blocks.com/blocks/marketing/hero-sections/simple-centred) T2 |
| 中文行长规范 | **W3C《中文排版需求》(clreq)** | 行长应为字号整数倍；标题占整数倍行高 | [clreq](https://w3c.github.io/clreq/zh/) T0 |
| 中文理论重建 | **The Type「孔雀计划」** | 专章谈行长；不覆盖 standfirst 构图专名 | [孔雀计划索引](https://www.thetype.com/kongque/) T1（专业字体媒体） |

USWDS measure token 数值（官方表）：

| Token | 值 | 官方适用提示 |
|-------|-----|----------------|
| 1 | 44ex | helper，或**较大字号**的小标题/intro |
| 2 | 60ex | 长文舒适区下限附近；66 字符常被当作目标 |
| 3 | 64ex | 长文 |
| 4 | 68ex | **默认正文** `$theme-text-measure` |
| 5 | 72ex | 长文上限区 |
| 6 | 88ex | 短块、非长读；**默认 lead** `$theme-lead-measure` |

### 4.4 布局原理：为何标题要更窄

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 正文过长的行会让眼睛难以找回下一行行首 | Butterick T0 | Bringhurst/Rutter T1 | 已确认 |
| 行距加大时，可以容忍略长的 measure | [USWDS Typography](https://designsystem.digital.gov/components/typography/) T0 | 与 Butterick「行距与行长联动」方向一致 | 已确认 |
| **大号字占用更多水平空间，宜配较短 measure** | USWDS 同上 T0 | 与「字号↑ → 同物理宽度下 cpl↓」几何事实一致 | 已确认 |
| 标题宜紧行距（约 1.1–1.35），长文至少约 1.5 | USWDS line-height tokens T0 | 设计系统共识，非单一实验论文 | 很可能 |
| 大号标题可略减字距（tracking） | USWDS letterspacing 指导 T0 | — | 很可能（单源官方） |
| 标题换行宜「视觉平衡」，可用 `text-wrap: balance` | CSS 标准能力；MDN/实现稿 | 非本主题核心，作实现注释 | 很可能 |

几何直觉（非独立研究，由上述规则推出）：同一 `max-width: 42rem` 下，72px 标题的 cpl 远小于 20px 正文。若希望标题仍保持 2–3 行的「标题形」，必须**再收窄标题盒子**；若希望 standfirst 接近 60–75 cpl，必须**给它更宽的盒子**。这就是 max-w-2xl vs max-w-4xl 的来源，而不是 Tailwind 官方规定必须如此。

---

## 5. 时间线

| 日期 | 事件 | 来源（Tier） |
|------|------|-------------|
| 1992 起（现通行第 3/4 版） | Bringhurst 写定 45–75 / 理想 66 字符行长 | *Elements of Typographic Style*；[webtypography.net](https://webtypography.net/2.1.2) T1 |
| 2009-02-16 | Guardian 教育用《Typographical terms》将 Standfirst 与 Body 分列 | [PDF](http://image.guardian.co.uk/sys-files/Guardian/documents/2009/02/16/Typographicalterms.pdf) T0 |
| 2012-07 / 2012-09 | Guardian 公开讨论 standfirst 作为 furniture，以及网上标题必须脱离 standfirst 可读 | [Naughton](https://www.theguardian.com/commentisfree/2012/jul/26/subeditor-role-changed)；[Elliott](https://www.theguardian.com/commentisfree/2012/sep/16/headlines-more-easily-misunderstood-online) T0 |
| 2015-09-16 | GOV.UK 设计笔记：桌面正文约 2/3 栏宽、≤75 cpl；独立规定 heading / lead / body 字号 | [Design in government](https://designnotes.blog.gov.uk/2015/09/16/tips-for-creating-good-typography/) T0 |
| 2017 起 | The Type「孔雀计划」从「行长为字号整数倍」重建中文排版论述 | [thetype.com/kongque](https://www.thetype.com/kongque/) T1 |
| 持续维护（检索日仍有效） | USWDS 发布 measure tokens 与 `$theme-lead-measure` 默认 6 | [USWDS settings](https://designsystem.digital.gov/documentation/settings/) T0 |
| 2024-03-20 | USWDS 排版页加 WCAG 2.1 AA 标记 | [Typography updates](https://designsystem.digital.gov/components/typography/) T0 |

本主题不是产品发布，时间线表示**术语与规范被公开写定的节点**，不是功能上线史。

---

## 6. 实体关系

```
[文章入口家具 furniture]
   ├─ Kicker / 肩题 / eyebrow     ← 标题之上
   ├─ Headline / hed / 主题
   └─ Standfirst / deck / 副题    ← 标题之下、正文之前
         │
         ▼
[正文 copy]
   ├─ Lede / lead / 导语          ← 第一段（常被误称为 standfirst）
   ├─ Nut graf（特稿）
   └─ Body / 主体
```

**Measure 关系（西文长文，权威共识）：**

```
display 标题 ──较短 measure──► 少词换行、块面更紧
standfirst / lead ──中等到偏宽──► 一句到一小段仍可读
body ──45–75（Butterick 至 90）──► 舒适阅读
```

**USWDS 默认数值关系（已确认）：** 正文 measure 4（68ex）< lead measure 6（88ex）。标题本身不设单独默认 measure token，靠「大号用更短 measure」的指导自行选择。

---

## 7. 增量信息

### 7.0 增量对照表（多源 diff）

相对「词典式定义」（standfirst/deck/lede 各是什么），下列为官方定义未写成一句口号、但多源可见的增量点。

| 增量主张 | 相对 Tier 0 定义的新增点 | 首见来源（Tier） | 互证来源 | 验证结果 | 置信度 |
|---------|-------------------------|-----------------|---------|---------|--------|
| 网上 headline 必须能脱离 standfirst 独立成立 | Guardian 术语表只定义块，未谈 SEO/社交拆件 | [Elliott 2012](https://www.theguardian.com/commentisfree/2012/sep/16/headlines-more-easily-misunderstood-online) T0 | [Naughton 2012](https://www.theguardian.com/commentisfree/2012/jul/26/subeditor-role-changed) T0 | 已确认 | 已确认 |
| USWDS 默认 lead **宽于**正文 | 排版页强调大号宜短 measure，未在同一句写默认 lead=6 | [Settings](https://designsystem.digital.gov/documentation/settings/) T0 | [Measure tokens](https://designsystem.digital.gov/design-tokens/typesetting/measure/) T0 | 已确认 | 已确认 |
| USWDS 指导「intro 可用 measure 1」与默认 lead=6 **并存** | 同一官方站点两套信号 | [Typography](https://designsystem.digital.gov/components/typography/) T0 | Settings T0 | 已确认（内部张力） | 已确认 |
| Web hero 大量采用「描述比标题更窄」 | 无官方「必须上窄下宽」 | 模板生态 T2 | Shadcn 一例反证「也可以上窄下宽」T2 | 很可能（实践观察） | 很可能 |
| 「上窄下宽」无单一权威英文品类名 | 检索无标准名 | 本 loop 穷尽 | — | 已确认 | 已确认 |
| Wikipedia 把 UK standfirst 写成 lead 的别名 | 与 Guardian 分列冲突 | [Lead paragraph](https://en.wikipedia.org/wiki/Lead_paragraph) T2 | Guardian PDF T0 | 分歧 | — |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| Guardian 认为 standfirst 对记者是 furniture，对许多网上读者则「容易与标题拆开、根本读不到」 | [Elliott 2012](https://www.theguardian.com/commentisfree/2012/sep/16/headlines-more-easily-misunderstood-online) T0 | 已确认 | 对落地的含义：hero 描述不能承担标题没说清的关键事实 |
| USWDS `$theme-text-measure` 默认 4，`$theme-lead-measure` 默认 6 | [Settings](https://designsystem.digital.gov/documentation/settings/) T0 | 已确认 | 官方实现里 **intro 行长 > 正文行长** |
| GOV.UK Lead paragraph 仅建议每页一次、桌面 24px | [Paragraphs](https://design-system.service.gov.uk/styles/paragraphs/) T0 | 已确认 | 功能上接近 standfirst，但与标题同处 2/3 栏，**不强制上窄下宽** |
| 中文复合标题：肩题主虚、副题主实；副题可长于主题、可多行 | 中国新闻培训网写作稿（行业教材，非监管文件） | 很可能 | 单源教材气质，与百科「引题/副题」结构一致 |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源（Tier） | 拒绝原因 |
|----------|-------------|---------|
| 存在名为 “constrained heading + wide lede pattern” 的国际标准或 ISO/W3C 模块 | 检索未发现 | 权威源未覆盖；不得写成已登记模式名 |
| Wiktionary 把 kicker 列为 standfirst 的同义词，故二者等同 | [Wiktionary](https://en.wiktionary.org/wiki/standfirst) T2 | 与 News style / ThoughtCo 的 kicker 多义冲突，不能当唯一事实 |
| 所有现代 SaaS hero「都应该」标题窄、描述宽 | 无 | 与大量模板实践相反；属口味而非规范 |

### 7.3 权威媒体解读

- **Guardian 读者编辑（2012）**：印刷时代标题常依赖配图与 standfirst 才能读懂（例：奥运金牌次日头版一个 “Phew!”）；网上标题出现在 RSS、Twitter、搜索结果里，**读者往往看不到 standfirst**。风格指南因此要求标题本身不可歧义。增量含义：Web 上「宽 standfirst」是**页内阅读体验**，不能替代标题信息架构。
- **Bringhurst → Rutter**：Web 与印刷的本质差是读者能改字号与视口。用 **px 定宽**会让字号变大时 measure 变短；用 **em / ch** 才能锁住字符数。这对「标题一个 max-w、描述另一个 max-w」提出实现警告：两个盒子若都用 px/rem 绝对值，放大字体后标题与描述的 cpl 比例会漂移。
- **USWDS**：把 measure 做成 token，等于承认**同一页面允许多种行长**，而不是「全站一个 max-width」。这是「上窄下宽」在设计系统里的制度基础。

### 7.4 社区与舆论反响

**观点分布（Tier 2，非事实源）：**

- **Hacker News** 多次讨论 “best line length”，主流引用 Bringhurst 45–75 / 66，或 TeX 默认约 66。争论焦点是**正文与代码**，不是 hero 标题与 subtitle 的相对宽度。[例：2025-08「The Best Line Length」](https://news.ycombinator.com/item?id=44839776)；[2013 Bringhurst 引用](https://news.ycombinator.com/item?id=6141422)。
- **检索范围内**，HN / 主流设计媒体**未见**把 “wider standfirst than headline” 当作可检索的热门模式名来争论。
- **组件市场**把差异化 `max-w` 当实现细节随手写，不上升为理论：有的标题 2xl、描述 3xl；有的标题 3xl、描述 2xl。说明实践是**经验法则**，不是学派。

### 7.5 争议与风险

| 风险 | 说明 |
|------|------|
| **可访问性** | 过窄的大标题在放大字号、长德语句、屏幕阅读器用户「标题即摘要」场景下可能被切得难以扫读。GOV.UK / USWDS 更强调 75–90 上限，而不是追求戏剧性收窄。 |
| **标题歧义** | Guardian 已记录：读者只看标题、不看 standfirst，会读错新闻。宽描述救不了坏标题。 |
| **中西文混排** | 西文 66 cpl 与中文「17–40 字、横排硬上限约 48 字」（clreq / 中文实务）不是同一把尺；把 `max-w-2xl` 从英文 hero 原样搬到中文大标题，cpl 会偏长。 |
| **用 lede 指 standfirst** | 跨团队（尤其英美混编）会沟通错位：工程师说 lede 想的是 `<p class="lead">`，编辑说 lede 想的是正文第一段。 |

### 7.6 竞品与行业对照

| 系统 | 标题 vs 描述宽度 | 术语 |
|------|-----------------|------|
| Guardian 印刷/网站 | 由版式决定，无公开 token；概念上 standfirst 是独立样式块 | standfirst |
| USWDS | 大号宜短 measure；**lead 默认比正文宽** | lead / usa-intro |
| GOV.UK | 同栏同宽（2/3），靠**字号**分层不靠不同 max-width | lead paragraph |
| 典型 Tailwind SaaS hero | 常见**描述更窄** | subheadline / description |
| 中文报纸 | 副题可宽于、长于主题（「副题主实」） | 副题 / 导语（后者属正文） |

### 7.7 中文语境

| 中文术语 | 最接近英文 | 说明 |
|----------|------------|------|
| **主题** | headline | 复合标题的中心 |
| **肩题 / 引题 / 眉题** | kicker / overline | 主题之上，宜短、常「主虚」 |
| **副题 / 子题** | deck / standfirst | 主题之下，补事实，「主实」，可多行 |
| **导语** | lede / lead | 消息**第一段**，不是副题 |
| **行长** | measure | clreq：应为字号整数倍 |
| **提要题** | 接近加长 standfirst | 复合标题里的提要，教材有列，西文无完全对等词 |

中文权威渠道（W3C clreq、The Type 孔雀计划）**深入讨论行长与标题占行**，但**不使用 standfirst 一词**，也不把「上窄下宽 hero」写成命名模式。国内产品文案把首页大标题下的灰色说明叫「副标题 / 描述 / 导语」的都有，后一种最容易和新闻导语撞车。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| Standfirst 是不是 lede | Wikipedia *Lead paragraph*：英国把新闻第一段也叫 standfirst | Guardian 术语表：standfirst 是独立块，body 另算 | **以出版物自家术语为准**；跨团队写作时拆开：furniture = standfirst/deck，copy 开篇 = lede |
| Kicker 指哪一段 | 标题上的 overline；稿件结尾 punchline；更大号的开篇词 | 有人当 deck 用 | 避免单独说 kicker；改说 eyebrow 或 deck |
| Deck 指一行标题还是副题 | Glossary 义项 1：headline 的一行 | 义项 2：主标题下的副题 | 上下文写清；Web 产品用 deck 多半是义项 2 |
| Intro 该用短 measure 还是长 measure | USWDS 文案：大号/intro 可用 measure 1 | USWDS 默认 `$theme-lead-measure: 6` | 短句 intro 可偏宽；大号多行标题应偏窄；**不要混用同一 token** |
| Hero 描述该比标题宽还是窄 | 编辑/display 逻辑：标题短 measure | 许多 SaaS：描述当正文收窄 | 按字号与句长选：字号差越大，越应给标题单独、更短的 max-w |

---

## 9. 对用户问题的直接回答

### 9.1 这是什么

是一套**编辑术语 + 一条排版规则**，不是一个注册过的 UI 模式名。

- **最贴切的词**：英式 **standfirst**（标题下的副文段）；美式常说 **deck / dek**；**lede** 严格说是正文导语，口语和部分百科会把它和 standfirst 混用。
- **布局**：通常只能描述为 *centered hero with a wider standfirst/deck*，或 *constrained heading + wide lede*。
- **原理**：标题与描述使用不同 **measure**。大号标题用较短 max-w（如 `max-w-2xl`），描述用更宽 max-w（如 `max-w-4xl` / `max-w-5xl`），做出上窄下宽的收放。权威依据是行长研究（45–75/90 cpl）加上 USWDS「大号文字用更短 measure」，而不是某个名叫 “standfirst layout” 的规范。

### 9.2 有哪些类型

按**位置**：肩题/kicker（上）→ 主题 → 副题/standfirst/deck（下）→ 导语/lede（正文第一段）。

按**Web 宽度关系**：上窄下宽（本主题）、同宽（GOV.UK 式网格）、上宽下窄（常见 SaaS hero）。三者都合法，取决于字号差和句子长度。

### 9.3 有哪些知名产品 / 代表方案

- **术语原产地**：Guardian（standfirst）、英美杂志的 hed/dek。
- **把不同 measure 写成系统**：USWDS（正文 68ex vs lead 88ex）、GOV.UK（Lead paragraph + 2/3 栏 ≤75 cpl）。
- **理论**：Bringhurst / Butterick / Rutter；中文 clreq 与 The Type「行长」。
- **实现工具**：Tailwind 容器尺、`ch`、`usa-intro`、`govuk-body-l`。
- **不要**用 SEO「Top hero patterns」榜单当标准。

---

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方

- [Guardian, *Typographical terms* (PDF), 2009-02-16](http://image.guardian.co.uk/sys-files/Guardian/documents/2009/02/16/Typographicalterms.pdf)
- [Chris Elliott, Guardian readers’ editor, 2012-09-16](https://www.theguardian.com/commentisfree/2012/sep/16/headlines-more-easily-misunderstood-online)
- [Charlotte Naughton, Guardian, 2012-07-26](https://www.theguardian.com/commentisfree/2012/jul/26/subeditor-role-changed)
- [USWDS Typography](https://designsystem.digital.gov/components/typography/)
- [USWDS Measure tokens](https://designsystem.digital.gov/design-tokens/typesetting/measure/)
- [USWDS Settings（含 `$theme-lead-measure`）](https://designsystem.digital.gov/documentation/settings/)
- [USWDS Prose / `usa-intro`](https://designsystem.digital.gov/components/prose/)
- [GOV.UK Design System — Paragraphs (Lead)](https://design-system.service.gov.uk/styles/paragraphs/)
- [GOV.UK Design System — Layout](https://design-system.service.gov.uk/styles/layout/)
- [Design in government: Tips for creating good typography, 2015-09-16](https://designnotes.blog.gov.uk/2015/09/16/tips-for-creating-good-typography/)
- [Butterick, *Line length*](https://practicaltypography.com/line-length.html)
- [W3C *Requirements for Chinese Text Layout*（中文排版需求）](https://w3c.github.io/clreq/zh/)

### Tier 1 权威媒体 / 词典 / 经典转写

- [Merriam-Webster: lede](https://www.merriam-webster.com/dictionary/lede)
- [Collins: standfirst](https://www.collinsdictionary.com/dictionary/english/standfirst)（检索日遇 Cloudflare 挑战，定义与公开词典条目一致：introductory paragraph in larger/bolder type）
- [Richard Rutter, *The Elements of Typographic Style Applied to the Web* §2.1.2](https://webtypography.net/2.1.2)
- [The Type：孔雀计划](https://www.thetype.com/kongque/)
- [The Type：孔雀计划序，2019-02-15](https://www.thetype.com/2019/02/12498/)

### Tier 2 补充（反响 / 术语索引 / 实现示例）

- [Wikipedia: Lead paragraph](https://en.wikipedia.org/wiki/Lead_paragraph)
- [Wikipedia: Glossary of journalism](https://en.wikipedia.org/wiki/Glossary_of_journalism)
- [Wikipedia: News style](https://en.wikipedia.org/wiki/News_style)
- [Wiktionary: standfirst](https://en.wiktionary.org/wiki/standfirst)
- [Language Log: hed, dek, lede](https://itre.cis.upenn.edu/~myl/languagelog/archives/004380.html)
- [David Agnew, How to Write Better Deks, 2022-05-03](https://www.davidagnew.com/2022/05/03/how-to-write-better-deks/)
- [HN: The Best Line Length](https://news.ycombinator.com/item?id=44839776)
- [Shadcn UI Blocks: Simple Centred hero](https://www.shadcn-ui-blocks.com/blocks/marketing/hero-sections/simple-centred)
- [Tailwind CSS max-width](https://tailwindcss.com/docs/max-width)

---

## 附录：验收自检（§5）

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | 本地隔离 | 未读取客户业务文档 |
| 2 | Loop ≥3 | 6 轮 |
| 3 | 权威来源 | 核心定义来自 Guardian / USWDS / GOV.UK / Butterick / 词典 |
| 4 | 多源验证 | 执行摘要事实均有对照 |
| 5–9 | 增量与拒绝 | §7 已填；无农场文定稿 |
| 10 | 反响 | HN 有 measure、无本布局专名 |
| 12 | Fetch | Guardian PDF、USWDS 多页、GOV.UK、Butterick、Rutter、Wiktionary |
| 14 | 三问 | §4.1–4.3 与 §9 对应 |
| 15 | 无编造 | 未虚构 URL；Collins/MW 正文曾被 Cloudflare 拦截，定义以公开条目与二次引述标注 |

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-08-30，共 6 轮 loop。*
