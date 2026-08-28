# 深度搜索报告 — Headless CMS / API-first 内容管理

> **检索基准日**：2026-08-28  
> **时间范围**：2024–2026（侧重 2025–2026 产品/行业动态）  
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档（仅读 spec、KB 模板与既有 slug/交叉链接列表）  
> **Loop 轮次**：6 轮  
> **来源统计**：Tier 0 18 · Tier 1 12 · Tier 2 6  
> **置信度摘要**：概念基线三问（Q1–Q3）已由 Tier 0/1 多源互证；2026 增量（Payload→Figma、Sanity MCP、Replatform Radar 搜索曲线）以官方 + Tier 1 为主；社区舆情仅作观点层。

---

## 1. 执行摘要

**Headless CMS** 是**无内置展示层**的内容管理系统：后台建模/编辑/存储，经 **REST / GraphQL 等 API** 向 Web、App、IoT 等渠道交付结构化内容；与 **Traditional / Coupled CMS**（WordPress 主题、Webflow 画布）相对，也与 **headless browser**（Playwright 无 UI 浏览器自动化）**完全不同隐喻**——检索时必须消歧。

按架构分类（TechTarget / Contentful 互证）：**Traditional**（前后端紧耦合）→ **Decoupled**（分离但保留可选原生前端/预览）→ **Headless**（无 presentation layer，前端完全自建）。另有 **Git-based**（Markdown/MDX 存 repo，构建期交付）与 **API SaaS Headless** 并列，Strapi 官方区分 **API-first** 与 Git 交付模型。

**市场份额（W3Techs，2026-08）**：WordPress 占已知 CMS **58.9%**（占全部网站 40.7%）；Shopify **7.7%**、Wix **6.1%**——W3Techs 将建站 SaaS、SSG 等一并计入「CMS」，**不等于** Headless API-first 采用度。Born-headless 代表：**Contentful、Sanity、Strapi、Payload、Storyblok、Hygraph** 等分场景领先（企业治理 / 结构化 DX / 自托管 OSS / Next.js 同仓 / 可视化编辑 / GraphQL 联邦）。

**2026 行业增量**：① **MACH / composable** 从「选型话术」进入 **AI-ready 结构化内容 + API 编排**（Contentful 2026 MACH 文、MACH Alliance 2026 Open/Composable/Connected 原则）；② **Payload 加入 Figma**（2025-06-17，Tier 0），OSS 承诺保留，与 Figma Sites 设计→部署闭环；③ **Sanity** 双 MCP（写操作 MCP Server + 只读 Sanity Context for 生产 Agent）；④ **Strapi 5 GA**（2024-09-23）Vite + 全 TypeScript + Document Service API；⑤ **Replatform Radar**（2026-07）测得 US「headless/composable/DXP/enterprise CMS」类搜索量自 **2025-03 峰值降约 33%**——解读为 hype 回落 + 买家进入迁移执行期 + 部分定义类 query 转向 AI 助手（著者自述未直接证伪/证实 AI 替代）。

