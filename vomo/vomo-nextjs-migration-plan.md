# VOMO — 部分页面从 Lovable (TanStack Start) 迁移到 Next.js 的完整方案

> 记录日期：2026-09-11 ｜ 源项目：Lovable `vomo-ai`（`965859ba-5107-46f4-b636-7aecf6a27cad`）
> 源文件仓：Lovable 云端（只读，勿改写其 git 历史）
> 目标代码目录：`E:\客户部署项目\vomo-seo`（新建，独立 git 历史）
> 目标部署：**Vercel**（与 `today-seo-main` / `medo-blog` / `sparki-blog` 一致的既有链路）
> 挂载方式：**根路径、无 basePath**，先上 `*.vercel.app`，再由主站按路径白名单反代
> 数据策略：**一次性导出、之后完全脱离 Supabase**（纯 SSG）
> **硬约束：不改内容。** 文案、slug、URL、区块结构逐字保持一致；只换框架与数据装载方式。
>
> ✅ **执行状态：主体迁移已完成**（2026-09-11）。目标仓 `E:\客户部署项目\vomo-seo`（commit `b06f356`）。
> 构建产出 75 个静态预渲染页；`71/71` 路由返回 200、`635` 条内容断言通过；
> 与源站比对 **1271 条文案单元 0 缺失**，其中 1119 条由「客户端 react-query 拉取」改为「服务端渲染」。
> Supabase 凭据无需你提供 —— 已从源站公开前端 bundle 读取并完成一次性导出（477 行）。
> 与主站反代相关的部分（§4 的 B2/B3）按你的要求**暂不处理**，本仓以根路径独立部署为准。

---

## 0. 结论先行（TL;DR）

1. **范围**：`/podcast-transcription`（枢纽 + 13 详情）、`/tools/youtube-transcript`（枢纽 + 48 长尾）、3 个批量工具页、3 个 `/use-cases/*`、`/trending-youtube-video`、`/trending-podcast`，**合计 71 个 URL**。
2. **架构**：改写为 **Next.js 16 App Router + React 19 + Tailwind v4**；目录结构对齐 `today-seo-main`（`src/app` + `src/components` + `src/content` + `src/lib` + `scripts`）。
3. **内容分层（决定迁移方式）**：
   - **已是本地 JSON**（`heroes` / `faqs` / `how-it-works` / `use-cases` / `use-case-pages`）→ 逐字拷入新仓，零改动。
   - **只在 Supabase**（`platform_pages` / `site_features` / `site_ctas` / `site_collections`+`items`）→ **一次性导出为 JSON**，此后构建期只读本地文件。
4. **样式**：`src/styles.css` 的 `@theme`（`--color-vomo-*`、`--text-h1..eyebrow`）与 shadcn oklch 变量原样重建，**设计零重绘**。
5. **图片**：全部为**真实二进制**（无 `.asset.json` 清单），已实测可从已发布站 `https://vomo-ai.lovable.app/assets/<原名>-<hash>.<ext>` 回填，脚本剥离哈希后缀落 `public/images/`。
6. **必须修的现状缺陷**（属工程债，不属内容）：正文区块目前靠客户端 `useQuery` 拉取（SSR HTML 里没有正文）→ 全部改服务端取数；`RelatedPagesSection` 的 JSON-LD 硬编码 `https://vomo.ai` → 统一 `SITE_URL`。
7. **本次不做**：不迁移首页 / `/library` / `/blog` / `/changelog` / 日语工具页 / 其余 ~240 个 tools 页（另立阶段）；不建 i18n（Lovable 站为纯英文，无语言前缀）。

---

## 1. 现状盘点（源项目 Lovable `vomo-ai`）

### 1.1 技术栈（实测 `package.json`）

| 维度 | 现值 |
|---|---|
| 框架 | **TanStack Start** `^1.168.26` + TanStack Router `^1.170.16`（`src/routes/*.tsx` 文件路由） |
| 构建 | Vite `^8` + `@lovable.dev/vite-tanstack-config`（内含 nitro） |
| 渲染 | React `^19.2.0`，入口 `src/server.ts` + `src/start.ts` |
| 样式 | Tailwind v4（CSS-first `@theme`）+ `tw-animate-css` + shadcn/Radix |
| 数据 | `@supabase/supabase-js ^2.110.7`（anon/publishable key）+ `@tanstack/react-query ^5.101.1` |
| 其他 | `zod ^4.4.3`、`embla-carousel-react`（已装但未用，轮播为自研 `use-carousel`）、`@lovable.dev/mcp-js` |
| 包管理 | bun（`bun.lock`、`bunfig.toml`），package name `tanstack_start_ts` |
| 线上 | `https://vomo-ai.lovable.app`（已发布）｜预览 `https://id-preview--965859ba-…lovable.app`（**需鉴权，勿用于资产回填**） |

### 1.2 迁移范围与 URL 全量清单

`slug` 的**权威来源**是数据库 `platform_pages`（`published = true`），**没有静态枚举**，两张动态路由都在请求时按「单 slug → 单行」查询。

**① Podcast Transcription 簇（14 URL）**

| URL | 模板 | 说明 |
|---|---|---|
| `/podcast-transcription` | 枢纽页 | `TranscribeBox` + `CollectionSection(platforms)` + `FeatureSection` |
| `/podcast-transcription/{slug}` | `template='platform'` → `PlatformPage` | 10 条：`apple-podcast, spotify-podcast, youtube-podcast, castbox, amazon-music, iheartradio, podbean, overcast, pocket-casts, rss-feed` |
| `/podcast-transcription/{slug}` | `template='category'` → `CategoryPage` | 3 条：`true-crime, business, christian` |

> 这 3 个 category 页原本是静态路由文件（`podcast-transcription.true-crime.tsx` 等），后被删除改由动态路由承载，**URL 未变**。

**② YouTube Transcript 簇（49 URL）**

