# Sparki Product Video · 页面结构

> 产品/电商视频 SEO 页面。聚合页与形态详情页的 IA、模块与 URL 规则。分类编号见 [video-types-taxonomy.md](./video-types-taxonomy.md) 维度 1-A(F01–F06) 与维度 2-A(C01–C06)。

---

## 一、已上线站点

| 类型 | 正式 URL |
|------|----------|
| 聚合页 | <https://sparki.io/video-editor/product-video> |
| 形态详情页范例 | <https://sparki.io/video-editor/product-demo> |

**URL 规则**

- 聚合页：`/video-editor/product-video`
- 形态详情页：`/video-editor/{format-slug}`

---

## 二、聚合页结构

**URL**：[sparki.io/video-editor/product-video](https://sparki.io/video-editor/product-video)  
**H1**：AI Product Video Maker

页面自上而下模块：

| 模块 | 说明 |
|------|------|
| Hero | 上传框 + Try For Free；副标题说明 cuts / captions / transitions / aspect ratios |
| **Product videos made with Sparki** | 4 帧 9:16 成片轮播（Beauty · Electronics · Home & Kitchen · Fashion） |
| Why Choose Sparki for Product Videos | 6 卡：Clone Styles · Auto Cuts · Auto Captions · Aspect Ratio · Batch Variants · No Skills |
| **Types of Product Video You Can Create** | 两组卡片（见下表）——**核心分类区** |
| Use Cases | 6 Persona：Ecom Sellers · DTC · Agencies · UGC Creators · SaaS Marketers · SMB |
| How to Make a Product Video in 3 Steps | Upload → Pick Format or Reference → Export |
| Explore More Sparki Tools | FeatureNav：Copy Style / Product Video / Gaming / Long to Short / AI Caption / AI Commentary / Video Resizer / Highlight Reels |
| FAQ | 6 条 |
| 底部 CTA | Ready to make your product video? → Try For Free |

### 「Types of Product Video」与 taxonomy 映射

#### By video format（维度 1-A · 6 卡 → 6 个详情页）

| 编号 | 形态 | 聚合页卡片 | 详情页 slug | 状态 |
|------|------|-----------|-------------|------|
| F02 | Product Demo Video | Landing page · 30–60s · 16:9 | `product-demo` | ✅ [已上线](https://sparki.io/video-editor/product-demo) |
| F05 | Product Tutorial | How-to · 60–90s · 16:9 | `product-tutorial` | ✅ [已上线](https://sparki.io/video-editor/product-tutorial) |
| F01 | Unboxing Video | TikTok · 15–45s · 9:16 | `unboxing` | ✅ [已上线](https://sparki.io/video-editor/unboxing) |
| F06 | E-commerce Product Video | Listing · 20–40s · 1:1 | — | ⏳ 仅聚合页 section，**无独立详情页** |
| F04 | Product Review Video | Reels · 20–45s · 9:16 | `product-review` | ✅ [已上线](https://sparki.io/video-editor/product-review) |
| F03 | Product Video Ad | Paid social · 6–30s · 9:16 / 1:1 | `product-ad` | ✅ [已上线](https://sparki.io/video-editor/product-ad) |

#### By industry & channel（维度 2-A · 6 卡 · 仅聚合页）

> 行业组(C01–C06)与平台组(P11–P15)不应混为同一层级。TikTok Shop / Amazon / Meta Ads 等 channel 卡对应 [platforms-pages.md](./platforms-pages.md) P11–P15；品类详情页仍走 `/product-video/{品类}`(规划)。

| 编号 | 品类 | 聚合页卡片 | 详情页 |
|------|------|-----------|--------|
| — | Amazon & Ecommerce Listings | Listing · 30s · 16:9 | ⏳ 规划 `/product-video/{品类}` |
| C01 | Beauty & Skincare | TikTok Shop · 9:16 | ⏳ 规划 |
| C02 | Fashion & Apparel | Reels · 9:16 | ⏳ 规划 |
| C03 | Consumer Electronics & Gadgets | YouTube · 16:9 | ⏳ 规划 |
| C04 | Home & Kitchen | Facebook Ads · 1:1 | ⏳ 规划 |
| C06 | SaaS & App Demos | Product page · 60s · 16:9 | ⏳ 规划 |

> **口径说明**：行业组属于维度 2-A（消费品牌品类），不应与维度 1 格式卡混为同一层级独立页；长尾 URL 规划为 `/product-video/{品类}`，与本地商户 `/industries/{slug}` 分线。

---

## 三、形态详情页结构

5 个已上线形态详情页共用同一模板，自上而下：

| 模块 | 说明 |
|------|------|
| Hero | `AI {Format} Maker` + 价值主张 + 上传框（Upload / YouTube / TikTok / Instagram Link） |
| Trending Shorts 轮播 | 4 条参考 Shorts 缩略图（可选） |
| 导语段 | 1 段 SEO 正文 + 链至 step-by-step guide |
| **Why Choose Sparki for {Format}** | 6 条形态专属卖点 |
| **Who Makes {Format} With Sparki** | 3 个 Persona |
| How to Make a {Format} in 3 Steps | Upload → Pick style or reference → Export |
| **Related Product Video Formats** | 链至同簇其他 5 个形态详情页 |
| FAQ | 5–6 条形态专属问题 |
| 底部 CTA | Try For Free |

**SEO 约定**

- Title 模式：`AI {Format} Maker for {Use Case} | Sparki`
- 面包屑：Home → Product Video → {Format}

---

## 四、已上线形态详情页清单

| slug | H1 | URL |
|------|-----|-----|
| `product-demo` | AI Product Demo Video Maker | [product-demo](https://sparki.io/video-editor/product-demo) |
| `product-tutorial` | AI Product Tutorial Video Maker | [product-tutorial](https://sparki.io/video-editor/product-tutorial) |
| `unboxing` | AI Unboxing Video Maker | [unboxing](https://sparki.io/video-editor/unboxing) |
| `product-review` | AI Product Review Video Maker | [product-review](https://sparki.io/video-editor/product-review) |
| `product-ad` | AI Product Video Ad Maker | [product-ad](https://sparki.io/video-editor/product-ad) |

### Product Demo 详情页要点（范例）

| 模块 | 内容摘要 |
|------|---------|
| 定位 | DTC landing page / SaaS / ecommerce 的「产品在用」证明剪辑 |
| Why 6 卡 | In Use Not On Shelf · Feature Callouts · Physical + Screen · Landing-Page Length · Punch-Ins · 16:9 + 9:16 |
| Persona | DTC Landing Page Teams · SaaS Product Marketers · Ecommerce Sellers |
| FAQ 核心 | 时长(30–60s) · 手机素材 · SaaS 录屏 · vs Unboxing · vs Tutorial |

---

## 五、分类漂移与待定项

| 项目 | 状态 | 说明 |
|------|------|------|
| F06 E-commerce 独立页 | ⏳ | 聚合页有卡片，独立 URL 尚未上线 |
| C01–C06 品类长尾页 | ⏳ | 聚合页「By industry」组已有文案，详情页暂缓 |
| Product Explainer | ❌ 不占独立形态位 | F05×F02 混合；裸词偏动画外包，与素材重剪工具不匹配 |
| Product Launch Video | ❌ 并入 F03 | 属 Product Ad 投放场景 |
| UGC 定语 | ⚠️ | Review 卡历史上加 UGC 前缀；测评不限于 UGC 形式 |

**已拍板决策（2026-08-12）**

- [x] A 类 6 形态：建 4 个独立页(Demo / Review / Ad / E-commerce) + Unboxing / Tutorial 各建详情页 → **线上 5/6 形态详情页已上线**，E-commerce 仍仅 section
- [x] 维度 2 拆分：C01–C06 与 B1–B7 文档层已完成；行业长尾页落地暂缓
- [ ] 代码层：`VideoTypes` 卡片 href + `src/content/taxonomy.ts` 数据源化

---

*遵循 [客户文档规范](../../demo/client-template.md)*  
*关联：[video-types-taxonomy.md](./video-types-taxonomy.md) | [industries-pages.md](./industries-pages.md) | [keywords](../sparki-keywords.md)*  
*Last updated: 2026-08-26*
