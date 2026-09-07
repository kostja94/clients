# Frontier Rounds — 从「AI Funding Hub」到 Next.js + Cloudflare 的完整构建与部署方案

> 记录日期：2026-09-07 ｜ 适用源码：`E:\自有部署项目\AI Funding Hub` ｜ 目标域名：frontierrounds.com
> 目标代码目录：`E:\自有部署项目\frontierrounds`（新建，不动原仓，保留 Lovable git 历史）
> 目标部署：**Cloudflare Workers**（替代原 Vercel 习惯）
>
> ✅ **执行状态：阶段 A（重构）与阶段 B（部署）均已完成并上线**（2026-09-07）。本文为执行蓝图；实际链路与踩坑以 `README.md`「执行进度/部署链路备忘」为准。

---

## 0. 结论先行（TL;DR）

1. **重构**：把 TanStack Start + Vite 项目改写为 **Next.js App Router** 项目；目录结构对齐 `nova-scientia-main` / `alignify production`（app/ 路由 + src/ 组件数据 + scripts/ 验证脚本 + CLAUDE.md）。
2. **样式**：保留 **Tailwind CSS v4**（CSS-first `@theme` + oklch），原 editorial 设计系统（Instrument Serif / Work Sans / ink-rule 纸张墨色）零重绘迁移。
3. **数据**：`fundingRounds.ts` / `fundingLeaderboard.ts` / `investors/*.ts` 原样搬运，无数据库；全部可静态生成 + 边缘缓存。
4. **图片**：实体 PNG 在 Lovable 云端，用回填脚本从 preview 域名批量下载到 `public/logos`、`public/portraits`。
5. **品牌**：全站 "AI Capital" → **Frontier Rounds**；替换残留 Lovable canonical；补齐 sitemap / robots / metadata。
6. **部署**：`@opennextjs/cloudflare`（OpenNext）打包为 Worker 部署到 Cloudflare，绑定 `frontierrounds.com`（apex + www）。`vinext` 为官方新实验路线，留备选。

**为什么默认 OpenNext 而非 vinext**：vinext（Cloudflare 2026 年新推，Vite 重写 Next.js 运行时）被官方标注 experimental，对成熟生产负载 CF 官方仍建议 OpenNext；OpenNext 与本方案"先成为标准 Next.js 项目"的前提完全兼容，回退/迁移成本最低。详见 §B1。

---

## 1. 现状盘点（AI Funding Hub）

### 1.1 技术栈（实测 package.json / 配置文件）

| 维度 | 现值 |
|---|---|
| 框架 | **TanStack Start**（`@tanstack/react-start`）+ **TanStack Router** 文件路由（`src/routes/*.tsx`） |
| 构建 | Vite 8（`@lovable.dev/vite-tanstack-config`，内含 nitro 以 cloudflare 为默认 target——但从未部署） |
| 渲染 | React 19.2，服务端入口 `src/server.ts` + `src/start.ts` |
| 样式 | Tailwind CSS v4（CSS-first）+ `tw-animate-css`；shadcn/ui 风格组件（Radix 全家桶已装） |
| 数据/图表 | recharts（FundingScaleChart）、date-fns、TanStack Query（有 Provider 但**实际未使用**） |
| 内容 | 全部硬编码 TS（无 CMS / 无数据库 / 无远程 API） |
| 包管理 | bun（`bun.lock`、`bunfig.toml`）；package name `tanstack_start_ts` |
| Git | 连接 Lovable（AGENTS.md 标注勿改写已推送历史） |

### 1.2 页面清单（TanStack 路由 → 语义）

