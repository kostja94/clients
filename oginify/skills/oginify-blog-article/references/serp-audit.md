# Oginify SERP Audit — SERP Fit 与信息增量

> 加载时机：Phase 0R / Phase 5
> 主文件：SKILL.md §3.0R 指针

---

## 1. SERP Fit 审计（Phase 0R 执行）

对 primary keyword 做 R2 搜索后，填入：

```
## SERP Fit — {keyword}

| 项 | 值 |
|----|-----|
| Keyword | {primary keyword} |
| Intent | Informational | Commercial | Transactional |
| Top 1 | {URL + title} |
| Top 2 | {URL + title} |
| Top 3 | {URL + title} |
| PAA (People Also Ask) | 1. … 2. … 3. … |
| Reader gap | Top3 未回答的问题 |
| Our differentiation | {≥1 独有增量} |
| Gate 0R | PASS / FAIL（One-line thesis 不得与 Top5 同句） |
```

---

## 2. 信息增量审计（Phase 5 — 高竞争词必做）

| 指标 | 计算 | 阈值 |
|------|------|------|
| Redundancy Ratio | 与 SERP Top3 重复的段落数 / 总段落数 | 高竞争词 ≤30%；超则 STOP 或改角度 |
| Unique Content Ratio | 独有框架/分类法/对比维度占比 | ≥40%（flagship） |

**高竞争词判定**：Top3 均为权威域（大平台/大品牌）或内容高度同质 → 高竞争。

**STOP 条件**：高竞争词 + Redundancy >30% → STOP（改选题或 MERGE）。

---

## 3. PAA 使用（FAQ 题源）

- FAQ 题目优先来自 R2 的 PAA + 内容相关补充
- 至少 1 题覆盖 objection（"Do I still need og:image if I have a hero image?" 等）
- 禁止通用模板题（"What is AI?" 等）

---

## 4. Meta 清单（Phase 5）

| 项 | 标准 |
|----|------|
| Title | 45–65 chars；含主关键词；可含 2026 |
| Description | 120–160 chars；benefit + intent；主词前 80 chars |
| H1 | 与 title 呼应但可略长；含主关键词 |
| Slug | Gate B 全 Pass（见 slug-gate.md） |
| Snippet-ready | TL;DR bullet 1 = 40–60 词定义句，可独立成 snippet |
