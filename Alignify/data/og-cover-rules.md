# Alignify OG 封面规则（v3）

> 脚本 SSOT  companion：`scripts/ops/generate-og-cover.py` · registry：`data/og-prompt-registry.json`

---

## 1. 三条硬规则

### R1 — 与页面强相关

每张 OG 的**视觉主体**必须让人一眼看出「这篇讲什么」，不能是通用 abstract 装饰。

| 页面类型 | 应出现的视觉（示例） |
|----------|---------------------|
| Tools Best（如 image-generator） | prompt 输入框 + 生成图网格、对比/放大镜、与品类相关的样张 |
| Blog 对比文 | 对比两侧产品 UI 或能力示意图（无真实 logo） |
| SEO / Marketing 教程 | 与 H1 主题直接相关的示意图（搜索框、sitemap、邮件等） |

**禁止**：纯色块、空网格、与 slug 无关的 generic tech 背景。

`composition` 字段写 **2–3 个视觉元素**，用英文描述（模型遵循更好）；画布上的标签语言随 `locale`。

### R2 — 文字像 PPT，适中即可

**AI 画布上只允许出现 registry 里的标题文字**，其余信息用图表达。

| 允许 | 禁止 |
|------|------|
| `headline` + 可选 `headline_line2`（最多 2 行主标题） | 排名列表、模型名文字、脚注、slogan |
| 可选 **一行** `subtitle` + 可选 **一行** `tagline`（EN 宜稍丰富；ZH 宜极简） | 箭头旁标签、多张小卡片说明文字 |
| — | 「示例提示词」标题、Style/Ratio 等 UI 小字 |

**作者名 `Kostja` 不由 AI 渲染**，由脚本后期叠加（保证清晰、统一）。

### R3 — 品牌标记（v3.5：三选一，无缝融入）

**Kostja · Alignify 字标 · Logo** 不由 AI 渲染，由脚本后期叠加 —— **每张图只选其中一个**。

| 模式 | 样式 |
|------|------|
| `kostja` | 小号 byline，半透明纸纹底 + 轻阴影，**无**色块徽章 |
| `alignify` | 小号 「Alignify」字标，同样轻量 |
| `logo` | 小号 logo（~44px），**无** accent 色方块底，仅 soft shadow |

**规则**
- 每次生成 **仅 1 个**品牌标记（哈希稳定：`kostja` / `alignify` / `logo` 轮换）
- 角落：`bottom-left` · `bottom-right` · `top-right`（避开标题区）
- 设计目标：**无缝融入**拼贴，不像后期贴上去的贴纸
- CLI：`--brand-mode kostja|alignify|logo` · `--brand-corner` · `--shuffle-branding`

> **已验收图不改**：现有 staging 图（含 image-generator、marketing 批次等）保持原样，规则仅作用于**后续新生成**。

### R0 — 先 LLM 分析（v4 流程）

生图前必须产出 `data/og-briefs/{section}/{slug}/brief.json`：
- `visual_anchors` — 必选视觉，#1 为 HERO
- `anti_patterns` — 禁止出现的错误隐喻
- `locales.en/zh.composition` — 英文视觉描述

工具：`scripts/ops/analyze-og-page.py`（GPT-4o，需 `OPENAI_API_KEY`）

---

## 2. Registry 字段

```json
{
  "section": "tools",
  "slug": "image-generator",
  "locale": "en",
  "style": "editorial-collage",
  "accent": "klein-blue",
  "author": "Kostja",
  "headline": "BEST AI IMAGE GENERATORS",
  "headline_line2": "(2026)",
  "subtitle": "Text-to-Image · Image-to-Image · Style Control",
  "tagline": "Compare Top Models Side by Side",
  "composition": "Visual-only: (1) prompt card + emerging thumbnail. (2) 2x2 AI sample grid. (3) magnifying glass on one sample.",
  "status": "pending"
}
```

| 字段 | 必填 | 说明 |
|------|:---:|------|
| `composition` | ✅ | 2–3 个**与页面相关**的视觉元素，英文，**不写**要出现在图上的额外文字 |
| `headline` | ✅ | 主标题 |
| `headline_line2` | 可选 | 第二行（年份等） |
| `subtitle` | 可选 | 一行副标题 |
| `tagline` | 可选 | 第二行副标题（EN 推荐；ZH 通常省略） |
| `author` | 可选 | 默认 `Kostja` |
| `accent` | 可选 | `klein-blue` / `mars-green` / `titian-red` / `alignify-navy` |

---

## 3. 验收清单

- [ ] 不看 URL 也能猜出页面主题
- [ ] 画布除标题/副标题外无多余文字块
- [ ] **仅 1 个**品牌标记（Kostja / Alignify / Logo），融入自然、无厚重贴纸感
- [ ] 1200×630 · **WebP** q≥90 · EN/ZH 分图 · 语言正确
- [ ] 上下文仓验收 → `approved` → `migrate-og-covers.py`

---

## 4. 写 composition 的模板

```
Visual-only collage for [{section}/{slug} — {one-line page topic}]:
(1) {primary metaphor UI/object}
(2) {secondary supporting visual}
(3) optional {third accent visual}
Paper torn edges, halftone. No extra text labels, no lists, no footnotes.
```

**示例 — image-generator**

```
Visual-only collage for AI image generator tools comparison page:
(1) Prompt input card with one small generated fox watercolor thumbnail.
(2) 2x2 grid of four distinct AI outputs (portrait, landscape, product, abstract) — images only.
(3) Magnifying glass over the fox sample.
No ranking text, no model names as text, no arrow labels.
```
