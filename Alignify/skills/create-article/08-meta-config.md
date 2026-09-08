# Step 8 — Meta + Config + Final CTA + 发布日期

> **规范**：[`meta.md`](meta.md) · [`sections.md`](sections.md) Part 5  
> **部署仓**：`src/data/*-meta.ts` · `*-pages-config.ts` · `*-article-images.ts` · **`src/data/cta-config.json`**  
> **日期脚本**：`scripts/ops/next-publish-date.mjs`  
> **锚定日**：执行 Step 08 时的**实际日历日（UTC+8）**——禁止把文档示例日期当作「今天」

---

## 按 articleType 注册

| articleType | Meta | Config | 图片 |
|-------------|------|--------|------|
| best-ranking | `blog-meta.ts` | `blog-pages-config.ts` | `blog-article-images.ts` |
| best-ranking-legacy | `tools-meta.ts` | `tools-pages-config.ts` | tools 映射 |
| seo-guide | `blog-meta.ts`（**新文**） | `blog-pages-config.ts` | `blog-article-images.ts` |
| marketing-strategy | `blog-meta.ts`（**新文**） | `blog-pages-config.ts` | — |
| insights-analysis | `blog-meta.ts`（**新文**） | `blog-pages-config.ts` | `insights-article-images.ts` |

> **存量不重迁**：仍挂在 `content/marketing/`、`content/seo/` 等的 slug 继续用对应 `*-meta.ts`；**新 slug 一律** `blog-meta.ts` + `blog-pages-config.ts`。详见 [`templates.md`](templates.md)。

---

<a id="taxonomy-v2"></a>

## Taxonomy 分类赋值（pillar / section / contentType）

pillar / section / contentType 三个 frontmatter 字段在本步随 meta 一并注册，是 **Taxonomy v2** 的文档 SSOT。

> **SSOT（部署仓）**：`src/data/taxonomy-v2.ts` · **迁移脚本**：`scripts/permanent/migrate-taxonomy-v2.py` · **Frontmatter 审计**：`scripts/audit/audit-frontmatter.py`

**已废弃（E49）**：`category` · `categorySecondary` —— 全站 md 不得再出现。

### 三个 frontmatter 字段

| 字段 | 含义 | 必填 | 示例 |
|------|------|------|------|
| `pillar` | 主分类（15 值） | ✅ | `dev` · `marketing` · `seo` |
| `section` | Hub 组 / 次主题 | 可选（events 可为空） | `dev-coding` · `content-seo` |
| `contentType` | 文章形态（7 值） | ✅ | `tool-guide` · `strategy` · `architecture` |

### pillar（15 值）

| pillar | 频道 | 说明 |
|--------|------|------|
| `image` · `video` · `audio` · `design` · `3d` | tools | Tools Hub 产品类 |
| `dev` · `search` · `llm` · `productivity` · `vertical` | tools | Tools Hub 技术/效率/垂直 |
| `marketing` | marketing / blog | 增长策略；blog 中 marketingHub 文 |
| `seo` | seo | SEO 指南 |
| `geo` | marketing / blog | GEO 与 AI 可见度（`geo` · `ai-visibility` 等） |
| `insights` | insights | 行业洞察 |
| `events` | events | 活动 recap |

**推导优先级**（迁移脚本 / 人工赋值一致）：

1. `PILLAR_OVERRIDES`（如 blog/`ai-visibility` → `geo`）
2. 频道默认（seo → `seo`，marketing → `marketing`，insights → `insights`，events → `events`）
3. `section` 落在 Marketing / SEO / Insights section 集合 → 对应 pillar
4. Tools `hubGroup` → `TOOLS_HUB_GROUP_TO_PILLAR` 映射
5. 兜底 `dev`

### section（Hub 组 ID）

