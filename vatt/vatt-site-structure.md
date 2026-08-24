# Vatt — 站点结构

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[vatt.md](./vatt.md) | [vatt-keywords.md](./vatt-keywords.md) | [vatt-features.md](./vatt-features.md) | [vatt-others.md](./vatt-others.md)

**Last updated**: 2026-08-06 | 识别方式：首页 + 定价页抓取 + [vatt-reaction-video-types.md §11](./vatt-reaction-video-types.md)

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [vatt.md](./vatt.md) |
| 关键词 | [vatt-keywords.md](./vatt-keywords.md) |
| 功能 | [vatt-features.md](./vatt-features.md) |
| 使用场景 | [vatt-use-cases.md](./vatt-use-cases.md) |
| 竞品 | [vatt-competitors.md](./vatt-competitors.md) |
| 增长策略（已归档） | [archive/vatt-growth-strategy.md](./archive/vatt-growth-strategy.md) |
| Channel 详情页策略 | [vatt-channel-pages-strategy.md](./vatt-channel-pages-strategy.md) |
| Reaction 类型 / Blog 队列 | [vatt-reaction-video-types.md](./vatt-reaction-video-types.md) |
| Sitemap 明细 | [vatt-others.md](./vatt-others.md) |
| 多语言迁移（已归档） | [archive/vatt-i18n-path-migration.md](./archive/vatt-i18n-path-migration.md) |

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 首页（品牌 + FAQ + 邀请码入口） | ai reaction video editor, edit reaction videos faster | P0 |
| `/pricing` | 定价页 | vatt pricing, ai video editor pricing | P0 |
| `/login` | 登录/注册页 | vatt login | P1 |

---

## 2. URL 层级与信息架构

```
vatt.ai（极简站点，SPA 推测 React/Next.js）
├── /                                          # 首页
│   ├── Hero：Edit reaction videos 10x faster
│   ├── 价值主张副标题
│   ├── 邀请码输入框（Enter invite code）
│   └── FAQ 区域（4 条问答）
│
├── /pricing                                   # 定价页
│   ├── Monthly / Annual 切换
│   ├── 套餐动态加载（Loading plans…）
│   ├── Cycle resets monthly
│   ├── Flexible tier expansion
│   ├── Tier matching billing
│   └── One-time free credits
│
├── /login                                     # 登录页
│   ├── Sign in / Get Invite
│   └── Redirecting to sign in…
│
└── 缺失页面（均返回 404）
    ├── /about（404）
    ├── /blog（404）
    ├── /features（404）
    ├── /terms（404）
    ├── /privacy（404）
    └── robots.txt（404）
```

### 首页结构（单页）

| 区域 | 内容 | CTA |
|------|------|-----|
| Hero | # Edit reaction videos 10x faster. + 副标题 | Enter invite code（输入框） |
| FAQ | Q1: What is vatt? / Q2: Who is it for? / Q3: How long? / Q4: Manual edit? | — |
| 页脚 | © 2026 Vatt Inc. Built for the next generation of storytellers. | — |

---

## 3. 技术架构

