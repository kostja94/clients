# Final Round 生产路由与技术栈（前端实施）

> **读者**：负责主域 **Rewrite / 边缘转发** 的前端（或全栈）同学。  
> **站点根**：https://www.finalroundai.com/  
> **营销子站（Vercel 部署域名）**：**https://finalround.vercel.app** —— 营销内容由该子站单独配置与发布；主站 `rewrites` / 边缘规则的 `destination` 应指向该 origin（或通过环境变量覆盖为预览 URL）。  
> **Tech Layoffs 子站（独立 Vercel 项目）**：**https://finalround-nextjs.vercel.app** —— Tech Layoffs 板块独立部署、本地维护；主站**仅** `/tech-layoffs` 路径 Rewrite 至此 origin（Mohit 维护），子域名上其他路径不转发。运营手册见 [tech-layoffs/README.md](../tech-layoffs/README.md)。  
> **URL 实值**：以 [finalround-site-structure.md](../finalround-site-structure.md) 为准；下文代码里用 **`marketing`** 作为 **`<segment>` 的示例首段**，合并规则时请替换为实际路径段。

---

## 内容与视觉（维护边界）

- **内容**：营销子站（或 `/<segment>` 下）由 **同一维护者** 单独维护；主站前端主要对接 **转发规则** 与子站 **origin** 环境变量。  
- **外观**：可与主站略有差异，须对齐 [finalround-brand-visual.md](../finalround-brand-visual.md) 中的品牌与组件级一致性。

---

## 1. 技术栈（给前端的落地说明）

| 层级 | 选型 | 前端需要做什么 |
|------|------|----------------|
| **营销子站** | **Next.js**（App Router，建议 14+） | 子站仓库内路由、`metadata`、`next.config` 的 **basePath**（若不用则默认为 `/`）。与主域拼接无关的纯子站开发在此完成。 |
| **子站托管** | **Vercel**（营销子站固定使用 **`https://finalround.vercel.app`**） | 主站转发基址：`FINALROUND_MARKETING_ORIGIN`（建议生产设为 `https://finalround.vercel.app`，预览可指向 Preview Deployment URL）。若日后绑定营销专用自定义域，同步改环境变量与网关 `Host` 策略即可。 |
| **主域分流** | 三选一或组合：**① 主站 Next `rewrites`**、**② 主站 `vercel.json` rewrites**、**③ Cloudflare Worker/Snippet**、**④ Nginx `proxy_pass`** | **在托管 www.finalroundai.com 的仓库或网关** 增加规则；**不要**只在营销子站仓库改代码期望主域生效。 |
| **DNS** | **Cloudflare** 橙云代理（若主域走 CF） | 与运维确认 **SSL 模式（Full/Strict）**；Worker 与 DNS 代理链路由运维/平台文档约束。 |

**概念**：对用户使用 **Rewrite / 反向代理**，地址栏保持 **www.finalroundai.com**；避免整页 **302** 到托管商默认域名等裸露跳转（品牌与 SEO）。

---

## 2. 配置写在哪里？（必须先对齐）

| 主站实际托管 | 前端改哪里 |
|--------------|------------|
| **Vercel 上的主站项目** | 主站仓库根目录 **`vercel.json`** 的 `rewrites`，或 Dashboard → Project → Rewrites |
| **主站是 Next.js（含 Vercel）** | 主站 **`next.config.ts` / `next.config.js`** 里 `async rewrites()`（与 `vercel.json` 二选一或合并策略以团队为准，避免重复转发） |
| **主域经 Cloudflare** | **Wrangler / 控制台** 的 Worker、或 **Snippets**、或 **Transform / Origin Rules**（能力视套餐） |
| **自建 Nginx / Caddy** | 网关配置里 **`location` + `proxy_pass`** |

营销子站仓库 **单独部署**；规则生效对象是 **「用户请求主域时」** 由哪一层把请求转到子站 origin。

---

## 3. 模式 A：整段前缀交给子站（子站独占该前缀）

适用于：`/<segment>` 及其子路径 **全部**由营销 Next 提供（列表页 + 动态 slug 同栈）。

