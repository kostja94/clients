# 面包屑 Section 规范

本文档定义面包屑导航（BreadcrumbNav 组件）的配置规则与自动生成机制。

**来源**：`src/components/BreadcrumbNav.tsx`（部署仓源码）。

---

## 一、自动生成机制（覆盖 6 个类目）

**BreadcrumbNav 已实现全自动标签生成**，以下类目的页面无需手动配置 pathNameMap：

| 类目 | 数据源 | 自动注入方式 | 需要更新的文件 |
|------|--------|-------------|---------------|
| Tools（`/tools/` 和 `/blog/` tools 文章） | `tools-pages-config.ts` | `useMemo` + `...toolsPathLabels` | `tools-pages-config.ts` |
| Marketing（`/marketing/` 和 `/blog/` marketing 文章） | `marketing-pages-config.ts` | `useMemo` + `...marketingPathLabels` | `marketing-pages-config.ts` |
| SEO | `seo-pages-config.ts` | `for` 循环注入 | `seo-pages-config.ts` |
| Insights | `insights-pages-config.ts` | `for` 循环注入 | `insights-pages-config.ts` |
| Glossary | `glossary-pages-config.ts` | `for` 循环注入 | `glossary-pages-config.ts` |
| Blog | `blog-pages-config.ts` | `for` 循环注入 | `blog-pages-config.ts` |

**结论**：新增文章只需更新对应的 `*-config.ts` 文件，**BreadcrumbNav.tsx 无需任何手动修改**。

## 二、路由自动识别（Blog 路径智能分发）

BreadcrumbNav 能自动识别 Blog 路径下的文章类型，生成正确的面包屑层级：

| 文章类型 | 路由 | 面包屑层级 |
|----------|------|-----------|
| Tools 文章 | `/blog/{slug}` | 首页 → AI 工具 → 文章标题 |
| Marketing 文章 | `/blog/{slug}` | 首页 → 增长策略 → 文章标题 |
| 普通 Blog 文章 | `/blog/{slug}` | 首页 → 博客 → 文章标题 |

通过 `isBlogToolsArticle()` 和 `isBlogMarketingArticle()` 函数自动判断。

## 三、静态页面的 pathNameMap（需手动维护）

以下静态页面的 pathNameMap 仍需手动添加（`src/components/BreadcrumbNav.tsx` 第 63-90 行）：

| 路径 | 格式 |
|------|------|
| `/` | `t('nav.home')` |
| `/seo` | `getLabel` |
| `/marketing` | `getLabel` |
| `/tools` | `getLabel` |
| `/glossary` | `getLabel` |
| `/about` | `t()` |
| `/author/kostja` | `getLabel` |
| `/events` | `getLabel` |
| `/events/{slug}` | 每条单独 `getLabel` |
| `/insights` | `getLabel` |
| `/blog` | `getLabel` |
| 其他静态页 | `getLabel('中文', 'English')` |

**路径格式**：使用完整路径（如 `/tools/animation-library`），带前导斜杠。使用 `getLabel()` 提供中英文标签。

## 四、Fallback 机制

`pathNameMap` 未命中时的自动兜底：

- **英文**：`segment.split('-').map(capitalize).join(' ')`（如 `animation-library` → `Animation Library`）
- **中文**：直接使用原始 segment 名称

## 五、样式

- **定位**：`sticky z-40`，`top: var(--breadcrumb-top, 72px)`
- **字体**：`text-xs md:text-sm`
- **背景**：`bg-background/95 backdrop-blur-sm`
- **最大宽度**：最后一级 `max-w-[180px] md:max-w-none`，中间级 `max-w-[140px] md:max-w-none`
- **JSON-LD**：自动生成 `BreadcrumbList` Schema（`https://alignify.co` + 本地化路径）

## 六、检查清单

- [ ] 新增类目页面时，更新对应的 `*-pages-config.ts`
- [ ] 新增静态页面时，在 `pathNameMap` 中添加映射
- [ ] 使用 `getLabel()` 提供中英文标签
- [ ] 路径使用完整路径并带前导斜杠
- [ ] `npm run build` + 访问路由检查面包屑显示
