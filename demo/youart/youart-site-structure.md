# YouArt 网站结构与 URL 架构

> **本文职责**：页面优先级、URL 结构、导航层级、分阶段上线计划、关键词/场景/增长映射。产品概览、关键词、竞品详见各自子文档。面向海外市场，URL 为英文路径、国际 SEO 策略。
> 关联文档：[youart.md](./youart.md) | [youart-features.md](./youart-features.md) | [youart-keywords.md](./youart-keywords.md) | [youart-competitors.md](./youart-competitors.md) | [youart-use-cases.md](./youart-use-cases.md) | [youart-growth-strategy.md](./youart-growth-strategy.md) | [README.md](./README.md)

---

## 1. 当前网站结构（基于网站分析）

| 路径/区块 | 描述 | 类型 | SEO 状态 |
|-----------|------|------|---------|
| / | 首页（着陆页）— 单页滚动/多区块，含价值主张、YOUART ORIGINALS、Monetize 介绍、客户 Logo 墙 | 多区块页面 | 可索引性待验证 |
| /seedance-2-0 | Seedance 2.0 专题页 — 功能展示、技术规格、适用人群、FAQ、定价引导 | 独立页 | 可索引性待验证 |
| /pricing | 定价页 — 完整定价层级、功能对比 | 独立页 | 可索引性待验证 |
| /terms-of-service | 服务条款 | 法律页 | 低优先级 |
| /privacy-policy | 隐私政策 | 法律页 | 低优先级 |

**当前状态**：YouArt 网站为多区块/多页结构，但有明显的 SEO 优化空间。核心问题：
1. **缺少独立功能页**：功能信息分散在首页和 Seedance 页中，没有专门的 /features 页承接功能搜索词
2. **变现故事未被搜索引擎捕获**：YouArt 最核心的差异化（Patreon for AI）缺少独立的 SEO 着陆页
3. **缺少创作者社区/案例页**：社会证明内容（客户 Logo 墙）在首页，但没有创作者成功案例页
4. **缺少竞品对比页**：Sora 关停带来的大量"alternative"搜索流量未被捕获
5. **无 Blog 基础设施**：长尾信息词无承接载体

---

## 2. 推荐 URL 结构（多页架构）

### 2.1 核心路径表

| 路径 | 页面 | 目标关键词 | 优先级 | 阶段 |
|------|------|-----------|--------|------|
| / | 首页（保留核心内容 + hero） | YouArt、AI video generator、Patreon for AI creators | P0 | 已完成 |
| /seedance-2-0 | Seedance 2.0 专题页（已有） | Seedance 2.0、multimodal video generation、lip sync AI video | P0 | 已完成 |
| /pricing | 定价页（已有） | Seedance 2.0 pricing、AI video generator pricing | P0 | 已完成 |
| /features | 功能总览页（新建） | text to video AI、AI video with audio、all in one AI creative studio | P0 | 第一阶段 |
| /monetize | 创作者变现页（新建） | monetize AI content、AI creator monetization、crowdfund AI film | P0 | 第一阶段 |
| /creators | 创作者社区/案例页（新建） | AI creator community、AI film maker showcase | P1 | 第二阶段 |
| /compare | 竞品对比页（新建） | Runway alternative、Sora replacement、Kling AI alternative | P0 | 第一阶段 |
| /templates | 模板库（如可搜索） | AI video templates、product video template | P2 | 第三阶段 |
| /blog | Blog 索引（新建） | — | P1 | 第二阶段 |
| /blog/{slug} | Blog 文章 | 各类长尾关键词 | P1 | 第二阶段 |
| /about | 关于/团队页 | YouArt AI company、Formative Intelligence | P2 | 第三阶段 |
| /affiliate | 联盟计划 | YouArt affiliate program | P2 | 第三阶段 |

### 2.2 URL 设计原则

- 英文路径，短且干净（现有页面已遵循此原则）
- 全小写，使用连字符（如 `/seedance-2-0`）
- 无技术栈后缀（无 `.html`、`.php`）
- 功能页最多两级深
- Blog 使用 `/blog/{slug}` 模式
- 法律页放置在 `/terms-of-service`、`/privacy-policy`（已实现）

### 2.3 国际化策略

当前网站仅英文。如未来需要多语言（考虑到创始人的中国背景和亚洲市场机会），建议子目录方案：

```text
youart.ai/              → 英文（默认）
youart.ai/zh/           → 简体中文
youart.ai/ja/           → 日文（动画/AI 创作市场大）
youart.ai/es/           → 西班牙语（拉美电商市场）
```

设置 hreflang 标签和 x-default 指向英文，确保多语言内容的搜索引擎正确处理。

---

## 3. 导航架构