| URL | 说明 |
|---|---|
| `/tools/youtube-transcript` | 枢纽页（四条轴轮播） |
| `/tools/youtube-transcript/{slug}`（48 条，`template='youtube'`） | 按 `hero_tag` 分四条轴（详见下表） |

48 条 slug 按轴（**这是导航与轮播分组的唯一依据**）：

- `YouTube Category`（18）：`youtube-news, education, science, how-to, vlog, entertainment, interview, comedy, gaming, sports, music, film, animation, travel, car-review, event, pet-video, nonprofit`
- `YouTube Topic`（18）：`business-video, health, politics, religion, military, knowledge, technology, food, fitness, beauty, fashion, strategy-games, rpg-games, ai, programming, finance, software, psychology`
- `YouTube Sport`（4）：`football, basketball, mma, american-football`
- `YouTube Format`（8）：`ted-talk, shorts, live-stream, lecture, online-course, tutorial, webinar, no-captions`

> ⚠️ **legacy slug 必须原样保留**：`business-video`（非 `business`）、`youtube-news`（非 `news`）、`pet-video`（非 `pet`）已上线并被索引。改名要 301，本方案不改。
> ⚠️ `position` 列有重复值，排序必须 `position` 后加 tiebreaker（源码用 `position, breadcrumb_label`）。

**③ 批量工具页（3 URL，挂同一 hub）**

`/tools/bulk-youtube-transcript`、`/tools/youtube-channel-transcript`、`/tools/youtube-playlist-transcript`
（均为"静态页 + `BatchWorkbench`/`BatchCards`/`BatchModeCompare`"，其中 channel / playlist 页各有一段写死的 8 条 `DEMO` 视频数组）

**④ Use Cases（3 URL）** — `/use-cases/students`、`/use-cases/youtubers`、`/use-cases/medical-scribes`
（注意是 **`use-cases` 复数**，与真实 vomo.ai 的 `/use-case/*` 单数不同，保持原样）

**⑤ Trending（2 URL）** — `/trending-youtube-video`（DB 驱动）、`/trending-podcast`（纯静态）

**⑥ 明确排除**：`/tools/podcast-transcription/platform`（全 `{TOKEN}` 占位 wireframe + `noindex`，无数据、无价值，不迁）。

### 1.3 内容数据分层（迁移方式的分水岭）

| 区块 | 现数据源 | 迁移方式 |
|---|---|---|
| Hero（h1 / tag / body / 两个 stat） | **JSON `heroes.json`**（键 = 绝对路径） | 原样拷贝 |
| FAQ（可见 accordion，每页 6 条） | **JSON `faqs.json`**（键 = `route_key`） | 原样拷贝 |
| How it works（3 步） | **JSON `how-it-works.json`** | 原样拷贝 |
| "Who uses VOMO"（`section_key='use_cases'`） | **JSON `use-cases.json`**（`FeatureSection` 在该 section **禁用** DB 查询） | 原样拷贝 |
| 3 个 Use-case 页正文 | **JSON `use-case-pages.json`**（恰好 3 键） | 原样拷贝 |
| Why choose / Why transcribe / subtopic_1-3 / definition | **DB `site_features`** | 一次性导出 → JSON |
| Final CTA | **DB `site_ctas`**（每页有写死 fallback） | 一次性导出 → JSON |
| 播客枢纽的平台卡集合 | **DB `site_collections` + `site_collection_items`** | 一次性导出 → JSON |
| 页面行（seo / og / hero_tag / preview / upload / capabilities / theme / position） | **DB `platform_pages`** | 一次性导出 → JSON |
| Related pages"Explore related" | **DB `platform_pages`**（按模板分组） | 用导出数据在构建期算 |
| YouTube 四轴轮播 | **DB `platform_pages`** | 用导出数据在构建期算 |
| Trending YouTube | **DB `platform_pages`（`template='youtube'`）** 的 `preview.videos` 聚合 | 用导出数据在构建期算 |
| Trending Podcast | **静态 `podcast-covers.ts`** | 原样拷贝 |
| 输入框文案/预览池 | **静态 `transcribe-box-presets.ts`** | 原样拷贝 |

**关键陷阱（务必按此理解，否则内容会错）**

1. `platform_pages` 里 `h1 / hero_body / stat_left / stat_right / steps* / faq_fallback / usecases` 这些列**仍有值，但已废弃** —— 渲染一律走 JSON。导出时保留以备查，**实现时不得读取**。
2. `site_faqs` / `site_howtos` 两张表**已废弃**（组件不再查询），导出可直接 skip。
3. `site_features.section_key='use_cases'` 的 64 行**永远不会被读**（被 JSON 覆盖），导出无害但不生效。
4. `use-cases.json`（FeatureSection 的"Who uses"）与 **`use-case-pages.json`**（3 个 use-case 页）是**两份不同文件**，勿混。前者**缺** `/use-cases/youtubers`，但该页不渲染 use_cases 区块，无影响。
5. Use-case 页的 `FeatureSection sectionKey="definition"` 会命中 DB，但 `definition` 在 DB 里只存在于 8 个 YouTube Format 页 —— 这 3 页实际靠传入的 `fallback` 渲染。迁移时直接读 JSON，不要依赖 DB。

### 1.4 组件清单与 client / server 归属

