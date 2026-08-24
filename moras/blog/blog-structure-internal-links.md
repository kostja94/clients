# Moras Blog 文章结构与内链

> **用途**：全站 Blog 唯一的**结构与内链优化**参考（人类 + 站点维护）。只回答两件事：**① 64 篇文章如何组织；② 文章之间应如何互链**。
>
> **Skill 对齐**：创作 Gate / Canonical / Hub-Spoke 以 [`../skills/blog-article/references/content-graph.md`](../skills/blog-article/references/content-graph.md) 为 SSOT；本文是同一信息的**项目级视图**，并附**当前成稿内链快照**与**补链优先级**。
>
> **最后更新**：2026-08-24（Cluster F #59–#68 完整 · **全库 R1–R4 内链优化 PASS**）

---

## 一、Blog 文章结构

```
Blog (/blog) — 64 篇 · 下一序号 #69
│
├── creator-affiliate/          ← Cluster A（Creator / Affiliate）
│   ├── #01  how-to-make-money-on-tiktok              ★ Pillar Hub
│   ├── #02  tiktok-shop-setup
│   ├── #04  tiktok-product-research
│   ├── #06  tiktok-captions-hashtags
│   ├── #07  tiktok-affiliate-side-hustle
│   ├── #08  tiktok-shop-no-sales
│   ├── #09  tiktok-shop-influencer-marketing         （品牌 ICP）
│   ├── #44  tiktok-shop-dropshipping
│   ├── #49  tiktok-shop-niche-selection              ★ 垂直化框架（新）
│   ├── #52  tiktok-shop-free-samples                 （新）
│   ├── #54  tiktok-creator-rewards-guide             ★ CR 车道 spoke（新）
│   ├── #56  faceless-vs-face-tiktok-shop             （新）
│   ├── #57  tiktok-shop-affiliate-disclosure         （新）
│   └── #58  tiktok-shop-affiliate-commissions        （新）
│
├── seasonal-campaign/          ← Cluster F（Seasonal / Campaign）
│   ├── #59  tiktok-shop-sales-calendar                 ★ 大促日历 Hub（evergreen · 每年更新）
│   ├── #60  tiktok-shop-labor-day
│   ├── #61  tiktok-shop-september-restock
│   ├── #62  tiktok-shop-back-to-school
│   ├── #63  tiktok-shop-black-friday                   ★ BFCM spoke
│   ├── #64  tiktok-shop-holiday-gifts
│   ├── #65  tiktok-shop-halloween
│   ├── #66  tiktok-shop-fall-deals
│   ├── #67  tiktok-shop-jumpstart
│   └── #68  tiktok-shop-summer-sale
│
├── tiktok-video/               ← Cluster A 制作 + Cluster E 格式 Spoke
│   ├── #03  faceless-tiktok-shop-videos
│   ├── #05  tiktok-video-hooks                         ★ 钩子 Framework
│   ├── #25  tiktok-video-formats                       ★ 格式 Hub
│   ├── #35–#42  格式 Spoke（photo / storytime / POV / satisfying / B&A / duet / classification / green-screen）
│   ├── #50  tiktok-shop-video-script                   ★ 全片脚本 Framework（新）
│   └── #55  tiktok-shop-slideshow-compliance           （新）
│
├── content-discovery/          ← Cluster C
│   ├── #26  how-the-tiktok-algorithm-works             ★ 分发算法 Hub
│   ├── #27  tiktok-keyword-research
│   ├── #28  trending-tiktok-sounds
│   ├── #29  tiktok-ai-content-rules                    ★ AI 合规 Hub
│   ├── #30  how-to-use-tiktok-trends
│   └── #47  tiktok-shop-algorithm                      （Shop 向；与 #26 区分）
│
├── platform-ops/               ← Cluster B
│   ├── #10–#14, #16, #18–#22  核心 + 三 Hub（#12 Toolkit · #14 SPS · #18 Buyer）
│   ├── #43  is-tiktok-shop-legit
│   ├── #45  tiktok-shop-fees
│   ├── #46  tiktok-shop-account-health-rating
│   ├── #48  tiktok-shop-promo-codes
│   └── #51  tiktok-shop-violation-appeal               （新）
│
└── （根目录）Cluster D — E-commerce AI
    ├── #31  ai-commerce-agent-ecommerce                ★ Agent Hub
    ├── #32  ai-ugc-content-creator
    ├── #33  ai-custom-avatar-videos
    ├── #34  ai-ecommerce-video-workflow
    └── #53  ai-ugc-tiktok-shop-conversion              （新 · 转化验证）
```