### 3.1 推荐主导航（Header）

```text
Home    |   Features    |   Seedance 2.0    |   Pricing    |   Monetize    |   Blog
/       /features       /seedance-2-0       /pricing       /monetize       /blog
```

### 3.2 推荐底部导航（Footer）

```text
产品：Features | Seedance 2.0 | Templates | Pricing
创作者：Monetize | Creator Community | Affiliate Program | Success Stories
资源：Blog | Help Center | API Status
公司：About | Team | Contact
法律：Privacy Policy | Terms of Service
```

### 3.3 面包屑导航

```text
Home > Seedance 2.0 > Technical Specifications
Home > Monetize > How Crowdfunding Works
Home > Blog > {文章标题}
```

---

## 4. 分阶段上线计划

### 第一阶段 — 立即（建立 SEO 基础）

| 页面 | 理由 |
|------|------|
| /features | 承接所有"AI video generator""AI video maker"等核心功能搜索词 |
| /monetize | 承接 YouArt 最独特的差异化搜索词——"Patreon for AI"、"monetize AI content" |
| /compare | 紧急：捕获 Sora 关停后的"alternative""replacement"搜索流量 |

**第一阶段目标**：把 YouArt 的三大核心价值（创作工具、多模型、变现）分别建立独立 SEO 着陆页。

### 第二阶段 — 1 个月

| 页面 | 理由 |
|------|------|
| /creators | 社会证明——展示创作者的 AI 原创作品和成功案例 |
| /blog | 内容营销基础设施——覆盖长尾教程、评测、趋势关键词 |
| /templates | 产品内已有模板系统，建立可搜索的公开模板库增加自然流量 |

**第二阶段目标**：建立内容引擎和社会证明页面，开始覆盖长尾关键词。

### 第三阶段 — 3 个月

| 页面 | 理由 |
|------|------|
| /about | 品牌信任页——YC 背书、创始人故事 |
| /affiliate | 联盟计划独立页——发展 KOL 推广网络 |
| /blog/* 深化 | 教程系列、创作者访谈、模型评测等深度内容 |
| 多语言 | 如日文市场有需求，优先建 `/ja/` |

**第三阶段目标**：完成品牌建设和国际化基础。

---

## 5. 技术 SEO 建议

| 项目 | 建议 |
|------|------|
| 渲染 | 当前为客户端渲染（CSR）Web 应用，需确认搜索引擎可完整抓取内容。如有必要，采用 SSR/SSG（Next.js 或 Nuxt） |
| 页面标题 | 每页独立标题，格式：`{页面主题} — YouArt AI Creative Studio` |
| Meta Description | 每页独立，150-160 字符，包含核心关键词 |
| Canonical | 每页自指 canonical |
| hreflang | 目前仅英文，暂不需要；未来多语言时设置 |
| Schema | 首页：Organization schema；Seedance 页：SoftwareApplication schema；定价页：Product schema；Blog：Article schema |
| Sitemap | 生成 XML sitemap，提交 Google Search Console 和 Bing Webmaster Tools |
| 性能 | 优化 LCP（视频 Demo 可能影响加载速度）；目标 LCP < 2.5s |
| 内链 | 首页 → Seedance → Features → Monetize → Pricing 形成自然内链流 |
| Open Graph | 所有页面的 OG 标签完整配置——对于创作者平台，社交分享预览至关重要 |
| 结构化数据 | /creators 页使用 ProfilePage/Person schema 标记创作者信息 |

---

## 6. 关键词/场景/增长映射

| 页面 | 关键词 | 场景 | 增长阶段 |
|------|--------|------|---------|
| / | 品牌 + 核心功能 | 所有人物第一接触 | 获客 |
| /seedance-2-0 | Seedance 2.0 + 技术词 | Marcus、Yuki（技术选型） | 获客 + 激活 |
| /pricing | 定价 + 模型访问 | Carlos、Sofia（预算评估） | 转化 |
| /features | 功能总览 + AI video 核心词 | 所有人物（功能评估） | 获客 + 转化 |
| /monetize | 变现关键词 | Marcus（变现需求） | 获客 + 转化 |
| /compare | 竞品截流词 | Sora 迁移用户 | 获客 |
| /creators | 社区 + 案例 | Yuki（社区归属感） | 激活 + 留存 |
| /blog | 长尾信息 + 教程 | 所有人物（内容吸引） | 获客 + 留存 |
| /templates | 模板词 | Sofia、Carlos（效率需求） | 激活 |

---

*文档创建：2026-06-27 | 模式：Mode A 冷启动 — 国际版 | URL 架构为基于网站结构分析的建议 | 来源：[youart.ai](https://youart.ai/) 网站结构分析*