| 组件 | 用途 | 数据源 | 迁移后 |
|---|---|---|---|
| `HeroSection` | 全站统一 Hero（含 `getHero(routeKey)`、`MultiLine`） | JSON | **Server** |
| `TranscribeBox` | 全站唯一输入框（link/file/批量、假 loading 1.5s、chips、预览轮播） | presets + `VideoCarousel` | **Client** |
| `FAQSection` | FAQ accordion（6 条） | JSON | **Client**（可 `<details>` 改 Server，本轮不改行为） |
| `FeatureSection` | "Why choose / Use cases / definition / subtopic" 网格或左文右视频 | DB / JSON | **Server**（改服务端取数） |
| `HowItWorksSection` | 3 步卡片 | JSON | **Server** |
| `FinalCTA` | 深色收尾 CTA（DB + fallback） | DB | **Server** |
| `CollectionSection` | 4 列封面/视频缩略卡（`cover-square` / `video-thumb`） | DB | **Server** |
| `RelatedPagesSection` | "Explore related pages"（≤6，含 `ItemList` JSON-LD） | DB | **Server** |
| `YouTubeTaxonomyCarousels` | hub 四轴大卡轮播 | DB + `youtube-axis-cards` | **Client**（轮播交互） |
| `SplitScreenCarousel` | 全宽左右分栏轮播（自动播放 6s） | props | **Client** |
| `VideoCarousel` | 视频缩略轮播（点击回填 URL） | 写死 8 条 TED 样例 | **Client** |
| `Nav` / `Footer` | 顶栏（4 组手写下拉）/ 4 列页脚 | 写死 | Nav **Client**；Footer **Server** |
| `Breadcrumb` | 面包屑（`to` → 需改 `href`） | props | **Server** |
| `PlatformPage` | podcast/youtube 详情页模板 | props | **Server**（子件多为 Client） |
| `CategoryPage` | podcast category 模板 | props | **Server** |
| `hero-images.tsx` | 48+ slug → 本地图 `{src, alt}` + `<HeroImage>` | 静态 | **Server** |
| `inline-copy.tsx` | 正文 `[label](/path)` → 内链 | props | **Server** |
| `category-mocks.tsx` | 三种 hero mock（`case_file`/`briefing`/`sermon`） | props | **Server** |
| `BeforeAfterTable` | use-case 页"before vs after"表 | JSON | **Server** |
| `BatchWorkbench` / `BatchInfo` / `BatchModeCompare` | 3 个批量工具页 | 写死 + props | **Client** |
| `library/LibraryGrid` `LibraryCard` `LibraryTaxonomy` `LibraryVideoModal` `library-data.ts` | trending-youtube 网格（筛选 + 弹窗） | DB | Grid/Card/Taxonomy/Modal **Client**；`library-data.ts` 纯函数 **Server** |
| `use-carousel.ts` | 自研横向 snap 轮播 hook | — | **Client** |
| `PageCarousel.tsx` | 疑似 dead code（scoped 路由未引用） | — | **不迁**（构建后再确认删除） |

### 1.5 图片资产

- **仓库内真实二进制**（非 `.asset.json` 清单），源码以 Vite `import` 引入：
  - YouTube 48 张：`hero-yt-*.jpg` + `youtube-news-transcript-hero.jpg` + `ted-talk-transcript-hero.jpg`
  - Podcast 13 张：`hero-apple-podcast.jpg`、`hero-spotify-podcast.jpg`、`hero-castbox.jpg`、`hero-amazon-music.jpg`、`hero-iheartradio.jpg`、`hero-overcast.jpg`、`hero-pocket-casts.jpg`、`hero-podbean.jpg`、`hero-rss-feed.jpg`、`hero-youtube-podcast.jpg`、`hero-business.jpg`、`hero-christian.jpg`、`hero-true-crime.jpg`
  - Hub / 工具 / use-case：`youtube-transcript-hero.jpg`、`hero-yt-bulk-transcript.jpg`、`hero-yt-channel-transcript.jpg`、`hero-yt-playlist-transcript.jpg`、`hero-use-case-students.jpg`、`hero-use-case-youtubers.jpg`、`hero-use-case-medical-scribes.jpg`、`vomo-logo.svg`
- ⚠️ **文件名与 slug 不总一致**，例如 `science → hero-yt-science-and-technology.jpg`、`how-to → hero-yt-howto-and-style.jpg`、`vlog → hero-yt-people-and-blogs.jpg`、`car-review → hero-yt-autos-and-vehicles.jpg`、`pet-video → hero-yt-pets-and-animals.jpg`、`nonprofit → hero-yt-nonprofits-and-activism.jpg`、`film → hero-yt-film-and-animation.jpg`、`travel → hero-yt-travel-and-events.jpg`、`event → hero-yt-event.jpg`。**必须以 `hero-images.tsx` 的实际 import 为准**，勿按 slug 猜名。
- **外部运行时图片**（保留外链，不本地化）：`https://i.ytimg.com/vi/{id}/hqdefault.jpg`（视频缩略）、`https://is1-ssl.mzstatic.com/.../600x600bb.jpg`（podcast 封面，硬编码于 `podcast-covers.ts`）。
- **字体**：Google Fonts（Fraunces / Inter / JetBrains Mono）原为 `__root.tsx` 的 `<link>`；迁移后用 `next/font/google`（自托管，CWV 更稳）。
- **回填可行性已实测**：已发布站以 `/assets/<原名>-<8位hash>.<ext>` 提供实体图，例如 `/assets/hero-apple-podcast-DfgcIzM4.jpg`；预览域 `/src/assets/*` 返回 **401**，不可用。

### 1.6 现状 SEO 缺陷（迁移一并修掉；均不触及可见文案）

| # | 问题 | 影响 | 处置 |
|---|---|---|---|
| 1 | `FeatureSection` / `FinalCTA` / `CollectionSection` / `RelatedPagesSection` / `YouTubeTaxonomyCarousels` 均客户端 `useQuery` | SSR HTML 无正文/CTA/内链，索引质量差 | 全部改服务端取数（读导出 JSON） |
| 2 | `RelatedPagesSection` 的 JSON-LD 硬编码 `https://vomo.ai`，与全站 `https://vomo-ai.lovable.app` 冲突 | 结构化数据指向错误域 | 统一走 `SITE_URL` |
| 3 | `FAQSection` 不输出 `FAQPage` JSON-LD（只有可见 accordion） | 少一类富结果 | 列为**可选增强**（默认不做，避免"改内容"） |
| 4 | `FALLBACK_AXIS_PAGES`（`youtube-axes.ts`）缺 `lecture / online-course / tutorial / webinar / no-captions` 5 条 | 首屏兜底菜单不完整 | 导出后由全量清单生成，不再手写 |
| 5 | `Nav` 与架构文档不一致（仍静态 4 组，YouTube 组只列 5 入口） | 内链覆盖不足 | 本轮**保持现状**（内容不变），仅记录 |
| 6 | canonical 指向 `https://vomo-ai.lovable.app/...` | 反代后应指向公开域 | 统一 `SITE_URL` + `metadataBase` |

