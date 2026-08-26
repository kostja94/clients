# Moras — Use Cases 页面规格与 rollout

> **职责**：`/use-cases/*` 文案规格、Hub 结构、SEO 边界、实施顺序。  
> **Moras 契合与模型定义**：[labor-models.md](./labor-models.md) · **采购方**：[icp.md](./icp.md)  
> **模板契约（已归档）**：[../_archive/moras-page-composition-guide.md](../_archive/moras-page-composition-guide.md) §3.2  
> **已上线 URL**：[../moras-site-structure.md](../moras-site-structure.md)

**Last updated**: 2026-08-26

---

## 1. Hub 结构

`/use-cases` 两段式：

1. **By who buys Moras** — 6 张 Layer A 卡片（均已上线）
2. **By how affiliates post** — Layer B，先 2 张 P0，P1 上线后再加

`affiliates` 页 Hero 须点名 Layer B 子人设；第三张 product spotlight 在 `deal-hunters` 上线后链过去。

---

## 2. 已上线页 — 改文案要点（P0，不新开 slug）

| slug | 改什么 |
|------|--------|
| `affiliates` | 明确为**父页**；区分与 `creators`；预留子人设链接位 |
| `creators` | 出镜垂类 + 品牌 deal + UGC 交片；Gen Z 全职垂类；**不**写「所有联盟客」 |
| `side-hustlers` | 1000 粉门槛、Pilot 3 条/天、60–90 分钟；主推 faceless/hybrid |
| `tiktok-sellers` | Official/Marketing；`@based` 方向；短视频测款 vs 全天 LIVE |
| `agencies` | 分达人侧 MCN vs 品牌侧联盟代理（各 1 句） |
| `dropship` | 卖家多 SKU 测款；不冒充达人劳动模型 |

---

## 3. P0 新页规格

模板字段：`hero` · `capabilities`（3 段）· `steps`（3 步）· `products` · `compare`。CTA → App Store。仅美区。数字只用行业例证。

### 3.1 `/use-cases/deal-hunters` 🔜

**H1**：TikTok Shop Deal Accounts — Post Shoppable Demos Without Filming Every SKU  
**Who**：选品号、折扣号、faceless finder（`@trending_ttok` 类）

| 字段 | 内容 |
|------|------|
| `hero` | 每天要上新演示，瓶颈是拍摄。Moras：链接 → 多版本可购短视频。 |
| `capabilities` | ① 同一 SKU 多 hook ② 清洁/厨房/3C 演示密度 ③ 选品评分挡高退货 |
| `steps` | 锁垂类 → 链入生成 3 cuts → 看点击再加 SKU |
| `products` | Product research · Video generator · Product scorer |
| `compare` | vs 每条实拍；vs 无货盘逻辑的随机搬运 |

**TVG**：`cleaning-gadgets` · `kitchen-gadgets` · `vacuum`  
**Blog**：`/blog/faceless-tiktok-shop-videos` · `/blog/tiktok-shop-niche-selection` · `/blog/faceless-vs-face-tiktok-shop`  
**AudienceGrid**：`For Deal-Hunter Affiliates`  
**禁写**：LIVE 逼单、佣金保证、Charm GMV 当 Moras 效果。Pilot：3 条/天里测点击。

### 3.2 `/use-cases/credentialed-creators` 🔜

**H1**：Nurses, Estheticians, and Trainers on TikTok Shop — Only When the License Matches the SKU  
**Who**：持证/经验对齐货盘；排除白大褂卖吸尘器

| 字段 | 内容 |
|------|------|
| `hero` | 信任来自判断，产量来自可演示 SKU。Moras 做演示层，不编疗效。 |
| `capabilities` | ① 用法/机理可购短视频 ② 功效声称真人出镜 ③ 同步骤多 hook |
| `steps` | 证货一句话 → 只选可演示 SKU → 演示 AI、声称真人 |
| `products` | Video generator · Product research · 不主推数字人证言 |
| `compare` | vs AI 脸说「我用了就好了」（FTC + 健康内容风险） |

**TVG**：`skincare` · `makeup-tools`（手法/工具，非处方功效）  
**Blog**：`/blog/tiktok-ai-content-rules` · `/blog/faceless-vs-face-tiktok-shop` · `/blog/tiktok-shop-video-script`  
**硬边界**：补充剂/医疗声称弱 Moras；清洁工具、涂抹手法可 AI。

---

## 4. P1 新页（摘要）

### `family-creators`

家庭/爸爸/夫妻 POV；宝妈是子集。演示段可 Moras，人设段出镜。TVG：`home-organization` · `cleaning-gadgets` · `pet-products`。

### `niche-hobbyists`

1–2 万粉、窄货盘；粉非瓶颈，演示密度与退货才是。TVG：`vacuum` · `kitchen-gadgets` · `pet-products`。禁把 `@ericsfindss` GMV 写成 Moras 效果。

---

## 5. SEO 与内链

| 栏目 | 吃什么词 | 不抢 |
|------|----------|------|
| `/use-cases/{persona}` | who it's for（nurse TikTok Shop、faceless affiliate） | 品类词 → TVG |
| `/tiktok-video-generator/{v}` | 品类长尾 | 人设词 |
| Blog | 决策框架 | 复制 use-case Hero |

**镜像规则**：同一 persona 在 TVG 与 use-case 页 `description` 须按主语重写。

**Blog G6**：当前禁止链 `/use-cases/*`；人设页上线且解禁后再做博客回链。

**关键词方向**（写 `personas.ts` 前再跑搜索量）：

| slug | 主词方向 |
|------|----------|
| deal-hunters | faceless TikTok Shop affiliate, TikTok Shop deal account |
| credentialed-creators | nurse TikTok Shop, esthetician TikTok Shop affiliate |
| family-creators | family TikTok Shop, dad TikTok Shop finds |
| niche-hobbyists | small account TikTok Shop, niche TikTok Shop affiliate |

---

## 6. 实施顺序

1. 改 Hub + `affiliates` / `creators` / `side-hustlers` / `tiktok-sellers`（**不加**未上线 `to`）
2. 上线 `deal-hunters`：`personas.ts` + 路由 + Hub 第二段 + TVG AudienceGrid 换 1 张
3. 上线 `credentialed-creators`
4. P1：`family-creators` · `niche-hobbyists`
5. Blog G6 解禁后做回链

`src/components/site/use-cases/personas.ts` 为唯一数据源。禁止为填模板硬凑 `metrics`。

---

*Moras · https://moras.ai/*
