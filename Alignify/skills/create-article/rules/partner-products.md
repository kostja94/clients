# 客户产品在 Tools / Blog 文章中的处理规则

> **版本**：v1.0 · 2026-06-24  
> **适用范围**：`content/tools/`、`content/blog/` 中 **Markdown `###` 产品块**（原 JSON `bestTools` 字段）、对比表、TL;DR、FAQ、结论等产品露出。  
> **术语**：下文 `bestTools` = 正文产品 H3 段，**非**已删 JSON block 类型。
> **与选品规则的关系**：产品**如何选**见 [`sections.md` Part 3.3](./sections.md#part-33-best-产品-h3best-ranking) 与 KB `knowledge/tools/{slug}.md`；本文只规定**客户身份**如何影响增删与保留。  
> **客户名单来源**：部署仓 `alignify-by-kostja/app/[locale]/customer-stories/page.tsx`（Featured + 分类列表；页面营销口径「80+」为总量，下表为页内显式列出的品牌）。

---

## 一、三层规则（速查）

| 层级 | 谁 | 新增 | 保留 | 突出 |
|------|-----|------|------|------|
| **Tier 0** | 非客户 / 普通编辑选品 | 仅按 KB 形态谱系 + bestTools 规范 | 按 KB 与编辑判断 | 无 |
| **Tier 1** | Customer Stories 列表客户 | ❌ **不得**仅因「是客户」加入 bestTools | ✅ 已在页内则**不得删除或悄然降级** | 无硬性排位 |
| **Tier 2** | 合同 / 战略客户 | 同 Tier 1；slug 相关时**应**在 KB 与页内体现 | ✅ 必须保留 | ✅ bestTools **靠前**、对比表、TL;DR/FAQ 须有露出 |

**允许移除 Tier 1 / Tier 2 产品的唯一理由**（须在 PR / 变更说明中写一句）：

1. 产品已关闭或域名失效  
2. 明确不属于本 slug（相邻品类分流）  
3. KB 主卡层已正式移出，且 **非 Tier 2**

**禁止**：

- 为给第三方腾位而删除 Tier 1/2 客户  
- 把 Customer Stories 全表同步进某一 slug 的 bestTools  
- 仅因客户身份把 KB「非 bestTools 横评参考」产品升为主卡（Tier 2 除外）

---

## 二、Tier 2 — 合同 / 战略客户

| 产品 | 域名 | 相关 slug | 露出要求 |
|------|------|-----------|----------|
| **Utell AI** | utell.ai | `accent-conversion`、`audio-translator`；`voice` hub 可列 integrations | bestTools 靠前；对比表；TL;DR / 结论 / FAQ 至少一处点名 |
| **TemPolor** / TemPolor AI | tempolor.com | `music-generator` | 同上 |

Tier 2 名单由运营维护；变更时同步改本节表格。

---

## 三、Tier 1 — Customer Stories 客户引用

下列品牌来自 Customer Stories 页（Featured 6 + 五类列表）。**默认 Tier 1**：保留型，不主动新增。

**图例（Tools 露出，2026-06-24 快照）**

- **BT** = 已在至少一个 slug 的 `bestTools` 中  
- **页内** = 在 Tools JSON 其他区块（正文 / FAQ / 对比表等）出现，但不在 bestTools  
- **—** = 当前 Tools 内容中未出现（符合「不主动加」）

### Featured（精选案例 6）

| 产品 | 域名 | Tier | Tools 露出 | 备注 |
|------|------|------|------------|------|
| Tunee | tunee.ai | 1 | — | 音乐 Agent；KB `music-video-generator` 有提及，Tools 页暂无 |
| VoiSpark | voispark.com | 1 | **BT** `text-to-speech`, `voice` | |
| Lessie AI | lessie.ai | 1 | **BT** `b2b`, `influencer-marketing`, `recruiting`, `fundraising` | |
| Medeo AI | medeo.app | 1 | **BT** `story-generator`, `video` | |
| Final Round AI | finalroundai.com | 1 | **BT** `interview-assistant` | |
| ThetaWave | thetawave.ai | 1 | **BT** `notes-generator` | |

### Voice

| 产品 | 域名 | Tier | Tools 露出 | 备注 |
|------|------|------|------------|------|
| Dubbing AI | dubbingai.io | 1 | **BT** `voice-changer` | |
| Utell AI | utell.ai | **2** | **BT** `accent-conversion`, `audio-translator`, `voice` | 见 §二 |
| Tunee | tunee.ai | 1 | — | 同上 Featured |
| TemPolor AI | tempolor.com | **2** | **BT** `music-generator` | 见 §二 |
| VoiSpark | voispark.com | 1 | **BT** `text-to-speech`, `voice` | 同上 Featured |

### Image

| 产品 | 域名 | Tier | Tools 露出 | 备注 |
|------|------|------|------------|------|
| PatternLook | patternlook.com | 1 | — | |
| Molypix AI | molypix.ai | 1 | **BT** `design`, `poster-generator` | |
| SellerPic | sellerpic.ai | 1 | — | |
| Kaze.ai | kaze.ai | 1 | — | |
| Vofy | vofy.art | 1 | — | |

### Video

| 产品 | 域名 | Tier | Tools 露出 | 备注 |
|------|------|------|------------|------|
| GoEnhance AI | goenhance.ai | 1 | **BT** `animation-generator`, `video-to-video`, `video-effects`, `video-generator`, `video` 等 | |
| Vozo AI | vozo.ai | 1 | **BT** `video-translator`, `lip-sync`, `video` | |
| Topview AI | topview.ai | 1 | **BT** `avatar`, `lip-sync`, `short-drama`, `video`, `voice` | |

### Industry

| 产品 | 域名 | Tier | Tools 露出 | 备注 |
|------|------|------|------------|------|
| Collov AI | collov.ai | 1 | **BT** `virtual-staging`, `image` | |
| Edensign | edensign.io | 1 | **BT** `virtual-staging`, `image` | |
| BeFreed AI | befreed.ai | 1 | — | |
| Powerdrill AI | powerdrill.ai | 1 | — | |
| RockFlow | rockflow.ai | 1 | — | |
| Clacky AI | clacky.ai | 1 | **BT** `ide` | |
| DolphinRadar | dolphinradar.com | 1 | — | |
| Pine AI | 19pine.ai | 1 | — | |
| Artlas | artlas.art | 1 | — | |
| Openmart | openmart.com | 1 | **BT** `lead-generation` | |
| ThetaWave | thetawave.ai | 1 | **BT** `notes-generator` | 同上 Featured |
| Nori | heynori.com | 1 | **BT** `family-assistant` | |
| Dynal | dynal.ai | 1 | **BT** `linkedin` | |
| Final Round AI | finalroundai.com | 1 | **BT** `interview-assistant` | 同上 Featured |

### Agent

| 产品 | 域名 | Tier | Tools 露出 | 备注 |
|------|------|------|------------|------|
| hiData | hidata.ai | 1 | — | |
| Medeo AI | medeo.app | 1 | **BT** `story-generator`, `video` | 同上 Featured |
| Crepal AI | crepal.ai | 1 | — | |
| Fellou AI | fellou.ai | 1 | **BT** `browser` | |
| Simular AI | simular.ai | 1 | **BT** `agent-for-desktop` | |
| Karis | karis.im | 1 | **BT** `geo` | |
| Hellyeah | hellyeahai.com | 1 | — | |
| MeDo | medo.dev | 1 | **BT** `vibe-coding` | |
| Datus | datus.ai | 1 | — | |
| Moras | moras.ai | 1 | — | |
| Floatboat | floatboat.ai | 1 | **BT** `agent-for-desktop` | |
| Lessie AI | lessie.ai | 1 | **BT** `b2b`, `influencer-marketing`, `recruiting`, `fundraising` | 同上 Featured |

---

## 四、编辑 / Agent 操作清单

创建或优化 Tools / Blog 文章时，在 bestTools 定稿前核对：

- [ ] 新增产品是否**仅**因 Customer Stories，而 KB 形态谱系不需要？→ 若是，**不要加**（Tier 2 除外）
- [ ] 本次 diff 是否从 bestTools / 对比表 / TL;DR 中**删掉** §三或 §二 中的域名？→ 若是，对照 Tier 与 §一移除理由
- [ ] Tier 2 是否仍在目标 slug 的 bestTools **前段**且有对比表或摘要点名？
- [ ] 普通选品是否仍服从 KB「与站内 bestTools 一致」主卡层 + [best-tools.md](./sections/best-tools.md) 字数规则？

---

## 五、与 create-tools-article 流程的衔接

| 步骤 | 读本节 |
|------|--------|
| Step 2 — 从 KB 提取 BestTools | §一 Tier 0；新增前查 §三是否已「—」→ 不主动加 |
| Step 2 — 优化已有 Tools 页 | §一 Tier 1/2 保留；§三查当前 slug 是否有客户 |
| Step 5 — 质检 | §四 清单 |

**Customer Stories 页更新时**：同步复审 §三表格「Tools 露出」列（不必每次发版都改，批量优化或新增客户后更新即可）。

---

*partner-products · v1.0 · 2026-06-24*