| 现有路由 | 页面 | 备注 |
|---|---|---|
| `src/routes/__root.tsx` | 根布局（Head/Scripts/QueryClient/404/Error） | `head()` 里含全站 title/desc/fonts/favicon |
| `src/routes/index.tsx` | **Latest Rounds** 首页 | LeadStory + StatStrip + FundingTable |
| `src/routes/leaderboard.tsx` | **Funding Leaderboard** 排行榜 | ItemList + FAQPage JSON-LD；⚠️ canonical 残留 Lovable preview URL |
| `src/routes/investors.tsx`（5 行） | investors 段布局（Outlet） | |
| `src/routes/investors.index.tsx` | **Investor Atlas** 目录页 | 按 firm / accelerator / person 分组 |
| `src/routes/investors.$slug.tsx` | 单家机构档案（动态） | loader 查 `getInvestorProfile(slug)`，notFound 兜底；含头像/纹章/portfolio 表 |
| `src/routeTree.gen.ts` 等 | TanStack 生成物 | 迁移后删除 |

### 1.3 数据资产（全部纯 TS，可整包平移）

- `src/data/fundingRounds.ts` — 25 条近期轮次 + `formatUsd/formatDate/getStats/leadStory` 工具。
- `src/data/fundingLeaderboard.ts` — ~30 家公司的融资总量/最大单轮/估值/领投/来源与 tier（Disclosed/Reported/Estimated）+ 排序/统计工具。条目含真实外链 sourceUrl（保留）。
- `src/data/investors/` — `types.ts` + `profiles.ts`（注册表）+ 12 份档案（Sequoia、a16z、Peak XV、YC、MiraclePlus、Hongshan、Shunwei、Lollapalooza、Elad Gil、Naval、Nat Friedman…）+ 大量 `*Logos.ts`（logo 导入映射）+ `investorTypes.ts`（机构分类枚举与摘要）。
- ⚠️ 内容为 2026-08 前后示例/演示数据，部分条目（如 Helion Labs、Mistral Forge 等）疑似虚构占位。**上线前须逐条校验**（详见 §5）。

### 1.4 组件（迁移可复用，仅换路由 import）

`SiteHeader`/`SiteNav`/`SiteFooter`/`LeadStory`/`StatStrip`/`FundingTable`/`leaderboard/{CriteriaGrid,FundingScaleChart,LeaderboardTable,MethodNote}` + `ui/*`（shadcn 系，~45 个，多为 Lovable 预生成标准件）。站点级定制在 `SiteHeader`（品牌字标 "AI Capital"）与首页区块。

### 1.5 图片资产机制（关键风险点，已实测）

- `src/assets/` 下 ~250 个 logo/肖像文件。但**绝大多数是 `*.png.asset.json` 清单而非实体图**，例如：

```json
{ "version": 1, "asset_id": "379d46c3-…", "project_id": "1e49e127-…",
  "url": "/__l5e/assets-v1/379d46c3-…/openai.png", "r2_key": "a/v1/…", "original_filename": "openai.png", … }
```

- 组件引用方式是 `import azOpenai from "@/assets/logos/openai.png.asset.json"` 再取 `.url`；少数几个是真 PNG（`cerebras.png`、`groq.png`、`scale-ai.png`、`physical-intelligence.png`、`safe-superintelligence.png`、`elad.jpg` 等）直接 import。
- **实体图可回填**（已实测 200 OK，Content-Type: image/png）：
  `https://id-preview--1e49e127-78ec-480f-9a11-53fbb3437103.lovable.app/__l5e/assets-v1/{asset_id}/{original_filename}`
- 迁移动作：写脚本遍历全部 `*.png.asset.json` → 下载到 `public/logos/`（及 `public/portraits/`）→ 把各 `*Logos.ts` / profile 里的 `xxx.url` 引用改为 `/logos/原文件名` 字符串常量（见 §A4）。

### 1.6 品牌与 SEO 现状（重构必须处理）

- 品牌词现为 **"AI Capital — Global AI Startup Funding Tracker"**（`__root.tsx`、`index.tsx`、`SiteHeader`、investors 页 title 均含），迁移期整体改为 **Frontier Rounds**。
- `leaderboard.tsx` 中 `CANONICAL_URL` 硬编码为 `https://id-preview--…lovable.app/leaderboard`（Lovable 预览域名）——**上线前必须替换为 `https://frontierrounds.com/leaderboard`**。
- 只有 `public/robots.txt` 与 `favicon.ico`；**无 sitemap、无 OG 图、无 RSS**。App Router 版将用 `app/sitemap.ts` + `app/robots.ts` 补齐。

