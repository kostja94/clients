# Vofy Sitemap 优化计划

> 参考：[xml-sitemap skill 最佳实践](https://github.com/kostja94/marketing-skills/blob/main/skills/seo/technical/sitemap/SKILL.md) · [Sitemap SEO Guide](https://alignify.co/seo/sitemap)  
> 关联：[vofy-site-structure.md](./vofy-site-structure.md) · [vofy-keywords.md](./vofy-keywords.md)  
> **Sitemap 快照**：[https://www.vofy.art/sitemap.xml](https://www.vofy.art/sitemap.xml)（2026-06-18 lastmod · 2026-06-22 审计）

**最后更新**：2026-06-22

---

## 一、当前 Sitemap 概览

### 1.1 基本指标

| 指标 | 值 |
|------|-----|
| 总 URL 数 | **381** |
| 格式 | 单文件 XML（非 sitemap index） |
| 命名空间 | `http://www.sitemaps.org/schemas/sitemap/0.9` |
| `<lastmod>` | ✅ 全部覆盖 |
| `<changefreq>` | ❌ 未使用 |
| `<priority>` | ❌ 未使用 |
| 扩展类型（image/video/news） | ❌ 未使用 |
| `robots.txt` Sitemap 声明 | ✅ 已验证（`Sitemap: https://www.vofy.art/sitemap.xml`） |

### 1.2 URL 分布

| 分类 | 数量 | lastmod 范围 | 路径形态 / 备注 |
|------|------|-------------|----------------|
| **核心 / 营销页** | 25 | 2026-02-14 ~ 2026-06-18 | `/`、`/models`、`/models/rankings`、`/blog`（索引）、`/pricing`、`/privacy`、`/terms`、`/community`、`/canvas`、`/ai-tools`、`/ai-effects`、6× AI 能力 hub（`/ai-image-generate`、`/ai-image-editor`、`/ai-video-generate`、`/ai-video-motion-control`、`/ai-video-editor`、`/ai-video-extender`）、`/use-cases` + 6 行业子页、`/campaign/world-cup-2026` |
| **模型页** | 23 | 2025-08-26 ~ 2026-06-09 | **`/models/{slug}`**（扁平路径，如 `/models/sora-2`、`/models/kling-3.0`；**非** `/models/sora/2`） |
| **Blog** | 74 + 索引 | 2026-02-02 ~ 2026-06-18 | `/blog/{slug}`；索引页 `/blog` 计入上方「核心 / 营销页」 |
| **Apps** | 259 | hub：`2026-06-17`；工具：`2026-04-25` ~ `2026-06-17` | 5 个 hub（`/apps/image-editing`、`/apps/image-effects`、`/apps/image-filters`、`/apps/image-generators`、`/apps/image-styles`）+ **254** 个 `/apps/{slug}` 工具页 |

**不在 sitemap 但可访问的页面**：

| URL | 状态 | SEO 含义 |
|-----|------|---------|
| `/apps` | ✅ 200（robots Allow） | 旧版工具聚合索引；**未列入 sitemap**，主目录已迁移至 `/ai-tools`、`/ai-effects` |
| `/explore` | ❌ 404 | 旧导航项，已下线 |
| `/assets` | ❌ 404 | 旧导航项，已下线 |
| `/tools/*` | ❌ 404 | 旧路径形态，已全部迁移至 `/apps/{slug}` |

> **口径说明**：381 = 25 核心 + 23 模型 + 74 Blog 文章 + 259 Apps（5 hub + 254 工具）。Blog 索引 `/blog` 与 Apps 聚合 `/apps` 分别计入核心页计数与「不在 sitemap」清单，避免重复统计。

---

## 二、发现的问题

### 2.1 🔴 严重

**问题 1：Sora 2 模型页 lastmod 异常**
- URL：`/models/sora-2`（路径已扁平化，旧文档中的 `/models/sora/2` 已失效）
- lastmod：`2025-09-30`
- 早于站点上线时间（2026-03），且 Sora 2 可能已于 2026 年 4 月停运或降级
- **建议**：确认模型状态 → 若已停运，从 sitemap 移除该 URL 或标注不可用；若保留为历史模型信息页，更新 lastmod 为实际内容修改日期

**问题 2：Pricing 页疑似过期**
- URL：`/pricing`
- lastmod：`2026-03-20`（距今 3 个月）
- 定价信息一般随产品更新而变动
- **建议**：核实当前定价是否仍准确；若已更新，更新 lastmod

### 2.2 🟡 中

**问题 3：lastmod 准确性存疑 · 批量日期分化**
- **Apps 工具页（254 个）**：lastmod 分散在 15 个日期；其中 **81 个** 仍为 `2026-04-25`（占 32%），疑似批量生成日期而非真实修改时间
- **Apps hub（5 个）**：统一为 `2026-06-17`
- **Blog（74 篇）**：lastmod 覆盖 `2026-02-02` ~ `2026-06-18`，近期 Father's Day / World Cup 文章已更新，但部分早期 Nano Banana 2 系列可能已随模型更新而过时，lastmod 未反映实际内容变更
- **建议**：建立 lastmod 自动更新机制——内容修改时自动同步至 sitemap；避免使用批量统一日期

**问题 4：无 sitemap index 分拆**
- 381 个 URL 全在一个文件中（远低于 50,000 上限，暂无性能问题）
- 但缺少逻辑分组——不利于各模块独立监控
- **建议**：拆分为 sitemap index：
  ```
  /sitemap.xml          → 指向子 sitemap 的索引
  /pages-sitemap.xml    → 核心页 + 模型页（48 个）
  /blog-sitemap.xml     → Blog 文章（74 个）
  /apps-sitemap.xml     → Apps hub + 工具页（259 个）
  ```

**问题 5：目录页策略不一致 · `/apps` 缺失**
- Sitemap 含 **254** 个 `/apps/{slug}` 工具页 + 5 个 hub，但 **`/apps` 聚合索引不在 sitemap**
- 主目录已迁移至 `/ai-tools`、`/ai-effects`（均在 sitemap，lastmod `2026-06-17`）
- 站内仍可能从旧链接或外部引用访问 `/apps`（robots 已 Allow）
- **建议**：
  1. 明确 canonical：以 `/ai-tools`、`/ai-effects` 为主目录，或在 `/apps` 设置 301 → `/ai-tools`
  2. 若保留 `/apps` 为有效着陆页，将其加入 sitemap 并更新 lastmod
  3. 审计完整 Apps 清单，确保所有**公开可访问**的工具页都在 sitemap 中（当前 254 个，较旧文档 85 个已大幅扩容）

**问题 6：新增模块 lastmod 与内链覆盖**
- 新增 `/community`、`/canvas`、`/use-cases/*`、`/campaign/world-cup-2026` 等已在 sitemap
- 需确认这些页面与 Blog / Apps / Studio 之间的内链是否完整，避免「已索引但孤立」

### 2.3 🟢 低 / 后续优化

**问题 7：无 `<changefreq>` 和 `<priority>`**
- 这两个标签为可选，搜索引擎如今主要依赖 `lastmod` 和爬取频率
- 但加上可以辅助传达页面重要性
- **建议**（低优先级）：
  - 首页 `/`：priority=1.0, changefreq=daily
  - `/models`、`/ai-tools`、`/ai-effects`、`/blog`：priority=0.8, changefreq=weekly
  - 模型页：priority=0.7, changefreq=weekly
  - Apps 工具页：priority=0.6, changefreq=monthly
  - Blog 文章：priority=0.5, changefreq=monthly
  - Privacy/Terms：priority=0.3, changefreq=yearly

**问题 8：未使用扩展 sitemap 类型**
- Vofy 为图像/视频生成平台，blog 文章和模型页可能含有大量截图与演示视频
- **建议**（低优先级）：
  - 为核心模型页和 blog 文章中的关键图片添加 `<image:image>` 标签
  - 若模型页嵌入了演示视频，考虑添加 `<video:video>` 标签

**问题 9：`robots.txt` 引用 — ✅ 已验证**
- 2026-06-22 确认 `https://www.vofy.art/robots.txt` 包含 `Sitemap: https://www.vofy.art/sitemap.xml`
- 同时声明 `Host: https://www.vofy.art`；AI 爬虫（GPTBot、ClaudeBot 等）对 `/blog`、`/models`、`/apps`、`/use-cases`、`/campaign` 单独 Allow
- **无需进一步行动**；后续仅需在 robots 变更时复查

---

## 三、不应出现在 Sitemap 中的内容

### 3.1 当前正确排除

以下 URL 正确地**未出现**在 sitemap 中：

- `/studio/*` — 工作台，需登录，不可被索引（robots Disallow）
- `/api/*` — 后端接口
- `/c/*`、`/p/*`、`/share/*`、`/internal/*` — 内部或分享路径
- 带查询参数（`?mode=`, `?model=`）的 URL

### 3.2 已下线 / 404 路径（勿再引用）

以下旧路径**现网返回 404**，文档与内链应停止使用：

| 旧路径 | 现网状态 | 替代 |
|--------|---------|------|
| `/explore` | ❌ 404 | `/` 或 `/ai-tools` |
| `/assets` | ❌ 404 | 无直接替代 |
| `/tools/*` | ❌ 404 | `/apps/{slug}` |
| `/models/{vendor}/{version}` | ❌ 404 | `/models/{slug}`（如 `/models/sora-2`） |

> ⚠️ 旧文档将 `/explore` 标注为「可能需登录」已过时；2026-06-22 审计确认其为 404。

---

## 四、优化行动清单

### Phase 1（立即 · 本周）

| # | 行动 | 类型 |
|---|------|------|
| 1 | 确认 Sora 2 模型状态（`/models/sora-2`），若停运则从 sitemap 移除或标注不可用 | 修复 |
| 2 | 确认 Pricing 页内容是否最新，更新 lastmod | 修复 |
| 3 | ~~确认 `robots.txt` 中 sitemap 声明~~ | ✅ 已验证 |
| 4 | 明确 `/apps` vs `/ai-tools` canonical 策略，决定是否将 `/apps` 加入 sitemap 或 301 重定向 | 策略 |
| 5 | 将 sitemap 提交至 [Google Search Console](https://search.google.com/search-console) 并检查索引覆盖率报告 | 提交 |

### Phase 2（本月）

| # | 行动 | 类型 |
|---|------|------|
| 6 | 拆分 sitemap index：pages / blog / apps 三个子 sitemap | 优化 |
| 7 | 建立 lastmod 自动更新机制（内容 CMS/构建流程中集成） | 流程 |
| 8 | 审计 Apps 完整清单，确保所有公开工具都在 sitemap 中（当前 254，持续增长） | 覆盖 |
| 9 | 检查 Blog 索引页（`/blog`）是否所有 74 篇文章都可以从该页通过链接或分页到达 | 覆盖 |
| 10 | 为新增模块（`/use-cases/*`、`/community`、`/canvas`）建立内链 hub | 覆盖 |

### Phase 3（后续迭代）

| # | 行动 | 类型 |
|---|------|------|
| 11 | 按需添加 `<changefreq>` 和 `<priority>` | 增强 |
| 12 | 为核心模型页/Blog 关键图添加 `<image:image>` | 增强 |
| 13 | 建立月度 sitemap 审计流程：检查死链、lastmod 偏差、索引覆盖率 | 流程 |
| 14 | 若扩展中文站（`/zh/`），添加 hreflang sitemap 或 `xhtml:link` 标注 | 扩展 |

---

## 五、Sitemap Index 示例结构

实施 Phase 2 后，主 sitemap 应变为：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://www.vofy.art/pages-sitemap.xml</loc>
    <lastmod>2026-06-22</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.vofy.art/blog-sitemap.xml</loc>
    <lastmod>2026-06-22</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://www.vofy.art/apps-sitemap.xml</loc>
    <lastmod>2026-06-22</lastmod>
  </sitemap>
</sitemapindex>
```

各子 sitemap 内容范围：
- **pages-sitemap.xml**：25 个核心/营销页 + 23 个 `/models/{slug}` 模型页（共 48 个）
- **blog-sitemap.xml**：74 篇 `/blog/{slug}` 文章
- **apps-sitemap.xml**：5 个 Apps hub + 254 个 `/apps/{slug}` 工具页（共 259 个）

---

## 六、lastmod 更新策略

| 页面类型 | 触发条件 | lastmod 值 |
|---------|---------|-----------|
| 首页 `/` | 改版、What's New 更新 | 实际修改日期 |
| AI 能力 hub（`/ai-image-*`、`/ai-video-*`） | 功能描述、默认模型、示例变更 | 实际修改日期 |
| 工具目录（`/ai-tools`、`/ai-effects`） | 分类结构、Featured 工具变更 | 实际修改日期 |
| 模型页 `/models/{slug}` | 模型信息/描述/价格变更 | 实际修改日期 |
| Blog 文章 | **任何内容修改**（含事实勘误、模型名更新、步骤变更） | 实际修改日期 |
| Apps 工具页 | 功能描述、截图、Credits 消耗变更 | 实际修改日期 |
| Use Cases / Campaign | 案例、CTA、关联工具变更 | 实际修改日期 |
| Community / Canvas | 功能上线、展示内容变更 | 实际修改日期 |
| Pricing | 任何定价/套餐变更 | 实际修改日期 |
| Privacy/Terms | 条款文字变更 | 实际修改日期 |

> **注意**：避免所有同类型页面使用统一日期（如 81 个 Apps 仍为 `2026-04-25`）。Google 对批量统一 lastmod 可能降低信任。

---

## 七、监控与审计

### 7.1 定期检查

| 频率 | 检查项 |
|------|--------|
| 每次部署 | sitemap 生成是否成功、XML 格式是否正确、新增 URL 是否入库 |
| 每周 | GSC 索引覆盖率报告 → 是否有新的"已发现但未索引"或"抓取异常" |
| 每月 | lastmod 抽查（随机 10 个 URL，对比实际页面内容修改时间） |
| 每季 | 全量 URL 爬取 → 检查 404/301/302，从 sitemap 中移除异常 URL；复查 `/explore`、`/assets`、`/tools/*` 等旧路径是否仍 404 |

### 7.2 GSC 关键指标

- 索引覆盖率：目标 > 95% sitemap 中的 URL 被索引
- 抓取统计：关注抓取频率是否因 sitemap 更新而提升
- 站点地图报告：确认无格式错误
- 重点关注新增模块（Use Cases、Campaign、Community）的索引速度与孤立页比例

---

> *本计划基于 sitemap 2026-06-18 快照（2026-06-22 全量审计，381 URL）与 xml-sitemap skill 最佳实践编写。所有改动建议需与 Vofy 工程团队确认实施方式（CMS 自动生成 vs 构建时生成 vs 手动维护）。*
