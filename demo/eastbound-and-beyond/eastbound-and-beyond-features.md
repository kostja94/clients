# Eastbound and Beyond — 功能分析

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./eastbound-and-beyond.md) | [site-structure](./eastbound-and-beyond-site-structure.md) | [use-cases](./eastbound-and-beyond-use-cases.md) | [keywords](./eastbound-and-beyond-keywords.md) | [competitors](./eastbound-and-beyond-competitors.md) | [growth-strategy](./eastbound-and-beyond-growth-strategy.md)

**Last updated**: 2026-07-27 | 来源：产品页 + [curated-city-tours](https://eastboundandbeyond.com/pages/curated-city-tours) + [china-journeya](https://eastboundandbeyond.com/pages/china-journeya)

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **Private City Tours** | 2–5 人私享团，按家庭/朋友定制节奏；含接送（上海）、门票、手工艺体验等 | ★ | `/pages/curated-city-tours#private-city-tours`；各 `/products/*` | private Shanghai tour, Forbidden City private tour |
| **Small-Group City Tours** | 2–10 人小团步行/美食团，无旗帜、无扩音器，强调对话式导览 | ★ | `/pages/curated-city-tours#small-group-city-tours` | Shanghai food tour, hutong walking tour Beijing |
| **Multi-Day Journey Builder** | 选城市→天数→体验模块→提交，12 小时内回复报价 | ★ | `/pages/china-journeya` | customize China trip, China itinerary planner |
| **Example Itineraries** | 8 条主题多日线路（Golden Route、Southern China、Flavour Journey 等）作灵感 | | `/pages/china-journeya#example-china-trips` 及 `/pages/*-journey` | China tour 10 days, Beijing Xi'an Shanghai tour |
| **Curated Guide Network** | 50+ 精选导游，全球视野、多语言/跨文化背景；可预览导游档案 | ★ | `/pages/guides` | English speaking tour guide China |
| **Direct Operator Model** | 自营设计与执行，去除中间商，统一沟通与品控 | ★ | `/pages/about-us` | boutique China travel company |
| **Online Booking & Cart** | Shopify 产品页 Add to Cart / Book Now，PayPal 支付 | | 各 `/products/{slug}` | book Shanghai tour online |
| **Local Insider Content** | 月度 Top Spots / Top Eats 博客，展示本地洞察 | ★ | `/blogs/news` | things to do Shanghai, where to eat Beijing |
| **Concierge Support** | Email / WhatsApp / WeChat / 美国电话；12 小时内回复； dietary 定制 | | 全站页脚 + 产品 Q&A | China travel advice English |
| **Flexible Cancellation** | 24 小时前全额退款（扣除 4.4% PayPal 手续费）；极端天气全额退 | | 产品页 Cancellation Policy | — |

> ★ = 相对 OTA 大团/旗帜团、纯打包社差异明显的能力。

---

## 2. 用户流程

### 2.1 城市日游预订（Small-Group）

```
浏览首页或 Curated City Tours
  → 选择 Small-Group 产品（如 Shanghai Breakfast Tour）
  → 选成人/儿童人数 → Add to Cart / Book Now
  → PayPal 结账
  → 收到确认；导游 brown shirt + logo 会合
  → 3 小时步行 + 多站美食 → TripAdvisor 评价
```

### 2.2 私享日游预订（Private）

```
选择 Private City Tour（如 Real Shanghai in a Day）
  → 配置 2–5 人 → 选择 Premier taxi 或 +$20–40/人 Private car
  → 可选 sunset extension（+1–2 小时）
  → 支付 → 市中心 6km 内免费接送
  → 8 小时深度游（地标 +  hidden alleys + 湿市场午餐自选 + 手工艺）
```

### 2.3 多日定制旅程

```
进入 Customize Your Journey
  → 点选城市（Beijing / Shanghai / Xi'an / Chengdu 等 10 城）
  → 设定每城天数
  → Pick Your Experiences（美食/胡同/长城/科技主题等）
  → 提交询价表单
  → 12 小时内 travel expert 回复定制方案与报价
  → 参考 Example Trips 调整 → 确认预订
```

### 2.4 售前咨询

```
任意页面 → Email / WhatsApp / WeChat
  →  dietary / solo traveler / 6+ 人群特殊需求
  → 人工协调档期与定制
```

---

## 3. 技术指标

| 指标/声明 | 内容 | 状态 |
|----------|------|------|
| 月服务旅客 | 400+ global travelers/month | [about-us](https://eastboundandbeyond.com/pages/about-us) 2026-07-27 |
| 导游规模 | 50+ guides | 同上 |
| 体验数量 | 40+ experiences | 同上 |
| TripAdvisor 评分 | 100% five-star reviews（官网声明） | ⚠️ 待验证：需 TripAdvisor 页面核对 |
| 响应时效 | 12 小时内回复咨询 | 全站 CTA |
| 小团规模 | Private 2–5；Small-Group 2–10 | 产品页 |
| 步行强度 | 小团 ~3 km；全日私享 ~6–7 km | 产品页 |
| 退款政策 | 24h 前退（扣 4.4% 支付费） | 产品页 |

---

## 4. 定价

| 产品类型 | 价格 | 备注 | 来源 |
|---------|------|------|------|
| **Small-Group 美食/步行团** | **$65/成人，$52/儿童（4–12）**；3 岁及以下免费 | 如 Shanghai Breakfast Tour；2–10 人 | [breakfast-in-shanghai](https://eastboundandbeyond.com/products/breakfast-in-shanghai) 2026-07-27 |
| **Private 全日游** | ⚠️ 待验证（页面 JS 动态价，未抓取到数值） | Real Shanghai in a Day；含接送、门票、饮料、手工艺 | [shanghai-full-day-tour](https://eastboundandbeyond.com/products/shanghai-full-day-tour) |
| **Private 半日游** | ⚠️ 待验证 | Forbidden City 4h；门票含 Treasure Gallery | [beijing-private-forbidden-city](https://eastboundandbeyond.com/products/beijing-private-forbidden-city) |
| **Private Car 升级** | +$20–40/人（视人数） | 替代 Premier taxi | shanghai-full-day-tour Q&A |
| **多日定制** | 询价制 | Builder 提交后 12h 回复 | china-journeya |
| **支付** | PayPal / 信用卡；4.4% 不可退手续费 | — | Cancellation Policy |

**定价模式摘要**：小团明码标价可即时预订；私享与多日行程偏 premium boutique 定位，价格需表单/购物车动态展示。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Small-Group Food Tour | 初到上海、想半天吃遍本地早餐 | **Expat Explorer** |
| Private Full-Day Tour | 家庭/朋友希望一天看精华又避人流 | **Culture-First Family** |
| Forbidden City Private | 对历史/建筑有深度兴趣，厌弃打卡团 | **History Buff Traveler** |
| Electric Moped Tour | 短时长高密度看老城 | **Time-Pressed Professional** |
| Multi-Day Builder | 首次中国行，多城串联 | **First-Time China Visitor** |
| Example Itineraries | 有灵感但需要专业微调 | **Planner Couple** |
| Things to Do Blog | 已在中国居住，找周末去处 | **Expat Explorer** |
| Guide Profiles | 预订前想确认导游风格/语言 | **Culture-First Family** |

---
