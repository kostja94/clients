# Moras — 劳动模型与 slug 映射

> **职责**：联盟侧「内容怎么生产」的 7 类模型、Moras 契合度、对应页面动作。  
> **不含**：Hero 文案（→ [pages.md](./pages.md)）、采购方总表（→ [icp.md](./icp.md)）  
> **索引**：[README.md](./README.md)

**Last updated**: 2026-08-26 · **行业核验**：2026-08-26

---

## 1. 为什么需要这一层

「带货红人」= 能稳定把 Shop 流量变成订单。宝妈常见是因为时间 + 日用货盘，**不是**官方按身份拆过的最大 GMV 群体。

Layer A（[icp.md](./icp.md)）的 `affiliates` 过粗：选品号、护士号、爱好者号工作流完全不同。Layer B 在 **不拆掉现有 6 页** 的前提下，给 Hub 第二段和 `affiliates` 子链用。

---

## 2. 七类劳动模型

平台身份默认：**#1–6 = Affiliate**（可兼 UGC 交片）；**#7 = Official / Marketing** → `tiktok-sellers`。

| # | 劳动模型 | 典型账号形态 | Moras 契合 | 页面动作 | 状态 |
|---|----------|--------------|------------|----------|------|
| 1 | **职业权威**（护士/美容师/教练；**证货对齐**） | `@midlife.nursing` 类 | 中：演示层 AI；功效/医疗声称必须真人 | `credentialed-creators` | 🔜 P0 |
| 2 | **Gen Z 全职垂类** | Logan Walter 类男性美妆垂类 | 中高：高频测 hook | 并进 `creators` | ✅ |
| 3 | **选品 / 折扣号**（含 faceless finder） | `@trending_ttok` 类 | **最高**：演示即卖点、SKU 轮换 | `deal-hunters` | 🔜 P0 |
| 4 | **家庭 / 爸爸 / 夫妻档** | `@myfamilypov` 类 | 中：家居可演示；人设仍要出镜 | `family-creators` | 🔜 P1 |
| 5 | **垂类爱好者**（粉少、货盘极窄） | `@ericsfindss` 类 | 高：吸尘器/厨房等已有 TVG | `niche-hobbyists` | 🔜 P1 |
| 6 | **副业上班族** | 1000–5000 粉 + 正职 | 高：时间穷 → 少实拍 | `side-hustlers` | ✅ |
| 7 | **品牌自营创始人** | `@based` 类 | 中：短视频测款；全天 LIVE 非 Moras | `tiktok-sellers` | ✅ |

### 边界规则（写页必守）

- **证货不对齐**的白大褂卖吸尘器 → **不算 #1**，按 #3 或 #5。
- **`@based`、品牌 `@*shop_us`** → **不算联盟**，只进 `tiktok-sellers`。
- **不开** `/use-cases/moms` — 宝妈并进 #4 `family-creators`。
- **不开** 纯 LIVE 主播页 — LIVE 不是 Moras 主产品。

---

## 3. 三张榜（不要合成一张「最容易跑出来」）

| 问题 | 优先看 |
|------|--------|
| 转化最高（证货对齐） | #1 |
| GMV 快照里常见 | #3、#4、#5、#7 |
| 最容易起步 | #6 + #3 的模板（仍须过 Pilot / 5K） |
| 最适合 faceless / 数字人演示层 | #3；#1 仅演示层（声称层不行） |

---

## 4. 与 Layer A slug 交叉索引

| Layer A slug | 覆盖的劳动模型 |
|--------------|----------------|
| `affiliates` | #1–6 父页；链向 Layer B 子页 |
| `creators` | #2；+ UGC 交片（合作模型，未必 Shop Affiliate） |
| `side-hustlers` | #6（Layer A 采购方 + 劳动模型合一） |
| `tiktok-sellers` | #7 |
| `dropship` | 无（卖家侧，非达人劳动模型） |
| `agencies` | 组织层，可服务 #1–6 任意模型 |

---

## 5. 例证数字（禁写错）

仅作类型示意，**非 Moras 效果**；完整校正见 [platform-taxonomy.md §6](./platform-taxonomy.md#6-事实校正禁写清单)。

| 锚点 | 校正要点 |
|------|----------|
| `@midlife.nursing` | 2026-01 GMV ≈ $916K；「$100K」是佣金推算；LIVE $0 |
| Just Another Nurse | 爆款吸尘器/户外，**不算** #1 |
| Logan Walter | 开卖已约 10 万粉；男性美妆垂类，非乱切品类 |
| Charm 30 天 GMV | 快照，非稳定月收入 |
| Pilot | &lt;5000 粉：每天最多 3 条带货视频 |

---

*Moras · https://moras.ai/*