---

## 2. 目标架构（对齐参考项目）

```
E:\自有部署项目\frontierrounds            ← 新源码仓（git init，独立历史）
├─ app/                                   ← App Router
│  ├─ layout.tsx                          （根布局 + 字体 + metadata + 视口）
│  ├─ page.tsx                            （/ Latest Rounds 首页）
│  ├─ globals.css                         （原 styles.css 改写 @source 指向）
│  ├─ sitemap.ts
│  ├─ robots.ts
│  ├─ error.tsx                           （原 errorComponent）
│  ├─ not-found.tsx                       （原 NotFoundComponent）
│  ├─ leaderboard/
│  │  └─ page.tsx
│  └─ investors/
│     ├─ layout.tsx
│     ├─ page.tsx                         （Investor Atlas）
│     └─ [slug]/
│        └─ page.tsx                      （+ generateStaticParams / notFound / generateMetadata）
├─ src/
│  ├─ components/                         （原样迁移；TanStack <Link> → next/link）
│  │  ├─ ui/…                             （shadcn 预生成件，原样）
│  │  ├─ FundingTable.tsx  LeadStory.tsx  StatStrip.tsx  SiteHeader.tsx  SiteNav.tsx  SiteFooter.tsx
│  │  └─ leaderboard/…
│  ├─ data/                               （TS 硬编码数据，原样）
│  │  ├─ fundingRounds.ts  fundingLeaderboard.ts  investorTypes.ts
│  │  └─ investors/…
│  └─ lib/  utils.ts                       （cn 等）
├─ public/
│  ├─ logos/  portraits/  favicon.ico     （回填下载 + 真图复制）
├─ scripts/
│  ├─ download-lovable-assets.mjs          （图片回填，§A4）
│  └─ validate-data.mjs                    （可选：校验 slug 唯一/外链格式）
├─ next.config.ts
├─ tsconfig.json                           （paths @/* → ./src/*）
├─ postcss.config.mjs                      （@tailwindcss/postcss）
├─ components.json
├─ package.json
├─ wrangler.jsonc                          （§B3，Cloudflare Worker 配置）
├─ open-next.config.ts                     （§B3）
├─ .gitignore  .env.example  README.md  CLAUDE.md
```

约定：页面壳组件放 `app/`，业务组件/数据放 `src/`（对齐 nova-scientia 与 alignify 的拆分习惯）；`CLAUDE.md` 记录命令与编辑安全规则（对齐既有项目惯例）。

---

## 3. 阶段 A：重构为 Next.js

### A0 准备与备份

1. 保留原目录 `E:\自有部署项目\AI Funding Hub` 不动（其 git 连接 Lovable，勿改写历史）。
2. 确认可访问 preview 图片源（§1.5 URL）；若 Lovable 项目被删则此源失效，需先在 Lovable 编辑器内下载资源。
3. 建新仓：
```bash
mkdir "E:\自有部署项目\frontierrounds" && cd "E:\自有部署项目\frontierrounds"
git init
```
4. 从 AI Funding Hub 拷贝非生成物到暂存区，再按 A2 落位。

### A1 脚手架与依赖

不跑 `create-next-app` 模板（避免带入不需要的 boilerplate），按参考项目手工搭最小 App Router：

`package.json` 要点（版本对齐已部署参考项目；React 19 与 Tailwind v4 均兼容）：

