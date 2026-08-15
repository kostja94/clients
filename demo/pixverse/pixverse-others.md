# PixVerse — 杂项归档

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[pixverse-site-structure.md](./pixverse-site-structure.md) | [pixverse.md](./pixverse.md)

**Last updated**: 2026-07-03

---

## 1. Sitemap 明细

### 1.1 索引结构

```
https://pixverse.ai/sitemap-index.xml   # 当前返回 HTTP 500 错误（2026-07-03 验证）
robots.txt: Sitemap: https://pixverse.ai/sitemap-index.xml
```

**状态**：sitemap 不可用。品牌站实际页面依赖首页 + 导航手动抓取估算。

### 1.2 URL 模式统计（基于已抓取页面 + 导航推断）

| 模式 | 说明 | 估算量级 | 状态 |
|------|------|---------|------|
| `/` | 品牌站首页（Research 内嵌） | 1 | 已验证 |
| `/en` | 英文首页 | 1 | 已验证 |
| `/news` | 新闻列表 | 1 | 已验证 |
| `/news/{slug}` | 新闻详情 | 16+ | 已验证（列表页抓取到 16 篇） |
| `/community` | 社区/CPP | 1 | 已验证 |
| `/community/creator-spotlight` | 创作者精选 | 1 | 可能 |
| `/research` | 研究/模型页 | **待验证** | 首页内嵌或独立页 |
| `/careers` | 招聘页 | **404** | 测试返回 404 |
| `/enterprise` | 企业方案 | **404** | 测试返回 404 |
| `/api` | API 平台 | **404** | 测试返回 404 |
| `/blog` | 博客 | **待验证** | 可能不存在 |
| `app.pixverse.ai/` | 创作平台首页 | 1 | 已验证 |
| `app.pixverse.ai/creation` | 视频创作 | 1 | 导航项 |
| `app.pixverse.ai/agent` | Agent | 1 | 导航项 |
| `app.pixverse.ai/canvas` | Canvas | 1 | 导航项 |
| `app.pixverse.ai/mini-apps` | Mini-Apps | 1 | 导航项 |
| `app.pixverse.ai/marketing-hub` | Marketing Hub | 1 | 导航项 |
| `app.pixverse.ai/posted` | 已发布作品 | 1 | 导航项 |
| `app.pixverse.ai/subscribe` | 订阅 | 1 | 导航项 |
| `app.pixverse.ai/earn-credits` | 积分获取 | 1 | 导航项 |

### 1.3 News 内容抽样（2026-07-03 抓取）

| 标题 | 日期 | 分类 |
|------|------|------|
| Captain Tsubasa Fans Can Now Bring Their Favorite Football Moments to Life With PixVerse | 2026-06-18 | 合作/品牌 |
| Captain Tsubasa x PixVerse: KAGAMI Gate PoC Launches for FIFA World Cup 2026 | 2026-06-12 | 合作/品牌 |
| PixVerse Partners with UN AI for Good Global Summit 2026 and Film Festival | 2026-04-23 | 合作/社会 |
| PixVerse Introduces C1, an AI Video Model Built for Film Production | 2026-04-07 | 产品/模型 |
| PixVerse Updates R1 Real-Time World Model with Shared Worlds and Personalized Avatars | 2026-04-01 | 产品/模型 |
| PixVerse Evolves From Creation Tool to Production Platform With New Studio and Developer Releases | 2026-03-31 | 产品/平台 |
| PixVerse Launches V6, Advancing AI Video Generation Across Creative and Agentic Workflows | 2026-03-30 | 产品/模型 |
| PixVerse Joins the Ranks of Global AI Unicorns with Asia's Largest Funding Round in AI Video Generation | 2026-03-12 | 融资/里程碑 |
| PixVerse V5.6 Ranks #2 on Artificial Analysis Leaderboard | 2026-02-28 | 产品/评测 |
| Alibaba-backed PixVerse launches real-time AI video tool, top executive tells CNBC | — | 媒体/PR |
| PixVerse Launches R1: A Real-Time World Model That Redefines AI Video Generation | 2026-01-12 | 产品/模型 |
| GMI Cloud Partners with PixVerse on AI Video Hackathon Ahead of SIGNAL 26 Launch | — | 合作/社区 |
| PixVerse Unveils Remix Feature, Following Swap Update, to Enhance Social Co-Creation | — | 产品/功能 |
| PixVerse Announces Series B Round to Drive International Expansion in AI Video | — | 融资 |
| PixVerse Debuts at Busan ACFM with Ten AI Films and Global AI Boot Camp | — | 活动/影视 |
| Tech in Asia: Alibaba leads $60m series B in SG-based AI video firm PixVerse | 2025-09-25 | 媒体/融资 |

### 1.4 Community / Creator Spotlight 抽样

| 作品 | 创作者 | 类型 |
|------|--------|------|
| Mars Landings | AI Video School | 科幻短片 |
| The Reckless Play | Maria Zozulia | 剧情短片 |
| Space Urbex | michaelheina | 氛围/探索 |
| Change | Caroline | 实验/艺术 |
| We're Going Live | TrishaCode | 活力/音乐 |
| SoulMatters | Pietro Fantone | 剧情/科幻 |
| Kiyosumi shirakawa | Wind Chen, Shen Siyuan | 7分钟短片/剧情 |
| Ruins | Yinqian Li | 剧情/社会 |

---

