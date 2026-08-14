# Tunee — Brand Visual Guidelines

> 遵循 [brand-visual](../../.cursor/skills/components/branding/brand-visual/SKILL.md) | 关联 [tunee.md](./tunee.md)  
> **来源**：[tunee.ai](https://www.tunee.ai/) 构建产物（Tailwind CSS v3.4 + 自定义 CSS 变量，2026-04-29 自 CDN `res-cdn.tunee.ai/.../_next/static/css/` 抓取）。**哈希文件名会随部署变化**，更新视觉时请重新在浏览器 DevTools → Computed / Network 中核对。  
> 用于：官网、落地页、功能页、MV/创作场景配图、社媒、Brief 给设计与前端。

**Last updated**: 2026-04-29

---

## Brand Identity

| 项 | 内容 |
|----|------|
| **Brand Name** | Tunee |
| **One-line** | The smartest AI music agent — chat to create music（见 [tunee.md](./tunee.md) §1） |
| **Hero 文案示例** | "HI! I'M TUNEE" / "Your AI Creative Partner. Create the music. Turn it into visuals." |
| **Website** | https://www.tunee.ai/ |
| **品类气质** | 创意伙伴、对话式创作、音乐 + 视觉一体化；浅色界面为主（`html.light`），强调包容与易用（Music is for everyone） |

---

## Logo

- **主站**：导航与营销区块使用 Tunee 字标 / 图形标识（具体 SVG/PNG 以线上 `_next/static/media` 或 CDN 为准）。
- **Minimum Clear Space**：建议 **≥ 字标高度的 0.5×** 四周留白；勿横向拉伸、勿与嘈杂背景重叠导致辨识度下降。
- **Favicon**：以线上站点 `favicon` / `apple-touch-icon` 为准（随构建更新）。
- **禁止**：任意改色导致对比不足；在复杂 MV 截图或渐变背景上放置无底板浅色标。

*若需印刷或合作方矢量包，建议由产品侧导出官方 Logo Kit 并在此补充路径。*

---

## Color Palette

### A. 语义色板（`:root`，HSL 分量 — Tailwind `hsl(var(--token))`）

站点采用 **浅色全局底**（`--background-global`）+ **近黑主按钮**（`--primary`）+ **中性正文**（`--foreground`），并配有 **chart / brand-* 彩色**用于插画与数据点缀。

| Token | HSL（浅色主题） | 约 Hex | 用途 |
|-------|-----------------|--------|------|
| `--background-global` | `0 0% 96%` | `#f5f5f5` | 页面整体浅灰底 |
| `--background` | `0 0% 100%` | `#ffffff` | 卡片 / 主表面 |
| `--foreground` | `0 0% 14%` | `#242424` | 主标题与正文倾向 |
| `--primary` | `0 0% 10%` | `#1a1a1a` | 主 CTA 填充（深色） |
| `--primary-foreground` | `0 0% 100%` | `#ffffff` | 主按钮上的字 |
| `--muted-foreground` | `0 0% 56%` | `#8f8f8f` | 次要说明文字 |
| `--border` | `0 0% 92%` | `#ebebeb` | 分割线、边框 |
| `--destructive` | `7 100% 60%` | 偏红 | 危险操作、错误提示 |
| `--selection` | `214 100% 90%` | 浅蓝 | 文本选中背景 |

### B. 背景层级（浅蓝紫倾向）

| Token | HSL | 用途 |
|-------|-----|------|
| `--background-light` | `220 20% 97%` | 浅区块 |
| `--background-secondary` | `231 100% 96%` | 次级浅紫氛围 |
| `--background-tertiary` | `240 100% 98%` | 更浅层级 |
| `--cream` | `37 68% 96%` | 奶油色点缀 |

### C. 品牌彩色（装饰 / 插画 / Chart）

| Token | HSL（浅色主题） | 说明 |
|-------|-----------------|------|
| `--brand-indigo` / `--active` | `242 99% 64%` | 蓝紫强调 |
| `--brand-violet` | `251 100% 63%` | 紫 |
| `--brand-magenta` | `316 100% 64%` | 洋红 |
| `--brand-sky` | `204 100% 58%` | 天蓝 |
| `--brand-purple` | `260 80% 42%` | 深紫 |

**Chart（示例）**：`--chart-1` `27 100% 47%`（橙）、`--chart-2` `199 100% 43%`（青）等 — 用于报表式组件或首页数据条，勿与主 CTA 深色冲突。

### D. 正文中的原子色（Tailwind arbitrary）

首页模块可见 **`text-[#555555]`** 作为较轻正文（实例：`font-poppins` + `font-light`），可与 `--muted-foreground` 对照使用。

### 无障碍

- 正文与背景对比建议 **≥ 4.5 : 1**；大标题 **≥ 3 : 1**。
- **勿单独用颜色**表达状态；错误需配合文案或图标。
- 动画尊重 `prefers-reduced-motion`（站内已有多种 `@keyframes`，营销素材避免过度闪烁）。

---

## Typography

### Font Families（与构建 CSS 一致）

| 角色 | 字体 | CSS 变量 |
|------|------|----------|
| **UI / 正文主栈** | **Poppins**（400–700） | `--font-poppins` |
| **展示 / 衬线标题** | **Playfair Display**（600–700） | `--font-playfair-display` |
| **几何无衬线备选** | **Outfit**（400–700） | `--font-outfit` |
| **窄标题 / 统计数字感** | **Barlow Condensed**（400–700） | `--font-barlow-condensed` |

字体文件托管于：`https://res-cdn.tunee.ai/web_static/ai-agent-client-en/_next/static/media/*.woff2`（文件名随构建变）。

### 分工建议

- **营销 Hero**：衬线气质可用 **Playfair Display**；偏现代 UI 段落用 **Poppins**。
- **同一屏**：避免混用超过 **两种** 标题家族（例如 Playfair + Poppins 已足够；Outfit / Barlow 用于局部组件即可）。

### Type Scale（实践向）

站点大量使用 Tailwind 工具类；常见模式包括 **`text-[0.96rem]` + `leading-[1.7]`** 说明段落。具体 Display 字号随 breakpoint 变化，以线上为准。

---

## Spacing & Layout

| 项 | 规范 |
|----|------|
| **基准网格** | Tailwind 默认 `0.25rem`（4px） |
| **导航高度（变量）** | `--nav-top-height: 72px`；移动端 `--nav-top-height-mobile: 56px` |
| **会话区** | `--conversation-nav-bar-height: 48px` 等（应用内创作流） |
| **垂直留白** | 区块多用大块 `py-*` + flex/grid；以现有首页 Section 为参考 |
| **圆角** | 组件跟随 shadcn/Tailwind 默认；按钮可见 **pill / 全宽卡片圆角** 等混排 |

---

## UI Components

### Buttons

- **主 CTA**：`bg-primary`（深近黑）+ `text-primary-foreground`（白）；部分入口使用 **图片按钮**（如 `ApplyButton` 使用整张 PNG/WebP 资源以保持品牌纹理）。
- **Hover**：常见 `md:hover:opacity-90` 等透明度变化。
- **文案**：Start Creating for Free、Make Your MV Now、Make Your Own Character 等（英文主站）。

### Cards / 设备画框

- 首页包含 **Music Agent / MV Studio / AI Character** 等功能模块卡片；保持 **白底或浅紫氛围底** 与边框一致。
- MV、虚拟艺人相关区块可出现 **竖屏预览框 + 渐变**，需保证前景文字对比度。

### Navigation

- 顶栏：**浅色背景** + 深色字；右侧为主要行动入口。
- HTML `class="light"`：营销站以浅色模式为主。

---

## Iconography

- **站内**：优先 **SVG** 图标（含渠道、功能入口）。
- **新建 UI**：与 shadcn/Lucide 类体系对齐；**不用 emoji 充当功能图标**（与 brand-visual skill 一致）。

---

## Imagery

- **风格**：音乐创作场景、创作者故事、MV 视觉抓帧；可搭配 **brand-* / chart-* 渐变**作为装饰。
- **资源**：静态资源域名 **`res-cdn.tunee.ai`**；插图与截图需统一浅色界面气质。
- **版权**：商用授权叙事见首页「Full Commercial License」区块 — 配图勿暗示侵权素材。

---

## Content Voice & Tone

摘自 [tunee.md](./tunee.md) §8：

- **Voice**：友好、创意伙伴感、易用、包容。
- **Tone**：强调 chat、conversation、creative dialogue、no music theory。
- **Avoid**：过度技术化、冷冰冰的 B2B 语气。
- **Preferred terms**：`AI music agent`、`chat`、`create`、`conversation`、`music partner`。
- **CTA**：Create / Start Creating for Free、MV / Character 转化动词清晰。

---

## SEO & Meta

| 项 | 规范 |
|----|------|
| **Title 模式** | 官网示例：`Next-Gen AI Music Agent \| Tunee`（随页面扩展） |
| **Description** | 含 AI music agent、music maker、conversation、MV、royalty-free / commercial 等核心词 |
| **Canonical** | `https://www.tunee.ai/` + 各功能路径 |
| **OG 图** | 建议使用品牌色 + 产品界面或 MV 帧；避免与深色主按钮对比失控 |

---

## Tech Notes（供前端）

- **框架**：Next.js；**样式**：Tailwind **v3.4.x**（以构建为准）。
- **设计令牌**：颜色以 **HSL 分量**存在于 `:root`，通过 `hsl(var(--primary))` 使用；深浅色 `--chart-*`、`--brand-*` 在 `.dark` 下有一组覆盖值（应用内深色模式时需整体复验对比度）。
- **CDN**：`res-cdn.tunee.ai/web_static/ai-agent-client-en/`

---

## Product Marketing Context（Section 12）

可复制到 `.cursor/product-marketing-context.md`：

```markdown
## 12. Visual Identity (Tunee)

**Mood**: Light UI; neutral gray page (#f5f5f5 family); primary CTA dark near-black (#1a1a1a) on white text; creative music + MV imagery; inclusive tone.
**Typography**: Poppins (UI/body); Playfair Display (display serif); Outfit & Barlow Condensed for selective components.
**Colors**: HSL tokens in :root — background-global 96% lightness, foreground ~14%, primary 10% with white foreground; brand-indigo/violet/magenta/sky/purple for accents; chart-* for illustrations.
**Layout**: Nav ~72px desktop / 56px mobile (CSS vars); Tailwind spacing.
**Icons**: SVG-first; no emoji as UI icons.
**Voice**: Friendly creative partner; chat-first; see tunee.md §8.
**Ref**: `./tunee-brand-visual.md`
```

---

## Quick Reference

| Section | Used by |
|---------|---------|
| Logo, Colors, Typography | 官网、落地页、功能页、广告素材 |
| Spacing, Components | 前端、设计稿、A/B 测试变体 |
| Imagery | 博客、社媒、MV 封面 |
| Voice & SEO | 文案、metadata |

---

## 验证要点（对照 brand-visual skill）

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Logo 规则 | ⚠ | 待补充官方矢量与最小尺寸截图 |
| 色彩体系 | ✓ | `:root` HSL + brand-* / chart-* 已摘录 |
| 字体层级 | ✓ | Poppins + Playfair + Outfit + Barlow Condensed |
| 间距 / 导航变量 | ✓ | nav height、dvh 等已列 |
| 无障碍 | ⚠ | 新组件需逐块测对比度与 focus |
| 图标 | ✓ | SVG；禁用 emoji 作 UI 图标 |

---

## 文档导航

| 文档 | 用途 |
|------|------|
| [tunee.md](./tunee.md) | 产品概览、定位、Brand & Voice |
| [tunee-brand-visual.md](./tunee-brand-visual.md) | **本文档**：视觉与格式规范 |
| [tunee-features.md](./tunee-features.md) | 功能页结构、产品线 |
| [tunee-use-cases.md](./tunee-use-cases.md) | Use Cases |
| [tunee-competitors.md](./tunee-competitors.md) | 竞品分析 |
| [tunee-keywords.md](./tunee-keywords.md) | 关键词映射 |
| [tunee-music-generator.md](./tunee-music-generator.md) | Music Generator 程序化 SEO |