```jsonc
{
  "name": "frontier-rounds",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint .",
    "preview": "opennextjs-cloudflare build && opennextjs-cloudflare preview",   // §B
    "deploy": "opennextjs-cloudflare build && opennextjs-cloudflare deploy",     // §B
    "assets:fetch": "node scripts/download-lovable-assets.mjs",                 // §A4
    "cf-typegen": "wrangler types --env-interface CloudflareEnv cloudflare-env.d.ts"
  },
  "dependencies": {
    "next": "^16.3.0",
    "react": "^19.2.8",
    "react-dom": "^19.2.8",
    "tailwindcss": "^4.2.0",
    "@tailwindcss/postcss": "^4.2.0",
    "lucide-react": "^0.575.0",
    "recharts": "^2.15.4",
    "date-fns": "^4.1.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "tailwind-merge": "^3.5.0",
    "tw-animate-css": "^1.3.4",
    "@radix-ui/react-*": "…原项目保留实际用到的即可"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^22",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "16.3.3",
    "wrangler": "^4",
    "@opennextjs/cloudflare": "latest",
    "tsx": "^4"
  }
}
```

要点：
- **依赖裁剪**：删除 `@tanstack/react-router`、`@tanstack/react-start`、`@tanstack/router-plugin`、`@tanstack/react-query`（无实际查询调用）、`vite*`、`@vitejs/plugin-*`、`nitro`、`@lovable.dev/*`、`bun` 相关。Radix 组件按「实际 import 到的」保留（可先用全量，构建后再删未用项，但会拖慢构建——建议按 `ui/*` 实际引用裁剪）。
- 复制原 `tsconfig.json`，改为 Next 标准（保留 `@/*` → `./src/*` 别名），删除 `vite/client` types。
- Tailwind v4 不再需要 `tailwind.config.ts`；`postcss.config.mjs`：
```js
export default { plugins: { "@tailwindcss/postcss": {} } };
```

### A2 文件迁移映射表（全量）

| 原文件（AI Funding Hub） | 目标（frontierrounds） | 处理 |
|---|---|---|
| `src/styles.css` | `app/globals.css` | `@source "../src"` → `@source "../"`；其余原样 |
| `src/routes/__root.tsx` | `app/layout.tsx` + `app/not-found.tsx` + `app/error.tsx` | 拆分并改写（A3） |
| `src/routes/index.tsx` | `app/page.tsx` | head → `generateMetadata`/layout |
| `src/routes/leaderboard.tsx` | `app/leaderboard/page.tsx` | 同上；canonical 换域名 |
| `src/routes/investors.tsx` | `app/investors/layout.tsx` | Outlet → `children` |
| `src/routes/investors.index.tsx` | `app/investors/page.tsx` | head → metadata |
| `src/routes/investors.$slug.tsx` | `app/investors/[slug]/page.tsx` | loader → Server Component 取值 / generateStaticParams；notFound() |
| `src/router.tsx`、`src/server.ts`、`src/start.ts`、`src/routeTree.gen.ts` | 删除 | TanStack 运行时代码 |
| `src/components/**` | `src/components/**` | 原样；仅 TanStack `<Link>`/`activeProps` → Next `<Link>`/`usePathname`（A3） |
| `src/data/**` | `src/data/**` | 原样 |
| `src/lib/utils.ts` | `src/lib/utils.ts` | 原样 |
| `src/lib/error-capture.ts`、`lovable-error-reporting.ts` | 删除 | Lovable 上报专用 |
| `src/hooks/use-mobile.tsx` | `src/hooks/use-mobile.tsx` | 原样 |
| `src/assets/*.asset.json` | `public/logos`、`public/portraits`（经 A4 脚本） | 下载实体图 |
| `public/favicon.ico` | `public/favicon.ico` | 复制（可后续换 FR 字标） |
| `public/robots.txt` | 删除，由 `app/robots.ts` 生成 | 见 A6 |
| `src/styles.css` 中 Google Fonts link | `app/layout.tsx` 用 `next/font/google` 或保留 `<link>` | 建议 next/font（自托管，CWV 更稳） |
| `.gitignore`/`README.md`/`CLAUDE.md`/`components.json` | 新建 | 对齐参考项目 |

### A3 路由语义改写对照（TanStack → App Router）

