# Yoyo Market

> 遵循 [客户文档规范](../../client-template.md) | 基于 [yoyomarket.com](https://yoyomarket.com/)（**复核 2026-06-04**）

**Last updated**: 2026-06-04

---

## 文档体系（六主文档）

| 文档 | 职责 | 引用 |
|------|------|------|
| **yoyomarket.md**（本文） | 产品概览、定位、ICP、摘要 | 详述见各专项 |
| [yoyomarket-features.md](./yoyomarket-features.md) | 功能、交易形态、费用与链上能力 | keywords、use-cases |
| [yoyomarket-use-cases.md](./yoyomarket-use-cases.md) | Persona、情境、/for/* 规划 | features |
| [yoyomarket-keywords.md](./yoyomarket-keywords.md) | 关键词、目标页、承接载体 | site-structure |
| [yoyomarket-competitors.md](./yoyomarket-competitors.md) | 竞品矩阵、差异化、合规风险 | features |
| [yoyomarket-site-structure.md](./yoyomarket-site-structure.md) | URL、IA、分阶段落地 | keywords、growth-strategy |
| [yoyomarket-growth-strategy.md](./yoyomarket-growth-strategy.md) | 渠道、内容战役、实验 | keywords、site-structure |

**原则**：每条重要信息**一处详述**、他处摘要 + 链接。

*产品入口*：Web [yoyomarket.com](https://yoyomarket.com/) | Telegram Bot [yoyo_market_bot](https://t.me/yoyo_market_bot) | 文档 [GitBook](https://yoyo-market.gitbook.io/yoyo-market-documentation)

---

## 1. 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C / Web3 / **预测市场（Prediction Market）** / Telegram Mini App |
| 网站 | https://yoyomarket.com/ |
| 备用域名 | https://www.yoyomarket.io（文档站引用，**待验证**是否与主站同一运营主体） |
| 当前阶段 | 增长期（2023-11 Beta 上线 Telegram；Web App 文档标注 Coming soon） |
| 核心产品 | **Yoyo Market**：面向 Telegram 与加密用户的 **PvP 预测市场**——以少量点击完成价格/事件方向押注，强调简单、有趣、社交化 |
| Slogan | **亞洲自己的預測市場**（官网 title，2026-06-04） |
| 目标市场 | **亚洲**加密与 Telegram 用户为主；英文/中文社区并存（来源：官网 + [GitBook](https://yoyo-market.gitbook.io/yoyo-market-documentation)、[Medium Beta](https://medium.com/@yoyomarket/yoyo-market-beta-release-fb72b2023056)） |
| 产品形态 | **Telegram Mini App / Bot**（主交付）；**Web App**（规划中）；原生代币 **YOYO**（费用、质押、治理，来源：[Coinbase 资产页](https://www.coinbase.com/price/yoyo-market)） |
| 关键差异化 | **Telegram 原生 + PvP/池化押注** vs 全球 CLOB 型平台（Polymarket/Kalshi）；**亚洲叙事** vs 欧美监管与合规中心 |
| 更新日期 | 2026-06-04 |

### 能力与边界（Scope）

| 维度 | 说明 |
|------|------|
| **提供** | 链上/应用内预测池、价格方向类市场（Beta 以 **Pools** 为先）；Telegram 内钱包创建与下注流程 |
| **不提供** | 持牌经纪/证券投顾；**非**对全球所有司法辖区的合规承诺（亚洲各地对预测/博彩监管差异大，见 competitors §合规） |
| **链与资产** | Beta 文档：**Arbitrum 上 ETH** 入金；支持 Chainlink 预批准币对与 Dexscreener 泛化币对（**待验证** 当前主网是否仍为 Arbitrum） |

### 商业摘要

- **平台费**：池/PvP 规模的 **5%** 佣金；创建池固定 **0.002 ETH**（来源：Medium Beta，2023-11）
- **代币**：YOYO 用于生态费用、质押与治理（细节见 GitBook Tokenomics，**待验证** 2026 状态）
- **NFT**：The Yoyonians——早期用户 $150 交易量可领，含降费与早鸟功能（来源：Medium Beta）

*功能与费用详表* → [yoyomarket-features.md](./yoyomarket-features.md)

---

## 2. 产品定位

### 产品摘要

**Yoyo Market** 是 **玩家对玩家（PvP）预测市场**，让 **Telegram 用户** 以极简交互参与对加密货币价格等结果的押注。官方定位强调 **simplified, fun and engaging**，与 Polymarket 等「事件合约 + 订单簿」的全球平台形成区隔：更偏 **社交 + 链上小游戏化**，而非宏观政治/经济大盘。

### 一句话定位

> **亚洲视角的 Telegram 原生预测市场**——用几次点击完成押注，把预测市场带给 crypto degens 与社群用户。

（英文档可写：*Asia's prediction market on Telegram — PvP pools in a few taps.*）

### 核心价值主张

| 主张 | 说明 |
|------|------|
| **Telegram-First** | Bot + Mini App，无需单独下载大型交易客户端 |
| **PvP / Pools** | 用户与用户对赌（池化先上线，1v1 PvP 文档称后续推出） |
| **低门槛交互** | `/start` → `/create` 钱包 → 充值 → 点 App 开玩（Beta 流程） |
| **多币对覆盖** | Chainlink 主流币 + Dexscreener 扩展（流动性门槛 $200k，Beta 文档） |
| **亚洲叙事** | 官网中文 Slogan；与全球平台「默认欧美事件」形成心智差异 |

*Persona 与场景* → [yoyomarket-use-cases.md](./yoyomarket-use-cases.md)

---

## 3. 目标受众 / ICP

- **Telegram 加密社群用户**：习惯 Bot、Mini App、链上小额实验
- **DeFi / Degen 交易者**：对价格短期方向有观点，愿在池子里表达
- **预测市场尝鲜者**：觉得 Polymarket/Kalshi 开户或法币路径太重
- **亚洲时区活跃散户**：偏好本地语言社群与「亚洲自己的市场」叙事
- **合作方生态**（B2B2C）：文档提及可为其他项目做 **Telegram 白标预测应用**（如与 dApp 合作，来源：X @yoyomarket_io 帖文，**待验证**）

---

## 4. 核心产品线（摘要）

| 模块 | 状态（文档口径） | 说明 |
|------|------------------|------|
| **Prediction Pools** | Beta 已上线 | 多用户池化押注；部分币对结算可达 ~1 天 |
| **1v1 PvP** | 计划推出 | 与 Pools 合约相近，分阶段降风险 |
| **Telegram Bot / Mini App** | 主入口 | [t.me/yoyo_market_bot](https://t.me/yoyo_market_bot) |
| **Web App** | Coming soon | GitBook 2024-04 |
| **YOYO Token** | 生态代币 | 费用、质押、治理 |
| **Yoyonians NFT** | 早期激励 | 降费、新功能早鸟 |

*完整能力表* → [yoyomarket-features.md](./yoyomarket-features.md)

---

## 5. 关键词摘要

| 类型 | 示例 |
|------|------|
| **品牌** | Yoyo Market, yoyomarket, YOYO token |
| **Primary** | prediction market, crypto prediction market, telegram prediction market |
| **Secondary** | PvP prediction market, price prediction pool, bet on crypto price |
| **Long-tail** | telegram bot crypto betting, polymarket alternative telegram, asia prediction market |
| **中文** | 預測市場、加密预测市场、电报 预测 |

*完整映射* → [yoyomarket-keywords.md](./yoyomarket-keywords.md)

---

## 6. 竞品摘要

- **全球交易型**：Polymarket、Kalshi、Opinion、PredictIt
- **社区/趣味型**：Manifold、Metaculus（偏预测准确度社区）
- **渠道差异**：Telegram 内同类 Bot/小游戏（**待验证** 具体名单）

**差异化（一句）**：Yoyo Market = **Telegram + PvP 池 + 亚洲品牌**，而非全球政治事件 CLOB。

*矩阵与合规对比* → [yoyomarket-competitors.md](./yoyomarket-competitors.md)

---

## 7. 网站结构（摘要）

| 路径/触点 | 说明 |
|-----------|------|
| https://yoyomarket.com/ | 品牌落地（当前抓取仅 title，**待验证** 完整 IA） |
| GitBook | 产品与操作文档 |
| Telegram Bot / 社群 | 转化主路径 |
| Medium / X | 发布与生态合作 |

*分阶段 URL 规划* → [yoyomarket-site-structure.md](./yoyomarket-site-structure.md)

---

## 8. 内容营销（摘要）

- **教育**：预测市场入门、Pools vs 1v1、Chainlink/Dexscreener 数据源说明
- **对比**：Telegram 预测 vs Polymarket；亚洲用户合规须知（须法务审核）
- **社群**：Yoyonians、Telegram portal 运营
- **待建**：英文/中文 `/learn/*`、`/alternatives/*`、事件类 SEO（若扩展非纯币价市场）

*战役节奏* → [yoyomarket-growth-strategy.md](./yoyomarket-growth-strategy.md)

---

## 9. 优化建议

1. **官网加厚**：当前 landing 信息过少，建议对齐六主文档中的 Phase 1 页面（功能、如何开始、费用、合规提示）。
2. **统一域名叙事**：yoyomarket.com vs yoyomarket.io canonical 与 hreflang（中/英）。
3. **承接闭环**：品牌词 → 首页；「telegram prediction market」→ Bot CTA + 分步截图页。
4. **合规页前置**：亚洲多法域；避免「博彩」表述误伤 SEO 与广告政策（见 growth-strategy §合规）。
5. **Proof 区**：交易量、活跃池数、支持链——需可验证数据后写入（标日期）。

---

## 10. 调研 Backlog（开放）

| ID | 需查证 | 优先级 |
|----|--------|--------|
| R1 | 2026 年产品是否仍仅币价池，或已支持政治/体育事件 | P0 |
| R2 | yoyomarket.com 完整 sitemap 与 Web App 上线状态 | P0 |
| R3 | YOYO 代币流通与交易所列表（Coinbase 标注 Not Trading） | P1 |
| R4 | 亚洲重点市场（台/港/新/菲等）合规表述口径 | P0 |
| R5 | 与 Polymarket/Kalshi 的定量流量对比 | P2 |

---

*文档创建：2026-06-04 | 来源： [yoyomarket.com](https://yoyomarket.com/)、[GitBook](https://yoyo-market.gitbook.io/yoyo-market-documentation)、[Medium Beta 2023-11](https://medium.com/@yoyomarket/yoyo-market-beta-release-fb72b2023056)、[Coinbase YOYO](https://www.coinbase.com/price/yoyo-market)*
