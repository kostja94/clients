# ARTIFIN 使用场景与用户故事

> **本文职责**：典型人物画像、JTBD、场景-功能-关键词映射、用户旅程、不适用边界。产品概览、功能、关键词、竞品详见各自子文档。面向海外市场，人物画像对齐国际投资者。
> 关联文档：[artifin.md](./artifin.md) | [artifin-features.md](./artifin-features.md) | [artifin-keywords.md](./artifin-keywords.md) | [artifin-competitors.md](./artifin-competitors.md) | [artifin-growth-strategy.md](./artifin-growth-strategy.md) | [artifin-site-structure.md](./artifin-site-structure.md) | [artifin-brand-visual.md](./artifin-brand-visual.md) | [README.md](./README.md)

---

## 1. 核心人物画像

### 人物 1：严肃的自驱型投资者（David）

| 属性 | 描述 |
|------|------|
| 标签 | David，42 岁，科技公司高管 |
| 所在地 | 旧金山湾区，美国 |
| 投资经验 | 8 年美股 + 部分国际市场 |
| 资产规模 | $20万-$200万可投资资产 |
| 痛点 | 信息过载 — 每天淹没在新闻、分析师报告和市场数据中；怀疑自己的确认偏误正在侵蚀收益；尝试过用 ChatGPT 做股票分析但回答肤浅或幻觉 |
| 目标 | 需要一个"AI 智囊团"，在大决策前不会只说他爱听的话 — 需要多角度论点验证 |
| 使用模式 | 每周 3-5 小时投资研究；任何 $1万以上仓位前使用 ARTI |

**JTBD**：
1. 准备进入新仓位时，从多个投资哲学角度验证我的论点
2. 持仓波动时，区分正常波动和基本面恶化
3. 发现新机会时，快速评估多维度风险收益

### 人物 2：进阶中的零售投资者（Sarah）

| 属性 | 描述 |
|------|------|
| 标签 | Sarah，29 岁，金融科技公司产品经理 |
| 所在地 | 伦敦，英国 |
| 投资经验 | 2 年，主要是 ETF 和少量个股（Robinhood / eToro） |
| 资产规模 | $1万-$5万 |
| 痛点 | 不会看资产负债表；容易被 Reddit/Twitter 热度左右；想超越"凭感觉投资"但觉得 Bloomberg Terminal 替代品太复杂 |
| 目标 | 一个值得信赖的 AI 工具，帮她理解一只股票"为什么"该买或不该买 — 不只是给个分数，而是能从中学习的解释 |
| 使用模式 | 通勤时每天使用 — 查看 ARTI 对 r/WallStreetBets 上热门股票或同事讨论的股票的看法 |

**JTBD**：
1. 当一只股票在社交媒体走红时，快速看懂看涨和看跌理由（通俗语言）
2. 看到社区推荐时，用对立视角交叉验证
3. 不知道买什么时，基于市场环境和风险偏好获得个性化建议

### 人物 3：专业投资组合经理（Michael）

| 属性 | 描述 |
|------|------|
| 标签 | Michael，38 岁，中型资管公司投资组合经理 |
| 所在地 | 新加坡 |
| 投资经验 | 12 年专业投资管理 |
| AUM | $5亿+ 亚太股票 |
| 痛点 | 投委会排期贵且慢；需要快速多角度第二意见作为提交投委会前的交叉验证；MAS 合规要求严格 |
| 目标 | 一个 AI 投委会，在每次投委会前预生成多维度初步分析，节省数小时人工研究并揭示盲点 |
| 使用模式 | 每天投委会前 — 对持仓和关注候选运行 ARTI；将输出作为团队讨论起点 |

**JTBD**：
1. 为晨间投委会准备时，快速生成所有持仓的预分析
2. 需要验证自己的投资假设时，获得来自对立哲学的结构化反驳
3. 向投委会汇报时，生成含牛熊证据的专业报告以供透明决策

---

## 2. 场景-功能-关键词映射

