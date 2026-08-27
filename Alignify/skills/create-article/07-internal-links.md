# Step 7 — 内链 & Internal Link Plan

> **SSOT**：[`rules/internal-links.md`](./rules/internal-links.md)  
> **全类型必读**：Part 1–2（编辑层 + R1–R7）· Part 8（外链 UTM/Nofollow）  
> **按类型追加**（见下表 · 一次只多读 **1 个** Part，遵守渐进加载）  
> **存量批量优化**：Part 6–7 → [`optimize-internal-links`](../optimize-internal-links/SKILL.md)，**非**本 Step

---

## 按 articleType 阅读路径

| articleType | 追加 Part | 锚点 |
|-------------|-----------|------|
| `best-ranking` · `best-ranking-legacy` | **Part 3** Tools（R1–R7 · 邻居矩阵 · FAQ 试点） | [Part 3](./rules/internal-links.md#part-3-tools-类目) |
| `marketing-strategy` | **Part 4.5** M1–M11 | [Part 4.5](./rules/internal-links.md#part-45-marketing-频道内链) |
| `seo-guide` | **Part 4** SEO 频道 | [Part 4](./rules/internal-links.md#part-4-seo-频道内链) |
| `insights-analysis` | **Part 5** Insights / 其他 | [Part 5](./rules/internal-links.md#part-5-insights--其他频道) |

Brief 中的 `articleType` 决定上表行；写 Tools 型 blog 新文仍走 Part 3（非仅 legacy）。

---

## 分布原则（无硬性条数）

| 区块 | 建议 |
|------|------|
| 核心要点 intro | 0–1 链 |
| 什么是 · 主体段 | 链嵌任务句；**每段 ≤1 链** |
| 应用场景 / 如何选择 | 0–1 链/段 |
| 结论 | **0–2** 链（见 [`sections.md`](./rules/sections.md) Part 4.4） |
| FAQ | **允许**站内链；**计入正文**；同 URL 全文 1 次（R4） |
| 全文 | **点击意图**优先，不为凑数加链 |

Brief 中 **Planned internal links** 记录预期互链与点击意图。**仅登记已上线 slug**（Gate G6）。

---

## Internal Link Plan（Flagship 交付物）

```markdown
## Internal Link Plan — {slug}

| # | 锚文本 | 目标 slug | 所在 section | 点击意图 |
|---|--------|-----------|--------------|----------|
| 1 | … | … | … | 读者此刻想搞清什么 |
```

ZH 定稿后 EN 须复用相同 distinct 目标（锚文本可本地化）。

---

## 检查

- [ ] 已读 Part 1–2 + 上表对应 **类型 Part** + Part 8
- [ ] 每条链过点击意图三问（Marketing 见 [Part 4.5 §一](./rules/internal-links.md#一第一原则读者想点click-intent)；Tools 见 Part 3 §1.3）
- [ ] FAQ 内链（若有）遵守 R4：同 URL 全页 1 次
- [ ] 同 URL 全页 1 次
- [ ] 正文外链 / References 须经 `addUtmToExternalLink()`（见 [Part 8](./rules/internal-links.md#part-8-外链utm-与-nofollow)）
- [ ] Link Plan 已产出

下一步：[08-meta-config.md](./08-meta-config.md)
