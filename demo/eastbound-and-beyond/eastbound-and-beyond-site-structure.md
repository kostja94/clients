# Eastbound and Beyond — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./eastbound-and-beyond.md) | [keywords](./eastbound-and-beyond-keywords.md) | [features](./eastbound-and-beyond-features.md) | [competitors](./eastbound-and-beyond-competitors.md) | [use-cases](./eastbound-and-beyond-use-cases.md) | [growth-strategy](./eastbound-and-beyond-growth-strategy.md)

**Last updated**: 2026-07-27 | 识别方式：robots.txt + sitemap.xml + 首页 withAllLinks + 核心页抓取（[eastboundandbeyond.com](https://eastboundandbeyond.com/)）

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 | 状态 |
|------|---------|-----------|--------|------|
| `/` | 首页（价值主张 + 评价轮播 + CTA） | curated China tours, Shanghai cultural tour | P0 | 已上线 |
| `/pages/curated-city-tours` | 城市日游目录（Private / Small-Group 分区） | private city tour China, small group Shanghai tour | P0 | 已上线 |
| `/pages/china-journeya` | 多日定制行程构建器（选城市→天数→体验→提交） | customize China trip, multi-day China itinerary | P0 | 已上线 |
| `/pages/about-us` | 品牌故事、核心数据、价值观 | Eastbound and Beyond reviews, boutique China travel | P1 | 已上线 |
| `/pages/guides` | 导游团队介绍（20+ 导游卡片） | China tour guide English speaking | P1 | 已上线 |
| `/products/shanghai-full-day-tour` | 旗舰私享日游产品页 | Real Shanghai in a day, private Shanghai tour | P0 | 已上线 |
| `/products/breakfast-in-shanghai` | 小团美食步行团产品页 | Shanghai breakfast food tour | P0 | 已上线 |
| `/blogs/news` | Things to Do 内容 hub（月度 Top Spots / Top Eats） | things to do Shanghai, where to eat Shanghai | P1 | 已上线 |
| `/policies/terms-of-service` | 条款 | — | P2 | 已上线 |

访问日期：2026-07-27。来源：[eastboundandbeyond.com](https://eastboundandbeyond.com/)

---

## 2. URL 层级与信息架构

```
eastboundandbeyond.com（Shopify 电商 + Tapita 页面构建）
├── /                                    # 首页
├── /pages/
│   ├── curated-city-tours               # 城市日游总览（#private / #small-group）
│   ├── china-journeya                   # 定制多日行程（交互式 builder）
│   ├── customize-your-journey           # 定制入口（sitemap 别名）
│   ├── about-us                         # 关于我们
│   ├── guides                           # Meet Our Guides
│   ├── contact                          # 联系
│   ├── bookings-terms                   # 预订条款
│   └── example-itineraries/             # 示例多日线路（8 条主题页）
│       ├── iconic-beijing
│       ├── shanghai-journey
│       ├── chinas-golden-route-beijing-xian-and-shanghai
│       ├── poetic-southern-china
│       ├── natural-wonders-of-china
│       ├── new-china-cities-of-the-future
│       ├── china-villages-arts-and-cultural-heritage
│       └── the-flavour-journey-tastes-of-china
├── /products/{slug}                     # 可预订日游产品（17 条）
├── /collections/                        # 集合页（1 条，Shopify 默认）
├── /blogs/
│   ├── news/{slug}                      # 月度本地指南（~28 篇）
│   ├── things-to-do                     # 博客索引
│   └── top-spots                        # 博客索引
├── /policies/                           # privacy / terms / refund 等
└── /cart                                  # 购物车（robots Disallow checkout 流程）
```

### 主导航结构

| 一级 | 二级 | 代表 URL |
|------|------|---------|
| City Tours | Private City Tours（按城市：Beijing / Shanghai / Suzhou / Hangzhou） | `/products/beijing-private-forbidden-city` 等 |
| City Tours | Small-Group City Tours（Beijing / Shanghai） | `/products/breakfast-in-shanghai` 等 |
| Multi-Day Journey | Customize Your Journey | `/pages/china-journeya` |
| Multi-Day Journey | Our Example Tours | `/pages/china-journeya#example-china-trips` |
| Our Company | Meet Our Guides / About Us | `/pages/guides`、`/pages/about-us` |
| Things to Do | 博客 hub | `/blogs/news` |

### 页脚内链

Private / Small-Group Tours · Customize · Example Tours · About · Guides · Privacy · Terms · Email / WhatsApp / TripAdvisor / Instagram / Facebook

---

## 3. 技术架构

| 维度 | 观测 | 依据 |
|------|------|------|
| 平台 | **Shopify**  storefront | robots.txt 注释 "Shopify storefront"；UCP/MCP 端点 |
| 页面构建 | **Tapita**（评价轮播、产品区块） | 首页/产品页 "powered by Tapita" |
| 支付 | PayPal + PayPal 授权信用卡（4.4% 手续费） | 产品页 Cancellation Policy |
| robots | Allow `/`；Disallow `/admin`、`/cart/`、`/checkout`、filter/sort 陷阱 | [robots.txt](https://eastboundandbeyond.com/robots.txt) 2026-07-27 |
| Agent 接口 | `agents.md`、UCP discovery、MCP endpoint | robots.txt 声明 |
| Sitemap | 5 个子 sitemap（products / pages / collections / blogs / agentic_discovery） | [sitemap.xml](https://eastboundandbeyond.com/sitemap.xml) |
| 多语言 | 英文为主；未见 hreflang / 语言切换 | 待验证 |
| CDN | Shopify CDN（`/cdn/` 路径） | 标准 Shopify |

---

## 4. 多语言

| 项 | 状态 |
|----|------|
| 站点语言 | 英文（面向国际游客） |
| hreflang | 未见 |
| 本地化 | 导游页含俄语专长（Tongfei）；站点 UI 无多语言 |
| 联系渠道 | Email、WhatsApp（+86）、美国电话 +1 (917) 9206-248、WeChat |

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| sitemap_products_1 | `/products/{slug}` | **17** 产品 + 首页 | 2026-07-27 |
| sitemap_pages_1 | `/pages/{slug}` | **~18** 页面 | 2025-02 ~ 2026-05 |
| sitemap_collections_1 | `/collections/{slug}` | **1** | — |
| sitemap_blogs_1 | `/blogs/news/{slug}` 等 | **~31** URL（含 3 个 blog 索引） | 2025-03 ~ 2026-07 |
| sitemap_agentic_discovery | Agent 发现用 | ⚠️ 待验证 | — |

**URL 模式归纳**：

- 产品：`/products/{kebab-slug}`（如 `shanghai-full-day-tour`、`beijing-breakfast`）
- 内容页：`/pages/{kebab-slug}`
- 博客：`/blogs/news/{monthly-slug}`（`where-to-eat-this-{month}-...` / `where-to-go-this-{month}-...`）
- 政策：`/policies/{policy-type}`

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/` 首页 | 产品卡片、Our Story、评价 | 私享/小团 flagship 产品、About |
| `/pages/curated-city-tours` | 全量日游产品 | 转化预订 |
| `/pages/china-journeya` | 城市选择 + 示例线路 + 询价表单 | 多日定制线索 |
| `/pages/guides` | 导游信任背书 | 提升转化、降低决策焦虑 |
| `/blogs/news` | 月度本地指南 | SEO 长尾、品牌权威 |
| 产品页 | Q&A、Book Now、联系 CTA | 直接转化 |

---

## 7. URL 分阶段规划

| 阶段 | 建议新增页面 | 对标关键词优先级 |
|------|-------------|-----------------|
| **短期（0–3 月）** | `/pages/shanghai-food-tours` 着陆页（聚合 5 条上海美食/步行团） | P0：`shanghai food tour` |
| **短期** | `/pages/beijing-private-tours` 城市 hub 页 | P0：`beijing private tour` |
| **短期** | `/blogs/news/shanghai-food-tour-vs-walking-tour` 对比文 | P1：信息型意图 |
| **中期（3–6 月）** | `/pages/eastbound-and-beyond-vs-getyourguide` 差异化对比 | P1：商业型 |
| **中期** | 示例线路独立 SEO 页优化（8 条已有 page，补 meta + 内链） | P1：`China itinerary 10 days` |
| **长期（6–12 月）** | `/pages/china-travel-guide` 权威 hub + 链向 blog 集群 | P0：信息型集群 |
| **长期** | 多城市 landing（Xi'an / Chengdu 定制 builder 已有选项，缺独立 SEO 页） | P2 |

---
