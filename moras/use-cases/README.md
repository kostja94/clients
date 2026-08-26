# Moras — Use Cases 文档集

> **市场**：仅美区 TikTok Shop。Moras 主战场是 **可购短视频产量**（选品 → 成片），不是 LIVE 逼单。  
> **站点 IA**：[moras-site-structure.md](../moras-site-structure.md) · **页面模板（已归档）**：[../_archive/moras-page-composition-guide.md](../_archive/moras-page-composition-guide.md)

**Last updated**: 2026-08-26

---

## 读哪一份

| 文档 | 何时读 | 职责 |
|------|--------|------|
| [icp.md](./icp.md) | 写 Moras 叙事、定采购方、做内容选题 | **Moras SSOT**：6 个已上线 slug、场景矩阵、风险 |
| [labor-models.md](./labor-models.md) | 拆联盟达人子人设、定 Moras 契合度 | **劳动模型 SSOT**：7 类内容生产方式 → slug 映射 |
| [pages.md](./pages.md) | 改 `/use-cases/*` 文案、上线新页、做内链 | **站点执行 SSOT**：Hero/互链/SEO/ rollout |
| [platform-taxonomy.md](./platform-taxonomy.md) | 查平台身份、合作模型、案例、政策 | **行业参考 SSOT**：TikTok Shop 红人 taxonomy，少 Moras 话术 |

依赖方向（单向，避免双源维护）：

```text
platform-taxonomy（平台事实）
        ↓
icp + labor-models（Moras 谁买单、怎么发内容）
        ↓
pages（slug 文案与上线）
        ↓
moras-site-structure（已上线 URL）
```

---

## 分类轴（只在这里解释一次）

讨论「带货红人」时行业常混用四套轴。**Use case 页只服务 Moras 采购决策**，不是把 TikTok 全行业 taxonomy 都做成 URL。

| 轴 | 问什么 | Moras 文档 | 是否单独 use-case 页 |
|----|--------|------------|------------------------|
| **A. 采购方 / 店铺角色** | 谁买单、后台是什么身份 | [icp.md](./icp.md) | **是** — 6 个已上线 slug |
| **B. 劳动模型** | 联盟内容怎么生产、信任从哪来 | [labor-models.md](./labor-models.md) | **部分** — 2–4 个子页，挂 Hub 第二段 |
| **C. 平台身份** | Official / Marketing / Affiliate | [platform-taxonomy.md](./platform-taxonomy.md) §1 | **否** — 映射进 A 层 |
| **D. 合作关系** | Open / Target / Ambassador / UGC | [platform-taxonomy.md](./platform-taxonomy.md) §2 | **否** — 品牌侧选人维度 |

**不要用美妆/家居再开人设页** — 品类由 `/tiktok-video-generator/{vertical}` 承接。

---

## 已上线 vs 规划（URL）

### Layer A — 采购方（已上线 6 页）

| slug | 状态 | 一句话 |
|------|------|--------|
| `/use-cases/tiktok-sellers` | ✅ | Official / Marketing；自有货；短视频测款 |
| `/use-cases/affiliates` | ✅ | 联盟父页；Marketplace 选品挂佣 |
| `/use-cases/creators` | ✅ | 出镜垂类 + 品牌 deal + UGC 交片（**不是**所有联盟客） |
| `/use-cases/side-hustlers` | ✅ | 有正职；60–90 分钟/天；常遇 Pilot 限流 |
| `/use-cases/agencies` | ✅ | MCN/CAP 或品牌侧联盟代理；规模化出片 |
| `/use-cases/dropship` | ✅ | 卖家侧多 SKU 快测（**不是**达人劳动模型） |

### Layer B — 联盟怎么发内容（规划）

| slug | 状态 | 优先级 |
|------|------|--------|
| `/use-cases/deal-hunters` | 🔜 | P0 — 选品/折扣号；Moras 契合最高 |
| `/use-cases/credentialed-creators` | 🔜 | P0 — 证货对齐的权威号 |
| `/use-cases/family-creators` | 🔜 | P1 — 家庭/爸爸/夫妻 POV |
| `/use-cases/niche-hobbyists` | 🔜 | P1 — 粉少、货盘极窄 |

Hub `/use-cases` 规划为两段：**By who buys**（上表 6 张）+ **By how you post**（Layer B，先上 2 张 P0）。

**Hard rule**：未上线 slug **禁止**写进 `personas.ts` 的 `to`（404 伤 SEO）。

---

## 三个已拍板的产品定义

1. **`creators`** = 以**出镜或交片**为核心产能的人：Shop Affiliate 里的垂类出镜创作者、品牌 deal、UGC 素材交付。Gen Z 全职垂类并进此页。**不含** faceless 选品号（→ `deal-hunters`）、**不含**所有 Marketplace 联盟客（→ `affiliates` 父页）。
2. **`side-hustlers`** = Layer A 采购方（有正职、时间紧），同时对应劳动模型 #6。Hub 放在 **By who buys**，不在 Layer B 重复卡片。
3. **`dropship`** = 卖家商业模式（多 SKU、快迭代），与「带货红人劳动模型」无关，保留一级入口是因为 Moras 对**测款出片**有价值。

---

*Moras · https://moras.ai/*
