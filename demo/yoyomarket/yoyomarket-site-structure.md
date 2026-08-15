# Yoyo Market 网站结构

> **本文档职责**：必备页、URL 优先级、导航与关键词映射；路由明细可随产品迭代追加。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[yoyomarket.md](./yoyomarket.md) | [yoyomarket-keywords.md](./yoyomarket-keywords.md)

**Last updated**: 2026-06-04 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [yoyomarket.md](./yoyomarket.md) |
| 关键词 | [yoyomarket-keywords.md](./yoyomarket-keywords.md) |
| 功能 | [yoyomarket-features.md](./yoyomarket-features.md) |
| 增长策略 | [yoyomarket-growth-strategy.md](./yoyomarket-growth-strategy.md) |

---

## 一、当前线上触点（2026-06-04）

| 触点 | URL | 角色 | 备注 |
|------|-----|------|------|
| 官网 | https://yoyomarket.com/ | 品牌/SEO | 抓取仅 title，**待建设** |
| 备用站 | https://www.yoyomarket.io | 品牌 | GitBook 嵌入，canonical **待统一** |
| 文档 | https://yoyo-market.gitbook.io/yoyo-market-documentation | 支持/SEO 长尾 | |
| Telegram Bot | https://t.me/yoyo_market_bot | **主转化** | |
| 社群 | https://t.me/yoyomarket_portal | 社群 | |
| Medium | https://medium.com/@yoyomarket | 发布 | |
| X | https://x.com/yoyomarket_io | 社交 | |

---

## 二、核心路径表（≥5，含目标意图）

| 用户路径 | 步骤 | 主意图 | 现状 |
|----------|------|--------|------|
| 品牌直达 | Google「yoyomarket」→ 首页 → Bot | 品牌 | 首页薄 |
| 品类认知 | 「prediction market」→ /learn → Bot | 信息 | 缺页 |
| 交易意图 | 「bet btc telegram」→ /features/pools → Bot | 交易 | 缺页 |
| 对比选型 | 「polymarket alternative」→ /vs/polymarket | 对比 | 缺页 |
| 中文流量 | 「預測市場」→ /zh/ → Bot | 商业 | 缺页 |
| 文档自助 | GitBook → Bot | 支持 | 已有 |
| 代币研究 | 「YOYO token」→ /token | 投资 | 缺页 |

---

## 三、建议信息架构（分阶段）

### Phase 1 — Must Have（MVP 官网）

| 路径 | 类型 | 目标关键词 |
|------|------|------------|
| `/` | 首页 | crypto prediction market, 亞洲預測市場 |
| `/how-it-works` | 教程 | how to use yoyo market |
| `/features/pools` | 功能 | prediction pool crypto |
| `/features/telegram` | 功能 | telegram prediction market |
| `/pricing` | 费用 | yoyo market fees |
| `/learn/what-is-prediction-market` | 教育 | what is prediction market |
| `/legal/terms` | 法务 | — |
| `/legal/risk` | 风险披露 | — |

**首页模块建议**：Hero（Slogan + Bot CTA）→ 三步开始 → Pools 示意图 → 费用摘要 → 合规短声明 → FAQ → Footer（链 GitBook、社群）

### Phase 2 — Growth

| 路径 | 类型 |
|------|------|
| `/features/pvp` | 功能 |
| `/features/data` | 技术信任 |
| `/vs/polymarket` | 对比 |
| `/alternatives` | 聚合对比 |
| `/for/crypto-traders` | 场景 |
| `/for/beginners` | 场景 |
| `/token` | 代币 |
| `/nft` | NFT |

### Phase 3 — 本地化与 B2B

| 路径 | 类型 |
|------|------|
| `/zh/` | 中文首页 |
| `/zh/learn/*` | 中文教育 |
| `/for/communities` | 白标 |
| `/partners` | 合作案例 |
| `/blog` | 内容 SEO |

---

## 四、导航草案

```
[Logo]  Product ▾   Learn ▾   Compare ▾   [中文]   [Launch App → Bot]

Product: Pools · PvP · Telegram · Token · NFT
Learn: What is PM · Safety · Regulation (Asia)
Compare: vs Polymarket · Alternatives
```

移动端：Sticky **Open in Telegram** CTA。

---

## 五、技术架构（推断）

| 层 | 推测 | 待验证 |
|----|------|--------|
| 营销站 | 静态站或 Webflow/Next | 当前几乎空页 |
| 应用 | Telegram Mini App + 合约后端 | Arbitrum |
| 文档 | GitBook | 已用 |
| 分析 | GA4 / Plausible | — |
| 多语言 | `/zh` 子目录 + hreflang | — |

---

## 六、SEO 技术项

| 项 | 建议 |
|----|------|
| canonical | 统一 .com 与 .io |
| hreflang | en + zh-Hant/zh-Hans（按运营市场选） |
| Schema | Organization、SoftwareApplication（Telegram） |
| Sitemap | Phase 1 起提交 |
| Bot 深链 | `t.me/yoyo_market_bot?start=utm_xxx` 区分战役 |

---

## 七、URL ↔ 关键词速查

见 [yoyomarket-keywords.md](./yoyomarket-keywords.md) §六 JTBD 表；结构变更时同步更新 keywords「状态」列。

---

*线上 IA 以实际部署为准；本轮基于公开文档与落地页抓取（2026-06-04）。*
