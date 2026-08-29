# 官网路径与 Vercel 子站：Rewrite / 反向代理说明

本文说明如何将 **https://thetawave.ai/** 上的部分路径，在不改变用户浏览器地址栏域名的前提下，转发到本仓库部署的 **https://thetawave-three.vercel.app/**（下称「营销子站」或「本项目」）。

**多语种 URL**（如 `/fr/use-cases/...`）：代理规则需与子站 `/<locale>/...` 路由一致，见专文 [thetawave-production-routing-i18n.md](./thetawave-production-routing-i18n.md)。

---

## 1. 背景与目标

| 项目 | 说明 |
|------|------|
| 产品官网 | https://thetawave.ai/（主站，可能为独立应用、CMS 或另一套前端） |
| 本项目 | 当前 Next.js 应用，部署在 Vercel：`https://thetawave-three.vercel.app/` |
| 目标 | 用户访问 `https://thetawave.ai/use-cases/...` 等路径时，**仍显示 thetawave.ai**，由边缘或源站将请求**透明转发**到 Vercel 子站并返回 HTML/静态资源 |

**推荐行为**：使用 **Rewrite（内部转发）** 或 **反向代理**，避免使用 302 跳到 `*.vercel.app`（不利于品牌与部分 SEO 场景）。

> **路径命名**：主站若使用 `/use-case/`（单数），而本项目路由为 **`/use-cases`**（复数），需在下方规则中按需统一为「主站对外路径 → 子站真实路径」的映射（见第 6 节）。

---

## 2. 本项目（thetawave-three）路径清单

以下路径由本仓库 [App Router](src/app) 提供，可按需挑选要挂在 `thetawave.ai` 下的前缀。

### 2.1 静态路径（固定段）

| 路径 | 说明 |
|------|------|
| `/` | 首页 |
| `/features` | Features 列表 |
| `/use-cases` | Use Cases 聚合页 |
| `/download` | 下载页 |
| `/chrome-extension` | Chrome 扩展 |
| `/thetawave-vs-chatgpt` | 对比页 |
| `/explore` | Explore |
| `/pricing` | 定价 |
| `/knowledge-hub` | Knowledge Hub 首页 |

### 2.2 动态路径

| 模式 | 说明 |
|------|------|
| `/knowledge-hub/[slug]` | 学科/主题笔记子页 |
| `/[slug]` | Feature 详情或 Use Case 详情（与静态段不冲突时由动态段匹配） |

配置代理时，请使用通配符覆盖子路径，例如 `/use-cases`、`/use-cases/foo`、动态 slug 页等。

---

## 3. 概念：Rewrite、反向代理与重定向

| 方式 | 浏览器地址栏 | 典型用途 |
|------|----------------|----------|
| **Rewrite（URL 重写）** | 始终为 `thetawave.ai/...` | 由 CDN/边缘/网关把请求转发到子站，用户无感 |
| **反向代理** | 同上 | 源站或网关作为客户端向 `thetawave-three.vercel.app` 发起 HTTP 请求，再返回给用户 |
| **301/302 重定向** | 会变成 `thetawave-three.vercel.app/...` | 简单但不利于统一域名展示，慎用 |

本文主要讨论 **Rewrite / 反向代理**。

---

## 4. 配置写在哪里？（重要）

**必须在「托管 thetawave.ai 的那一层」配置**，例如：

- 主站若部署在 **Vercel**：在主站对应项目的 `vercel.json`（或 Dashboard → Project → Rewrites）里写规则。
- 若走 **Cloudflare**：在 Cloudflare 的 Workers / Snippets / 源站规则中配置。
- 若自建 **Nginx / Caddy / Traefik**：在网关配置 `proxy_pass`。
- 若主站本身是 **Next.js**：可在主站项目的 `next.config.js` 里写 `async rewrites()` 指向外部域名。

**本项目仓库**（thetawave-three）仅在被 **直接访问** 时生效；要让 `thetawave.ai` 显示相同内容，需要 **主站项目或 DNS 前置层** 做转发，而不是只改本仓库（除非整个域名都指向本项目）。

---

## 5. 方案 A：主站托管在 Vercel 时使用 `vercel.json`

