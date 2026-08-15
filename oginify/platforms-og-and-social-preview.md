# OG 图与 Social Preview 平台参考

> **本文档职责**：汇总 Open Graph / Social Preview / Twitter Card 相关概念、尺寸标准，以及各平台的内置能力与配置方式——作为 Oginify 内容页 `/platforms-with-built-in-og` 的**文档源**，也可独立作知识库引用。  
> **引用**：[主文档](./oginify.md) | [竞品 §内置方案](./oginify-competitors.md#3-内置方案平台自带-og-生成) | [增长策略 §2.4](./oginify-growth-strategy.md#24-platforms-with-built-in-og--规划) | [尺寸参考](./use-cases/by-image-size.md) | [Gallery 线上](https://oginify.com/gallery) | [Websites Without OG 线上](https://oginify.com/websites-without-og-image)  
> **更新日期**：2026-07-26

---

## 1. 核心概念

### 1.1 三个名字，Often 同一张图

| 术语 | 视角 | 说明 |
|------|------|------|
| **Open Graph Image / OG 图** | 技术标准 | HTML `<meta property="og:image" content="...">`；Facebook 2010 年 Open Graph 协议推广，现成事实标准 |
| **Social Preview / 社交媒体预览图** | 产品/UI 叫法 | 各平台 Settings 里「上传分享封面」的入口名；上传后写入 `og:image` |
| **Twitter Card / X Card** | X 平台扩展 | `twitter:image` 等标签；大图卡片常用 **1200×675** 或 **1200×628**（`summary_large_image`） |

**关系**：在 GitHub 等平台上，**Social Preview = 你在后台配置的 OG 图**；没配置时，平台可能用自动生成图或仅显示头像+文字。

### 1.2 OG 图出现的位置

| 场景 | 作用 |
|------|------|
| **外链分享** | Twitter/X、LinkedIn、Facebook、Slack、Discord、WhatsApp、iMessage、Telegram 等读取 `og:image` 展示卡片 |
| **平台内列表** | GitHub Topics、部分搜索/Explore 卡片标题上方 banner |
| **Discover / Newsletter** | Google Discover、邮件转发链接时的视觉入口 |
| **SEO / 传播** | 提高 CTR；pSEO 站点每 URL 独立预览图支撑规模化分发 |

### 1.3 两类平台能力

| 类型 | 含义 | 例子 |
|------|------|------|
| **平台级封面** | 整个仓库/站点/产品一条链接对应一张（或自动生成） | GitHub Social Preview、npm 包页 |
| **页面级 OG** | 每个 URL（文章、产品页、落地页）各自一张 | WordPress Featured Image、Next.js `opengraph-image.tsx` |

---

## 2. 尺寸与格式标准

### 2.1 通用推荐（Oginify 默认输出）

| 属性 | 推荐值 |
|------|--------|
| **尺寸** | **1200 × 630 px**（宽高比 ≈ 1.91:1） |
| **最小** | 600 × 315 px |
| **格式** | PNG / JPG / GIF（动图多数平台只显示第一帧） |
| **文件大小** | < 1 MB（GitHub Social Preview 上限）；一般建议 < 8 MB |
| **安全区** | 核心文案/Logo 放在中间 **1000 × 500** 区域，边缘可能被裁切 |

> **628 vs 630**：Google/Meta 广告规范常用 1200×**628**（精确 1.91:1）；OG 协议惯例 1200×**630**。差 2px，跨平台可互换。详见 [use-cases/by-image-size.md](./use-cases/by-image-size.md)。

### 2.2 平台差异速查

| 平台 / 用途 | 推荐尺寸 | 备注 |
|-------------|----------|------|
| Facebook / LinkedIn / Slack / Discord | 1200 × 630 | 读取 `og:image` |
| X / Twitter 大图卡片 | 1200 × 628 或 1200 × 675 | `summary_large_image`；Oginify 有专用 [Twitter Card Generator](https://oginify.com/twitter-card-generator) |
| **GitHub Social Preview** | **1280 × 640**（2:1） | 与通用 OG 略不同；最低 640×320 |
| LinkedIn 文章封面 | 1200 × 644 | 与 630 可勉强复用，可能上下裁切 |
| Google Discover 大图 | ≥1200 宽，16:9 优先 | 1200×675，非 1.91:1 |

### 2.3 设计原则（2 秒法则）

- **项目名 + 一句话价值**，大字号、高对比
- **不要写 Star 数、版本号**（会过时）
- 透明 PNG 需测试深色/浅色背景；不确定时用纯色底
- 社媒平台缓存 OG 图 **24–48 小时**，更新后可用 [Facebook Debugger](https://developers.facebook.com/tools/debug/) 等强制刷新

---

## 3. 平台分类详表

### 3.1 代码托管 / 包注册 / 开发者平台

这类平台的「Social Preview」是**资源级**（一个 repo / 一个包），不是每篇 README 一张。

| 平台 | 功能名称 | 配置方式 | 尺寸 | 自动/手动 | 说明 |
|------|----------|----------|------|-----------|------|
| **GitHub** | Social Preview | 仓库 → **Settings → General → Social preview → Upload** | 1280×640，<1MB | 手动上传 **或** 自动生成 OG | 上传后 = `og:image`；Topics 列表标题上方 banner 主要来自此图。未上传时 `opengraph.githubassets.com` 动态生成（含 Star、描述、语言）。Issue/PR 有独立 OG URL。 |
| **GitLab** | Social image | 项目 **Settings → General → Visibility → Social media preview** | 类似 OG 标准 | 手动 + 部分自动 | 与 GitHub 概念一致 |
| **npm** | 包页 OG | 由 npmjs.com 页面 meta 决定，**非**单独上传入口 | 1200×630 级 | 自动（包名+描述） | 分享 `npmjs.com/package/xxx` 时的卡片；维护者通过 package.json description 等间接影响 |
| **PyPI** | 项目页 OG | 项目页 meta | 通用 OG | 自动 | 分享 pypi.org/project/xxx 链接时的预览 |
| **VS Code Marketplace** | 扩展页截图/图标 | Marketplace 发布表单 | 1280×720 等截图规范 | 手动上传截图 | 非 OG 协议，但是「第一印象图」同类需求 |

#### GitHub 补充（常见问答）

```
自定义 Social Preview  ≈  配置的 og:image（同一文件）
未上传                 →  opengraph.githubassets.com/<hash>/<owner>/<repo> 自动生成
README 顶部 <img>       ≠  Social Preview（需单独上传）
```

自动生成 URL 示例：

```
https://opengraph.githubassets.com/1/<owner>/<repo>
https://opengraph.githubassets.com/1/<owner>/<repo>/issues/<n>
https://opengraph.githubassets.com/1/<owner>/<repo>/pull/<n>
```

官方文档：[Customizing your repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)

---

### 3.2 CMS / 博客 /  Newsletter

**页面级**：每篇文章通常一张 Featured Image → 自动写入 `og:image`。

| 平台 | 机制 | 配置入口 | 尺寸 | 说明 |
|------|------|----------|------|------|
| **WordPress** | Featured Image → `og:image`；插件可增强 | 文章编辑器 Featured Image；**Yoast / Rank Math / Jetpack** | 1200×630 | Jetpack Social Image Generator 等可自动生成 |
| **Ghost** | Feature image + 标题/meta | 文章 Feature image | 1200×630 | 内置 OG，开箱即用 |
| **Substack** | 标题+作者+Logo 合成卡片 | 发布流程自动 | 分享 OG ≈1200×630；**邮件头图** 1100×220（勿混淆） | 邮件内横幅 ≠ 分享 OG |
| **Medium** | 服务端自动渲染 | 无需单独配置 | 1200×630 级 | 强调标题与品牌 |
| **Dev.to** | 动态卡片（标题+头像+标签） | 自动生成 | 1200×630 级 | 开发者社区 |
| **Hashnode** | 动态 OG（标题+作者+品牌色） | 自动生成 | 1200×630 级 | 技术博客托管 |

---

### 3.3 框架 / Hosting（开发者自建站）

通过代码或约定文件**按 URL 动态生成** OG 图。

| 平台 / 工具 | 机制 | 典型实现 | 说明 |
|-------------|------|----------|------|
| **Vercel** | `@vercel/og` | Edge API Route，JSX → PNG | [官方博客](https://vercel.com/blog/introducing-vercel-og-image-generation-fast-dynamic-social-card-images) |
| **Next.js** | `ImageResponse` / `opengraph-image.tsx` | App Router 文件约定 | 与 Vercel OG 同源（Satori + resvg） |
| **Nuxt** | `nuxt-og-image` 等模块 | 服务端渲染 OG | SEO 模块生态 |
| **Astro** | `@astrojs/og` / 集成 | 构建时或 SSR | 静态站友好 |
| **SvelteKit** | `@vercel/og` 或自定义 route | API endpoint | 灵活 |
| **Cloudflare Workers** | `@vercel/og` 兼容方案 | Edge 动态生成 | 低延迟 |
| **Docusaurus** | `themeConfig.image` + 插件 | 文档站默认 OG | 开源文档常见 |
| **Mintlify** | 文档配置 + 自动 OG | `mint.json` | 开发者文档 SaaS |

**特点**：适合有工程能力的团队；每页可不同，但需维护模板与部署。

---

### 3.4 No-code / 建站 / 文档

| 平台 | 机制 | 配置方式 | 说明 |
|------|------|----------|------|
| **Framer** | 发布时生成 OG | 页面 SEO 设置 | 设计稿即站点 |
| **Webflow** | CMS 集合可模板化 OG | Collection 字段 / Page settings | 营销站常见 |
| **Notion** | 公开页 emoji + 标题 | 自动 | 定制能力有限 |
| **Super.so / Potion** | Notion 转站，继承/覆盖 OG | 平台 SEO 设置 | Notion 生态 |
| **Read.cv** | 个人页分享卡片 | 平台默认 | 创作者简历 |
| **Linear** | 产品/更新页分享 | 部分自动生成 | 偏 B2B 工具 |
| **Lovable / v0 / Bolt** | 依赖托管方 meta 或手动 `<head>` | 项目 SEO 设置 | **通常无内置 OG 生成** → Oginify 目标用户 |

---

### 3.5 应用商店 / 产品发布（同类需求，不同机制）

| 平台 | 「封面」形态 | 说明 |
|------|-------------|------|
| **Product Hunt** | Gallery 图、Launch 封面 | 非 `og:image`，但是产品首发视觉 |
| **App Store / Google Play** | 截图、预览视频 | 商店规范，非链接 unfurl |
| **Chrome Web Store** | 图标 + 截图 | 扩展分发 |
| **Gumroad / Lemon Squeezy** | 产品封面图 | 数字商品页 |

---

## 4. 决策树：要不要用 Oginify？

```
你的网站/内容在哪？
│
├─ 已在 GitHub / Ghost / Medium / Hashnode 等「内置 OG」平台
│   └─ 直接用平台能力；GitHub 可选手动 Social Preview 加强品牌
│
├─ 用 Next.js / Vercel 等，愿意写 opengraph-image 代码
│   └─ 用 @vercel/og 或框架约定；Oginify 作原型 / 非工程同事出图
│
├─ 自建站 / 静态站 / Lovable / Webflow 无模板 OG / pSEO 成百上千 URL
│   └─ 需要外部工具：Oginify（粘贴 URL → 1200×630）或 social-cards-skills（Agent 程序化）
│
└─ 不确定有没有 og:image
    └─ 用 Oginify Validator：https://oginify.com/open-graph-validator
```

**Oginify 定位**（与 [oginify-competitors.md](./oginify-competitors.md) 一致）：平台**已内置** → 不必重复造轮子；**未内置**或需**每 URL 定制** → Oginify 填补空白。

---

## 5. 生成方式对照（行业四种路线）

| 方式 | 代表 | 速度 | 成本 | 灵活性 | 适合 |
|------|------|------|------|--------|------|
| **代码模板** | `@vercel/og`、Satori | 快（Edge） | 低 | 高（需开发） | 工程团队 |
| **平台内置** | GitHub、Ghost、Medium | 即时 | 免费 | 低–中 | 托管平台用户 |
| **模板 SaaS** | Canva、Bannerbear | 中 | 订阅 | 中（手工） | 营销人员 |
| **AI / 读页生成** | **Oginify** | 中 | 按张 | 高（content-aware） | 站长、SEO、pSEO |
| **首屏截图** | **Oginify Above the Fold** | 快 | 零 AI | 中（保真） | 落地页、产品页 |

---

## 6. 工具与资源

### 6.1 Oginify 产品矩阵（站内）

| 工具 | URL | 用途 |
|------|-----|------|
| OG Generator | [oginify.com](https://oginify.com) | 粘贴 URL → 2 张 1200×630 |
| OG Validator | [/open-graph-validator](https://oginify.com/open-graph-validator) | 解析 OG/Twitter 标签 + 多平台预览 |
| Above the Fold | [/above-the-fold](https://oginify.com/above-the-fold) | 首屏截图 → 1200×630 |
| Gallery | [/gallery](https://oginify.com/gallery) | ~100 品牌 OG 灵感 |
| Websites Without OG | [/websites-without-og-image](https://oginify.com/websites-without-og-image) | 21 个缺 OG 知名站反面案例 |
| social-cards-skills | [GitHub](https://github.com/kostja94/social-cards-skills) | MIT Agent Skills，程序化出图 |

### 6.2 第三方生成 / 校验

| 工具 | 链接 | 说明 |
|------|------|------|
| SylphxAI/og | [GitHub](https://github.com/SylphxAI/og) | URL 参数生成，6 主题 |
| OGCardForge | [GitHub](https://github.com/Bismay-exe/ogcardforge) | 5 模板含 Terminal 风 |
| readme-SVG Social Preview Generator | [GitHub](https://github.com/readme-SVG/github-social-preview-generator) | 输入 repo URL 浏览器端生成 |
| GitHub OG 图提取 | [jsurrea/github-repository-social-preview-extractor](https://github.com/jsurrea/github-repository-social-preview-extractor) | 下载 opengraph.githubassets.com 自动图 |
| metaprev | [GitHub](https://github.com/hungv47/metaprev) | 本地校验 + Facebook/X/LinkedIn/Discord mock |
| Facebook Sharing Debugger | [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug/) | 强制刷新 OG 缓存 |

### 6.3 内容三件套（Oginify SEO 策略）

| 页面 | 角色 | 目标搜索词 |
|------|------|------------|
| Gallery | 正面灵感 | og image examples / best og images |
| Websites Without OG | 反面警示 | sites without og image |
| **Platforms Built-in OG**（本文档 → 未来 `/platforms-with-built-in-og`） | 决策参考 | vercel og / wordpress social image / github social preview |

---

## 7. 待核实与维护

| 项 | 状态 | 备注 |
|----|------|------|
| GitLab Social preview 入口文案 | 待逐版核实 | 各版本 Settings 路径可能微调 |
| npm / PyPI 是否支持自定义 OG 上传 | **无**独立上传 | 依赖 registry 页面 meta |
| Linear / Super.so OG 细节 | 待补截图 | 增长策略已列名 |
| 各平台 2026 尺寸政策变更 | 定期复查 | 以平台官方文档为准 |

**维护建议**：每季度抽查上表「配置入口」链接；新平台内置 OG 能力时追加 §3 对应分类。

---

## 8. 相关文档索引

| 文档 | 内容 |
|------|------|
| [use-cases/by-image-size.md](./use-cases/by-image-size.md) | 1200×630 全场景、广告复用、628 vs 630 |
| [use-cases/by-page-type.md](./use-cases/by-page-type.md) | Featured Image = OG Image |
| [oginify-competitors.md §3](./oginify-competitors.md) | 内置方案 vs Oginify |
| [oginify-growth-strategy.md §2.4](./oginify-growth-strategy.md) | Platforms 页 SEO 与叙事 |
| [oginify-build-in-public.md](./oginify-build-in-public.md) | 调研来源与三件套策略 |
