# Anyway 网站结构与 URL 架构

> **本文职责**：页面优先级、URL 结构、导航层级、分阶段上线计划、关键词/场景/增长映射。产品概览、关键词、竞品详见各自子文档。面向海外市场，URL 为英文路径、国际 SEO 策略。
> 关联文档：[anyway.md](./anyway.md) | [anyway-features.md](./anyway-features.md) | [anyway-keywords.md](./anyway-keywords.md) | [anyway-competitors.md](./anyway-competitors.md) | [anyway-use-cases.md](./anyway-use-cases.md) | [anyway-growth-strategy.md](./anyway-growth-strategy.md) | [anyway-brand-visual.md](./anyway-brand-visual.md) | [README.md](./README.md)

---

## 1. 当前网站结构（基于网站分析）

| 路径/区块 | 描述 | 类型 | SEO 状态 |
|-----------|------|------|---------|
| / | 首页（着陆页）— 单页滚动，含问题陈述、产品介绍、使用场景、FAQ | 单页 | 可索引性待验证 |
| /products | 产品页面链接 | 导航 | 不适用 |
| /superapi | SuperAPI 独立页 | 可能独立子页 | 待确认 |
| /docs | 文档 | 可能存在 | 待确认 |
| /quickstart | 快速开始 | 可能存在 | 待确认 |

**当前状态**：Anyway 网站主要为单页应用（SPA），核心内容集中在下述区块：Manifesto → Problem → What We Do → Products → Use Cases → SuperAPI → FAQ。少量子页（如 SuperAPI、Docs）可能独立存在。

---

## 2. 推荐 URL 结构（多页架构）

### 2.1 核心路径表

| 路径 | 页面 | 目标关键词 | 优先级 | 阶段 |
|------|------|-----------|--------|------|
| / | 首页（保留核心叙事） | Anyway、agent payments、payment network for AI agents | P0 | 第一阶段 |
| /features | 功能概览 | agent-native payments、multi-protocol routing、Secure Sandbox、verifiable agent traces | P0 | 第一阶段 |
| /superapi | SuperAPI 产品页 | SuperAPI、one API for all APIs、API for AI agents | P0 | 第一阶段 |
| /security | 安全与信任 | prompt injection payment protection、secure agent transactions、agent payment sandbox | P0 | 第一阶段 |
| /use-cases | 使用场景 | monetize AI agent、agent-to-agent settlement、autonomous procurement | P1 | 第二阶段 |
| /use-cases/agent-to-agent | Agent-to-Agent 结算详情 | agent-to-agent settlement、agent hiring agent | P1 | 第二阶段 |
| /use-cases/monetize | Agent 货币化详情 | monetize AI agent、agent subscription billing | P1 | 第二阶段 |
| /docs | 开发者文档 | build paying AI agent、X402 integration、ACP integration | P1 | 第二阶段 |
| /docs/quickstart | 快速开始 | integrate agent payments、agent payment SDK | P1 | 第二阶段 |
| /blog | Blog 索引 | — | P1 | 第二阶段 |
| /blog/{slug} | Blog 文章 | 各类长尾关键词 | P1 | 第二阶段 |
| /pricing | 定价 | agent payment pricing、AI agent billing cost | P2 | 第三阶段 |
| /compare | 竞品对比 | Stripe for AI agents、agent payment alternative | P2 | 第三阶段 |
| /about | 关于我们 | Anyway team、financial OS for agents | P2 | 第三阶段 |

### 2.2 URL 设计原则

- 英文路径，短且干净
- 全文使用 kebab-case（如 `/use-cases`、`/agent-to-agent`）
- 无技术栈后缀（无 `.html`、`.php`）
- 功能页最多两级深
- Blog 使用 `/blog/{slug}` 模式
- Docs 使用 `/docs/` 前缀

### 2.3 国际化策略

优先英文全球站，再按需扩展：

```
anyway.sh/              → 英文（默认，全球通用）
anyway.sh/zh/           → 简体中文（如需要）
anyway.sh/ja/           → 日文（如需要）
```

---

## 3. 导航架构

### 3.1 主导航（Header）

