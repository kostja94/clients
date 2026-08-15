# Oginify Project Config — 品牌、URL 白名单、Gate

> 加载时机：Phase 0 / Phase 0R / Phase 5
> 主文件：SKILL.md §1 指针

---

## 1. 品牌与产品速查

| 配置项 | 值 |
|--------|-----|
| 品牌 | Oginify |
| 主域名 | oginify.com |
| 博客前缀 | /blog/ |
| 品类 one-liner | Open Graph cards, instantly — AI OG image generator from any URL |
| 核心机制 | 粘贴 URL → 读取页面品牌色/标题/logo/语气 → 生成 4 张 1200×630 卡片（1 on-brand + 3 wildcards） |
| 生成时长 | ~30 秒 |
| 作者/创始人 | Kostja（alignify.co）· Built with Lovable |
| 开源版 | social-cards-skills（MIT，GitHub kostja94/social-cards-skills） |
| 署名默认 | `Oginify`（作者池：Oginify / Kostja / {团队具体成员}） |
| 语言 | 英文正文；中文仅沟通用 |
| 日期策略 | 一天一篇；错开日期 |

**差异化核心**：URL-first（无 prompt、无模板选择、无注册）vs 通用生图（Gemini/GPT Image/Midjourney 需自己写 prompt）vs 代码驱动（Vercel OG 需写 JSX）。

---

## 2. URL 白名单（内链优先）

| 类型 | 路径示例 | 上线状态 |
|------|---------|:---:|
| 首页 | `/` | ✅ |
| 博客 | `/blog/{slug}` | ✅ |
| 免费工具 | `/text-to-og-image` · `/image-to-og-image` · `/bulk-og-image-generator` · `/twitter-card-generator` · `/github-social-preview-generator` | ✅ |
| 免费检查 | `/og-scorer` · `/open-graph-validator` · `/free-og-image-maker` | ✅ |
| 探索页 | `/pages/{page-type}` · `/websites/{site-type}` · `/styles/{style}` · `/gallery` · `/explore` | ✅ |
| 集成/用例 | `/integrations` · `/use-cases` | ✅ |
| 定价 | `/pricing` | ✅ |
| 登录/注册 | `/login` · `/signup` | ✅（不作主 CTA） |

**G6 规则**：不链未上线路径；forthcoming ≤1 且仅脚注；正文核心流程不用 forthcoming 链接。**blog 内链 ≥2**。

---

## 3. G1–G7 + P1–P6 + C1–C4 阻断 Gate

### G1–G7（通用）

| # | 阻断条件 | Oginify 判定示例 |
|---|---------|-----------------|
| G1 | 事实错误 | 免费额度/定价/机制与 oginify.com 现网矛盾 |
| G2 | 死链 | 内链 404；工具页路径错误 |
| G3 | 无来源数字 | 6 张/天、$0.99、$7.90、$29、竞品定价无 attribution |
| G4 | 竞品/产品状态错误 | Gemini/GPT Image/Midjourney 版本或 GA 状态与官方公告矛盾 |
| G5 | 产品能力夸大 | 禁「唯一支持」「全球首个」「唯一能生成」 |
| G6 | 内链指向未上线页面 | 对照 §2 白名单；forthcoming >1 → Fail |
| G7 | 品牌/合规风险 | 对比文贬低竞品；无来源 CTR 承诺 |

### P1–P6（Oginify 产品专用）

| # | Gate | Pass 条件 | 反例 |
|---|------|----------|------|
| P1 | 产品数字 as-of | 免费额度/定价/生成时长 claim 含 `as of {month} {year}` + 来源 | 「6 张/天」无 as-of |
| P2 | URL-first 边界 | 承认通用生图（Gemini/GPT Image/Midjourney）**能做** OG 卡片，只是需手动处理尺寸/文字/托管；不写 Oginify「唯一无需 prompt」 | 「只有 Oginify 不用写 prompt」 |
| P3 | 1200×630 规格 | 尺寸/平台裁剪 claim 有来源（oginify.com 或 ogp.me） | 「1200×630 是标准」无来源 |
| P4 | SaaS vs 开源边界 | social-cards-skills 是 Oginify 的 MIT 开源发行版（自带模型/资产、自己运行）；Oginify 是托管 SaaS（粘贴 URL 即用） | 「Oginify 是开源的」 |
| P5 | 竞品公平 | Comparison/Ranking/Alternative 每竞品 ≥1 真实优势 + ≥1 非 Oginify 更合适场景 | 只写竞品缺点 |
| P6 | 禁夸大措辞 | 无 magic / zero-work / promptless / 「自动提升 CTR 300%」 | 「零工作量」「魔法般生成」 |

### C1–C4（内容冲突）

| # | Gate | Pass 条件 |
|---|------|----------|
| C1 | slug 冲突未声明 | 与 content-graph §5 冲突表重叠须先声明处置 |
| C2 | Hub 抢词 | 新稿 title/H1 不得抢 `what-is-open-graph-image` Hub 的 P0 词（open graph image 定义） |
| C3 | 程序化页 duplicate | 不得复制 `/free-og-image-maker` 等工具页全文 |
| C4 | 301 目标冲突 | slug 已被 301 到别处（如 `best-og-image-generator` → hub）不得新建 |

---

## 4. 前端 frontmatter Schema

```yaml
---
title: "Title Case — Subtitle After Em Dash"   # 45–65 chars，含主关键词
description: "120–160 chars, benefit + main intent keyword"
slug: "kebab-case-slug"                        # 常青，无年份，5–8 词，≤60 chars
date: 2026-08-XX                               # 发布时间，永不改变
updated: 2026-08-XX                            # 可选；实质性更新才改
author: "Oginify"                              # 每次创作确认：Oginify | Kostja | {具体成员}
category: "Tutorial | Guide | Case Study | Reference | Product"
secondary_category: "Open Graph"
articleFormat: "Ranking | —"                   # Ranking 文必填 Ranking
---
```

> **2026-08-15 起**：正文不设 `## Related articles` 区块；所有内链均为**上下文内链**。`image` / `keywords` / `related` 不再写入 frontmatter（image 由 CMS/OG 管理；keywords 由正文与 CMS 配置承载；related 已取消）。
>
> **日期最佳实践**：`date` = 发布时间，永不改变；`updated` 仅实质性更新时修改。页面只显示一个日期。

---

## 5. 日期发布策略

| 规则 | 说明 |
|------|------|
| 一天一篇 | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| 错开方向 | 从锚点日往前排，越重要的文章排越近 |
| 避让已占用日 | 已有文章的日期不重复使用 |

---

## 6. E-E-A-T 增强

| 维度 | Oginify Blog 做法 |
|------|------------------|
| Experience | URL-first workflow 的步骤来自产品实测（粘贴 URL → 4 变体 → 下载 PNG → 粘贴 meta tags） |
| Expertise | URL-first vs 通用生图 vs 代码驱动 三分类框架技术准确 |
| Authoritativeness | P0 数字官方来源（oginify.com、ogp.me、平台官方定价页） |
| Trustworthiness | 诚实竞品优势、as-of 标注、无 CTR 虚假承诺 |