| 来源 | 配置 SSOT | hub 字段名 |
|------|-----------|------------|
| `/tools/*` | `tools-pages-config.ts` | `hubGroup` |
| `/seo/*` | `seo-pages-config.ts` | `group` |
| `/marketing/*` | `marketing-pages-config.ts` | `group` |
| `/blog/*`（Tools 向） | `blog-pages-config.ts` | `toolsHubCategory` |
| `/blog/*`（Marketing 向） | `blog-pages-config.ts` | `marketingHubCategory` |
| `/insights/*` | 脚本内 `INSIGHTS_SECTION` 映射 | — |
| `/events/*` | 空字符串 | — |

**注意**：`marketingHubCategory: "content"` 已 normalize 为 **`content-seo`**（egc-marketing 等）。

### contentType（7 值）

| 值 | 适用 |
|----|------|
| `tool-guide` | Tools 产品榜 / 对比（默认） |
| `how-to` | 操作教程（`how-to-*` slug 或 HOW_TO_SLUGS） |
| `strategy` | 增长策略（`/marketing/*` 或 STRATEGY_BLOG_SLUGS） |
| `architecture` | 架构选型（headless-cms · git-hosting 等） |
| `reference` | SEO 参考指南 |
| `analysis` | Insights 分析 |
| `event` | Events recap |

### 新建文章 Checklist

- [ ] Brief 填写 **Hub / pillar / section / contentType**（见 [`article-brief.md`](article-brief.md)）
- [ ] frontmatter 写 `pillar` + `contentType`；有 Hub 归属则写 `section`
- [ ] 在对应 `*-pages-config.ts` 注册 slug → hub 映射
- [ ] 跑 `generate-article-category-map.py` 更新面包屑 map
- [ ] 跑 `audit-frontmatter.py` Pass

### 与 UI 的关系

- Hero 主 badge：`pillarLabel(pillar)`
- Hero 次 badge：`sectionLabel(section, pillarToChannel(pillar))`
- 面包屑：`ARTICLE_CATEGORY_MAP`（slug → pillar，由 generate 脚本生成）

---

## TL;DR / FAQ / References JSON（与 meta 同批）

**线上 SSOT = JSON 侧车**（见 [`anatomy.md`](anatomy.md) §二·一）。**Brief 采用 FAQ/TL;DR/References 时**，Step 08 注册（**不写 md**）：

| 文件 | 键 | 内容 |
|------|-----|------|
| `src/data/tldr-data.json` | `pages["{pageUrl路径}"]` | `introduction` + `items[]` |
| `src/data/faq-data.json` | 同上 pathname | `items[]` × **7** |
| `src/data/references-data.json` | 同上 pathname | `items[]` |

**键格式** = frontmatter `pageUrl` 去域路径（中英各一），全频道键表见 [`anatomy.md`](anatomy.md) §二·一。极简示例：blog 新文 `/blog/{slug}`（EN）· `/zh/blog/{slug}`（ZH）。

**Brief 省略** TL;DR/FAQ/Refs → 三 JSON **不得**留对应键（否则页面上仍会显示）。

验收：人工核对 JSON 键与 Brief；`npm run verify:content-json` 实际跑 `verify-content-md.py`（**不验 JSON/E10**）。

---

## blog-meta.ts 示例

```ts
"{slug}": {
  en: { title: "Best … (2026): … | Alignify", description: "…" },
  zh: { title: "最佳…（2026）：… | Alignify", description: "探索2026年最佳…" },
  publishDate: "2026-06-23T00:00:00+08:00",
  modifiedDate: "2026-06-23T00:00:00+08:00",
},
```

