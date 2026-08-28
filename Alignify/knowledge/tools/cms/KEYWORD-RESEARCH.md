# CMS 簇 · 关键词快判 SSOT

> **方法**：[`intent-near-keyword-volume.md`](../../skills/knowledge-block/references/intent-near-keyword-volume.md) · **现搜** 2026-08-28 · Bing EN-US · **方向性代理，非 MSV**

---

## 何时新建 spoke 知识块（三关 · 须全过）

| # | 关 | 问什么 | 不过 → |
|---|-----|--------|--------|
| 1 | **SERP** | 有自然头词？与现有 slug SERP 重叠 <50%？ | 写进现有文 H2/FAQ |
| 2 | **垂直产品** | 是否有 **≥2 款 born-for-category 产品**（从第一天为该子类设计，不是通用平台的「一种部署/许可证/模式」）？ | **不建 spoke** |
| 3 | **轴类型** | 子类是 **买家任务 / 交付形态**，而非品牌词、许可证轴、学术 taxonomy？ | 不建 spoke |

**明确不做 spoke 的：**

- **品牌 slug**（WordPress、Contentful、Shopify…）— 可在 listicle 里写，不单占 KB
- **许可证/部署轴**（open source CMS、SaaS CMS）— 是筛选维度，不是垂直品类
- **学术/architecture 标签**（traditional · decoupled · monolithic · composable）— 并入 `headless-cms` 或 Hub 概念节
- **泛 listicle 角**（best CMS）— 发文角度或 Hub，不是产品子类 KB

**Hub 例外**：`content-management-system` 可建 **索引 Hub**（概念基线三问 + 决策树链 spoke），**不以垂直产品表为主**。

---

## 簇内已有

| slug | Primary EN | 垂直产品（born-for） | 判定 |
|------|------------|---------------------|------|
| `headless-cms` | Headless CMS | Contentful, Sanity, Strapi, Payload, Storyblok, Hygraph… | ✅ 已过三关 |

---

## 子类重评（搜索量 + 垂直产品 · 2026-08-28）

| 子类 / 检索词 | Bing 约结果 | born-for 产品？ | 单独 KB？ | 归处 |
|---------------|-------------|----------------|-----------|------|
| **Enterprise CMS / DXP** | ~107k–250k | ✅ AEM, Sitecore, Optimizely, Kentico | **✅ 建议 `enterprise-cms`** | 下一 spoke |
| **CCMS**（组件/技术文档） | 中 | ✅ Paligo, Heretto, MadCap Flare | **⚠️ 待定** | 与 [`documentation`](../enterprise-knowledge/documentation.md) 分工后再定 |
| **Headless CMS** | ~48k | ✅ 见上 | ✅ 已有 | — |
| **Open source CMS** | ~1.3M | ❌ 许可证轴；产品是 WP/Drupal/**Strapi**（属 WCM 或 headless） | **❌** | Hub §类型；Strapi 在 headless |
| **WordPress** | 品牌极大 | ❌ 品牌，非子类 | **❌** | blog-website-builder / listicle |
| **Best CMS** | ~794k | ❌ 混排角 | **❌** | Hub 或 flagship 文题 |
| **Content management system** | ~1.44M | ❌ 定义/总称 | **Hub only** | 概念 + 链 spoke |
| **Git / flat-file CMS** | ~169k–239k | ⚠️ Tina, Decap 垂直，但 SERP≈headless | **❌** | `headless-cms` Type C |
| **Decoupled / composable** | ~63k–200k | ❌ Marketing 标签 | **❌** | headless secondary |
| **Traditional / monolithic** | ~50–13k | ❌ 无独立垂直产品 | **❌** | 不写 |
| **WCM 经典一体**（WordPress.org 模式） | 分散在 best CMS | ⚠️ Drupal/Joomla 广义 WCM，无新垂直赛道 | **❌** | 不单建 `wcm-platform`；份额在 blog-website-builder |

---

## 建议 backlog（修正后）

| 顺序 | slug | 理由 |
|:----:|------|------|
| 1 | **`content-management-system`** | Hub · 概念三问 · **无**独立垂直产品表 |
| 2 | **`enterprise-cms`** | 唯一通过三关、且尚无 KB 的 **产品子类** |
| — | `headless-cms` | 已有 |
| 观望 | `ccms` | 有垂直产品，需与 documentation 簇划界 |

**已从 backlog 移除**：`open-source-cms`（**部署/许可维度**，见下）、`wordpress`（品牌）、`best-cms`（发文角）。

---

## Open Source · 跨品类维度（不单建 slug）

**结论（2026-08-28 续研）**：GitHub 上有大量开源 CMS，但 GitHub **按 repo/主题（headless-cms、wordpress）组织**，不是按「open source CMS」垂直品类。Open source 对 **所有 Alignify 工具品类** 通用——应作为产品表的 **License / Self-host** 列，不是 spoke。

**商业化 ↔ 开源 · 六种关系**（详表 → [`open-source-deployment-dimension.md`](../../skills/knowledge-block/references/open-source-deployment-dimension.md)）：

| 模式 | CMS 例 |
|------|--------|
| OSS + 托管云 | Strapi、Payload、Ghost |
| Open core | Strapi 企业功能 |
| 分层栈（UI 开源 / 数据闭源） | **Sanity**（Studio MIT，Content Lake 不可自托管） |
| 纯 SaaS + 市场 OSS 替代 | Contentful ↔ Strapi/Payload（**不同厂商**） |
| 基金会 + 商业品牌 | WordPress.org / WordPress.com |
| Source-available / 收入阈 | Directus 2026 |

**高量检索怎么处理**：

| Query | 归处 |
|-------|------|
| open source CMS · best open source CMS | Hub §部署维度 + 各 spoke 产品表 |
| open source alternative to Contentful | `headless-cms` FAQ |
| self hosted vs SaaS | 各产品表 **Self-host** 列 |

---

## 与 Website Builder 簇边界

| 检索词 | 文件夹 |
|--------|--------|
| headless · enterprise CMS · CCMS | **`cms/`** |
| blog website builder · ecommerce builder | [`../website-builder/`](../website-builder/README.md) |

WordPress 份额 SSOT：`blog-website-builder` §市场份额；不单建品牌 KB。

---