| 维度 | 观测 |
|------|------|
| 公司域 | [vattention.com](https://www.vattention.com/)（品牌站：公司愿景/技术理念/团队） |
| 产品域 | [vatt.ai](https://vatt.ai/)（产品站：Vatt 编辑器入口） |
| 前端栈 | **待验证**（推测 React/Next.js SPA，登录页有 redirect 行为） |
| 部署 | **待验证**（推测 Vercel 或 AWS） |
| 身份认证 | OAuth 重定向登录（**待验证** 具体提供商：Google/GitHub/邮箱） |
| 视频处理 | **待验证**（推测云服务 + AI 推理集群） |
| AI 模型 | **待验证**（情感检测模型，推测自研或基于开源 CV 模型微调） |
| 支付 | **待验证**（定价页动态加载，推测 Stripe） |
| CDN | **待验证** |
| SEO 状态 | 极差（无 robots.txt、无 sitemap、无 meta description） |
| 多语言 | `?lang=` 查询参数切换，URL 不变；已验证 **en / it / es / fr / de / zh / pt / ja** 8 种；路径前缀迁移方案见 [archive/vatt-i18n-path-migration.md](./archive/vatt-i18n-path-migration.md)（已归档） |
| 移动端 | **待验证**（SPA 推测响应式设计） |

---

## 4. robots.txt 与 Sitemap

| 项 | 内容 |
|----|------|
| robots.txt | **404 不存在** |
| sitemap.xml | **待验证**（推测未配置） |
| SEO 基本要素 | 首页仅标题 "Vatt | Edit reaction videos 10x faster"，**待验证** meta description |

---

## 5. 内链枢纽

| 枢纽页 | 链出类型 | 主要目标 |
|--------|---------|---------|
| `/` 首页 | 邀请码输入 → 注册流程 | /login |
| `/login` | Sign in → 认证跳转 | OAuth provider |
| `/pricing` | 套餐选择 → 订阅（**待验证** 是否从定价页直接订阅） | — |

**内链极度匮乏**：无导航栏、无页脚链接、无交叉引用。

---

## 6. URL 分阶段规划（SEO 建议）

### 6.1 基建（短期必做）

| 阶段 | 建议新增 | 链关键词 |
|------|---------|---------|
| **短期** | `/features` — AI 功能详解页 | ai reaction video editor, ai video highlight detection |
| **短期** | robots.txt + sitemap.xml | — |
| **短期** | `/privacy` + `/terms` + `/about` | — |
| **短期** | `/blog` — Blog 体系 | reaction video editing tips |

### 6.2 Blog Hub-Spoke（按 Semrush ROI 排序）

| 优先级 | 路径 | 主关键词 | 月搜 (US) | KDI |
|--------|------|---------|----------|-----|
| **P0** | `/blog/try-not-to-laugh-reaction-videos` | try not to laugh | 22,200 | 36 |
| **P0** | `/blog/types-of-reaction-videos` | reaction video, types of reaction videos | 1,600 | 46 |
| **P0** | `/blog/live-reaction-videos-guide` | live reaction | 1,600 | 27 |
| **P0** | `/blog/movie-reaction-videos-guide` | movie reaction, first time watching | ~1,480 | 34–36 |
| **P0** | `/blog/tiktok-reaction-videos-guide` | tiktok reaction | 480 | 26 |
| **P0** | `/blog/how-to-edit-reaction-videos-faster` | edit reaction videos faster | 待验证 | 低 |
| **P1** | `/blog/music-reaction-videos-guide` | music reaction, first time hearing | ~1,190 | 22–31 |
| **P1** | `/blog/ai-reaction-editor-vs-generator` | ai reaction editor vs generator | — | — |
| **P2** | `/blog/sports-reaction-videos` | sports reaction | 90 | 22 |
| **P2** | `/blog/trailer-reaction-videos` | trailer reaction | 50 | 23 |

**内链规则**：Hub = `types-of-reaction-videos` → 链出全部 Spoke → 各 Spoke 回链 Hub + `/features`

### 6.3 Channel 页 pSEO（Reactor 图谱）

| 优先级 | 路径 | 主关键词 | 状态 |
|--------|------|---------|------|
| **P0** | `/channel` | reaction video creators, best reaction channels | 待建 |
| **P0** | `/channel/xqc` | xqc reaction, xqc reaction videos | ✅ 已上线 |
| **P0** | `/channel/xiaolinshuo` | 小Lin说 reaction | ✅ 已上线 |
| **P0** | `/channel/{slug}` × 8 | {creator name} reaction | Phase 3 种子名单 |
| **P1** | `/source-video/{slug}` | {topic} reaction videos | Phase 4 联动 |

*完整策略、种子名单与 Roadmap* → [vatt-channel-pages-strategy.md](./vatt-channel-pages-strategy.md)

### 6.4 中期 / 长期

| 阶段 | 建议新增 | 链关键词 |
|------|---------|---------|
| **中期** | `/blog/vatt-vs-revid` | vatt vs revid |
| **中期** | `/blog/vatt-vs-descript` | vatt vs descript |
| **中期** | `/tutorials` | how to use vatt |
| **长期** | `/showcase` | vatt reaction video examples |
| **长期** | `/pricing` 静态化 | vatt pricing |

---

*来源：[vatt.ai](https://vatt.ai/)、[定价页](https://vatt.ai/pricing)、[登录页](https://vatt.ai/login) 2026-07-06*
