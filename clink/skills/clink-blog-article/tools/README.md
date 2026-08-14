# Clink Blog Article — Tools

Phase 5 机器预检脚本。在 `clink/skills/clink-blog-article/` 目录下执行，或传入文章绝对路径。

## 依赖

- Python 3.10+
- 可选：`pyyaml`（无则用简易 frontmatter 解析）

```bash
pip install pyyaml
```

## 脚本

### frontmatter_validator.py

校验 title / description / slug / category / image / author / date；禁止 keywords/related/disclosure；结构须为 **Conclusion → FAQ**（最后两节）。

```bash
python tools/frontmatter_validator.py ../../blog/01-what-is-clink.md --keyword "Clink"
```

### word_count_narrative.py

叙事词数（排除 frontmatter、表格、FAQ 问答块）。

| `--intent` | 叙事下限（excl. FAQ/tables） |
|------------|------|
| brand | 2500 |
| comparison | 1600 |
| product | 1800 |
| opinion | 1800 |
| evaluation | 2500 |
| glossary | 1800 |

基线（2026-07-21）：四篇已发稿 frontmatter / H3 / link 全 PASS（校准后）。新稿仍以 `article-types.md` 创作目标词数为准；H3 为叙事下限（excl. FAQ/tables）。

```bash
python tools/word_count_narrative.py ../../blog/01-what-is-clink.md --intent brand
```

### link_checker.py

检查 placeholder 链接与 forbidden 内链（默认 `/vs/`、`/pricing`、`/for/`、`/learn/`、`/customers/`）。

```bash
python tools/link_checker.py ../../blog/01-what-is-clink.md
```

## Phase 5 推荐顺序

```bash
cd clink/skills/clink-blog-article
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{kw}"
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {intent}
python tools/link_checker.py ../../blog/NN-{slug}.md
```

任一 FAIL → 修复后重跑，再进入人工 12 维 SelfCheck。

---

*tools · v1.0.0 · 2026-07-21*
