# CrushOn.AI — 站点结构

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[crushon.md](./crushon.md) | [crushon-keywords.md](./crushon-keywords.md) | [crushon-features.md](./crushon-features.md)

**Last updated**: 2026-06-17 | 识别方式：手动访问 crushon.ai、chat.crushon.ai、aiwiki.crushon.ai

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [crushon.md](./crushon.md) |
| 关键词 | [crushon-keywords.md](./crushon-keywords.md) |
| 功能 | [crushon-features.md](./crushon-features.md) |
| 使用场景 | [crushon-use-cases.md](./crushon-use-cases.md) |
| 竞品 | [crushon-competitors.md](./crushon-competitors.md) |
| 增长策略 | [crushon-growth-strategy.md](./crushon-growth-strategy.md) |

---

## 1. 核心路径表

| 路径 | 页面类型 | 目标关键词 | 优先级 |
|------|---------|-----------|--------|
| `/` | 产品首页 / Discover | crushon ai, character ai chat | P0 |
| `/pricing` | 定价 | crushon ai pricing | P0 |
| `chat.crushon.ai/` | SEO 营销落地 | ai girlfriend, character ai alternative | P0 |
| `chat.crushon.ai/character-ai-chat` | 品类着陆 | character ai chat | P0 |
| `aiwiki.crushon.ai/wiki/Main_Page` | 产品 Wiki | crushon guide | P1 |
| `aiwiki.crushon.ai/wiki/FAQ` | 帮助/订阅 FAQ | crushon cancel subscription | P1 |
| Discover（标签页） | 角色发现 | anime ai chat, nsfw character ai | P0 |
| Characters | 角色库入口 | browse ai characters | P0 |
| Memories | 记忆管理 | ai chat memory | P1 |
| Creators | 创作者中心 | create ai character | P0 |
| Login | 转化 | crushon login | P0 |

---

## 2. URL 层级与信息架构

```
crushon.ai（主产品域）
├── /                          # Discover + 角色 Feed
├── /pricing                   # 定价（内容较薄）
├── Characters                 # 我的/浏览角色
├── Memories                   # 固定记忆
├── Creators                   # 创作与发布
├── Log In                     # 认证
├── 顶栏 SEO 着陆链接
│   ├── AI Porn Chat           # 成人向 SEO 入口
│   ├── AI Sex Chat
│   └── Juicy Chat AI
└── 页脚合规
    ├── Complaints Policy
    └── 18 U.S.C. 2257 Statement

chat.crushon.ai（营销子域）
├── /                          # 长文 SEO：AI Girlfriend / Roleplay / FAQ
├── /character-ai-chat         # Character AI 品类页
└── 内嵌对比表（vs Character.AI / Janitor.AI）

aiwiki.crushon.ai（文档 Wiki）
├── /wiki/Main_Page
├── /wiki/FAQ
├── /wiki/Subscription
└── 角色创建、模型、Memories 等专题页
```

### 主导航（2026-06-17 观测）

| 区域 | 项 |
|------|-----|
| 顶栏 | Search、English、Log In |
| 主导航 | Characters · Memories · Creators |
| Discover 筛选 | gender、Animated、Unfiltered、标签云（100+ 标签） |
| 营销链接 | AI Porn Chat、AI Sex Chat、Juicy Chat AI、More |

---

## 3. 技术架构

| 维度 | 观测 | 置信度 |
|------|------|--------|
| **前端** | SPA 式 Discover Feed，动态加载角色卡 | 高 |
| **子域策略** | 产品（crushon.ai）与 SEO（chat.）与文档（aiwiki.）分离 | 高 |
| **移动端** | iOS PWA 主屏安装；Android 独立 APK | 高（Wiki FAQ） |
| **支付** | App Store、Google Play、SubscribeStar、Paymentwall、G2A | 高 |
| **CDN/资源** | 角色 Banner 托管于 file.garden、postimg、S3 等第三方 | 中 |
| **sitemap** | `crushon.ai/sitemap.xml` → **404**（2026-06-17） | 已验证 |
| **框架/CMS** | 未确认（**待验证** Wappalyzer） | 低 |

---

## 4. 多语言

| 维度 | 说明 |
|------|------|
| **UI 语言** | 英文为主；顶栏 Language 切换 |
| **角色语言** | 聊天设置或 Prompt 指定回复语言 |
| **语音** | 9 语言预设（英/日/韩/中/俄/西/葡/德/印尼） |
| **hreflang** | **待验证** 是否有独立 `/zh` 等路径 |
| **SEO** | chat 子域英文长文；未见完整 i18n 站点地图 |

---

## 5. URL 分阶段规划

### 短期（0–90 天）

| 建议 URL | 目的 | 链接关键词 |
|----------|------|-----------|
| `/pricing` 充实 | 统一套餐表 + Schema | crushon ai pricing P0 |
| `/vs/character-ai` | 主域 canonical 对比页 | character ai alternative P0 |
| `/vs/janitor-ai` | BYOK 迁移承接 | janitor ai alternative P1 |
| `/download` | APK + iOS 安装指南 | crushon ai apk P1 |
| `/sitemap.xml` | 技术 SEO 基础 | — |

### 中期（90–180 天）

| 建议 URL | 目的 |
|----------|------|
| `/learn/create-character` | 创作者教程（镜像 Wiki） |
| `/tags/{slug}` | 可索引标签页（Anime、Fantasy…） |
| `/characters/{id}` | 公开角色详情 SEO（需 moderation 策略） |
| `/help/billing` | 订阅/退款/取消 |

### 长期（180 天+）

| 建议 URL | 目的 |
|----------|------|
| `/blog/*` | 评测聚合、更新日志、创作者 spotlight |
| `/creators/program` | 创作者计划与分成政策 |
| 多语言 `/ja`、`/ko` | 语音已支持，落地页本地化 |

---

## 6. 子域权重策略建议

| 问题 | 现状 | 建议 |
|------|------|------|
| SEO 内容在 chat. 子域 | 对比表、FAQ 权重可能在子域 | 主域 mirror + canonical 指向主域 |
| Wiki 与产品割裂 | 深度文档在 aiwiki. | 主域 `/help` 摘要 + 链到 Wiki |
| 成人 SEO 链接在顶栏 | AI Porn Chat 等 | 保留但注意 SERP 品牌调性；配套合规页 |

---

*来源：手动访问 2026-06-17；[crushon.ai](https://crushon.ai/)、[chat.crushon.ai](https://chat.crushon.ai/)、[aiwiki.crushon.ai](https://aiwiki.crushon.ai/wiki/Main_Page)*
