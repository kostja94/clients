# Crescendia — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./crescendia.md) | [keywords](./crescendia-keywords.md) | [features](./crescendia-features.md) | [competitors](./crescendia-competitors.md) | [use-cases](./crescendia-use-cases.md) | [growth-strategy](./crescendia-growth-strategy.md)

**Last updated**: 2026-07-21 | 识别方式：robots.txt + sitemap.xml + 首页 withAllLinks + 核心页抓取（[crescendia.ai](https://www.crescendia.ai/)）

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 | 状态 |
|------|---------|-----------|--------|------|
| `/` | 首页（GEO 定位 + 服务 + Mission/Story + FAQ + Partner） | generative engine optimization, GEO agency, AI search visibility | P0 | 已上线 |
| `/company` | 公司/品牌故事（内容与首页 Company 区高度重合） | Deeplumen about, AI growth agency | P1 | 已上线（品牌仍写 Deeplumen） |
| `/report` | SEO & GEO 诊断表单（线索采集） | SEO GEO diagnostic report, AI search readiness | P0 | 已上线 |
| `/workspace` | 与 `/report` 同构的诊断表单 | — | P2 | 已上线（疑似重复入口） |
| `/demo` | Demo 预约页 | Crescendia demo, Deeplumen demo | P0 | 已上线（文案仍写 Deeplumen） |
| `/login` | 登录 | Crescendia login | P1 | ⚠️ 抓取时 HTTP 503 |
| `/about` | 应为 About；实际为 Nuxt 脚手架页 | — | — | ⚠️ 未完成（boilerplate） |

访问日期：2026-07-21。来源：[crescendia.ai](https://www.crescendia.ai/)

---

## 2. URL 层级与信息架构

```
crescendia.ai（Nuxt SSR 单页营销站 + 少数独立路由）
├── /                         # 首页（锚点导航）
│   ├── #products             # AI-Native Marketing Services
│   ├── #services             # GEO 能力 / 技术栈叙事
│   ├── #company              # Mission / Story / Partner / FAQ
│   └── CTA：Get GEO Report / Get in Touch / Log in
├── /company                  # 公司页（Deeplumen 叙事）
├── /report                   # SEO & GEO Diagnostic 表单
├── /workspace                # 同构诊断表单（待验证是否同后端）
├── /demo                     # Demo 预约
├── /login                    # 登录（不稳定）
└── /about                    # ⚠️ Nuxt 模板占位，非正式 About
```

### 首页结构（单页长滚动）

| 区域 | 内容 | CTA |
|------|------|-----|
| Nav | Home / Products / Services / Company / Log in | Log in |
| Hero | Diagnose Digital Potential, Drive Intelligent Growth. / More Than a Tool—Your AI Search Growth Partner. | Get GEO Report |
| 价值支柱 | Be the Answer / Data-Driven Diagnosis / Build Authority & Trust (E-E-A-T) | — |
| 社会证明 | Trusted by Leading Brands；指标位 AI Mentions / AI Search Traffic / User Pay Rate（当前显示 0%+） | — |
| 线索漏斗 | AI Search Readiness Scan™（含 SEO Health assessment） | Get in Touch |
| 叙事 | Traditional search will drop 25% by 2026；ChatGPT 5.7B monthly queries | — |
| Products | AI Visibility Performance Report™ / 90-day AEO Pilot / Ongoing AEO Optimization | Learn More |
| GEO Engine | AI-Search Logic / Proprietary Stack / Performance-Driven Optimization | — |
| Mission & Story | See. Engage. Grow.；正文仍大量出现 **Deeplumen** | — |
| Partner | Affiliate：最高 15% recurring commissions | Submit |
| FAQ | GEO 定义、行业、Partner、SEO vs GEO、周期等 | — |
| Footer | © 2026 Crescendia | — |

---

## 3. 技术架构

| 维度 | 观测 | 依据 |
|------|------|------|
| 框架 | **Nuxt 4** + **Vue 3** + **TypeScript** | `/about` 明示 Tech Stack；robots 注释 `nuxt-robots` |
| 渲染 | SSR（Nuxt 默认） | 页面可被直接抓取为 HTML |
| 样式 | CSS3（Grid/Flexbox/animations） | `/about` 声明 |
| robots | `Allow: /`；Disallow `/api/` `/admin/` `/_nuxt/` `/.git/` `/node_modules/` | [robots.txt](https://crescendia.ai/robots.txt) 2026-07-21 |
| Sitemap | **配置错误**：声明 `https://my-nuxt-app.com/sitemap.xml`，sitemap 内 URL 亦为 `my-nuxt-app.com/*` | 待修复（严重 SEO 基建问题） |
| 多语言 | 未见 hreflang / 语言切换；诊断表单可选区域语言 | 待验证 |
| 关联域 | [deeplumen.com](https://www.deeplumen.com/) 为 Agentic Commerce 产品站（Shopify App 等） | 品牌关系见主文档 |

---

## 4. 多语言

| 项 | 状态 |
|----|------|
| 站点语言 | 英文为主 |
| URL 结构 | 无 `/en/` `/zh/` 等语言前缀 |
| 诊断表单市场 | North America / Europe / Southeast Asia / Mainland China（单主市场选择） |
| 本地化深度 | 浅（仅表单市场选项，无本地化内容站） |

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| sitemap.xml | `/` `/about` `/company` `/demo` `/login` `/report` `/workspace` | 7 | 无（且 host 错误） |
| 实际可访问 | 同上，但 host 应为 `crescendia.ai` | 7 | — |
| 博客/资源 | 无 | 0 | — |
| Programmatic | 无 | 0 | — |

> Sitemap 明细极少，无需归档至 others。**P0 修复**：将 sitemap/robots 中的 `my-nuxt-app.com` 全部替换为 `https://www.crescendia.ai/`。

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/` | 锚点导航 + CTA | Products/Services/Company；GEO Report；Login |
| `/` FAQ | 信息型锚点 | 建立 GEO/SEO 概念信任 |
| `/report` `/workspace` | 表单提交 | 诊断线索 |
| `/demo` | Demo 预约 | 销售线索 |
| `/company` | Mission/Story/Partner/FAQ | 品牌信任（文案品牌名未统一） |

**缺失枢纽**：Blog、定价页、独立服务详情页（Products 仅「Learn More」无独立 URL）、Case Study、对比页。

---

## 7. URL 分阶段规划

| 阶段 | 建议新增 | 对标关键词优先级 | 说明 |
|------|---------|-----------------|------|
| 短期（0–3 月） | 修复 sitemap/robots；正式 `/about`；独立服务页 `/services/visibility-report` `/services/aeo-pilot` `/services/ongoing-aeo`；`/pricing` 或套餐说明 | P0 | 承接首页 Products CTA |
| 中期（3–6 月） | `/blog`；`/compare/seo-vs-geo`；`/compare/crescendia-vs-profound`；行业落地页 `/industries/{vertical}` | P0–P1 | 教育型 + 商业型流量 |
| 长期（6–12 月） | Case studies；Partner portal；多语言落地；与 Deeplumen 产品线清晰分流（服务站 vs 产品站） | P1–P2 | 品牌架构清晰化 |

---

## 待验证项

- [ ] `/login` 恢复可用性与登录后产品形态（SaaS 面板 vs 仅客户门户）
- [ ] `/report` 与 `/workspace` 是否同一表单的两入口
- [ ] Products「Learn More」目标 URL 是否尚未发布
- [ ] Crescendia 与 Deeplumen 的法人/产品线关系（姊妹品牌 / 重品牌 / 服务层）
