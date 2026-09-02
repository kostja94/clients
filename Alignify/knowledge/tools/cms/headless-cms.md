# Headless CMS / 无头内容管理系统 · 知识块（非线性笔记）

**材料范围**：公开网络检索（MDN、Contentful / Sanity / Strapi / Payload / Storyblok / Hygraph / Tina 官方文档；TechTarget、CMSWire、W3Techs、MACH Alliance、Figma Config 2025、Replatform Radar 2026-07 研究；Playwright 官方文档）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-08-28**。

**站内对照**：待上线正式页时对齐（新文优先 **`/blog/headless-cms`** · **`/zh/blog/headless-cms`**）· slug **`headless-cms`**

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 `#headless-cms-tools`）· `keywordEn`: **Headless CMS / API-first CMS** · `keywordZh`: **无头 CMS / API 优先内容管理**

**主题簇**：[README.md](./README.md) · Hub：[content-management-system.md](./content-management-system.md) · 路由 SSOT：[website-builder.md §簇级 FAQ](../website-builder/website-builder.md#簇级-faq)

**站内相邻**（CMS 簇）：[open-source-cms.md](./open-source-cms.md)（OSS 选型）· [enterprise-cms.md](./enterprise-cms.md) · [website-builder.md](../website-builder/website-builder.md)（builder Hub）· [blog-website-builder.md](../website-builder/blog-website-builder.md) · [app-builder.md](../coding/app-builder.md)

**站内相邻**（Tools · 簇外）：[headless-browser.md](../web-data/headless-browser.md) · [geo.md](../search-geo/geo.md)

**站内相邻**（跨频道 · 已发布）：[如何不用 CMS，用 AI 搭建博客](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai)（Sanity/API vs 无 CMS 选型）· [主域名下的分块建站](https://alignify.co/blog/subdirectory-hosting) · [AI 组件（Vibe + Headless 前端）](https://alignify.co/blog/ai-components)

## 与相邻 slug 分流

> Builder 簇对照与 FAQ → **[website-builder §分流](../website-builder/website-builder.md#与相邻-slug-分流)** · **[§簇级 FAQ](../website-builder/website-builder.md#簇级-faq)**。CMS 簇边界 → [README](./README.md)。

| 维度 | **`headless-cms`（本文）** | **`website-builder`** | **`blog-website-builder`** |
|------|---------------------------|----------------------|----------------|
| 典型买家问题 | 结构化内容放哪、前端怎么接 API？ | 帮我做一个能上线的网站 | 博客/专栏怎么写、发、被订阅？ |
| 交付形态 | Content API + Studio/Admin | 托管整站 + 可视化编辑器 | 文章时间线 +（可选）Newsletter |
| 展示层 | **无绑定**；前端自选 Next/Nuxt 等 | **内置**主题/画布/组件 | 一体主题 / 出版流 |
| 验收核心 | Schema、Preview、Webhook、多通道 | 视觉、托管、转化 | 发稿流、SEO/RSS、所有权 |

| 你的问题 | 看哪个 slug |
|----------|-------------|
| 「Contentful 和 Webflow 有什么区别？」 | **本页** vs [`website-builder`](../website-builder/website-builder.md)（亦见 Hub FAQ） |
| 「Next 博客：CMS API 还是 Git MDX？」 | API → **本页**；Git **博客** → [`blog-website-builder` Type E](../website-builder/blog-website-builder.md#形态谱系type-定义--产品见-工具与产品类型) |
| 「headless 是不是无头浏览器？」 | **不是** → [`headless-browser`](../web-data/headless-browser.md) |
| 「Shopify Hydrogen 算不算 headless？」 | [`ecommerce-website-builder`](../website-builder/ecommerce-website-builder.md) §Headless + **本页** |
| 「公开 WordPress 博客还是 Headless？」 | [`blog-website-builder`](../website-builder/blog-website-builder.md) vs **本页** |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Headless CMS / 无头 CMS**：**无内置展示层（presentation layer）** 的内容管理系统；编辑后台（CMA）与内容存储经 **REST / GraphQL 等 API** 交付，由 Next.js、Nuxt、Astro、移动 App 等**自行渲染**。与 **Traditional / Coupled CMS**（WordPress 主题、Webflow 画布）相对。
- **成文：嵌入演进脉络（非独立 History H2）**：术语 = 砍掉 presentation **head**；~2010s JAMstack/mobile API → Contentful/Prismic 主流化；~2020s MACH/composable → 进 RFP；2025+ 检索降温 → 买家问 **迁移 SEO + Preview 治理**。正式文 1 段收束到 checklist；`#types` 可附 3 行阶段表。全品类编年 → hub `content-management-system`。
- **与 headless-browser 的区分（必消歧）**：**Headless browser** = 无 UI 的浏览器进程（Playwright/Chromium headless shell），供 E2E 测试与 Agent 自动化；**Headless CMS** = 无「网站头部/前端」的内容 API。**Headless** 在两条赛道里是不同隐喻，检索与 slug 均勿混用 → [`headless-browser`](../web-data/headless-browser.md)。
- **CMS（Content Management System）**：创建、编辑、协作、发布与存储数字内容的软件（含图片、视频、交互代码等）（[MDN — CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS)）。
- **CMA / CDA**：**Content Management Application**（编辑界面）与 **Content Delivery Application**（存储与对外交付）；Headless 保留 CMA+CDA，**剥离**与页面模板绑定的 presentation。
- **Traditional / Monolithic CMS**：CMA 与主题/模板 **紧耦合**；常见 LAMP/PHP 路径输出 HTML（WordPress 经典、Drupal 传统模式）。
- **Decoupled / Hybrid / API-first / Git-based / MACH**：见上表与 [TechTarget](https://www.techtarget.com/enterprise-software/feature/Headless-CMS-vs-decoupled-CMS-Whats-the-difference)、[Strapi API-first](https://strapi.io/blog/api-first-cms)。
- **Visual Builder / DAM·ECM 边界**：Webflow 等 → [`website-builder`](../website-builder/website-builder.md)；DAM/ECM/CCMS 非 WCM 同义词。

---

## 专题对照：架构 × 建站 × 内容存储

> 术语定义见 §词汇锚点；Hub 概念三问见 [`content-management-system`](./content-management-system.md#概念基线三问ssot)。下表只列**买家体验差**。

| 维度 | **Headless CMS（API SaaS/OSS）** | **Coupled / Visual Builder** | **Traditional CMS** | **Git-based** |
|------|----------------------------------|------------------------------|---------------------|---------------|
| 展示层 | 前端自建 | **平台内置** | 主题/插件 | SSG/SSR 读 repo |
| 典型买家 | 工程+营销协作、多渠道 | 设计/营销要快速整站 | 插件生态、低成本 WCM | 工程主导、PR 审稿 |
| SEO 责任 | **前端** SSR/SSG/ISR | 平台模板 + 托管 | 主题 + 插件 | 构建模板 |
| 运行时 API | **是**（REST/GraphQL） | 部分（Webflow Cloud 等） | 可选（WPGraphQL） | 多为构建期 |
| 平台锁定 | schema/API 迁移成本 | **强**（画布/托管） | 中（数据可迁，主题重写） | **低**（Git） |
| Alignify slug | **`headless-cms`** | **`website-builder`** | [`open-source-cms`](./open-source-cms.md) | 本页 Type C |

---

## 问题域

- **全渠道内容复用**：同一产品描述、Blog、落地页需 Web、App、邮件、IoT 同步——Traditional 主题难覆盖；Headless 以 **content hub + 多前端** 解决。
- **前端栈自由与性能**：团队已选 Next/Nuxt/Astro，不愿被 PHP 主题或 builder 运行时束缚；SSG + CDN 与 **Core Web Vitals** 对齐（实现不当的 CSR Headless 反而伤害 SEO——见风险节）。
- **编辑体验 vs 工程 schema**：非技术编辑要 Studio；工程要 TypeScript schema、版本化 model——Sanity/Payload **schema-as-code** 回应此张力。
- **Composable 采购**：Gartner 退役 WCM MQ → DXP；2026 ≥70% 组织须 composable DXP（CMSWire 引 Gartner）。单买 Headless **≠** 完整 DXP。
- **W3Techs CMS 总盘**：WordPress 等份额见 [`blog-website-builder` §市场份额快照](../website-builder/blog-website-builder.md#市场份额快照w3techs--2026-08--占已知-cms网站)（含 Shopify/Wix 等 **非 Headless** 路径）。
- **2026 搜索趋势**：Replatform Radar 测 US 15 个 headless/composable/DXP 词，2025-03 峰值后 **-33%**（买家或已从「搜定义」转向「做迁移」）。
- **Agent 内容操作**：Sanity 双 MCP（写/读分离）；Git-based 则 **Agent 开 PR 改 MDX**。

---

## 能力栈（概念维度）

- **Modeling & API**：schema 灵活度；REST / GraphQL / GROQ；SSG 构建期 vs SSR 运行时。
- **Preview & workflow**：pure headless 常缺原生 preview；draft/publish 环境隔离、`noindex`。
- **Webhook & SEO**：ISR `revalidate`；slug→路由/sitemap 单一事实源。
- **Visual / Federation / Agent**：Storyblok Bridge；Hygraph Remote Sources；Sanity 双 MCP（写/读分离）。
- **迁移 & lock-in**：model/富文本定制；ETL + 前端重写成本。

---

## 形态谱系（Type 定义 · 产品见 §六产品速览 / §工具与产品类型）

- **Type A — Headless SaaS**：少运维、多渠道、REST/GraphQL API。
- **Type B — OSS 自托管**：数据主权；DevOps 自负。
- **Type C — Git-based CMS**：Content-as-Code；与 **Git 博客**（[`blog-website-builder` Type E](../website-builder/blog-website-builder.md#形态谱系type-定义--产品见-工具与产品类型)）买家问题重叠时分流：要 **API + Studio** → 本页；要 **repo + PR 审稿发博客** → blog-website-builder。
- **Type D/E — Hybrid / Traditional+API**：Sitecore、AEM、WordPress+WPGraphQL；渐进迁移。
- **Type F — Coupled Builder（非 Headless · SSOT）**：Webflow、Framer、Wix 内置画布与托管 → [`website-builder`](../website-builder/website-builder.md)。**Webflow/Framer ≠ Headless** 以此为准。

---

## 六产品速览（2026 · 旗舰 SSOT；非排名）

> 完整 URL 与官方一句话见 **§外链索引**；OSS 深度见 [`open-source-cms`](./open-source-cms.md)。

| 产品 | 差异化 | 2026 注记 |
|------|--------|-----------|
| **Contentful** | 企业 API 生态、治理 | MACH + AI 结构化内容 |
| **Sanity** | GROQ、schema-as-code、实时协作 | **双 MCP**（写 Server / 读 Context） |
| **Strapi** | OSS 自托管、插件 | **Strapi 5**（Vite、全 TS、Document Service API） |
| **Payload** | Next/TS 同仓、code-first | **2025-06 加入 Figma**；OSS 承诺保留 |
| **Storyblok** | **Visual Editor**、组件块 | 营销编辑 UX 领先 |
| **Hygraph** | GraphQL + **Content Federation** | Remote Sources 联外源 |

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **SEO / AEO 反模式**：Headless + **纯 CSR** → 首响 HTML 缺 meta/canonical；AEM→Headless 迁移若丢 schema/redirect，AI Overviews 引用可静默转向竞品（Replatform Radar 2026 系列）。须 **SSG/ISR/SSR**（与 [`geo](../search-geo/geo.md) 可抓取性一致）。
- **Preview 泄漏**：预览 URL 未 `noindex`/未鉴权 → 草稿进索引；与生产 **canonical 冲突**。
- **Webhook 不同步**：CMS 已发布但前端未 rebuild → 404、旧 meta、sitemap 缺页。
- **Vendor lock-in**：content model、富文本、定制字段 → 迁移 **ETL + 前端模板重写**；试验期验证导出。
- **OSS 隐性 TCO**：Strapi/Payload 许可免费 ≠ 零成本——补丁、监控、升级；社区对 Strapi **localization/运维** 评价分化（HN Tier 2）。
- **迁移 SEO**：redirect map 先于设计；大型站再索引可 **3–6 个月**。
- **Scope 错位**：**≠** 内部 RAG / 开发者文档栈 → [README §不要放进本簇](./README.md#为什么单独成簇)。

---

## 落地碎片

- **选型第一问**：非技术编辑是否 **每天** 发稿？是 → Headless SaaS（Storyblok 偏 visual）或 Hybrid；否且重 Git diff → Git-based / MDX。
- **和 Webflow/Framer 的分叉**：要 **设计稿级整站 + 平台托管** → [`website-builder`](../website-builder/website-builder.md)；要 **Next 团队控 UI + 结构化 content API** → **Headless**。
- **Next.js 默认路径**：营销页 SSG/ISR + webhook `revalidate`；避免全站 CSR 拉 CMS。
- **Preview checklist**：独立域名或路径、`noindex`、token 隔离、与生产 API 分离。
- **slug 单一事实源**：CMS slug 驱动 `[slug]` 路由与 sitemap——**一处维护**。
- **混合架构**：落地页 Git；Blog/新闻 Headless——合理，但需 **两套发布流程** 文档化。
- **Agent 集成**：Sanity MCP / 官方 API 查 **draft vs published**；生产写入走 CI。
- **原型选型**：同一 schema 在多个平台做 mini POC，比纸面 RFP 有效（HN 共识）。

---

## 工具与产品类型（检索常混品类；非穷尽）

> **列举顺序**：见 [README §产品列举原则](./README.md#产品列举原则)。旗舰深度见 **§六产品速览**（SSOT）。

| 类型（英文常检索词） | 垂直优先（典型） | 横向 / 非 Headless（典型） | 备注 |
|---------------------|-----------------|---------------------------|------|
| **Headless SaaS** | **Contentful**, Sanity, Storyblok, Hygraph | — | 见 §六产品速览 |
| **OSS 自托管** | Strapi, Payload, Directus | — | 深度见 [**open-source-cms**](./open-source-cms.md) |
| **Git-based CMS** | Tina, Decap, Nuxt Studio | — | Type C；**Git 博客** → blog-website-builder Type E |
| **Hybrid DXP** | Sitecore, AEM, Optimizely | — | 企业 DXP |
| **Traditional + API** | WordPress + WPGraphQL | — | Type E |
| **Coupled visual builder** | — | Webflow, Framer, Wix | Type F → website-builder |
| **电商 headless storefront** | Shopify Hydrogen | Shopify Admin | → ecommerce §Headless |

### 按场景 → §六产品速览 / Type

| 若 PRIMARY 需求是… | 见 |
|-------------------|-----|
| 企业治理 + 成熟 API 生态 | §六产品速览 · Contentful |
| 结构化内容 + TS schema + Agent MCP | §六产品速览 · Sanity |
| 自托管 + 插件 | §六产品速览 · Strapi / Directus |
| Next.js 同仓 + code-first CMS | §六产品速览 · Payload |
| 营销编辑要 visual、少工程 | §六产品速览 · Storyblok |
| 多 API 源 GraphQL 联邦 | §六产品速览 · Hygraph |
| Git **博客**、MDX、PR 审稿 | [`blog-website-builder` Type E](../website-builder/blog-website-builder.md#形态谱系type-定义--产品见-工具与产品类型) |
| 设计驱动整站（不要 pure Headless） | Type F → website-builder |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **MDN — CMS** | CMS 术语 | [developer.mozilla.org/docs/Glossary/CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS) |
| **Contentful — Headless / MACH 2026** | 定义 + composable AI | [contentful.com/headless-cms](https://www.contentful.com/headless-cms/) |
| **Sanity — MCP / Context** | Agent 写/读分离 | [sanity.io/docs/ai/mcp-server](https://www.sanity.io/docs/ai/mcp-server) |
| **Strapi 5 / API-first** | v5 GA；vs Git-based | [strapi.io/blog/api-first-cms](https://strapi.io/blog/api-first-cms) |
| **Payload — Figma** | 2025-06 加入 Figma | [payloadcms.com/posts/blog/payload-is-joining-figma](https://payloadcms.com/posts/blog/payload-is-joining-figma) |
| **Storyblok / Hygraph / Tina** | Visual / Federation / Git | [storyblok.com/tp/headless-cms-explained](https://www.storyblok.com/tp/headless-cms-explained) |
| **TechTarget — Headless vs Decoupled** | 架构边界 | [techtarget.com/.../Headless-CMS-vs-decoupled-CMS](https://www.techtarget.com/enterprise-software/feature/Headless-CMS-vs-decoupled-CMS-Whats-the-difference) |
| **W3Techs / Playwright / Replatform Radar** | 份额 / browser 消歧 / 搜索趋势 | [w3techs.com](https://w3techs.com/technologies/overview/content_management/) |

### 对比与测评（第三方；观点非官方）

- **架构**：Headless 无展示层；Decoupled 有 optional head；Git-based 交付链不同（Strapi 官方）。
- **2026 增量**：Figma+Payload 设计→部署；Webflow visual-first vs Contentful API-first 买家分化；迁移泄漏点在 redirect/schema/CSR（Replatform Radar）。
- **HN（非事实源）**：Contentful  enterprise 定价摩擦；Strapi 运维分化；Payload DX 偏好。

*网摘综合，非本站实测。*

---

## 延伸阅读 · 站内外

**站外**（产品 URL 见 §外链索引）

- [CMSWire — DXP 2026 / Headless Grows Up / Gartner WCM MQ](https://www.cmswire.com/digital-experience/what-you-need-to-know-about-digital-experience-platforms/)
- [CMSWire — Figma Payload deal](https://www.cmswire.com/digital-experience/when-cms-meets-ux-design-what-figmas-payload-deal-really-means/)
- [InfoQ — Nuxt Studio OSS (2026-02)](https://www.infoq.com/news/2026/02/nuxt-studio-cms/)
- [Replatform Radar — platform shopping cooled / AEM→Headless](https://replatformradar.com/blog/platform-shopping-has-cooled)

**站内 / 底稿**

- 网搜底稿：[headless-cms-web-search-2026-08-28.md](../../../temp/headless-cms-web-search-2026-08-28.md)

---

*档位：B · KB only（发文走 `/blog/headless-cms`）· Territory：编程工具链 · 刷新 2026-08-28*