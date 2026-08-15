# Editorial — 写作规则

TopicEditorialSection（intro + sections[]）正文写作规范。

**字段定义**：[content-model.md](../../specs/content-model.md) · **结构**：[page-types.md](../../specs/page-types.md)

---

## 章节类型

| 上下文 | JSON 路径 | TOC |
|--------|-----------|-----|
| Intro | `content.intro` | intro.title |
| 正文 | `content.sections[]` | section.title |

---

## 写作规则

### title（H2）

- 20–80 字符，含关键词，禁止 `"Introdução"` 等空标题
- 每页 `id` + `title` 唯一

### paragraphs

- 每节 2–6 段，每段 80–300 字符
- 首段直接回答本节主题
- 外链允许 `<a rel="noopener noreferrer nofollow">`

### highlights（可选）

- 0–4 条，30–100 字符，事实/统计/建议，不重复段落

### productCards（可选）

- 0–3 张，与本节主题相关
- description 40–100 字符；cta_text ≤20 字符

---

## 推荐章节顺序

1. 定义（`o-que-e`）→ 2. 原理（`como-funciona`）→ 3. 选择标准（`como-escolher`）→ 4. 对比（`a-vs-b`）→ 5. 用例（`casos-de-uso`）→ 6. 趋势（`tendencias`）

---

## Checklist

- [ ] 每节 id 唯一（kebab-case）
- [ ] title 20–80 字符、有信息量
- [ ] 首段直答
- [ ] highlights 不重复段落
- [ ] productCards 与本节相关
- [ ] 逻辑顺序：定义 → 标准 → 对比 → 应用
