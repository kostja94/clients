# Marketing 页面模板

本文档为 Alignify Marketing 类页面的标准模板，用于创建或优化营销策略指南、方法论指南（如关键词调研、竞品调研、联盟营销、红人营销、GEO、外链建设等）。

**参考**：content-rules、[section 文档](../README.md)、[README.md](../README.md)、[template-tools](./best-ranking.md)、[bloglayout](./bloglayout.md)、[section-consistency](../consistency.md)（字数与表达一致性）

**内容格式（2026-08）**：**新文** `content/blog/{locale}/{slug}.md` + `/blog/{slug}`；**存量** `content/marketing/` 不重迁。正文用 `<!-- block:section -->` + Markdown `##`/`###`；列表/表格用 `childrenHtml`（见 [`anatomy.md`](../anatomy.md) §四·一）。

**首篇落地**：关键词调研（存量 `content/marketing/zh/keyword-research.md`）；blog 路由范例：`content/blog/zh/rate-limit-reset.md`、`wrapped-marketing.md`

---

## 〇、一致性规范（必读）

**目标**：同一类型（Marketing）页面之间 **H2 格式、方法论结构、语气** 一致；正文篇幅见 [section-consistency §〇–§二](../consistency.md#〇字数层级硬底线-vs-建议必读)。

- **跨页面**：结构、标题格式与表达习惯对齐；**不**强制各章总字数逐页相等
- **章节间**：避免极短与极长章节相邻
- **章节内**：并列块不宜约 3 倍以上长短差

**统一篇幅**：见 [section-consistency](../consistency.md) + 下文「Marketing 页面字数速查」。

**EN/ZH 结构同步（必读）**：创建或优化任一语言版本后，**必须**同步另一语言版本的 section 顺序与锚点 id（`## … {#id}`）。内容语言不同，但 md 章节结构须一一对应。

**语言硬约束**：EN md 文件中所有面向用户的文本（H2、H3、段落）**必须**是英文。若 Brief 采用 FAQ → Step 08 注册 `faq-data.json` **7 问**（见 [faq.md](../sections/faq.md)）。

---

## 一、页面结构（参考模板）

> **内容优先**：下列为 Marketing 类**常见结构**；具体节数与顺序由 Step 01/05 大纲决定。A 层见 [`anatomy.md`](../anatomy.md) §〇。

```
1. 核心要点（TL;DR，40–80字 intro + 4–5 条 items）← [tldr.md](../sections/tldr.md)
2. 什么是 XXX ← [what-is.md](../sections/what-is.md)
3. 核心方法论 / 步骤 / 框架（按主题展开，可含表格、列表）— 主体节
4. 如何实施（How To）← **可选**，正文 section，[how-to.md](../sections/how-to.md)（**仅方法驱动型采用**；策略分析/观点文不设，见 how-to.md「适用范围」）
5. 结论 ← [conclusion.md](../conclusion.md)
6. FAQ ← [faq.md](../sections/faq.md)（**7 问**）
7. References（可选）← [references.md](../sections/references.md)
```

**A 层**：md 以 `#conclusion` 收束；Brief 采用 FAQ 则 JSON 7 问、答案无内链。

**常见组合**（非强制五节清单）：核心要点 + 什么是 + 主体方法论 + [如何实施] + 结论 + FAQ。Hub 索引页（如 `marketing-types`）可大幅简化。

> **如何实施非默认章节（2026-08 修订）**：只有「方法论/操作驱动」的 Marketing 文（如 keyword-research、localization-strategy）才有决策路径可走；「策略判断/观点」文（如 rate-limit-reset、competitive-analysis 的判断型正文）用分析节表达落地，**禁止**套 step-1~N 步骤。判据见 [how-to.md](../sections/how-to.md)「适用范围」。

例外：`marketing-types` 等 Hub 索引页可不含如何选择/如何实施 section。

### 1.1 可选章节（参考，非骨架）

**结构纯粹由内容决定**——Step 01/05 根据读者任务与 SSOT 定 H2，**不**套用固定「A/B 骨架」。下表仅为**何时常用 / 何时可省**的参考；省略须在 Brief 写一句理由。

| 章节 | 常用场景 | 可省略时 |
|------|----------|----------|
| **TL;DR** | 搜索意图需 10 秒内直答；方法论入门 | 长文叙事已开篇即答（如 `rate-limit-reset`）；省略不降级 |
| **什么是** | 几乎总是 | 极短 Hub 索引 |
| **How To** | 方法/操作驱动（keyword-research） | 策略判断/观点文；见 [how-to.md](../sections/how-to.md) |
| **FAQ** | PAA 有独立决策点、正文未覆盖 | 正文已穷尽问答、FAQ 会重复（如部分 campaign 长文） |
| **结论** | 几乎总是 | — |
| **References** | 有事件相关一手源 | 无合格引用时可省 |

**已发布范例（仅作对照，非模板）**：`keyword-research`（TL;DR + FAQ JSON）· `rate-limit-reset`（正文无 TL;DR/FAQ section，**JSON 侧车仍有** — 页面上会显示）· `coding-plan`（同上）。**新文照内容画大纲，Brief 与 JSON 须一致（E10）。**

**Step 04 截图**：仅 `best-ranking` / `best-ranking-legacy` 走 [`04-screenshots.md`](../../04-screenshots.md)。Marketing / Blog / Insights **跳过 Step 04**；OG 封面见 [`ops/og-covers.md`](../../../ops/og-covers.md)。

**内链**：Brief 的 Planned internal links **只列已上线 slug**。未发布主题可文字提及，**禁止** `href`（Gate **G6** · [marketing-internal-links.md §M11](../marketing-internal-links.md)）。

**Marketing 页面三种题材倾向**（帮助选题，**不**决定必有章节）：

| 类型 | 代表页面 | 正文特征 |
|------|----------|----------|
| **A 类 — 策略框架型** | affiliate、keyword-research、competitive-analysis、pricing-strategy | 方法论驱动，章节以步骤/框架/分析维度为主 |
| **B 类 — 平台战术型** | reddit、x-formerly-twitter、geo、email-marketing | 围绕特定平台展开，含平台机制解析 + 操作指南 |
| **C 类 — 项目运营型** | creator-program、influencer、referral-program、lifetime-deal、localization-strategy | 以「如何搭建/运营一个项目」为主线，含激励机制、招募、平台分析 |

创建新页面时，先判断**题材倾向**再画 H2 大纲——**不**预设 TL;DR/FAQ/How To 必有；采用或省略各可选节须在 Brief 说明理由。

**与 Tools 的差异**：Marketing 无产品 H3 榜单、应用场景专节；正文以方法论为主，可含工具参考表（UTM 外链）。

**Marketing 页面字数速查**：

| 章节 | 中文 | 英文 | 导向 |
|------|------|------|------|
| **meta title** | 25-32 字 | 50-60 字符 | SEO |
| **meta description** | 60-80 字 | 120-158 字符 | SEO |
| **H1 (title)** | 14-22 字 | 40-60 字符 | 用户可读性 |
| **excerpt** | 100-150 字 | 200-250 字符 | 用户可读性 |
| 核心要点 intro | 40–80 字 | 40–70 词 | GEO |
| 核心要点 items | 4–5 条，每条 25–40 字，同组长度相近 | 4–5 条，每条 18–28 词，同组长度相近 | GEO |
| 什么是 | 约 **180–380 字** | 约 **150–280 词** | 与 [what-is.md](../sections/what-is.md) 一致 |
| How To 每步骤 | 约 **60–140 字** | 约 **50–120 词** | 步骤间不宜悬殊 |
| 结论 | 见 [conclusion.md §2.3](../conclusion.md) | 见 [conclusion.md §2.3](../conclusion.md) | - |
| FAQ 答案 | 约 **60–120 字** | 约 **40–80 词** | - |

---

## 二、Metadata 与 Frontmatter

> Meta title/description → **`blog-meta.ts`**（新文）；存量 `content/marketing/` 页仍可能用 `marketing-meta.ts`。H1/excerpt → md frontmatter `title`/`description`。

### 2.2 SEO 导向（meta title、meta description）

**详见**：[meta.md](../meta.md) §一–二（字数、模板、CTA）、[meta.md](../meta.md)（像素值、截断机制）。

**Marketing 特有约束**：
- 中文不含「指南」，英文不含 "Guide"
- 常青内容不含年份
- 主动语态：探索/掌握…比较…立即学习/开始实践

### 2.3 用户可读性导向（H1、excerpt）

**完整规范**：见 [meta.md](../meta.md) §三–四（字数、三段式结构）、[sections/generic.md](../sections/generic.md)（H1-H6 层级与可访问性）。H1 与 excerpt 的**文案构建形式**须符合跨类型统一格式（`[策略]：[价值]`；excerpt 三段式首句→中段→收尾）。

### 2.4 Hero 区域

**全站 blog / marketing / tools md**：**禁止** frontmatter `heroHtml:` / `heroContent:`（E44）。导语、框架名、姊妹篇内链写在 **`## 什么是…`（或等价首节）首段 BLUF**（≥3 句）；EN 同理。`description` 承担 excerpt 级摘要。

**可选** OG 配图：`heroImage` + `heroImageAlt`（见 `anatomy.md` §二）。

**送审前**：`python scripts/audit/audit-frontmatter.py` — 0 issues。

**已废弃**（E44）：

```yaml
# ❌ 勿写
heroHtml: |
  <h3>…</h3>
```

### 2.5 中英文页面差异

| 项目 | 中文 | 英文 |
|------|------|------|
| pageUrl | `/zh/blog/[slug]` | `/blog/[slug]` |
| readTime | `XX 分钟阅读` | `XX min read` |
| 日期格式 | `2026年1月15日` | `January 15, 2026` |
| Introduction 标题 | 文章简介 | Introduction |
| Conclusion 标题 | 结论 | Conclusion |
| FAQ 数量 | **7 问** | **7 问** |

---

## 三、正文写法（Markdown）

| 章节 | 写法 | 规范 |
|------|------|------|
| 核心要点 | `tldr-data.json`（Step 08） | [tldr.md](../sections/tldr.md) |
| 什么是 XXX | `## … {#id}` + 段落 | [what-is.md](../sections/what-is.md) |
| 方法论/步骤 | `##` / `###`；列表/表格 → `childrenHtml` | [anatomy.md](../anatomy.md) §四·一 |
| 如何实施 | `## 如何实施…` + `###`（可选） | [how-to.md](../sections/how-to.md) |
| 结论 | `## 结论 {#conclusion}` | [conclusion.md](../conclusion.md) |
| FAQ | `faq-data.json`（Step 08 · 页底全局组件） | [faq.md](../sections/faq.md) |
| References | `references-data.json`（Step 08） | [references.md](../sections/references.md) |
| Hero | **全站无** frontmatter hero；首段 BLUF + 正文内链 | E44 · `anatomy.md` §二 |

**H2 间距**：容器 `space-y-12`；正文 H2 之间不加 divider。

---

## 四、Marketing 各章节特有规则

### 4.1 核心要点（Tldr）

- **JSON 注册**：`tldr-data.json`；参见 [tldr.md](../sections/tldr.md) § 4.2 Marketing 页面
- **introduction**：40–80 字，含 [策略名称]、[方法关键词]、[受众]；直答式
- **items**：4–5 条，每条 25–40 字，同组长度相近
- **内容方向**：核心价值+数据、完整方法论、工具+案例、适用受众

### 4.2 什么是 XXX

- **结构**：常见 **2–4 段**；首段定义+价值+适用人群；后续段可写边界与分流；内链按 [what-is.md](../sections/what-is.md)
- **术语密集型主题**（如 Wrapped / 年终回顾、**AI 提交署名**）：须在「什么是」节列出**全部行业别名**（表格或并列段），并写清与易混概念（如平台聚合报告、**广告归因**）的边界。译法 SSOT：`terminology-glossary.md` §六 · `marketing-glossary.json`
- **篇幅**：见 [section-consistency §二](../consistency.md#二通用字数与篇幅建议区间)
- **内链**：与主题有强功能/工作流关联

### 4.2b 策略适用性节（campaign / GTM 专题）

当题材回答「什么产品该用这个营销策略」时，正文须设独立 H2（如「哪些产品适合…」），含 **go / no-go 决策矩阵** + **按产品形态的分流**——二者均用 **prose** 表达，遵守 [`presentation.md`](../presentation.md) **生成顺序协议**：

1. H2 首段 BLUF **≥3 句**（含为何要做 go/no-go，末句自然引出矩阵表，**禁止**「…如下：」独段）
2. `childrenHtml` 决策矩阵表
3. 表后 **≥2 句** prose 写形态分流（Cursor / Lovable / 垂直 copilot 等写在**同一段或连续长段**，**禁止**表后单句案例收尾）

目标读者为 founder 时，案例节优先 **AI / Agent** 垂直，不必铺全量 C 端（音乐、外卖等）案例表。

### 4.3 正文章节（方法论、步骤、框架）

- **结构**：按主题分 H2/H3，每节聚焦一个子问题
- **H3/H4 写法**：用 Markdown `### 小节 {#anchor}` / `#### …`，**禁止**在 `childrenHtml` 内写 `<h3 class="text-lg font-semibold…">`（遗留格式，见 [anatomy.md §四·一](../anatomy.md)）
- **childrenHtml 范围**：仅 **列表**（`<ul>`/`<ol>`）、**表格**（`<div class="content-html"><table>`）、**图片网格**；正文段落用 Markdown
- **可含**：表格、列表、工具参考表
- **外链**：使用 `addUtmToExternalLink()` 添加 UTM
- **内容分块**：每块可独立回答一个子查询，利于 AI 提取与 Featured Snippets

### 4.4 How To（如何实施）

**仅方法驱动型设置**（判据见 [sections/how-to.md](../sections/how-to.md) 适用范围）；策略判断/观点文**不设**此节。

- **禁止**：链接、具体产品名、工具名、平台名
- **使用通用表述**：如「趋势类工具」「问题汇总工具」「关键词挖掘工具」
- **步骤数**：3–5 步（按主题复杂度，见 [sections/how-to.md](../sections/how-to.md) Part 2）
- **每步骤**：动词开头 + 分叉短语；内容优先，字数仅质检参考（建议约 **60–140 字**，见 [sections/how-to.md](../sections/how-to.md) Part 3）

### 4.5 结论

- **可含**：**0–2** 条内链（见 [conclusion.md](../conclusion.md) §3.2、§4）
- **禁止**：外链；清单式延伸阅读
- **篇幅**：见 [conclusion.md](../conclusion.md) §2.3

### 4.6 FAQ

- **数量**：**7 问**（`faq-data.json`）
- **禁止**：内链、手动 H2
- **答案**：见 [faq.md](../sections/faq.md) 与 [section-consistency §二](../consistency.md#二通用字数与篇幅建议区间)

### 4.7 References

- **可选**：置于 FAQ 之后；无合格**事件相关**源时可整节省略
- **仅收录**（见 [references.md §3.2](../sections/references.md#32-引用分型2026-08-起--marketing--blog-策略文强制)）：
  - **A** 带日期的政策/公告/事故一手页（官方 Help、Changelog、定价变更说明）
  - **B** Tier 1 媒体对**具体事件**的报道
- **禁止进 References**：
  - 与本文同题的增长策略文、Freemium/GTM playbook、Substack 技巧帖（类型 D）
  - 仅用于对比表/Benchmark 的竞品静态 docs（类型 C → 正文内链 + Source Map）
- **目标条数**：通常 3–6 条；description 须写明事件或政策，勿写「行业对照」

---

## 五、内容最佳实践（Blog md · 策略文）

> **呈现 SSOT**：段落节奏以 [`presentation.md`](../presentation.md) 为准；本表 SEO/GEO 实践与其**不冲突**——BLUF 与 Answer Block 用**长段首段**表达，不用伪列表替代正文。

| 实践 | 说明 |
|------|------|
| **意图映射** | 先诊断搜索意图：informational vs transactional；内容与意图匹配 |
| **E-E-A-T** | 展示 Expertise、Experience、Authoritativeness、Trust；数据和引用可增强可信度 |
| **内容分块** | 每 major H2 为独立可回答块：**首段 BLUF（≥3 句 prose）** → 展开分析 → **按需**列表/表格（非默认堆结构） |
| **生成顺序** | 见 [`presentation.md`](../presentation.md) §生成顺序协议 — **先写 BLUF，再 childrenHtml，再表后长段**；禁止表前冒号桥接 |
| **段落优先** | 全文 **≥3 处长段（≥4 句）**；连续短段（≤2 句）**≤2 处**；单句独立段 **≤2 处**（E42）；禁 `**第一，**` + 单句 × N（E37） |
| **表格预算** | 策略/GTM 长文默认 **≤5 张** HTML 表；≥6 须 Brief 说明「必表理由」；案例数据优先 **prose**（E38） |
| **TOC** | 长文可加目录（Table of Contents） |
| **关键词布局** | 自然融入，避免堆砌；Title、H1、intro、H2 含核心词 |
| **Topic Cluster** | 方法论类可考虑 Hub & Spoke：主文 + 衍生专题 |
| **内链** | 见 [`marketing-internal-links.md`](../marketing-internal-links.md)（M1–M11）；**点击意图**优先，无硬性条数 |
| **更新** | 定期更新 modifiedDate 与内容 |

### 5.1 表格 vs prose（策略文）

| 适合表格 | 适合长段落 |
|----------|------------|
| 术语别名对照（Wrapped 名称族） | 案例叙事（Cluely/Wispr 时间线） |
| 决策 go/no-go 矩阵 | 「我的判断」三节合并为 1–2 段 |
| 工具默认行为 benchmark（列多、需扫读） | 跨行业对照（Duolingo/Gymshark 一条链写清） |
| 合规义务清单（FTC 行项） | 单行流程箭头链（勿用 `` ``` ``） |

**范例**：`rate-limit-reset`（长段 + 少量必表）· `keyword-research`（方法论表 + How To prose）

### 5.2 禁止呈现债（生成时 Gate · E40–E42）

| 债类型 | 典型坏例 | 正确做法 |
|--------|----------|----------|
| 表前冒号桥接 | 「…载体完全不同：」+ 表 | 扩成 ≥3 句 BLUF，末句「…对照见下表。」 |
| 孤立标签 | `**按 AI 产品形态：**` 单独一行 | `矩阵过关后，我会再按 AI 产品形态分流：…` |
| 表后单句 | 表 + 「Lovable 分轨：…」一句结束 | 表后 ≥2 句，含判断与 founder 建议 |
| 套话免责声明 | 结论后另起一段「请核对 FAQ…」 | 并入结论最后一段末句（`conclusion.md` §2.4） |
| 列表改 prose 残留 | 删 `<ul>` 留标签行 | Step 06 专门扫 E41 |

**送审前必跑**：`audit-marketing-md-render.py` — E40–E42 **Fail 即不可 audit-ready**。

---

## 六、Meta 注册（新文 · Markdown）

**新文**不写 per-slug `page.tsx`。Meta 注册到 `blog-meta.ts`（或项目约定的 `*-meta.ts`），由动态路由 `app/[locale]/blog/[slug]/page.tsx` 的 `generateMetadata()` 读取。

```ts
// blog-meta.ts 示例键
export const BLOG_META = {
  "rate-limit-reset": {
    title: "…",
    description: "…",
    // …
  },
};
```

正文路径：`content/blog/{locale}/{slug}.md`（见 [`anatomy.md`](../anatomy.md) · [`bloglayout.md`](./bloglayout.md)）。

---

## 七、标准 H2 标题格式与示例

| 章节 | H2 标题格式 | 示例 |
|------|-------------|------|
| 核心要点 | 核心要点（`tldr-data.json` · `title` 字段） | 固定 |
| 介绍 | 什么是 [策略名称] | 什么是关键词调研 |
| 方法论 | [主题] 的 [方法] 步骤 / [主题] 框架 | 关键词调研与 Topical Map 的四步法 |
| 实施 | 如何实施 [策略名称] | 如何实施关键词调研 |
| 结论 | 结论 | 固定 |
| FAQ | 常见问题 | 固定 |

---

## 八、路由与渲染（新文）

- **正文**：`content/blog/{locale}/{slug}.md` + frontmatter + `<!-- block:section -->`
- **Meta**：`blog-meta.ts`（无需新建 `page.tsx`）
- **URL**：`/blog/{slug}` · `/zh/blog/{slug}`

详见 [`bloglayout.md`](./bloglayout.md) §Meta 注册。

---

## 九、质量检查清单

- [ ] **H1 与 excerpt**：符合 [sections/generic.md](../sections/generic.md)
- [ ] 章节完整：至少 **什么是 + 主体 + 结论**；TL;DR / How To / FAQ 按 Brief 采用或已说明省略理由
- [ ] 正文使用 `<!-- block:section -->` + Markdown `##`/`###`
- [ ] childrenHtml 仅用于列表/表格/布局 HTML（E33–E35）
- [ ] 如何实施（若设置）3–5 个 `###` 步骤（见 [how-to.md](../sections/how-to.md)）
- [ ] How To 步骤中禁止链接、产品名、工具名
- [ ] Conclusion 在 FAQ 之前；结论可含 0–2 内链，非清单式
- [ ] FAQ：**若采用**则 JSON **7 问**（E10）；FAQ 无内链
- [ ] 内链：见 [`marketing-internal-links.md`](../marketing-internal-links.md)（M1–M11）；点击意图优先，无机械指路链（M8）
- [ ] 锚文本描述性（策略名/任务名）；同 URL 全页 1 次（含首节 BLUF，M3）
- [ ] 每条链过「三问」：删链后句通顺 · 10 秒感到来对了 · 本段不抢注意力
- [ ] EN md 所有用户面文本为英文
- [ ] EN 与 ZH section 顺序与锚点一致

---

## 十、关键词调研页面示例（首篇落地）

**结构**：

1. 核心要点（Tldr，含「关键词调研」关键词）
2. 什么是关键词调研
3. 关键词调研与 Topical Map 的四步法
4. 如何寻找增量信息
5. 关键词扩展参考（功能词、多语言、有人搜）
6. 如何实施关键词调研（正文 section）
7. 结论
8. FAQ（**7 问**）

**工具参考表**：在正文中可含表格，外链加 UTM。

---

## 十一、常见错误与日期更新

### 11.1 常见错误

- ❌ 新文写入 `content/marketing/` 或注册 `/marketing/{slug}`（应 `content/blog/` + `/blog/{slug}`）
- ❌ blog md 用 GFM 表格或 Markdown 列表（须 `childrenHtml`；E33–E35）
- ❌ blog md 用 Markdown fenced code `` ``` ``（须 prose 或 `<pre><code>`；E36）
- ❌ 伪列表 / 全文碎片短段（E37；须过 [`presentation.md`](../presentation.md)）
- ❌ 表前冒号桥接 / 孤立标签 / 单句段超标（E40–E42；须跑 `audit-marketing-md-render.py`）
- ❌ 策略文 HTML 表 ≥6 且无 Brief 豁免（E38）
- ❌ `childrenHtml` 内 legacy `<h3 class="text-lg…">` / `<p class="text-base md:text-lg…">`（E35）
- ❌ BlogLayout 缺失（存量 TSX 页）
- ❌ frontmatter `heroHtml:` / `heroContent:` / `howTo:`（E44 — 全站禁止；导语写首段 BLUF）
- ❌ frontmatter 区内 HTML 行（E45）
- ❌ frontmatter 未知键 / 缺必填键（E46–E47）；须 `audit-frontmatter.py` Pass
- ❌ 正文使用遗留 JSON `"type": "html"` 裸块 → 须 `<!-- block:section -->` + Markdown
- ❌ Section 块带 `showDivider: true`（存量 JSON 页）
- ❌ 结论位置错误（必须在 FAQ 之前）
- ❌ FAQ 重复 H2
- ❌ 如何实施步骤数 < 3
- ❌ 如何实施步骤中含产品名、链接
- ❌ 外链未加 UTM
- ❌ EN 文件出现中文标题或段落
- ❌ EN 与 ZH 的 section 顺序或锚点 id 不一致
- ❌ EN 文件有中文 H2 但 H1 是英文（半翻译状态）

### 11.2 日期更新规则

**创建**：publishDate 与 modifiedDate 使用当前日期；publishDate 永不更改。

**更新**：modifiedDate 更新为本次更新日期；