**结构规则**（与 `topic-cluster-layout.md` 一致）：

| 规则 | 说明 |
|------|------|
| **NN 全局递增** | 不按子目录重置；#15/#17/#23/#24 已删/合并，不重排 |
| **公开 URL 扁平** | frontmatter `slug` = `/blog/{url-slug}`，不含文件夹名 |
| **文件夹仅本地组织** | `creator-affiliate/`、`tiktok-video/` 等不影响线上路径 |
| **frontmatter `category`** | 与 Cluster 注册表一致（见 content-graph §1B） |
| **不设 Related 模块** | 内链只在正文自然语境中出现 |

---

## 二、Cluster 角色速查

| Cluster | folder | Hub slug | 受众主轴 |
|---------|--------|----------|----------|
| **A** Creator / Affiliate | `creator-affiliate/` | `how-to-make-money-on-tiktok` | US TikTok Shop affiliate |
| **B** Platform Ops | `platform-ops/` | `tiktok-shop-toolkit` | 平台政策 / 买家卖家实务 |
| **C** Content & Discovery | `content-discovery/` | `how-the-tiktok-algorithm-works` | 算法 / SEO / 趋势 / 合规 |
| **D** E-commerce AI | *(root)* | `ai-commerce-agent-ecommerce` | 跨平台 AI 带货生产 |
| **E** Video Format Spokes | `tiktok-video/` | `tiktok-video-formats` | 格式 Spoke（#35–#42） |
| **F** Seasonal / Campaign | `seasonal-campaign/` | `tiktok-shop-sales-calendar` | US 大促窗口 / affiliate 排期 |

---

## 三、内链硬性规则

> 与 skill `content-graph.md` §4.5、`project-config.md` G6 一致。

| # | 规则 | 说明 |
|---|------|------|
| **R1** | 每篇正文 ≥2 条其他 `/blog/` slug 内链 | Phase 5 SelfCheck |
| **R2** | 锚文本描述性 | 禁 `click here` / `learn more` / `this article` |
| **R3** | 同 slug 同篇通常 ≤2 次 | 第 2 次仅在结论或最强语境 |
| **R4** | **TL;DR 与 FAQ 不加内链** | Moras 成稿惯例 |
| **R5** | 禁 G6 路径 | `/use-cases/*` `/app/*` 等 + forthcoming |
| **R6** | **自然优先，不强求双向** | 入链为 0 的 spoke 仅在有语境时补 1 条 |
| **R7** | **Pillar #01** 须链向 Cluster A 全部 spoke（#02–#09） | 缺则补 |

**Canonical 概念**：同一概念只在一篇展开；他文 1–2 句 + link（见 content-graph §4.3）。

---

## 四、Cluster 内链矩阵（应链向 / 应被链自）

> 「应链向」= 新稿 Outline 阶段优先规划；「应被链自」= 维护时检查入链是否过薄。  
> ✓ = 2026-08-24 成稿中已有正文出链；△ = 入链 ≤1，建议补；✗ = **零入链**（优先补）。

