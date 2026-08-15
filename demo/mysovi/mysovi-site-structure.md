# Sovi.AI — 站点结构

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[mysovi.md](./mysovi.md) | [mysovi-keywords.md](./mysovi-keywords.md) | [mysovi-features.md](./mysovi-features.md) | [mysovi-others.md](./mysovi-others.md)

**Last updated**: 2026-06-24 | 识别方式：robots.txt + sitemap 索引 + 子 sitemap 抽样 + 首页/导航 withAllLinks（[mysovi.ai](https://mysovi.ai/)）

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [mysovi.md](./mysovi.md) |
| 关键词 | [mysovi-keywords.md](./mysovi-keywords.md) |
| 功能 | [mysovi-features.md](./mysovi-features.md) |
| 使用场景 | [mysovi-use-cases.md](./mysovi-use-cases.md) |
| 竞品 | [mysovi-competitors.md](./mysovi-competitors.md) |
| 增长策略 | [mysovi-growth-strategy.md](./mysovi-growth-strategy.md) |
| Sitemap 明细 | [mysovi-others.md](./mysovi-others.md) |

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 营销首页 | sovi ai, ai study companion | P0 |
| `/chat` | 产品：Ask Sovi 作业助手 | ai homework helper, snap and solve | P0 |
| `/study` | 产品：AI Study Tools | chat pdf, ai notes, quiz generator | P0 |
| `/apexam` | 产品：AP 模考 | ap test prep, ap practice exam | P0 |
| `/resources` | SEO：题库聚合入口 | math questions solved, homework answers | P0 |
| `/resources/{subject}/{slug}` | SEO：单题详情（programmatic） | [题目长尾] | P0 |
| `/resources/category/{subject}` | SEO：学科分类列表 | ap statistics questions | P1 |
| `/blog` | 内容：博客索引 | essay writing tips | P1 |
| `/blog/basic-knowledge/{slug}` | 内容：写作/基础学科 | how to write thesis statement | P1 |
| `/video` | 功能：视频讲解 | video explanation homework | P1 |
| `/expert` | 功能：真人/专家辅导 | expert homework help | P1 |
| `/search` | 站内搜索 | sovi ai search | P2 |
| `/faq` | 支持/FAQ 索引 | sovi ai not working | P1 |
| `/about` | App 下载 / 关于 | sovi ai app download | P1 |
| `/privacy-policy` | 合规 | — | P2 |
| `/terms-of-service` | 合规 | — | P2 |

---

## 2. URL 层级与信息架构

```
mysovi.ai（主域）
├── /                              # 营销首页：社会证明 + 三大能力 CTA
├── /home                          # 应用内 Home（登录态，与 / 部分重叠）
│
├── Ask Sovi（作业求解）
│   ├── /chat                      # 主聊天/拍照解题
│   ├── /video                     # 视频讲解
│   ├── /expert                    # Expert Help
│   └── /apps/assignment-helper    # Assignment Helper 着陆
│
├── AI Study（材料学习）
│   ├── /study                     # 上传 PDF/Photo/Text/Word/PPT
│   ├── /study?tab=cheatsheet      # Cheatsheet
│   ├── /study?tab=notes           # AI Notes
│   ├── /study?tab=writing         # Smart Writing
│   ├── /study?tab=recording       # Live Recording
│   ├── /study?type=knowledge      # Chat PDF
│   ├── /study?type=quiz           # Quiz Generator
│   └── /apps/{cheatsheet|ai-notes|smart-writing|live-recording}
│
├── AP Test Prep
│   └── /apexam                    # 单元练习 + Full Length Mock（MCQ+FRQ）
│
├── Resources（Programmatic SEO 题库）★
│   ├── /resources                 # 默认/math 题库列表
│   ├── /resources/category/{subject}[/{page}]
│   └── /resources/{subject}/{slug}
│
├── Blog
│   ├── /blog
│   └── /blog/basic-knowledge/{slug}
│
├── Apps / 营销着陆
│   ├── /apps/assignment-helper
│   ├── /apps/cheatsheet | ai-notes | smart-writing | live-recording
│   ├── /apps/career/              # 招聘
│   └── /apps/whoami               # 20 Questions 小游戏（**待验证** 与主产品关系）
│
├── 支持 / 合规
│   ├── /faq                       # FAQ 索引
│   ├── /faq/{cat}/{id}            # FAQ 详情
│   ├── /about                     # App 下载 QR
│   ├── /privacy-policy
│   ├── /terms-of-service
│   ├── /cookie-policy             # App Store 引用，**待验证** Web 可访问性
│   └── /legal                     # App Store 引用，**待验证**
│
└── /search                        # 站内搜索

外部 / 子域
├── question-banks.mysovi.ai       # 旧/并行题库域（robots Disallow /question-banks/ 于主域）
├── apps.apple.com/.../id6740720452
└── mysov.onelink.me/...           # 深度链接 / App 归因
```

### 主导航（2026-06-24 观测）

| 区域 | 项 |
|------|-----|
| 顶栏 | Home · Ask Sovi（Video / Expert / Assignment Helper）· AI Study（Cheatsheet / Notes / Writing / Recording）· AP Test Prep · Resources · Blog · Careers · App |
| 首页 CTA | Ask Sovi · Open study tools · Start AP practice · Get the App |
| 页脚 Features | Ask Sovi · AI Study · AP Test Prep · Resources · Blog · Search |
| 页脚 Learn More | About Us · FAQ · Careers · Privacy · Terms |
| 社交 | TikTok · Reddit r/Sovi_ai · Instagram |

### URL 别名 / 不一致（整理待办）

| 问题 | 路径 A | 路径 B | 建议 |
|------|--------|--------|------|
| AI Notes | `/study?tab=notes` | `/ai-notes`、`/apps/ai-notes` | 统一 canonical |
| Careers | `/apps/career/` | `/page_in/apps/career` | 301 合并 |
| Resources 默认 | `/resources` | `/resources/category/math` | 明确默认学科 |
| App 页 | `/about` | `/app`（sitemap 有 `/app`） | **待验证** 是否同页 |

---

## 3. 技术架构

| 维度 | 观测 | 置信度 |
|------|------|--------|
| **前端** | SPA/Web App；`/chat` 为产品壳，需登录/Upgrade | 高 |
| **Sitemap** | 三级索引：`sitemap.xml` → main / resources / blog | 高 |
| **Programmatic SEO** | `/resources/{subject}/{slug}` 海量单题页；12 学科子 sitemap | 高 |
| **robots.txt** | 开放索引；显式 Allow GPTBot、ClaudeBot、PerplexityBot 等 AI 爬虫（2026-03-11） | 高 |
| **Disallow** | `/api/`、`/question-banks/` | 高 |
| **App** | iOS 优先（Edgewise Limited）；OneLink 深度链接 | 高 |
| **框架/CMS** | 未确认（**待验证** Wappalyzer） | 低 |
| **多语言** | App 支持 EN+7；Web 以英文为主 | 中 |

---

## 4. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| `sitemap-main.xml` | 核心产品/合规/Apps 着陆 | **17** URL | 2026-04-03 ~ 2026-05-14 |
| `blog-sitemap.xml` | `/blog/basic-knowledge/*` | **19** URL | 2026-04-13 |
| `resources/sitemap.xml` | 12 学科子 sitemap 索引 | 12 索引文件 | — |
| `resource/sitemap-math-page-1.xml` | `/resources/math/{slug}` | **≥500**/页（math 仅 page-1） | — |
| 分类分页 | `/resources/category/math/{n}` | math 分页至 **949+** | — |
| 其他学科 | calculus, physics, chemistry, biology, statistics, economics, literature, business, social_science, writing, others | 各 ≥1 sitemap 页 | — |

**URL 模式归纳**：

- 单题页：`/resources/{subject}/{question-slug}` — slug 取自题干关键词
- 分类列表：`/resources/category/{subject}`、`/resources/category/{subject}/{page}`
- 博客：`/blog/basic-knowledge/{slug}`

> 完整 sitemap 索引与子 sitemap 列表 → 详见 [mysovi-others.md §1](./mysovi-others.md#1-sitemap-明细)

---

## 5. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/` | 产品 CTA + 功能锚点 | `/chat`、`/study`、`/apexam`、App Store |
| `/chat` | 侧栏全站导航 | `/video`、`/expert`、`/study`、Resources 分类 |
| `/resources` | 题目列表 → 单题 | `/resources/math/{slug}`、分页 `/category/math/{n}` |
| `/faq` | 支持文章 | `/faq/{cat}/{id}`、`support@mysovi.ai` |
| `/blog` | 内容集群 | `/blog/basic-knowledge/*` |
| 页脚（全站） | 功能 + 合规 | Features 五链 + About/FAQ/Careers/Privacy/Terms |

**SEO 权重策略**：Resources 题库 + Blog 基础写作内容承担长尾；首页与 `/chat`/`/study`/`/apexam` 承接品牌与商业意图。

---

## 6. 多语言

| 维度 | 说明 |
|------|------|
| **App** | EN、FR、DE、JA、KO、ZH-Hans、ZH-Hant、ES（App Store 2026-06-24） |
| **Web** | 英文为主；未见 `/zh` 等独立 locale 路径 |
| **hreflang** | **待验证** |
| **题库** | slug 含少量非英文题干（如法语统计题） |

---

## 7. URL 分阶段规划

### 短期（0–90 天）

| 建议 URL | 目的 | 链接关键词 |
|----------|------|-----------|
| `/pricing` | 独立定价页（当前仅 App IAP + Upgrade CTA） | sovi ai pricing P0 |
| `/vs/gauth`、`/vs/solvely` | 对比着陆 | gauth alternative P0 |
| canonical 统一 | 合并 `/ai-notes` vs `/apps/ai-notes` vs query tab | 减少重复索引 |
| `/download` | iOS + Web 统一下载 | sovi ai app P1 |

### 中期（90–180 天）

| 建议 URL | 目的 |
|----------|------|
| `/ap/{subject}` | 按 AP 科目拆分模考着陆（Bio、Psych、Stat…） |
| `/subjects/{slug}` | 学科 hub 页链向 Resources + Chat |
| `/help/{topic}` | FAQ 结构化（替代 `/faq/0/{id}` 数字 ID） |

### 长期（180 天+）

| 建议 URL | 目的 |
|----------|------|
| 多语言 `/es`、`/zh-cn` | 匹配 App 语言与海外 K12 |
| Android 官方页 | **待验证** 是否有 Google Play |
| 创作者/教师 B2B `/for-teachers` | 拓展 2M+ 用户中的教师 Persona |

---

*来源：手动访问 + sitemap 解析 2026-06-24；[mysovi.ai](https://mysovi.ai/)、[robots.txt](https://mysovi.ai/robots.txt)、[sitemap.xml](https://mysovi.ai/sitemap.xml)*
