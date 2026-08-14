# FinalRound Tools（Skill tools）

Phase 5 机器预检脚本。运行目录：`finalround/skills/finalround-blog-article`。

## 脚本

| 脚本 | 用途 | 用法 |
|------|------|------|
| `frontmatter_validator.py` | Frontmatter 机器检查（必填字段、slug kebab-case/常青/长度、title 含主关键词、description 长度） | `python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "primary kw"` |
| `word_count_narrative.py` | 叙事词数（排除 frontmatter/表格/FAQ）+ H3 字数硬门槛 | `python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {announcement\|review\|alternative\|roundup\|prep\|research\|industry}` |
| `link_checker.py` | 内链白名单（G6）、禁链路径、F1–F5 红线扫描、外链存活（可选） | `python tools/link_checker.py ../../blog/NN-{slug}.md --forbidden /zh --check-live` |

## 说明

- 任一脚本 `FAIL` → 修复后重跑，再进人工 SelfCheck
- `link_checker.py` 的 `F5` 提示为 warning（"undetectable" 是否作为首要卖点需人工判定）
- 退出码：0 = PASS，1 = FAIL

## 要求

Python 3.8+；无第三方依赖（标准库）。
