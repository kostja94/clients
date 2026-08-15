# Yoyo Market 功能与产品能力

> **本文档职责**：产品**能做什么**、模块、费用、技术数据源；情境见 [yoyomarket-use-cases.md](./yoyomarket-use-cases.md)。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[yoyomarket.md](./yoyomarket.md) | [yoyomarket-keywords.md](./yoyomarket-keywords.md) | [yoyomarket-competitors.md](./yoyomarket-competitors.md)

**Last updated**: 2026-06-04 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [yoyomarket.md](./yoyomarket.md) |
| 关键词 | [yoyomarket-keywords.md](./yoyomarket-keywords.md) |
| 使用场景 | [yoyomarket-use-cases.md](./yoyomarket-use-cases.md) |
| 竞品 | [yoyomarket-competitors.md](./yoyomarket-competitors.md) |
| 网站结构 | [yoyomarket-site-structure.md](./yoyomarket-site-structure.md) |
| 增长策略 | [yoyomarket-growth-strategy.md](./yoyomarket-growth-strategy.md) |

---

## 一、功能概览与建议 URL

| 产品线 | 建议 URL | 目标关键词（示例） |
|--------|----------|-------------------|
| **Prediction Pools** | /features/pools | crypto prediction pool, bet on btc price |
| **1v1 PvP** | /features/pvp | pvp prediction market, 1v1 crypto bet |
| **Telegram App** | /features/telegram | telegram prediction market bot |
| **Wallet & Onboarding** | /how-it-works | how to use yoyo market, telegram crypto wallet |
| **Price Feeds** | /features/data | chainlink price prediction, dexscreener odds |
| **YOYO Token** | /token | yoyo token staking, prediction market token |
| **Yoyonians NFT** | /nft | yoyonians nft, reduced prediction fees |

*当前线上以 Bot + GitBook 为主；上表为 **SEO 落地草案**。*

---

## 二、核心用户流程（Beta 文档，2023-11）

```
Telegram → /start → /create 钱包 → 复制地址 → 充值 ETH（Arbitrum）→ 打开 Mini App → 创建/加入 Pool → 结算
```

| 步骤 | 说明 | 风险/提示 |
|------|------|-----------|
| 启动 Bot | [t.me/yoyo_market_bot](https://t.me/yoyo_market_bot) | 仅官方链接，防钓鱼 |
| 创建钱包 | `/create` 应用内钱包 | 用户需理解自托管/密钥责任（**待验证** 托管模型） |
| 入金 | **仅 Arbitrum ETH** | 跨链误充资产损失 |
| 下注 | Pools 为主 | 部分交易对结算慢（最长约 1 天，Beta 文档） |

---

## 三、差异化能力（≥5 条）

| # | 能力 | 用户价值 | 对外表达簇 |
|---|------|----------|------------|
| 1 | **Telegram Mini App** | 在熟悉 IM 内完成全流程 | *Predict in Telegram, not another exchange UI* |
| 2 | **Prediction Pools** | 与社群一起押方向，社交感强 | *Pool your conviction on BTC/ETH/…* |
| 3 | **双数据源** | Chainlink（快、准）+ Dexscreener（覆盖广） | *Major coins via Chainlink, long tail via DEX liquidity* |
| 4 | **PvP 架构** | 用户对用户，非仅做市商对手盘 | *Player-vs-player, not house odds* |
| 5 | **低点击下注** | 几次点击完成 | *Few taps to place a prediction* |
| 6 | **Yoyonians 权益** | 早期用户降费、早鸟功能 | *NFT for fee discounts & early access* |
| 7 | **白标合作**（待验证） | 其他项目可嵌 Telegram 预测 | *Whitelabel prediction mini app for your community* |

---

## 四、交易形态详解

### 4.1 Prediction Pools（已上线）

- 多参与者对**同一价格方向/区间**押注的池化合约（表述来源：Medium Beta）。
- Beta 策略：**先 Pools 后 1v1**，降低双合约并行排障成本。
- 结算：依赖预言机/价格源；部分 Dex 币对 **结算周期可达 ~1 天**。

### 4.2 1v1 PvP（计划）

- 与 Pools 合约「近乎相同」，分阶段发布（Medium Beta）。
- 适合：**明确对手盘**、网红/社群挑战叙事。

### 4.3 支持的市场类型（Beta）

以 **加密货币价格** 为主；预批准 Chainlink 对示例：

BTC/USD, ETH/USD, SOL/USD, ARB/USD, LINK/USD, DOGE/USD, OP/USD, GMX/USD 等（共 28+ 对，见 Medium Beta 列表）。

**Dexscreener 路径**：Uniswap V2/V3 与 WETH 配对、流动性 ≥ **$200,000**（Beta 阈值，可能调整）。

---

## 五、费用与经济学

| 费用类型 | 金额/比例 | 说明 |
|----------|-----------|------|
| Gas | 用户承担 | Arbitrum 网络 |
| 创建池 | **0.002 ETH** 固定 | 覆盖后台 gas（Beta） |
| 平台佣金 | **5%** of pool/PvP size | 入 treasury |
| NFT 持有 | 降费（幅度 **待验证**） | Yoyonians 效用 |

**Revenue sharing**：官方称探索中，需注意各法域证券/博彩法规（Medium Beta）。

---

## 六、技术指标与依赖（公开信息）

| 组件 | 技术 | 备注 |
|------|------|------|
| 链 | Arbitrum | Beta 入金网络 |
| 价格 — 主流币 | Chainlink Aggregated Feeds | 后端预批准列表 |
| 价格 — 长尾 | Dexscreener API | 任意 Uni V2/V3 + WETH 对 |
| 前端 | Telegram Web App | 主入口 |
| 文档 | GitBook | 操作与 tokenomics |

---

## 七、功能 ↔ 关键词承接

| 功能模块 | 用户口语 | 主承接载体 |
|----------|----------|------------|
| Pools | bet on eth price telegram | /features/pools + Bot CTA |
| Telegram | prediction market bot | /features/telegram |
| PvP | challenge friend crypto bet | /features/pvp |
| Token | yoyo staking | /token |
| NFT | lower fees prediction | /nft |

*词表详述* → [yoyomarket-keywords.md](./yoyomarket-keywords.md)

---

*来源： [GitBook Welcome](https://yoyo-market.gitbook.io/yoyo-market-documentation)、[Medium Beta Release 2023-11-03](https://medium.com/@yoyomarket/yoyo-market-beta-release-fb72b2023056)*
