# Vofy Effect 类 Apps — 缺口分析与页面模板

> **适用品类**：Effect（特效）——单次可视化处理：叠加元素、光斑、故障、噪点、镜头效果等，侧重「对这一层/这一步做了什么」。覆盖 Glitch、Cinematic Flash、Double Exposure、Light Leaks、Bokeh、Chromatic Aberration、Halftone 等。
>
> 关联：[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [Filter 类指南](./vofy-filter-apps-guide-zh.md) · [Edit 类指南](./vofy-edit-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md)

**创建日期**：2026-05-11 · **更新**：2026-05-12（合并缺口分析与页面模板）

---

# 第一部分：缺口分析

## 一、Effect 品类定义

Effect 类 App 的核心动作是「加一个视觉效果」——单次可视化处理，叠加元素到原图上。用户心智为单次操作型搜索，侧重创意趣味和病毒传播潜力。

| 维度 | Effect | Style | Filter | Edit |
|------|--------|-------|--------|------|
| **核心动作** | 「加一个视觉效果」 | 「变成某种风格」 | 「套一个整体色调」 | 「改这张图的某个部分」 |
| **用户心智** | 单次操作 | 审美方向 | 一键快餐 | 实用修改 |
| **典型搜索** | `add bokeh to photo`, `glitch effect online` | `Ghibli style AI` | `vintage filter online` | `remove background` |

## 二、Vofy 现有 Effect Apps

Vofy 85 个 Apps 中，Effect 类仅 1 个（1.2%）：

- `ai-camera-movement-effect`

**严重不足**。`photo effects` 月搜索量 50K–150K，`AI photo effect` 10K–30K，均高于 `photo style`（10K–40K）。Vofy 在 Effect 品类存在显著的内容空白。

## 三、竞品对标

### 3.1 Picsart API Effects（Effect 相关）

**Blur 类（6 个）**：blur, gblur（高斯模糊）, lensblur（镜头模糊）, motionblur（运动模糊）, smartblur（智能模糊）, pixelize（像素化）

**Light / 漏光（20 个）**：light1–light20，全系列不支持 fade 参数

### 3.2 2026 社交媒体趋势（Effect 相关）

| 趋势 | 热度 | 描述 |
|------|------|------|
| **Cinematic Flash / Paparazzi Flash** | 🔥🔥🔥 | 2026 年 Instagram/TikTok 第一大病毒趋势。高对比度电影级闪光灯效果 |
| **Glitch Art** | 🔥🔥 | 故障艺术持续热门，约 38.8K 用户使用专用在线工具 |
| **Double Exposure** | 🔥🔥 | Instagram Reels 上重新流行，AI 版可自动匹配两层图像 |
| **Bokeh / 散景** | 🔥 | 人像摄影刚需 |

## 四、Effect 缺口矩阵

### 4.1 AI 原生类缺口

| 序号 | 缺口功能 | 竞品对标 | 搜索量估算 | 类型 |
|------|---------|---------|-----------|------|
| 1 | **Cinematic Flash** | Gemini Flash prompt | 20K–50K/月（爆发中） | Effect |
| 2 | **Double Exposure** | Instagram Reels 热门 | 15K–30K/月 | Effect |
| 3 | **Blur 系列** | Picsart 6 种 blur | 50K–100K/月 | Effect |
| 4 | **Light Leaks / 漏光** | Picsart light1–20 | 8K–15K/月 | Effect |
| 5 | **Bokeh / 散景** | Overlay 可做 | 8K–18K/月 | Effect |

### 4.2 算法基础类缺口

| 序号 | 缺口功能 | 竞品对标 | 搜索量估算 | 备注 |
|------|---------|---------|-----------|------|
| 6 | **Vignette / 暗角** | Canva vignette | 10K–20K/月 | 门槛极低 |
| 7 | **Liquify / 液化** | Canva liquify | 5K–12K/月 | 病毒传播潜力 |
| 8 | **Tilt-Shift / 移轴** | lensblur 近似 | 5K–12K/月 | 社交媒体讨喜 |
| 9 | **Chromatic Aberration / 色散** | 第三方有 | 3K–8K/月 | 可并入 Glitch 包 |
| 10 | **Halftone / 网点半色调** | 第三方有 | 3K–8K/月 | 漫画/波普艺术 |

## 五、优先级与路线图

### 🔴 P0 — 大流量 × 病毒传播潜力

| 新增 App（建议 slug） | 搜索量估算 | 竞品信号 | 社交热度 |
|----------------------|-----------|---------|---------|
| `cinematic-flash-effect` | 20K–50K/月 | Gemini Flash prompt | 🔥🔥🔥 #1 病毒趋势 |
| `double-exposure-effect` | 15K–30K/月 | Instagram Reels 热门 | 🔥🔥 |

### 🟡 P1 — 高搜索量基础效果

| 新增 App | 搜索量估算 | 竞品信号 |
|---------|-----------|---------|
| `blur-image` | 50K–100K/月 | Picsart 6 种 blur，基础刚需 |
| `light-leaks` | 8K–15K/月 | Picsart 20 种，微工具矩阵 |
| `add-bokeh` | 8K–18K/月 | 人像摄影热门 |

### 🟢 P2 — 趣味/利基

| 新增 App | 搜索量估算 | 备注 |
|---------|-----------|------|
| `vignette-effect` | 10K–20K/月 | Canva 有，门槛低 |
| `liquify-effect` | 5K–12K/月 | 病毒传播潜力 |
| `tilt-shift-effect` | 5K–12K/月 | 微缩模型效果 |

### 推荐实施路线

| Phase | 时间 | App 数量 | 内容 |
|-------|------|---------|------|
| **Phase 1** | 本月 | 2 个 P0 | Cinematic Flash、Double Exposure |
| **Phase 2** | 下月 | 3 个 P1 | Blur、Light Leaks、Bokeh |
| **Phase 3** | 后续 | 3 个 P2 | Vignette、Liquify、Tilt-Shift |

## 六、现有 Effect 命名优化

Vofy 仅 1 个 Effect 类 App。以下 Filter 类 App 实质属于 Effect，建议在 H1/meta 中强化 "effect" 语义（不改 URL）：

| 当前命名 | 建议 H1 | 理由 |
|---------|---------|------|
| rainbow-air-filter | "Rainbow Air **Effect**" | 光斑叠加属于 effect |
| ghost-filter | "Ghost **Effect**" | 透明叠加属于 effect |
| pop-art-filter | "Pop Art **Effect**" | 风格化属于 style/effect |
| bold-glamour-filter | "Bold Glamour **Effect**" | 多步骤处理 |

## 七、Blog 内容联动

- `cinematic-flash-ai-effect-guide` → 2026 最热趋势教程
- `double-exposure-effect-ai-guide` → 双重曝光教程
- `how-to-add-blur-effect-to-photo` → 模糊效果入门
- `light-leaks-photo-effect-tutorial` → 漏光效果教程
- `add-bokeh-to-photo-guide` → 散景效果教程

---

# 第二部分：页面模板

## 一、页面线框图（Effect 类专用）

```
┌─────────────────────────────────────────────────────────────┐
│  BREADCRUMB                                                  │
│  Apps > Effect > [Effect Name] Effect                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  HERO                                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Effect]  badge                                       │   │
│  │                                                       │   │
│  │  H1: AI [Effect Name] Effect —                        │   │
│  │      Add [Adjective] [Visual] to Any Photo             │   │
│  │                                                       │   │
│  │  Subtitle: 1-2 句，第一句描述视觉效果（酷炫/趣味），   │   │
│  │           第二句说明技术能力 + 含 1-2 个变体关键词      │   │
│  │                                                       │   │
│  │  [Upload an image]  CTA                                │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  TOOL WIDGET                                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Upload an image  [JPG, PNG, WebP, GIF]               │   │
│  │                                                       │   │
│  │  Effect intensity  [slider: ──────○──────]            │   │
│  │  or  [Effect variant selector: dropdown]              │   │
│  │  ┌──────────────┬──────────────┬──────────────┬─────┐│   │
│  │  │ Variant 1    │ Variant 2    │ Variant 3    │Var 4││   │
│  │  │ (具名+缩略图) │ (具名+缩略图) │ (具名+缩略图) │ ... ││   │
│  │  └──────────────┴──────────────┴──────────────┴─────┘│   │
│  │                                                       │   │
│  │  Settings: [Model ▼] · [Aspect ▼] · [Resolution ▼]   │   │
│  │                                                       │   │
│  │  [Add [Effect Name] Effect]  CTA                       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  EXAMPLE GALLERY                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Example]  [Latest]  [History]   tabs                │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │ Before  │ │ Before  │ │ Before  │ │ Before  │   │   │
│  │  │  After  │ │  After  │ │  After  │ │  After  │   │   │
│  │  │(original│ │         │ │         │ │         │   │   │
│  │  │→effected│ │         │ │         │ │         │   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 01 — 教育模块                                       │
│  H2: What is the [Effect Name] Effect, Exactly?              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  2-3 段正文：                                          │   │
│  │  段 1 — 特效定义 + 它给照片添加什么视觉效果（1-2 句）    │   │
│  │  段 2 — 特效的起源/流行文化背景（如 Glitch = 90s 电子    │   │
│  │        故障美学, Cinematic Flash = 2026 狗仔队风潮）     │   │
│  │  段 3 — Vofy AI 如何实现（单次操作即可, 强度可控）       │   │
│  │  [Available on all Vofy plans]  badge                  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 02 — 效果流程（3-4 步可视化）                        │
│  H2: How the [Effect Name] Effect Works.                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐        │   │
│  │  │ 01         │ │ 02         │ │ 03         │        │   │
│  │  │ Overlay    │ │ Intensity  │ │ Output     │        │   │
│  │  │ 效果叠加   │ │ 强度控制   │ │ 输出格式   │        │   │
│  │  │            │ │            │ │            │        │   │
│  │  │ [特效如何  │ │ [强度/参数 │ │ [输出格式  │        │   │
│  │  │ 叠加在原图 │ │ 的可控    │ │ 与兼容性  │        │   │
│  │  │ 上——mix/  │ │ 范围——    │ │ 说明——    │        │   │
│  │  │ overlay/  │ │ slider/   │ │ PNG/JPG/  │        │   │
│  │  │ replace]  │ │ variants] │ │ 透明度等] │        │   │
│  │  └────────────┘ └────────────┘ └────────────┘        │   │
│  │                                                       │   │
│  │  ┌────────────┐  ← 第 4 张卡片（若适用）              │   │
│  │  │ 04         │                                       │   │
│  │  │ Conditions │                                       │   │
│  │  │ 适用条件   │                                       │   │
│  │  │ [最佳照片  │                                       │   │
│  │  │ 类型 +    │                                       │   │
│  │  │ 限制说明] │                                       │   │
│  │  └────────────┘                                       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 03 — 使用场景                                       │
│  H2: When to Add the [Effect Name] Effect.                   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│   │
│  │  │ Portraits│ │ Creative │ │  Music/  │ │  Social  ││   │
│  │  │ 人像     │ │ 创意项目 │ │  Events  │ │ 社交媒体 ││   │
│  │  │          │ │          │ │ 音乐/活动│ │          ││   │
│  │  │ [2-3句   │ │ [2-3句   │ │ [2-3句   │ │ [2-3句   ││   │
│  │  │ 场景说明]│ │ 场景说明]│ │ 场景说明]│ │ 场景说明]││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 04 — HowTo 步骤                                    │
│  H2: How to Add the [Effect Name] Effect                     │
│      to Your Photo in Three Steps.                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  01 — Upload Your Photo                               │   │
│  │  [描述：支持格式、建议照片类型]                         │   │
│  │  Tip: [哪种照片构图/内容适合该特效]                     │   │
│  │                                                       │   │
│  │  02 — Adjust the [Effect Name] Intensity              │   │
│  │  [描述：拖动滑块或选择变体，实时预览效果变化]            │   │
│  │  Tip: [推荐的强度区间或变体选择建议]                    │   │
│  │                                                       │   │
│  │  03 — Generate & Download                             │   │
│  │  [描述：点击生成 + Credits 一句说明 + 下载选项]         │   │
│  │  Tip: [效果可叠加其他 Effect 或进 Studio 继续编辑]      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  SOCIAL PROOF                                                │
│  H2: What Creators Say                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────────────────┐ ┌──────────────────────┐    │   │
│  │  │ "[特效感受引文]"      │ │ "[特效感受引文]"      │    │   │
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
│  │  │ Effect   │ │ Style/   │ │ Popular  │             │   │
│  │  │ App      │ │ Filter   │ │ App      │             │   │
│  │  └──────────┘ └──────────┘ └──────────┘             │   │
│  │  [See all apps →]                                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  FAQ（使用 `<details>/<summary>` HTML，确保 Bing 可抓取）     │
│  H2: Questions, Answered.                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Q1: [效果可移除性——如 "Can I remove the effect?"]    │   │
│  │  A1: [说明非破坏性处理，可随时撤销或调整]              │   │
│  │  ─────────────────────────────────────────            │   │
│  │  Q2: 适用照片类型（什么照片效果最佳）                  │   │
│  │  Q3: 强度/参数可调范围                                 │   │
│  │  Q4: 效果叠加能力（能否叠加多个 Effect）               │   │
│  │  Q5: 与竞品同类效果的区别                              │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CLOSING CTA                                                 │
│  H2: Make Your Photos Pop with [Effect Name].                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Subtitle: [简短行动描述，强调创意趣味]                 │   │
│  │  [Add [Effect Name] to Your Photo]  CTA                │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、H1 标题公式

**公式**：`AI [Effect Name] Effect — Add [Adjective] [Visual] to Any Photo`

**设计原则**：
- 破折号前 = 搜索引擎主词（匹配 "ai [effect] effect" / "[effect] effect online"）
- 破折号后 = 视觉描述 + 动作钩子（匹配 "add [effect] to photo" 长尾）
- Title Tag 取破折号前 + ` | Vofy`（50-60 字符），H1 取完整双段式（50-70 字符）

**填充示例**：

| App | H1 |
|-----|-----|
| Glitch | `AI Glitch Effect — Add Stunning Digital Distortion to Any Photo` |
| Cinematic Flash | `AI Cinematic Flash Effect — Add Paparazzi-Style Flash to Your Portraits` |
| Double Exposure | `AI Double Exposure Effect — Blend Two Images into Surreal Art` |
| Light Leaks | `AI Light Leaks Effect — Add Dreamy Film Light Bleeds to Your Photos` |
| Bokeh | `AI Bokeh Effect — Add Creamy Background Blur to Any Photo` |
| Chromatic Aberration | `AI Chromatic Aberration Effect — Add Retro Color Fringing to Your Images` |

---

## 三、各区块内容规范

### 3.1 Breadcrumb

```
Apps > Effect > [Effect Name] Effect
```

### 3.2 Hero

| 元素 | 规范 |
|------|------|
| **Badge** | `Effect` |
| **H1** | 按 §二公式，必须含主关键词 `AI [Effect Name] Effect` |
| **Subtitle** | 段 1：视觉效果描述（酷炫/趣味，1 句）。段 2：单次操作即可 + 含 1-2 个变体关键词（如 "add … to photo"、"photo effect online"） |
| **CTA** | `Upload an image` 或 `Add [Effect] Now` |
| **关键词密度** | H1 含 "AI" + "[effect]" + "effect"；subtitle 含变体如 "photo effect" / "visual effect" |

### 3.3 Tool Widget

| 元素 | 规范 |
|------|------|
| **上传区域** | JPG, PNG, WebP, GIF |
| **Selector** | `Effect intensity slider` 或 `Effect variant selector`（下拉 + 预设条）——取决于特效是否有多变体 |
| **预设/变体命名** | 使用效果变体名（如 Glitch 的 "RGB Split"、"Scan Line"、"Pixel Sort"；Bokeh 的 "Circular"、"Hexagonal"、"Creamy"） |
| **Settings 行** | Model · Aspect Ratio · Resolution（默认推荐模型 + Auto） |
| **Generate CTA** | `Add [Effect Name] Effect` |

### 3.4 Example Gallery

- 3 个 Tab：Example / Latest / History
- 4 列 Before/After 对比网格
- 前 2 列：精选高质量示例（不同强度/变体各 1 组）
- 后 2 列：最近生成 / 历史记录
- 每列 Before 标注 `Original` / After 标注 `[Effect Name]`

### 3.5 Chapter 01 — 教育

| 元素 | 规范 |
|------|------|
| **H2** | `What is the [Effect Name] Effect, Exactly?` |
| **段 1** | 特效定义 + 它给照片添加什么视觉效果（1-2 句） |
| **段 2** | 特效的起源/流行文化背景（如 Glitch = 90s 电子故障美学, Cinematic Flash = 2026 狗仔队/红毯风潮） |
| **段 3** | Vofy AI 如何实现——单次操作即可、强度可控、可与其他效果叠加（1-2 句） |
| **Badge** | `Available on all Vofy plans`（若适用） |
| **关键词** | 主词出现 2-3 次，变体（如 "add [effect]" / "photo effect"）1-2 次 |

### 3.6 Chapter 02 — 效果流程

**H2**：`How the [Effect Name] Effect Works.`

**3 张必选卡片 + 1 张可选卡片**：

| 卡片 | 标题 | 必选 | 内容要求 |
|------|------|------|---------|
| **01 — Overlay Method** | 效果叠加方式的名称 | ✅ | 2-3 句描述特效如何叠加在原图上（混合模式 blend mode / 元素叠加 overlay / 像素替换 replace / 双图合成 composite） |
| **02 — Intensity Control** | 强度/参数可控范围的名称 | ✅ | 2-3 句描述用户可调参数（slider 强度 0-100% / variant 选择器 A-B-C / 颜色/方向/密度参数） |
| **03 — Output Format** | 输出格式与兼容性 | ✅ | 2-3 句说明输出格式（PNG 保留透明度？/ JPG 压缩？/ 是否支持透明背景）和分辨率 |
| **04 — Best Image Types** | 适用图像类型 | 可选 | 2-3 句说明效果在什么照片上最佳（人像？风景？高对比？暗调？）以及不适用的情况 |

> 3 张卡片为最小必选，第 4 张适用条件卡片在特效较挑照片时加入。

### 3.7 Chapter 03 — 使用场景

**H2**：`When to Add the [Effect Name] Effect.`

**4 张场景卡片**（Effect 类侧重）：

| 场景 | 适用条件 | 内容示例 |
|------|---------|---------|
| **Portraits & Fashion** | 人像、时尚、个人风格 | "Give your portraits an edgy [effect] look — perfect for fashion editorials and bold profile pictures." |
| **Creative Projects** | 艺术创作、海报、专辑封面 | "[Effect] turns ordinary photos into statement pieces. Album covers, posters, zine art — all from one upload." |
| **Music & Events** | 演出、音乐节、派对 | "Match the energy of live shows and events with [effect] — your crowd shots will actually feel like the moment." |
| **Social Media Content** | Instagram/TikTok/BeReal | "Stop the scroll with [effect] — when every feed looks the same, [effect] makes your content unforgettable." |

### 3.8 Chapter 04 — HowTo

**H2**：`How to Add the [Effect Name] Effect to Your Photo in Three Steps.`

| 步骤 | 标题 | 正文要求 | Tip |
|------|------|---------|-----|
| **01** | `Upload Your Photo` | 支持 JPG/PNG/WebP；拖拽上传；建议照片类型 | "Photos with [high contrast / clear subjects / dark backgrounds] tend to show the [effect] most dramatically." |
| **02** | `Adjust the [Effect Name] Intensity` | 拖动强度滑块或选择变体；实时预览效果变化 | "Start at 50% and dial up — [effect] can be subtle texture or full-on statement. Preview both before you commit." |
| **03** | `Generate & Download` | 点击生成；AI 处理一句说明；下载 PNG/JPG；Credits 一句 | "Layer [effect] with other effects in the Studio — try adding grain after [effect] for a mixed-media look." |

> JSON-LD HowTo schema 参考 [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) 范例 C。

### 3.9 Social Proof

- **H2**：`What Creators Say`
- 1-2 条引言，语气酷炫、突出创意趣味

### 3.10 Related Apps

- **H2**：`Also in the Studio`
- **选择策略**：1 个同品类 Effect App + 1 个相邻品类（Style 或 Filter）+ 1 个热门通用 App
- `See all apps →` 链接指向 `/apps`

### 3.11 FAQ

**H2**：`Questions, Answered.`

**5 个问答**（使用 `<details>/<summary>` HTML）：

| # | 主题 | 问题示例 |
|---|------|---------|
| **Q1** | 效果可移除性 | "Can I remove the [Effect Name] effect after applying it?" → 说明非破坏性处理 |
| **Q2** | 适用照片 | "What kind of photos work best with the [Effect Name] effect?" |
| **Q3** | 强度/参数 | "Can I control how strong the [Effect Name] effect is?" |
| **Q4** | 叠加能力 | "Can I combine the [Effect Name] effect with other effects?" |
| **Q5** | 竞品对标 | "How is this different from [app]'s [similar effect]?" |

### 3.12 Closing CTA

| 元素 | 规范 |
|------|------|
| **H2** | `Make Your Photos Pop with [Effect Name].`（呼应 Hero 的视觉冲击钩子） |
| **Subtitle** | 简短行动描述（1 句） |
| **CTA 按钮** | `Add [Effect Name] to Your Photo` |

---

## 四、SEO 检查清单（Effect 类）

### 4.1 关键词矩阵

| 层级 | 关键词类型 | 示例（以 Glitch 为例） | 投放位置 |
|------|-----------|---------------------------|---------|
| **主词** | `AI [effect] effect` / `[effect] photo effect` | `AI glitch effect` / `glitch photo effect` | H1 破折号前、breadcrumb、meta title |
| **变体 1** | `add [effect] to photo` | `add glitch effect to photo` | H1 破折号后、Ch.01 正文、subtitle |
| **变体 2** | `[effect] art generator` | `glitch art generator` | Ch.01 正文、Ch.04 H2 |
| **变体 3** | `[effect] online free` | `glitch effect online free` | Ch.03 场景、FAQ |
| **长尾** | `how to make [effect] photo` / `create [effect] images` | `how to make glitch art photos` | FAQ Q5、配套 Blog |

### 4.2 Title Tag vs H1 对照

| 元素 | 内容 | 字符数 |
|------|------|--------|
| **Title Tag** | `AI [Effect Name] Effect — Add [Style] Look to Photos \| Vofy` | 50-60 |
| **H1** | `AI [Effect Name] Effect — Add [Adjective] [Visual] to Any Photo` | 50-70 |
| **Meta Description** | `Add stunning [effect] to your photos with Vofy's free AI [Effect Name] Effect. [1 句效果描述]. No editing skills needed — upload and apply in seconds.` | 140-155 |

### 4.3 FAQ 长尾关键词映射

| FAQ | 覆盖长尾 |
|-----|---------|
| Q1 | `remove [effect] from photo` / `[effect] reversible` |
| Q2 | `best photos for [effect]` / `[effect] before after examples` |
| Q3 | `[effect] intensity control` / `[effect] strength slider` |
| Q4 | `combine [effect] with` / `layer effects photo` |
| Q5 | `[effect] AI generator vs [competitor]` / `best [effect] tool` |

---

## 五、极简草稿版（用于快速填充）

```
┌──────────────────────────────────────┐
│  Apps > Effect > [Effect Name] Effect│  BREADCRUMB
├──────────────────────────────────────┤
│  [Effect] badge                      │  HERO
│  H1: AI [Effect] Effect —            │
│      Add [Adjective] [X] to Any Photo│
│  [Subtitle: 视觉效果 + 单次操作]      │
│  [Upload an image]                   │
├──────────────────────────────────────┤
│  [Upload] [Intensity slider ▼]       │  TOOL WIDGET
│  [4 variant cards with thumbnails]   │  + GALLERY
│  Settings: [Model ▼]·[Aspect ▼]·[Res]│
│  [Examples: Original→Effected ×4]    │
├──────────────────────────────────────┤
│  What is the [Effect] Effect?        │  CH.01
│  [定义→起源/文化→AI 实现, 2-3段]     │
├──────────────────────────────────────┤
│  How the [Effect] Effect Works.      │  CH.02
│  [3-4 cards: Overlay│Intensity│      │
│            Output│Conditions(可选)]   │
├──────────────────────────────────────┤
│  When to Add the [Effect] Effect.    │  CH.03
│  [4 cards: Portraits│Creative│       │
│            Music│Social]              │
├──────────────────────────────────────┤
│  How to Add [Effect] in 3 Steps.     │  CH.04
│  01 Upload  02 Adjust  03 Generate   │
├──────────────────────────────────────┤
│  "What creators say" [2 quotes]      │  SOCIAL
├──────────────────────────────────────┤
│  Also in the Studio [3 app cards]    │  RELATED
├──────────────────────────────────────┤
│  FAQ [5 Q&A: 可移除→照片→强度→叠加→竞品]│ FAQ
├──────────────────────────────────────┤
│  Make Your Photos Pop with [Effect]. │  CLOSING
│  [Add [Effect] to Your Photo]        │
└──────────────────────────────────────┘
```

---

## 六、品类内一致性检查清单

每次新增 Effect 类 App 页面时，逐项核对：

| # | 检查项 | 标准 |
|---|--------|------|
| ① | H1 句式 | 必须匹配 `AI [X] Effect — Add [Adjective] [Visual] to Any Photo` |
| ② | Ch.02 卡片数 | 必须 3-4 张（最少 3 张必选：Overlay / Intensity / Output） |
| ③ | Ch.02 卡片维度 | 必须使用 Overlay / Intensity / Output 三个维度，第 4 张仅放特殊条件 |
| ④ | HowTo 步骤 2 | 必须以 `Adjust the [X] Intensity` 为核心动词 |
| ⑤ | FAQ Q1 | 必须覆盖效果可移除性/非破坏性处理 |
| ⑥ | slug 后缀 | 必须以 `-effect` 结尾 |
| ⑦ | Breadcrumb 品类 | 必须为 `Apps > Effect > [App Name]` |
| ⑧ | Related Apps #1 | 必须为同品类 Effect App |
| ⑨ | CTA 文案 | 必须强调视觉冲击/创意趣味（Make it pop / Stand out / Transform） |
| ⑩ | 情感基调 | 酷炫、趣味、创意——避免机械技术说明，突出好玩和病毒传播潜力 |

---

## 站内关联

[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [缺口分析](./vofy-effect-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) · [站面结构](../vofy-site-structure.md) · [关键词映射](../vofy-keywords.md)

---

*基于 Vofy 站内已上线页面的结构分析。所有区块和顺序已验证为全站一致模式。*
