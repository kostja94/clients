# Vofy Filter 类 Apps — 缺口分析与页面模板

> **适用品类**：Filter（滤镜）——一键预设的整体调色或叠加，基于 LUT 或 AI 后处理，改变全局外观。覆盖 80s Grain、VHS Retro、Pastel、Golden Hour、Bold Glamour、Duotone、PS2 Retro 等。
>
> 关联：[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [Effect 类指南](./vofy-effect-apps-guide-zh.md) · [Edit 类指南](./vofy-edit-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md)

**创建日期**：2026-05-11 · **更新**：2026-05-12（合并缺口分析与页面模板）

---

# 第一部分：缺口分析

## 一、Filter 品类定义

Filter 类 App 的核心动作是「套一个整体色调」——一键预设的调色或叠加，通常基于颜色查找表（LUT）或 AI 后处理。用户心智为一键快餐型搜索，关注便捷性和即时效果。

| 维度 | Filter | Style | Effect | Edit |
|------|--------|-------|--------|------|
| **核心动作** | 「套一个整体色调」 | 「变成某种风格」 | 「加一个视觉效果」 | 「改这张图的某个部分」 |
| **用户心智** | 一键快餐 | 审美方向 | 单次操作 | 实用修改 |
| **典型搜索** | `vintage filter online`, `film grain preset` | `Ghibli style AI` | `add bokeh to photo` | `remove background` |

## 二、Vofy 现有 Filter Apps

Vofy 85 个 Apps 中，Filter 类约 38 个（44.7%），是最大的品类：

**发色**（13）：hair-color, grey-hair, pixie-cut, blonde-hair, pink-hair, silver-hair, black-hair, bangs, wolf-cut, curly-hair, long-hair, short-hair, buzzcut

**面部**（10）：beard, no-beard, black-eye, blue-eye, eye-color-change, braces, bald, piercing, jawline-enhancement, face-slimmer

**身体**（3）：waist-slimmer, fat-to-fit, skin-color-changer

**风格化滤镜**（12）：bold-glamour, barbie, kawaii, ghost, emoji, rainbow-air, pop-art, golden-hour, 80s-grain, old-camera, mugshot, baby, negative-image, teeth-whitening

## 三、竞品对标

### 3.1 Picsart Magic Effects（25+ 个）

Pastel Magic, White Ice Magic, Nightcore Magic, Midnight Magic, Moonlight Magic, Badlands Magic, Rainbow Magic, Rose Quartz, Shades of Gray, Haze, Crushed Marble, Galaxy, Wonderland, Soul, Flora, Let It Snow, Holiday Party, Stay Gold, Feast, Undead, Neopop, Colorbright, Highlight, Pretty in Pink, Rose Gold, Winter Blues, Shamrock, Flare, Wispy, Geode, Dystopia, Pow, Hint of Yellow

### 3.2 2026 社交媒体趋势（Filter 相关）

| 趋势 | 热度 | 描述 |
|------|------|------|
| **PS2 / Retro Gaming Filter** | 🔥🔥 | 怀旧 PlayStation 2 低多边形美学，约 42.6K 用户 |
| **VHS Retro** | 🔥🔥 | 复古录像带/低保真美学 |
| **Pastel / 粉彩** | 🔥 | 柔光粉彩色调，Instagram 常青 |
| **Duotone / 双色调** | 🔥 | 品牌设计场景，Canva 有覆盖 |
| **Vintage Retro（1970s/80s/90s）** | 🔥 | 分年代复古色调 |

## 四、Filter 缺口矩阵

### 4.1 完全缺失的 Filter

| 序号 | 缺口功能 | 竞品对标 | 搜索量估算 | 社交热度 |
|------|---------|---------|-----------|---------|
| 1 | **VHS Retro Effect** | Picsart cyber/VHS | 10K–30K/月 | 🔥 |
| 2 | **Pastel / 粉彩** | Picsart Pastel Magic 热门 | 8K–18K/月 | 🔥 |
| 3 | **Duotone / 双色调** | Canva duotone | 8K–18K/月 | 🔥 |
| 4 | **PS2 Retro Gaming** | 独立工具 ~42K 用户 | 5K–12K/月 | 🔥🔥 |

### 4.2 已有但可强化的 Filter

Vofy 已有 38 个 Filter 类 App，当前策略应为**优化现有页面的 H1/SEO 关键词覆盖**（见第二部分模板），而非大规模新增。新增重点放在竞品已验证但 Vofy 缺失的差异化滤镜。

## 五、优先级与路线图

### 🔴 P0 — 竞品已验证 × 社交热度高

| 新增 App（建议 slug） | 搜索量估算 | 竞品信号 | 实施方式 |
|----------------------|-----------|---------|---------|
| `vhs-retro-effect` | 10K–30K/月 | Picsart VHS/cyber | Filter preset + grain overlay |

### 🟡 P1 — 差异化空间

| 新增 App | 搜索量估算 | 竞品信号 | 实施方式 |
|---------|-----------|---------|---------|
| `pastel-effect` | 8K–18K/月 | Picsart Pastel Magic | Filter preset（粉彩/糖果色系） |
| `duotone-effect` | 8K–18K/月 | Canva duotone | 双色调预设（品牌设计场景） |
| `ps2-retro-filter` | 5K–12K/月 | 社交怀旧趋势 | 低多边形 + 色块滤镜 |

### 推荐实施路线

| Phase | 时间 | App 数量 | 内容 |
|-------|------|---------|------|
| **Phase 1** | 本月 | 1 个 P0 | VHS Retro |
| **Phase 2** | 下月 | 3 个 P1 | Pastel、Duotone、PS2 Retro |

> **注**：Filter 类缺口相对较少（Vofy 已有 38 个 Filter App），策略重心在优化现有页面 SEO 而非大量新增。重点新增仅限竞品已验证且有明确社交热度的差异化滤镜。

## 六、Blog 内容联动

- `vhs-retro-filter-guide` → VHS 复古教程
- `how-to-get-pastel-photo-filter` → 粉彩滤镜教程
- `duotone-photo-effect-guide` → 双色调教程
- `ps2-retro-gaming-filter-tutorial` → PS2 滤镜教程

---

# 第二部分：页面模板

## 一、页面线框图（Filter 类专用）

```
┌─────────────────────────────────────────────────────────────┐
│  BREADCRUMB                                                  │
│  Apps > Filter > [Filter Name] Filter                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  HERO                                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Filter]  badge                                       │   │
│  │                                                       │   │
│  │  H1: AI [Filter Name] Filter —                        │   │
│  │      Apply [Adjective] [Element] in One Tap            │   │
│  │                                                       │   │
│  │  Subtitle: 1-2 句，第一句描述色调/氛围感受，           │   │
│  │           第二句强调一键套用 + 含 1-2 个变体关键词      │   │
│  │                                                       │   │
│  │  [Upload an image]  CTA                                │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  TOOL WIDGET                                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Upload an image  [JPG, PNG, WebP, GIF]               │   │
│  │                                                       │   │
│  │  Filter preset  [dropdown: Select a filter preset]    │   │
│  │  ┌──────────────┬──────────────┬──────────────┬─────┐│   │
│  │  │ Preset 1     │ Preset 2     │ Preset 3     │Prst4││   │
│  │  │ (参数化名称  │ (参数化名称  │ (参数化名称  │ ... ││   │
│  │  │ + 缩略图)    │ + 缩略图)    │ + 缩略图)    │     ││   │
│  │  └──────────────┴──────────────┴──────────────┴─────┘│   │
│  │                                                       │   │
│  │  Settings: [Model ▼] · [Aspect ▼] · [Resolution ▼]   │   │
│  │                                                       │   │
│  │  [Apply [Filter Name] Filter]  CTA                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  EXAMPLE GALLERY                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Example]  [Latest]  [History]   tabs                │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │ Before  │ │ Before  │ │ Before  │ │ Before  │   │   │
│  │  │  After  │ │  After  │ │  After  │ │  After  │   │   │
│  │  │(original│ │         │ │         │ │         │   │   │
│  │  │→filtered│ │         │ │         │ │         │   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 01 — 教育模块                                       │
│  H2: What is the [Filter Name] Filter, Exactly?              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  2-3 段正文：                                          │   │
│  │  段 1 — 滤镜定义 + 它给你的照片带来什么效果（1-2 句）    │   │
│  │  段 2 — 滤镜的色调/氛围特征概述（2-3 句）               │   │
│  │  段 3 — Vofy AI 如何实现（与传统 LUT 滤镜的区别, 1-2句）│   │
│  │  [Available on all Vofy plans]  badge                  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 02 — 色调参数拆解（4 张参数卡片）                    │
│  H2: The [Filter Name] Look.                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│   │
│  │  │ 🌡️       │ │ ◐        │ │ 📺       │ │ 🔲       ││   │
│  │  │ Temp     │ │ Contrast │ │ Grain    │ │ Vignette ││   │
│  │  │ 色温     │ │ 对比度   │ │ 颗粒感   │ │ 暗角     ││   │
│  │  │          │ │          │ │          │ │          ││   │
│  │  │ [该滤镜  │ │ [该滤镜  │ │ [该滤镜  │ │ [该滤镜  ││   │
│  │  │ 的色温   │ │ 的对比度 │ │ 的颗粒   │ │ 的暗角   ││   │
│  │  │ 倾向 +   │ │ 风格 +   │ │ 风格 +   │ │ 风格 +   ││   │
│  │  │ 可调范围]│ │ 可调范围]│ │ 可调范围]│ │ 可调范围]││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 03 — 使用场景                                       │
│  H2: When to Use the [Filter Name] Filter.                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│   │
│  │  │ Portraits│ │  Travel  │ │  Social  │ │  Brand   ││   │
│  │  │ 人像     │ │ 旅行/日常 │ │ 社交媒体 │ │ 品牌/风格 ││   │
│  │  │          │ │          │ │          │ │          ││   │
│  │  │ [2-3句   │ │ [2-3句   │ │ [2-3句   │ │ [2-3句   ││   │
│  │  │ 场景说明]│ │ 场景说明]│ │ 场景说明]│ │ 场景说明]││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 04 — HowTo 步骤                                    │
│  H2: How to Apply the [Filter Name] Filter                   │
│      in Three Steps.                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  01 — Upload Your Photo                               │   │
│  │  [描述：支持格式、上传即开始]                           │   │
│  │  Tip: [建议使用何种类型的照片效果最佳]                  │   │
│  │                                                       │   │
│  │  02 — Choose a Filter Preset                          │   │
│  │  [描述：浏览预设、实时预览、一键套用]                    │   │
│  │  Tip: [不同预设适合什么场景——如 Fade 30% vs Grain 50%] │   │
│  │                                                       │   │
│  │  03 — Download or Keep Editing                        │   │
│  │  [描述：下载选项 + Credits 一句说明]                    │   │
│  │  Tip: [可叠加多个滤镜或在 Studio 中继续微调参数]        │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  SOCIAL PROOF                                                │
│  H2: What Creators Say                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────────────────┐ ┌──────────────────────┐    │   │
│  │  │ "[滤镜感受引文]"      │ │ "[滤镜感受引文]"      │    │   │
│  │  │  — Name, Role        │ │  — Name, Role        │    │   │
│  │  └──────────────────────┘ └──────────────────────┘    │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  RELATED APPS                                                │
│  H2: Also in the Studio                                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐             │   │
│  │  │ 同品类   │ │ 相邻品类  │ │ 热门通用  │             │   │
│  │  │ Filter   │ │ Style/   │ │ Popular  │             │   │
│  │  │ App      │ │ Effect   │ │ App      │             │   │
│  │  └──────────┘ └──────────┘ └──────────┘             │   │
│  │  [See all apps →]                                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  FAQ（使用 `<details>/<summary>` HTML，确保 Bing 可抓取）     │
│  H2: Questions, Answered.                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Q1: [滤镜可逆性——如 "Does this change my original?"]│   │
│  │  A1: [说明非破坏性编辑，原始照片始终保留]              │   │
│  │  ─────────────────────────────────────────            │   │
│  │  Q2: 滤镜参数可调范围                                  │   │
│  │  Q3: 能否批量套用同一滤镜                              │   │
│  │  Q4: 输出格式与分辨率                                  │   │
│  │  Q5: AI 滤镜与传统 LUT 滤镜的区别                      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CLOSING CTA                                                 │
│  H2: One Tap. Instant [Filter Name] Vibes.                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Subtitle: [简短行动描述，强调一键即得]                 │   │
│  │  [Apply the [Filter Name] Filter Now]  CTA             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、H1 标题公式

**公式**：`AI [Filter Name] Filter — Apply [Adjective] [Element] in One Tap`

**设计原则**：
- 破折号前 = 搜索引擎主词（匹配 "ai [filter] filter" / "[filter] filter online"）
- 破折号后 = 体验钩子（强调一键、即时）+ 含形容词描述（匹配风格长尾）
- Title Tag 取破折号前 + ` | Vofy`（50-60 字符），H1 取完整双段式（50-70 字符）

**填充示例**：

| App | H1 |
|-----|-----|
| 80s Grain | `AI 80s Grain Filter — Apply Retro Film Texture in One Tap` |
| VHS Retro | `AI VHS Retro Filter — Apply Lo-Fi Video Tape Grain in One Tap` |
| Pastel | `AI Pastel Filter — Apply Soft Candy Tones to Your Photos Instantly` |
| Golden Hour | `AI Golden Hour Filter — Apply Warm Sunset Glow in One Tap` |
| Bold Glamour | `AI Bold Glamour Filter — Apply High-Contrast Portrait Polish Instantly` |
| PS2 Retro | `AI PS2 Retro Filter — Apply Low-Poly Gaming Aesthetics in One Tap` |

---

## 三、各区块内容规范

### 3.1 Breadcrumb

```
Apps > Filter > [Filter Name] Filter
```

### 3.2 Hero

| 元素 | 规范 |
|------|------|
| **Badge** | `Filter` |
| **H1** | 按 §二公式，必须含主关键词 `AI [Filter Name] Filter` |
| **Subtitle** | 段 1：色调/氛围感受（1 句）。段 2：一键套用提示 + 含 1-2 个变体关键词（如 "photo filter"、"retro effect"、"film grain"） |
| **CTA** | `Upload an image` 或 `Apply the [Filter]` |
| **关键词密度** | H1 含 "AI" + "[filter]" + "filter"；subtitle 含 "apply … to photo" / "[era/style] vibes" 等变体 |

### 3.3 Tool Widget

| 元素 | 规范 |
|------|------|
| **上传区域** | JPG, PNG, WebP, GIF |
| **Selector** | `Filter preset` dropdown — 3-5 个参数化预设，每项有滤镜缩略图 |
| **预设命名** | 使用强度/风格变体名（如 "Fade 30%"、"Grain 50%"、"Heavy VHS"、"Light Grain"） |
| **Settings 行** | Model · Aspect Ratio · Resolution（默认推荐模型 + Auto） |
| **Generate CTA** | `Apply [Filter Name] Filter` |

### 3.4 Example Gallery

- 3 个 Tab：Example / Latest / History
- 4 列 Before/After 对比网格
- 前 2 列：精选高质量示例（不同场景类型各 1 组）
- 后 2 列：最近生成 / 历史记录
- 每列 Before 标注 `Original` / After 标注 `[Filter Name]`

### 3.5 Chapter 01 — 教育

| 元素 | 规范 |
|------|------|
| **H2** | `What is the [Filter Name] Filter, Exactly?` |
| **段 1** | 滤镜定义 + 它给你的照片带来什么效果（1-2 句） |
| **段 2** | 滤镜的色调/氛围特征概述——自然融入 Ch.02 四个参数维度的关键词（2-3 句） |
| **段 3** | Vofy AI 如何实现（与传统 LUT 滤镜的区别——AI 可理解画面内容做适应性调色）（1-2 句） |
| **Badge** | `Available on all Vofy plans`（若适用） |
| **关键词** | 主词出现 2-3 次，变体（如 "photo filter" / "film grain overlay"）1-2 次 |

### 3.6 Chapter 02 — 色调参数拆解

**H2**：`The [Filter Name] Look.`

**4 张参数卡片**（固定维度，不可增减）：

| 卡片 | 标题 | 内容要求 |
|------|------|---------|
| **Temperature**（色温） | 色温倾向的名称 | 2-3 句描述暖/冷调倾向，以及色温如何影响照片情绪。可注明 Kelvin 区间（如 "pulls toward 3500K warm amber"） |
| **Contrast**（对比度） | 对比度风格的名称 | 2-3 句描述对比度特征（高对比 punchy / 低对比 faded / 中间调柔和），以及对画面层次的影响 |
| **Grain**（颗粒感） | 颗粒风格的名称 | 2-3 句描述颗粒/噪点的强度与质感（细密胶片感 / 粗犷 VHS 噪点 / 纯净无颗粒），以及可调范围 |
| **Vignette**（暗角/边框） | 暗角风格的名称 | 2-3 句描述画面边缘处理（柔焦暗角 / 硬边裁切 / 漏光边框 / 无边框），以及强度范围 |

### 3.7 Chapter 03 — 使用场景

**H2**：`When to Use the [Filter Name] Filter.`

**4 张场景卡片**（Filter 类侧重）：

| 场景 | 适用条件 | 内容示例 |
|------|---------|---------|
| **Portraits & Selfies** | 单人/双人，面部可见 | "Give your selfies an instant [filter mood] — no editing skills, just one tap." |
| **Travel & Daily Moments** | 日常、街拍、旅行 | "Turn everyday snapshots into [era/style] memories. All your travel photos, one consistent aesthetic." |
| **Social Media Feeds** | Instagram/TikTok/小红书 | "Build a cohesive feed aesthetic. Apply the [filter] to every post for instant brand consistency." |
| **Brand & Content Aesthetic** | 品牌视觉、创作者风格 | "Define your visual identity with one filter. Consistent tone across product shots, flat lays, and behind-the-scenes." |

### 3.8 Chapter 04 — HowTo

**H2**：`How to Apply the [Filter Name] Filter in Three Steps.`

| 步骤 | 标题 | 正文要求 | Tip |
|------|------|---------|-----|
| **01** | `Upload Your Photo` | 支持 JPG/PNG/WebP；拖拽或点击上传 | "For the most dramatic [filter] effect, try photos with good lighting — the filter enhances what's already there." |
| **02** | `Choose a Filter Preset` | 从预设中选择强度变体；实时预览效果；一键套用 | "[Preset A] gives you a subtle [effect], while [Preset B] goes all-in. Tap between them to compare." |
| **03** | `Download or Keep Editing` | 下载 PNG/JPG；Credits 一句说明；可继续叠加其他滤镜 | "Layer multiple filters — start with [Filter Name], then add grain or vignette in the Studio for a custom look." |

> JSON-LD HowTo schema 参考 [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) 范例 B。

### 3.9 Social Proof

- **H2**：`What Creators Say`
- 1-2 条引言，语气轻松、突出 "一键即得" 的便捷感

### 3.10 Related Apps

- **H2**：`Also in the Studio`
- **选择策略**：1 个同品类 Filter App + 1 个相邻品类（Style 或 Effect）+ 1 个热门通用 App
- `See all apps →` 链接指向 `/apps`

### 3.11 FAQ

**H2**：`Questions, Answered.`

**5 个问答**（使用 `<details>/<summary>` HTML）：

| # | 主题 | 问题示例 |
|---|------|---------|
| **Q1** | 滤镜可逆性 | "Does applying the [Filter Name] filter change my original photo?" → 说明非破坏性编辑 |
| **Q2** | 参数可调范围 | "Can I adjust how strong the [Filter Name] effect is?" |
| **Q3** | 批量套用 | "Can I apply the [Filter Name] filter to multiple photos at once?" |
| **Q4** | 输出格式 | "What resolution and format do filtered photos come in?" |
| **Q5** | 与传统滤镜区别 | "How is this AI filter different from Instagram's [similar filter]?" |

### 3.12 Closing CTA

| 元素 | 规范 |
|------|------|
| **H2** | `One Tap. Instant [Filter Name] Vibes.`（呼应 Hero 的 "一键" 体验钩子） |
| **Subtitle** | 简短行动描述（1 句） |
| **CTA 按钮** | `Apply the [Filter Name] Filter Now` |

---

## 四、SEO 检查清单（Filter 类）

### 4.1 关键词矩阵

| 层级 | 关键词类型 | 示例（以 VHS Retro 为例） | 投放位置 |
|------|-----------|---------------------------|---------|
| **主词** | `AI [filter] filter` / `[filter] photo filter` | `AI VHS filter` / `VHS retro photo filter` | H1 破折号前、breadcrumb、meta title |
| **变体 1** | `apply [filter] to photo` | `apply VHS filter to photo` | H1 破折号后、Ch.01 正文、subtitle |
| **变体 2** | `[filter] effect online` | `VHS retro effect online` | Ch.01 正文、Ch.04 H2 |
| **变体 3** | `[era/style] photo filter` | `retro photo filter` / `80s film filter` | Ch.03 场景卡片、FAQ |
| **长尾** | `how to get [filter] look` / `[filter] preset` | `how to get VHS photo look` | FAQ Q5、配套 Blog |

### 4.2 Title Tag vs H1 对照

| 元素 | 内容 | 字符数 |
|------|------|--------|
| **Title Tag** | `AI [Filter Name] Filter — Apply [Style] Vibes to Photos \| Vofy` | 50-60 |
| **H1** | `AI [Filter Name] Filter — Apply [Adjective] [Element] in One Tap` | 50-70 |
| **Meta Description** | `Give your photos instant [filter mood] with Vofy's free AI [Filter Name] Filter. One tap, no editing skills needed. [1 句氛围描述]. Try it now.` | 140-155 |

### 4.3 FAQ 长尾关键词映射

| FAQ | 覆盖长尾 |
|-----|---------|
| Q1 | `[filter] non destructive` / `does [filter] change original photo` |
| Q2 | `[filter] intensity slider` / `adjust [filter] strength` |
| Q3 | `batch apply [filter]` / `apply filter to multiple photos` |
| Q4 | `[filter] output resolution` / `[filter] PNG JPG` |
| Q5 | `[filter] vs Instagram filter` / `AI filter vs LUT` |

---

## 五、极简草稿版（用于快速填充）

```
┌──────────────────────────────────────┐
│  Apps > Filter > [Filter Name] Filter│  BREADCRUMB
├──────────────────────────────────────┤
│  [Filter] badge                      │  HERO
│  H1: AI [Filter] Filter —            │
│      Apply [Adjective] [X] in One Tap│
│  [Subtitle: 色调感受 + 一键套用]      │
│  [Upload an image]                   │
├──────────────────────────────────────┤
│  [Upload] [Filter preset ▼]          │  TOOL WIDGET
│  [4 preset cards with thumbnails]    │  + GALLERY
│  Settings: [Model ▼]·[Aspect ▼]·[Res]│
│  [Examples: Original→Filtered ×4]    │
├──────────────────────────────────────┤
│  What is the [Filter] Filter?        │  CH.01
│  [定义→色调概述→AI 实现, 2-3段]      │
├──────────────────────────────────────┤
│  The [Filter Name] Look.             │  CH.02
│  [4 cards: Temp│Contrast│Grain│Vign] │
├──────────────────────────────────────┤
│  When to Use the [Filter] Filter.    │  CH.03
│  [4 cards: Portraits│Travel│        │
│            Social│Brand]             │
├──────────────────────────────────────┤
│  How to Apply [Filter] in 3 Steps.   │  CH.04
│  01 Upload  02 Choose Preset  03 Gen │
├──────────────────────────────────────┤
│  "What creators say" [2 quotes]      │  SOCIAL
├──────────────────────────────────────┤
│  Also in the Studio [3 app cards]    │  RELATED
├──────────────────────────────────────┤
│  FAQ [5 Q&A: 可逆性→可调→批量→格式→竞品]│ FAQ
├──────────────────────────────────────┤
│  One Tap. Instant [Filter] Vibes.    │  CLOSING
│  [Apply the [Filter] Filter Now]     │
└──────────────────────────────────────┘
```

---

## 六、品类内一致性检查清单

每次新增 Filter 类 App 页面时，逐项核对：

| # | 检查项 | 标准 |
|---|--------|------|
| ① | H1 句式 | 必须匹配 `AI [X] Filter — Apply [Adjective] [Element] in One Tap` |
| ② | Ch.02 卡片数 | 必须恰好 4 张（不可多不可少） |
| ③ | Ch.02 卡片维度 | 必须使用 Temperature / Contrast / Grain / Vignette 四个维度 |
| ④ | HowTo 步骤 2 | 必须以 `Choose a Filter Preset` 为核心动词 |
| ⑤ | FAQ Q1 | 必须覆盖滤镜可逆性/非破坏性问题 |
| ⑥ | slug 后缀 | 必须以 `-filter` 结尾 |
| ⑦ | Breadcrumb 品类 | 必须为 `Apps > Filter > [App Name]` |
| ⑧ | Related Apps #1 | 必须为同品类 Filter App |
| ⑨ | CTA 文案 | 必须强调 "一键/即时" 的便捷感 |
| ⑩ | 情感基调 | 快捷、一键、轻松——全文不可出现复杂操作描述 |

---

## 站内关联

[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [缺口分析](./vofy-filter-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) · [站面结构](../vofy-site-structure.md) · [关键词映射](../vofy-keywords.md)

---

*基于 Vofy 站内已上线 Filter 类页面的结构分析。所有区块和顺序已验证为全站一致模式。*
