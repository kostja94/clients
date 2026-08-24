# Blog 文章质量检查表

> **版本**：v2.0 · 2026-08-23

---

## 自动化

```bash
npm run verify:content-json
npm run build
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --locale both --violations-only
```

> **已废弃**：`audit:howto-choose`、`audit:internal-links`（npm）、JSON block 体系

---

## P0

| # | 检查项 | 标准 |
|---|--------|------|
| P0-1 | 结论在 FAQ 前 | md 顺序 |
| P0-2 | FAQ | **7 问** |
| P0-3 | FAQ 答案 | 无内链 |
| P0-4 | 无 `howTo:` frontmatter | verify 脚本 |
| P0-5 | heroImage/heroHtml | frontmatter |
| P0-6 | 日期双源 | meta ISO = md 同日 |
| P0-7 | build | 通过 |

---

*quality-checklist · v2.0 · 2026-08-23*
