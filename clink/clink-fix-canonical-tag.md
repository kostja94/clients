# Clink 任务单 — 全站补充 Canonical Tag 与 og:url

> **任务类型**：Technical SEO（页面级 URL 规范化）
> **目标域名**：clinkbill.com
> **状态**：待处理
> **优先级**：P1（全站可索引页面缺少 canonical 信号；Blog 亦缺 og:url，影响索引选择与社交预览）
> **提交**：2026-08-26
> **关联任务**：[clink-fix-canonical-host.md](./clink-fix-canonical-host.md)（www / 裸域 301，独立问题；canonical href 须与最终首选 host 一致）

---

## 问题概述

### 问题是什么

Clink **主站仓库**与 **Blog 仓库**的可索引页面在 HTML `<head>` 中 **均未输出 `<link rel="canonical">`**；Blog 文章页亦 **缺少 `og:url`**。Google 与社交平台无法从页面源码读取「此页面的官方 URL」，只能依赖重定向、sitemap 或自行推断。

这与 www / 裸域是否 301 是 **两个独立问题**：即使 host 已统一，缺少 canonical 仍会导致尾斜杠、带参 URL、分页等变体难以合并。

### 会造成什么影响

1. **Google 自行选择 canonical，与预期不符**  
   无明确 canonical 时，Google 可能将带 query string、尾斜杠变体或内链较多的副本选为 canonical，与 sitemap / 运营口径不一致。

2. **同 host 内的 URL 变体无法合并**  
   例如 `/blog/foo` vs `/blog/foo/`、带 UTM 的分享链接，在无 canonical 时均可能被当作独立 URL 消耗抓取预算。

3. **社交分享预览 URL 不确定**  
   Blog 缺少 `og:url` 时，Facebook / LinkedIn / Slack 等可能从分享链接或页面内其他信号推断 URL，预览与索引 URL 可能分叉。

4. **GSC「Google 选择的 canonical」报表噪音**  
   大量页面无自指 canonical，GSC 会显示「用户声明：无 / Google 选择：xxx」，难以批量审计哪些页面规范化失败。

5. **与结构化数据 / 内链的协同缺失**  
   面包屑 JSON-LD、内链 absolute URL 需要与 canonical 指向同一 URL；缺 canonical 时，各信号源各自为政，富结果与索引稳定性下降。

---

## 1. 任务目标

在 **主站仓库 + Blog 仓库** 为所有可索引页面输出：

1. **自指**的 `<link rel="canonical" href="...">`（绝对 URL，含正确 path，不含 fragment）；
2. Blog 及需社交分享的页面同步输出 **`og:url`**，值与 canonical 完全一致；
3. canonical / og:url 中的 host 与全站 **首选 host** 一致（与 [clink-fix-canonical-host.md](./clink-fix-canonical-host.md) 结论对齐，默认 `https://www.clinkbill.com`）。

修复后任意抽查页面，Rich Results Test / 查看源码均可验证 canonical 存在且正确。

---

## 2. 问题证据（2026-08-26 实测）

对以下 URL 抓取 HTML 源码，检索 `rel="canonical"`、`property="og:url"`：

| URL | `<link rel="canonical">` | `og:url` |
|-----|--------------------------|----------|
| `https://www.clinkbill.com/` | ❌ 无 | ❌ 无 |
| `https://clinkbill.com/` | ❌ 无 | ❌ 无 |
| `https://www.clinkbill.com/products/billing` | ❌ 无 | ❌ 无 |
| `https://clinkbill.com/products/billing` | ❌ 无 | ❌ 无 |
| `https://www.clinkbill.com/blog/monthly-recurring-revenue` | ❌ 无 | ❌ 无 |
| `https://clinkbill.com/blog/monthly-recurring-revenue` | ❌ 无 | ❌ 无 |

Blog 文章页 **有** `og:title`、`og:description`，但 **无** `og:url`：

```html
<meta property="og:title" content="What Is MRR? — Monthly Recurring Revenue, Explained — Clink"/>
<meta property="og:description" content="MRR is the predictable monthly revenue..."/>
<!-- og:url 缺失 -->
```

主站首页仅有基础 meta，无 canonical / Open Graph URL：

```html
<title>Clink | Subscription &amp; Billing Solutions</title>
<meta name="description" content="Clink | Subscription &amp; Billing Solutions | One-Stop Integration with Stripe, Adyen, Checkout, Nuvei &amp; More" data-next-head=""/>
<!-- rel="canonical" 缺失 -->
```

---

## 3. 根因分析

1. **Next.js metadata 未配置 `alternates.canonical`**  
   主站与 Blog 均未在 root layout 或 `generateMetadata` 中设置 canonical；Pages Router 项目亦未在 `_document` / `<Head>` 注入。

2. **Blog Open Graph 配置不完整**  
   Blog 仓库设置了 `og:title` / `og:description`，但未设置 `openGraph.url`（或等效 `<meta property="og:url">`）。

3. **缺少全局 SITE_URL 驱动的 metadata 层**  
   无统一函数根据 `pathname` + `SITE_URL` 生成 canonical，导致全站遗漏；与 host 统一任务解耦后，仍须在代码层显式输出 tag。

Google [规范化 URL 文档](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) 将 `rel="canonical"` 列为首选信号之一；缺失时 Google 使用其他启发式规则，结果不可控。

因果链：**无 canonical 输出** + **Blog 无 og:url** → 同页多 URL 变体无法合并 → GSC canonical 报表异常 → 社交预览 URL 不确定。

---

