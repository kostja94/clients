# 2mv — 站点结构

> 面向海外市场（英文为主）。本文件为纯事实层：URL、IA、技术栈。产品能力见 [2mv-features.md](./2mv-features.md)。

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（Landing）：五引擎 agency 定位、对比矩阵、病毒案例、Book a demo CTA | 2mv, ai social media marketing agency | P0 |
| `/research` | Research Lab 产品页（SaaS）：5 大视图、定价、FAQ、证言、niche 列表 | viral video finder, social media analytics tool, social media competitor analysis | P0 |
| `/insights` | 博客列表页（目前仅 1 篇博文） | viral content guides, tiktok trends | P1 |
| `/insights/{slug}` | 博文详情页（`how-to-find-viral-content-ideas-before-they-peak` 等） | how to find viral content ideas | P1 |
| `/book-a-demo` | 预约演示表单（name / work email / brand website / social links） | book a demo, ai marketing agency | P1 |
| `/privacy-policy` | 隐私政策（Fluxspark Inc.，Last updated 2026-06-25） | — | P2 |
| `/terms-of-use` | 服务条款（页脚链接「terms of use」，实际路径 `待验证`） | — | P2 |

> 站点抓取日期：2026-08-13。`/service`、`/services`、`/research-lab`、`/privacy`、`/terms`、`/terms-of-use` 均返回 404 或未确认，真实 URL 以页脚链接为准，详见 §2。

---

## 2. URL 层级（IA 树）

```
2mv.ai
├── 首页 /                    五引擎 agency 叙事（Watch→Decode→Architect→Produce→Grow）+ 对比矩阵
├── 产品层
│   └── /research             Research Lab SaaS：5 视图 + 定价 + FAQ + 证言 + niche
├── 内容层
│   ├── /insights             博客列表
│   └── /insights/{slug}      博文详情（当前仅 1 篇）
├── 转化层
│   └── /book-a-demo          预约演示表单
├── 法务层
│   ├── /privacy-policy       隐私政策
│   └── /terms-of-use         服务条款（路径待验证）
└── API（robots Disallow）
    └── /api/                 后端接口，禁止爬取
```

**导航标签 vs 实际 URL 映射**（页脚「explore: service / research lab / insights」）：

| 导航标签 | 实际 URL | 备注 |
|---------|---------|------|
| service | 待验证（`/service`、`/services` 均 404，可能指向首页或 `/research`） | 待验证 |
| research lab | `/research` | 已确认 |
| insights | `/insights` | 已确认 |
| book a demo | `/book-a-demo` | 已确认 |
| privacy policy | `/privacy-policy` | 已确认 |
| terms of use | 待验证（`/terms`、`/terms-of-use` 均 404） | 待验证 |

---

## 3. 技术架构

| 维度 | 识别 | 识别方式 |
|------|------|---------|
| 前端框架 | 疑似 Next.js SPA（未确认） | `待验证`（需查看页面 HTML 资源路径） |
| 支付 | Stripe（隐私政策声明：billing info processed by Stripe） | /privacy-policy 2026-08-13 |
| 运营主体 | Fluxspark Inc. | /privacy-policy 2026-08-13 |
| 联系邮箱 | hi@2mv.ai | /privacy-policy + /research 2026-08-13 |
| 托管 / CDN | 未确认 | `待验证` |
| 分析 / 埋点 | 未确认 | `待验证` |
| OAuth 集成 | 支持连接 TikTok / Instagram / YouTube 第三方账号（OAuth 授权） | /privacy-policy §1.c 2026-08-13 |

---

## 4. 多语言

- 目前为**英文单语**站点（未发现 hreflang 或多语言路径）。目标市场覆盖 TikTok / Reels / Shorts 三平台全球用户，`待验证：是否有本地化计划`。

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| robots.txt 声明 | `sitemap.xml` | 抓取返回 **500**，无法确认内容 | 待验证 |
| 已确认路径 | `/`、`/research`、`/insights`、`/book-a-demo`、`/privacy-policy` | 5 个一级路径 | 2026-08-13 |
| 博文 | `/insights/{slug}` | 1 篇（"How to Find Viral Content Ideas Before They Peak"，2026-07-22） | 2026-08-13 |

> 完整 URL 明细无法获取（sitemap.xml 返回 500）。`⚠️ 待验证：sitemap.xml 是否有效；/terms-of-use 与 service 页真实 URL；博文详情页 URL 模式`。

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 `/` | 主导航 CTA：Book a demo / Start research / 五引擎区块 | /book-a-demo、/research、注册转化 |
| 主导航 | service（待验证）、research lab、insights | 产品页、博客 |
| 页脚 | explore（service / research lab / insights）、connect（book a demo）、legal（privacy / terms） | 全站核心页 |
| `/research` | 定价卡 CTA「Start for free」、FAQ「Contact us via hi@2mv.ai」 | 注册转化、邮件线索 |
| `/insights` | 博文卡片 → 详情页 | 内容阅读 |

---

## 7. URL 分阶段规划

| 阶段 | 新增页面 | 对应关键词优先级 | 理由 |
|------|---------|----------------|------|
| 短期（0–3 月） | 修复 sitemap.xml（当前 500） | — | 影响抓取与收录，SEO 基建 |
| 短期 | `/research` 建设 analytics 核心词池 + 主词 viral video finder | P0 商业型词 | 承接 social media analytics tool（8,100 月搜）等 331 词 |
| 短期 | `/research/social-media-competitor-analysis`（首个下级页） | P0 商业型词 | 意图明确，竞品有真实页面支撑，Phase 1 提前建设 |
| 短期 | `/insights` 扩容（问题型文章、niche 解码、趋势报告系列） | P0/P1 信息型词 | 当前仅 1 篇博文，内容缺口最大 |
| 中期（3–6 月） | `/tools/competitor-content-analyzer`、`/tools/post-analysis` 工具页 | P1 工具型词 | 复用工具页模板；跑通后再决定 `/tools` Hub 是否上线 |
| 中期 | 独立 `/pricing` 页（当前定价内嵌于 `/research`） | P1 商业型词 | 定价透明度影响转化 |
| 中期 | `/service`（代运营）独立落地页 | P1 导航/商业型词 | 代运营形态目前与首页耦合，无独立 URL |
| 长期（6–12 月） | 平台页 `/research/tiktok-analytics` 等（Phase 2/3） | P2 平台词 | tik tok analytics（33,100）等词量大但后置 |
| 长期 | `/resources/social-media-audit`、`social-media-benchmarks` | P2 资源词 | audit 词池（2,900）有 lead magnet 价值 |
| 长期（观察） | `/niches/{slug}` 各细分领域落地页（500+ niches） | P2 长尾词 | programmatic SEO 机会，量级大 |

---

> 关联：[主文档](./2mv.md) | [keywords](./2mv-keywords.md) | [features](./2mv-features.md) | [competitors](./2mv-competitors.md) | [use-cases](./2mv-use-cases.md) | [growth-strategy](./2mv-growth-strategy.md)

*Last updated: 2026-08-14（URL 规划对齐 Keyword Planner 真实词池）*
