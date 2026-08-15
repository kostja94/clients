# 02 — References 与 blogLayout

> 对齐 `content/sections/section-references.md` §2.5

## References（中文页）

| 字段 | 中文页 |
|------|--------|
| `title` | **必须中文**（原文译名或官方中文名） |
| `description` | **必须中文**，20–60 字，客观说明参考价值 |
| `source` | 机构常用名（Google、Moz） |
| `date` | `2026年` / `持续更新` |
| `url` | 不变 |

```
❌ title: "Meta tags that Google understands"
✅ title: "Google 支持的 Meta 标签"
```

英文页：`title` / `description` 均为英文。

---

## blogLayout（中文 JSON）

| 字段 | 格式 |
|------|------|
| `publishDate` | `2026年6月23日` |
| `modifiedDate` | 同上，勿用 `June 8, 2026` |
| `readTime` | `14 分钟阅读`（与英文分钟数一致，不用 `~`） |
| `pageUrl` | `https://alignify.co/zh/...` |
| `locale` | `"zh"` |

---

## FAQ 对等

- 条数与英文一致
- 问句必须是中文
- 答案语义覆盖英文要点；中文可更简练，但不可漏关键限制（如「不能」「必须唯一」）

---

## 内链

- 中文正文：`href="/zh/seo/..."` 、`href="/zh/marketing/..."`
- 锚文本中文，与英文页链接目标 slug 一致