| TanStack Start 写法 | Next.js App Router 等价 |
|---|---|
| `export const Route = createFileRoute("/x")({ component, head, loader })` | 默认导出页面组件 + `export const metadata`（静态）或 `generateMetadata()`（动态） |
| `Route.useLoaderData()` | Server Component 直接 `await` / 顶层取数 |
| `head: () => ({ meta: […], links: […] })` | `metadata` / `viewport` / `generateMetadata`（title/description/OG/Twitter/canonical） |
| `Link to="/investors/$slug" params={{slug}}` | `Link href={/investors/${slug}}`；`activeProps` → 用 `usePathname()` 判 active |
| `Outlet` | `{children}`（layout.tsx） |
| `throw notFound()` / `notFoundComponent` | `notFound()` + `app/not-found.tsx` |
| `errorComponent` | `app/error.tsx`（'use client'） |
| `<HeadContent/> <Scripts/>` | 无（Next 托管）；根布局 `<html lang="en"><body>` |
| `QueryClientProvider` | 删除（无远程数据）；图表等纯客户端组件加 `"use client"` |
| 字体 `<link>` | `next/font/google`（Instrument Serif + Work Sans） |
| `scripts`（dangerouslySetInnerHTML JSON-LD） | 保留在页面组件内；或改 `<script type="application/ld+json">` 于 Server Component |

注意：
- 需要交互/浏览器 API 的组件（如可能用 recharts 的 `FundingScaleChart`、日历/弹窗类 ui 组件、面包屑 active 态）文件顶部加 `"use client"`；纯展示组件保持 Server Component。
- `SiteHeader` 的导航 active 态：把 `activeProps` 改为 `usePathname()` 比较，或直接简化为 hover 样式（信息架构稳定，差异小）。
- `next.config.ts`：`output` 默认（Node → 由 OpenNext 转换）；`images.remotePatterns` 如后续引入远程 OG 图再配。

### A4 图片回填脚本（`scripts/download-lovable-assets.mjs`）

在**新仓内**执行一次，遍历 `AI Funding Hub/src/assets` 的 `*.asset.json`：

```js
// scripts/download-lovable-assets.mjs  （在 E:\自有部署项目\frontierrounds 下运行）
// 用法: node scripts/download-lovable-assets.mjs <SOURCE_ROOT>
import { readdirSync, readFileSync, mkdirSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";

const SOURCE = process.argv[2] ?? "E:/自有部署项目/AI Funding Hub/src/assets";
const PREVIEW_HOST = "https://id-preview--1e49e127-78ec-480f-9a11-53fbb3437103.lovable.app";
const OUT = "public"; // logos -> public/logos, portraits -> public/portraits

function walk(dir, acc = []) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) walk(p, acc); else acc.push(p);
  }
  return acc;
}

const seen = new Map(); // filename -> source path (conflict guard)
for (const file of walk(SOURCE).filter((f) => f.endsWith(".asset.json"))) {
  const m = JSON.parse(readFileSync(file, "utf8"));
  if (!m.asset_id || !m.original_filename) continue;
  const name = m.original_filename;
  if (seen.has(name)) { console.warn("⚠️ 冲突:", name, file, "vs", seen.get(name)); continue; }
  seen.set(name, file);
  const sub = name.match(/\.(jpe?g|png|webp|gif)$/i) ? "logos" : "logos"; // jpg 名人肖像也可另分
  const dest = join(OUT, sub, name);
  mkdirSync(dirname(dest), { recursive: true });
  const res = await fetch(`${PREVIEW_HOST}/__l5e/assets-v1/${m.asset_id}/${encodeURIComponent(name)}`);
  if (!res.ok) { console.error("❌", res.status, name); continue; }
  writeFileSync(dest, Buffer.from(await res.arrayBuffer()));
  console.log("✅", dest, res.headers.get("content-length"));
}
```

（Node ≥18 自带 fetch；如个别文件名重复，手动改名并同步 `*Logos.ts`。）

随后改造引用：把每个 `*Logos.ts` 中的
`import azOpenai from "@/assets/logos/openai.png.asset.json"; … azOpenai.url`
替换为指向 public 的常量，例如：

