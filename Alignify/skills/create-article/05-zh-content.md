# Step 5 — 创建中文 Markdown

> **前置**：Brief 定稿 + Gate 0R Pass  
> **产出**：`content/{channel}/zh/{slug}.md`  
> **规范**：[`rules/presentation.md`](./rules/presentation.md) · [`rules/extractability-checklist.md`](./rules/extractability-checklist.md)

---

## Gate B（动笔前）

- [ ] Article Brief 已锁定（Moat + Answer Blocks 3–5）
- [ ] Planned H2 与 Brief 一致
- [ ] **Outline 3.5**（同批 ≥2 篇）：[`outline-cross-check.md`](./rules/outline-cross-check.md) Pass 或 `N/A`

---

## 路径

| articleType | 路径 |
|-------------|------|
| best-ranking | `content/blog/zh/{slug}.md` |
| best-ranking-legacy | `content/tools/zh/{slug}.md` |
| seo-guide | `content/blog/zh/{slug}.md`（新文）；存量 `content/seo/zh/{slug}.md` |
| marketing-strategy | `content/blog/zh/{slug}.md`（新文）；存量 `content/marketing/zh/{slug}.md` |
| insights-analysis | `content/blog/zh/{slug}.md`（新文）；存量 `content/insights/zh/{slug}.md` |

---

## 起草协议（Flagship）

1. 按 Brief **Answer Blocks** 顺序写 major H2；每节首段 **BLUF**（先答后背景）
2. Moat Asset **至少 1 项**须在正文显式兑现（非 footnote）
3. **Author POV**（Brief）至少 1 处 **第一人称**判断段（建议独立 H2 或结论前）
4. TL;DR intro 40–80 字直接回答 primary keyword
5. FAQ **7 问** — 首句即答，与正文相似度 <30%
6. 段落优先 — 禁伪列表（见 `presentation.md`）
7. 节规范按实际采用的节查阅 `rules/sections/`

### 05b 深度扩写（动笔后、Step 06 前）

- 每 major H2 含 **事实 + 场景 + 判断** 中至少两类（见 `localization-quality.md` §3.3）
- 对照 [`templates/marketing.md`](./rules/templates/marketing.md) 节级建议区间；**不足则补论证**，不堆同义句
- 从 SSOT 抽**事件时间线**与**可核实数字**，勿只留表格摘要

**Best-ranking Meta**（Step 8 注册）：title 含「最佳」+ `（2026）`；H1 不含最佳/年份

---

## 禁止

- 偏离 Brief One-line thesis / Moat
- 从知识块整段复制
- frontmatter `howTo:`
- JSON 注入 TL;DR / FAQ / References

---

## A 层检查

- [ ] 主体节覆盖 Brief
- [ ] 若有结论 + FAQ → 结论在 FAQ 前
- [ ] FAQ 7 问、无内链
- [ ] Moat 已兑现

下一步：[06-localize-zh.md](./06-localize-zh.md)
