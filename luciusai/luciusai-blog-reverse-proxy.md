# Lucius AI Blog — 反向代理上线与维护手册

> **目标**：把 `https://luciusai.com/blog/*` 反向代理到独立部署的 OpenBlog 博客（Vercel：`https://lucius-blog-mocha.vercel.app`），使访客与搜索引擎**只见主域 URL**；此后博客内容由你（客户）自行维护（Markdown in Git）。
>
> **状态**：博客侧改造 ✅ 已完成（本地 + 线上 Vercel 均已验证）· **主站反代待配置**（需 Cloudflare/Railway 权限）
> **更新日期**：2026-09-11

---

## 0. TL;DR

---
> **关键**：主站是 Vite（非 Next.js），且博客已改为**完全自包含**（资源全在 `/blog` 下），因此主域 `/_next/*` 保持干净，反代只需 2 条规则。
>
> **SSOT**：资源路径 → §1.2；反代规则 → §2.1；Worker 代码 → §3.1；Vercel env → §6.1；验收 → §7。
---

---

## 1. 现状与目标

### 1.1 组件清单

| 组件 | 位置 / 地址 | 说明 |
|------|------------|------|
| **主站** | `https://luciusai.com` | Vite 应用，部署于 **Railway**，前置 **Cloudflare**（实测响应头含 `x-railway-request-id`、`Server: cloudflare`） |
| **博客（线上）** | `https://lucius-blog-mocha.vercel.app/blog` | Vercel 部署的 OpenBlog 应用 |
| **博客（仓库）** | `git@github.com:kostja94/lucius-blog.git`（分支 `master`） | 内容 + 代码同仓，内容变更走 git |

### 1.2 目标架构 — 资源路径 SSOT

```
luciusai.com（Vite 主站 · Railway + Cloudflare）
   ├── /blog/*     ─┐
   └── /zh/blog/*   ┘  Rewrite / Worker（地址栏不变）
                       │
                       ▼
   lucius-blog-mocha.vercel.app（OpenBlog · Next.js）
     · 页面：/blog/*、/zh/blog/*
     · 资源：/blog/_next/static/*（JS/CSS/字体）
     · 图片：/blog/_next/image?url=%2Fblog%2Fimages%2F...
     · 品牌：/blog/brand/lucius-logo.svg、/blog/favicon.svg
```

**关键**：博客的**每一个**资源（JS/CSS/字体/图片优化端点/logo/favicon）都在 `/blog` 下，主域 `/_next/*` 完全不被使用 —— 这也是反代只需两条规则的原因（§2.1），且未来主站若迁 Next.js 也不会冲突。

---

## 2. 反代规则

### 2.1 两条规则（SSOT）

| # | 主域路径 | 转发目标 |
|---|---------|---------|
| 1 | `/blog/*` | `{BLOG_ORIGIN}/blog/*` |
| 2 | `/zh/blog/*` | `{BLOG_ORIGIN}/zh/blog/*` |

`{BLOG_ORIGIN} = https://lucius-blog-mocha.vercel.app`

`sitemap.xml`、`rss.xml`、`_next/*`、`images/*`、`brand/*`、`favicon.svg` **全部以 `/blog` 开头**，已被规则 1 覆盖，无需单列。

### 2.2 改造前后对照

| 改造前曾必须单列转发 | 现在 |
|---|---|
| `/_next/*`（JS/CSS/字体）、`/_next/image`、`/brand/lucius-logo.svg`、`/favicon.svg` | 全部收进 `/blog`，由规则 1 覆盖（改动详见 §5） |

### 2.3 无尾斜杠

OpenBlog 约定 **无尾斜杠**（`/blog/post`）。反代规则**不要**添加 `/blog/post` → `/blog/post/` 的重定向。

---

## 3. 方案 A（推荐）：Cloudflare Worker

主站已在 Cloudflare 后面，Worker 最可控、最易回滚。

### 3.1 Worker 代码

Cloudflare Dashboard → **Workers & Pages → Create → Worker**，粘贴：

