# ARTIFIN 网站结构与 URL 架构

> **本文职责**：页面优先级、URL 结构、导航层级、分阶段上线计划、关键词/场景/增长映射。产品概览、关键词、竞品详见各自子文档。面向海外市场，URL 为英文路径、国际 SEO 策略。
> 关联文档：[artifin.md](./artifin.md) | [artifin-features.md](./artifin-features.md) | [artifin-keywords.md](./artifin-keywords.md) | [artifin-competitors.md](./artifin-competitors.md) | [artifin-use-cases.md](./artifin-use-cases.md) | [artifin-growth-strategy.md](./artifin-growth-strategy.md) | [artifin-brand-visual.md](./artifin-brand-visual.md) | [README.md](./README.md)

---

## 1. 当前网站结构（基于网站分析）

| 路径/区块 | 描述 | 类型 | SEO 状态 |
|-----------|------|------|---------|
| / | 首页（着陆页）— 单页滚动，含价值主张、功能、竞品对比、圆桌 Demo | 单页 | 可索引性待验证 |
| /logo/ | Logo 资源目录（arti-circle-dark.svg、arti-squircle-dark.svg） | 静态资源 | 不适用 |
| /avatars/circle/ | 大师和分析师头像资源目录 | 静态资源 | 不适用 |

**当前状态**：ARTIFIN 网站为单页应用（SPA）。所有内容集中在一个页面上，通过滚动和交互展示。这对 SEO 不利 — 所有关键词竞争同一个页面，无法对不同搜索意图做独立页面优化。对国际扩张来说，这是关键问题。

---

## 2. 推荐 URL 结构（多页架构）

### 2.1 核心路径表

| 路径 | 页面 | 目标关键词 | 优先级 | 阶段 |
|------|------|-----------|--------|------|
| / | 首页（保留核心 SPA 内容） | ARTIFIN、AI investment roundtable、AI investment analysis | P0 | 第一阶段 |
| /demo | 圆桌 Demo（独立页） | AI investment analysis demo、NVDA analysis | P0 | 第一阶段 |
| /features | 功能概览 | dual-layer AI engine、red-blue adversarial、licensed AI advisor | P0 | 第一阶段 |
| /masters | 七位大师 | AI investment masters、Buffett AI、Peter Lynch AI | P1 | 第二阶段 |
| /analysts | 七位分析师 | AI investment analysts、quant analysis team | P1 | 第二阶段 |
| /markets | 市场覆盖 | US stock AI analysis、HK stock AI analysis、Japan ETF AI | P1 | 第二阶段 |
| /risk | 风控与合规 | AI risk management、licensed AI financial advisor、SFC license | P1 | 第二阶段 |
| /assets | 独家资产通道 | Japan ETF、RWA investment | P2 | 第三阶段 |
| /compare | 竞品对比 | QarvioFin alternative、Bloomberg terminal alternative | P2 | 第三阶段 |
| /pricing | 定价（上线后） | AI investment tool pricing、robo-advisor cost | P2 | 第三阶段 |
| /blog | Blog 索引 | — | P1 | 第二阶段 |
| /blog/{slug} | Blog 文章 | 各类长尾关键词 | P1 | 第二阶段 |
| /about | 关于我们 | ARTIFIN team、AI investment roundtable background | P2 | 第三阶段 |
| /hk | 香港/亚太区域页 | HK stock AI analysis、SFC licensed AI advisor | P1 | 第二阶段 |

### 2.2 URL 设计原则

- 英文路径，短且干净
- 全文使用 kebab-case（如 `/site-structure`）
- 无技术栈后缀（无 `.html`、`.php`）
- 功能页最多两级深
- Blog 使用 `/blog/{slug}` 模式
- 区域页按需使用顶级国家/地区代码：`/hk`、`/sg`、`/jp`

### 2.3 国际化策略

面向全球扩张，考虑子目录 i18n 方案：

```
artifin.ai/              → 英文（默认，全球通用）
artifin.ai/zh/           → 简体中文
artifin.ai/hk/           → 繁体中文 / 香港市场特供
artifin.ai/ja/           → 日文（如需日本市场推广）
```

设置 `hreflang` 标签和 `x-default` 指向英文。每种语言获得独立 SEO 定位，同时共享同一产品基础设施。

---

## 3. 导航架构

### 3.1 主导航（Header）

