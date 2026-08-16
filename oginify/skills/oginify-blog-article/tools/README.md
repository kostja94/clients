# Oginify Blog Skill — Tools

Phase 5 Gate C 前的机器检查脚本。**从 `oginify/` 项目根目录运行**（路径含中文字符时需加引号）。

```bash
python skills/oginify-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary kw}"
python skills/oginify-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {ranking|howto|glossary|sizeguide|metaguide|alternative|toolguide|developerguide|usecase|trendanalysis|opensourceguide|announcement}
python skills/oginify-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/vs,/templates
```

## frontmatter_validator.py

| Check | 规则 |
|-------|------|
| F1 | title 45–65 chars 含主关键词 |
| F2 | description 120–160 chars |
| F4 | slug 常青（无年份） |
| F5 | category ∈ Tutorial/Guide/Case Study/Reference/Product |
| F5b | secondary_category = Open Graph |
| F5c | best-* slug 需 articleFormat: Ranking |
| F6 | 无废弃 image/keywords/related 字段 |
| F7 | author 存在 |
| F8 | slug kebab-case |

## word_count_narrative.py

排除 frontmatter / 表格 / FAQ 块后的叙事词数。阈值见脚本顶部 THRESHOLDS（对应 article-types.md）。

## link_checker.py

| Check | 规则 |
|-------|------|
| G2 | 无空/占位/格式错误链接（同时检查 markdown `[text](url)` 与 HTML `<a href="url">` 描述性内链） |
| G6 | 无 forbidden 前缀（默认 /pricing,/vs,/templates） |

## 依赖

纯 Python 3 标准库；frontmatter_validator 可选依赖 `pyyaml`（无则用内置解析）。
