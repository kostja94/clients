# 2mv — Brand Visual Guidelines & Design Tokens

> **数据来源**：www.2mv.ai 线上实测（2026-08-16，桌面视口）
> **方法**：首页 HTML + `/_next/static/chunks/*.css`（537KB）DevTools CSS 抓取，跨页对比
> **技术栈**：Next.js + Tailwind CSS v4（`lightningcss` 编译，CSS 变量即设计 token）
> **关联**：[2mv.md](./2mv.md)（产品上下文）· [OG-COVER-WORKFLOW.md](./blog/images/OG-COVER-WORKFLOW.md)（封面图生成规范）· [2mv-features.md](./2mv-features.md)

---

## 0. 品牌一句话

> **2mv = 从 0 到数百万 organic views 的 agentic growth agency。**
> 视觉语言：**深色科技 editorial + 黄绿（lime）强调 + 大号粗体标题 + 数据优先**。

### 0.1 视觉风格语言（官网实测 2026-08-16）

| 特征 | 官网表现 | 封面应用 |
|------|---------|---------|
| **背景** | 深色 `#131313` 面板 / 米白 `#f5f5f7` 页底双模式 | 深色为主（`#131313`） |
| **标题** | 超大 Plus Jakarta Sans 粗体（如 "From zero to millions of views."） | 大号白字粗体 + 黄绿强调词 |
| **数据优先** | 大量数字卡（806.9K / 24.6M / 49.4M views） | 融入 view-count 数据元素 |
| **强调色** | 黄绿 `#d6fd70`（logo 方块、高亮、下划线） | 标题下划线/关键词/图标 |
| **视频卡片** | TikTok/Reels/Shorts 缩略图网格墙（全屏滚动） | 手机/卡片网格作为视觉主体 |
| **五引擎 loop** | WATCH → DECODE → ARCHITECT → PRODUCE → GROW 编号步骤 | 步骤编号/时间轴元素 |
| **对比叙事** | "Others deliver content. 2mv delivers growth." | 对比式构图 |
| **圆角** | 大圆角卡片 2.15rem、药丸按钮 999px | 卡片式圆角块 |
| **情绪** | 锐利、自信、数据驱动、科技感 | 深色 + 亮绿 + 大标题 |

### 0.2 官网 OG 图参考

官网自己的 `og-image.png`（1200×630）是深色风格基准：深底 `#131313` + 大号粗体标题 + 黄绿强调 + 视频卡片元素。

---

## 1. 色彩体系（Core Color Tokens）

### 1.1 品牌主色（Lime / 黄绿系）— 核心识别

| Token | 值 | 角色 | 使用 |
|-------|-----|------|------|
| `--green` | `#d6fd70` | **品牌主色**（首页 22 次） | 强调色、logo 方块底色、高亮块 |
| `--green-deep` | `#c2ef4e` | 深黄绿 | hover/深色场景的强调 |
| `--get-green` | `#4f6208` | 深橄榄绿 | 黄绿上的文字色（对比度保证） |
| `--get-green-soft` | `#f1f8dc` | 极浅黄绿 | 强调底色/标签背景 |
| `#eaff9e` | — | 亮黄绿 | 浅色高亮块 |
| `#6b8a1e` / `#8bb02c` | — | 中橄榄绿 | 次级强调/图表 |
| `#33420f` / `#35410f` | — | 深橄榄 | 面板文字/深色块上的绿色 |

### 1.2 亮蓝（次强调）

| Token | 值 | 角色 |
|-------|-----|------|
| `--blue` | `#2453ff` | 次强调色（链接/图标/数字） |

### 1.3 中性色（墨色 + 纸色）

