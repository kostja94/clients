# Internal & External Links Checklist（Collov AI Blog）

> **依据**：与 [Dubbing AI blog](../../dubbingai/blog/internal-external-links-checklist.md)、[ThetaWave blog](../../thetawave/blog/internal-external-links-checklist.md) 同一思路；站点以 **collov.ai** 为准；正文为 **英文**，本规范为 **中文**。  
> **信息增量**：成稿前对照仓库根目录 [内容-信息增量-笔记.md](../../../内容-信息增量-笔记.md) —— 先满足主意图，再叠加可验证的新信息（步骤、边界条件、清单），避免仅复述 SERP 共识层。  
> **产品语境**：[collov.md](../collov.md) · **关键词**：[collov-keywords.md](../collov-keywords.md) · **功能 URL**：[collov-features.md](../collov-features.md)

---

## 链接分层（Collov AI Blog）

| 类型 | 路径 / URL | 用途 |
|------|------------|------|
| **Blog 互链** | `https://collov.ai/blog/{slug}` | 相关主题；与 **frontmatter `related`** 一致 |
| **核心转化** | `https://collov.ai/`、`https://collov.ai/pricing` | 首页、定价 |
| **虚拟软装主线** | `/virtual-staging-ai`、`/virtual-staging` | 产品主入口、品类页 |
| **Solutions / Persona** | `/real-estate`、`/designer`、`/homeowner` | 与稿内受众一致时链 |
| **高频工具线** | `/add-furniture`、`/change-seasons`、`/360-panorama-generator`、`/ai-virtual-tour-generator` | 与稿内任务一致时分散插入 |
| **延伸工具** | `/furniture-finder`、`/design-callout`、`/moodboard-generator` | 功能已上线且稿内提及时链（见 collov-features.md） |
| **API / 企业** | `https://collov.ai/API` 或官方 API 文档 URL | 开发者、Enterprise 语境 |
| **站内对比博文** | `/blog/choosing-ai-virtual-staging-for-real-estate-2026-comparison` | 平台对比矩阵；与 **best-of / how-to / vs traditional** 分流 |

---

## Internal Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **首段或第二段** | ≥1 条 | **Blog 互链**（意图分流）或 **virtual-staging-ai / pricing**，避免与同意图 pillar cannibalize |
| **Body Blog 互链** | 每篇 **1–4 条** | 链至 **`/blog/{slug}`**；锚文本区分 *software roundup* vs *cost/MLS/traditional* vs *comparison matrix* |
| **产品 / 转化内链** | 按 **H2** 分散 | **virtual-staging-ai、pricing、real-estate** 等忌同段堆砌；每 URL 全文不宜重复过多 |
| **文末 Next steps** | `related` + 正文一致 | 至少 1 条 blog + 1 条产品或定价 |
| **锚文本** | 描述性 | 避免 "click here"；可混合 exact keyword / partial / **Collov AI** |

---

## External Links 规范

| 要求 | 目标 | 说明 |
|------|------|------|
| **权威 / 政策** | 按需 **2–6 条** | MLS、协会、监管或知名媒体；**可核对**；`rel="nofollow noopener"` 按法务与站点惯例 |
| **数据 / 研究** | 注明出处 | 统计类句子尽量带来源；避免不可验证的绝对化因果 |
| **竞品** | 对比稿 | 与 [collov-competitors.md](../collov-competitors.md) 一致；锚文本用公司名 |

---

## 博文互链矩阵（Blog ↔ Blog）

| slug | 建议指向（正文至少 1 次锚文本） |
|------|----------------------------------|
| `best-virtual-staging-software` | → `virtual-staging-vs-traditional-staging`（成本/披露/实体 vs 数字）· → `choosing-ai-virtual-staging-for-real-estate-2026-comparison`（平台对比，若已发布） |
| `virtual-staging-vs-traditional-staging` | → `best-virtual-staging-software`（选工具）· → `choosing-ai-virtual-staging-for-real-estate-2026-comparison`（矩阵） |
| `choosing-ai-virtual-staging-for-real-estate-2026-comparison`（站内已发布则纳入） | → `best-virtual-staging-software` · → `virtual-staging-vs-traditional-staging` |

**意图三角**：**best-of** = 软件选型；**vs traditional** = 成本、买家心理、MLS、混合打法；**choosing… comparison** = 多平台参数对照。

---

## 文章链接状态

新稿入库后在 [README.md](./README.md) 登记表补充一行，并更新下表。

| # | 文章 slug | 内链 Body（Blog+产品） | `related` | 外链 | 已优化 |
|---|-----------|-------------------------|-----------|------|--------|
| 01 | `best-virtual-staging-software` | ✅ | `virtual-staging-vs-traditional-staging`, `choosing-ai-virtual-staging-for-real-estate-2026-comparison` | 竞品站按需 | ✅ |
| 02 | `virtual-staging-vs-traditional-staging` | ✅ | `best-virtual-staging-software`, `choosing-ai-virtual-staging-for-real-estate-2026-comparison` | MLS/NAR/媒体按需 | ✅ |

---

## 规范总结

- **内链**：首段分流 + Body blog 互链 + 产品页按节分布；新文上线后**回写**旧文 `related` 与一句互链。  
- **外链**：政策与数据可追溯；竞品 **nofollow**。  
- **信息增量**：简报中写明相对 SERP 共识层的**新增点**（清单、反例、可执行步骤）；参见 [内容-信息增量-笔记.md](../../../内容-信息增量-笔记.md)。
