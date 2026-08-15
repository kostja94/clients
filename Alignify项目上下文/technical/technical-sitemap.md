# Sitemap 生成说明与优化方案

本文档说明 Alignify 站点的 Sitemap 生成实现，并基于业界最佳实践提供优化方案。

**实现位置**：`app/sitemap.ts`

**参考**：[Next.js Sitemap](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)、[sitemaps.org 协议](https://www.sitemaps.org/protocol.html)、[Google Search Console](https://support.google.com/webmasters/answer/12817956)

---

## 一、架构说明

### 1.1 单一 Sitemap 结构（优化后）

站点规模远低于 sitemaps.org 单文件限制（≤50,000 URL、≤50MB），采用**单一 Sitemap 文件**更简洁、易维护：

| 输出 | 说明 |
|------|------|
| `/sitemap.xml` | 全站所有可索引页面，由 Next.js 根据 `app/sitemap.ts` 的 default export 生成 |

**何时使用 Sitemap Index**：仅当 URL 总量超过 50,000 时，才需使用 `generateSitemaps` 拆分子 Sitemap。

### 1.2 robots.txt 引用

`public/robots.txt` 已配置：

```
Sitemap: https://alignify.co/sitemap.xml
```

---

## 二、业界最佳实践总结

### 2.1 sitemaps.org 协议要点

| 项目 | 规范 |
|------|------|
| **单 Sitemap 限制** | ≤50,000 URL，≤50MB（未压缩） |
| **Sitemap Index** | 超过限制时使用，索引文件可引用多个子 Sitemap |
| **编码** | UTF-8 |
| **URL 格式** | 同一 host，含协议（https） |
| **必选标签** | `<loc>` |
| **可选标签** | `<lastmod>`、`<changefreq>`、`<priority>` |

### 2.2 Google / Bing 与 lastmod 建议

- **lastmod 必须准确**：应为**页面实际修改时间**，而非 sitemap 生成时间。Google 要求与真实修改可验证一致；Bing 统计约 18% 的 sitemap 使用错误 lastmod（如全部相同），可能被忽略。
- **格式**：W3C Datetime（`YYYY-MM-DD` 或 `YYYY-MM-DDTHH:MM:SS+TZD`）
- **适用场景**：内容有明显更新、结构化数据变更、链接变更时更新

### 2.3 changefreq 与 priority

- **changefreq**：仅为提示，不影响爬取频率。建议按实际更新频率设置（`daily`/`weekly`/`monthly`）
- **priority**：0.0–1.0，表示相对重要性，**不影响排名**。重要页面（首页、核心服务）可设高值；避免全部相同

### 2.4 排除内容

- 在 robots.txt 或 X-Robots-Tag 中排除：`/_next/*`、`/api/*`、静态资源等
- Sitemap 仅包含希望被索引的页面

---

## 三、当前实现与问题

### 3.1 数据来源

| 问题 | 描述 | 状态 |
|------|------|------|
| **硬编码维护** | 工具页 URL 在 sitemap 内手写，与 `TOOLS_PAGES` 重复 | ✅ 已优化：工具页从 `TOOLS_PAGES` 生成 |
| **三处维护** | sitemap、IndexNow 脚本、Feed 各维护一份，易遗漏 | ✅ 已优化：IndexNow 从 `site-pages-config` 导入 |
| **中英文不一致** | 如英文工具页缺少 `code-review`，中文有 | 已消除：工具页统一源自 `TOOLS_PAGES` |

### 3.2 lastmod 问题

| 问题 | 影响 |
|------|------|
| **大量使用 `new Date()`** | 每次生成 sitemap 都是“当前时间”，不符合 lastmod 语义 |
| **搜索引擎可能忽略** | 错误 lastmod 可能降低搜索引擎对 sitemap 的信任 |

### 3.3 其他

- 部分页面（如 `html-a-tag`、`google-tag-manager`、`indie-hackers`、`author`）已使用固定 `lastModified` 日期

---

## 四、优化方案

### 4.1 单一数据源（P0）✅

**目标**：工具页从 `TOOLS_PAGES` 自动生成，消除重复维护。

**实现**：`app/sitemap.ts` 通过 `buildToolsSitemapEntries(prefix)` 从 `TOOLS_PAGES` 生成工具页 URL。

**效果**：新增工具页只需在 `TOOLS_PAGES` 中添加，sitemap 与 AlsoInterestedIn 自动同步。

### 4.2 lastmod 优化（P1）

**目标**：lastmod 使用页面实际修改时间。

**方案 A（推荐）**：在 `site-pages-config` 或类似配置中为每页维护 `modifiedDate`，生成 sitemap 时读取。Tools 页面可在 pageConfig 中已有 `modifiedDate`，需统一导出供 sitemap 使用。

**

**格式**：`YYYY-MM-DD` 或 `YYYY-MM-DDTHH:MM:SS+08:00`（东八区）。

### 4.3 统一配置与 IndexNow（P2）🔶 部分完成

**目标**：sitemap 与 IndexNow 共用同一 URL 列表。

- 已新建 `src/data/site-pages-config.ts`，导出 `getAllPageUrls(baseUrl)`
- `scripts/permanent/submit-all-pages-to-indexnow.ts` 从 `site-pages-config` 导入 URL
- 工具页来自 `TOOLS_PAGES`，其他页面由 `ZH_OTHER_PATHS`、`EN_OTHER_PATHS` 定义

### 4.4 其他页面配置化（P3）

将 SEO、Marketing、Glossary、Insights、Events 等页面也从配置数组生成，进一步减少硬编码。

---

## 五、实施步骤建议

| 步骤 | 任务 | 优先级 | 状态 |
|------|------|--------|------|
| 1 | sitemap 工具页从 `TOOLS_PAGES` 生成 | P0 | ✅ |
| 2 | 新建 `site-pages-config`，IndexNow 从 config 导入 | P1 | ✅ |
| 3 | 合并为单一 sitemap 文件（站点规模 < 50k URL） | P1 | ✅ |
| 4 | 为 Tools 页面建立 modifiedDate 映射，sitemap 使用真实 lastmod | P2 | 待实施 |
| 5 | 其他页面配置化 | P3 | 待实施 |

---

## 六、字段说明

| 字段 | 说明 | 建议 |
|------|------|------|
| url | 完整 URL | 含 `https://alignify.co` |
| lastModified | 页面最后修改时间 | 使用页面 metadata，格式 ISO 8601 |
| changeFrequency | 更新频率提示 | 首页 `daily`，工具页 `weekly`，指南页 `monthly` |
| priority | 相对重要性 | 首页 1.0，聚合页 0.9，工具页 0.8，其他 0.5–0.6 |

---

## 七、Middleware 排除

`sitemap` 相关路径已在 `middleware.ts` 中排除，避免被 i18n 重定向：

```ts
'/((?!api|_next|_vercel|sitemap|sitemap-index|.*\\..*).*)'
```

---

## 八、新页面添加流程

**Tools 页面**：在 `TOOLS_PAGES` 中添加 slug 和 keyword，sitemap 与 IndexNow 自动更新。

**其他页面**：在 `site-pages-config` 的 `ZH_OTHER_PATHS` 或 `EN_OTHER_PATHS` 中添加路径，IndexNow 自动更新；同时需在 `app/sitemap.ts` 的 `getChineseOtherEntries()` 或 `getEnglishOtherEntries()` 中添加对应 URL 及 metadata。

**未来优化**：将「其他页面」也从 `site-pages-config` 驱动生成，实现单一数据源。

---

## 九、常见问题

1. **sitemap 404**：确认 Next.js 构建成功，`app/sitemap.ts` 的 default export 返回有效数组
2. **页面缺失**：检查是否在 `TOOLS_PAGES` 或 `get*OtherEntries` 中添加
3. **lastmod 不准确**：避免使用 `new Date()`，尽量使用页面实际 `modifiedDate`
4. **Google 不索引**：在 Search Console 提交 `https://alignify.co/sitemap.xml`，并检查 Coverage 报告
5. **何时改用 Sitemap Index**：若 URL 总量超过 50,000，需使用 `generateSitemaps` 拆分子 Sitemap


---

## 十、待办：完全统一数据源

以下工作源自原 technical-optimization-plan.md，大部分 P0/P1 已完成，剩余项汇总于此。

### 待实施

| 步骤 | 任务 | 优先级 |
|------|------|--------|
| 1 | sitemap 非工具页从 site-pages-config 统一导入 | P2 |
| 2 | 修复 sitemap 缺失 /seo/glossary（IndexNow 脚本已包含） | P2 |
| 3 | 为 Tools 页面建立 modifiedDate 映射，sitemap 使用真实 lastmod | P2 |
| 4 | Feed 文章列表从 BlogIndex/Explore 统一数据源 | P3 |
| 5 | 其他页面从配置数组生成 sitemap 条目 | P3 |

### 已实施

- ✅ sitemap 工具页从 TOOLS_PAGES 生成（P0）
- ✅ 新建 site-pages-config.ts（P1）
- ✅ IndexNow 从 site-pages-config 导入 URL（P1）
- ✅ 合并为单一 sitemap 文件（P1）
