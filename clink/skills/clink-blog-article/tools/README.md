# Clink Blog Tools（Phase 5）

Clink fork（Conclusion→FAQ 结构校验 + 类别枚举）+ SSOT 对齐的 `link_checker`。

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

## `--intent` 与文章类型

| 类型 | `--intent` | 推荐 `--min` |
|------|------------|-------------|
| BrandIntroduction | `brand` | 2500 |
| Comparison | `comparison` | 1600 |
| Product / StripeRisk | `product` | 1800 |
| Opinion / IndustryNews | `opinion` | 1800 |
| EvaluationComparison | `evaluation` | 2500 |
| GlossaryTerm | `glossary` | 1800 |

## 脚本

| 脚本 | Gate | 说明 |
|------|------|------|
| `frontmatter_validator.py` | F1–F8 + structure | **Clink fork**；类别含 Agentic Payments / Industry News / Stripe Risk |
| `word_count_narrative.py` | H3 | Clink intent（brand/evaluation/glossary） |
| `link_checker.py` | G2/G6 | 内置 forbidden 前缀 |

## 同步 SSOT

```powershell
Copy-Item "E:\Agent执行\blog-create\tools\link_checker.py" `
  "e:\clients\clink\skills\clink-blog-article\tools\" -Force
# frontmatter_validator / word_count 保留 Clink fork
```

*clink tools · v2.0 · 2026-08-23 · L1 overlay on blog-create SSOT*