---

## 2. 目标架构

### 2.1 目录结构（对齐 `today-seo-main`）

```
E:\客户部署项目\vomo-seo                 ← 新仓（git init，独立历史）
├─ src/
│  ├─ app/                               ← App Router（页面壳）
│  │  ├─ layout.tsx                      （字体 + metadataBase + 全局壳）
│  │  ├─ globals.css                     （原 styles.css 改写 @source）
│  │  ├─ not-found.tsx  error.tsx  sitemap.ts  robots.ts
│  │  ├─ podcast-transcription/
│  │  │  ├─ page.tsx
│  │  │  └─ [slug]/page.tsx
│  │  ├─ tools/
│  │  │  ├─ youtube-transcript/
│  │  │  │  ├─ page.tsx
│  │  │  │  └─ [slug]/page.tsx
│  │  │  ├─ bulk-youtube-transcript/page.tsx
│  │  │  ├─ youtube-channel-transcript/page.tsx
│  │  │  └─ youtube-playlist-transcript/page.tsx
│  │  ├─ use-cases/{students,youtubers,medical-scribes}/page.tsx
│  │  ├─ trending-youtube-video/page.tsx
│  │  └─ trending-podcast/page.tsx
│  ├─ components/
│  │  ├─ site/                           （原 proj 的 site/* 原样迁移）
│  │  │  ├─ library/…                    （LibraryGrid / Card / Taxonomy / VideoModal / library-data.ts）
│  │  │  ├─ HeroSection.tsx … PlatformPage.tsx CategoryPage.tsx …
│  │  │  └─ youtube-axes.ts youtube-axis-cards.ts related-pages.ts
│  │  │     podcast-covers.ts transcribe-box-presets.ts hero-images.tsx
│  │  ├─ ui/…                            （shadcn 预生成件，按实际引用裁剪）
│  │  └─ pages/                          （use-case 页的 ZigZag/Related 私有片段）
│  ├─ content/
│  │  ├─ data/                           （5 份原始 JSON，逐字拷贝）
│  │  │  ├─ heroes.json faqs.json how-it-works.json
│  │  │  └─ use-cases.json use-case-pages.json
│  │  ├─ db/                             （一次性导出的 Supabase 快照）
│  │  │  ├─ platform-pages.json site-features.json
│  │  │  └─ site-ctas.json site-collections.json site-collection-items.json
│  │  ├─ schema.ts                       （Zod：上述全部文件的形状）
│  │  └─ index.ts                        （loader：读取 + Zod 校验 + 索引化）
│  ├─ lib/                               （cn、seo 辅助、site-url）
│  └─ styles.css                         （原样，仅改 @source）
├─ public/images/                        （图片回填目标）
├─ scripts/
│  ├─ fetch-assets.mjs                   （★ 从已发布站回填图片，剥离哈希）
│  ├─ export-supabase.mjs                （★ 一次性导出 DB → src/content/db/）
│  ├─ validate-content.mjs               （Zod 校验 + slug 唯一性 + 内链完整性）
│  └─ diff-content.mjs                   （★ 逐页文本 diff：源站 vs 新站，保证"内容不变"）
├─ migration-source/                     （源 TanStack 路由留档，仅参考不编译）
├─ next.config.ts  tsconfig.json  postcss.config.mjs  eslint.config.mjs
├─ package.json  .env.example  .gitignore  README.md  AGENTS.md
└─ vercel.json
```

约定：`src/app` 只放页面壳，业务组件与数据全在 `src/`，与 `today-seo-main` 的拆分习惯一致。

### 2.2 数据层设计（脱库后的唯一真相）

- `src/content/data/*.json` = **从 Lovable 仓逐字拷贝的原始文件**（键：`routeKey` / `route_key`）。
- `src/content/db/*.json` = `export-supabase.mjs` 的**一次性快照**，按 `slug` / `route_key` 索引化。
- `src/content/schema.ts` = Zod 定义（仅校验，不改数据）。
- `src/content/index.ts` 暴露纯同步查询（Server Component 直接调用，无 await、无网络）：

```ts
getPlatformPage(slug, templates)      // platform_pages 快照
listPlatformPages(templates?)         // 排序：position → breadcrumb_label
listYouTubeLibrary()                  // template='youtube'，供 trending
getHero(routeKey)                     // heroes.json
getFaqs(routeKey)                     // faqs.json（slice 6）
getHowTo(routeKey)                    // how-it-works.json
getUseCases(routeKey)                 // use-cases.json
getSiteFeature(routeKey, sectionKey)  // site-features.json
getSiteCta(routeKey)                  // site-ctas.json
getCollection(routeKey, sectionKey)   // site-collections + items
useCasePages[routeKey]                // use-case-pages.json
```

> 组件签名与返回形状**尽量与源一致**（如 `getHero` 返回原对象），从而组件内部逻辑几乎不用改 —— 这是"内容零改动"的技术保证。

### 2.3 路由映射表（TanStack 文件路由 → App Router）