## 4. 影响范围

| 范围 | 说明 |
|------|------|
| **主站仓库 — 全部可索引页** | `/`、`/products/*`、`/agentic-payment`、`/skills`、`/contact`、`/privacy`、`/terms` 及 i18n 变体（若可索引） |
| **Blog 仓库 — 全部可索引页** | `/blog` 列表页、`/blog/{slug}` 全部文章 |
| **不在范围** | 明确 `noindex` 的页面、纯 redirect 中间页、404/500 错误页 |

已抽验页面：`/`、`/products/billing`、`/blog/monthly-recurring-revenue` — **均无 canonical**。

---

## 5. 修复要求

### 5.1 修复位置

**主站仓库**

- App Router：`app/layout.tsx` 或各 route 的 `generateMetadata`
- Pages Router（若适用）：`pages/_app.tsx` / `pages/_document.tsx` / 各 page 的 `<Head>`
- 搜索关键词：`metadata`、`alternates`、`canonical`、`next/head`

**Blog 仓库**

- `app/blog/[slug]/page.tsx`（或等效动态路由）的 `generateMetadata`
- `/blog` 列表页 layout / page metadata
- 确保 `openGraph.url` 与 `alternates.canonical` 同源

**共享约定**

- 读取环境变量 `NEXT_PUBLIC_SITE_URL`（与 host 统一任务对齐，默认 `https://www.clinkbill.com`）
- 禁止手写每页不同的 host；禁止输出相对路径 canonical（必须为绝对 URL）

### 5.2 规则（必须满足）

1. **绝对 URL**：`href` 必须为 `https://{首选host}{path}`，禁止 `/blog/foo` 相对形式。
2. **自指**：canonical 指向 **当前页面的首选 URL**（非首页、非其他 slug）。
3. **与 og:url 一致**：Blog 及所有含 Open Graph 的页面，`og:url` === canonical `href`。
4. **不含 fragment**：canonical 不带 `#section`；query string 默认 **不包含**（除非该页 canonical 设计上带参，Clink 博客/营销页应使用无参 canonical）。
5. **尾斜杠策略统一**：全站择一（建议 **无尾斜杠**，与 sitemap 一致），canonical 与 sitemap `<loc>` 格式相同。
6. **全局生效**：修复 layout / metadata 生成器一处，覆盖同仓库所有模板页；特殊页（如分页 `/blog?page=2`）若可索引须单独定义 canonical，否则对分页使用 `noindex` 或 canonical 到 `/blog`。
7. **不改动 UI**：仅补 `<head>` metadata，不改变可见面包屑或页面内容。

### 5.3 修复后的期望输出

**Blog 文章页 `/blog/monthly-recurring-revenue`**

```html
<link rel="canonical" href="https://www.clinkbill.com/blog/monthly-recurring-revenue" />
<meta property="og:url" content="https://www.clinkbill.com/blog/monthly-recurring-revenue" />
<meta property="og:title" content="What Is MRR? — Monthly Recurring Revenue, Explained — Clink" />
<meta property="og:description" content="MRR is the predictable monthly revenue..." />
```

**主站首页 `/`**

```html
<link rel="canonical" href="https://www.clinkbill.com/" />
```

**主站产品页 `/products/billing`**

```html
<link rel="canonical" href="https://www.clinkbill.com/products/billing" />
```

**Blog 列表页 `/blog`**

```html
<link rel="canonical" href="https://www.clinkbill.com/blog" />
<meta property="og:url" content="https://www.clinkbill.com/blog" />
```

### 5.4 代码级参考（示意，按项目实际实现调整）

**Next.js App Router — 动态文章页**

```tsx
const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? "https://www.clinkbill.com";

export async function generateMetadata({ params }): Promise<Metadata> {
  const path = `/blog/${params.slug}`;
  const canonical = `${SITE_URL}${path}`;
  return {
    alternates: { canonical },
    openGraph: {
      url: canonical,
      title: "...",
      description: "...",
    },
  };
}
```

**Next.js App Router — 根 layout 默认值 + 子页覆盖**

```tsx
export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? "https://www.clinkbill.com"),
  alternates: {
    canonical: "./", // 子路由可覆盖
  },
};
```

**验收用 curl 提取**

```bash
curl -s https://www.clinkbill.com/blog/monthly-recurring-revenue | grep -i 'rel="canonical"\|og:url'
```

---

## 6. 验收标准

- [ ] `https://www.clinkbill.com/` 源码含 `<link rel="canonical" href="https://www.clinkbill.com/" />`
- [ ] `https://www.clinkbill.com/products/billing` 源码含正确 canonical（path 为 `/products/billing`）
- [ ] `https://www.clinkbill.com/blog/monthly-recurring-revenue` 源码含 canonical 与 `og:url`，两者 URL 完全一致
- [ ] `https://www.clinkbill.com/blog` 列表页含 canonical 与 `og:url`
- [ ] 抽查 3 篇不同类型 Blog 文章（Glossary / Product / Industry News）均通过
- [ ] 主站抽查 `/agentic-payment`、`/contact` 均含 canonical
- [ ] 所有 canonical 均为 **绝对 URL**，host 与全站首选 host 一致
- [ ] 无页面 canonical 指向错误 slug 或错误 host
- [ ] GSC URL Inspection 对抽查 URL 显示「用户声明的 canonical」与预期一致（部署并重新抓取后验证）

---

*本任务单由外部 SEO 审计/协作方提交，供 Clink 方 agent 直接执行。完成后请将本文档移入 `clink/archive/`。*
