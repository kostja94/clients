# Clink Blog Tools（Phase 5）

Clink fork：frontmatter 校验（Conclusion→FAQ 结构 + category 枚举）+ SSOT 对齐的 link_checker。

## 用法（从 `clink/` 项目根目录）

```bash
# 根目录成稿
python skills/clink-blog-article/tools/frontmatter_validator.py blog/01-what-is-clink.md --keyword "Clink"
python skills/clink-blog-article/tools/word_count_narrative.py blog/01-what-is-clink.md --intent brand --min 2500
python skills/clink-blog-article/tools/link_checker.py blog/01-what-is-clink.md

# 集群成稿
python skills/clink-blog-article/tools/frontmatter_validator.py blog/stripe-risk/25-stripe-account-suspended.md --keyword "Stripe account suspended"
python skills/clink-blog-article/tools/word_count_narrative.py blog/agentic-payments/04-agent-payments.md --intent opinion --min 1800
```

## 参数来源（SSOT，非重复定义）

- `--intent` / `--min` 映射：`references/article-types.md` §1（每类型行含默认 Mode 与词数下限）
- `--forbidden` 前缀：`references/project-config.md` §2（可链接白名单 + G6 禁止项）

## 脚本

| 脚本 | Gate | 说明 |
|------|------|------|
| `frontmatter_validator.py` | F1–F8 + structure | **Clink fork**；类别含 Agentic Payments / Industry News / Stripe Risk / secondaryCategory |
| `word_count_narrative.py` | H3 | Clink intent（brand/comparison/product/opinion/evaluation/glossary） |
| `link_checker.py` | G2/G6 | 内置 forbidden 前缀 |

## 维护

`frontmatter_validator.py` / `word_count_narrative.py` 为 Clink fork，就地维护；`link_checker.py` 与通用 SSOT 对齐（维护通用版本后同步，见 `references/portable/README.md`）。

---

*clink tools · v3.0 · 2026-09-08 · self-contained*
