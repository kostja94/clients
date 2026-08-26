# Moras Blog — 选题 backlog

> **用途**：只记录**尚未成稿**或**下一批计划**的选题与关键词调研。  
> **不是**成稿索引——已发布/已 planned 文章以 [`README.md`](./README.md) 为准。  
> **不是**内链 SSOT——结构与互链以 [`blog-structure-internal-links.md`](./blog-structure-internal-links.md) 为准。  
> **Agent 登记**：成稿时在 [`content-graph.md`](../skills/blog-article/references/content-graph.md) §4.1 追加行；Skill 不自动改 README。

**Portfolio 现状**：**64 篇**（#01–#14、#16、#18–#68；#15/#17/#23/#24 已删/合并）  
**下一序号**：**#69** · 建议 `isoDate`：`2026-09-16`

---

## 文档分工（避免重复维护）

| 维护什么 | 唯一/主 SSOT | 同步副本（成稿后人工更新） |
|----------|-------------|---------------------------|
| NN / slug / isoDate / 主题 / 状态 | **README.md** 文章表 | — |
| Agent 用 NN 注册表、Canonical、下一序号 | **content-graph.md** §4.1 / §4.3 | README 文章表 |
| Cluster 树、内链矩阵、用户旅程、补链优先级 | **blog-structure-internal-links.md** | content-graph Hub-Spoke（策略层） |
| 文件夹路由 | **topic-cluster-layout.md** | blog-structure 树状图 |
| **未写选题**、关键词调研、批次规划 | **本文件** | 成稿后移入 README，从本文件删除或标 ✅ |
| 创作 Gate / Phase / 工具 | **moras-blog-article skill** | — |

**原则**：同一信息只在一处「起草/规划」；成稿后索引进 README + content-graph，内链规则进 blog-structure，**不要**在 backlog 里保留已与 README 重复的完整文章表。

---

## 已完成批次（归档 · 勿再当 backlog）

<details>
<summary>Cluster C #25–#30（2026-06-25 起 · 已全部 planned）</summary>

| NN | slug | 状态 |
|----|------|------|
| 25 | `/blog/tiktok-video-formats` | ✅ planned |
| 26 | `/blog/how-the-tiktok-algorithm-works` | ✅ planned |
| 27 | `/blog/tiktok-keyword-research` | ✅ planned |
| 28 | `/blog/trending-tiktok-sounds` | ✅ planned |
| 29 | `/blog/tiktok-ai-content-rules` | ✅ planned |
| 30 | `/blog/how-to-use-tiktok-trends` | ✅ planned |

原 §1 主选 6 篇 Brief 见 git 历史；边界已写入各成稿与 content-graph Canonical。
</details>

<details>
<summary>Cluster F #59–#68（Seasonal / Campaign · 2026-09-06 起 · 已全部 planned）</summary>

| NN | slug | 角色 |
|----|------|------|
| 59 | `/blog/tiktok-shop-sales-calendar` | Hub（evergreen · 每年更新正文） |
| 60 | `/blog/tiktok-shop-labor-day` | Spoke |
| 61 | `/blog/tiktok-shop-september-restock` | Spoke |
| 62 | `/blog/tiktok-shop-back-to-school` | Spoke |
| 63 | `/blog/tiktok-shop-black-friday` | Spoke（BFCM 旗舰） |
| 64 | `/blog/tiktok-shop-holiday-gifts` | Spoke |
| 65 | `/blog/tiktok-shop-halloween` | Spoke |
| 66 | `/blog/tiktok-shop-fall-deals` | Spoke |
| 67 | `/blog/tiktok-shop-jumpstart` | Spoke |
| 68 | `/blog/tiktok-shop-summer-sale` | Spoke |

Hub ↔ spoke 内链矩阵见 `blog-structure-internal-links.md` §4.6。
</details>

<details>
<summary>Cluster A 缺口簇 #49–#58（2026-08-27 起 · 已全部 planned）</summary>

见 [`README.md`](./README.md) #49–#58 行；Reddit/keyword 缺口分析已完成。
</details>

---

## 待写 backlog（#69+）

优先级按 **搜索缺口 × 与 Moras ICP 重合 × 不与 Canonical 互斥** 排序。

### P1 — Cluster F 延伸（H1 / 文化窗口）

| 优先 | 建议 NN | Working title | slug（evergreen） | 主关键词 | 边界 |
|------|---------|---------------|---------------------|---------|------|
| P1 | 69 | TikTok Shop Spring Sale Affiliate Guide | `/blog/tiktok-shop-spring-sale` | tiktok shop spring sale affiliate | Hub #59 摘要 + link；vs April Restock 可合并为一篇 |
| P2 | 70 | TikTok Shop Memorial Day Deals for Affiliates | `/blog/tiktok-shop-memorial-day` | tiktok shop memorial day deals | 户外 / patio；链 #59 #49 |
| P2 | 71 | TikTok Shop Valentine's Affiliate Playbook | `/blog/tiktok-shop-valentines` | tiktok shop valentines affiliate | 仅 beauty / gift 垂类；Feb Restock 语境 |

### P2 — 其他 Cluster（需 Phase 0 KEEP）

| 建议 | Working title | slug | 暂缓原因 |
|------|---------------|------|----------|
| — | How to Grow a TikTok Shop Account (Without Ads) | `/blog/how-to-grow-on-tiktok-shop` | 与 #26/#27/#05 易 cannibalize；须严格边界 |
| — | TikTok Shop Creator Account Types (Official / Marketing / Affiliate) | `/blog/tiktok-shop-creator-account-types` | 内部 [use-cases/platform-taxonomy.md](./use-cases/platform-taxonomy.md) 可转化；品牌/affiliate 双受众 |
| — | Open Collaboration Playbook for Brands | `/blog/tiktok-shop-open-collaboration` | 偏品牌 ICP；与 #09 重叠风险 |

### 明确不写（产品页 / 已有 Canonical）

| 候选 | 处置 |
|------|------|
| Promo codes 买家向 | #48 canonical |
| 全年 sales calendar | #59 Hub（evergreen，改文不改 slug） |
| link-to-video / UGC ad generator 等工具词 | 产品页 `/tiktok-video-generator` |
| 第二篇全片 script | #50 + #05 |
| `tiktok-shop-deals-for-you-days` | 原 #23 已删；若写须 affiliate 视角 + 新 angle |

---

## 调研信号（复用 · 2026）

| 信号 | 数据点 | 用途 |
|------|--------|------|
| TikTok 搜索量 | 查询 +174% YoY | #27 / 季节 spoke 标题 |
| 信息型关键词 | 高量词 73% 信息型 | Strategy / Framework 优先 |
| 趋势窗口 | 5K–20K 视频 band | #30 / Cluster F spoke 引用 |
| Q4 Shop GMV | BFCM 单周 $500M+（第三方） | #63 / #59 已引用 |

完整历史调研见本文件 git 历史 §0（2026-06 版）。

---

## 成稿后 checklist（每篇）

1. 写入 `moras/blog/{folder}/NN-{slug}.md`
2. 更新 **README.md** 文章表一行
3. 更新 **content-graph.md** §4.1（+ Canonical 若新概念）
4. 更新 **blog-structure-internal-links.md** §4 矩阵（若新 Cluster / 新 spoke）
5. 从**本 backlog** 删除或标 ✅ 对应行
6. 跑 `link_checker.py` + `word_count_narrative.py`

---

*Moras · blog-article-backlog · 2026-08-24 · portfolio 64 篇 · 下一篇 #69*