```js
// lucius-blog-proxy
const BLOG_ORIGIN = "https://lucius-blog-mocha.vercel.app";

// Only these two path prefixes belong to the blog. Everything else is the
// main site and passes through untouched.
function isBlogPath(pathname) {
  return (
    pathname === "/blog" ||
    pathname.startsWith("/blog/") ||
    pathname === "/zh/blog" ||
    pathname.startsWith("/zh/blog/")
  );
}

export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (!isBlogPath(url.pathname)) {
      return fetch(request); // main site: untouched
    }

    const target = new URL(BLOG_ORIGIN);
    url.protocol = target.protocol;
    url.hostname = target.hostname;
    url.port = "";

    // Host header is set automatically from the target URL (Vercel needs its
    // own host) — do not try to override it.
    return fetch(new Request(url.toString(), request), { redirect: "manual" });
  },
};
```

### 3.2 绑定路由

Worker → **Settings → Triggers → Routes**，添加 **两条**：

| Route | Zone |
|-------|------|
| `luciusai.com/blog/*` | luciusai.com |
| `luciusai.com/zh/blog/*` | luciusai.com |

> 也可放宽为 `luciusai.com/*` 一条（Worker 内部已用 `isBlogPath` 白名单过滤），但两条精确 route 更保险。

### 3.3 可选：重定向兜底

Next.js 的 `redirects()`（本项目已有 `/blog/knockin-guide` → `/blog/how-to-use-knockin`）生成**相对** `Location`，浏览器按主域解析，不泄漏 Vercel 子域。若仍要加固，在 §3.1 的 `fetch` 后包一层：读 `res.headers.get("location")`，含 `lucius-blog-mocha.vercel.app` 时用 `new Response(res.body, res)` 改写为 `https://luciusai.com` 再返回。

### 3.4 缓存建议

| 条件 | 动作 |
|------|------|
| `/blog/_next/static/*` | Edge 长缓存（1 年，immutable） |
| `/blog/_next/image*` | 沿用 Vercel 返回的 `Cache-Control`（**勿覆盖**） |
| `/blog/*` HTML | **不要**长缓存（内容会更新） |

---

## 4. 方案 B：Cloudflare Transform Rules（无代码）

**Rules → Transform Rules → Rewrite URL**：

| 字段 | 值 |
|------|----|
| 条件 | `starts_with(http.request.uri.path, "/blog/") or starts_with(http.request.uri.path, "/zh/blog/") or http.request.uri.path eq "/blog" or http.request.uri.path eq "/zh/blog"` |
| 动作 | Rewrite URL → Dynamic |
| Target | `concat("https://lucius-blog-mocha.vercel.app", http.request.uri.path)` |
| Query | 保留原样 |

注意：Transform Rules 的 **host 改写能力随套餐而异**（部分套餐只能改 path）。若改写后请求仍回主站，请改用方案 A。

---

## 5. 博客侧改造（已实施并验证）

改动已落地并推送（commit `a4a04df`，博客仓 `master`）：

| # | 改动 | 文件 |
|---|------|------|
| 1 | `images.path` 跟随 `ASSET_PREFIX` → `/blog/_next/image` | `next.config.ts` |
| 2 | `ASSET_PREFIX=/blog`（驱动 `assetPrefix` + `images.path`） | `.env.example`、`.env.local`、**Vercel Env（待补，见 §6.1）** |
| 3 | logo → `/blog/brand/lucius-logo.svg` | `openblog.config.ts` + `site-header.tsx` |
| 4 | favicon → `/blog/favicon.svg` | `root-shell.tsx` |
| 5 | 删 `src/app/icon.svg`（与 favicon 字节相同的副本，会注入根路径 `/icon.svg`） | `src/app/icon.svg`（已删） |
| 6 | 删未引用的模板遗留资源 | `public/brand/openblog-logo.svg`、`public/images/openblog-cover.svg` |

**本地实测**（生产 build + `next start`）：

- 产物中 **0 处**无前缀 `/_next/` 引用；实际形态为 `/blog/_next/static/chunks/*`、`/blog/_next/static/media/*.woff2`、`/blog/_next/image`、`/blog/brand/lucius-logo.svg`、`/blog/favicon.svg`
- 页面 `/blog`、`/blog/{slug}`、`/zh/blog`：**200**
- 运行时资源请求（CSS/JS/字体/logo）：**12/12 200**
- 图片优化端点 `/blog/_next/image?url=%2Fblog%2Fimages%2F...`：**200**，`content-type: image/jpeg`
- dev 模式（同带 `ASSET_PREFIX`）：资源全在 `/blog/_next/static/*`，**200**
- CSS 内字体走相对路径 `../media/*.woff2` → 解析为 `/blog/_next/static/media/`

