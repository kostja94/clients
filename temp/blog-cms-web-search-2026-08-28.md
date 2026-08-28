# 深度搜索报告 — Blog CMS / Blogging Platform

> **检索基准日**：2026-08-28  
> **时间范围**：2026 年以来（份额与产品口径以 2026-08 为准）  
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档  
> **Loop 轮次**：6 轮  
> **来源统计**：Tier 0 12 · Tier 1 4 · Tier 2 6  
> **置信度摘要**：概念基线三问（Q1–Q3）均有 Tier 0 互证；Substack/Medium 边界与社区争议有官方 + HN 对照；W3Techs 份额为单源统计（行业惯例引用）。

---

## 1. 执行摘要

**Blog CMS / Blogging Platform（博客 CMS / 博客发布平台）** 指以**逆序时间线发布文章**为核心验收的软件或服务；Buyer 问的是「文章怎么写、怎么发、怎么被搜到/被订阅」，而非通用企业内容 API 或开发者文档站。

**WordPress** 在 W3Techs（2026-08）仍占**已知 CMS 网站 58.9%**、**全部网站 40.7%**，但占全部网站比例自 2026-01 的 43.0% 缓降至 2026-08 的 41.0%。**Ghost** 占已知 CMS 约 **0.1%**，定位为出版 + 原生 Newsletter + 会员。**Substack** 与 **beehiiv** 属 **newsletter-first**：内置发现网络或运营工具，与「自有域名 SEO 博客」边界不同。**Medium** 更像**分发网络**而非基础设施。**Wix / Squarespace** 的博客是**建站平台模块**，Blog 非一等公民（Alignify 归入 `website-builder`）。

**Headless blog**（Next.js + Sanity/Contentful 或 WPGraphQL）适合工程团队控前端；与 **born-blog** 平台（Ghost、WordPress 经典路径）是不同 Buyer。**社区（HN）** 对 Substack 的主要顾虑：canonical/SEO、平台锁定与「租地」；对 Ghost/SSG 倾向 POSSE（Publish Once, Syndicate Everywhere）。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `what is blogging platform definition CMS`, `site:w3techs.com WordPress CMS market share 2026` | Q1 骨架：WordPress 官方「blog tool + CMS」；W3Techs 份额表 |
| R2 | `Ghost vs WordPress site:ghost.org`, `types of CMS business blog hosted SaaS headless` | Ghost 官方 vs WordPress 对比轴；五类 CMS 分型（SaaS / 传统 / headless / SSG）线索 |
| R3 | `Substack vs Ghost vs Medium blogging platform`, `site:substack.com about` | Substack 90% 分成 + 内置网络；Medium/Substack 边界 |
| R4 | `Wix Squarespace blog vs WordPress blog 2026`, `git-based blog MDX Astro TinaCMS` | Squarespace 博客强于 Wix；Astro/Hugo/Tina Git 路径 |
| R5 | `headless blog CMS WordPress Ghost Contentful Next.js`, `site:beehiiv.com newsletter platform` | Headless blog 选型 fork；beehiiv 双通道（邮件 + SEO 博文） |
| R6 | `site:news.ycombinator.com Ghost Substack blog platform`, `site:substack.com writers keep 90%` | HN：Substack 无 canonical；Substack Help 10% 平台费 + Stripe 细则 |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线三问：Q1 Blog CMS 是什么 | `blogging platform definition`, `wordpress.org introduction to blogging` | 已覆盖 |
| 概念基线三问：Q2 有哪些类型 | `types CMS hosted SaaS headless static`, Ghost/Substack 官方定位 | 已覆盖 |
| 概念基线三问：Q3 知名产品/方案 | `site:w3techs.com content management`, Ghost W3Techs | 已覆盖 |
| WordPress / Ghost / Medium / Substack 边界 | `Ghost vs Substack official`, `Substack about` | 已覆盖 |
| Wix / Squarespace 博客边界 | `Wix Squarespace blog feature comparison` | 已覆盖 |
| Headless blog | `headless blog Next.js CMS` | 已覆盖 |
| 排除 documentation / knowledge-base | 未深入 API 文档宿主与 RAG 栈 | 不适用（边界在 KB 分流表） |
| 社区反响 | `site:news.ycombinator.com Substack Ghost blog` | 已覆盖 |
| 中文轴 | 未单独跑 Round 1b | 权威源未覆盖（本报告 EN-first，中文二手未作事实源） |

