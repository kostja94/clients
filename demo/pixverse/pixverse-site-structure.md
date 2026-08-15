# PixVerse — 站点结构

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[pixverse.md](./pixverse.md) | [pixverse-keywords.md](./pixverse-keywords.md) | [pixverse-features.md](./pixverse-features.md) | [pixverse-others.md](./pixverse-others.md)

**Last updated**: 2026-07-03 | 识别方式：robots.txt + 首页内容 + 主导航抓取（[pixverse.ai](https://pixverse.ai/) + [app.pixverse.ai](https://app.pixverse.ai/)）

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [pixverse.md](./pixverse.md) |
| 关键词 | [pixverse-keywords.md](./pixverse-keywords.md) |
| 功能 | [pixverse-features.md](./pixverse-features.md) |
| 使用场景 | [pixverse-use-cases.md](./pixverse-use-cases.md) |
| 竞品 | [pixverse-competitors.md](./pixverse-competitors.md) |
| 增长策略 | [pixverse-growth-strategy.md](./pixverse-growth-strategy.md) |
| Sitemap 明细 | [pixverse-others.md](./pixverse-others.md) |

---

## 1. 双域架构总览

PixVerse 采用 **品牌营销站 + 应用平台** 双域分离架构：

```
pixverse.ai（品牌/营销/研究/社区主域）
├── 品牌展示 + 模型研究 + 新闻 + 社区 + 招聘

app.pixverse.ai（创作平台/应用域）
├── 视频创作 + 模板 + Agent + Canvas + 订阅
```

---

## 2. 核心路径表

### 2.1 pixverse.ai（品牌站）

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（Research 主导） | ai video generation, frontier ai video | P0 |
| `/en` | 英文首页（与 `/` 可能同一页面） | ai video generator | P0 |
| `/news` | 新闻/博客索引 | pixverse news, ai video news | P1 |
| `/news/{slug}` | 新闻详情 | [话题长尾] | P1 |
| `/community` | 社区 + CPP 创作者计划 | ai video creator community | P1 |
| `/research` | 研究/模型介绍 | pixverse v6, pixverse r1, ai video model | P0 |
| `/careers` | 招聘页（404 待验证路径） | pixverse jobs | P2 |
| `/enterprise` | 企业方案（404 待验证路径） | enterprise ai video | P0 |
| `/blog` | 博客（待验证是否存在） | ai video blog | P1 |
| API 相关 | **待验证** 独立子域或 /api 路径 | video generation api | P0 |

### 2.2 app.pixverse.ai（创作平台）

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 创作平台首页 | pixverse ai video generator | P0 |
| `/creation` | 视频创作（文本/图片转视频） | text to video ai, image to video ai | P0 |
| `/agent` | Agent 对话式创作 | ai video agent | P1 |
| `/canvas` | 创意画布 | ai video canvas | P2 |
| `/mini-apps` | 轻量工具集 | ai video tools | P2 |
| `/marketing-hub` | 营销素材中心 | ai marketing video | P1 |
| `/subscribe` | 订阅/定价 | pixverse pricing | P0 |
| `/earn-credits` | 积分获取 | pixverse credits | P2 |
| API Platform | **待验证** app 内或独立入口 | ai video api | P0 |

---

## 3. URL 层级与信息架构

```
pixverse.ai（品牌站）
├── /                                          # 首页：Research + Model Showcase
│
├── 研究 / 模型
│   ├── /research 或 首页内嵌                  # V6 / R1 / C1 / V5.6 / V5.5 / V5 / V4.5 模型介绍
│   └── 产品能力展示                            # Text/Image to Video · Templates · MultiShot · Agent ...
│
├── 内容
│   ├── /news                                   # 新闻列表
│   └── /news/{slug}                            # 单篇新闻
│
├── 社区
│   ├── /community                              # CPP 2.0 Creator Partner Program
│   └── /community/creator-spotlight            # 创作者精选展示
│
├── 企业
│   ├── /enterprise（**404 待验证**）            # 企业方案
│   └── API Platform（**待验证** 路径）           # API 文档 + 定价
│
├── 招聘
│   ├── /careers（**404 待验证**）                # Engineering / Product / Growth / Business
│   └── Join Us（首页锚点）
│
└── 页脚
    ├── Products: PixVerse Web · API Solutions
    ├── Company: About Us · News · Community · Join Us · Affiliate
    ├── API: API Platform · API Documentation · API Console
    └── Contact: support@pixverse.ai · Feedback

app.pixverse.ai（创作平台）
├── /                              # 创作平台首页
├── /creation                      # 视频创作入口
├── /agent                         # Agent 对话式创作
├── /canvas                        # 创意画布
├── /mini-apps                     # 轻量工具集
├── /marketing-hub                 # 营销素材
├── /posted                        # 已发布作品
├── /subscribe                     # 订阅管理
├── /earn-credits                  # 积分获取
└── API Platform（可能独立入口或 app 内）
```

### 主导航（2026-07-03 观测）

#### pixverse.ai 顶栏

| 区域 | 项 |
|------|-----|
| 主导航 | Research · Product · Enterprise · Community · News · Careers · Blog |
| CTA | Download App · Login · Try PixVerse · API |

#### app.pixverse.ai 顶栏

| 区域 | 项 |
|------|-----|
| 主导航 | Home · Creation · Agent · Canvas · Mini-Apps · Marketing Hub · Posted |
| 用户区 | Subscribe · Earn Credits |

---

## 4. 技术架构

| 维度 | 观测 |
|------|------|
| 前端栈 | **待验证**（app 端推测 React/Next.js 或 Vue SPA） |
| 视频模型 | 自研 V6 / R1 / C1 / V5.6 / V5.5 / V5 / V4.5 模型矩阵 |
| AI 基础设施 | **待验证**（推测自有 GPU 集群或云服务商合作） |
| API | RESTful API，按分钟计费 |
| CDN / 安全 | **待验证** Cloudflare 或其他 |
| 认证 | app 端需登录（**待验证** 邮箱/Google/其他 OAuth） |
| 支付 | Subscribe（**待验证** Stripe 或其他支付渠道） |
| 多语言 | 品牌站仅英文；177+ 国家服务但无多语言站点结构 |

---

## 5. Sitemap 与 URL 模式

| 来源 | 路径/模式 | 估算量级 | lastmod |
|------|----------|---------|---------|
| sitemap-index.xml | **500 错误**，待修复验证 | — | — |
| robots.txt | `Sitemap: https://pixverse.ai/sitemap-index.xml` | — | 2026-07-03 |
| 品牌站首页 | 单页应用/SSR 首页，模型内容内嵌 | 1 核心页 | 2026-07-03 |
| /news | 新闻列表 + 详情页 | 16+ 篇新闻 | 2025-09–2026-06 |
| /community | CPP 2.0 + Creator Spotlight | 2-3 页 | 2026-06 |
| app 子域 | Creation/Agent/Canvas 等 | ~10+ 页面 | 2026-07-03 |

> 完整 URL 统计与抽样 → [pixverse-others.md](./pixverse-others.md#1-sitemap-明细)

---

## 6. robots.txt 要点

| 项 | 内容 |
|----|------|
| Allow | `/`（默认 User-agent: *，全 Allow） |
| Disallow | 无 |
| Sitemap | `https://pixverse.ai/sitemap-index.xml`（当前返回 500，**待修复**） |
| AI 爬虫 | **待验证** 是否对 GPTBot/ClaudeBot 等做针对性屏蔽 |

---

## 7. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/`（品牌站首页） | CTA（Try PixVerse / Download App）+ 模型 Showcase + News 摘要 | app.pixverse.ai、/news、/community |
| `/news` | 新闻列表 → 详情 | /news/{slug} |
| `/community` | CPP 介绍 + Creator Spotlight + 申请入口 | CPP 申请流程 |
| app 首页 | Creation / Agent / Canvas / Templates 入口 | 各创作功能模块 |
| 页脚 | 产品矩阵 + API + 公司信息 + 社区 | API、News、Community |
| app `/subscribe` | 定价套餐对比 | 付费转化 |

---

## 8. URL 分阶段规划（SEO 建议）

| 阶段 | 建议新增 | 链关键词 |
|------|---------|---------|
| **短期** | 修复 sitemap-index.xml 500 错误 | — |
| **短期** | `/features/text-to-video`、`/features/image-to-video` 能力着陆 | ai video generator |
| **短期** | `/vs/sora`、`/vs/kling`、`/vs/runway` 对比页 | pixverse vs sora |
| **短期** | `/pricing` 公开定价页（含 C+B 端） | pixverse pricing |
| **中期** | `/templates` 公开 Template Gallery | ai video templates |
| **中期** | `/blog` + 教程/Guide 内容体系 | how to use pixverse |
| **中期** | 多语言 Landing（/ja /ko /es /pt） | ai 動画生成 等 |
| **长期** | `/enterprise` 企业方案详情页 | enterprise ai video |
| **长期** | API 开发者文档站（独立或 /api/docs） | video generation api docs |

---

*来源：robots.txt、首页内容、主导航 2026-07-03*
