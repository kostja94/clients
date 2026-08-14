# 2mv — 功能分析

> 2mv 为**双形态**产品：① 代运营机构（agency，五引擎闭环）；② 自研 SaaS「2mv Research Lab」（病毒内容研究工具）。本文件按两条产品线记录能力。站点结构见 [2mv-site-structure.md](./2mv-site-structure.md)。

---

## 1. 核心功能模块

### A. 代运营机构（五引擎闭环，来源：首页 `/`）

| 功能 | 描述（用户语言） | 差异化? | 对应页面 URL | 目标关键词 |
|------|-----------------|---------|-------------|-----------|
| **Watch（找信号）** | 24/7 监控 TikTok/Reels/Shorts 病毒视频，在爆火前发现真正在涨的内容 | ★ | `/`（首页五引擎区块） | find viral content before it peaks |
| **Decode（解码）** | 逐帧拆解每个病毒视频的 hook、节奏、结构、脚本、触发器，秒级还原「为什么火」 | ★ | `/` + `/research`（Viral Breakdown） | viral video breakdown, video decoder |
| **Architect（策划）** | 把解码出的模式转成围绕品牌与受众的高潜病毒选题 | ★ | `/`（Architect 区块） | viral content ideas, content strategy |
| **Produce（生产）** | 把选题变成平台原生短视频，第一帧就为表现而设计 | ★ | `/`（Produce 区块） | short-form content production |
| **Grow（复利增长）** | 播放量复利、粉丝增长、病毒爆款带动真实客户与品牌增长 | ★ | `/`（Grow 区块） | organic growth, viral marketing |

### B. 2mv Research Lab（SaaS，来源：`/research`）

| 功能 | 描述（用户语言） | 差异化? | 对应页面 URL | 目标关键词 |
|------|-----------------|---------|-------------|-----------|
| **Market Signals（市场信号）** | 每天监控 12,000+ 条病毒视频（TikTok/Reels/Shorts），覆盖 500+ 细分领域，实时呈现正在起量的信号 | ★ | `/research` | viral video finder, trend tracker |
| **Target Tracking（目标追踪）** | 追踪你关心的账号/竞品/创作者，实时呈现发帖表现、互动数据、增长轨迹、异军突起者 | ★ | `/research` | competitor tracking, creator analysis |
| **Viral Breakdown（病毒解码）** | 逐帧拆解病毒视频，还原公式、hook、结构、脚本、触发器 | ★ | `/research` | viral video decoder, hook analysis |
| **Content Patterns（内容模式）** | 把头部视频聚类为病毒模式，按竞争度与增长潜力排序 | ★ | `/research` | content patterns, viral patterns |
| **Viral Playbook（病毒手册）** | 把实时信号 + 解码 + 模式变成可直接执行的专属内容策略蓝图 | ★ | `/research` | viral playbook, content blueprint |

> 差异化标记 `★` 表示与竞品差异最大的能力（详见 [2mv-competitors.md](./2mv-competitors.md)）。核心差异化锚点：**「逐帧解码 + 模式聚类 + 复利闭环」三者合一**，而非单一的视频生成或表面数据看板。

---

## 2. 用户流程

**代运营（agency）路径**：

```
品牌方 → /book-a-demo 预约 → 需求沟通 → 进入五引擎循环
        Watch(找信号) → Decode(解码) → Architect(策划) → Produce(生产) → Grow(复利)
        ↓ 每一轮产出数据反哺下一轮（自迭代复利闭环）
```

**Research Lab（SaaS）路径**：

```
注册 → 免费额度试用 → 选择 niche（500+） → 发起研究
     → Market Signals（看趋势） → Target Tracking（盯账号） → Viral Breakdown（解码）
     → Content Patterns（聚类） → Viral Playbook（导出蓝图） → 按蓝图生产/发布
```

---

## 3. 技术指标

> 来源：`/research` 页自报数据，抓取日期 2026-08-13。均为官网口径，`⚠️ 待验证`（需第三方核验）。

| 指标 | 数值 | 口径 |
|------|------|------|
| 每日监控视频量 | 12,000+ videos / day | 跨 TikTok、Reels、Shorts |
| 监控细分领域 | 500+ niches | 官网列 35 个代表 niche |
| 生成有机播放量 | 100M+ organic views | 基于 2mv 模式生产的内容 |
| 节省研究时间 | 100 hrs / month | 替代人工 doomscroll |
| 广告支出减少 | -60% | 有机替代付费 |
| 研究提速 | 10x faster | research → content plan |
| 减少无效尝试 | -80% fewer wasted attempts | — |
| 实时追踪 | 12,847 videos tracked today | 首页 live 计数器（实时口径） |
| 服务客户 | 170+ brands & creators | /research 证言区声明 |

---

## 4. 定价

> 来源：`/research` 定价区块，抓取 2026-08-13。仅 Research Lab SaaS 有公开定价；代运营按结果报价（「Pay for the results」），未公开。

| 套餐 | 价格 | 额度 | 适用 |
|------|------|------|------|
| **Kick-Off** | $139/月 | 1,500 credits/mo | 起步：趋势概览、全谱数据、逐帧解码、拍摄指南、报告导出 |
| **Pro**（最受欢迎） | $399/月 | 5,000 credits/mo（3x） | 成长团队：+ 多账号追踪、团队协作、优先支持 |
| **Scale** | $999/月 | 15,000 credits/mo（10x） | 重度创作者/团队：+ 专属 1 对 1 支持 |
| **Custom** | 定制报价 | 自定义额度 | 专属客户经理、自定义集成 & API、定制工作流 |

- **年付**：20% off。
- **免费额度**：有 free credits（可先试用）。
- **支付**：Stripe。
- **代运营（agency）**：价格不公开，定位「Pay for the results（按结果付费）」，非按人头/工时计费——这是相对传统代理的核心定价差异。

---

## 5. 功能 ↔ 场景映射简表

> 场景与 Persona 完整定义见 [2mv-use-cases.md](./2mv-use-cases.md)，本表为摘要回填。

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Watch / Market Signals | 「帮我盯着赛道里什么在火」 | 增长/社媒负责人、创作者 |
| Decode / Viral Breakdown | 「这条为什么火？逐帧还原」 | 增长负责人、创作者、代理机构 |
| Architect / Viral Playbook | 「下个月我该拍什么选题」 | 品牌创始人、社媒负责人 |
| Produce | 「把选题变成能发的短视频」 | 品牌方（代运营）、创作者 |
| Target Tracking | 「竞品/对标账号最近在干嘛」 | 增长团队、代理机构 |
| Grow | 「播放量怎么变成真实客户」 | DTC 品牌、SaaS 创始人 |

---

> 关联：[主文档](./2mv.md) | [site-structure](./2mv-site-structure.md) | [use-cases](./2mv-use-cases.md) | [keywords](./2mv-keywords.md) | [competitors](./2mv-competitors.md) | [growth-strategy](./2mv-growth-strategy.md)

*Last updated: 2026-08-13*
