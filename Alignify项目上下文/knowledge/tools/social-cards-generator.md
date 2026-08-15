# Social Cards Generator · 知识块（非线性笔记）

> 自动生成 Open Graph 图片、Twitter Cards 等社交分享预览图的工具品类。

---

## 材料范围

**材料范围**：公开网络检索（厂商文档、开发者博客、行业对比文）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 2026-05-20。

---

## 站内对照

待上线 Tools 页时对齐。

---

## Tools 关键词与 slug 映射

尚未录入 `tools-pages-config`。

---

## 与相邻 slug 分流

| Slug | 品类 | 差异 |
|------|------|------|
| **`social-cards-generator`** | 社交分享预览图生成 | 产出 1200×630 OG 图片/Twitter Cards，面向链接分享场景 |
| `image-generator` | 通用文生图/图生图 | 面向创作场景（艺术、设计、摄影），非特定于社交分享尺寸 |
| `logo-generator` | Logo 设计 | 产出品牌标志，使用场景和尺寸规范完全不同 |
| `presentation-maker` | 演示文稿 | 产出多页幻灯片，非单张社交卡片 |

---

以下条目可任意顺序阅读；**不是**文章体例，无叙事主线。

---

## 词汇锚点

- **Open Graph (OG) Image**：社交平台分享链接时显示的预览图片，标准尺寸 1200×630px。由 Facebook 在 2010 年提出，现已成为 Twitter/X、LinkedIn、Slack、Discord 等平台的通用约定。通过 HTML `<meta property="og:image">` 标签引用。
- **Twitter Card**：Twitter/X 对链接预览卡片的总称。分为 summary（小图）、summary_large_image（大图）、player（视频/音频）、app（应用推广）四种类型。通过 `<meta name="twitter:card">` 标签指定。
- **Satori**：Vercel 开源的 JSX→SVG 渲染引擎，是 `@vercel/og` 和 `next/og` 的核心。支持 flexbox 布局和自定义字体，输出 SVG 后通过 ReSVG 转换成 PNG。
- **Social Preview**：链接在社交时间线上展示的完整卡片，包含图片、标题、描述和域名。OG Image 只是其中视觉最突出的部分。
- **Edge Generation**：在 CDN 边缘节点（如 Vercel Edge Functions）实时生成 OG 图片，避免预生成和存储成本，支持动态内容（如用户头像、实时数据）。
- **Programmatic OG Image**：通过代码/API 按需生成的 OG 图片，区别于设计师在 Canva/Figma 中手动设计的静态图片。核心价值在于规模化、个性化、自动化。
- **Meta Tag Preview**：模拟社交平台如何解析和展示页面 meta 标签的工具（如 Facebook Sharing Debugger、Twitter Card Validator）。用于调试 OG 图片和卡片效果。

---

## 问题域（为何会出现这类产品）

- **链接分享即品牌触点**：一个没有 OG 图片的链接在社交时间线上只是一段灰文字，点击率远低于带卡片预览的链接。据平台数据，带 OG 图片的分享链接点击率提升 30–70%。
- **规模化的矛盾**：内容型网站每篇文章都需要独立的 OG 图片。手动设计不可行——1000 篇文章就需要 1000 张图。自动生成成为刚需。
- **多平台碎片化**：Facebook OG、Twitter Card、LinkedIn、Slack、Discord、WhatsApp……每个平台对预览图片的解析规则和展示方式不同。一套 meta 标签通吃所有平台需要精确配置。
- **动态内容的实时需求**：含用户数据（头像、名称、实时分数）的 OG 图片必须在请求时生成，无法预先构建。Edge Functions 的出现使这成为可能。
- **SEO 与社交的交叉压力**：Google 搜索结果也展示 OG 图片；AI 搜索引擎（Perplexity、ChatGPT）在引用页面时同样会提取 OG 图片。OG Image 的质量间接影响 AI 搜索中的可见性。

---

## 能力栈（概念拆分）