### 4.1 Cluster A — Creator / Affiliate

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `how-to-make-money-on-tiktok` | **Pillar** | 02, 03, 04, 05, 06, 07, 08, 09, 44, 54 | 全库高频 |
| `tiktok-shop-setup` | Setup | 01, 07, 58 | 02, 04, 07, 09, 11, 57 |
| `tiktok-product-research` | Research | 01, 08, 49 | 04, 07, 12, 27, 44, 49, 50, 52, 56 |
| `tiktok-captions-hashtags` | Strategy | 05, 27 | 01, 02, 06, 08, 26, 57 |
| `tiktok-affiliate-side-hustle` | Side Hustle | 01, 04, 07, 54 | 01, 07, 45, 52, 58 |
| `tiktok-shop-no-sales` | Diagnosis | 05, 08, 14, 26, 47 | 01, 08, 12, 41, 44, 47, 49, 58 |
| `tiktok-shop-influencer-marketing` | 品牌 | 01, 03, 09 | 01, 09, 44 |
| `tiktok-shop-dropshipping` | Strategy | 01, 04, 44, 46 | ✓01, 02 |
| `tiktok-shop-niche-selection` | Framework | 01, 04, 07, 08 | ✓01, 02, 04, 08, 49, 50, 56 |
| `tiktok-shop-free-samples` | Strategy | 04, 07, 29 | ✓04, 07 |
| `tiktok-creator-rewards-guide` | CR spoke | 01, 07, 27 | ✓01, 07, 27 |
| `faceless-vs-face-tiktok-shop` | 决策 | 03, 33, 49, 56 | ✓03, 07, 49 |
| `tiktok-shop-affiliate-disclosure` | 合规 | 06, 29, 57 | ✓01, 06, 29 |
| `tiktok-shop-affiliate-commissions` | 佣金 | 02, 07, 45 | ✓01, 02, 07, 08 |

### 4.2 Cluster A 制作 + Cluster E 格式（`tiktok-video/`）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `faceless-tiktok-shop-videos` | Production | 03, 05, 29 | 01, 03, 25, 31, 34, 42, 53, 56 |
| `tiktok-video-hooks` | **Framework** | 05, 08, 25 | 02, 03, 05, 08, 27, 30, 47, 50 |
| `tiktok-video-formats` | **Hub** | 25, 35–42, 03, 05 | 25, 26, 27, 35–42 |
| `tiktok-shop-video-script` | Framework | 05, 49, 50, 03 | ✓05, 07, 08, 25, 49 |
| `tiktok-shop-slideshow-compliance` | 合规 | 29, 35, 51 | ✓29, 35, 51 |
| #35–#42 各格式 spoke | Spoke | 25, 29, 27 | 25；△ 部分 spoke 入链=1 |

### 4.3 Cluster C — Content & Discovery

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `how-the-tiktok-algorithm-works` | **Hub** | 26, 05, 08, 47 | 25, 26, 27, 30, 47 |
| `tiktok-keyword-research` | Strategy | 06, 26, 27 | 26, 27, 35, 38, 42, 47 |
| `trending-tiktok-sounds` | Strategy | 05, 28, 30 | 28, 29, 38 |
| `tiktok-ai-content-rules` | **合规 Hub** | 29, 03, 55 | 29, 31–34, 52, 53, 55, 56, 57 |
| `how-to-use-tiktok-trends` | Strategy | 04, 28, 30 | △28 |
| `tiktok-shop-algorithm` | Shop 算法 | 26, 47, 08 | 26, 44, 47 |

### 4.4 Cluster B — Platform Ops

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `tiktok-shop-toolkit` | **Hub** | 12, 10, 14, 21 | 12, 20, 21, 45 |
| `tiktok-shop-performance-score` | **Hub** | 14, 08, 46 | 08, 14, 19, 21, 22, 44, 45, 46, 47 |
| `how-to-shop-on-tiktok-shop` | **Buyer Hub** | 18, 10, 43, 48 | 10, 18, 19, 43, 48 |
| `tiktok-shop-violation-appeal` | Ops | 46, 10, 51 | ✓46, 55 |
| `tiktok-shop-fees` | Ops | 45, 07, 58 | 07, 45, 58 |
| `tiktok-shop-account-health-rating` | Ops | 46, 14, 44 | 44, 46, 47, 51 |
| 其他 #10–#22 | Spoke | 各 Hub + 相关 spoke | 见 content-graph §4.2b |

