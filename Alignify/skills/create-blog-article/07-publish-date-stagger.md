# Step 7 — 发布日期错开

> **引用**：复用 [`create-tools-article/06-publish-date-stagger.md`](../create-tools-article/06-publish-date-stagger.md)

---

## 双处同步（非三处 JSON）

| 位置 | 格式 |
|------|------|
| `blog-meta.ts`（或对应 `*-meta.ts`） | ISO `2026-07-16T00:00:00+08:00` |
| md frontmatter `date` / `updated` | 中文 `"2026年7月16日"` / 英文 `"July 16, 2026"` |

部署仓暂无专用 stagger 脚本；成批未上线文章须**手动**从锚点日往前一天一篇分配。

---

## 检查清单

- [ ] 未上线 slug 的 publishDate 两两不同
- [ ] 已上线 slug 的 publishDate 未改
- [ ] meta 与 md frontmatter 日期一致
- [ ] `npm run build` 通过

---

*07-publish-date-stagger · v2.0 · 2026-08-23*
