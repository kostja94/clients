# Enter Pro — 站点结构

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[enter.md](./enter.md) | [enter-keywords.md](./enter-keywords.md) | [enter-features.md](./enter-features.md) | [enter-others.md](./enter-others.md)

**Last updated**: 2026-06-25 | 识别方式：robots.txt + sitemap.xml + 首页 withAllLinks（[enter.converge.ai](https://enter.converge.ai/)）

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [enter.md](./enter.md) |
| 关键词 | [enter-keywords.md](./enter-keywords.md) |
| 功能 | [enter-features.md](./enter-features.md) |
| 使用场景 | [enter-use-cases.md](./enter-use-cases.md) |
| 竞品 | [enter-competitors.md](./enter-competitors.md) |
| 增长策略 | [enter-growth-strategy.md](./enter-growth-strategy.md) |
| Sitemap 明细 | [enter-others.md](./enter-others.md) |

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 营销首页 | enter pro, ai dev agent, vibe coding | P0 |
| `/features/ai-app-builder` | 功能着陆 | ai app builder, no code app maker | P0 |
| `/features/ai-website-builder` | 功能着陆 | ai website builder | P0 |
| `/features/ai-agent-builder` | 功能着陆 | ai agent builder | P0 |
| `/features/visual-editor` | 功能着陆 | visual editor ai coding | P0 |
| `/templates` | 模板库 | website templates ai | P0 |
| `/components` | 组件库 | ui components ai builder | P1 |
| `/code` | 产品：Enter Code | ai coding terminal agent | P0 |
| `/cli` | 产品：Enter CLI | enter cli cursor claude code | P0 |
| `/ai-all` | 产品：AI ALL | unified llm api builder | P1 |
| `/blog` | 内容索引 | ai app builder guide | P1 |
| `/blog/{slug}` | 内容详情 | [话题长尾] | P1 |
| `/school` | 教育/教程 | enter pro tutorial | P2 |
| `/forum` | 社区 | enter pro community | P2 |
| `/docs/code` | 文档 | enter code docs | P1 |
| `converge.ai/pricing?product=enter` | 定价（父域） | enter pro pricing | P0 |

---

## 2. URL 层级与信息架构

```
enter.converge.ai（营销 + 社区主域）
├── /                              # 首页：Vibe Coding AI Dev Agent
├── /{lang}/                       # 多语言首页（de/pt/es/fr/id/it/ja/ko/ru/ar/tr/zh/hi 等）
│
├── 产品线
│   ├── /code                      # Enter Code — 终端本地 AI Super Agent
│   ├── /cli                       # Enter CLI — 对接 Claude Code / Cursor / Codex
│   ├── /ai-all                    # AI ALL — 统一 LLM 入口
│   └── /school                    # Enter School 教程
│
├── 资源
│   ├── /templates                 # 网站/应用模板库
│   └── /components                # 可复用 UI 组件
│
├── Features（能力 + 行业/角色着陆）★
│   ├── /features                  # 功能聚合（页脚）
│   ├── /features/ai-app-builder
│   ├── /features/ai-website-builder
│   ├── /features/ai-agent-builder
│   ├── /features/visual-editor
│   ├── /features/collaborative-coding
│   ├── /features/website-template
│   ├── /features/code-editor
│   ├── /features/ai-for-{developers|product-manager|small-businesses|...}
│   └── /features/{saas-website-builder|online-shop-builder|ai-page-generator|...}
│
├── 内容
│   ├── /blog                      # 博客索引（?category=Announcement|Changelog|Guide|...）
│   └── /blog/{slug}               # 单篇（含多语言镜像 /{lang}/blog/{slug}）
│
├── 社区
│   ├── /forum                     # 论坛首页
│   ├── /forum/activities          # 活动
│   └── /forum/t/{uuid}            # 帖子（programmatic 量级大）
│
├── 增长
│   └── /ambassador                # 大使计划
│
└── 文档
    └── /docs/code                 # Enter Code 文档

应用内（robots Disallow，不索引）
├── /workspace
└── /app

外部 / 生态
├── converge.ai/pricing?product=enter   # 统一定价（Converge AI 账户体系）
├── converge.ai/terms-of-service
├── converge.ai/privacy-policy
├── framia.converge.ai / combos.fun / concat.pro / anycap.ai  # 同团队产品
├── ambassador.enter.pro
├── x.com/EnterProAI · discord · tiktok · youtube · linkedin/enterproai
└── feedback@enter.pro · support@enter.pro
```

### 主导航（2026-06-25 观测）

| 区域 | 项 |
|------|-----|
| 顶栏 | Home · Pricing（跳转 converge.ai）· 产品（AI ALL / Enter Code / Enter CLI）· Templates · Components |
| Features 下拉 | Website Templates · AI Agent Builder · Visual Editor · Collaborative Coding · AI Website/App Builder · 角色（Developers/PM/Small Biz/Startup）· 行业（HR/Op/Marketing/SaaS/...） |
| Blog 下拉 | Announcement · Changelog · Event · Guide · Insight · User Story |
| 社区 | Ambassador · School · Forum |
| 页脚 Products | Framia · Combos · Concat · AnyCap · AI All |
| 页脚 Resources | Blog · Changelog · Enter Code Docs · Forum · Features · Activity · Ambassador · School |

---

## 3. 技术架构

| 维度 | 观测 |
|------|------|
| 前端栈（生成物） | React + Tailwind（FAQ 明示可导出标准代码） |
| 后端 / BaaS | Supabase（数据库、存储、Serverless、Cron）；Stripe 支付 |
| 部署 | 一键部署至全球 Edge；支持 Custom Domain |
| LLM | 统一 API Key 接入 GPT、Claude、Gemini、Grok 等；按 list price 计费 |
| 集成 | GitHub Sync、Google Analytics（更多 Coming Soon） |
| CDN / 安全 | Cloudflare Managed robots Content-Signal |
| 多语言 | 路径前缀 `/{lang}/` 镜像核心页与 blog/features |

---

## 4. 多语言

| 语言代码 | 示例路径 | 备注 |
|---------|---------|------|
| en（默认） | `/features/ai-app-builder` | 无语言前缀 |
| de, pt, es, fr, id, it, ja, ko, ru, ar, tr | `/de/features/...` | sitemap 全量镜像 |
| zh, hi | `/zh/blog/...` | 博客等部分路径 |

**hreflang / canonical**：多语言页在 sitemap 中并列出现；**待验证** 各语言页 canonical 与 x-default 策略。

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| sitemap.xml（单文件） | 全站 URL 平铺 | **~3,870** | 2026-06-25 |
| 多语言镜像 | `/{lang}/features/{slug}` | ~14 语言 × 功能页 | 2026-06-25 |
| Blog | `/blog/{slug}` + `/{lang}/blog/{slug}` | 数十篇 × 多语言 | 2026-04–06 |
| Forum | `/forum/t/{uuid}` | 数百+ 帖子 | 2026-04–06 |
| Features 着陆 | `/features/{slug}` | ~25+ 英文 slug × 多语言 | 2026-06-25 |

> 完整 URL 统计与抽样 → [enter-others.md](./enter-others.md#1-sitemap-明细)

---

## 6. robots.txt 要点

| 项 | 内容 |
|----|------|
| Allow | `/`（默认 User-agent: *） |
| Disallow | `/workspace`、`/app`（应用内工作区） |
| Sitemap | `https://enter.converge.ai/sitemap.xml` |
| Content-Signal | `search=yes`；通用 `ai-train=yes`；Cloudflare 段对 GPTBot/ClaudeBot/Google-Extended 等 **Disallow** |
| AI 爬虫 | 对 Amazonbot、GPTBot、ClaudeBot 等主流 AI 训练/扩展爬虫 **禁止抓取**（与 search 索引策略分离） |

---

## 7. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/` | CTA + Feature 卡片 + FAQ | `/features/*`、注册试用 |
| `/features/ai-app-builder` 等 | 功能子模块 + Try Enter | 转化、交叉链至 Visual Editor / Agent |
| `/templates`、`/components` | 模板/组件详情 | 降低冷启动、SEO 长尾 |
| `/blog` | 分类 + 最新文章 | Guide/Changelog 培育 |
| 页脚 | 产品矩阵 + 文档 + 社区 | Forum、School、Converge 定价 |
| `converge.ai/pricing` | 套餐对比表 | 付费转化 |

---

## 8. URL 分阶段规划（SEO 建议）

| 阶段 | 建议新增 | 链关键词 |
|------|---------|---------|
| **短期** | `/vs/{bolt|lovable|replit}` 对比页 | enter pro vs lovable |
| **短期** | 定价镜像页或 enter 子路径 `/pricing`（减少跳转流失） | enter pro pricing |
| **中期** | `/templates/{category}` 可索引分类 Hub | saas landing page template |
| **中期** | `/use-cases/{slug}` 与 features 角色页去重整合 | ai app builder for startup |
| **长期** | Forum 高质帖 curated `/showcase` | enter pro examples |

---

*来源：robots.txt、sitemap.xml、首页 withAllLinks 2026-06-25*