- **渲染引擎**：底层技术决定输出质量和性能。Satori（JSX→SVG→PNG）是目前 Next.js 生态的标准方案；Puppeteer/Playwright（HTML→截图）更灵活但更重；Canvas API（纯浏览器端）零服务器成本。
- **模板系统**：定义 OG 图片布局的方式。从代码内 JSX 模板（`@vercel/og`）、可视化编辑器（Bannerbear、Placid）、到 JSON 配置（Pixelixe）。
- **字体处理**：OG 图片中的文字渲染需要字体文件。方案包括 Google Fonts 在线加载、本地字体文件嵌入（增加 bundle 体积）、或系统字体回退。
- **缓存策略**：动态生成的 OG 图片需要合理缓存。CDN 缓存（`Cache-Control`）、文件名哈希、或专用的图片 CDN（如 `ogimg.xyz` 内置缓存）。
- **Meta 标签同步**：OG 图片必须与页面的 `og:title`、`og:description`、`twitter:card` 等标签协调一致。工具应覆盖图片生成 + 标签管理，而非只做图片。
- **多平台适配**：不同平台对 OG 图片的裁剪和处理不同。LinkedIn 截取中间区域、Twitter 展示全图、Discord 强制 4:3。好的工具提供平台预览或自动适配。
- **AI 辅助设计**：AI 根据页面内容自动生成布局、配色和图标选择，降低模板设计门槛（如 OpenGraph.xyz、OGimagen、Oginify）。

## OG 与 Twitter Card 标签规范

Social Cards Generator 产出的图片最终通过 HTML meta 标签被社交平台消费。理解标签规范是评估工具输出质量的必要条件。

### Open Graph 必需标签

OG 协议由 Facebook 2010 年提出，现已成为跨平台链接预览的标准。

| 标签 | 约束 | 说明 |
|------|------|------|
| `og:title` | ≤60 字符 | 页面标题，需与 `<title>` 内容一致 |
| `og:description` | 150–200 字符 | 页面描述，含隐含 CTA |
| `og:image` | 1200×630px，绝对 HTTPS URL | 最重要的标签——决定卡片视觉效果 |
| `og:url` | 规范 URL，绝对 HTTPS | 用于社交去重和分享计数 |

**强烈推荐的补充标签**：`og:type`（website/article/product）、`og:site_name`（品牌名）、`og:image:width/height`（避免渲染闪烁）、`og:image:alt`（无障碍描述）、`og:locale`（如 zh_CN、en_US）。

**Article 类型专用**：当 `og:type="article"` 时，可用 `article:published_time`、`article:modified_time`、`article:author`、`article:section`、`article:tag`。

### Twitter Card 四种类型

X（Twitter）使用专有的 `twitter:` 命名空间。若缺少 Twitter 标签，X 会回退读取 OG 标签。

| 类型 | 图片展示 | 适用场景 |
|------|---------|---------|
| `summary` | 小方形缩略图 | 基本链接分享 |
| `summary_large_image` | 大图横幅（全宽） | **推荐**——文章、博客、产品页 |
| `app` | 应用推广卡片 | 移动应用推广 |
| `player` | 内嵌播放器 | 视频/音频内容 |

Twitter `summary_large_image` 的官方宽高比为 2:1（1200×675px），但业界实用共识使用 1.91:1（1200×628px）以兼容 OG 标准。

### 标签一致性规则（最易出错的交叉检查项）

| 维度 | 要求 |
|------|------|
| `og:title` ↔ `twitter:title` ↔ `<title>` | 三处使用**完全相同**的字符串 |
| `og:description` ↔ `twitter:description` ↔ `<meta description>` | 同上 |
| `og:url` ↔ `<link rel="canonical">` | 指向同一 URL |
| `og:image` ↔ `twitter:image` | 可用同一张 1200×630 图 |

**最佳实践**：OG 和 Twitter 两个协议都配置。Twitter 标签精确控制 X 展示效果，OG 标签作为跨平台回退。

---

## 平台尺寸与约束

### 黄金尺寸：1200×630px

所有平台均可使用同一张 1200×630px（1.91:1）图片。这是 Facebook 2010 年设定的原始标准，此后所有平台都采用或兼容此尺寸。

| 平台 | 推荐尺寸 | 比例 | 最大文件 |
|------|---------|------|---------|
| Facebook | 1200×630 | 1.91:1 | 8 MB |
| LinkedIn | 1200×627 | 1.91:1 | 5 MB |
| X/Twitter (large card) | 1200×628* | 1.91:1（官方 2:1） | 5 MB |
| Slack | 1200×630 | 1.91:1 | ≤5 MB |
| Discord | 1200×630 | 1.91:1 | 8 MB |
| WhatsApp | 1200×630 | 1.91:1 | **300 KB** |
| Telegram | 1200×630 | 1.91:1 | 10 MB |
| iMessage | 1200×630 | 1.91:1 | 无上限 |
| Pinterest | **735×1102**（竖版） | 2:3 | Rich Pins 横竖兼容 |

*\*X 官方指定 `summary_large_image` 宽高比 2:1（1200×675px）。1200×628 是业界实用共识，使用时将关键内容居中即可避免裁切。*

