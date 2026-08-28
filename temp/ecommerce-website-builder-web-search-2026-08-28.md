# 深度搜索报告 — E-commerce Website Builder / Online Store Platform

> **检索基准日**：2026-08-28  
> **时间范围**：2026 年公开资料；份额统计取 W3Techs 2026-08 快照  
> **检索约束**：按 web-deep-search-spec v1.4，未读取本地客户文档  
> **Loop 轮次**：6 轮  
> **来源统计**：Tier 0 12 · Tier 1 9 · Tier 2 4  
> **置信度摘要**：概念基线三问（Q1–Q3）均有 Tier 0/1 互证；Shopify vs WooCommerce 选型分歧有官方定价 + W3Techs + Forbes 交叉验证；平台锁定/第三方网关费以 Shopify 官方定价页为 Tier 0 基准

---

## 1. 执行摘要

**E-commerce website builder（电商建站平台 / 在线商店平台）** 指让商户在**自有品牌域名**上搭建网店、管理商品目录、结账与履约的软件——典型代表 Shopify、WooCommerce、BigCommerce、Wix Commerce、Squarespace Commerce。它与 **marketplace（Amazon、Shopee、Etsy 等第三方卖场）** 不同：后者商户在平台规则下挂牌，不拥有完整品牌站与客户数据；也与 **headless commerce** 不同：后者前后端解耦，需自建 Storefront。

**市场份额（W3Techs，2026-08）**：在已检测到电商系统的网站中，**WooCommerce 约 48.1%**、**Shopify 约 31.7%**；占全部网站用量分别为 8.1% 与 5.3%，且 Shopify 份额持续上升、WooCommerce 缓慢下降。**Shopify vs WooCommerce** 是最高频选型意图：Shopify 偏托管 SaaS、快速上线与非技术团队；WooCommerce 偏 WordPress 开源插件、数据与代码自控，但需自管主机与运维。

**增量要点**：Shopify 对非 Shopify Payments 的第三方网关收取 **2%（Basic）至 0.2%（Plus）** 附加费（官方定价页）；BigCommerce 以「无平台交易费、多支付商嵌入」作为迁移卖点；华人跨境语境下 Shopify 常需海外主体，WooCommerce 在支付插件灵活度上更受讨论。

---

## 2. 搜索过程摘要

| 轮次 | 新增 query 示例 | 本轮增量发现 |
|------|----------------|--------------|
| R1 | `what is ecommerce website builder site:shopify.com` | Q1 定义骨架：平台 = 自建品牌网店 + 目录/支付/库存 |
| R1 | `site:w3techs.com ecommerce market share` | Q3：WooCommerce 48.1%、Shopify 31.7%（电商子类份额） |
| R1 | `types headless commerce traditional site:techtarget.com` | Q2：Traditional / Headless / Composable 分类 |
| R2 | `Shopify vs WooCommerce Forbes Advisor 2026` | Tier 1 选型对照：托管 vs 自托管、定价起点 |
| R2 | `site:shopify.com ecommerce platform vs marketplace` | Tier 0 明确 Amazon ≠ 电商平台 |
| R3 | `site:shopify.com headless Hydrogen Storefront API` | Shopify 同平台内 headless 路径（Hydrogen） |
| R3 | `site:news.ycombinator.com Shopify WooCommerce` | 社区：速度 vs 定制、WC 性能顾虑 |
| R4 | `Shopify WooCommerce 独立站 2026` | 中文：华人卖家 Shopify 验证 + Woo SEO 常见组合 |
| R5 | `site:bigcommerce.com ecommerce platforms 2026` | SaaS / Composable / Open SaaS 厂商分类 |
| R5 | `Shopify third-party transaction fees site:shopify.com/pricing` | 官方第三方网关附加费率表 |
| R6 | `site:woocommerce.com what is WooCommerce` | Woo 官方：WordPress 插件、无平台月费 |

---

## 3. 搜索意图拆解

