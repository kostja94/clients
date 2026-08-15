# Oginify 使用场景（Index）

> **本文档职责**：使用场景总入口——场景总览、S/A/B/C 分级快查、子文档导航。面向用户的场景展示与决策框架。  
> **子文档**：[by-page-type.md](./by-page-type.md) 页面类型（58 种 S/A/B/C） | [by-site-type.md](./by-site-type.md) 网站类型（16 种） | [by-style.md](./by-style.md) 风格（6+10 种 + A/B 测试） | [by-image-size.md](./by-image-size.md) 图片尺寸（1200×630 全场景 + 平台限制 + 一图多用）  
> **引用**：[主文档](../oginify.md) 概览 | [features](../oginify-features.md) 产品 | [keywords](../oginify-keywords.md) 关键词 | [growth-strategy](../oginify-growth-strategy.md) 增长

---

## 为什么重构

旧分类（website-owners / seo-marketing / ai-builders / cms-platforms）存在两个问题：

1. **维度混乱**：前两个是「角色 + 渠道」，后两个是「集成方」。一个独立站长既是 website-owner 又在做 seo-marketing，不知道自己该点哪个。
2. **搜索意图弱**：用户不会搜"website owner og image"——他们会搜"og image for blog post"或"landing page social share card"。

新体系用两个正交维度：**页面类型**（你有什么页面）和 **网站类型**（你是什么站），一个穷举一个聚合，不重叠。

---

## 与线上 `/use-cases` 的分工

