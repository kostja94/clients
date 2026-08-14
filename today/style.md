# Today AI — Style Tokens

> 类型：视觉参数定义 | 版本：0.2 | 更新：2026-08-06
>
> 本文档是 **Today AI 项目的视觉参数事实来源（SSoT）**。所有颜色、字体、间距、圆角、阴影、动效参数在此定义。本文件基于 [today.ai/landing](https://today.ai/landing) 线上实际渲染的 CSS 提取整理，任何实现以本文件为准。
>
> **产生方式**：`reference_extracted` — 从线上页面实际加载的样式类、CSS 变量、Tailwind 类名直接提取。
>
> **核心原则**：本文件是项目的最终决策记录。所有组件直接消费本文件的 token 与类名模式。

---

```yaml
version: alpha
name: Today AI
description: "个人 AI 助手——living memory（活的记忆）+ proactive（主动帮助）+ 跨设备，温暖、柔和、日常感的个人生活管理"
derived_from:
  method: "reference_extracted"
  theme: null
  reference_urls: ["https://today.ai/landing"]
  note: "从 landing 页面实际渲染提取：Hero 渐变与基底色、前景色 text-black/85 + #21201c、粉彩区块背景、bg-white/60 毛玻璃卡、bg-black/85 CTA、绿色发光圆 #e1f7bc"
colors:
  # 页面基底（Hero）
  background: "#F4F1EB"
  # 主前景色（正文 / 标题，接近纯黑）
  foreground: "#21201C"
  # 半透明毛玻璃卡
  card: "rgba(255,255,255,0.60)"
  card-foreground: "#21201C"
  # 次级底色 / 图标底
  muted: "#EBF5EF"
  muted-foreground: "rgba(33,32,28,0.65)"
  # 卡片边框（白色半透明）
  border: "rgba(255,255,255,0.40)"
  border-strong: "rgba(33,32,28,0.10)"
  # 主 CTA（黑色填充）
  primary: "rgba(0,0,0,0.85)"
  primary-foreground: "#FFFFFF"
  # 链接 / 交互
  accent: "#03A9F4"
  ring: "rgba(33,32,28,0.50)"
  destructive: "#E5484D"
  # Hero 渐变三个关键色（52% 透明度使用）
  hero-sky: "#ACCDEC"
  hero-lavender: "#E7EBF4"
  hero-peach: "#FFDDB9"
  # 绿色发光圆（Hero 装饰）
  glow-green: "#E1F7BC"
  # 粉彩区块背景色板
  pastel-cream: "#F4F1EB"
  pastel-mint: "#EBF5EF"
  pastel-sky: "#EBF1F5"
  pastel-lemon: "#F3F5EB"
  pastel-rose: "#F5EBEB"
  # 图标底 / 点缀色
  icon-blue: "#03A9F4"
  icon-sky: "#C9F1FF"
  icon-ink: "#303136"
  # 深色模式
  dark-background: "#1A1A2E"
  dark-surface: "#1C1C20"
typography:
  h1:
    fontFamily: "Figtree"
    fontSize: 62px
    fontWeight: 400
    lineHeight: 74px
    letterSpacing: 0
  h2:
    fontFamily: "Figtree"
    fontSize: 44px
    fontWeight: 300
    lineHeight: 52px
    letterSpacing: 0
  h3:
    fontFamily: "Figtree"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: "Figtree"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  lead:
    fontFamily: "Figtree"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 28px
  small:
    fontFamily: "Figtree"
    fontSize: 14px
    fontWeight: 400
  caption:
    fontFamily: "Figtree"
    fontSize: 12px
    fontWeight: 400
  serif:
    fontFamily: "Sentient"
    fontSize: 16px
    fontWeight: 400
  handwriting:
    fontFamily: "Courgette"
    fontSize: 16px
    fontWeight: 400
  code:
    fontFamily: "Geist Mono"
    fontSize: 14px
    fontWeight: 400
rounded:
  cta: 49px
  pill: 9999px
  card-lg: 24px
  card: 16px
  card-sm: 20px
  ui: 12px
  control: 8px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section-py: 60px
# === 结构维度 ===
border-width:
  default: 1px
grid:
  type: clean
density:
  level: comfortable
  line-height-multiplier: 1.0
```

---

## Overview

Today AI 的视觉系统——**温暖、柔和、有陪伴感的生活化界面**。

线上实际页面建立在**暖米色 `#F4F1EB` 基底**之上：Hero 区叠加一层 **52% 透明度的浅蓝→淡紫→暖桃渐变**（`mix-blend-color`）与白色图层，四周有 4 个 **`#E1F7BC` 绿色发光圆环**做 3D 视差装饰。页面主体文字使用**接近纯黑的深褐 `#21201C` / `text-black/85`**，各 Section 用**柔和的粉彩底色**（薄荷、浅蓝、柠檬、粉）交替区分。卡片是**半透明白 + 白色描边**的毛玻璃质感，CTA 是**黑色圆角胶囊**。

与"暗色+霓虹+紫色渐变"的常见 AI 产品不同，Today 的核心是**浅色、柔和、日常感**——大量留白、细字重（`font-light`）标题、暖色氛围。

---

## Colors

所有颜色通过语义 token 消费。**禁止在组件中硬编码裸 hex/rgb/oklch。**

### 核心调色板

| Token | 值 | 用途 |
|-------|-----|------|
| `--background` | `#F4F1EB` | 页面基底色（Hero / 通用背景） |
| `--foreground` | `#21201C` | 正文、标题（深黑褐） |
| `--card` | `rgba(255,255,255,0.60)` | 毛玻璃卡（`bg-white/60`） |
| `--card-foreground` | `#21201C` | 卡片内文字 |
| `--muted` | `#EBF5EF` | 次级底色、图标底 |
| `--muted-foreground` | `rgba(33,32,28,0.65)` | 次级文字（`text-black/65`） |
| `--border` | `rgba(255,255,255,0.40)` | 卡片描边（`border-white/40`） |
| `--border-strong` | `rgba(33,32,28,0.10)` | 组件边框（`border-black/5`、`border-[rgba(60,59,65,0.1)]`） |
| `--primary` | `rgba(0,0,0,0.85)` | 主 CTA 填充（`bg-black/85`） |
| `--primary-foreground` | `#FFFFFF` | primary 上的文字 |
| `--ring` | `rgba(33,32,28,0.50)` | Focus ring |
| `--destructive` | `#E5484D` | 错误、删除操作 |

### 前景色使用惯例（线上实际）

线上页面**不统一使用单一前景 token**，而是按层级使用：

| 层级 | 实际类名 | 说明 |
|------|---------|------|
| 主标题 / 正文 | `text-black/85` | Hero H1、Section H2、卡片标题 |
| 次级文字 | `text-black/65` | Section 副标题、卡片描述 |
| 页脚 / 局部深色区 | `text-[#21201c]/65` → hover `/85` | Footer 链接与标题 |
| 卡片前景 | `text-[#303136]` | 部分卡片内文字 |

### 粉彩区块背景色板（Section 交替）

| Token | Hex | 使用场景 |
|-------|-----|---------|
| `pastel-cream` | `#F4F1EB` | Hero 基底、默认底色 |
| `pastel-mint` | `#EBF5EF` | 薄荷色 Section / 图标圆底 |
| `pastel-sky` | `#EBF1F5` | 浅蓝色 Section / 图标圆底 |
| `pastel-lemon` | `#F3F5EB` | 柠檬色 Section |
| `pastel-rose` | `#F5EBEB` | 粉色 Section |

### 图标底 / 点缀色

| Token | Hex | 用途 |
|-------|-----|------|
| `icon-blue` | `#03A9F4` | 亮蓝点缀（进度条、激活指示） |
| `icon-sky` | `#C9F1FF` | 浅蓝图标底 |
| `icon-ink` | `#303136` | 深灰图标底 / 深色卡 |

### Hero 渐变（品牌签名）

```css
/* 线上实际：52% 透明度 + mix-blend-color 叠加在 #F4F1EB 之上 */
--gradient-hero: linear-gradient(
  180deg,
  rgba(172, 205, 236, 0.52) 0%,    /* #ACCDEC @ 52% */
  rgba(231, 235, 244, 0.52) 61.54%, /* #E7EBF4 @ 52% */
  rgba(255, 221, 185, 0.52) 100%    /* #FFDDB9 @ 52% */
);
```

Hero 背景实际为**三层叠加**：
1. 基底 `bg-[#f4f1eb]/60`（暖米，底部渐隐）
2. 渐变层 `bg-[linear-gradient(...)] mix-blend-color`
3. 白色层 `bg-white/28`（28% 白压淡）

### 绿色发光圆（Hero 签名装饰）

Hero 区有 4 个 **`#E1F7BC`（荧光绿）发光圆环**，3D 视差分层：

```css
/* 实际类名模式 */
--glow-green: #e1f7bc;
/* rounded-full border-2 border-[#e1f7bc] shadow-[0_-15px_40px_#e1f7bc]
   bg-[linear-gradient(...)] size-80/64/48/32  由外到内递减 */
```

4 个圆尺寸递减：`size-80` → `size-64` → `size-48` → `size-32`，随滚动 `translateZ()` 视差移动。

### 禁止使用的颜色

以下 Tailwind 调色板**全站禁止出现在 JSX className 中**：

`gray-*` `slate-*` `zinc-*` `neutral-*` `stone-*`

禁止直写 `text-white` `bg-white` 覆盖全部背景——白色仅允许以半透明叠加（`bg-white/28`~`/70`）形式存在，`bg-white` 不透明度 100% 仅用于极小面积元素（如输入框）。

---

## Typography

### 字体族

| 名称 | Tailwind class | 来源 | 用途 | 字重 |
|------|----------------|------|------|------|
| **Figtree** | `font-sans` | Google Fonts / 自托管 | 全站主字体（正文、UI、按钮、标题） | 300 / 400 / 500 / 600 |
| **Sentient** | `font-serif` | 自托管 | 情感化强调、引语、品牌标语强调短语 | 400 / 600 |
| **Courgette** | `font-handwriting` | 自托管 | 亲笔感问候语、手写批注（如 "Hoy [OY]"） | 400 |
| **Geist Mono** | `font-mono` | 自托管 | 时间、数据、代码、状态 | 400 / 500 |

> 字体栈提取自线上实际加载：`--font-sans-stack: "Figtree", ui-sans-serif, system-ui, sans-serif`；`--font-sentient-stack: "Sentient", Georgia, serif`；`--font-courgette-stack: "Courgette", cursive`；`--font-mono-stack: "Geist Mono", ui-monospace, monospace`。

### 字号体系（线上实际）

| 角色 | Class | 字号 | 行高 | 字重 |
|------|-------|------|------|------|
| Hero H1 | `text-[62px]/[74px] font-normal` | 62px | 74px | 400 |
| Section H2 | `text-[44px]/[52px] font-light` | 44px | 52px | **300（细）** |
| H2 响应式 | `max-2xl:text-[32px]/[40px] max-sm:text-[26px]/[36px]` | 32 / 26px | — | 300 |
| Section 副标题 | `text-2xl/[28px] font-normal` | 24px | 28px | 400 |
| Body | `text-base` / `text-[15px]` / `text-[16px]` | 16px | — | 400 |
| 小字 | `text-sm` / `text-[14px]` | 14px | — | 400 |
| 微小字 | `text-xs` / `text-[12px]` / `text-[10px]` | 12 / 10px | — | 400 |

**关键特征**：标题**不用粗体**——H1 用 `font-normal`(400)，H2 用 `font-light`(300)，靠字号与留白建立层级。这与品牌"温和、不压迫"的气质一致。

### 字体使用规则

- **Figtree 是全站默认**：标题与正文同族，靠字号差异（62/44/24/16）+ 细字重建立层级
- **Sentient 只用于情感强调**：品牌标语中的关键短语、引语——每屏 ≤ 1 处
- **Courgette 只用于拟人手写感**：问候语、手写批注、极少数装饰性文字——**禁止**用作 UI 标签或标题
- **Geist Mono 只用于数据/时间**：状态值、睡眠时长、统计数字

### 禁止使用的字体

- ❌ 任何 Comic Sans / Papyrus 类系统手写体
- ❌ 在正文中使用 Sentient / Courgette
- ❌ 即兴使用 `text-6xl` / `text-7xl` 等绕过字号体系

---

## Layout & Spacing

| 规则 | 值 |
|------|-----|
| 容器水平内边距 | `px-8`（`px-6 md:px-8` 窄屏） |
| Section 上下间距 | `pt-30 pb-15` / `py-15` / `pt-26 pb-16`（约 60px 级） |
| 卡片内边距 | `p-4` ~ `p-8`（按卡片密度） |
| 网格间距 | `gap-3` ~ `gap-6` |
| 圆角 | `rounded-[49px]`（CTA）、`rounded-3xl`（大卡）、`rounded-2xl`（卡）、`rounded-xl`（控件）、`rounded-full`（pill/图标圆） |

---

## Elevation & Depth

线上实际的深度表达**以毛玻璃为主、阴影为辅**：

- 卡片：`bg-white/60 backdrop-blur-[20px]` + `border border-white/40`（毛玻璃，白描边）
- 大卡 / 预览卡：`bg-white/30 backdrop-blur-sm` + `shadow-[0_2px_20px_0_rgba(0,0,0,0.08)]`
- 顶部导航 / pill：`bg-white/60 backdrop-blur` + `border border-white/40`
- 输入框：`bg-white/70 backdrop-blur-sm` + `border border-white/40` + `shadow-[inset_0_1px_1px_rgba(255,255,255,0.25)]`

**禁止**：堆叠多重阴影、霓虹/发光卡片（绿色发光圆是 Hero 专属装饰，不用于卡片）。

---

## Shapes

| 层级 | 圆角值 | 使用场景 |
|------|--------|---------|
| CTA 胶囊 | `rounded-[49px]` | 主按钮（"Organize changes"） |
| 胶囊按钮 | `rounded-[47px]` / `rounded-[34px]` | 导航 pill、快捷操作 |
| 大卡 | `rounded-3xl`（24px） | 浮层、大型预览卡 |
| 中卡 | `rounded-2xl`（16px） | 记忆卡、任务卡 |
| 小卡 | `rounded-[20px]` | 紧凑内容卡 |
| 控件 | `rounded-xl`（12px） | 输入框、小按钮 |
| 图标圆 | `rounded-full` | 图标容器、头像、发光圆 |

---

## Components

组件结构、变体、交互状态以线上实际为准。本文档仅定义组件所消费的视觉 token。

| 组件 | 实际类名模式 |
|------|-----------|
| CTA 按钮（primary） | `rounded-[49px] bg-black/85 text-white` |
| 胶囊按钮（ghost） | `rounded-full !bg-white/60 border border-white/40 backdrop-blur` |
| 毛玻璃卡 | `bg-white/60 backdrop-blur-[20px] border border-white/40 rounded-2xl` |
| 大预览卡 | `bg-white/30 backdrop-blur-sm rounded-3xl border-2 border-white/40 shadow-[0_2px_20px_0_rgba(0,0,0,0.08)]` |
| 图标容器 | `flex size-10 items-center justify-center rounded-full bg-[#ebf5ef]` |
| 输入框 | `bg-white/70 border border-white/40 rounded-xl backdrop-blur-sm shadow-[inset_0_1px_1px_rgba(255,255,255,0.25)]` |
| 进度条 | `h-1.5 rounded-[3px] bg-[#03a9f4]`（轨道 `bg-[rgba(0,0,0,0.06)]`） |

---

## Motion

### 动效参数（线上实际）

| 元素 | 动效 |
|------|------|
| 头像指示器光环 | `avatar-beam-spin 2.8s linear infinite` + drop-shadow 蓝色发光 |
| 发光圆视差 | 随滚动 `translateZ()` 分层移动（`data-connector-parallax`） |
| 悬浮记忆卡 | `translate3d(0,-9px,0)` 循环，`4.6s ease-in-out` |
| 徽章 shimmer | `4.86s linear` 循环（仅 Premium 会员卡） |
| Spotlight 卡 | 鼠标跟随 radial-gradient，`opacity .5s ease`（hover/focus-within） |
| Tilted 卡 | 3D 倾斜跟随鼠标，`perspective 900px`，`will-change: transform` |
| 按钮过渡 | `transition-colors duration-150` |
| prefers-reduced-motion | 所有无限循环动画必须停止 |

### 动画约束

- 动画库：CSS only（Tailwind + 自定义 keyframes），不引入 JS 动画库
- 禁止弹跳式缓动（bounce）
- 无限循环动画只允许出现在**装饰性/背景**元素上，禁止在内容元素上循环

---

## 附录：CJK 字号调整

- 字号上调 1 级（`text-sm` → `text-base`，`text-base` → `text-lg`）
- 行高统一 `1.8`
- 标题 CJK 时字重调整为 `font-normal`（线上使用 `lang-cjk:font-normal`）
- Courgette 手写体不覆盖 CJK（使用系统中文手写替代或直接禁用）

---

*本文件为 Today AI 项目的视觉参数实例，基于线上页面实际渲染提取。*
*最后更新：2026-08-06*
