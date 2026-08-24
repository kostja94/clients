# Step 5 — 创建英文 Markdown

> **产出**：`content/{channel}/en/{slug}.md` + 集中 JSON 英文键
> **引用**：[`create-tools-article/04-english-localization.md`](../create-tools-article/04-english-localization.md)

---

## 前置条件

- [ ] 中文 md 定稿 + Step 4 Meta 已注册
- [ ] Research 英文素材已备

---

## 核心原则

- **意译**，非逐句翻译
- **结构 parity**：相同 block 标记、H2/H3 锚点 id、section 数量
- **FAQ 7 问**；可不同于中文的具体问题
- **HowTo**：若有，英文 H2 `## How to Choose…` + 3–5 个 `###` 步骤；**禁止** frontmatter `howTo:`

---

## 流程

```
1. 创建 content/{channel}/en/{slug}.md
2. 翻译 frontmatter（改 locale、pageUrl、日期展示格式）
3. 逐 section 翻译，保持 <!-- block:section --> 与 {#anchor}
4. 同步 tldr-data.json / faq-data.json / references-data.json 英文键
5. 更新 *-meta.ts 英文 title/description
```

---

## 输出清单

- [ ] 英文 md 已创建
- [ ] frontmatter `pageUrl` 无 `/zh/` 前缀
- [ ] 集中 JSON 英文键与 en `pageUrl` 一致
- [ ] FAQ 7 问；答案无内链
- [ ] `npm run verify:content-json && npm run build`

---

*05-english-localization · v2.0 · 2026-08-23*
