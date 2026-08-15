# NeoDrop — 功能

> 遵循 [客户文档规范](../../client-template.md)
> **本文档职责**：核心能力、产品模块、Credits 与技术指标。  
> **引用**：[neodrop.md](./neodrop.md) 概览 | [neodrop-use-cases.md](./neodrop-use-cases.md) 场景 | [neodrop-keywords.md](./neodrop-keywords.md) 关键词

**最近更新**：2026-05-22

---

## 一、产品矩阵

| 模块 | 形态 | 受众 | 说明 |
|------|------|------|------|
| **Channel Agent** | 对话式创建向导 | 创作者 / 订阅者 | 描述兴趣 → AI 分步引导创建 Channel |
| **Drop 生成** | 多模态内容单元 | 全体用户 | 文章、图文帖、播客、音乐、视频 |
| **Feed** | 个性化订阅流 | 订阅者 | Subscribed / Recommended / Activity |
| **Discover** | 频道市场 | 全体用户 | 发现、订阅、按分类浏览 |
| **Credits 系统** | 计量与订阅 | 付费用户 | 按生成消耗 credits，分档队列优先级 |

---

## 二、核心用户流程

```
登录 / 注册
  → 描述兴趣（Create Channel）
    → Channel Agent 引导配置
      → 多 Agent 采集 + 研究 + 生成 Drop
        → 订阅者 Feed 推送 / Discover 公开展示
          → 持续更新（按 Channel 节奏）
```

---

## 三、Channel Agent（频道创建）

| 能力 | 说明 | 对外表达 |
|------|------|----------|
| **自然语言意图** | 用户描述想追踪的主题、受众、风格 | *Tell NeoDrop AI what you want to follow* |
| **分步向导** | 登录后对话式完成 Channel 配置 | *Create your own channel* |
| **持续更新** | Channel 非一次性生成，而是持续产出 Drop | *Continuously updated channel* |
| **公开展示** | Channel 可出现在 Discover 榜单 | *Subscribe* / 订阅数、Drop 数展示 |

*来源：[neodrop.ai/create/agent](https://neodrop.ai/create/agent)、[neodrop.ai/discover](https://neodrop.ai/discover)，2026-05-22*

---

## 四、Drop 多模态生成

| 模态 | Discover 筛选标签 | 典型用途 |
|------|-------------------|----------|
| **Article** | Article | 深度资讯、Research Brief、周报 |
| **Image Post** | Image Post | 图文摘要、信息图风格帖 |
| **Podcast** | Podcast | 音频简报、对话式摘要 |
| **Music** | Music | 主题音乐创作（如 Daily AI R&B） |
| **Video** | Video | 短视频、可视化内容 |

### 研究深度能力（Pro+）

| 能力 | 说明 | 可用档位 |
|------|------|----------|
| **Deep Research** | 长文深度调研，多源引用 | Pro、Studio |
| **Wide Research** | 更广来源覆盖 | Pro、Studio |
| **标准队列** | 常规定时生成 | Free、Starter |
| **Priority 队列** | 优先生成 | Pro |
| **Highest-priority** | 最高并发与优先级 | Studio |

*来源：[neodrop.ai/pricing](https://neodrop.ai/pricing)，2026-05-22*

---

## 五、Feed 与 Discover

### Feed

| 区块 | 说明 |
|------|------|
| **Subscribed** | 已订阅 Channel 的 Drop 更新 |
| **Recommended** | 推荐内容（需先 Follow 部分 Channel） |
| **Activity** | 用户活动相关动态 |

空状态引导：*No recommendations yet. Head to Discover and follow a few channels.*

### Discover 榜单

| 榜单 | 说明 |
|------|------|
| **Editor's Picks** | 编辑精选（含 NeoDrop Official 示范频道） |
| **Most Subscribed** | 按订阅数排序 |
| **Fastest Growth** | 近期增长最快 |
| **Newly Created** | 最新创建 |

### 内容分类（Channel 标签）

Side Hustle · Deals & Savings · AI · Technology · Business · Finance · Investing · Science · Health & Wellness · Lifestyle · Culture · Sports · Local News · Other

---

## 六、Credits 与定价

| 档位 | 月费 | Credits | 核心权益 |
|------|------|---------|----------|
| **Free** | $0 | 注册 2,000 + 每日签到 200（月限 7 次） | 全模态试用、Community support |
| **Starter** | $3.99 | 2,000/月 | 单 Channel 稳定更新（约 10–15 Drop/月） |
| **Pro** | $20 | 10,000/月 + 首月 5,000 bonus | 多 Channel、Priority 队列、Deep/Wide Research、Beta |
| **Studio** | $200 | 100,000/月 + 首月 62,500 bonus | 团队/MCN 级产能、最高优先级、Early access 新模型 |

### Credits 消耗参考

| 内容类型 | 预估消耗 | 说明 |
|----------|----------|------|
| 短篇 Drop | ~1,000–2,000 credits | FAQ 典型值 |
| 长文 Deep Research | 更高 | 取决于模型调用、研究深度、媒体合成 |
| 实时展示 | 生成过程中 live 显示 | 透明计费 |

*规则：月 credits 不 rollover；Pro/Studio 首月 bonus 在订阅期内有效。支付：Waffo（Visa/Mastercard/Amex）。*

---

## 七、差异化能力条目

| # | 能力 | 与竞品差异 |
|---|------|------------|
| 1 | **Channel 持续生产** | 非一次性 Newsletter，而是长期运行的内容线 |
| 2 | **多模态 Drop** | 同一 Channel 可产出文/图/音/视频/音乐 |
| 3 | **Multi-agent 团队** | 定价页强调 *multi-agent team* 分工生产 |
| 4 | **Discover 双边市场** | 消费他人 Channel + 创建自己的 Channel |
| 5 | **Deep / Wide Research** | Pro 档深度调研，官方 Drop 质量可对标专业 Newsletter |
| 6 | **低门槛 Starter** | $3.99 入门，低于多数 AI 写作/资讯 SaaS |
| 7 | **Credits 透明** | 生成过程 live 显示消耗，FAQ 说明计算逻辑 |

---

## 八、技术指标（推断 + 待验证）

| 指标 | 值/说明 | 状态 |
|------|---------|------|
| 支持模态 | 5 种（Article / Image / Podcast / Music / Video） | 已确认 |
| 支付 | Waffo 国际信用卡 | 已确认 |
| 认证 | `/auth` 登录注册 | 已确认 |
| API / MCP | 未公开 | ⚠️ 待验证 |
| 移动端 App | 未见 | ⚠️ 待验证 |
| SSO / Enterprise | Studio + 反馈渠道洽谈 | 定价页 FAQ |

---

*文档创建日期：2026-05-22 | 模式：冷启动*
