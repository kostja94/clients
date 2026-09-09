# today.ai/articles 308 无限重定向 — 修复说明（给 today-web 主站方）

> 排查日期：2026-09-09 · 定位方式：只读（Vercel API + 线上请求对照），未改动任何项目
> 问题归属：**today-web（`today.ai` 域名的 Vercel 项目）**，本仓 today-seo 无法自行解决

---

## 一、现象

| 路径 | 结果 |
|---|---|
| `https://today.ai/articles` | ⚠️ 308 无限循环（浏览器报"重定向次数过多"） |
| `https://today.ai/articles/healthcare` 等子路径 | ✅ 200 正常 |
| `https://article.today.ai/articles?__today_seo_proxy=today-web`（后端直连） | ✅ 200，0 次跳转 |

## 二、定位结论

- `today.ai` 域名 → Vercel 项目 **today-web**
- `article.today.ai` 域名 → Vercel 项目 **today-seo**（新 SEO 站）
- 关键对照：请求 `https://today.ai/articles?__today_seo_proxy=today-web` **仍然 308 到相同 URL**；而同一 URL 直接请求 `article.today.ai` 返回 **200 无跳转**
- 结论：308 由 **today-web 在转发给 SEO 站之前自己发出**，today-seo 后端收不到请求，故 today-seo 侧任何修改都无效

## 三、根因

today-web 把 `/articles` 转给 SEO 站时写成 **redirect（308）** 而非 **rewrite（服务端代理）**。

Vercel 匹配 redirect 只看 pathname、忽略 query：规则把请求改写为 `/articles?__today_seo_proxy=today-web` 后，pathname 仍是 `/articles`，**再次命中自身 → 无限循环**。子路径 `/articles/xxx` 不命中该条、走 rewrite，所以一直正常。

> 背景：以前 `/articles` 由主站直接渲染（无转发），迁移到 article.today.ai 后这条转发被加成 redirect 才暴露。

## 四、改法（today-web 一处）

把 `/articles` 这条从 **redirect 改为 rewrite**（destination 不变）；若已有 `/articles/:path*` 的 rewrite，直接**删除该 redirect** 即可。

```ts
// 现在（错误）—— redirects()
{ source: "/articles", destination: "https://article.today.ai/articles?__today_seo_proxy=today-web", statusCode: 308 }

// 改为（正确）—— rewrites()
{ source: "/articles", destination: "https://article.today.ai/articles?__today_seo_proxy=today-web" }
```

修改位置视规则现状：
- 代码：`today-platform-web` 的 `next.config.ts`（`redirects()` / `rewrites()`）或仓库根 `vercel.json` → 改后正常发版
- 面板：Vercel → today-web → Settings → Redirects / Rewrites → 移到 Rewrites 或删除

## 五、验证（部署后）

```sh
curl -sSI https://today.ai/articles
# 期望：200（非 308）；/articles/healthcare 等子路径保持 200
```

> article.today.ai（today-seo 项目 vercel.json）中的 host 重定向是防旧域名直连循环的保护逻辑，**无需改动**。
