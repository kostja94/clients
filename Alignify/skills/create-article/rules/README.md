# Create Article — 规范索引

> Alignify **每篇 flagship**。内容决定架构；质量全链路见 Gate / SelfCheck / audit-article。

---

## 质检地图（何时读哪个）

| 阶段 | 文档 |
|------|------|
| Step 02 Brief | [`article-brief.md`](./article-brief.md) · [`research-triangle.md`](./research-triangle.md) |
| Step 05–06 成稿 | [`presentation.md`](./presentation.md) · [`extractability-checklist.md`](./extractability-checklist.md) |
| Step 07 内链 | [`07-internal-links.md`](../07-internal-links.md) · [`internal-links.md`](./internal-links.md) · 快照 [`../../optimize-internal-links/references/site-structure-internal-links.md`](../../optimize-internal-links/references/site-structure-internal-links.md) |
| Step 08 注册 | [`meta.md`](./meta.md) · [`sections.md`](./sections.md) Part 5 |
| Step 10 自审 | [`selfcheck.md`](./selfcheck.md) · [`quality-checklist.md`](./quality-checklist.md) · [`common-errors.md`](./common-errors.md) |
| 终审 | [`../../audit-article/SKILL.md`](../../audit-article/SKILL.md) · [`perfect-article-checklist.md`](./perfect-article-checklist.md)（S 级） |
| 同批 ≥2 篇 | [`outline-cross-check.md`](./outline-cross-check.md) · [`cross-article-audit.md`](./cross-article-audit.md) |

---

## Flagship 质量（优先读）

| 文档 | 用途 |
|------|------|
| [gates.md](./gates.md) | audit-ready / publish-ready / S 级语义 |
| [gate-rollback.md](./gate-rollback.md) | Fail → 回退 Step |
| [article-brief.md](./article-brief.md) | Brief 模板（Moat + Answer Blocks） |
| [research-triangle.md](./research-triangle.md) | Step 02 Gate 0R |
| [selfcheck.md](./selfcheck.md) | Step 10 · 12 维 + H0–H4 |
| [presentation.md](./presentation.md) | BLUF + 段落 + Kostja Voice |
| [localization-quality.md](./localization-quality.md) | 中英文地道化 Pass |
| [terminology-glossary.md](./terminology-glossary.md) | 全站中文术语对照（§六 Git 提交署名） |
| [marketing-glossary.json](./marketing-glossary.json) | Marketing 术语表 |
| [extractability-checklist.md](./extractability-checklist.md) | Draft / Step 06 |
| [perfect-article-checklist.md](./perfect-article-checklist.md) | S 级标杆 |
| [serp-fit-template.md](./serp-fit-template.md) | SERP Fit |
| [source-map-template.md](./source-map-template.md) | EEAT / Source Map |
| [outline-cross-check.md](./outline-cross-check.md) | 同批 Outline 3.5 |
| [cross-article-audit.md](./cross-article-audit.md) | 同批 5.5 |

**终审**：[`../../audit-article/SKILL.md`](../../audit-article/SKILL.md)

---

## 结构与模板

| 文档 | 用途 |
|------|------|
| [anatomy.md](./anatomy.md) | 内容优先 + 参考菜单（§四·一 childrenHtml · **E35**） |
| [article-types.md](./article-types.md) | 类型 / 新文 `/blog` vs 存量路径 |
| [meta.md](./meta.md) | Meta 四要素 |
| [word-counts.md](./word-counts.md) | 字数底线 |
| [consistency.md](./consistency.md) | 跨页一致性 |
| [sections.md](./sections.md) | 章节 SSOT（Part 0–5 · 含结论与 Final CTA） |
| [internal-links.md](./internal-links.md) | 内链 SSOT（Part 1–2 · Part 4.5 Marketing M1–M11） |
| [quality-checklist.md](./quality-checklist.md) | P0/P1 汇总 |
| [product-screenshots.md](./product-screenshots.md) | Best 榜单产品截图 URL |
| Hero / OG 美学速查 | `E:\个人知识库\设计\11-通用-Hero与插图美学参考.md`（完整 SSOT → [`knowledge/design/aesthetic-references.md`](../../../knowledge/design/aesthetic-references.md)） |

## 章节规范

[`sections.md`](./sections.md)（唯一 SSOT · Part 0–5）

## 页面模板（参考 — 非施工图）

[`templates.md`](./templates.md)（唯一 SSOT）

## 自动化脚本（Step 10）

| 脚本 | 用途 |
|------|------|
| `scripts/audit/audit-frontmatter.py` | E44–E48 frontmatter |
| `npm run verify:content-json` | 实际 = `verify-content-md.py`（md 结构；**不验 JSON/E10**） |
| `scripts/ops/normalize-frontmatter.py` | 批量去除 frontmatter 区内首尾空行（E48） |
| `scripts/ops/strip-hero-html-frontmatter.py` | 剥离遗留 `heroHtml:`（一次性） |

---

*rules README · v3.3 · 2026-08-27*