**线上实测**（Vercel，`ASSET_PREFIX` 已配置并部署）：

- 页面**完整渲染**（截图核验：样式、卡片网格、hero 图正常，非裸 HTML）
- 导航 logo → `/blog/brand/lucius-logo.svg` ✅ 已带 `/blog` 前缀
- 图片优化端点 → `/blog/_next/image?url=%2Fblog%2Fimages%2F...` ✅ 已带 `/blog` 前缀
- sitemap：**43 篇文章 + 5 个分类 + 全部作者页的 `<loc>` 均指向 `https://luciusai.com/...`**，**零 `vercel.app` 泄漏**
- 分类已为新 5 类（AI / Community / AI Employee Role Guide / Automation / Knockin）；FAQ 与结尾 CTA 均正常

> 线上 HTML 里的 `/_next/static/*` 无法从外部抓取工具直接读取（不在其可提取的元素内）。但 `assetPrefix` 与 `images.path` 在 `next.config.ts` 中读**同一个** `ASSET_PREFIX`，图片端点已实测带前缀 → `assetPrefix` 必然同样生效。如需肉眼确认，浏览器 DevTools → Network 查看 JS/CSS 请求是否均以 `/blog/_next/static/` 开头即可。

> **一处需知**：Next 应用在**其自身部署域**（Vercel）上仍会响应根路径 `/_next/image`（框架向后兼容行为），但**页面已不再请求该路径** —— 不对主域命名空间造成任何占用。

---

## 6. Vercel 侧配置

### 6.1 环境变量（SSOT）

Vercel 项目 → Settings → Environment Variables（Production）：

| 变量 | 值 | 说明 |
|------|----|------|
| `SITE_URL` | `https://luciusai.com` | 兜底（canonical 实际以 `config.site.url` 优先） |
| `DEPLOY_MODE` | `subdirectory` | 保留 `/blog` 前缀 |
| `BLOG_BASE_PATH` | `/blog` | 博客基路径 |
| **`ASSET_PREFIX`** | **`/blog`** | **⚠️ 必须加**。未加则资源回落到 `/_next/*`，§2.1 的两条规则即失效 |

> 该变量在 **build 阶段**被 `next.config.ts` 读取并烘焙进产物，因此**改完必须重新部署**（§6.3）。
> ✅ 线上已配置并生效（导航 logo 与图片端点均已带 `/blog` 前缀，详见 §5 线上实测）。

### 6.2 部署保护

Settings → **Deployment Protection**：若开启（Vercel Authentication / Password），反代会拿到 **401** → 需关闭，或使用 **Protection Bypass for Automation**（在 §3.1 的 Worker 里补 `x-vercel-protection-bypass` 头）。

### 6.3 重新部署

改造后需在 Vercel 触发一次部署（push 即自动，或 Deployments → 最新提交 → **Redeploy**），否则线上仍是无前缀的旧版本。

---

## 7. 上线验收清单

| # | 检查 | 通过标准 |
|---|------|---------|
| 1 | `curl -I https://luciusai.com/blog` | 200，内容为**新版**博客 |
| 2 | `curl -I https://luciusai.com/blog/what-is-an-ai-coworker` | 200 |
| 3 | `curl -I https://luciusai.com/zh/blog` | 200 |
| 4 | 浏览器打开文章页 → Network | **无 404**；CSS 生效；图片显示；logo 正常 |
| 5 | 资源路径抽查 | 形如 `/blog/_next/static/*`、`/blog/_next/image?url=...` |
| 6 | `canonical` | `https://luciusai.com/blog/{slug}` |
| 7 | `https://luciusai.com/blog/sitemap.xml` | `<loc>` 全为主域，**无** `vercel.app` 泄漏 |
| 8 | 语言切换 | `/blog` ↔ `/zh/blog` 互跳，地址栏无 vercel 子域 |
| 9 | **主域 `/_next/*` 未被占用** | `curl -I https://luciusai.com/_next/static/x.js` → 404 |
| 10 | 移动端 | 汉堡菜单开合正常 |

---

## 8. 回滚

| 方案 | 动作 | 生效 |
|------|------|------|
| A / B（Cloudflare） | 删除 Worker Route / Transform Rule | 秒级 |
| 博客侧 | 移除 `ASSET_PREFIX` 并 Redeploy（资源回到 `/_next/*`） | 需同步恢复旧的反代规则 |

