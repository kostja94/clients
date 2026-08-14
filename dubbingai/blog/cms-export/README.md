# Dubbing AI CMS 博客镜像（cms-export）

CMS 已发布文章的 **Markdown 忠实镜像**，与 [`../`](../README.md) 根目录下的 **2026 新稿**（`NN-{slug}-2026.md`）分目录存放。

| 目录 | 用途 | 文件命名 |
|------|------|----------|
| `blog/` 根 | 2026+ pillar / 重写稿 | `NN-{slug}-2026.md` |
| `blog/cms-export/` | CMS 已发布镜像 | `{slug}.md` |

线上 URL：`https://dubbingai.io/blog/{slug}/`

---

## Frontmatter 规范

与 [03-how-to-change-your-voice-2026.md](../03-how-to-change-your-voice-2026.md) 对齐，并增加 CMS 溯源字段。完整示例见 [_template.md](./_template.md)。

必填：`title`、`description`、`slug`、`date`、`author`、`status`、`source`、`canonical`、`migrated_at`

---

## manifest.csv（迁移 SSOT）

| 列 | 说明 |
|----|------|
| `slug` | 文章 slug |
| `url` | 完整 CMS URL |
| `category` | CMS 分类（抓取后回填） |
| `lang` | `en` / `pt` 等 |
| `status` | `pending` · `done` · `skip` · `error` |
| `date_published` | CMS 发布日 |
| `migrated_at` | 入库日 |
| `notes` | 备注（301、skip 原因等） |
| `superseded_by` | 301 目标 slug |
| `batch` | `P0`–`P3` 批次 |

重新生成清单（从 URL 源）：

```bash
python scripts/generate_manifest.py
```

---

## 转换脚本

依赖（一次性）：`pip install beautifulsoup4 html2text lxml`

```bash
# P0 试点
python scripts/fetch_and_convert.py --batch P0

# 按批次全量（请求间隔默认 1s）
python scripts/fetch_and_convert.py --batch P1
python scripts/fetch_and_convert.py --batch P2
python scripts/fetch_and_convert.py --batch P3

# 单篇重跑
python scripts/fetch_and_convert.py --slug jett-voice-changer --force
```

正文来源：WordPress `.entry-content` → HTML→Markdown（html2text），**忠实镜像**，不改写 SEO。

---

## 批次定义

| 批次 | 范围 |
|------|------|
| **P0** | 5 篇试点（结构各异） |
| **P1** | slug 含 dubbing-ai / voice-changer / discord / valorant / fortnite |
| **P2** | slug 含 soundboard / sound-effect / meme / soundbutton / sfx |
| **P3** | 其余长尾 |

**Skip**：`hello-world`（WordPress 默认稿）

**301 标注**（仍保留镜像）：`top-5-voice-changers`、`top-10-free-voice-changer-online-2025` → `superseded_by: best-ai-voice-changer`

---

## 进度（2026-06-15）

| 指标 | 数量 |
|------|------|
| manifest 总行 | 257 |
| `done` | 256 |
| `skip` | 1（`hello-world`） |
| `error` | 0 |

验收：`python scripts/qa_spotcheck.py`

---

## 第二阶段（未开始）

- 补 `related` 与 [internal-external-links-checklist.md](../internal-external-links-checklist.md) 互链
- 竞品外链 `nofollow`
- 图片本地化 `/blog/images/`

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [../README.md](../README.md) | Blog 总览、新稿命名、301 表 |
| [../internal-external-links-checklist.md](../internal-external-links-checklist.md) | 内链规范（第二阶段） |
| [../../dubbingai-keywords.md](../../dubbingai-keywords.md) | 关键词映射 |
