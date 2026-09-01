# Today AI 任务单 — 将 article 子域 SEO 页面反向代理至主域 today.ai

> **任务类型**：域名架构 / 反向代理 / Technical SEO  
> **目标域名**：today.ai（主域）、article.today.ai（内容源站，不对外暴露为规范 URL）  
> **状态**：待处理 · **优先级**：P0 · **提交**：2026-08-25

---

## 1. 背景

Healthcare / Finance / Blog 这批 SEO 页**本应部署在 `today.ai` 主域**，因沟通偏差建在了 **`article.today.ai` 子域**。主域从未构建这些页面（同路径 404 是预期状态），内容目前只在子域上线。

子域对 Google 是[独立站点](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)，canonical / sitemap 均指向 `article.today.ai`，**权重无法归入主域**；且 `article.today.ai/` 与 `today.ai/landing` 存在内容重复风险。

---

## 2. 影响

- **搜索权重**：Healthcare / Finance / Blog 长尾流量信号留在子域，主域 today.ai 无法承接（[Consolidate duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)）
- **URL 不统一**：分享、广告、内链应以 `today.ai` 为准，但目前落地页在子域
- **索引分裂**：须通过反向代理 + canonical / sitemap 让搜索引擎以 today.ai 为规范 URL

---

## 3. 迁移范围

### 3.1 必须迁移（16 条 URL）

| 分组 | 英文路径 | 中文路径 |
|------|---------|---------|
| Healthcare hub | `/healthcare` | `/zh-Hans/healthcare` |
| Healthcare spoke | `/healthcare/fitness-coach` | `/zh-Hans/healthcare/fitness-coach` |
| Healthcare spoke | `/healthcare/meal-planner` | `/zh-Hans/healthcare/meal-planner` |
| Healthcare spoke | `/healthcare/sleep-tracker` | `/zh-Hans/healthcare/sleep-tracker` |
| Finance | `/finance` | `/zh-Hans/finance` |
| Blog 列表 | `/blog` | `/zh-Hans/blog` |
| Blog 文章 | `/blog/what-is-today` | `/zh-Hans/blog/what-is-today` |
| Blog 文章 | `/blog/meet-today` | `/zh-Hans/blog/meet-today` |

### 3.2 不在本次范围

| 路径 | 说明 |
|------|------|
| `today.ai/`、`/landing`、`/downloads`、`/waitlist`、`/login`、`/privacy`、`/terms` | 不动 |
| `article.today.ai/` | 根域首页，后续单独处理 |
| `article.today.ai/ai-personal-assistant` 等未列页面 | 后续单独规划 |

---

## 4. 架构说明

**today.ai 反向代理**：用户只访问 `today.ai/healthcare`，today.ai 在服务端向 article 项目拉取 HTML 并返回。article 子域是**内容源（origin）**，对外规范 URL 只能是 today.ai。

防 duplicate 靠以下组合（[Google canonical 指南](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)）：

| 手段 | 作用 |
|------|------|
| today.ai rewrites 反向代理 | 对外唯一入口，返回 200 |
| canonical / og:url → `today.ai` | 声明规范 URL |
| today.ai sitemap 加入、article sitemap 移除迁移 URL | 引导爬虫索引主域 |
| article robots `Disallow` 迁移路径 | 辅助隐藏子域（不能替代 canonical） |
| 全站内链只指向 `today.ai` | 不再对外推广 article URL |

### 任务目标

1. `https://today.ai{path}` → **200**（反向代理）
2. canonical、`og:url`、hreflang、sitemap 全部指向 **today.ai**
3. article 子域不再作为规范 URL 出现
4. 现有主站页面行为不变

---

## 5. 修复要求

### 5.1 修复位置

| 项目 | 找什么 |
|------|--------|
| **today.ai**（Next.js） | `vercel.json`、`next.config.ts` 的 `rewrites`；或 middleware 反向代理 |
| **article.today.ai** | `SITE_URL` / canonical 生成逻辑；sitemap 生成器；`robots.txt` |
| **共用** | 环境变量 `CANONICAL_ORIGIN` / `NEXT_PUBLIC_SITE_URL` |

### 5.2 规则

#### A. today.ai — 反向代理

1. §3.1 全部 16 条路径返回 **200**
2. 实现二选一：
   - **方案 1**：`rewrites` 转发至 article 同源路径
   - **方案 2**：路由代码合并进 today.ai 项目（长期更优，工作量更大）
3. 不得覆盖 §3.2 现有路由（已有路由匹配优先于 rewrite）
4. 静态资源（`/_next/`、字体、图片）须正常加载；若 proxy 导致 404，补 rewrite 或改方案 2
5. 通过 `X-Forwarded-Host` 等头让源站知道公开域名为 `today.ai`

