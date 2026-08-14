# Dubbing AI blog

英文 Markdown 文章存放于本目录（`*.md` + YAML frontmatter），与公开 URL **`https://dubbingai.io/blog/{slug}`** 对齐。正文语言以 **英文** 为主，与 [dubbingai.md](../dubbingai.md) 一致。

**韩国 Naver Blog**：韩文 Markdown、ONE 发刊 SOP 与 **第一篇品牌长文** 见 [`../localization/`](../localization/readme.md)（与英文 `blog/` **分目录**，勿混流水线）。

**关键词与页面映射**：[dubbingai-keywords.md](../dubbingai-keywords.md) · **Voice Changer 程序化**：[dubbingai-voice-changer.md](../dubbingai-voice-changer.md) · **竞品**：[dubbingai-competitors.md](../dubbingai-competitors.md)

**Agent 创作 skill**：[dubbingai-blog-article](../skills/dubbingai-blog-article/SKILL.md)（Track S 战略新稿 + Track C cms-export 长尾；v1.2.1）

---

## 命名与 Frontmatter

| 约定 | 说明 |
|------|------|
| **新稿** | `NN-{slug-kebab}-2026.md`（序号 + slug + 年份） |
| **CMS 镜像** | `cms-export/{slug}.md`（与线上 slug 1:1，见 [cms-export/README.md](./cms-export/README.md)） |
| `slug` | **不含年份**（新稿）；CMS 镜像 slug 与 URL 完全一致（可含 `-2025` 等） |
| `title` | 可含年份与主意图词，供 SERP 使用 |
| `related` | 其他博文的 `slug` 数组，不含域名 |

```yaml
---
title: "Best AI Voice Changer (2026): Top Picks for Gaming, Streaming & Real-Time Chat"
description: "Compare the best AI voice changers for real-time gaming, Discord, and streaming—plus soundboard picks. Updated for 2026."
slug: "best-ai-voice-changer"
date: 2026-04-20
author: "Kostja"
---
```

> **2026-08-11 起废弃**：`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS 单独管理；keywords/related 由正文内链与 CMS 配置承载）。

封面图路径需与 CMS/静态资源一致后替换占位。

---

## 301 重定向（站内待执行）

以下旧文计划 **301** 至新 pillar（上线后由你方在服务器/CDN/WordPress 配置）：

| 旧 URL | 新 URL（目标） |
|--------|----------------|
| `/blog/top-5-voice-changers/` | `/blog/best-ai-voice-changer/` |
| `/blog/top-10-free-voice-changer-online-2025/` | `/blog/best-ai-voice-changer/` |

发布后请在全站搜索替换内链，并提交 Search Console 变更网址（如适用）。

---

## 已放入草稿 / 已发布镜像

| File | slug | 说明 |
|------|------|------|
| [01-best-ai-voice-changer-2026.md](./01-best-ai-voice-changer-2026.md) | `best-ai-voice-changer` | Voice changer 词簇 pillar：最佳 AI 变声器盘点（2026） |
| [02-how-to-change-google-assistant-voice-2026.md](./02-how-to-change-google-assistant-voice-2026.md) | `how-to-change-google-assistant-voice` | 更改 Google Assistant 语音；与实时变声意图分流 + 内链 Dubbing |
| [03-how-to-change-your-voice-2026.md](./03-how-to-change-your-voice-2026.md) | `how-to-change-your-voice` | How-to：Web/PC、路由检查清单、场景；与榜单/Assistant 文互链 |
| [04-dubbing-ai-vs-voicemod-2026.md](./04-dubbing-ai-vs-voicemod-2026.md) | `dubbing-ai-vs-voicemod` | Alternative：Dubbing AI vs Voicemod 公平对比；PromoteFrom cms-export |

**下一文件序号：05**（与 skill `references/content-graph.md` 同步）

---

## CMS 归档（cms-export）

CMS 已发布旧文的 **Markdown 忠实镜像**（约 257 篇），与上表 **2026 新稿** 分目录：

- 目录：[cms-export/](./cms-export/)
- 清单：[cms-export/manifest.csv](./cms-export/manifest.csv)（`status`: pending / done / skip / error）
- 转换：`python cms-export/scripts/fetch_and_convert.py`

第一阶段仅 HTML→MD + frontmatter，**不改写**正文 SEO；内链优化见第二阶段。

---

## 关联文档

| 文档 | 用途 |
|------|------|
| [dubbingai.md](../dubbingai.md) | 产品定位与核心信息 |
| [localization/readme.md](../localization/readme.md) | **韩国 Naver**：韩文成稿目录、与英文 blog 分工 |
| [dubbingai-internal-links.md](../dubbingai-internal-links.md) | 全站内链总纲 |
| [internal-external-links-checklist.md](./internal-external-links-checklist.md) | **Blog** 内链分层、博文互链矩阵、`related` 与抽检表 |
| [cms-export/README.md](./cms-export/README.md) | CMS 已发布文章镜像、manifest、转换脚本 |

---

## Skill 使用与版本同步

### 触发语（Agent）

```
按 dubbingai-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Comparison|HowTo|IntentSplit|Alternative|...} 文章。
Track：{S|C|auto}。发布目的：{SEO|品牌|转化|趋势}。
```

详见 [skills/dubbingai-blog-article/SKILL.md](../skills/dubbingai-blog-article/SKILL.md) §0。

### 发布后 checklist（人类）

每发布一篇 Track S 新稿须：

1. 在本 README「已放入草稿」表新增一行
2. bump `skills/dubbingai-blog-article/references/content-graph.md` §4.1 下一序号
3. 更新 [internal-external-links-checklist.md](./internal-external-links-checklist.md) 互链矩阵（如适用）
4. bump `skills/dubbingai-blog-article/SKILL.md` frontmatter `version` patch（如 1.0.0 → 1.0.1）
5. Track C 新稿/刷新：更新 [cms-export/manifest.csv](./cms-export/manifest.csv) 的 `notes` / `superseded_by`
6. PromoteFrom cms：在 cms-export 原稿填 `superseded_by: {slug}`

**当前 skill 版本**：1.2.1 · **下一文件序号**：05
