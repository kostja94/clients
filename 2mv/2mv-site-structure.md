# 2mv — 站点结构

> 网站结构规划文档。URL、IA 与页面构建方案。

---

## 1. 核心路径表

### 1.1 基础层

| 路径 | 页面类型 |
|------|---------|
| `/` | 首页（Landing）：五引擎 agency 定位、对比矩阵、病毒案例、Book a demo CTA |
| `/studio` | Studio 产品页（SaaS）：5 大视图、定价、FAQ、证言、niche 列表 |
| `/service` | 代运营服务落地页 |
| `/book-a-demo` | 预约演示表单 |
| `/blog` | 博客列表页 |
| `/blog/{slug}` | 博文详情页（见 §5） |
| `/privacy-policy` | 隐私政策 |
| `/terms-of-use` | 服务条款 |

**路径迁移**（旧 → 新）：

| 旧路径 | 新路径 |
|--------|--------|
| `/research` | `/studio` |
| `/insights` | `/blog` |

### 1.2 核心产品（Feature，根域名一级路径）

| 路径 | Feature | 对应能力 |
|------|---------|---------|
| `/content-discovery` | Content Discovery | Market Signals / Watch |
| `/tracking-center` | Tracking Center | Target Tracking |
| `/profile-analysis` | Profile Analysis | 账号/频道维度分析 |
| `/ai-video-analyzer` | Viral Video Analysis | Viral Breakdown / Content Patterns |

> 4 个 Feature 能力内嵌于 `/studio`；独立根域名路径为 SEO 拆分规划。

**下级页规则**：

| 核心产品 | 下级页类型 | 路径 |
|---------|---------|------|
| `/ai-video-analyzer` | **平台页**（仅此产品） | `/ai-video-analyzer/instagram-reels`、`/tiktok`、`/youtube-shorts` |
| `/content-discovery` | 任务长尾页 | `/content-discovery/youtube-niche-finder` |
| `/tracking-center` | 任务长尾页 | `/tracking-center/tiktok-account-tracker` |
| `/profile-analysis` | 任务长尾页 | `/profile-analysis/youtube-channel-analyzer`、`/instagram-account-analyzer` |

> 已移除 `/ai-video-analyzer/tiktok-video-analyzer`——与 `/ai-video-analyzer/tiktok` 意图重复，统一用平台页承接。

### 1.3 Tools（§6）

| 路径 | 工具 |
|------|------|
| `/tools` | Tools Hub 列表页 |
| `/tools/hook-analyzer` | Hook Analyzer |
| `/tools/hashtag-generator` | Hashtag Generator |
| `/tools/video-idea-generator` | Video Idea Generator |

### 1.4 Library & Reports（§7）

| 路径 | 页面类型 |
|------|---------|
| `/library` | Library 聚合页 |
| `/library/{slug}` | Library 详情页 |
| `/reports` | Reports 聚合页 |
| `/reports/{slug}` | Reports 详情页 |

### 1.5 其他

| 路径 | 页面类型 |
|------|---------|
| `/pricing` | 独立定价页（当前定价内嵌于 `/studio`） |

---

## 2. URL 层级（IA 树）

```
2mv.ai
├── 服务层          /  ·  /service  ·  /book-a-demo
├── 产品层          /studio  ·  /{product-slug}/
├── 工具层          /tools/*
├── 内容层          /blog/*  ·  /library/*  ·  /reports/*
├── 扩展层          /pricing
└── 法务层          /privacy-policy  ·  /terms-of-use
```

**完整 URL 树**：

```
/
├── studio/
├── content-discovery/
│   └── youtube-niche-finder/
├── tracking-center/
│   └── tiktok-account-tracker/
├── profile-analysis/
│   ├── youtube-channel-analyzer/
│   └── instagram-account-analyzer/
├── ai-video-analyzer/
│   ├── instagram-reels/
│   ├── tiktok/
│   └── youtube-shorts/
├── tools/
│   ├── hook-analyzer/
│   ├── hashtag-generator/
│   └── video-idea-generator/
├── blog/
│   ├── what-is-2mv
│   ├── best-social-media-marketing-agencies
│   └── introducing-2mv-reports
├── library/
│   └── {slug}/
├── reports/
│   └── {slug}/
├── pricing/
└── service/
```

---

## 3. 页面类型与路径规则

| 层级 | 路径模式 | 适用 | 交互 |
|------|---------|------|------|
| 产品总览 | `/studio` | Studio 入口 | 注册/试用 |
| 核心产品 | `/{product-slug}` | 4 个 Feature | 无，纯营销 |
| 平台页 | `/ai-video-analyzer/{platform}` | **仅** ai-video-analyzer | 无，纯营销 |
| 任务长尾页 | `/{product-slug}/{task-slug}` | 其余 3 个 Feature | 无，纯营销 |
| 工具页 | `/tools/{tool-slug}` | Tools Hub | 有，轻量交互 |
| 博客 | `/blog/{slug}` | Blog | 无 |
| Library | `/library/{slug}` | 案例库 | 无 |
| Reports | `/reports/{slug}` | 研究报告 | 无 |

