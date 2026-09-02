# Content Management System / 内容管理系统 · 知识块（Hub · 非线性笔记）

**材料范围**：公开网络检索（MDN、Drupal.org、TechTarget、IBM、W3Techs CMS 概览；Gartner DXP / WCM 公开摘要；2026 CMS 对比 Tier 1 稿）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-08-28**。

**站内对照**：KB → 正式文优先 **`/blog/content-management-system`** · **`/zh/blog/content-management-system`**

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 `#content-management-system-tools`）· `keywordEn`: **Content Management System / CMS** · `keywordZh`: **内容管理系统 / CMS** · Secondary：what is a CMS · best CMS · web content management

**主题簇**：[README.md](./README.md) · **本页 = CMS 簇 Hub（概念 + 决策树；产品深度在 spoke）**

**站内相邻**：[`../website-builder/README.md`](../website-builder/README.md)（建站器簇）· [`open-source-deployment-dimension.md`](../../skills/knowledge-block/references/open-source-deployment-dimension.md)

---

## 与相邻 slug 分流

> **Hub 不写完整产品榜** — 选型表在 spoke。本页回答「CMS 是什么 / 有哪些类型 / 去哪读」。

| 你的问题 | 看哪个 slug |
|----------|-------------|
| 什么是 CMS？有哪些类型？ | **本页** §概念基线三问 |
| 开源 · 自托管 · OSS 替代 Contentful | [`open-source-cms`](./open-source-cms.md) |
| Headless · API-first · Contentful/Sanity | [`headless-cms`](./headless-cms.md) |
| 大企业 DXP · AEM/Sitecore | [`enterprise-cms`](./enterprise-cms.md) |
| 拖拽建站 · AI 整站（非 CMS 采购） | [`website-builder`](../website-builder/website-builder.md) |
| 开博客 · blog website builder | [`blog-website-builder`](../website-builder/blog-website-builder.md) |
| 开发者 API 文档站 | [`documentation`](../enterprise-knowledge/documentation.md) |

---

## 概念基线三问（SSOT）

### Q1 — CMS 是什么？

**CMS（Content Management System，内容管理系统）**：用于 **创建、编辑、协作、发布与存储数字内容** 的软件；典型含 **CMA（编辑界面）** 与 **CDA（存储与交付）**（[MDN — CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS)）。  
**不是**：无头浏览器 · 纯 API 文档宿主 · 企业内部 RAG 知识库 · 拖拽建站器（后者在 website-builder 簇，尽管 W3Techs 把 Shopify/Wix 计入 CMS 份额）。

### Q2 — 有哪些类型？（Alignify 簇地图）

| 类型（买家语言） | 架构/交付 | CMS 簇 spoke |
|------------------|-----------|--------------|
| **Open source / self-hosted** | 源码 + 自托管 | [`open-source-cms`](./open-source-cms.md) |
| **Headless / API-first** | 无绑定展示层 | [`headless-cms`](./headless-cms.md) |
| **Enterprise / DXP** | 治理、合规、多站点 | [`enterprise-cms`](./enterprise-cms.md) |
| **Website builder + 博客** | 托管拖拽整站 | [`website-builder`](../website-builder/) |
| **Born-blog / listicle** | Wix+WP+Ghost 同 SERP | [`blog-website-builder`](../website-builder/blog-website-builder.md) |

**不按 slug 拆**：traditional · decoupled · composable（标签 → 并入 headless/Hub）；**WordPress 品牌**（进 open-source / blog spoke，不单占 KB）。

### Q3 — 有哪些知名产品/方案？（入口，非排名）

| 路径 | 代表 |
|------|------|
| OSS WCM | WordPress.org, Drupal → [`open-source-cms`](./open-source-cms.md) |
| OSS Headless | Strapi, Payload → [`open-source-cms`](./open-source-cms.md) + [`headless-cms`](./headless-cms.md) |
| SaaS Headless | Contentful, Sanity → [`headless-cms`](./headless-cms.md) |
| Enterprise DXP | AEM, Sitecore → [`enterprise-cms`](./enterprise-cms.md) |
| 托管建站 | Wix, Squarespace → [`website-builder`](../website-builder/website-builder.md) |

**份额 SSOT**：[blog-website-builder §W3Techs](../website-builder/blog-website-builder.md#市场份额快照w3techs--2026-08--占已知-cms网站)（WordPress 等）；**不在 Hub 重复数字**。

---

## 决策树（CMS 簇 + 姊妹 builder 簇）

```
你要解决什么？
├─ 理解 CMS 定义/类型 → 本页
├─ 要源码/自托管 → open-source-cms
├─ 要 API + 自建前端 → headless-cms
├─ 大企业采购/DXP/合规 → enterprise-cms
├─ 最快拖拽官网（非 CMS 采购语）→ ../website-builder/website-builder
├─ blog website builder listicle → ../website-builder/blog-website-builder
└─ 不用 CMS · Git+AI 博客 → /blog/how-to-build-a-blog-without-a-cms-using-ai
```

---

## 问题域（为何 CMS 品类仍存在）

- **内容与展示分离**：多渠道、工程前端 → headless 增长；**简单 presence** 仍被 builder 吃掉。
- **合规与治理**：金融/政务/全球品牌 → enterprise 栈；SMB → builder 或 OSS。
- **W3Techs 广义无头**：Shopify/Wix 计 CMS 份额，但检索词常是 **online store / website builder** → 簇分流。

---

## 风险 · 合规 · 治理（Hub 级）

- **品类混读**：「CMS」检索 listicle 混 Wix 与 WordPress — 用 **决策树** 先定簇再读 spoke。
- **SEO**：选型错误（CSR headless、builder 博客上限）→ 各 spoke §风险。
- **锁定**：SaaS schema / builder 画布 / OSS 运维 TCO — spoke 分述。

---

## 外链索引

| 名称 | URL |
|------|-----|
| MDN — CMS | [developer.mozilla.org/docs/Glossary/CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS) |
| W3Techs — CMS overview | [w3techs.com/technologies/overview/content_management/](https://w3techs.com/technologies/overview/content_management/) |
| TechTarget — CMS definition | [techtarget.com/.../What-is-a-content-management-system-CMS](https://www.techtarget.com/enterprise-software/definition/What-is-a-content-management-system-CMS) |

---

## 延伸阅读 · 站内外

- [`open-source-cms.md`](./open-source-cms.md) · [`headless-cms.md`](./headless-cms.md) · [`enterprise-cms.md`](./enterprise-cms.md)
- [`../website-builder/README.md`](../website-builder/README.md)

---

*档位：B · Hub · KB → `/blog/content-management-system` · Territory：编程工具链*