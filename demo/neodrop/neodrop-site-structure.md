# NeoDrop — 站点结构

> 遵循 [客户文档规范](../../client-template.md)
> **本文档职责**：URL 层级、信息架构、技术栈推断。  
> **引用**：[neodrop.md](./neodrop.md) 概览 | [neodrop-growth-strategy.md](./neodrop-growth-strategy.md) 增长策略

**最近更新**：2026-05-22（初建，部分路径待抓取复核）

---

## 一、域名体系

| 域名 | 定位 | 说明 |
|------|------|------|
| [neodrop.ai](https://neodrop.ai/) | 品牌主站 | SPA Web App：Feed、Discover、Channel、Pricing |
| — | 文档站 | ⚠️ 未见独立 docs 子域 |
| — | 博客 | ⚠️ 未见 `/blog`；Drop 内容承担部分内容 SEO |

*单域名架构，内容型 URL 以 `/feed/`、`/channel/` 为主。*

---

## 二、导航结构（已确认）

| 导航/入口 | 目标 | 状态 |
|-----------|------|------|
| **Feed** | `/feed` | 已确认 |
| **Discover channels** | `/discover` | 已确认 |
| **Create Channel** | `/create/agent` | 已确认 |
| **Pricing** | `/pricing` | 已确认 |
| **Sign in / Sign up** | `/auth` | 已确认 |
| **Subscription Terms** | `/paid-terms` | 已确认（定价页链接） |

首页 Feed 子 Tab：**Subscribed** · **Recommended** · **Activity**

---

## 三、已知 URL 清单

### 已确认路径

| 路径 | 内容 | 来源 |
|------|------|------|
| `/` | 首页（Feed 视图） | 直接访问 |
| `/feed` | Feed 主列表 | 直接访问 |
| `/feed/{dropId}` | 单条 Drop 详情（如 AI Agent 生态速报） | 直接访问 |
| `/discover` | 频道发现：Editor's Picks、榜单、分类 | 直接访问 |
| `/channel/{channelId}` | 单个 Channel 页 | 直接访问 |
| `/create/agent` | 创建 Channel 向导（需登录） | 直接访问 |
| `/auth` | 登录注册 | 直接访问 |
| `/pricing` | 定价与 FAQ | 直接访问 |
| `/paid-terms` | 订阅条款 | 定价页链接 |

### URL 模式

| 模式 | 示例 | 说明 |
|------|------|------|
| Channel ID | `/channel/J1xzxS3pbYM` |  opaque ID |
| Drop ID | `/feed/DT3KQuWFM0R` |  opaque ID |

---

## 四、核心路径表（§0.3 达标）

| # | 用户路径 | 步骤 | 转化目标 |
|---|----------|------|----------|
| 1 | **发现 → 订阅** | `/` → `/discover` → Subscribe Channel → `/feed` | 激活订阅者 |
| 2 | **创建首个 Channel** | `/create/agent` → `/auth` → 描述兴趣 → 生成 Drop | 创作者激活 |
| 3 | **阅读 Drop** | `/discover` 或 `/feed` → `/feed/{id}` | 内容消费深度 |
| 4 | **付费转化** | `/pricing` → `/auth` → Checkout（Waffo） | Starter/Pro/Studio |
| 5 | **官方示范** | `/discover` Editor's Picks → Official Channel → Drop | 质量信任建立 |

---

## 五、信息架构（IA）

```
neodrop.ai
├── Feed（消费）
│   ├── Subscribed
│   ├── Recommended
│   └── Activity
├── Discover（发现）
│   ├── Editor's Picks
│   ├── Most Subscribed
│   ├── Fastest Growth
│   ├── Newly Created
│   └── 分类筛选（AI / Side Hustle / …）
├── Create（创作）
│   └── Channel Agent 向导
├── Channel（公开页）
│   └── Drops 列表 + Subscribe
├── Drop（内容页）
│   └── 文章 / 多媒体详情
└── Monetization
    ├── Pricing
    ├── Auth
    └── Paid Terms
```

---

## 六、技术栈推断

| 层级 | 推断 | 依据 |
|------|------|------|
| **前端** | SPA（React/Next 类） | 客户端渲染、opaque 路由、Pricing 需 Jina 渲染 |
| **认证** | 自建 `/auth` | 登录-gated 创建流程 |
| **支付** | Waffo Checkout | Pricing FAQ |
| **内容** | 多 Agent 后端 + Credits 计量 | 产品文案 |
| **CDN/SEO** | ⚠️ 部分页面 SSR/预渲染弱 | 原始 fetch 部分页面为二进制/乱码 |

---

## 七、URL 优先级分阶段规划

### Phase 0（当前已有）

| 路径 | 优先级 | 作用 |
|------|--------|------|
| `/` | P0 | 首页/Feed |
| `/discover` | P0 | 发现与冷启动 |
| `/create/agent` | P0 | 创作者转化 |
| `/pricing` | P0 | 付费 |
| `/channel/{id}` | P0 | Channel SEO 与社会分享 |
| `/feed/{id}` | P0 | Drop 深度阅读 |

### Phase 1（建议新建，3 个月内）

| 路径 | 优先级 | 作用 |
|------|--------|------|
| `/features` | P0 | 功能 SEO 承接 |
| `/about` | P1 | 团队/信任 |
| `/blog` | P1 | 品牌内容 + SEO |
| `/channels/ai` 等分类 Landing | P1 | Discover 分类 SEO 化 |
| `/vs/{competitor}` | P1 | 竞品拦截 |

### Phase 2（增长期）

| 路径 | 优先级 | 作用 |
|------|--------|------|
| `/use-cases/{persona}` | P1 | 场景 Landing |
| `/docs/api` | P2 | Studio/Enterprise API |
| `/download` 或 App Store | P2 | 移动端 |
| SEO 友好 Drop URL | P1 | `/feed/{slug}` 或 `/d/{slug}` |

---

## 八、SEO / 结构待办

| ID | 问题 | 建议 |
|----|------|------|
| S1 | Drop URL 为 opaque ID，不利于分享 SEO | 增加 slug 或 canonical title path |
| S2 | 缺少 `/features`、`/about` | 补齐营销页 |
| S3 | 无 sitemap 公开 | 生成 `/sitemap.xml` 含 Channel/Drop |
| S4 | 部分路由 crawlers 抓取差 | 加强 SSR/预渲染或 prerender 关键页 |

---

*文档创建日期：2026-05-22 | 模式：冷启动*