- `publishDate` / `modifiedDate` 为 **slug 级** ISO 字段
- Hub 归属由 frontmatter `pillar` + `section` 推导；**无** `routeCategory`（Taxonomy v2，见下文 [Taxonomy 分类赋值](#taxonomy-v2)）

---

<a id="发布日期与-modifieddate"></a>

## 发布日期与 modifiedDate

### 双源格式

| 位置 | 格式 |
|------|------|
| `*-meta.ts` | ISO `T00:00:00+08:00` |
| md frontmatter `date` / `updated` | `"2026年8月26日"` / `"August 26, 2026"` |

同一日历日须一致。

### 核心规则

| 规则 | 说明 |
|------|------|
| **R1 新 slug 唯一** | 每个**新注册** slug 的 `publishDate` 日历日，在**全站所有** `*-meta.ts` 中**不得与任何已有 slug 重复** |
| **R2 已上线不改** | 已上线 slug 的 `publishDate` **永不更改**（内容大改只更新 `modifiedDate`） |
| **R3 双源一致** | `*-meta.ts` ISO 与 md frontmatter `date` **同一日历日**；`updated` / `modifiedDate` = 本次内容变更日 |
| **R4 时区** | 一律 `T00:00:00+08:00` |
| **R5 批量错开** | 同批多篇新文：每篇占用**不同**日历日，按脚本顺序分配 |

**新建 vs 更新**：

| 场景 | `publishDate` / md `date` | `modifiedDate` / md `updated` |
|------|---------------------------|-------------------------------|
| **新 slug 首发** | 分配**新的唯一**日历日（通常 ≈ 锚定日） | 与 publishDate **相同** |
| **已上线 slug 改版** | **不变** | 更新为锚定日 |

### 执行流程（注册 meta 前必做）

**禁止**手写日期或复制邻近 slug。

#### 1. 查占用 & 取下一天

部署仓根目录（或设 `ALIGNIFY_DEPLOY_ROOT`）：

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs
```

输出示例（锚定日 2026-08-26）：

```
Next free publishDate: 2026-08-26
ISO: 2026-08-26T00:00:00+08:00
ZH md date: 2026年8月26日
EN md date: August 26, 2026
```

同批第二篇起：

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --from 2026-08-27
```

#### 2. 注册前校验

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --check 2026-08-26
```

- 输出 `OK` → 可用  
- 输出 `BLOCKED` → 换 `--from` 再取下一空闲日

#### 3. 写入（须同一日历日）

| 位置 | 字段 | 示例 |
|------|------|------|
| `src/data/{channel}-meta.ts` | `publishDate` | `"2026-08-26T00:00:00+08:00"` |
| `src/data/{channel}-meta.ts` | `modifiedDate`（新 slug） | 同 publishDate |
| `content/.../zh/{slug}.md` | `date` / `updated` | `"2026年8月26日"` |
| `content/.../en/{slug}.md` | `date` / `updated` | `"August 26, 2026"` |

#### 4. 审计占用（可选）

```powershell
node E:\clients\Alignify\scripts\ops\next-publish-date.mjs --list
```

标记 `[DUPLICATE]` 的为历史遗留；**新 slug 禁止再占用这些日**。

### 多频道

扫描范围含全部 meta 文件，**不限频道**：

`blog-meta.ts` · `tools-meta.ts` · `seo-meta.ts` · `marketing-meta.ts` · `insights-meta.ts` · `events-meta.ts`

新 marketing 文占用 2026-08-26 后，同日不能再注册 blog/seo 新 slug。

### 改版与存量 `/tools/`

**已上线 slug 改版（任意频道）**

| 字段 | 操作 |
|------|------|
| `publishDate` / md `date` | **不改** |
| `modifiedDate` / md `updated` | → 锚定日 |

- **例外**：纯格式迁移（无内容变更）→ **不**更新 modifiedDate

**存量 `best-ranking-legacy`（`/tools/{slug}`）**

| 规则 | 说明 |
|------|------|
| 更新时机 | 内容实质改版时 |
| 写入 | `tools-meta.ts` → `modifiedDate` + md frontmatter `updated` |
| 批量节奏 | 保守：**同日 ≤2 篇** |
| publishDate | **永不改** |

### 相关日期字段（其他文档）

| 主题 | 位置 | 说明 |
|------|------|------|
| Meta title 年份 | [`meta.md`](meta.md) | H1 不含年份；新鲜度由 publishDate/modifiedDate 表达 |
| E20 / E26 | [`common-errors.md`](common-errors.md) | publishDate 被改 · 新 slug 同日冲突 |
| Brief publishDate | [`01-intake.md`](01-intake.md) | Intake 可登记计划发布日 |
| Insights 改版同步 | [`internal-links.md`](internal-links.md) Part 5 | `blogLayout.modifiedDate` · OG · RSS |
| RSS / Sitemap | [`../ops/feed.md`](../ops/feed.md) · [`../ops/sitemap.md`](../ops/sitemap.md) | 按 modifiedDate；勿用 `new Date()` |
| 脚本说明 | [`scripts/README.md`](../../scripts/README.md) | `next-publish-date.mjs` 参数 |
| 全站日期清单 | [`../ops/article-dates.md`](../ops/article-dates.md) | 各 slug 的 publishDate / modifiedDate |

### 日期常见错误

| 错误 | 正确 |
|------|------|
| 把 skill 示例 `2026-06-23` 当今天 | 以执行日为准，跑脚本取日 |
| 新 slug 与已有 slug 同日 publishDate | `--check` 后换下一空闲日 |
| 大改版改掉 publishDate | 只改 modifiedDate |
| meta 与 md `date` 差一天 | 三处同一日历日 |
| legacy tools 同日改 >2 篇 modifiedDate | 错开至下一日历日 |

见 [`common-errors.md`](common-errors.md) **E20**、**E26**。

> **publish-ready 后**：新 slug 首发前复核本节日期字段已与 meta/md 一致；无需单独 Step。发布后运维 → [`../ops/README.md`](../ops/README.md)

---

## Final CTA（页底 SecondaryCta）

与 meta **同批**写入 `src/data/cta-config.json` → `slugs.{slug}`：

```json
"{slug}": {
  "zh": {
    "title": "一句 punchline（Brief Final CTA 草案）",
    "description": "1–2 句，承接结论或 Author POV",
    "cta": "开始合作"
  },
  "en": {
    "title": "English punchline (draft OK; finalize after Step 09)",
    "description": "1–2 sentences tied to EN conclusion",
    "cta": "Work with us"
  }
}
```

- Brief **Step 02** 须含 **Final CTA** 四字段（见 [`article-brief.md`](article-brief.md)）
- Step 09 EN 完稿后更新 `en.title` / `en.description`
- 验收：`node E:\clients\Alignify\scripts\ops\merge-cta-slugs.mjs --check` → `Missing: 0`

细则：[`sections.md`](sections.md) Part 5

---

## 检查

- [ ] Meta title/description 符合 [`meta.md`](meta.md)
- [ ] **新 slug**：`next-publish-date.mjs --check` Pass；publishDate 全站唯一
- [ ] **改版 slug**：publishDate 未改；modifiedDate = 锚定日
- [ ] **legacy `/tools/`**（若适用）：同日 modifiedDate 更新 ≤2 篇
- [ ] meta ISO 与 md frontmatter 日历日一致
- [ ] `*-pages-config.ts` 已注册
- [ ] **`cta-config.json`** 已注册 `slugs.{slug}`（ZH + EN；非 fallback）
- [ ] frontmatter `pageUrl` 与频道一致
- [ ] sitemap 自动从 config 生成，无需手改

下一步：若 EN 轨尚未完成 → [`content-locale.md`](content-locale.md) Part 4（Step 09）；否则 → Part 5（09c 对等对比）→ [quality-gates.md](quality-gates.md)

---

*08-meta-config · v3.0 · 2026-09-09 · 含原 Step 11 发布日期 SSOT · v3.0：并入原 category-assignment（Taxonomy 分类赋值 pillar/section/contentType）*
