# Blog Audit Tools

> **路径**：`floatboat/blog/skills/floatboat-blog-article/tools/`  
> 机器可执行检查，输出 **Pass/Fail + Gate ID + 行号/详情**。在 **Phase 5** Gate C 人工检查前先跑脚本。

## 脚本

| 脚本 | Gate ID | 覆盖标准 |
|------|---------|---------|
| `frontmatter_validator.py` | Gate C / 维度 9 | Frontmatter F1–F8（见 `references/selfcheck.md` §9） |
| `word_count_narrative.py` | **H3** | 字数硬阻断下限（见 `references/selfcheck.md` §H3） |
| `link_checker.py` | **P0 G2**, **G6** | 死链 + 禁止内链路径 |

## 输出格式

每行一条结果：

```
PASS | {gate_id} | {message}
FAIL | {gate_id} | {message} [line {n}]
```

退出码：`0` = 全部 Pass，`1` = 至少一条 Fail。

## 用法

在 skill 目录下执行（路径相对 `tools/`）：

```bash
python frontmatter_validator.py ../../09-{slug}.md --keyword "{primary kw}"
python word_count_narrative.py ../../09-{slug}.md --intent research
python link_checker.py ../../09-{slug}.md --forbidden /pricing-beta,/agent
```

## `--intent` 与文章类型对照

脚本检查的是 **硬阻断下限**（低于即 Fail）；SKILL §2 中的词数区间是 **创作目标**，两者不同。

| SKILL §2 文章类型 | 创作目标 | 推荐 `--intent` | 脚本硬门槛 |
|------------------|---------|-----------------|-----------|
| Research / Glossary | 2400–3500 | `research` 或 `deep_glossary` | ≥2000 |
| Comparison | 2800–3500 | `comparison` | ≥1500 |
| Alternative | 2200–3000 | `comparison` | ≥1500 |
| Product / Scenario | 2000–2700 | `product_tutorial` | ≥1500 |
| Product Announcement | 1500–2000 | `simple_glossary` | ≥1200 |

### `--intent` 全部取值

| intent | 硬门槛 |
|--------|--------|
| `simple_glossary` | ≥1200 |
| `deep_glossary` | ≥2000 |
| `research` | ≥2000 |
| `comparison` | ≥1500 |
| `case_study` | ≥1500 |
| `product_tutorial` | ≥1500 |

*tools · v1.1 · 2026-06-23*
