# NeoDrop

> 遵循 [客户文档规范](../../client-template.md)

**最近更新**：2026-05-22

---

## 文档导航

| 文档 | 职责 | 引用 |
|------|------|------|
| [neodrop.md](./neodrop.md)（本文） | 产品概览、ICP、文档索引 | — |
| [neodrop-site-structure.md](./neodrop-site-structure.md) | 站点结构：URL 层级、IA、技术栈 | [neodrop.md](./neodrop.md) |
| [neodrop-growth-strategy.md](./neodrop-growth-strategy.md) | 增长策略：渠道、实验、内容计划 | [neodrop-keywords.md](./neodrop-keywords.md)、[neodrop-site-structure.md](./neodrop-site-structure.md) |
| [neodrop-features.md](./neodrop-features.md) | 功能页：Channel Agent、多模态生成、Credits | [neodrop-use-cases.md](./neodrop-use-cases.md) |
| [neodrop-use-cases.md](./neodrop-use-cases.md) | 应用场景：Persona、Scenario、用户旅程 | [neodrop-features.md](./neodrop-features.md) |
| [neodrop-competitors.md](./neodrop-competitors.md) | 竞品分析、差异化 | [neodrop-features.md](./neodrop-features.md) |
| [neodrop-keywords.md](./neodrop-keywords.md) | 关键词映射、目标页、待办 | [neodrop-features.md](./neodrop-features.md)、[neodrop-use-cases.md](./neodrop-use-cases.md) |

