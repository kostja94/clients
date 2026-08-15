# Oginify 网站结构与 URL

> **站点根**：https://oginify.com  
> **本文档职责**：URL 层级、IA、技术栈、多语言、页面状态。  
> **引用**：[主文档](./oginify.md) 概览 | [keywords](./oginify-keywords.md) 关键词 | [features](./oginify-features.md) 产品 | [growth-strategy](./oginify-growth-strategy.md) 增长

**用途**：描述线上 URL、导航层级与页面状态，供 SEO、内链与文档对齐。**站点改版后请更新本文**。

**信息来源**：oginify.com 页面抽样（2026-05-31）。

---

## 总则

| 项 | 说明 |
|----|------|
| **站点根** | https://oginify.com |
| **主语言** | 英文（`/`），当前唯一线上语言 |
| **中文** | **暂不提供** — `/zh` 及 `/zh/*` 已下线（404）；曾短期上线后撤回，恢复时间待定 |
| **URL 习惯** | kebab-case 路径 |

---

## 树状 IA（概览）

```
oginify.com/
├── /                              ← OG Generator（核心）
├── /above-the-fold                ← 首屏截图转 OG（无配额）
├── /open-graph-validator          ← Validator
├── /twitter-card-generator        ← Twitter/X Card（1200×675）
├── /templates                     ← 6 风格模板库
├── /gallery                       ← OG 图灵感库
├── /websites-without-og-image     ← 缺 OG 站点清单（21 站）
├── /use-cases                     ← 使用场景 Hub（三轴 + B2B）
├── /pricing                       ← 定价
├── /changelog                     ← 产品更新日志
├── /platforms-with-built-in-og    ← 规划中（404）
└── Footer 待建/404
    ├── Amazon Sponsored Display
    └── Responsive Display Ads
```

**导航分组**（线上顶栏）：

| 分组 | 典型路径 |
|------|----------|
| **Product** | `/`、`/twitter-card-generator` |
| **Free tools** | `/open-graph-validator`、`/above-the-fold`、`/templates` |
| **Use Cases** | `/use-cases` |
| **Pricing** | `/pricing` |
| **Resources** | `/gallery`、`/websites-without-og-image`、`/templates`、`/use-cases`、`/changelog` |
| **Open source** | GitHub social-cards-skills、marketing-skills |

---

## 核心 URL 表

| 路径 | 页面 | 状态 | 用途 | 搜索意图 | keywords 章节 |
|------|------|------|------|----------|---------------|
| `/` | OG Generator | 200 | 粘贴 URL → AI 生成 4 张 OG 图 | og image generator, ai og image | §1 Generator |
| `/above-the-fold` | Above the Fold | 200 | 首屏截图 → 1200×630，无 AI | screenshot to og image | §6 Above the Fold |
| `/open-graph-validator` | Validator | 200 | OG 标签校验 + 多平台预览 | og checker, facebook link preview | §2 Validator |
| `/twitter-card-generator` | Twitter Card | 200 | 1200×675 X 专用卡片 | twitter card generator | §7 Twitter Card |
| `/templates` | Templates | 200 | 6 风格模板库 + 可编辑布局 | og image template | §8 Templates |
| `/gallery` | Gallery | 200 | 品牌 OG 图案例（约 100，待核实） | og image examples | §3 Gallery |
| `/websites-without-og-image` | Missing List | 200 | 21 站缺 OG 清单 | sites without og image | §4 Websites Without |
| `/use-cases` | Use Cases Hub | 200 | 三轴场景 + B2B 集成入口 | og image use cases | §9 Use Cases |
| `/pricing` | Pricing | 200 | PAYG $0.99 / Bundle $7.90–$29.00 | oginify pricing | §5 Pricing |
| `/changelog` | Changelog | 200 | 产品版本记录 | oginify changelog | §10 Changelog |
| `/zh` | 中文版 | **404** | 曾上线，**已暂时下线** | — | — |
| `/platforms-with-built-in-og` | Platforms | **404** | 内置 OG 平台清单（规划中；文档源：[platforms-og-and-social-preview.md](./platforms-og-and-social-preview.md)） | vercel og image | §11 Platforms |

---

## 与文档 use-cases/ 的分工

| | 线上 `/use-cases` | 文档 `use-cases/` 文件夹 |
|---|---|---|
| **受众** | 访客、B2B 集成咨询 | 内部策略、SEO 内容规划 |
| **结构** | 三轴（page / website / style）+ CMS/Agency/API | 四维度（page-type / site-type / style / image-size） |
| **深度** | 营销导向，部分标 Soon | 58 种页面 S/A/B/C、16 种网站类型等穷举 |

两者互补：线上页获客，文档文件夹做策略与 pSEO 规划。

---

## 技术栈

| 组件 | 方案 | 说明 |
|------|------|------|
| **前端** | Lovable | [oginify.com](https://oginify.com) 为**绑定自有域名**；应用仍托管于 Lovable（非独立站迁出） |
| **图像生成** | Google Gemini Nano Banana 2 | `gemini-3.1-flash-image-preview` |
| **爬取** | Firecrawl `/v2/scrape` + native fetch fallback | JSON extract 5 credits/次 |
| **LLM 理解** | Gemini 3 Flash Preview | 输入 3–5k tok |
| **截图** | 无头浏览器 + 浏览器端裁切 | Above the Fold |
| **支付** | 接入中 | 提供商待定，价格待上线确认 |
| **开源 Skills** | Satori + resvg | 6 种视觉风格，npm 分发 |

---

## 规划中 / 待处理

| 项 | 状态 | 说明 |
|----|------|------|
| `/platforms-with-built-in-og` | 404，内容待建 | 与 Websites Without 形成正反对照 |
| Footer Amazon Sponsored Display | 404 | 待建落地页或移除链接 |
| Footer Responsive Display Ads | 404 | 待建落地页或移除链接 |
| CMS / API 集成 | 文档与 use-cases 页提及 | WordPress、Webflow 等，商务洽谈 |
| 中文版 `/zh` | **404，已暂时下线** | 曾短期上线；首页 hreflang 已移除；恢复时间待定 |

---

*Last updated: 2026-05-31*
