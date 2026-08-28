# Datus Blog — Validation Tools

> Phase 5 预检。路径相对于本仓库内的 `datus/` 根目录。

## 用法

```bash
python datus/skills/datus-blog-article/tools/frontmatter_validator.py datus/blog/semantic-layer/49-{slug}.md --keyword "{primary keyword}"

python datus/skills/datus-blog-article/tools/word_count_narrative.py datus/blog/{path}.md --intent {glossary|toolslist|comparison|research|howto|pillar} --min {threshold}

python datus/skills/datus-blog-article/tools/link_checker.py datus/blog/{path}.md --forbidden /agent,/features/,/use-cases/,/vs/,/alternatives/,/case-studies/
```

## Datus overlay

| 脚本 | Datus 约定 |
|------|------------|
| frontmatter_validator | 必填 `category` + `secondaryCategory`；slug 无年份 |
| word_count_narrative | `--min` 见 `references/selfcheck.md` H3 |
| link_checker | G6 forbidden 前缀见上 |

ArticleType → `--intent` 映射见 `references/selfcheck.md`。

---

*tools README · Datus overlay · 2026-08-28*