```
Home  |  Features  |  Demo  |  Masters  |  Markets  |  Blog
/     /features    /demo   /masters    /markets   /blog
```

### 3.2 底部导航（Footer）

```
产品：Features | Roundtable Demo | Masters | Analysts | Market Coverage | Asset Channels
资源：Blog | Help Center | API（如有）
公司：About | Risk & Compliance | Contact
法律：Privacy Policy | Terms of Service | Risk Disclosure
```

### 3.3 面包屑导航

```
Home > Features > Dual-Layer AI Engine
Home > Masters > Warren Buffett
Home > Blog > {文章标题}
```

---

## 4. 分阶段上线计划

### 第一阶段 — 立即（MVP 多页化）

| 页面 | 理由 |
|------|------|
| / | 首页 — 现有内容，确保可索引 |
| /demo | 核心转化页 — 潜在客户体验的第一触点 |
| /features | 功能声索着陆页 — 核心功能关键词 SEO |

**第一阶段目标**：让搜索引擎在独立页面上索引 3 种不同意图（品牌/功能/体验）。

### 第二阶段 — 1 个月

| 页面 | 理由 |
|------|------|
| /masters | 投资大师 IP 是首要获客钩子；每位大师设置锚点（#buffett、#lynch 等） |
| /analysts | 专业信任建设 — 展示 L1 分析师团队的方法论深度 |
| /markets | 市场覆盖信息页 — 捕获"US stock AI analysis""HK stock AI analysis"搜索 |
| /risk | 合规信任页 — SFC 牌照信息、风控流程概述 |
| /hk | 亚太区域着陆页 |
| /blog | 内容营销基础设施 |

**第二阶段目标**：完成覆盖所有 P0-P1 关键词页面目标的信息架构。

### 第三阶段 — 3 个月

| 页面 | 理由 |
|------|------|
| /compare | 竞品截流页 — 客观差异罗列，非攻击 |
| /pricing | 如定价已建立，创建透明定价页 |
| /assets | 独家资产通道详情 |
| /about | 品牌信任页 |

**第三阶段目标**：长尾覆盖 + 转化优化。

---

## 5. 技术 SEO 建议

| 项目 | 建议 |
|------|------|
| 渲染 | 如保留 SPA 体验，采用 SSR/SSG（Next.js 或 Nuxt）；确保搜索引擎可抓取完整内容 |
| 页面标题 | 每页独立标题，格式：`{页面主题} — ARTIFIN AI Investment Roundtable` |
| Meta Description | 每页独立，150-160 字符，包含核心关键词 |
| Canonical | 每页自指 canonical |
| hreflang | 如多语言，设置 en、zh、ja、x-default 的 hreflang 标签 |
| Schema | 首页：Organization schema；功能页：WebApplication schema；大师页：Person schema（每位大师）；Blog：Article schema |
| Sitemap | 生成 XML sitemap，提交 Google Search Console 和 Bing Webmaster Tools |
| 性能 | 头像图片（avatars/circle/）使用 WebP + CDN；目标 LCP < 2.5s |
| 内链 | 清晰的内链结构（Features → Masters、Demo → Features 等） |
| Core Web Vitals | 针对交互式 Demo 优化 INP、CLS |

---

## 6. 关键词/场景/增长映射

| 页面 | 关键词 | 场景 | 增长阶段 |
|------|--------|------|---------|
| / | 品牌 + 核心功能 | 所有人物的第一接触 | 获客 |
| /demo | 股票代码定向 | Sarah（体验驱动） | 激活 |
| /features | 差异化定位 | David（功能评估） | 转化 |
| /masters | 投资大师 IP | Sarah（好奇心驱动） | 获客 |
| /markets | 市场覆盖 | David、Michael（覆盖验证） | 转化 |
| /blog | 长尾信息 | 所有人物（内容吸引） | 获客 + 留存 |
| /risk | 合规信任 | Michael（合规验证） | 转化 |
| /compare | 竞品截流 | David（对比决策） | 转化 |
| /hk | 亚太区域 | Michael、亚太投资者 | 获客 |

---

*文档创建：2026-05-14 | 最后更新：2026-05-14（第二轮精炼） | 模式：Mode A 冷启动 — 国际版 → Mode C 增量精炼 | URL 架构为基于 SPA 结构分析的建议 | 来源：[artifin.ai](https://www.artifin.ai/) 网站结构分析*