| | 线上 [oginify.com/use-cases](https://oginify.com/use-cases) | 本文档文件夹 |
|---|---|---|
| **受众** | 访客、B2B 集成咨询 | 内部策略、SEO 内容规划 |
| **结构** | 三轴（page / website / style）+ CMS/Agency/API | 四维度穷举（page-type / site-type / style / image-size） |
| **深度** | 营销导向，部分标 Soon | 58 种页面 S/A/B/C、16 种网站类型 |

两者互补：线上页获客，本文件夹做策略与 pSEO 规划。详见 [site-structure](../oginify-site-structure.md#与文档-use-cases-的分工)。

**定价口径**：SaaS **6 张/天**免费；主流程非 AI（截图+模板），AI 仅用于 Regenerate；超额 PAYG $0.99 / Bundle $7.90–$29.00。Skills MIT 永久免费。

---

## 场景总览（8 个场景）

| # | 场景 | 状态 | JTBD | 目标用户 |
|---|------|------|------|----------|
| 1 | Landing Pages | ✅ | 产品页需要贴合品牌、可 A/B 测试的 OG 图 | SaaS 创始人、产品营销 |
| 2 | Blog Posts & Articles | ✅ | 内容站批量自动出图，每篇一张风格统一的卡片 | 内容创作者、SEOer、媒体 |
| 3 | Product & Pricing Pages | ✅ | 商品/定价页，卖点、价格需要在图上体现 | 电商运营、增长团队 |
| 4 | Marketing Campaigns | ✅ | 活动/Newsletter 短链，wildcard 风格测点击率 | 市场团队、增长黑客 |
| 5 | Docs & Changelog | ✅ | 文档/版本日志，终端/CLI 调性 OG 图 | 开发者关系、开源维护者 |
| 6 | Portfolio & Personal | ✅ | 个人站/作品集，个人品牌调性 | 独立开发者、设计师 |
| 7 | About & Brand Pages | 🔲 | 公司/品牌关于页，PR 引用时展示品牌形象 | 品牌经理、PR 团队 |
| 8 | Category & Collection Pages | 🔲 | 电商/内容站分类页，体现品类调性 | 电商运营、内容站编辑 |

完整场景详情（JTBD、用户路径、关键词）见子文档。场景 1–6 的细节保留在下方折叠区。

---

## OG 图优先级快查（S/A/B/C）

决定哪些页面值得花 AI 成本单独生成 OG 图：

| 级别 | 定义 | 典型页面 | 策略 |
|------|------|---------|------|
| **S（必做）** | 页面天然为分享而存在 | blog post, case study, research report, changelog, event, campaign landing | 每页单独生成，预算不限 |
| **A（高优）** | 分享后转化价值极高 | homepage, pricing, feature, use-case, comparison/vs, PDP, newsletter, waitlist, showcase | 单独生成，优先于 B |
| **B（中）** | 偶尔分享，做不做得看量 | about, category, integration, template, author, docs, tutorial, forum, careers, podcast | 量大用模板批量；量少单独做 |
| **C（跳过）** | 几乎无人分享 | login, signup, cart, checkout, dashboard, billing, privacy, terms, 404, contact | 设置一张品牌默认图保底 |

完整 9 大类 × 每个页面类型的 S/A/B/C 标注见 [by-page-type.md](./by-page-type.md)。

---

## 文档导航

| 文档 | 职责 | 什么时候看 |
|------|------|-----------|
| [index.md](./index.md) | **本文档**：场景总览、分级快查、子文档入口 | 先看这个 |
| [by-page-type.md](./by-page-type.md) | 穷举所有页面类型，S/A/B/C 分级 + OG 图策略 | 想知道"我的页面值不值得做" |
| [by-site-type.md](./by-site-type.md) | 按网站类型组织：覆盖 16 种网站类型 | 想知道"我这种站怎么做 OG 图" |
| [by-style.md](./by-style.md) | OG 图风格分类：6 已实现 + 10 可扩展，风格 × 页面 × 平台三维匹配，A/B 测试框架 | 想知道"用什么风格效果最好"或"怎么做 A/B 测试" |
| [by-image-size.md](./by-image-size.md) | 图片尺寸参考：1200×630 全场景（OG + 广告 + 博客头图）、平台限制、易混淆尺寸、一图多用 | 想知道"这个尺寸还能用在哪"或"各平台有什么限制" |

---

## 场景详情（1–6 已实施）

### 1. Landing Pages — 产品落地页

**JTBD**：我上线了一个 SaaS 产品/功能页面，需要一张 1200×630 的社交分享图。图要贴合品牌调性，不准模板感。最好能一次出几个方案让我选，或者做个 A/B 对比。

**典型用户**：SaaS 创始人、产品营销经理、独立开发者发布新产品

**使用路径**：粘贴 landing page URL → AI 读页面理解产品定位与品牌色 → 品牌贴合风格（主力）→ 下载部署 → 改版后重新生成对比新旧点击率。

**Oginify 匹配点**：截图保真 + 模板渲染双管齐下；AI Regenerate 按需补充；零成本随时重生成。

**SEO 关键词**："og image for landing page""saas social share card""startup og image""product launch social card"

### 2. Blog Posts & Articles — 博客与内容站

**JTBD**：博客几十上百篇文章，不想每篇手动做 OG 图。最好是自动的，每篇文章根据标题和内容生成风格统一的卡片。

**典型用户**：SEOer、内容创作者、媒体编辑、用 WordPress/Ghost 的博主

**使用路径**：单个粘贴文章 URL → AI 读标题+摘要 → 杂志风或报纸风。批量（规划中）sitemap URL → 批量生成。集成（规划中）CMS 插件 → 发布时自动触发。

**Oginify 匹配点**：截图+模板覆盖内容站日常需求；杂志风/报纸风天然匹配；6 张/天免费对文章多的站足够试用。

**SEO 关键词**："og image for blog post""auto generate og image""wordpress og image generator""blog social share card"

### 3. Product & Pricing Pages — 商品与定价页

**JTBD**：电商/SaaS 商品页或定价页。OG 图上面要有产品名、价格、卖点。图片本身要传达价值。

**典型用户**：电商运营、SaaS 定价页负责人、DTC 品牌

**使用路径**：粘贴 product/pricing URL → AI 提取产品名+价格+卖点 → 品牌贴合风格 → 下载配置。

**Oginify 匹配点**：AI 自动识别页面上的价格、CTA、卖点文字；品牌贴合风保持视觉一致性；免费不成为放弃 OG 图的理由。

**SEO 关键词**："product page og image""ecommerce social share card""pricing page og image""shopify og image"

### 4. Marketing Campaigns — 营销活动

**JTBD**：投放/Newsletter/活动，落地页是临时的。OG 图不需要精致但要抓眼球，风格可以大胆。最好能快速试几个版本。

**典型用户**：市场团队、增长黑客、Newsletter 作者

**使用路径**：粘贴 campaign landing URL → AI 读活动主题 → 终端风/复古风/杂志风（最大胆的）→ 快速多套 → 投放看 CTR。

**Oginify 匹配点**：6 种风格任选 + AI Regenerate；campaign 适合偏离日常品牌调性；6 张/天免费，OG 图这环不是 campaign 预算大头。

**SEO 关键词**："campaign og image""social card for newsletter""event og image""marketing social share card"

### 5. Docs & Changelog — 文档与更新日志

**JTBD**：开源项目/开发者工具的文档站和 changelog，OG 图需要终端风、命令行风、代码等宽字体。不需要花哨，但要一眼看出来是给开发者看的。

**典型用户**：开源维护者、DevRel、技术文档团队

**使用路径**：粘贴 docs/changelog URL → AI 识别文档类型 → 终端风（主力）→ 下载配置 → 每次发新 changelog 重新生成。

**Oginify 匹配点**：终端风天然匹配；同步 Skills 供不想用 SaaS 的开发者在 Cursor 里运行；免费适合开源项目。

**SEO 关键词**："docs og image""changelog social card""terminal style og image""dev tool og image"

### 6. Portfolio & Personal Sites — 作品集与个人站

**JTBD**：个人网站/作品集需要 OG 图。不是公司站，有个人风格即可。可能就一两张，不想为这个学 Canva。

**典型用户**：独立开发者、设计师、自由职业者、学生

**使用路径**：粘贴个人站 URL → 读页面内容与个人定位 → 每次 2 张（截图 + 模板，6 风格可选）→ 挑最喜欢的 → 下载配置；改版或新 project 页可再生成。

**Oginify 匹配点**：6 风格库 + 截图+模板组合；零门槛不学设计工具；6 张/天免费试用，超额 PAYG / Bundle——个人站页数少但单页仍值得独立预览图。

**SEO 关键词**："portfolio og image""personal site social share card""about me page og image""designer portfolio og image"

---

## 与产品矩阵的对应关系

| 场景 | 主力产品 | 辅助产品 |
|------|---------|----------|
| Landing Pages | Generator（品牌贴合风格） | Validator（发布前校验） |
| Blog Posts | Generator（杂志/报纸风） | Gallery（看同行博客 OG 图） |
| Product & Pricing | Generator（品牌贴合风格） | Websites Without（看竞品有没有配 OG） |
| Marketing Campaigns | Generator（终端/大胆风格） | Validator（各平台预览一致性） |
| Docs & Changelog | Generator（终端风）+ Skills | Gallery（参考其他 dev tool OG） |
| Portfolio | Generator（6 风格库，每次 2 张） | Gallery（看同行个人站 OG 图） |
| About & Brand（候选） | Generator（品牌贴合 + 杂志风） | Validator |
| Category & Collection（候选） | Generator（品牌贴合风） | Gallery |

---

## 旧分类对照

| 旧分类 | 映射到新场景 | 说明 |
|--------|------------|------|
| website-owners | Landing Pages / Portfolio / Blog Posts | 旧分类太宽，拆为三个具体场景 |
| seo-marketing | Blog Posts / Campaigns | SEO 做内容站 → Blog；投放/活动 → Campaigns |
| ai-builders | Landing Pages / Docs | AI 产品落地页 + AI 工具文档 |
| cms-platforms | Blog Posts / Product | CMS 集成对应内容站和电商站 |

---

## 实施优先级

| 优先级 | 场景 | 状态 | 理由 |
|--------|------|------|------|
| **P0** | Blog Posts & Articles | ✅ | 用户量最大，搜索量最高 |
| **P0** | Landing Pages | ✅ | 最核心 SaaS 场景 |
| **P1** | Portfolio & Personal | ✅ | 页数少但单页预览图仍重要；6 张/天免费 + PAYG |
| **P1** | Docs & Changelog | ✅ | Skills 交叉引流，开发者群体 |
| **P2** | Product & Pricing Pages | ✅ | 电商场景，信息提取能力要求高 |
| **P2** | Marketing Campaigns | ✅ | 批量需求，适合未来 sitemap 功能 |
| **P3** | Category & Collection | 🔲 | 电商第二场景，用户量待验证 |
| **P3** | About & Brand Pages | 🔲 | 分享频率中等，搜索量待验证 |
| **P4** | 品牌默认图生成 | 🔲 | 搭配批量功能，先做框架再做功能 |
| **P4** | 批量生成 + 优先级建议 | 🔲 | 内容站刚需，实施成本高 |

---

*Last updated: 2026-05-31*