| 意图 | 检索词示例 | 结果状态 |
|------|------------|----------|
| 概念基线三问：Q1 是什么 | `ecommerce platform definition site:shopify.com` | 已覆盖 |
| 概念基线三问：Q2 有哪些类型 | `ecommerce frameworks SaaS headless composable site:bigcommerce.com` | 已覆盖 |
| 概念基线三问：Q3 知名产品/份额 | `site:w3techs.com ecommerce` | 已覆盖 |
| Shopify vs WooCommerce 选型 | `Shopify vs WooCommerce 2026 Forbes` | 已覆盖 |
| 与 marketplace 边界 | `ecommerce platform vs marketplace site:shopify.com` | 已覆盖 |
| 与 headless commerce 边界 | `headless commerce definition site:techtarget.com` | 已覆盖 |
| 平台锁定 / 费用争议 | `Shopify pricing third-party transaction fees` | 已覆盖 |
| 社区反响 | `site:news.ycombinator.com WooCommerce Shopify` | 已覆盖（历史帖为主，2026 新帖有限） |
| 中文语境 | `独立站 Shopify WooCommerce 2026` | 已覆盖（中文社区/行业站；核心事实已与 Tier 0 交叉） |

---

## 4. 核心发现（多源验证）

### 4.1 E-commerce Website Builder 是什么

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| 电商建站平台是供商户**创建、管理、扩展自有在线商店**的软件，涵盖商品目录、交易、集成与客户体验 | [BigCommerce — Ecommerce Platforms](https://www.bigcommerce.com/articles/ecommerce/ecommerce-platforms/) T0 | [Shopify — What is Ecommerce](https://www.shopify.com/blog/what-is-ecommerce) T0 | 已确认 |
| 与 **marketplace** 不同：平台让商户拥有品牌站与运营工具；marketplace 是多卖家共用的第三方网站 | [Shopify — Platform vs Marketplace](https://www.shopify.com/blog/ecommerce-platform-vs-marketplace) T0 | [Wix — eCommerce vs Marketplace](https://www.wix.com/blog/ecommerce-vs-marketplace) T0 | 已确认 |
| 与 **纯 website builder** 交叠：commerce-first 平台以**卖货闭环**（购物车、支付、库存、税运）为默认能力栈 | [Shopify — Best Ecommerce Platforms 2026](https://www.shopify.com/blog/best-ecommerce-platforms) T0 | [Wix — Best Ecommerce Platforms 2026](https://www.wix.com/blog/best-ecommerce-platforms) T0 | 已确认 |

**叙述**：E-commerce website builder / online store platform（本报告统称「电商建站平台」）解决的是「在**自己的域名与品牌**下完成在线销售」——注册域名、设计 storefront、上架 SKU、接入支付、处理订单与物流。Shopify 官方将 Amazon 明确排除在「电商平台」之外，称其为 marketplace：卖家依附平台规则与流量，而非运营独立品牌站（[Shopify Best Ecommerce Platforms](https://www.shopify.com/blog/best-ecommerce-platforms)）。Shopee、Lazada、淘宝等同属 marketplace 赛道，**不属于**本 slug 的 commerce-first builder 范畴（可与平台**多渠道同步**销售，但非替代关系）。

与 **headless commerce**：传统/一体式平台前后端耦合（主题 + Admin）；headless 将 Storefront 与 commerce 后端 API 分离，前端可自建（[TechTarget — Headless Commerce](https://www.techtarget.com/enterprise-software/definition/headless-commerce-headless-e-commerce)）。Shopify、BigCommerce、WooCommerce 均提供 headless 路径，但多数中小商户仍使用一体式主题店。

### 4.2 有哪些类型

| 类型（分类依据：部署与前后端架构，来源 BigCommerce + TechTarget） | 特征 | 典型场景 | 来源 |
|-----------------------------------|------|----------|------|
| **Hosted SaaS 一体式** | 平台托管、主题/编辑器内置、订阅制；运维由厂商负责 | 快速开店、非技术团队、DTC 品牌 | [BigCommerce Frameworks](https://www.bigcommerce.com/articles/ecommerce-website-development/ecommerce-frameworks/) T0 |
| **开源插件 + 自托管（OSS on CMS）** | 核心免费、需 WordPress 主机；代码与数据自控 | 内容+商城同栈、深度定制、已有 WP 团队 | [WooCommerce 官方](https://woocommerce.com/woocommerce/) T0 |
| **Website-builder-with-commerce** | 通用建站为主、商务能力在较高套餐启用 | 小微品牌、设计优先、SKU 规模中等 | [Squarespace — Ecommerce Builders](https://www.squarespace.com/blog/best-ecommerce-website-builder) T0 |
| **Headless / Composable** | 后端 API（Storefront API 等）+ 自选前端框架 |  omnichannel、定制 UX、企业开发团队 | [TechTarget Headless](https://www.techtarget.com/enterprise-software/definition/headless-commerce-headless-e-commerce) T1 · [Shopify Hydrogen](https://apps.shopify.com/hydrogen) T0 |
| **Enterprise Monolith** | Adobe Commerce (Magento)、SAP Commerce Cloud 等 | 复杂 B2B 定价、大型目录、ERP 深度集成 | [BigCommerce B2B Platforms](https://www.bigcommerce.com/articles/b2b-ecommerce/b2b-ecommerce-platforms/) T0 |

**易混淆点**：
- **Wix / Squarespace Commerce** 既是 website builder 也是电商建站平台——买家意图决定归类：要「漂亮官网顺带卖货」偏 `website-builder`；要「网店为主、运营闭环」偏本品类。
- **WooCommerce** 在 W3Techs 中同时计入 CMS 与 ecommerce 子类——它是 **WordPress 上的电商插件**，不是独立 SaaS。
- **Headless CMS**（Contentful 等）常作为 headless storefront 的内容层，**不是**电商建站平台本身。

### 4.3 知名产品 / 代表方案

| 场景或类型 | 代表产品 | 备注（份额/定位） | 来源 |
|-----------|----------|------------------|------|
| 托管 SaaS · DTC | **Shopify** | 电商系统份额 **~31.7%**（2026-08）；全站用量 **5.3%** | [W3Techs E-commerce](https://w3techs.com/technologies/subdetails/ecommerce) |
| OSS 插件 · WP 生态 | **WooCommerce** | 电商系统份额 **~48.1%**；全站用量 **8.1%** | 同上 |
| 托管 SaaS · B2B/多店 | **BigCommerce** | 强调 open SaaS、原生 B2B、无 Shopify 式第三方网关附加费叙事 | [BigCommerce vs Shopify](https://www.bigcommerce.com/compare/bigcommerce-vs-shopify/) T0 |
| Builder + Commerce | **Wix**、**Squarespace** | 设计/全能建站 + 商务套餐；Squarespace 强调设计+服务/订阅售卖 | [Wix vs Shopify](https://www.wix.com/blog/wix-vs-shopify) T0 |
| 长尾开源 | PrestaShop、OpenCart | W3Techs 各约 **0.5% / 0.3%** 全站用量 | [W3Techs History](https://w3techs.com/technologies/history_sub/content_management/ecommerce/all) |
| Headless / Composable | commercetools、Shopify Hydrogen | 企业/API-first；Hydrogen 为 Shopify 官方 React headless 栈 | [Shopify Hydrogen](https://apps.shopify.com/hydrogen) T0 |

**份额趋势（W3Techs 月度，2025-07 → 2026-07）**：WooCommerce 在电商系统内从 **51.4% → 48.6%**；Shopify 从 **27.4% → 30.9%**（[Market Share Trend](https://w3techs.com/technologies/history_sub/content_management/ecommerce)）。解读：Woo 仍居首但份额缓降；Shopify 持续蚕食；**不得**用 SEO「Top 10」农场文替代 W3Techs 排名。

### 4.4 Shopify vs WooCommerce（高频搜索意图）

| 结论 | 来源 A | 来源 B | 置信度 |
|------|--------|--------|--------|
| Shopify = 全托管 SaaS，Basic **$39/月**（年付可更低），适合快速上线 | [Shopify Pricing](https://www.shopify.com/pricing) T0 | [Forbes Advisor — WooCommerce vs Shopify](https://www.forbes.com/advisor/business/software/woocommerce-vs-shopify/) T1 | 已确认 |
| WooCommerce 插件**免费**，需自购主机与维护 WordPress | [WooCommerce Pricing](https://woocommerce.com/pricing/) T0 | [Forbes Advisor](https://www.forbes.com/advisor/business/software/woocommerce-vs-shopify/) T1 | 已确认 |
| 选型 heuristic：要速度/省心 → Shopify；要定制/内容 SEO/数据主权 → WooCommerce | [Forbes Advisor](https://www.forbes.com/advisor/business/software/woocommerce-vs-shopify/) T1 | [Shopify — Website Builder vs Developer](https://www.shopify.com/blog/website-builder-vs-web-developer) T0 | 很可能 |

---

## 5. 时间线

| 日期 | 事件 | 来源（Tier） |
|------|------|-------------|
| 2006 | Shopify 创立 | [Shopify About](https://www.shopify.com/about) T0 |
| 2011 | WooCommerce 项目起源（后归 Automattic） | [WooCommerce](https://woocommerce.com/) T0 |
| 2021-11 | Shopify 发布 Hydrogen 开发者预览（headless） | [Shopify Enterprise Blog](https://www.shopify.com/enterprise/blog/headless-commerce-half-helix) T0 |
| 2026-08 | W3Techs：WooCommerce 48.1% / Shopify 31.7%（电商系统份额） | [W3Techs](https://w3techs.com/technologies/subdetails/ecommerce) T1 统计 |
| 2026 | Shopify 定价页：Basic 第三方网关附加费 **2%** | [Shopify Pricing](https://www.shopify.com/pricing) T0 |

---

## 6. 实体关系（如适用）

```
Merchant（商户）
    │
    ├─► E-commerce Website Builder（本品类）
    │       ├─ Hosted SaaS: Shopify, BigCommerce, Wix Commerce, Squarespace Commerce
    │       ├─ OSS Plugin: WooCommerce (on WordPress)
    │       └─ Headless layer: Storefront API + Hydrogen / Next.js / Catalyst
    │
    ├─► Marketplace（非本品类）: Amazon, Shopee, eBay, Etsy（可作 sales channel 接入）
    │
    └─► Adjacent: Website Builder（内容/落地页为主）· Headless CMS（内容 API）· App Builder（业务逻辑应用）
```

---

## 7. 增量信息

### 7.0 增量对照表（多源 diff）

| 增量主张 | 相对 Tier 0 的新增点 | 首见来源（Tier） | 互证来源 | 验证结果 | 置信度 |
|---------|---------------------|-----------------|---------|---------|--------|
| Shopify 第三方网关附加费 Basic **2%** | 官方定价页有表格式费率 | [Shopify Pricing](https://www.shopify.com/pricing) T0 | [BigCommerce vs Shopify](https://www.bigcommerce.com/compare/bigcommerce-vs-shopify/) T0 | 已确认 | 已确认 |
| BigCommerce 强调「Embedded Payment Providers 无平台交易费」 | 相对 Shopify 的迁移卖点 | [BigCommerce Compare](https://www.bigcommerce.com/compare/bigcommerce-vs-shopify/) T0 | [BigCommerce Software 2026](https://www.bigcommerce.com/articles/ecommerce/software/) T0 | 已确认 | 已确认 |
| WooCommerce 在电商系统份额仍第一但趋势下降 | W3Techs 月度序列 | [W3Techs Trend](https://w3techs.com/technologies/history_sub/content_management/ecommerce) T1 | [W3Techs Subdetails](https://w3techs.com/technologies/subdetails/ecommerce) T1 | 已确认 | 已确认 |
| 华人卖家 Shopify 需海外主体/支付限制 | 官方未写中国区细节 | SegmentFault 2026 文 T2 | 狐狸客对比文 T2 | 待核实 | 待核实 |
| Shopify Payments 年处理量 **$130B+** 与锁定争议 | 非 Shopify 官方首页数据 | Ecommerce Times 2026-07 T2 | — | 待核实 | 待核实 |

### 7.1 已验证增量信息

| 增量事实 | 来源 | 置信度 | 备注 |
|---------|------|--------|------|
| 使用非 Shopify Payments 主网关时，Shopify 按套餐收取 **2% / 1% / 0.6% / 0.2%**（Basic / Grow / Advanced / Plus）附加费 | [Shopify Pricing](https://www.shopify.com/pricing) T0 | 已确认 | 官方定价表 |
| BigCommerce 将「减少 app 依赖、原生 B2B、多 storefront」列为 Shopify 迁移理由 | [BigCommerce vs Shopify](https://www.bigcommerce.com/compare/bigcommerce-vs-shopify/) T0 | 已确认 | 厂商对比页，观点带立场 |
| Forbes 2026：Shopify 更易用；WooCommerce 更灵活但需 WordPress 熟悉度 | [Forbes Advisor](https://www.forbes.com/advisor/business/software/woocommerce-vs-shopify/) T1 | 很可能 | 单源 Tier 1 评测 |
| W3Techs：Shopify 在北美、澳、日更强；Woo 在欧洲、非洲、亚洲长尾更常见 | [W3Techs WooCommerce vs Shopify](https://w3techs.com/technologies/comparison/cm-shopify,cm-woocommerce) T1 | 很可能 | 地理分布为 W3Techs 页面描述 |

### 7.2 未通过验证的传闻

| 传闻/主张 | 来源（Tier） | 拒绝原因 |
|----------|-------------|---------|
| Shopify 全球活跃店 **480 万**、Woo **650 万**（精确数） | tech-insider.org T? | 非 §2.3 白名单；与 W3Techs 方法论不一致 |
| WooCommerce 平均转化率高于 Shopify 的量化对比（2–3% vs 1.4%） | 中文 SEO/行业站 T2 | 无 Tier 0/1 方法学支撑 |
| Shopify Payments 年处理 **$130B** | Ecommerce Times T2 | 仅单源行业博客，未找到 Tier 0/1 互证 |

### 7.3 权威媒体解读

- **TechTarget** 将 headless commerce 描述为传统一体式平台的演进：企业有开发能力后「拆掉前端训练轮」，以 API 连接自定义 Storefront（[Headless Commerce Definition](https://www.techtarget.com/enterprise-software/definition/headless-commerce-headless-e-commerce)）。
- **Forbes Advisor（2026）** 定位 Shopify 为「fully hosted, all-in-one」、WooCommerce 为「free plugin, greater flexibility, more technical skill」（[对比文](https://www.forbes.com/advisor/business/software/woocommerce-vs-shopify/)）。
- **BigCommerce** 2026 内容矩阵将平台分为 **SaaS / Composable / Open SaaS**，并强调 B2B 原生能力为企业选型轴（[Ecommerce Platforms 2026](https://www.bigcommerce.com/articles/ecommerce/ecommerce-platforms/)）。

### 7.4 社区与舆论反响

- **Hacker News**（历史帖，Tier 2）：分裂明显——一派认为 Shopify 让商户专注销售而非运维（[Ask HN: self-hosted alternative](https://news.ycombinator.com/item?id=23581414)）；另一派强调 WooCommerce 在熟悉 WordPress 时成本更低、定制更深，但需控制插件数量与维护（同帖）。
- **性能顾虑**：HN 多次提及 WooCommerce 可能拖慢 WordPress，Hosted 平台（Shopify）在「不想自己扛安全/扩展」时更常被推荐（[item 21017792](https://news.ycombinator.com/item?id=21017792)）。
- **2026 新帖**：检索范围内未见与 Hydrogen 3.0 等相关的大规模 HN 热帖；**权威社区对 2026 新品类的显著讨论有限**。

### 7.5 争议与风险

| 风险 | 要点 | 来源 |
|------|------|------|
| **平台锁定** | Shopify 主题 Liquid、App 生态、Shop Pay 与 Payments 捆绑提高迁移成本 | T0 Shopify Help · T2 HN |
| **第三方网关附加费** | 不用 Shopify Payments 则按交易收取平台附加费 | [Shopify Pricing](https://www.shopify.com/pricing) T0 |
| **WooCommerce 运维** | 主机、插件冲突、PCI、备份由商户负责 | [WooCommerce Build Store Doc](https://woocommerce.com/document/build-online-store/) T0 |
| **TCO 误判** | Woo 插件免费 ≠ 总成本低；需计主机、开发、维护 | Forbes T1 · HN T2 |

### 7.6 竞品与行业对照

| 对照 | 差异摘要 |
|------|----------|
| Shopify vs BigCommerce | BigCommerce 强调 B2B 原生、多 storefront、开放 API；Shopify 强调 DTC 生态与 Shop Pay（[BigCommerce Compare](https://www.bigcommerce.com/compare/bigcommerce-vs-shopify/)） |
| Shopify vs Wix | Wix 偏「网站+商务」一体；Shopify 偏 commerce-first、多渠道库存（[Wix vs Shopify](https://www.wix.com/blog/wix-vs-shopify)） |
| Platform vs Shopee/Amazon | 自有品牌站 vs 平台内卖家；可 omnichannel 并用（[Shopify Platform vs Marketplace](https://www.shopify.com/blog/ecommerce-platform-vs-marketplace)） |

### 7.7 中文语境（如适用）

- **独立站**语境下，Shopify 常被视为「开箱快、生态全」的 SaaS 默认项；WooCommerce 被视为「SEO/内容同栈、长期成本可控」方案（[SegmentFault 2026](https://segmentfault.com/a/1190000048166659) — Tier 2，观点类）。
- 常见策略表述：**Shopify 验证 SKU**，内容与 SEO 用 WordPress/Woo 承接——属运营经验，非官方建议。
- **Shopee / 淘宝** 在中文流量中常混称「开店」，但属 **marketplace**，与本品类分流（与 Tier 0 Shopify/Wix 定义一致）。

---

## 8. 分歧与待核实

| 项 | 说法 A | 说法 B | 建议 |
|----|--------|--------|------|
| 长期 TCO | WooCommerce 长期更省（中文行业文） | Shopify 18 个月内运维人力更低（Presta 等博客） | 按团队是否具备 WP 运维能力建模 3 年 TCO |
| 转化率 / 性能 | 部分中文稿称 Woo 转化更高 | Shopify 强调 Checkout 转化与速度 | 不以无方法学对比定稿；自有 A/B 为准 |
| 华人 Shopify 主体 | 中文社区称需海外主体 | 官方 Help 以目标市场为准 | 以 Shopify 目标国家/支付开通文档为准 |

---

## 9. 对用户问题的直接回答

### 9.1 E-commerce Website Builder 是什么

供商户在**自有域名**上搭建并运营在线商店的软件平台，集成（或可通过插件获得）商品目录、购物车、支付、订单、库存与基础营销工具。与 **marketplace（Shopee、Amazon 等）** 不同——后者你在别人的平台上卖；与 **headless CMS** 不同——后者管内容 API，不管完整 commerce 闭环。

### 9.2 有哪些类型

按部署/架构：**(1) 托管 SaaS 一体式**（Shopify、BigCommerce）；**(2) 开源插件 + 自托管**（WooCommerce）；**(3) 通用建站 + 商务套餐**（Wix、Squarespace Commerce）；**(4) Headless / Composable**（Storefront API + 自建前端，如 Hydrogen）。分类依据见 BigCommerce / TechTarget 公开材料。

### 9.3 有哪些知名产品 / 代表方案

**份额（W3Techs，2026-08，电商系统内）**：WooCommerce **~48.1%**、Shopify **~31.7%**，其次 PrestaShop、OpenCart 等。**选型**：快速 DTC → Shopify；WP/内容/定制 → WooCommerce；设计优先小微 → Squarespace/Wix；B2B/多店 → BigCommerce；企业 composable → commercetools 等。

---

## 10. 参考链接（按 Tier 排序）

### Tier 0 官方

- [Shopify — What is Shopify (2026)](https://www.shopify.com/blog/what-is-shopify)
- [Shopify — Best Ecommerce Platforms 2026](https://www.shopify.com/blog/best-ecommerce-platforms)
- [Shopify — Ecommerce Platform vs Marketplace](https://www.shopify.com/blog/ecommerce-platform-vs-marketplace)
- [Shopify — Pricing](https://www.shopify.com/pricing)
- [Shopify — Hydrogen App](https://apps.shopify.com/hydrogen)
- [WooCommerce — What is WooCommerce](https://woocommerce.com/woocommerce/)
- [WooCommerce — Pricing](https://woocommerce.com/pricing/)
- [BigCommerce — Ecommerce Platforms 2026](https://www.bigcommerce.com/articles/ecommerce/ecommerce-platforms/)
- [BigCommerce — vs Shopify 2026](https://www.bigcommerce.com/compare/bigcommerce-vs-shopify/)
- [Wix — Best Ecommerce Platforms 2026](https://www.wix.com/blog/best-ecommerce-platforms)
- [Squarespace — Best Ecommerce Website Builders 2026](https://www.squarespace.com/blog/best-ecommerce-website-builder)

### Tier 1 权威媒体 / 统计

- [W3Techs — E-commerce Systems Aug 2026](https://w3techs.com/technologies/subdetails/ecommerce)
- [W3Techs — E-commerce Market Share Trend](https://w3techs.com/technologies/history_sub/content_management/ecommerce)
- [W3Techs — WooCommerce vs Shopify](https://w3techs.com/technologies/comparison/cm-shopify,cm-woocommerce)
- [TechTarget — Headless Commerce Definition](https://www.techtarget.com/enterprise-software/definition/headless-commerce-headless-e-commerce)
- [TechTarget — Headless vs Traditional](https://www.techtarget.com/enterprise-software/tip/6-key-benefits-of-headless-commerce)
- [Forbes Advisor — WooCommerce vs Shopify 2026](https://www.forbes.com/advisor/business/software/woocommerce-vs-shopify/)

### Tier 2 补充（反响/社区/中文）

- [HN — Shopify self-hosted alternative](https://news.ycombinator.com/item?id=23581414)
- [HN — WooCommerce performance](https://news.ycombinator.com/item?id=21017792)
- [SegmentFault — WooCommerce vs Shopify 华人独立站 2026](https://segmentfault.com/a/1190000048166659)

---

*本报告按 web-deep-search-spec v1.4 生成，检索日 2026-08-28，共 6 轮 loop。*
