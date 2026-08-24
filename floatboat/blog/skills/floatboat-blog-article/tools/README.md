# Floatboat Blog Tools（Phase 5 · 自包含）

通用验证脚本 + Floatboat category 枚举。**随 skill 文件夹分发**，无需外部依赖。

## 用法（从 `floatboat/` 项目根目录）

```bash
# 根目录成稿
python blog/skills/floatboat-blog-article/tools/frontmatter_validator.py blog/07-ai-follow-up-automation.md --keyword "AI follow-up automation" --categories "Research,Comparison,Product,Reference,Claude,DeepSeek,OpenAI,World Cup"

python blog/skills/floatboat-blog-article/tools/word_count_narrative.py blog/07-ai-follow-up-automation.md --intent product_tutorial --min 2000

python blog/skills/floatboat-blog-article/tools/link_checker.py blog/07-ai-follow-up-automation.md

# 子目录成稿（claude/ deepseek/ openai/ worldcup/ Updates/）
python blog/skills/floatboat-blog-article/tools/frontmatter_validator.py blog/claude/35-what-is-claude-cowork.md --keyword "what is Claude Cowork" --categories "Research,Comparison,Product,Reference,Claude,DeepSeek,OpenAI,World Cup"

python blog/skills/floatboat-blog-article/tools/word_count_narrative.py blog/openai/57-codex-harness-open-source.md --intent research --min 2400
```

## `--intent` 与文章类型（H3 硬门槛）

| SKILL §2 类型 | 创作目标 | `--intent` | 推荐 `--min` |
|--------------|---------|------------|-------------|
| Research / Glossary | 2400–3500 | `research` | 2400 |
| Comparison | 2800–3500 | `comparison` | 2800 |
| Ranking / Listing | 2400–3200 | `comparison` | 2400 |
| Alternative | 2200–3000 | `comparison` | 2200 |
| Product / Scenario | 2000–2700 | `product_tutorial` | 2000 |
| Announcement | 1500–2000 | `announcement` | 1500 |

## 脚本

| 脚本 | Gate | 说明 |
|------|------|------|
| `frontmatter_validator.py` | F1–F8 | `--categories` 含 OpenAI 等 Floatboat 枚举 |
| `word_count_narrative.py` | H3 | 优先用 `--min` 传入上表推荐值 |
| `link_checker.py` | G2/G6 | 可选 `--forbidden` 前缀 |

## 维护者同步 SSOT（内网用）

```powershell
Copy-Item "E:\Agent执行\blog-create\tools\*.py" `
  "e:\clients\floatboat\blog\skills\floatboat-blog-article\tools\" -Force
```

*floatboat tools · v5.1 · 2026-08-24 · self-contained*