## 2. 数据引用

| 数据项 | 数值/描述 | 来源 | 日期 |
|--------|----------|------|------|
| V6 ELO 评分 | 1,343（Image-to-Video 排名最高） | Artificial Analysis | 2026-04-02 |
| Sora 2 Pro ELO | 1,195.5 | Artificial Analysis | 2026-04-02 |
| Kling 3.0 Omni ELO | 1,298 | Artificial Analysis | 2026-04-02 |
| VEO 3.1 ELO | 1,246 | Artificial Analysis | 2026-04-02 |
| V6 API 价格 | $4.80/min | pixverse.ai 官网 | 2026-07-03 |
| Sora 2 API 价格 | $6.00/min | pixverse.ai 官网对比 | 2026-07-03 |
| VEO 3.1 API 价格 | $24.00/min | pixverse.ai 官网对比 | 2026-07-03 |
| 成本降低 | 68% | pixverse.ai Enterprise 区 | 2026-07-03 |
| 生产加速 | 57% faster | pixverse.ai Enterprise 区 | 2026-07-03 |
| 内容产出提升 | 最高 10× | pixverse.ai Enterprise 区 | 2026-07-03 |
| 服务国家 | 177+ | pixverse.ai Enterprise 区 | 2026-07-03 |
| 视频分辨率 | 1080P（R1 实时生成） | pixverse.ai Research 区 | 2026-07-03 |
| 融资轮次 | Series B $60M（Alibaba 领投） | pixverse.ai/news + Tech in Asia | 2025-09 |
| 公司阶段 | AI 独角兽 | pixverse.ai/news | 2026-03-12 |
| CPP 等级 | Partner → Pro → Premier（及以上） | pixverse.ai/community | 2026-06-02 |
| 运营主体 | PixVerse（新加坡公司？**待验证**法律实体） | 官网 | — |
| 联系邮箱 | support@pixverse.ai | 官网页脚 | 2026-07-03 |
| 流量 / DR | **待验证** Semrush | — | — |
| sitemap | sitemap-index.xml HTTP 500 | robots.txt | 2026-07-03 |

---

## 3. 待验证项

| 项 | 说明 |
|----|------|
| **C 端定价详情** | app.pixverse.ai Subscribe 需登录，套餐档位与月费 $ **待验证** |
| **API 文档 URL** | API 文档入口路径未公开（/api 返回 404）；需确认 docs 子域或 app 内路径 |
| **sitemap 修复** | sitemap-index.xml 500 错误，无法确认完整 URL 结构 |
| **app 子域 SPA/SSR** | app.pixverse.ai 渲染方式（CSR/SSR）待验证，影响 SEO 可抓取性 |
| **多语言策略** | 177+ 国家服务但首页仅英文；是否存在隐藏语言切换 |
| **公司法律实体** | 新加坡公司（Tech in Asia 提到）具体实体名称待验证 |
| **前端技术栈** | app 端前端框架（React/Next.js/Vue）待验证 |
| **支付渠道** | Subscribe 使用的支付服务商（Stripe/其他）待验证 |
| **AI 爬虫策略** | robots.txt 仅声明 Allow 所有爬虫，是否有特殊规则 |
| **结构化数据** | 是否已添加 Schema.org VideoObject / Organization 标记 |
| **Core Web Vitals** | 品牌站 + app 站性能得分待 Lighthouse 审计 |
| **Semrush 流量** | 品牌词与品类词搜索量、点击量、DR 待复核 |
| **竞品 ELO 最新数据** | Artificial Analysis 数据截止 2026-04-02，后续排名变化待更新 |
| **R1 产品化程度** | R1 实时引擎在 app 中的可用性与限制待验证 |
| **C1 发布状态** | 2026-04-07 宣布，"Built for Film Production" 具体 GA 状态待验证 |
| **Canvas/Mini-Apps** | 功能详情需登录后深度体验验证 |

---

## 4. 品牌站导航完整记录（2026-07-03）

### pixverse.ai 首页顶栏

```
Research | Product | Enterprise | Community | News | Careers | Blog
[Download App] [Login] [Try PixVerse] [API]
```

### pixverse.ai 首页模型展示

```
R1: Real-Time Interactive World Engine
V6: Precision Control & Native Artistry
V5.6: Enhanced Audio-Visual Consistency & Output Quality
V5.5: One-Click Complete Storytelling
V5: A Fully Upgraded General-Purpose Model
V4.5: Narrative Takes Shape
C1: AI Video Model Built for Film Production（News 页提及）
```

### pixverse.ai 产品能力展示

```
Text/Image to Video | AI Templates | MultiShot | Agent
Lip Sync & Audio | Video Editing | Multi-Frame Control | Character Reference
```

### pixverse.ai 页脚

```
Products: PixVerse Web · API Solutions

Company: About Us · News · Community · Join Us · Affiliate

API: API Platform · API Documentation · API Console

Contact & Support: support@pixverse.ai · Feedback
```

### app.pixverse.ai 导航

```
Home · Creation · Agent · Canvas · Mini-Apps · Marketing Hub · Posted

用户区: Subscribe · Earn Credits
```

### 外部/社交链接

```
**待验证** X/Twitter · YouTube · TikTok · Discord · LinkedIn · Instagram
```

---

*归档规则：sitemap 不可用（500），URL 清单基于手动抓取 + 导航推导；News 16 篇全量标题已记录*