**社区反响（Tier 2）**：HN 对 Contentful **贵/enterprise 销售摩擦**、Strapi **自托管运维与 localization 分化**、Payload **开发者体验偏好** 并存；**争议焦点**仍是 preview/SEO（CSR 空壳）、迁移 SEO/AEO、vendor lock-in 与 OSS TCO。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `what is headless CMS site:contentful.com`; `headless vs decoupled site:techtarget.com`; `site:w3techs.com CMS`; `MACH Alliance composable 2026` | Q1–Q3 骨架：定义、架构类型、W3Techs 份额 |
| R2 | `Contentful Sanity Strapi Payload Storyblok Hygraph comparison`; `Gartner WCM Magic Quadrant retired site:cmswire.com`; `Payload Figma acquisition`; `Replatform Radar headless migration` | Payload→Figma；Gartner WCM MQ 退役→DXP；迁移 SEO 风险叙事 |
| R3 | `site:news.ycombinator.com headless CMS`; `headless browser Playwright site:playwright.dev`; `Sanity MCP server 2026` | headless-browser 消歧；Sanity 双 MCP；HN 选型观点 |
| R4 | `Webflow headless CMS site:cmswire.com`; `Hygraph content federation`; `Storyblok visual editor`; `Strapi 5 release site:strapi.io` | Webflow 次世代 CMS + 可视化/API 混合；Hygraph 联邦；Strapi 5 细节 |
| R5 | `Tina CMS git-based site:tina.io`; `platform shopping cooled replatformradar` | Git-based Tina；Replatform Radar 搜索量完整数据表 |
| R6 | `headless CMS git-based vs API`; `CMSWire headless content infrastructure 2026`; `Forrester replatforming 2026` | API-first vs Git 边界（Strapi 官方）；买方「小改而非大迁移」趋势互证 |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线三问：Q1 Headless CMS 是什么 | `headless CMS definition Contentful TechTarget MDN` | 已覆盖 |
| 概念基线三问：Q2 有哪些类型 | `headless vs decoupled vs traditional`; `git-based CMS` | 已覆盖 |
| 概念基线三问：Q3 知名产品/方案 | `W3Techs CMS`; `Contentful Sanity Strapi…` | 已覆盖（份额用 W3Techs；Headless 细分无单一权威份额表） |
| vs Coupled builder（Webflow/Framer/Wix） | `Webflow CMS overhaul CMSWire 2026` | 已覆盖 |
| vs Git-based CMS | `Tina CMS git`; `Strapi API-first vs git` | 已覆盖 |
| vs headless-browser | `Playwright headless browser` | 已覆盖 |
| MACH / composable | `MACH Alliance 2026`; `Contentful MACH 2026` | 已覆盖 |
| Replatform Radar 搜索趋势 | `platform shopping cooled replatformradar` | 已覆盖（单源 primary research，见 §8） |
| 六产品对比（Contentful/Sanity/Strapi/Payload/Storyblok/Hygraph） | 厂商官方 + CMSWire + NetGuru | 已覆盖 |
| 社区反响 | `site:news.ycombinator.com headless CMS` | 已覆盖（Tier 2） |
| 中文轴 | 未单独跑 Round 1b | 权威源未覆盖（本次 EN-first；核心事实不依赖中文二手稿） |

---

## 4. 核心发现（多源验证）

