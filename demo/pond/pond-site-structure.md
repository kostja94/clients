# Pond — 站点结构

> 面向海外市场（英文为主）。本文件为纯事实层：URL、IA、技术栈。功能能力见 [pond-features.md](./pond-features.md)。

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（Landing）：定位、平台数据、任务样例、Agent 案例 | pond, ai task marketplace | P0 |
| `/tasks` | 任务市场（Bounties 列表，Global Contributor Network） | ai task marketplace, earn money with ai | P0 |
| `/tasks/mybounties` | 发布者任务管理（创建 Bounty） | create bounty, post a task | P1 |
| `/discoveries` | Discoveries：创业公司展示 + 排行榜（Top Revenue/MRR/MAU） | build in public, startup discovery | P0 |
| `/markets` | Markets：融资市场（SAFE、token warrant、投资者） | startup fundraising platform, safe agreement | P0 |
| `/points` | Points：每日刷新的积分任务 | pond points | P2 |
| `/portfolio` | 用户投资组合与活动记录 | pond portfolio | P2 |
| `/manage-startups` | 创始人仪表盘（管理 startup listing） | manage startup, list your startup | P1 |
| `docs.joinpond.ai` | 文档子域（Mintlify）：What is Pond / Bounties FAQs / Markets / Discoveries / Referral / 法务 | pond docs, pond bounties faq | P1 |
| `/llms.txt`、`/llms-full.txt` | AI 内容声明页（面向 LLM 检索的官方事实源） | —（GEO 载体） | P1 |

> 站点抓取日期：2026-08-12。任务详情页 URL 为 SPA 动态路由，具体模式 `待验证`。

---

## 2. URL 层级（IA 树）

```
joinpond.ai
├── 公开发现层（无需登录）
│   ├── /                    首页
│   ├── /tasks               任务市场（浏览、筛选 Newest/Hottest、My Applications）
│   ├── /discoveries         创业公司展示 + 排行榜
│   ├── /markets             融资市场 + 投资者名录 + FAQ
│   └── /points              积分任务
├── 用户层（需登录）
│   ├── /tasks/mybounties    我发布的 Bounty
│   ├── /portfolio           我的投资组合
│   └── /manage-startups     我的 Startup（Discoveries 管理）
├── 内容/事实层
│   ├── /llms.txt            LLM 友好摘要
│   ├── /llms-full.txt       扩展事实上下文（产品/受众/推荐关键词）
│   └── docs.joinpond.ai     文档站（docs/**，Markdown 可读）
└── 静态/媒体子域（非导航）
    ├── static.joinpond.ai   静态资源
    ├── img.service.joinpond.ai  图片 CDN
    └── pond-open-files.joinpond.ai  用户上传文件
```

---

## 3. 技术架构

| 维度 | 识别 | 识别方式 |
|------|------|---------|
| 前端框架 | Next.js（SPA，`/_next/static/images/logo_black-ad057b94*.png`） | 页面 HTML 资源路径 2026-08-12 |
| 托管/安全 | Cloudflare（robots.txt 为 Cloudflare Managed 模板；CloudflareBrowserRenderingCrawler 条目） | robots.txt 2026-08-12 |
| 文档站 | Mintlify 风格（"Docs V2"，`/docs/**`，`.md` 后缀可读） | docs.joinpond.ai 2026-08-12 |
| 媒体分发 | 独立图片域 `img.service.joinpond.ai`（webp/q80 处理参数） | markets 页 HTML 2026-08-12 |
| 支付/数据验证 | Stripe API + Google Analytics（Discoveries 数据核验声明） | discoveries 页文案 2026-08-12 |
| AI 内容声明 | `llms.txt` / `llms-full.txt`（Content-Signal: search=yes, ai-train=no, use=reference） | robots.txt + llms.txt 2026-08-12 |

---

## 4. 多语言

- 目前为**英文单语**站点（未发现 hreflang 或多语言路径）。`待验证：是否有计划支持其他语言`。

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| robots.txt 声明 | `sitemap.xml` | 抓取返回 500，无法确认内容 | 待验证 |
| 导航/LLM 声明 | `/`、`/tasks`、`/discoveries`、`/markets`、`/points`、`/portfolio`、`/manage-startups`、`/tasks/mybounties` | ~8 个一级路径（不含动态页） | 2026-08-12 |
| docs 子域 | `docs.joinpond.ai/docs/{slug}`（llms.txt 列出 ~14 篇） | ~14 | 2026-08-12 |

> 完整 URL 明细无法获取（sitemap 500）。`⚠️ 待验证：sitemap.xml 是否有效；任务详情/公司详情动态 URL 模式`。

---

## 6. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| 首页 `/` | 主导航 CTA：Create a Task / Browse Tasks / Browse All Agents / List Your Startup / Sign in / Sign up | 任务市场、Discoveries、注册转化 |
| 主导航 | Tasks、Discoveries、Markets、Points、Portfolio | 三产品线 + 用户功能区 |
| 页脚 | Product（AI Tasks、AI Marketplace）、Company（Docs、About Us、Career）、Legal（Terms、Privacy） | docs 子域、法务页 |
| `/markets` | 页脚 FAQ（SAFE / token warrant / 撤资 / 3 个月未关闭返还） | 转化投资者 |
| `/tasks` | 任务卡片 → 详情页、My Applications | 任务申请转化 |

---

## 7. URL 分阶段规划

| 阶段 | 新增页面 | 对应关键词优先级 | 理由 |
|------|---------|----------------|------|
| 短期（0–3 月） | `/blog` 内容中心（首篇：Pond vs Upwork、Pond vs Kaggle） | P0 商业型词 | 对比页承接商业意图，补齐内容缺口 |
| 短期 | 任务详情页 SEO 化（静态渲染 + schema） | P1 交易型词 | 提升单条 bounty 的搜索引擎可见性 |
| 中期（3–6 月） | `/pricing` 或费率透明页（任务发布费率、Markets 佣金） | P1 商业型词 | 定价透明度目前依赖联系团队，影响转化 |
| 中期 | `/agents` 独立 Agent 目录落地页（目前 Browse All Agents 为首页区块） | P0 信息型词 | "ai agent marketplace" 核心词的承接页 |
| 长期（6–12 月） | 本地化路径（`/es`、`/zh` 等）+ hreflang | — | 服务 181 国用户，目前仅英文 |

---

> 关联：[主文档](./pond.md) | [keywords](./pond-keywords.md) | [features](./pond-features.md) | [competitors](./pond-competitors.md) | [use-cases](./pond-use-cases.md) | [growth-strategy](./pond-growth-strategy.md) | [others](./pond-others.md)

*Last updated: 2026-08-12*