### 4.5 Cluster D — E-commerce AI（根目录）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `ai-commerce-agent-ecommerce` | **Hub** | 31, 32, 34 | 31, 32, 34 |
| `ai-ugc-content-creator` | Production | 32, 33, 29 | 31, 32, 53 |
| `ai-custom-avatar-videos` | Production | 33, 29, 03 | 32, 33, 56 |
| `ai-ecommerce-video-workflow` | Framework | 34, 31, 03 | 31, 34, 53 |
| `ai-ugc-tiktok-shop-conversion` | Research | 32, 29, 03, 53 | ✓31, 32, 34, 53 |

### 4.6 Cluster F — Seasonal / Campaign（`seasonal-campaign/`）

| slug | 角色 | 应链向 | 应被链自 |
|------|------|--------|----------|
| `tiktok-shop-sales-calendar` | **Hub** | 01, 04, 05, 07, 08, 27, 30, 48, 49, 50, 52, 54, 57, 58, 60–68 | ✓48；#60–#68 spoke 链回 |
| `tiktok-shop-labor-day` | Spoke | 59, 49, 04, 05, 50, 61 | ✓59 |
| `tiktok-shop-september-restock` | Spoke | 59, 49, 04, 05, 52, 58, 60 | ✓59 |
| `tiktok-shop-back-to-school` | Spoke | 59, 49, 30, 05, 50, 27, 04 | ✓59 |
| `tiktok-shop-black-friday` | Spoke | 59, 49, 04, 05, 50, 58, 48, 08 | ✓59 |
| `tiktok-shop-holiday-gifts` | Spoke | 59, 63, 49, 05, 50, 54, 58 | ✓59 |
| `tiktok-shop-halloween` | Spoke | 59, 49, 05, 57, 29, 30 | ✓59 |
| `tiktok-shop-fall-deals` | Spoke | 59, 65, 49, 30, 05, 04 | ✓59 |
| `tiktok-shop-jumpstart` | Spoke | 59, 07, 49, 04, 05, 50 | ✓59 |
| `tiktok-shop-summer-sale` | Spoke | 59, 62, 49, 04, 05, 08 | ✓59 |

**Canonical 边界**：`tiktok-shop-promo-codes`（#48）= 买家券码与叠加规则；`tiktok-shop-sales-calendar`（#59）= affiliate **何时研究 / 拍摄 / 发布**；`tiktok-shop-black-friday`（#63）= BFCM 单窗口 deep dive；其余 #60–#62、#64–#68 = 各窗口 spoke，Hub 保留摘要 + link。

---

## 五、跨簇桥接（Context Bridge）

| 从 | 到 | 语境 |
|----|-----|------|
| A 制作 #03 | C #29 | faceless + AI 披露 |
| A #07 副业 | B #45 费用 | 到手佣金 vs 平台费栈 |
| A #08 诊断 | C #26 / #47 | 分发 vs Shop 算法 |
| E #25 格式 Hub | A #05 钩子 | 格式 ≠ 开场机制 |
| E #50 脚本 | A #49 niche | script vs product 前先定垂直 |
| E #55 slideshow | B #51 申诉 | 违规后恢复路径 |
| D #53 转化 | A #03 faceless | AI UGC 在 Shop 上的信任阈值 |
| A #54 Creator Rewards | A #07 Shop affiliate | 两车道择一 primary |
| B #18 买家 | B #43 legit | 买家信任入口 |
| A #01 Pillar | A #44 dropshipping | 收入地图 → dropshipping 现实 |
| F #59 日历 Hub | B #48 promo codes | 排期 vs 买家券码机制 |
| F #59 日历 Hub | A #49 niche | 季节 SKU 须在锁定垂直内 |
| F #59 日历 Hub | C #30 trends | 平台大促 + 内容趋势双层 |
| A #07 副业 | F #59 日历 | 90 天验证 → 季节 sprint 压缩版 |

---

## 六、推荐用户旅程

### 6.1 新 affiliate（零起步）

```
how-to-make-money-on-tiktok (#01)
  → tiktok-shop-setup (#02)
  → tiktok-shop-niche-selection (#49)
  → tiktok-product-research (#04)
  → faceless-tiktok-shop-videos (#03) 或 faceless-vs-face-tiktok-shop (#56)
  → tiktok-video-hooks (#05) → tiktok-shop-video-script (#50)
  → tiktok-shop-no-sales (#08)  （卡住时）
```

