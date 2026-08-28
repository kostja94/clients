# Create Article — 规范索引

> Alignify **每篇 flagship**。内容决定架构；质量全链路见 Gate / SelfCheck / audit-article。

---

## 步骤文档速查

| 步骤 | 文档 |
|------|------|
| 01–04 | [`01-intake.md`](../01-intake.md) … [`04-screenshots.md`](../04-screenshots.md) |
| 05–06 · 09–09c | [`content-locale.md`](./content-locale.md) |
| 07 | [`07-internal-links.md`](../07-internal-links.md) · [`internal-links.md`](./internal-links.md) |
| 08 | [`08-meta-config.md`](../08-meta-config.md)（Meta + **日期** + CTA + JSON 侧车） |
| 10 | [`10-quality-gates.md`](../10-quality-gates.md) |

---

## 已合并 / 已删除（勿引用旧路径）

| 旧文件 | 现 SSOT |
|--------|---------|
| `05-zh-content.md` · `06-localize-zh.md` · `09-en-content.md` · `localization-quality.md` | [`content-locale.md`](./content-locale.md) |
| `terminology*.md` · `marketing-glossary.json` | [`locale-glossary.md`](./locale-glossary.md) + `.json` |
| `11-publish-dates.md` · `12-legacy-tools-dates.md` | [`08-meta-config.md`](../08-meta-config.md) §发布日期 |
| `utm-nofollow.md` | [`internal-links.md`](./internal-links.md) Part 8 |
| `sections/` · `conclusion.md` · `final-cta.md` | [`sections.md`](./sections.md) |
| `templates/` 子目录 | [`templates.md`](./templates.md) |
| `marketing-internal-links.md` | [`internal-links.md`](./internal-links.md) Part 4.5 |
| `partner-products.md` | [`sections.md`](./sections.md) Part 3.3 §3.3.0 |
| `consistency.md` | [`copy-quality.md`](./copy-quality.md) |

---

## 质检地图（何时读哪个）

| 阶段 | 文档 |
|------|------|
| Step 02 Brief | [`article-brief.md`](./article-brief.md) · [`research-triangle.md`](./research-triangle.md) · [`product-coverage.md`](./product-coverage.md) · [`copy-quality.md`](./copy-quality.md) 附录 A |
| Step 03 关键词 | [`03-keywords.md`](../03-keywords.md) · Brief `Primary keyword`（须与 KB keyword 映射一致，见 [`knowledge-block/SKILL.md`](../../knowledge-block/SKILL.md)） |
| Step 05–06 / 09–09c 双语正文 | [`content-locale.md`](./content-locale.md) Part 2–5 · [`locale-glossary.md`](./locale-glossary.md) · [`gtm-prose-voice.md`](./gtm-prose-voice.md) · [`presentation.md`](./presentation.md) · [`copy-quality.md`](./copy-quality.md) Part 2·4 |
| Step 07 内链 | [`07-internal-links.md`](../07-internal-links.md)（**按 articleType** 选 Part 3/4/4.5/5）· [`internal-links.md`](./internal-links.md) Part 1–2 + Part 8 · 快照 [`../../optimize-internal-links/references/site-structure-internal-links.md`](../../optimize-internal-links/references/site-structure-internal-links.md) |
| Step 08 注册 | [`meta.md`](./meta.md) · [`sections.md`](./sections.md) Part 5 · [`08-meta-config.md`](../08-meta-config.md) §发布日期 · `next-publish-date.mjs` |
| Step 10 自审 | [`selfcheck.md`](./selfcheck.md) · [`quality-checklist.md`](./quality-checklist.md) · [`common-errors.md`](./common-errors.md) |
| 终审 | [`../../audit-article/SKILL.md`](../../audit-article/SKILL.md) · [`perfect-article-checklist.md`](./perfect-article-checklist.md)（S 级 · **可选**） |
| 同批 ≥2 篇 | [`outline-cross-check.md`](./outline-cross-check.md) · [`cross-article-audit.md`](./cross-article-audit.md) · [`copy-quality.md`](./copy-quality.md) M2 |

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
| [gtm-prose-voice.md](./gtm-prose-voice.md) | GTM/PLG 禁腔（分轨·同族分流·组合拳·姊妹篇）+ 存量待改快照 |
| [zh-en-mixing.md](./zh-en-mixing.md) | 中文正文英混禁则（export/watermark/playbook/gate 等）+ audit naked_loanwords |
| [content-locale.md](./content-locale.md) | 双语正文 SSOT：05–06 ZH · 09–09c EN · 双轨 Subagent + 地道 Pass |
| [locale-glossary.md](./locale-glossary.md) | 双语术语 SSOT（Part 1–3 对照 · Part 2 GTM · 文风） |
| [locale-glossary.json](./locale-glossary.json) | 机器层：`localize_required` · `forbidden_*` · audit 脚本 |
| [copy-quality.md](./copy-quality.md) | 五维 · Swap Test · 去模板化（M1/M2/M3） |
| [extractability-checklist.md](./extractability-checklist.md) | Draft / Step 06 |
| [perfect-article-checklist.md](./perfect-article-checklist.md) | S 级标杆（**可选**，非 Gate C） |
| [serp-fit-template.md](./serp-fit-template.md) | SERP Fit |
| [source-map-template.md](./source-map-template.md) | EEAT / Source Map |
| [outline-cross-check.md](./outline-cross-check.md) | 同批 Outline 3.5 |
| [cross-article-audit.md](./cross-article-audit.md) | 同批 5.5 |
| [product-coverage.md](./product-coverage.md) | 垂类选题 · 产品数量 · 全站独占 |

**终审**：[`../../audit-article/SKILL.md`](../../audit-article/SKILL.md)

---

## 结构与模板

| 文档 | 用途 |
|------|------|
| [anatomy.md](./anatomy.md) | 内容优先 + 参考菜单（§四·一 childrenHtml · **E35**） |
| [article-types.md](./article-types.md) | 类型 / 新文 `/blog` vs 存量路径 |
| [meta.md](./meta.md) | Meta 四要素 |
| [word-counts.md](./word-counts.md) | 字数硬底线 |
| [sections.md](./sections.md) | 章节 SSOT（Part 0–5 · 含结论与 Final CTA） |
| [internal-links.md](./internal-links.md) | 内链 + 外链 SSOT（Step 07：Part 1–2 + 按类型 3/4/4.5/5 + Part 8） |
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

*rules README · v3.5 · 2026-08-27*
