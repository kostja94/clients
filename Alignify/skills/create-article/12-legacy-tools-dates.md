# Step 12 — 存量 /tools/ modifiedDate（附录）

> **适用**：仅 `best-ranking-legacy`（维护 108 篇 `/tools/{slug}`）

---

## 规则

- 内容更新时改 `tools-meta.ts` → `modifiedDate`
- 同步 md frontmatter `updated`
- 保守更新：同日 ≤2 篇
- **不**改 `publishDate`

## 与 Step 11 分工

| 字段 | 新 `/blog/` 文 | 存量 `/tools/` |
|------|---------------|----------------|
| publishDate | Step 11 错开 | 不变 |
| modifiedDate | 内容更新时 | 内容更新时 |

---

*12-legacy-tools-dates · v1.0 · 2026-08-26*
