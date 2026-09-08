# Forbidden Loads — 不得触发完整创作工作流的场景

> 下列场景可加载 skill 主文件做路由，但 **不得** 跑 Phase 0–6 全文创作。title/description 专项只读 `references/meta-title-description.md`。

## 1. title / description 专项优化（轻量路径）

**输入示例**：
- "优化 /blog/02-what-is-vibe-coding 的 meta description"
- "给 best-ai-mobile-app-builders 写一个 SERP title"
- "批量检查博客 description 字符数"

**应触发**：`medo-blog-article` → **仅** `references/meta-title-description.md`（禁止 Phase 0–6、禁止改正文）

**若误跑完整创作**：浪费上下文且可能覆写已有稿的 frontmatter。

---

## 2. 工具页 / 落地页内容（非博客正文）

**输入示例**：
- "为 /ai-mobile-app-builder 写落地页文案"
- "/features 页 SEO 正文优化"

**应触发**：对应页面策略文档（`medo-site-structure.md` 等，skill 外，由人类驱动）

**若误触发 blog-article**：会按博客类型路由，产出 editorial 内容而非工具页转化文案，且违反 A4（博客不抢工具页词）。

---

## 3. 非 medo.dev 博客

**输入示例**：
- "帮我写一篇 Medium 文章讲 AI app builder"
- "给另一个产品写 guest post"

**应触发**：通用 blog skill 或无 skill（手动创作）

**若误触发 blog-article**：会强制注入 MeDo 品牌上下文、Credits 消费单位与 URL 白名单。

---

## 4. 非英文内容

**输入示例**：
- "写一篇中文的 AI 建站教程"

**应触发**：另建 ZH skill（当前不存在）

**若误触发 blog-article**：Voice、BLUF、TL;DR 结构均为英文设计，中文输出质量不可控。

---

## 5. 已发稿回溯审计

**输入示例**：
- "对 blog/03 做合规扫描，只输出 diff 清单"

**应触发**：`references/portable/retro-audit.md`（只读扫描，不改文）

**若误跑完整创作**：会尝试重写既有文章而非产出 diff。

---

## 6. 发布前终审

**输入示例**：
- "对 NN-slug 做发布前终审打分"

**应触发**：`references/portable/final-audit.md`（十维加权 S/A/B/C/D）

**若误跑完整创作**：混淆创作自检与独立审核（SelfCheck = audit-ready；终审 ≥70 + P0 Pass = publish-ready）。