### 文件格式

| 格式 | 推荐度 | 说明 |
|------|-------|------|
| PNG | **首选** | 文字、Logo、图形——所有平台完美支持 |
| JPEG | 可用 | 照片类，文件更小 |
| WebP | 谨慎 | 大部分平台已支持，但 LinkedIn 部分版本和部分 SEO 插件仍拒绝 |
| SVG | **禁用** | 所有平台静默忽略 |

### WhatsApp 特殊约束

WhatsApp 是最严格的平台，超出限制会**静默删除整个链接预览**：

| 字段 | WhatsApp 限制 | 通用推荐 |
|------|-------------|---------|
| `og:title` | **≤35 字符** | ≤60 字符 |
| `og:description` | **≤65–155 字符** | 150–200 字符 |
| `og:image` | **≤300 KB**（超限则完全不显示） | <1 MB |

### 设计安全区

平台会在不同上下文中裁剪卡片边缘。保留**所有方向 60px 的安全边距**，有效内容区域 1080×510px。在 1200px 画布上：标题 ≥48px，副标题 ≥28px，标题最多 2-3 行。

---

## 测试与调试

| 平台 | 工具 | URL |
|------|------|-----|
| Facebook | Sharing Debugger | https://developers.facebook.com/tools/debug/ |
| X (Twitter) | Card Validator | https://cards-dev.twitter.com/validator |
| LinkedIn | Post Inspector | https://www.linkedin.com/post-inspector/ |
| 多平台综合 | OpenGraph.xyz Checker | https://www.opengraph.xyz |

**调试要点**：
- 修改后必须点击"Scrape Again"刷新缓存，否则平台缓存持续 24-72 小时
- 图片 URL 可加查询参数 `?v=2` 强制平台重新抓取
- 图片必须可公网访问（无防盗链、无登录要求、无 CORS 阻止）
- 标签必须在 SSR/SSG 阶段注入 HTML，仅靠客户端 JS 渲染无效

---

## 常见错误

| 错误 | 后果 | 正确做法 |
|------|------|---------|
| 相对路径 `og:image="/img/og.png"` | 所有平台不显示图片 | 始终使用 `https://` 绝对 URL |
| 图片 <600×315px | Facebook 拒绝展示大图 | 至少 1200×630px |
| 方图（1:1）用作 OG 图 | 边缘被大幅裁剪 | 使用 1.91:1 横版图 |
| 缺少 `og:image:width/height` | 卡片渲染闪烁/延迟 | 补全尺寸声明 |
| 所有页面用同一张 OG 图 | 分享任何页面都显示相同卡片 | 每页唯一定制 |
| WhatsApp 场景图片 >300KB | 卡片不显示图片 | 压缩或同时提供轻量版 |
| 生成工具输出 WebP | LinkedIn 等平台不兼容 | 转 PNG 或 JPEG |
| SVG 作为 OG 图片 | 所有平台静默忽略 | 使用位图格式 |

---

## 形态谱系（与具体品牌解耦）

1. **开发者库 / SDK** —— 嵌入项目代码中，通过函数调用生成 OG 图片。代表：`@vercel/og`、`satori` + `resvg`、`@ogify/core`。优势：完全控制、无第三方依赖、Edge 原生。门槛：需开发能力。
2. **托管 API 服务** —— 通过 HTTP API 提交参数获得图片 URL。代表：`ogimg.xyz`、Pixelixe、Bannerbear API、Placid API。优势：零部署、内置缓存和 CDN。门槛：按量付费、有网络延迟。
3. **可视化模板编辑器 + API** —— 拖拽设计模板后通过 API 填充变量生成图片。代表：Bannerbear、Placid、DynaPictures、Templated.io。优势：设计团队可独立维护模板。门槛：较高的订阅费用。
4. **浏览器端生成器** —— 纯前端工具，在浏览器中通过 Canvas API 合成图片。代表：CardForge、hidekazu-konishi 的 OG Generator。优势：零服务器成本、无数据泄露。局限：无法集成到自动化流程。
5. **CMS 插件** —— 嵌入 WordPress 等内容管理系统，自动为每篇文章生成 OG 图片。代表：OpenGraph.xyz（WP 插件）、OG Pilot。优势：即装即用、与 CMS 深度集成。局限：锁定平台。
6. **AI 驱动生成器** —— 通过 AI 分析页面内容自动设计 OG 图片布局。代表：OGimagen（AI + MCP 集成）、OpenGraph.xyz（AI 模板创建）、SEO Image Gen（LobeHub）。优势：零模板设计工作。局限：输出一致性依赖 AI 质量。

