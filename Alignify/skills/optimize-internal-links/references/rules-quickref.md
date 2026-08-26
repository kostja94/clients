# 规则速查 · 违规修复 · 附录 B 用法

> **权威 SSOT**：[`../../create-article/rules/internal-links.md`](../../create-article/rules/internal-links.md) Part 1–3 · Marketing [`../../create-article/rules/marketing-internal-links.md`](../../create-article/rules/marketing-internal-links.md)

---

## R-TLDR + R1–R7

| 规则 | 要求 | 严重度 |
|------|------|--------|
| R-TLDR-1 | TLDR 块 ≤2 distinct slug；Hub 建议 0–1 | high |
| R-TLDR-2 | TLDR 相邻两链间距 ≥40 字符 | high |
| R-TLDR-3 | TLDR slug 不得再出现在 section/html | high |
| R1 | 同 URL 全文 1 次；无机械指路链；**无 distinct 下限** | medium |
| R2 | 单屏密度 ≤3（400 词 / 250 字窗口） | medium |
| R3 | tools↔tools 预留跨板块（低优先级） | low |
| R4 | 同一目标 slug 全文仅一次 | high |
| R5 | 锚文本覆盖目标页核心语义 | 人工 |
| R6 | 锚 ≥2 汉字 / ≥1 英文词；禁 click here | medium |
| R7 | FAQ 无内链（md `#faq` 7 问 plain text） | high |
| **R-LINK-ONLY** | 存量修复只改 `<a>`；禁止整段重写结论 | **阻断** |

**Hub 页**：核心要点纯文本列子品类；首次链放在「什么是」第二段。

---

## 违规 → 修复

| 规则 | 违规 | 修复 |
|------|------|------|
| R1 | 机械指路链 / 同段堆链 | 改为任务句内链；每段 ≤1 |
| R2 | 密度窗口 >3 链 | 分散或删弱相关链 |
| R4 | 重复 slug | unwrap 重复 `<a>`；FAQ 与正文 slug 不重复 |
| R5–R6 | 锚文本差 | keywords 表 / 描述性策略名 |
| R7 | FAQ 含链 | 删 `<a>`，保留 plain text |

---

## URL 模式

| 语言 | 存量 Tools | 新文 Blog | 存量 Marketing/SEO |
|------|-----------|-----------|-------------------|
| EN | `/tools/{slug}` | `/blog/{slug}` | `/marketing/` · `/seo/` 等 |
| ZH | `/zh/tools/{slug}` | `/zh/blog/{slug}` | `/zh/marketing/` 等 |

新文任意类型 → `/blog/{slug}`；旧 URL 不重迁。

---

## 邻居选题

1. **附录 B**（`internal-links.md`）相邻 Tools 行
2. [`knowledge/tools/territory-map.md`](../../../knowledge/tools/territory-map.md) 同 Territory
3. 全站快照 [`site-structure-internal-links.md`](./site-structure-internal-links.md) 高入链 Hub
4. 不足时自拟，后续补 keywords

---

## 排期

**快照队列**（[`site-structure-internal-links.md`](./site-structure-internal-links.md) §五）：P0（结构性违规）→ P1（零入链 Hub）→ P2（零出链）→ P3（观察项）

**Tools slug 批次**（SSOT §1.5.7）：Wave 0 Blog Tools → P0 Agent 执行链 → P1 高流量 → P2 中流量 → P3 长尾
