# Articuler — Technical 审计任务

## 文档信息

| 项 | 内容 |
|----|------|
| **站点** | [https://www.articuler.ai/](https://www.articuler.ai/) |
| **定位** | Technical 防线：**结论摘要 + 优先任务**；细则、KPI、外链、GEO 等 → **后续独立文档** |
| **外部报告** | `articuler_seo_audit_report(1).docx`（2026-03，内部） |
| **更新** | 2026-03-26 |

**目录**：[1. 基线与结论](#1-基线与结论) · [2. 技术结论](#2-技术结论) · [3. 优先任务](#3-优先任务) · [附录](#附录)

---

## 1. 基线与结论

### 1.1 快照（报告口径）

| 项 | 内容 |
|----|------|
| 综合 SEO 评分 | **28 / 100** |
| Google 收录 | 约 **1** 条（`site:articuler.ai`） |
| 主因判断 | **多因素叠加**（新站、首包可索引内容不足、sitemap/GSC、外链与声量等），非单点原因 |

### 1.2 Technical 相关结论

| 主题 | 要点 |
|------|------|
| **渲染** | 报告为 CSR/SPA；源码见 **§2**（Next **CSR bailout**、首包多 loading）。与「首包缺正文 DOM」一致。 |
| **爬虫** | Googlebot 可跑 JS，新站仍易慢收录；**Bing 等对 JS 页更弱**。 |
| **主轴** | 营销/内容 URL：**SSG/SSR/预渲染** + **sitemap、GSC**；已在 Next 上，重在**静态或服务端输出**与**消除 bailout**。 |
| **其他** | 核心词弱、Resources 薄、**关键落地页缺失**（如 **Pricing** 等）、**Articul8** 易混淆 → 见任务 **T8–T10**。 |

---

## 2. 技术结论

### 2.1 CSR / 首包 HTML

**结论**：主内容链路为 **CSR bailout**（`BAILOUT_TO_CLIENT_SIDE_RENDERING`），**非**整页服务端 HTML 直出。

| 观察 | 说明 |
|------|------|
| Next 标记 | `BAILOUT_TO_CLIENT_SIDE_RENDERING`，主 UI **退回客户端渲染** |
| `<body>` 首包 | 多为 **全屏 loading**，非完整营销 DOM |
| 正文 | Hero、标题、Resources 等在 **React Flight** 中，需 **JS / hydration** |
| `<head>` | 已有 `title`、`description` 等；**正文 SEO 仍依赖渲染完成** |

**归纳**：可索引路由（首页、定价、**/resources** 等）应在构建/服务端产出 **含 H1 与正文** 的 HTML，或消除 bailout；**Dashboard** 等可保持 CSR。

### 2.2 On-page 与标记（另三类问题）

与 CSR **并列**处理；改版或补全 head 时一并落地。

| 问题 | 现象 / 影响 | 处理方向 |
|------|-------------|----------|
| **Heading** | **首页多个 `<h1>`**，削弱主题与大纲 | **每 URL 仅 1 个 H1**，其余 **H2 → H3**，不跳级 |
| **Canonical** | **`rel="canonical"` 缺失**（或模板漏加） | 可索引页统一 **绝对 URL canonical**，与 301、内链一致 |
| **Schema** | **JSON-LD 未部署** | **Organization**、**SoftwareApplication**、文章 **Article** 等；与可见内容一致，Rich Results Test 校验 |

### 2.3 站点结构：关键落地页缺失

当前站点 **缺少大量 SaaS / 增长常见独立页**（或未成可索引 URL / 未进主导航），导致 **商业与转化意图词无着陆页**、**内链与 sitemap 可覆盖面过少**。

| 类型 | 示例（按需取舍） | 说明 |
|------|------------------|------|
| **商业与转化** | **`/pricing`**（定价/计划）、**`/contact`** 或 **`/support`** | 承接「价格、套餐、联系」类搜索与广告落地 |
| **信任与合规** | **`/about`**、**`/security`**、**`/privacy`**（若仅站外静态页，需统一 canonical/内链策略） | E-E-A-T、B2B 决策路径 |
| **产品深度** | **`/features`**、集成/FAQ、**`/changelog`** | 功能词、长尾与更新信号 |
| **内容** | **`/resources`** 已部分存在 | 持续扩充；与 Blog/指南协同 |

**处理方向**：为上述类型建立 **独立、可索引 URL**（SSG/SSR 优先），配齐 **title/meta、H1、canonical、Schema**；写入 **主导航/页脚**、**内链** 与 **sitemap**。具体 IA 与优先级 → 后续 **站点结构** 文档。

---

## 3. 优先任务

| 编号 | 任务 | 优先级 | 说明 |
|------|------|--------|------|
| T1 | Title / Meta description | P0 | 替换泛化文案，嵌入目标词与差异化 |
| T2 | GSC + sitemap + robots | P0 | 验证属性、提交 sitemap、robots 不误拦 |
| T3 | SSG / SSR / ISR，消除 bailout | P0 | 需收录页静态或服务端渲染；排查触发 bailout 的边界 |
| T4 | 首屏 HTML 可读内容 | P0 | 弱 JS 下可见 **H1 + 关键段落**，避免仅 spinner |
| T5 | Canonical（待补全） | P0 | 全站 **`rel="canonical"`**；www/apex、内容页、`static` 子域关系 |
| T6 | Schema.org（待补全） | P1 | 全站 Organization + SoftwareApplication；文章 **Article/BlogPosting** |
| T7 | Heading 层级（多 H1） | P1 | 单 H1 + H2/H3；见 **§2.2** |
| T8 | /resources 与内容资产 | P1 | 可索引长尾与 GEO 基础；选题见后续内容文档 |
| T9 | 品牌区隔（Articul8） | P1 | 官网/商店/社媒表述一致 |
| T10 | **关键落地页补齐**（**Pricing**、About、Contact、Security 等） | P1 | 独立 URL、可索引、进导航/页脚/内链与 sitemap；见 **§2.3** |

**完成进度**：0 / 10

---

## 附录

### A. 后续独立文档（建议范围）

| 方向 | 建议包含 |
|------|----------|
| Technical 深度 | 抓取日志、robots/sitemap 原文、重定向、CWV |
| 内容与关键词 | 词表、栏目、对比页 |
| 站点结构（IA） | 必备 URL 清单（Pricing 等）、导航与内链图 |
| 外链与 PR | 媒体、Pitch、Harvard 等资产复用 |
| GEO | AI 可见度、listing、可引用源 |

### B. 优先级说明

| 优先级 | 含义 |
|--------|------|
| **P0** | 立即推进，直接影响索引与抓取 |
| **P1** | 高优先级，紧接 P0 |

### C. 已完成

| 编号 | 任务 | 完成日 | 备注 |
|------|------|--------|------|
| — | 暂无 | — | — |

---

*外部报告中的 DA 等为预估值，仅供参考。*
