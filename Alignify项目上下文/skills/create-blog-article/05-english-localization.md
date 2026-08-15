# Step 5 — 创建英文文章 JSON

> **定位**：中文 JSON 定稿后创建英文版。意译非逐句，保持信息深度相当，适当本地化差异。
> **产出**：`content/blog/en/{slug}.json`
> **引用**：`skills/create-tools-article/04-english-localization.md`（可复用意译原则）

---

## 前置条件

- [ ] 中文 JSON 已完成并通过 Step 3b 本地化润色
- [ ] 中文 Meta 已在 Step 4 注册
- [ ] Research Log 的英文素材（R2/R3 中的英文来源）已备

---

## 核心原则

### 意译，非逐句翻译

- 中文的成语、惯用语、文化类比 → 替换为英语对应的表达
- 中文的长复合句 → 英文拆为更短的主谓宾结构（英文自然比中文长 1.2–1.8×）
- 数字、数据、产品名 → 保持原样
- 案例中涉及中国公司的 → 保留，但补充国际背景说明（如适用）

### 本地化差异

| 可差异的内容 | 原因 |
|------------|------|
| 示例/案例 | 英文读者更熟悉国际案例 |
| 定价单位 | 人民币转美元 |
| FAQ 问题 | 英文读者关心的可能不同 |
| References | 英文来源优先 |

### 结构 parity

中英文 JSON 必须保持：
- 相同的 block 数量和类型（type 字段一致）
- 相同的 section 标题结构（H2/H3 层级一致）
- 相同的 howToChoose 步骤数量和 id

---

## 逐类型翻译要点

### Tools 型

- **bestTools description**：EN ≥280 字符（比中文 100 字长很多）
- **Meta title**：`Best XXX (2026): Subtitle | Alignify`
- **H1**：40–60 字符，不含年份

### Marketing 型

- **heroHtml**：如果中文版有，英文版需重新设计 CTA 文案
- **childrenHtml**：表格/数据可视化中的文本需翻译
- **useCases**：可能需替换为国际读者熟悉的案例

### SEO 型

- **tldr.items**：对象格式的 `title` 和 `content` 都需翻译
- **childrenHtml 代码块**：注释和变量名可能需要本地化
- **技术术语**：确保英文技术术语使用业内标准表达

### Insights 型

- **html block**：整个 html 字符串需完整翻译（最大的工作量）
- **内部 `<a href="/blog/...">`** 链接 path 保持不变，仅翻译锚文本

---

## 翻译流程

```
1. 创建 content/blog/en/{slug}.json
2. 先翻 blogLayout（title/excerpt/readTime/pageUrl）
3. 再翻 blocks（从上到下，每个 block 保持结构）
4. FAQ 和 References 最后翻
5. 全文通读，检查 structure parity
6. 与中文版逐 block 比对 type 和 id 一致性
```

---

## 翻译后验证

- [ ] `blogLayout.publishDate` 格式为 `"July 16, 2026"`
- [ ] `pageUrl` 为 `/blog/{slug}`（英文不）不写 `en/` 前缀）`
- [ ] H1 40–60 字符
- [ ] Excerpt 200–250 字符
- [ ] Blocks 数量与中文 JSON 一致
- [ ] 每个 block 的 `type` 与中文一致
- [ ] bestTools 每产品 description ≥280 字符
- [ ] 全文无明显机翻痕迹
- [ ] 同步更新 `blog-meta.ts` 中英文 title/description

---

## 输出清单

- [ ] `content/blog/en/{slug}.json` 已创建
- [ ] 中英文 block 数量和 type 一致
- [ ] 英文 Meta title/description 已填入 blog-meta.ts
- [ ] `npm run build` 成功

---

*05-english-localization.md · v1.0 · 2026-07-16*
