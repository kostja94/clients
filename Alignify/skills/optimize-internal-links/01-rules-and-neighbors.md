# 规则速查与附录 B 用法

权威来源：[internal-links.md §3.1.5.4](../create-article/rules/internal-links.md#154-综合底线规则)

## R1–R7 + R-TLDR（部署仓 `audit-tldr-adjacent-links.py`）

| 规则 | 要求 | 严重度 |
|------|------|--------|
| R-TLDR-1 | TLDR 块 ≤2 distinct slug；**创建/Hub 建议 0–1** | high |
| R-TLDR-2 | TLDR 相邻两链间距 ≥40 字符 | high |
| R-TLDR-3 | TLDR slug 不得再出现在 section/html | high |
| R1 | distinct 站内链 ≥ 5 | high |
| R2 | 单屏密度 ≤ 3（400 词 / 250 字窗口） | medium |
| R3 | tools↔tools ≤ 总配额 70%（预留跨板块） | low |
| R4 | 同一目标 slug 全文仅一次 | high |
| R5 | 锚文本覆盖目标页核心语义 | 人工 |
| R6 | 锚 ≥ 2 汉字 / ≥ 1 英文词；禁「点击这里」 | medium |
| R7 | FAQ ≤3 distinct slug，与正文去重；单答 ≤2 链 | high |
| **R-LINK-ONLY** | 存量修复只改 `<a>`；锚文本改纯文本不算删字；禁止整段重写 | **阻断**（`audit:text-regression`） |

**Hub 页**（`voice`、`image` 等）：核心要点纯文本列子品类；首次 `<a>` 放在「什么是」第二段。见 [`create-article/07-internal-links.md`](../create-article/07-internal-links.md)。

## URL 模式

| 语言 | Tools | Blog（routeCategory: tools） |
|------|-------|------------------------------|
| EN | `/tools/{slug}` | `/blog/{slug}` |
| ZH | `/zh/tools/{slug}` | `/zh/blog/{slug}` |

Blog 文可混链 `/tools/` 与 `/blog/`；Blog 型 slug：`agent-sandbox`、`inference-infrastructure`、`ai-training-data`、`data-engineering-agent`、`medical-scribe`、`web-fetch`。

## 邻居选题

1. **附录 B** 相邻 Tools 行（优先）
2. [alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点段
3. [territory-map.md](../../knowledge/tools/territory-map.md) 同 Territory 辐条
4. 不足时自拟，后续补 keywords

## 排期

见专册 **§1.5.7**：P0 → P1 → P2 → P3。
