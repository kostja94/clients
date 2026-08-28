# Open Source CMS / 开源 CMS · 知识块（非线性笔记）

**材料范围**：公开网络检索（WordPress.org、Drupal、Joomla、Ghost、Strapi、Payload、Directus、TYPO3 官方文档；MDN、W3Techs、OSI/Open Core 行业文；GitHub `awesome-headless-cms` 类资源；Tier 1 2026 open-source CMS 对比稿）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-08-28**。

**站内对照**：KB → 正式文 **`/blog/open-source-cms`** · **`/zh/blog/open-source-cms`**（2026-07-23）

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 `#open-source-cms-tools`）· `keywordEn`: **Open Source CMS / OSS CMS** · `keywordZh`: **开源 CMS / 开源内容管理系统** · Secondary：self-hosted CMS · open source alternative to Contentful · 快判 → [KEYWORD-RESEARCH.md](./KEYWORD-RESEARCH.md)

**主题簇**：[README.md](./README.md) · Hub：[content-management-system.md](./content-management-system.md)

**站内相邻**（CMS 簇）：[headless-cms.md](./headless-cms.md)（API-first · 含 SaaS 闭源）· [enterprise-cms.md](./enterprise-cms.md) · [open-source-deployment-dimension.md](../../skills/knowledge-block/references/open-source-deployment-dimension.md)（**跨品类** OSS 维度 SSOT）

**站内相邻**（builder 簇）：[blog-website-builder.md](../website-builder/blog-website-builder.md)（WordPress/Ghost 博客 listicle）· [website-builder.md](../website-builder/website-builder.md)