*产品入口*：Web [neodrop.ai](https://neodrop.ai/) | 创建频道 [Create Channel](https://neodrop.ai/create/agent) | 定价 [Pricing](https://neodrop.ai/pricing)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C SaaS · **AI 个性化内容频道平台**（Personalized AI Content Channels） |
| 网站 | https://neodrop.ai/ |
| 当前阶段 | 早期增长（产品已上线，Discover 有活跃频道生态，订阅数个位数至十数位） |
| 核心产品 | 用户用自然语言描述想追踪的主题，**NeoDrop AI** 引导创建 **Channel**，多 Agent 团队持续采集、研究并生成 **Drop**（文章 / 图文 / 音频 / 音乐 / 视频），订阅者在 Feed 中消费 |
| 公司 | ⚠️ 待验证（官网未公开公司主体与团队信息） |
| 产品形态 | Web 应用（Feed + Discover + Channel 创建向导） |
| 关键差异化 | **「为你、由你、关于你」的频道式内容**——不是通用新闻聚合，而是用户定义兴趣后 AI **持续生产**多模态内容；官方示范频道（如 AI Agent 生态速报）展示 Deep Research 级长文质量 |
| Slogan | *The content about you, by you, for you* |
| 目标用户 | 信息过载的职场人、垂直兴趣订阅者、个人创作者、Side Hustle 学习者、小型内容团队 |
| 目标市场 | 全球（英文 UI 为主；示例频道含中文内容如「AI Agent 生态速报」） |
| 商业模式 | Freemium + Credits 订阅（Free / Starter $3.99 / Pro $20 / Studio $200） |
| 数据规模 | ⚠️ 待验证（Discover 可见频道订阅约 1–12，早期社区规模） |

---

## 1. 产品摘要

NeoDrop 是一个 AI 驱动的个性化内容频道平台。用户登录后描述自己关心的主题——例如「每周追踪 NVIDIA 新芯片」「旧金山公寓精选」「AI 创始人访谈摘要」——平台会通过对话式向导帮助创建 **Channel**，并由多 Agent 团队持续更新内容。

与 RSS 阅读器或 AI 新闻摘要工具不同，NeoDrop 的核心单位是 **Channel + Drop**：Channel 像一条专属内容生产线，Drop 是单次产出的内容单元，支持 **Article、Image Post、Podcast、Music、Video** 等多模态。用户可以在 **Discover** 浏览 Editor's Picks、Most Subscribed、Fastest Growth 等榜单并订阅他人频道，也可以在 **Feed** 查看已订阅频道的更新。

平台采用 **Credits** 计费：注册送 2,000 credits，每日签到 +200（每月最多 7 次）；付费档从 Starter（$3.99/月，2,000 credits）到 Studio（$200/月，100,000 credits + 首月 bonus）。Pro 档提供 Priority 队列、Deep Research / Wide Research 与 Beta 功能优先体验。

官方频道（NeoDrop Official）已展示较高内容质量，例如「AI Agent 生态速报」类长文含 Research Brief、多源引用与结构化章节——说明产品定位偏向 **AI-native 内容生产 + 个性化订阅**，而非简单链接聚合。

*完整功能线见 [neodrop-features.md](./neodrop-features.md)。*

---

## 2. 定位要点

| 维度 | 说明 |
|------|------|
| **品类标签** | *AI content channel*、*personalized AI feed*、*AI newsletter generator*、*multimodal content agent* |
| **差异锚点** | **Channel 即产品**——用户定义兴趣 → AI 持续产出而非一次性生成；**多模态 Drop**（文/图/音/视频）；**Discover 生态**——可订阅他人频道，兼具消费与创作；**Credits + Multi-agent** 透明计费与产能队列 |
| **竞品三圈** | **① 直接竞品**：Yournalist、Perceptive.news、Particle、CondenseIt/Horizon（自托管 digest）。**② 横向挤压**：Google 信息代理、A01、Perplexity Discover、Feedly Leo、Substack/Beehiiv 定制 Newsletter、Neural Draft/Dropapost（偏发布自动化）。**③ 替代方案**：手动 RSS + ChatGPT 摘要、n8n 工作流模板。详见 [neodrop-competitors.md](./neodrop-competitors.md) |
| **地缘策略** | 英文主站 + 美元定价（Waffo 支付）；内容语言可随 Channel 主题变化（已有中文 AI 资讯类 Drop） |
| **信任信号** | 官方高质量示范频道、结构化 Research Brief、FAQ 说明 credits 计算；⚠️ 缺少公开团队、案例数据与第三方评测 |

---

## 3. ICP（简版）

- **信息过载的职场人**：需要 AI/科技/投资等垂直资讯但不想刷 Twitter/X 或 10 个 Newsletter；核心诉求是「一条 Feed 搞定我的主题」。
- **垂直兴趣订阅者**：追剧集上线、半导体周报、SEO 踩坑指南等窄主题；愿意订阅他人 Channel 或自建。
- **个人创作者 / Solo Publisher**：想维持一个主题栏目但缺写作产能；用 Channel Agent 持续产出 Drop。
- **Side Hustle 学习者**：Discover 中 Side Hustle 分类频道；用 AI 追踪副业、Deals 等主题。
- **小型内容团队 / MCN**：Studio 档高 credits + 最高优先级队列；多 Channel 矩阵运营。

*展开见 [neodrop-use-cases.md](./neodrop-use-cases.md)。*

---

## 4. 关键词与竞品（入口）

- [neodrop-keywords.md](./neodrop-keywords.md)
- [neodrop-competitors.md](./neodrop-competitors.md)

## 5. 站点结构与增长策略（入口）

- [neodrop-site-structure.md](./neodrop-site-structure.md)
- [neodrop-growth-strategy.md](./neodrop-growth-strategy.md)

---

## 6. 网络检索补充（非官网原文，供策略参考）

| 补充项 | 说明 | 来源 |
|--------|------|------|
| **定价详情** | Free：注册 2,000 + 每日签到 200（月限 7 次）；Starter $3.99/2,000 credits；Pro $20/10,000 + 首月 5,000 bonus；Studio $200/100,000 + 首月 62,500 bonus | [neodrop.ai/pricing](https://neodrop.ai/pricing)，2026-05-22 |
| **Discover 生态** | Editor's Picks、Most Subscribed（如 Daily AI R&B 12 subs）、Fastest Growth、Newly Created；分类含 AI、Side Hustle、Finance 等 | [neodrop.ai/discover](https://neodrop.ai/discover)，2026-05-22 |
| **内容质量样例** | 「AI Agent 生态速报」含 21 条核心信号、Research Brief、多源链接——接近专业 Newsletter 水准 | [neodrop.ai/feed/DT3KQuWFM0R](https://neodrop.ai/feed/DT3KQuWFM0R)，2026-05-22 |
| **品类 adjacent** | Yournalist（waitlist）、Perceptive.news（自选源 + AI 打分）、CondenseIt/Horizon（自托管 digest）占据「个性化资讯」相邻位；Google 信息代理、A01 为「个人信息 Agent / 监控 + 通知」赛道 | 联网检索，2026-05-22 |

---

*Demo 文档包 · NeoDrop · https://neodrop.ai/*
