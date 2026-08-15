# Eastbound and Beyond — 使用场景

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./eastbound-and-beyond.md) | [features](./eastbound-and-beyond-features.md) | [keywords](./eastbound-and-beyond-keywords.md)

**Last updated**: 2026-07-27

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **First-Time China Visitor** | 35–55 岁欧美旅客，首次访华 7–14 天，与家人或好友同行 | 语言障碍、怕踩购物团、不知如何排京沪陕 | 一次看懂中国经典+有人帮订门票与路线 | 中（会用 OTA，愿 PayPal 付款） |
| **Expat Explorer** | 25–40 岁在华工作的国际专业人士，居上海/北京 1–3 年 | 「游客景点都去过了」，周末缺灵感 | 像本地人一样吃、走、听懂城市故事 | 高（WhatsApp 咨询、读英文 blog） |
| **Culture-First Family** | 带父母或青少年访华的华裔/国际家庭，重视安全与节奏 | 老人走不动、孩子无聊、大团太赶 | 私享 2–5 人、可调整步行量、有手工艺/美食互动 | 中 |
| **Time-Pressed Professional** | 出差转 1–2 天空档的商务客 | 只有半天，要高效看精华 | 4h Forbidden City 或 3h moped/步行团 | 高 |
| **Planner Couple** | 30–45 岁夫妇，蜜月或 anniversary trip | 想要 unique 非模板行程 | 用 builder 拼 10 天线路，要 12h 内有人回复 | 中 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| First-Time China Visitor | 出发前 2 个月规划京沪 | 设计一条 10 天经典路线并拿到报价 | Multi-Day Builder + Example Trips | `china itinerary 10 days` |
| First-Time China Visitor | 落地上海第一天 | 一天内看外滩豫园又避开人挤人 | Real Shanghai in a Day（Private） | `private shanghai tour` |
| Expat Explorer | 周六早上想「像游客一样重新发现自己城市」 | 跟英语导游吃早餐逛南京路 | Shanghai Breakfast Tour | `shanghai breakfast food tour` |
| Expat Explorer | 外籍同事来访只有 3 小时 | 快速展示法租界历史+咖啡 | French Concession Walking Tour | `french concession tour shanghai` |
| Culture-First Family | 父母首次来北京 | 看懂故宫但不被朝代名淹没 | Decoding the Forbidden City | `forbidden city tour english` |
| Culture-First Family | 孩子喜欢动手 | 做中国手工艺带回家 | Tianzifang craft（含于 Full Day） | `shanghai family tour` |
| Time-Pressed Professional | 北京转机 5 小时 | 高效故宫精华游 | Forbidden City Private 4h | `beijing layover tour` |
| Time-Pressed Professional | 上海会议结束下午空档 | 3 小时 moped 看老城 | Electric Moped Tour | `shanghai moped tour` |
| Planner Couple | 对比 OTA 后犹豫 | 找到「不是大团」的可靠运营商 | About Us + TripAdvisor + Guides | `best shanghai tour company` |
| Planner Couple | 已选好城市组合 | 提交定制表单等方案 | china-journeya 表单 | `customize china trip` |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 上海早餐美食半日 | Expat Explorer | Small-Group Breakfast Tour | shanghai food tour | `/products/breakfast-in-shanghai` |
| 上海全日私享 | Culture-First Family | Private Real Shanghai in a Day | private shanghai tour | `/products/shanghai-full-day-tour` |
| 故宫深度半日 | First-Time China Visitor | Private Forbidden City | forbidden city private tour | `/products/beijing-private-forbidden-city` |
| 长城自选 | First-Time China Visitor | Your Great Wall Your Way | great wall private tour | `/products/your-great-wall-your-way` |
| 10 天经典线 | Planner Couple | Example Golden Route + Builder | beijing xian shanghai tour | `/pages/chinas-golden-route-beijing-xian-and-shanghai` |
| 周末本地去处 | Expat Explorer | Things to Do Blog | things to do shanghai | `/blogs/news` |
| 出差空档 moped | Time-Pressed Professional | Electric Moped Tour | shanghai moped tour | `/products/moped` |
| 水乡一日 | Planner Couple | Fengjing / Tongli Private | watertown tour shanghai | `/products/an-authentic-watertown` |

---

## 4. 用户旅程

```
认知：Google「shanghai food tour」/ TripAdvisor / 朋友推荐
  ↓
考虑：读产品页 Q&A + 首页评价 + Guides 页建立信任
  ↓
转化：Add to Cart（小团）或 Submit 定制表单（多日）
  ↓
体验：无旗帜会合 → 步行/美食/故事 → 手工艺或 hidden gem
  ↓
留存：TripAdvisor 评价 + Email 推其他 city tour + Blog 订阅
  ↓
推荐：评价中「recommend to Swedish friends」类口碑 → 新访客
```

**关键触达点**：12h 响应承诺、24h 取消政策、素食/ dietary FAQ、brown shirt 会合标识。

---

## 5. 未覆盖场景

| 场景 | 关键词需求 | 机会 |
|------|-----------|------|
| 亲子专属产品线 | `shanghai tour with kids` | 可在现有 family private 上建 landing，强调 child pricing |
| 企业团建 / incentive | `team building shanghai` | 无 B2B 页；可 WhatsApp 渠道承接 |
| 摄影/Instagram 主题团 | `shanghai photo tour` | 产品含 IG 叙事但未独立 SKU |
| 夜间酒吧/胡同 | `beijing bar tour` | 北京 Under Moonlight 仅在 builder 体验列表，无产品页 |
| 纯 Xi'an / Chengdu 日游 | `xian terracotta tour` | Builder 可选城但无 SKU，仅定制 |

---
