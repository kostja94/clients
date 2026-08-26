# Moras 任务单 — 构建品牌自定义 404 页面

> **状态**：已归档（2026-08-26）。不再作为现行文档维护。  
> **任务类型**：页面开发 + Technical SEO  
> **目标域名**：moras.ai  
> **优先级**：P1（HTTP 404 正确，但 UX/元数据/品牌一致性未达标；影响跳出率、内链恢复与 GSC 信号清晰度）  
> **提交**：2026-08-24

---

## 0. 重要性（为什么必须做）

### 0.1 规范要点（摘要）

缺失 URL 须返回 **404/410** 与品牌一致的导航壳；**禁止** HTTP 200 假成功、禁止无差别 redirect 到首页（soft 404）。自定义 404 可同时对用户友好且 SEO 正确——关键是 **404 状态码 + 独立 metadata**，而非 redirect。Next.js App Router 若在 Streaming 开始后调用 `notFound()`，可能退化为 200+noindex，须在 Suspense 前校验或使用 `global-not-found.js`。

完整依据见文末 [§7](#7-依据文档)。

### 0.2 对 Moras 的业务重要性

| 维度 | 现状问题 | 建好后的收益 |
|------|----------|--------------|
| **UX / 转化** | 默认 Next.js 404：无 Header/Footer、无恢复路径，用户易直接离开 | 保留导航 + 指向 TVG / Product research / Blog / App Store，降低死链跳出 |
| **SEO 信号** | 404 页 `<link rel="canonical" href="https://moras.ai"/>` 指向首页（见 §2 证据）——与「缺失 URL」语义冲突 | 404 专用 metadata；HTTP 404 保持不变；避免软 404 模式 |
| **品牌** | 黑白系统字体页与 moras.ai 营销站视觉脱节 | 与 SEO 页一致的 Moras / K2 Lab 品牌壳 |
| **运维** | Footer 链到 `/contact`（404）、sitemap 含 `/top-tiktok-shop-sellers`（404） | 404 页不能替代修链，但可缓冲用户；配合后续修 sitemap/内链 |
| **双应用** | 主应用（`/` SPA）+ SEO 子应用（Blog/TVG/Tools 等 ~50 页）各自需一致 404 体验 | 共享 `NotFoundPage` 组件，两仓库或 monorepo 同步 |

### 0.3 本任务边界

**包含**：品牌 404 UI、正确 HTTP 404、404 专用 metadata、主应用 + SEO 子应用落地、基础验收脚本。  
**不包含**（另开任务）：修复 `/contact`、Vision/Careers 占位链、`/top-tiktok-shop-sellers` 上线或移出 sitemap、西语 `/es/` 404 全文案（Phase 1 可先做英文壳 + `lang` 继承）。

---

## 1. 任务目标

将 moras.ai 上所有「路由不存在」的响应，从 **Next.js 默认 404** 升级为 **Moras 品牌自定义 404 页**，且同时满足：

1. **HTTP 状态码仍为 `404 Not Found`**（不得 200、不得 302/301 到 `/`）。
2. **页面包含与 SEO 页一致的 `Navbar` + `Footer`**，并提供 ≥4 条有效恢复链接（见 §5.3）。
3. **404 页 metadata 独立**：`title` 说明未找到；**不得**将 `canonical` / `og:url` 设为首页 `https://moras.ai`。
4. **主应用与 SEO 子应用**均部署同一套 Not Found 体验（组件可共享 package，按仓库实际调整）。
5. 部署后 `curl -I` 与 HTML 抽验通过 §6 验收清单。

---

## 2. 问题证据（2026-08-24 实测）

### 2.1 HTTP 状态（正确）

```http
GET https://moras.ai/this-page-does-not-exist-moras-test
HTTP/1.1 404 Not Found
x-powered-by: Next.js
```

同测 `/contact`、`/top-tiktok-shop-sellers` 均为 **404 Not Found**。

### 2.2 页面内容与 UI（未达标）

抓取 `https://moras.ai/this-page-does-not-exist-moras-test` 可见：

- 正文为 Next.js 默认：`404` + `This page could not be found.`（system-ui 居中，**无** Moras Navbar/Footer）。
- `<meta name="robots" content="noindex"/>`（Next.js 默认，可保留）。
- **Metadata 冲突（须修复）**：
  - `<title>404: This page could not be found.</title>`（内联）
  - 同时注入站点级：`<title>Moras - AI Commerce Producer for Viral Videos | K2 Lab</title>`
  - `<link rel="canonical" href="https://moras.ai"/>` ← **错误：404 URL 不应 canonical 到首页**
  - `<meta property="og:url" content="https://moras.ai"/>` ← 同上

### 2.3 与站点 IA 的交叉问题（404 页不能替代，但相关）

| URL | 状态 | 来源 |
|-----|------|------|
| `/contact` | 404 | [moras-site-structure.md §Footer](../moras-site-structure.md) — Footer Connect 区 |
| `/top-tiktok-shop-sellers` | 404 | sitemap 收录但未上线 |
| `/?lang=es` → `/es` | 404（i18n 未落地） | [moras-i18n-routing-migration.md](./moras-i18n-routing-migration.md) |

---

## 3. 根因分析

```
用户 / 爬虫请求不存在路径
    → Next.js App Router 命中内置 not-found 分支
    → 渲染默认 error UI（无项目组件）
    → 仍返回 HTTP 404 ✓
    → 但 root layout 的 generateMetadata 仍注入首页 canonical/og ✗
    → 用户看不到 Moras 导航，无法回到 TVG/Blog/下载 ✗
```

**因果链说明：**

1. 项目未实现自定义 `app/not-found.tsx`（或 SEO 子应用等价文件），故 fallback 到 Next 默认页 ([Next.js not-found 文档](https://nextjs.org/docs/app/api-reference/file-conventions/not-found))。
2. Layout 级 metadata 未对 `not-found` 分支做 override，导致 404 响应体携带**首页 canonical**——虽非 soft 404（HTTP 仍是 404），但向搜索引擎传递「缺失 URL 与首页等价」的错误信号。
3. [moras-page-composition-guide](./moras-page-composition-guide.md) 要求 SEO 页使用共享 `Navbar`/`Footer`，默认 404 违反该约定。
4. 双应用架构（[moras-i18n-routing-migration.md §0.5](./moras-i18n-routing-migration.md)）意味着 **主应用 + SEO 子应用** 可能各自独立部署，需分别确认 `not-found` 实现，避免仅修一侧。

**禁止采用的「捷径」（Google 明确反模式）：**

- 将所有 unknown path `redirect('/')` 或 middleware rewrite 到首页 → **soft 404**
- 404 页返回 HTTP 200 → **soft 404**
- 用 robots.txt 屏蔽 404 路径 → 阻碍 Google 确认 404

---

## 4. 影响范围

| 应用 | 受影响请求 | 说明 |
|------|------------|------|
| **主应用**（`/`、`/landing`） | 任意未定义路由 | 当前实测走主域默认 not-found |
| **SEO 子应用**（Blog、TVG、Tools、Use cases、Product、法务等） | rewrite 后仍不存在的 slug | 须与子应用路由共用 Not Found；**抽验 ≥2 URL** |
| **西语前缀** `/es/*` | 未本地化或不存在 slug | Phase 1：英文 404 壳 + 保留 `/es/` 前缀在链接中；文案西语可 Phase 2 |

**抽验建议（部署后）：**

- `https://moras.ai/fake-path-test`
- `https://moras.ai/blog/fake-slug-test`
- `https://moras.ai/tiktok-video-generator/fake-vertical`
- `https://moras.ai/contact`（真实 404，应有品牌页）

---

## 5. 修复要求

### 5.1 修复位置

在 **主应用** 与 **SEO 子应用** 仓库中分别定位（路径按实际 repo 调整）：

| 文件 | 用途 |
|------|------|
| `app/not-found.tsx` | 全站未匹配路由的 UI（Blog/TVG 等 SEO 页） |
| `app/global-not-found.js`（可选） | 若需跳过 layout 的完全自定义 404 HTML shell |
| `components/NotFoundPage.tsx`（新建，建议） | 共享品牌 404 block，供 not-found 引用 |
| `app/layout.tsx` 或 `generateMetadata` | 确保 **not-found 不继承首页 canonical** |
| `middleware.ts` | **禁止**添加 catch-all → `/`；i18n rewrite 失败应落到 not-found，非 302 首页 |

搜索关键词：`not-found`、`This page could not be found`、`next-error-h1`。

### 5.2 规则（必须满足）

**HTTP / SEO**

1. 响应 **HTTP 404**（`curl -I` 验证）；禁止 200/301/302 到 `/`。
2. **禁止** middleware / `next.config` 将 unknown paths 统一 redirect 到首页。
3. 404 页 **不要** 用 robots.txt 屏蔽；**不要** 仅依赖 noindex 替代 404 状态码。
4. `metadata` / `<title>`：`Page not found | Moras`（或等价）；**不输出** 指向 `https://moras.ai` 的 canonical（404 页建议 **omit canonical**，或 canonical 为当前请求 URL——二选一，**禁止**指首页）。
5. `og:url` 同理：omit 或使用当前 404 URL，**禁止**首页 URL。
6. 保留 Next.js 注入的 `robots: noindex` 可接受；核心是 **404 status**。

**UI / 品牌（对齐 [moras-page-composition-guide](./moras-page-composition-guide.md)）**

7. 复用现有 **`Navbar`**、**`Footer`**（与 `/blog`、`/tiktok-video-generator` 相同组件）。
8. 主内容区（`NotFoundContent`）须包含：
   - H1：`Page not found`（plain language，不责怪用户）
   - 1 句说明：链接可能失效或地址输错
   - **Primary CTA**：App Store Download（与 SEO 页 SecondaryCTA 策略一致，单 CTA）
   - **恢复链接网格**（至少 4 个，全部 HTTP 200）——见 §5.3
9. **不要** 全屏居中 system-ui 默认样式；使用站点 design token / Tailwind 与 SEO 页一致。
10. 404 页 **不需要** Breadcrumbs、FAQ、PageHero（非 SEO 着陆页）。
11. 内链 **必须** 来自 [moras-site-structure.md](../moras-site-structure.md) 已上线路径；**禁止** 链到 `/contact`、Vision、Careers 等已知 404。

**动态路由 / Streaming（Next.js）**

12. 对 `[slug]` 类页面：在 **任何 `Suspense` / streaming 之前** 做 slug 存在性检查并 `notFound()`；否则可能 200+noindex（软 404 风险）。见 [Next.js Streaming 指南](https://nextjs.org/docs/app/guides/streaming)。
13. 空搜索结果、空 CMS 列表页：若实质「无内容」，返回 **404 或 noindex**，勿返回 200 空壳（防 soft 404）。

**双应用 / i18n**

14. SEO 子应用部署后，rewrite 链路上的 404 须与子应用 `not-found` 一致，而非主应用默认页。
15. 若请求路径以 `/es/` 开头，Navbar/Footer 链接须保留 locale 前缀（与 [moras-i18n-routing-migration.md](./moras-i18n-routing-migration.md) 一致）；404 文案 Phase 1 可英文。

### 5.3 恢复链接清单（404 页「Where to go next」）

以下链接 **2026-07-14 IA 文档记载为已上线**；实现前须再 HEAD 200：

| 标签 | URL | 理由 |
|------|-----|------|
| TikTok video generator | `/tiktok-video-generator` | 核心产品 SEO 枢纽 |
| Product research | `/product-research` | 选品工具入口 |
| Use cases | `/use-cases` | 人群 hub |
| Blog | `/blog` | 内容 hub |
| Pricing | `/pricing` | 转化 |
| Home | `/` | 最后选项，非 redirect |

可选增强（Recommended，非阻塞发布）：

- 站内搜索：若 Blog 已有搜索组件，嵌入简化版；**无搜索则不做假搜索框**。
- 「Popular guides」3 卡：链到高流量 blog slug（如 `/blog/how-to-make-money-on-tiktok`），slug 须存在。

### 5.4 修复后的期望输出

**HTTP 头（示例）**

```http
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=utf-8
```

**HTML 结构（语义示意）**

```tsx
// components/NotFoundPage.tsx — 按项目实际 import 调整
export function NotFoundPage() {
  return (
    <>
      <Navbar />
      <main id="main-content">
        <h1>Page not found</h1>
        <p>
          We couldn&apos;t find that page. The link may be outdated, or the URL may be mistyped.
        </p>
        <PrimaryCta href="https://apps.apple.com/us/app/moras-create-earn-with-ai/id6755306262">
          Download Moras
        </PrimaryCta>
        <nav aria-label="Helpful links">
          <Link href="/tiktok-video-generator">TikTok video generator</Link>
          <Link href="/product-research">Product research</Link>
          <Link href="/use-cases">Use cases</Link>
          <Link href="/blog">Blog</Link>
          <Link href="/pricing">Pricing</Link>
          <Link href="/">Home</Link>
        </nav>
      </main>
      <Footer />
    </>
  );
}
```

**Metadata（`app/not-found.tsx` 内 export，示意）**

```tsx
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Page not found | Moras",
  description: "This page doesn't exist on moras.ai. Explore our TikTok Shop tools and guides.",
  robots: { index: false, follow: true },
  // 刻意 omit alternates.canonical — 勿指向 https://moras.ai
  openGraph: {
    title: "Page not found | Moras",
    siteName: "Moras",
    // omit url 或不用首页 URL
  },
};
```

**`app/not-found.tsx`（示意）**

```tsx
import { NotFoundPage } from "@/components/NotFoundPage";

export { metadata } from "./not-found.metadata"; // 或内联 export metadata

export default function NotFound() {
  return <NotFoundPage />;
}
```

### 5.5 404 vs 301 决策（供后续内容运维，非本 PR 必须）

| 场景 | 动作 |
|------|------|
| 内容永久删除、无等价页 | 保持 **404**（如 `/top-tiktok-shop-sellers` 在未建页前） |
| 内容搬到新 URL | **301 到新 URL**（一对一） |
| 有外链/流量的旧 URL | 301 到**最相关**现存页，不是首页 |
| Footer `/contact` | **建页或改链**（另任务）；404 页不要链到 contact |

### 5.6 代码级参考（双应用）

```
moras-web/                    # 主应用
  app/not-found.tsx
  components/NotFoundPage.tsx

moras-seo/                    # SEO 子应用（名称以实际为准）
  app/not-found.tsx           # import 共享 NotFoundPage 或 duplicate
  app/[locale]/...            # slug 页：getPost(slug) 失败 → notFound() 在 Suspense 前
```

若两仓库无法共享 package，**复制 `NotFoundPage` 并注明同步点**，避免一侧仍用默认 404。

---

## 6. 验收标准

### 6.1 HTTP 与 SEO

- [ ] `curl.exe -I https://moras.ai/{random-test-path}` → **`404 Not Found`**
- [ ] `curl.exe -I https://moras.ai/blog/{random-test-slug}` → **`404 Not Found`**（SEO 子应用）
- [ ] 404 HTML **不包含** `<link rel="canonical" href="https://moras.ai"/>`（除非 canonical 为当前 404 URL——推荐 omit）
- [ ] 404 HTML **不包含** `og:url` 指向 `https://moras.ai`  alone 作为首页替代
- [ ] GSC URL Inspection（抽 1 条假 URL）：HTTP 404；Rendered 页为 Moras 品牌 UI（部署后人工验）

### 6.2 UI / 品牌

- [ ] 页面含 **Navbar + Footer**（与 `/blog` 同源组件）
- [ ] 含 H1 `Page not found`（或等价 plain copy）
- [ ] 含 **App Store** 主 CTA（单 CTA）
- [ ] 恢复链接 ≥4 且均可 200（TVG、Product research、Use cases、Blog 等）
- [ ] **无** 指向 `/contact`、Vision、Careers 的链接
- [ ] 移动端布局正常（Navbar 可折叠）

### 6.3 反模式回归

- [ ] **无** unknown path → `/` 的 301/302/307
- [ ] **无** 404 页 HTTP 200
- [ ] 动态 slug 不存在时：非 Streaming 场景下 HTTP 404（抽 1 个 TVG 假 slug）

### 6.4 文档与后续（Recommended）

- [ ] 在工程 README 或内部 docs 记录：`not-found` 与 `NotFoundPage` 位置
- [ ] 创建 follow-up：从 sitemap 移除 `/top-tiktok-shop-sellers` 或上线该页；修复 Footer `/contact`

---

## 7. 依据文档

- **内部**：[moras-site-structure.md](../moras-site-structure.md) · [moras-page-composition-guide.md](./moras-page-composition-guide.md) · [moras-i18n-routing-migration.md](./moras-i18n-routing-migration.md) · [404 调研](../../temp/404-page-web-search-2026-08-24.md)
- **外部**：[Google 404 / soft 404](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors) · [GSC 404 帮助](https://support.google.com/webmasters/answer/2445990) · [Next.js not-found / Streaming](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)

---

*本任务单由外部 SEO/内容协作方提交，供 Moras 工程 Agent 直接执行。*  
*已归档至 `_archive/`。现行站点 IA：[moras-site-structure.md](../moras-site-structure.md)。*
