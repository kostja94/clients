# Step 4 — 创建英文文章 JSON

> **前置条件**：Step 2–3 完成（中文 JSON + blog-meta.ts + blog-pages-config.ts + blog-article-images.ts 已就绪，中文文章质量通过）
> **产出**：`content/blog/en/{slug}.json`
> **参照**：`content/templates/template-tools.md` §十四、[`references/section-word-counts.md`](./references/section-word-counts.md)

---

## 4.1 核心原则

- **意译，不逐句翻译**：理解中文含义后用自然英文表达
- **信息深度相当，字数不机械对齐**：英文自然比中文长 1.2–1.8×
- **本地化差异**：示例、定价、地区适用性可根据英文市场调整
- **FAQ 可不同**：英文 FAQ 可以覆盖与中文不同的问题（但数量保持 8 问）

---

## 4.2 创建英文 JSON

### 文件位置
```
content/blog/en/{slug}.json
```

### 建议流程

1. **先读中文 JSON**：理解全文结构和信息层次
2. **逐 section 翻译**：按以下优先级
   - 先写 blogLayout（H1、excerpt）
   - 再写核心板块（什么是、如何工作）
   - 再写产品板块（BestTools、对比表格）
   - 最后写 FAQ 和参考文献
3. **每完成一个 section 即自检**：对照字数速查表

---

## 4.3 各章节英文特别注意事项

### H1（blogLayout.title）
- 40–60 字符
- 格式：`{Tool Type}: {Core Value Proposition}`

### Excerpt
- 200–250 字符
- 三段式，英文自然段落

### TL;DR
- introduction 30–60 词
- items 4–5 条，每条 10–25 词

### 什么是 XXX（What Is）
- 130–320 词，段数自然
- 与中文信息深度对等

### 如何工作（How It Works）
- technologyBase 140–280 词
- advantages 3–5 项，name + description 各 20–50 字符
- architectureDifferences 90–200 词

### BestTools
- shortDescription 硬底线 10 字符，建议 15–35
- description 硬底线 280 字符，建议 350–650
- **本地化优化**：定价改用 USD、示例换为英文市场案例

### 结论
- 篇幅：见 [alignify-conclusion.md §2.3](../../../content/alignify-conclusion.md)
- Conclusion 在 FAQ 之前

### FAQ
- 8 问
- 答案 40–80 词
- 可不同于中文 FAQ 的具体问题

---

## 4.4 英文 vs 中文差异对照

| 项目 | 中文 | 英文 |
|------|------|------|
| 颜色方案 | `data-locale="zh"`（浅色） | `data-locale="en"`（深色） |
| H2 分割线 | 有分割线 | 无分割线，仅 `pt-8` |
| Hero 布局 | 右对齐 | 左对齐 |
| 更新日期 | "更新于 2026年X月X日" | "Updated on Month Day, 2026" |
| 产品定价 | 人民币示例 | USD 示例 |
| 内链文本 | 中文链接文本 | 英文链接文本 |

---

## 4.5 Step 4 完成检查

- [ ] JSON 格式有效
- [ ] 英文与中文结构一致（10 节顺序不变）
- [ ] 所有章节字数在建议区间或可说明理由
- [ ] BestTools 英文硬底线达标
- [ ] 无 mid-word 截断
- [ ] FAQ 8 问；Tools/Blog JSON 的 FAQ 内链符合 §1.5（全文唯一、FAQ ≤3 slug）
- [ ] 定价/示例已本地化
- [ ] 英文自然流畅（非机器翻译腔）

---

*04-english-localization · v2.0 · 2026-06-23*
