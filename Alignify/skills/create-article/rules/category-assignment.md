# Taxonomy v2 — 分类赋值规则

> **SSOT（部署仓）**：`src/data/taxonomy-v2.ts`  
> **迁移脚本**：`scripts/permanent/migrate-taxonomy-v2.py`  
> **Frontmatter 审计**：`scripts/audit/audit-frontmatter.py`

---

## 1. 三个 frontmatter 字段

| 字段 | 含义 | 必填 | 示例 |
|------|------|------|------|
| `pillar` | 主分类（15 值） | ✅ | `dev` · `marketing` · `seo` |
| `section` | Hub 组 / 次主题 | 可选（events 可为空） | `dev-coding` · `content-seo` |
| `contentType` | 文章形态（7 值） | ✅ | `tool-guide` · `strategy` · `architecture` |

**已废弃（E49）**：`category` · `categorySecondary` — 全站 md 不得再出现。

---

## 2. pillar（15 值）

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

---

## 3. section（Hub 组 ID）

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

---

## 4. contentType（7 值）

| 值 | 适用 |
|----|------|
| `tool-guide` | Tools 产品榜 / 对比（默认） |
| `how-to` | 操作教程（`how-to-*` slug 或 HOW_TO_SLUGS） |
| `strategy` | 增长策略（`/marketing/*` 或 STRATEGY_BLOG_SLUGS） |
| `architecture` | 架构选型（headless-cms · git-hosting 等） |
| `reference` | SEO 参考指南 |
| `analysis` | Insights 分析 |
| `event` | Events recap |

---

## 5. 新建文章 Checklist

- [ ] Brief 填写 **Hub / pillar / section / contentType**（见 [`article-brief.md`](./article-brief.md)）
- [ ] frontmatter 写 `pillar` + `contentType`；有 Hub 归属则写 `section`
- [ ] 在对应 `*-pages-config.ts` 注册 slug → hub 映射
- [ ] 跑 `generate-article-category-map.py` 更新面包屑 map
- [ ] 跑 `audit-frontmatter.py` Pass

---

## 6. 与 UI 的关系

- Hero 主 badge：`pillarLabel(pillar)`
- Hero 次 badge：`sectionLabel(section, pillarToChannel(pillar))`
- 面包屑：`ARTICLE_CATEGORY_MAP`（slug → pillar，由 generate 脚本生成）