```
Home  |  Features  |  Use Cases  |  SuperAPI  |  Docs  |  Pricing
/     /features    /use-cases    /superapi   /docs   /pricing
```

### 3.2 底部导航（Footer）

```
产品：Features | Use Cases | SuperAPI | Security | Pricing
开发者：Docs | Quickstart | API Reference | SDK | Status
资源：Blog | Case Studies | Whitepaper | FAQ
公司：About | Careers | Press | Contact
法律：Trust Center | Privacy Policy | Terms of Service
社交：X / Twitter | LinkedIn | Discord
```

### 3.3 面包屑导航

```
Home > Features > Secure Sandbox
Home > Use Cases > Agent-to-Agent Settlement
Home > Docs > Quickstart
Home > Blog > {文章标题}
```

---

## 4. 分阶段上线计划

### 第一阶段 — 立即（MVP 多页化）

| 页面 | 理由 |
|------|------|
| / | 首页 — 现有单页核心叙事，确保可索引 |
| /features | 核心功能页 — 覆盖 P0 功能关键词 SEO |
| /superapi | SuperAPI 产品页 — 第二大产品的独立 SEO 着陆页 |
| /security | 安全页 — 差异化定位，Prompt Injection 和安全信任是核心竞争力 |

**第一阶段目标**：将 4 个核心意图（品牌/功能/产品/安全）从单页拆分为独立可索引页面。

### 第二阶段 — 1 个月

| 页面 | 理由 |
|------|------|
| /use-cases | 场景总览页 + 子场景详情页 |
| /docs + /docs/quickstart | 开发者文档 — 开发者是核心用户，文档是获客和激活的关键 |
| /blog | 内容营销引擎 — 品类教育、SEO 长尾 |

**第二阶段目标**：覆盖场景关键词和开发者意图，建立内容飞轮。

### 第三阶段 — 3 个月

| 页面 | 理由 |
|------|------|
| /pricing | 定价透明化 — 促进购买决策 |
| /compare | 竞品截流页 — 客观差异罗列 |
| /about | 品牌信任页 |

**第三阶段目标**：转化优化 + 品牌信任建设。

---

## 5. 技术 SEO 建议

| 项目 | 建议 |
|------|------|
| 渲染 | 采用 SSR/SSG（Next.js 或类似），确保搜索引擎可抓取完整内容 |
| 页面标题 | 每页独立标题，格式：`{页面主题} — Anyway` |
| Meta Description | 每页独立，150-160 字符，包含核心关键词 |
| Canonical | 每页自指 canonical |
| Schema | 首页：Organization schema；功能页：WebApplication schema；Docs：TechArticle schema；Blog：Article schema |
| Sitemap | 生成 XML sitemap，提交 Google Search Console 和 Bing Webmaster Tools |
| 性能 | 优化 LCP < 2.5s；动画使用 GPU 加速；图片使用 WebP + CDN |
| 内链 | 首页 → Features → Security → Use Cases → Docs → Blog 形成清晰内链结构 |
| Core Web Vitals | 优化 INP、CLS |

---

## 6. 关键词/场景/增长映射

| 页面 | 关键词 | 场景 | 增长阶段 |
|------|--------|------|---------|
| / | 品牌 + 核心定位 | 所有人的第一接触 | 获客 |
| /features | 功能差异化 | 开发者评估（Aiden、Marcus） | 转化 |
| /superapi | SuperAPI | 开发者（Aiden） | 激活 |
| /security | 安全差异化 | 企业决策者（Marcus） | 转化 |
| /use-cases | 场景教育 | 所有人物（灵感驱动） | 获客 + 转化 |
| /docs | 开发者激活 | Aiden、独立开发者 | 激活 + 留存 |
| /blog | 内容获客 + 品类教育 | 所有人物 | 获客 |
| /compare | 竞品截流 | 评估对比中的潜在用户 | 转化 |
| /pricing | 购买决策 | 漏斗底部 | 转化 |

---

*文档创建：2026-07-09 | 模式：Mode A 冷启动 — 国际版 | URL 架构为基于网站结构分析的建议 | 来源：[anyway.sh](https://anyway.sh/) 网站结构分析*
