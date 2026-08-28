# Landing Page Builder / 落地页构建器 · 知识块（非线性笔记）

**材料范围**：公开网络检索（Unbounce / Instapage / Leadpages / Framer 官方产品页与定价；Future Market Insights 市场报告；Shopify 生态 PageFly / GemPages 厂商材料；Hacker News 社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-08-28**。

**站内对照**：待上线正式页时对齐（新文优先 **`/blog/landing-page-builder`** · **`/zh/blog/landing-page-builder`**）· slug **`landing-page-builder`**

**Tools 关键词与 slug 映射**：待写入 [alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 `#landing-page-builder-tools`）· `keywordEn`: **Landing Page Builder / Conversion Page Builder** · `keywordZh`: **落地页构建器 / 转化页工具**

**主题簇**：[README.md](./README.md) · 路由 SSOT：[website-builder.md §簇级 FAQ](website-builder.md#簇级-faq)

**站内相邻**（六轴）：[website-builder.md](website-builder.md)（Hub）· [advertising-agent.md](../marketing-growth/advertising-agent.md) · [lead-generation.md](../marketing-growth/lead-generation.md)

**站内相邻**（跨频道 · 已发布）：[落地页创建（SEO）](https://alignify.co/seo/landing-page) · [如何不用 CMS，用 AI 搭建博客](https://alignify.co/blog/how-to-build-a-blog-without-a-cms-using-ai)（落地页与博客同 Content-as-Code 流水线）· [主域名下的分块建站](https://alignify.co/blog/subdirectory-hosting)

## 与相邻 slug 分流

> 六轴全表与跨轴 FAQ → **[website-builder §分流](website-builder.md#与相邻-slug-分流)** · **[§簇级 FAQ](website-builder.md#簇级-faq)**。

| 维度 | **`landing-page-builder`（本文）** | **`website-builder`** | **`advertising-agent`** |
|------|-----------------------------------|----------------------|-------------------------|
| **典型买家问题** | 「广告点击后落地页怎么搭、怎么测？」 | 「多页网站怎么上线？」 | 「AI 能不能替我管广告账户？」 |
| **交付形态** | **单页/变体** + 托管 + CRO 栈 | 多页站点 + 导航 + 托管 | 连接 Ads API 的 Agent |
| **验收核心** | **CVR / CPA / message match / 实验** | 品牌呈现、整站 IA | ROAS、账户自动化 |

| 你的问题 | 看哪个 slug |
|----------|-------------|
| 「Unbounce 和 Framer 做落地页有什么区别？」 | **本页** vs [`website-builder`](website-builder.md) |
| 「Contentful 能代替 Unbounce 吗？」 | **不能** → [`headless-cms`](../cms/headless-cms.md) |
| 「Shopify 广告页用 PageFly 还是 Unbounce？」 | Shopify campaign → 本页 Type C；站外 lead gen → Type A |
| 「Smartly 会不会顺便做落地页？」 | [`advertising-agent`](../marketing-growth/advertising-agent.md) — 管广告；LP 仍常需 dedicated builder |
| 「Wix 整站和 Unbounce 都要买吗？」 | 整站 [`website-builder`](website-builder.md)；高量 paid → 本页 Type A |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Landing Page / 落地页**：为**单一营销战役**创建的**独立**网页；访客从广告、邮件或社交链接进入；设计目标是**一个 CTA**（注册、下载、购买），通常**无全站导航**以降低干扰（[Unbounce 定义](https://unbounce.com/landing-page-articles/what-is-a-landing-page/)）。
- **Landing Page Builder / 落地页构建器**：无/低代码搭建、托管并**优化**上述页面的 SaaS 或模块；核心不是「站点地图」，而是**转化实验栈**（表单、Popups、A/B、动态文案、流量分配）。
- **与 Homepage / Website 的区分**：Homepage 是站点入口、常多目标；Website 是多页探索；Landing Page 是**战役专用目的地**（[Unbounce — LP vs homepage](https://unbounce.com/landing-page-articles/whats-the-difference-between-a-landing-page-and-a-homepage/)）。
- **Post-click / 点击后体验**：Paid media 点击之后的第一屏——message match（广告承诺与页头一致）是 LP Builder 要解决的主问题，不是 [`advertising-agent`](../marketing-growth/advertising-agent.md) 的主战场。
- **CRO（Conversion Rate Optimization）**：在 LP 语境下 = A/B、多变量测试、Heatmaps、AI 流量路由（如 Smart Traffic）、Dynamic Text Replacement——Dedicated LP SaaS 的差异化所在。
- **Campaign Page（电商）**：Shopify 等平台上**脱离默认 PDP/集合模板**的促销/广告专用页；验收含**加购/checkout/像素**继承，见 Type C。

---

## 问题域（为何会出现这类产品）

- **Paid traffic 贵**：每次点击都有成本；把流量送到「全站首页」而非匹配 offer 的 LP，会直接抬高 CPA（Instapage / Unbounce 官方叙事）。
- **战役数量爆炸**：每个广告组、受众、创意角度需要**独立 URL** 与变体；开发排期跟不上 media buy 节奏。
- **Message match 难规模化**：搜索词、广告标题与 H1 不一致会损 CVR；DTR（动态文案替换）与 1:1 ad-to-page（AdMap）产品化此需求。
- **实验文化**：高转化团队把 LP 当**可迭代资产**而非一次性设计稿——需要内置实验而非外接 Optimizely + 自建页。
- **电商 post-click 特殊**：DTC 需要 campaign 页保留店铺 checkout 与 catalog，但主题默认页不适合广告流量（Shopify App 生态）。
- **AI 工作流上移**：2026 年 Unbounce MCP 等将「brief → 上线 → 实验」搬进 Claude/ChatGPT，减少在 builder UI 间切换。

---

## 能力栈（概念拆分，非厂商功能表）

- **编辑器与模板**：拖拽区块、响应式、行业模板——入门门槛；与「设计系统级控制」是不同维度（Framer vs Unbounce）。
- **表单与 Lead capture**：多步表单、Hidden fields、CRM/Webhook——B2B 管线入口；常与 [`lead-generation](../marketing-growth/lead-generation.md) 工具链衔接。
- **Popups / Sticky bars**：页内二次转化触达；Dedicated SaaS 常见（Unbounce Build+）。
- **A/B & 多变量测试**：变体流量分配、置信区间、胜者推广——**起始定价档**是 2026 选型关键（Leadpages Grow 含 A/B vs Unbounce Experiment 档）。
- **AI 流量优化**：Smart Traffic 类——按访客特征路由到更易转化变体（Unbounce Optimize、Leadpages Optimize）。
- **Ad ↔ Page 映射**：Instapage AdMap——可视化广告结构与 LP 对应关系，适合多账户代理。
- **动态文案（DTR）**：搜索词/UTM 驱动 H1 变化，提升 message match。
- **性能与 AMP**：移动加载（Instapage Thor Render Engine、Swipe Pages 等 AMP 向）——电商与移动 paid 敏感。
- **集成层**：Google/Meta Ads、HubSpot、Marketo、Stripe、Analytics——LP 是 martech 枢纽，不是孤岛。
- **AI / MCP 生成与运维**：Unbounce MCP——在 AI assistant 内创建、发布、实验、读报表；与「仅 AI 生成静态 HTML」不同，仍绑定平台 CRO 栈。
- **电商原生**：Shopify 产品块、购物车、discount、pixel——Campaign builder 额外维度。

---

## 形态谱系（Type 定义 · 产品见 §工具与产品类型）

- **Type A — Dedicated LP SaaS（转化优先）**：单一使命 = paid/lead gen 战役页 + CRO；按**访客/转化**分档常见。适合 performance marketing、代理店 heavy paid。
- **Type B — Design-first 建站 LP 模式**：强视觉、CMS、SEO、整站发布；战役页是站点子集。适合品牌/content 团队要**设计系统一致** → [`website-builder`](website-builder.md)。
- **Type C — 电商 Campaign Page Builder**：店铺 App 或 AI 生成；页在店铺域/子域，继承 checkout。适合 DTC、大促、influencer 专属 offer。
- **Type D — Funnel / 销售栈**：多步漏斗、upsell、邮件/支付一体；LP 是漏斗第一步。适合信息产品、直销。
- **Type E — Micro LP（极简单页）**：极低价、快上线、弱实验；waitlist/MVP。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **访客上限与超量费**：Unbounce / Instapage 按 UV 分档；大流量 campaign 需建模总成本（Leadpages 等主打 unlimited traffic 作为对位）。
- **托管锁定**：页面常托管在 vendor 子域或 CNAME；迁移需重搭实验与集成。
- **GDPR / CASL / 表单同意**：LP 表单是合规触点；Unbounce 等提供 checkbox 能力，**法律责任在企业**（官方 FAQ 口径）。
- **MCP / AI 数据访问**：Agent 连接 LP 账户时涉及页面与线索数据——企业需审查 OAuth 范围与 DPA。
- **Shopify App 性能与锁定**：App 渲染可能增加 JS；卸载后页面失效风险——native Liquid 生成（Fudge 等）是对立路线。
- **实验伦理与宣称**：第三方「+30% CVR」多为单场景；对外宣称需自有实验证据。

---

## 落地碎片（实践建议）

- 先写清**单一转化目标**与**广告 message**；再选工具——避免先买 SaaS 再改战役结构。
- Paid 量 >$5k/月 且实验频繁 → 评估 **Type A** 的起始 A/B 档位，而非只看入门价。
- 品牌站已用 Framer/Webflow → 战役页优先评估 **能否在同一设计系统内发布**；仅当 CRO 栈不足再叠加 Unbounce。
- Shopify paid → 优先 **Type C** 保证 checkout/pixel；子域名 Instapage 方案需单独测速与归因。
- 记录 **UV 上限 / 超量规则** 于采购 checklist；大促月提前升级或买 overage。
- 将 LP Builder 与 [`advertising-agent`](../marketing-growth/advertising-agent.md) **分工**：Agent 管账户与创意批量；LP 管 post-click 与实验——接口在 UTM + webhook + offline conversion。

---

## 工具与产品类型

> **列举顺序**：**post-click / CRO 垂直**（Unbounce、Instapage）先于 **整站 LP 模式**（Framer、Webflow）；Shopify campaign 类为 **电商子场景垂直**。

| 类型（英文常检索词） | 垂直优先（典型） | 横向 / 附带（典型） | 备注 |
|---------------------|-----------------|-------------------|------|
| **Dedicated LP SaaS** | **Unbounce**, Instapage, Leadpages, Landingi | — | **Landing page 垂直**；CRO + 表单 |
| **Shopify campaign builder** | GemPages, PageFly, Shogun, Replo | — | 店铺内 campaign **垂直** |
| **Shopify AI LP** | Landra, Fudge, Lexsis | — | NL → 店铺页 |
| **Funnel stack** | ClickFunnels, Systeme.io | — | 漏斗 + 支付垂直 |
| **Micro LP** | Carrd | — | 极简单页 |
| **Design LP mode** | — | Framer, Webflow | 整站/SEO；实验弱于 Type A |

---

## 外链索引

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Unbounce** | Dedicated LP + Smart Traffic + MCP（Claude/ChatGPT） | [unbounce.com](https://unbounce.com/) |
| **Instapage** | 企业/代理向；AdMap、协作、Heatmaps | [instapage.com](https://instapage.com/) |
| **Leadpages** | Grow 档含 A/B；全计划 unlimited traffic | [leadpages.com](https://leadpages.com/) |
| **Framer** | AI 建站 + 战役页与 CMS/SEO 一体 | [framer.com](https://www.framer.com/) |
| **Webflow** | 设计控制 + CMS；LP 为站点工作流一部分 | [webflow.com](https://webflow.com/) |
| **GemPages** | Shopify 漏斗与 LP；免费–$199/mo 档 | [gempages.net](https://gempages.net/) |
| **PageFly** | Shopify LP 模板与 CRO 元素 | [pagefly.io](https://pagefly.io/) |
| **Carrd** | 极简单页 | [carrd.co](https://carrd.co/) |

### 对比与测评（第三方；观点非官方）

- **Dedicated 三巨头**：Unbounce 偏 Smart Traffic + MCP 工作流；Instapage 偏 AdMap 与代理协作；Leadpages 2026 重构后以 **Grow $99 含 A/B + 无限流量** 对位（见各厂 pricing T0）。
- **Framer vs Unbounce**（[Framer 官方对比](https://www.framer.com/compare/framer-vs-unbounce)）：整站+战役一体 vs 独立 CRO 实验室——厂商立场，但分流框架可用。
- **Shopify**：GemPages / PageFly 适合 hands-on 商家；AI 生成（Landra 等）适合「要整页生成而非拖拽」团队（垂直媒体 2026 口径，非独立审计）。
- **HN 社区**（T2）：开发者偏静态站自托管；增长团队认可 Instapage/Unbounce/Carrd 换速度——见 [HN 讨论](https://news.ycombinator.com/item?id=21701092)。

---

## 延伸阅读与参考材料

- [Unbounce — What is a landing page](https://unbounce.com/landing-page-articles/what-is-a-landing-page/)（T0 定义）
- [Unbounce — Pricing & MCP FAQ](https://unbounce.com/pricing/)（T0 定价）
- [Unbounce — MCP Server](https://unbounce.com/product/mcp-server/)（T0 AI 工作流）
- [Instapage — Plans](https://instapage.com/plans)（T0）
- [Instapage — Drag-and-drop builder roundup](https://instapage.com/blog/drag-and-drop-landing-page-builder)（T0 类型谱）
- [Leadpages — Platform](https://leadpages.com/platform/landing-page-builder)（T0）
- [Future Market Insights — Landing Page Builders Market](https://www.futuremarketinsights.com/reports/landing-page-builders-market)（T1 市场规模）
- 本次 Web Deep Search 全文：[landing-page-builder-web-search-2026-08-28.md](../../../temp/landing-page-builder-web-search-2026-08-28.md)

---

*档位：B · KB only（发文走 `/blog/landing-page-builder`）· Territory：编程工具链 · 新建 2026-08-28*
