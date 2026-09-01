# Tools — Today Blog SelfCheck（Phase 5）

配合 `today-blog-article/SKILL.md` Phase 5 使用。从 **`today/` 项目根目录**运行。

## 使用方法

```bash
# Frontmatter
python blog/skills/today-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary keyword}" --categories "Product,Guide,Tutorial,Opinion" --require-secondary-category

# 字数（H3）
python blog/skills/today-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent brandpillar --min 2500

# 链接（G2/G6）
python blog/skills/today-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/compare,article.today.ai
```

输出：`PASS|FAIL | GateID | message [line N]`

## intent 枚举

`brandpillar` · `glossaryguide` · `comparison` · `alternative` · `usecase` · `healthcareguide` · `howto` · `opinion` · `announcement`

## 脚本

| 脚本 | Gate | 检查 |
|------|------|------|
| frontmatter_validator.py | GateC-SEO-F | title/description/slug/category |
| word_count_narrative.py | H3 | 叙事词数 |
| link_checker.py | P0-G2/G6 | 死链 / 禁止路径 |

*today-blog-article tools · v1.0 · 2026-09-01 · synced from blog-create SSOT*
