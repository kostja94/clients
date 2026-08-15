# HeySoda 网站结构（推断）

> 关联：[heysoda.md](./heysoda.md) | [heysoda-features.md](./heysoda-features.md) | [heysoda-keywords.md](./heysoda-keywords.md) | [heysoda-competitors.md](./heysoda-competitors.md) | [heysoda-use-cases.md](./heysoda-use-cases.md) | [heysoda-growth-strategy.md](./heysoda-growth-strategy.md)

**说明**：以下基于 [heysoda.io](https://www.heysoda.io/) 首页与导航**可见**内容推断；**非**经爬虫验证的完整站点地图，路由变更后需更新。

---

## 一、导航与语言

| 项 | 说明 |
|----|------|
| 主 nav | Home · How to Use · **About Us** · **Real Feedback** · **Q&A** · **Contact** |
| 语言 | **Language** 入口（多语言/切换，具体语对应关系需线上确认） |
| 账户 | **Sign In**；主 CTA **Start for free** |

---

## 二、首页信息架构（逻辑块）

| 模块（顺序示意） | 内容 | 备注 |
|------------------|------|------|
| Hero / 品牌区 | 标题 *HeySoda - AI Social Connection Platform*、*Where Love and Ambition Grow Together*、轮播/示例「帖」、**Start for free**、SCROLL TO EXPLORE | 双行标题重复为页面抓取特征，可优化为单一 H1 利于 SEO |
| 3 steps | Tell us about YOU → AI Matching → AI Bot for icebreaking & ongoing convo | 适合 **HowTo** 简版或分步长图 |
| Why HeySoda | 多类示例卡：Cofounder / Buddy / Recruitment / Relationship / Investor + 「10000+ posts…」 | 可拆为**场景锚点** |
| What makes HeySoda pop | ① 理解人的连接的 AI ② AI Icebreaker | 与竞品区隔文案 |
| Real Feedback | 多条用户引述 + 简单身份标签 | 适合 `Review` 或精选引用模块 |
| Let the data talk | 匹配率、消息量相对「Leading Social App」的对比条 | 需脚注支撑 |
| Q&A 折叠 | How it works、Privacy、Pricing/是否收费 等 | FAQ schema 候选 |
| 小程序 | WeChat Mini Program **QR** | 转化华东/华语用户 |
| Footer | 品牌句 *One scan away from your perfect match*、**Privacy & Policy**、**Terms & Condition**、社媒：小红书、LinkedIn、X、小宇宙、© 2025 | 合规与外链 |

---

## 三、核心路径表（统一视口）

> 下表整合导航、URL 假设与 SEO 优先级，是日常维护的主引用表。

| 路径（待验证） | 用途 | 导航入口 | SEO 优先级 | 状态 | 备注 |
|---------------|------|----------|-----------|------|------|
| `/` | 英文首页（Hero + 3 Steps + 示例卡 + 数据区） | Home | P0 | 已上线 | 双行 H1 可优化为单一 H1 |
| `/how-to-use` 或等效 | How to Use（操作引导） | How to Use | P1 | 待确认 | 适合 HowTo 结构化数据 |
| `/about` 或等效 | About Us（品牌故事与团队） | About Us | P1 | 待确认 | — |
| `/feedback` 或等效 | Real Feedback（用户评价/案例） | Real Feedback | P1 | 待确认 | 可整合 Review 结构化数据 |
| `/q-a` 或 FAQ | Q&A（常见问题：隐私、收费、匹配原理） | Q&A | P1 | 待确认 | 建议扩展为 FAQPage schema |
| `/contact` | Contact（联系方式） | Contact | P2 | 待确认 | — |
| `/cofounder-matching` | 联合创始场景落地页 | 建议新增至 nav | P0 | **待建** | 与关键词 `AI cofounder matching` 承接 |
| `/relationship-matching` | 认真恋爱场景落地页 | 建议新增至 nav | P0 | **待建** | 与关键词 `serious relationship AI matching` 承接 |
| `/recruitment-matching` | 招聘场景落地页 | 建议新增至 nav | P0 | **待建** | — |
| `/investor-matching` | 投资对接场景落地页 | 建议新增 | P1 | **待建** | — |
| `/buddy-matching` | 活动搭子场景落地页 | 建议新增 | P1 | **待建** | — |
| `/blog/` | 对比文/教育文/用户故事 | 建议新增 Blog | P1 | **待建** | 承接长尾关键词与竞品对比搜索 |
| 微信小程序 | 中文用户扫码入口 | 首页 QR 码区 | P0 | 已上线 | 与英文站账号体系统一策略待确认 |

### 三-A、URL 与页面假设（原始推断，保留备查）

| 路径（待验证） | 可能用途 |
|----------------|----------|
| `/` | 英文首页 |
| `/how-to-use` 或等效 | How to Use |
| `/about` 或等效 | About Us |
| `/feedback` 或等效 | Real Feedback（或锚点区） |
| `/q-a` 或 FAQ | Q&A（或锚点区） |
| `/contact` | Contact |
| 微信域 | 小程序与 Web 的账号体系统一策略需产品确认 |

---

## 四、技术栈（未审计）

- 需通过 DevTools、Response header 或 `sitemap.xml` 确认框架。  
- 建议：**canonical**、核心页 **Open Graph / Twitter Card**、**WebSite** + **Organization** 类 JSON-LD（若品牌成熟）。

---

## 五、内容/SEO 优先级建议

| 优先级 | 动作 |
|--------|------|
| P0 | 每类场景（cofounder / hiring / relationship…）**独立可索引介绍** 或长滚动内锚点清晰 |
| P0 | Privacy / Terms 可爬、与小程序**同一政策版本**可追踪 |
| P1 | FAQ 扩展为 **FAQPage** 结构化数据 |
| P1 | 与 **Ditto** 等的对比内容：**维度化**、引用第三方数据时附来源 |
| P2 | 城市/时区/语言 landing（若全球化推进） |

---

*文档日期：2026-04-24（创建） · 2026-05-11（扩充：新增统一核心路径表 + 待建场景页规划）*
