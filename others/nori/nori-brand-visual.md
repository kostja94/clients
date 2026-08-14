# Nori — Brand Visual Guidelines

> 遵循 [brand-visual](../../.cursor/skills/components/branding/brand-visual/SKILL.md) | 关联 [nori.md](./nori.md)  
> **来源**：[heynori.com](https://heynori.com/) 构建产物（Tailwind CSS v4 变量，2026-03-24 抓取）。**哈希文件名会随部署变化**，更新视觉时请重新在浏览器 DevTools → Computed / Sources 中核对。  
> 用于：官网、落地页、功能页、博客配图、社媒、Brief 给设计与前端。

**Last updated**: 2026-03-24

---

## Brand Identity

| 项 | 内容 |
|----|------|
| **Brand Name** | Nori |
| **One-line** | AI-powered family assistant — schedules, tasks, meals, routines（见 [nori.md](./nori.md) §1） |
| **Hero 文案示例** | "Make family life easier with AI, with Nori" / "Just ask Nori what you need…" |
| **Website** | https://heynori.com/ |
| **Web App** | https://heynori.com/app |
| **Help** | https://help.heynori.com/ |

---

## Logo

- **主站**：导航与页脚使用 Nori 字标 + 图形标识（具体 SVG/PNG 以 `public.heynori.com` 与站点 `_next/static/media` 为准）。
- **Minimum Clear Space**：建议 **≥ 图标高度的 0.5×** 四周留白；勿贴边或与高对比杂纹重叠。
- **Favicon**：以线上站点 `favicon` / `apple-touch-icon` 为准（随构建更新）。
- **禁止**：横向拉伸字标、任意改色导致对比不足、在杂乱照片上放置无描边/无底色的浅色标。

*若需印刷或合作方矢量包，建议由产品侧导出官方 Logo Kit 并在此补充路径。*

---

## Color Palette

### A. 营销页 / 浅色氛围（首页主调）

站点使用 **亚麻色（linen）背景层级** + **深灰文字（基于 #151515 透明度阶梯）** + **暖色品牌强调（橙/琥珀系）**。

| Token / 名称 | Hex（或说明） | 用途 |
|--------------|---------------|------|
| **Text primary（--text-1）** | `rgb(21,21,21)` ≈ `#151515` | 主标题、核心正文 |
| **Text secondary（--text-2）** | 同上 80% 不透明 | 次级正文 |
| **Text tertiary（--text-3）** | 同上 60% 不透明 | 说明、辅助段落 |
| **Background dark** | `#e0dacc`（--linen-40） | 深一点的区块底 |
| **Background mid** | `#ede8da`（--linen-30） / `#f5f2e9`（--linen-20） | 中段层级 |
| **Background light** | `#fcfbf7`（--linen-10） | 浅底、卡片感 |
| **Brand accent 50** | `#d68125` | 主 CTA、强调色（暖橙） |
| **Brand accent 40** | `#e6953d` | Hover、渐变高光 |
| **Brand accent 80** | `#945107` | 深强调、深色上的点缀 |
| **Secondary lilac** | `#f7d9ff` | 装饰色块（与插画体系搭配） |
| **Secondary sky** | `#b4dcff` | 装饰色块 |
| **Secondary mint** | `#d0f49d` | 装饰色块 |
| **Secondary butter** | `#fefd9f` | 装饰色块 |
| **Reversed white** | `#ffffff` | 按钮反白、卡片 |

### B. 组件 / 语义色板（设计系统向，与 Untitled UI 类命名一致）

站内 CSS 同时包含 **紫色系 brand** 与 **灰蓝、成功、警告、错误** 等语义色，适用于表单、按钮、标签等产品 UI（含官网内嵌组件）。

| 用途 | 示例 Token | 示例 Hex |
|------|------------|----------|
| Brand / 主色倾向 | `--color-brand-500` | `#9e77ed` |
| Brand 深 | `--color-brand-900` | `#42307d` |
| 成功 | `--color-success-500` | `#17b26a` |
| 警告 | `--color-warning-500` | `#f79009` |
| 错误 | `--color-error-500` | `#f04438` |
| 边框 / 分割线 | `--color-gray-200` 等 | 见构建 CSS |

### 无障碍

- 正文与背景对比建议 **≥ 4.5 : 1**；大标题 **≥ 3 : 1**。
- **勿单独用颜色**表达状态；成功/错误需配合文案或图标。
- 动画尊重 `prefers-reduced-motion`。

---

## Typography

### Font Families（与线上一致）

| 角色 | 字体 | 说明 |
|------|------|------|
| **Display / 营销标题** | **Instrument Sans**（`--font-instrument-sans`，工具类 `font-instrument`） | 官网主视觉标题 |
| **Body / UI** | **Inter**（`--font-inter`）+ system-ui 回退 | 正文、按钮、导航 |

CSS 片段（概念）：

```text
--font-body: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
  "Helvetica Neue", var(--font-inter, "Inter"), "Arial", sans-serif;
.font-instrument → var(--font-instrument-sans), sans-serif
```

### Type Scale（来自站点 CSS 变量）

| Token | 大致尺寸 | 用途 |
|-------|----------|------|
| `--text-display-xl` | `calc(3.75rem)` 量级 + 负字距 | 超大展示标题 |
| `--text-display-lg` | `3rem` 量级 | Hero 副层 |
| `--text-display-md` | `2.25rem` 量级 | 区块主标题 |
| `--text-display-sm` | `1.875rem` 量级 | 小标题 |
| `--text-display-xs` | `1.5rem` 量级 | 卡片标题 |
| `--text-md` | `1rem` 行高约 1.5rem | 正文加强 |
| `--text-base` | `1rem` | 默认正文 |

**规则**：同一屏 **Display（Instrument）** 与 **Body（Inter）** 分工明确；避免第三种展示字体。

---

## Spacing & Layout

| 项 | 规范 |
|----|------|
| **基准网格** | `0.25rem`（4px，Tailwind 默认 `--spacing`） |
| **容器最大宽** | `--max-width-container: 1280px` |
| **圆角** | `--radius-full: 9999px`（药丸按钮）；`--radius-2xl: 1rem`（卡片常见） |
| **区块留白** | 垂直 `py-20`～`py-24` 量级（以现有页为参考） |
| **阴影** | `--shadow-skeumorphic`：内凹轻拟物（按钮/控件） |

---

## UI Components

### Buttons

- **主 CTA**：暖色填充（品牌橙系）+ **白字** 或 **深灰字**（以线上对比度为准）；圆角多用 **全圆角（pill）**。
- **次按钮**：描边或浅底 + `--text-1` / `--text-2`。
- **Hover**：透明度或略深一阶色（官网社交图标用 `hover:opacity-60` 类模式）。

### Cards / 设备画框

- 首页大量使用 **手机/平板外框 + 功能截图**（资源域名 `public.heynori.com/home/*`）。
- 保持 **圆角屏幕 + 浅色亚麻背景** 一致，避免混用未品牌化的设备 Mockup。

### Navigation

- 顶栏：浅色底 + 深色字；CTA **Download App** / **Try Nori Online** 与主色一致。

---

## Iconography

- **站内**：社交与渠道图标为 **SVG**（如 `social-instagram.*.svg`）。
- **新建 UI**：优先 **Lucide / Heroicons** 等 SVG，**不用 emoji 充当图标**（与 brand-visual skill 一致）。

---

## Imagery

- **风格**：明亮、家庭场景、产品界面截图为主；色块与 **secondary-1～5** 装饰色可与插画搭配。
- **画幅**：Hero 多竖屏设备图 + 横屏桌面帧；保持与亚麻背景统一。
- **资源**：`https://public.heynori.com/...`（以实际 URL 为准）。

---

## Content Voice & Tone

摘自 [nori.md](./nori.md) §8：

- **Voice**：友好、温暖、实用、不啰嗦。
- **Tone**：像家人助手，自信但不傲慢；强调「减轻负担」「更轻松」。
- **Avoid**：过度技术化、冷冰冰的 AI 术语。
- **Preferred terms**：`family`、`organize`、`easier`、`Nori`；用 `families` / `parents` 而非生硬 `user`。
- **CTA**：Download App、Try Nori Online、Get Started；突出 **Free Forever** 与 **按需升级高级 AI**。

---

## SEO & Meta

| 项 | 规范 |
|----|------|
| **Title 模式** | `Nori \| [Page Topic]` 或 `[Topic] \| Nori`（与现网一致） |
| **Description** | 含 AI family organizer、calendar、tasks、meal planning 等核心词 |
| **Canonical** | `https://heynori.com/` + 各功能页路径 |
| **OG 图** | 使用品牌色与产品截图；避免与主站视觉冲突 |

---

## Tech Notes（供前端）

- **框架**：Next.js；**样式**：Tailwind CSS **v4.1.x**（以构建为准）。
- **设计令牌**：颜色同时存在 **营销自定义属性**（linen / warm brand）与 **语义 design tokens**（`--color-brand-*` 等），新页面需与现有页对齐层级，避免混用未定义灰阶。

---

## Product Marketing Context（Section 12）

可复制到 `.cursor/product-marketing-context.md`：

```markdown
## 12. Visual Identity (Nori)

**Mood**: Light, warm linen backgrounds; family-friendly; warm orange/gold CTAs; deep gray text (#151515 family).
**Typography**: Instrument Sans (display/hero); Inter + system-ui (body/UI).
**Colors**: Linen scale (#e0dacc–#fcfbf7); warm brand accent ~#d68125; semantic purple UI ~#9e77ed where components use design tokens.
**Layout**: Max width 1280px; 4px base spacing; pill buttons; skeumorphic subtle shadows optional.
**Icons**: SVG only (no emoji as UI icons).
**Voice**: Warm, practical; families/parents; see nori.md §8.
**Ref**: 本专案 `./nori-brand-visual.md`（相对路径以当前仓库中的 Nori 目录为准）
```

---

## Quick Reference

| Section | Used by |
|---------|---------|
| Logo, Colors, Typography | 官网、落地页、功能页、广告素材 |
| Spacing, Components | 前端、设计稿、A/B 测试变体 |
| Imagery | 博客、社媒、应用商店截图 |
| Voice & SEO | 文案、博客、元数据 |

---

## 验证要点（对照 brand-visual skill）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Logo 规则 | ⚠ | 待补充官方矢量与最小尺寸截图 |
| 色彩体系 | ✓ | 营销色 + 语义色双轨已区分 |
| 字体层级 | ✓ | Instrument Sans + Inter |
| 间距 / 容器 | ✓ | 来自构建 CSS |
| 无障碍 | ⚠ | 新组件需逐块测对比度与 focus |
| 图标 | ✓ | SVG；禁用 emoji 作 UI 图标 |

---

## 文档导航

| 文档 | 用途 |
|------|------|
| [nori.md](./nori.md) | 产品概览、定位、Brand & Voice 摘要 |
| [nori-brand-visual.md](./nori-brand-visual.md) | **本文档**：视觉与格式规范 |
| [nori-features.md](./nori-features.md) | 功能页结构、URL |
| [nori-site-structure.md](./nori-site-structure.md) | 网站层级与落地页关系 |
| [nori-blog.md](./nori-blog.md) | 博客策略与配图需求 |
| [nori-others.md](./nori-others.md) | 杂项与索引 |
