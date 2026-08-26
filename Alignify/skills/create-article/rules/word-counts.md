# 各章节字数硬底线与建议区间

> **Flagship**：除下表节级底线外，全文叙事须**内容饱满**（场景 + 事件 + 判断），Brief `word count target` 为参考；**禁止**为凑字加空话。  
> **Marketing / Blog 策略文**（叙事正文 md）：建议 ZH **≥2,800 汉字** / EN **≥2,000 words** — 低于此通常说明节内缺场景或判断，须扩写而非堆词。Tools 榜单文 ZH **≥3500 字** / EN **≥2800 words**（不含 frontmatter）。  
> **地道化**：见 [`localization-quality.md`](./localization-quality.md)  
> **版本**：v2.2 · 2026-08-26

---

## 一、中文页面

| 章节 | 硬底线 | 建议区间 | 说明 |
|------|--------|---------|------|
| blogLayout excerpt | 三段式 | 80–150 字 | 避免通用结尾；与 meta description 主题一致 |
| TL;DR introduction | 40 字 | 40–80 字 | 不足则摘要价值不足 |
| TL;DR items | ×4 条 | 4–5 条 | 每条 8–25 字 |
| 什么是 XXX | 2 段 | 3–4 段（180–380 字） | ≥2 段否则信息量不足 |
| 如何工作 technologyBase | 220 字 | 220–420 字 | 不足则技术深度不够 |
| 如何工作 advantages | ×3 项 | 3–5 项 | 每项 name + description |
| BestTools shortDescription | 4 字 | 6–18 字 | <4 字被截断 |
| BestTools description | 100 字 | 180–260 字 | <100 字内容质量不达标 |
| 应用场景 cases | ×3 个 | 4–6 个 | 按工具类型调整 |
| 应用场景 description | — | 100–260 字/场景 | — |
| 如何选择 introduction | 40 字 | 40–120 字 | **仅选型/操作类**（tools、seo 视题材）采用；Marketing/Blog 策略文默认不设此节 |
| 如何选择 steps | ×3–5 步 | 3–5 步 | 每步 `id` + `title` + description；按主题复杂度定，**不硬性 5 步** |
| 如何选择 description/步 | 80 字 | 120–200 字 | <80 字视为 stub，不达标 |
| 结论 | 2 段 | 2–3 段（**约 180–320 字**） | ≥2 段否则仓促；**软约束·内容优先**，非硬性红线；篇幅与例外见 [alignify-conclusion.md §2.3](../../skills/create-article/rules/conclusion.md) |
| FAQ items | ×8 问 | 8 问 | 中英文各 ≥8 问 |
| FAQ answer | 40 字 | 40–80 字 | <40 字答案不充分 |

---

## 二、英文页面

| 章节 | 硬底线 | 建议区间 | 说明 |
|------|--------|---------|------|
| blogLayout excerpt | 三段式 | 200–250 字符 | 避免通用结尾；与 meta description 主题一致 |
| TL;DR introduction | 30 词 | 30–60 词 | — |
| TL;DR items | ×4 条 | 4–5 条 | — |
| 什么是 XXX | 2 段 | 3–4 段（130–320 词） | — |
| 如何工作 technologyBase | 140 词 | 140–280 词 | — |
| 如何工作 advantages | ×3 项 | 3–5 项 | — |
| BestTools shortDescription | 10 字符 | 15–35 字符 | <10 字符被截断 |
| BestTools description | 280 字符 | 350–650 字符 | <280 字符内容质量不达标 |
| 应用场景 cases | ×3 个 | 4–6 个 | — |
| 应用场景 description | — | 100–260 词/场景 | — |
| 如何选择 introduction | 40 词 | 40–80 词 | **仅选型/操作类**采用；Marketing/Blog 策略文默认不设此节 |
| 如何选择 steps | ×3–5 步 | 3–5 步 | 每步 `id` + `title` + description；按主题复杂度定 |
| 如何选择 description/步 | 80 词/字符 | 100–180 词 | — |
| 结论 | 2 段 | 2–3 段（约 120–220 词） | 软约束·内容优先，见 [alignify-conclusion.md §2.3](../../skills/create-article/rules/conclusion.md) |
| FAQ items | ×8 问 | 8 问 | — |
| FAQ answer | 40 词 | 40–80 词 | — |

---

## 三、章节间一致性规则

1. **跨页面**：与同类型已有页面对比结构、标题格式与表达习惯；不强制逐页对齐字数
2. **章节间**：避免极短与极长章节相邻（如 80 字章节紧挨 400 字章节）
3. **章节内**：并列块（场景、步骤、FAQ）不宜出现约 3 倍以上长短差
4. **产品描述**：同页 BestTools 各产品 description 的 max/min < 3×

---

## 四、英文 vs 中文差异

- 英文与中文**信息深度**相当即可，不必字符数机械对齐
- 英文可针对具体工具做**本地化优化**（示例、定价、地区适用性）
- 英文 FAQ 可不同于中文 FAQ 的具体问题（但数量保持 8 问）
- 英文禁止 mid-word 截断——字数检查按完整句子截断

---

## 五、质检方式

- 以「是否说清、是否重复、单段是否过长」为主判
- 不因贴旧数字而删必要限定
- 字符统计：去 HTML、合并空格；中文按字，英文按词看可读长度

---

*section-word-counts · v2.0 · 2026-06-23*
