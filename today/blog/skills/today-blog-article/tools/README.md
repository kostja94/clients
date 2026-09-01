# Tools — Today Blog SelfCheck（Phase 5）

配合 `today-blog-article/SKILL.md` Phase 5 使用。从 **`today/` 项目根目录**运行。

## 使用方法

```bash
# Frontmatter
python blog/skills/today-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary keyword}" --categories "Product,Guide,Tutorial,Opinion" --require-secondary-category

# 字数（H3）
python blog/skills/today-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent brandpillar --min 2500

# 链接（G2/G6 + R4/R5）
python blog/skills/today-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/compare,article.today.ai

# 散文审计（阻断门，--strict 失败时 exit 1）
python blog/skills/today-blog-article/tools/audit_prose_links.py blog/NN-{slug}.md --strict
python blog/skills/today-blog-article/tools/audit_prose_links.py blog/personal-agent/NN-{slug}.md --intent comparison --strict
```

输出：`PASS|FAIL|WARN | GateID | message [line N]`

## intent 枚举

`brandpillar` · `glossaryguide` · `comparison` · `alternative` · `usecase` · `healthcareguide` · `howto` · `opinion` · `announcement`

## 脚本

| 脚本 | Gate | 检查 |
|------|------|------|
| frontmatter_validator.py | GateC-SEO-F | title/description/slug/category |
| word_count_narrative.py | H3 | 叙事词数 |
| link_checker.py | P0-G2/G6, **R4**, **R5** | 死链 / 禁止路径 / 重复 blog slug / TL;DR 内链 |
| audit_prose_links.py | **Prose** | 长段、伪列表、列表占比、中文正文 |

### link_checker.py — R4 / R5

| 规则 | 条件 | 严重度 |
|------|------|--------|
| **R4** | 同一 `/blog/{slug}`（忽略 `#` anchor）出现 >1 次 | FAIL |
| **R5** | `## TL;DR` 至下一 `##` 之间 `/blog/` 链接 >1 | WARN |

可选 `--strict-r5` 将 R5 WARN 升级为 FAIL。

### audit_prose_links.py — 阻断门（`--strict`）

| 条件 | 阈值 | 适用 |
|------|------|------|
| `long_paras_ge4` | ≥3 | 全文 |
| `pseudo_list_total` | ≤5 | 全文 |
| `list_table_pct` | ≤35% | Comparison / BrandPillar（`--intent` 或 frontmatter 自动推断） |
| `chinese_line_count` | 0 | 正文（frontmatter 除外） |

**伪列表检测**：

- 行首 `**Bold label.**` + 单句
- 行首 `**Mistake N**`
- `**Choose X when:**` 后接 bullet 列表

输出末尾 `RESULT: PASS` 或 `RESULT: FAIL`；`--strict` 且 FAIL 时 exit code 1。

*today-blog-article tools · v1.0.1 · 2026-09-01*
