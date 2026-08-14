# QVeris Blog Article — Tools

Phase 5 机器预检脚本。在 `qveris/skills/qveris-blog-article/` 目录下执行，或传入文章绝对路径。

## 依赖

- Python 3.10+
- 可选：`pyyaml`（无则用简易 frontmatter 解析）

```bash
pip install pyyaml
```

## 脚本

### frontmatter_validator.py

校验 QVeris schema（精简版）：frontmatter 必填字段（slug/metaTitle/description/author/publishedAt/updatedAt；readTime 推荐）；正文 `# H1` = title（45–90 字符、含主关键词），H1 后首段 = excerpt（≥40 字符），`## TL;DR` 区块 = 3–5 条 `- **label** — body` bullet（首条 BLUF ≥40 字符）；禁止已移除字段（title/excerpt/tldr/badge/breadcrumb/authorInitials/heroImage/heroAlt/tocExtra）及 date/isoDate/category/keywords/related/disclosure；`metaTitle` 须含 `| QVeris`；slug 常青 kebab-case；readTime 格式。**结构（Conclusion→FAQ）为 WARN 建议**——QVeris 已发稿不一定含此结构，不阻断交付。

```bash
python tools/frontmatter_validator.py ../../blog/01-stock-api-free-comparison.md --keyword "free stock api"
```

### word_count_narrative.py

叙事词数（排除 frontmatter、表格、FAQ 问答块）。

| `--intent` | 叙事下限 |
|------------|---------|
| technical | 2500 |
| fieldtest | 2500 |
| workflow | 2200 |
| market | 2000 |
| comparison | 2200 |
| product | 2000 |

> comparison 阈值 2200 由已发稿 01（2236 词）校准。

```bash
python tools/word_count_narrative.py ../../blog/01-stock-api-free-comparison.md --intent comparison
```

### link_checker.py

检查 placeholder 锚文本与 forbidden 内链（默认 `/auth/`、`/admin/`、`/dashboard/`、`/use-cases/`、`/scenarios/`、`/alternative/`、`/applications`——官网已下线栏目与 404 路径）。**internal blog links ≥2 为 WARN 建议**——纯第三方对比文（如 golden 01）可合法为 0，不阻断。

```bash
python tools/link_checker.py ../../blog/01-stock-api-free-comparison.md
```

## Phase 5 推荐顺序

```bash
cd qveris/skills/qveris-blog-article
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{kw}"
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {type}
python tools/link_checker.py ../../blog/NN-{slug}.md
```

任一 FAIL → 修复后重跑，再进入人工 10 维 SelfCheck。

---

*tools · v1.0.0 · 2026-08-06*