#### B. article.today.ai — 源站配置

1. 迁移路径 HTML 的 canonical / og:url 输出 `https://today.ai{path}`
2. `article.today.ai/sitemap.xml` **移除** §3.1 全部 URL
3. `article.today.ai/robots.txt` 对迁移路径加 `Disallow`（辅助）：

```
Disallow: /healthcare
Disallow: /finance
Disallow: /blog
Disallow: /zh-Hans/healthcare
Disallow: /zh-Hans/finance
Disallow: /zh-Hans/blog
```

4. 全站不再对外链接 article 迁移路径

#### C. SEO 元数据

1. canonical = `https://today.ai{path}`
2. `og:url` 与 canonical 一致
3. hreflang 互指改为主域：

```html
<link rel="alternate" hreflang="en" href="https://today.ai/healthcare" />
<link rel="alternate" hreflang="zh-Hans" href="https://today.ai/zh-Hans/healthcare" />
<link rel="alternate" hreflang="x-default" href="https://today.ai/healthcare" />
```

4. `today.ai/sitemap.xml` 含 §3.1 全部 URL
5. `today.ai/robots.txt` 声明 `Sitemap: https://today.ai/sitemap.xml`

#### D. 内链

- 页面内相对链接在 today.ai 上须正常解析
- 硬编码的 `article.today.ai` 绝对 URL 改为相对路径或 `today.ai`

### 5.3 期望输出

```
GET https://today.ai/healthcare              → 200（反向代理内容）
GET https://today.ai/zh-Hans/healthcare      → 200
GET https://today.ai/                        → 200（waitlist，不变）
GET https://today.ai/landing                 → 200（不变）
```

**canonical（以 `/healthcare` 为例）：**

```html
<link rel="canonical" href="https://today.ai/healthcare"/>
<meta property="og:url" content="https://today.ai/healthcare"/>
```

**sitemap 条目（节选）：**

```xml
<url>
  <loc>https://today.ai/healthcare</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://today.ai/healthcare" />
  <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://today.ai/zh-Hans/healthcare" />
  <xhtml:link rel="alternate" hreflang="x-default" href="https://today.ai/healthcare" />
</url>
```

### 5.4 代码参考（按项目实际调整）

**today.ai — vercel.json rewrites**

```json
{
  "rewrites": [
    { "source": "/healthcare/:path*", "destination": "https://article.today.ai/healthcare/:path*" },
    { "source": "/finance", "destination": "https://article.today.ai/finance" },
    { "source": "/blog/:path*", "destination": "https://article.today.ai/blog/:path*" },
    { "source": "/zh-Hans/healthcare/:path*", "destination": "https://article.today.ai/zh-Hans/healthcare/:path*" },
    { "source": "/zh-Hans/finance", "destination": "https://article.today.ai/zh-Hans/finance" },
    { "source": "/zh-Hans/blog/:path*", "destination": "https://article.today.ai/zh-Hans/blog/:path*" }
  ]
}
```

> 仅 rewrite 不够：源站须输出 `canonical` = `today.ai`。参考 [reverse proxy 须改写 canonical/meta 为主域](https://stringerseo.co.uk/technical/how-to-modify-all-wordpress-links-for-a-reverse-proxy-setup/)。

**canonical 根域（article 源站）**

```typescript
const CANONICAL_ORIGIN = process.env.CANONICAL_ORIGIN ?? 'https://today.ai';

export function canonicalUrl(path: string) {
  return `${CANONICAL_ORIGIN}${path}`;
}
```

---

## 6. 验收标准

- [ ] §3.1 全部 16 条 URL：`today.ai` → **200**，内容与 article 版一致
- [ ] 抽验 `/healthcare`、`/finance`、`/blog/what-is-today`：canonical 与 og:url 为 `https://today.ai/...`
- [ ] `today.ai/sitemap.xml` 含全部迁移 URL；**article sitemap 不含**迁移 URL
- [ ] article 迁移路径 robots Disallow 已配置
- [ ] `today.ai/`、`/landing`、`/downloads`、`/waitlist` 无回归
- [ ] 页面内链在 today.ai 上无 404

---

## 7. 部署后建议

1. **GSC**：在 today.ai 属性提交 sitemap；用「网址检查」确认 canonical 为 today.ai
2. **索引观察**：canonical 收敛通常需数周，持续观察 GSC 规范 URL 是否变为 today.ai
3. **article 根域**：`article.today.ai/` 与 `today.ai/landing` 重复问题留待后续
4. **回归**：确认 today.ai proxy 200 + canonical 正确

---

*本任务单由外部 SEO 协作方提交，供 Today AI 方 agent 直接执行。*