### 3.1 `vercel.json`（主站项目在 Vercel 时）

将示例中的 **`marketing`** 全部替换为你们的 **`<segment>`**；`destination` 基址默认为 **`https://finalround.vercel.app`**（与上文「营销子站」一致）。

```json
{
  "rewrites": [
    {
      "source": "/marketing",
      "destination": "https://finalround.vercel.app/marketing"
    },
    {
      "source": "/marketing/:path*",
      "destination": "https://finalround.vercel.app/marketing/:path*"
    },
    {
      "source": "/_next/:path*",
      "destination": "https://finalround.vercel.app/_next/:path*"
    }
  ]
}
```

最后一组 **`/_next`**：仅当 **主站自身不是另一套 Next 占用根路径 `/_next`** 时可直接加；若主站也是 Next 且会冲突，见 **§7**，优先 **子域承载营销** 或更窄的匹配策略。

### 3.2 主站 `next.config.ts` 的 `rewrites`（等价）

```ts
import type { NextConfig } from "next";

const MARKETING =
  process.env.FINALROUND_MARKETING_ORIGIN ?? "https://finalround.vercel.app";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      { source: "/marketing", destination: `${MARKETING}/marketing` },
      { source: "/marketing/:path*", destination: `${MARKETING}/marketing/:path*` },
      // 若采用 §3.1 的 _next 转发且不与主站冲突：
      { source: "/_next/:path*", destination: `${MARKETING}/_next/:path*` },
    ];
  },
};

export default nextConfig;
```