---

## 4. 核心发现（多源验证）

### 4.1 Blog CMS / Blogging Platform 是什么

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| **Blog** = 持续更新的时间线式网站，文章通常逆序排列，含评论、分类、RSS 等 | [WordPress — Introduction to Blogging](https://wordpress.org/documentation/article/introduction-to-blogging/) T0 | [Wix — What is a blogging platform](https://www.wix.com/blog/best-blogging-platforms) T1 | 已确认 |
| **CMS** 是更广类别：创建、组织、发布数字内容；许多 blog 工具是 CMS 的子集 | [MDN — CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS) T0 | WordPress 同上 T0 | 已确认 |
| **Blog CMS / 博客平台**  Buyer 核心：编辑 → 发布 URL →（可选）邮件订阅/SEO/评论；与「任意结构化内容 API」或「开发者 OpenAPI 文档站」不同 | Ghost 产品页 T0 | Alignify 品类边界（本任务定义） | 已确认 |

**叙述**：WordPress.org 自述为「Blog Tool, Publishing Platform, and CMS」，并说明 blogging 软件提供「写文章、点发布即可上线」的界面（[wordpress.org/about](https://wordpress.org/about/)）。**Blog CMS** 在本调研中特指**以博客/专栏发稿为主场景**的内容系统，包含一体托管（Ghost Pro、WordPress.com）、自托管 OSS（WordPress.org、Ghost）、newsletter-first（Substack、beehiiv）与 Git/Headless 等实现方式。

**与相邻概念边界**：

| 相邻概念 | 边界 |
|----------|------|
| **Headless CMS** | 无绑定展示层，内容经 API 交付；Blog 只是 content model 之一 |
| **Website builder** | 整站可视化 + 托管；Blog 常为模块而非 PRIMARY |
| **Documentation** | 开发者 API/产品文档，版本与 OpenAPI 优先 |
| **Knowledge base** | 企业内部 RAG/问答，非公开 SEO 博客 |
| **Newsletter platform** | 邮件/订阅为第一出口；Web 博文可为副通道 |

### 4.2 Blog CMS 有哪些类型

**分类依据**：部署形态 × 内容出口 × 买家意图（综合 WordPress 官方、Ghost 官方、Substack 官方、W3Techs CMS 口径）。

| 类型 | 特征 | 典型场景 | 来源 |
|------|------|----------|------|
| **A — 托管 SaaS 博客** | 厂商托管 CMS + 前端 + CDN；开箱发稿 | 个人/小企业要快 | WordPress.com、Ghost(Pro)、Medium |
| **B — OSS 自托管 WCM** | 装在自己服务器；主题/插件生态 | SEO 内容营销、可扩展站点 | WordPress.org、Ghost self-host |
| **C — Newsletter-first** | 邮件列表 + 付费订阅为核心；Web 为配套 | 创作者经济、专栏 | Substack、beehiiv、Kit |
| **D — Git-based / SSG** | Markdown/MDX 在 repo；构建期静态化 | 工程主导、PR 审稿 | Astro、Hugo、11ty + Tina/Decap |
| **E — Headless blog** | CMS/API 存文，Next/Astro 渲染 | 产品博客、设计系统一致 | Sanity/Contentful + Next；WPGraphQL |
| **F — 建站器博客模块** | 拖拽建站 + Blog 区块 | 品牌站附带偶尔发文 | Wix、Squarespace → `website-builder` |

**易混淆点**：

- **Substack** = 博客界面 + **社交网络式发现**（Notes、推荐）；不是传统 CMS（[substack.com/about](https://substack.com/about)）。
- **Medium** = **平台内阅读与算法分发**；弱品牌定制与列表导出（社区共识，Tier 2）。
- **Ghost** = **born for publishing**：原生 SEO、Newsletter、会员，0% 平台抽成（[ghost.org](https://ghost.org/) vs [ghost.org/vs/substack](https://ghost.org/vs/substack/)）。
- W3Techs 将 **wiki、blog engine、SSG、website editor** 一并计入 CMS 大类（[w3techs.com/technologies/overview/content_management](https://w3techs.com/technologies/overview/content_management/)）。

### 4.3 知名产品 / 代表方案

| 场景或类型 | 代表产品 | 备注（份额/定位） | 来源 |
|-----------|----------|------------------|------|
| 全球 WCM 份额 #1 | **WordPress** | 已知 CMS 的 **58.9%**；全站 **40.7%** | [W3Techs WordPress](https://w3techs.com/technologies/details/cm-WordPress) |
| WCM #2–#3（含电商/建站） | **Shopify** 7.7%、**Wix** 6.1%（占已知 CMS） | 非 blog-primary | [W3Techs CMS overview](https://w3techs.com/technologies/overview/content_management/) |
| 出版型 OSS | **Ghost** | 已知 CMS **~0.1%**；v6 + Docker 自托管 | [W3Techs Ghost](https://w3techs.com/technologies/details/cm-ghost) |
| Newsletter-first | **Substack**, **beehiiv** | Substack：5M+ 付费订阅网络（官方）；beehiiv：Launch 免费至 2.5K 订阅 | Substack/beehiiv T0 |
| 分发网络 | **Medium** | 借平台 DA 获流；非「自有站」 | Tier 2 综合 |
| 建站器博客 | **Squarespace**, **Wix** | Squarespace 博客体验优于 Wix；弱于 WP 重度 SEO | Tier 1 评测综合 |
| Headless + 前端 | **Sanity**, **Contentful**, **Payload** + Next/Astro | Blog 为 content type 之一 | 工程媒体 |
| Git 博客 | **Astro**, **Hugo**, **TinaCMS** | 工程/Content-as-Code | Tina/Astro 官方 |

**WordPress 趋势（W3Techs）**：占全部网站比例 2026-01 **43.0%** → 2026-08 **41.0%**（缓降，仍绝对主导）。

### 4.4 Medium / Substack / Ghost / WordPress 边界（增量）

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| Substack 付费：平台 **10%** + Stripe 卡费与 recurring billing fee | [Substack Support — How much does Substack cost](https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost) T0 | [substack.com/going-paid](https://substack.com/going-paid-i) T0 | 已确认 |
| Ghost 付费订阅：**0%** 平台费，直连 Stripe | [ghost.org/vs/substack](https://ghost.org/vs/substack/) T0 | ghost.org 首页 T0 | 已确认 |
| Substack **>30%** 新付费订阅来自站内网络 | [substack.com/about](https://substack.com/about) T0 | — | 很可能（单源官方） |
| Ghost(Pro) 托管自 **$15/mo**，含 CDN、邮件、分析 | [docs.ghost.org/hosting](https://docs.ghost.org/hosting) T0 | Ghost vs WP 页 T0 | 已确认 |

---

## 5. 时间线

| 日期 | 事件 | 来源（Tier） |
|------|------|-------------|
| 2003 | WordPress 诞生（b2/cafelog fork） | WordPress.org T0 |
| 2013 | Ghost 开源发布（Node.js 出版平台） | W3Techs Ghost brief T0 |
| 2020+ | Substack 创作者网络扩张；Defender 法律支持 | substack.com/about T0 |
| 2026 | Ghost 6.0；Docker Compose 为推荐自托管路径 | docs.ghost.org T0 |
| 2026-08 | W3Techs：WordPress 58.9% CMS 份额；全站 40.7% | W3Techs T0 |
| 2026 | beehiiv 强调「Newsletter + SEO 博文」双通道 | beehiiv.com T0 |

---

## 6. 实体关系（如适用）

```
                    ┌─────────────────────────────────────┐
                    │     Blog CMS / Blogging Platform     │
                    │  （Buyer：发稿、订阅、SEO、所有权）    │
                    └─────────────────┬───────────────────┘
          ┌───────────────────────────┼───────────────────────────┐
          ▼                           ▼                           ▼
   OSS + 自托管                  托管 SaaS                    Newsletter-first
 WordPress.org                  WordPress.com                 Substack / beehiiv
 Ghost self-host               Ghost(Pro) / Medium
          │                           │                           │
          └───────────────┬───────────┴───────────┬───────────────┘
                          ▼                       ▼
                   Git/SSG 路径              Headless blog 路径
              Astro/Hugo/Tina/Decap      Sanity/Contentful + Next.js
                          │                       │
                          ▼                       ▼
              相邻（非本 slug PRIMARY）    相邻 headless-cms
              website-builder (Wix/SS)   documentation (API docs)
                                       knowledge-base (RAG)
```

---

## 7. 增量信息

### 7.0 增量对照表（多源 diff）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源（Tier） | 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|-----------------|---------|---------|--------|
| Substack 不支持站外 canonical 为主源 | 官方未强调；社区实测 SEO 隐患 | HN item 34167586 T2 | HN item 45615402 T2 | 很可能 | 很可能 |
| WordPress 全站占比 2026 年缓降 | W3Techs 历史表非 WP 新闻稿 | W3Techs history T0 | W3Techs WP detail T0 | 已确认 | 已确认 |
| Squarespace 博客强于 Wix | 官方未写对比 | Shipwithout 2026 T1 | RateTheTool T1 | 很可能 | 很可能 |
| Ghost 36% 用户从 Substack/Medium 迁移（2 年） | Ghost 官方未写该数字 | thestacc.com T1（单源） | — | 待核实 | 待核实 |
| beehiiv 每帖可同时邮件 + SEO 博文 | beehiiv 博客营销文 | beehiiv.com T0 | beehiiv blog T0 | 已确认 | 已确认 |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| Substack 付费订阅平台费 10% + Stripe 2.9%+$0.30 + recurring billing fee | [Substack Support](https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost) T0 | 已确认 | |
| Ghost 6 自托管推荐 Docker Compose（ActivityPub/Analytics 多服务） | [docs.ghost.org/install/docker](https://docs.ghost.org/install/docker/) T0 | 已确认 | |
| W3Techs：BetterDocs（WordPress 文档插件）为最常见 documentation 平台 | [W3Techs CMS overview](https://w3techs.com/technologies/overview/content_management/) T0 | 已确认 | 与 `documentation` slug 边界相关 |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源（Tier） | 拒绝原因 |
|----------|-------------|---------|
| Ghost「36% 用户从 Substack 迁移」 | thestacc.com T1 | 仅单源非官方；未找到 Ghost 官方互证 |
| johal.in Contentful vs Sanity 博客 benchmark 数字 | johal.in | 非 Tier 1；方法论未独立验证 |

### 7.3 权威媒体解读

- **建站器 vs 博客 CMS**：多篇 2026 建站对比（Shipwithout、RateTheTool）共识——Wix/Squarespace 适合「站里有个博客」；**SEO 驱动、大量发文**仍指向 WordPress 或专用出版栈（Ghost）。
- **Newsletter 平台分化**：beehiiv 官方将自身与 Mailchimp 等 **email marketing** 区分——前者 **recurring 内容 + 受众增长**，后者促销/电商自动化（[beehiiv.com/blog/best-website-for-newsletters](https://www.beehiiv.com/blog/best-website-for-newsletters)）。

### 7.4 社区与舆论反响

**HN 观点分布（Tier 2，非事实源）**：

- **偏自建/ Ghost/ SSG**：重视 canonical、POSSE、数据所有权（[HN 34167586](https://news.ycombinator.com/item?id=34167586)、[40059038](https://news.ycombinator.com/item?id=40059038)）。
- **对 Substack skeptical**：「租地」、Google 可见性、无 canonical（[HN 45615402](https://news.ycombinator.com/item?id=45615402)）。
- **Substack 支持者**：要内置网络与付费转化，接受 10% 与平台规则（[HN 46428349](https://news.ycombinator.com/item?id=46428349) 讨论串）。

### 7.5 争议与风险

| 风险 | 说明 |
|------|------|
| **平台锁定** | Substack/Medium 受众与规则绑定平台；Ghost/WP 自托管可迁 |
| **SEO** | Newsletter-first 与 walled garden 可能弱化「自有域名为主索引源」 |
| **WordPress 维护** | 插件/安全面；headless 或 Ghost 换维护类型 |
| **费用结构** | Substack 10% 随收入放大；Ghost  flat fee + Stripe |

### 7.6 竞品与行业对照

| 若 PRIMARY 需求是… | 常见选型 |
|---------------------|----------|
| SEO 内容营销 + 插件生态 | WordPress |
| 出版 + 邮件 + 会员一体 | Ghost |
| 快速起量 + 站内发现 | Substack |
| 运营型 Newsletter + 广告网络 | beehiiv |
| 借平台流量、非基础设施工 | Medium（ syndication ） |
| 工程控 UI + 多站点产品博客 | Headless CMS + Next/Astro |
| 偶尔发文 + 整站设计 | Wix / Squarespace |

### 7.7 中文语境

检索范围内未对 36氪/量子位等中文 Tier 1 做专项 fetch；**未纳入执行摘要事实**。中文创作者讨论与英文社区结构类似（Substack 简 vs WordPress 灵活），无独立权威统计补充。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| Substack SEO | 社区：closed ecosystem 损害 Google | Substack 官方：内置发现补流量 | 以业务模型选：要搜索主权 → 自有站 + syndication |
| Ghost 迁移率 | 第三方称高 Substack→Ghost 迁移 | Ghost 官方未公布 | 不写入份额结论 |
| 「Blog platform」定义 | 厂商（Superblog）强调 SEO-first | WordPress 强调 general CMS | Alignify 用 Buyer 意图分流，不单一定义 |

---

## 9. 对用户问题的直接回答

### 9.1 Blog CMS / Blogging Platform 是什么

以**博客文章**（时间线、RSS、评论/订阅）为核心交付的内容发布系统，可托管或自托管。它是 **CMS 的子集或特化场景**，区别于 headless 内容 API、开发者文档宿主与企业 RAG 知识库。

### 9.2 有哪些类型

1. 托管 SaaS 博客  
2. OSS 自托管（WordPress、Ghost）  
3. Newsletter-first（Substack、beehiiv）  
4. Git-based / MDX / SSG  
5. Headless blog（API + 自建前端）  
6. 建站器博客模块（归 adjacent `website-builder`）

### 9.3 有哪些知名产品 / 代表方案

- **份额**：WordPress **58.9%**（已知 CMS）；Shopify **7.7%**；Wix **6.1%**；Ghost **~0.1%**（W3Techs，2026-08）  
- **出版/Newsletter**：Ghost、Substack、beehiiv  
- **分发**：Medium  
- **Headless**：Sanity、Contentful、Payload + Next.js  
- **Git**：Astro、Hugo、TinaCMS  

---

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方

- [WordPress — About](https://wordpress.org/about/)
- [WordPress — Introduction to Blogging](https://wordpress.org/documentation/article/introduction-to-blogging/)
- [MDN — CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS)
- [Ghost — Home](https://ghost.org/)
- [Ghost — vs WordPress](https://ghost.org/vs/wordpress/)
- [Ghost — vs Substack](https://ghost.org/vs/substack/)
- [Ghost — Hosting / Docker](https://docs.ghost.org/hosting)
- [Substack — About](https://substack.com/about)
- [Substack Support — Pricing & fees](https://support.substack.com/hc/en-us/articles/360037607131-How-much-does-Substack-cost)
- [beehiiv — Newsletter Platform](https://www.beehiiv.com/newsletter-platform)
- [W3Techs — CMS overview](https://w3techs.com/technologies/overview/content_management/)
- [W3Techs — WordPress](https://w3techs.com/technologies/details/cm-WordPress)

### Tier 1 权威媒体

- [Wix — Best Blogging Platforms 2026](https://www.wix.com/blog/best-blogging-platforms)
- [Shipwithout — Squarespace vs Wix 2026](https://shipwithout.com/en/site-builders/squarespace-vs-wix)

### Tier 2 补充（反响/社区）

- [HN — Ask: Preferred Platform to Blog](https://news.ycombinator.com/item?id=34167586)
- [HN — Ghost vs Substack thread](https://news.ycombinator.com/item?id=40059038)
- [HN — Newsletter platform cage](https://news.ycombinator.com/item?id=45615402)

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-08-28，共 6 轮 loop。*
