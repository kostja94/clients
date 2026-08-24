---
name: localize-content-zh
description: >-
  Alignify 中文内容本地化：seo/marketing/insights/blog/tools Markdown 的地道化、术语统一、
  References 中文化、与英文结构 parity。在优化 zh md、审查翻译质量、修复中英不一致时使用。
---

# Localize Content ZH — Alignify 中文本地化 Skill

> **版本**：v2.0 · 2026-08-23  
> **适用范围**：`content/{seo,marketing,insights,tools,blog}/zh/*.md` + 集中 JSON（`tldr-data.json` / `faq-data.json` / `references-data.json`）  
> **标杆页**：`content/insights/zh/reasons-you-need-seo.md`

---

## 何时使用

- 中英文 **结构已对齐**，但中文仍像英译稿
- 新建/扩写中文 md 后做 **地道化润色**
- References title 英文残留、术语 CTR/CTA/ROI 混用

**不适用**：知识块撰写；英文意译（用 `create-tools-article/04-english-localization.md`）

---

## 流程（逐页）

```
1. 读 en + zh .md，确认 section 顺序与锚点一致
2. 按 01-terminology-and-style.md 润色正文
3. 按 02-references-and-metadata.md 修 frontmatter + references-data.json
4. 对照 en FAQ：信息等价，7 问
5. npm run verify:content-json
```

---

## 核心规则（摘要）

| 维度 | 中文页要求 |
|------|-----------|
| **文风** | 行业长文口吻；避免说明书腔 |
| **术语** | 正文用中文指标名；缩写首次可「点击率（CTR）」 |
| **内链** | 中文页 `href="/zh/..."` |
| **References** | title + description 均中文（`references-data.json`） |
| **frontmatter** | 日期 `2026年6月8日`；readTime `14 分钟阅读` |
| **与 EN** | 语义等价；FAQ 7 问一致 |

---

## 详细文档

| 文档 | 内容 |
|------|------|
| [`01-terminology-and-style.md`](./01-terminology-and-style.md) | 术语表、直译腔改写 |
| [`02-references-and-metadata.md`](./02-references-and-metadata.md) | References、frontmatter、FAQ |
| [`03-per-page-workflow.md`](./03-per-page-workflow.md) | 检查清单 |

---

## 与 create-tools-article 的关系

Step 2 产出中文初稿 → 本 Skill 润色定稿 → Step 4 英文意译。

---

## 编辑方式

- 少量替换：`StrReplace` 改 md / 集中 JSON
- 批量：UTF-8 脚本 + `npm run verify:content-json`
- **禁止**引用已删除的 `polish-zh-page.py` / `polish-zh-batch.py`