| 场景 | 使用功能 | 目标关键词 | 人物 |
|------|---------|-----------|------|
| 买入前多角度验证 | 圆桌辩论（7 位大师） | AI investment analysis、AI stock analysis | David、Sarah |
| 持仓监控 | 24/7 策略追踪 | AI portfolio analysis、quantitative analysis AI | David、Michael |
| 热门股票快速评估 | 圆桌 Demo | NVDA AI analysis、TSLA stock AI analysis | Sarah |
| 组合风险审计 | SFC 持牌风控、Thor（风控分析师） | AI risk management、licensed AI advisor | Michael |
| 发现新配置机会 | 智能资产匹配、Steve（行业轮动） | Japan ETF AI analysis、RWA investment AI | David、Michael |
| 财报季持仓审视 | Sam（财报）、Clint（基本面） | AI earnings call analysis、AI financial analyst | David、Michael |
| 投资方法论学习 | 大师页、Blog | Buffett AI、AI value investing | Sarah |
| Reddit/Twitter 热度交叉验证 | 红蓝对抗机制 | red team blue team investing、bull bear AI analysis | Sarah |

---

## 3. 典型用户旅程

### 旅程 1：首次用户 → 首次分析

```
1. 发现 → 通过 Google 搜索（"AI stock analysis tool"）、Reddit 讨论或金融科技媒体报道找到 ARTI
2. 着陆 → 访问 artifin.ai，阅读"七位传奇投资者辩论你的论点"
3. 上手 → 在 Demo 输入框中输入熟悉的股票代码（如 NVDA）
4. 体验 → 观看进度条：巴菲特 → 林奇 → 马克斯 → ... → 圆桌综合
5. 阅读 → 获得 7 位大师的独立分析 + 综合建议 + 风险报告
6. 决策 → 基于多角度分析做出更明智的投资决策
7. 留存触发 → 注册 24/7 策略追踪以接收持续监控
```

### 旅程 2：组合风险管理（日常活跃使用）

```
1. 盘前 → 打开 ARTI 查看持仓的策略追踪状态
2. 异常检测 → ARTI 推送"TSLA 策略底层前提可能正在变化"预警
3. 深入分析 → 点击查看受影响仓位的最新 7 位大师辩论
4. 风险评估 → 检查 Thor 的压力测试 + 圆桌综合仓位建议
5. 决策执行 → 基于综合建议调整仓位
```

---

## 4. 不适用边界

| 不适用场景 | 原因 | 替代方案 |
|-----------|------|---------|
| 自动下单执行 | ARTI 不自动交易 | Interactive Brokers、Robinhood |
| 高频/毫秒级交易 | ARTI 定位为决策支持，非执行层 | 量化平台（QuantConnect） |
| 纯技术分析/图表 | ARTI 价值在于深度分析，非图表 | TradingView、TrendSpider |
| 希望 AI 替自己做决定 | ARTI 是决策支持工具，非替代人类判断 | 不推荐 — 任何 AI 不应替代自主决策 |
| 非美/港/A 股资产 | 当前仅覆盖三个市场 | Bloomberg Terminal、AlphaSense |

---

## 5. 用户增长假设

| 假设 | 验证方法 | 优先级 |
|------|---------|--------|
| 严肃投资者更看重"多角度辩论"而非"快速回答" | 用户访谈 / NPS 调研 | P0 |
| 中级投资者（1-5 年经验）是最大增长细分 | 用户数据分析 | P0 |
| 投资大师 IP（巴菲特 AI、索罗斯 AI）是首要获客钩子 | 着陆页 A/B 测试 | P1 |
| 免费 Demo 是转化率最高的激活路径 | 漏斗分析 | P1 |
| Reddit/社区讨论是首要发现渠道 | 归因分析 | P1 |

---

*文档创建：2026-05-14 | 最后更新：2026-05-14（第二轮精炼） | 模式：Mode A 冷启动 — 国际版 → Mode C 增量精炼 | 人物画像：基于网站目标用户描述 + 市场研究推导*
