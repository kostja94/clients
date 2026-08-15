# TLDR 底部 Skills 推广方案

在每篇文章的 TLDR 最底部无缝添加与主题相关的 npx 指令，引导读者用 Cursor / OpenClaw（小龙虾）安装对应技能并转化至 GitHub 点赞。

**参考**：[section-tldr](../section/section-tldr.md)、[template-skills](./template-skills.md)

---

## 〇、目标与原则

| 目标 | 说明 |
|------|------|
| **主题相关** | 技能与文章主题一一对应，无匹配则不加 |
| **agent/OpenClaw** | 文案用「让 agent / OpenClaw 帮你」，不用「让 AI 帮你」 |
| **无缝结合** | 与 TLDR 融为一体，不干扰阅读，无视觉割裂 |
| **转化 GitHub** | 引导 Star → 提升 marketing-skills 曝光 |

---

## 一、技术方案

### 1.1 扩展 Tldr 组件

新增可选 prop `skillCta`，当传入时在 TLDR 底部**无缝**渲染技能 CTA：

```tsx
skillCta?: {
  skills: string[];      // 1–3 个 skill name
  description: string;   // 吸引文案，用 agent/OpenClaw
  locale?: 'zh' | 'en';
}
```

### 1.2 无缝设计要点

- **无分隔线**：不加 `border-t`，与要点列表自然衔接
- **同字号/色**：描述与 items 一致 `text-[15px] text-muted-foreground`
- **命令块**：轻量 `font-mono` 行内块，与 TLDR 卡片风格统一（非黑底 Terminal）
- **作为最后一条**：视觉上像 TLDR 的延伸，而非独立 CTA 区

### 1.3 命令格式

```bash
npx skills add kostja94/marketing-skills --skill affiliate-marketing affiliate-page-generator
```

### 1.4 Star/Fork CTA

在 skillCta 底部增加 GitHub 呼吁，引导用户 Star 或 Fork 获取 160+ 全套技能：

| 语言 | 文案 |
|------|------|
| 中文 | Star 或 Fork 获取 160+ 全套技能 → |
| 英文 | Star or fork on GitHub for 160+ skills → |

链接：`https://github.com/kostja94/marketing-skills`，新标签打开。详见 [template-add-star-fork-cta](./template-add-star-fork-cta.md)。

---

## 二、文案规范

### 2.1 描述模板（agent / OpenClaw）

| 语言 | 模板 | 示例 |
|------|------|------|
| 中文 | 用 Cursor / OpenClaw 帮你 [动作/产出] | 用 Cursor / OpenClaw 帮你规划联盟计划和落地页 |
| 英文 | Use Cursor / OpenClaw to [verb] your [noun] | Use Cursor / OpenClaw to plan your affiliate program & landing page |

**备选**：`让 agent 帮你` / `Let your agent` — 与 OpenClaw 品牌一致。

### 2.2 字数

- 中文：12–22 字
- 英文：8–15 词

---

## 三、页面 → 技能映射（仅加有 TLDR 且技能匹配的页面）

### 3.1 映射规则

- **无 TLDR** → 不加
- **与现有 skills 完全不相关** → 不加
- **1:1 或强相关** → 加

### 3.2 映射表