### 6.2 内容 / 算法优化

```
how-the-tiktok-algorithm-works (#26)
  → tiktok-shop-algorithm (#47)
  → tiktok-keyword-research (#27)
  → tiktok-video-formats (#25) → 格式 Spoke (#35–#42)
  → trending-tiktok-sounds (#28) → how-to-use-tiktok-trends (#30)
```

### 6.3 AI 生产栈

```
ai-commerce-agent-ecommerce (#31)
  → ai-ugc-content-creator (#32) → ai-custom-avatar-videos (#33)
  → ai-ecommerce-video-workflow (#34)
  → ai-ugc-tiktok-shop-conversion (#53)
  → tiktok-ai-content-rules (#29) + tiktok-shop-affiliate-disclosure (#57)
```

### 6.4 Creator Rewards 车道（非 Shop）

```
how-to-make-money-on-tiktok (#01)
  → tiktok-creator-rewards-guide (#54)
  → tiktok-keyword-research (#27)  （search value / 长视频）
```

### 6.5 季节 / Q4 大促（affiliate 排期）

```
tiktok-shop-niche-selection (#49)
  → tiktok-product-research (#04) → tiktok-shop-free-samples (#52)
  → tiktok-shop-sales-calendar (#59)  ← Hub：全年窗口 + 两周 prep
  → tiktok-shop-labor-day (#60) → tiktok-shop-september-restock (#61)
  → tiktok-shop-back-to-school (#62) · tiktok-shop-halloween (#65) · tiktok-shop-fall-deals (#66)
  → tiktok-shop-black-friday (#63) → tiktok-shop-holiday-gifts (#64)
  → tiktok-video-hooks (#05) → tiktok-shop-video-script (#50)
  → tiktok-shop-no-sales (#08)  （窗口内仍零转化时）
```

H1 窗口：`tiktok-shop-jumpstart (#67)` · `tiktok-shop-summer-sale (#68)` → 链回 #59。

---

## 七、内链现状快照（2026-08-24 · 全库 R1–R4 PASS）

> 统计口径：frontmatter 之后正文中 `](/blog/{slug})` 链接；`link_audit.py` 验证 R3/R4 = 0。创作规范见 [`internal-links.md`](../skills/blog-article/references/internal-links.md)。

### 7.1 零入链 — ~~优先补链~~ ✅ 已补（#50–#58 新簇）

| NN | slug | 入链来源（已加） |
|----|------|----------------|
| 50 | `tiktok-shop-video-script` | #05 hooks、#25 formats、#07 side hustle |
| 52 | `tiktok-shop-free-samples` | #04 product-research、#07 side hustle |
| 53 | `ai-ugc-tiktok-shop-conversion` | #32 UGC、#31 agent hub |
| 55 | `tiktok-shop-slideshow-compliance` | #35 photo-posts、#29 AI rules |
| 56 | `faceless-vs-face-tiktok-shop` | #03 faceless、#07 FAQ |
| 57 | `tiktok-shop-affiliate-disclosure` | #06 captions、#29 AI rules |
| 58 | `tiktok-shop-affiliate-commissions` | #07 side hustle、#02 setup |

### 7.2 入链薄弱（=1）— ✅ 已补第二条入链

| slug | 新增入链来源 |
|------|-------------|
| `tiktok-creator-rewards-guide` | #07 side hustle、#27 keyword（原 #01） |
| `tiktok-shop-violation-appeal` | #46 AHR（原 #55） |
| `tiktok-shop-dropshipping` | #02 setup（原 #01） |
| `tiktok-giveaway` | #14 SPS（原 #21） |
| `tiktok-pov-marketing` | #36 storytime（原 #25） |
| `tiktok-duet-stitch` | #30 trends（原 #25） |
| `tiktok-green-screen` | #03 faceless（原 #25） |
| `is-tiktok-shop-legit` | #45 fees（原 #18） |
| `tiktok-shop-promo-codes` | #45 fees（原 #18） |

