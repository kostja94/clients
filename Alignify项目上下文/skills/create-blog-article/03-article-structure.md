# Step 3 — 创建中文文章 JSON

> **定位**：从知识块 + Research 素材到完整中文 JSON 的核心步骤。
> **产出**：`content/blog/zh/{slug}.json` + 内链初稿
> **引用**：`skills/create-tools-article/02-article-structure.md`（tools 型复用）、`references/article-types.md`（4 种类型结构）、`skills/create-tools-article/02c-internal-links-drafting.md`（内链初稿）

---

## 前置条件

- [ ] Step 1 Gate A 已通过（类型已判定）
- [ ] Step 2 Research Log 完整（素材充足）
- [ ] 已阅读对应类型的章节结构（`references/article-types.md`）

---

## 通用 JSON 骨架

所有类型的 JSON 共享 `ArticleDocV1` 结构：

```jsonc
{
  "version": 1,  // SEO 类型用 2.0
  "category": "...",
  "categoryZh": "...",
  "categorySecondary": "...",   // Marketing 型必需
  "categorySecondaryZh": "...", // Marketing 型必需
  "blogLayout": {
    "title": "H1 标题",
    "excerpt": "三段式摘要",
    "publishDate": "2026年7月16日",  // 中文格式
    "modifiedDate": "2026年7月16日",
    "readTime": "...",
    "pageUrl": "/blog/{slug}",
    "locale": "zh",
    "heroImage": "...",   // Tools 型必填，Marketing 型 heroHtml 与 heroImage 互斥
    "heroImageAlt": "...",
    "heroHtml": "..."     // Marketing 型可选
  },
  "blocks": [ /* 见各类型章节列表 */ ]
}
```

---

## 各类型创作要点

### Tools 型

1. **复用 `skills/create-tools-article/02-article-structure.md`** 的完整 10 节结构流水线
2. **bestTools**：从知识块的「形态谱系」和「产品类型表」提取产品，每个产品三段式描述（核心定位+关键差异+最佳适用场景）
3. **howToChoose**：禁止 `name` 字段，必须用 `title`
4. **FAQ**：≥8 问，从知识块「问题域」和「落地碎片」提取

### Marketing 型

1. **概念定义 section**：从知识块的「词汇锚点」和「概念定义」提取
2. **策略 sections**：每个核心策略一个独立 section，含操作步骤和数据支撑
3. **useCases**：每个案例需具体数据（如「XX 公司通过 XX 策略提升了 40% 转化率」）
4. **heroHtml**：可嵌入 CTA Hero HTML，优于 heroImage
5. **childrenHtml**：当需要展示对比表格/数据可视化时使用

### SEO 型

1. **tldr.items**：使用 `{title, content}` 对象格式
2. **subSections 重使用**：每个操作步骤一个 subSection
3. **childrenHtml**：嵌入代码示例（`<pre><code>`）、配置片段
4. **技术术语**：首次出现时解释或提供中英对照

### Insights 型

1. **主体走 `type: "html"` block**：className 设为 `"prose max-w-none"`
2. **html 块内包含完整文章**：从 H2 开始，含所有段落/表格/图片/列表
3. **tldr 用对象格式**：`{title, content}`
4. **Conclusion section**：在 html 块之后单独一个 section 总结洞察
5. **FAQ**：≥3 问

---

## 写作原则

### 金科玉律

> **知识块是非线性笔记，文章需改写为叙事线。**

- 知识块可以用列表、表格、碎片条目 → 文章需串成线性叙述
- 知识块可以「按需查阅」→ 文章需「一口气读完」
- 知识块面向编辑者 → 文章面向读者

### BLUF（Bottom Line Up Front）原则

- TL;DR 直接给出核心结论
- 每个 H2 下的第一段先给答案再展开论证
- FAQ 首句即答

### 避免 AI 腔

检查清单（来自 clients `05-writing-style.md`）：

- [ ] 无「在当今数字化时代」「随着AI技术的不断发展」等模板开头
- [ ] 无「不仅如此」「更重要的是」「总而言之」等机械过渡
- [ ] 无结尾的「希望本文能……」式废话
- [ ] 有具体的例子和数据，而非泛泛描述
- [ ] 每个 section 有独立的叙事弧（引入→论证→小结）

---

## 内链初稿

加载 `skills/create-tools-article/02c-internal-links-drafting.md` 的规则，核心约束：

| 规则 | 说明 |
|------|------|
| **R-TLDR** | TLDR block 内 ≤2 个内链 slug |
| **R1** | 全文 ≥ 本类型的 distinct slug 数（Tools ≥5，其他 ≥3） |
| **R4** | 同一 slug 全文仅出现 1 次 `<a>` |
| **R7** | FAQ 内 ≤3 个内链 slug，且与正文不重复 |
| **锚文本融入语境** | 禁止「参见我们的 XX 专页」「详见 XX」等导航式插入；链接必须自然出现在对工作流的解释中 |

---

## 输出清单

- [ ] `content/blog/zh/{slug}.json` 已创建
- [ ] 所有必填 block 类型都存在（对照类型结构）
- [ ] `version` 字段正确（1 或 2.0）
- [ ] `category`/`categoryZh` 与知识块目录一致
- [ ] `blogLayout` 各字段完整（含 heroImage 或 heroHtml）
- [ ] howToChoose 无 `name` 字段（如适用）
- [ ] 内链初稿已写入
- [ ] 全文通过 BLUF + AI 腔检查

---

*03-article-structure.md · v1.0 · 2026-07-16*
