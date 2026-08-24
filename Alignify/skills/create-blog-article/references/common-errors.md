# Blog 常见错误

> **版本**：v2.0 · 2026-08-23

| # | 错误 | 修复 |
|---|------|------|
| E1 | 产出仍为 `.json` | 改用 `.md` + 集中 JSON |
| E2 | 配置 `routeCategory` | 改用 frontmatter `category`；config 只填 hub 字段 |
| E3 | FAQ ≥8 | 线上标准为 **7 问** |
| E4 | frontmatter `howTo:` | 删除；HowTo 仅正文 section |
| E5 | 引用 `audit:howto-choose` | 已废弃 |
| E6 | SEO 文写到 `content/blog/` | SEO → `content/seo/` |
| E7 | 日期只改 meta 未改 md | 双源同步 |

---

*common-errors · v2.0 · 2026-08-23*