**站内相邻**（跨频道 · 已发布）：[如何不用 CMS，用 AI 搭建博客](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai) · [Git 托管](https://alignify.co/blog/git-hosting)

## 与相邻 slug 分流

> OSS **作为维度**适用于全站所有 Tools 品类；**本文**专收 **OSS CMS 选型资源**（SERP、GitHub 生态、自托管 TCO）。架构深度 → [`headless-cms`](./headless-cms.md)；博客 builder listicle → [`blog-website-builder`](../website-builder/blog-website-builder.md)。

| 维度 | **`open-source-cms`（本文）** | **`headless-cms`** | **`blog-website-builder`** |
|------|--------------------------------|-------------------|---------------------------|
| **检索头词** | open source CMS · self-hosted CMS · OSS alternative | headless CMS · API-first CMS | blog website builder |
| 买家在问 | 要 **源码/自托管/无 SaaS 锁定**，选哪套 CMS？ | 内容 **API + 自建前端** 怎么接？ | 怎么 **开博客站**（常混 Wix/WP）？ |
| 许可范围 | **OSI / source-available / open-core** 谱系 | SaaS + OSS 均含 | 多为托管 builder + born-blog |
| 产品举例 | WP.org, Drupal, Strapi, Ghost, Payload | Contentful, Sanity, Strapi | Wix, Ghost, Substack |

| 你的问题 | 看哪个 slug |
|----------|-------------|
| 「Strapi vs WordPress vs Drupal 开源选型？」 | **本页** §工具与产品类型 |
| 「Contentful 的开源替代？」 | **本页** FAQ + [`headless-cms`](./headless-cms.md) |
| 「只要 headless、不管开不开源？」 | [`headless-cms`](./headless-cms.md) |
| 「开博客、SERP 是 best blog website builder？」 | [`blog-website-builder`](../website-builder/blog-website-builder.md) |
| 「Sanity 算开源 CMS 吗？」 | **本页** §分层栈；Studio 开源、Content Lake 否 |
| 「Open source 对 AI 工具/CLI 也适用吗？」 | [`open-source-deployment-dimension`](../../skills/knowledge-block/references/open-source-deployment-dimension.md)（跨品类） |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Open Source CMS / 开源 CMS**：**可获取源代码**（OSI 或 vendor 定义的 source-available）并通常支持 **自托管** 的内容管理系统；买家诉求是 **审计、定制、数据驻留、规避 SaaS 锁定**——不是单一架构（headless / 一体式均可）。
- **与「OSS 跨品类维度」**：Open Source 对 API、IDE、Agent 等 **所有品类** 通用（见 skill reference）；**本 KB** 因 **OSS CMS 检索量 + GitHub/文档生态** 独立维护 **选型 SSOT**。
- **Self-hosted / 自托管**：数据与运行时在你控制的 VPS/K8s/裸金属；**≠** 厂商 Managed Cloud（Strapi Cloud 等仍可用，但非必须）。
- **Open core**：核心开源 + 企业功能闭源（Strapi SSO、Review Workflows 等）。
- **分层栈（半开源）**：Sanity — Studio MIT，**Content Lake 不可自托管**；写进选型表时 **Self-host 数据 = ❌**。
- **Source-available / 收入阈**：Directus 2026 — 中小组织可免费自托管，超阈需商业许可；**≠** 经典 MIT/GPL 心智。

---

## 专题对照：OSS CMS × 架构 × 商业化

| 模式 | 含义 | 代表 | Self-host 数据 |
|------|------|------|----------------|
| **经典 OSS WCM** | 主题一体、PHP/自托管 | WordPress.org, Drupal, Joomla | ✅ |
| **OSS Headless** | API + 自托管 Studio | Strapi, Payload, Directus | ✅（Directus 看许可） |
| **OSS Born-blog** | 出版垂直 | Ghost (MIT) | ✅ |
| **OSS + 官方 Cloud** | 同厂托管可选 | Strapi Cloud, Payload Cloud, Ghost(Pro) | ✅ 自托管路径仍在 |
| **Open core** | 企业功能付费 | Strapi Enterprise 功能 | ✅ CE 免费 |
| **分层栈** | UI 开源 / 后端 SaaS | Sanity Studio | ❌ |
| **纯 SaaS（对照）** | 闭源 | Contentful | ❌ → 用 **别厂 OSS** 替代，非同厂 fork |

---

## 问题域

- **检索量**：`open source CMS` Bing 代理 **~1,300,000**（2026-08-28）— 与 `best CMS` 同量级，**值得独立 KB**（资源：官方文档、GitHub topic、awesome 列表、迁移文）。
- **GitHub 生态**：Strapi 70k+ stars、WordPress 核心 repo、Payload/ Directus 等 — **发现渠道**，不是「GitHub 品类 = open source CMS slug」的唯一依据，但与 SERP listicle **一致**。
- **vs 闭源 SaaS**：TCO = 许可 $0 + **运维/补丁/升级**；HN/对比文常低估 OSS 人力（见 [`headless-cms` §OSS 隐性 TCO](./headless-cms.md#风险--合规--治理外部框架可对照非法律意见)）。
- **合规/驻留**：GDPR、政务、内网 — 自托管 OSS 为默认路径；须读 **Directus 2026 收入阈** 等非 MIT 许可。
- **与 WordPress 份额**：W3Techs 总盘见 [`blog-website-builder` §市场份额](../website-builder/blog-website-builder.md#市场份额快照w3techs--2026-08--占已知-cms网站)；**OSS CMS ≠ 只有 WordPress**，但 WP 是 OSS WCM 基准。

---

## 形态谱系（Type · 产品见 §工具与产品类型）

- **Type A — 经典 OSS WCM（Coupled）**：一体化主题/插件。适合插件生态、编辑熟悉 WP、低成本 WCM。
- **Type B — OSS Headless API**：REST/GraphQL 自托管。适合 Next/Nuxt 团队、要多端复用内容。
- **Type C — OSS Born-blog**：出版/Newsletter。适合创作者、MIT 自托管。
- **Type D — Git-native CMS**：Tina、Decap — 内容在 repo。适合 PR 审稿；与 [`headless-cms` Type C](./headless-cms.md#形态谱系type-定义--产品见-六产品速览--工具与产品类型) 交叉。
- **Type E — Source-available / 条件免费**：Directus 等 — 选型前 **读当前 license**。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **隐性 TCO**：监控、备份、安全补丁、大版本升级（Strapi 4→5）。
- **Open core 边界**：以为「全免费」却需要 SSO/Review Workflow → 预算企业模块。
- **分层栈误判**：Sanity Studio 在 GitHub ≠ 可迁出 Content Lake。
- **插件/供应链**：WordPress 插件攻击面 — 最小权限、官方源。
- **许可变更**：Directus BSL→2026 新许可 — **选型时读 license 页，不凭记忆**。
- **SEO**：自托管 OSS 仍须 SSR/缓存；架构不自动等于 SEO。

---

## 落地碎片

- **第一问**：必须 **自托管数据** 吗？否 → 也可看 [`headless-cms`](./headless-cms.md) SaaS；是 → 本页 Type A/B/C。
- **Contentful 替代短路径**：工程团队 → Strapi/Payload/Directus；编辑要强 → Strapi + 插件或 Ghost；已有 WP 内容 → WPGraphQL 或渐进迁移。
- **小团队 MVP**：Ghost（博客）· PocketBase/Strapi（API）· WordPress.com 对立面是自托管 WP.org。
- **许可 checklist**：MIT/GPL ✅ 审计 · Open core 标 enterprise 功能 · Source-available 标收入阈。
- **与 headless 分工**：已定 API-first → headless 文内 §OSS 行链 **本页**；已定「只要开源」→ **本页** 为主。

---

## 工具与产品类型（OSS CMS · 检索常混；非穷尽）

> **列举顺序**：**垂直 OSS 优先** → 广义 WCM 平台。闭源对照单列最后一行。**License / Self-host 数据** 为必选列（跨品类 OSS 维度 SSOT）。

| 产品 | Type | License / 模式 | Self-host 数据 | 典型买家 |
|------|------|----------------|----------------|----------|
| **WordPress.org** | A | GPL | ✅ | 插件生态 · SEO · 最大 WCM 份额 |
| **Drupal** | A | GPL | ✅ | 复杂站点 · 政府/enterprise WCM |
| **Joomla** | A | GPL | ✅ | 中小 WCM |
| **Strapi** | B | MIT CE + open core | ✅ | Node · headless · 插件 |
| **Payload** | B | MIT | ✅ | Next/TS · code-first |
| **Directus** | B/E | Source-available 2026 | ✅（看阈） | 已有 SQL · 数据平台 |
| **Ghost** | C | MIT | ✅ | 博客 · Newsletter |
| **TYPO3** | A | GPL | ✅ | 欧洲 enterprise WCM |
| **Tina** | D | Apache 2.0 | ✅ Git | MDX · 视觉编辑 + Git |
| **Decap** | D | MIT | ✅ Git | 原 Netlify CMS |
| **Sanity** | 分层栈 | Studio MIT · Lake 闭源 | ❌ | 对照：非 full OSS CMS |
| **Contentful** | — | 闭源 | ❌ | **对照**；替代 → Strapi/Payload |

### 按场景 → Type

| 若 PRIMARY 需求是… | Type / 产品 |
|-------------------|-------------|
| 最大生态 + 插件 | A · WordPress.org |
| 复杂权限 + enterprise WCM（仍 OSS） | A · Drupal |
| Node headless + 自托管 | B · Strapi / Payload |
| 已有 Postgres/MySQL 套壳 | B/E · Directus |
| 博客 + 自托管 + MIT | C · Ghost |
| Git PR 审稿发内容 | D · Tina / Decap |
| 闭源 SaaS 的开源替代 | B · 上表 + [`headless-cms` FAQ](./headless-cms.md) |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **WordPress.org** | OSS WCM 基准 | [wordpress.org](https://wordpress.org/) |
| **Drupal** | Enterprise OSS WCM | [drupal.org](https://www.drupal.org/) |
| **Strapi** | MIT headless · v5 | [strapi.io](https://strapi.io/) |
| **Payload** | MIT · Next-native | [payloadcms.com](https://payloadcms.com/) |
| **Directus** | SQL-first · 2026 license | [directus.io](https://directus.io/) |
| **Ghost** | MIT publishing | [ghost.org](https://ghost.org/) |
| **MDN — CMS** | 定义 | [developer.mozilla.org/docs/Glossary/CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS) |
| **W3Techs — CMS** | 份额 | [w3techs.com/technologies/overview/content_management/](https://w3techs.com/technologies/overview/content_management/) |
| **OSI — Open Source Definition** | 许可边界 | [opensource.org/osd](https://opensource.org/osd) |

---

## 延伸阅读

- 跨品类 OSS 维度：[`open-source-deployment-dimension.md`](../../skills/knowledge-block/references/open-source-deployment-dimension.md)
- Headless 深度：[`headless-cms.md`](./headless-cms.md)
- 博客 builder SERP：[`blog-website-builder.md`](../website-builder/blog-website-builder.md)
- 调研底稿：[`headless-cms-web-search-2026-08-28.md`](../../../temp/headless-cms-web-search-2026-08-28.md) · [`blog-cms-web-search-2026-08-28.md`](../../../temp/blog-cms-web-search-2026-08-28.md)

---

*档位：B · KB → `/blog/open-source-cms` · Territory：编程工具链 · 簇：`cms`*