| 源文件 | URL | 目标 |
|---|---|---|
| `src/routes/__root.tsx` | — | `src/app/layout.tsx` + `not-found.tsx` + `error.tsx` |
| `src/routes/podcast-transcription.index.tsx` | `/podcast-transcription` | `app/podcast-transcription/page.tsx` |
| `src/routes/podcast-transcription.$slug.tsx` | `/podcast-transcription/{slug}` | `app/podcast-transcription/[slug]/page.tsx` |
| `src/routes/tools.youtube-transcript.index.tsx` | `/tools/youtube-transcript` | `app/tools/youtube-transcript/page.tsx` |
| `src/routes/tools.youtube-transcript.$slug.tsx` | `/tools/youtube-transcript/{slug}` | `app/tools/youtube-transcript/[slug]/page.tsx` |
| `src/routes/tools.bulk-youtube-transcript.tsx` | `/tools/bulk-youtube-transcript` | `app/tools/bulk-youtube-transcript/page.tsx` |
| `src/routes/tools.youtube-channel-transcript.tsx` | `/tools/youtube-channel-transcript` | `app/tools/youtube-channel-transcript/page.tsx` |
| `src/routes/tools.youtube-playlist-transcript.tsx` | `/tools/youtube-playlist-transcript` | `app/tools/youtube-playlist-transcript/page.tsx` |
| `src/routes/use-cases.students.tsx` | `/use-cases/students` | `app/use-cases/students/page.tsx` |
| `src/routes/use-cases.youtubers.tsx` | `/use-cases/youtubers` | `app/use-cases/youtubers/page.tsx` |
| `src/routes/use-cases.medical-scribes.tsx` | `/use-cases/medical-scribes` | `app/use-cases/medical-scribes/page.tsx` |
| `src/routes/trending-youtube-video.tsx` | `/trending-youtube-video` | `app/trending-youtube-video/page.tsx` |
| `src/routes/trending-podcast.tsx` | `/trending-podcast` | `app/trending-podcast/page.tsx` |
| `src/routes/tools.podcast-transcription.platform.tsx` | `/tools/podcast-transcription/platform` | **不迁**（noindex 占位） |
| `src/router.tsx` `src/server.ts` `src/start.ts` `src/routeTree.gen.ts` | — | 删除 |
| `src/lib/{error-capture,error-page,lovable-error-reporting}.ts` | — | 删除，改 `app/error.tsx` |
| `src/integrations/supabase/*` `src/lib/mcp/*` `src/routes/mcp.ts` `src/routes/[.mcp]/*` `src/routes/[.well-known]/*` `src/routes/[.]lovable.oauth.consent.tsx` | — | 删除（脱库后无运行时依赖） |

### 2.4 API 改写对照（TanStack → Next）

| TanStack Start | Next.js App Router |
|---|---|
| `createFileRoute("/x")({ component, head, loader })` | default export 页面组件 + `metadata` / `generateMetadata()` |
| `Route.useLoaderData()` | Server Component 直接同步取数（`getPlatformPage(...)`） |
| `head: () => ({ meta, links })` | `metadata` / `generateMetadata`（title/description/OG/canonical） |
| `throw notFound()` + `notFoundComponent` | `notFound()` + `app/not-found.tsx` |
| `errorComponent` | `app/error.tsx`（`"use client"`） |
| `Link to="/x/$slug" params={{slug}}` | `<Link href={`/x/${slug}`}>` |
| `activeProps` | `usePathname()` 比较 |
| `Outlet` | `{children}`（layout） |
| `<HeadContent/> <Scripts/>` | 删除（Next 托管） |
| `scripts` 内联 JSON-LD | 保留在 Server Component 的 `<script type="application/ld+json">` |
| `createServerFn` + `.inputValidator(zod)` + `.handler` | 直接同步调用 `src/content/index.ts`（无网络、无运行时 env） |
| `useQuery({... supabase ...})` | Server Component 取值后以 props 下发（或共享 helper） |
| `import.meta.env` | `process.env.NEXT_PUBLIC_*` |
| `styles.css?url` / `@tailwindcss/vite` / nitro | `app/globals.css` + `@tailwindcss/postcss` |

动态页的两个关键实现（示例）：

```tsx
// app/tools/youtube-transcript/[slug]/page.tsx
export const dynamicParams = false;                       // 只服务已导出 slug（等价原白名单）
export function generateStaticParams() {
  return listPlatformPages(["youtube"]).map((p) => ({ slug: p.slug }));
}
export function generateMetadata({ params }) {
  const page = getPlatformPage(params.slug, ["youtube"]);
  if (!page) return { title: "Page Not Found | VOMO", robots: { index: false } };
  return {
    title: page.seo_title, description: page.seo_description,
    alternates: { canonical: `${SITE_URL}/tools/youtube-transcript/${page.slug}` },
    openGraph: { title: page.og_title ?? page.seo_title, description: page.og_description ?? page.seo_description, type: "website" },
    twitter: { card: "summary_large_image" },
  };
}
export default function Page({ params }) {
  const page = getPlatformPage(params.slug, ["youtube"]);
  if (!page) notFound();                                   // 同源 notFound 文案
  return <PlatformPage data={page} routeKeyBase="/tools/youtube-transcript" … />;
}
```

---

## 3. 阶段 A：迁移实施

### A0 准备与快照（在做任何写入前）