---

## 风险 · 合规 · 治理

- **字体授权**：OG 图片中使用的字体需要合法的商业授权。Google Fonts 等开源字体可安全使用，商业字体需确认覆盖「图片生成」场景。
- **图片版权**：OG 图片中引用的背景图、插图、Logo 必须拥有使用权。自动生成工具可能从网络抓取图片，需注意版权风险。
- **缓存与时效**：动态 OG 图片的 CDN 缓存可能导致旧内容展示。策略上应使用内容哈希作为缓存键，或在内容更新时主动 purge 缓存。
- **性能开销**：OG 图片生成消耗服务器计算资源（特别是 Puppeteer/Playwright 方案）。在流量高峰时可能成为性能瓶颈。Edge Functions + Satori 方案资源消耗相对可控。
- **可访问性**：OG 图片中的文字信息应同时在 `og:title`/`og:description` 中提供，不能只依赖图片传达关键信息。

---

## 落地碎片

- 优先采用 Edge 方案（Satori + Vercel Edge）而非 Puppeteer 截图，前者冷启动快 10–50 倍。
- 为生产环境配置多级缓存：CDN 层（长时间缓存）+ 应用层（内容变更时失效）+ 浏览器层（短时间缓存）。
- 字体文件是 OG 图片生成的瓶颈——限制每张图片使用的字重数量（建议 ≤2），优先使用系统字体或 Google Fonts。
- 使用 `opengraph-image.tsx` 约定（Next.js App Router）可零配置为每个路由生成动态 OG 图片。
- 用 Facebook Sharing Debugger 和 Twitter Card Validator 验证最终效果，不要仅依赖本地预览。
- OG 图片尺寸严格保持 1200×630px（1.9:1 比例），避免平台裁剪导致关键信息丢失。
- 在 OG 图片中叠加品牌 Logo 和 URL，即使图片被单独保存也能追溯来源。

---

## 工具与产品类型

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|-------------|------|
| **开发者 SDK/库**（OG image library, social card SDK） | `@vercel/og`, Satori + resvg, `@ogify/core` | 嵌入项目代码，函数调用生成——完全控制、Edge 原生、需开发能力 |
| **托管 API 服务**（OG image API, dynamic og image） | ogimg.xyz, Pixelixe, Bannerbear API, Placid API | 通过 HTTP API 提交参数获得图片 URL——零部署、内置缓存和 CDN |
| **可视化模板编辑器**（OG image template editor, social card designer） | Bannerbear, Placid, DynaPictures, Templated.io | 拖拽设计模板后通过 API 填充变量——设计团队可独立维护模板 |
| **CMS 插件**（WordPress OG plugin, social card plugin） | OpenGraph.xyz WP 插件, OG Pilot | 自动为每篇文章生成 OG 图片——即装即用、与 CMS 深度集成 |
| **AI 驱动生成器**（AI OG image, AI social card） | OGimagen（AI + MCP 集成）, OpenGraph.xyz AI, SEO Image Gen | AI 自动设计布局——零模板设计工作但一致性依赖 AI 质量 |

---

### 对比与测评（第三方；观点非官方）

2026 年社区对 OG 图片生成工具的讨论集中在三个维度：(1) **Edge 运行时性能**——Satori + Vercel Edge 方案冷启动 <50ms 对比 Puppeteer/Playwright 方案 >1s，边缘生成是生产环境的首选架构；(2) **可视化 vs 代码**——Bannerbear/Placid 等可视化编辑器降低了非开发者的进入门槛，但 API 调用成本和模板灵活性上限不及自建方案；(3) **AI 辅助设计的可用性**——OGimagen 等 AI 工具可以自动生成布局，但多篇文章的品牌一致性仍然需要人工模板约束。社区共识：高流量内容站优先自建 Edge 方案（`@vercel/og` + Next.js），小团队和个人优先用可视化托管 API。*网摘综合，非 Alignify 实测。*

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Vercel OG Image** | Vercel 开源的 OG 图片生成库，Satori 渲染 | [github.com/vercel/og-image](https://github.com/vercel/og-image) |
| **Satori** | Vercel 的 HTML→SVG 渲染引擎，OG 图片生成核心依赖 | [github.com/vercel/satori](https://github.com/vercel/satori) |
| **Open Graph Protocol** | Facebook 的 OG 标签规范，social cards 的事实标准 | [ogp.me](https://ogp.me/) |
| **Twitter Cards** | X/Twitter 的社交卡片规范文档 | [developer.x.com](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/markup) |