| 页面（含 EN） | 技能 | 中文描述 | 英文描述 |
|---------------|------|----------|----------|
| **Marketing** | | | |
| Affiliate | affiliate-marketing, affiliate-page-generator | 用 Cursor / OpenClaw 帮你规划联盟计划和落地页 | Use Cursor / OpenClaw to plan your affiliate program & landing page |
| InfluencerMarketing | influencer-marketing | 用 Cursor / OpenClaw 帮你规划红人合作 | Use Cursor / OpenClaw to plan influencer partnerships |
| ReferralProgram | referral-program | 用 Cursor / OpenClaw 帮你设计推荐计划 | Use Cursor / OpenClaw to design your referral program |
| GEO | generative-engine-optimization | 用 Cursor / OpenClaw 帮你优化 AI 搜索可见性 | Use Cursor / OpenClaw to optimize for AI search visibility |
| KeywordResearch | keyword-research, content-strategy | 用 Cursor / OpenClaw 帮你做关键词与内容策略 | Use Cursor / OpenClaw for keyword & content strategy |
| CreatorProgram | creator-program | 用 Cursor / OpenClaw 帮你规划创作者计划 | Use Cursor / OpenClaw to plan your creator program |
| CreatorContest | contest-page-generator | 用 Cursor / OpenClaw 帮你设计竞赛落地页 | Use Cursor / OpenClaw to design your contest landing page |
| EmailMarketing | email-marketing | 用 Cursor / OpenClaw 帮你规划邮件营销 | Use Cursor / OpenClaw to plan email marketing |
| RedditMarketing | reddit-posts | 用 Cursor / OpenClaw 帮你写 Reddit 内容 | Use Cursor / OpenClaw to write Reddit posts |
| LocalizationStrategy | localization-strategy | 用 Cursor / OpenClaw 帮你规划本地化 | Use Cursor / OpenClaw to plan localization |
| PricingPackaging | pricing-page-generator, pricing-strategy | 用 Cursor / OpenClaw 帮你设计定价页 | Use Cursor / OpenClaw to design your pricing page |
| LifetimeDeal | discount-marketing-strategy | 用 Cursor / OpenClaw 帮你规划折扣策略 | Use Cursor / OpenClaw to plan discount strategy |
| CompetitiveAnalysis | competitor-research | 用 Cursor / OpenClaw 帮你做竞品调研 | Use Cursor / OpenClaw for competitor research |
| XFormerlyTwitter | twitter-x-posts | 用 Cursor / OpenClaw 帮你写 X 帖子 | Use Cursor / OpenClaw to write X posts |
| MarketingTypes | integrated-marketing | 用 Cursor / OpenClaw 帮你规划整合营销 | Use Cursor / OpenClaw to plan integrated marketing |
| **SEO** | | | |
| RobotsTxt | robots-txt | 用 Cursor / OpenClaw 帮你配置 robots.txt | Use Cursor / OpenClaw to configure robots.txt |
| Sitemap | xml-sitemap | 用 Cursor / OpenClaw 帮你创建与优化 sitemap | Use Cursor / OpenClaw to create & optimize sitemap |
| SchemaGuide | schema-markup | 用 Cursor / OpenClaw 帮你添加结构化数据 | Use Cursor / OpenClaw to add structured data |
| LandingPage | landing-page-generator | 用 Cursor / OpenClaw 帮你写落地页 | Use Cursor / OpenClaw to write your landing page |
| Domain | domain-selection | 用 Cursor / OpenClaw 帮你选 SEO 友好域名 | Use Cursor / OpenClaw to choose an SEO-friendly domain |
| Breadcrumbs | breadcrumb-generator | 用 Cursor / OpenClaw 帮你添加面包屑 | Use Cursor / OpenClaw to add breadcrumbs |
| CategoryPages | category-page-generator | 用 Cursor / OpenClaw 帮你设计分类页 | Use Cursor / OpenClaw to design category pages |
| InternalLinks | internal-links | 用 Cursor / OpenClaw 帮你优化内链 | Use Cursor / OpenClaw to optimize internal links |
| LinkBuilding | link-building | 用 Cursor / OpenClaw 帮你规划外链建设 | Use Cursor / OpenClaw to plan link building |
| MetaTagGuide | meta-description, title-tag | 用 Cursor / OpenClaw 帮你优化 title 与 meta | Use Cursor / OpenClaw to optimize title & meta |
| NavigationMenu | navigation-menu-generator | 用 Cursor / OpenClaw 帮你设计导航菜单 | Use Cursor / OpenClaw to design navigation menu |
| WebsiteStructure | website-structure | 用 Cursor / OpenClaw 帮你规划网站结构 | Use Cursor / OpenClaw to plan website structure |
| WebsiteIndexing | indexing | 用 Cursor / OpenClaw 帮你解决索引问题 | Use Cursor / OpenClaw to fix indexing issues |
| Crawler | site-crawlability | 用 Cursor / OpenClaw 帮你优化抓取 | Use Cursor / OpenClaw to optimize crawlability |
| SERP | serp-features | 用 Cursor / OpenClaw 帮你优化 SERP 特性 | Use Cursor / OpenClaw to optimize for SERP features |
| CreateBlog | blog-page-generator | 用 Cursor / OpenClaw 帮你设计博客结构 | Use Cursor / OpenClaw to design blog structure |
| Glossary | glossary-page-generator | 用 Cursor / OpenClaw 帮你创建术语表页 | Use Cursor / OpenClaw to create glossary page |
| LearnSEO | seo-strategy | 用 Cursor / OpenClaw 帮你规划 SEO | Use Cursor / OpenClaw to plan SEO strategy |
| SeoChecklist | seo-strategy | 用 Cursor / OpenClaw 帮你执行 SEO 清单 | Use Cursor / OpenClaw to run SEO checklist |
| SubdomainVsSubfolder | domain-architecture | 用 Cursor / OpenClaw 帮你决定子域/子目录 | Use Cursor / OpenClaw to decide subdomain vs subfolder |
| URLOptimization | url-structure | 用 Cursor / OpenClaw 帮你优化 URL 结构 | Use Cursor / OpenClaw to optimize URL structure |
| WebsiteTraffic | traffic-analysis | 用 Cursor / OpenClaw 帮你分析流量 | Use Cursor / OpenClaw to analyze traffic |
| DarkTraffic | traffic-analysis | 用 Cursor / OpenClaw 帮你分析暗流量 | Use Cursor / OpenClaw to analyze dark traffic |
| ExampleArticle | article-page-generator | 用 Cursor / OpenClaw 帮你优化文章页 | Use Cursor / OpenClaw to optimize article pages |
| NewDomainsTLD | domain-selection | 用 Cursor / OpenClaw 帮你选 TLD | Use Cursor / OpenClaw to choose TLD |
| WebsiteRendering | rendering-strategies | 用 Cursor / OpenClaw 帮你选渲染策略 | Use Cursor / OpenClaw to choose rendering strategy |
| RedirectChain | canonical-tag | 用 Cursor / OpenClaw 帮你配置 canonical 与 URL 规范化 | Use Cursor / OpenClaw to configure canonical and URL consolidation |
| HowSearchEnginesWork | site-crawlability, indexing | 用 Cursor / OpenClaw 帮你优化抓取与解决索引问题 | Use Cursor / OpenClaw to optimize crawlability and fix indexing issues |
| SubmitWebsite | indexing, google-search-console | 用 Cursor / OpenClaw 帮你解决索引问题与 GSC 分析 | Use Cursor / OpenClaw to fix indexing issues and analyze GSC |
| ExternalLinks | eeat-signals | 用 Cursor / OpenClaw 帮你优化 E-E-A-T 与引用策略 | Use Cursor / OpenClaw to optimize E-E-A-T and citation strategy |
| GoogleTagManagerGuide | analytics-tracking | 用 Cursor / OpenClaw 帮你配置 GA4 与事件跟踪 | Use Cursor / OpenClaw to set up GA4 and event tracking |
| BrandedQueriesFilter | google-search-console | 用 Cursor / OpenClaw 帮你分析 GSC 数据 | Use Cursor / OpenClaw to analyze GSC data |
| HTMLATag | internal-links | 用 Cursor / OpenClaw 帮你优化内链与锚文本 | Use Cursor / OpenClaw to optimize internal links and anchor text |
| HTMLTagGuide | schema-markup | 用 Cursor / OpenClaw 帮你添加结构化数据 | Use Cursor / OpenClaw to add structured data |
| **Insights** | | | |
| DirectorySubmissionSites | directory-submission | 用 Cursor / OpenClaw 帮你准备目录提交 | Use Cursor / OpenClaw to prepare directory submission |
| IndieHackers | indie-hacker-strategy | 用 Cursor / OpenClaw 帮你规划独立开发 | Use Cursor / OpenClaw to plan indie hacker strategy |
| ReasonsYouNeedSEO | seo-strategy | 用 Cursor / OpenClaw 帮你规划 SEO | Use Cursor / OpenClaw to plan SEO strategy |
| AILogoDesign | logo-generator | 用 Cursor / OpenClaw 帮你优化 Logo 放置与品牌识别 | Use Cursor / OpenClaw to optimize logo placement and brand recall |
| **Tools** | | | |
| AffiliateMarketingTools | affiliate-marketing, affiliate-page-generator | 用 Cursor / OpenClaw 帮你规划联盟计划 | Use Cursor / OpenClaw to plan affiliate program |
| ReferralProgramTools | referral-program | 用 Cursor / OpenClaw 帮你设计推荐计划 | Use Cursor / OpenClaw to design referral program |
| InfluencerMarketingTools | influencer-marketing | 用 Cursor / OpenClaw 帮你规划红人合作 | Use Cursor / OpenClaw to plan influencer partnerships |
| DirectoryTools | directory-submission | 用 Cursor / OpenClaw 帮你准备目录提交 | Use Cursor / OpenClaw to prepare directory submission |
| **Events** | | | |
| LandingPageEN | landing-page-generator | - | Use Cursor / OpenClaw to write your landing page |
| FounderPark20241106 / EN | seo-strategy | 用 Cursor / OpenClaw 帮你规划 SEO | Use Cursor / OpenClaw to plan SEO strategy |
| Praxis20250927 / EN | generative-engine-optimization | 用 Cursor / OpenClaw 帮你优化 AI 搜索可见性 | Use Cursor / OpenClaw to optimize for AI search visibility |
| LinkLoudEventDetail / LinkLoud20250223EN | growth-funnel | 用 Cursor / OpenClaw 帮你规划增长漏斗 | Use Cursor / OpenClaw to plan growth funnel |
| LinkLoud20260124 / EN | growth-funnel | 用 Cursor / OpenClaw 帮你规划增长漏斗 | Use Cursor / OpenClaw to plan growth funnel |

### 3.3 不加的页面

- **无 TLDR**：部分 legacy、其他 events 详情
- **无匹配 skill**：Google、OpenAI、GenerativeAILandscape、BestTools、SearchEngine
- **Tools 产品列表**：ImageGeneratorTools、CodingTools 等（无直接策略 skill）