**平台 slug**（仅用于 `/ai-video-analyzer/`）：`instagram-reels` · `tiktok` · `youtube-shorts`

**平台页 vs 任务长尾页**：

| | 平台页 | 任务长尾页 |
|--|--------|-----------|
| 适用范围 | 仅 `/ai-video-analyzer/` | `/content-discovery`、`/tracking-center`、`/profile-analysis` |
| 路径示例 | `/ai-video-analyzer/tiktok` | `/tracking-center/tiktok-account-tracker` |
| 命名 | 固定三平台 slug | 平台 + 任务组合 slug |
| 何时新建 | 不需要新建，仅 3 个 | 搜索意图独立、且不能用平台页表达时 |

---

## 4. 规划页面清单

| 路径 | 页面类型 |
|------|---------|
| `/content-discovery` | 核心产品 |
| `/content-discovery/youtube-niche-finder` | 任务长尾页 |
| `/tracking-center` | 核心产品 |
| `/tracking-center/tiktok-account-tracker` | 任务长尾页 |
| `/profile-analysis` | 核心产品 |
| `/profile-analysis/youtube-channel-analyzer` | 任务长尾页 |
| `/profile-analysis/instagram-account-analyzer` | 任务长尾页 |
| `/ai-video-analyzer` | 核心产品 |
| `/ai-video-analyzer/instagram-reels` | 平台页 |
| `/ai-video-analyzer/tiktok` | 平台页 |
| `/ai-video-analyzer/youtube-shorts` | 平台页 |
| `/tools` | Tools Hub |
| `/tools/hook-analyzer` | 工具页 |
| `/tools/hashtag-generator` | 工具页 |
| `/tools/video-idea-generator` | 工具页 |
| `/library` | Library 聚合页 |
| `/library/{slug}` | Library 详情页 |
| `/reports` | Reports 聚合页 |
| `/reports/{slug}` | Reports 详情页 |
| `/pricing` | 独立定价页 |
| `/service` | 代运营服务落地页 |

---

## 5. Blog 路径与文章

**路径前缀**：`/blog/`

| slug | 路径 | 类型 |
|------|------|------|
| `what-is-2mv` | `/blog/what-is-2mv` | Research |
| `best-social-media-marketing-agencies` | `/blog/best-social-media-marketing-agencies` | Comparison |
| `introducing-2mv-reports` | `/blog/introducing-2mv-reports` | Product |

**Tag 分类**（每篇 2–4 个 Tag；Tag 归档页 `noindex, follow`）：

| 分类 | Tag |
|------|-----|
| 平台类 | YouTube Shorts、TikTok、Instagram Reels、Cross-Platform |
| 内容与研究类 | Video Ideas、Hooks、Outliers、Content Patterns、Viral Research、Competitor Research、Content Strategy、Content Creation、Organic Growth |
| 行业洞察类 | Expert Opinion、Interview、Podcast、Industry Events、Platform Updates、Creator Economy、AI Content Tools |

> 原创研究报告走 `/reports/*`，不在 `/blog/` 重复建设。

---

## 6. Tools Hub 结构

**Hub 路径**：`/tools`

| 属性 | 说明 |
|------|------|
| 主要作用 | 免费获客入口 |
| 交互 | 页内轻量功能，免注册、免付费 |
| 边界 | 必须真实可用；不与 Feature 营销页混淆 |

| 路径 | 工具 | 阶段 |
|------|------|------|
| `/tools/hook-analyzer` | Hook Analyzer | Analyze |
| `/tools/video-idea-generator` | Video Idea Generator | Create |
| `/tools/hashtag-generator` | Hashtag Generator | Create |

**Hub 四阶段分组**：Discover · Analyze · Create · Track & Optimize

---

## 7. Library & Reports 结构

### 7.1 Library

| 属性 | 说明 |
|------|------|
| 聚合页 | `/library` |
| 详情页 | `/library/{slug}` |
| 主要作用 | 公开的真实研究案例与灵感库 |
| 交互 | 无，纯内容 |

**内容类型**：Hook 库 · Viral Video 库 · Prompts 库

### 7.2 Reports

| 属性 | 说明 |
|------|------|
| 聚合页 | `/reports` |
| 详情页 | `/reports/{slug}` |
| 主要作用 | 原创研究与行业权威内容 |
| 交互 | 无，纯内容 |

**内容类型**：趋势报告 · 行业报告 · 年度/季度报告

---

> 面向海外市场（英文为主）。

> 关联：[主文档](./2mv.md) | [keywords](./2mv-keywords.md) | [features](./2mv-features.md) | [growth-strategy](./2mv-growth-strategy.md) | [competitors](./2mv-competitors.md) | [use-cases](./2mv-use-cases.md) | [blog/](./blog/)

*Last updated: 2026-08-24*