| Token | 值 | 角色 |
|-------|-----|------|
| `--ink` | `#0a0a09` | **主文字色**（近黑墨色） |
| `--dark` | `#131313` | **深色面板/背景**（首页 58 次） |
| `--dark-2` | `#191815` | 深色层级 2 |
| `--dark-3` | `#2f2f2f` | 深色层级 3 |
| `--page` | `#f5f5f7` | **页面底色**（浅纸色） |
| `--on-dark` | `#f2f2f2` | 深背景上的文字 |
| `--on-dark-muted` | `#a6a69e` | 深背景上的弱文字 |
| `--panel-bg` | `#131313` | 面板背景 |
| `--get-canvas` | `#f4f4f2` | 内容画布底色 |
| `--get-text` | `#1d1d1f` | 正文深灰 |
| `--get-muted` / `--get-faint` | `#57575b` / `#646469` | 弱化文字 |
| `--white` | `#fff` | 白色卡片/背景 |

### 1.4 语义色（shadcn/ui 体系）

| Token | 值 |
|-------|-----|
| `--primary` | `#171717` |
| `--primary-foreground` | `#fafafa` |
| `--secondary` / `--muted` / `--accent` | `#f5f5f5` |
| `--muted-foreground` | `#737373` |
| `--destructive` | `#e40014` |
| `--border` / `--input` | `#e5e5e5` |
| `--ring` | `#a1a1a1` |

### 1.5 色彩规则

| 规则 | 说明 |
|------|------|
| **主强调** | 一律用 `#d6fd70`（黄绿），禁用电光绿 `#00FF66`（那是误判，非品牌色） |
| **深色优先** | 深色面板 `#131313` + 黄绿强调是最常见组合 |
| **文字对比** | 黄绿上文字用深橄榄 `#4f6208`；深色上文字用 `#f2f2f2` |
| **链接/数字** | 次强调用亮蓝 `#2453ff` |
| **圆角** | 见 §4 |

---

## 2. 字体体系（Typography）

### 2.1 字体栈

| Token | 值 | 用途 |
|-------|-----|------|
| `--home-heading-font` / `--research-heading-font` | **`"Plus Jakarta Sans"`, var(--font-sans)** | **标题**（H1/H2/大字号展示） |
| `--font-sans` | `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", ...` | 正文/UI |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, ...` | 代码/数据 |
| Geist Mono | `Geist Mono, monospace` | 等宽数据展示（research 区） |

### 2.2 字号 Token（Tailwind 语义）

| Token | 值 |
|-------|-----|
| `--text-xs` | 0.75rem |
| `--text-sm` | 0.875rem |
| `--text-base` | 1rem |
| `--text-lg` | 1.125rem |

### 2.3 字重

| Token | 值 |
|-------|-----|
| `--font-weight-medium` | 500 |
| `--font-weight-semibold` | 600 |

### 2.4 字距（tracking）

| Token | 值 |
|-------|-----|
| `--tracking-adjust` | 0.02em（基线） |
| `--tracking-tight` | -0.025em |
| `--tracking-tighter` | -0.05em |
| `--tracking-wide` / wider / widest | +0.025 / 0.05 / 0.1em |

### 2.5 排版规则

| 规则 | 说明 |
|------|------|
| **标题字体** | 统一 `Plus Jakarta Sans`（大标题、hero、research 标题） |
| **正文字体** | 系统 sans 栈 |
| **数据字体** | 等宽（ui-monospace / Geist Mono） |
| **字距** | 标题用 tight/tighter 收紧，正文用 normal（+0.02em） |

---

## 3. 布局与间距（Layout & Spacing）

| Token | 值 | 说明 |
|-------|-----|------|
| `--max` | 1280px | 内容最大宽度 |
| `--engine-shell-max` | 1300px | 引擎区最大宽 |
| `--navbar-height` | 60px | 导航高度 |
| `--navbar-top` | 24px | 导航顶部留白 |
| `--inset` | 0.55rem | 页面内边距（inset） |
| `--spacing` | 0.25rem | Tailwind spacing 基数 |
| `--snap-height` | `calc(100svh - (var(--inset) * 2))` | 全屏区块高度 |

---

## 4. 圆角与形状（Radius & Shape）

| Token | 值 | 用途 |
|-------|-----|------|
| `--radius` | **2.15rem** | 大卡片（`--radius-card-lg`） |
| `--radius-card-md` | 1.5rem | 中卡片 |
| `--radius-sm` | 0.75rem | 小卡片（`--radius-card-sm`） |
| `--radius-lg` | **3rem** | 区块（`--radius-section`） |
| `--radius-control` | **999px** | 药丸按钮/控制 |
| `--radius-ui` | 0.625rem | UI 小控件 |

> ⚠️ **注意**：Tailwind 默认 `--radius-lg` 是 0.5rem，2mv 覆盖为 **3rem**（大圆角区块）。`--radius-section: var(--radius-lg)` 即 3rem。

---

## 5. 动效（Motion）

| Token | 值 |
|-------|-----|
| `--ease` | `cubic-bezier(.19, 1, .22, 1)` |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` |
| `--entrance-delay` | 0.66s |
| `--col-in` | 0.27s |
| `--burst` | 1.05s |