Vercel 对外部 `destination` 规则见官方文档：[Project Configuration — Rewrites](https://vercel.com/docs/projects/project-configuration#rewrites)。

---

## 4. 模式 B：同一前缀下「父路径主站、子路径子站」

适用于：**`/<segment>` 根路径** 由主应用渲染（hub），**`/<segment>/topic-a`** 等由营销子站渲染。

**易错点**：若写 **`/marketing/:path*`** 且平台里 `:path*` 含 **零段**，可能把 **`/marketing` 本身**也转发到子站，与产品要求冲突。

**推荐**：

- **逐条**列出已上线子路径；或  
- 使用平台支持的 **「至少一段」** 语法（如 `:path+`、正则），并在预发验证 **`/marketing` 仍由主站 200**。

**规则顺序**：更具体的 `source` 排在宽泛规则之前，避免被主站其它 catch-all 吞掉。

```ts
const MARKETING =
  process.env.FINALROUND_MARKETING_ORIGIN ?? "https://finalround.vercel.app";

async rewrites() {
  return [
    {
      source: "/marketing/topic-a",
      destination: `${MARKETING}/marketing/topic-a`,
    },
    // 若 next / 网关支持「至少一段」：
    // { source: "/marketing/:path+", destination: `${MARKETING}/marketing/:path+` },
  ];
}
```

多语言与 **「英文一条、各 locale 平行一条」** 的 rewrites 写法见 **§6**。

---

## 5. 主域路径与子站路径不一致时（网关映射）

若对外是 **`/foo`**，子站只实现了 **`/bar`**，在 **同一层** rewrites 做映射（不必先改子站），示例：

```json
{
  "rewrites": [
    { "source": "/foo", "destination": "https://finalround.vercel.app/bar" },
    { "source": "/foo/:path*", "destination": "https://finalround.vercel.app/bar/:path*" }
  ]
}
```

单复数、对外别名等：在网关 **逐条映射** `source` → `destination`，与子站真实路由对齐，并在预发抽测所有对外 URL。

---

## 6. 多语言前缀（若主站有 `/<locale>/...`）

代理须 **原样保留** locale 段：例如主域 `/fr/marketing/...` → 子站 **`https://finalround.vercel.app/fr/marketing/...`**。**不要**剥掉 `/fr` 再指望子站猜语言。子站 **必须先存在** 对应 App Router（如 `app/[locale]/...`）再配主域规则。英文与每种语言 **平行加一组** rewrites（或与英文逐条对齐，更安全）。各语言页仍请求 **`/_next/static/...`**（通常 **不带** locale 前缀）；若主域已为营销页配置 `/_next` 转发，各 locale 一般 **共用** 同一组 `/_next` 规则——若尚未配置，会出现能打开页面但无样式，需与 **§7** 一并处理。

---

## 7. `/_next` 与「主站也是 Next」的冲突

- 营销页会请求 **`/_next/static/...`**（及 RSC 相关请求）。**只转业务路径、不转 `/_next`** → 常见 **无样式 / 控制台大量 404**。  
- **主站与子站两套 Next 共用主域根上的 `/_next`** 时，**不能**简单把全局 `/_next` 指到子站，否则会打断主站自身资源加载。  
- **可行方向**：① 营销用 **独立子域** 直连子站托管（无冲突）；② 主站 **非 Next** 或 `/_next` 可由子站独占时，再配 **`/_next` → 子站 origin**；③ **Monorepo 单构建**（超出本文，需架构决策）。

---

## 8. Cloudflare（思路）

- 在 Worker / Snippet 里按 **`url.pathname`** 匹配 `/<segment>` 前缀，`fetch("https://finalround.vercel.app" + pathname + search)`（或与 `FINALROUND_MARKETING_ORIGIN` 一致）返回 **Response**；注意 **上游 `Host` / SNI** 与 **`finalround.vercel.app`** 证书一致，必要时设置 **`X-Forwarded-Host` / `X-Forwarded-Proto`**。  
- HTML 与静态资源 **缓存策略分开**；发版后按需 **Purge** 或短 TTL。  
- 与 **Vercel `rewrites`** 不要重复配置导致 **双跳** 或环，由团队定「只保留一层」。

---

## 9. Nginx（思路）

```nginx
# 反向代理到 Vercel 子站：Host / SNI 与 finalround.vercel.app 证书一致
location /marketing/ {
    proxy_pass https://finalround.vercel.app/;
    proxy_ssl_server_name on;
    proxy_set_header Host finalround.vercel.app;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

路径尾部 **`/`** 与 `proxy_pass` 拼接行为以 Nginx 文档为准；生产配置需与运维评审。

---

## 10. 子站 Next 侧（与转发配套）

- **`FINALROUND_MARKETING_ORIGIN`**：主站 rewrites 的 destination 基址；生产建议 **`https://finalround.vercel.app`**（与 Vercel 子站项目一致）。  
- **`NEXT_PUBLIC_SITE_URL=https://www.finalroundai.com`**：子站生成绝对链接、`metadataBase`、canonical、sitemap 时用 **主域**；**不要**把对外链接写死为 `finalround.vercel.app`（用户经主域 Rewrite 访问时应感知主域）。  
- 子站路由目录须与主域 **最终 pathname** 一致（除非仅由网关改写路径，则按 §5 维护映射表）。

---

## 11. 验证（前端自测）

1. 无痕：主域下 **`/marketing`（替换后）** 与子页，地址栏仍为 **www.finalroundai.com**（若未采用子域方案）。  
2. Network：**文档 + `/_next/static/*`（及按需的 RSC）** 为 **200**，无大面积 404。  
3. 直接打开 **https://finalround.vercel.app** 下同路径，与主域 **HTML 与关键 chunk 名** 一致。  
4. 若存在 **模式 B**：确认 **仅 hub** 由主站响应、子路径进子站。  
5. 多语言：抽测 **`/fr/...`** 等是否与预期 locale 内容一致。

---

## 12. 必记三件事（摘要）

1. **`/_next`**：与主站 Next 冲突时 **不要用全局 `/_next` 指子站`**，改子域或架构方案。  
2. **SEO**：`NEXT_PUBLIC_SITE_URL`、`metadataBase` / canonical 指向 **正式主域**。  
3. **发布**：子站可独立部署；**新增顶层 `<segment>` 或改网关规则** 时再走主站/基建发版节奏；尽量 **`/<segment>/:path*`** 减少改表次数。

---

*实路径表与 [finalround-site-structure.md](../finalround-site-structure.md) 同步；品牌见 [finalround-brand-visual.md](../finalround-brand-visual.md)。Last updated: 2026-04-15*