### 7.3 高入链 Hub（维护时优先从此处链出新文）

| slug | 入链约数 | 角色 |
|------|:--------:|------|
| `how-to-make-money-on-tiktok` | 18+ | Pillar |
| `tiktok-video-hooks` | 16+ | Framework |
| `tiktok-ai-content-rules` | 15+ | 合规 Hub |
| `tiktok-video-formats` | 11+ | 格式 Hub |
| `tiktok-product-research` | 13+ | 选品 |

### 7.4 §4 出站链 + §6 旅程审计（2026-08-24 ✅）

**#49–#58 出站**：矩阵「应链向」列已覆盖；补链项 — #54→#27 keyword、#53→#57 disclosure、#34→#53 转化验证。

**§6.1 新 affiliate 旅程** `#01→#02→#49→#04→#03/#56→#05→#50→#08`：

| 步骤 | 状态 |
|------|------|
| #01→#49 | ✅ Pillar 零起步段 |
| #02→#49 | ✅ Setup marketplace 段 |
| #04→#49 | ✅ 选品四信号段 |
| #49→#56 | ✅ 垂直化后 production 决策 |
| #49→#05 | ✅ Week 1 hooks |
| #50→#08 | ✅ 脚本测试后诊断 |
| #08→#49/#50/#58 | ✅ 分发/脚本/佣金瓶颈 |

**§6.3 AI 栈** `#31→#32→#34→#53→#29+#57`：#34→#53、#53→#57 已补。

### 7.5 Cluster F 入链（2026-08-24 · #59–#68 + Hub 外入链）

| slug | 入链来源 |
|------|----------|
| `tiktok-shop-sales-calendar` | #60–#68 spoke 链回；#01 Pillar 年度规划 |
| `tiktok-shop-labor-day` | ✓#59、#61；**#49** niche 季节性 |
| `tiktok-shop-september-restock` | ✓#59、#60；**#04** product-research |
| `tiktok-shop-back-to-school` | ✓#59、#68；**#30** trends |
| `tiktok-shop-black-friday` | ✓#59、#64；**#05** hooks、**#08** no-sales |
| `tiktok-shop-holiday-gifts` | ✓#59、#63；**#07** side hustle |
| `tiktok-shop-halloween` | ✓#59、#66；**#05** hooks |
| `tiktok-shop-fall-deals` | ✓#59、#65；**#01** Pillar |
| `tiktok-shop-jumpstart` | ✓#59；**#49** niche、**#07** side hustle |
| `tiktok-shop-summer-sale` | ✓#59、#62；**#04** product-research |

**审计**：9/9 spoke 均有 ≥1 条簇外 Hub 入链；零入链 / 单入链 slug = 0。

---

## 八、新文入簇检查清单

1. 在 [`content-graph.md`](../skills/blog-article/references/content-graph.md) §4.1 登记 NN / folder / slug / Canonical 边界  
2. 更新 [`README.md`](./README.md) 文章表  
3. 更新**本文** §4 矩阵 + §7 快照  
4. Phase 3 Outline：对照 §4「应链向」列规划内链；Phase 3.5 交叉检查同批互链  
5. 从 §7.3 Hub 挑 2–3 篇加**自然入链**到新 slug  
6. 跑 `python ../skills/blog-article/tools/link_checker.py {file}`  
7. 跑 `word_count_narrative.py` 按类型校验字数  

---

## 九、维护节奏

| 时机 | 动作 |
|------|------|
| 每篇新稿发布前 | link_checker + 对照 §4 应链向 |
| 每批 ≥3 篇新稿后 | 扫 §7 零入链表，补 1 条/篇 |
| T+30 发布复盘 | GSC top queries → 决定是否 MERGE 或加 FAQ 内链 |
| 策略变更 | bump content-graph + 本文「最后更新」日期 |

---

*Moras blog · blog-structure-internal-links · v1.3 · 2026-08-24（全库 R1–R4 PASS + Cluster F Hub 外入链）*