在主站代码仓库根目录增加（或合并）`vercel.json`，将指定路径转发到本项目域名。

**示例：将营销相关路径全部交给子站**

```json
{
  "rewrites": [
    {
      "source": "/use-cases",
      "destination": "https://thetawave-three.vercel.app/use-cases"
    },
    {
      "source": "/use-cases/:path*",
      "destination": "https://thetawave-three.vercel.app/use-cases/:path*"
    },
    {
      "source": "/features",
      "destination": "https://thetawave-three.vercel.app/features"
    },
    {
      "source": "/features/:path*",
      "destination": "https://thetawave-three.vercel.app/features/:path*"
    },
    {
      "source": "/knowledge-hub",
      "destination": "https://thetawave-three.vercel.app/knowledge-hub"
    },
    {
      "source": "/knowledge-hub/:path*",
      "destination": "https://thetawave-three.vercel.app/knowledge-hub/:path*"
    },
    {
      "source": "/download",
      "destination": "https://thetawave-three.vercel.app/download"
    },
    {
      "source": "/chrome-extension",
      "destination": "https://thetawave-three.vercel.app/chrome-extension"
    },
    {
      "source": "/thetawave-vs-chatgpt",
      "destination": "https://thetawave-three.vercel.app/thetawave-vs-chatgpt"
    },
    {
      "source": "/explore",
      "destination": "https://thetawave-three.vercel.app/explore"
    },
    {
      "source": "/pricing",
      "destination": "https://thetawave-three.vercel.app/pricing"
    }
  ]
}
```

**说明：**

- `/:path*` 用于带子路径或尾部斜杠差异；可按实际上线路径增删。
- 动态 slug（如 `/notes-generator`）若也要走子站，需增加更宽规则（注意与主站其它路由冲突），例如单独列出 slug 或由主站产品确认列表后再加。
- Vercel 对外部 `destination` 的 Rewrite 以 [官方文档](https://vercel.com/docs/projects/project-configuration#rewrites) 为准；若团队策略不允许外联，可改为 **同账号下多项目** 用内部别名（若适用）。

部署主站项目后，用无痕窗口访问 `https://thetawave.ai/use-cases` 应得到与子站一致的页面，且地址栏不变。

---

## 6. 主站路径为 `/use-case/` 而子站为 `/use-cases` 时

若对外统一使用 **`https://thetawave.ai/use-case`**（单数），但子站只有 **`/use-cases`**（复数），有两种做法：

### 6.1 仅在网关做映射（推荐，不改子站代码）

在主站 `vercel.json`（或 Nginx / Cloudflare）中：

```json
{
  "rewrites": [
    {
      "source": "/use-case",
      "destination": "https://thetawave-three.vercel.app/use-cases"
    },
    {
      "source": "/use-case/",
      "destination": "https://thetawave-three.vercel.app/use-cases"
    },
    {
      "source": "/use-case/:path*",
      "destination": "https://thetawave-three.vercel.app/use-cases/:path*"
    }
  ]
}
```

请根据真实路由调整：若不存在 `/use-cases/xxx` 子路径，可只保留前两行。

### 6.2 在子站增加 Next.js 重定向（可选）

若希望 **`thetawave-three.vercel.app/use-case`** 也能访问，可在 **本项目** `next.config.ts` 增加 `redirects`，把 `/use-case` 永久重定向到 `/use-cases`。这会影响直接访问子站域名的用户，需产品确认。

---

## 7. 方案 B：Cloudflare

若 thetawave.ai 的 DNS 在 Cloudflare，可使用：

- **Workers** 或 **Snippets**：按 `pathname` 匹配后 `fetch` 子站 URL，返回响应；可改写 `Location` 头（谨慎）。
- **Transform Rules / Origin Rules**：视套餐能力将特定路径回源到另一主机（取决于当前架构）。

具体以 Cloudflare 控制台与文档为准；思路与 Vercel Rewrite 相同：**匹配 path → 上游为 `thetawave-three.vercel.app`**。

---

## 8. 方案 C：Nginx 反向代理

适用于自建源站或前置 Nginx 的场景：

```nginx
# 示例：仅说明思路，域名与证书需自行配置
location /use-cases {
    proxy_pass https://thetawave-three.vercel.app;
    proxy_ssl_server_name on;
    proxy_set_header Host thetawave-three.vercel.app;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

- `Host` 必须与子站 Vercel 期望一致，否则可能 404 或证书问题；若 Vercel 项目绑定了自定义域，需与 Vercel 文档核对 **Host / 自定义域** 策略。
- 更稳妥的方式是：为 **thetawave-three** 在 Vercel 上绑定 **`marketing.thetawave.ai`** 等专用子域，Nginx 反代到该子域，避免与 `vercel.app` 默认 Host 不一致。

---

## 9. 方案 D：主站也是 Next.js 时的 `rewrites`

若 thetawave.ai 主站是 Next.js，可在主站 `next.config.ts` 中：

```ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/use-cases",
        destination: "https://thetawave-three.vercel.app/use-cases",
      },
      {
        source: "/use-cases/:path*",
        destination: "https://thetawave-three.vercel.app/use-cases/:path*",
      },
      // …按需追加
    ];
  },
};

