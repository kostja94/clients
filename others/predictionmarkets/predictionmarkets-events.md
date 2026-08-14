# Prediction Markets 事件（Events）— 程序化 SEO 核心

> **本文档职责**：事件分类、数据 schema、URL 模式、程序化 SEO 模板。**核心用于驱动程序化 SEO**，独立于 [predictionmarkets.md](./predictionmarkets.md)、[predictionmarkets-competitors.md](./predictionmarkets-competitors.md)。  
> **引用**：关键词见 [predictionmarkets-keywords.md](./predictionmarkets-keywords.md)；竞品平台见 [predictionmarkets-competitors.md](./predictionmarkets-competitors.md)

---

## 1. 事件分类体系（Polymarket 12 类）

> 来源：[Polymarket Guide](https://polymarketguide.gitbook.io/polymarketguide/markets/basics/categories)、[Polymarket API](https://docs.polymarket.com/concepts/markets-events)

| 类别 | Slug | 说明 | 代表事件/关键词 |
|------|------|------|----------------|
| **Politics** | politics | 总统选举、参议院多数、政府关门 | presidential election, senate majority, government shutdown |
| **Sports** | sports | 超级碗、NBA 总决赛、世界杯、温网 | Super Bowl, World Cup, NFL prediction |
| **Crypto** | crypto | 比特币价格、代币发行、NFT | Bitcoin prediction, crypto price, Ethereum prediction |
| **Earnings** | earnings | 季报、EPS 发布 | earnings prediction, EPS release |
| **Geopolitics** | geopolitics | 乌克兰停火、俄乌战争、台海 | Iran prediction, Ukraine ceasefire, geopolitical |
| **Tech** | tech | AI 模型、robotaxi、SpaceX 发射 | AI prediction, SpaceX launch |
| **Culture** | culture | 格莱美、诺贝尔和平奖、电影上映 | Grammy, Nobel Prize, celebrity prediction |
| **World** | world | 国际政治、全球结果 | international election |
| **Economy** | economy | 通胀、就业、GDP | inflation prediction, Fed prediction, GDP growth |
| **Trump** | trump | 特朗普相关政治事件 | Trump prediction, Trump SOTU |
| **Elections** | elections | 国际选举结果 | election prediction, international election |
| **Mentions** | mentions | 特定词/短语是否在活动中被提及 | mention market, SOTU mention, earnings call mention |

*Polymarket 结构：Series → Events → Markets。每 Event 可含单市场或多市场（互斥选项）。*

---

## 2. 事件子类与长尾（程序化 SEO 数据源）

### 2.1 Politics

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| Presidential | 2028 总统提名、谁胜选 | presidential prediction market, election prediction market |
| Senate | 参议院多数、席位 | senate prediction market, senate odds |
| House | 众议院多数 | house prediction market |
| Governor | 州长选举 | governor prediction market |
| Government | 政府关门、预算 | government shutdown prediction |

### 2.2 Economy

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| Fed | FOMC 决议、利率 | Fed prediction market, interest rate prediction |
| Inflation | CPI、通胀率 | inflation prediction market |
| GDP | GDP 增长区间 | GDP prediction market |
| Jobs | 非农、失业率 | jobs report prediction |

### 2.3 Crypto

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| Bitcoin | BTC 价格区间、ATH | Bitcoin prediction market, BTC price prediction |
| Ethereum | ETH 价格 | Ethereum prediction market |
| Altcoins | 代币发行、NFT | crypto prediction market |

### 2.4 Geopolitics

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| Iran | 美军行动、伊朗局势 | Iran prediction market, war prediction market |
| Ukraine | 停火、俄乌 | Ukraine prediction market |
| China-Taiwan | 台海冲突 | china taiwan prediction |
| Middle East | 地区冲突 | geopolitical prediction market |

### 2.5 Sports

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| NFL | 超级碗、MVP | Super Bowl prediction, NFL prediction |
| NBA | 总决赛、冠军 | NBA prediction market |
| World Cup | 世界杯冠军 | World Cup prediction |
| Tennis | 温网、大满贯 | Wimbledon prediction |

### 2.6 Mentions（Mention Markets）

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| SOTU | 国情咨文提及词 | SOTU prediction, Trump SOTU mention |
| FOMC | 美联储会议提及 | Fed mention market |
| Earnings | 财报电话会提及 | earnings call mention |
| Sports | NFL 直播提及 | mention market |

*Kalshi 运营最大 mention markets 目录；Polymarket 亦有。结算依据：活动视频、官方来源、可信报道共识。*

### 2.7 Weather（Kalshi 特色）

| 子类 | 示例事件 | 关键词 |
|------|----------|--------|
| Temperature | 气温区间 | weather prediction market |
| Hurricane | 飓风路径、登陆 | hurricane prediction |
| NOAA | 官方气象数据结算 | weather market |

*Kalshi 覆盖天气市场，结算依据 NOAA 等官方机构。*

---

## 3. 事件结算规则（Resolution）

> 平台结算机制影响用户信任与争议处理。详见 [predictionmarkets-features.md](./predictionmarkets-features.md) §八 Resolution。

| 平台 | 机制 | 结算依据 |
|------|------|----------|
| **Polymarket 国际** | UMA Optimistic Oracle；提案+保证金→2h 异议期→UMA 投票 | 去中心化 |
| **Polymarket 美国** | 平台判定；公开可验证信息 | 官方来源、主流媒体、政府/联盟网站 |
| **Kalshi** | 中心化；Source Agencies 指定 | 每市场指定机构（NFL/NBA、BLS、NOAA 等） |

*来源：[Polymarket Resolution](https://docs.polymarket.com/concepts/resolution)、[DefiRate](https://defirate.com/prediction-markets/how-contracts-settle/)*

---

## 4. 程序化 SEO 数据 Schema

### 4.1 单事件页数据字段

```json
{
  "event_id": "string",
  "slug": "string",
  "category": "politics|economy|crypto|geopolitics|sports|tech|culture|earnings|world|trump|elections|mentions",
  "sub_category": "string",
  "title": "string",
  "description": "string",
  "resolution_date": "ISO8601",
  "platforms": ["polymarket", "kalshi"],
  "volume_24h": "number",
  "volume_total": "number",
  "markets_count": "number",
  "keywords": ["string"],
  "url": "string"
}
```

### 4.2 分类页数据字段

```json
{
  "category": "string",
  "slug": "string",
  "sub_categories": ["string"],
  "keywords": ["string"],
  "url": "string",
  "events_count": "number"
}
```

### 4.3 数据来源

| 来源 | 用途 | 更新频率 |
|------|------|----------|
| **Polymarket Gamma API** | GET /events, GET /markets, GET /series | 实时/日 |
| **Polymarket CLOB API** | 价格、order book | 实时 |
| **Kalshi API** | 事件、市场列表 | 日/周 |
| **手动/爬虫** | 高价值事件补充、关键词 |

---

## 5. URL 模式（程序化 SEO）

| 类型 | 模式 | 示例 |
|------|------|------|
| **分类 Hub** | /events/{category} | /events/politics、/events/economy、/events/crypto |
| **子类** | /events/{category}/{sub-category} | /events/politics/election、/events/economy/fed |
| **单事件** | /events/{category}/{slug} 或 /events/{slug} | /events/politics/trump-2028、/events/bitcoin-ath-2025 |
| **平台+事件** | /events/{platform}/{slug} | /events/polymarket/iran-august（可选） |

### 5.1 推荐结构

| 层级 | URL | 说明 |
|------|-----|------|
| 1 | /events | 事件总览 Hub |
| 2 | /events/{category} | 分类页（政治、经济、加密货币等） |
| 3 | /events/{category}/{slug} | 单事件页（程序化生成） |

---

## 6. 程序化 SEO 模板结构

### 6.1 分类页模板（/events/{category}）

| Section | 内容 |
|---------|------|
| **H1** | {Category} Prediction Markets |
| **Intro** | 该类别预测市场简介、为何重要、平台覆盖 |
| **Evidence block** | 当前活跃事件表（HTML table）：事件名、平台、结算日、交易量 |
| **Sub-categories** | 子类列表 + 链至子类页或锚点 |
| **FAQ** | 如 "What is {category} prediction market?" |
| **CTA** | Subscribe、链至平台 |

### 6.2 单事件页模板（/events/{category}/{slug}）

| Section | 内容 |
|---------|------|
| **H1** | {Event title} Prediction Market |
| **Intro** | 事件背景、为何可交易、平台 |
| **Evidence block** | 市场列表（Polymarket/Kalshi）、当前价格、交易量、结算日 |
| **Related** | 同类别其他事件 |
| **FAQ** | 如 "How does {event} resolve?" |
| **CTA** | 链至 Polymarket/Kalshi、Subscribe |

### 6.3 内容要求（Programmatic SEO）

| 要求 | 说明 |
|------|------|
| **300+ 词** | 每页最低字数 |
| **Evidence block** | 每页含真实数据表/列表（事件、价格、量） |
| **唯一数据** | 每页有独特、可验证的数据，非简单变量替换 |
| **内部链接** | 分类↔事件、相关事件互链 |

---

## 7. 事件关键词映射（程序化 SEO 目标词）

| 类别 | 主关键词 | 长尾模式 |
|------|----------|----------|
| Politics | political prediction market, election prediction market | {election type} prediction market, {candidate} prediction |
| Economy | economic prediction market | inflation prediction market, Fed prediction market, GDP prediction |
| Crypto | crypto prediction market | Bitcoin prediction market, {token} price prediction |
| Geopolitics | geopolitical prediction market | Iran prediction market, Ukraine prediction market |
| Sports | sports prediction market | {league} prediction, {event} prediction market |
| Tech | tech prediction market | AI prediction market, SpaceX prediction |
| Culture | celebrity prediction market | Grammy prediction, Nobel prediction |
| Mentions | mention market | SOTU mention market, earnings call mention |

---

## 8. 实施优先级

| 优先级 | 动作 |
|--------|------|
| **P0** | 定义数据 schema（Event、Category）；对接 Polymarket API 或手动种子数据 |
| **P0** | 新建 /events Hub、/events/{category} 分类页（Politics、Economy、Crypto、Geopolitics、Sports） |
| **P1** | 单事件页模板；首批 50–100 高价值事件 |
| **P1** | Sitemap 分段（/events/*）；noindex 低价值页 |
| **P2** | Kalshi 数据接入；Mention markets 子类 |
| **P2** | 数据更新自动化（日/周） |

---

## 9. 文档关联

| 文档 | 关联 |
|------|------|
| [predictionmarkets.md](./predictionmarkets.md) | 概览；事件页链入 Understanding、News |
| [predictionmarkets-competitors.md](./predictionmarkets-competitors.md) | 平台覆盖（Polymarket、Kalshi、PredictIt、Opinion、Manifold） |
| [predictionmarkets-keywords.md](./predictionmarkets-keywords.md) | 事件关键词→目标页映射 |
| [predictionmarkets-features.md](./predictionmarkets-features.md) | Resolution 结算规则、How-To 实践、Use cases |

---

**Last updated**：2026-03-02
