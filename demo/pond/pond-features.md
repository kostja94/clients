# Pond — 功能分析

> 功能描述使用用户语言。`★` 标记与竞品差异最大的功能。URL 取自 [pond-site-structure.md](./pond-site-structure.md)。

---

## 1. 核心功能模块

| 功能 | 描述（用户语言） | 差异化? | 对应页面 URL | 目标关键词 |
|------|-----------------|---------|-------------|-----------|
| ★ Pond Tasks / Bounties | 任务市场：你发一个任务和奖励，全球的人类和 AI agent 竞争交付，你只验收通过的结果并付款——"you only pay for results" | ★ | `/tasks` | ai task marketplace |
| ★ AI 辅助任务创建（Pond AI） | 描述需求或选示例任务，AI 帮你把模糊需求整理成可发布的任务 | ★ | `/` | create a task |
| ★ 三种 Agent 交付模式 | Individual（单个专家 agent）、Collaboration（agent 团队协作）、Competition（多个 agent 竞争，只付胜者） | ★ | `/` | ai agent delivery |
| ★ 人类 + AI Agent 同场竞争 | 平台同时接受真人贡献者与 AI agent 提交同一任务（官网：Humans and AI agents are welcome） | ★ | `/tasks` | humans and ai agents |
| Agent 目录 | 已上架 agent 展示（评级、用户数、运行次数），"Building an agent? Connect your agent and distribute on Pond" | — | `/` | ai agents marketplace |
| ★ Discoveries（build in public） | 创业公司公开展示增长：收入、MRR、MAU、用户数，并核验数据（Stripe API + Google Analytics），有 Top Revenue / Top MRR / Hottest 排行榜 | ★ | `/discoveries` | build in public |
| ★ Markets（融资） | 融资市场：SAFE、token warrant、stablecoin 募资；资金进 Pond Vault 按月释放，投资者可撤资，3 个月未达成全额返还 | ★ | `/markets` | startup fundraising platform |
| Points 积分 | 每日刷新积分任务，用户做任务攒积分 | — | `/points` | pond points |
| Referral 推荐系统 | 把联系人/网络转化为机会的推荐机制 | — | docs（pond-referral-system） | pond referral |
| 钱包与支付 | 奖励以法币或 USDC 等 stablecoin 发放；Markets 投资资金托管在 Pond Vault | — | `/markets` | — |
| Portfolio | 用户的投资组合与活动记录区 | — | `/portfolio` | pond portfolio |

---

## 2. 用户流程

### 2.1 发布者（Startup 创始人）流程

```
注册并登录（推荐使用常用邮箱）
  → 描述需求（或选示例：Generate Sales Leads / Get Product Feedback / Test & Find Bugs / Recruit Talent / Content Creation）
  → AI 辅助生成任务 + 设定奖励包（推荐 base $10/用户，$20 标准；可自定义）
  → 发布到 /tasks
  → 全球贡献者（人类 + AI agent）提交
  → 逐条审核提交，只验收达标的
  → 仅对通过的结果付款（来源：docs/pond-bounties-faqs）
```

### 2.2 贡献者（用户 / AI Agent）流程

```
浏览 /tasks（Newest / Hottest 排序，My Applications 追踪申请）
  → 选择任务并提交真实工作/反馈/输出
  → 通过审核后获得奖励（法币或 USDC）
  → 攒 Points、积累 Portfolio 记录
```

### 2.3 投资者 / 市场参与者流程

```
浏览 /markets（Create Round / 投资者名录 / Active & Planning 轮次）
  → 评估项目（结合 Discoveries 的透明数据）
  → 通过 SAFE / token warrant 参与
  → 轮次关闭后资金由 Pond Vault 按月释放（前提：创始人上传月度更新或办 AMA）
  → 轮次关闭前可随时撤资；未达成目标（≤3 个月）全额返还
```

---

## 3. 技术指标 / 可量化声明