export default nextConfig;
```

部署主站后同样实现「域名不变、内容由子站生成」。

---

## 10. 注意事项

### 10.1 绝对 URL 与 SEO

- 子站内若存在写死 **`https://thetawave-three.vercel.app`** 的链接，用户在主站域名下会看到跳到 Vercel 域名。应优先使用 **相对路径**（如 `/use-cases`）或环境变量 **`NEXT_PUBLIC_SITE_URL=https://thetawave.ai`** 生成绝对链接。
- `metadata` / `canonical` 建议在主站域名下由主站或子站构建时注入正确 `metadataBase`（本项目 [layout](src/app/layout.tsx) 已使用 `metadataBase`，部署到自定义域时需改为生产官网域名）。

### 10.2 Cookie 与登录态

- 若 `thetawave.ai` 与 `vercel.app` 跨域，Cookie 默认不共享。营销页通常无登录；若有统一账号，需 SSO 或同站点 Cookie 策略，超出本文范围。

### 10.3 `_next` 静态资源

- Next 页面会请求 `/_next/static/...`。若只 Rewrite 了 `/use-cases` 而 **未** 转发 `/_next`，可能出现样式/脚本 404。
- **做法**：对子站所需资源，在主站增加规则，将 `/_next/:path*` 也转发到同一 Vercel 部署（或与 Vercel 支持确认是否需单独规则）。若主站自身也是 Next 且同版本，可能冲突，需单独子路径部署或统一构建。

**简化建议**：由 **整站子域**（如 `www.thetawave.ai` 或路径前缀 `/marketing`）完整指向 Vercel 项目并绑定自定义域，减少 `/_next` 分裂问题。

### 10.4 安全与缓存

- 对外部上游做 Rewrite 时，注意 Vercel 的 **防火墙与速率限制**。
- CDN 缓存：HTML 与 `/_next` 缓存策略需区分，避免错缓存用户态页面。

---

## 11. 验证清单

1. 无痕窗口打开 `https://thetawave.ai/use-cases`（及已配置其它路径），地址栏仍为 `thetawave.ai`。
2. 打开开发者工具 → Network，确认文档与关键请求返回 200，无大量 404（尤其 `/_next/*`）。
3. 对比直接访问 `https://thetawave-three.vercel.app/use-cases`，核心内容与样式一致。
4. 若配置了 `/use-case` → `/use-cases`，两种主站 URL 行为符合预期。

---

## 12. 与本仓库的关系

- **本文件仅作运维/架构说明**；真正生效的 Rewrite 在 **thetawave.ai 的托管配置** 或 **主站代码仓库** 中。
- 若仅将 **自定义域**（如 `marketing.thetawave.ai`）在 Vercel 后台绑定到 **本项目**，则无需主站 Rewrite，用户通过子域访问即可，这是另一种常见部署方式。

---

## 13. 参考链接

- Vercel 项目配置（Rewrites）：https://vercel.com/docs/projects/project-configuration  
- 产品官网（当前线上文案与结构）：https://thetawave.ai/  
- 本项目 Vercel 预览/部署示例：https://thetawave-three.vercel.app/

---

*文档版本：与仓库 Next.js 迁移结构一致；路径以 `src/app` 为准，若路由有变更请同步更新第 2 节表格。*