主站旧 `/blog`（CMS）**不要立即删除**；反代生效后观察 2–4 周再下线。

---

## 9. 博客日常更新流程（你来维护）

博客内容 = **Markdown in Git**，改完 push 即自动上线（Vercel 已连 GitHub）。

### 9.1 内容位置

```
{blog-repo}/
├── content/blog/*.md          # 英文文章（42 篇）
└── content/blog/zh/*.md       # 中文文章（42 篇，与英文同 slug）
├── public/blog/images/{slug}/ # 每篇 hero / 正文图（webp）
└── src/data/
    ├── faq-data.json          # 每页 FAQ（key 形如 /blog/{slug}、/zh/blog/{slug}）
    └── final-cta-data.json    # 每篇文章结尾 CTA
```

### 9.2 Frontmatter 字段（新增文章照抄）

```yaml
---
title: "主主题: 副标题"           # 页面 H1，Title Case
description: "130–160 字符摘要"    # 列表卡片 excerpt（下限 50，中文可短）
seoTitle: "≤60 字符 SERP 标题"     # 可选，缺失回退 title
seoDescription: "≤155 字符 SERP 描述"  # 可选，缺失回退 description
slug: "kebab-case-与文件名一致"
date: "2026-09-11"
author: "Lucius Team"
category: "AI"                    # 5 选 1：AI / AI Employee Role Guide / Automation / Community / Knockin
categorySlug: "ai"                # 中文文章必填（中文分类名无法自动转 slug）
tags: ["AI"]
cover: "/blog/images/{slug}/hero.webp"
locale: "en"                      # en | zh
draft: false
---
```

> ⚠️ `slug` 必须与文件名一致，否则 `npm run validate:posts` 失败。
> ⚠️ 图片路径必须以 `/blog/images/...` 开头（不要写成 `/images/...`），否则反代下取不到。

### 9.3 预览与校验

```powershell
npm install
npm run dev            # http://localhost:3000/blog
npm run validate:posts # frontmatter 校验（发版前必跑）
```

### 9.4 发布

```powershell
git add content/blog public/blog/images src/data
git commit -m "content: add <slug>"
git push origin master
```

推送后 **Vercel 自动构建部署**（1–3 分钟），主站反代即时透传，无需重配 Cloudflare。若未自动部署，见 §6.3。

### 9.5 内容规范

写作规范见同目录 `skills/luciusai-blog-article/SKILL.md`（含 article-types / keywords / internal-links / gates / selfcheck）。

---

## 10. 风险与待办

| # | 事项 | 处理 |
|---|------|------|
| 1 | **反代配置**：主站 Railway/Cloudflare 后台不在我方控制范围 | 需由你或运维执行 §3 / §4 |
| 2 | **Vercel Deployment Protection**：开启则反代 401 | §6.2 |
| 3 | **上线后按验收清单逐项核对** | §7 |
| 4 | **新文章图片路径**写成 `/images/...` 会在反代下 404 | 必须用 `/blog/images/...`（§9.2） |

---

## 11. 参考

| 来源 | 可借鉴之处 |
|------|-----------|
| **OpenBlog 官方集成文档**（`integrations/patterns/`） | `reverse-proxy.md`：`ASSET_PREFIX` 用途、nginx sketch、**无尾斜杠**约定；`subdirectory.md`：子目录挂载五步 |
| **同构博客迁移项目的历史经验** | 多个「独立博客 + 主域反代」项目的通用坑：双 Next 应用的 `/_next` 命名空间冲突（CSS 404），解法即本文的 `ASSET_PREFIX` 方案 |
| **反代型 SEO 站发版流程经验** | CI 即部署 + 上线后 URL 复核 + 回滚开关设计 |
| **CloudFront → Vercel 反代实例经验** | 反代只统一 URL 路径，**不会**继承主站前端资源 / 统计代码（GA 等需在博客侧单独配置） |

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [luciusai-blog-migration-plan.md](./luciusai-blog-migration-plan.md) | Blog 迁移总计划 |
| [luciusai-site-structure.md](./luciusai-site-structure.md) | 全站 URL 架构与 i18n |
| [luciusai-zh-i18n-audit.md](./luciusai-zh-i18n-audit.md) | 中文 blog 质量审计 |
| [README.md](./README.md) | 本目录文件索引 |

*Last updated: 2026-09-11*
