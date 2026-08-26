# Moras Blog Tools（Phase 5 · 自包含）

Moras 博客 Phase 5 验证工具，含 `/blog/` slug overlay（`--moras-slug`）。**随 skill 文件夹分发**，无需外部依赖。

## 用法（从 `moras/` 项目根目录）

```bash
python skills/blog-article/tools/frontmatter_validator.py blog/tiktok-video/05-tiktok-shop-hooks-framework.md --keyword "TikTok Shop hooks" --moras-slug

python skills/blog-article/tools/word_count_narrative.py blog/creator-affiliate/01-how-to-make-money-on-tiktok.md --intent pillar --min 3500

python skills/blog-article/tools/link_checker.py blog/tiktok-video/03-tiktok-shop-videos-without-filming.md --forbidden "/use-cases/,/app/,/auth/,/admin/"

python skills/blog-article/tools/link_audit.py   # 在 moras/blog/ 目录运行；R1–R4 + 入链快照
```

## `--intent` 与文章类型（H3 硬门槛）

| SKILL §2 类型 | 创作目标 | `--intent` | 推荐 `--min` |
|--------------|---------|------------|-------------|
| Pillar | 3500–5000 | `pillar` | 3500 |
| Setup | 2500–3500 | `howto` | 2500 |
| Production | 2800–3800 | `product` | 2800 |
| Research | 2800–3500 | `research` | 2800 |
| Framework | 2500–3200 | `framework` | 2500 |
| Strategy | 2500–3200 | `howto` | 2500 |
| Side Hustle | 2200–3000 | `howto` | 2200 |
| Diagnosis | 2500–3200 | `diagnosis` | 2500 |
| Platform Ops | 1800–2500 | `announcement` | 1800 |

## Moras 专属

| 项 | 说明 |
|----|------|
| `--moras-slug` | frontmatter `slug` 格式 `/blog/{kebab}`；`category` 可选 |
| `--forbidden` | 默认禁链前缀见 project-config G6 |
| title/description | 45–60 / 140–160（见 meta-title-description.md） |

*moras tools · v2.1 · 2026-08-24 · self-contained*