```ts
export const leaderboardLogos: Record<string, string | undefined> = {
  openai: "/logos/openai.png",
  anthropic: "/logos/anthropic.png",
  // …逐一对应 original_filename
  cerebras: "/logos/cerebras.png",   // 原本就是真 png，直接复制到 public/logos 即可
};
```

本地真 png/jpg（cerebras/groq/scale-ai/physical-intelligence/safe-superintelligence + 三张名人肖像 jpg）直接 `Copy-Item` 到 `public/logos`、`public/portraits`，肖像引用在 `investors/*.ts`（eladGil/navalRavikant/natFriedman 的 `portrait` 字段）。

### A5 品牌换标：AI Capital → Frontier Rounds

替换点清单（全局 grep `AI Capital` / `ai-capital` / `aicapital`）：

| 位置 | 现值 | 改为 |
|---|---|---|
| 根布局 title | `AI Capital — Global AI Startup Funding Tracker` | `Frontier Rounds — AI Funding Intelligence` |
| 根布局 description | “Daily funding intelligence on AI startups worldwide…” | 精炼重写（见 A6） |
| `SiteHeader` 字标 | AI Capital | **Frontier Rounds**（两词首字母大写，DOM 内规范写法） |
| `SiteHeader` 副标 | — Global funding intelligence for AI | 保留/改措辞 |
| 首页 / leaderboard / investors 页 title | …\| AI Capital | …\| Frontier Rounds |
| leaderboard `CANONICAL_URL` | `https://id-preview--….lovable.app/leaderboard` | `https://frontierrounds.com/leaderboard` |
| `notFound`/`error` 提示文案 | 中性文案 | 保持中性 |

Tagline 候选（首屏/页脚可用）：`The money fueling frontier AI.` / `Capital at the frontier of intelligence.`

### A6 SEO 与元数据就位

- 根 `layout.tsx`：`metadata`（title.template `%s | Frontier Rounds`、description、OG/Twitter、canonical 由各页显式给）、`viewport`、`icons`；`generateMetadata` 于动态页。
- `app/sitemap.ts`：枚举静态页 + `generateStaticParams` 全部 investor slug + 未来文章，`lastModified` 用数据里最新日期；`alternates.canonical` 指向 `https://frontierrounds.com`。
- `app/robots.ts`：`allow all`，`sitemap` 指向 `https://frontierrounds.com/sitemap.xml`；可仿 alignify 对 `/_next/static` 不加限制（Next 默认资源已有不可猜 token；可选加 `X-Robots-Tag`）。
- `app/not-found.tsx` 返回 404 并 `noindex`；`error.tsx` 为客户端边界。
- JSON-LD（leaderboard ItemList + FAQPage、后续公司页 Article/Organization）保留并移到 Server Component。
- 可选项：AI 代理发现响应头 `Link: </sitemap.xml>; rel="sitemap"`（仿 alignify next.config headers）。
- OG 图：上线后做一张 1200×630（FR 字标 + 报头风），每页给 `og:image`。

### A7 本地构建验证

```bash
cd "E:\自有部署项目\frontierrounds"
npm install
node scripts/download-lovable-assets.mjs          # 回填图片
npm run dev                                        # 冒烟：/、/leaderboard、/investors、/investors/sequoia-capital
npm run build                                      # 必须 0 error；留意：图片 alt、next/link 传参、use client 遗漏
npm run start
```

常见坑：
1. 全站图片 `<img>` 直接可用（public 静态图）；若改用 `next/image`，本地 public 图无需 remotePatterns；`sharp` 由 Next 自动安装。
2. `generateStaticParams` 需覆盖 `investors/profiles.ts` 全部 slug（含 firm/accelerator/person 三类）。
3. Tailwind v4 `@source` 需包含 `app/` 与 `src/`，否则样式缺失。
4. 任何用 `useState/useEffect/usePathname` 的组件文件加 `"use client"`，否则构建报 “async/use client” 错。
5. ESLint 用 `eslint-config-next`，`next lint` 在新版独立执行（对齐 alignify 注记）。