### 4.1 Headless CMS 是什么

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 分离 presentation layer 与 content backend，经 API 交付 | [Contentful — Headless CMS](https://www.contentful.com/headless-cms/) T0 | [TechTarget — Definition](https://www.techtarget.com/enterprise-software/definition/What-is-a-headless-content-management-system-headless-CMS) T1 | 已确认 |
| CMS 广义：创建、组织、发布数字内容（含图片/视频/交互代码） | [MDN — CMS Glossary](https://developer.mozilla.org/en-US/docs/Glossary/CMS) T0 | [Wikipedia — Headless CMS](https://en.wikipedia.org/wiki/Headless_content_management_system) T2* | 已确认 |
| **≠ headless browser**：CMS 的 headless = 无网站「头/前端」；browser 的 headless = 无 UI 的浏览器进程 | [Playwright — Browsers](https://playwright.dev/docs/browsers) T0 | [Strapi — API-first CMS](https://strapi.io/blog/api-first-cms) T0 | 已确认 |

Headless CMS 将 **CMA（编辑/建模）** 与 **CDA（存储/API 交付）** 保留在平台侧，**展示层（head）由 Next.js、Nuxt、移动 App 等自建**。Contentful 强调：Traditional CMS 内容「缠在代码与模板里」，Headless 使内容可独立管理、多通道部署。Adobe 口径：内容以 JSON 经 GraphQL/REST 暴露，**presentation 由品牌自选技术栈**（[Adobe — headless CMS overview](https://business.adobe.com/blog/basics/a-brief-overview-of-headless-cms) T0）。

**与相邻概念**：**DAM/ECM/CCMS** 非 WCM 同义词；**Visual Website Builder**（Webflow/Wix）主路径是画布+托管，非 API-first Headless（见 §4.4）。

### 4.2 Headless CMS 有哪些类型

**分类依据**：权威来源普遍按 **架构耦合度 × 交付/部署模型** 划分（TechTarget、Contentful、Strapi）。

| 类型（分类依据：架构） | 特征 | 典型场景 | 来源 |
|------------------------|------|----------|------|
| **Traditional / Monolithic** | CMA+主题/模板一体；服务端组 HTML | 单站 WCM、插件生态 | TechTarget T1 |
| **Decoupled** | 后台独立，**保留可选原生前端/模板/预览** | 渐进迁移、要 WYSIWYG 预览 | TechTarget T1; Contentful T0 |
| **Headless（pure-play）** | **无** presentation layer；仅 API | 多渠道、前端栈自选 | TechTarget T1; Contentful T0 |
| **Hybrid / Enterprise DXP** | 传统渲染 + Headless API 双轨 | 大企业营销栈、个性化 | CMSWire DXP 2026 T1 |
| **Traditional + API 出口** | 保留主题，另开 REST/GraphQL | WordPress + WPGraphQL 渐进式 | TechTarget T1 |

**按部署/内容存储（Strapi 官方维度）**：

| 类型 | 特征 | 代表方向 | 来源 |
|------|------|----------|------|
| **Headless SaaS（API-first）** | 托管 Content API + Studio | Contentful, Sanity, Storyblok, Hygraph | 厂商 T0 |
| **OSS 自托管** | 数据主权；DevOps 自负 | Strapi, Payload, Directus | Strapi/Payload T0 |
| **Git-based / Content-as-Code** | Markdown/MDX 在 repo；构建期交付；可选可视化 Studio | Tina, Decap, Nuxt Studio | Tina T0; InfoQ Nuxt Studio T1 |

**易混淆点**：Decoupled 与 Headless 常被混称，但 **Decoupled 仍有「可选 head」**；Headless **完全不提供** 绑定展示层（Contentful、TechTarget 一致）。Git-based 可称 headless（无绑定前端），但 **运行时 API 模型不同**（Strapi 明确：API-first ⊂ headless，Git 交付是另一分支）。

### 4.3 知名产品 / 代表方案

**全球网站 CMS 使用量（≠ Headless 份额）** — [W3Techs，2026-08](https://w3techs.com/technologies/overview/content_management/) T0：

| 产品 | 占已知 CMS | 占全部网站 | 备注 |
|------|-----------|-----------|------|
| WordPress | 58.9% | 40.7% | 传统+可 headless 出口 |
| Shopify | 7.7% | 5.3% | 电商 SaaS；storefront 可 headless |
| Wix | 6.1% | 4.2% | 耦合建站 |
| Webflow | ~1.2% | ~0.9% | 可视化建站；2026 强化 CMS+Cloud |

**Born-headless / API-first 代表（按场景，非 SEO 排名）**：

| 场景 | 代表产品 | 2026 定位要点 | 来源 |
|------|----------|--------------|------|
| 企业治理、成熟 API 生态 | **Contentful** | API-first content platform；MACH 加速器叙事 | Contentful T0; CMSWire T1 |
| 结构化内容、schema-as-code、实时协作 | **Sanity** | Content Lake + GROQ；**MCP Server + Sanity Context** 分读写 Agent | Sanity T0 |
| OSS 自托管、插件生态 | **Strapi** | **Strapi 5**（Vite/TS/Document Service API）；Strapi Cloud | Strapi T0 |
| Next.js/TS 同仓、code-first | **Payload** | **2025-06 加入 Figma**；仍 MIT OSS + 自托管 | Figma/Payload T0; CMSWire T1 |
| 营销侧可视化编辑 | **Storyblok** | Visual Editor + component blocks + Bridge | Storyblok T0 |
| GraphQL-native、多源联邦 | **Hygraph** | Remote Sources **content federation** | Hygraph T0 |
| Git + Markdown 可视化 | **Tina** | repo 即数据库；TinaCloud 可选 | Tina T0 |

**MACH 认证（部分厂商）**：Contentful、Contentstack、Kontent.ai、Hygraph 等为 MACH Alliance 认证成员；Sanity、Storyblok **非认证**但仍 API-first（Brightspot 2026 对照，T1 单源——选型时「MACH certified」≠ 唯一 composable 路径）。

### 4.4 增量主题：vs Coupled Builder · vs Git · 迁移与 2026 趋势

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| Webflow 完成次世代 CMS 迁移全员；强调可视化编辑 + AI/AEO，非 pure headless 买家路径 | [CMSWire — Webflow CMS 2026](https://www.cmswire.com/digital-experience/webflow-opens-next-gen-cms-to-all-customers-and-bets-big-on-ai-search-visibility/) T1 | Webflow Cloud + Next.js 并存（CMSWire 2025）T1 | 很可能 |
| Headless 迁移最大风险：URL/redirect、meta/schema、CSR 渲染导致抓取/AEO 泄漏 | [Replatform Radar — AEM→Headless](https://replatformradar.com/blog/aem-to-headless-what-maps-what-rebuilds-where-rankings-leak) T2* | Essential Code migration guide T2* | 很可能（实践型，非 peer-reviewed） |
| US CMS 品类搜索量 2025-03 峰值后降 ~33% | [Replatform Radar — Platform shopping cooled](https://replatformradar.com/blog/platform-shopping-has-cooled) T2* | Replatform Radar blog index T2* | 很可能（著者方法论自披露） |
| Gartner：2026 至少 70% 组织被要求采用 composable DXP（vs 2023 50%） | [CMSWire DXP 2026 Guide](https://www.cmswire.com/digital-experience/what-you-need-to-know-about-digital-experience-platforms/) T1 | Gartner MQ 语境（须 sign-in 原文） | 很可能（单源 Tier 1 转引 Gartner） |

---

## 5. 时间线

| 日期 | 事件 | 来源（Tier） |
|------|------|-------------|
| 2020 | Gartner **退役 WCM Magic Quadrant** → 转向 DXP / Market Guide | CMSWire T1 |
| 2020 | MACH Alliance 创立；Microservices/API-first/Cloud/Headless | MACH Alliance T0 |
| 2024-09-23 | **Strapi 5 GA**（Vite、全 TS、Document Service API） | Strapi T0 |
| 2025-06-17 | **Payload 团队加入 Figma**；Config 2025 公布 Figma Sites | Figma/Payload T0 |
| 2025-03 | US headless/composable/DXP/CMS 类搜索量峰值 ~22,641/月 | Replatform Radar T2* |
| 2026 | Sanity MCP Server 持续迭代（v2.30.x changelog）；Sanity Context GA 路径 | Sanity T0 |
| 2026 | Webflow 次世代 CMS 全员 rollout；AEO 产品 private beta | CMSWire T1 |
| 2026-07 | Replatform Radar：品类搜索 ~15,212/月，较峰值 -33% | Replatform Radar T2* |
| 2026-08 | W3Techs：WordPress 58.9% CMS share | W3Techs T0 |

---

## 6. 实体关系

```
[WCM 概念层]
Traditional CMS ──► Decoupled ──► Headless (pure) ──► + MACH/composable 栈
       │                                    │
       │                                    ├── SaaS: Contentful, Sanity, Storyblok, Hygraph…
       │                                    ├── OSS: Strapi, Payload
       │                                    └── Git-based: Tina, Decap (构建期交付)
       │
Coupled Visual Builder (Webflow/Wix/Framer) ── 非 Headless 主路径
       │
Headless Browser (Playwright/CDP) ── 无内容管理关系（术语撞车）

[2026 整合]
Figma ──acquired team──► Payload (OSS CMS) ──► Figma Sites 后端/编辑
Sanity ──► MCP Server (写) + Sanity Context (读/生产 Agent)
MACH Alliance ──certifies──► 部分 Headless CMS 厂商（非 exhaustive）
```

---

## 7. 增量信息

### 7.0 增量对照表（多源 diff）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源（Tier） | 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|-----------------|---------|---------|--------|
| Payload 加入 Figma，非单纯收购 shut-down | OSS/自托管/社区承诺不变；设计→代码→CMS 闭环 | [Figma blog](https://www.figma.com/blog/payload-joins-figma/) T0 | [Payload blog](https://payloadcms.com/posts/blog/payload-is-joining-figma) T0 | 已确认 | 已确认 |
| Sanity 两套 MCP：编辑写 vs 生产读 | Context 只读 scoped；MCP Server 40+ 写工具 | [Sanity MCP docs](https://www.sanity.io/docs/ai/mcp-server) T0 | [Sanity Context docs](https://www.sanity.io/docs/ai/sanity-context) T0 | 已确认 | 已确认 |
| CMS 品类搜索降 33% | 15 个 US 词合并量；2025-03 峰值 | [Replatform Radar](https://replatformradar.com/blog/platform-shopping-has-cooled) T2* | Blog index T2* | 很可能 | 很可能（单源 primary research） |
| Webflow ≠ Headless 选型同构 | 可视化编辑+托管为主；API 为辅 | CMSWire 2026 T1 | Webflow 官方发布语境（间接） | 很可能 | 很可能 |
| Strapi 5 破坏式 API 变更 | documentId；v4 兼容 header | Strapi docs T0 | Strapi blog T0 | 已确认 | 已确认 |
| HN：Contentful enterprise 销售/定价摩擦 | NDA 才能报 enterprise 价 | HN T2 | — | 待核实 | 社区观点 |
| AI 助手吸收「what is headless CMS」搜索 | Replatform 著者假设 | Replatform Radar T2* | — | 待核实 | 著者明示未证明 |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| Strapi 5：2024-09-23 GA；Vite 默认 bundler；Entity Service → Document Service API | [Strapi year review](https://strapi.io/blog/bye-2024-hello-2025-a-year-in-review) T0 | 已确认 | — |
| Hygraph Content Federation：Remote Sources 联 REST/GraphQL 外源，单 GraphQL 查询 | [Hygraph docs](https://hygraph.com/docs/core-concepts/content-federation) T0 | 已确认 | — |
| Storyblok Visual Editor：`storyblokEditable` + Bridge 实时预览 | [Storyblok JS SDK docs](https://www.storyblok.com/docs/libraries/js/js-sdk) T0 | 已确认 | — |
| MACH 2026 框架扩展为 Open / Composable / Connected | [Storyblok MACH guide](https://www.storyblok.com/mp/mach-cms) T0 | 很可能 | 厂商解读 MACH Alliance 方向 |
| Replatform Radar：1,205 站迁移就绪扫描（2026-07 博文索引） | Replatform Radar blog T2* | 很可能 | 方法论见原文 |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源（Tier） | 拒绝原因 |
|----------|-------------|---------|
| 「Headless CMS 全球份额 X%」具体数字 | 多家 SEO 对比文 T? | 无 W3Techs/Gartner 分项；农场文不得定稿 |
| Payload 将闭源 | 社区猜测 | 与 Tier 0 官方承诺矛盾；无 Tier 1 互证 |
| 「Sanity 已完全取代 Contentful 为企业默认」 | 营销文 | 无权威份额数据 |

### 7.3 权威媒体解读

- **CMSWire（2026）**：Headless 从「架构选择」升级为 **content infrastructure**；纯 API-first 若牺牲营销可视化，会把日常改字变成开发队列——市场要求 **composable + in-context editing**（[Headless CMS Grows Up](https://www.cmswire.com/web-cms/13-headless-cmss-to-put-on-your-radar/)）。
- **CMSWire（2025-06）**：Figma+Payload = **design-to-deployment**；社区信任取决于 governance/pricing 是否侵蚀 OSS 灵活性（[Figma Payload deal](https://www.cmswire.com/digital-experience/when-cms-meets-ux-design-what-figmas-payload-deal-really-means/)）。
- **CMSWire（2026 DXP Guide）**：Gartner 称 2026 **≥70%** 组织须采用 composable DXP（vs 2023 50%）；composable 不仅是技术，还需 **composable business/thinking**（Irina Guseva 引述）。

### 7.4 社区与舆论反响

**HN（2023–2024 线程，Tier 2）观点分布**：

- **Contentful**：早期市场教育者；UI/SDK 好，但 **enterprise 定价/销售流程** 劝退部分团队（[HN 38493619](https://news.ycombinator.com/item?id=38493619)）。
- **Strapi**：自托管可控 vs **运维/本地化/API 体验** 差评并存（[HN 40809584](https://news.ycombinator.com/item?id=40809584)）。
- **Payload**：开发者体验、TS 扩展、REST+GraphQL 自动生成获赞；**「试过难回退」** 式偏好（[HN 36180712](https://news.ycombinator.com/item?id=36180712)）。
- **方法论**：多个 HN 用户建议 **同一 schema 原型跑 20+ 厂商** 比 RFP 纸面选型有效。

### 7.5 争议与风险

| 风险 | 要点 | 来源 |
|------|------|------|
| **SEO/AEO** | Headless+CSR 首屏无 meta/canonical；迁移丢 schema/redirect | Replatform Radar; TechTarget |
| **Preview 缺口** | Pure headless 无原生 preview → 自定义预览环境成本 | TechTarget |
| **Vendor lock-in** | content model、富文本、定制字段 | TechTarget; CMSWire |
| **OSS TCO** | 补丁/备份/升级人力 | 行业实施经验；Strapi 用户 HN 争议 |
| **迁移流量** | 文档称失败迁移可丢 30–60% 自然流量（Replatform 营销口径，需个案验证） | Replatform Radar T2* |

### 7.6 竞品与行业对照

| 维度 | Headless SaaS | OSS Headless | Git-based | Coupled Builder |
|------|--------------|--------------|-----------|-----------------|
| 买家问题 | 内容 API + 多通道 | 数据主权/定制 | 版本 diff、工程主导 | 快速整站上线 |
| 编辑 UX | Studio；Storyblok 最强 visual | Strapi UI / Payload Admin | Tina visual on MD | 画布 WYSIWYG |
| 前端责任 | 100% 自建 | 100% 自建 | SSG/SSR 模板 | 平台模板 |
| 2026 动态 | Sanity MCP；Contentful MACH+AI | Strapi 5；Payload+Figma | Nuxt Studio OSS（InfoQ 2026-02） | Webflow CMS 2.0 |

### 7.7 中文语境

本次 loop **未** 以 36氪/量子位等作 Round 1b 定稿源。中文检索环境下「无头 CMS」与「无头浏览器」混搜仍常见——Alignify KB 须显式消歧（见交付 KB §词汇锚点）。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| Decoupled = Headless? | 部分厂商/marketing 互换 | TechTarget/Contentful：Decoupled 有 optional head | 以 **有无原生 presentation layer** 为准 |
| Replatform 搜索下降原因 | Hype 正常化 + 执行期 | 著者：+ AI 助手吸收定义类 query | 作 **趋势信号**，非采购决策唯一依据 |
| Webflow 是否「Headless」 | 有 API/Cloud/Next | 主路径仍是 visual builder | 按 **primary buyer intent** 分流到 website-builder |
| Headless 是否天然 SEO 更好 | 支持者：SSG/CDN | 批评者：CSR Implementation 失败更糟 | 验收 **SSR/SSG + meta 在首响 HTML** |

---

## 9. 对用户问题的直接回答

### 9.1 Headless CMS 是什么

无内置展示层的内容管理系统：在后台完成内容建模、协作、发布与存储，通过 **API** 把结构化内容交给任意前端渲染。与 Traditional CMS（内容+模板一体）、headless browser（自动化浏览器）不同。

### 9.2 有哪些类型

按架构：**Traditional → Decoupled → Headless → Hybrid**；按部署：**SaaS API / OSS 自托管 / Git-based Content-as-Code**。Git-based 可无运行时 CMS API，仍属广义无绑定前端的内容管理路径。

### 9.3 有哪些知名产品 / 代表方案

**W3Techs 全体 CMS**：WordPress、Shopify、Wix 领先（含非 Headless）。**API-first Headless 代表**：Contentful、Sanity、Strapi、Payload、Storyblok、Hygraph——分别偏 enterprise、结构化 DX、自托管 OSS、Next/TS 同仓、visual editing、GraphQL 联邦。Coupled：**Webflow/Wix/Framer** → 非 Headless 主选型。

---

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方
- https://www.contentful.com/headless-cms/
- https://www.contentful.com/blog/everything-about-mach-architecture/
- https://developer.mozilla.org/en-US/docs/Glossary/CMS
- https://www.sanity.io/docs/ai/mcp-server
- https://www.sanity.io/docs/ai/sanity-context
- https://strapi.io/blog/bye-2024-hello-2025-a-year-in-review
- https://strapi.io/blog/api-first-cms
- https://payloadcms.com/posts/blog/payload-is-joining-figma
- https://www.figma.com/blog/payload-joins-figma/
- https://www.storyblok.com/tp/headless-cms-explained
- https://hygraph.com/docs/core-concepts/content-federation
- https://tina.io/docs
- https://machalliance.org/insights-hub/what-does-it-mean-to-be-mach-certified-
- https://playwright.dev/docs/browsers
- https://w3techs.com/technologies/overview/content_management/

### Tier 1 权威媒体
- https://www.techtarget.com/enterprise-software/definition/What-is-a-headless-content-management-system-headless-CMS
- https://www.techtarget.com/enterprise-software/feature/Headless-CMS-vs-decoupled-CMS-Whats-the-difference
- https://www.cmswire.com/digital-experience/why-did-gartner-kill-the-web-content-management-magic-quadrant/
- https://www.cmswire.com/digital-experience/what-you-need-to-know-about-digital-experience-platforms/
- https://www.cmswire.com/web-cms/13-headless-cmss-to-put-on-your-radar/
- https://www.cmswire.com/digital-experience/when-cms-meets-ux-design-what-figmas-payload-deal-really-means/
- https://www.cmswire.com/digital-experience/webflow-opens-next-gen-cms-to-all-customers-and-bets-big-on-ai-search-visibility/
- https://www.infoq.com/news/2026/02/nuxt-studio-cms/
- https://www.netguru.com/blog/strapi-vs-storyblok-vs-contentful
- https://www.forrester.com/blogs/the-results-are-in-for-the-first-forrester-wave-on-both-b2b-and-b2c-commerce-solutions/

### Tier 2 补充（反响/社区/primary research）
- https://news.ycombinator.com/item?id=38493619
- https://news.ycombinator.com/item?id=40809584
- https://news.ycombinator.com/item?id=36180712
- https://replatformradar.com/blog/platform-shopping-has-cooled
- https://replatformradar.com/blog/aem-to-headless-what-maps-what-rebuilds-where-rankings-leak
- https://en.wikipedia.org/wiki/Headless_content_management_system

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-08-28，共 6 轮 loop。*