| 指标 | 数值 | 来源 + 日期 |
|------|------|------------|
| 平台用户数（首页宣称） | 252,317 Users、181 Countries、20 Agents at Work、34 Tasks Completed、$30,715 Paid Out | 首页 2026-08-12 `⚠️ 该组数字与任务页/案例规模存在明显量级矛盾（见 §5 待验证）` |
| 活跃贡献者（Bounties 文档宣称） | "tens of thousands of active users" | docs/pond-bounties-faqs 2026-08-12 |
| Bounty 参与度 | "Every bounty launched on Pond has hit 3x the expected participation" | docs/pond-bounties-faqs 2026-08-12 |
| Moatt 案例 | 1 周 245 人注册、99 份带证据的产品测试提交、仅 35 份通过验证并付款 | 首页 Meet Pond 区块 2026-08-12 |
| PhotoBase 案例 | 2,300 人参与（工程师/设计师/消费者）、157 份真实录屏、50 人获得报酬 | 首页 Meet Pond 区块 2026-08-12 |
| Pond 自身 Discoveries 数据 | Total Revenue $204.6k（+469%）、MRR $1.1k、MAU 18.1k、Total Users 77.3k | `/discoveries` 2026-08-12 |
| 已验证投资方 | Seed $7.5M：Archetype、Coinbase Ventures、Delphi Ventures、cyberFund、NEAR Foundation、Anagram + 30+ 天使 | 官网 Backed by the Best + 第三方融资库 2026-08 |

---

## 4. 定价

| 维度 | 内容 | 来源 |
|------|------|------|
| 平台基础 | Freemium——核心功能（Discoveries 列表、Markets、Bounties 参与）免费开放 | needaiforthis.com / stork.ai 评测 2026；平台无付费墙 |
| Bounty 发布价格 | 由发布者自定义：奖励 = 计划奖励的提交数 × 每份价值；推荐 base $10/用户，$20 为最佳效果标准；复杂任务更高 | docs/pond-bounties-faqs 2026-08-12 |
| 高级/企业套餐 | 未公开定价，需联系团队（加速器/VC 网络有定制方案） | needaiforthis.com 2026 |
| Markets 佣金/费率 | 未公开；SAFE 无投票权、无治理权（官方 FAQ 强调） | `/markets` FAQ 2026-08-12 `⚠️ 待验证：平台抽佣比例` |

---

## 5. 待验证项

- `⚠️ 待验证` 首页平台数据（252,317 用户等）与任务页/案例披露规模的矛盾——可能为营销演示数字或统计口径不同（如"Tasks Completed"仅统计已验证付款的完成任务）
- `⚠️ 待验证` 平台抽佣比例（任务发布侧与 Markets 融资侧）
- `⚠️ 待验证` 提现方式与到账时效（docs 提及 Pond wallet / 指定钱包分发）
- `⚠️ 待验证` 任务详情页 URL 模式

---

## 6. 功能 ↔ 场景映射简表

> 完整场景与 Persona 见 [pond-use-cases.md](./pond-use-cases.md)。

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Bounties | "帮我的项目快速拿到真实用户反馈" | Startup 创始人 |
| Bounties | "想用 AI 赚点零花钱" | 贡献者（人类/AI Agent） |
| AI 辅助任务创建 | "我不会写任务描述，帮我生成" | 新手创始人 |
| Discoveries | "让投资人看到我们的增长数据" | Startup 创始人 |
| Markets | "融一笔钱，还要有退出通道" | Startup 创始人 / 投资者 |
| Points | "每天刷点小任务攒积分" | 贡献者 |
| Referral | "把认识的人变成我的用户/投资人" | Startup 创始人 |

---

> 关联：[主文档](./pond.md) | [site-structure](./pond-site-structure.md) | [use-cases](./pond-use-cases.md) | [keywords](./pond-keywords.md) | [competitors](./pond-competitors.md) | [growth-strategy](./pond-growth-strategy.md) | [others](./pond-others.md)

*Last updated: 2026-08-12*
