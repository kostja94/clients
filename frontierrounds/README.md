# Frontier Rounds — 项目记录索引

> **定位**：AI 融资额度的英文内容站（融资追踪 / 排行榜 / 投资机构档案）
> **域名**：[frontierrounds.com](https://frontierrounds.com)（已购）
> **代码来源**：`E:\自有部署项目\AI Funding Hub`（Lovable 导出的 TanStack Start + Vite 项目，现品牌名 "AI Capital"）
> **目标态**：Next.js App Router 项目（对齐 nova-scientia / alignify 等参考项目），部署于 **Cloudflare Workers**（不再用 Vercel）
> **记录创建**：2026-09-07

---

## 文件清单

| 文件 | 内容 | 状态 |
|------|------|------|
| [frontier-rounds-nextjs-build-plan.md](./frontier-rounds-nextjs-build-plan.md) | **完整构建 + 部署方案**：现状盘点、Next.js 迁移映射表、图片资产回填脚本、品牌换标、SEO 就位、Cloudflare（OpenNext）部署全步骤、上线验收清单 | ✅ 完成（2026-09-07） |
| [branding/](./branding/) | **最终品牌 SVG**：`fr-icon.svg`（黑底白图）、`fr-icon-mono.svg`（透明底纯黑）、`fr-wordmark.svg`（Instrument Serif 轮廓化 wordmark） | ✅ 完成（2026-09-07） |
| [funded-products/](./funded-products/) | **融资的 AI 产品**（24 份档案 + `_index.md`）：网站 Funding Leaderboard 上的真实融资 AI 产品，字段含累计融资/最大轮/估值/领投方/来源 URL/可信度 | ✅ 完成（2026-09-08） |
| [funding-investors/](./funding-investors/) | **融资的投资方**（11 份档案 + `_index.md`）：网站 Investor Atlas 上的真实投资方，字段含基本档案/投资逻辑/投资组合（全部可溯源公司） | ✅ 完成（2026-09-08） |

## 执行进度

| 阶段 | 内容 | 状态 |
|------|------|------|
| 阶段 A（重构） | 代码仓 `E:\自有部署项目\frontierrounds`：Next.js 16 + Tailwind v4 + shadcn 全套组件 + 数据层迁移；图片 189 张回填 `public/logos\|portraits`；品牌换标 Frontier Rounds；sitemap/robots/404/error/metadata 就位 | ✅ 完成（2026-09-07） |
| 本地验证 | `npm run build` 通过（18 页全 SSG）；冒烟测试全绿 | ✅ 完成 |
| 阶段 B（部署） | GitHub 仓 `kostja94/frontier-rounds`（SSH 推送）+ Actions CI（ubuntu 构建 OpenNext）；wrangler routes 绑 `frontierrounds.com` + www；SSG 经 static-assets incremental cache 修复动态路由 404 | ✅ 上线（2026-09-07 21:5x） |

## 线上验收（2026-09-07）

- `https://frontierrounds.com` 200；`www` 200
- `/`、`/leaderboard`、`/investors`、`/investors/{11 个 slug}` 全部 200，无 "AI Capital" 残留，canonical 均指向 frontierrounds.com
- `/sitemap.xml`（含全部 investor slug）、`/robots.txt`、`/logos/*.png` 200；未知 investor slug 正确 404

## 数据治理：移除虚构演示轮次（2026-09-07）

- **问题**：首页 "Latest Funding Rounds" 区块的 25 条数据全部来自 Lovable 演示/样例（含 `Helion Labs`、`Mistral Forge`、`Quanta Vision` 等虚构公司），对真实内容站属误导性信息。
- **处置**：`src/data/fundingRounds.ts` 置为 `[]`（保留类型与 format 工具函数）；首页改为空态引导页（H1 "The money behind frontier AI, one round at a time." + Investor Atlas / Leaderboard CTA）；footer "Sample data / illustrative" 声明删除。
- **保留**：leaderboard（`fundingLeaderboard.ts`）与 investor 档案为另一套含真实公司 + sourceUrl 的数据，未受影响；investor 页 "Related rounds" 已有空态文案。
- **验收**：commit `cfe6252` 经 CI 部署；线上 `/` 已无虚构公司名与 sample 声明，4 条主路由全部 200。

## 站内真实数据归档（2026-09-08）

将网站现有的**两套真实数据**转录为可阅读/可追溯的 Markdown 档案，落在本记录仓：

- **[funded-products/](./funded-products/)** — "融资的 AI 产品"：24 家（OpenAI → Sarvam AI，按累计融资降序）。数据源 `fundingLeaderboard.ts`，每份档案含国家/赛道/累计融资/最大一轮/估值/最近融资日期/领投方/来源机构/数据可信度（Disclosed / Reported），并附 `sourceUrl` 溯源。
- **[funding-investors/](./funding-investors/)** — "融资的投资方"：11 家（Sequoia、a16z、HongShan、Peak XV、Shunwei、Lollapalooza、YC、MiraclePlus、Elad Gil、Naval、Nat Friedman）。数据源 `investors/*.ts`，每份档案含基本档案表、投资逻辑（thesis）、投资组合（含官网链接与中文别名）、别名。

> 生成方式：临时解析脚本（`@temp/parse_fr_ts.py`）忠实转录站点 TS 数据层，字段与线上页面一致，未增删事实。**注意**：若线上站点后续增删条目，可重跑该脚本刷新本目录。

## 事实核查与数据修复（2026-09-08）

用 subagent 对 `funded-products/`（24 家）与 `funding-investors/`（11 家/人）档案逐项联网核查（公司存在性、金额/日期/估值/领投方、人物事实），**只依据公开来源**判定，无证据者不保留。发现的问题已同步修复线上数据层（`fundingLeaderboard.ts`、`investors/*.ts`）与本目录 md：

- **融资数据纠偏（约 30 处）**：OpenAI 领投方改为官方披露财团；Anthropic 累计 US$74.6B→US$118B、xAI→US$37B、Databricks→US$25B、SSI→US$8B、ElevenLabs→US$781M、Cerebras→US$2.85B、MiniMax→US$3.4B、Unitree→US$1.15B 等累计修正；Zhipu 更正为 2026-07 IPO 后配售（US$4B / 估值 US$64B，原"2024 Series D US$420M"为过时数据）；Harvey（US$200M G 轮 / US$11B / 2026-03-25）、Abridge（Series E / US$300M / 2025-06-24）、Physical Intelligence（2025-11-20 / CapitalG）、Mistral（2025-09-09 / ASML）、Scale AI（2025-06-12）等日期/轮次/领投方修正；**弱来源一律替换为官方或权威媒体 sourceUrl**（公司 blog、Reuters/CNBC/Bloomberg/STCN/36kr 等）。
- **机构档案修复**：a16z AUM US$45B→~US$106B（2026-03 Form ADV）；HongShan 对 Unitree 进入时点 2020→2019-12、MiniMax 轮次角色表述修正；Sequoia Doug Leone 2026-03 回归 chairman 时点、Harvey G 轮为 co-led。
- **个人天使档案修复**：Elad Gil 组合删除 **Cursor / Runway / Glean** 三项（CB Insights/融资报道查无投资记录，其中 Runway 属同名金融科技公司混淆），补入官网自证的 **OpenAI**，披露数 ~140 → 250+；Nat Friedman 组合删除 **Ideogram**（多源交叉无 NFDG 记录），SSI 备注补 Gross 联合创始人语境，Meta 任职表述精确化（Friedman=VP of Product & Applied Research 与 Alexandr Wang 共领 MSL，NFDG 停止新投资）。

> 修复原则：改前逐项复核实证，改后 TS（站点展示层）与本地 md（归档层）逐字一致；本次不涉及新增融资事件，仅修正既有条目。

## SEO/分析就位（2026-09-07）

- **GSC**：网域属性 `frontierrounds.com`（Domain 验证，DNS TXT）已验证通过；sitemap.xml 含 14 个 URL（/、/leaderboard、/investors + 11 investor 档案），逐一 curl 全部 200。
- **GA4**：属性 ID `G-YCMXNXZENN`，经 `@next/third-parties/google` `<GoogleAnalytics>` 接入根布局（`src/lib/site.ts` 暴露 `GA_MEASUREMENT_ID`，可用 `NEXT_PUBLIC_GA_ID` 覆盖）。commit `8facb9c` 部署；线上 HTML 含 gtag.js，端点 200。
- **踩坑**：`package-lock.json` 早期曾被跟踪，`.gitignore` 对已跟踪文件无效——`git add -A` 会重新带入；需 `git rm --cached`（commit `65fa848`）后才会被忽略。CI 用 `npm install` 不依赖 lock，故两轮部署均成功。

## 品牌系统落地：替换 Lovable favicon/icon/OG（2026-09-07）

- **设计源**（本记录仓 `branding/`，已定稿）：基于 Apineed+GPT-Image v3 反白小样重绘的**黑白两色** SVG——
  - `fr-icon.svg`：黑圆角方块 + 白色开环（缺口右上）+ 内节点弧链 + 缺口外探点（深底/图标用）
  - `fr-icon-mono.svg`：同形，透明底纯黑（浅底/单色/可改色）
  - `fr-wordmark.svg`：品牌名 "Frontier Rounds"，Instrument Serif Regular **轮廓化 path**（不依赖字体安装）
- **过程文件已清理**（2026-09-08）：branding-samples 概念小样 PNG、APINEED 生图/生成/派生脚本、OG 模板、字体源均已删除，只保留最终定稿 SVG。未来若需调整 logo 形状，直接编辑 `fr-icon.svg` 即可（几何结构见 commit 历史）。
- **站点接入**（deploy 仓 commit `f8755b1`，已 CI 上线验收）：
  - `app/favicon.ico`（16/32/48 多尺寸**极简标**：仅开环+缺口+外探点，小尺寸可辨）+ `app/icon.png`(512) + `app/apple-icon.png`(180) —— Next 约定式自动注入 `<link rel=icon/apple-touch-icon>`
  - `app/manifest.ts`：PWA manifest（paper/ink 主题色，192+512 icon）；`public/icons/icon-192.png`
  - `public/og/og-default.png`（1200×630，Wordmark+图标+tagline 组合）；`layout.tsx` 补 `openGraph.images` + `twitter:image`（指向 `OG_IMAGE`）
  - `public/favicon.ico`（Lovable 旧图）已删，避免与 `app/favicon.ico` 双源
  - **验收**：构建产物含 `/icon.png`、`/apple-icon.png`、`/manifest.webmanifest` 路由；线上 `<head>` 已含全部 icon/manifest/og:image 标签，`/favicon.ico`、`/icon.png`、`/og/og-default.png` 等端点全部 200，无 lovable 残留
- **又一次踩坑**：`.gitignore` 中 `/package-lock.json   # 注释` 的**行内注释无效**——gitignore 仅行首 `#` 为注释，行内 `#` 视为模式一部分，整条规则失效（`git check-ignore` 静默不匹配）。已改为独立注释行。

### www → 裸域 301（防重复内容，2026-09-07 已生效）

四象限 URL 全部收敛到 canonical `https://frontierrounds.com`（路径保留）：

| 入口 | 行为 |
|---|---|
| `https://www.*` | 301 → `https://frontierrounds.com/...`（1 hop） |
| `http://www.*` | 301 → https://www → 301 → 裸域（2 hops） |
| `http://frontierrounds.com` | 301 → https 裸域（1 hop） |
| `https://frontierrounds.com` | 直接 200（0 hop，canonical） |

**实现方式（重要踩坑）**：域名是绑定在 Worker 上的 Custom Domain，流量判定为 Worker route，**Page Rules 的 Forwarding URL 会被 CF 静默忽略**（官方文档确认）→ 必须用 **Redirect Rules**（新版规则引擎，`http_request_dynamic_redirect` 阶段，先于 Worker 执行）。CF 自带模板 **"Redirect from WWW to root"**：`https://www.*` → `https://${1}`（`*` 捕获 `www.` 后的主机名+路径，天然保留路径）301；http 变体同理另建一条 `http://www.*` → `https://${1}`。

## 部署链路备忘（下次更新发版）

```
1. 本地改数据/内容 → commit
2. git push origin main（走 SSH remote：git@github.com:kostja94/frontier-rounds.git）
   ※ HTTPS 到 github.com:443 在本网络不可达，务必用 SSH
3. Actions workflow "Deploy Frontier Rounds" 自动：npm install → opennextjs-cloudflare build → wrangler deploy
4. 等 run 绿（约 1.5–2 min）：gh run watch $(gh run list --repo kostja94/frontier-rounds -L1 --json databaseId -q '.[0].databaseId') --repo kostja94/frontier-rounds --exit-status
```

> 经验教训（踩坑记录）：
> - Windows 上 OpenNext build 不可用（官方不支持，缺 edge config 产物）；必须在 ubuntu CI 构建
> - 勿把 Windows npm 生成的 package-lock.json 入库（@emnapi 等平台依赖导致 Linux `npm ci` 失败）；CI 用 `npm install`
> - wrangler 4.129 已弃用顶层 `custom_domains`，绑自定义域要用 `routes: [{pattern, custom_domain:true, zone_name}]`
> - OpenNext + Next 16 SSG 动态页 404：必须 `dynamicParams=false` + open-next.config.ts 用 `staticAssetsIncrementalCache`

## 关键结论速览

1. **技术选型**：Next.js App Router（React 19 + Tailwind CSS v4，保留原 editorial 设计系统）+ 数据层 TS 硬编码迁移。
2. **部署选型**：Cloudflare Workers + `@opennextjs/cloudflare`（OpenNext，成熟稳定）；`vinext` 为官方实验性新路线，留作备选。
3. **图片资产**：`src/assets/*.png.asset.json` 仅是 Lovable 云端指针，实体图在
   `https://id-preview--1e49e127-78ec-480f-9a11-53fbb3437103.lovable.app/__l5e/assets-v1/{asset_id}/{原文件名}`
   ——已实测可访问，需脚本回填到 `public/logos`（脚本见方案 §A4）。
4. **品牌与 SEO 遗留**：现文案品牌为 "AI Capital"；leaderboard 页 canonical 残留 Lovable preview URL（`id-preview--….lovable.app/leaderboard`）；无 sitemap。均须在重构中替换/补齐。
5. **双仓结构**：源码仓 `E:\自有部署项目\frontierrounds`（Next + CF 配置）；策略/记录仓 `E:\clients\frontierrounds`（本目录）。

---

*本目录为策略记录仓，不混入 Next 应用代码。最后更新：2026-09-08（事实核查修复）*