---

## 4. 阶段 B：Cloudflare 部署（frontierrounds.com）

### B1 部署技术选型对比

| 路线 | 说明 | 取舍 |
|---|---|---|
| **A. OpenNext `@opennextjs/cloudflare`**（默认 ✅） | Next 标准构建 → 转译为 CF Workers（.open-next/worker.js + assets） | 成熟稳定、文档全、保留 App Router/ISR/next/image 生态；构建稍慢 |
| B. **vinext**（官方新路线，实验） | CF 官方 Vite 重写 Next API；`npx vinext init` + `deploy` | 构建快/体积小；但标注 experimental，生产负载官方仍建议 OpenNext；**待成熟后再评估切换** |
| C. 纯静态导出 `output:"export"` | 全站静态 HTML 扔 CF Pages | 最省；但放弃 SSR/ISR/RSC 运行时与将来动态能力，本内容站短期可行但成长受限；不作为默认 |

结论：**A**。它与阶段 A 产出的"标准 Next 项目"零冲突，未来可平滑评估 B。

### B2 前置条件

1. Cloudflare 账号；安装 `wrangler`（随 devDependencies 已装），`npx wrangler login` 或设 `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`。
2. **域名接入**：把 `frontierrounds.com` 的 nameserver 改为 Cloudflare 分配的 NS（Dashboard → Add site）。若已在 Cloudflare 注册/托管则跳过。等待 `Active` 后（通常分钟级～24h），后续 Worker 自定义域才可自动签证书。

### B3 适配器配置（三个文件）

`open-next.config.ts`：
```ts
import { defineCloudflareConfig } from "@opennextjs/cloudflare";
export default defineCloudflareConfig();
```

`wrangler.jsonc`：
```jsonc
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "frontier-rounds",
  "main": ".open-next/worker.js",
  "compatibility_date": "2024-09-23",
  "compatibility_flags": ["nodejs_compat"],
  "assets": {
    "directory": ".open-next/assets",
    "binding": "ASSETS"
  },
  "observability": { "enabled": true },
  "vars": { }
}
```

package.json 已含：
```jsonc
"build": "next build",
"preview": "opennextjs-cloudflare build && opennextjs-cloudflare preview",
"deploy": "opennextjs-cloudflare build && opennextjs-cloudflare deploy",
"cf-typegen": "wrangler types --env-interface CloudflareEnv cloudflare-env.d.ts"
```

站点 URL 常量：`next.config.ts` 内 `env: { NEXT_PUBLIC_SITE_URL: "https://frontierrounds.com" }`（sitemap/metadata/canonical 使用；build 期注入）。

### B4 本地预览（Workers 运行时）

```bash
npm run build
npm run preview      # 本地 Workers runtime 起服务，验证 SSR/ISR 行为与静态构建一致
```

### B5 首次部署 + 自定义域名

```bash
npm run deploy       # = opennextjs-cloudflare build && opennextjs-cloudflare deploy
```
- 首次会生成 `*.workers.dev` 子域（如 `frontier-rounds.<子域>.workers.dev`），先在此验证。
- 绑定域名（二选一）：
  - Dashboard：Workers → frontier-rounds → Settings → Domains & Routes → Add → `frontierrounds.com` + `www.frontierrounds.com`（自动 DNS + 证书）。
  - 或 `wrangler.jsonc` 配 `routes`/`custom_domains` 后重新 deploy：
```jsonc
"custom_domains": [
  { "name": "frontierrounds.com" },
  { "name": "www.frontierrounds.com" }
]
```
- 建议 apex 为主、www 301 → apex（在 Worker 内或规则里处理一次跳转）。

### B6 CI/CD（可选但推荐）