---

## 6. 组件样式速查

### 6.1 按钮 / 控制

| 组件 | 样式 |
|------|------|
| CTA pill | `--radius-control: 999px`（药丸形） |
| 标签 chip | `--act-chip: 2rem` 高，`--act-h: 2.32rem` |
| Panel | `--panel-bg: #131313` 深色 + 黄绿强调 |

### 6.2 卡片

| 组件 | 圆角 | 说明 |
|------|------|------|
| Card L | `--radius-card-lg` = 2.15rem | 主卡片 |
| Card MD | 1.5rem | 中卡片 |
| Card SM | 0.75rem | 小卡片 |

### 6.3 引擎/Research 区

| Token | 值 |
|-------|-----|
| `--research-heading-font` | Plus Jakarta Sans |
| `--rlh-title-size` | `clamp(3rem, 5.1vw, 5rem)` |
| `--engine-top-safe` | `clamp(5.4rem, 9svh, 6.4rem)` |
| `--engine-bottom-safe` | `clamp(3.6rem, 7svh, 5.2rem)` |

---

## 7. Logo

| 项 | 值 |
|----|-----|
| **Logo 形式** | 黄绿圆角方块（`#d6fd70`，rx=80）+ 黑色粗体 **"2mv"** 文字标 |
| **来源** | `https://www.2mv.ai/icons/favicon.svg`（矢量）/ `apple-touch-icon.png`（180×180） |
| **使用规则** | 深色背景上保留黄绿底方块；浅色背景可叠加或加边框 |

---

## 8. 品牌视觉要点（快速记忆）

```
颜色：  黄绿 #d6fd70（主）· 深墨 #131313（背景）· 米白 #f5f5f7（浅底）· 亮蓝 #2453ff（次）
字体：  标题 Plus Jakarta Sans 大号粗体 · 正文 system sans · 数据 ui-monospace/Geist Mono
形状：  大圆角卡片 2.15rem · 区块 3rem · 药丸按钮 999px
布局：  内容宽 1280px · 深色面板 + 黄绿强调 · 数据优先
风格：  Deep-tech editorial · 大标题 · 视频卡片网格 · 数据卡 · 锐利自信
情绪：  "From zero to millions of views." — 增长、数据、系统化
```

---

## 9. 验证命令

在 2mv 官网 Console 运行：

```javascript
// 品牌主色
console.log(getComputedStyle(document.documentElement).getPropertyValue('--green'));
// 期望：#d6fd70

// 标题字体
console.log(getComputedStyle(document.querySelector('h1')).fontFamily);
// 期望：含 "Plus Jakarta Sans"

// 区块圆角
console.log(getComputedStyle(document.documentElement).getPropertyValue('--radius-section'));
// 期望：3rem

// 深色面板
console.log(getComputedStyle(document.documentElement).getPropertyValue('--dark'));
// 期望：#131313
```

---

*Last updated: 2026-08-16 · based exclusively on live www.2mv.ai audit + CSS token extraction*