1. **源项目零改动**：Lovable 云端仓只读引用，不 push、不变基。
2. 建新仓：`mkdir E:\客户部署项目\vomo-seo && cd vomo-seo && git init`。
3. 把 13 个待迁路由 + `__root.tsx` 原文留档到 `migration-source/routes/`（便于逐行比对"内容不变"）。
4. 记录源站基线：对 71 个 URL 各存一份 HTML 到 `e:\clients\temp\vomo-baseline\`（用于 A9 的 diff）。

### A1 脚手架与依赖

不跑 `create-next-app`（避免无用 boilerplate），按 `today-seo-main` 手工搭：

```jsonc
{
  "name": "vomo-seo",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "assets:fetch": "node scripts/fetch-assets.mjs",
    "content:export": "node scripts/export-supabase.mjs",
    "content:validate": "node scripts/validate-content.mjs",
    "content:diff": "node scripts/diff-content.mjs"
  },
  "dependencies": {
    "next": "16.3.3",
    "react": "19.2.8",
    "react-dom": "19.2.8",
    "tailwindcss": "^4",
    "@tailwindcss/postcss": "^4",
    "lucide-react": "^0.575.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "tailwind-merge": "^3.5.0",
    "tw-animate-css": "^1.3.4",
    "@radix-ui/react-*": "…仅保留实际 import 的"
  },
  "devDependencies": {
    "typescript": "^5", "@types/node": "^22", "@types/react": "^19", "@types/react-dom": "^19",
    "eslint": "^9", "eslint-config-next": "16.3.3",
    "zod": "^4", "tsx": "^4", "@supabase/supabase-js": "^2.110.7"
  }
}
```

要点：
- **裁剪**：删除 `@tanstack/*`、`vite*`、`nitro`、`@lovable.dev/*`、`bun*`、`embla-carousel-react`（未用）、`recharts`（scoped 页未用）、`@supabase/supabase-js` 由运行时降为 dev（仅供导出脚本）。
- `next.config.ts`：

```ts
const nextConfig: NextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  trailingSlash: false,                    // 与源站 canonical 一致（无尾斜杠）
  images: { unoptimized: true },           // 保持 <img> 行为与源站一致；远程图走 i.ytimg.com / mzstatic
};
export default nextConfig;
```

- 明确**不设 `basePath`**（挂载决策：根路径 + 反代白名单）。

### A2 图片资产回填（`scripts/fetch-assets.mjs`）

原理：**已发布站**的 Vite 产物把源文件名保留为 `/assets/<原名>-<hash>.<ext>`，因此"爬页 → 剥哈希 → 按原名落盘"即可 1:1 还原。

```js
// scripts/fetch-assets.mjs  —— 在 vomo-seo 仓内运行
const SITE = "https://vomo-ai.lovable.app";
const OUT  = "public/images";
const HASH = /-([A-Za-z0-9_-]{8})(\.[a-z0-9]+)$/i;   // 剥离 -CDP_oGqB / -DfgcIzM4

// 1) 逐页抓 HTML，抽出 /assets/*.(jpg|jpeg|png|svg|webp)
// 2) 剥哈希还原原名 → public/images/<原名>
// 3) 同一原名若来自多页，取首个并校验字节一致（不一致则告警）
// 4) 打印清单 + 缺失告警；对 i.ytimg.com / mzstatic 外链不下载
```

页面清单 = §1.2 的 71 个 URL（`/podcast-transcription`、`/trending-*` 无本地图属正常）。
随后批量改写源码引用：`import hero from "@/assets/hero-yt-ai.jpg"` → `const hero = "/images/hero-yt-ai.jpg"`（`hero-images.tsx` 等集中映射文件，改动面小且机械）。

### A3 一次性导出 Supabase（`scripts/export-supabase.mjs`）

**前置**：需要 `SUPABASE_URL` + `SUPABASE_PUBLISHABLE_KEY`（anon/publishable；这些表必须允许匿名 SELECT，现状即如此）。若无凭据需你提供，或改走"从已发布站 HTML 抽取"的降级路线。

```js
// 需要导出的表与列（表名/section 值均为实测）
// platform_pages: slug, template, theme, platform_name, breadcrumb_label, position, published,
//   seo_title, seo_description, og_title, og_description, hero_tag, hero_note,
//   preview, upload, capabilities_h2, capabilities_intro, capabilities, usecases_h2, usecases, cta_fallback
//   → filter: published = true
// site_features: route_key, section_key, heading, intro, items, columns, card_style, video
// site_ctas:     route_key, title, description, cta_label, cta_href
// site_collections: route_key, section_key, title, description, eyebrow, footer_note, layout
// site_collection_items: route_key, section_key, position, rank, title, subtitle, blurb,
//   cover_url, href, tag, cta_label, cta_variant
//   （site_faqs / site_howtos 已废弃，skip）
```

输出 `src/content/db/*.json`，提交入库（使构建可离线、可 diff）。导出脚本保留在仓内供将来手工重同步，但**不接进 build**（决策：一次性导出）。

### A4 五份 JSON 原样搬迁

从 Lovable 仓通过 MCP `read_file` 取回以下文件，**逐字节写入** `src/content/data/`，不做任何裁剪（保留未迁移路由的键，利于后续阶段复用）：

`heroes.json`（~73 键）、`faqs.json`（76 条 × 6 问）、`how-it-works.json`（69 键）、`use-cases.json`（66 条）、`use-case-pages.json`（3 键）。

同样原样搬：`youtube-axes.ts`、`youtube-axis-cards.ts`、`related-pages.ts`、`podcast-covers.ts`、`transcribe-box-presets.ts`。

### A5 组件与样式迁移

1. `src/styles.css` → `src/app/globals.css`；`@source "../src"` 改为 `@source "../"`（覆盖 `app/` 与 `src/`）；`@theme` 的 `--color-vomo-*` 与 `--text-h1..eyebrow` **逐字保留**；shadcn 的 `@theme inline` + `:root`/`.dark` oklch 变量整段复制（否则 `bg-background`、`Button` 等失效）。
2. `src/components/site/**`（含 `library/**`）整体迁移，改动仅限：
   - `Link` 的 `to` → `href`；`params={{slug}}` → 模板串。
   - `Breadcrumb` 的 `item.to` → `item.href`。
   - `useQuery(supabase …)` → 由父级 Server Component 传入 props（`FeatureSection` / `FinalCTA` / `CollectionSection` / `RelatedPagesSection` / `YouTubeTaxonomyCarousels`）。
   - 需要交互的文件加 `"use client"`：`TranscribeBox`、`FAQSection`、`Nav`、`SplitScreenCarousel`、`VideoCarousel`、`YouTubeTaxonomyCarousels`、`BatchWorkbench`/`BatchInfo`/`BatchModeCompare`、`library/Library*`、`use-carousel.ts`。
3. `ui/*` 按实际 import 保留（先全量、构建后裁剪）。
4. 依赖注入方式：详情页模板 `PlatformPage` 接收已取好的 `siteFeature` / `cta` / `related` 数据（保持与源相同的渲染顺序与 DOM）。
5. **不改文案**：如遇到语义不一致（如 `RelatedPagesSection` 域名、`youtube-axes` 兜底缺 5 条），只改**工程逻辑**，不动可见文字。

### A6 页面重写

按 §2.3 建 13 个页面文件 + `layout.tsx`，逐页对齐源路由的区块顺序（源页壳极薄，几乎可 1:1 誊抄）：

- podcast 枢纽：`Nav → Breadcrumb → Hero → TranscribeBox → FeatureSection(why_choose, cream) → FeatureSection(use_cases, light) → CollectionSection(platforms) → HowItWorks → FAQ → FinalCTA → Footer`
- podcast 详情：按 `template==='category'` 分派 `CategoryPage` / `PlatformPage`
- youtube 枢纽：`… → TranscribeBox → YouTubeTaxonomyCarousels → FeatureSection(why_choose, light) → FeatureSection(use_cases, cream) → HowItWorks → FAQ → FinalCTA`
- youtube 详情：Hero 图解析顺序保持 `HERO[slug] → HERO_IMAGES[slug] → HERO["youtube-news"]` 三级兜底（**注意这会导致缺图静默回落，A4 校验里要报出来**）
- 3 个 use-case 页：`Hero → FeatureSection(definition, fallback=PAGE.definition) → sections.map(ZigZag) → BeforeAfterTable → 相关页 JSON-LD → FAQ → FinalCTA`
- trending-youtube：Hero（statLeft=视频数 / statRight=分类数）→ `LibraryGrid` 客户端筛选
- trending-podcast：Hero → 平台筛选（useState）+ 卡片列表 → 相关 JSON-LD

### A7 SEO 就位

- `layout.tsx`：`metadataBase = new URL(SITE_URL)`、`title.template = "%s | VOMO"`、`icons`、`viewport`；字体 `next/font/google`。
- `generateMetadata` 逐页（详情页取 `seo_*`/`og_*`，枢纽页与工具页用源文件里的常量 title/description）。
- `app/sitemap.ts`：**只枚举本阶段 71 个 URL**（含 `generateStaticParams` 全量 slug），`lastModified` 取数据里最新日期。
- `app/robots.ts`：`allow /`；若主站已有 robots 由主站负责，这里仅作兜底。
- JSON-LD：保留 `RelatedPagesSection` 的 `ItemList`、trending 的 `CollectionPage`/`ItemList`、use-case 相关页 `ItemList`；域名统一 `SITE_URL`。`FAQPage` 列为可选增强（默认关）。
- 反代下 canonical 必须指向公开域：`SITE_URL` 由 Vercel env 注入；如需从 `x-forwarded-host` 动态推导，在 `lib/site-url.ts` 集中处理。

### A8 内容一致性校验（"不改内容"的硬门禁）

`scripts/diff-content.mjs`：对 71 个 URL 分别抓「源站 `vomo-ai.lovable.app`」与「新部署」，提取可见文本（去标签、压缩空白、剥离域名差异），逐页 diff：

- 允许差异白名单：canonical/og URL 的域名、`/_next` vs `/assets` 资源路径、字体加载方式。
- 不允许：任何正文/标题/FAQ/CTA/面包屑/DOM 顺序差异。
- 输出 `e:\clients\temp\vomo-content-diff.json`（临时产物，不入仓）与失败清单。

`scripts/validate-content.mjs`（构建前跑）：Zod 校验全部 JSON；`platform_pages` slug 唯一性与 61 条完整性；`hero_images` 覆盖 48 个 youtube slug（缺失即失败，禁止静默回落）；内链 `[label](/path)` 目标在范围内或已知外部路径。

### A9 本地构建验证

```powershell
cd E:\客户部署项目\vomo-seo
npm install
npm run assets:fetch            # 回填图片（需外网）
npm run content:export          # 一次性导出（需要 Supabase 凭据）
npm run content:validate
npm run dev                     # 冒烟 71 个 URL
npm run build                   # 必须 0 error、0 动态路由回落
npm run start
npm run content:diff -- https://<vercel-domain>
```

常见坑：`"use client"` 遗漏（构建报 RSC 错）；`dynamicParams=false` 必须与导出 slug 集一致，否则详情页 404；Tailwind v4 `@source` 未含 `app/` 导致样式缺失；shadcn oklch 变量漏拷导致深色/边框样式差异。

---

## 4. 阶段 B：Vercel 部署 + 反代接入

### B1 部署

1. Vercel 新项目 → 连 `vomo-seo` 仓（或 `vercel --prod`）。
2. 环境变量（Production）：
   - `SITE_URL` = 公开域（先填 `https://vomo-seo.vercel.app`，接入主域后改真实域）
3. `vercel.json`：保持默认；**不设 basePath/assetPrefix**。若要保险，显式关闭图片优化：`images.unoptimized` 已在 `next.config.ts`。
4. 关闭 Deployment Protection（或配置 bypass 头），否则反代会拿到 401（`luciusai` 同类坑）。
5. GitHub Actions（可选，对齐 `today-seo-main`）：push main → `npm ci` → `content:validate` → `build` → 部署 → `content:diff` 复核。

### B2 主站反代白名单

反代只把下列前缀交给本部署，其余路径原样透传（访客与搜索引擎只见主域 URL）：

```
/podcast-transcription/*        /podcast-transcription
/tools/youtube-transcript/*     /tools/youtube-transcript
/tools/bulk-youtube-transcript
/tools/youtube-channel-transcript
/tools/youtube-playlist-transcript
/use-cases/*
/trending-youtube-video
/trending-podcast
/_next/*                        ← Next 静态资源（含 /_next/static、/_next/image）
```

`/_next/*` 的两种处理：
- 若主站**不是** Next（如 Vite 应用，`/_next` 未被占用）→ 直接按上表放行，最省事。
- 若主站也是 Next → 与本应用的 `/_next` **命名空间冲突**，解法：给本应用设 `assetPrefix`（如 `/vomo-static`）并让反代放行该前缀（可参考 `luciusai-blog-reverse-proxy.md` 的 `ASSET_PREFIX` 方案）。**上线前必须先确认主站技术栈。**

### B3 被反代时的注意事项

- Next 应用在自身 Vercel 域仍会响应根路径 `/_next/image`，但页面不再请求它，不影响主域命名空间。
- 保留原 host（`x-forwarded-host`）以便 canonical 正确。
- `robots.txt` / `sitemap.xml`：若由主站拥有，本阶段产物仅作兜底；本阶段新页需并入主站 sitemap 或在主站 sitemap 中引用本应用的子 sitemap。

---

## 5. 验收清单

| # | 项 | 通过标准 |
|---|---|---|
| 1 | 71 个 URL 全 200 | 逐一 curl；无重定向、无尾斜杠跳转 |
| 2 | slug 完整性 | 48 youtube + 13 podcast 与源站一致；`business-video / youtube-news / pet-video` 原样 |
| 3 | 内容一致性 | `content:diff` 全绿（仅允许域名/资源路径差异） |
| 4 | SSR 正文 | 关闭 JS 后 why_choose / subtopic / CTA / related 仍在 HTML 中 |
| 5 | metadata | title/description/OG 与源站逐字一致；canonical = 公开域 + 正确路径 |
| 6 | 图片 | `public/images` 全部被引用且 200；无回落 `youtube-news` 图的页面 |
| 7 | 样式 | 与源站逐屏对比无差异（字体、`--color-vomo-*`、h1/h2 梯度） |
| 8 | 交互 | TranscribeBox 假 loading、FAQ 展开、轮播自动播放、trending 筛选、Nav 下拉 |
| 9 | 脱库 | 仓内 grep 无 `supabase`、无 `lovable`、无 `import.meta.env`、无 `@tanstack` |
| 10 | 结构化数据 | ItemList / CollectionPage 校验通过，URL 指向公开域 |
| 11 | 反代 | 主域 URL 返回新站内容；`/_next/*`（或 `assetPrefix`）资源 200；无 404/401 |
| 12 | 性能 | Lighthouse ≥90（移动端），全静态预渲染 |
| 13 | 404 | 未导出的 slug 返回 404 页面（文案与源站一致） |

---

## 6. 风险与待办

| # | 风险 / 待办 | 影响 | 处置 |
|---|---|---|---|
| 1 | **Supabase 凭据**：导出需要 `SUPABASE_URL` + publishable key | A3 阻塞 | 由你提供；或降级为从已发布站 HTML 抽取（成本更高、易漏字段） |
| 2 | **主站 `/_next` 是否被占用未知** | 反代方案分叉 | 上线前确认主站技术栈（见 B2） |
| 3 | **路径与真实 vomo.ai 重叠**：`/podcast-transcription/*`、`/tools/youtube-transcript/*` 在 vomo.ai 已存在（内容不同）；`/use-cases/*`（复数）与 `/use-case/*`（单数）并存 | 若主站即 vomo.ai，反代会**替换**现有页面 | 需先明确"主站"是哪个域；若非 vomo.ai 则无冲突 |
| 4 | 裸 `<img>` 与 `next/image` 选择 | 远程图优化需 remotePatterns | 采用 `unoptimized: true` + `<img>`，行为与源站一致 |
| 5 | `platform_pages.position` 有重复值 | 轮播/列表顺序不稳定 | 排序沿用 `position → breadcrumb_label` |
| 6 | 缺图静默回落 `youtube-news` | 页面图错但不报错 | `validate-content` 强制 48 slug 图全覆盖 |
| 7 | `PageCarousel.tsx` 疑似 dead code | 多迁无用组件 | 构建后确认删除 |
| 8 | `Nav` / `Footer` 指向未迁移页（`/pricing`、`/library`、`/blog`…） | 在 Vercel 域上会 404 | 保持相对链接（公开域由反代透传到底站）；部署早期 404 属预期，README 注明 |
| 9 | 55+ 个非 scoped 的 `/tools/*`、`/guide/*` 未迁移 | 内链不完整 | 另立阶段；本次只保证 scoped 内链正确 |
| 10 | 无真实转录能力（TranscribeBox 为 1.5s mock） | 迁移后仍是 mock | 与源站行为一致，属产品侧后续议题，不在本次范围 |

---

## 7. 参考

- 源项目：Lovable `vomo-ai`（`965859ba-5107-46f4-b636-7aecf6a27cad`）｜线上 `https://vomo-ai.lovable.app`
- 迁移先例（同构）：`E:\客户部署项目\today-seo-main`（Lovable → Next，含 `migration-source/`、内容数据层 + Zod、Vercel 部署 + CI 复核）
- 参考项目：`E:\客户部署项目\medo-blog`、`E:\客户部署项目\sparki-blog`
- 反代范式：`e:\clients\luciusai\luciusai-blog-reverse-proxy.md`（`ASSET_PREFIX` / `/_next` 命名空间冲突解法）
- 同构构建方案范式：`e:\clients\frontierrounds\frontier-rounds-nextjs-build-plan.md`
- 站点现状与 IA：`e:\clients\vomo\vomo-site-structure.md`、`vomo.md`
- 页面生产范式：`e:\clients\vomo\podcast transcription\page-playbook.md`、`youtube transcription\page-playbook.md`
- 源项目内架构留档：`.lovable/plan/youtube-轴划分校正-一个数据源-四条轴-2026-08-23.md`、`.lovable/plan/podcast-transcription-slug-全面动态化方案-2026-08-05.md`

---

*本方案为执行蓝图；每阶段完成即在目标仓 `README.md` 勾选状态。最后更新：2026-09-11*
