#!/usr/bin/env python3
"""Generate rules/templates.md SSOT."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "skills" / "create-article" / "rules" / "templates.md"

CONTENT = r'''# Alignify 文章类型参考（唯一真相源）

> **位置**：`skills/create-article/rules/templates.md`  
> **Last updated**：2026-08-27  
> **说明**：本文档描述**四类存量文章**的常见模式与类型差异。**不是**正文骨架清单；**不要求**与任一现存篇目一比一复刻。  
> **新文默认**：`content/blog/` + `/blog/{slug}`（见 [`article-types.md`](./article-types.md)）。  
> **节怎么写** → [`sections.md`](./sections.md) · **格式/JSON** → [`anatomy.md`](./anatomy.md) · **路由/Meta 注册** → [`article-types.md`](./article-types.md)

---

## 目录

1. [Part 0 · 核心原则（必读）](#part-0-核心原则必读)
2. [Part 1 · 全类型共性](#part-1-全类型共性)
3. [Part 2 · Tools / best-ranking](#part-2-tools--best-ranking)
4. [Part 3 · Marketing](#part-3-marketing)
5. [Part 4 · SEO](#part-4-seo)
6. [Part 5 · Insights](#part-5-insights)
7. [附录 A · 部署仓实证](#附录-a-部署仓实证2026-08-27)
8. [附录 B · 代表篇 H2 地图](#附录-b-代表篇-h2-地图对照用非标准)
9. [附录 C · 各类型 A 层 checklist](#附录-c-各类型-a-层-checklist)

---

<a id="part-0-核心原则必读"></a>

# Part 0 · 核心原则（必读）

## 0.1 模板 = 建议，不是施工图

| 层级 | 含义 |
|------|------|
| **A 硬底线** | 违反即 Fail：结论收束 md、E44 frontmatter、FAQ 7 问（若采用）等 — 见 [`anatomy.md`](./anatomy.md) §〇、[`sections.md`](./sections.md) 附录 B |
| **B/C 类型惯例** | 某 `articleType` **历史上常见**的做法；**可因题材调整或整节省略** |
| **代表篇** | 对照用范例；**不是**必须复制的 H2 清单 |

**即使存量 108 篇 Tools**，线上 H2 标题、顺序、有无对比表/应用场景也**并不统一**。Agent **禁止**为「对齐模板」增删节或改写成机械骨架。

## 0.2 新文 → `/blog`，题材可以从未有过

**迁移政策（2026-08）**：新 slug **统一** `content/blog/` + `blog-meta.ts` + `/blog/{slug}`，不再按频道拆路径。原因：

- 很多新文是**全新题材**（架构科普、GTM 事件、coding-dev…），硬套「Tools 10 节 / Marketing 7 节」无意义
- **类型**由 Brief 的 `articleType` + 内容问题决定，**不是**由 URL 目录决定
- 存量 `/tools/`、`/marketing/`、`/seo/`、`/insights/` **只维护不重迁**

**工作流**：

1. Step 01：Research + **Answer Blocks** → 画出本篇**实际** H2（[`sections.md`](./sections.md) Part 0 Section Plan）
2. 若题材新颖：在 Brief **Type Plan** 写 `articleType` + **参照篇**（可跨类型，或写「无参照，Answer Blocks 驱动」）
3. 仅当需要时才打开本文 Part 2–5 看**类型差异**（Meta 词根、References 分型等）

## 0.3 Brief Type Plan（推荐）

```markdown
| 字段 | 值 |
|------|-----|
| articleType | best-ranking / marketing-strategy / seo-guide / insights-analysis / … |
| 路由 | content/blog/（新文）· 存量路径若维护更新则注明 |
| 参照篇（可选） | video-generator · geo · 无（全新题材） |
|  deliberate 省略 | 无 How To — 策略判断文 · 无对比表 — 仅 2 款产品 |
| Section Plan | 见 sections.md Part 0 |
```

## 0.4 与相关 SSOT 分工

| 文档 | 职责 |
|------|------|
| [`article-types.md`](./article-types.md) | 四类型 × 路径 × Meta 注册表 |
| **本文 `templates.md`** | 类型差异、常见原型、部署仓对照、**禁止误套**说明 |
| [`sections.md`](./sections.md) | 节型写法（TL;DR、什么是、Best H3…） |
| [`anatomy.md`](./anatomy.md) | frontmatter、block、JSON 侧车 |
| [`templates/*.md`](./templates/) | **跳转 stub**，勿编辑 |

---

<a id="part-1-全类型共性"></a>

# Part 1 · 全类型共性

## 1.1 路由与 Meta（新文）

| 项 | 新文（默认） | 存量（维护不重迁） |
|----|-------------|-------------------|
| 正文 | `content/blog/{locale}/{slug}.md` | `content/tools|marketing|seo|insights/…` |
| URL | `/blog/{slug}` · `/zh/blog/{slug}` | 各频道原路径 |
| Meta | `blog-meta.ts` + `blog-pages-config.ts` | 对应 `*-meta.ts` |
| 渲染 | `app/[locale]/blog/[slug]/page.tsx` 动态路由 | 各频道动态路由 |

JSON 侧车键 = frontmatter `pageUrl` 去域路径（如 `/zh/blog/{slug}`）。详见 [`anatomy.md`](./anatomy.md) §二·一。

## 1.2 frontmatter

允许键：`title` · `description` · `slug` · `date` · `updated` · `readingMinutes` · `pageUrl` · `locale` · `category` · `categorySecondary` · `heroImage` · `heroImageAlt`

**禁止（E44）**：`heroHtml` · `howTo` · `heroContent`

## 1.3 正文壳

- `<!-- block:section -->` + Markdown `##` / `###` + `{#kebab-case-id}`
- 列表/表格/复杂 HTML → `childrenHtml`（E35）
- md 以 `## 结论 {#conclusion}` 收束；FAQ 页底全局组件（若 Brief 采用）

## 1.4 Meta 规则组（摘要）

| articleType | title 倾向 | 详见 |
|-------------|-----------|------|
| best-ranking | 含 **Best** / **最佳** + `（2026）：` 副线 | Part 2 · [`meta.md`](./meta.md) |
| marketing-strategy | 策略/案例型 | [`meta.md`](./meta.md) |
| seo-guide | 指南型；**中文 meta 不含「指南」、英文不含 Guide** | Part 4 |
| insights-analysis | 分析/洞察型 | Part 5 |

H1 / excerpt：frontmatter `title` / `description`；**H1 不写年份**。

## 1.5 禁止误套（全类型）

- ❌ 为凑「模板 N 节」加空 H2
- ❌ 新题材硬套 Tools 10 步或 Marketing 7 步
- ❌ 复制代表篇 H2 标题/id（`#author-take`、`#gtm-combo` 等**存量 blog 残留**，新文默认不设 — E49/E50）
- ❌ 正文「细节进 future skills」（E49）
- ✅ Brief Section Plan 与成稿 H2 一致；ZH/EN **对齐实际采用的节**与 anchor id

---

<a id="part-2-tools--best-ranking"></a>

# Part 2 · Tools / best-ranking

> **适用**：工具选型、榜单、对比类。新文 `articleType` 常为 best-ranking；存量 108 篇在 `/tools/`。

## 2.1 常见节型（C 层 — 非强制顺序）

历史上 Tools 长文**经常**出现：

```
[TL;DR JSON] → 什么是 → [技术原理] → Best 产品 H3 主体 → [对比表] → [应用场景] → [如何选择] → 结论 → [FAQ JSON]
```

**部署仓（108 篇 EN）大致比例**：结论 100% · 什么是 ~99% · Best/榜单 ~86% · 应用场景 ~80% · 对比表 ~31% · 标准 `#how-to-choose` ~47%

→ **对比表、应用场景、How To 均可省略**；Brief 写理由即可。

## 2.2 不推荐独立成章（C 层）

Workflow · Cost Analysis · Getting Started · Future Trends — 易与「如何选择」重复，一般不单独开 H2。

## 2.3 Meta 硬约束（A 层 · Tools/best-ranking）

- Meta title **必须**含「最佳」/ `Best`；`（2026）：` / `(2026):` + 副线
- Meta description **≥2** 代表产品名
- H1 **不写年份**；不强制 H1 含「最佳」
- 质检：`scripts/ops/audit-tools-meta-titles.mjs`

节写法 → [`sections.md`](./sections.md) Part 3.1–3.4 · 字数 → [`consistency.md`](./consistency.md)

## 2.4 标杆对照（可选打开 md，勿复制骨架）

| slug | 备注 |
|------|------|
| `video-generator` | 经典 9 H2：what-is → how-it-works → best → comparison → use-cases → how-to-choose |
| `llm` | 多 H3 分组 + 大对比表 |
| `agent-sandbox` | blog 新文 Tools 型范例 |

---

<a id="part-3-marketing"></a>

# Part 3 · Marketing

> **适用**：策略、GTM、渠道、运营。新文走 `/blog/`；存量 16 篇在 `/marketing/`。

## 3.1 原型（建议 — 非固定章节名）

| 原型 | 代表 slug | 读者任务 | 常见 H2 模式 |
|------|-----------|----------|-------------|
| **A 策略框架** | keyword-research, pricing-strategy | 建立方法论 | what-is → 框架/步骤 H2×N → [how-to-implementation] → conclusion |
| **B 平台战术** | geo, x-formerly-twitter | 搞清平台机制+落地 | what-is → 原则/差异 → **多个 how-to-* 散落主体** → cases → conclusion |
| **C 事件/GTM** | rate-limit-reset, coding-plan | 判断+架构+案例 | 开篇即答 → 架构/案例 H2×N → conclusion（**通常无**独立 How To 节） |

**部署仓**：16 篇仅 **~31%** 有独立 How To 型 H2；**禁止**策略/观点文硬套 step-1~N（见 [`sections.md`](./sections.md) Part 3.5）。

## 3.2 Marketing 类型差异（保留在本文）

### TL;DR / 什么是

写法 → [`sections.md`](./sections.md) Part 2.1 / 3.1。Marketing intro 常含策略名+受众；术语密集主题须在「什么是」列**行业别名**（`terminology-glossary.md`）。

### 策略适用性 / go-no-go（仅 marketing-strategy · 可选）

**仅当**题材回答「什么产品/场景该用此策略」时，可设独立 H2 + 决策表 + 表后 prose（≥2 句）。  
**不适用** insights-analysis、架构科普 — **禁止**默认 `#should-you-do-this` 模板表。  
Author POV **写入**适用性/案例/结论节，**不**默认独立 `#author-take`（E50）。

### Marketing How To（可选）

- **仅方法驱动型**（如 keyword-research）
- 步骤内：**禁止**链接、具体产品/平台名；用「关键词挖掘工具」等泛称
- 判据 → [`sections.md`](./sections.md) Part 3.5

### References（Marketing / Blog 策略文）

仅 **A 事件一手 + B 事件报道**；禁止同题第三方 playbook（类型 D）。详见 [`sections.md`](./sections.md) Part 2.3 §3.2。

### 呈现债（Marketing blog md）

E40–E42：表前冒号桥接、表后单句、列表改 prose 残留 → [`presentation.md`](./presentation.md) · `audit-marketing-md-render.py`

内链 M1–M11 → [`internal-links.md`](./internal-links.md) Part 4.5

## 3.3 EN/ZH

EN md 用户可见文本须为英文；section 顺序与 **anchor id 对齐**，节数不必机械一致。

---

<a id="part-4-seo"></a>

# Part 4 · SEO

> **适用**：搜索/索引/结构化数据等指南。存量 38 篇在 `/seo/`；**新 slug 政策**走 `/blog/`（尚无批量范例）。

## 4.1 常见节型（C 层 — 主题驱动）

SEO 文 H2 **因题而异**，常见模式：

- 概念/定义 → 原理或语法 → 最佳实践 → 常见错误 → [工具/验证] → [如何选择] → 结论

**部署仓（38 篇）**：结论 100% · 什么是类 ~71% · How To ~24% · **多数无固定「什么是 XXX」标题**（如 `landing-page` 用 introduction 式 H2）

## 4.2 SEO Meta 差异（A/B 层）

- 中文 meta title：**不含**「指南」
- 英文 meta title：**不含** `Guide`
- 常青内容 meta **不含年份**（与 Tools best-ranking 不同）

## 4.3 正文特点

- 无 Best 产品 H3 榜单（少数对比型除外）
- 列表/表格多用 `childrenHtml`
- How To **可选**；可含 SEO 内链
- 内链 → [`internal-links.md`](./internal-links.md) Part 4

代表对照：`robots-txt`（10 主题 H2）· `landing-page`（要素→优化→CRO 链）

---

<a id="part-5-insights"></a>

# Part 5 · Insights

> **适用**：分析、科普、架构、行业洞察。新文 `articleType: insights-analysis` + `/blog/`；存量 7 篇在 `/insights/`。

## 5.1 结构：Answer Blocks 驱动（非 Marketing 收束）

```
[TL;DR JSON] → 分析 sections×N（由 Brief 问题拆分）→ [案例/边界] → 结论 → [FAQ] → [References]
```

- **主体 H2 从 Answer Blocks 推导** — 例：定义 · 与 X 分工 · 决策对照 · 案例 · 坑/验收
- **默认不设**：`#author-take` · `#should-you-do-this` go/no-go · How To step 节
- **E49**：禁止「细节进 future skills」；**E50**：Author POV 融入案例/坑/结论，非独立收束节
- 第一人称 → [`presentation.md`](./presentation.md) §Author voice

## 5.2 与 Marketing 边界

| 维度 | Insights | Marketing GTM |
|------|----------|---------------|
| go/no-go 矩阵 | 一般不单独 H2 | marketing-strategy 可选 §3.2 |
| How To | 通常省略 | 仅方法驱动型 |
| 全新架构题材 | **首选** insights-analysis + `/blog/` | 勿硬套 GTM 模板 |

代表对照：`reasons-you-need-seo`（9 个主题 H2，无 what-is 式标题）· `subdirectory-hosting`（blog 新文 insights-analysis）

---

<a id="附录-a-部署仓实证2026-08-27"></a>

# 附录 A · 部署仓实证（2026-08-27）

扫描：`alignify production/content/**/en/*.md`

| 频道 | EN 篇数 | 均 H2 | 结论 | 什么是* | How To† | Best/榜单‡ |
|------|---------|-------|------|---------|---------|-----------|
| tools | 108 | 8.8 | 100% | 99% | 高 | 86% |
| blog | 33 | 8.9 | 100% | 91% | 61% | 52% |
| seo | 38 | 8.1 | 100% | 71% | 24% | 26% |
| marketing | 16 | 10.0 | 100% | 100% | 31% | 6% |
| insights | 7 | 少§ | 29% | 43% | 0% | 0% |

\* 正文含 what-is / 什么是 类 H2 或同等 intro 节  
† 含 how-to-choose / 如何选择 / How to 类 H2  
‡ 含 best- / 最好 类 H2 或产品 H3 主体  
§ 多篇仍为 JSON 长文；md H2 少不代表结构薄

**blog 33 篇**：**路由混合类型**，含 Tools 型、Marketing 型、insights 型；7 篇含 `#author-take`、6 篇 `#gtm-combo` — **存量**，新文 skills 已禁。

**结论**：任一频道均**无**100% 统一的 N 节骨架 → 模板只能作 C 层参考。

---

<a id="附录-b-代表篇-h2-地图对照用非标准"></a>

# 附录 B · 代表篇 H2 地图（对照用，非标准）

> 打开部署仓 md **理解节奏**，**不要**复制 id 或强行凑齐下列 H2。

### Tools — `video-generator`（9 H2）

`what-are-ai-video-generators` → `how-ai-video-generation-works` → `best-ai-video-generators-2026` → `comparison` → `use-cases` → `how-to-choose-ai-video-generators` → `conclusion`

### Marketing — `geo`（12 H2，How To 散落）

`what-is-geo` → `geo-principles` → `why-geo` → … → 多个 `how-to-*` → `challenges` → `conclusion`

### Marketing — `keyword-research`（8 H2，含 How To）

`what-is-keyword-research` → … → `how-to-keyword-research` → `conclusion`

### SEO — `robots-txt`（10 H2，主题链）

`what-is-robots-txt` → `core-functions` → `syntax-and-standards` → … → `how-to-choose` → `conclusion`

### Insights — `reasons-you-need-seo`（9 H2，无 what-is 标题）

`why-seo-matters` → `seo-as-google` → `funnel-value` → … → `conclusion`

### Blog 新文 — `subdirectory-hosting`（insights-analysis，内容驱动）

`not-a-new-blog-only-idea` → `what-is-subdirectory-hosting` → … → `conclusion`（**无** author-take / should-you-do-this 模板节）

---

<a id="附录-c-各类型-a-层-checklist"></a>

# 附录 C · 各类型 A 层 checklist

> 完整 P0 → [`quality-checklist.md`](./quality-checklist.md)

| 检查项 | Tools | Marketing | SEO | Insights |
|--------|-------|-----------|-----|----------|
| md `#conclusion` 收束 | ✅ | ✅ | ✅ | ✅ |
| Meta 类型规则 | Best/最佳 | 策略型 | 无 Guide/指南 | 分析型 |
| FAQ 7 问（若采用） | ✅ | ✅ | ✅ | ✅ |
| frontmatter 无 howTo: | ✅ | ✅ | ✅ | ✅ |
| 新文禁 author-take / skills defer | — | ✅ | ✅ | ✅ |
| Best H3 ≥2 产品（若有榜单节） | ✅ | — | — | — |

B/C 层偏离（无对比表、无 How To、H2 仅 5 个…）→ Brief 或 SelfCheck **一句理由**即可。

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 初版：合并 templates/ 五文件；强调模板=建议、新文 /blog、禁止一比一复刻；附录部署仓实证 |

*templates.md · v1.0 · 2026-08-27*
'''

OUT.write_text(CONTENT.strip() + "\n", encoding="utf-8")
print(f"Wrote {OUT} ({len(CONTENT.splitlines())} lines)")