`.github/workflows/deploy.yml`：
```yaml
name: Deploy Frontier Rounds
on:
  push: { branches: [main] }
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run deploy
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          CLOUDFLARE_ACCOUNT_ID: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
```
CF token 权限：Workers Scripts → Edit；Account ID 从 Dashboard 取。另可开 CF Workers Builds（连 git 仓，Build command `npm run build`、Deploy command `npm run deploy`）。

### B7 上线验收清单

| # | 项 | 验收方法 |
|---|---|---|
| 1 | apex + www HTTPS | `curl -I https://frontierrounds.com` 200；证书有效 |
| 2 | www → apex | 301 单跳无环 |
| 3 | `/sitemap.xml` | 含全部静态页 + 全部 investor slug |
| 4 | `/robots.txt` | allow + sitemap 声明 |
| 5 | 关键页 meta | `/`、`/leaderboard`、`/investors`、`/investors/{slug}` title/description/canonical=frontierrounds.com |
| 6 | 旧 canonical 残留 | 全仓 grep `lovable.app` = 0 |
| 7 | JSON-LD | leaderboard ItemList/FAQPage 通过 Rich Results 校验 |
| 8 | 图片 | `public/logos` 引用全部 200，无 broken img；alt 齐 |
| 9 | 品牌一致性 | 全站无 "AI Capital" 残留（favicon 如需换 FR 字标） |
| 10 | 性能 | Lighthouse ≥90（移动端 LCP），边缘缓存生效（响应头 cache hit） |
| 11 | 分析 | GA4/Clarity 挂载；GSC 添加属性并提交 sitemap |
| 12 | 404/错误页 | 访问不存在的 investor slug 返回 404 页面 |
| 13 | ISR/更新机制 | 内容改动重新 `npm run deploy` 即上线（纯静态数据，无需 DB） |

### B8 备选路线备注

- **vinext**（官方推荐向）：待生产可用后执行 `npx vinext init --platform=cloudflare` 自动迁移（保留 app/、next.config），然后 `npx @vinext/cloudflare deploy`。迁移脚本非破坏，`next build` 仍可用。
- **静态导出**：若最终仅保留三五个静态页 + 数据表，可切 `output:"export"` 用 CF Pages 免费静态托管；代价是放弃 RSC/ISR 演进空间，长期不推荐。

---

## 5. 风险与待办

| 风险/待办 | 影响 | 处置 |
|---|---|---|
| 部分榜单/轮次数据疑似演示占位（Helion Labs、Mistral Forge 等非真实公司） | 上线后事实性风险，动摇 "sourced & tagged" 卖点 | 上线前逐条校验；`tier: Reported/Estimated` 缺 sourceUrl 的补齐或删除；立 `validate-data` 脚本 |
| `.png.asset.json` 若 Lovable 项目失效则无法回填 | 图片丢失 | 尽快执行 A4；事后图片全部本地化，无外部依赖 |
| `asset.json` 指向的真实外链（sourceUrl）与 future 文章链接 | SEO 资产 | 保留并规范化（https、无追踪参数） |
| 真 png 与清单同名冲突 | 脚本冲突告警 | 冲突时以清单优先，手动改名真图并同步引用 |
| 品牌关键词竞争（Frontier Rounds 无同名媒体，见调研） | 低 | 域名已购 + 无撞名；上线后靠内容与 GSC 建立 |
| Cloudflare 免费层限制 | 低 | 静态+边缘缓存免费层足够；观察请求量，超限再上 Pro |

---

## 6. 参考链接

- Cloudflare OpenNext 适配器文档：https://developers.cloudflare.com/workers/framework-guides/web-apps/opennext/
- OpenNext Cloudflare 快速开始：https://opennext.js.org/cloudflare/get-started
- Cloudflare Next.js（vinext 新路线）：https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/ ｜ https://github.com/cloudflare/vinext
- 参考项目：`E:\自有部署项目\nova-scientia-main`、`E:\自有部署项目\alignify production`、`E:\客户部署项目\medo-blog`

---

*本方案为执行蓝图；每阶段完成即在本仓 README 勾选状态。最后更新：2026-09-07*
