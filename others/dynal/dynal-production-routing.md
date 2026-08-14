# Dynal 生产路由（dynal.ai）：Rewrite、子站与多语言

本文说明如何在 **https://dynal.ai/** 上，对用户**保持主域与路径不变**的前提下，将**部分路径**透明转发到独立部署的 **Next.js 营销子站**。

**营销子站（当前）**：**[https://dynal-nextjs.vercel.app/](https://dynal-nextjs.vercel.app/)** —— 下文示例中的 `destination` 均指向该 origin。若 Vercel 项目更名或绑定其它预览域名，请同步替换全文中的 URL。

> **⚠️ 状态（2026-05）**：营销子站方案**未上线**；本文内容保留供日后复用。当前阶段不使用 dynal-nextjs.vercel.app 进行 Rewrite。

Dynal 的**特殊点**：同一前缀 **`/linkedin-post-generator`** 下 **父路径与子路径分流** —— **hub（`/linkedin-post-generator`）已上线**，留在主应用；**子路径**（如 `/linkedin-post-generator/hiring-post`）走营销子站（见 §2、§5，当前子站方案未上线）。

**站内 URL 权威**（sitemap、Solutions 路径等）：仍以 [dynal-site-structure.md](./dynal-site-structure.md) 为准。**`/linkedin-post-generator`** 已上线（hub 页）；**`/linkedin-post-generator/{topic}`** 为 SEO 集群子路径（与竞品常见 `…/linkedin-post-generator/{topic}` 形态对齐）。**`/solutions/linkedin-post-generator`** 将被废弃。

---

**Last updated**: 2026-05-11 — `/linkedin-post-generator` hub 已上线；标注营销子站未上线；`/solutions/linkedin-post-generator` 将被废弃。

## 1. 背景与目标

| 项目 | 说明 |
|------|------|
| 主站 / 主应用 | **https://dynal.ai/**，承载首页、应用区、`/solutions/*` 等（见 [dynal-site-structure.md](./dynal-site-structure.md)） |
| 营销子站 | Next 应用，当前部署 **https://dynal-nextjs.vercel.app** |
| 目标 | 指定路径在浏览器地址栏仍为 **dynal.ai**，由边缘或源站 **Rewrite** 到子站；避免 302 裸露 `*.vercel.app`（品牌与部分 SEO 场景） |

**推荐**：Rewrite / 反向代理，而非整页 302 到子站域名。

---

## 2. 核心结论：「父路径本地，子路径走子站」

Dynal 在 **`/linkedin-post-generator`** 上采用**分层路由**（区别于「从根前缀起整棵子树全部转发到子站」的简单模式）：

| 用户访问（主域） | 期望行为 |
|------------------|----------|
| **`/linkedin-post-generator`**（**无**后续 path segment，或仅尾部 `/`） | 由**主项目（当前 dynal.ai 主应用）**直接响应，**不做**到营销子站的 Rewrite。 |
| **`/linkedin-post-generator/hiring-post`** 等 **至少多一段路径** | 通过 Next `rewrites`（或网关等价规则）转发到 **`https://dynal-nextjs.vercel.app/linkedin-post-generator/hiring-post`**（路径与子站 App Router 保持一致）。 |

**一句话**：**hub 页留在主栈**；**topic / 集群落地页**在营销子站实现，由代理把 **`/linkedin-post-generator/*`** 的「有子路径」请求指过去。

**实现注意（避免误匹配父路径）**

- Vercel / Next 常见写法 **`/linkedin-post-generator/:path*`** 中，若 `:path*` 含 **零段**，可能把 **`/linkedin-post-generator` 本身**也重写到子站，与产品要求冲突。  
- **推荐**：  
  - **逐条列举**已上线的子路径（如 `/linkedin-post-generator/hiring-post`），或  
  - 使用平台支持的 **「至少一段」** 匹配（若你方 `next.config` / 网关支持 `:path+`、正则等），并在预发环境验证 **`/linkedin-post-generator` 仍为 200 且由主应用渲染**。  
- **规则顺序**：更具体的路径规则应排在宽泛规则之前，避免被其它 catch-all 吃掉。

---

## 3. 配置写在哪里？

**必须在托管 dynal.ai 的那一层**配置：

- 主站若在 **Vercel**：主站项目的 `vercel.json` 或 Dashboard → Rewrites。  
- **Cloudflare / Nginx / Caddy** 等：在对应 Worker、Snippet 或 `proxy_pass` 中匹配 path。  
- 主站若本身是 **Next.js**：主站 `next.config.ts` 的 `async rewrites()` 指向 **`https://dynal-nextjs.vercel.app`**（或环境变量，见下节）。

营销子站仓库**单独部署**；仅当用户**直接访问** [dynal-nextjs.vercel.app](https://dynal-nextjs.vercel.app/) 时，子站路由在该域名下单独生效。

---

## 4. 主站 Next.js：`rewrites` 示例（英文路径）

下列示例演示「**只转发子路径**」；**不要**加入会把裸 `/linkedin-post-generator` 送到子站的规则。

```ts
import type { NextConfig } from "next";

/** 营销子站 — 与 Vercel 部署一致；生产可用环境变量覆盖 */
const DYNAL_MARKETING_NEXT =
  process.env.DYNAL_MARKETING_NEXT_ORIGIN ?? "https://dynal-nextjs.vercel.app";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: "/linkedin-post-generator/hiring-post",
        destination: `${DYNAL_MARKETING_NEXT}/linkedin-post-generator/hiring-post`,
      },
      // 若有更多 topic 页，继续追加，或改为受支持的「至少一段」通配（见 §2）
      // {
      //   source: "/linkedin-post-generator/:path+",
      //   destination: `${DYNAL_MARKETING_NEXT}/linkedin-post-generator/:path+`,
      // },
    ];
  },
};

export default nextConfig;
```

`vercel.json` 等价写法亦为 `source` / `destination` 对；合并进主站现有 `rewrites` 数组即可。

```json
{
  "rewrites": [
    {
      "source": "/linkedin-post-generator/hiring-post",
      "destination": "https://dynal-nextjs.vercel.app/linkedin-post-generator/hiring-post"
    }
  ]
}
```

---

## 5. 与 `/solutions/linkedin-post-generator` 的关系

> **⚠️ 规划变更（2026-05）**：`/solutions/linkedin-post-generator` **将被废弃**，`/linkedin-post-generator` 已上线（hub + 10 topic 子页）。原 Solutions 另两页已迁移至 `/product/linkedin-ai-writer` 和 `/product/linkedin-content-system`。

路径状态与迁移详情见 [dynal-site-structure.md](./dynal-site-structure.md) §五 和 [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md) §2。内链与 canonical 请在子站与主站 `metadata` 中显式维护，避免同一意图多 URL 无标注。

---

## 6. 多语言路径（`/fr/...`、`/es/...` 等）

原则与英文路径相同：**代理层原样保留 `/<locale>/` 前缀**，子站需存在对应 `app/[locale]/...`（或 `next-intl` 等）路由后再在主域写 rewrites。

### 6.1 线上语言前缀（与 sitemap 一致）

根据 [dynal-site-structure.md](./dynal-site-structure.md) **〇.2**：

- **默认英文**：多数模板路径**无前缀**（如 `/pricing`）。  
- **其它 UI 语言**：**`/{locale}/`**，`locale ∈ { es, fr, de, pt, it }`（**无** `/en/`）。

### 6.2 代理层要「原样转发语言前缀」

用户访问 **`https://dynal.ai/fr/linkedin-post-generator/hiring-post`** 时，上游应请求 **`https://dynal-nextjs.vercel.app/fr/linkedin-post-generator/hiring-post`**（或团队约定的等价路径），**不要**剥掉 `/fr` 再指望子站猜语言。

### 6.3 子站必须先有对应路由

在浏览器**直接打开**（不经过主域）：

- `https://dynal-nextjs.vercel.app/fr/linkedin-post-generator/hiring-post`

若 **404**：先在**营销子站**实现 `app/[locale]/linkedin-post-generator/...`（或等价结构），再补主域 rewrites。

### 6.4 与英文规则「平行」增加 `/<locale>`

**方案 A — 宽前缀（仅当主站在该 locale 下无冲突路由时）**

```json
{
  "rewrites": [
    {
      "source": "/fr/linkedin-post-generator/:path+",
      "destination": "https://dynal-nextjs.vercel.app/fr/linkedin-post-generator/:path+"
    }
  ]
}
```

> 若平台不支持 `:path+`，则对 **`/fr/linkedin-post-generator/hiring-post`** 等**逐条**写规则（同 §4）。  
> **`/fr/linkedin-post-generator`** 是否留在主应用：应与英文 **`/linkedin-post-generator`** 策略一致（通常 **hub 仍主应用**）。

**方案 B — 与英文逐条对齐（更安全）**  
对每个已代理的英文子路径，增加 `es`、`fr`、`de`、`pt`、`it` 各一条，避免误伤主站同前缀下的其它业务。

### 6.5 `/_next` 与静态资源

多语种页仍请求 **`/_next/static/...`**，路径**通常不带** `fr`。若主站已对营销子站页面转发过 `/_next`，各语言页一般**共用**同一套规则。

若页面能打开但**无样式、控制台大量 `/_next/*` 404**：在主站为子站页面补充 **`/_next/:path*`** → **`https://dynal-nextjs.vercel.app/_next/:path*`**（或与运维确认是否由 CDN 统一回源）；注意与主站自身 Next 构建的 `/_next` **不要冲突**（冲突时需更窄匹配或专用子路径部署）。

### 6.6 默认语言 URL 与 hreflang

| 策略 | 主域示例 | 注意 |
|------|----------|------|
| 默认语无前缀 | 英文 `/linkedin-post-generator/...`；法文 `/fr/linkedin-post-generator/...` | 英文用 §4；法文用 §6。 |
| 所有语言均带前缀 | `/en/...`、`/fr/...` | 需为 **`/en` 与 `/fr` 等** 同时配置 rewrites，并与子站路由一致。 |

与 **canonical、`hreflang` alternate** 一致；在子站 `metadata` / sitemap 维护，代理只转发不改变路径语义。

### 6.7 不建议的捷径

| 做法 | 问题 |
|------|------|
| 只代理英文子路径，用法文 cookie 在子站切语言但 URL 仍英文 | 分享链接与 SEO 语言信号弱；与 `/fr/...` 策略不一致。 |
| 主域 302 到 `dynal-nextjs.vercel.app/fr/...` | 与统一主域 **dynal.ai** 展示冲突。 |

---

## 7. 绝对 URL、Cookie、`metadataBase`

- 子站内链避免写死 **`dynal-nextjs.vercel.app`**；用相对路径或 **`NEXT_PUBLIC_SITE_URL=https://dynal.ai`**。  
- 营销页通常无登录；若跨域 Cookie，需单独方案。  
- **`metadataBase` / canonical** 以 **https://dynal.ai** 为准（用户经 Rewrite 访问时地址栏仍为 dynal.ai）。

---

## 8. 验证清单

1. **`/linkedin-post-generator`**（无子路径）：**200**，且由**主应用**提供（非子站 HTML 特征可对比响应头或构建指纹）。  
2. **`/linkedin-post-generator/hiring-post`**（及已配置其它子路径）：地址栏为 dynal.ai，**内容与** [https://dynal-nextjs.vercel.app/linkedin-post-generator/hiring-post](https://dynal-nextjs.vercel.app/linkedin-post-generator/hiring-post) **一致**（路径以实际上线为准）。  
3. **`/fr/linkedin-post-generator/hiring-post`**（若已上线）：同上，且为对应语言内容。  
4. **Network**：`/_next/*` 无大面积 404。  
5. 对照 [dynal-site-structure.md](./dynal-site-structure.md)： **`/solutions/linkedin-post-generator`** 过渡期间行为不受本文子路径 Rewrite 破坏；废弃后以 `/linkedin-post-generator/` 为准。

---

## 9. 与本目录的关系

- 本文描述**架构与配置位置**；生效的 `rewrites` 在 **主站（dynal.ai）托管仓库** 或边缘网关。  
- **营销子站**（dynal-nextjs）内的 App Router、翻译与集群页在子站代码仓库实现；路径变更时请同步更新本文示例与 [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md) 中的内链规划。

---

## 10. 参考

- Dynal 站点结构：[dynal-site-structure.md](./dynal-site-structure.md)  
- Post generator 专档：[dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)  
- 营销子站（直接访问校验）：[https://dynal-nextjs.vercel.app/](https://dynal-nextjs.vercel.app/)  
- Vercel Rewrites：https://vercel.com/docs/projects/project-configuration  

---

*文档版本：Dynal 主域 + dynal-nextjs 营销子站；`/linkedin-post-generator` 父子分流。子站 origin 以 Vercel 部署为准，若变更请替换文中 `https://dynal-nextjs.vercel.app` 并补齐 topic 列举规则。*
