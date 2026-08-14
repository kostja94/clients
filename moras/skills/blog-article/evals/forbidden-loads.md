# Forbidden Loads — 不得触发完整创作工作流的场景

> 下列场景可加载 skill 主文件做路由，但 **不得** 跑 Phase 0–6 全文创作。title/description 专项只读 `references/meta-title-description.md`。

## 1. title/description 专项优化（轻量路径）

**输入示例**：
- "优化 /blog/faceless-tiktok-shop-videos 的 meta description"
- "给 TikTok Shop hooks 文章写一个 SERP title"
- "批量检查博客的 description 字符数"

**应触发**：`moras-blog-article` → **仅** `references/meta-title-description.md`（禁止 Phase 0–6、禁止改正文）

**若误跑完整创作**：浪费上下文且可能覆写已有稿。

---

## 2. TVG 落地页长文

**输入示例**：
- "为 /tiktok-video-generator/skincare 写一篇品类落地页"
- "mattress vertical 页面正文优化"

**应触发**：TVG 模板体系（非本 skill 范围）

**若误触发 blog-article**：会按博客类型路由，产出 editorial 风格内容而非 transactional landing page。

---

## 3. 非博客页 metadata

**输入示例**：
- "给首页写 title 和 description"
- "优化 /tiktok-video-generator 的 meta"

**应触发**：产品仓 SEO 或查阅 `_archive/meta-title-description/` 历史规则（非博客范围）

---

## 4. 非 moras.ai 博客

**输入示例**：
- "帮我写一篇 Medium 博客讲 TikTok Shop 选品"
- "给客户写 guest post 关于 affiliate marketing"

**应触发**：通用 blog skill 或无 skill（手动创作）

**若误触发 blog-article**：会强制注入 Moras 产品上下文、品牌后缀和合规规则。

---

## 5. 非英文内容

**输入示例**：
- "写一篇中文的 TikTok Shop 入门教程"
- "日本語で TikTok Shop の記事を書いて"

**应触发**：另建 ZH skill（当前不存在）

**若误触发 blog-article**：所有语言策略、Voice 标准均为英文设计，中文输出质量不可控。

---

## 6. 纯数据/报告类内容

**输入示例**：
- "整理 TikTok Shop Q1 2026 GMV 数据报告"
- "做一份 affiliate commission rates 对比表格"

**应触发**：通用数据分析 skill 或手动

**若误触发 blog-article**：会套用博客叙事弧和 H2 模板，产出 editorial 格式而非数据报告格式。
